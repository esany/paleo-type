#!/usr/bin/env python3
"""Rebuildable text-only Nr. 632 edition; source files remain canonical (#376)."""
from __future__ import annotations
import argparse
import csv
import html
import re
from collections import defaultdict
from pathlib import Path

PROJECT = Path("projects/ssta-20578-nr-632")
GUID = "edd69aa1-eae4-4970-a695-94aaeccd6724"
SOURCE_ID = "SSTA-ARCHIVIALE-EDD69AA1"
LINE_ID = re.compile(r"^(?:\d{4}[LR]|1781-CH-(?:FRONT|REVERSE))-[A-Z]\d{2}[LR]?$")
PAGE_ID = re.compile(r"^\d{4}[LR]$")
CHECK = re.compile(
    r"^Vergleich: (?P<page>\d{4}[LR](?:-\d+)?) \| Lesung [0-9a-f]{40}"
    r" \| Vorab [0-9a-f]{40} \| Abweichungen (?P<errors>\d+)"
    r" \| davon Vereinheitlichung (?P<normalized>\d+)"
    r" \| Urteil (?P<decision>passt|überarbeiten)$"
)
UNCLEAR = re.compile(r"(⟦[^⟧]*⟧|\[[^\]]*\])")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def table_cells(line: str) -> list[str]:
    if not line.startswith("|") or not line.rstrip().endswith("|"):
        return []
    return [part.strip() for part in line.strip().strip("|").split("|")]


def strip_code(value: str) -> str:
    backtick = chr(96)
    return value[1:-1] if len(value) >= 2 and value.startswith(backtick) and value.endswith(backtick) else value


def plain_inventory(value: str) -> str:
    """Strip presentation-only Markdown without touching diplomatic readings."""
    return value.replace("**", "").replace(chr(96), "")


def read_inventory(root: Path) -> list[dict[str, str]]:
    file = root / PROJECT / "research/content-document-function-inventory-2026-10-30.md"
    if not file.is_file():
        raise FileNotFoundError(f"canonical document inventory missing: {file}")
    out = []
    for line in file.read_text(encoding="utf-8").splitlines():
        cols = table_cells(line)
        if len(cols) != 5 or not re.match(r"^\d{4}", cols[0]):
            continue
        area, function, date, evidence, unresolved = cols
        slug = re.sub(r"[^a-z0-9]+", "-", area.lower()).strip("-")
        out.append({"anchor": f"doc-{slug}", "area": plain_inventory(area),
                    "function": plain_inventory(function),
                    "date": plain_inventory(date) if date not in ("", "–", "-") else "offen",
                    "evidence": plain_inventory(evidence),
                    "open": plain_inventory(unresolved) if unresolved else "offen"})
    return out


def read_lines(root: Path) -> tuple[dict[str, tuple[str, str]], dict[str, bool]]:
    files = sorted((root / PROJECT / "research").glob("transcription-pilot-*.md"))
    if not files:
        raise FileNotFoundError("no canonical transcription-pilot-*.md sources")
    latest: dict[str, tuple[str, str]] = {}
    checked: dict[str, bool] = {}
    highest_sample: dict[str, int] = {}
    for file in files:
        for line in file.read_text(encoding="utf-8").splitlines():
            cols = table_cells(line)
            if len(cols) >= 3:
                key = strip_code(cols[0])
                reading = strip_code(cols[1])
                if LINE_ID.fullmatch(key):
                    latest[key] = (reading, " | ".join(cols[2:]))
            m = CHECK.fullmatch(line)
            if m and int(m["normalized"]) <= int(m["errors"]):
                recorded_id = m["page"]
                page, sep, suffix = recorded_id.partition("-")
                number = int(suffix) if sep else 1
                if number >= highest_sample.get(page, 0):
                    checked[page] = m["decision"] == "passt" and int(m["errors"]) <= 1
                    highest_sample[page] = number
    return latest, checked


def status_lines(root: Path) -> dict[str, str]:
    file = root / PROJECT / "STATUS.md"
    values = {}
    if file.is_file():
        for line in file.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^- \*\*(Stand für den Eigentümer):\*\* (.+)$", line)
            if m and m[1] not in values:
                values[m[1]] = m[2].replace(chr(96), "").replace("**", "")
    return values


