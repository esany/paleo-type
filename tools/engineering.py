#!/usr/bin/env python3
"""Validate and inspect the admitted WP1 engineering knowledge baseline."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

ARTIFACT_ID_RE = re.compile(r"^ENG-A-\d{4}$")
FINDING_ID_RE = re.compile(r"^F\d{2}$")
GIT_REF_RE = re.compile(r"^git:[0-9a-f]{40}$")
ISSUE_REF_RE = re.compile(r"^github-(?:issue|pr):[^/#]+/[^#]+#\d+$")
DISPOSITIONS = {
    "open",
    "integrated",
    "promoted",
    "deferred",
    "rejected",
    "superseded",
    "local-only",
    "no-change",
    "controlled",
    "partly-controlled",
    "unresolved",
}
AUTHORITY_ROLES = {"canonical", "accepted-decision", "admitted-change", "non-normative-evidence", "derived", "work-metadata"}
LIFECYCLE_STATES = {"active", "closed", "historical", "superseded", "proposed"}
COVERAGE_STATES = {"not-reviewed", "in-review", "complete-at-evidence-state", "superseded", "not-required-with-rationale"}
RELATION_STATUSES = {"candidate", "accepted", "historical", "unresolved"}
RELATION_PREDICATES = {
    "supports",
    "derived-from",
    "refines",
    "supersedes",
    "implements",
    "verifies",
    "validates",
    "affects",
    "part-of",
    "documents",
    "admitted-by",
    "programme-owner",
    "implementation-owner",
    "describes",
    "covers",
    "transitions-to",
    "constrains",
    "records",
    "promotes-to",
    "integrated-into",
    "remains",
    "controlled-by",
    "deferred-to",
}


def repo_root(explicit: str | None = None) -> Path:
    return Path(explicit).resolve() if explicit else Path(__file__).resolve().parents[1]


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        headers = reader.fieldnames or []
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]
    return headers, rows


def require_headers(path: Path, headers: list[str], required: list[str], errors: list[str]) -> None:
    missing = [header for header in required if header not in headers]
    if missing:
        errors.append(f"{path}: missing columns: {', '.join(missing)}")


def unique_rows(path: Path, rows: list[dict[str, str]], key: str, errors: list[str]) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for line, row in enumerate(rows, start=2):
        value = row.get(key, "")
        if not value:
            errors.append(f"{path}:{line}: {key} must not be empty")
        elif value in indexed:
            errors.append(f"{path}:{line}: duplicate {key} {value}")
        else:
            indexed[value] = row
    return indexed


def ref_exists(ref: str, artifacts: dict[str, dict[str, str]], findings: dict[str, dict[str, str]], changes: set[str], decisions: set[str], adrs: set[str], root: Path) -> bool:
    if ref.startswith("artifact:"):
        return ref.removeprefix("artifact:") in artifacts
    if ref.startswith("finding:"):
        return ref.removeprefix("finding:") in findings
    if ref.startswith("change:"):
        return ref.removeprefix("change:") in changes
    if ref.startswith("decision:"):
        return ref.removeprefix("decision:") in decisions
    if ref.startswith("adr:"):
        return ref.removeprefix("adr:") in adrs
    if ref.startswith("path:"):
        path = Path(ref.removeprefix("path:"))
        return not path.is_absolute() and ".." not in path.parts and (root / path).is_file()
    if GIT_REF_RE.fullmatch(ref) or ISSUE_REF_RE.fullmatch(ref):
        return True
    return False


def validate(root: Path) -> tuple[list[str], dict[str, Any]]:
    engineering = root / "engineering"
    catalog = engineering / "catalog"
    errors: list[str] = []
    tables: dict[str, dict[str, dict[str, str]]] = {}

    specs = {
        "artifacts": (catalog / "artifacts.tsv", ["artifact_id", "kind", "path", "owner_scope", "authority_role", "lifecycle_state", "change_id", "title"]),
        "findings": (catalog / "findings.tsv", ["finding_id", "source_ref", "summary", "materiality", "disposition", "target_ref", "rationale"]),
        "coverage": (catalog / "coverage.tsv", ["coverage_id", "source_ref", "coverage_scope", "review_basis", "reviewed_by_role", "coverage_state", "finding_refs", "nonfinding_material_dispositions", "reviewed_at_ref", "notes_or_rationale"]),
        "relations": (catalog / "relations.tsv", ["relation_id", "subject_ref", "predicate", "object_ref", "relation_status", "evidence_ref"]),
    }
    for name, (path, required) in specs.items():
        if not path.is_file():
            errors.append(f"{path}: missing canonical WP1 table")
            tables[name] = {}
            continue
        headers, rows = read_tsv(path)
        require_headers(path, headers, required, errors)
        tables[name] = unique_rows(path, rows, required[0], errors)

    artifacts = tables["artifacts"]
    findings = tables["findings"]
    coverage = tables["coverage"]
    relations = tables["relations"]
    changes = {"SD-KA-01"}
    decisions_text = (root / "DECISIONS.md").read_text(encoding="utf-8") if (root / "DECISIONS.md").is_file() else ""
    decisions = set(re.findall(r"^## (D-\d{3})\b", decisions_text, re.MULTILINE))
    adrs = {"ADR-0001"} if (engineering / "decisions" / "ADR-0001-sd-ka-01-target-package.md").is_file() else set()

    artifact_path = catalog / "artifacts.tsv"
    for artifact_id, row in artifacts.items():
        if not ARTIFACT_ID_RE.fullmatch(artifact_id):
            errors.append(f"{artifact_path}: invalid artifact_id {artifact_id!r}")
        if row.get("authority_role") not in AUTHORITY_ROLES:
            errors.append(f"{artifact_path}: {artifact_id}: invalid authority_role {row.get('authority_role')!r}")
        if row.get("lifecycle_state") not in LIFECYCLE_STATES:
            errors.append(f"{artifact_path}: {artifact_id}: invalid lifecycle_state {row.get('lifecycle_state')!r}")
        raw_path = row.get("path", "")
        if raw_path.startswith("github://"):
            continue
        path = root / raw_path
        if Path(raw_path).is_absolute() or ".." in Path(raw_path).parts or not path.is_file():
            errors.append(f"{artifact_path}: {artifact_id}: artifact path is not an existing repository file: {raw_path!r}")

    finding_path = catalog / "findings.tsv"
    expected_findings = {f"F{i:02d}" for i in range(1, 46)}
    actual_findings = set(findings)
    if actual_findings != expected_findings:
        errors.append(f"{finding_path}: expected exactly F01–F45; missing={sorted(expected_findings - actual_findings)} extra={sorted(actual_findings - expected_findings)}")
    for finding_id, row in findings.items():
        if not FINDING_ID_RE.fullmatch(finding_id):
            errors.append(f"{finding_path}: invalid finding_id {finding_id!r}")
        if row.get("materiality") != "material":
            errors.append(f"{finding_path}: {finding_id}: WP1 baseline rows must be material")
        if row.get("disposition") not in DISPOSITIONS:
            errors.append(f"{finding_path}: {finding_id}: invalid disposition {row.get('disposition')!r}")
        if not ref_exists(row.get("source_ref", ""), artifacts, findings, changes, decisions, adrs, root):
            errors.append(f"{finding_path}: {finding_id}: unresolved source_ref {row.get('source_ref')!r}")
        if not row.get("target_ref"):
            errors.append(f"{finding_path}: {finding_id}: target_ref is required even for residual dispositions")
        elif not ref_exists(row["target_ref"], artifacts, findings, changes, decisions, adrs, root):
            errors.append(f"{finding_path}: {finding_id}: unresolved target_ref {row['target_ref']!r}")

    coverage_path = catalog / "coverage.tsv"
    covered: list[str] = []
    for coverage_id, row in coverage.items():
        if row.get("coverage_state") not in COVERAGE_STATES:
            errors.append(f"{coverage_path}: {coverage_id}: invalid coverage_state {row.get('coverage_state')!r}")
        for field in ("source_ref", "review_basis", "reviewed_at_ref"):
            if not ref_exists(row.get(field, ""), artifacts, findings, changes, decisions, adrs, root):
                errors.append(f"{coverage_path}: {coverage_id}: unresolved {field} {row.get(field)!r}")
        refs = [item for item in row.get("finding_refs", "").split(";") if item]
        covered.extend(refs)
        for finding_id in refs:
            if finding_id not in findings:
                errors.append(f"{coverage_path}: {coverage_id}: unresolved finding_ref {finding_id!r}")
    if set(covered) != expected_findings or len(covered) != len(set(covered)):
        errors.append(f"{coverage_path}: coverage must account for each F01–F45 exactly once")

    relation_path = catalog / "relations.tsv"
    for relation_id, row in relations.items():
        if row.get("predicate") not in RELATION_PREDICATES:
            errors.append(f"{relation_path}: {relation_id}: invalid predicate {row.get('predicate')!r}")
        if row.get("relation_status") not in RELATION_STATUSES:
            errors.append(f"{relation_path}: {relation_id}: invalid relation_status {row.get('relation_status')!r}")
        for field in ("subject_ref", "object_ref", "evidence_ref"):
            if not ref_exists(row.get(field, ""), artifacts, findings, changes, decisions, adrs, root):
                errors.append(f"{relation_path}: {relation_id}: unresolved {field} {row.get(field)!r}")

    config_path = engineering / "configuration.json"
    config: dict[str, Any] = {}
    if not config_path.is_file():
        errors.append(f"{config_path}: missing configuration owner")
    else:
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{config_path}: invalid JSON: {exc}")
        if config.get("schema_version") != 1:
            errors.append(f"{config_path}: schema_version must be 1")
        for field in ("architecture_baselines", "requirements_baselines", "active_changes"):
            if not isinstance(config.get(field), list):
                errors.append(f"{config_path}: {field} must be a list")
            else:
                for ref in config[field]:
                    if not ref_exists(ref, artifacts, findings, changes, decisions, adrs, root):
                        errors.append(f"{config_path}: unresolved {field} reference {ref!r}")
                    elif field in {"architecture_baselines", "requirements_baselines"} and ref.startswith("artifact:"):
                        role = artifacts[ref.removeprefix("artifact:")].get("authority_role")
                        if role not in {"canonical", "accepted-decision"}:
                            errors.append(f"{config_path}: {field} cannot point at non-accepted artifact {ref!r}")
        focus = config.get("current_focus")
        if focus is not None and (not isinstance(focus, str) or not ref_exists(focus, artifacts, findings, changes, decisions, adrs, root)):
            errors.append(f"{config_path}: current_focus must be null or a resolvable reference")
        if not ref_exists(str(config.get("decision_owner", "")), artifacts, findings, changes, decisions, adrs, root):
            errors.append(f"{config_path}: unresolved decision_owner")
        provenance = config.get("transition_provenance", {})
        for field in ("admission_ref", "decision_ref", "programme_owner", "implementation_owner"):
            if not ref_exists(str(provenance.get(field, "")), artifacts, findings, changes, decisions, adrs, root):
                errors.append(f"{config_path}: unresolved transition_provenance.{field}")
        if not GIT_REF_RE.fullmatch(f"git:{provenance.get('admission_head', '')}"):
            errors.append(f"{config_path}: admission_head must be a 40-character Git SHA")

    state_path = engineering / "changes" / "SD-KA-01" / "STATE.json"
    state: dict[str, Any] = {}
    if not state_path.is_file():
        errors.append(f"{state_path}: missing bounded change state")
    else:
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{state_path}: invalid JSON: {exc}")
        if state.get("change_id") != "SD-KA-01":
            errors.append(f"{state_path}: change_id must be SD-KA-01")
        if state.get("lifecycle") != "implementing":
            errors.append(f"{state_path}: admitted WP1 state must be implementing")
        if state.get("admission") != "admitted":
            errors.append(f"{state_path}: admission must be admitted")
        for field in ("admission_ref", "work_owner", "programme_owner", "plan_ref"):
            if not ref_exists(str(state.get(field, "")), artifacts, findings, changes, decisions, adrs, root):
                errors.append(f"{state_path}: unresolved {field}")
        if state.get("blocking_uncertainties") != []:
            errors.append(f"{state_path}: WP1 must expose no blocking uncertainties at this admitted execution cursor")
        if "bulk requirements migration in WP1" not in state.get("non_goals", []):
            errors.append(f"{state_path}: WP1 must explicitly exclude bulk requirements migration")
        for name, entry in state.get("coverage", {}).items():
            if entry.get("state") not in {"required-satisfied", "not-required-with-rationale", "re-entered", "required-open", "blocked"}:
                errors.append(f"{state_path}: coverage.{name} has invalid state {entry.get('state')!r}")
            if not ref_exists(str(entry.get("basis", "")).split(";", 1)[0], artifacts, findings, changes, decisions, adrs, root):
                errors.append(f"{state_path}: coverage.{name} has unresolved basis")

    summary = {
        "artifact_count": len(artifacts),
        "finding_count": len(findings),
        "coverage_count": len(coverage),
        "relation_count": len(relations),
        "change": state.get("change_id"),
        "lifecycle": state.get("lifecycle"),
        "admission": state.get("admission"),
        "current_focus": config.get("current_focus"),
    }
    return errors, summary


def command_validate(root: Path) -> int:
    errors, summary = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"status": "PASS", **summary}, indent=2, sort_keys=True))
    return 0


def command_derive(root: Path) -> int:
    errors, summary = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    config = json.loads((root / "engineering" / "configuration.json").read_text(encoding="utf-8"))
    state = json.loads((root / "engineering" / "changes" / "SD-KA-01" / "STATE.json").read_text(encoding="utf-8"))
    print(json.dumps({"status": "PASS", "configuration": config, "change": state, "summary": summary}, indent=2, sort_keys=True))
    return 0


def command_query(root: Path, kind: str | None, lifecycle: str | None) -> int:
    path = root / "engineering" / "catalog" / "artifacts.tsv"
    _, rows = read_tsv(path)
    selected = [row for row in rows if (kind is None or row["kind"] == kind) and (lifecycle is None or row["lifecycle_state"] == lifecycle)]
    print(json.dumps(selected, indent=2, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", help="repository root; defaults to the repository containing this tool")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    subparsers.add_parser("derive")
    query = subparsers.add_parser("query")
    query.add_argument("--kind")
    query.add_argument("--lifecycle")
    args = parser.parse_args()
    root = repo_root(args.root)
    if args.command == "validate":
        return command_validate(root)
    if args.command == "derive":
        return command_derive(root)
    return command_query(root, args.kind, args.lifecycle)


if __name__ == "__main__":
    raise SystemExit(main())
