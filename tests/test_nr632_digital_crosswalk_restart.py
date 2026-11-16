from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


class Nr632DigitalCrosswalkRestartTests(unittest.TestCase):
    def test_project_context_exposes_exact_compact_pdf_and_digital_crosswalk(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(REPO / "tools" / "project_context.py"), "--project", "ssta-20578-nr-632"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, proc.returncode, proc.stderr)
        result = json.loads(proc.stdout)

        self.assertIn(
            "corpus/source-data/SSTA-ARCHIVIALE-EDD69AA1/digital-crosswalk.tsv",
            result["canonical_references"]["digital_crosswalk_paths"],
        )
        self.assertIn(
            "FILE-SSTA-20578-NR632-COMPACT-PDF-20261029",
            result["canonical_references"]["file_ids"],
        )

    def test_resolver_returns_all_135_file_bound_digital_mappings(self) -> None:
        proc = subprocess.run(
            [
                sys.executable,
                str(REPO / "tools" / "source_contract.py"),
                "resolve",
                "--project",
                "ssta-20578-nr-632",
                "--source-id",
                "SSTA-ARCHIVIALE-EDD69AA1",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, proc.returncode, proc.stderr)
        result = json.loads(proc.stdout)
        rows = result["digital_crosswalk"]
        self.assertEqual(135, len(rows))
        self.assertEqual("0001", rows[0]["provider_image"])
        self.assertEqual("1", rows[0]["pdf_page"])
        self.assertEqual("0135", rows[-1]["provider_image"])
        self.assertEqual("135", rows[-1]["pdf_page"])
        self.assertTrue(all(row["provider_file_id"].startswith("FILE-SSTA-20578-NR632-IMG") for row in rows))
        self.assertTrue(all(row["pdf_file_id"] == "FILE-SSTA-20578-NR632-COMPACT-PDF-20261029" for row in rows))


if __name__ == "__main__":
    unittest.main()
