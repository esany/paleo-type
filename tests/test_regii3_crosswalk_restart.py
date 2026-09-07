from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class RegIi3CrosswalkRestartTests(unittest.TestCase):
    def test_neustadt_crosswalk_is_exposed_without_creating_research_priority(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(REPO / "tools" / "project_context.py"), "--project", "ega-reg-ii-3"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, proc.returncode, proc.stderr)
        result = json.loads(proc.stdout)

        self.assertIn(
            "corpus/source-data/THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V/crosswalk.tsv",
            result["canonical_references"]["crosswalk_paths"],
        )
        status = result["canonical_status"]["text"]
        self.assertIn("fol. 41r–63v ↔ export images 83–128 ↔ PDF pages 2–47", status)
        self.assertIn("recto rows 41r–63r are `observed`", status)
        self.assertIn("paired verso rows 41v–63v are `inferred-high`", status)
        self.assertIn("No owner-selected manuscript/source-research task is currently recorded", status)


if __name__ == "__main__":
    unittest.main()
