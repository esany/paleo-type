"""Git-history and blind-declaration regressions for Nr. 632 (#368 / #371)."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parents[1] / "tools" / "gegenlesung_check.py"
BASE = "projects/ssta-20578-nr-632"
OWNER = BASE + "/research/transcription-pilot-0102R-0103L-2026-10-30.md"
REVIEW = BASE + "/research/gegenlesung-vorab.md"


class GegenlesungCI(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / BASE / "research").mkdir(parents=True)
        self.git("init", "-q")
        self.git("config", "user.name", "fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.owner, self.review = self.root / OWNER, self.root / REVIEW
        self.owner.write_text("# Forschungsowner\n", encoding="utf-8")
        self.review.write_text("# Vorab\n\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "baseline")
        self.owner.write_text("# Forschungsowner\n0106R-A08: Dafür\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "reading commit")
        self.reading = self.git("rev-parse", "HEAD")
        self.review.write_text(
            "# Vorab\n\n## 0106R\n- Datum: 2026-10-31\n"
            "- Leser: fresh independent chat\n"
            "- Bildquelle: FILE-SSTA-20578-NR632-FULL-PDF-20261030, PDF-Seite 106\n"
            "- Blind: ja (kein Hauptchat-Text eingesehen)\n"
            "- Haupttext rechts, Z. 8 von oben: " + chr(96) + "Darüber ich in [Pflicht?]" + chr(96) + "\n",
            encoding="utf-8",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "review AFTER source reading")
        self.vorab = self.git("rev-parse", "HEAD")

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True).strip()

    def check(self, line=None, review_ref=None):
        if line is None:
            line = (f"Vergleich: 0106R | Lesung {self.reading} | Vorab {self.vorab} "
                    "| Abweichungen 1 | davon Vereinheitlichung 0 | Urteil passt")
        self.owner.write_text("# Forschungsowner\n0106R-A08: Dafür\n" + line + "\n", encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(TOOL), "--root", str(self.root),
             "--research-owner", OWNER, "--review-path", REVIEW,
             "--review-ref", review_ref or self.vorab],
            capture_output=True, text=True, check=False,
        )
        try:
            output = json.loads(proc.stdout)
        except json.JSONDecodeError:
            output = {"stdout": proc.stdout, "stderr": proc.stderr}
        return proc.returncode, output

    def test_valid_blind_review_even_if_saved_after_reading(self):
        rc, out = self.check()
        self.assertEqual(0, rc, out)
        self.assertEqual(1, out["checked"])

    def test_nonblind_section_rejected(self):
        self.review.write_text(self.review.read_text().replace("Blind: ja", "Blind: nein"))
        self.git("add", ".")
        self.git("commit", "-qm", "nonblind review")
        commit = self.git("rev-parse", "HEAD")
        rc, out = self.check(
            line=f"Vergleich: 0106R | Lesung {self.reading} | Vorab {commit} "
                 "| Abweichungen 1 | davon Vereinheitlichung 0 | Urteil passt",
            review_ref=commit,
        )
        self.assertNotEqual(0, rc)

    def test_wrong_comparison_format_rejected(self):
        rc, out = self.check(line="Vergleich: 0106R | passt")
        self.assertNotEqual(0, rc)

    def test_reading_commit_must_change_owner(self):
        rc, out = self.check(
            line=f"Vergleich: 0106R | Lesung {self.vorab} | Vorab {self.vorab} "
                 "| Abweichungen 1 | davon Vereinheitlichung 0 | Urteil passt"
        )
        self.assertNotEqual(0, rc)

    def test_nonexistent_reading_commit_rejected(self):
        rc, out = self.check(
            line=f"Vergleich: 0106R | Lesung {'0'*40} | Vorab {self.vorab} "
                 "| Abweichungen 1 | davon Vereinheitlichung 0 | Urteil passt"
        )
        self.assertNotEqual(0, rc)

    def test_pass_cannot_ignore_stated_two_unmarked_errors(self):
        rc, out = self.check(
            line=f"Vergleich: 0106R | Lesung {self.reading} | Vorab {self.vorab} "
                 "| Abweichungen 2 | davon Vereinheitlichung 0 | Urteil passt"
        )
        self.assertNotEqual(0, rc)

    def test_malformed_review_section_rejected(self):
        self.review.write_text(self.review.read_text().replace("- Datum: 2026-10-31\n", ""))
        self.git("add", ".")
        self.git("commit", "-qm", "missing review date")
        rc, out = self.check(review_ref=self.git("rev-parse", "HEAD"))
        self.assertNotEqual(0, rc)


if __name__ == "__main__":
    unittest.main()
