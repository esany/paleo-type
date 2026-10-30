#!/usr/bin/env python3
"""P0 (#353): derived PR measures and enforceable evidence-growth constraints."""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "engineering/evidence/"
LABEL = "verfahren-ausnahme"
CATEGORIES = ("Forschung", "Technik", "Verfahren")


class GuardFailure(ValueError):
    pass


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def tree_paths(ref: str) -> set[str]:
    return set(filter(None, git("ls-tree", "-r", "-z", "--name-only", ref).decode().split("\0")))


def new_evidence_files(base: set[str], head: set[str]) -> list[str]:
    # Set difference also detects a rename from outside engineering/evidence.
    return sorted(path for path in head - base if path.startswith(PREFIX))


def has_reason(body: str, heading: str) -> bool:
    match = re.search(r"(?im)^" + re.escape(heading) + r":\s*(\S[^\r\n]*)$", body)
    return bool(match and len(match.group(1).strip()) >= 12 and match.group(1).rstrip().endswith((".", "!", "?")))


def guard_evidence(added: list[str], labels: set[str], body: str) -> None:
    if not added:
        return
    if LABEL not in labels:
        raise GuardFailure(f"Neue engineering/evidence/-Dateien ohne Label {LABEL}: {', '.join(added)}")
    if not has_reason(body, "Verfahren-Ausnahme-Begründung"):
        raise GuardFailure("Ausnahme erfordert einen Satz: Verfahren-Ausnahme-Begründung: ... .")


def added_lines(base: str) -> tuple[int, int]:
    output = git("diff", "--numstat", "--no-renames", base, "HEAD", "--", "engineering/", "projects/").decode()
    eng = proj = 0
    for row in output.splitlines():
        added, _removed, path = row.split("\t", 2)
        if added == "-":
            continue
        if path.startswith("engineering/"):
            eng += int(added)
        elif path.startswith("projects/"):
            proj += int(added)
    return eng, proj


def guard_growth(eng: int, proj: int, body: str) -> None:
    # #353's target: <= 1 procedural line per 2 research lines, with exceptions explained.
    if eng and eng * 2 > proj and not has_reason(body, "Verfahrenszuwachs-Begründung"):
        raise GuardFailure(
            f"Verfahrenszuwachs {eng}, Forschungszuwachs {proj}: "
            "Begründungssatz im PR erforderlich (Verfahrenszuwachs-Begründung: ... .)."
        )


def tracked_text_sizes() -> tuple[dict[str, int], int]:
    sizes = {"engineering": 0, "projects": 0}
    skipped = 0
    for path in filter(None, git("ls-files", "-z").decode().split("\0")):
        group = path.split("/", 1)[0]
        if group in sizes:
            try:
                sizes[group] += len((ROOT / path).read_text(encoding="utf-8"))
            except (UnicodeDecodeError, OSError):
                skipped += 1
    return sizes, skipped


def issue_counts(issues: list[dict]) -> dict[str, int]:
    result = {c: 0 for c in CATEGORIES}
    result["Unklassifiziert"] = 0
    for issue in issues:
        if "pull_request" in issue:  # GitHub's issues endpoint includes PRs
            continue
        labels = {lab["name"].casefold() for lab in issue.get("labels", [])}
        matches = [c for c in CATEGORIES if c.casefold() in labels or ("bereich:" + c.casefold()) in labels]
        result[matches[0] if len(matches) == 1 else "Unklassifiziert"] += 1
    return result


