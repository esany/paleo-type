#!/usr/bin/env python3
"""Reference implementation for the bounded paleo-type .prompt capability."""

from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Any

PALEO_REPOS = {"paleo-type", "esany/paleo-type"}


def _is_paleo_repo(repo: str | None) -> bool:
    return bool(repo and repo.strip().lower() in PALEO_REPOS)


def build_prompt(task: str, repo: str | None = None) -> str:
    task = task.strip()
    if not task:
        raise ValueError("task must not be empty")

    if not _is_paleo_repo(repo):
        return (
            f"Task: {task}\n\n"
            "Preserve the requested purpose and scope. Use only the context needed for the task, "
            "state material uncertainty rather than inventing facts, and return the requested output directly."
        )

    return f"""Work in `esany/paleo-type` on this bounded task:

{task}

Before consequential work, freshly read `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, the applicable current task/Project owner, and every canonical rule/requirement needed for this task. Resolve current authority/state from repository owners rather than old chat, filename dates, Issue order, Git recency or CI.

Stay inside already-authorized scope. Do not create or change Project purpose/priority/scholarly `NEXT ACTION`, Human-owner authority, or D-016 admission unless the task is explicitly at that authority boundary. If a genuinely new material choice appears, return it instead of silently absorbing it.

Use complete applicable context, not `read everything`; keep deeper provenance reachable on demand. Persist restart-relevant results repository-first in the actual canonical owner or working branch. Treat technical/CI PASS as only the properties actually checked.

For consequential review, state the review evidence basis, what remained inherited, what was re-tested, and any evidence-depth limit. A fresh context or second model is not independent evidence merely because it is new.

When repository semantics/code change, run `python tools/check.py`. Finish by stating the actual state change, deliberate non-changes, residual limits, and any required whole-system/programme return to the existing owner.
""".strip()


def review_prompt(prompt: str, repo: str | None = None) -> dict[str, Any]:
    original = prompt.strip()
    if not original:
        raise ValueError("prompt must not be empty")

    issues: list[str] = []
    improved = original

    open_read_patterns = [
        r"(?i)read everything",
        r"(?i)read the (?:entire|whole) repo(?:sitory)?",
        r"(?i)load everything",
    ]
    if any(re.search(pattern, improved) for pattern in open_read_patterns):
        issues.append("open read scope: replace indiscriminate repository loading with applicable canonical-owner discovery")
        improved = re.sub(r"(?i)read everything", "read only the canonical owners applicable to the task", improved)
        improved = re.sub(
            r"(?i)read the (?:entire|whole) repo(?:sitory)?",
            "read only the canonical owners applicable to the task",
            improved,
        )
        improved = re.sub(r"(?i)load everything", "load only context applicable to the task", improved)

    if re.search(r"(?i)(?:implement|continue|work) until done", improved):
        issues.append("non-closable work: replace open-ended execution with an explicit bounded completion/return condition")
        improved = re.sub(
            r"(?i)(?:implement|continue|work) until done",
            "execute only the authorized bounded task and stop at its explicit completion/return condition",
            improved,
        )

    if re.search(r"(?i)latest (?:file|issue|commit|design|architecture)", improved):
        issues.append("latest-wins pressure: repository recency must not be treated as semantic authority")

    if re.search(r"(?i)(independent review|independent evidence)", improved):
        issues.append("independence claim must be supported by the actual review evidence basis, not context/model freshness")

    if _is_paleo_repo(repo):
        prefix = (
            "Freshly resolve `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, the applicable current owner and canonical rules before consequential work. "
            "Do not manufacture Project priority, D-016 authority or acceptance from Issue/CI/current-context metadata.\n\n"
        )
        if "GOVERNING_OBJECTIVE.md" not in improved or "AGENTS.md" not in improved:
            issues.append("missing paleo-type authority bootstrap: add fresh governing/current-owner resolution")
            improved = prefix + improved
        if "tools/check.py" not in improved:
            issues.append("missing shared full-check entrypoint for repository semantic/code changes")

    return {
        "status": "copy-ready" if not issues else "copy-ready-with-material-corrections",
        "issues": issues,
        "prompt": improved,
        "authority": "review output does not change the supplied prompt's purpose/scope/authority",
    }


def test_prompt(prompt: str, result: str | None = None, self_review: bool = False) -> dict[str, Any]:
    text = prompt.strip()
    if not text:
        raise ValueError("prompt must not be empty")

    findings: list[str] = []
    if re.search(r"(?i)read everything|read the (?:entire|whole) repo(?:sitory)?|load everything", text):
        findings.append("open-read-scope")
    if re.search(r"(?i)(?:implement|continue|work) until done", text):
        findings.append("non-closable-work")
    if re.search(r"(?i)latest (?:file|issue|commit|design|architecture)", text):
        findings.append("latest-wins-authority-risk")
    if re.search(r"(?i)(?:automatically )?(?:admit|approve|accept) (?:the )?(?:architecture|change|project)", text):
        findings.append("authority-laundering-risk")

    independence = "not-independent-self-review" if self_review else "not-established"
    if result and re.search(r"(?i)independent(?:ly)? (?:validated|verified|reviewed)", result):
        findings.append("independence-overclaim")

    return {
        "status": "PASS" if not findings else "NEEDS_REVIEW",
        "findings": findings,
        "review_evidence_basis": {
            "basis_class": "same-evidence-rejudgement" if self_review else "unknown/not-established",
            "independence_claim": independence,
            "note": "This deterministic prompt test is not independent scholarly/specialist proof.",
        },
        "demonstrates": "bounded deterministic failure-pattern evaluation only",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    create = subparsers.add_parser("create", help=".prompt <task>")
    create.add_argument("task")
    create.add_argument("--repo")

    review = subparsers.add_parser("review", help=".prompt review <prompt>")
    review.add_argument("prompt")
    review.add_argument("--repo")

    test = subparsers.add_parser("test", help=".prompt test <prompt/result/context>")
    test.add_argument("prompt")
    test.add_argument("--result")
    test.add_argument("--self-review", action="store_true")

    args = parser.parse_args()
    try:
        if args.command == "create":
            print(build_prompt(args.task, args.repo))
            return 0
        if args.command == "review":
            reviewed = review_prompt(args.prompt, args.repo)
            print(reviewed["prompt"])
            if reviewed["issues"]:
                print("\nMaterial corrections:", file=sys.stderr)
                for issue in reviewed["issues"]:
                    print(f"- {issue}", file=sys.stderr)
            return 0
        tested = test_prompt(args.prompt, args.result, args.self_review)
        print(json.dumps(tested, indent=2, sort_keys=True))
        return 0 if tested["status"] == "PASS" else 1
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