def catalog_url(root: Path) -> str:
    file = root / "corpus/sources.tsv"
    if file.is_file():
        with file.open(encoding="utf-8", newline="") as fp:
            for row in csv.DictReader(fp, delimiter="\t"):
                if row.get("source_id") == SOURCE_ID:
                    value = row.get("digital_url", "")
                    if value.startswith("https://www.archiv.sachsen.de/"):
                        return value
    return ""


def line_page(line_id: str) -> str:
    if line_id.startswith("1781-CH-"):
        return line_id.rsplit("-", 1)[0]
    return line_id.split("-", 1)[0]


def sort_page(page: str) -> tuple[int, int, str]:
    if PAGE_ID.fullmatch(page):
        return (int(page[:4]), 0 if page.endswith("L") else 1, "")
    return (9999, 0, page)


def render_diplomatic(reading: str) -> str:
    pieces = []
    for token in UNCLEAR.split(reading):
        if not token:
            continue
        if UNCLEAR.fullmatch(token):
            pieces.append('<span class="uncertain">' + esc(token) + '</span>')
            pieces.append('<span class="uncertainty-flag" aria-label="unsicher">?</span>')
        else:
            pieces.append(esc(token))
    return "".join(pieces)


def render_note(note: str) -> str:
    """Interpret only established presentation markup, not historical readings."""
    note = note.replace("**", "")
    chunks = re.split(r"(`[^`]+`)", note)
    return "".join(
        "<code>" + esc(chunk[1:-1]) + "</code>"
        if len(chunk) > 1 and chunk.startswith(chr(96)) and chunk.endswith(chr(96))
        else esc(chunk)
        for chunk in chunks
    )


def render_line(identifier: str, reading: str, note: str) -> str:
    number = '<span class="line-id">' + esc(identifier) + '</span>'
    anchor = 'line-' + identifier.lower()
    descriptive = re.fullmatch(r"\*\*(.+?)\*\*", reading.strip(), re.S)
    if descriptive:
        # Source commentary in a reading-shaped table cell is not a diplomatic transcription.
        body = number + '<em class="description">' + esc(descriptive.group(1)) + '</em>'
    else:
        text = '<span class="diplomatic">' + render_diplomatic(reading) + '</span>'
        if UNCLEAR.search(reading):
            body = ('<details><summary>' + number + text + '</summary>'
                    '<p>Hinweis zur Zeile: ' + render_note(note or "Unsicherer Befund") + '</p></details>')
        else:
            body = number + text
    return '<li id="' + esc(anchor) + '" class="reading-line">' + body + '</li>'


def render_page(page: str, rows: list[tuple[str, str, str]], verified: bool) -> str:
    state = ('KI-Stichprobe: geprüft (keine Fachprüfung)' if verified
             else 'KI-Entwurf, ungeprüft')
    badge = '<span class="status ' + ('checked' if verified else 'draft') + '">' + state + '</span>'
    link = '<span>Fotobeziehung offen; siehe Archivkatalog</span>'
    if PAGE_ID.fullmatch(page):
        num = page[:4]
        url = f"https://www.archiv.sachsen.de/digitalisate/{GUID}/fullsize/{num}.jpg"
        link = '<a rel="external" href="' + esc(url) + '">Foto beim Archiv (Ansicht ' + num + ')</a>'
    lines = "\n".join(render_line(*row) for row in rows)
    return ('<article class="page" id="page-' + esc(page.lower()) + '">'
            '<h3>Schriftfläche ' + esc(page) + '</h3>' + badge
            + '<p>' + link + '</p><ol class="diplomatic-lines">' + lines
            + '</ol></article>')


