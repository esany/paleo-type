#!/usr/bin/env python3
"""Reference implementation for the bounded paleo-type .prompt capability."""

from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Any

PALEO_REPOS = {"paleo-type", "esany/paleo-type"}

MINIMALITY_TERMS = re.compile(
    r"(?i)\b(?:lean|minimal|minimality|simplif(?:y|ied|ication)|cleanup|shortcut|quick fix|cheap(?:er)?|small(?:er)? patch)\b"
)
LOCAL_FIRST_VIOLATION = re.compile(
    r"(?i)(?:develop|work|save|stage|keep|use|create|run).{0,40}(?:locally|local checkout|worktree|clone|uncommitted|local git)|(?:push|transfer|copy).{0,30}later"
)
CONNECTOR_FAILURE_LOCAL_FALLBACK = re.compile(
    r"(?i)(?:connector|github).{0,80}(?:fail|unavailable|error).{0,80}(?:local|worktree|clone|checkout|save|push)|(?:local|worktree|clone|checkout|save).{0,80}(?:connector|github).{0,80}(?:fail|unavailable|error)"
)
PREMATURE_CLOSURE = re.compile(
    r"(?i)(?:local|technical|unit|ci|github|issue|pr|work package).{0,60}(?:pass|green|closed|done|complete).{0,60}(?:means|proves|establishes|therefore|so|enough|accept|close)"
)
_ADEQUACY_MARKERS = (
    r"(?i)\b(?:user|research) (?:outcome|pain|need)\b",
    r"(?i)\broot cause\b",
    r"(?i)\b(?:affected )?owner(?: chain|s)?\b",
    r"(?i)\b(?:invariant|distinction)s?\b",
    r"(?i)\b(?:evidence|acceptance|accept(?:ed)? criteria|dod)\b",
    r"(?i)\bnon[- ]goal(?:s)?\b",
    r"(?i)\b(?:counter[- ]extreme|opposite extreme)\b",
    r"(?i)\b(?:whole[- ]system|return condition)\b",
)
_EXECUTION_PROOF_MARKERS = (
    "current main commit",
    "working branch or pr",
    "remote branch and commit",
    "restartability",
    "handoff",
    "affected canonical owner",
    "connector",
    "stop",
)
ADEQUACY_GUARDRAIL = """Adequacy before minimality:
Treat lean/minimal/simplified implementation as a conclusion, not a starting assumption. Before taking a shortcut, state the user/research outcome or pain, root cause, affected owner chain, required invariants and semantic distinctions, evidence and acceptance condition, non-goals, counter-extreme check, whole-system return condition and residual uncertainty. A smaller diff, local/CI PASS, fewer workflow steps or completed work package is not proof of root-cause resolution or user acceptance. Keep work-package completion, root-cause resolution and user acceptance distinct. If this evidence is missing, return the material decision instead of silently implementing the shortcut."""
ONLINE_EXECUTION_GUARDRAIL = """Repository-first execution and proof gate:
Before consequential repository work, freshly resolve the current main commit, applicable owner/current task, intended working branch or PR, bounded scope, DOR, DOD and STOP criteria through the authorized GitHub connector. Use the authorized GitHub connector exclusively: do not clone, create or use a local checkout/worktree, run local Git, or save repository state for later promotion. After every mutation, verify the remote repository path, branch and commit and record the exact remote commit as the durable work cursor. Before handoff, status or completion, prove fresh-context restartability, reconcile every materially affected canonical owner, and state residuals and non-changes. Technical/CI PASS, Issue closure, PR status and work-package completion are not automatic user or whole-system acceptance. If connector, permission, remote-write, branch-verification, restart or owner-reconciliation proof fails, stop and do not fall back locally or silently downgrade the work."""
def _has_adequacy_contract(text: str) -> bool:
    return sum(bool(re.search(pattern, text)) for pattern in _ADEQUACY_MARKERS) >= 6
def _has_execution_proof_contract(text: str) -> bool:
    lowered = text.lower()
    return sum(marker in lowered for marker in _EXECUTION_PROOF_MARKERS) >= 7



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

{ONLINE_EXECUTION_GUARDRAIL}

{ADEQUACY_GUARDRAIL}

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

    if LOCAL_FIRST_VIOLATION.search(improved):
        issues.append("local-first repository violation: use the authorized GitHub connector directly; do not stage repository work locally or push later")
        if "authorized GitHub connector" not in improved:
            improved = improved.rstrip() + "\n\n" + ONLINE_EXECUTION_GUARDRAIL

    if CONNECTOR_FAILURE_LOCAL_FALLBACK.search(improved):
        issues.append("connector failure cannot be routed to local staging or a later push")
        if "authorized GitHub connector" not in improved:
            improved = improved.rstrip() + "\n\n" + ONLINE_EXECUTION_GUARDRAIL

    if MINIMALITY_TERMS.search(improved) and not _has_adequacy_contract(improved):
        issues.append("lean/minimality shortcut lacks adequacy evidence: require outcome, root cause, owner chain, invariants, acceptance and whole-system return")
        if "Adequacy before minimality" not in improved:
            improved = improved.rstrip() + "\n\n" + ADEQUACY_GUARDRAIL

    if PREMATURE_CLOSURE.search(improved):
        issues.append("status laundering: local/technical/CI/Issue/PR completion cannot establish user or whole-system acceptance")
        if "ONLINE_EXECUTION_GUARDRAIL" not in improved:
            improved = improved.rstrip() + "\n\n" + ONLINE_EXECUTION_GUARDRAIL

    if _is_paleo_repo(repo):
        if not _has_execution_proof_contract(improved):
            issues.append("missing online execution proof gate: require current main, intended branch/PR, remote commit, restart/handoff and affected-owner reconciliation")
            improved = improved.rstrip() + "\n\n" + ONLINE_EXECUTION_GUARDRAIL

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
    if LOCAL_FIRST_VIOLATION.search(text):
        findings.append("local-first-repository-violation")
    if CONNECTOR_FAILURE_LOCAL_FALLBACK.search(text):
        findings.append("connector-failure-local-fallback")
    if MINIMALITY_TERMS.search(text) and not _has_adequacy_contract(text):
        findings.append("lean-shortcut-without-adequacy")
    if (
        re.search(r"(?i)\b(?:local|technical|ci|unit)\b.{0,80}\bpass\b", text)
        and not re.search(r"(?i)whole[- ]system|root cause resolved|user accepted|return condition", text)
    ):
        findings.append("local-pass-without-whole-system-return")
    if PREMATURE_CLOSURE.search(text):
        findings.append("premature-closure-laundering")
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
