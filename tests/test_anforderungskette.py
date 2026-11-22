"""Tests für die Anforderungskette (tools/anforderungskette.py)."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "tools"))

import anforderungskette as kette  # noqa: E402

NEEDS_HEADER = "\t".join(kette.NEED_COLUMNS)
REQ_HEADER = "\t".join(["requirement_id", "current_support"] + kette.CHAIN_COLUMNS)


def need(*fields: str) -> str:
    return "\t".join(fields)


ZIEL = "docs/o-toene.md#01.01.2026 Ziel"
GOOD_NEEDS = [
    need("I-01", "Intent", "", "Jede Quelle lesen.", "wörtlich", "jede Quelle lesen", ZIEL),
    need("B-01", "Bedürfnis", "I-01", "Lesen.", "wörtlich", "wissen, was da steht", ZIEL),
    need("B-02", "Bedürfnis", "I-01", "Einordnen.", "abgeleitet", "einordnen können", ZIEL),
    need("P-01", "Pain", "B-01", "Prosa statt Funktion.", "wörtlich", "ein repo der Prosa", "docs/o-toene.md#01.01.2026 Kern"),
    need("R-01", "Rahmen", "", "Deutsch.", "wörtlich", "Englisch ist falsch", "docs/o-toene.md#01.01.2026 Sprache"),
]
O_TOENE = (
    "# O-Töne\n\n## 01.01.2026 · Chat · direkt\n\n"
    "**Ziel**\n> ich will jede Quelle lesen und\n> wissen, was da steht, und es einordnen können\n\n"
    "Anmerkung der KI: Der Satz bezieht sich auf eine Notiz.\n\n"
    "**Kern**\n> Das Repo ist ein repo der Prosa.\n\n"
    "**Sprache**\n> Englisch ist falsch\n\n"
    "**Zustimmung** (vorgegebener Antwortknopf gewählt)\n> Ja, übernehmen\n"
)


def req(rid: str, needs: str = "B-01", applies: str = "G2", verified: str = "keine",
        depends: str = "", overlaps: str = "", support: str = "gap", kurz: str = "Kurz") -> str:
    return "\t".join([rid, support, kurz, needs, applies, verified, depends, overlaps])


class Fixture:
    def __init__(self, needs: list[str] | None = None, reqs: list[str] | None = None) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        (self.root / "requirements").mkdir()
        (self.root / "tests").mkdir()
        (self.root / "docs" / "o-toene.md").write_text(O_TOENE, encoding="utf-8")
        (self.root / "tests" / "test_beispiel.py").write_text(
            "def test_vorhanden():\n    pass\n", encoding="utf-8")
        (self.root / "tests" / "test_verwaist.py").write_text(
            "def test_etwas():\n    pass\n", encoding="utf-8")
        self.write(needs if needs is not None else GOOD_NEEDS,
                   reqs if reqs is not None else [req("REQ-EDIT-008", verified="tests/test_beispiel.py::test_vorhanden"),
                                                   req("REQ-UX-003", needs="P-01", depends="REQ-EDIT-008")])

    def write(self, needs: list[str], reqs: list[str]) -> None:
        (self.root / "requirements" / "beduerfnisse.tsv").write_text(
            "\n".join([NEEDS_HEADER] + needs) + "\n", encoding="utf-8")
        (self.root / "requirements" / "domain-requirements.tsv").write_text(
            "\n".join([REQ_HEADER] + reqs) + "\n", encoding="utf-8")

    def findings(self) -> list[str]:
        return kette.validate(self.root)

    def close(self) -> None:
        self.tmp.cleanup()


class EchteDaten(unittest.TestCase):
    def test_echte_kette_ist_gueltig(self) -> None:
        self.assertEqual([], kette.validate(REPO))

    def test_ansicht_ist_aktuell(self) -> None:
        view = (REPO / kette.VIEW_PATH).read_text(encoding="utf-8")
        self.assertEqual(kette.render(REPO), view,
                         "requirements/kette.md ist veraltet: python3 tools/anforderungskette.py schreiben")

    def test_jede_echte_anforderung_hat_die_kettenspalten(self) -> None:
        """Eine neue Anforderung ohne Bedürfnis, Stufe oder Prüfangabe darf nicht unbemerkt hinzukommen."""
        _, rows = kette.read_tsv(REPO / kette.REQS_PATH)
        self.assertGreater(len(rows), 100)
        for row in rows:
            for column in ("kurz", "need_ids", "applies_from", "verified_by"):
                self.assertTrue(row[column].strip(), f"{row['requirement_id']}: {column} leer")


class Kette(unittest.TestCase):
    def setUp(self) -> None:
        self.fx = Fixture()
        self.addCleanup(self.fx.close)

    def test_gueltige_kette_hat_keine_befunde(self) -> None:
        self.assertEqual([], self.fx.findings())

    def test_o_ton_muss_woertlich_in_der_fundstelle_stehen(self) -> None:
        needs = list(GOOD_NEEDS)
        needs[1] = need("B-01", "Bedürfnis", "I-01", "Lesen.", "wörtlich", "wissen, was dort steht", ZIEL)
        self.fx.write(needs, [req("REQ-EDIT-008")])
        self.assertIn("B-01: O-Ton steht nicht wörtlich in einem Zitat des genannten Abschnitts: 'wissen, was dort steht'",
                      self.fx.findings())

    def test_o_ton_ueber_zeilenumbruch_und_zitatzeichen_wird_gefunden(self) -> None:
        needs = list(GOOD_NEEDS)
        needs[1] = need("B-01", "Bedürfnis", "I-01", "Lesen.", "wörtlich", "jede Quelle lesen und wissen", ZIEL)
        self.fx.write(needs, [req("REQ-EDIT-008")])
        self.assertEqual([], self.fx.findings())

    def test_fundstelle_ausserhalb_der_o_toene_faellt_auf(self) -> None:
        needs = list(GOOD_NEEDS)
        needs[1] = need("B-01", "Bedürfnis", "I-01", "Lesen.", "wörtlich", "x", "../geheim.md#01.01.2026 Ziel")
        self.fx.write(needs, [req("REQ-EDIT-008")])
        self.assertIn("B-01: Fundstelle muss docs/o-toene.md sein, dort stehen die O-Töne", self.fx.findings())

    def test_o_ton_aus_falschem_abschnitt_faellt_auf(self) -> None:
        needs = list(GOOD_NEEDS)
        needs[1] = need("B-01", "Bedürfnis", "I-01", "Lesen.", "wörtlich", "wissen, was da steht", "docs/o-toene.md#01.01.2026 Kern")
        self.fx.write(needs, [req("REQ-EDIT-008")])
        self.assertTrue(any("nicht wörtlich in einem Zitat des genannten Abschnitts" in f for f in self.fx.findings()))

    def test_ueberschrift_anmerkung_und_wortbruchstueck_sind_kein_o_ton(self) -> None:
        for quote in ("Ziel ich will jede Quelle lesen", "Der Satz bezieht sich auf eine Notiz", "ill jede Quel"):
            needs = list(GOOD_NEEDS)
            needs[1] = need("B-01", "Bedürfnis", "I-01", "Lesen.", "wörtlich", quote, ZIEL)
            self.fx.write(needs, [req("REQ-EDIT-008")])
            self.assertTrue(any("nicht wörtlich" in f for f in self.fx.findings()), quote)

    def test_o_ton_ueber_zwei_zitate_hinweg_faellt_auf(self) -> None:
        (self.fx.root / "docs" / "o-toene.md").write_text(
            O_TOENE.replace("> Das Repo ist ein repo der Prosa.\n",
                            "> Das Repo ist ein repo der Prosa.\n\n> Es fehlt Funktion.\n>\n> […]\n>\n> Und mehr\n"),
            encoding="utf-8")
        for quote in ("der Prosa. Es fehlt", "Funktion. […] Und mehr", "Funktion. Und mehr"):
            needs = list(GOOD_NEEDS)
            needs[3] = need("P-01", "Pain", "B-01", "Prosa.", "wörtlich", quote, "docs/o-toene.md#01.01.2026 Kern")
            self.fx.write(needs, [req("REQ-EDIT-008")])
            self.assertTrue(any("nicht wörtlich" in f for f in self.fx.findings()), quote)

    def test_abschnittsname_muss_ganze_woerter_treffen(self) -> None:
        needs = list(GOOD_NEEDS)
        needs[4] = need("R-01", "Rahmen", "", "Deutsch.", "wörtlich", "Englisch ist falsch", "docs/o-toene.md#01.01.2026 S")
        self.fx.write(needs, [req("REQ-EDIT-008")])
        self.assertIn("R-01: Abschnitt '01.01.2026 S' gibt es nicht", self.fx.findings())

    def test_knopfwahl_ist_kein_eigener_wortlaut(self) -> None:
        needs = list(GOOD_NEEDS)
        needs[1] = need("B-01", "Bedürfnis", "I-01", "Lesen.", "wörtlich", "Ja, übernehmen", "docs/o-toene.md#01.01.2026 Zustimmung")
        self.fx.write(needs, [req("REQ-EDIT-008")])
        self.assertIn("B-01: Abschnitt '01.01.2026 Zustimmung' ist eine Knopfwahl, kein eigener Wortlaut", self.fx.findings())

    def test_unbekannter_oder_fehlender_abschnitt_faellt_auf(self) -> None:
        needs = list(GOOD_NEEDS)
        needs[1] = need("B-01", "Bedürfnis", "I-01", "Lesen.", "wörtlich", "wissen, was da steht", "docs/o-toene.md#02.01.2026 Ziel")
        needs[2] = need("B-02", "Bedürfnis", "I-01", "Einordnen.", "abgeleitet", "einordnen können", "docs/o-toene.md")
        self.fx.write(needs, [req("REQ-EDIT-008")])
        findings = self.fx.findings()
        self.assertIn("B-01: Abschnitt '02.01.2026 Ziel' gibt es nicht", findings)
        self.assertIn("B-02: Fundstelle nennt keinen Abschnitt (Datum und Überschrift nach #)", findings)

    def test_abhaengigkeit_von_spaeterer_stufe_faellt_auf(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-UX-005", applies="immer", depends="REQ-EDIT-006"), req("REQ-EDIT-006", applies="G2")])
        self.assertEqual(["REQ-UX-005 gilt ab immer, braucht aber REQ-EDIT-006, das erst ab G2 gilt"], self.fx.findings())

    def test_selbstverweis_wird_einmal_gemeldet(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-EDIT-008", depends="REQ-EDIT-008")])
        self.assertEqual(["REQ-EDIT-008: verweist in depends_on auf sich selbst"], self.fx.findings())

    def test_pain_muss_zu_beduerfnis_gehoeren(self) -> None:
        needs = list(GOOD_NEEDS)
        needs[3] = need("P-01", "Pain", "I-01", "Prosa.", "wörtlich", "ein repo der Prosa", "docs/o-toene.md#Kern")
        self.fx.write(needs, [req("REQ-EDIT-008")])
        self.assertIn("P-01: Pain muss zu einem Bedürfnis gehören, nicht zu I-01", self.fx.findings())

    def test_anforderung_ohne_bekannte_pruefung_faellt_auf(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-EDIT-008", verified=""),
                                   req("REQ-UX-003", verified="tests/test_beispiel.py::test_fehlt"),
                                   req("REQ-UX-004", verified="tests/test_gibtsnicht.py::test_x"),
                                   req("REQ-UX-005", verified="sieht gut aus")])
        findings = self.fx.findings()
        self.assertIn("REQ-EDIT-008: keine Angabe, was die Anforderung prüft (Test, Fachurteil, Gebrauch oder keine)", findings)
        self.assertIn("REQ-UX-003: Test test_fehlt steht nicht in tests/test_beispiel.py", findings)
        self.assertIn("REQ-UX-004: Testdatei tests/test_gibtsnicht.py gibt es nicht", findings)
        self.assertIn("REQ-UX-005: unbekannte Prüfangabe 'sieht gut aus'", findings)

    def test_keine_und_test_zugleich_ist_ein_widerspruch(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-EDIT-008", verified="keine;tests/test_beispiel.py::test_vorhanden")])
        self.assertIn("REQ-EDIT-008: „keine“ widerspricht den genannten Tests", self.fx.findings())

    def test_anforderung_ohne_beduerfnis_faellt_auf(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-EDIT-008", needs=""), req("REQ-UX-003", needs="B-99"),
                                   req("REQ-UX-004", needs="fach;B-01"), req("REQ-UX-005", needs="fach")])
        findings = self.fx.findings()
        self.assertIn("REQ-EDIT-008: dient keinem Bedürfnis und ist nicht als Fachanspruch („fach“) markiert", findings)
        self.assertIn("REQ-UX-003: unbekanntes Bedürfnis B-99", findings)
        self.assertIn("REQ-UX-004: „fach“ steht allein; sonst die Bedürfnisse nennen", findings)
        self.assertEqual(3, len(findings))

    def test_stufe_muss_bekannt_sein(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-EDIT-008", applies="bald"), req("REQ-UX-003", applies="Auslöser: Publikation")])
        self.assertEqual(["REQ-EDIT-008: „gilt ab“ muss immer, G1–G6 oder „Auslöser: …“ sein, nicht 'bald'"],
                         self.fx.findings())

    def test_abhaengigkeit_im_kreis_faellt_auf(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-EDIT-008", depends="REQ-UX-003"), req("REQ-UX-003", depends="REQ-EDIT-008")])
        self.assertTrue(any(f.startswith("Abhängigkeit im Kreis") for f in self.fx.findings()))

    def test_ueberschneidung_muss_beidseitig_sein(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-EDIT-008", overlaps="REQ-UX-003"), req("REQ-UX-003")])
        self.assertIn("REQ-EDIT-008: Überschneidung mit REQ-UX-003 ist nicht beidseitig eingetragen", self.fx.findings())

    def test_neue_anforderung_ohne_kettenspalten_faellt_auf(self) -> None:
        (self.fx.root / "requirements" / "domain-requirements.tsv").write_text(
            "requirement_id\tcurrent_support\nREQ-EDIT-008\tgap\n", encoding="utf-8")
        self.assertTrue(any("Kettenspalten fehlen" in f for f in self.fx.findings()))


class Ansicht(unittest.TestCase):
    def setUp(self) -> None:
        self.fx = Fixture()
        self.addCleanup(self.fx.close)
        self.view = kette.render(self.fx.root)

    def test_ansicht_zeigt_kette_vom_beduerfnis_zur_pruefung(self) -> None:
        self.assertIn("### B-01 Lesen.", self.view)
        self.assertIn("- Pain **P-01** Prosa statt Funktion.", self.view)
        self.assertIn("| EDIT-008 | Kurz | G2 | Test genannt (1) |", self.view)
        self.assertIn("| UX-003 | Kurz | G2 | **kein Test bekannt** |", self.view)

    def test_anforderung_fuer_rahmen_erscheint_in_der_ansicht(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-UX-012", needs="R-01", kurz="Alltagssprache")])
        self.assertIn("- **R-01** Deutsch. (wörtlich; O-Ton: „Englisch ist falsch“) Dient: UX-012 Alltagssprache.",
                      kette.render(self.fx.root))

    def test_zaehlung_ordnet_jede_anforderung_genau_einer_spalte_zu(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-A-001", verified="tests/test_beispiel.py::test_vorhanden"),
                                   req("REQ-A-002", verified="Fachurteil"),
                                   req("REQ-A-003", verified="keine;Fachurteil"),
                                   req("REQ-A-004", verified="Gebrauch")])
        self.assertIn("| G2 | 4 | 1 | 2 | 1 |", kette.render(self.fx.root))

    def test_ansicht_nennt_beduerfnis_ohne_anforderung(self) -> None:
        self.assertIn("### B-02 Einordnen.", self.view)
        self.assertIn("**Keine Anforderung dient diesem Bedürfnis.** Das ist eine Lücke.", self.view)
        self.assertIn("## Bedürfnisse ohne Anforderung\n\n- **B-02** Einordnen.", self.view)

    def test_ansicht_nennt_tests_ohne_anforderung(self) -> None:
        self.assertIn("- `tests/test_verwaist.py`", self.view)
        self.assertNotIn("- `tests/test_beispiel.py`", self.view)

    def test_selbstbewertung_ohne_test_wird_gezaehlt(self) -> None:
        self.fx.write(GOOD_NEEDS, [req("REQ-EDIT-008", support="adequate", verified="Fachurteil"),
                                   req("REQ-UX-003", support="adequate method / not yet exercised", verified="keine")])
        self.assertIn("Bei **1** Anforderungen lautet die Selbstbewertung", kette.render(self.fx.root))
        self.assertIn("aber kein Test ist genannt: EDIT-008.", kette.render(self.fx.root))

    def test_luecken_tabelle_nennt_abhaengigkeit(self) -> None:
        self.assertIn("| G2 | UX-003 | Kurz | P-01 | EDIT-008 |", self.view)

    def test_pruefen_meldet_veraltete_ansicht(self) -> None:
        self.assertEqual(1, kette.main(["pruefen", "--root", str(self.fx.root)]))
        self.assertEqual(0, kette.main(["schreiben", "--root", str(self.fx.root)]))
        self.assertEqual(0, kette.main(["pruefen", "--root", str(self.fx.root)]))


FUNC_HEADER = "\t".join(kette.FUNC_COLUMNS)
ALL_ASPECTS = ";".join(a for a in kette.ASPECTS if a != "Nutzer")


def func(fid: str = "FN-01", rang: str = "1", braucht: str = "", sichert: str = "REQ-UX-003",
         befunde: str = "Nutzer: Will mitlesen [belegt: B-01]", ohne: str = ALL_ASPECTS,
         dod: str = "`tests/test_beispiel.py` prüft es", status: str = "Vorschlag", schmerz: str = "Fehlt.") -> str:
    values = {"id": fid, "name": "Name", "zweck": "Zweck.", "sichert": sichert, "lindert": "B-01", "schmerz": schmerz,
              "befunde": befunde, "ohne_befund": ohne, "groesse": "hoch", "aufwand": "klein", "braucht": braucht,
              "bestand": "", "dor": "bereit", "dod": dod, "iteration": "1: erst", "rang": rang,
              "begruendung": "weil", "status": status, "issue": ""}
    return "\t".join(values[c] for c in kette.FUNC_COLUMNS)


class Funktionen(unittest.TestCase):
    def setUp(self) -> None:
        self.fx = Fixture()
        self.addCleanup(self.fx.close)

    def write(self, *rows: str) -> list[str]:
        (self.fx.root / kette.FUNC_PATH).write_text("\n".join([FUNC_HEADER, *rows]) + "\n", encoding="utf-8")
        return self.fx.findings()

    def test_gueltige_funktion_hat_keine_befunde(self) -> None:
        self.assertEqual([], self.write(func()))

    def test_unbedachte_perspektive_faellt_auf(self) -> None:
        findings = self.write(func(ohne=ALL_ASPECTS.replace("Recht;", "")))
        self.assertIn("FN-01: Recht ist nicht bedacht (Befund oder „ohne Befund“)", findings)

    def test_befund_ohne_herkunft_faellt_auf(self) -> None:
        findings = self.write(func(befunde="Nutzer: Will mitlesen"))
        self.assertTrue(any("braucht die Form" in f for f in findings), findings)

    def test_doppelt_bedachte_perspektive_faellt_auf(self) -> None:
        findings = self.write(func(ohne=ALL_ASPECTS + ";Nutzer"))
        self.assertIn("FN-01: Nutzer steht doppelt", findings)

    def test_was_gebraucht_wird_kommt_zuerst(self) -> None:
        self.assertEqual([], self.write(func("FN-01", rang="2", braucht="FN-02"), func("FN-02", rang="1")))
        findings = self.write(func("FN-01", rang="1", braucht="FN-02"), func("FN-02", rang="2"))
        self.assertIn("FN-01 (Rang 1) braucht FN-02 (Rang 2); was gebraucht wird, kommt zuerst", findings)

    def test_dod_ohne_test_faellt_auf(self) -> None:
        findings = self.write(func(dod="sieht gut aus"))
        self.assertIn("FN-01: DOD nennt keinen Test (tests/test_….py), an dem „fertig“ prüfbar ist", findings)

    def test_fertig_verlangt_vorhandenen_test_und_gepruefte_anforderung(self) -> None:
        findings = self.write(func(status="fertig", dod="`tests/test_fehlt.py` prüft es"))
        self.assertIn("FN-01: fertig, aber tests/test_fehlt.py gibt es nicht", findings)
        self.assertIn("FN-01: fertig, aber REQ-UX-003 nennt noch keinen Test", findings)

    def test_unbekannte_anforderung_faellt_auf(self) -> None:
        self.assertIn("FN-01: unbekannte Anforderung REQ-XX-999", self.write(func(sichert="REQ-XX-999")))

    def test_issue_text_darf_keine_kontextwurst_sein(self) -> None:
        findings = self.write(func(schmerz="lang " * 900))
        self.assertIn(f"FN-01: Issue-Text länger als {kette.MAX_ISSUE_CHARS} Zeichen; kürzen statt Kontextwurst",
                      findings)

    def test_ansicht_zeigt_rang_und_luecken_ohne_funktion(self) -> None:
        self.write(func(sichert="REQ-EDIT-008"))
        view = kette.render(self.fx.root)
        self.assertIn("| 1 | FN-01 Name | hoch | klein | EDIT-008 | B-01 |  | Vorschlag |  |", view)
        self.assertIn("## Lücken bis G3 ohne Funktion", view)
        self.assertIn("- UX-003 Kurz (G2)", view)

    def test_issue_text_hat_dor_und_dod_als_abhakliste(self) -> None:
        self.write(func())
        _, rows = kette.read_tsv(self.fx.root / kette.FUNC_PATH)
        _, reqs = kette.read_tsv(self.fx.root / kette.REQS_PATH)
        _, needs = kette.read_tsv(self.fx.root / kette.NEEDS_PATH)
        body = kette.issue_body(rows[0], {r["requirement_id"]: r for r in reqs}, {n["id"]: n for n in needs})
        self.assertIn("**DOR (bereit, wenn):**\n- [ ] bereit", body)
        self.assertIn("**DOD (fertig, wenn):**\n- [ ] `tests/test_beispiel.py` prüft es", body)
        self.assertIn("**Sichert:** UX-003 Kurz (**kein Test bekannt**)", body)


class EchteFunktionen(unittest.TestCase):
    def test_funktionstabelle_liegt_vor_und_jede_funktion_hat_rang(self) -> None:
        _, rows = kette.read_tsv(REPO / kette.FUNC_PATH)
        self.assertGreaterEqual(len(rows), 1)
        self.assertEqual(sorted(int(r["rang"]) for r in rows), list(range(1, len(rows) + 1)))


if __name__ == "__main__":
    unittest.main()
