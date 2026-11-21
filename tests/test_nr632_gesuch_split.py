"""Verlusttest für das Abtrennen des Gesuchs 0104R–0107L (Nr. 632).

Prüft nur, dass beim Verschieben nichts verloren geht oder doppelt vorkommt.
Er beurteilt keine Lesung.
"""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "projects/ssta-20578-nr-632/research"
PILOT = RESEARCH / "transcription-pilot-0102R-0103L-2026-10-30.md"
GESUCH = RESEARCH / "gesuch-0104R-0107L.md"

# Git-Blob der bisherigen Datei am Forschungsbranch, Commit f4a6ca5abded, vor dem Abtrennen.
ORIGINAL_BLOB = "63b4f23eece770bce225302b8b2fbbc928efbcd1"
KEYS = ("0104R", "0105-0107", "F1-bilanz")
ROW = re.compile(r"(?m)^\|\s*`(0104R|0105L|0105R|0106L|0106R|0107L)-([^`]+)`\s*\|")
MARK = re.compile(r"<!-- VERGLEICH-IM-BISHERIGEN-OWNER:([^ ]+) -->\n")
VERGLEICH = re.compile(r"(?m)^Vergleich:[^\n]*\n")


def git_blob(text: str) -> str:
    data = text.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def restore(pilot: str, gesuch: str) -> str:
    """Setzt die bisherige Datei aus beiden Dateien wieder zusammen."""
    for key in KEYS:
        start = f"<!-- F4-START:{key} -->\n"
        end = f"<!-- F4-END:{key} -->\n"
        if gesuch.count(start) != 1 or gesuch.count(end) != 1:
            raise AssertionError(f"Block {key}: Marker fehlen oder doppelt")
        block = gesuch.split(start, 1)[1].split(end, 1)[0]
        pages = MARK.findall(block)
        pointer = re.compile(
            r"<!-- F4-VERSCHOBEN:" + re.escape(key) + r" [^\n]*-->\n"
            + r"".join(r"(Vergleich: " + re.escape(p) + r" \|[^\n]*\n)" for p in pages)
        )
        found = list(pointer.finditer(pilot))
        if len(found) != 1:
            raise AssertionError(f"Block {key}: Verweis in der bisherigen Datei fehlt oder doppelt")
        restored = block
        for line in found[0].groups():
            restored = MARK.sub(lambda _m: line, restored, count=1)
        pilot = pilot[: found[0].start()] + restored + pilot[found[0].end():]
    return pilot


class GesuchSplitLossTest(unittest.TestCase):
    def setUp(self) -> None:
        self.pilot = PILOT.read_text(encoding="utf-8")
        self.gesuch = GESUCH.read_text(encoding="utf-8")

    def test_original_is_restorable_byte_for_byte(self) -> None:
        self.assertEqual(git_blob(restore(self.pilot, self.gesuch)), ORIGINAL_BLOB)

    def moved_blocks(self) -> str:
        """Nur die verschobenen Transkriptionsblöcke, ohne spätere Arbeitsabschnitte."""
        return "".join(
            self.gesuch.split(f"<!-- F4-START:{k} -->\n", 1)[1].split(f"<!-- F4-END:{k} -->\n", 1)[0]
            for k in KEYS
        )

    def test_all_physical_rows_moved_once(self) -> None:
        rows = [m.group(0) for m in ROW.finditer(self.moved_blocks())]
        self.assertEqual(len(rows), 97)
        self.assertEqual(len(set(rows)), 97, "keine doppelten Zeilen-IDs")
        self.assertEqual(ROW.findall(self.pilot), [], "keine Gesuch-Zeilen mehr in der bisherigen Datei")

    def test_comparison_lines_stay_where_the_checker_reads_them(self) -> None:
        restored = restore(self.pilot, self.gesuch)
        self.assertEqual(VERGLEICH.findall(self.pilot), VERGLEICH.findall(restored))
        self.assertEqual(VERGLEICH.findall(self.gesuch), [], "Vergleichszeilen nur in der bisherigen Datei")

    def test_counter_case_detects_loss(self) -> None:
        damaged = self.gesuch.replace("Allergnädigster Herr!", "Allergnädigster Herr", 1)
        self.assertNotEqual(git_blob(restore(self.pilot, damaged)), ORIGINAL_BLOB)


if __name__ == "__main__":
    unittest.main()
