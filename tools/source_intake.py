#!/usr/bin/env python3
"""Read-only intake routing over the canonical paleo-type source contract.

This adapter derives only deterministic facts from an exact supplied file:
SHA-256 identity, an exact canonical File match, its canonical Source, existing
crosswalk presence, structural Project containment and the part of evidence
availability that canonical File state can actually establish. It never creates
or selects a Project, Source relation, research_function, rights interpretation,
external-access claim, target-context staging state or scholarly priority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import source_contract


def evidence_readiness(root: Path, file_row: dict[str, str]) -> dict:
    """Report only evidence facts derivable from canonical File state.

    A repo-preserved File can establish that exact verified bytes exist at a
    project-visible filesystem path. It cannot establish that another/fresh
    work context has received the object, can open it, or (for visual research)
    can inspect its pixels. Action-specific research readiness therefore remains
    NOT_ESTABLISHED until the target context proves the required staging/access.
    """
    storage = file_row.get("storage_status", "")
    repository_path = file_row.get("repository_path", "")
    verified_local_bytes = bool(storage == "repo-preserved" and repository_path)
    access_path = str((root / repository_path).resolve()) if verified_local_bytes else None

    if verified_local_bytes:
        basis = (
            "source-contract establishes exact SHA-verified repository bytes at the recorded path; "
            "this does not establish delivery/staging into the target work context or visual inspectability"
        )
    else:
        basis = (
            "canonical File identity/storage state does not establish local exact bytes for this repository context; "
            "external/institutional retrieval or controlled persistence must be verified separately, and any retrieved "
            "object must still be staged/inspectable in the target context when the task requires it"
        )

    return {
        "identifiable": True,
        "verified_local_bytes": verified_local_bytes,
        "repository_available": verified_local_bytes,
        "access_path": access_path,
        "target_context_staged": "NOT_ASSESSED",
        "vision_inspectable": "NOT_ASSESSED",
        "research_ready_now": "NOT_ESTABLISHED",
        "basis": basis,
    }


def inspect_file(root: Path, file_path: Path) -> tuple[int, dict]:
    if not file_path.is_file():
        return 2, {"status": "ERROR", "error": f"input file does not exist: {file_path}"}

    errors, warnings, cache = source_contract.validate(root, source_contract.load_contract(root))
    if errors:
        return 1, {"status": "ERROR", "errors": errors, "warnings": warnings}

    digest = hashlib.sha256(file_path.read_bytes()).hexdigest()
    exact_matches = [row for row in cache["files"].values() if row.get("sha256") == digest]

    if not exact_matches:
        return 0, {
            "status": "UNRESOLVED_FILE",
            "sha256": digest,
            "exact_file_match": None,
            "source": None,
            "structurally_containing_projects": [],
            "crosswalk_available": False,
            "evidence_readiness": {
                "identifiable": False,
                "verified_local_bytes": False,
                "repository_available": False,
                "access_path": None,
                "target_context_staged": "NOT_ASSESSED",
                "vision_inspectable": "NOT_ASSESSED",
                "research_ready_now": "NOT_ESTABLISHED",
                "basis": "exact canonical File identity is unresolved",
            },
            "project_routing": {
                "requires_explicit_decision": True,
                "allowed_outcomes": ["existing-project", "candidate-new-project", "corpus-only"],
                "note": "No exact canonical File match. Do not infer Source identity, crosswalk applicability, Project membership or research function from filename, page count, OCR, visual similarity or chat context.",
            },
            "human_or_scholarly_questions": [
                "Which historical Source does this distinct/unresolved File instantiate, if currently knowable?",
                "What rights/access facts apply where they cannot be independently verified?",
                "After Source identity is established: existing Project, candidate new Project, or Corpus-only?",
            ],
            "warnings": warnings,
        }

    if len(exact_matches) > 1:
        return 1, {
            "status": "ERROR",
            "sha256": digest,
            "error": "multiple canonical File rows carry the same exact SHA-256; canonical File identity is ambiguous",
            "file_matches": exact_matches,
            "warnings": warnings,
        }

    file_row = exact_matches[0]
    source_id = file_row.get("source_id", "")
    source_row = cache["sources"].get(source_id)
    containing_projects = source_contract.source_projects(
        source_id, cache["projects"], cache["parents_by_source"]
    )

    result = {
        "status": "EXACT_FILE_MATCH",
        "sha256": digest,
        "exact_file_match": file_row,
        "source": source_row,
        "structurally_containing_projects": containing_projects,
        "crosswalk_available": source_id in cache["crosswalks"],
        "evidence_readiness": evidence_readiness(root, file_row),
        "project_routing": {
            "requires_explicit_decision": True,
            "allowed_outcomes": ["existing-project", "candidate-new-project", "corpus-only"],
            "note": "Structural containment is deterministic context only. It does not mean this File/Source is currently used by a Project, does not choose research_function, and does not select the current scholarly NEXT ACTION.",
        },
        "human_or_scholarly_questions": [
            "Should this established Source/File be used in an existing Project, be considered for a new purpose-established Project, or remain Corpus-only?",
            "If used by a Project, what evidenced research function and relevant locus does it serve?",
            "If direct inspection is required, has the exact evidence actually been staged/opened in the target context, and for visual work is it vision-inspectable there?",
        ],
        "warnings": warnings,
    }
    return 0, result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect an exact supplied file against canonical Source/File/Project state without mutating it."
    )
    parser.add_argument("file", help="Local/working file to hash and inspect.")
    parser.add_argument("--root", help="Repository root; defaults to the script's repository.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = source_contract.repo_root(args.root)
    rc, result = inspect_file(root, Path(args.file).resolve())
    stream = sys.stderr if rc and result.get("status") == "ERROR" else sys.stdout
    print(json.dumps(result, ensure_ascii=False, indent=2), file=stream)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
