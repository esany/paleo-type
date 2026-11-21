#!/usr/bin/env python3
"""Verify blind-review metadata and immutable Git evidence, not handwriting.

Issue #368 P1, amended by #371: no chronological prerequisite between the
independent review and source-reading commits.  The reading commit must exist,
change the named canonical research owner, and be cited verbatim in a
machine-readable comparison row.  This cannot establish that a chat really
opened one text before another; the human declaration 'Blind: ja' remains a
declared provenance claim, not technically independently provable blindness.

Open pages (owner decision 22.11.2026, "Ja, erst Prüfung"): with
``--offen-pruefen`` the checker also reports, per listed page, whether its
latest comparison still leaves the page open.  This turns the existing method
rule (ARBEITSPLAN Nr. 632, Fehlerschwelle: "die Seite vor Fortsetzung
nachbessern und erneut prüfen") into a red check instead of prose.  A page is
open when its latest probe says "überarbeiten", has no comparison at all, or —
with ``--reading-dir`` — when the compared reading commit does not contain the
page's reading file or the diplomatic reading changed since that commit.  It
never judges whether a reading is right.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
from pathlib import Path

SHA = re.compile(r"[0-9a-f]{40}\Z")
PAGE = re.compile(r"\d{4}[LR](?:-\d+)?\Z")
PROBE = re.compile(r"(?P<base>\d{4}[LR])(?:-(?P<n>\d+))?\Z")
BASE_PAGE = re.compile(r"\d{4}[LR]\Z")
HEADER = re.compile(r"^## (\d{4}[LR](?:-\d+)?)\s*$", re.M)
COMPARISON = re.compile(
    r"^Vergleich: (?P<page>\d{4}[LR](?:-\d+)?) \| "
    r"Lesung (?P<reading>[0-9a-f]{40}) \| "
    r"Vorab (?P<review>[0-9a-f]{40}) \| "
    r"Abweichungen (?P<errors>\d+) \| "
    r"davon Vereinheitlichung (?P<normalized>\d+) \| "
    r"Urteil (?P<judgement>passt|überarbeiten)$"
)
REVIEW_LABELS = ("Datum:", "Leser:", "Bildquelle:", "Blind:")


def git(root: Path, *args: str) -> tuple[bool, str]:
    result = subprocess.run(
        ["git", "-C", str(root), *args], text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    return result.returncode == 0, result.stdout


def safe_project_path(root: Path, name: str) -> Path:
    path = Path(name)
    if path.is_absolute() or ".." in path.parts or not name.startswith("projects/"):
        raise ValueError("owner/review must be a relative Project path")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root):
        raise ValueError("Project path escapes repository")
    return resolved


def review_sections(contents: str, findings: list[str], *, all_sections: bool = True) -> dict[str, str]:
    matches = list(HEADER.finditer(contents))
    result: dict[str, str] = {}
    for i, match in enumerate(matches):
        page = match.group(1)
        section = contents[match.end():matches[i + 1].start() if i + 1 < len(matches) else len(contents)]
        if page in result:
            # Subsequent correction sections are permitted in general, but ambiguity
            # about which one to compare is not. Use distinct names/ref and trace.
            findings.append(f"duplicate review heading: {page}")
        result[page] = section
        if all_sections:
            for label in REVIEW_LABELS:
                if not re.search(r"^-\s*" + re.escape(label) + r"\s*\S+", section, re.M):
                    findings.append(f"{page}: missing {label} in review section")
            if not re.search(r"^-\s*Blind:\s*ja(?:[\s;,.]|$)", section, re.M):
                findings.append(f"{page}: reviewer did not declare Blind: ja")
            has_numbered_line = bool(re.search(
                r"^-\s*(?:.*\bZ\.\s*\d+\b.*):\s*.+", section, re.M
            ))
            # Some photographed views show only bleed-through and therefore
            # have no independently transcribable physical lines. Do not force
            # fabricated graphemes or numbered lines to satisfy a format check.
            # This validates an explicit ZERO observation, not a 2-3-line PASS.
            zero_line_observation = bool(
                re.search(r"^-\s*Stichprobe:\s*0(?:\s|$)", section, re.M)
                and re.search(r"^-\s*Bildbefund[^:]*:\s*\S+", section, re.M)
            )
            if not (has_numbered_line or zero_line_observation):
                findings.append(f"{page}: no numbered physical-line locus or evidenced zero-line observation")
    return result


def owner_changed_at_reading(root: Path, sha: str, owner_paths: str | list[str]) -> bool:
    """True if the reading commit itself changes one of the allowed owner files."""
    if isinstance(owner_paths, str):
        owner_paths = [owner_paths]
    if not SHA.fullmatch(sha):
        return False
    ok, _ = git(root, "cat-file", "-e", sha + "^{commit}")
    if not ok:
        return False
    # The claimed reading SHA must itself change the named owner file, not
    # merely point to an existing tree or a review-only commit.
    ok, paths = git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", sha)
    if not ok:
        return False
    changed = set(paths.splitlines())
    for owner_path in owner_paths:
        if owner_path in changed and git(root, "show", f"{sha}:{owner_path}")[0]:
            return True
    return False


def probe_key(page: str) -> tuple[str, int]:
    """'0104R' -> ('0104R', 1); '0104R-2' -> ('0104R', 2)."""
    match = PROBE.fullmatch(page)
    if match is None:
        raise ValueError(f"not a probe id: {page}")
    return match["base"], int(match["n"] or 1)


def reading_rows(text: str) -> list[tuple[str, str]]:
    """(line_ref, diplomatic_reading) in file order; other columns may change freely."""
    rows = [r for r in csv.reader(io.StringIO(text), delimiter="\t", quoting=csv.QUOTE_NONE) if r]
    if not rows:
        raise ValueError("empty reading file")
    header = rows[0]
    try:
        i_ref, i_read = header.index("line_ref"), header.index("diplomatic_reading")
    except ValueError:
        raise ValueError("reading file lacks line_ref/diplomatic_reading columns") from None
    width = max(i_ref, i_read) + 1
    return [(r[i_ref], r[i_read]) for r in rows[1:] if len(r) >= width]


def open_pages(root: Path, comparisons: list[dict], scope: list[str], invalid: set[str],
               reading_dir: str | None, findings: list[str]) -> tuple[list[dict], list[dict]]:
    """Per listed page: is it still open, and why?  Returns (offen, verglichen)."""
    offen: list[dict] = []
    verglichen: list[dict] = []
    for base in scope:
        lines = [c for c in comparisons if probe_key(c["page"])[0] == base]
        if not lines:
            offen.append({"seite": base, "grund": "keine Vergleichszeile; die Gegenlesung ist offen"})
            continue
        ids = [c["page"] for c in lines]
        duplicates = sorted({i for i in ids if ids.count(i) > 1})
        if duplicates:
            findings.append(f"{base}: doppelte Vergleichszeile {', '.join(duplicates)}; "
                            "welcher Vergleich gilt, ist nicht eindeutig")
            offen.append({"seite": base, "grund": "doppelte Vergleichszeile, siehe Befunde"})
            continue
        latest = max(lines, key=lambda c: probe_key(c["page"])[1])
        probe = latest["page"]
        following = f"{base}-{probe_key(probe)[1] + 1}"
        sha12 = latest["reading"][:12]
        if probe in invalid:
            offen.append({"seite": base, "letzter_vergleich": probe,
                          "grund": f"der letzte Vergleich {probe} ist ungültig, siehe Befunde"})
            continue
        if latest["judgement"] == "überarbeiten":
            offen.append({"seite": base, "letzter_vergleich": probe,
                          "grund": f"letztes Urteil „überarbeiten“ ({probe}); offen, bis eine neue "
                                   f"Blindprobe {following} gegen die überarbeitete Lesung „passt“ ergibt"})
            continue
        if reading_dir:
            path = f"{reading_dir}/{base}.tsv"
            ok, then = git(root, "show", f"{latest['reading']}:{path}")
            if not ok:
                offen.append({"seite": base, "letzter_vergleich": probe,
                              "grund": f"verglichen wurde Commit {sha12}; dort gibt es {base}.tsv noch "
                                       "nicht. Ob die heutige Lesung blind verglichen ist, lässt sich nicht "
                                       f"feststellen; nötig ist eine neue Blindprobe {following}"})
                continue
            now = root / path
            if not now.is_file():
                offen.append({"seite": base, "letzter_vergleich": probe,
                              "grund": f"Lesungsdatei {path} fehlt im heutigen Stand"})
                continue
            try:
                changed = reading_rows(then) != reading_rows(now.read_text(encoding="utf-8"))
            except ValueError as err:
                findings.append(f"{path}: {err}")
                offen.append({"seite": base, "letzter_vergleich": probe,
                              "grund": "Lesungsdatei nicht lesbar, siehe Befunde"})
                continue
            if changed:
                offen.append({"seite": base, "letzter_vergleich": probe,
                              "grund": f"die Lesung wurde nach dem verglichenen Commit {sha12} geändert; "
                                       f"nötig ist eine neue Blindprobe {following}"})
                continue
        verglichen.append({"seite": base, "letzter_vergleich": probe, "lesung": latest["reading"]})
    return offen, verglichen


def run(root: Path, owner_path: str | list[str], review_path: str, review_ref: str,
        reading_dir: str | None = None, scope: list[str] | None = None) -> tuple[int, dict]:
    findings: list[str] = []
    owner_paths = [owner_path] if isinstance(owner_path, str) else list(owner_path)
    try:
        for path in owner_paths:
            safe_project_path(root, path)
        safe_project_path(root, review_path)
        if reading_dir:
            safe_project_path(root, reading_dir)
        for base in scope or []:
            if not BASE_PAGE.fullmatch(base):
                raise ValueError(f"--offen-pruefen expects pages like 0104R, got {base!r}")
    except ValueError as err:
        return 1, {"result": "FAIL", "checked": 0, "findings": [str(err)]}
    for path in owner_paths:
        if not (root / path).is_file():
            return 1, {"result": "FAIL", "checked": 0, "findings": [f"research owner missing: {path}"]}
    ok, latest = git(root, "show", f"{review_ref}:{review_path}")
    if not ok:
        return 1, {"result": "FAIL", "checked": 0, "findings": ["review ref/file missing"]}
    active = review_sections(latest, findings)
    checked = 0
    comparisons: list[dict] = []
    invalid: set[str] = set()
    for owner in owner_paths:
        for line in (root / owner).read_text(encoding="utf-8").splitlines():
            if not line.startswith("Vergleich:"):
                continue
            checked += 1
            match = COMPARISON.fullmatch(line)
            if match is None:
                findings.append("malformed comparison line (expected 6 literal fields)")
                continue
            data = match.groupdict()
            page, reading, pre = data["page"], data["reading"], data["review"]
            before = len(findings)
            n, normalized = int(data["errors"]), int(data["normalized"])
            if normalized > n:
                findings.append(f"{page}: normalized count exceeds errors")
            if data["judgement"] == "passt" and n > 1:
                findings.append(f"{page}: 'passt' contradicts >1 unmarked errors")
            if page not in active:
                findings.append(f"{page}: no review section in active review branch")
            allowed = [owner]
            if reading_dir:
                allowed.append(f"{reading_dir}/{probe_key(page)[0]}.tsv")
            if not owner_changed_at_reading(root, reading, allowed):
                findings.append(f"{page}: reading commit absent or does not change research owner")
            ok, recorded = git(root, "show", f"{pre}:{review_path}")
            if not ok:
                findings.append(f"{page}: cited review commit/file missing")
            else:
                historical = review_sections(recorded, [], all_sections=False)
                if page not in historical or not re.search(
                    r"^-\s*Blind:\s*ja(?:[\s;,.]|$)", historical[page], re.M
                ):
                    findings.append(f"{page}: cited review snapshot lacks a Blind: ja section")
            if len(findings) > before:
                invalid.add(page)
            comparisons.append(data)
    result = {
        "checked": checked,
        "review_sections": len(active),
        "findings": findings,
        "claim_ceiling": "Git commit/format and declared blindness only; no source reading accepted.",
    }
    if scope:
        offen, verglichen = open_pages(root, comparisons, scope, invalid, reading_dir, findings)
        result["offen"] = offen
        result["verglichen"] = verglichen
    failed = bool(findings) or bool(result.get("offen"))
    result = {"result": "FAIL" if failed else "PASS", **result}
    return (1 if failed else 0), result


def summary_markdown(result: dict, owners: list[str]) -> str:
    """Plain-language German summary for the GitHub check page."""
    offen = result.get("offen", [])
    verglichen = result.get("verglichen", [])
    findings = result.get("findings", [])
    if findings:
        status = "Fehler im Format oder in der Herkunft der Vergleiche"
    elif offen:
        status = f"offen ({len(offen)} Seite{'n' if len(offen) != 1 else ''})"
    else:
        status = "alle geprüften Seiten blind verglichen und seither unverändert"
    out = ["## Blindproben-Prüfung", "", f"**Ergebnis: {status}.**", "",
           f"Gelesen: {result.get('checked', 0)} Vergleichszeilen in "
           + ", ".join(f"`{o}`" for o in owners) + ".", ""]
    if offen:
        out += [f"### Offen ({len(offen)})", ""] + [f"- **{o['seite']}:** {o['grund']}" for o in offen] + [""]
    if findings:
        out += [f"### Befunde ({len(findings)})", ""] + [f"- {f}" for f in findings] + [""]
    if verglichen:
        out += [f"### Verglichen und seither unverändert ({len(verglichen)})", ""]
        out += [f"- {v['seite']}: Vergleich {v['letzter_vergleich']}, Lesung `{v['lesung'][:12]}`" for v in verglichen]
        out += [""]
    out += ["**Grenze:** Geprüft wird nur, ob blind verglichen wurde, ob das Urteil eingehalten ist und ob die "
            "Lesung seit dem Vergleich gleich geblieben ist. Ob eine Lesung stimmt, prüft das nicht. "
            "„Blind: ja“ ist eine Erklärung des Gegenlesers, kein technischer Beweis.", ""]
    return "\n".join(out)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--research-owner", required=True, action="append",
                   help="file with Vergleich: lines; may be given more than once")
    p.add_argument("--review-path", required=True)
    p.add_argument("--review-ref", required=True)
    p.add_argument("--reading-dir", help="directory with <page>.tsv reading files (first-reading)")
    p.add_argument("--offen-pruefen", help="comma-separated pages, e.g. 0104R,0105L: report open pages")
    p.add_argument("--zusammenfassung", type=Path, help="append a German Markdown summary to this file")
    args = p.parse_args()
    scope = [s.strip() for s in args.offen_pruefen.split(",") if s.strip()] if args.offen_pruefen else None
    rc, result = run(args.root.resolve(), args.research_owner, args.review_path, args.review_ref,
                     reading_dir=args.reading_dir, scope=scope)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    if args.zusammenfassung:
        with args.zusammenfassung.open("a", encoding="utf-8") as handle:
            handle.write(summary_markdown(result, args.research_owner))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
