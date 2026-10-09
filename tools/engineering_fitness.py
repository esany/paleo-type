#!/usr/bin/env python3
"""Validate the admitted SD-KA-01 WP4 engineering-fitness contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    from tools import engineering, engineering_context
except ModuleNotFoundError:  # direct execution from tools/
    import engineering  # type: ignore
    import engineering_context  # type: ignore

EXPECTED_CHECK_IDS = {f"ENG-FIT-{i:02d}" for i in range(1, 10)}
EXPECTED_FIXTURE_FAMILIES = {
    "stale-current",
    "latest-wins-trap",
    "orphan-finding",
    "coverage-loophole",
    "broken-stable-reference",
    "missing-transition-authority",
    "stale-generated-view",
    "local-pass-trap",
    "context-starvation",
    "false-relation",
    "no-change-result",
    "concurrent-investigations",
    "tiny-routine-change",
    "lean-shortcut-trap",
    "local-pass-without-whole-system-return",
    "local-first-repository-violation",
    "connector-failure-local-fallback",
    "premature-closure-laundering",
    "missing-remote-execution-proof",
    "exact-head",
}
LEGACY_HEADERS = ["legacy_path", "artifact_id", "current_path", "migration_commit"]
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def repo_root(explicit: str | None = None) -> Path:
    return Path(explicit).resolve() if explicit else Path(__file__).resolve().parents[1]


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _artifact_rows(root: Path) -> dict[str, dict[str, str]]:
    _, rows = engineering.read_tsv(root / "engineering" / "catalog" / "artifacts.tsv")
    return {row["artifact_id"]: row for row in rows}


def _ref_resolves(root: Path, ref: str, artifacts: dict[str, dict[str, str]]) -> bool:
    if ref.startswith("artifact:"):
        return ref.removeprefix("artifact:") in artifacts
    if ref.startswith("path:"):
        rel = Path(ref.removeprefix("path:"))
        return not rel.is_absolute() and ".." not in rel.parts and (root / rel).is_file()
    if re.fullmatch(r"github-(?:issue|pr):[^/#]+/[^#]+#\d+", ref):
        return True
    return False


def validate_fitness_contract(root: Path) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    contract_path = root / "engineering" / "assurance" / "fitness.json"
    if not contract_path.is_file():
        return [f"{contract_path}: missing WP4 fitness contract"], {}

    try:
        contract = _load_json(contract_path)
    except json.JSONDecodeError as exc:
        return [f"{contract_path}: invalid JSON: {exc}"], {}

    if contract.get("schema_version") != 1:
        errors.append(f"{contract_path}: schema_version must be 1")
    if contract.get("work_package") != "WP4":
        errors.append(f"{contract_path}: work_package must be WP4")

    artifacts = _artifact_rows(root)
    for field in ("owner_ref", "programme_owner_ref", "design_ref", "shared_execution_boundary_ref"):
        ref = str(contract.get(field, ""))
        if not _ref_resolves(root, ref, artifacts):
            errors.append(f"{contract_path}: unresolved {field} {ref!r}")

    checks = contract.get("checks")
    if not isinstance(checks, list):
        errors.append(f"{contract_path}: checks must be a list")
        checks = []
    check_ids = [str(item.get("id", "")) for item in checks if isinstance(item, dict)]
    if set(check_ids) != EXPECTED_CHECK_IDS or len(check_ids) != len(set(check_ids)):
        errors.append(f"{contract_path}: checks must contain ENG-FIT-01..ENG-FIT-09 exactly once")
    for item in checks:
        if not isinstance(item, dict):
            errors.append(f"{contract_path}: every check entry must be an object")
            continue
        check_id = str(item.get("id", "<missing>"))
        owner_ref = str(item.get("owner_ref", ""))
        if not _ref_resolves(root, owner_ref, artifacts):
            errors.append(f"{contract_path}: {check_id} unresolved owner_ref {owner_ref!r}")
        if not str(item.get("implementation", "")).strip():
            errors.append(f"{contract_path}: {check_id} missing implementation mapping")
        families = item.get("fixture_families")
        if not isinstance(families, list) or not families:
            errors.append(f"{contract_path}: {check_id} must map to at least one fixture family")
        else:
            unknown = sorted(set(map(str, families)) - EXPECTED_FIXTURE_FAMILIES)
            if unknown:
                errors.append(f"{contract_path}: {check_id} has unknown fixture families {unknown}")

    families = contract.get("fixture_families")
    if not isinstance(families, dict):
        errors.append(f"{contract_path}: fixture_families must be an object")
        families = {}
    if set(families) != EXPECTED_FIXTURE_FAMILIES:
        errors.append(
            f"{contract_path}: fixture families mismatch; missing={sorted(EXPECTED_FIXTURE_FAMILIES - set(families))} extra={sorted(set(families) - EXPECTED_FIXTURE_FAMILIES)}"
        )
    for name, test_ref in families.items():
        if not str(test_ref).strip():
            errors.append(f"{contract_path}: fixture family {name!r} has no regression/assurance reference")

    return errors, contract


def _check_generated_views(root: Path, errors: list[str], report: dict[str, Any]) -> None:
    stale_owner = root / "engineering" / "generated" / "CURRENT_STATE.json"
    if stale_owner.exists():
        errors.append(
            f"{stale_owner}: committed CURRENT_STATE.json is forbidden; current engineering state must be rebuilt on demand"
        )
    report["ENG-FIT-05"] = {
        "status": "PASS" if not stale_owner.exists() else "FAIL",
        "mode": "on-demand-derived-current-state",
    }


def _check_legacy_paths(root: Path, errors: list[str], report: dict[str, Any]) -> None:
    path = root / "engineering" / "catalog" / "legacy-paths.tsv"
    headers, rows = engineering.read_tsv(path)
    if headers != LEGACY_HEADERS:
        errors.append(f"{path}: expected headers {LEGACY_HEADERS!r}, got {headers!r}")
    artifacts = _artifact_rows(root)
    for index, row in enumerate(rows, start=2):
        artifact_id = row.get("artifact_id", "")
        artifact = artifacts.get(artifact_id)
        if artifact is None:
            errors.append(f"{path}:{index}: unknown artifact_id {artifact_id!r}")
            continue
        legacy_path = Path(row.get("legacy_path", ""))
        if not row.get("legacy_path") or legacy_path.is_absolute() or ".." in legacy_path.parts:
            errors.append(f"{path}:{index}: legacy_path must be a safe repository-relative locator")
        current_path = row.get("current_path", "")
        if current_path != artifact.get("path"):
            errors.append(
                f"{path}:{index}: current_path {current_path!r} does not match catalog path {artifact.get('path')!r}"
            )
        migration_commit = row.get("migration_commit", "")
        if not SHA_RE.fullmatch(migration_commit):
            errors.append(f"{path}:{index}: migration_commit must be an exact 40-character Git SHA")
    state = _load_json(root / "engineering" / "changes" / "SD-KA-01" / "STATE.json")
    wp5 = state.get("work_package_status", {}).get("WP5")
    report["ENG-FIT-08"] = {
        "status": "PASS",
        "row_count": len(rows),
        "applicability": "active" if rows or wp5 not in {"not-started", "ready-next"} else "not-yet-applicable-before-WP5",
    }


def _check_context_profiles(root: Path, errors: list[str], report: dict[str, Any]) -> None:
    checked: list[str] = []
    for profile in sorted(engineering_context.PROFILES):
        context_errors, packet = engineering_context.compile_context(root, profile)
        errors.extend(f"context {profile}: {item}" for item in context_errors)
        if not context_errors:
            adequacy = engineering_context.context_adequacy_errors(packet)
            errors.extend(f"context {profile}: {item}" for item in adequacy)
        checked.append(profile)
    report["ENG-FIT-07"] = {"status": "PASS", "profiles": checked}


def _check_prompt_contract(root: Path, errors: list[str], report: dict[str, Any]) -> None:
    required = [
        root / "engineering" / "prompts" / "CONTRACT.md",
        root / "tools" / "prompt.py",
        root / "tests" / "test_prompt.py",
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        errors.append(f"ENG-FIT-09: activated prompt contract is missing required owners/regressions: {missing}")
    report["ENG-FIT-09"] = {"status": "PASS" if not missing else "FAIL", "required_paths": [str(p.relative_to(root)) for p in required]}


def _check_whole_return(root: Path, errors: list[str], report: dict[str, Any]) -> None:
    state = _load_json(root / "engineering" / "changes" / "SD-KA-01" / "STATE.json")
    result_path = root / "engineering" / "changes" / "SD-KA-01" / "RESULT.md"
    result = result_path.read_text(encoding="utf-8") if result_path.is_file() else ""
    whole_return = str(state.get("whole_system_return", "")).strip()
    if not whole_return:
        errors.append("bounded change state: whole_system_return is required")
    verified = [name for name, status in state.get("work_package_status", {}).items() if status == "verified"]
    for package in verified:
        if f"## {package} " not in result and f"## {package} —" not in result:
            errors.append(f"{result_path}: verified {package} has no durable result/whole-system section")
    report["ENG-FIT-06"] = {"status": "PASS", "verified_packages": verified, "whole_system_return_present": bool(whole_return)}


def run_fitness(root: Path) -> tuple[list[str], dict[str, Any]]:
    errors, contract = validate_fitness_contract(root)
    report: dict[str, Any] = {
        "status": "PASS",
        "contract": "engineering/assurance/fitness.json",
        "work_package": "WP4",
        "checks": {},
    }

    engineering_errors, engineering_summary = engineering.validate(root)
    errors.extend(engineering_errors)
    for check_id in ("ENG-FIT-01", "ENG-FIT-02", "ENG-FIT-03", "ENG-FIT-04"):
        report["checks"][check_id] = {"status": "PASS" if not engineering_errors else "FAIL", "owner": "tools/engineering.py validate"}

    _check_generated_views(root, errors, report["checks"])
    _check_whole_return(root, errors, report["checks"])
    _check_context_profiles(root, errors, report["checks"])
    _check_legacy_paths(root, errors, report["checks"])
    _check_prompt_contract(root, errors, report["checks"])

    report["engineering_summary"] = engineering_summary
    report["fixture_family_count"] = len(contract.get("fixture_families", {})) if contract else 0
    report["non_claims"] = contract.get("non_claims", []) if contract else []
    if errors:
        report["status"] = "FAIL"
    return errors, report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root")
    args = parser.parse_args()
    root = repo_root(args.root)
    try:
        errors, report = run_fitness(root)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ENGINEERING FITNESS FAIL: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(json.dumps(report, indent=2, sort_keys=True))
        return 1
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
