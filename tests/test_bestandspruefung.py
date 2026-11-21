"""Bestandsprüfung: Was gibt es zu einem Gegenstand schon?

Regressionsfall vom 21.11.2026: Vor dem Abtrennen des Gesuchs 0104R–0107L (PR #417)
wurde nicht gesehen, dass der Eigentümer in #394 schon entschieden hatte und #397
den Auftrag dazu enthielt. Die Prüfung muss beides zeigen.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import bestandspruefung as bp  # noqa: E402

FIXTURE = ROOT / "tests/fixtures/bestandspruefung/github.json"


class BestandspruefungTest(unittest.TestCase):
    def setUp(self) -> None:
        data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.issues, self.prs = data["issues"], data["prs"]

    def test_real_case_finds_open_assignment_and_owner_decision(self) -> None:
        # Benutzer schreibt den Gegenstand mit einfachem Bindestrich, die Issues mit Halbgeviertstrich.
        result = bp.pruefe(["Gesuch 0104R-0107L"], self.issues, self.prs, files={})
        offen = [h["number"] for h in result["offene_issues"]]
        entschieden = [h["number"] for h in result["entscheidungen"]]
        self.assertIn(397, offen, "offener Auftrag #397 muss erscheinen")
        self.assertIn(394, entschieden, "Eigentümerentscheidung in #394 muss erscheinen")
        self.assertNotIn(13, offen, "nicht passendes Issue darf nicht erscheinen")

    def test_open_pr_and_repo_files_are_listed(self) -> None:
        files = {"projects/x/README.md": "Text\nGesuch 0104R–0107L hier\n", "andere.md": "nichts\n"}
        result = bp.pruefe(["0104R"], self.issues, self.prs, files=files)
        self.assertIn(359, [h["number"] for h in result["offene_prs"]])
        self.assertEqual([f["path"] for f in result["dateien"]], ["projects/x/README.md"])
        self.assertEqual(result["dateien"][0]["line"], 2)

    def test_counter_case_unknown_subject_finds_nothing(self) -> None:
        result = bp.pruefe(["Kaiserchronik"], self.issues, self.prs, files={})
        self.assertEqual(sum(len(v) for v in result.values()), 0)

    def test_command_line_with_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = subprocess.run(
                [sys.executable, str(ROOT / "tools/bestandspruefung.py"), "--github-json", str(FIXTURE),
                 "--repo", tmp, "Gesuch 0104R–0107L"],
                capture_output=True, text=True, check=True,
            ).stdout
        self.assertIn("#397", out)
        self.assertIn("#394", out)
        self.assertIn("Eigentümerentscheidung", out)



class TermsFromPathsTest(unittest.TestCase):
    """Für den automatischen Lauf bei PRs: Gegenstände aus den geänderten Pfaden ableiten."""

    def test_pr_417_paths_give_the_six_surfaces(self) -> None:
        paths = [
            "projects/ssta-20578-nr-632/transcription/first-reading/0104R.tsv",
            "projects/ssta-20578-nr-632/transcription/first-reading/0107L.tsv",
            "projects/ssta-20578-nr-632/research/gesuch-0104R-0107L.md",
            "projects/ssta-20578-nr-632/transcription/first-reading/0105L.tsv",
            "tests/test_nr632_first_reading_migration.py",
            "corpus/source-data/SSTA-ARCHIVIALE-EDD69AA1/digital-crosswalk.tsv",
        ]
        self.assertEqual(bp.terms_from_paths(paths), ["0104R", "0105L", "0107L"])

    def test_project_without_surface_gives_project_id(self) -> None:
        self.assertEqual(bp.terms_from_paths(["projects/ega-reg-ii-3/STATUS.md"]), ["ega-reg-ii-3"])

    def test_tool_only_change_gives_nothing(self) -> None:
        self.assertEqual(bp.terms_from_paths(["tools/bestandspruefung.py", "tests/test_bestandspruefung.py"]), [])

    def test_command_line_from_paths_with_nothing_to_check(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            listing = Path(tmp) / "changed.txt"
            listing.write_text("tools/bestandspruefung.py\n", encoding="utf-8")
            out = subprocess.run(
                [sys.executable, str(ROOT / "tools/bestandspruefung.py"), "--github-json", str(FIXTURE),
                 "--repo", tmp, "--from-paths", str(listing)],
                capture_output=True, text=True, check=True,
            ).stdout
        self.assertIn("Keine Gegenstände", out)

if __name__ == "__main__":
    unittest.main()
