#!/usr/bin/env python3
"""Read-only verification/Corpus reconciliation of an archive acquisition package.

This is an optional provider-neutral bridge, not a GitHub writer or proof of
external storage control. The caller must separately verify that the selected
root is an authorized, durable external source store before claiming preservation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import source_contract


SHA = re.compile(r"^[0-9a-f]{64}$")


class PackageIntakeError(ValueError):
    pass


def _object(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise PackageIntakeError(f"missing/invalid package JSON: {path.name}: {error}") from error
    if not isinstance(value, dict):
        raise PackageIntakeError(f"expected JSON object in {path.name}")
    return value


def _digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            digest.update(block)
    return digest.hexdigest()


def _checksums(text: str) -> dict[str, str]:
    items: dict[str, str] = {}
    for line in text.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\\/]+)", line)
        if not match:
            raise PackageIntakeError("malformed SHA256SUMS.txt entry")
        digest, name = match.groups()
        if name in items or name in {".", ".."} or Path(name).name != name:
            raise PackageIntakeError("duplicate/unsafe checksums filename")
        items[name] = digest
    if not items:
        raise PackageIntakeError("empty checksum inventory")
    return items


def inspect_package(package: Path, root: Path) -> dict:
    """Read-only, fail-closed; no artifact is changed, no remote calls."""
    package = package.resolve()
    root = root.resolve()
    if package == root or root in package.parents:
        raise PackageIntakeError("package must not be inside repository")
    if not package.is_dir():
        raise PackageIntakeError("missing acquisition package folder")

    manifest = _object(package / "QUELLENINFO.json")
    progress = _object(package / "ACQUISITION_STATE.json")
    if manifest.get("status") != "complete" or progress.get("status") != "complete":
        raise PackageIntakeError("acquisition progress/manifest are not both complete")
    if manifest.get("package_name") != package.name:
        raise PackageIntakeError("package name does not match its manifest")
    if not (package / "QUELLENINFO.txt").is_file() or not (package / "QUELLENINFO.txt").read_text(encoding="utf-8").strip():
        raise PackageIntakeError("missing/empty human-readable source sidecar")
    if manifest.get("progress_state") != "ACQUISITION_STATE.json":
        raise PackageIntakeError("manifest does not identify the expected progress state")
    source = manifest.get("source")
    if not isinstance(source, dict) or not all(source.get(k) for k in (
        "archive", "fonds", "signature", "title", "date_label", "guid", "page_url"
    )):
        raise PackageIntakeError("incomplete source catalogue identity")
    if not isinstance(manifest.get("images"), list):
        raise PackageIntakeError("manifest lacks image inventory")
    identity = progress.get("plan")
    if not isinstance(identity, dict) or any(identity.get(k) != manifest.get(k) for k in (
        "package_name", "route", "file_list_url", "file_list_sha256"
    )) or identity.get("guid") != source["guid"]:
        raise PackageIntakeError("acquisition plan and completed manifest disagree")
    if not isinstance(progress.get("images"), list):
        raise PackageIntakeError("missing verified progress image inventory")

    try:
        sums = _checksums((package / "SHA256SUMS.txt").read_text(encoding="utf-8"))
    except OSError as error:
        raise PackageIntakeError("missing checksum sidecar") from error
    originals = manifest["images"]
    names = [image.get("filename") for image in originals if isinstance(image, dict)]
    if len(names) != len(originals) or any(not isinstance(n, str) for n in names):
        raise PackageIntakeError("malformed manifest image")
    if len(set(names)) != len(names) or not names or sorted(names) != names:
        raise PackageIntakeError("image inventory must be unique and in order")
    if set(names) != set(sums) or identity.get("expected_filenames") != names:
        raise PackageIntakeError("image list, checksums and persisted plan differ")
    progress_map = {img.get("filename"): img for img in progress["images"] if isinstance(img, dict)}
    if len(progress["images"]) != len(names) or len(progress_map) != len(names) or set(progress_map) != set(names):
        raise PackageIntakeError("verified progress inventory does not match the originals")
    for image in originals:
        name = image["filename"]
        if name in {".", ".."} or Path(name).name != name or "/" in name or "\\" in name:
            raise PackageIntakeError("unsafe source filename")
        digest = image.get("sha256")
        if not isinstance(digest, str) or not SHA.fullmatch(digest):
            raise PackageIntakeError(f"invalid original checksum: {name}")
        if sums[name] != digest or progress_map[name].get("sha256") != digest:
            raise PackageIntakeError(f"checksum or progress disagreement: {name}")
        if progress_map[name].get("status") not in {"verified", "verified-existing"}:
            raise PackageIntakeError(f"progress has unverified original: {name}")
        file = package / name
        if not file.is_file() or file.is_symlink() or _digest(file) != digest:
            raise PackageIntakeError(f"missing or mutated original: {name}")

    errors, _, cache = source_contract.validate(root, source_contract.load_contract(root))
    if errors:
        raise PackageIntakeError(f"canonical Source Contract invalid: {errors[:2]}")
    by_guid = [row for row in cache["sources"].values() if row.get("record_id") == source["guid"]]
    by_url = [row for row in cache["sources"].values() if row.get("digital_url") == source["page_url"]]
    candidates = {row["source_id"]: row for row in (by_guid + by_url)}
    if len(candidates) > 1:
        raise PackageIntakeError("catalogue GUID/URL map to conflicting Source nodes")
    existing = next(iter(candidates.values()), None)
    if existing and (source["archive"] not in existing.get("archive", "")
                     or source["fonds"] not in existing.get("fonds", "")
                     or source["signature"] not in existing.get("signature", "")):
        raise PackageIntakeError("manifest catalogue and existing canonical Source disagree")

    hashes = {}
    for row in cache["files"].values():
        if row.get("sha256"):
            hashes.setdefault(row["sha256"], []).append(row)
    already, missing = [], []
    for image in originals:
        name, digest = image["filename"], image["sha256"]
        matches = hashes.get(digest, [])
        if len(matches) > 1:
            raise PackageIntakeError("duplicate canonical SHA identity")
        if matches:
            record = matches[0]
            if existing is None or record.get("source_id") != existing["source_id"] or record.get("filename") != name:
                raise PackageIntakeError(f"SHA is already bound to a different Source/File: {name}")
            already.append({"filename": name, "file_id": record["file_id"], "sha256": digest})
        else:
            missing.append({"filename": name, "sha256": digest})

    return {
        "status": "VERIFIED_BYTES_RECONCILIATION_PLAN",
        "read_only": True,
        "external_durability": "NOT_ESTABLISHED_BY_THIS_TOOL",
        "source_id": existing["source_id"] if existing else None,
        "source_identity": source,
        "source_resolution": "EXISTING_SOURCE" if existing else "REQUIRES_EVIDENCED_SOURCE_RESOLUTION",
        "originals_verified": len(names),
        "already_registered": already,
        "unregistered": missing,
        "repo_write_completed": False,
        "project_created": False,
        "zotero_written": False,
        "next": "Verify controlled external persistence and rights, then use authorized online GitHub owner writes and Source Contract validation; do not infer Project routing.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only package-byte and Corpus identity preflight")
    parser.add_argument("package", type=Path)
    parser.add_argument("--root", help="Repository root for read-only contract checks")
    args = parser.parse_args()
    try:
        result = inspect_package(args.package, source_contract.repo_root(args.root))
    except PackageIntakeError as error:
        print(json.dumps({"status": "FAIL_CLOSED", "read_only": True, "error": str(error)}), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
