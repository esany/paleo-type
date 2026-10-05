#!/usr/bin/env python3
"""Validate and inspect the admitted engineering knowledge/configuration plane."""

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
APPLICABILITY_BASIS_KINDS = {
    "formal-derived",
    "owner-declared",
    "work-contract",
    "selected-with-basis",
    "candidate/unresolved",
}
CHANGE_TRANSITION_STATES = {
    "proposed",
    "admitted",
    "implemented",
    "verified",
    "accepted",
    "no-change",
    "needs-decision",
    "re-entered",
    "revoked",
    "rejected",
    "superseded",
}
ALLOWED_CHANGE_TRANSITIONS = {
    "proposed": {"admitted", "rejected", "superseded", "re-entered"},
    "admitted": {"implemented", "revoked", "rejected", "superseded", "re-entered"},
    "implemented": {"verified", "re-entered", "rejected", "superseded"},
    "verified": {"accepted", "no-change", "needs-decision", "re-entered", "rejected", "superseded"},
    "needs-decision": {"accepted", "no-change", "re-entered", "rejected", "superseded"},
    "accepted": {"superseded", "re-entered"},
    "no-change": {"superseded", "re-entered"},
    "re-entered": {"proposed", "admitted", "rejected", "superseded"},
    "revoked": {"proposed", "superseded"},
    "rejected": {"proposed", "superseded"},
    "superseded": set(),
}
RESULT_CONSEQUENCES = {"pending", "baseline-change", "no-change"}
CHANGE_LIFECYCLES = {"implementing", "verifying", "reviewing", "complete", "re-entered"}
ADMISSION_STATES = {"not-admitted", "admitted", "revoked"}
WORK_PACKAGE_STATES = {"not-started", "ready-next", "implementing", "implemented-candidate", "verified", "complete", "blocked", "re-entered"}


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


def discover_changes(engineering: Path) -> set[str]:
    changes_dir = engineering / "changes"
    if not changes_dir.is_dir():
        return set()
    return {path.name for path in changes_dir.iterdir() if path.is_dir()}


def discover_adrs(engineering: Path) -> set[str]:
    decisions_dir = engineering / "decisions"
    if not decisions_dir.is_dir():
        return set()
    adrs: set[str] = set()
    for path in decisions_dir.iterdir():
        match = re.match(r"^(ADR-\d{4})\b", path.name)
        if match:
            adrs.add(match.group(1))
    return adrs


def ref_exists(
    ref: str,
    artifacts: dict[str, dict[str, str]],
    findings: dict[str, dict[str, str]],
    changes: set[str],
    decisions: set[str],
    adrs: set[str],
    root: Path,
) -> bool:
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


def transition_allowed(from_state: str, to_state: str) -> bool:
    return from_state in ALLOWED_CHANGE_TRANSITIONS and to_state in ALLOWED_CHANGE_TRANSITIONS[from_state]


