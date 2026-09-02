from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class ProjectContextRegressionTests(unittest.TestCase):
    def compile(self, project_id: str) -> dict:
        proc = subprocess.run(
            [sys.executable, str(REPO / "tools" / "project_context.py"), "--project", project_id],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, proc.returncode, proc.stderr)
        return json.loads(proc.stdout)

    def test_reg_ii_3_context_is_derived_and_preserves_no_current_task(self) -> None:
        result = self.compile("ega-reg-ii-3")
        self.assertEqual("DERIVED_PROJECT_CONTEXT", result["view"])
        self.assertFalse(result["canonical"])
        self.assertEqual("ACT-THHSTAW-EGA-REG-II-3", result["documentary_anchor"]["source_id"])
        internal_ids = {row["source_id"] for row in result["internal_sources"]}
        self.assertIn("THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V", internal_ids)
        self.assertIn("THHSTAW-EGA-REG-II-3-STAT-VIS-00000235", internal_ids)
        self.assertEqual([], result["project_source_uses"])
        self.assertIn("No owner-selected manuscript/source-research task is currently recorded", result["canonical_status"]["text"])
        self.assertIn("must not invent one", result["execution_boundary"]["note"])

    def test_reg_ii_5_context_preserves_legacy_state_without_promoting_it(self) -> None:
        result = self.compile("ega-reg-ii-5-knau")
        self.assertEqual("ACT-THHSTAW-EGA-REG-II-5", result["documentary_anchor"]["source_id"])
        self.assertTrue(result["legacy_project_source_uses"])
        self.assertEqual([], result["project_source_uses"])
        self.assertIn("No new owner-selected manuscript/source-research task is currently recorded", result["canonical_status"]["text"])
        self.assertIn("research_function from structural containment", result["execution_boundary"]["do_not_infer"])
        readiness = {
            item["file"]["file_id"]: item["evidence_readiness"]["research_ready_now"]
            for item in result["internal_source_files"]
        }
        self.assertIn("FILE-REG-II-5-00000129-EXCERPT", readiness)
        self.assertEqual("NOT_ESTABLISHED", readiness["FILE-REG-II-5-00000129-EXCERPT"])


if __name__ == "__main__":
    unittest.main()
