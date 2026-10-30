#!/usr/bin/env python3
"""S0 (#353): PR measures and a narrow new-evidence-file freeze."""
from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "engineering/evidence/"
LABEL = "verfahren-ausnahme"
RESCUE_LABEL = "rettung-eigentümer"
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


def guard_evidence(added: list[str], labels: set[str]) -> None:
    if added and LABEL not in labels:
        raise GuardFailure(f"Neue engineering/evidence/-Dateien ohne Label {LABEL}: {', '.join(added)}")


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


def rescue_counts(items: list[dict]) -> dict[str, int]:
    """Explicit owner-rescue labels only; include closed items and PRs exactly once."""
    counts = {"Issues": 0, "Pull Requests": 0}
    for item in items:
        labels = {lab["name"].casefold() for lab in item.get("labels", [])}
        if RESCUE_LABEL.casefold() in labels:
            counts["Pull Requests" if "pull_request" in item else "Issues"] += 1
    return counts


def fetch_issues(state: str) -> tuple[list[dict] | None, str]:
    repo, token = os.getenv("GITHUB_REPOSITORY"), os.getenv("GITHUB_TOKEN")
    if not repo or not token:
        return None, "Keine authentifizierte GitHub-API verfügbar."
    items = []
    try:
        for page in range(1, 21):
            request = urllib.request.Request(
                f"https://api.github.com/repos/{repo}/issues?state={state}&per_page=100&page={page}",
                headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                         "User-Agent": "paleo-type-metrics"},
            )
            with urllib.request.urlopen(request, timeout=15) as response:
                batch = json.load(response)
            if not isinstance(batch, list):
                return None, "GitHub-API-Antwort ist keine Liste."
            items.extend(batch)
            if len(batch) < 100:
                return items, "vollständig"
        return None, "Unvollständig: mehr als 2000 Einträge."
    except (OSError, ValueError, KeyError) as exc:
        return None, f"GitHub-API-Abfrage fehlgeschlagen: {exc}"


def live_issue_counts() -> tuple[dict[str, int] | None, str]:
    items, note = fetch_issues("open")
    if items is None:
        return None, note
    return issue_counts(items), "Nur eindeutige Bereich-Labels zählen; S0 ordnet fehlende Labels nicht selbst zu."


def live_rescue_counts() -> tuple[dict[str, int] | None, str]:
    items, note = fetch_issues("all")
    if items is None:
        return None, note
    return rescue_counts(items), "Nur Label rettung-eigentümer; offene und geschlossene Issues und PRs."


def event_labels() -> set[str]:
    path = os.getenv("GITHUB_EVENT_PATH")
    if not path:
        raise GuardFailure("GITHUB_EVENT_PATH fehlt; Fail-Closed")
    try:
        pr = json.loads(Path(path).read_text(encoding="utf-8"))["pull_request"]
        return {x["name"] for x in pr.get("labels", [])}
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
    rescues, rescue_note = live_rescue_counts()
    lines = [
        "## P0 – Verfahren und Forschung (#353)", "",
        f"- Bestand: engineering/ {e:,} Textzeichen; projects/ {p:,}; Verhältnis {e / p:.2f}:1."
        if p else f"- Bestand: engineering/ {e:,} Zeichen; projects/ 0 (kein Verhältnis).",
        f"- Neue PR-Zeilen (nur Messwert): engineering/ {added_e}, projects/ {added_p}.",
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
    lines.extend(["", "### Rettungseingriffe des Eigentümers (Label rettung-eigentümer)"])
    if rescues is None:
        lines.append(f"- Nicht geprüft: {rescue_note}")
    else:
        lines.extend([
            f"- Issues (offen und geschlossen): {rescues['Issues']}",
            f"- Pull Requests (offen und geschlossen): {rescues['Pull Requests']}",
            f"- Gesamt: {sum(rescues.values())}",
            f"- {rescue_note}",
        ])
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
            labels = event_labels()
            guard_evidence(new_evidence_files(tree_paths(args.base), tree_paths("HEAD")), labels)
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
