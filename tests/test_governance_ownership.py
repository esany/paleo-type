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


if __name__ == "__main__":
    unittest.main()
