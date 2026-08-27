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
    return Path(explicit).resolve() if explicit else Path(__file__).resolve().parents[1]


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

    act_cfg = contract["tables"]["archival_acts"]
    act_path = root / act_cfg["path"]
    ah, acts = read_tsv(act_path)
    check_headers(act_path, ah, act_cfg["required_columns"], errors)
    act_by_id: dict[str, dict[str, str]] = {}
    allowed_act_status = set(contract["controlled_values"]["archival_acts.status"])
    for i, row in enumerate(acts, start=2):
        for field in act_cfg["required_nonempty"]:
            if not row.get(field):
                errors.append(f"{act_path}:{i}: {field} must not be empty")
        aid = row.get(act_cfg["key"], "")
        if aid:
            if aid in act_by_id:
                errors.append(f"{act_path}:{i}: duplicate archival_act_id {aid}")
            act_by_id[aid] = row
        status = row.get("status", "")
        if status and status not in allowed_act_status:
            errors.append(f"{act_path}:{i}: unknown archival-act status {status!r}")

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
        aid = row.get("archival_act_id", "")
        if aid not in act_by_id:
            errors.append(f"{source_path}:{i}: archival_act_id {aid} does not exist in corpus/archival-acts.tsv")
        else:
            act = act_by_id[aid]
            for field in ("archive", "fonds", "signature"):
                if row.get(field) != act.get(field):
                    errors.append(f"{source_path}:{i}: {field} differs from parent act {aid}")
        identity = tuple(row.get(f, "") for f in source_cfg.get("identity_fields", []))
        if identity and all(identity):
            if identity in identity_seen and identity_seen[identity] != sid:
                errors.append(f"{source_path}:{i}: protocol identity duplicates source {identity_seen[identity]}")
            identity_seen[identity] = sid
        if bool(row.get("date_from")) != bool(row.get("date_to")):
            errors.append(f"{source_path}:{i}: date_from/date_to must be supplied together")
        if bool(row.get("date_serial_from")) != bool(row.get("date_serial_to")):
            errors.append(f"{source_path}:{i}: date_serial_from/date_serial_to must be supplied together")
        if (row.get("date_serial_from") or row.get("date_serial_to")) and not row.get("date_calendar_label"):
            errors.append(f"{source_path}:{i}: serial date values require date_calendar_label")

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
        if sid and sid not in source_by_id:
            errors.append(f"{file_path}:{i}: source_id {sid} does not exist in corpus/sources.tsv")
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
    project_rows: dict[tuple[str, str], dict[str, str]] = {}
    for path in sorted(root.glob(project_cfg["glob"])):
        headers, rows = read_tsv(path)
        check_headers(path, headers, project_cfg["required_columns"], errors)
        project_id = path.parents[1].name
        for i, row in enumerate(rows, start=2):
            for field in project_cfg["required_nonempty"]:
                if not row.get(field):
                    errors.append(f"{path}:{i}: {field} must not be empty")
            sid = row.get("source_id", "")
            if sid not in source_by_id:
                errors.append(f"{path}:{i}: source_id {sid} does not exist in corpus/sources.tsv")
                continue
            key = (project_id, sid)
            if key in project_rows:
                errors.append(f"{path}:{i}: duplicate project/source pair {project_id}/{sid}")
            project_rows[key] = row
            title = row.get("archival_title", "")
            if title and title != source_by_id[sid].get("title", ""):
                errors.append(f"{path}:{i}: archival_title differs from canonical protocol title for {sid}")
            fid = row.get("primary_file_id", "")
            if fid:
                if fid not in file_by_id:
                    errors.append(f"{path}:{i}: primary_file_id {fid} does not exist in corpus/files.tsv")
                elif file_by_id[fid].get("source_id") != sid:
                    errors.append(f"{path}:{i}: primary_file_id {fid} belongs to another protocol source")

    cross_cfg = contract["tables"]["crosswalks"]
    allowed_mapping = set(contract["controlled_values"]["crosswalk.mapping_status"])
    crosswalks_by_source: dict[str, list[dict[str, str]]] = {}
    for path in sorted(root.glob(cross_cfg["glob"])):
        headers, rows = read_tsv(path)
        check_headers(path, headers, cross_cfg["required_columns"], errors)
        source_dir = path.parent.name
        if source_dir not in source_by_id:
            errors.append(f"{path}: source-data directory {source_dir} has no protocol source record")
        loci_seen: set[str] = set()
        for i, row in enumerate(rows, start=2):
            sid = row.get("source_id", "")
            if sid != source_dir:
                errors.append(f"{path}:{i}: row source_id {sid!r} must match directory {source_dir}")
            locus = row.get("archival_folio", "")
            if not locus:
                errors.append(f"{path}:{i}: archival_folio must not be empty")
            elif locus in loci_seen:
                errors.append(f"{path}:{i}: duplicate archival_folio {locus}")
            loci_seen.add(locus)
            mapping = row.get("mapping_status", "")
            if mapping not in allowed_mapping:
                errors.append(f"{path}:{i}: unknown mapping_status {mapping!r}")
            if not any(row.get(field, "") for field in cross_cfg["locator_fields"]):
                errors.append(f"{path}:{i}: at least one digital locator is required ({', '.join(cross_cfg['locator_fields'])})")
            urn = row.get("stable_image_urn", "")
            if urn and not urn.startswith("urn:"):
                errors.append(f"{path}:{i}: stable_image_urn must start with 'urn:'")
        crosswalks_by_source[source_dir] = rows

    for (project_id, sid), row in project_rows.items():
        if row.get("status") == "active" and row.get("relevant_locus") and sid not in crosswalks_by_source:
            warnings.append(f"projects/{project_id}: active source {sid} has a relevant_locus but no source-data crosswalk yet")

    cache.update(
        archival_acts=act_by_id,
        sources=source_by_id,
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

    key = (args.project, args.source_id)
    project_row = cache["project_sources"].get(key)
    if not project_row:
        print(f"ERROR: source {args.source_id} is not registered in project {args.project}", file=sys.stderr)
        return 2
    source_row = cache["sources"][args.source_id]
    act_row = cache["archival_acts"].get(source_row.get("archival_act_id", ""))
    fid = project_row.get("primary_file_id", "")
    file_row = cache["files"].get(fid) if fid else None

    rows = cache["crosswalks"].get(args.source_id, [])
    locus_matches = []
    if args.locus:
        locus_matches = [row for row in rows if row.get("archival_folio") == args.locus]
        if not locus_matches:
            print(
                f"ERROR: canonical crosswalk has no exact archival_folio {args.locus!r} for {args.source_id}",
                file=sys.stderr,
            )
            return 3

    result = {
        "project": args.project,
        "project_source": project_row,
        "source": source_row,
        "source_level": "protocol_record",
        "parent_archival_act": act_row,
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

    r = sub.add_parser("resolve", help="Resolve a project protocol source to its parent act, file and locus provenance.")
    r.add_argument("--project", required=True)
    r.add_argument("--source-id", required=True)
    r.add_argument("--locus")
    r.set_defaults(func=cmd_resolve)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
