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
        self.assertIn("certify historical d-017 authority retroactively", admission.lower())
        self.assertIn("must not be rewritten as proof", admission.lower())

    def test_current_project_scopes_require_owner_selection_and_do_not_promote_legacy_knau(self) -> None:
        li3 = (REPO / "projects" / "ega-reg-ii-3" / "project.yml").read_text(encoding="utf-8")
        li4 = (REPO / "projects" / "ega-reg-ii-4-bd-ii" / "project.yml").read_text(encoding="utf-8")
        li5 = (REPO / "projects" / "ega-reg-ii-5-knau" / "project.yml").read_text(encoding="utf-8")

        self.assertIn("No owner-selected active scholarly scope is currently recorded", li3)
        self.assertIn("previously inspected Knau-related sections", li3)
        self.assertIn("Owner-selected 2026-09-03", li4)
        self.assertIn("THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089", li4)
        self.assertIn("fol. 306v–309r / export images 667–672", li4)
        self.assertIn("completed through #96–#99 on 2026-09-06", li4)
        self.assertIn("No owner-selected active scholarly scope is currently recorded", li4)
        self.assertIn("historical principal/comparison uses remain preserved", li4)
        self.assertIn("Human Owner selected #166 on 2026-09-12", li5)
        self.assertIn("62r-L19–25", li5)
        self.assertIn("62v-L01–L07", li5)
        self.assertIn("analysis unit is not pre-established", li5)
        self.assertIn("#165 is reopened", li5)
        self.assertIn("R0 is a REAL BLOCKER", li5)
        self.assertIn("G3 remains reached at the current internal-evidence level", li5)
        self.assertIn("G4 unchanged", li5)
        self.assertIn("no G5/G6", li5)
        self.assertIn("no G5/G6, source-wide continuation or 62v-L08–L25 follow-up is authorized", li5)
        self.assertNotIn("completed and working Knau locus research remains preserved", li5)

    def test_reg_ii_3_4_5_source_hierarchy_stays_explicit(self) -> None:
        relationships = read_tsv(REPO / "corpus" / "relationships.tsv")
        part_of = {(row["subject_id"], row["object_id"]) for row in relationships if row["predicate"] == "part_of"}
        self.assertIn(("THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V", "ACT-THHSTAW-EGA-REG-II-3"), part_of)
        self.assertIn(("THHSTAW-EGA-REG-II-3-STAT-VIS-00000235", "ACT-THHSTAW-EGA-REG-II-3"), part_of)
        self.assertIn(("THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089", "ACT-THHSTAW-EGA-REG-II-4-BD-II"), part_of)
        self.assertIn(("THHSTAW-EGA-REG-II-5-STAT-VIS-00000129", "ACT-THHSTAW-EGA-REG-II-5"), part_of)

        readme = (REPO / "projects" / "README.md").read_text(encoding="utf-8")
        self.assertIn("separate material Sources/witnesses", readme)
        self.assertIn("fol. 306v–309r / export images 667–672", readme)
        self.assertIn("fol. 55v–66v", readme)

    def test_legacy_diplomatic_material_is_quarantined_from_current_li5_truth(self) -> None:
        li5 = (REPO / "projects" / "ega-reg-ii-5-knau" / "STATUS.md").read_text(encoding="utf-8")
        project = (REPO / "projects" / "ega-reg-ii-5-knau" / "project.yml").read_text(encoding="utf-8")
        projects_readme = (REPO / "projects" / "README.md").read_text(encoding="utf-8")
        provenance = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "legacy-witness-provenance.tsv")

        self.assertIn("Legacy diplomatic material — verification/recovery only", li5)
        self.assertIn("not canonical current Reg. Ii 5 diplomatic transcription state", li5)
        self.assertIn("witness attribution unresolved or potentially mixed", li5)
        self.assertIn("Current Reg. Ii 5 diplomatic truth is owned by `transcription/first-reading/*.tsv`", li5)
        self.assertIn("Later exact-source G2 research artifacts — bounded direct authority", li5)
        self.assertIn("None validates legacy `transcription/132.tsv`–`135.tsv` row-by-row", li5)
        self.assertIn("not canonical current transcription state", project)
        self.assertIn("legacy verification/recovery evidence", projects_readme)
        self.assertIn("witness-specific scientific use requires fresh Source/File/locus verification", projects_readme)

        by_path = {row["legacy_path"]: row for row in provenance}
        self.assertNotIn("research/g2-*", by_path)
        self.assertEqual("direct-source-provenance-evidence", by_path["research/g2-baseline-provenance.md"]["current_classification"])
        self.assertEqual("direct-source-observation-evidence", by_path["research/g2-checkpoint-a-physical-inventory.md"]["current_classification"])
        self.assertEqual("source-bound-semantic-loss-evidence", by_path["research/g2-checkpoint-b-semantic-loss.md"]["current_classification"])
        self.assertEqual("source-bound-domain-review-evidence", by_path["research/g2-domain-review-checkpoint-b.md"]["current_classification"])
        self.assertTrue(all("legacy reading" not in row["allowed_use"].lower() for path, row in by_path.items() if path.startswith("research/g2-")))

    def test_method_and_migration_do_not_repromote_legacy_g2_as_li5_witness_truth(self) -> None:
        lifecycle = (REPO / "methodology" / "project-lifecycle.md").read_text(encoding="utf-8")
        self.assertIn("verification/recovery evidence and a systems/methodology falsification fixture", lifecycle)
        self.assertIn("must each be re-established from their own canonical Source/File/locus", lifecycle)
        self.assertNotIn("The preserved Reg. Ii 5/Knau work remains valid project work", lifecycle)

        migration = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "project-source-migration.tsv")
        by_id = {row["fixture_id"]: row for row in migration}
        ambiguous_ids = {
            "TRANS-132", "TRANS-133", "TRANS-134", "TRANS-135",
            "APPARATUS-001", "LEXICON-001", "NUM-IJ", "NUM-1", "NUM-80",
            "NUM-VIERTEL", "NUM-GROSCH", "NUM-PFENNIG",
            "NUM-W1", "NUM-W2", "NUM-W3", "NUM-W4", "NUM-W5", "NUM-W6",
        }
        for fixture_id in ambiguous_ids:
            row = by_id[fixture_id]
            self.assertIn("legacy-witness-provenance.tsv", row["target_location"])
            self.assertEqual("reclassified-2026-09-02", row["status"])
            self.assertNotIn("Reg. Ii 5 internal source-specific scholarly work", row["target_location"])

        c2 = by_id["NUM-C2"]
        self.assertIn("USE-REGII3-00000235-NOTATION-CONTROL", c2["target_location"])
        self.assertEqual("preserved-linked-2026-09-02", c2["status"])

        inspection = by_id["INSPECTION-STATUS-001"]
        self.assertEqual("corrected-2026-09-02", inspection["status"])
        self.assertIn("partially-transcribed to images-inspected", inspection["loss_test"])

        sources = read_tsv(REPO / "corpus" / "sources.tsv")
        li5_source = next(row for row in sources if row["source_id"] == "THHSTAW-EGA-REG-II-5-STAT-VIS-00000129")
        self.assertEqual("images-inspected", li5_source["inspection_status"])

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
        self.assertIn("699fa6eada61db483dfca950193412715d9603a5", li5)
        self.assertIn("That bounded work package was completed on 2026-09-08 as an **Editionsbaustein**", li5)
        self.assertIn("Current Reg. Ii 5 diplomatic truth is owned by `transcription/first-reading/*.tsv`", li5)
        self.assertIn("#123 problem-focused internal relecture | `complete`", li5)
        self.assertIn("H re-tested", li5)
        self.assertIn("xxxij", li5)
        self.assertIn("#165 analysis-unit reconciliation | `reopened — current executable support action`", li5)
        self.assertIn("#166 relation/function adjudication | `owner-selected / paused — R0 REAL BLOCKER`", li5)
        self.assertIn("STAGED = FAIL", li5)
        self.assertIn("VISION-INSPECTABLE = NOT TESTABLE", li5)
        self.assertIn("research/internal-comparanda-relecture-61v-63r.md", li5)
        self.assertIn("research/source-understanding-synthesis-61v-63r.md", li5)

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

    def test_role_and_relevance_cleanup_occurs_only_with_loss_checked_target_mapping(self) -> None:
        self.assertFalse((REPO / "projects" / "ega-reg-ii-5-knau" / "sources" / "sources.tsv").exists())

        uses = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "source-uses.tsv")
        self.assertEqual(
            {"principal", "textual-comparison", "notation-control", "historical-context"},
            {row["research_function"] for row in uses},
        )
        by_function = {row["research_function"]: row for row in uses}
        self.assertEqual("active", by_function["principal"]["status"])
        self.assertEqual("fol. 61v–63r", by_function["principal"]["relevant_locus"])
        self.assertIn("#123 completed 2026-09-12", by_function["principal"]["evidence_basis"])
        self.assertIn("Human Owner selected bounded cross-folio research #166", by_function["principal"]["evidence_basis"])
        self.assertIn("analysis unit is not pre-established", by_function["principal"]["notes"])
        self.assertIn("R0-blocked", by_function["principal"]["notes"])
        self.assertEqual("historical", by_function["textual-comparison"]["status"])
        self.assertEqual("historical", by_function["notation-control"]["status"])
        self.assertEqual("historical", by_function["historical-context"]["status"])
        self.assertTrue(all("loss-checked migration 2026-09-02" in row["evidence_basis"] for row in uses))

        evidence = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "use-evidence.tsv")
        self.assertEqual(4, len(evidence))
        by_evidence = {row["evidence_id"]: row for row in evidence}
        principal_evidence = by_evidence["EVID-REGII5-00000129-PRINCIPAL"]
        self.assertEqual("active", principal_evidence["status"])
        self.assertIn("#123 completed 2026-09-12", principal_evidence["evidence_basis"])
        self.assertIn("reactivated for Human-Owner-selected #166", principal_evidence["evidence_basis"])
        self.assertIn("REAL BLOCKER", principal_evidence["notes"])
        self.assertEqual("historical", by_evidence["EVID-REGII4-00000089-TEXTUAL-COMPARISON"]["status"])
        self.assertEqual("historical", by_evidence["EVID-REGII3-00000235-NOTATION-CONTROL"]["status"])
        self.assertEqual("historical", by_evidence["EVID-REGII3-NEUSTADT-HISTORICAL-CONTEXT"]["status"])

        sources = read_tsv(REPO / "corpus" / "sources.tsv")
        self.assertTrue(all(not row.get("relevance") for row in sources))
        self.assertTrue(all(row.get("inspection_status") for row in sources))

        migration = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "project-source-migration.tsv")
        relevance = [row for row in migration if row["fixture_id"].startswith("CORPUS-REL-")]
        self.assertEqual(7, len(relevance))
        self.assertTrue(all(row["transformation"] == "remove-after-loss-checked-migration" for row in relevance))


if __name__ == "__main__":
    unittest.main()
