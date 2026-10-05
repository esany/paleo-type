#!/usr/bin/env python3
"""Compile bounded, derived engineering context profiles from repository owners."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    from tools import engineering
except ModuleNotFoundError:  # direct execution from tools/
    import engineering  # type: ignore

PROFILES = {
    "human-system-overview",
    "system-development-execution",
    "architecture-review",
    "human-material-decision",
    "maintenance-review",
}
REVIEW_BASIS_CLASSES = {
    "direct-source-inspection",
    "primary-owner-reinspection",
    "same-evidence-rejudgement",
    "derived-owner-review",
    "independent-external-support",
    "unknown/not-established",
}
ISSUE_REF_RE = re.compile(r"^github-issue:([^/]+)/([^#]+)#(\d+)$")


def repo_root(explicit: str | None = None) -> Path:
    return Path(explicit).resolve() if explicit else Path(__file__).resolve().parents[1]


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_artifact_rows(root: Path) -> list[dict[str, str]]:
    _, rows = engineering.read_tsv(root / "engineering" / "catalog" / "artifacts.tsv")
    return rows


def _load_relation_rows(root: Path) -> list[dict[str, str]]:
    _, rows = engineering.read_tsv(root / "engineering" / "catalog" / "relations.tsv")
    return rows


def _load_finding_rows(root: Path) -> list[dict[str, str]]:
    _, rows = engineering.read_tsv(root / "engineering" / "catalog" / "findings.tsv")
    return rows


def _issue_catalog_path(ref: str) -> str | None:
    match = ISSUE_REF_RE.fullmatch(ref)
    if not match:
        return None
    owner, repo, number = match.groups()
    return f"github://github.com/{owner}/{repo}/issues/{number}"


def _work_artifact(ref: str, artifacts: list[dict[str, str]]) -> dict[str, str] | None:
    catalog_path = _issue_catalog_path(ref)
    if catalog_path is None:
        return None
    for row in artifacts:
        if row.get("path") == catalog_path:
            return row
    return None


def _action_statement(prefix: str, title: str, ref: str) -> str:
    cleaned = title.strip().rstrip(".")
    if not cleaned:
        cleaned = f"work item {ref}"
    return f"{prefix}: {cleaned}."


def _candidate_from_relation(
    relation: dict[str, str], artifacts: list[dict[str, str]], state: dict[str, Any]
) -> dict[str, Any]:
    ref = relation["object_ref"]
    artifact = _work_artifact(ref, artifacts)
    title = artifact.get("title", "") if artifact else ""
    return {
        "state": "ready-next",
        "statement": _action_statement("Next eligible work", title, ref),
        "work_ref": ref,
        "scope": f"{state.get('change_id', 'engineering')}/next-eligible",
        "basis_kind": "work-contract",
        "basis_ref": relation.get("evidence_ref"),
        "catalog_artifact": f"artifact:{artifact['artifact_id']}" if artifact else None,
    }


def resolve_work(
    root: Path,
    config: dict[str, Any],
    state: dict[str, Any],
    artifacts: list[dict[str, str]],
    relations: list[dict[str, str]],
    explicit_work_ref: str | None = None,
) -> dict[str, Any]:
    focus = config.get("current_focus")

    if explicit_work_ref:
        artifact = _work_artifact(explicit_work_ref, artifacts)
        title = artifact.get("title", "") if artifact else ""
        if isinstance(focus, dict) and focus.get("ref") == explicit_work_ref:
            return {
                "state": "active",
                "statement": _action_statement("Current work", title, explicit_work_ref),
                "work_ref": explicit_work_ref,
                "scope": focus.get("scope"),
                "basis_kind": focus.get("basis_kind"),
                "basis_ref": focus.get("basis_ref"),
                "catalog_artifact": f"artifact:{artifact['artifact_id']}" if artifact else None,
                "resolution": "explicit-work-ref-matches-current-focus",
            }
        matching = [
            row
            for row in relations
            if row.get("predicate") == "transitions-to"
            and row.get("relation_status") == "accepted"
            and row.get("object_ref") == explicit_work_ref
        ]
        return {
            "state": "scoped-not-claimed-current",
            "statement": _action_statement("Scoped work", title, explicit_work_ref),
            "work_ref": explicit_work_ref,
            "scope": f"{state.get('change_id', 'engineering')}/explicit-scope",
            "basis_kind": "work-contract" if matching else "candidate/unresolved",
            "basis_ref": matching[0].get("evidence_ref") if matching else None,
            "catalog_artifact": f"artifact:{artifact['artifact_id']}" if artifact else None,
            "resolution": "explicit-work-ref",
        }

    if isinstance(focus, dict):
        ref = str(focus.get("ref", ""))
        artifact = _work_artifact(ref, artifacts)
        title = artifact.get("title", "") if artifact else ""
        return {
            "state": "active",
            "statement": _action_statement("Current work", title, ref),
            "work_ref": ref,
            "scope": focus.get("scope"),
            "basis_kind": focus.get("basis_kind"),
            "basis_ref": focus.get("basis_ref"),
            "catalog_artifact": f"artifact:{artifact['artifact_id']}" if artifact else None,
            "resolution": "configured-current-focus",
        }

    transition_candidates = [
        row
        for row in relations
        if row.get("predicate") == "transitions-to" and row.get("relation_status") == "accepted"
    ]
    active_paths = {row.get("path") for row in artifacts if row.get("lifecycle_state") == "active"}
    transition_candidates = [
        row
        for row in transition_candidates
        if (_issue_catalog_path(row.get("object_ref", "")) in active_paths)
    ]

    candidates = [_candidate_from_relation(row, artifacts, state) for row in transition_candidates]
    if len(candidates) == 1:
        candidate = candidates[0]
        candidate["resolution"] = "single-ready-next-transition"
        return candidate
    if len(candidates) > 1:
        return {
            "state": "ambiguous",
            "statement": "Current work is ambiguous; no repository-global work item was silently selected.",
            "scope": f"{state.get('change_id', 'engineering')}/ambiguous",
            "candidates": candidates,
            "resolution": "multiple-ready-next-transitions",
        }
    return {
        "state": "absent",
        "statement": "No active or next eligible engineering work is explicitly resolved.",
        "scope": f"{state.get('change_id', 'engineering')}/none",
        "resolution": "explicit-absence",
    }


def _review_basis(target: str | None) -> dict[str, Any]:
    return {
        "review_target": target,
        "material_premise": None,
        "basis_class": "unknown/not-established",
        "basis_refs": [],
        "inherited_premises": [
            "The generated context begins from repository owners; generation alone does not re-inspect their underlying evidence."
        ],
        "retested_premises": [],
        "independence_claim": "not-established",
        "remaining_evidence_depth_limit": "A fresh context or second model is not independent evidence merely because it is new.",
        "allowed_basis_classes": sorted(REVIEW_BASIS_CLASSES),
    }


def _unresolved_findings(root: Path) -> list[dict[str, str]]:
    return [
        {
            "finding_id": row["finding_id"],
            "summary": row["summary"],
            "target_ref": row["target_ref"],
            "rationale": row["rationale"],
        }
        for row in _load_finding_rows(root)
        if row.get("disposition") == "unresolved"
    ]


def compile_context(
    root: Path,
    profile: str,
    work_ref: str | None = None,
    changed_ref: str | None = None,
) -> tuple[list[str], dict[str, Any]]:
    if profile not in PROFILES:
        return [f"unknown context profile {profile!r}"], {}

    current_errors, current = engineering.compile_current_state(root)
    if current_errors:
        return current_errors, {}

    engineering_root = root / "engineering"
    config = _load_json(engineering_root / "configuration.json")
    state = _load_json(engineering_root / "changes" / "SD-KA-01" / "STATE.json")
    artifacts = _load_artifact_rows(root)
    relations = _load_relation_rows(root)
    work = resolve_work(root, config, state, artifacts, relations, explicit_work_ref=work_ref)

    packet: dict[str, Any] = {
        "view_kind": "derived-engineering-context",
        "profile": profile,
        "authority": {
            "kind": "derived-only",
            "canonical_owners": [
                "path:GOVERNING_OBJECTIVE.md",
                "path:AGENTS.md",
                "path:engineering/configuration.json",
                "path:engineering/changes/SD-KA-01/STATE.json",
                "path:engineering/catalog/artifacts.tsv",
                "path:engineering/catalog/relations.tsv",
            ],
            "rule": "This context selects and explains canonical/admitted owners; it does not become a parallel truth store.",
        },
        "current_work": work,
        "work_package_status": state.get("work_package_status", {}),
        "applicability": current.get("applicability", []),
        "blocking_uncertainties": state.get("blocking_uncertainties", []),
        "accepted_configuration": current.get("accepted_configuration", {}),
        "active_changes": current.get("active_changes", []),
        "non_claims": current.get("non_claims", []),
        "deeper_provenance": [
            "artifact:ENG-A-0032",
            "artifact:ENG-A-0035",
            "artifact:ENG-A-0036",
            "artifact:ENG-A-0037",
            "artifact:ENG-A-0033",
        ],
    }

    transition_state = None
    if packet["active_changes"]:
        transition_state = packet["active_changes"][0].get("transition_state")

    if profile == "human-system-overview":
        packet["overview"] = {
            "why": "Reduce engineering-state reconstruction and Human relay burden without hiding authority, uncertainty or provenance.",
            "current_or_next_work": work,
            "readiness": state.get("work_package_status", {}),
            "needs_human_decision": transition_state == "needs-decision",
            "material_residuals": _unresolved_findings(root),
            "verification_boundary": current.get("non_claims", []),
            "deeper_evidence": packet["deeper_provenance"],
        }

    elif profile == "system-development-execution":
        packet["execution_contract"] = {
            "requested_activity": "implementation" if work.get("state") == "active" else work.get("state"),
            "purpose": work.get("statement"),
            "scope": work.get("scope"),
            "authority_reads": [
                "path:GOVERNING_OBJECTIVE.md",
                "path:AGENTS.md",
                work.get("work_ref"),
                "artifact:ENG-A-0035",
                "artifact:ENG-A-0036",
                "artifact:ENG-A-0037",
            ],
            "applicable_requirements": current.get("applicability", []),
            "non_goals": state.get("non_goals", []),
            "write_boundary": "Only the already-admitted SD-KA-01 engineering slice may change; Project/manuscript purpose, priority, gate and scholarly NEXT ACTION remain out of scope.",
            "acceptance_refs": [work.get("work_ref"), "artifact:ENG-A-0035", "artifact:ENG-A-0036"],
            "technical_verification": "python tools/check.py",
            "whole_system_return": state.get("programme_owner"),
        }

    elif profile == "architecture-review":
        packet["review_context"] = {
            "accepted_baseline": current.get("accepted_configuration", {}),
            "admitted_change": current.get("active_changes", []),
            "applicability": current.get("applicability", []),
            "residual_findings": _unresolved_findings(root),
        }
        packet["review_evidence_basis"] = _review_basis(work.get("work_ref"))

    elif profile == "human-material-decision":
        needs_decision = transition_state == "needs-decision"
        packet["decision_view"] = {
            "status": "needs-human-material-decision" if needs_decision else "no-new-human-material-decision-required",
            "plain_language": (
                "The active change has reached a material decision boundary; the Human Owner must decide the stated consequence."
                if needs_decision
                else "The current bounded work is already covered by the existing D-016 admission; no new Human approval is created by this derived view."
            ),
            "decision_owner": config.get("decision_owner"),
            "current_or_next_work": work,
            "non_effects": state.get("non_goals", []),
        }

    elif profile == "maintenance-review":
        packet["maintenance_context"] = {
            "changed_ref": changed_ref,
            "changed_ref_state": "provided" if changed_ref else "not-provided",
            "programme_owner": state.get("programme_owner"),
            "propagation_rule": "Update the changed canonical owner first, then only materially affected dependents and restart/navigation surfaces.",
        }
        packet["review_evidence_basis"] = _review_basis(changed_ref or work.get("work_ref"))

    adequacy = context_adequacy_errors(packet)
    if adequacy:
        return adequacy, {}
    return [], packet


def context_adequacy_errors(packet: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    authority = packet.get("authority")
    if not isinstance(authority, dict) or authority.get("kind") != "derived-only":
        errors.append("context starvation: derived authority boundary is missing")

    work = packet.get("current_work")
    if not isinstance(work, dict):
        errors.append("context starvation: current/next work resolution is missing")
    else:
        statement = str(work.get("statement", "")).strip()
        if not statement or statement in {str(work.get("work_ref", "")), str(work.get("state", ""))}:
            errors.append("human-facing work resolution is opaque or missing")
        if work.get("state") in {"active", "ready-next"}:
            if not work.get("scope"):
                errors.append("current/next work scope is missing")
            if not work.get("basis_ref"):
                errors.append("current/next work authority basis is missing")
        if work.get("state") == "ambiguous" and not work.get("candidates"):
            errors.append("ambiguous work resolution must expose candidates")

    applicability = packet.get("applicability")
    if not isinstance(applicability, list):
        errors.append("applicability provenance is missing")
    else:
        for index, entry in enumerate(applicability):
            if not isinstance(entry, dict):
                errors.append(f"applicability[{index}] is not structured")
                continue
            for field in ("ref", "basis_kind", "basis_ref", "scope"):
                if not entry.get(field):
                    errors.append(f"applicability[{index}] lacks {field}")

    profile = packet.get("profile")
    if profile == "system-development-execution":
        execution = packet.get("execution_contract")
        if not isinstance(execution, dict):
            errors.append("execution profile lacks execution contract")
        elif execution.get("technical_verification") != "python tools/check.py":
            errors.append("execution profile must expose the shared full-check entrypoint")

    if profile in {"architecture-review", "maintenance-review"}:
        basis = packet.get("review_evidence_basis")
        required = {
            "review_target",
            "material_premise",
            "basis_class",
            "basis_refs",
            "inherited_premises",
            "retested_premises",
            "independence_claim",
            "remaining_evidence_depth_limit",
        }
        if not isinstance(basis, dict) or not required.issubset(basis):
            errors.append("review profile lacks review-evidence-basis semantics")
        elif basis.get("independence_claim") == "independent" and basis.get("basis_class") == "unknown/not-established":
            errors.append("independence cannot be claimed from an unknown evidence basis")

    return errors


def render_human_cursor(packet: dict[str, Any]) -> str:
    work = packet["current_work"]
    lines = [str(work.get("statement", "")).strip()]
    if work.get("scope"):
        lines.append(f"Scope: {work['scope']}")
    if work.get("work_ref"):
        lines.append(f"Authority/work owner: {work['work_ref']}")
    if work.get("basis_ref"):
        lines.append(f"Resolution basis: {work.get('basis_kind', 'unspecified')} via {work['basis_ref']}")
    if work.get("state") == "ambiguous":
        for candidate in work.get("candidates", []):
            lines.append(f"Candidate: {candidate.get('statement')} [{candidate.get('work_ref')}; basis {candidate.get('basis_ref')}]")
    return "\n".join(line for line in lines if line)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", help="repository root")
    parser.add_argument("--profile", choices=sorted(PROFILES), required=True)
    parser.add_argument("--work-ref", help="explicit scoped work reference; does not manufacture currentness")
    parser.add_argument("--changed-ref", help="changed owner/reference for maintenance-review")
    parser.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args()

    errors, packet = compile_context(
        repo_root(args.root),
        args.profile,
        work_ref=args.work_ref,
        changed_ref=args.changed_ref,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.format == "text":
        print(render_human_cursor(packet))
    else:
        print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
