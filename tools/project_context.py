#!/usr/bin/env python3
"""Compile a read-only restart context from canonical paleo-type state.

The output is rebuildable derived state. It deliberately does not infer a
scholarly NEXT ACTION, research function, Project purpose, evidence access or
authority that is not already represented by canonical owners.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import source_contract
import source_intake


def compile_project_context(root: Path, project_id: str) -> tuple[int, dict]:
    errors, warnings, cache = source_contract.validate(root, source_contract.load_contract(root))
    if errors:
        return 1, {"status": "ERROR", "errors": errors, "warnings": warnings}

    project = cache["projects"].get(project_id)
    if not project:
        return 2, {"status": "ERROR", "error": f"project {project_id} has no valid project.yml"}

    project_dir = root / "projects" / project_id
    status_name = project.get("canonical_status_file", "STATUS.md")
    status_path = project_dir / status_name
    if not status_path.is_file():
        return 2, {"status": "ERROR", "error": f"canonical status file is missing: {status_path}"}

    root_id = project.get("project_source_id", "")
    internal_sources = []
    for source_id, source in cache["sources"].items():
        if root_id and source_contract.is_within(source_id, root_id, cache["parents_by_source"]):
            internal_sources.append(source)
    internal_sources.sort(key=lambda row: row.get("source_id", ""))

    evidence_files = []
    internal_ids = {row.get("source_id", "") for row in internal_sources}
    for file_row in cache["files"].values():
        if file_row.get("source_id", "") in internal_ids:
            evidence_files.append(
                {
                    "file": file_row,
                    "evidence_readiness": source_intake.evidence_readiness(root, file_row),
                }
            )
    evidence_files.sort(key=lambda row: row["file"].get("file_id", ""))

    target_uses = []
    for (pid, sid), rows in cache["uses_by_project_source"].items():
        if pid != project_id:
            continue
        for use in rows:
            target_uses.append(
                {
                    "use": use,
                    "evidence": [
                        {
                            "evidence": evidence,
                            "file": cache["files"].get(evidence.get("file_id", "")),
                        }
                        for evidence in cache["evidence_by_use"].get(use.get("use_id", ""), [])
                    ],
                }
            )

    legacy_uses = [
        row
        for (pid, _), row in cache["project_sources"].items()
        if pid == project_id
    ]

    return 0, {
        "status": "OK",
        "view": "DERIVED_PROJECT_CONTEXT",
        "canonical": False,
        "project_id": project_id,
        "governing_sources": [
            "GOVERNING_OBJECTIVE.md",
            "AGENTS.md",
            "DECISIONS.md",
            "methodology/historical-source-workflow.md",
            "methodology/project-lifecycle.md",
            "methodology/source-and-provenance.md",
            f"projects/{project_id}/project.yml",
            f"projects/{project_id}/{status_name}",
        ],
        "project_definition": project,
        "documentary_anchor": cache["sources"].get(root_id),
        "internal_sources": internal_sources,
        "project_source_uses": target_uses,
        "legacy_project_source_uses": legacy_uses,
        "internal_source_files": evidence_files,
        "canonical_status": {
            "path": f"projects/{project_id}/{status_name}",
            "text": status_path.read_text(encoding="utf-8"),
        },
        "execution_boundary": {
            "do_not_infer": [
                "Project existence or purpose from Source/File structure",
                "research_function from structural containment",
                "current scholarly NEXT ACTION from historical work, active evidence or legacy labels",
                "research-ready evidence availability from identity/reproducibility alone",
                "scholarly readings or interpretations from deterministic structure",
            ],
            "note": "Use canonical STATUS for current/restart state. If STATUS records no authorized NEXT ACTION, this derived context must not invent one.",
        },
        "warnings": warnings,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compile rebuildable project restart context from canonical repository state.")
    parser.add_argument("--project", required=True)
    parser.add_argument("--root", help="Repository root; defaults to the script's repository.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = source_contract.repo_root(args.root)
    rc, result = compile_project_context(root, args.project)
    stream = sys.stderr if rc else sys.stdout
    print(json.dumps(result, ensure_ascii=False, indent=2), file=stream)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