def render_document(item: dict[str, str], pages: list[str]) -> str:
    nums = [int(x) for x in re.findall(r"\d{4}", item["area"])]
    matches = [p for p in pages if PAGE_ID.fullmatch(p) and nums
               and min(nums) <= int(p[:4]) <= max(nums)]
    links = " · ".join(
        '<a href="#page-' + esc(p.lower()) + '">' + esc(p) + '</a>' for p in matches
    )
    return (
        '<article class="document" id="' + esc(item["anchor"]) + '">'
        '<h3>' + esc(item["area"]) + ' — ' + esc(item["function"]) + '</h3>'
        '<p><strong>Datum/Akteure:</strong> ' + esc(item["date"]) + '</p>'
        '<p><strong>Beobachtung:</strong> ' + esc(item["evidence"]) + '</p>'
        '<p><strong>Offen:</strong> ' + esc(item["open"]) + '</p>'
        + ('<p>Schriftflächen: ' + links + '</p>' if links
           else '<p>Textlesung in dieser Zone: offen.</p>') + '</article>'
    )


STYLES = """
:root {color-scheme:light;font-family:system-ui, sans-serif;background:#faf9f6;color:#242522;}
* {box-sizing:border-box;}
body {margin:0;line-height:1.6;}
a {color:#184c73;text-underline-offset:3px;}
a:focus-visible, summary:focus-visible {outline:3px solid #1b5b95;outline-offset:3px;}
.skip {position:absolute;top:-4rem;left:1rem;background:white;padding:.5rem;}
.skip:focus {top:.5rem;}
.masthead {border-bottom:1px solid #cbc9c1;padding:2rem max(1rem, calc((100vw - 78rem)/2));}
h1,h2,h3 {font-family:Georgia,serif;font-weight:500;line-height:1.25;}
h1 {font-size:clamp(2rem, 5vw, 3.3rem);margin:.2rem 0;}
h2 {margin:2.6rem 0 1rem;font-size:1.65rem;}
h3 {font-size:1.25rem;}
.layout {max-width:82rem;margin:auto;padding:1rem;}
.layout main {display:grid;grid-template-columns:minmax(11rem,19rem) minmax(0,75ch);column-gap:3rem;min-width:0;}
.layout aside {grid-column:1;grid-row:1 / span 4;}
.layout section {grid-column:2;}
nav {position:sticky;top:1rem;max-height:95vh;overflow:auto;font-size:.9rem;}
.mobile-outline {display:none;}
nav ol {padding-left:1.3rem;}
nav li {padding-bottom:.5rem;}
main {min-width:0;overflow-wrap:anywhere;}
.document,.page {padding:1rem 0 1.5rem;border-bottom:1px solid #d8d6d0;}
.page {margin-top:1.5rem;}
.status {display:inline-block;font-weight:650;padding:.1rem .45rem;border-left:4px solid;}
.checked {border-color:#315f3e;color:#285532;}
.draft {border-color:#93612b;color:#754714;}
.diplomatic-lines {list-style:none;padding:0;margin-top:1rem;}
.reading-line {display:flex;padding:.22rem 0;font-family:Georgia,serif;line-height:1.55;}
.reading-line details {width:100%;}
.reading-line summary {cursor:pointer;display:list-item;list-style:none;}
.reading-line summary::-webkit-details-marker {display:none;}
.line-id {display:inline-block;width:8.6rem;font: .8rem/1.5 system-ui,sans-serif;color:#54534e;vertical-align:baseline;}
.diplomatic {white-space:pre-wrap;}
.uncertain {background:#f8e9bc;text-decoration:underline dotted;text-underline-offset:3px;}
.uncertainty-flag {font:bold .7rem system-ui,sans-serif;color:#805007;}
.line-note p {font: .87rem/1.5 system-ui,sans-serif;margin:.3rem 0 .9rem 8.6rem;}
.metadata {color:#454540;}
footer {padding:2rem 1rem;border-top:1px solid #cbc9c1;}
@media(max-width:700px) {.layout{padding:1rem;} .layout main{display:block;} nav{position:static;max-height:none;border-bottom:1px solid #ccc;} .desktop-outline{display:none;} .mobile-outline{display:block;} .line-id{width:7rem;} .line-note p{margin-left:0;}}
@media(prefers-reduced-motion:reduce) {* {scroll-behavior:auto !important;}}
"""


