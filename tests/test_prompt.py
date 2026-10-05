from __future__ import annotations

import unittest

from tools import prompt


class PromptCapabilityTests(unittest.TestCase):
    def test_simple_non_repo_prompt_stays_simple(self) -> None:
        result = prompt.build_prompt("Improve this paragraph without changing its meaning.")
        self.assertIn("Improve this paragraph", result)
        self.assertNotIn("GOVERNING_OBJECTIVE.md", result)
        self.assertNotIn("D-016", result)
        self.assertNotIn("GitHub", result)

    def test_paleo_repo_prompt_requires_fresh_authority_and_shared_check(self) -> None:
        result = prompt.build_prompt("Implement the currently authorized bounded engineering task.", repo="esany/paleo-type")
        self.assertIn("GOVERNING_OBJECTIVE.md", result)
        self.assertIn("AGENTS.md", result)
        self.assertIn("applicable current task/Project owner", result)
        self.assertIn("repository-first", result)
        self.assertIn("python tools/check.py", result)
        self.assertIn("fresh context or second model is not independent evidence", result)
        self.assertIn("Do not create or change Project purpose/priority", result)

    def test_review_repairs_open_scope_and_non_closable_work(self) -> None:
        reviewed = prompt.review_prompt(
            "Read everything and implement until done. Use the latest architecture.",
            repo="esany/paleo-type",
        )
        self.assertEqual("copy-ready-with-material-corrections", reviewed["status"])
        improved = reviewed["prompt"].lower()
        self.assertNotIn("read everything", improved)
        self.assertNotIn("implement until done", improved)
        self.assertTrue(any("latest-wins" in issue for issue in reviewed["issues"]), reviewed["issues"])
        self.assertIn("governing_objective.md", improved)

    def test_self_review_is_never_labeled_independent(self) -> None:
        tested = prompt.test_prompt("Return a bounded result.", self_review=True)
        basis = tested["review_evidence_basis"]
        self.assertEqual("same-evidence-rejudgement", basis["basis_class"])
        self.assertEqual("not-independent-self-review", basis["independence_claim"])
        self.assertIn("not independent", basis["note"].lower())

    def test_independence_overclaim_is_detected(self) -> None:
        tested = prompt.test_prompt(
            "Review this result.",
            result="This was independently validated by the same model in a fresh context.",
            self_review=True,
        )
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("independence-overclaim", tested["findings"])

    def test_prompt_create_does_not_manufacture_admission(self) -> None:
        result = prompt.build_prompt("Prepare the repository for the next task.", repo="paleo-type")
        self.assertIn("Do not create or change", result)
        self.assertIn("D-016 admission", result)
        self.assertNotIn("automatically admit", result.lower())


if __name__ == "__main__":
    unittest.main()
