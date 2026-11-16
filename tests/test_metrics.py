"""S0 (#353): label-only evidence freeze and honest derived measures."""
import os
import unittest
from unittest.mock import patch

from tools import metrics


class EvidenceFreezeTests(unittest.TestCase):
    def setUp(self):
        self.path = "engineering/evidence/research/forbidden-test.md"

    def test_new_path_fails_without_label(self):
        added = metrics.new_evidence_files({"README.md"}, {"README.md", self.path})
        self.assertEqual(added, [self.path])
        with self.assertRaisesRegex(metrics.GuardFailure, "ohne Label"):
            metrics.guard_evidence(added, set())

    def test_label_alone_passes_without_body_or_reason(self):
        metrics.guard_evidence([self.path], {metrics.LABEL})

    def test_existing_file_changes_are_not_new(self):
        self.assertEqual(metrics.new_evidence_files({self.path}, {self.path}), [])
        metrics.guard_evidence([], set())

    def test_archive_move_without_label_is_allowed(self):
        old = "engineering/evidence/audits/existing.md"
        new = "engineering/archive/existing.md"
        added = metrics.new_evidence_files({old}, {new})
        self.assertEqual(added, [])
        metrics.guard_evidence(added, set())

    def test_renamed_path_into_evidence_is_new(self):
        self.assertEqual(
            metrics.new_evidence_files({"somewhere/old.md"}, {self.path}),
            [self.path],
        )

    def test_label_spelling_must_match(self):
        with self.assertRaises(metrics.GuardFailure):
            metrics.guard_evidence([self.path], {"Verfahren-Ausnahme"})

    def test_growth_has_no_guard(self):
        self.assertFalse(hasattr(metrics, "guard_growth"))

    def test_unclassified_issues_not_guessed_from_title(self):
        issues = [
            {"title": "[AUDIT] ambiguous", "labels": []},
            {"title": "A", "labels": [{"name": "Forschung"}]},
            {"title": "B", "labels": [{"name": "bereich:Technik"}]},
            {"title": "C", "labels": [{"name": "Technik"}, {"name": "Forschung"}]},
            {"title": "PR", "pull_request": {"url": "somewhere"}, "labels": []},
        ]
        self.assertEqual(
            metrics.issue_counts(issues),
            {"Forschung": 1, "Technik": 1, "Verfahren": 0, "Unklassifiziert": 2},
        )

    def test_owner_rescue_label_counts_open_and_closed_issues_and_prs(self):
        tagged = [{"name": metrics.RESCUE_LABEL}]
        items = [
            {"state": "open", "labels": tagged},                     # issue
            {"state": "closed", "labels": tagged},                   # issue
            {"state": "open", "pull_request": {"url": "pr/1"}, "labels": tagged},
            {"state": "closed", "pull_request": {"url": "pr/2"}, "labels": tagged},
            {"state": "open", "pull_request": {"url": "pr/3"}, "labels": []},
            {"state": "closed", "labels": []},
        ]
        self.assertEqual(metrics.rescue_counts(items), {"Issues": 2, "Pull Requests": 2})

    def test_rescue_label_is_not_inferred_from_title(self):
        items = [
            {"title": "[RETTUNG] eingegriffen", "labels": []},
            {"title": "normale Arbeit", "labels": [{"name": "andere"}]},
        ]
        self.assertEqual(metrics.rescue_counts(items), {"Issues": 0, "Pull Requests": 0})

    def test_no_api_means_not_verified_not_zero(self):
        with patch.dict(os.environ, {"GITHUB_REPOSITORY": "", "GITHUB_TOKEN": ""}):
            counts, note = metrics.live_rescue_counts()
        self.assertIsNone(counts)
        self.assertIn("Keine authentifizierte GitHub-API", note)
        with (
            patch.object(metrics, "tracked_text_sizes", return_value=({"engineering": 12, "projects": 6}, 0)),
            patch.object(metrics, "live_issue_counts", return_value=({"Forschung": 0, "Technik": 0, "Verfahren": 0, "Unklassifiziert": 0}, "Test")),
            patch.object(metrics, "live_rescue_counts", return_value=(None, note)),
        ):
            text = metrics.report(None)
        self.assertIn("Rettungseingriffe", text)
        self.assertIn("Nicht geprüft", text)
        self.assertNotIn("Gesamt: 0", text)


if __name__ == "__main__":
    unittest.main()
