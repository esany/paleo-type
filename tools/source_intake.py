#!/usr/bin/env python3
"""Read-only intake routing over the canonical paleo-type source contract.

This adapter derives only deterministic facts from an exact supplied file:
SHA-256 identity, an exact canonical File match, its canonical Source, existing
crosswalk presence and Projects whose documentary roots structurally contain
that Source. It never creates or selects a Project, Source relation,
research_function, rights interpretation or scholarly priority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import source_contract


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
        "project_routing": {
            "requires_explicit_decision": True,
            "allowed_outcomes": ["existing-project", "candidate-new-project", "corpus-only"],
            "note": "Structural containment is deterministic context only. It does not mean this File/Source is currently used by a Project, does not choose research_function, and does not select the current scholarly NEXT ACTION.",
        },
        "human_or_scholarly_questions": [
            "Should this established Source/File be used in an existing Project, be considered for a new purpose-established Project, or remain Corpus-only?",
            "If used by a Project, what evidenced research function and relevant locus does it serve?",
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
