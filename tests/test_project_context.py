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

    def test_reg_ii_4_context_preserves_completed_uses_without_current_priority(self) -> None:
        result = self.compile("ega-reg-ii-4-bd-ii")
        self.assertEqual("ACT-THHSTAW-EGA-REG-II-4-BD-II", result["documentary_anchor"]["source_id"])
        self.assertIn("No owner-selected active scholarly scope is currently recorded", result["project_definition"]["active_scope"])
        self.assertEqual(2, len(result["project_source_uses"]))
        by_function = {item["use"]["research_function"]: item for item in result["project_source_uses"]}
        self.assertEqual({"principal", "textual-comparison"}, set(by_function))
        self.assertTrue(all(item["use"]["status"] == "historical" for item in result["project_source_uses"]))
        self.assertEqual(
            "FILE-REG-II-4-II-00000089-EXPORT",
            by_function["principal"]["evidence"][0]["file"]["file_id"],
        )
        self.assertEqual(
            "FILE-REG-II-5-00000129-EXCERPT",
            by_function["textual-comparison"]["evidence"][0]["file"]["file_id"],
        )
        self.assertIn("No owner-selected next manuscript/source-research target is currently recorded", result["canonical_status"]["text"])

    def test_reg_ii_5_context_exposes_active_relecture_without_legacy_promotion(self) -> None:
        result = self.compile("ega-reg-ii-5-knau")
        self.assertEqual("ACT-THHSTAW-EGA-REG-II-5", result["documentary_anchor"]["source_id"])
        self.assertNotIn("legacy_project_source_uses", result)
        self.assertEqual(4, len(result["project_source_uses"]))
        principal = next(
            row for row in result["project_source_uses"]
            if row["use"]["use_id"] == "USE-REGII5-00000129-PRINCIPAL"
        )
        self.assertEqual("active", principal["use"]["status"])
        self.assertEqual("principal", principal["use"]["research_function"])
        self.assertEqual("fol. 61v–63r", principal["use"]["relevant_locus"])
        self.assertEqual("FILE-REG-II-5-00000129-EXCERPT", principal["evidence"][0]["file"]["file_id"])
        self.assertEqual("active", principal["evidence"][0]["evidence"]["status"])
        active_scope = result["project_definition"]["active_scope"]
        self.assertIn("#123 problembezogene interne Relektüre", active_scope)
        self.assertIn("Editionslocus remains fol. 61v–63r", active_scope)
        self.assertIn("fol. 55v–66v", active_scope)
        self.assertIn("does not authorize source-wide transcription", active_scope)
        status = result["canonical_status"]["text"]
        self.assertIn("#115 source-exact editorial work package | `complete`", status)
        self.assertIn("current Reg. Ii 5 diplomatic truth is owned by `transcription/first-reading/*.tsv`", status)
        self.assertIn("Legacy diplomatic material — verification/recovery only", status)
        self.assertIn("G4 controlled comparison", status)
        self.assertIn("#123 remains the current owner-selected active scholarly work package", status)
        self.assertIn("WP-R1 is complete; no pixel-dependent manuscript reading under #123 has yet begun", status)
        self.assertIn("target-context pixel readiness is **not yet re-established**", status)
        self.assertIn("G3 remains `reached at current internal evidence level` at #123 activation and after WP-R1", status)
        self.assertIn("WP-R2 — current-context evidence readiness for target cluster A", status)
        self.assertIn("research/internal-comparanda-relecture-61v-63r.md", status)
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

    def test_current_scope_reactivates_only_principal_use_without_legacy_or_comparison_promotion(self) -> None:
        result = self.compile("ega-reg-ii-5-knau")
        project = result["project_definition"]
        self.assertIn("#123 problembezogene interne Relektüre", project["active_scope"])
        self.assertIn("Editionslocus remains fol. 61v–63r", project["active_scope"])
        self.assertIn("fol. 55v–66v", project["active_scope"])
        by_id = {item["use"]["use_id"]: item["use"] for item in result["project_source_uses"]}
        self.assertEqual("active", by_id["USE-REGII5-00000129-PRINCIPAL"]["status"])
        self.assertEqual("fol. 61v–63r", by_id["USE-REGII5-00000129-PRINCIPAL"]["relevant_locus"])
        self.assertEqual("historical", by_id["USE-REGII4-00000089-TEXTUAL-COMPARISON"]["status"])
        self.assertEqual("historical", by_id["USE-REGII3-00000235-NOTATION-CONTROL"]["status"])
        self.assertEqual("historical", by_id["USE-REGII3-NEUSTADT-HISTORICAL-CONTEXT"]["status"])
        self.assertIn("current scholarly NEXT ACTION from historical work, active evidence or legacy labels", result["execution_boundary"]["do_not_infer"])


if __name__ == "__main__":
    unittest.main()
