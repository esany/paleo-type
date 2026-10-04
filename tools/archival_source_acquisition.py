#!/usr/bin/env python3
"""Bounded acquisition of digital archival images.

The generic core handles planning, safe external storage, integrity checks and
manifest generation. Provider-specific URL construction lives in the provider
adapter. The tool never creates Projects, Source uses, research functions or
Corpus rows.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import re
import sys
import time
import unicodedata
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Iterable
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class AcquisitionError(RuntimeError):
    """A bounded acquisition or integrity failure."""


@dataclass(frozen=True)
class SourceMetadata:
    archive: str
    fonds: str
    signature: str
    title: str
    date_label: str
    guid: str
    page_url: str
    archive_code: str = "SStA"
    name_key: str = ""
    classification_path: str = ""
    rights_status: str = "unknown"
    image_count: int = 0


@dataclass(frozen=True)
class ImageSpec:
    sequence: int
    filename: str
    url: str


@dataclass(frozen=True)
class AcquisitionPlan:
    source: SourceMetadata
    package_name: str
    route: str
    images: tuple[ImageSpec, ...]


def _safe_token(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^A-Za-z0-9]+", "_", ascii_value).strip("_")
    return value or "unbenannt"


def package_name(source: SourceMetadata) -> str:
    """Create a deterministic external package name from supplied metadata."""
    date_token = _safe_token(source.date_label)
    archive_token = _safe_token(source.archive_code)
    fonds_token = _safe_token(source.fonds)
    signature_token = _safe_token(source.signature)
    name_token = _safe_token(source.name_key or source.title)
    return "_".join(
        (date_token, archive_token, fonds_token, signature_token, name_token)
    )


class SaechsischesStaatsarchivProvider:
    """Provider boundary for the SStA page/viewer and image routes.

    The current MVP consumes metadata supplied by intake and constructs the
    explicitly tested routes. It does not claim to discover or parse live HTML.
    Viewer-specific selectors remain owned here rather than by the generic core.
    """

    VIEWER_STRUCTURE = {
        "thumbnail_strip_wrapper": "digitalisat-viewer-thumbnailstrip-wrapper",
        "image_container": "viewer_digitalisate",
    }

    DOWNLOAD_ENDPOINT = "https://www.archiv.sachsen.de/archiv/download.jsp"
    FULLSIZE_ENDPOINT = "https://www.archiv.sachsen.de/digitalisate"

    @classmethod
    def viewer_structure(cls) -> dict[str, str]:
        """Return the SStA viewer markers without exposing them to the core."""
        return dict(cls.VIEWER_STRUCTURE)

    def image_url(self, guid: str, filename: str, route: str) -> str:
        if route == "download":
            return f"{self.DOWNLOAD_ENDPOINT}?{urlencode({'guid': guid, 'filename': filename})}"
        if route == "fullsize":
            return f"{self.FULLSIZE_ENDPOINT}/{guid}/fullsize/{filename}"
        raise ValueError(f"unsupported SStA route: {route}")

    def plan(
        self,
        source: SourceMetadata,
        *,
        route: str = "download",
        count: int | None = None,
    ) -> AcquisitionPlan:
        image_count = count if count is not None else source.image_count
        if image_count < 1:
            raise ValueError("image count must be positive")
        images = tuple(
            ImageSpec(
                sequence=index,
                filename=f"{index:04d}.jpg",
                url=self.image_url(source.guid, f"{index:04d}.jpg", route),
            )
            for index in range(1, image_count + 1)
        )
        return AcquisitionPlan(
            source=source,
            package_name=package_name(source),
            route=route,
            images=images,
        )


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    """Read dimensions from a JPEG SOF marker without third-party libraries."""
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        raise AcquisitionError("file is not a JPEG")
    cursor = 2
    sof_markers = set(range(0xC0, 0xC4)) | set(range(0xC5, 0xC8))
    sof_markers |= set(range(0xC9, 0xCC)) | set(range(0xCD, 0xD0))
    while cursor + 4 <= len(data):
        if data[cursor] != 0xFF:
            cursor += 1
            continue
        while cursor < len(data) and data[cursor] == 0xFF:
            cursor += 1
        if cursor >= len(data):
            break
        marker = data[cursor]
        cursor += 1
        if marker in (0xD8, 0xD9):
            continue
        if marker == 0xDA:
            break
        if cursor + 2 > len(data):
            break
        segment_length = int.from_bytes(data[cursor:cursor + 2], "big")
        if segment_length < 2 or cursor + segment_length > len(data):
            break
        if marker in sof_markers and segment_length >= 7:
            height = int.from_bytes(data[cursor + 3:cursor + 5], "big")
            width = int.from_bytes(data[cursor + 5:cursor + 7], "big")
            return width, height
        cursor += segment_length
    raise AcquisitionError("JPEG dimensions could not be determined")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _download(
    spec: ImageSpec,
    destination: Path,
    *,
    opener: Callable[..., object] = urlopen,
    retries: int = 3,
    timeout: float = 60.0,
) -> dict:
    partial = destination.with_name(destination.name + ".part")
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            request = Request(
                spec.url,
                headers={"User-Agent": "paleo-type archival-source-acquisition/0.1"},
            )
            response = opener(request, timeout=timeout)
            with response, partial.open("wb") as output:
                for chunk in iter(lambda: response.read(1024 * 1024), b""):
                    output.write(chunk)
            dimensions = jpeg_dimensions(partial.read_bytes())
            digest = _sha256(partial)
            if destination.exists():
                if _sha256(destination) == digest:
                    partial.unlink()
                    return {
                        "filename": spec.filename,
                        "sequence": spec.sequence,
                        "status": "already-present",
                        "sha256": digest,
                        "pixel_width": dimensions[0],
                        "pixel_height": dimensions[1],
                        "url": spec.url,
                    }
                raise AcquisitionError(
                    f"refusing to overwrite existing different file: {destination}"
                )
            partial.replace(destination)
            return {
                "filename": spec.filename,
                "sequence": spec.sequence,
                "status": "downloaded",
                "sha256": digest,
                "pixel_width": dimensions[0],
                "pixel_height": dimensions[1],
                "url": spec.url,
            }
        except Exception as error:
            last_error = error
            if partial.exists():
                partial.unlink()
            if attempt < retries:
                time.sleep(min(2**(attempt - 1), 4))
    raise AcquisitionError(f"failed to acquire {spec.filename}: {last_error}")


def _write_text_atomic(path: Path, content: str) -> None:
    temporary = path.with_name(path.name + ".part")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def acquire(
    plan: AcquisitionPlan,
    output_root: Path,
    *,
    opener: Callable[..., object] = urlopen,
    retries: int = 3,
    rate_limit_seconds: float = 0.1,
) -> dict:
    """Acquire one plan into the configured external root only."""
    target = output_root / plan.package_name
    target.mkdir(parents=True, exist_ok=True)
    results = []
    for index, spec in enumerate(plan.images):
        if index:
            time.sleep(rate_limit_seconds)
        results.append(
            _download(
                spec,
                target / spec.filename,
                opener=opener,
                retries=retries,
            )
        )

    expected_names = [spec.filename for spec in plan.images]
    actual_names = [item["filename"] for item in results]
    if actual_names != expected_names:
        raise AcquisitionError("image sequence is incomplete or unstable")

    manifest = {
        "schema": "paleo-type.archival-source-acquisition.v1",
        "status": "complete",
        "package_name": plan.package_name,
        "route": plan.route,
        "source": asdict(plan.source),
        "images": results,
        "constraints": {
            "external_storage_only": True,
            "creates_project": False,
            "creates_source_use": False,
            "creates_research_function": False,
            "creates_corpus_rows": False,
        },
    }
    _write_text_atomic(
        target / "QUELLENINFO.json",
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    )
    info_lines = [
        f"Kurztitel: {plan.package_name}",
        f"Archiv: {plan.source.archive}",
        f"Bestand: {plan.source.fonds}",
        f"Archivaliensignatur: {plan.source.signature}",
        f"Titel: {plan.source.title}",
        f"Datierung: {plan.source.date_label}",
        f"Digitalisat-GUID: {plan.source.guid}",
        f"Digitalisat: {plan.source.page_url}",
        f"Bildroute: {plan.route}",
        f"Umfang: {len(results)} Fullsize-JPEGs",
        "Dateien: " + f"{expected_names[0]}–{expected_names[-1]}",
        f"Rights-/Zugriffsstatus: {plan.source.rights_status}",
        "",
        "Die Ablage wurde durch paleo-type archival-source-acquisition erzeugt.",
        "Project-, Source-use- und Forschungsfunktionsentscheidungen sind nicht enthalten.",
    ]
    _write_text_atomic(target / "QUELLENINFO.txt", "\n".join(info_lines) + "\n")
    checksums = "\n".join(
        f"{item['sha256']}  {item['filename']}" for item in results
    )
    _write_text_atomic(target / "SHA256SUMS.txt", checksums + "\n")
    return manifest


def load_source(path: Path) -> SourceMetadata:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = ("archive", "fonds", "signature", "title", "date_label", "guid", "page_url")
    missing = [field for field in required if not data.get(field)]
    if missing:
        raise ValueError("metadata missing required fields: " + ", ".join(missing))
    return SourceMetadata(**data)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Acquire SStA digitalisat images into an external source root."
    )
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--route", choices=("download", "fullsize"), default="download")
    parser.add_argument("--count", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--rate-limit", type=float, default=0.1)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    source = load_source(args.metadata)
    plan = SaechsischesStaatsarchivProvider().plan(
        source, route=args.route, count=args.count
    )
    if args.dry_run:
        print(json.dumps(asdict(plan), ensure_ascii=False, indent=2))
        return 0
    manifest = acquire(
        plan,
        args.output_root,
        rate_limit_seconds=args.rate_limit,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
