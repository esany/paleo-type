"""P0 (#353) executable false/true controls for the PR evidence freeze."""
import unittest

from tools import metrics


class EvidenceFreezeTests(unittest.TestCase):
    def setUp(self):
        self.path = "engineering/evidence/research/forbidden-test.md"
        self.reason = "Verfahren-Ausnahme-Begründung: Dies ist eine ausdrücklich begründete Ausnahme."
        self.growth_reason = "Verfahrenszuwachs-Begründung: Der technische Zuwachs ist für diese Prüfung notwendig."

    def test_new_path_fails_without_label(self):
        added = metrics.new_evidence_files({"README.md"}, {"README.md", self.path})
        self.assertEqual(added, [self.path])
        with self.assertRaisesRegex(metrics.GuardFailure, "ohne Label"):
            metrics.guard_evidence(added, set(), self.reason)

    def test_label_without_sentence_still_fails(self):
        with self.assertRaisesRegex(metrics.GuardFailure, "erfordert einen Satz"):
            metrics.guard_evidence([self.path], {metrics.LABEL}, "Nur ein Label.")

    def test_label_and_sentence_pass(self):
        metrics.guard_evidence([self.path], {metrics.LABEL}, self.reason)

    def test_existing_file_changes_are_not_new(self):
        self.assertEqual(metrics.new_evidence_files({self.path}, {self.path}), [])
        metrics.guard_evidence([], set(), "")

    def test_renamed_path_into_evidence_is_new(self):
        self.assertEqual(
            metrics.new_evidence_files({"somewhere/old.md"}, {self.path}),
            [self.path],
        )

    def test_label_spelling_must_match(self):
        with self.assertRaises(metrics.GuardFailure):
            metrics.guard_evidence([self.path], {"Verfahren-Ausnahme"}, self.reason)

    def test_growth_without_reason_fails(self):
        with self.assertRaisesRegex(metrics.GuardFailure, "Verfahrenszuwachs"):
            metrics.guard_growth(3, 0, "")

    def test_growth_with_reason_passes(self):
        metrics.guard_growth(3, 0, self.growth_reason)

    def test_growth_in_goal_passes_without_reason(self):
        metrics.guard_growth(2, 4, "")

    def test_unclassified_issues_not_guessed_from_title(self):
        issues = [
            {"title": "[AUDIT] ambiguous", "labels": []},
            {"title": "A", "labels": [{"name": "Forschung"}]},
            {"title": "B", "labels": [{"name": "bereich:Technik"}]},
            {"title": "C", "labels": [{"name": "Technik"}, {"name": "Forschung"}]},
            {"title": "PR", "pull_request": {"url": "somewhere"}, "labels": []},
        ]
        self.assertEqual(metrics.issue_counts(issues),
                         {"Forschung": 1, "Technik": 1, "Verfahren": 0, "Unklassifiziert": 2})

    def test_malformed_justification_does_not_pass(self):
        self.assertFalse(metrics.has_reason("Verfahren-Ausnahme-Begründung: kurz", "Verfahren-Ausnahme-Begründung"))
        self.assertTrue(metrics.has_reason(self.reason, "Verfahren-Ausnahme-Begründung"))


if __name__ == "__main__":
    unittest.main()
