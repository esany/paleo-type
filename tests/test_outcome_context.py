from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class OutcomeContextRegressionTests(unittest.TestCase):
    def compile(self, *args: str, expected_rc: int = 0) -> dict:
        proc = subprocess.run(
            [sys.executable, str(REPO / "tools" / "outcome_context.py"), *args],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(expected_rc, proc.returncode, proc.stderr or proc.stdout)
        payload = proc.stdout if proc.returncode == 0 else proc.stderr
        return json.loads(payload)

    def test_corpus_only_context_does_not_materialize_project_or_work(self) -> None:
        result = self.compile()
        self.assertEqual("DERIVED_OUTCOME_CONTROL_CONTEXT", result["view"])
        self.assertFalse(result["canonical"])
        self.assertIsNone(result["project_id"])
        self.assertEqual("NO_PROJECT", result["authority_binding"]["status"])
        self.assertFalse(result["authority_binding"]["work_generation_allowed"])
        self.assertIsNone(result["work_proposal"]["generated_next_action"])

    def test_reg_ii_3_explicitly_preserves_no_authorized_outcome(self) -> None:
        result = self.compile("--project", "ega-reg-ii-3")
        self.assertEqual("NO_AUTHORIZED_OUTCOME_RECORDED", result["authority_binding"]["status"])
        self.assertFalse(result["authority_binding"]["work_generation_allowed"])
        self.assertTrue(result["authority_binding"]["explicit_absence_evidence"])
        self.assertEqual("NO_AUTHORIZED_OUTCOME", result["outcome_disposition"]["status"])
        self.assertIsNone(result["work_proposal"]["generated_next_action"])

    def test_requested_outcome_does_not_override_reg_ii_3_authority_absence(self) -> None:
        result = self.compile(
            "--project",
            "ega-reg-ii-3",
            "--outcome",
            "Produce a critical edition of the currently relevant passage.",
        )
        self.assertEqual("HUMAN_AUTHORITY_REQUIRED", result["authority_binding"]["status"])
        self.assertFalse(result["authority_binding"]["work_generation_allowed"])
        self.assertEqual("OWNER_DECISION_REQUIRED", result["outcome_disposition"]["status"])
        self.assertIsNone(result["work_proposal"]["generated_next_action"])

    def test_reg_ii_4_completed_gates_do_not_auto_generate_g5_or_next_action(self) -> None:
        result = self.compile(
            "--project",
            "ega-reg-ii-4-bd-ii",
            "--outcome",
            "Continue the Knau work to a critically consolidated text.",
        )
        self.assertEqual("HUMAN_AUTHORITY_REQUIRED", result["authority_binding"]["status"])
        self.assertFalse(result["authority_binding"]["work_generation_allowed"])
        self.assertIsNone(result["work_proposal"]["generated_next_action"])
        self.assertIn(
            "No owner-selected active scholarly scope is currently recorded",
            result["project_context"]["project_definition"]["active_scope"],
        )
        self.assertIn("G4 controlled comparison", result["project_context"]["canonical_status"]["text"])
        self.assertIn("G5 critical consolidation/validation", result["project_context"]["canonical_status"]["text"])

    def test_requirement_metadata_is_resolved_from_canonical_table(self) -> None:
        result = self.compile("--requirement", "REQ-AI-010")
        selected = result["requirement_resolution"]["selected"]
        self.assertEqual(1, len(selected))
        row = selected[0]
        self.assertEqual("REQ-AI-010", row["requirement_id"])
        self.assertEqual("ai-engineering-hitl", row["domain"])
        self.assertIn("specialist", row["validation_mode"].casefold())
        self.assertTrue(row["specialist_trigger"])
        self.assertEqual("requirements/domain-requirements.tsv", result["canonical_references"]["requirements"])

    def test_unknown_requirement_is_rejected_deterministically(self) -> None:
        result = self.compile("--requirement", "REQ-NOT-REAL", expected_rc=3)
        self.assertEqual("ERROR", result["status"])
        self.assertEqual(["REQ-NOT-REAL"], result["requirement_ids"])

    def test_same_canonical_state_rebuilds_equivalent_deterministic_context(self) -> None:
        first = self.compile("--project", "ega-reg-ii-3", "--requirement", "REQ-UX-011")
        second = self.compile("--project", "ega-reg-ii-3", "--requirement", "REQ-UX-011")
        self.assertEqual(first, second)

    def test_local_result_cannot_be_promoted_to_whole_outcome_completion(self) -> None:
        result = self.compile("--project", "ega-reg-ii-4-bd-ii")
        boundary = result["completion_boundary"]
        self.assertFalse(boundary["local_result_establishes_whole_outcome"])
        self.assertEqual("NOT_DERIVED", boundary["whole_outcome_completion"])


if __name__ == "__main__":
    unittest.main()