def _artifact_kind(ref: str, artifacts: dict[str, dict[str, str]]) -> str | None:
    if not ref.startswith("artifact:"):
        return None
    row = artifacts.get(ref.removeprefix("artifact:"))
    return row.get("kind") if row else None


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
            errors.append(f"{path}: missing canonical engineering table")
            tables[name] = {}
            continue
        headers, rows = read_tsv(path)
        require_headers(path, headers, required, errors)
        tables[name] = unique_rows(path, rows, required[0], errors)

    artifacts = tables["artifacts"]
    findings = tables["findings"]
    coverage = tables["coverage"]
    relations = tables["relations"]
    changes = discover_changes(engineering)
    decisions_text = (root / "DECISIONS.md").read_text(encoding="utf-8") if (root / "DECISIONS.md").is_file() else ""
    decisions = set(re.findall(r"^## (D-\d{3})\b", decisions_text, re.MULTILINE))
    adrs = discover_adrs(engineering)

    def reference_ok(ref: str) -> bool:
        return ref_exists(ref, artifacts, findings, changes, decisions, adrs, root)

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
            errors.append(f"{finding_path}: {finding_id}: engineering baseline rows must be material")
        if row.get("disposition") not in DISPOSITIONS:
            errors.append(f"{finding_path}: {finding_id}: invalid disposition {row.get('disposition')!r}")
        if not reference_ok(row.get("source_ref", "")):
            errors.append(f"{finding_path}: {finding_id}: unresolved source_ref {row.get('source_ref')!r}")
        if not row.get("target_ref"):
            errors.append(f"{finding_path}: {finding_id}: target_ref is required even for residual dispositions")
        elif not reference_ok(row["target_ref"]):
            errors.append(f"{finding_path}: {finding_id}: unresolved target_ref {row['target_ref']!r}")

    coverage_path = catalog / "coverage.tsv"
    covered: list[str] = []
    for coverage_id, row in coverage.items():
        if row.get("coverage_state") not in COVERAGE_STATES:
            errors.append(f"{coverage_path}: {coverage_id}: invalid coverage_state {row.get('coverage_state')!r}")
        for field in ("source_ref", "review_basis", "reviewed_at_ref"):
            if not reference_ok(row.get(field, "")):
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
            if not reference_ok(row.get(field, "")):
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

        if config.get("schema_version") != 2:
            errors.append(f"{config_path}: schema_version must be 2")

        for field in ("architecture_baselines", "requirements_baselines", "active_changes"):
            if not isinstance(config.get(field), list):
                errors.append(f"{config_path}: {field} must be a list")
                continue
            for ref in config[field]:
                if not isinstance(ref, str) or not reference_ok(ref):
                    errors.append(f"{config_path}: unresolved {field} reference {ref!r}")
                elif field in {"architecture_baselines", "requirements_baselines"} and ref.startswith("artifact:"):
                    role = artifacts[ref.removeprefix("artifact:")].get("authority_role")
                    if role not in {"canonical", "accepted-decision"}:
                        errors.append(f"{config_path}: {field} cannot point at non-accepted artifact {ref!r}")

        change_states = config.get("change_states")
        if not isinstance(change_states, dict):
            errors.append(f"{config_path}: change_states must be an object")
            change_states = {}
        active_changes = config.get("active_changes") if isinstance(config.get("active_changes"), list) else []
        for ref in active_changes:
            if ref not in change_states:
                errors.append(f"{config_path}: active change {ref!r} has no explicit change_states entry")
        for change_ref, entry in change_states.items():
            if not isinstance(entry, dict):
                errors.append(f"{config_path}: change_states.{change_ref} must be an object")
                continue
            if not reference_ok(change_ref):
                errors.append(f"{config_path}: unresolved change state reference {change_ref!r}")
            transition_state = entry.get("transition_state")
            if transition_state not in CHANGE_TRANSITION_STATES:
                errors.append(f"{config_path}: {change_ref}: invalid transition_state {transition_state!r}")
            if not reference_ok(str(entry.get("basis_ref", ""))):
                errors.append(f"{config_path}: {change_ref}: unresolved basis_ref")
            if not reference_ok(str(entry.get("work_owner", ""))):
                errors.append(f"{config_path}: {change_ref}: unresolved work_owner")
            consequence = entry.get("accepted_consequence")
            if consequence not in RESULT_CONSEQUENCES:
                errors.append(f"{config_path}: {change_ref}: invalid accepted_consequence {consequence!r}")
            if transition_state == "accepted" and consequence == "pending":
                errors.append(f"{config_path}: {change_ref}: accepted transition requires an explicit accepted consequence")
            if transition_state == "no-change" and consequence != "no-change":
                errors.append(f"{config_path}: {change_ref}: no-change transition must carry accepted_consequence=no-change")

        focus = config.get("current_focus")
        if focus is not None:
            if not isinstance(focus, dict):
                errors.append(f"{config_path}: current_focus must be null or an object")
            else:
                if not reference_ok(str(focus.get("ref", ""))):
                    errors.append(f"{config_path}: current_focus.ref is unresolved")
                if focus.get("basis_kind") not in APPLICABILITY_BASIS_KINDS:
                    errors.append(f"{config_path}: current_focus has invalid basis_kind {focus.get('basis_kind')!r}")
                if not reference_ok(str(focus.get("basis_ref", ""))):
                    errors.append(f"{config_path}: current_focus.basis_ref is unresolved")
                work_ref = focus.get("work_ref")
                if work_ref is not None and not reference_ok(str(work_ref)):
                    errors.append(f"{config_path}: current_focus.work_ref is unresolved")
                if not str(focus.get("scope", "")).strip():
                    errors.append(f"{config_path}: current_focus.scope is required when focus is present")

        applicability = config.get("applicability")
        if not isinstance(applicability, list):
            errors.append(f"{config_path}: applicability must be a list")
            applicability = []
        for index, entry in enumerate(applicability):
            label = f"applicability[{index}]"
            if not isinstance(entry, dict):
                errors.append(f"{config_path}: {label} must be an object")
                continue
            if not reference_ok(str(entry.get("ref", ""))):
                errors.append(f"{config_path}: {label}.ref is unresolved")
            if entry.get("basis_kind") not in APPLICABILITY_BASIS_KINDS:
                errors.append(f"{config_path}: {label} has invalid basis_kind {entry.get('basis_kind')!r}")
            if not reference_ok(str(entry.get("basis_ref", ""))):
                errors.append(f"{config_path}: {label}.basis_ref is unresolved")
            if not str(entry.get("scope", "")).strip():
                errors.append(f"{config_path}: {label}.scope is required")

        if not reference_ok(str(config.get("decision_owner", ""))):
            errors.append(f"{config_path}: unresolved decision_owner")

        provenance = config.get("transition_provenance", {})
        if not isinstance(provenance, dict):
            errors.append(f"{config_path}: transition_provenance must be an object")
            provenance = {}
        for field in ("admission_ref", "decision_ref", "programme_owner", "implementation_owner"):
            if not reference_ok(str(provenance.get(field, ""))):
                errors.append(f"{config_path}: unresolved transition_provenance.{field}")
        result_ref = provenance.get("result_ref")
        if result_ref is not None and not reference_ok(str(result_ref)):
            errors.append(f"{config_path}: unresolved transition_provenance.result_ref")
        for field in ("admission_head", "implementation_head", "execution_baseline_head"):
            value = provenance.get(field)
            if value is not None and not GIT_REF_RE.fullmatch(f"git:{value}"):
                errors.append(f"{config_path}: {field} must be a 40-character Git SHA")

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
        if state.get("lifecycle") not in CHANGE_LIFECYCLES:
            errors.append(f"{state_path}: invalid lifecycle {state.get('lifecycle')!r}")
        if state.get("admission") not in ADMISSION_STATES:
            errors.append(f"{state_path}: invalid admission {state.get('admission')!r}")
        for field in ("admission_ref", "work_owner", "programme_owner", "plan_ref", "result_ref"):
            if not reference_ok(str(state.get(field, ""))):
                errors.append(f"{state_path}: unresolved {field}")
        if _artifact_kind(str(state.get("plan_ref", "")), artifacts) != "change-plan":
            errors.append(f"{state_path}: plan_ref must point to a change-plan artifact")
        if _artifact_kind(str(state.get("result_ref", "")), artifacts) != "result":
            errors.append(f"{state_path}: result_ref must point to a result artifact")
        if not isinstance(state.get("blocking_uncertainties"), list):
            errors.append(f"{state_path}: blocking_uncertainties must be a list")
        for ref in state.get("applicable_rules", []):
            if not reference_ok(str(ref)):
                errors.append(f"{state_path}: unresolved applicable_rule {ref!r}")
        verification_head = state.get("verification_head")
        if verification_head is not None and not reference_ok(str(verification_head)):
            errors.append(f"{state_path}: unresolved verification_head")
        package_status = state.get("work_package_status")
        if not isinstance(package_status, dict):
            errors.append(f"{state_path}: work_package_status must be an object")
        else:
            expected_packages = {f"WP{i}" for i in range(1, 7)}
            if set(package_status) != expected_packages:
                errors.append(f"{state_path}: work_package_status must contain exactly WP1..WP6")
            for name, status in package_status.items():
                if status not in WORK_PACKAGE_STATES:
                    errors.append(f"{state_path}: {name} has invalid status {status!r}")
        for name, entry in state.get("coverage", {}).items():
            if entry.get("state") not in {"required-satisfied", "not-required-with-rationale", "re-entered", "required-open", "blocked"}:
                errors.append(f"{state_path}: coverage.{name} has invalid state {entry.get('state')!r}")
            for basis_ref in [item for item in str(entry.get("basis", "")).split(";") if item]:
                if not reference_ok(basis_ref):
                    errors.append(f"{state_path}: coverage.{name} has unresolved basis {basis_ref!r}")

    focus = config.get("current_focus") if isinstance(config, dict) else None
    summary = {
        "artifact_count": len(artifacts),
        "finding_count": len(findings),
        "coverage_count": len(coverage),
        "relation_count": len(relations),
        "change": state.get("change_id"),
        "lifecycle": state.get("lifecycle"),
        "admission": state.get("admission"),
        "current_focus": focus.get("ref") if isinstance(focus, dict) else None,
    }
    return errors, summary


