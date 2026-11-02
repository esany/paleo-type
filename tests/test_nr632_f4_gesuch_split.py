"""Exact-loss check for the Nr. 632 F4 petition extraction (not a reading validator)."""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "projects/ssta-20578-nr-632/research"
OLD_OWNER = RESEARCH / "transcription-pilot-0102R-0103L-2026-10-30.md"
GESUCH = RESEARCH / "gesuch-0104R-0107L.md"
F1_ROW = re.compile(r"(?m)^\|\s*`(0104R|0105L|0105R|0106L|0106R|0107L)-([^`]+)`\s*\|")
# Hashes are of exact pre-extraction source blocks in research PR #359 at 7c22474.
BLOCKS = (
    ("0104R", "e3a7517bc46f74a1c5da87333de505827d19d1eb29a41101da860ed9220021fc", 14),
    ("0105-0107", "fff18a5c2a58806843bde6fa3bd583a07b5f88c591029b2e9af1ad8c0b932e22", 83),
    ("F1-bilanz", "44659c390e28de60bc2657662d6330bc2abbb4269a0b6b5a201ba850ec3ca83c", 0),
)


class GesuchF4LossTest(unittest.TestCase):
    def test_full_original_blocks_preserved_and_not_duplicated(self):
        self.assertTrue(GESUCH.is_file(), "F4 requires a separate petition owner")
        self.assertTrue(OLD_OWNER.is_file())
        gesuch = GESUCH.read_text(encoding="utf-8")
        old = OLD_OWNER.read_text(encoding="utf-8")
        rows = []
        for key, expected_hash, count in BLOCKS:
            left = "<!-- F4-START:" + key + " -->\n"
            right = "<!-- F4-END:" + key + " -->\n"
            self.assertEqual(gesuch.count(left), 1, key)
            self.assertEqual(gesuch.count(right), 1, key)
            chunk = gesuch.split(left, 1)[1].split(right, 1)[0]
            self.assertEqual(hashlib.sha256(chunk.encode("utf-8")).hexdigest(), expected_hash, key)
            self.assertEqual(len(F1_ROW.findall(chunk)), count, key)
            rows.extend(m.group(0) for m in F1_ROW.finditer(chunk))
            # The original block header must no longer appear in the former monolith.
            first_heading = chunk.splitlines()[0]
            self.assertNotIn(first_heading, old)
        self.assertEqual(len(rows), 97)
        self.assertEqual(len(set(rows)), 97, "no duplicate physical writing row IDs")
        self.assertEqual(F1_ROW.findall(old), [], "no F1 line rows remain in old owner")
        self.assertEqual(len(F1_ROW.findall(gesuch)), 97, "all F1 rows are in one F4 owner")


    def test_unrelated_research_owner_bytes_preserved(self):
        """Also protect all other 0102/0103 and 0108–0131 material from loss."""
        payload = OLD_OWNER.read_bytes()
        git_blob = hashlib.sha1(b"blob " + str(len(payload)).encode() + bytes([0]) + payload).hexdigest()
        self.assertEqual(git_blob, "bb4f209c1f6a68dfd2a7433e08bcb3615e8d7c4c")



if __name__ == "__main__":
    unittest.main()
