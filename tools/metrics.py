#!/usr/bin/env python3
"""P0 (#353): measure repository overhead and reject unapproved evidence additions.

The #353 historical size comparison used wc -c (bytes), not Unicode characters.
Token counts here are rough estimates, not tokenizer measurements.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "engineering/evidence/"


def size(root: Path, dirname: str) -> tuple[int, int]:
    chars = byte_count = 0
    for path in (root / dirname).rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        if any(p in {"__pycache__", ".git"} for p in path.parts) or path.suffix == ".pyc":
            continue
        content = path.read_bytes()
        chars += len(content.decode("utf-8", errors="replace"))
        byte_count += len(content)
    return chars, byte_count


def explained(body: str, heading: str) -> bool:
    for line in body.splitlines():
        if line.strip().casefold().startswith(heading.casefold() + ":"):
            reason = line.split(":", 1)[1].strip()
            return len(reason.split()) >= 4 and reason[-1:] in (".", "!", "?")
    return False


def rejected(context: dict) -> list[str]:
    files = context.get("files", [])
    labels = set(context.get("labels", []))
    body = context.get("body") or ""
    added = [
        f["filename"] for f in files
        if f["filename"].startswith(PREFIX)
        and (
            f["status"] in ("added", "copied")
            or (f["status"] == "renamed"
                and not f.get("previous_filename", "").startswith(PREFIX))
        )
    ]
    errors = []
    if added and (
        "verfahren-ausnahme" not in labels
        or not explained(body, "Verfahrens-Ausnahme")
    ):
        errors.append(
            "BLOCKED: new engineering/evidence/ files require label "
            "'verfahren-ausnahme' and a PR-body sentence headed "
            "'Verfahrens-Ausnahme: '. Files: " + ", ".join(added)
        )
    engineering = sum(
        int(f.get("additions", 0)) for f in files
        if f["filename"].startswith("engineering/")
    )
    projects = sum(
        int(f.get("additions", 0)) for f in files
        if f["filename"].startswith("projects/")
    )
    if engineering and 2 * engineering > projects and not explained(body, "Verfahrensanteil"):
        errors.append(
            "BLOCKED: engineering additions exceed 1:2 versus projects; "
            "add one PR-body sentence headed 'Verfahrensanteil: '."
        )
    return errors


def report(root: Path, context: dict | None, errors: list[str]) -> str:
    ec, eb = size(root, "engineering")
    pc, pb = size(root, "projects")
    agents = (root / "AGENTS.md").read_text(encoding="utf-8")
    issue_count = context.get("open_issues") if context else None
    drafts = context.get("draft_prs") if context else None
    files = context.get("files", []) if context else []
    eng_added = sum(int(f.get("additions", 0)) for f in files if f["filename"].startswith("engineering/"))
    prj_added = sum(int(f.get("additions", 0)) for f in files if f["filename"].startswith("projects/"))
    value = lambda n: "nicht geprüft" if n is None else str(n)
    lines = [
        "## P0 / #353 — Messwerte (keine wissenschaftliche Qualitätsmessung)",
        "",
        "| Messwert | Stand | Ziel aus #353 |",
        "|---|---:|---|",
        f"| engineering : projects (Zeichen) | {ec / pc:.2f}:1 ({ec:,} : {pc:,}) | ≤ 1:2 bei neuen Zeilen |" if pc else
        "| engineering : projects (Zeichen) | nicht berechenbar | ≤ 1:2 bei neuen Zeilen |",
        f"| engineering / projects (Bytes, wc -c) | {eb:,} / {pb:,} | historisch ≈ 2,7:1 |",
        f"| AGENTS.md, grobe Token-Schätzung (Zeichen / 4) | ≈ {round(len(agents) / 4):,} | ≤ 2.500 ab P1 |",
        f"| Offene Issues insgesamt (keine Verfahrensklassifizierung) | {value(issue_count)} | Verfahrens-Issues ≤ 5 nach P3 |",
        f"| Offene PR-Entwürfe insgesamt | {value(drafts)} | P3 ordnet sie |",
        f"| Neue Zeilen engineering / projects in diesem PR | {eng_added} / {prj_added} | ≤ 1:2 oder Begründung |",
        "| Eingriffe des Eigentümers | nicht gezählt | sinkend bei gleicher Forschungsqualität |",
        "",
        "Die Pflichtlektüre über AGENTS.md hinaus hängt vom konkreten Auftrag ab. "
        "Die Tokenzahl ist keine exakte Tokenizer-Zählung. "
        "Offene Verfahrens-Issues werden erst in P3 klassifiziert.",
        "",
        "**P0 CI-Sperre:** " + ("ROT" if errors else "GRÜN"),
    ]
    lines.extend("- " + e for e in errors)
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--context", help="GitHub-PR-Daten aus dem CI-Lauf (JSON)")
    parser.add_argument("--negative-control", action="store_true")
    parser.add_argument("--positive-control", action="store_true")
    args = parser.parse_args()
    if args.negative_control or args.positive_control:
        context = {
            "files": [{"filename": "engineering/evidence/audits/negative-fixture.md",
                       "status": "added", "additions": 1}],
            "labels": ["verfahren-ausnahme"] if args.positive_control else [],
            "body": (
                "Verfahrens-Ausnahme: Dies ist nur eine technische Gegenprobe.\n"
                "Verfahrensanteil: Diese Testdatei dient ausschließlich als Gegenprobe."
            ) if args.positive_control else "",
        }
        errors = rejected(context)
        for e in errors:
            print(e, file=sys.stderr)
        return 1 if errors else 0

    context = json.loads(Path(args.context).read_text(encoding="utf-8")) if args.context else None
    errors = rejected(context) if context is not None else []
    output = report(ROOT, context, errors)
    print(output)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with Path(summary).open("a", encoding="utf-8") as file:
            file.write(output)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