def _load_artifacts(root: Path) -> dict[str, dict[str, str]]:
    _, rows = read_tsv(root / "engineering" / "catalog" / "artifacts.tsv")
    return {row["artifact_id"]: row for row in rows}


def _expand_artifact(ref: str, artifacts: dict[str, dict[str, str]]) -> dict[str, Any]:
    if not ref.startswith("artifact:"):
        return {"ref": ref}
    artifact_id = ref.removeprefix("artifact:")
    row = artifacts[artifact_id]
    return {
        "ref": ref,
        "artifact_id": artifact_id,
        "kind": row["kind"],
        "title": row["title"],
        "path": row["path"],
        "authority_role": row["authority_role"],
        "lifecycle_state": row["lifecycle_state"],
    }


def compile_current_state(root: Path) -> tuple[list[str], dict[str, Any]]:
    errors, summary = validate(root)
    if errors:
        return errors, {}

    engineering = root / "engineering"
    config = json.loads((engineering / "configuration.json").read_text(encoding="utf-8"))
    state = json.loads((engineering / "changes" / "SD-KA-01" / "STATE.json").read_text(encoding="utf-8"))
    artifacts = _load_artifacts(root)

    active_changes: list[dict[str, Any]] = []
    for change_ref in config["active_changes"]:
        entry = dict(config["change_states"][change_ref])
        entry["ref"] = change_ref
        if change_ref == f"change:{state.get('change_id')}":
            entry["lifecycle"] = state.get("lifecycle")
            entry["work_package_status"] = state.get("work_package_status")
            entry["change_state_owner"] = "path:engineering/changes/SD-KA-01/STATE.json"
        active_changes.append(entry)

    focus = config.get("current_focus")
    focus_view: dict[str, Any]
    if focus is None:
        focus_view = {
            "state": "absent",
            "reason": "No explicitly authorized current engineering focus is recorded in configuration.",
        }
    else:
        focus_view = {"state": "present", **focus}

    current = {
        "view_kind": "derived-current-engineering-state",
        "authority": "derived-only; canonical facts remain in configuration/change/catalog owners",
        "accepted_configuration": {
            "architecture_baselines": [_expand_artifact(ref, artifacts) for ref in config["architecture_baselines"]],
            "requirements_baselines": [_expand_artifact(ref, artifacts) for ref in config["requirements_baselines"]],
            "decision_owner": config["decision_owner"],
        },
        "active_changes": active_changes,
        "current_focus": focus_view,
        "applicability": config["applicability"],
        "explicit_absence": {
            "active_changes": len(active_changes) == 0,
            "current_focus": focus is None,
        },
        "transition_provenance": config["transition_provenance"],
        "summary": summary,
        "non_claims": [
            "Git recency does not create semantic currentness.",
            "Issue, PR or CI state does not create accepted engineering baselines.",
            "This view does not own or infer Project scholarly purpose, priority, gate state or NEXT ACTION.",
        ],
    }
    return [], current


