"""Verlusttest für #397: Gesuch 0104R–0107L in das Zeilenformat der Visitationsakten.

Prüft nur, dass jede Tabellenzeile der bisherigen Markdown-Fassung genau einmal
und unverändert in `transcription/first-reading/<Fläche>.tsv` steht. Er beurteilt
keine Lesung.
"""

from __future__ import annotations

import csv
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "projects/ssta-20578-nr-632"
MARKDOWN = PROJECT / "research/gesuch-0104R-0107L.md"
FIRST_READING = PROJECT / "transcription/first-reading"
SURFACES = ("0104R", "0105L", "0105R", "0106L", "0106R", "0107L")
KEYS = ("0104R", "0105-0107", "F1-bilanz")
# Spalten wie in projects/ega-reg-ii-4-bd-ii/transcription/first-reading/*.tsv (Knau-Vorbild).
HEADER = [
    "reading_order", "diplomatic_reading", "line_ref", "region", "source_phenomena",
    "research_status", "alternatives", "abbreviation_layer", "editorial_supply", "evidence_note",
]
ROW = re.compile(r"^\|\s*`((?:0104R|0105L|0105R|0106L|0106R|0107L)-[A-Z]\d+)`\s*\|(.*)\|\s*$")


def markdown_rows() -> list[tuple[str, str, str]]:
    """Alle Tabellenzeilen der verschobenen Gesuch-Blöcke: (line_ref, Lesung, Grenze)."""
    text = MARKDOWN.read_text(encoding="utf-8")
    blocks = "".join(
        text.split(f"<!-- F4-START:{k} -->\n", 1)[1].split(f"<!-- F4-END:{k} -->\n", 1)[0] for k in KEYS
    )
    rows = []
    for line in blocks.splitlines():
        m = ROW.match(line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) != 2:
            raise AssertionError(f"{m.group(1)}: erwartet 3 Zellen")
        reading = cells[0][1:-1] if cells[0].startswith("`") and cells[0].endswith("`") else cells[0]
        rows.append((m.group(1), reading, cells[1]))
    return rows


def tsv_rows() -> dict[str, list[dict[str, str]]]:
    result = {}
    for surface in SURFACES:
        path = FIRST_READING / f"{surface}.tsv"
        with path.open(encoding="utf-8", newline="") as fh:
            reader = csv.reader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
            header = next(reader)
            if header != HEADER:
                raise AssertionError(f"{path.name}: Kopfzeile weicht vom Knau-Format ab")
            result[surface] = [dict(zip(HEADER, r)) for r in reader if r]
    return result


class FirstReadingMigrationTest(unittest.TestCase):
    def test_every_markdown_row_exactly_once_and_unchanged(self) -> None:
        source = markdown_rows()
        self.assertEqual(len(source), 97)
        target = tsv_rows()
        flat = [r for surface in SURFACES for r in target[surface]]
        self.assertEqual(len(flat), 97, "keine zusätzlichen oder fehlenden Zeilen")
        by_ref = {}
        for r in flat:
            self.assertNotIn(r["line_ref"], by_ref, f"{r['line_ref']} doppelt")
            by_ref[r["line_ref"]] = r
        for line_ref, reading, boundary in source:
            r = by_ref[line_ref]
            self.assertEqual(r["diplomatic_reading"], reading, line_ref)
            self.assertTrue(r["evidence_note"].startswith(boundary), f"{line_ref}: Grenze/Beleg verändert")

    def test_surface_files_keep_source_order(self) -> None:
        source = markdown_rows()
        target = tsv_rows()
        for surface in SURFACES:
            expected = [ref for ref, _, _ in source if ref.startswith(surface + "-")]
            actual = [r["line_ref"] for r in target[surface]]
            self.assertEqual(actual, expected, surface)
            self.assertEqual([r["reading_order"] for r in target[surface]],
                             [f"{i:03d}" for i in range(1, len(actual) + 1)], surface)

    def test_required_fields_present(self) -> None:
        for surface, rows in tsv_rows().items():
            for r in rows:
                for field in ("region", "source_phenomena", "research_status"):
                    self.assertTrue(r[field], f"{r['line_ref']}: {field} leer")
                self.assertIn(r["research_status"], {"observed", "working", "variant", "unresolved"}, r["line_ref"])
                self.assertIn("not_investigated", r["source_phenomena"], f"{r['line_ref']}: Nicht-Untersuchtes benennen")

    def test_owner_name_hints_stay_outside_the_reading(self) -> None:
        text = MARKDOWN.read_text(encoding="utf-8")
        hints = re.findall(r"(?m)^Namenshinweis: (\S+) (\S+) \| Eigentümer: ([^|]+)\|", text)
        self.assertTrue(hints)
        by_ref = {r["line_ref"]: r for rows in tsv_rows().values() for r in rows}
        for _surface, locator, owner_text in hints:
            first = locator.split("–")[0]
            if first not in by_ref:
                continue  # Hinweise des Durchgangs zu Stellen ohne eigene Zeile
            self.assertIn(owner_text.strip(), by_ref[first]["evidence_note"], locator)
            self.assertNotIn(owner_text.strip(), by_ref[first]["diplomatic_reading"], locator)


if __name__ == "__main__":
    unittest.main()
