from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class GovernanceOwnershipRegressionTests(unittest.TestCase):
    def test_material_change_admission_owner_is_maintenance(self) -> None:
        """Keep the one existing positive prose-owner regression for D-016.

        This is intentionally narrow: it protects the demonstrated ownership split
        between maintenance and AI governance, not general document wording.
        """
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

    def test_project_contract_v8_closes_purpose_owner_and_legacy_gaps(self) -> None:
        contract = json.loads((REPO / "corpus" / "source-contract.json").read_text(encoding="utf-8"))
        projects = contract["tables"]["projects"]

        self.assertEqual(8, contract["version"])
        self.assertIn("research_object", projects["required_keys"])
        self.assertIn("active_scope", projects["required_keys"])
        self.assertEqual(["source-uses.tsv"], projects["allowed_source_registers"])
        self.assertIn("principal_source_id", projects["forbidden_legacy_keys"])
        self.assertEqual("projects/*/sources/sources.tsv", projects["legacy_source_register_glob"])

    def test_project_templates_do_not_regenerate_source_first_or_forced_next_action(self) -> None:
        template = (REPO / "templates" / "project" / "project.yml").read_text(encoding="utf-8")
        status_template = (REPO / "templates" / "project" / "STATUS.md").read_text(encoding="utf-8")

        # These are demonstrated generative failure fixtures, not a general prose schema.
        self.assertNotIn("why this historically independent source structure is being worked on", template)
        self.assertIn('source_register: "source-uses.tsv"', template)
        self.assertIn("REQUIRED after Project selection", template)
        self.assertIn("only when an authorized next action exists", status_template)
        self.assertNotIn("State one bounded next research action.\n", status_template)

    def test_source_assurance_runs_without_semantic_path_filter(self) -> None:
        workflow = (REPO / ".github" / "workflows" / "source-contract.yml").read_text(encoding="utf-8")
        self.assertIn("pull_request:\n", workflow)
        self.assertNotIn("paths:", workflow)
        self.assertIn("formal/deterministic consistency", workflow)
        self.assertIn("does **not** by itself establish manuscript truth", workflow)

    def test_known_stale_governance_failures_do_not_reenter_binding_surfaces(self) -> None:
        """Target only failure strings that actually caused/encoded observed drift.

        This must not grow into a generic lexical governance checker. Add a string
        here only when a concrete stale-propagation failure has been demonstrated.
        """
        agents = (REPO / "AGENTS.md").read_text(encoding="utf-8")
        readme = (REPO / "README.md").read_text(encoding="utf-8")
        maintenance = (REPO / "methodology" / "maintenance.md").read_text(encoding="utf-8")
        provenance = (REPO / "methodology" / "source-and-provenance.md").read_text(encoding="utf-8")
        operational = (REPO / "methodology" / "workflow.md").read_text(encoding="utf-8")
        milestones = (REPO / "MILESTONES.md").read_text(encoding="utf-8")
        gates = (REPO / "methodology" / "research-gates.md").read_text(encoding="utf-8")

        self.assertNotIn("Project identity follows historical structure", agents)
        self.assertNotIn("read project `sources/sources.tsv`", agents)
        self.assertNotIn("project `sources/sources.tsv`", operational)
        self.assertNotIn("project `sources/sources.tsv`", provenance)
        self.assertNotIn("preservation-blocked-rights", maintenance)
        self.assertNotIn("preservation-blocked-rights", operational)
        self.assertNotIn("The current Knau project is at G2", milestones)
        self.assertNotIn("rejected semantic/fluent reconstructions do not re-enter without new evidence", gates)
        self.assertNotIn("Knau` is the current working focus", readme)

    def test_readme_does_not_copy_project_current_scope_or_next_action(self) -> None:
        readme = (REPO / "README.md").read_text(encoding="utf-8")

        # README may enumerate Project directories for navigation, but not current
        # Project scope/gate/task truth.
        self.assertNotIn("## Current active scope", readme)
        self.assertNotIn("Current active scope:", readme)
        self.assertNotIn("The current Knau project is at G2", readme)
        self.assertIn("Do not copy current Project scope/gate/`NEXT ACTION` into this README", readme)


if __name__ == "__main__":
    unittest.main()
