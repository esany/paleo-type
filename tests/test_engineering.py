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
    def test_engineering_baseline_passes_and_carries_all_findings(self) -> None:
        errors, summary = engineering.validate(REPO)
        self.assertEqual([], errors)
        self.assertEqual(45, summary["finding_count"])
        self.assertEqual("admitted", summary["admission"])
        self.assertEqual("implementing", summary["lifecycle"])
        self.assertEqual("github-issue:esany/paleo-type#261", summary["current_focus"]["ref"])

    def test_implemented_target_is_not_current_architecture_baseline(self) -> None:
        configuration = json.loads((REPO / "engineering" / "configuration.json").read_text(encoding="utf-8"))
        self.assertEqual(2, configuration["schema_version"])
        self.assertEqual(["artifact:ENG-A-0004"], configuration["architecture_baselines"])
        self.assertNotIn("artifact:ENG-A-0031", configuration["architecture_baselines"])
        self.assertEqual("implemented", configuration["change_states"]["change:SD-KA-01"]["transition_state"])
        self.assertEqual("pending", configuration["change_states"]["change:SD-KA-01"]["accepted_consequence"])
        self.assertEqual("github-issue:esany/paleo-type#261", configuration["current_focus"]["ref"])
        self.assertGreaterEqual(len(configuration["applicability"]), 4)

    def test_wp5_verified_and_wp6_active_qualification(self) -> None:
        state = json.loads((REPO / "engineering" / "changes" / "SD-KA-01" / "STATE.json").read_text(encoding="utf-8"))
        self.assertEqual("verified", state["work_package_status"]["WP1"])
        self.assertEqual("verified", state["work_package_status"]["WP2"])
        self.assertEqual("verified", state["work_package_status"]["WP3"])
        self.assertEqual("verified", state["work_package_status"]["WP4"])
        self.assertEqual("verified", state["work_package_status"]["WP5"])
        self.assertEqual("implementing", state["work_package_status"]["WP6"])
        self.assertEqual("github-issue:esany/paleo-type#261", state["work_owner"])
        self.assertIn("WP6 is executing", state["current_execution"])
        self.assertIn("moving unclassified or ambiguous artifacts by filename guess", state["non_goals"])

    def test_current_view_exposes_active_wp6_qualification(self) -> None:
        errors, current = engineering.compile_current_state(REPO)
        self.assertEqual([], errors)
        self.assertEqual("derived-current-engineering-state", current["view_kind"])
        self.assertEqual("artifact:ENG-A-0004", current["accepted_configuration"]["architecture_baselines"][0]["ref"])
        self.assertEqual("change:SD-KA-01", current["active_changes"][0]["ref"])
        self.assertEqual("implemented", current["active_changes"][0]["transition_state"])
        self.assertEqual("active", current["current_focus"]["state"])
        self.assertEqual("github-issue:esany/paleo-type#261", current["current_focus"]["ref"])
        self.assertFalse(current["explicit_absence"]["current_focus"])
        self.assertFalse(current["explicit_absence"]["active_changes"])
        self.assertEqual([], current["applicability"])
        self.assertNotIn("projects", current)
        self.assertFalse((REPO / "engineering" / "generated" / "CURRENT_STATE.json").exists())

    def test_explicit_absence_does_not_invent_replacement_focus(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            config_path = fixture / "engineering" / "configuration.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["active_changes"] = []
            config["change_states"] = {}
            config["current_focus"] = None
            config["applicability"] = []
            config_path.write_text(json.dumps(config), encoding="utf-8")
            errors, current = engineering.compile_current_state(fixture)
            self.assertEqual([], errors)
            self.assertEqual([], current["active_changes"])
            self.assertEqual("absent", current["current_focus"]["state"])
            self.assertTrue(current["explicit_absence"]["active_changes"])
            self.assertTrue(current["explicit_absence"]["current_focus"])

    def test_concurrent_change_does_not_manufacture_focus(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            (fixture / "engineering" / "changes" / "OTHER").mkdir()
            config_path = fixture / "engineering" / "configuration.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["active_changes"].append("change:OTHER")
            config["change_states"]["change:OTHER"] = {
                "transition_state": "proposed",
                "basis_ref": "artifact:ENG-A-0014",
                "work_owner": "github-issue:esany/paleo-type#999",
                "accepted_consequence": "pending",
            }
            config_path.write_text(json.dumps(config), encoding="utf-8")
            errors, current = engineering.compile_current_state(fixture)
            self.assertEqual([], errors)
            self.assertEqual(2, len(current["active_changes"]))
            self.assertEqual("absent", current["current_focus"]["state"])
            self.assertEqual("artifact:ENG-A-0004", current["accepted_configuration"]["architecture_baselines"][0]["ref"])

    def test_newer_proposed_artifact_does_not_win_currentness(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            artifact_path = fixture / "engineering" / "catalog" / "artifacts.tsv"
            rows = self._read_rows(artifact_path)
            rows.append({
                "artifact_id": "ENG-A-9998",
                "kind": "design",
                "path": "engineering/changes/SD-KA-01/DESIGN.md",
                "owner_scope": "SD-KA-01",
                "authority_role": "non-normative-evidence",
                "lifecycle_state": "proposed",
                "change_id": "SD-KA-01",
                "title": "Later-looking proposal that must not win by recency",
            })
            self._write_rows(artifact_path, rows)
            errors, current = engineering.compile_current_state(fixture)
            self.assertEqual([], errors)
            self.assertEqual("artifact:ENG-A-0004", current["accepted_configuration"]["architecture_baselines"][0]["ref"])
            self.assertEqual("absent", current["current_focus"]["state"])

    def test_work_metadata_cannot_become_current_baseline(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            config_path = fixture / "engineering" / "configuration.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["architecture_baselines"] = ["artifact:ENG-A-0054"]
            config_path.write_text(json.dumps(config), encoding="utf-8")
            errors, _ = engineering.validate(fixture)
            self.assertTrue(any("cannot point at non-accepted artifact" in error for error in errors), errors)

    def test_proposed_adr_cannot_become_current_baseline(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            config_path = fixture / "engineering" / "configuration.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["architecture_baselines"] = ["artifact:ENG-A-0031"]
            config_path.write_text(json.dumps(config), encoding="utf-8")
            errors, _ = engineering.validate(fixture)
            self.assertTrue(any("cannot point at non-accepted artifact" in error for error in errors), errors)

    def test_invalid_applicability_basis_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            config_path = fixture / "engineering" / "configuration.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["applicability"] = [{
                "ref": "artifact:ENG-A-0016",
                "basis_kind": "latest-wins",
                "basis_ref": "github-issue:esany/paleo-type#261",
                "scope": "invalid fixture",
            }]
            config_path.write_text(json.dumps(config), encoding="utf-8")
            errors, _ = engineering.validate(fixture)
            self.assertTrue(any("invalid basis_kind" in error for error in errors), errors)

    def test_invalid_change_transition_state_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            config_path = fixture / "engineering" / "configuration.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["change_states"]["change:SD-KA-01"]["transition_state"] = "latest"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            errors, _ = engineering.validate(fixture)
            self.assertTrue(any("invalid transition_state" in error for error in errors), errors)

    def test_transition_contract_distinguishes_acceptance_and_no_change(self) -> None:
        self.assertTrue(engineering.transition_allowed("proposed", "admitted"))
        self.assertTrue(engineering.transition_allowed("admitted", "implemented"))
        self.assertTrue(engineering.transition_allowed("verified", "accepted"))
        self.assertTrue(engineering.transition_allowed("verified", "no-change"))
        self.assertFalse(engineering.transition_allowed("proposed", "accepted"))
        self.assertFalse(engineering.transition_allowed("admitted", "accepted"))

    def test_broken_relation_reference_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            relation_path = fixture / "engineering" / "catalog" / "relations.tsv"
            rows = self._read_rows(relation_path)
            rows[0]["object_ref"] = "artifact:ENG-A-9999"
            self._write_rows(relation_path, rows)
            errors, _ = engineering.validate(fixture)
            self.assertTrue(any("unresolved object_ref" in error for error in errors), errors)

    def test_query_filters_catalog_without_chronology(self) -> None:
        rows = engineering.query_artifacts(REPO, authority_role="work-metadata", owner_scope="SD-KA-01")
        ids = {row["artifact_id"] for row in rows}
        self.assertIn("ENG-A-0054", ids)
        self.assertIn("ENG-A-0114", ids)
        active = engineering.query_artifacts(REPO, authority_role="work-metadata", owner_scope="SD-KA-01", lifecycle="active")
        active_ids = {row["artifact_id"] for row in active}
        self.assertIn("ENG-A-0114", active_ids)
        self.assertNotIn("ENG-A-0054", active_ids)

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
