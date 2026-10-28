#!/usr/bin/env python3
"""Bounded acquisition of digital archival images.

The generic core handles planning, safe external storage, restartable progress,
integrity checks and manifest generation. Provider-specific URL construction lives
in the provider adapter. The tool never creates Projects, Source uses, research
functions or Corpus rows.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import unicodedata
from dataclasses import asdict, dataclass, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
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
    file_list_url: str
    file_list_sha256: str
    images: tuple[ImageSpec, ...]


PROGRESS_SCHEMA = "paleo-type.archival-source-acquisition-progress.v1"
MANIFEST_SCHEMA = "paleo-type.archival-source-acquisition.v2"
PROGRESS_FILENAME = "ACQUISITION_STATE.json"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_token(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^A-Za-z0-9]+", "_", ascii_value).strip("_")
    return value or "unbenannt"


def _legacy_package_name(source: SourceMetadata) -> str:
    """Prior naming contract, retained solely for existing package lookup."""
    parts = (
        _safe_token(source.date_label),
        _safe_token(source.archive_code),
        _safe_token(source.fonds),
        _safe_token(source.signature),
        _safe_token(source.name_key or source.title),
    )
    return "_".join(parts)


def _source_year(source: SourceMetadata) -> str:
    """First explicitly printed calendar year; do not infer years from centuries."""
    year = re.search(r"(?<!\d)(?:[1-9]\d{2}|[12]\d{3})(?!\d)", source.date_label)
    return year.group(0) if year else "undatiert"


def package_name(source: SourceMetadata) -> str:
    """Start new package names with the year, preserving full date in metadata."""
    parts = (
        _source_year(source),
        _safe_token(source.archive_code),
        _safe_token(source.fonds),
        _safe_token(source.signature),
        _safe_token(source.name_key or source.title),
    )
    return "_".join(parts)


def _selected_package_name(source: SourceMetadata, output_root: Path) -> str:
    """Use a tracked legacy package in place; never silently fork or rename it."""
    current = package_name(source)
    legacy = _legacy_package_name(source)
    if current == legacy:
        return current
    new_path = output_root / current
    old_path = output_root / legacy
    if new_path.exists() and old_path.exists():
        raise AcquisitionError(
            "both year-only and legacy dated package folders exist; "
            "resolve the destination conflict before acquisition"
        )
    if old_path.exists():
        if not (old_path / PROGRESS_FILENAME).is_file():
            raise AcquisitionError(
                "legacy dated package folder has no tracked acquisition state; "
                "inspect it before any new acquisition"
            )
        return legacy
    return current


def _resolve_plan_destination(plan: AcquisitionPlan, output_root: Path) -> AcquisitionPlan:
    """Keep the original progress-plan identity for tracked legacy directories."""
    chosen = _selected_package_name(plan.source, output_root)
    if plan.package_name not in (package_name(plan.source), _legacy_package_name(plan.source)):
        raise AcquisitionError("plan uses an unexpected package name")
    return replace(plan, package_name=chosen) if plan.package_name != chosen else plan


class SaechsischesStaatsarchivProvider:
    """Resolve SStA's real file list and construct its image URLs.

    The viewer DOM is not needed for the documented single-image mode.
    Unsupported tile/manifest entries fail closed rather than being omitted.
    """

    FILE_LIST_ENDPOINT = "https://www.archiv.sachsen.de/digitalisate"
    DOWNLOAD_ENDPOINT = "https://www.archiv.sachsen.de/archiv/download.jsp"
    FULLSIZE_ENDPOINT = FILE_LIST_ENDPOINT
    GUID_PATTERN = re.compile(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
        r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\Z"
    )
    NAME_PATTERN = re.compile(r"[A-Za-z0-9_-]+\Z")

    def file_list_url(self, guid: str) -> str:
        if not self.GUID_PATTERN.fullmatch(guid):
            raise AcquisitionError("invalid SStA digitalisat GUID")
        return f"{self.FILE_LIST_ENDPOINT}/{guid}/files.json"

    def fetch_file_list(
        self,
        source: SourceMetadata,
        *,
        opener: Callable[..., object] = urlopen,
        timeout: float = 60.0,
    ) -> bytes:
        url = self.file_list_url(source.guid)
        request = Request(
            url,
            headers={"User-Agent": "paleo-type archival-source-acquisition/0.2"},
        )
        try:
            with opener(request, timeout=timeout) as response:
                return response.read()
        except Exception as error:
            raise AcquisitionError(f"SStA file list unavailable: {url}: {error}") from error

    def image_url(self, guid: str, filename: str, route: str) -> str:
        self.file_list_url(guid)
        if route == "download":
            return f"{self.DOWNLOAD_ENDPOINT}?{urlencode({'guid': guid, 'filename': filename})}"
        if route == "fullsize":
            return f"{self.FULLSIZE_ENDPOINT}/{guid}/fullsize/{filename}"
        raise ValueError(f"unsupported SStA route: {route}")

    def plan(
        self,
        source: SourceMetadata,
        file_list_bytes: bytes,
        *,
        route: str = "download",
    ) -> AcquisitionPlan:
        file_list_url = self.file_list_url(source.guid)
        try:
            entries = json.loads(file_list_bytes)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise AcquisitionError("invalid SStA files.json") from error
        if not isinstance(entries, list) or not entries:
            raise AcquisitionError("SStA files.json has no image entries")

        names: set[str] = set()
        filenames: list[str] = []
        for index, entry in enumerate(entries, start=1):
            if not isinstance(entry, dict):
                raise AcquisitionError(f"SStA entry {index} is not an object")
            name = entry.get("name")
            typ = entry.get("typ")
            if not isinstance(name, str) or not self.NAME_PATTERN.fullmatch(name):
                raise AcquisitionError(f"SStA entry {index} has an unsafe or missing name")
            if typ != "jpg" or entry.get("istEinzelbild") is not True:
                raise AcquisitionError(
                    f"SStA entry {index} is not a supported single-image JPEG"
                )
            filename = f"{name}.{typ}"
            if filename in names:
                raise AcquisitionError(f"duplicate SStA image: {filename}")
            names.add(filename)
            filenames.append(filename)

        filenames.sort()
        if source.image_count and len(filenames) != source.image_count:
            raise AcquisitionError(
                f"SStA file count {len(filenames)} differs from "
                f"supplied count {source.image_count}"
            )
        images = tuple(
            ImageSpec(
                sequence=index,
                filename=filename,
                url=self.image_url(source.guid, filename, route),
            )
            for index, filename in enumerate(filenames, start=1)
        )
        return AcquisitionPlan(
            source=source,
            package_name=package_name(source),
            route=route,
            file_list_url=file_list_url,
            file_list_sha256=hashlib.sha256(file_list_bytes).hexdigest(),
            images=images,
        )


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    """Fully decode the JPEG payload; an SOF header alone is not evidence of integrity."""
    from io import BytesIO

    if len(data) < 4 or data[:2] != b"\xff\xd8" or not data.endswith(b"\xff\xd9"):
        raise AcquisitionError("missing JPEG markers or truncated JPEG payload")
    try:
        from PIL import Image
    except ImportError as error:
        raise AcquisitionError(
            "Pillow is required for complete JPEG verification; "
            "install tools/requirements-archival-source-acquisition.txt"
        ) from error
    try:
        with Image.open(BytesIO(data)) as picture:
            if picture.format != "JPEG":
                raise AcquisitionError("downloaded payload is not a JPEG")
            picture.load()  # decode all image pixels, not just the SOF metadata
            if picture.width <= 0 or picture.height <= 0:
                raise AcquisitionError("JPEG dimensions are invalid")
            return picture.width, picture.height
    except (OSError, ValueError, SyntaxError) as error:
        raise AcquisitionError(f"JPEG cannot be fully decoded: {error}") from error


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _inspect_jpeg(path: Path) -> dict:
    dimensions = jpeg_dimensions(path.read_bytes())
    return {
        "sha256": _sha256(path),
        "pixel_width": dimensions[0],
        "pixel_height": dimensions[1],
    }


def _write_text_atomic(path: Path, content: str) -> None:
    temporary = path.with_name(path.name + ".part")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _is_within(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def _assert_external_output_root(output_root: Path) -> None:
    repo = Path(__file__).resolve().parents[1]
    if _is_within(output_root, repo):
        raise AcquisitionError(
            "refusing archival image acquisition into the repository/worktree; "
            "configure an external source destination"
        )


def _plan_identity(plan: AcquisitionPlan) -> dict:
    return {
        "package_name": plan.package_name,
        "guid": plan.source.guid,
        "route": plan.route,
        "file_list_url": plan.file_list_url,
        "file_list_sha256": plan.file_list_sha256,
        "expected_filenames": [spec.filename for spec in plan.images],
    }


def _new_progress(plan: AcquisitionPlan) -> dict:
    return {
        "schema": PROGRESS_SCHEMA,
        "status": "planned",
        "updated_at_utc": _utc_now(),
        "plan": _plan_identity(plan),
        "images": [],
        "last_failure": None,
    }


def _progress_path(target: Path) -> Path:
    return target / PROGRESS_FILENAME


def _write_progress(target: Path, progress: dict) -> None:
    progress["updated_at_utc"] = _utc_now()
    _write_text_atomic(
        _progress_path(target),
        json.dumps(progress, ensure_ascii=False, indent=2) + "\n",
    )


def _load_progress(target: Path, plan: AcquisitionPlan) -> dict:
    path = _progress_path(target)
    if not path.exists():
        return _new_progress(plan)
    try:
        progress = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise AcquisitionError(f"invalid acquisition progress state: {path}: {error}") from error
    if progress.get("schema") != PROGRESS_SCHEMA:
        raise AcquisitionError("unsupported acquisition progress schema")
    if progress.get("plan") != _plan_identity(plan):
        raise AcquisitionError(
            "existing acquisition progress belongs to a different provider list/route/source plan"
        )
    if not isinstance(progress.get("images"), list):
        raise AcquisitionError("acquisition progress images must be a list")
    return progress


def _recorded_images(progress: dict) -> dict[str, dict]:
    indexed: dict[str, dict] = {}
    for item in progress.get("images", []):
        filename = item.get("filename")
        if not isinstance(filename, str) or filename in indexed:
            raise AcquisitionError("acquisition progress contains invalid or duplicate image records")
        indexed[filename] = item
    return indexed


def _verify_recorded_image(spec: ImageSpec, destination: Path, recorded: dict) -> dict:
    if recorded.get("sequence") != spec.sequence or recorded.get("url") != spec.url:
        raise AcquisitionError(f"progress metadata mismatch for {spec.filename}")
    if not destination.is_file():
        raise AcquisitionError(
            f"progress state records {spec.filename} but the external file is missing"
        )
    inspected = _inspect_jpeg(destination)
    if inspected["sha256"] != recorded.get("sha256"):
        raise AcquisitionError(
            f"existing file checksum differs from persisted acquisition state: {destination}"
        )
    if inspected["pixel_width"] != recorded.get("pixel_width") or inspected[
        "pixel_height"
    ] != recorded.get("pixel_height"):
        raise AcquisitionError(
            f"existing file dimensions differ from persisted acquisition state: {destination}"
        )
    return {
        "filename": spec.filename,
        "sequence": spec.sequence,
        "status": "verified-existing",
        **inspected,
        "url": spec.url,
    }


def _download(
    spec: ImageSpec,
    destination: Path,
    *,
    opener: Callable[..., object] = urlopen,
    retries: int = 3,
    timeout: float = 60.0,
) -> dict:
    """Download one image.

    If an untracked file already exists, a fresh remote copy is downloaded to a
    temporary path and hashes are compared before the file is adopted into the
    restartable progress state. Persisted tracked files are verified locally by
    ``acquire`` and never redownloaded merely to prove idempotence.
    """
    partial = destination.with_name(destination.name + ".part")
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            request = Request(
                spec.url,
                headers={"User-Agent": "paleo-type archival-source-acquisition/0.2"},
            )
            response = opener(request, timeout=timeout)
            with response, partial.open("wb") as output:
                for chunk in iter(lambda: response.read(1024 * 1024), b""):
                    output.write(chunk)
            inspected = _inspect_jpeg(partial)
            if destination.exists():
                if _sha256(destination) == inspected["sha256"]:
                    existing_dimensions = jpeg_dimensions(destination.read_bytes())
                    if existing_dimensions != (
                        inspected["pixel_width"],
                        inspected["pixel_height"],
                    ):
                        raise AcquisitionError(
                            f"existing file dimensions differ: {destination}"
                        )
                    partial.unlink()
                    return {
                        "filename": spec.filename,
                        "sequence": spec.sequence,
                        "status": "already-present-adopted",
                        **inspected,
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
                **inspected,
                "url": spec.url,
            }
        except Exception as error:
            last_error = error
            if partial.exists():
                partial.unlink()
            if attempt < retries:
                time.sleep(min(2 ** (attempt - 1), 4))
    raise AcquisitionError(f"failed to acquire {spec.filename}: {last_error}")


def status_for_source(source: SourceMetadata, output_root: Path) -> dict:
    """Inspect existing acquisition state without fetching or mutating anything."""
    _assert_external_output_root(output_root)
    selected_name = _selected_package_name(source, output_root)
    target = output_root / selected_name
    state_path = _progress_path(target)
    if not state_path.is_file():
        return {
            "status": "not-started",
            "package_name": selected_name,
            "destination": str(target),
            "state_file": str(state_path),
            "read_only": True,
        }
    try:
        progress = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise AcquisitionError(f"invalid acquisition progress state: {state_path}: {error}") from error
    return {
        "status": progress.get("status", "unknown"),
        "package_name": selected_name,
        "destination": str(target),
        "state_file": str(state_path),
        "completed_images": len(progress.get("images", []))
        if isinstance(progress.get("images"), list)
        else None,
        "updated_at_utc": progress.get("updated_at_utc"),
        "last_failure": progress.get("last_failure"),
        "read_only": True,
    }


def acquire(
    plan: AcquisitionPlan,
    output_root: Path,
    *,
    opener: Callable[..., object] = urlopen,
    retries: int = 3,
    rate_limit_seconds: float = 0.1,
) -> dict:
    """Acquire one plan into the configured external root with durable resume state."""
    _assert_external_output_root(output_root)
    plan = _resolve_plan_destination(plan, output_root)
    target = output_root / plan.package_name
    target.mkdir(parents=True, exist_ok=True)
    progress = _load_progress(target, plan)
    recorded = _recorded_images(progress)
    results: list[dict] = []

    for spec in plan.images:
        try:
            if spec.filename in recorded:
                result = _verify_recorded_image(
                    spec, target / spec.filename, recorded[spec.filename]
                )
            else:
                if results or recorded:
                    time.sleep(rate_limit_seconds)
                result = _download(
                    spec,
                    target / spec.filename,
                    opener=opener,
                    retries=retries,
                )
                persisted = dict(result)
                persisted["status"] = "verified"
                progress["images"].append(persisted)
                recorded[spec.filename] = persisted
                progress["status"] = "partial-restartable"
                progress["last_failure"] = None
                _write_progress(target, progress)
            results.append(result)
        except KeyboardInterrupt:
            progress["status"] = "cancelled-restartable"
            progress["last_failure"] = {
                "filename": spec.filename,
                "sequence": spec.sequence,
                "error": "cancelled by operator",
                "at_utc": _utc_now(),
            }
            _write_progress(target, progress)
            raise
        except Exception as error:
            progress["status"] = "partial-restartable"
            progress["last_failure"] = {
                "filename": spec.filename,
                "sequence": spec.sequence,
                "error": str(error),
                "at_utc": _utc_now(),
            }
            _write_progress(target, progress)
            raise

    expected_names = [spec.filename for spec in plan.images]
    actual_names = [item["filename"] for item in results]
    if actual_names != expected_names:
        progress["status"] = "partial-restartable"
        progress["last_failure"] = {
            "error": "image sequence is incomplete or unstable",
            "at_utc": _utc_now(),
        }
        _write_progress(target, progress)
        raise AcquisitionError("image sequence is incomplete or unstable")

    # A verified image sequence is not yet a finished source package.
    # Persist a restartable state before generating all final sidecars, including
    # when a previously complete package is explicitly revalidated.
    progress["status"] = "partial-restartable"
    progress["last_failure"] = None
    progress.pop("completed_at_utc", None)
    _write_progress(target, progress)
    completed_at_utc = _utc_now()

    manifest = {
        "schema": MANIFEST_SCHEMA,
        "status": "complete",
        "acquired_at_utc": completed_at_utc,
        "file_list_url": plan.file_list_url,
        "file_list_sha256": plan.file_list_sha256,
        "package_name": plan.package_name,
        "route": plan.route,
        "source": asdict(plan.source),
        "images": results,
        "progress_state": PROGRESS_FILENAME,
        "constraints": {
            "external_storage_only": True,
            "restartable_progress": True,
            "status_read_is_non_mutating": True,
            "creates_project": False,
            "creates_source_use": False,
            "creates_research_function": False,
            "creates_corpus_rows": False,
        },
    }
    try:
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
            f"Dateiliste: {plan.file_list_url}",
            f"Dateiliste SHA-256: {plan.file_list_sha256}",
            f"Bildroute: {plan.route}",
            f"Umfang: {len(results)} Fullsize-JPEGs",
            "Dateien: " + f"{expected_names[0]}–{expected_names[-1]}",
            f"Rights-/Zugriffsstatus: {plan.source.rights_status}",
            f"Restart-/Fortschrittsstatus: {PROGRESS_FILENAME}",
            "",
            "Die Ablage wurde durch paleo-type archival-source-acquisition erzeugt.",
            "Project-, Source-use- und Forschungsfunktionsentscheidungen sind nicht enthalten.",
        ]
        _write_text_atomic(target / "QUELLENINFO.txt", "\n".join(info_lines) + "\n")
        checksums = "\n".join(
            f"{item['sha256']}  {item['filename']}" for item in results
        )
        _write_text_atomic(target / "SHA256SUMS.txt", checksums + "\n")
    except BaseException as error:
        # Never persist COMPLETE while any manifest/checksum write is missing.
        progress["last_failure"] = {
            "phase": "manifest-finalization",
            "error": str(error),
            "at_utc": _utc_now(),
        }
        _write_progress(target, progress)
        raise

    progress["status"] = "complete"
    progress["last_failure"] = None
    progress["completed_at_utc"] = completed_at_utc
    _write_progress(target, progress)
    return manifest

def load_source(path: Path) -> SourceMetadata:
    metadata_json = sys.stdin.read() if str(path) == "-" else path.read_text(encoding="utf-8")
    data = json.loads(metadata_json)
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
    parser.add_argument("--file-list", type=Path, help="offline files.json fixture")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--status",
        action="store_true",
        help="read existing package progress only; never fetch images or mutate state",
    )
    parser.add_argument("--rate-limit", type=float, default=0.1)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    source = load_source(args.metadata)
    if args.status:
        print(
            json.dumps(
                status_for_source(source, args.output_root),
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    provider = SaechsischesStaatsarchivProvider()
    file_list_bytes = (
        args.file_list.read_bytes()
        if args.file_list is not None
        else provider.fetch_file_list(source)
    )
    plan = provider.plan(source, file_list_bytes, route=args.route)
    plan = _resolve_plan_destination(plan, args.output_root)
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
