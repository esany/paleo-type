from __future__ import annotations

import csv
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
        self.assertEqual(14, report["fixture_family_count"])
        self.assertEqual({f"ENG-FIT-{i:02d}" for i in range(1, 10)}, set(report["checks"]))

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
        for extra in (
            "requirements/system-development-bugwave-assurance-closure-design-2026-10-04.md",
            "requirements/outcome-preserving-execution-control-d016-owner-admission-2026-10-05.md",
        ):
            source = REPO / extra
            destination = target / extra
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
