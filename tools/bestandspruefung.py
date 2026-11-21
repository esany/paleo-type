"""Bestandsprüfung: Was gibt es zu einem Gegenstand im Repo und auf GitHub schon?

Gedacht für den Beginn jeder Arbeit: Gegenstand nennen, zum Beispiel
„Gesuch 0104R–0107L“, „Nr. 632“ oder „0105L“, die Ausgabe lesen, erst dann arbeiten.

Das Skript sucht nur nach Wortlaut. Es beurteilt nichts und ändert nichts.

Aufruf:
    python tools/bestandspruefung.py "Gesuch 0104R-0107L" [weitere Begriffe …]
    python tools/bestandspruefung.py --github-json datei.json "0104R"   # ohne Netz
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

DASH_CLASS = "[-‐‑‒–—−]"
DECISION = re.compile(r"(?i)eigentümerentscheidung|human[- ]owner[- ]entscheidung|human[- ]owner decision")
TEXT_SUFFIXES = {".md", ".tsv", ".yml", ".yaml", ".json", ".txt", ".py"}
SKIP_PREFIXES = ("tests/fixtures/",)
FIELDS = "number,title,state,labels,body,comments"


def term_pattern(term: str) -> re.Pattern[str]:
    """Begriff ohne Rücksicht auf Groß/klein, Strichart und Leerraum suchen."""
    parts = re.split(r"(\s+|[-‐‑‒–—−])", term.strip())
    out = []
    for p in parts:
        if not p:
            continue
        if p.isspace():
            out.append(r"\s+")
        elif re.fullmatch(DASH_CLASS, p):
            out.append(DASH_CLASS)
        else:
            out.append(re.escape(p))
    return re.compile("".join(out), re.IGNORECASE)


def _snippet(text: str, m: re.Match[str], width: int = 70) -> str:
    start, end = max(0, m.start() - width), min(len(text), m.end() + width)
    return ("…" if start else "") + " ".join(text[start:end].split()) + ("…" if end < len(text) else "")


def _blocks(item: dict):
    yield "Titel", item.get("title") or ""
    yield "Text", item.get("body") or ""
    for c in item.get("comments") or []:
        yield "Kommentar", c.get("body") or ""


def _hit(item: dict, patterns: list[re.Pattern[str]]) -> dict | None:
    found = None
    decision = False
    for where, text in _blocks(item):
        if DECISION.search(text):
            decision = True
        if found is None:
            for p in patterns:
                m = p.search(text)
                if m:
                    found = (where, _snippet(text, m))
                    break
    if found is None:
        return None
    return {
        "number": item["number"],
        "title": item.get("title", ""),
        "state": item.get("state", ""),
        "labels": [lab["name"] for lab in item.get("labels") or []],
        "where": found[0],
        "snippet": found[1],
        "decision": decision,
    }


SURFACE = re.compile(r"(?<![0-9])([0-9]{4}[LR])(?![0-9A-Za-z])")
PROJECT = re.compile(r"^projects/([^/]+)/")


def terms_from_paths(paths: list[str]) -> list[str]:
    """Gegenstände aus geänderten Pfaden: Flächen wie `0104R`; sonst die Projekt-ID."""
    surfaces = sorted({m.group(1) for p in paths for m in SURFACE.finditer(p) if PROJECT.match(p)})
    if surfaces:
        return surfaces
    return sorted({m.group(1) for p in paths if (m := PROJECT.match(p))})


def pruefe(terms: list[str], issues: list[dict], prs: list[dict], files: dict[str, str]) -> dict[str, list[dict]]:
    patterns = [term_pattern(t) for t in terms if t.strip()]
    result: dict[str, list[dict]] = {
        "offene_issues": [], "offene_prs": [], "entscheidungen": [], "geschlossene_issues": [], "dateien": [],
    }
    for item in issues:
        h = _hit(item, patterns)
        if not h:
            continue
        if h["state"] == "OPEN":
            result["offene_issues"].append(h)
        elif h["decision"]:
            result["entscheidungen"].append(h)
        else:
            result["geschlossene_issues"].append(h)
    for item in prs:
        h = _hit(item, patterns)
        if h and h["state"] == "OPEN":
            result["offene_prs"].append(h)
    for path in sorted(files):
        for lineno, line in enumerate(files[path].splitlines(), 1):
            m = next((m for p in patterns if (m := p.search(line))), None)
            if m:
                result["dateien"].append({"path": path, "line": lineno, "snippet": _snippet(line, m, 50)})
                break
    result["offene_issues"].sort(key=lambda h: (not any(lab.startswith("an:") for lab in h["labels"]), -h["number"]))
    for key in ("offene_prs", "entscheidungen", "geschlossene_issues"):
        result[key].sort(key=lambda h: -h["number"])
    return result


def _repo_files(repo: Path) -> dict[str, str]:
    try:
        names = subprocess.run(["git", "-C", str(repo), "ls-files"], capture_output=True, text=True, check=True).stdout.split("\n")
    except (subprocess.CalledProcessError, FileNotFoundError):
        names = [str(p.relative_to(repo)) for p in repo.rglob("*") if p.is_file()]
    files = {}
    for name in names:
        if not name or name.startswith(SKIP_PREFIXES) or Path(name).suffix not in TEXT_SUFFIXES:
            continue
        p = repo / name
        try:
            if p.stat().st_size <= 2_000_000:
                files[name] = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
    return files


def _github(repo: Path) -> tuple[list[dict], list[dict], str]:
    try:
        run = lambda kind: json.loads(subprocess.run(  # noqa: E731
            ["gh", kind, "list", "--state", "all", "--limit", "1000", "--json", FIELDS],
            capture_output=True, text=True, check=True, cwd=str(repo)).stdout)
        return run("issue"), run("pr"), "live über gh"
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError) as err:
        return [], [], f"NICHT erreichbar ({type(err).__name__}); nur Repo-Dateien geprüft"


def _line(h: dict) -> str:
    labels = ", ".join(h["labels"])
    return f"#{h['number']} [{labels}] {h['title']}\n      {h['where']}: {h['snippet']}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terms", nargs="*", help="Gegenstand, z. B. \"Gesuch 0104R-0107L\"")
    ap.add_argument("--from-paths", type=Path, help="Datei mit geänderten Pfaden (eine je Zeile); Gegenstände werden daraus abgeleitet")
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--github-json", type=Path, help="Datei mit {\"issues\": [...], \"prs\": [...]} statt live")
    args = ap.parse_args()
    if args.from_paths:
        paths = [line.strip() for line in args.from_paths.read_text(encoding="utf-8").splitlines() if line.strip()]
        args.terms = list(args.terms) + terms_from_paths(paths)
        if not args.terms:
            print("Keine Gegenstände aus den geänderten Pfaden ableitbar (keine Projekt- oder Flächenpfade). Bestandsprüfung übersprungen.")
            return 0
    if not args.terms:
        ap.error("Gegenstand angeben oder --from-paths nutzen")

    if args.github_json:
        data = json.loads(args.github_json.read_text(encoding="utf-8"))
        issues, prs, source = data.get("issues", []), data.get("prs", []), f"Datei {args.github_json}"
    else:
        issues, prs, source = _github(args.repo)
    r = pruefe(args.terms, issues, prs, _repo_files(args.repo))

    print("Bestandsprüfung für: " + " | ".join(f"„{t}“" for t in args.terms))
    print(f"GitHub: {source}")
    sections = [
        ("Offene Issues (Aufträge zuerst)", "offene_issues"),
        ("Offene PRs", "offene_prs"),
        ("Geschlossene Issues mit Eigentümerentscheidung", "entscheidungen"),
    ]
    for title, key in sections:
        print(f"\n== {title}: {len(r[key])} ==")
        for h in r[key]:
            print(_line(h))
    print(f"\n== Weitere geschlossene Issues: {len(r['geschlossene_issues'])} ==")
    for h in r["geschlossene_issues"]:
        print(f"#{h['number']} {h['title']}")
    print(f"\n== Dateien im Repo: {len(r['dateien'])} ==")
    for f in r["dateien"][:60]:
        print(f"{f['path']}:{f['line']}  {f['snippet']}")
    if len(r["dateien"]) > 60:
        print(f"… und {len(r['dateien']) - 60} weitere")
    print("\nHinweis: Suche nach Wortlaut, keine Beurteilung. Offene Aufträge und Eigentümerentscheidungen vor dem Arbeiten lesen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
