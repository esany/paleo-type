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
RESEARCH_FUNCTION_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


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


def read_simple_yaml_scalars(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        data[key.strip()] = value
    return data


def check_headers(path: Path, headers: list[str], required: list[str], errors: list[str]) -> None:
    missing = [name for name in required if name not in headers]
    if missing:
        errors.append(f"{path}: missing required columns: {', '.join(missing)}")


def validate_project_relative_file(project_dir: Path, raw: str, field: str, errors: list[str]) -> Path | None:
    rel = Path(raw)
    if rel.is_absolute() or ".." in rel.parts:
        errors.append(f"{project_dir / 'project.yml'}: {field} must be a project-relative path without '..': {raw!r}")
        return None
    target = project_dir / rel
    if not target.is_file():
        errors.append(f"{project_dir / 'project.yml'}: {field} points to missing file {raw!r}")
        return None
    return target



def validate_source_entry_owner(
    root: Path,
    source_by_id: dict[str, dict[str, str]],
    file_by_id: dict[str, dict[str, str]],
    project_by_id: dict[str, dict[str, str]],
    errors: list[str],
) -> dict[str, object]:
    """Validate the admitted source-entry route/coverage owner.

    Route rows are append-only. Currentness is derived from the highest contiguous
    transition_sequence for each Source; coverage records retain the exact route_id
    under which they were created.
    """
    owner_dir = root / "source-entry"
    contract_path = owner_dir / "contract.json"
    if not contract_path.is_file():
        return {"routes": [], "coverage": [], "current_routes": {}}

    try:
        owner_contract = json.loads(contract_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{contract_path}: invalid JSON: {exc}")
        return {"routes": [], "coverage": [], "current_routes": {}}

    route_cfg = owner_contract.get("tables", {}).get("routes", {})
    coverage_cfg = owner_contract.get("tables", {}).get("coverage", {})
    route_path = owner_dir / route_cfg.get("path", "routes.tsv")
    coverage_path = owner_dir / coverage_cfg.get("path", "inspection-coverage.tsv")

    if route_path.is_file():
        route_headers, routes = read_tsv(route_path)
    else:
        route_headers, routes = [], []
    if coverage_path.is_file():
        coverage_headers, coverage = read_tsv(coverage_path)
    else:
        coverage_headers, coverage = [], []

    check_headers(route_path, route_headers, route_cfg.get("required_columns", []), errors)
    check_headers(coverage_path, coverage_headers, coverage_cfg.get("required_columns", []), errors)

    controlled = owner_contract.get("controlled_values", {})
    allowed_route_states = set(controlled.get("route_state", []))
    allowed_authority = set(controlled.get("authority_status", []))
    allowed_coverage = set(controlled.get("coverage_status", []))
    allowed_relevance = set(controlled.get("relevance_status", []))
    allowed_evidence = set(controlled.get("evidence_status", []))
    allowed_layers = set(controlled.get("claim_layer", []))

    forbidden_headers = {"active_scope", "gate", "next_action", "scholarly_scope"}
    for path, headers in ((route_path, route_headers), (coverage_path, coverage_headers)):
        for field in sorted(forbidden_headers.intersection(headers)):
            errors.append(
                f"{path}: source-entry owner must not contain Project/scholarly state column {field}"
            )

    route_by_id: dict[str, dict[str, str]] = {}
    routes_by_source: dict[str, list[tuple[int, dict[str, str]]]] = {}

    for i, row in enumerate(routes, start=2):
        for field in route_cfg.get("required_nonempty", []):
            if not row.get(field):
                errors.append(f"{route_path}:{i}: {field} must not be empty")

        route_id = row.get("route_id", "")
        if route_id:
            if route_id in route_by_id:
                errors.append(f"{route_path}:{i}: duplicate route_id {route_id}")
            route_by_id[route_id] = row

        source_id = row.get("source_id", "")
        if source_id and source_id not in source_by_id:
            errors.append(f"{route_path}:{i}: source_id {source_id} does not exist in corpus/sources.tsv")

        try:
            sequence = int(row.get("transition_sequence", ""))
            if sequence < 1:
                raise ValueError
        except ValueError:
            errors.append(f"{route_path}:{i}: transition_sequence must be a positive integer")
            sequence = 0

        if source_id and sequence:
            routes_by_source.setdefault(source_id, []).append((sequence, row))

        route_state = row.get("route_state", "")
        if route_state and route_state not in allowed_route_states:
            errors.append(f"{route_path}:{i}: unknown route_state {route_state!r}")

        authority = row.get("authority_status", "")
        if authority and authority not in allowed_authority:
            errors.append(f"{route_path}:{i}: unknown authority_status {authority!r}")

        project_id = row.get("project_id", "")
        if route_state in {"UNRESOLVED", "CANDIDATE_NEW_PROJECT", "CORPUS_ONLY / NO_PROJECT_YET"} and project_id:
            errors.append(f"{route_path}:{i}: {route_state} cannot carry project_id")

        if route_state == "CORPUS_ONLY / NO_PROJECT_YET" and authority != "HUMAN-OWNER-CONFIRMED":
            errors.append(
                f"{route_path}:{i}: CORPUS_ONLY / NO_PROJECT_YET requires HUMAN-OWNER-CONFIRMED authority_status"
            )

        if route_state == "EXISTING_PROJECT":
            if not project_id:
                errors.append(f"{route_path}:{i}: EXISTING_PROJECT requires project_id")
            elif project_id not in project_by_id:
                errors.append(f"{route_path}:{i}: project_id {project_id} does not exist")
            if authority != "HUMAN-OWNER-CONFIRMED":
                errors.append(
                    f"{route_path}:{i}: EXISTING_PROJECT requires HUMAN-OWNER-CONFIRMED authority_status"
                )

    current_route_by_source: dict[str, dict[str, str]] = {}
    for source_id, entries in routes_by_source.items():
        sequences = sorted(sequence for sequence, _ in entries)
        if len(sequences) != len(set(sequences)):
            errors.append(f"{route_path}: source {source_id} has duplicate transition_sequence values")
            continue
        expected = list(range(1, max(sequences) + 1))
        if sequences != expected:
            errors.append(
                f"{route_path}: source {source_id} transition_sequence must be contiguous from 1; got {sequences}"
            )
        current_route_by_source[source_id] = max(entries, key=lambda item: item[0])[1]

    coverage_by_id: dict[str, dict[str, str]] = {}
    for i, row in enumerate(coverage, start=2):
        for field in coverage_cfg.get("required_nonempty", []):
            if not row.get(field):
                errors.append(f"{coverage_path}:{i}: {field} must not be empty")

        inspection_id = row.get("inspection_id", "")
        if inspection_id:
            if inspection_id in coverage_by_id:
                errors.append(f"{coverage_path}:{i}: duplicate inspection_id {inspection_id}")
            coverage_by_id[inspection_id] = row

        source_id = row.get("source_id", "")
        if source_id and source_id not in source_by_id:
            errors.append(
                f"{coverage_path}:{i}: source_id {source_id} does not exist in corpus/sources.tsv"
            )

        route_id = row.get("route_id", "")
        route = route_by_id.get(route_id)
        if route_id and route is None:
            errors.append(f"{coverage_path}:{i}: route_id {route_id} does not exist in source-entry/routes.tsv")
        elif route is not None:
            route_source = route.get("source_id", "")
            if source_id and route_source != source_id:
                errors.append(
                    f"{coverage_path}:{i}: route_id {route_id} belongs to source {route_source}, not {source_id}"
                )
            route_state = route.get("route_state", "")
            if route_state not in {"CORPUS_ONLY / NO_PROJECT_YET", "EXISTING_PROJECT"}:
                errors.append(
                    f"{coverage_path}:{i}: durable coverage requires a resolved CORPUS_ONLY / NO_PROJECT_YET "
                    f"or EXISTING_PROJECT route; {route_id} is {route_state or 'UNSET'}"
                )

        file_id = row.get("file_id", "")
        if file_id:
            if file_id not in file_by_id:
                errors.append(f"{coverage_path}:{i}: file_id {file_id} does not exist in corpus/files.tsv")
            elif source_id and file_by_id[file_id].get("source_id") != source_id:
                errors.append(f"{coverage_path}:{i}: file_id {file_id} belongs to another Source")

        project_id = row.get("project_id", "")
        if project_id and project_id not in project_by_id:
            errors.append(f"{coverage_path}:{i}: project_id {project_id} does not exist")
        if project_id and route is not None:
            if route.get("route_state") != "EXISTING_PROJECT" or route.get("project_id") != project_id:
                errors.append(
                    f"{coverage_path}:{i}: Project-bound coverage requires its route_id to be "
                    f"EXISTING_PROJECT for {project_id}"
                )

        coverage_status = row.get("coverage_status", "")
        relevance = row.get("relevance_status", "")
        evidence = row.get("evidence_status", "")
        layer = row.get("claim_layer", "")

        if coverage_status and coverage_status not in allowed_coverage:
            errors.append(f"{coverage_path}:{i}: unknown coverage_status {coverage_status!r}")
        if relevance and relevance not in allowed_relevance:
            errors.append(f"{coverage_path}:{i}: unknown relevance_status {relevance!r}")
        if evidence and evidence not in allowed_evidence:
            errors.append(f"{coverage_path}:{i}: unknown evidence_status {evidence!r}")
        if layer and layer not in allowed_layers:
            errors.append(f"{coverage_path}:{i}: unknown claim_layer {layer!r}")
        if evidence == "H" and layer == "OBSERVATION":
            errors.append(f"{coverage_path}:{i}: H evidence cannot be claim_layer OBSERVATION")
        if coverage_status == "NOT_INSPECTED" and evidence == "P":
            errors.append(
                f"{coverage_path}:{i}: NOT_INSPECTED cannot claim P inspected-primary evidence"
            )

    return {
        "routes": routes,
        "coverage": coverage,
        "current_routes": current_route_by_source,
    }



def is_within(source_id: str, root_id: str, parents: dict[str, list[str]]) -> bool:
    if source_id == root_id:
        return True
    seen: set[str] = set()
    stack = list(parents.get(source_id, []))
    while stack:
        node = stack.pop()
        if node == root_id:
            return True
        if node in seen:
            continue
        seen.add(node)
        stack.extend(parents.get(node, []))
    return False


def validate(root: Path, contract: dict) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    cache: dict[str, object] = {}

    source_cfg = contract["tables"]["sources"]
    source_path = root / source_cfg["path"]
    sh, sources = read_tsv(source_path)
    check_headers(source_path, sh, source_cfg["required_columns"], errors)
    source_by_id: dict[str, dict[str, str]] = {}
    for i, row in enumerate(sources, start=2):
        for field in source_cfg["required_nonempty"]:
            if not row.get(field):
                errors.append(f"{source_path}:{i}: {field} must not be empty")
        sid = row.get(source_cfg["key"], "")
        if sid:
            if sid in source_by_id:
                errors.append(f"{source_path}:{i}: duplicate source_id {sid}")
            source_by_id[sid] = row
        if bool(row.get("date_from")) != bool(row.get("date_to")):
            errors.append(f"{source_path}:{i}: date_from/date_to must be supplied together")
        if bool(row.get("date_serial_from")) != bool(row.get("date_serial_to")):
            errors.append(f"{source_path}:{i}: date_serial_from/date_serial_to must be supplied together")
        if (row.get("date_serial_from") or row.get("date_serial_to")) and not row.get("date_calendar_label"):
            errors.append(f"{source_path}:{i}: serial date values require date_calendar_label")

    rel_cfg = contract["tables"]["relationships"]
    rel_path = root / rel_cfg["path"]
    rh, relationships = read_tsv(rel_path)
    check_headers(rel_path, rh, rel_cfg["required_columns"], errors)
    relation_by_id: dict[str, dict[str, str]] = {}
    parents_by_source: dict[str, list[str]] = {}
    part_pairs: set[tuple[str, str]] = set()
    for i, row in enumerate(relationships, start=2):
        for field in rel_cfg["required_nonempty"]:
            if not row.get(field):
                errors.append(f"{rel_path}:{i}: {field} must not be empty")
        rid = row.get(rel_cfg["key"], "")
        if rid:
            if rid in relation_by_id:
                errors.append(f"{rel_path}:{i}: duplicate relation_id {rid}")
            relation_by_id[rid] = row
        subject = row.get("subject_id", "")
        obj = row.get("object_id", "")
        predicate = row.get("predicate", "")
        if row.get("subject_locus") and subject not in source_by_id:
            errors.append(f"{rel_path}:{i}: subject_locus requires canonical source subject {subject}")
        if row.get("object_locus") and obj not in source_by_id:
            errors.append(f"{rel_path}:{i}: object_locus requires canonical source object {obj}")
        if predicate == "textually_corresponds_to":
            if subject not in source_by_id:
                errors.append(f"{rel_path}:{i}: textually_corresponds_to subject {subject} is not a corpus source node")
            if obj not in source_by_id:
                errors.append(f"{rel_path}:{i}: textually_corresponds_to object {obj} is not a corpus source node")
        if predicate != "part_of":
            continue
        if subject not in source_by_id:
            errors.append(f"{rel_path}:{i}: part_of subject {subject} is not a corpus source node")
        if obj not in source_by_id:
            errors.append(f"{rel_path}:{i}: part_of object {obj} is not a corpus source node")
        if subject == obj and subject:
            errors.append(f"{rel_path}:{i}: source {subject} cannot be part_of itself")
        pair = (subject, obj)
        if all(pair):
            if pair in part_pairs:
                errors.append(f"{rel_path}:{i}: duplicate part_of relation {subject} -> {obj}")
            part_pairs.add(pair)
            parents_by_source.setdefault(subject, []).append(obj)

    visited: set[str] = set()
    active: list[str] = []

    def visit(node: str) -> None:
        if node in active:
            cycle = active[active.index(node):] + [node]
            errors.append(f"{rel_path}: part_of cycle detected: {' -> '.join(cycle)}")
            return
        if node in visited:
            return
        active.append(node)
        for parent in parents_by_source.get(node, []):
            if parent in source_by_id:
                visit(parent)
        active.pop()
        visited.add(node)

    for sid in source_by_id:
        visit(sid)

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

    projects_cfg = contract["tables"]["projects"]
    project_by_id: dict[str, dict[str, str]] = {}
    allowed_source_registers = set(projects_cfg.get("allowed_source_registers", []))
    forbidden_legacy_keys = projects_cfg.get("forbidden_legacy_keys", [])
    for path in sorted(root.glob(projects_cfg["glob"])):
        meta = read_simple_yaml_scalars(path)
        for key in projects_cfg["required_keys"]:
            if not meta.get(key):
                errors.append(f"{path}: required project key {key} is missing or empty")
        for key in forbidden_legacy_keys:
            if meta.get(key):
                errors.append(f"{path}: legacy project key {key} is no longer allowed")

        project_id = meta.get("id", "")
        directory_id = path.parent.name
        if project_id and project_id != directory_id:
            errors.append(f"{path}: project id {project_id!r} must match directory {directory_id!r}")
        if project_id:
            if project_id in project_by_id:
                errors.append(f"{path}: duplicate project id {project_id}")
            project_by_id[project_id] = meta

        project_source_id = meta.get("project_source_id", "")
        if project_source_id and project_source_id not in source_by_id:
            errors.append(f"{path}: project_source_id {project_source_id} does not exist in corpus/sources.tsv")

        source_register = meta.get("source_register", "")
        if source_register:
            if allowed_source_registers and source_register not in allowed_source_registers:
                errors.append(
                    f"{path}: source_register {source_register!r} is not an allowed target Project source-use owner"
                )
            validate_project_relative_file(path.parent, source_register, "source_register", errors)

        status_file = meta.get("canonical_status_file", "")
        if status_file:
            validate_project_relative_file(path.parent, status_file, "canonical_status_file", errors)

    legacy_glob = projects_cfg.get("legacy_source_register_glob")
    if legacy_glob:
        for legacy_path in sorted(root.glob(legacy_glob)):
            errors.append(
                f"{legacy_path}: legacy Project source register is no longer allowed after loss-checked migration; "
                "use project source-uses.tsv plus research/use-evidence.tsv"
            )

    use_cfg = contract["tables"]["project_source_uses"]
    use_by_id: dict[str, dict[str, str]] = {}
    uses_by_project_source: dict[tuple[str, str], list[dict[str, str]]] = {}
    use_project: dict[str, str] = {}
    for path in sorted(root.glob(use_cfg["glob"])):
        headers, rows = read_tsv(path)
        check_headers(path, headers, use_cfg["required_columns"], errors)
        project_id = path.parent.name
        if project_id not in project_by_id:
            errors.append(f"{path}: no valid projects/{project_id}/project.yml definition")
        elif project_by_id[project_id].get("source_register") != path.name:
            errors.append(
                f"{path}: Project declares source_register {project_by_id[project_id].get('source_register')!r}, not {path.name!r}"
            )
        for i, row in enumerate(rows, start=2):
            for field in use_cfg["required_nonempty"]:
                if not row.get(field):
                    errors.append(f"{path}:{i}: {field} must not be empty")
            use_id = row.get("use_id", "")
            if use_id:
                if use_id in use_by_id:
                    errors.append(f"{path}:{i}: duplicate use_id {use_id}")
                use_by_id[use_id] = row
                use_project[use_id] = project_id
            sid = row.get("source_id", "")
            if sid not in source_by_id:
                errors.append(f"{path}:{i}: source_id {sid} does not exist in corpus/sources.tsv")
            function = row.get("research_function", "")
            if function and not RESEARCH_FUNCTION_RE.match(function):
                errors.append(
                    f"{path}:{i}: research_function {function!r} must be lowercase kebab-case; vocabulary remains open"
                )
            if sid:
                uses_by_project_source.setdefault((project_id, sid), []).append(row)

    evidence_cfg = contract["tables"]["project_use_evidence"]
    evidence_by_id: dict[str, dict[str, str]] = {}
    evidence_by_use: dict[str, list[dict[str, str]]] = {}
    for path in sorted(root.glob(evidence_cfg["glob"])):
        headers, rows = read_tsv(path)
        check_headers(path, headers, evidence_cfg["required_columns"], errors)
        if "source_id" in headers:
            errors.append(f"{path}: source_id must not be duplicated in use-evidence; resolve it through use_id")
        project_id = path.parents[1].name
        if project_id not in project_by_id:
            errors.append(f"{path}: no valid projects/{project_id}/project.yml definition")
        for i, row in enumerate(rows, start=2):
            for field in evidence_cfg["required_nonempty"]:
                if not row.get(field):
                    errors.append(f"{path}:{i}: {field} must not be empty")
            evidence_id = row.get("evidence_id", "")
            if evidence_id:
                if evidence_id in evidence_by_id:
                    errors.append(f"{path}:{i}: duplicate evidence_id {evidence_id}")
                evidence_by_id[evidence_id] = row
            use_id = row.get("use_id", "")
            if use_id not in use_by_id:
                errors.append(f"{path}:{i}: use_id {use_id} does not exist in project source uses")
            elif use_project.get(use_id) != project_id:
                errors.append(f"{path}:{i}: use_id {use_id} belongs to another project")
            fid = row.get("file_id", "")
            if fid not in file_by_id:
                errors.append(f"{path}:{i}: file_id {fid} does not exist in corpus/files.tsv")
            elif use_id in use_by_id:
                use_source_id = use_by_id[use_id].get("source_id", "")
                file_source_id = file_by_id[fid].get("source_id", "")
                if use_source_id and file_source_id != use_source_id:
                    errors.append(
                        f"{path}:{i}: file_id {fid} belongs to source {file_source_id}, not use source {use_source_id}"
                    )
            if use_id:
                evidence_by_use.setdefault(use_id, []).append(row)

    for project_id, meta in project_by_id.items():
        root_id = meta.get("project_source_id", "")
        project_use_pairs = [
            (pid, sid) for (pid, sid) in uses_by_project_source if pid == project_id
        ]
        has_internal_use = any(
            is_within(sid, root_id, parents_by_source) for _, sid in project_use_pairs
        ) if root_id else False
        if root_id and project_use_pairs and not has_internal_use:
            warnings.append(f"projects/{project_id}: no registered source/use lies within project_source_id {root_id}")

    cross_cfg = contract["tables"]["crosswalks"]
    allowed_mapping = set(contract["controlled_values"]["crosswalk.mapping_status"])
    crosswalks_by_source: dict[str, list[dict[str, str]]] = {}
    for path in sorted(root.glob(cross_cfg["glob"])):
        headers, rows = read_tsv(path)
        check_headers(path, headers, cross_cfg["required_columns"], errors)
        source_dir = path.parent.name
        if source_dir not in source_by_id:
            errors.append(f"{path}: source-data directory {source_dir} has no corpus source node")
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

    digital_cfg = contract["tables"].get("digital_crosswalks", {})
    digital_crosswalks_by_source: dict[str, list[dict[str, str]]] = {}
    if digital_cfg:
        digital_ids_seen: set[str] = set()
        for path in sorted(root.glob(digital_cfg["glob"])):
            headers, rows = read_tsv(path)
            check_headers(path, headers, digital_cfg["required_columns"], errors)
            source_dir = path.parent.name
            if source_dir not in source_by_id:
                errors.append(f"{path}: source-data directory {source_dir} has no corpus source node")

            tuples_seen: set[tuple[str, str, str, str]] = set()
            for i, row in enumerate(rows, start=2):
                for field in digital_cfg.get("required_nonempty", []):
                    if not row.get(field):
                        errors.append(f"{path}:{i}: {field} must not be empty")

                mapping_id = row.get(digital_cfg.get("key", "mapping_id"), "")
                if mapping_id:
                    if mapping_id in digital_ids_seen:
                        errors.append(f"{path}:{i}: duplicate digital mapping_id {mapping_id}")
                    digital_ids_seen.add(mapping_id)

                sid = row.get("source_id", "")
                if sid != source_dir:
                    errors.append(f"{path}:{i}: row source_id {sid!r} must match directory {source_dir}")

                mapping = row.get("mapping_status", "")
                if mapping not in allowed_mapping:
                    errors.append(f"{path}:{i}: unknown mapping_status {mapping!r}")

                provider_file_id = row.get("provider_file_id", "")
                pdf_file_id = row.get("pdf_file_id", "")
                for field_name, file_id in (
                    ("provider_file_id", provider_file_id),
                    ("pdf_file_id", pdf_file_id),
                ):
                    if file_id and file_id not in file_by_id:
                        errors.append(f"{path}:{i}: {field_name} {file_id} does not exist in corpus/files.tsv")
                    elif file_id and sid and file_by_id[file_id].get("source_id") != sid:
                        errors.append(
                            f"{path}:{i}: {field_name} {file_id} belongs to source "
                            f"{file_by_id[file_id].get('source_id')}, not {sid}"
                        )

                pdf_page = row.get("pdf_page", "")
                if pdf_page:
                    try:
                        if int(pdf_page) < 1:
                            raise ValueError
                    except ValueError:
                        errors.append(f"{path}:{i}: pdf_page must be a positive integer")

                mapping_tuple = (
                    provider_file_id,
                    row.get("provider_image", ""),
                    pdf_file_id,
                    pdf_page,
                )
                if all(mapping_tuple):
                    if mapping_tuple in tuples_seen:
                        errors.append(
                            f"{path}:{i}: duplicate provider/PDF locator mapping "
                            f"{mapping_tuple[0]}:{mapping_tuple[1]} -> {mapping_tuple[2]}:{mapping_tuple[3]}"
                        )
                    tuples_seen.add(mapping_tuple)

            digital_crosswalks_by_source[source_dir] = rows

    for (project_id, sid), rows in uses_by_project_source.items():
        if any(row.get("status") == "active" and row.get("relevant_locus") for row in rows) and sid not in crosswalks_by_source:
            warnings.append(f"projects/{project_id}: active source use {sid} has a relevant_locus but no source-data crosswalk yet")


    source_entry = validate_source_entry_owner(
        root,
        source_by_id,
        file_by_id,
        project_by_id,
        errors,
    )

    cache.update(
        sources=source_by_id,
        relationships=relation_by_id,
        parents_by_source=parents_by_source,
        files=file_by_id,
        projects=project_by_id,
        project_sources={},
        source_uses=use_by_id,
        uses_by_project_source=uses_by_project_source,
        use_project=use_project,
        use_evidence=evidence_by_id,
        evidence_by_use=evidence_by_use,
        crosswalks=crosswalks_by_source,
        digital_crosswalks=digital_crosswalks_by_source,
        source_entry_routes=source_entry["routes"],
        source_entry_coverage=source_entry["coverage"],
        source_entry_current_routes=source_entry["current_routes"],
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


def part_of_paths(source_id: str, source_by_id: dict[str, dict[str, str]], parents: dict[str, list[str]]) -> list[list[dict[str, str]]]:
    paths: list[list[dict[str, str]]] = []

    def walk(node: str, path: list[dict[str, str]]) -> None:
        node_parents = parents.get(node, [])
        if not node_parents:
            if path:
                paths.append(path)
            return
        for parent_id in node_parents:
            parent = source_by_id.get(parent_id)
            if parent:
                walk(parent_id, path + [parent])

    walk(source_id, [])
    return paths


def source_projects(source_id: str, projects: dict[str, dict[str, str]], parents: dict[str, list[str]]) -> list[str]:
    return sorted(
        project_id
        for project_id, meta in projects.items()
        if meta.get("project_source_id") and is_within(source_id, meta["project_source_id"], parents)
    )


def cmd_resolve(args: argparse.Namespace) -> int:
    root = repo_root(args.root)
    errors, warnings, cache = validate(root, load_contract(root))
    if errors:
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        return 1

    project_meta = cache["projects"].get(args.project)
    if not project_meta:
        print(f"ERROR: project {args.project} has no valid project.yml", file=sys.stderr)
        return 2
    if args.source_id not in cache["sources"]:
        print(f"ERROR: source {args.source_id} does not exist", file=sys.stderr)
        return 2

    key = (args.project, args.source_id)
    project_uses = cache["uses_by_project_source"].get(key, [])
    if not project_uses:
        print(f"ERROR: source {args.source_id} is not used in project {args.project}", file=sys.stderr)
        return 2

    source_row = cache["sources"][args.source_id]
    project_root_id = project_meta.get("project_source_id", "")
    project_root = cache["sources"].get(project_root_id)
    if args.source_id == project_root_id:
        structural_status = "project_root"
    elif is_within(args.source_id, project_root_id, cache["parents_by_source"]):
        structural_status = "internal"
    else:
        structural_status = "external"

    resolved_uses = []
    for use in project_uses:
        evidence_records = []
        for evidence in cache["evidence_by_use"].get(use["use_id"], []):
            evidence_records.append(
                {
                    "evidence": evidence,
                    "file": cache["files"].get(evidence.get("file_id", "")),
                }
            )
        resolved_uses.append({"use": use, "evidence": evidence_records})

    rows = cache["crosswalks"].get(args.source_id, [])
    digital_rows = cache["digital_crosswalks"].get(args.source_id, [])
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
        "project_definition": project_meta,
        "project_root_source": project_root,
        "project_scope": structural_status,
        "structural_status": structural_status,
        "source": source_row,
        "source_type": source_row.get("source_type") or None,
        "part_of_paths": part_of_paths(args.source_id, cache["sources"], cache["parents_by_source"]),
        "source_projects": source_projects(args.source_id, cache["projects"], cache["parents_by_source"]),
        "project_source_uses": resolved_uses,
        "research_functions": [use["research_function"] for use in project_uses],
        "legacy_project_source": None,
        "legacy_primary_file": None,
        "project_source": None,
        "primary_file": None,
        "locus": args.locus or None,
        "locus_matches": locus_matches,
        "digital_crosswalk": digital_rows,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate and resolve paleo-type source provenance and Project source use.")
    parser.add_argument("--root", help="Repository root; defaults to the script's repository.")
    sub = parser.add_subparsers(dest="command", required=True)

    v = sub.add_parser("validate", help="Validate the source/provenance/Project-use contract.")
    v.set_defaults(func=cmd_validate)

    r = sub.add_parser(
        "resolve",
        help="Resolve Project/Source structure, Project research uses, explicit use-evidence, File provenance and optional locus.",
    )
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