def build_site(root: Path, output: Path) -> None:
    """Compile one disposable presentation from the current named research owners."""
    documents = read_inventory(root)
    lines, checks = read_lines(root)
    status = status_lines(root)
    catalog = catalog_url(root)
    grouped = defaultdict(list)
    for identifier, (reading, note) in sorted(lines.items()):
        grouped[line_page(identifier)].append((identifier, reading, note))
    pages = sorted(grouped, key=sort_page)
    nav = "".join(
        '<li><a href="#' + esc(d["anchor"]) + '">'
        + esc(d["area"]) + " — " + esc(d["function"]) + "</a></li>"
        for d in documents
    )
    navigation = ('<h2>Gliederung</h2><ol class="desktop-outline">' + nav + '</ol>'
                  '<details class="mobile-outline"><summary>Gliederung anzeigen</summary>'
                  '<ol>' + nav + '</ol></details>')
    docs = "\n".join(render_document(d, pages) for d in documents)
    transcription = "\n".join(
        render_page(p, grouped[p], checks.get(p, False)) for p in pages
    )
    report = '<p>' + esc(status.get("Stand für den Eigentümer",
                                  "Aktueller Arbeitsstand noch nicht zusammengefasst.")) + '</p>'
    catalog_link = ('<a href="' + esc(catalog) + '" rel="external">Zum Archivkatalog</a>'
                    if catalog else '<span>Archivkatalog-Link offen</span>')
    html_text = (
        '<!doctype html><html lang="de"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Nr. 632 — Diplomatische KI-Arbeitsedition</title>'
        '<link rel="stylesheet" href="style.css"></head><body>'
        '<a class="skip" href="#hauptinhalt">Zum Text springen</a>'
        '<header class="masthead"><p>Sächsisches Staatsarchiv · Staatsarchiv Leipzig'
        ' · Bestand 20578</p><h1>Nr. 632 — Lehn zu gesamter Hand</h1>'
        '<p>GUID: ' + GUID + ' · ' + catalog_link + '</p>'
        '<p class="metadata">KI-Arbeitsstand, nicht fachlich begutachtet. '
        'Bildrechte: Bilder nur beim Archiv, hier keine Bilddateien.</p></header>'
        '<div class="layout"><main id="hauptinhalt"><section id="arbeitsstand">'
        '<h2>Aktueller Arbeitsstand</h2>' + report
        + '<p>Eigentümerentscheidungen richten sich nach dem Arbeitsplan; '
        'aus dieser Ansicht wird kein neuer Auftrag abgeleitet.</p></section>'
        '<aside><nav aria-label="Schriftstückgliederung">' + navigation + '</nav></aside>'
        '<section id="inventar"><h2>Schriftstücke und offene Grenzen</h2>'
        '<p>Die Gliederung enthält vorläufige Funktions- und Datierungskandidaten; '
        'Ansichtsnummern sind keine archivalische Foliierung.</p>'
        + docs + '</section>'
        '<section id="lesungen"><h2>Diplomatische Arbeitslesungen</h2>'
        '<p>Jede Zeile ist direkt adressierbar. Prüfstand bezeichnet allein '
        'KI-Gegenlese-Stichproben, keine wissenschaftliche Abnahme.</p>'
        + transcription + '</section>'
        '<section id="legende"><h2>Legende</h2><p><span class="uncertain">'
        '[Lesung?]</span> = vorgeschlagene, unsichere Lesung; '
        '<span class="uncertain">⟦…⟧</span> = sichtbare, nicht sicher '
        'transkribierte Schrift. Kürzungen bleiben in der diplomatischen '
        'Schreibung; Ergänzungen und Normalisierung sind nicht still erlaubt. '
        'Streichungen, Nachträge und Schäden bedürfen eigener '
        'quellenbezogener Kennzeichnung.</p></section></main></div>'
        '<footer>Reproduzierbare Darstellung aus den Forschungsdateien '
        'von Nr. 632. Keine neue Textautorität.</footer></body></html>'
    )
    if "**" in html_text:
        raise ValueError("unrendered Markdown bold marker in generated edition")
    output.mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(html_text, encoding="utf-8")
    (output / "style.css").write_text(STYLES, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build_site(args.root.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
