from __future__ import annotations

import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class GovernanceOwnershipRegressionTests(unittest.TestCase):
    def test_material_change_admission_owner_is_maintenance(self) -> None:
        decisions = (REPO / "DECISIONS.md").read_text(encoding="utf-8")
        maintenance = (REPO / "methodology" / "maintenance.md").read_text(encoding="utf-8")
        ai_governance = (REPO / "methodology" / "ai-governance.md").read_text(encoding="utf-8")
        workflow = (
            "analysis → requirements → concept → owner review / explicit implementation admission "
            "→ development → deterministic tests / scholarly loss checks → result review"
        )

        self.assertIn(
            "`methodology/maintenance.md` is the canonical operational owner of the general admission rule",
            decisions,
        )
        self.assertIn(
            "| material research-system change-admission workflow | `methodology/maintenance.md` | canonical operational admission rule |",
            maintenance,
        )
        self.assertIn(
            "This file is the canonical operational owner of the general consequence-based admission workflow",
            maintenance,
        )
        self.assertIn(workflow, maintenance)
        self.assertIn(
            "The canonical general material research-system change-admission workflow is owned by `methodology/maintenance.md`",
            ai_governance,
        )
        self.assertNotIn(workflow, ai_governance)
        self.assertNotIn(
            "`methodology/ai-governance.md` is the canonical operational owner of this admission rule",
            decisions,
        )

    def test_project_template_keeps_purpose_separate_from_documentary_anchor(self) -> None:
        decisions = (REPO / "DECISIONS.md").read_text(encoding="utf-8")
        template = (REPO / "templates" / "project" / "project.yml").read_text(encoding="utf-8")
        status_template = (REPO / "templates" / "project" / "STATUS.md").read_text(encoding="utf-8")

        self.assertIn(
            "## D-018 — Projects are purpose-established; `project_source_id` is a post-selection documentary anchor",
            decisions,
        )
        self.assertIn("why this scholarly investigation/work container exists", template)
        self.assertIn("REQUIRED after Project selection", template)
        self.assertIn("scholarly research purpose that establishes this Project", template)
        self.assertNotIn("why this historically independent source structure is being worked on", template)
        self.assertIn("## Research purpose and Project authority", status_template)
        self.assertIn("## Documentary Source anchor", status_template)
        self.assertIn("after Project selection", status_template)
        self.assertIn("only when an authorized next action exists", status_template)

    def test_method_uses_target_project_use_owners_not_removed_reg_ii_5_compatibility(self) -> None:
        lifecycle = (REPO / "methodology" / "project-lifecycle.md").read_text(encoding="utf-8")
        provenance = (REPO / "methodology" / "source-and-provenance.md").read_text(encoding="utf-8")
        li5_project = (REPO / "projects" / "ega-reg-ii-5-knau" / "project.yml").read_text(encoding="utf-8")

        self.assertIn("Project→Source research function and source-relative relevant locus → `projects/<id>/source-uses.tsv`", lifecycle)
        self.assertIn("concrete Project-use→File evidence binding → `projects/<id>/research/use-evidence.tsv`", lifecycle)
        self.assertIn("Reg. Ii 5 completed structured-use migration", lifecycle)
        self.assertIn("old Project→Source register `sources/sources.tsv`", lifecycle)
        self.assertIn("are no longer canonical compatibility owners", lifecycle)
        self.assertIn("Project→Source research function/locus → project `source-uses.tsv`", provenance)
        self.assertIn("concrete Project-use→File binding → project `research/use-evidence.tsv`", provenance)
        self.assertNotIn("project source use/role/locus → project `sources/sources.tsv`", provenance)
        self.assertIn('source_register: "source-uses.tsv"', li5_project)
        self.assertNotIn("principal_source_id:", li5_project)

    def test_method_distinguishes_identity_from_research_ready_availability(self) -> None:
        provenance = (REPO / "methodology" / "source-and-provenance.md").read_text(encoding="utf-8")
        workflow = (REPO / "methodology" / "historical-source-workflow.md").read_text(encoding="utf-8")

        self.assertIn("Identifiability, reproducibility and research-ready availability are separate properties", provenance)
        self.assertIn("verify an actual authorized access path", provenance)
        self.assertIn("identifiability**, **reproducibility** and **research-ready availability", workflow)
        self.assertIn("does not prove that a fresh authorized work context can actually open the evidence", workflow)


if __name__ == "__main__":
    unittest.main()
