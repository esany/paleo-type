"""Derived edition (text only) contracts for Nr. 632."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from edition_build import build_site


class EditionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.dest = self.root / "site"
        p = self.root / "projects/ssta-20578-nr-632"
        r = p / "research"
        r.mkdir(parents=True)
        self.readings = r / "transcription-pilot-fixture.md"
        self.readings.write_text(
            "PROSA NICHT AUSGEBEN\n"
            "| Local physical line | Reading | Note |\n"
            "|---|---|---|\n"
            "| \`0104R-A01\` | \`Herr [Name?]\` | unsicher am Schriftbild |\n"
            "| \`0104R-A02\` | \`ALT\` | früher |\n"
            "\n| Local physical line | Reading | Note |\n"
            "|---|---|---|\n"
            "| \`0104R-A02\` | \`NEU\` | gegen Bild nachgelesen |\n",
            encoding="utf-8",
        )
        (r / "content-document-function-inventory-2026-10-30.md").write_text(
            "| PDF-/Providerbild-Bereich | Dokumentfunktion / Textzone (I) | Datum / Akteure (L, nur soweit unterstützt) | Direkte Anker und historische Rolle (P/L/H) | Sicherheit und offene Grenze |\n"
            "|---|---|---|---|---|\n"
            "| 0103–0107 | Gesuch | 3. Juli 1760 | Beobachtung | Anschluss offen |\n",
            encoding="utf-8",
        )
        (p / "STATUS.md").write_text(
            "- **Forschungsstand:** KI-Arbeitslesung.\n"
            "- **Nächste fachliche Aktion:** Gegenlesung.\n"
            "- **Sperre:** 0112R gesperrt.\n", encoding="utf-8"
        )
        (self.root / "corpus").mkdir()
        (self.root / "corpus/sources.tsv").write_text(
            "source_id\tdigital_url\n"
            "SSTA-ARCHIVIALE-EDD69AA1\thttps://www.archiv.sachsen.de/archiv/bestand.jsp?guid=abc\n",
            encoding="utf-8",
        )

    def html(self):
        build_site(self.root, self.dest)
        return (self.dest / "index.html").read_text(encoding="utf-8")

    def test_uncertainty_marked_and_clickable(self):
        h = self.html()
        self.assertIn('class="uncertain"', h)
        self.assertIn("[Name?]", h)
        self.assertIn("<details", h)
        self.assertIn("unsicher am Schriftbild", h)

    def test_unchecked_page_stays_draft(self):
        self.assertIn("KI-Entwurf, ungeprüft", self.html())

    def test_prose_and_superseded_table_rows_not_published(self):
        h = self.html()
        self.assertIn("NEU", h)
        self.assertNotIn(">ALT<", h)
        self.assertNotIn("PROSA NICHT AUSGEBEN", h)
        self.assertIn('id="line-0104r-a02"', h)

    def test_fixed_addresses_and_stylesheet(self):
        h = self.html()
        self.assertIn('id="doc-0103-0107"', h)
        self.assertIn('id="page-0104r"', h)
        self.assertTrue((self.dest / "style.css").exists())


if __name__ == "__main__":
    unittest.main()
