from __future__ import annotations

import csv
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools import engineering


REPO = Path(__file__).resolve().parents[1]


class EngineeringContractTests(unittest.TestCase):
    def test_wp1_baseline_passes_and_carries_all_findings(self) -> None:
        errors, summary = engineering.validate(REPO)
        self.assertEqual([], errors)
        self.assertEqual(45, summary["finding_count"])
        self.assertEqual("admitted", summary["admission"])
        self.assertEqual("implementing", summary["lifecycle"])

    def test_admitted_target_is_not_current_architecture_baseline(self) -> None:
        configuration = json.loads((REPO / "engineering" / "configuration.json").read_text(encoding="utf-8"))
        self.assertEqual(["artifact:ENG-A-0004"], configuration["architecture_baselines"])
        self.assertNotIn("artifact:ENG-A-0031", configuration["architecture_baselines"])
        self.assertIsNone(configuration["current_focus"])

    def test_wp1_excludes_bulk_migration(self) -> None:
        state = json.loads((REPO / "engineering" / "changes" / "SD-KA-01" / "STATE.json").read_text(encoding="utf-8"))
        self.assertIn("bulk requirements migration in WP1", state["non_goals"])

    def test_broken_relation_reference_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            relation_path = fixture / "engineering" / "catalog" / "relations.tsv"
            rows = self._read_rows(relation_path)
            rows[0]["object_ref"] = "artifact:ENG-A-9999"
            self._write_rows(relation_path, rows)
            errors, _ = engineering.validate(fixture)
            self.assertTrue(any("unresolved object_ref" in error for error in errors), errors)

    def test_proposed_artifact_cannot_become_current_baseline(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            config_path = fixture / "engineering" / "configuration.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["architecture_baselines"] = ["artifact:ENG-A-0031"]
            config_path.write_text(json.dumps(config), encoding="utf-8")
            errors, _ = engineering.validate(fixture)
            self.assertTrue(any("cannot point at non-accepted artifact" in error for error in errors), errors)

    def _copy_contract_fixture(self, target: Path) -> Path:
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / "DECISIONS.md", target / "DECISIONS.md")
        shutil.copytree(REPO / "engineering", target / "engineering")
        _, artifacts = engineering.read_tsv(REPO / "engineering" / "catalog" / "artifacts.tsv")
        for row in artifacts:
            raw_path = row["path"]
            if raw_path.startswith("github://"):
                continue
            source = REPO / raw_path
            destination = target / raw_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        return target

    @staticmethod
    def _read_rows(path: Path) -> list[dict[str, str]]:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle, delimiter="\t"))

    @staticmethod
    def _write_rows(path: Path, rows: list[dict[str, str]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    unittest.main()