def live_issue_counts() -> tuple[dict[str, int] | None, str]:
    repo, token = os.getenv("GITHUB_REPOSITORY"), os.getenv("GITHUB_TOKEN")
    if not repo or not token:
        return None, "Keine authentifizierte GitHub-API verfügbar."
    issues = []
    try:
        for page in range(1, 21):
            request = urllib.request.Request(
                f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100&page={page}",
                headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                         "User-Agent": "paleo-type-metrics"},
            )
            with urllib.request.urlopen(request, timeout=15) as response:
                batch = json.load(response)
            issues.extend(batch)
            if len(batch) < 100:
                return issue_counts(issues), "Nur eindeutige Bereich-Labels zählen; P3 ordnet die übrigen Issues."
        return None, "Unvollständig: mehr als 2000 Einträge."
    except (OSError, ValueError, KeyError) as exc:
        return None, f"Issue-Abfrage nicht verifiziert: {exc}"


def event_pr() -> tuple[set[str], str]:
    path = os.getenv("GITHUB_EVENT_PATH")
    if not path:
        raise GuardFailure("GITHUB_EVENT_PATH fehlt; Fail-Closed")
    try:
        pr = json.loads(Path(path).read_text(encoding="utf-8"))["pull_request"]
        return {x["name"] for x in pr.get("labels", [])}, pr.get("body") or ""
    except (OSError, KeyError, ValueError, TypeError) as exc:
        raise GuardFailure(f"PR-Ereignis unlesbar: {exc}") from exc


def report(base: str | None) -> str:
    sizes, skipped = tracked_text_sizes()
    e, p = sizes["engineering"], sizes["projects"]
    required = {name: len((ROOT / name).read_text(encoding="utf-8"))
                for name in ("GOVERNING_OBJECTIVE.md", "AGENTS.md")}
    approx_tokens = math.ceil(sum(required.values()) / 4)
    added_e, added_p = added_lines(base) if base else (0, 0)
    counts, note = live_issue_counts()
    lines = [
        "## P0 – Verfahren und Forschung (#353)", "",
        f"- Bestand: engineering/ {e:,} Textzeichen; projects/ {p:,}; Verhältnis {e / p:.2f}:1."
        if p else f"- Bestand: engineering/ {e:,} Zeichen; projects/ 0 (kein Verhältnis).",
        f"- Neue PR-Zeilen: engineering/ {added_e}, projects/ {added_p} "
        "(Ziel maximal 1:2; größerer Verfahrenszuwachs erfordert PR-Begründung).",
        f"- Start-Pflichtlektüre: GOVERNING_OBJECTIVE.md {required['GOVERNING_OBJECTIVE.md']:,} "
        f"und AGENTS.md {required['AGENTS.md']:,} Zeichen; zusammen ca. {approx_tokens:,} Tokens. "
        "Näherung Zeichen/4, kein Tokenizer; weitere Lektüre ist auftragsabhängig.",
        f"- Nicht als Text zählbare Dateien in diesen Bereichen: {skipped}.",
        "", "### Offene Issues nach Perspektive (PRs ausgenommen)",
    ]
    if counts is None:
        lines.append(f"- Nicht geprüft: {note}")
    else:
        lines.extend(f"- {key}: {counts[key]}" for key in (*CATEGORIES, "Unklassifiziert"))
        lines.append(f"- {note}")
    lines.extend(["", "CI und Kennzahlen prüfen keine historische Lesung oder fachliche Validierung.", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", help="Exact PR base commit SHA")
    parser.add_argument("--guard", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    try:
        if args.guard:
            if not args.base:
                raise GuardFailure("Base-SHA fehlt; Fail-Closed")
            labels, body = event_pr()
            guard_evidence(new_evidence_files(tree_paths(args.base), tree_paths("HEAD")), labels, body)
            guard_growth(*added_lines(args.base), body)
            print("P0 GUARD PASS")
        else:
            text = report(args.base)
            print(text)
            if args.summary:
                dest = os.getenv("GITHUB_STEP_SUMMARY")
                if not dest:
                    raise GuardFailure("GITHUB_STEP_SUMMARY fehlt")
                with open(dest, "a", encoding="utf-8") as f:
                    f.write(text + "\n")
    except (GuardFailure, subprocess.CalledProcessError, OSError, ValueError) as exc:
        print(f"P0 FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
