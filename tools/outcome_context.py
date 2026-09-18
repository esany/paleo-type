#!/usr/bin/env python3
"""Compile a read-only Outcome Control Context from canonical paleo-type state.

This tool is a derived integration surface. It does not own or write Project
purpose/scope, scholarly NEXT ACTION, gate attainment, requirement applicability
or research conclusions. Stable repository facts and requirement metadata are
resolved mechanically; open semantic binding remains explicit for AI, specialist
or Human-Owner judgement.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

import project_context
import source_contract


NO_AUTHORITY_TERMS = ("scope", "task", "target", "action")


def load_requirements(root: Path) -> dict[str, dict[str, str]]:
    path = root / "requirements" / "domain-requirements.tsv"
    with path.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))

    requirements: dict[str, dict[str, str]] = {}
    for row in rows:
        requirement_id = row.get("requirement_id", "")
        if not requirement_id:
            continue
        if requirement_id in requirements:
            raise ValueError(f"duplicate requirement_id {requirement_id}")
        requirements[requirement_id] = row
    return requirements


def explicit_no_outcome_evidence(context: dict) -> list[dict[str, str]]:
    surfaces = [
        ("project.yml:active_scope", context.get("project_definition", {}).get("active_scope", "")),
        (
            context.get("canonical_status", {}).get("path", "STATUS.md"),
            context.get("canonical_status", {}).get("text", ""),
        ),
    ]
    evidence: list[dict[str, str]] = []
    for owner, text in surfaces:
        for line in text.splitlines():
            normalized = line.strip().casefold()
            if "no owner-selected" not in normalized:
                continue
            if not any(term in normalized for term in NO_AUTHORITY_TERMS):
                continue
            evidence.append({"owner": owner, "statement": line.strip()})
    return evidence


def requirement_view(row: dict[str, str]) -> dict[str, str]:
    return {
        "requirement_id": row.get("requirement_id", ""),
        "domain": row.get("domain", ""),
        "requirement": row.get("requirement", ""),
        "validation_mode": row.get("validation_mode", ""),
        "specialist_trigger": row.get("specialist_trigger", ""),
        "current_support": row.get("current_support", ""),
        "source_issue": row.get("source_issue", ""),
        "architecture_handoff": row.get("architecture_handoff", ""),
    }


def compile_outcome_context(
    root: Path,
    project_id: str | None = None,
    requested_outcome: str | None = None,
    requirement_ids: list[str] | None = None,
) -> tuple[int, dict]:
    try:
        requirements = load_requirements(root)
    except (OSError, ValueError) as exc:
        return 1, {"status": "ERROR", "error": str(exc)}

    requirement_ids = requirement_ids or []
    unknown_requirements = sorted({rid for rid in requirement_ids if rid not in requirements})
    if unknown_requirements:
        return 3, {
            "status": "ERROR",
            "error": "unknown requirement_id",
            "requirement_ids": unknown_requirements,
        }

    selected_requirements = [requirement_view(requirements[rid]) for rid in requirement_ids]
    domain_counts: dict[str, int] = {}
    for row in requirements.values():
        domain = row.get("domain", "")
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

    base = {
        "status": "OK",
        "view": "DERIVED_OUTCOME_CONTROL_CONTEXT",
        "canonical": False,
        "requested_outcome": requested_outcome,
        "canonical_references": {
            "requirements": "requirements/domain-requirements.tsv",
            "governing": [
                "GOVERNING_OBJECTIVE.md",
                "AGENTS.md",
                "methodology/historical-source-workflow.md",
                "methodology/research-gates.md",
                "methodology/project-lifecycle.md",
                "methodology/workflow.md",
                "methodology/maintenance.md",
                "methodology/ai-governance.md",
            ],
        },
        "requirement_resolution": {
            "selected": selected_requirements,
            "selection_status": "SELECTED_REQUIREMENTS_RESOLVED" if selected_requirements else "NO_REQUIREMENTS_SELECTED",
            "available_domain_counts": dict(sorted(domain_counts.items())),
            "applicability_boundary": (
                "Requirement metadata is deterministic once a requirement is selected. "
                "Applicability to a concrete scholarly outcome is not inferred here unless fixed by an existing formal owner."
            ),
        },
        "responsibility_boundary": {
            "deterministic": "canonical identity/state references, structured requirement metadata and explicit authority absence",
            "ai_assisted": "outcome semantic binding, open requirement applicability and bounded scholarly work composition",
            "specialist": "qualified validation where an applicable requirement or METHOD trigger requires it",
            "human_owner": "new/changed purpose, priority, material scope, unresolved authority and D-016 admission",
        },
        "completion_boundary": {
            "local_result_establishes_whole_outcome": False,
            "whole_outcome_completion": "NOT_DERIVED",
            "rule": "Local task/support/technical PASS never establishes whole-outcome completion by itself.",
        },
        "work_proposal": {
            "generated_next_action": None,
            "generation_policy": "This deterministic view never manufactures scholarly NEXT ACTION or priority.",
        },
    }

    if not project_id:
        base.update(
            {
                "project_id": None,
                "project_context": None,
                "authority_binding": {
                    "status": "NO_PROJECT",
                    "work_generation_allowed": False,
                    "basis": "No Project was supplied; Corpus/source structure alone cannot create Project authority.",
                },
                "outcome_disposition": {
                    "status": "NO_PROJECT",
                    "continuation": "NO_PROJECT_WORK",
                },
            }
        )
        return 0, base

    rc, context = project_context.compile_project_context(root, project_id)
    if rc:
        return rc, context

    absence_evidence = explicit_no_outcome_evidence(context)
    if absence_evidence:
        binding_status = "HUMAN_AUTHORITY_REQUIRED" if requested_outcome else "NO_AUTHORIZED_OUTCOME_RECORDED"
        binding_basis = (
            "Canonical Project state explicitly records that no owner-selected current scholarly scope/task/target/action exists."
        )
        disposition = "OWNER_DECISION_REQUIRED" if requested_outcome else "NO_AUTHORIZED_OUTCOME"
    elif requested_outcome:
        binding_status = "SEMANTIC_BINDING_REQUIRES_REASONING"
        binding_basis = (
            "No explicit absence marker was found, but absence of such a marker is not proof that the requested outcome is authorized."
        )
        disposition = "REQUIRES_REASONING"
    else:
        binding_status = "OUTCOME_NOT_REQUESTED_OR_NOT_DERIVED"
        binding_basis = "This tool does not derive a scholarly outcome from Project/evidence structure."
        disposition = "REQUIRES_OUTCOME_OR_REASONING"

    base["canonical_references"]["project_context"] = context.get("canonical_references", {})
    base.update(
        {
            "project_id": project_id,
            "project_context": context,
            "authority_binding": {
                "status": binding_status,
                "work_generation_allowed": False,
                "basis": binding_basis,
                "explicit_absence_evidence": absence_evidence,
                "binding_rule": (
                    "The tool may prove an explicit absence from canonical owner statements, "
                    "but it never treats lack of an absence marker as positive authorization."
                ),
            },
            "outcome_disposition": {
                "status": disposition,
                "continuation": "NO_DETERMINISTIC_WORK_GENERATION",
            },
        }
    )
    return 0, base


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile a rebuildable read-only outcome control context over existing canonical owners."
    )
    parser.add_argument("--project", help="Existing Project ID. Omit for a legitimate no-Project/Corpus-only context.")
    parser.add_argument("--outcome", help="Ordinary-language requested scholarly outcome; never treated as authorization by itself.")
    parser.add_argument(
        "--requirement",
        action="append",
        default=[],
        help="Requirement ID selected by an upstream scholarly/AI applicability step; repeat as needed.",
    )
    parser.add_argument("--root", help="Repository root; defaults to the script's repository.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = source_contract.repo_root(args.root)
    rc, result = compile_outcome_context(root, args.project, args.outcome, args.requirement)
    stream = sys.stderr if rc else sys.stdout
    print(json.dumps(result, ensure_ascii=False, indent=2), file=stream)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
