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

    def test_semicolon_after_blind_ja_is_still_explicitly_blind(self):
        # Existing independent review entries use "Blind: ja; ..." (#371).
        self.review.write_text(
            self.review.read_text(encoding="utf-8").replace(
                "Blind: ja (kein Hauptchat-Text eingesehen)",
                "Blind: ja; keine fremden Lesungen eingesehen",
            ),
            encoding="utf-8",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "blind declaration with explanatory semicolon")
        review_commit = self.git("rev-parse", "HEAD")
        rc, out = self.check(
            line=f"Vergleich: 0106R | Lesung {self.reading} | Vorab {review_commit} "
                 "| Abweichungen 1 | davon Vereinheitlichung 0 | Urteil passt",
            review_ref=review_commit,
        )
        self.assertEqual(0, rc, out)

    def test_comma_after_blind_ja_is_explicit_declaration(self):
        # The reviewer may add a comma-separated provenance explanation.
        self.review.write_text(
            self.review.read_text(encoding="utf-8").replace(
                "Blind: ja (kein Hauptchat-Text eingesehen)",
                "Blind: ja, keine fremde Lesung vorab gesehen",
            ),
            encoding="utf-8",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "blind declaration with comma")
        review_commit = self.git("rev-parse", "HEAD")
        rc, out = self.check(
            line=f"Vergleich: 0106R | Lesung {self.reading} | Vorab {review_commit} "
                 "| Abweichungen 1 | davon Vereinheitlichung 0 | Urteil passt",
            review_ref=review_commit,
        )
        self.assertEqual(0, rc, out)

    def test_explicit_zero_readable_lines_is_not_a_fabricated_line(self):
        # Reviewers can observe a left view containing no distinct readable lines.
        # This is NOT a positive 2-3-line transcription or a scholarly PASS.
        self.review.write_text(
            self.review.read_text(encoding="utf-8")
            + "\n## 0118L\n"
            + "- Datum: 2026-11-01\n"
            + "- Leser: fresh blind reviewer\n"
            + "- Bildquelle: FILE-SSTA-20578-NR632-FULL-PDF-20261030, PDF-Seite 118\n"
            + "- Blind: ja (no earlier reading seen)\n"
            + "- Bildbefund, linke Bildhälfte: nur spiegelverkehrte Durchscheinschrift, kein sicher eigener Textblock.\n"
            + "- Stichprobe: 0 eigenständige Schriftzeilen; keine diplomatische Zeilenlesung.\n",
            encoding="utf-8",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "separate image view with zero readable lines")
        rc, out = self.check(review_ref=self.git("rev-parse", "HEAD"))
        self.assertEqual(0, rc, out)
        self.assertEqual(1, out["checked"])

    def test_missing_locus_without_zero_line_evidence_is_rejected(self):
        self.review.write_text(
            self.review.read_text(encoding="utf-8").replace(
                "- Haupttext rechts, Z. 8 von oben: " + chr(96) + "Darüber ich in [Pflicht?]" + chr(96),
                "- Bildbefund, rechts: Schrift sichtbar, aber keine Zeile genannt.",
            ),
            encoding="utf-8",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "missing locator in non-zero review")
        rc, out = self.check(review_ref=self.git("rev-parse", "HEAD"))
        self.assertNotEqual(0, rc)

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



    @staticmethod
    def followup_section(page, blind="ja"):
        return (
            f"\n## {page}\n"
            "- Datum: 2026-11-02\n"
            "- Leser: other fresh blind chat\n"
            "- Bildquelle: FILE-SSTA-20578-NR632-FULL-PDF-20261030, PDF-Seite 105\n"
            f"- Blind: {blind}\n"
            "- Haupttext links, Z. 14 von oben: " + chr(96) + "[Wort?]" + chr(96) + "\n"
        )

    def followup_commit(self, sections):
        self.review.write_text(
            self.review.read_text(encoding="utf-8") + "".join(sections),
            encoding="utf-8",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "independent original and follow-up sections")
        return self.git("rev-parse", "HEAD")

    def test_followup_nonblind_section_rejected(self):
        # Old HEADER silently absorbs ## 0105L-2 into the previous 0106R.
        pre = self.followup_commit([
            self.followup_section("0105L-2", blind="nein")
        ])
        rc, out = self.check(review_ref=pre)
        self.assertNotEqual(0, rc, out)
        self.assertIn("0105L-2: reviewer did not declare Blind: ja", out["findings"])

    def test_followup_cannot_borrow_original_review_section(self):
        # A comparison citing the -2 sample must not bind to ## 0105L.
        pre = self.followup_commit([self.followup_section("0105L")])
        rc, out = self.check(
            line=f"Vergleich: 0105L-2 | Lesung {self.reading} | Vorab {pre} "
                 "| Abweichungen 0 | davon Vereinheitlichung 0 | Urteil passt",
            review_ref=pre,
        )
        self.assertNotEqual(0, rc, out)
        self.assertIn(
            "0105L-2: no review section in active review branch", out["findings"]
        )

    def test_original_and_followup_are_distinct_valid_keys(self):
        pre = self.followup_commit([
            self.followup_section("0105L"),
            self.followup_section("0105L-2"),
        ])
        rc, out = self.check(
            line=f"Vergleich: 0105L-2 | Lesung {self.reading} | Vorab {pre} "
                 "| Abweichungen 0 | davon Vereinheitlichung 0 | Urteil passt",
            review_ref=pre,
        )
        self.assertEqual(0, rc, out)
        self.assertEqual(3, out["review_sections"])
        self.assertEqual(1, out["checked"])

    def test_work_return_explicitly_rejects_missing_new_status_anchor(self):
        # A malformed block must fail via the REAL work_return script.
        import hashlib
        project = self.root / BASE
        (project / "project.yml").write_text(
            "canonical_status_file: STATUS.md\n", encoding="utf-8"
        )
        status = project / "STATUS.md"
        status.write_text("before\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "baseline status")
        baseline = self.git("rev-parse", "HEAD")
        recorded = hashlib.sha256(b"before\n").hexdigest()
        self.owner.write_text("# Forschungsowner\n0106R-A08: Darueber\n", encoding="utf-8")
        status.write_text("before\nnew but different return\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-qm", "real source delta and changed status")
        result = self.git("rev-parse", "HEAD")
        report = {
            "run_status": "completed",
            "recorded_status_sha256": recorded,
            "baseline_commit": baseline,
            "result_commit": result,
            "research_owner": OWNER,
            "continuation_anchor": "**not actually stored in STATUS**",
        }
        dest = self.root / "invalid-return.json"
        dest.write_text(json.dumps(report), encoding="utf-8")
        cmd = [sys.executable, str(TOOL.parent / "work_return.py"),
               "--root", str(self.root), "--project", "ssta-20578-nr-632",
               "--report", str(dest)]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        self.assertNotEqual(0, proc.returncode, proc.stdout)
        self.assertIn("Fortsetzung nicht belegt", proc.stdout)


GESUCH = BASE + "/research/gesuch-0104R-0107L.md"
READING_DIR = BASE + "/transcription/first-reading"
TSV_HEADER = "reading_order\tdiplomatic_reading\tline_ref\tevidence_note\n"


class OffeneSeiten(unittest.TestCase):
    """Eigentümerentscheidung 22.11.2026 („Ja, erst Prüfung“), Fall Gesuch 0104R.

    Eine Seite mit dem Urteil „überarbeiten“ gilt nicht als erledigt, solange
    keine neue Blindprobe gegen die überarbeitete Lesung „passt“ ergibt. Ebenso
    offen: Lesung nach dem Vergleich geändert, oder der verglichene Stand
    enthält die Lesungsdatei nicht (Fall der Blindprobe vom 21.11.2026).
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / BASE / "research").mkdir(parents=True)
        (self.root / READING_DIR).mkdir(parents=True)
        self.git("init", "-q")
        self.git("config", "user.name", "fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.owner = self.root / GESUCH
        self.review = self.root / REVIEW
        self.tsv = self.root / READING_DIR / "0104R.tsv"
        self.owner.write_text("# Gesuch\n", encoding="utf-8")
        self.review.write_text("# Vorab\n\n", encoding="utf-8")
        self.commit("baseline")
        self.owner.write_text("# Gesuch\nLesung noch im Markdown\n", encoding="utf-8")
        self.before_tsv = self.commit("Lesung im Markdown, noch ohne Lesungsdatei")
        self.write_tsv("4. Jul: 1760.", "Aller-Durchlauchtigster Großmäch-")
        self.r1 = self.commit("Lesung 0104R")
        self.v1 = self.add_review("0104R")
        self.write_tsv("4. July 1760.", "Aller-Durchlauchtigster-Großmäch-")
        self.r2 = self.commit("0104R überarbeitet")
        self.v2 = self.add_review("0104R-2")

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True).strip()

    def commit(self, message):
        self.git("add", ".")
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD")

    def write_tsv(self, h01, h02, note="Grenze"):
        self.tsv.write_text(
            TSV_HEADER + f"1\t{h01}\t0104R-H01\t{note}\n2\t{h02}\t0104R-H02\tGrenze\n",
            encoding="utf-8",
        )

    def add_review(self, page):
        self.review.write_text(
            self.review.read_text(encoding="utf-8")
            + f"## {page}\n- Datum: 2026-11-22\n- Leser: frischer Chat\n"
            + "- Bildquelle: FILE-SSTA-20578-NR632-FULL-PDF-20261030, PDF-Seite 104\n"
            + "- Blind: ja\n- Kopf, Z. 1 von oben: `4. July 1760.`\n\n",
            encoding="utf-8",
        )
        return self.commit(f"vorab: {page}")

    @staticmethod
    def line(page, reading, vorab, errors, judgement):
        return (f"Vergleich: {page} | Lesung {reading} | Vorab {vorab} | Abweichungen {errors} "
                f"| davon Vereinheitlichung 0 | Urteil {judgement}")

    def check(self, *lines, scope="0104R", reading_dir=True, summary=None):
        self.owner.write_text("# Gesuch\n" + "".join(l + "\n" for l in lines), encoding="utf-8")
        cmd = [sys.executable, str(TOOL), "--root", str(self.root), "--research-owner", GESUCH,
               "--review-path", REVIEW, "--review-ref", self.git("rev-parse", "HEAD")]
        if reading_dir:
            cmd += ["--reading-dir", READING_DIR]
        if scope:
            cmd += ["--offen-pruefen", scope]
        if summary:
            cmd += ["--zusammenfassung", str(summary)]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return proc.returncode, json.loads(proc.stdout)

    def gruende(self, out):
        return " | ".join(o["grund"] for o in out.get("offen", []))

    def test_ueberarbeiten_ohne_nachprobe_bleibt_offen(self):
        rc, out = self.check(self.line("0104R", self.r1, self.v1, 2, "überarbeiten"))
        self.assertEqual(1, rc, out)
        self.assertEqual([], out["findings"])
        self.assertIn("„überarbeiten“", self.gruende(out))
        self.assertIn("0104R-2", self.gruende(out))

    def test_ohne_offen_pruefen_bleibt_das_alte_verhalten(self):
        rc, out = self.check(self.line("0104R", self.r1, self.v1, 2, "überarbeiten"), scope=None)
        self.assertEqual(0, rc, out)
        self.assertNotIn("offen", out)

    def test_nachprobe_passt_gegen_ueberarbeitete_lesung_ist_erledigt(self):
        # Der Lesungs-Commit r2 ändert nur die TSV-Datei, nicht die Gesuch-Datei.
        rc, out = self.check(
            self.line("0104R", self.r1, self.v1, 2, "überarbeiten"),
            self.line("0104R-2", self.r2, self.v2, 0, "passt"),
        )
        self.assertEqual(0, rc, out)
        self.assertEqual([], out["offen"])
        self.assertEqual("0104R-2", out["verglichen"][0]["letzter_vergleich"])

    def test_absichtlich_falsch_passt_ohne_echte_blindprobe_bleibt_rot(self):
        # Jemand schreibt „passt“ hin, aber es gibt keine Blindprobe 0104R-2 im zitierten Stand.
        rc, out = self.check(
            self.line("0104R", self.r1, self.v1, 2, "überarbeiten"),
            self.line("0104R-2", self.r2, self.v1, 0, "passt"),
        )
        self.assertEqual(1, rc, out)
        self.assertTrue(any("0104R-2" in f for f in out["findings"]), out)
        self.assertIn("ungültig", self.gruende(out))

    def test_absichtlich_falsch_passt_mit_alter_lesung_bleibt_rot(self):
        # „passt“ zitiert den Lesungsstand vor der Überarbeitung: Die heutige Lesung ist eine andere.
        rc, out = self.check(
            self.line("0104R", self.r1, self.v1, 2, "überarbeiten"),
            self.line("0104R-2", self.r1, self.v2, 0, "passt"),
        )
        self.assertEqual(1, rc, out)
        self.assertIn("geändert", self.gruende(out))

    def test_lesung_nach_dem_vergleich_geaendert_ist_offen(self):
        self.write_tsv("4. July 1760.", "Aller-Durchlauchtigster-Großmächtig")
        self.commit("still geändert nach dem Vergleich")
        rc, out = self.check(
            self.line("0104R", self.r1, self.v1, 2, "überarbeiten"),
            self.line("0104R-2", self.r2, self.v2, 0, "passt"),
        )
        self.assertEqual(1, rc, out)
        self.assertIn("nach dem verglichenen Commit", self.gruende(out))

    def test_nur_beleghinweis_geaendert_ist_kein_neuer_vergleich_noetig(self):
        self.write_tsv("4. July 1760.", "Aller-Durchlauchtigster-Großmäch-", note="neuer Hinweis")
        self.commit("nur evidence_note")
        rc, out = self.check(
            self.line("0104R", self.r1, self.v1, 2, "überarbeiten"),
            self.line("0104R-2", self.r2, self.v2, 0, "passt"),
        )
        self.assertEqual(0, rc, out)

    def test_verglichener_stand_ohne_lesungsdatei_ist_offen(self):
        # Fall der Blindprobe vom 21.11.2026: verglichen wurde ein Stand vor den TSV-Dateien.
        rc, out = self.check(self.line("0104R", self.before_tsv, self.v1, 0, "passt"))
        self.assertEqual(1, rc, out)
        self.assertIn("lässt sich nicht feststellen", self.gruende(out))

    def test_massgeblich_ist_die_hoechste_probe_nicht_die_reihenfolge(self):
        rc, out = self.check(
            self.line("0104R-2", self.r2, self.v2, 0, "passt"),
            self.line("0104R", self.r1, self.v1, 2, "überarbeiten"),
        )
        self.assertEqual(0, rc, out)

    def test_seite_ohne_vergleich_ist_offen(self):
        rc, out = self.check(self.line("0104R-2", self.r2, self.v2, 0, "passt"), scope="0104R,0105L")
        self.assertEqual(1, rc, out)
        self.assertEqual(["0105L"], [o["seite"] for o in out["offen"]])

    def test_doppelte_vergleichszeile_ist_ein_befund(self):
        rc, out = self.check(
            self.line("0104R-2", self.r2, self.v2, 0, "passt"),
            self.line("0104R-2", self.r2, self.v2, 1, "passt"),
        )
        self.assertEqual(1, rc, out)
        self.assertTrue(any("doppelte Vergleichszeile" in f for f in out["findings"]), out)

    def test_zusammenfassung_in_alltagssprache(self):
        summary = self.root / "summary.md"
        self.check(self.line("0104R", self.r1, self.v1, 2, "überarbeiten"), summary=summary)
        text = summary.read_text(encoding="utf-8")
        self.assertIn("**Ergebnis: offen (1 Seite).**", text)
        self.assertIn("- **0104R:**", text)
        self.assertIn("Ob eine Lesung stimmt, prüft das nicht.", text)


if __name__ == "__main__":
    unittest.main()
