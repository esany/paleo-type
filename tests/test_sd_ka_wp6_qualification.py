from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

from tools import engineering_context, engineering_fitness, prompt


REPO = Path(__file__).resolve().parents[1]


class SdKaWp6QualificationTests(unittest.TestCase):
    def test_terminal_real_state_composition(self) -> None:
        config = json.loads((REPO / "engineering" / "configuration.json").read_text(encoding="utf-8"))
        state = json.loads((REPO / "engineering" / "changes" / "SD-KA-01" / "STATE.json").read_text(encoding="utf-8"))

        self.assertEqual(["artifact:ENG-A-0004"], config["architecture_baselines"])
        self.assertEqual(["artifact:ENG-A-0008"], config["requirements_baselines"])
        self.assertEqual("github-issue:esany/paleo-type#261", config["change_states"]["change:SD-KA-01"]["work_owner"])
        self.assertEqual("pending", config["change_states"]["change:SD-KA-01"]["accepted_consequence"])
        self.assertEqual("github-issue:esany/paleo-type#261", config["current_focus"]["ref"])
        self.assertEqual("SD-KA-01/WP6", config["current_focus"]["scope"])

        self.assertEqual("reviewing", state["lifecycle"])
        self.assertEqual("implementing", state["work_package_status"]["WP6"])
        for package in ("WP1", "WP2", "WP3", "WP4", "WP5"):
            self.assertEqual("verified", state["work_package_status"][package])

        errors, human = engineering_context.compile_context(REPO, "human-system-overview")
        self.assertEqual([], errors)
        self.assertEqual("active", human["current_work"]["state"])
        self.assertEqual("github-issue:esany/paleo-type#261", human["current_work"]["work_ref"])
        self.assertIn("WP6 adversarial qualification", human["current_work"]["statement"])

        errors, developer = engineering_context.compile_context(REPO, "system-development-execution")
        self.assertEqual([], errors)
        self.assertEqual("implementation", developer["execution_contract"]["requested_activity"])
        self.assertEqual("python tools/check.py", developer["execution_contract"]["technical_verification"])
        self.assertEqual("github-issue:esany/paleo-type#244", developer["execution_contract"]["whole_system_return"])

        errors, review = engineering_context.compile_context(REPO, "architecture-review")
        self.assertEqual([], errors)
        basis = review["review_evidence_basis"]
        self.assertEqual("not-established", basis["independence_claim"])
        self.assertTrue(basis["inherited_premises"])

        errors, fitness = engineering_fitness.run_fitness(REPO)
        self.assertEqual([], errors)
        self.assertEqual("PASS", fitness["status"])
        self.assertEqual("active", fitness["checks"]["ENG-FIT-08"]["applicability"])

    def test_residual_and_migration_boundaries_survive_terminal_composition(self) -> None:
        findings = self._rows(REPO / "engineering" / "catalog" / "findings.tsv")
        by_id = {row["finding_id"]: row for row in findings}
        self.assertEqual("unresolved", by_id["F10"]["disposition"])
        self.assertEqual("unresolved", by_id["F17"]["disposition"])
        self.assertEqual("promoted", by_id["F45"]["disposition"])

        migration = self._rows(REPO / "engineering" / "changes" / "SD-KA-01" / "MIGRATION.tsv")
        legacy = self._rows(REPO / "engineering" / "catalog" / "legacy-paths.tsv")
        self.assertEqual(74, len(migration))
        self.assertEqual(74, len(legacy))
        for row in migration:
            self.assertFalse((REPO / row["legacy_path"]).exists())
            self.assertTrue((REPO / row["current_path"]).is_file())

    def test_prompt_self_review_boundary_survives_terminal_composition(self) -> None:
        repo_prompt = prompt.build_prompt(
            "Perform the currently authorized bounded engineering work.",
            repo="esany/paleo-type",
        )
        self.assertIn("GOVERNING_OBJECTIVE.md", repo_prompt)
        self.assertIn("python tools/check.py", repo_prompt)
        tested = prompt.test_prompt(
            "Review the SD-KA terminal result.",
            result="The same model independently validated the result in a fresh context.",
            self_review=True,
        )
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("independence-overclaim", tested["findings"])

    @staticmethod
    def _rows(path: Path) -> list[dict[str, str]]:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle, delimiter="\t"))


if __name__ == "__main__":
    unittest.main()