def query_artifacts(
    root: Path,
    kind: str | None = None,
    lifecycle: str | None = None,
    authority_role: str | None = None,
    owner_scope: str | None = None,
) -> list[dict[str, str]]:
    _, rows = read_tsv(root / "engineering" / "catalog" / "artifacts.tsv")
    return [
        row
        for row in rows
        if (kind is None or row["kind"] == kind)
        and (lifecycle is None or row["lifecycle_state"] == lifecycle)
        and (authority_role is None or row["authority_role"] == authority_role)
        and (owner_scope is None or row["owner_scope"] == owner_scope)
    ]


def command_validate(root: Path) -> int:
    errors, summary = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"status": "PASS", **summary}, indent=2, sort_keys=True))
    return 0


def command_current(root: Path) -> int:
    errors, current = compile_current_state(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps(current, indent=2, sort_keys=True))
    return 0


def command_derive(root: Path) -> int:
    errors, summary = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    current_errors, current = compile_current_state(root)
    if current_errors:
        for error in current_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    config = json.loads((root / "engineering" / "configuration.json").read_text(encoding="utf-8"))
    state = json.loads((root / "engineering" / "changes" / "SD-KA-01" / "STATE.json").read_text(encoding="utf-8"))
    print(json.dumps({"status": "PASS", "configuration": config, "change": state, "current": current, "summary": summary}, indent=2, sort_keys=True))
    return 0


def command_query(root: Path, kind: str | None, lifecycle: str | None, authority_role: str | None, owner_scope: str | None) -> int:
    errors, _ = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(json.dumps(query_artifacts(root, kind, lifecycle, authority_role, owner_scope), indent=2, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", help="repository root; defaults to the repository containing this tool")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    subparsers.add_parser("derive")
    subparsers.add_parser("current")
    query = subparsers.add_parser("query")
    query.add_argument("--kind")
    query.add_argument("--lifecycle")
    query.add_argument("--authority-role")
    query.add_argument("--owner-scope")
    args = parser.parse_args()
    root = repo_root(args.root)
    if args.command == "validate":
        return command_validate(root)
    if args.command == "derive":
        return command_derive(root)
    if args.command == "current":
        return command_current(root)
    return command_query(root, args.kind, args.lifecycle, args.authority_role, args.owner_scope)


if __name__ == "__main__":
    raise SystemExit(main())
