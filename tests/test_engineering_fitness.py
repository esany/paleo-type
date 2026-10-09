from __future__ import annotations

import csv
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools import engineering, engineering_fitness


REPO = Path(__file__).resolve().parents[1]


class EngineeringFitnessTests(unittest.TestCase):
    def test_repository_fitness_contract_passes(self) -> None:
        errors, report = engineering_fitness.run_fitness(REPO)
        self.assertEqual([], errors)
        self.assertEqual("PASS", report["status"])
        self.assertEqual(20, report["fixture_family_count"])
        self.assertEqual({f"ENG-FIT-{i:02d}" for i in range(1, 10)}, set(report["checks"]))
        self.assertEqual("active", report["checks"]["ENG-FIT-08"]["applicability"])
        self.assertGreater(report["checks"]["ENG-FIT-08"]["row_count"], 0)

    def test_orphan_finding_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            path = fixture / "engineering" / "catalog" / "findings.tsv"
            rows = self._read_rows(path)
            rows = [row for row in rows if row["finding_id"] != "F45"]
            self._write_rows(path, rows)
            errors, _ = engineering_fitness.run_fitness(fixture)
            self.assertTrue(any("expected exactly F01–F45" in error for error in errors), errors)

    def test_coverage_loophole_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            path = fixture / "engineering" / "catalog" / "coverage.tsv"
            rows = self._read_rows(path)
            refs = [item for item in rows[0]["finding_refs"].split(";") if item and item != "F45"]
            rows[0]["finding_refs"] = ";".join(refs)
            self._write_rows(path, rows)
            errors, _ = engineering_fitness.run_fitness(fixture)
            self.assertTrue(any("coverage must account for each F01–F45 exactly once" in error for error in errors), errors)

    def test_missing_transition_authority_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            path = fixture / "engineering" / "configuration.json"
            config = json.loads(path.read_text(encoding="utf-8"))
            config["change_states"]["change:SD-KA-01"]["basis_ref"] = "artifact:ENG-A-9999"
            path.write_text(json.dumps(config), encoding="utf-8")
            errors, _ = engineering_fitness.run_fitness(fixture)
            self.assertTrue(any("unresolved basis_ref" in error for error in errors), errors)

    def test_committed_generated_current_view_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            generated = fixture / "engineering" / "generated"
            generated.mkdir()
            (generated / "CURRENT_STATE.json").write_text('{"stale": true}\n', encoding="utf-8")
            errors, _ = engineering_fitness.run_fitness(fixture)
            self.assertTrue(any("committed CURRENT_STATE.json is forbidden" in error for error in errors), errors)

    def test_verified_package_requires_whole_system_return(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            path = fixture / "engineering" / "changes" / "SD-KA-01" / "STATE.json"
            state = json.loads(path.read_text(encoding="utf-8"))
            state["whole_system_return"] = ""
            path.write_text(json.dumps(state), encoding="utf-8")
            errors, _ = engineering_fitness.run_fitness(fixture)
            self.assertTrue(any("whole_system_return is required" in error for error in errors), errors)

    def test_accepted_relation_requires_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            path = fixture / "engineering" / "catalog" / "relations.tsv"
            rows = self._read_rows(path)
            rows[0]["evidence_ref"] = ""
            self._write_rows(path, rows)
            errors, _ = engineering_fitness.run_fitness(fixture)
            self.assertTrue(any("unresolved evidence_ref" in error for error in errors), errors)

    def test_legacy_path_migration_row_must_match_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            path = fixture / "engineering" / "catalog" / "legacy-paths.tsv"
            rows = [{
                "legacy_path": "old/GOVERNING_OBJECTIVE.md",
                "artifact_id": "ENG-A-0001",
                "current_path": "wrong/path.md",
                "migration_commit": "0" * 40,
            }]
            self._write_rows(path, rows, fieldnames=engineering_fitness.LEGACY_HEADERS)
            errors, _ = engineering_fitness.run_fitness(fixture)
            self.assertTrue(any("does not match catalog path" in error for error in errors), errors)

    def test_wp5_migration_preserves_ids_paths_and_exact_pre_move_bytes(self) -> None:
        artifacts = {row["artifact_id"]: row for row in self._read_rows(REPO / "engineering" / "catalog" / "artifacts.tsv")}
        legacy = {row["artifact_id"]: row for row in self._read_rows(REPO / "engineering" / "catalog" / "legacy-paths.tsv")}
        migration = self._read_rows(REPO / "engineering" / "changes" / "SD-KA-01" / "MIGRATION.tsv")
        self.assertEqual(74, len(migration))
        for row in migration:
            artifact_id = row["artifact_id"]
            self.assertIn(artifact_id, artifacts)
            self.assertIn(artifact_id, legacy)
            self.assertEqual(row["current_path"], artifacts[artifact_id]["path"])
            self.assertEqual(row["legacy_path"], legacy[artifact_id]["legacy_path"])
            self.assertEqual(row["current_path"], legacy[artifact_id]["current_path"])
            self.assertRegex(legacy[artifact_id]["migration_commit"], r"^[0-9a-f]{40}$")
            self.assertFalse((REPO / row["legacy_path"]).exists(), row["legacy_path"])
            current = REPO / row["current_path"]
            self.assertTrue(current.is_file(), row["current_path"])
            data = current.read_bytes()
            git_blob = hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()
            self.assertEqual(row["baseline_blob_sha"], git_blob, artifact_id)

    def test_wp5_requirements_namespace_is_narrow_and_fully_classified(self) -> None:
        expected = {"README.md", "domain-requirements.tsv"}
        actual = {path.name for path in (REPO / "requirements").iterdir() if path.is_file()}
        self.assertEqual(expected, actual)
        artifacts = self._read_rows(REPO / "engineering" / "catalog" / "artifacts.tsv")
        managed_paths = {row["path"] for row in artifacts}
        for name in expected:
            self.assertIn(f"requirements/{name}", managed_paths)
        decisions = {
            row["artifact_id"]: row
            for row in artifacts
            if row["artifact_id"] in {"ENG-A-0053", "ENG-A-0110", "ENG-A-0111", "ENG-A-0112", "ENG-A-0113"}
        }
        self.assertEqual(5, len(decisions))
        for row in decisions.values():
            self.assertEqual("cross-project", row["owner_scope"])
            self.assertTrue(row["path"].startswith("engineering/evidence/decisions/"), row)

    def test_wp5_requirements_baseline_stays_put_and_old_paths_are_not_parallel_truth(self) -> None:
        self.assertTrue((REPO / "requirements" / "domain-requirements.tsv").is_file())
        self.assertTrue((REPO / "requirements" / "README.md").is_file())
        migration = self._read_rows(REPO / "engineering" / "changes" / "SD-KA-01" / "MIGRATION.tsv")
        for row in migration:
            self.assertFalse((REPO / row["legacy_path"]).exists(), row["legacy_path"])
            self.assertTrue((REPO / row["current_path"]).is_file(), row["current_path"])

    def test_fitness_mapping_must_cover_all_seeded_families(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            path = fixture / "engineering" / "assurance" / "fitness.json"
            contract = json.loads(path.read_text(encoding="utf-8"))
            contract["fixture_families"].pop("exact-head")
            path.write_text(json.dumps(contract), encoding="utf-8")
            errors, _ = engineering_fitness.run_fitness(fixture)
            self.assertTrue(any("fixture families mismatch" in error for error in errors), errors)

    def _copy_contract_fixture(self, target: Path) -> Path:
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / "DECISIONS.md", target / "DECISIONS.md")
        shutil.copytree(REPO / "engineering", target / "engineering")
        (target / "tools").mkdir()
        for name in ("engineering.py", "engineering_context.py", "engineering_fitness.py", "prompt.py"):
            shutil.copy2(REPO / "tools" / name, target / "tools" / name)
        (target / "tests").mkdir()
        shutil.copy2(REPO / "tests" / "test_prompt.py", target / "tests" / "test_prompt.py")
        _, artifacts = engineering.read_tsv(REPO / "engineering" / "catalog" / "artifacts.tsv")
        for row in artifacts:
            raw_path = row["path"]
            if raw_path.startswith("github://"):
                continue
            source = REPO / raw_path
            if not source.is_file():
                continue
            destination = target / raw_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        return target

    @staticmethod
    def _read_rows(path: Path) -> list[dict[str, str]]:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle, delimiter="\t"))

    @staticmethod
    def _write_rows(path: Path, rows: list[dict[str, str]], fieldnames: list[str] | None = None) -> None:
        if fieldnames is None:
            fieldnames = list(rows[0])
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    unittest.main()
