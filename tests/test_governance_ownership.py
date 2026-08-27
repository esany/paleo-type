from __future__ import annotations

import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class GovernanceOwnershipRegressionTests(unittest.TestCase):
    def test_material_change_admission_owner_is_maintenance(self) -> None:
        decisions = (REPO / "DECISIONS.md").read_text(encoding="utf-8")
        maintenance = (REPO / "methodology" / "maintenance.md").read_text(encoding="utf-8")
        ai_governance = (REPO / "methodology" / "ai-governance.md").read_text(encoding="utf-8")

        self.assertIn(
            "`methodology/maintenance.md` is the canonical operational owner of the general admission rule",
            decisions,
        )
        self.assertIn(
            "This file is the canonical operational owner of the general consequence-based admission workflow",
            maintenance,
        )
        self.assertIn(
            "The canonical general material research-system change-admission workflow is owned by `methodology/maintenance.md`",
            ai_governance,
        )
        self.assertNotIn(
            "`methodology/ai-governance.md` is the canonical operational owner of this admission rule",
            decisions,
        )


if __name__ == "__main__":
    unittest.main()
