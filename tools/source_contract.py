#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def repo_root(explicit: str | None = None) -> Path:
    if explicit:
        return Path(explicit).resolve()
    return Path(__file__).resolve().parents[1]


def load_contract(root: Path) -> dict:
    return json.loads((root / "corpus" / "source-contract.json").read_text(encoding="utf-8"))


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        headers = reader.fieldnames or []
        rows = [{k: (v or "").strip() for k, v in row.items()} for row in reader]
    return headers, rows


def check_headers(path: Path, headers: list[str], required: list[str], errors: list[str]) -> None:
    missing = [name for name in required if name not in headers]
    if missing:
        errors.append(f"{path}: missing required columns: {', '.join(missing)}")


def validate(root: Path, contract: dict) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    cache: dict[str, object] = {}

    source_cfg = contract["tables"]["sources"]
    source_path = root / source_cfg["path"]
    sh, sources = read_tsv(source_path)
    check_headers(source_path, sh, source_cfg["required_columns"], errors)
    source_by_id: dict[str, dict[str, str]] = {}
    identity_seen: dict[tuple[str, ...], str] = {}
    for i, row in enumerate(sources, start=2):
        for field in source_cfg["required_nonempty"]:
            if not row.get(field):
                errors.append(f"{source_path}:{i}: {field} must not be empty")
        sid = row.get(source_cfg["key"], "")
        if sid:
            if sid in source_by_id:
                errors.append(f"{source_path}:{i}: duplicate source_id {sid}")
            source_by_id[sid] = row
        identity = tuple(row.get(f, "") for f in source_cfg["identity_fields"])
        if all(identity):
            if identity in identity_seen and identity_seen[identity] != sid:
                errors.append(f"{source_path}:{i}: archival identity duplicates source {identity_seen[identity]}")
            identity_seen[identity] = sid

    unit_cfg = contract["tables"]["source_units"]
    unit_path = root / unit_cfg["path"]
    uh, units = read_tsv(unit_path)
    check_headers(unit_path, uh, unit_cfg["required_columns"], errors)
    unit_by_id: dict[str, dict[str, str]] = {}
    provider_seen: dict[str, str] = {}
    allowed_unit_status = set(contract["controlled_values"]["source_units.status"])
    for i, row in enumerate(units, start=2):
        for field in unit_cfg["required_nonempty"]:
            if not row.get(field):
                errors.append(f"{unit_path}:{i}: {field} must not be empty")
        uid = row.get(unit_cfg["key"], "")
        if uid:
            if uid in unit_by_id:
                errors.append(f"{unit_path}:{i}: duplicate source_unit_id {uid}")
            unit_by_id[uid] = row
        sid = row.get("source_id", "")
        if sid not in source_by_id:
            errors.append(f"{unit_path}:{i}: parent source_id {sid} does not exist in corpus/sources.tsv")
        provider_id = row.get("provider_record_id", "")
        if provider_id:
            if provider_id in provider_seen and provider_seen[provider_id] != uid:
                errors.append(f"{unit_path}:{i}: provider_record_id {provider_id} is already assigned to {provider_seen[provider_id]}")
            provider_seen[provider_id] = uid
        status = row.get("status", "")
        if status not in allowed_unit_status:
            errors.append(f"{unit_path}:{i}: unknown source-unit status {status!r}")
        if bool(row.get("date_from")) != bool(row.get("date_to")):
            errors.append(f"{unit_path}:{i}: date_from/date_to must be supplied together")
        if bool(row.get("date_serial_from")) != bool(row.get("date_serial_to")):
            errors.append(f"{unit_path}:{i}: date_serial_from/date_serial_to must be supplied together")
        if (row.get("date_serial_from") or row.get("date_serial_to")) and not row.get("date_calendar_label"):
            errors.append(f"{unit_path}:{i}: serial date values require date_calendar_label")

    file_cfg = contract["tables"]["files"]
    file_path = root / file_cfg["path"]
    fh, files = read_tsv(file_path)
    check_headers(file_path, fh, file_cfg["required_columns"], errors)
    file_by_id: dict[str, dict[str, str]] = {}
    allowed_storage = set(contract["controlled_values"]["files.storage_status"])
    for i, row in enumerate(files, start=2):
        for field in file_cfg["required_nonempty"]:
            if not row.get(field):
                errors.append(f"{file_path}:{i}: {field} must not be empty")
        fid = row.get(file_cfg["key"], "")
        if fid:
            if fid in file_by_id:
                errors.append(f"{file_path}:{i}: duplicate file_id {fid}")
            file_by_id[fid] = row
        sid = row.get("source_id", "")
        uid = row.get("source_unit_id", "")
        if sid and sid not in source_by_id:
            errors.append(f"{file_path}:{i}: source_id {sid} does not exist in corpus/sources.tsv")
        if uid:
            if uid not in unit_by_id:
                errors.append(f"{file_path}:{i}: source_unit_id {uid} does not exist in corpus/source-units.tsv")
            elif unit_by_id[uid].get("source_id") != sid:
                errors.append(f"{file_path}:{i}: source_unit_id {uid} belongs to another archival act")
        digest = row.get("sha256", "")
        if digest and not SHA256_RE.match(digest):
            errors.append(f"{file_path}:{i}: sha256 is not 64 lowercase hex characters")
        storage = row.get("storage_status", "")
        if storage and storage not in allowed_storage:
            errors.append(f"{file_path}:{i}: unknown storage_status {storage}")
        if storage == "repo-preserved":
            rel = row.get("repository_path", "")
            if not rel:
                errors.append(f"{file_path}:{i}: repo-preserved file needs repository_path")
            else:
                binary = root / rel
                if not binary.exists():
                    errors.append(f"{file_path}:{i}: repo-preserved file missing at {rel}")
                elif digest and hashlib.sha256(binary.read_bytes()).hexdigest() != digest:
                    errors.append(f"{file_path}:{i}: sha256 mismatch for {rel}")

    project_cfg = contract["tables"]["project_sources"]
    project_rows: dict[tuple[str, str, str], dict[str, str]] = {}
    for path in sorted(root.glob(project_cfg["glob"])):
        headers, rows = read_tsv(path)
        check_headers(path, headers, project_cfg["required_columns"], errors)
        project_id = path.parents[1].name
        for i, row in enumerate(rows, start=2):
            for field in project_cfg["required_nonempty"]:
                if not row.get(field):
                    errors.append(f"{path}:{i}: {field} must not be empty")
            sid = row.get("source_id", "")
            uid = row.get("source_unit_id", "")
            if sid not in source_by_id:
                errors.append(f"{path}:{i}: source_id {sid} does not exist in corpus/sources.tsv")
                continue
            if uid:
                if uid not in unit_by_id:
                    errors.append(f"{path}:{i}: source_unit_id {uid} does not exist in corpus/source-units.tsv")
                elif unit_by_id[uid].get("source_id") != sid:
                    errors.append(f"{path}:{i}: source_unit_id {uid} belongs to another archival act")
            key = (project_id, sid, uid)
            if key in project_rows:
                errors.append(f"{path}:{i}: duplicate project/source/unit tuple {project_id}/{sid}/{uid or '-'}")
            project_rows[key] = row
            archival_title = row.get("archival_title", "")
            if archival_title and archival_title != source_by_id[sid].get("title", ""):
                errors.append(f"{path}:{i}: archival_title differs from canonical corpus title for {sid}")
            unit_title = row.get("source_unit_title", "")
            if uid and unit_title != unit_by_id.get(uid, {}).get("title", ""):
                errors.append(f"{path}:{i}: source_unit_title differs from canonical unit title for {uid}")
            fid = row.get("primary_file_id", "")
            if fid:
                if fid not in file_by_id:
                    errors.append(f"{path}:{i}: primary_file_id {fid} does not exist in corpus/files.tsv")
                else:
                    frow = file_by_id[fid]
                    if frow.get("source_id") != sid:
                        errors.append(f"{path}:{i}: primary_file_id {fid} belongs to another archival act")
                    if uid and frow.get("source_unit_id") and frow.get("source_unit_id") != uid:
                        errors.append(f"{path}:{i}: primary_file_id {fid} belongs to another protocol/source unit")
            if row.get("status") == "unit-unresolved" and uid:
                errors.append(f"{path}:{i}: unit-unresolved row must not claim a source_unit_id")

    cross_cfg = contract["tables"]["crosswalks"]
    allowed_mapping = set(contract["controlled_values"]["crosswalk.mapping_status"])
    crosswalks_by_source: dict[str, list[dict[str, str]]] = {}
    for path in sorted(root.glob(cross_cfg["glob"])):
        headers, rows = read_tsv(path)
        check_headers(path, headers, cross_cfg["required_columns"], errors)
        source_dir = path.parent.name
        if source_dir not in source_by_id:
            errors.append(f"{path}: source-data directory {source_dir} has no corpus source record")
        loci_seen: set[tuple[str, str]] = set()
        for i, row in enumerate(rows, start=2):
            sid = row.get("source_id", "")
            uid = row.get("source_unit_id", "")
            if sid != source_dir:
                errors.append(f"{path}:{i}: row source_id {sid!r} must match directory {source_dir}")
            if uid:
                if uid not in unit_by_id:
                    errors.append(f"{path}:{i}: source_unit_id {uid} does not exist in corpus/source-units.tsv")
                elif unit_by_id[uid].get("source_id") != sid:
                    errors.append(f"{path}:{i}: source_unit_id {uid} belongs to another archival act")
            locus = row.get("archival_folio", "")
            locus_key = (uid, locus)
            if not locus:
                errors.append(f"{path}:{i}: archival_folio must not be empty")
            elif locus_key in loci_seen:
                errors.append(f"{path}:{i}: duplicate source-unit/archival-folio pair {uid or '-'}:{locus}")
            loci_seen.add(locus_key)
            mapping = row.get("mapping_status", "")
            if mapping not in allowed_mapping:
                errors.append(f"{path}:{i}: unknown mapping_status {mapping!r}")
            if not any(row.get(field, "") for field in cross_cfg["locator_fields"]):
                errors.append(f"{path}:{i}: at least one digital locator is required ({', '.join(cross_cfg['locator_fields'])})")
            urn = row.get("stable_image_urn", "")
            if urn and not urn.startswith("urn:"):
                errors.append(f"{path}:{i}: stable_image_urn must start with 'urn:'")
        crosswalks_by_source[source_dir] = rows

    for (project_id, sid, uid), row in project_rows.items():
        if row.get("status") == "active" and row.get("relevant_locus"):
            source_rows = crosswalks_by_source.get(sid, [])
            unit_rows = [r for r in source_rows if not uid or not r.get("source_unit_id") or r.get("source_unit_id") == uid]
            if not unit_rows:
                warnings.append(f"projects/{project_id}: active source unit {uid or sid} has a relevant_locus but no source-data crosswalk yet")

    cache.update(
        sources=source_by_id,
        source_units=unit_by_id,
        files=file_by_id,
        project_sources=project_rows,
        crosswalks=crosswalks_by_source,
    )
    return errors, warnings, cache


