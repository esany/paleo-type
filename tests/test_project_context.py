from __future__ import annotations

import csv
import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


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
        refs = result["canonical_references"]
        self.assertIn("projects/ega-reg-ii-3/project.yml", refs["project_files"])
        self.assertIn("projects/ega-reg-ii-3/STATUS.md", refs["project_files"])
        self.assertIn("projects/ega-reg-ii-3/source-uses.tsv", refs["project_files"])

    def test_reg_ii_5_context_uses_target_historical_state_without_promoting_it(self) -> None:
        result = self.compile("ega-reg-ii-5-knau")
        self.assertEqual("ACT-THHSTAW-EGA-REG-II-5", result["documentary_anchor"]["source_id"])
        self.assertNotIn("legacy_project_source_uses", result)
        self.assertEqual(4, len(result["project_source_uses"]))
        principal = next(
            row for row in result["project_source_uses"]
            if row["use"]["use_id"] == "USE-REGII5-00000129-PRINCIPAL"
        )
        self.assertEqual("historical", principal["use"]["status"])
        self.assertEqual("principal", principal["use"]["research_function"])
        self.assertEqual("FILE-REG-II-5-00000129-EXCERPT", principal["evidence"][0]["file"]["file_id"])
        self.assertIn("No owner-selected manuscript/source-research task is currently recorded", result["canonical_status"]["text"])
        self.assertIn("No current diplomatic transcription of Reg. Ii 5 is declared", result["canonical_status"]["text"])
        self.assertIn("research_function from structural containment", result["execution_boundary"]["do_not_infer"])
        self.assertIn(
            "witness attribution of legacy diplomatic material from project path, page_id or textual similarity",
            result["execution_boundary"]["do_not_infer"],
        )
        readiness = {
            item["file"]["file_id"]: item["evidence_readiness"]["research_ready_now"]
            for item in result["internal_source_files"]
        }
        self.assertIn("FILE-REG-II-5-00000129-EXCERPT", readiness)
        self.assertEqual("NOT_ESTABLISHED", readiness["FILE-REG-II-5-00000129-EXCERPT"])

    def test_reg_ii_5_context_preserves_all_canonical_use_and_evidence_references(self) -> None:
        result = self.compile("ega-reg-ii-5-knau")
        canonical_uses = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "source-uses.tsv")
        canonical_evidence = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "use-evidence.tsv")

        compiled_use_ids = {
            item["use"]["use_id"] for item in result["project_source_uses"]
        }
        compiled_evidence_ids = {
            evidence["evidence"]["evidence_id"]
            for item in result["project_source_uses"]
            for evidence in item["evidence"]
        }
        self.assertEqual({row["use_id"] for row in canonical_uses}, compiled_use_ids)
        self.assertEqual({row["evidence_id"] for row in canonical_evidence}, compiled_evidence_ids)

        refs = result["canonical_references"]
        self.assertIn("projects/ega-reg-ii-5-knau/source-uses.tsv", refs["project_files"])
        self.assertIn("projects/ega-reg-ii-5-knau/research/use-evidence.tsv", refs["project_files"])
        self.assertIn("projects/ega-reg-ii-5-knau/research/legacy-witness-provenance.tsv", refs["project_files"])
        self.assertEqual(
            {row["source_id"] for row in canonical_uses},
            set(row["use"]["source_id"] for row in result["project_source_uses"]),
        )
        self.assertTrue({row["file_id"] for row in canonical_evidence}.issubset(set(refs["file_ids"])))

    def test_context_does_not_promote_historical_use_to_current_scope_or_action(self) -> None:
        result = self.compile("ega-reg-ii-5-knau")
        project = result["project_definition"]
        self.assertIn("No owner-selected active", project["active_scope"])
        self.assertIn("must not be promoted as Li 5 evidence without fresh witness-specific verification", project["active_scope"])
        self.assertTrue(all(item["use"]["status"] == "historical" for item in result["project_source_uses"]))
        self.assertIn("must not invent one", result["execution_boundary"]["note"])


if __name__ == "__main__":
    unittest.main()
