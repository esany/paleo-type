from __future__ import annotations

import csv
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


class HistoricalRecoveryAssuranceTests(unittest.TestCase):
    def test_current_owner_authority_is_separate_from_retrospective_d017_claim(self) -> None:
        decisions = (REPO / "DECISIONS.md").read_text(encoding="utf-8")
        admission = (REPO / "requirements" / "source-project-owner-admission-2026-09-02.md").read_text(encoding="utf-8")

        self.assertIn("D-017 — Project materialization and boundary are human-owner decisions", decisions)
        self.assertIn("historical decision record under authority audit", decisions)
        self.assertIn("does **not** independently prove", decisions)
        self.assertIn("D-018 — Projects are purpose-established", decisions)
        self.assertIn("accepted by explicit human owner decision on 2026-09-02", decisions)
        self.assertIn("RETROSPECTIVE AUTHORITY", admission)
        self.assertIn("CURRENT OWNER INTENT / AUTHORITY", admission)
        self.assertIn("not retrospectively", admission.lower())

    def test_removed_source_unit_work_state_remains_visible_without_restoring_wrappers(self) -> None:
        li3 = (REPO / "projects" / "ega-reg-ii-3" / "STATUS.md").read_text(encoding="utf-8")
        li4 = (REPO / "projects" / "ega-reg-ii-4-bd-ii" / "STATUS.md").read_text(encoding="utf-8")
        li5 = (REPO / "projects" / "ega-reg-ii-5-knau" / "STATUS.md").read_text(encoding="utf-8")
        projects_readme = (REPO / "projects" / "README.md").read_text(encoding="utf-8")

        self.assertIn("699fa6eada61db483dfca950193412715d9603a5", li3)
        self.assertIn("not activated for full diplomatic transcription", li3)
        self.assertIn("no detailed page/folio crosswalk", li3)
        self.assertIn("Knaw Kirch Einkommen", li3)
        self.assertIn("fol. 304r / export image 625", li3)

        self.assertIn("699fa6eada61db483dfca950193412715d9603a5", li4)
        self.assertIn("not activated for source-wide work", li4)
        self.assertIn("independent reading", li4)

        self.assertIn("251ce9ed39e04bb852e0232dbcce21c68bd4c3a7", li5)
        self.assertIn("08c08bd6f90635210fbeff3f2d19cd0a485cc0b9", li5)
        self.assertIn("not activated for source-wide transcription", li5)
        self.assertIn("No new manuscript/source-research task is selected", li5)

        self.assertIn("source-unit", projects_readme.lower())
        self.assertIn("STATUS", projects_readme)

    def test_recovery_checkpoint_is_compare_boundary_not_rollback_truth(self) -> None:
        admission = (REPO / "requirements" / "source-project-owner-admission-2026-09-02.md").read_text(encoding="utf-8")
        self.assertIn("e8a7235bff875bf2c191c96c41638c4095f7ec76", admission)
        self.assertIn("not a baseline-truth or rollback anchor", admission)

    def test_reg_ii_5_file_coverage_and_source_crosswalk_boundary_remain_distinct(self) -> None:
        files = read_tsv(REPO / "corpus" / "files.tsv")
        parent = next(row for row in files if row["file_id"] == "FILE-REG-II-5-00000129-EXCERPT")
        self.assertIn("120-143", parent["filename"])

        crosswalk = read_tsv(
            REPO / "corpus" / "source-data" / "THHSTAW-EGA-REG-II-5-STAT-VIS-00000129" / "crosswalk.tsv"
        )
        export_images = [int(row["export_image"]) for row in crosswalk if row.get("export_image", "").isdigit()]
        self.assertEqual(120, min(export_images))
        self.assertEqual(142, max(export_images))
        self.assertNotIn(143, export_images)

        admission = (REPO / "requirements" / "source-project-owner-admission-2026-09-02.md").read_text(encoding="utf-8")
        self.assertIn("File covers export images 120–143", admission)
        self.assertIn("canonical Source crosswalk maps 120–142", admission)
        self.assertIn("image 143 / fol. 67r is adjacent File context outside the Source boundary", admission)

    def test_legacy_role_and_relevance_information_is_not_removed_before_loss_checked_mapping(self) -> None:
        legacy = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "sources" / "sources.tsv")
        self.assertEqual({"principal", "comparison", "control", "context"}, {row["project_role"] for row in legacy})

        sources = read_tsv(REPO / "corpus" / "sources.tsv")
        self.assertTrue(any(row.get("relevance") for row in sources))

        migration = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "project-source-migration.tsv")
        relevance = [row for row in migration if row["fixture_id"].startswith("CORPUS-REL-")]
        self.assertTrue(relevance)
        self.assertTrue(all(row["transformation"] == "remove-after-loss-checked-migration" for row in relevance))


if __name__ == "__main__":
    unittest.main()