def cmd_validate(args: argparse.Namespace) -> int:
    root = repo_root(args.root)
    errors, warnings, _ = validate(root, load_contract(root))
    for item in warnings:
        print(f"WARN: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    if errors:
        print(f"source-contract: FAIL ({len(errors)} error(s), {len(warnings)} warning(s))")
        return 1
    print(f"source-contract: OK ({len(warnings)} warning(s))")
    return 0


def cmd_resolve(args: argparse.Namespace) -> int:
    root = repo_root(args.root)
    errors, warnings, cache = validate(root, load_contract(root))
    if errors:
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        return 1
    if not args.source_id and not args.source_unit_id:
        print("ERROR: pass --source-id or --source-unit-id", file=sys.stderr)
        return 2

    candidates = [
        (key, row)
        for key, row in cache["project_sources"].items()
        if key[0] == args.project
        and (not args.source_id or key[1] == args.source_id)
        and (not args.source_unit_id or key[2] == args.source_unit_id)
    ]
    if not candidates:
        print(f"ERROR: requested source/unit is not registered in project {args.project}", file=sys.stderr)
        return 2
    if len(candidates) > 1:
        print("ERROR: archival act has multiple project source units; pass --source-unit-id", file=sys.stderr)
        return 2

    (_key, project_row) = candidates[0]
    sid = project_row["source_id"]
    uid = project_row.get("source_unit_id", "")
    source_row = cache["sources"][sid]
    unit_row = cache["source_units"].get(uid) if uid else None
    fid = project_row.get("primary_file_id", "")
    file_row = cache["files"].get(fid) if fid else None

    rows = cache["crosswalks"].get(sid, [])
    if uid:
        rows = [row for row in rows if not row.get("source_unit_id") or row.get("source_unit_id") == uid]
    locus_matches = []
    if args.locus:
        locus_matches = [row for row in rows if row.get("archival_folio") == args.locus]
        if not locus_matches:
            print(f"ERROR: canonical crosswalk has no exact archival_folio {args.locus!r} for {uid or sid}", file=sys.stderr)
            return 3

    result = {
        "project": args.project,
        "project_source": project_row,
        "archival_act": source_row,
        "source_unit": unit_row,
        "source_level": "protocol_source_unit" if unit_row else "archival_act",
        "primary_file": file_row,
        "locus": args.locus or None,
        "locus_matches": locus_matches,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate and resolve paleo-type source provenance.")
    parser.add_argument("--root", help="Repository root; defaults to the script's repository.")
    sub = parser.add_subparsers(dest="command", required=True)

    v = sub.add_parser("validate", help="Validate the source/provenance contract.")
    v.set_defaults(func=cmd_validate)

    r = sub.add_parser("resolve", help="Resolve a project protocol/source unit to its archival act, file and locus provenance.")
    r.add_argument("--project", required=True)
    r.add_argument("--source-id")
    r.add_argument("--source-unit-id")
    r.add_argument("--locus")
    r.set_defaults(func=cmd_resolve)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
