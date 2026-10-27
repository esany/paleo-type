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


    def test_repository_prompt_contains_execution_proof_gate(self) -> None:
        result = prompt.build_prompt("Implement the authorized bounded repository task.", repo="esany/paleo-type")
        lowered = result.lower()
        for marker in (
            "current main commit",
            "working branch or pr",
            "remote repository path, branch and commit",
            "restartability",
            "handoff",
            "affected canonical owner",
            "technical/ci pass",
            "do not fall back",
        ):
            self.assertIn(marker, lowered)

    def test_local_first_prompt_is_rejected(self) -> None:
        tested = prompt.test_prompt("Develop locally in a worktree and push later.")
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("local-first-repository-violation", tested["findings"])

        reviewed = prompt.review_prompt("Develop locally in a worktree and push later.", repo="esany/paleo-type")
        self.assertTrue(any("local-first" in issue for issue in reviewed["issues"]))
        self.assertIn("authorized github connector", reviewed["prompt"].lower())

    def test_connector_failure_never_falls_back_to_local_staging(self) -> None:
        tested = prompt.test_prompt("If the GitHub connector fails, save locally and push later.")
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("connector-failure-local-fallback", tested["findings"])

    def test_premature_status_cannot_establish_acceptance(self) -> None:
        tested = prompt.test_prompt("CI is green, so close the Issue as accepted.")
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("premature-closure-laundering", tested["findings"])

    def test_review_adds_remote_execution_proof(self) -> None:
        reviewed = prompt.review_prompt("Fix the repository and mark the work done.", repo="esany/paleo-type")
        self.assertTrue(any("execution proof" in issue for issue in reviewed["issues"]))
        self.assertIn("current main commit", reviewed["prompt"].lower())

    def test_lean_shortcut_without_adequacy_is_rejected(self) -> None:
        tested = prompt.test_prompt("Use a lean minimal quick fix and close the issue.")
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("lean-shortcut-without-adequacy", tested["findings"])

        reviewed = prompt.review_prompt("Use a lean minimal quick fix.", repo="esany/paleo-type")
        self.assertIn("adequacy", reviewed["prompt"].lower())
        self.assertTrue(any("lean/minimality" in issue for issue in reviewed["issues"]))

    def test_local_pass_cannot_close_the_whole_problem(self) -> None:
        tested = prompt.test_prompt("The local test PASS means the root cause is done.")
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("local-pass-without-whole-system-return", tested["findings"])

    def test_adequate_minimality_is_not_rejected(self) -> None:
        adequate = (
            "Use a minimal change only after stating the user outcome/pain, root cause, "
            "affected owner chain, invariants and distinctions, evidence and acceptance, "
            "non-goals, counter-extreme check and whole-system return condition."
        )
        tested = prompt.test_prompt(adequate)
        self.assertEqual("PASS", tested["status"])

    def test_prompt_create_does_not_manufacture_admission(self) -> None:
        result = prompt.build_prompt("Prepare the repository for the next task.", repo="paleo-type")
        self.assertIn("Do not create or change", result)
        self.assertIn("D-016 admission", result)
        self.assertNotIn("automatically admit", result.lower())

    def test_paleo_prompt_contains_outcome_preserving_return_gate(self) -> None:
        result = prompt.build_prompt("Implement the authorized bounded engineering task.", repo="esany/paleo-type")
        lowered = result.lower()
        for marker in (
            "protected user/research outcome",
            "semantic scope",
            "negative distinctions",
            "coupled obligations",
            "authorized action",
            "definition of ready",
            "definition of done",
            "residual/return condition",
            "claim ceiling",
            "stop/fail closed",
        ):
            self.assertIn(marker, lowered)

    def test_consequential_paleo_prompt_without_return_gate_is_rejected(self) -> None:
        tested = prompt.test_prompt("Implement a bounded change.", repo="esany/paleo-type")
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("missing-outcome-return-gate", tested["findings"])

    def test_owner_existence_cannot_relativize_a_reproduced_failure(self) -> None:
        tested = prompt.test_prompt(
            "The existing owner covers this failure, so no fix is needed.",
            repo="esany/paleo-type",
        )
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("owner-existence-relativization", tested["findings"])

        reviewed = prompt.review_prompt(
            "Fix the reproduced failure; the existing owner covers it, so no gap exists.",
            repo="esany/paleo-type",
        )
        self.assertTrue(any("owner-existence" in issue for issue in reviewed["issues"]))
        self.assertIn("return gate", reviewed["prompt"].lower())

    def test_collection_context_cannot_be_promoted_to_content(self) -> None:
        tested = prompt.test_prompt(
            "Wolkenburg identifies the content and priority of this archival unit.",
            repo="esany/paleo-type",
        )
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("context-content-promotion", tested["findings"])

        negative = prompt.test_prompt(
            "Wolkenburg is collection context only; content and identity require direct evidence.",
            repo="esany/paleo-type",
        )
        self.assertEqual("PASS", negative["status"])

    def test_complete_return_gate_can_pass(self) -> None:
        adequate = (
            "Implement only after stating the protected user outcome, semantic scope, negative distinctions, "
            "coupled obligations, authorized action, Definition of Ready, Definition of Done, "
            "residual condition and claim ceiling."
        )
        tested = prompt.test_prompt(adequate, repo="esany/paleo-type")
        self.assertEqual("PASS", tested["status"])


    def test_blank_return_gate_labels_do_not_establish_completion(self) -> None:
        unfilled = (
            "Implement this change; completed return gate:\n"
            "Protected user/research outcome:\n"
            "Semantic scope:\n"
            "Negative distinctions:\n"
            "Coupled obligations:\n"
            "Authorized action:\n"
            "Definition of Ready:\n"
            "Definition of Done:\n"
            "Residual/return condition:\n"
            "Claim ceiling:\n"
        )
        tested = prompt.test_prompt(unfilled, repo="esany/paleo-type")
        self.assertEqual("NEEDS_REVIEW", tested["status"])
        self.assertIn("unfilled-outcome-return-gate", tested["findings"])
        reviewed = prompt.review_prompt(unfilled, repo="esany/paleo-type")
        self.assertTrue(any("unfilled" in issue for issue in reviewed["issues"]))

        # The gate must not reject ordinary headings followed by actual values.
        filled = (
            "Implement this change; report the return gate:\n"
            "Protected user/research outcome:\n"
            "  Keep the Human's existing source-access objective.\n"
            "Semantic scope:\n"
            "  Access only, no scholarly interpretation.\n"
            "Negative distinctions:\n"
            "  Collection metadata is not documentary content.\n"
            "Coupled obligations:\n"
            "  Preserve the existing evidence and destination records.\n"
            "Authorized action:\n"
            "  Bounded implementation in the admitted branch.\n"
            "Definition of Ready:\n"
            "  Current repo and owner checked.\n"
            "Definition of Done:\n"
            "  Tests and remote proof complete.\n"
            "Residual/return condition:\n"
            "  Return unresolved host acceptance to its existing owner.\n"
            "Claim ceiling:\n"
            "  A test pass is not whole-system acceptance.\n"
        )
        self.assertEqual("PASS", prompt.test_prompt(filled, repo="esany/paleo-type")["status"])

    def test_context_promotion_guard_is_not_wolkenburg_only(self) -> None:
        for invalid in (
            "Bestand 20578 identifies the content and priority of this archival unit.",
            "Sammlung determines the identity and priority of the manuscript.",
            "Collection proves the content and priority of this source.",
        ):
            with self.subTest(invalid=invalid):
                tested = prompt.test_prompt(invalid, repo="esany/paleo-type")
                self.assertEqual("NEEDS_REVIEW", tested["status"])
                self.assertIn("context-content-promotion", tested["findings"])

        contextual_only = (
            "Bestand 20578 is collection context only; documentary content and "
            "research priority require direct evidence and authority."
        )
        self.assertEqual(
            "PASS",
            prompt.test_prompt(contextual_only, repo="esany/paleo-type")["status"],
        )


if __name__ == "__main__":
    unittest.main()
