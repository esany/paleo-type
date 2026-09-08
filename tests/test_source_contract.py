from __future__ import annotations

import contextlib
import csv
import importlib.util
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("source_contract", REPO / "tools" / "source_contract.py")
source_contract = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(source_contract)


def write_tsv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=headers, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


class CurrentRepositoryRegressionTests(unittest.TestCase):
    def test_current_repository_validates_project_use_state(self) -> None:
        contract = source_contract.load_contract(REPO)
        self.assertEqual(8, contract["version"])
        errors, _, cache = source_contract.validate(REPO, contract)
        self.assertEqual([], errors)
        self.assertFalse(cache["project_sources"])
        self.assertEqual(6, len(cache["source_uses"]))
        self.assertEqual(6, len(cache["use_evidence"]))

        principal = cache["source_uses"]["USE-REGII5-00000129-PRINCIPAL"]
        self.assertEqual("THHSTAW-EGA-REG-II-5-STAT-VIS-00000129", principal["source_id"])
        self.assertEqual("principal", principal["research_function"])
        self.assertEqual("fol. 61v–63r", principal["relevant_locus"])
        self.assertEqual("active", principal["status"])
        self.assertIn("loss-checked migration 2026-09-02", principal["evidence_basis"])
        self.assertIn("#123", principal["evidence_basis"])
        self.assertIn("fol. 55v–66v", principal["notes"])
        self.assertIn("does not authorize source-wide transcription", principal["notes"])

        evidence = cache["use_evidence"]["EVID-REGII5-00000129-PRINCIPAL"]
        self.assertEqual("USE-REGII5-00000129-PRINCIPAL", evidence["use_id"])
        self.assertEqual("FILE-REG-II-5-00000129-EXCERPT", evidence["file_id"])
        self.assertEqual("active", evidence["status"])
        self.assertIn("#123", evidence["evidence_basis"])
        self.assertIn("does not establish current STAGED or VISION-INSPECTABLE readiness", evidence["notes"])

        li4_principal = cache["source_uses"]["USE-REGII4PROJ-REGII4-00000089-PRINCIPAL"]
        self.assertEqual("THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089", li4_principal["source_id"])
        self.assertEqual("principal", li4_principal["research_function"])
        self.assertEqual("historical", li4_principal["status"])

        li4_comparison = cache["source_uses"]["USE-REGII4PROJ-REGII5-00000129-TEXTUAL-COMPARISON"]
        self.assertEqual("THHSTAW-EGA-REG-II-5-STAT-VIS-00000129", li4_comparison["source_id"])
        self.assertEqual("textual-comparison", li4_comparison["research_function"])
        self.assertEqual("historical", li4_comparison["status"])

        li4_principal_evidence = cache["use_evidence"]["EVID-REGII4PROJ-REGII4-00000089-PRINCIPAL"]
        self.assertEqual("USE-REGII4PROJ-REGII4-00000089-PRINCIPAL", li4_principal_evidence["use_id"])
        self.assertEqual("FILE-REG-II-4-II-00000089-EXPORT", li4_principal_evidence["file_id"])

        li4_comparison_evidence = cache["use_evidence"]["EVID-REGII4PROJ-REGII5-00000129-TEXTUAL-COMPARISON"]
        self.assertEqual("USE-REGII4PROJ-REGII5-00000129-TEXTUAL-COMPARISON", li4_comparison_evidence["use_id"])
        self.assertEqual("FILE-REG-II-5-00000129-EXCERPT", li4_comparison_evidence["file_id"])

        for project_id, meta in cache["projects"].items():
            self.assertTrue(meta["research_object"], project_id)
            self.assertTrue(meta["active_scope"], project_id)
            self.assertEqual("source-uses.tsv", meta["source_register"])
            self.assertTrue((REPO / "projects" / project_id / meta["source_register"]).is_file())
            self.assertTrue((REPO / "projects" / project_id / meta["canonical_status_file"]).is_file())

    def test_current_resolver_uses_target_use_evidence_without_legacy_primary_file(self) -> None:
        args = SimpleNamespace(
            root=str(REPO),
            project="ega-reg-ii-5-knau",
            source_id="THHSTAW-EGA-REG-II-5-STAT-VIS-00000129",
            locus=None,
        )
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = source_contract.cmd_resolve(args)
        self.assertEqual(0, rc)
        resolved = json.loads(out.getvalue())
        self.assertEqual("internal", resolved["structural_status"])
        self.assertEqual(["principal"], resolved["research_functions"])
        self.assertIsNone(resolved["legacy_project_source"])
        self.assertIsNone(resolved["legacy_primary_file"])
        self.assertEqual(1, len(resolved["project_source_uses"]))
        target = resolved["project_source_uses"][0]
        self.assertEqual("active", target["use"]["status"])
        self.assertEqual("fol. 61v–63r", target["use"]["relevant_locus"])
        self.assertEqual("active", target["evidence"][0]["evidence"]["status"])
        self.assertEqual(
            "FILE-REG-II-5-00000129-EXCERPT",
            target["evidence"][0]["file"]["file_id"],
        )

    def test_rel008_uses_pure_source_ids_and_separate_loci_without_strength_change(self) -> None:
        row = next(
            row for row in read_tsv(REPO / "corpus" / "relationships.tsv") if row["relation_id"] == "REL008"
        )
        self.assertEqual("THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089", row["subject_id"])
        self.assertEqual("306v-309r", row["subject_locus"])
        self.assertEqual("textually_corresponds_to", row["predicate"])
        self.assertEqual("THHSTAW-EGA-REG-II-5-STAT-VIS-00000129", row["object_id"])
        self.assertEqual("61v-63r", row["object_locus"])
        self.assertEqual("observed", row["status"])
        self.assertIn("Direct visual inspection of both loci", row["evidence_basis"])
        self.assertIn("not yet a claim of verbatim copying", row["notes"])

    def test_migration_fixture_accounts_for_every_target_use_evidence_file_id(self) -> None:
        migration_rows = read_tsv(
            REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "project-source-migration.tsv"
        )
        fixture_evidence = [row for row in migration_rows if row["fixture_id"].startswith("EVID-")]
        actual_evidence = read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "use-evidence.tsv")
        self.assertEqual(4, len(fixture_evidence))
        self.assertEqual(4, len(actual_evidence))
        actual_files = [row["file_id"] for row in actual_evidence]
        self.assertEqual(4, len(set(actual_files)))
        for fixture in fixture_evidence:
            file_id = fixture["old_value"]
            matches = [row for row in actual_evidence if row["file_id"] == file_id]
            self.assertEqual(1, len(matches), file_id)
            self.assertIn(file_id, fixture["loss_test"])
            self.assertIn("use-evidence.tsv", fixture["target_location"])

    def test_c2_numeral_observation_is_mapped_exactly_once_without_upgrade(self) -> None:
        numeral = next(
            row
            for row in read_tsv(REPO / "projects" / "ega-reg-ii-5-knau" / "palaeography" / "numerals.tsv")
            if row["token_or_form"] == "C2 accounting-list notation"
        )
        self.assertEqual("observed", numeral["status"])
        self.assertIn("THHSTAW-EGA-REG-II-3-STAT-VIS-00000235:304r", numeral["locations"])
        self.assertIn("hand identity with Reg. Ii 5 is not established", numeral["note"])
        migration = [
            row
            for row in read_tsv(
                REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "project-source-migration.tsv"
            )
            if row["fixture_id"] == "NUM-C2"
        ]
        self.assertEqual(1, len(migration))
        self.assertIn("status=observed", migration[0]["old_value"])
        self.assertIn("exactly one surviving observation", migration[0]["loss_test"])
        self.assertIn("same-hand/direct-proof limitation unchanged", migration[0]["loss_test"])

    def test_principal_relevance_and_inspection_status_are_explicit_migration_fixtures(self) -> None:
        rows = read_tsv(
            REPO / "projects" / "ega-reg-ii-5-knau" / "research" / "project-source-migration.tsv"
        )
        by_id = {row["fixture_id"]: row for row in rows}
        self.assertEqual("remove-duplicate-only-during-later-migration", by_id["PRINCIPAL-001"]["transformation"])
        self.assertEqual(
            "correct-after-witness-provenance-clarification-2026-09-02",
            by_id["INSPECTION-STATUS-001"]["transformation"],
        )
        self.assertEqual("corrected-2026-09-02", by_id["INSPECTION-STATUS-001"]["status"])
        self.assertIn("partially-transcribed to images-inspected", by_id["INSPECTION-STATUS-001"]["loss_test"])
        relevance = [row for row in rows if row["fixture_id"].startswith("CORPUS-REL-")]
        self.assertEqual(7, len(relevance))
        self.assertTrue(all(row["transformation"] == "remove-after-loss-checked-migration" for row in relevance))


class TargetProjectUseContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self._write_base_fixture()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _write_project(self, project_id: str, root_id: str) -> None:
        project = self.root / "projects" / project_id
        project.mkdir(parents=True, exist_ok=True)
        (project / "project.yml").write_text(
            f'id: {project_id}\n'
            f'project_source_id: {root_id}\n'
            'research_object: "Fixture scholarly investigation"\n'
            'active_scope: "No active scope in fixture"\n'
            'source_register: "source-uses.tsv"\n'
            'canonical_status_file: STATUS.md\n',
            encoding="utf-8",
        )
        (project / "STATUS.md").write_text("# Fixture status\n", encoding="utf-8")
        use_headers = source_contract.load_contract(REPO)["tables"]["project_source_uses"]["required_columns"]
        write_tsv(project / "source-uses.tsv", use_headers, [])

    def _write_base_fixture(self) -> None:
        (self.root / "corpus").mkdir(parents=True)
        shutil.copy(REPO / "corpus" / "source-contract.json", self.root / "corpus" / "source-contract.json")
        source_headers = source_contract.load_contract(REPO)["tables"]["sources"]["required_columns"]
        source_rows = []
        for sid, source_type, signature, title in [
            ("ROOT-A", "archival_act", "A", "Root A"),
            ("ROOT-B", "archival_act", "B", "Root B"),
            ("SRC-INTERNAL", "protocol_record", "A", "Internal source"),
            ("SRC-OTHER-PROJECT", "protocol_record", "B", "Other project source"),
            ("SRC-NO-PROJECT", "protocol_record", "C", "Source without own project"),
        ]:
            row = {header: "" for header in source_headers}
            row.update(
                source_id=sid,
                source_type=source_type,
                archive="Archive",
                fonds="Fonds",
                signature=signature,
                title=title,
            )
            source_rows.append(row)
        write_tsv(self.root / "corpus" / "sources.tsv", source_headers, source_rows)

        relationship_headers = source_contract.load_contract(REPO)["tables"]["relationships"]["required_columns"]
        relationship_rows = [
            dict.fromkeys(relationship_headers, "") | {
                "relation_id": "REL-A",
                "subject_id": "SRC-INTERNAL",
                "predicate": "part_of",
                "object_id": "ROOT-A",
                "status": "observed",
                "evidence_basis": "fixture",
            },
            dict.fromkeys(relationship_headers, "") | {
                "relation_id": "REL-B",
                "subject_id": "SRC-OTHER-PROJECT",
                "predicate": "part_of",
                "object_id": "ROOT-B",
                "status": "observed",
                "evidence_basis": "fixture",
            },
        ]
        write_tsv(self.root / "corpus" / "relationships.tsv", relationship_headers, relationship_rows)

        file_headers = [
            "file_id",
            "source_id",
            "filename",
            "sha256",
            "role",
            "coverage",
            "storage_status",
            "repository_path",
            "rights_status",
        ]
        file_rows = [
            {
                "file_id": "FILE-A",
                "source_id": "SRC-INTERNAL",
                "filename": "a.pdf",
                "sha256": "a" * 64,
                "role": "archive export",
                "coverage": "fixture",
                "storage_status": "external-controlled",
                "repository_path": "",
                "rights_status": "fixture",
            },
            {
                "file_id": "FILE-B",
                "source_id": "SRC-OTHER-PROJECT",
                "filename": "b.pdf",
                "sha256": "b" * 64,
                "role": "archive export",
                "coverage": "fixture",
                "storage_status": "external-controlled",
                "repository_path": "",
                "rights_status": "fixture",
            },
        ]
        write_tsv(self.root / "corpus" / "files.tsv", file_headers, file_rows)

        self._write_project("project-a", "ROOT-A")
        self._write_project("project-b", "ROOT-B")

        use_headers = source_contract.load_contract(REPO)["tables"]["project_source_uses"]["required_columns"]
        use_rows = [
            {
                "use_id": "USE-1",
                "source_id": "SRC-INTERNAL",
                "research_function": "principal",
                "relevant_locus": "2r-3v",
                "status": "active",
                "evidence_basis": "fixture",
                "notes": "",
            },
            {
                "use_id": "USE-2",
                "source_id": "SRC-INTERNAL",
                "research_function": "notation-control",
                "relevant_locus": "2r",
                "status": "active",
                "evidence_basis": "fixture",
                "notes": "",
            },
            {
                "use_id": "USE-3",
                "source_id": "SRC-OTHER-PROJECT",
                "research_function": "textual-comparison",
                "relevant_locus": "10r-11v",
                "status": "identified",
                "evidence_basis": "fixture",
                "notes": "",
            },
            {
                "use_id": "USE-4",
                "source_id": "SRC-NO-PROJECT",
                "research_function": "codicological-control",
                "relevant_locus": "",
                "status": "identified",
                "evidence_basis": "fixture",
                "notes": "open vocabulary fixture",
            },
        ]
        write_tsv(self.root / "projects" / "project-a" / "source-uses.tsv", use_headers, use_rows)

        evidence_headers = source_contract.load_contract(REPO)["tables"]["project_use_evidence"]["required_columns"]
        evidence_rows = [
            {
                "evidence_id": "EVID-1",
                "use_id": "USE-1",
                "file_id": "FILE-A",
                "evidence_locator": "pdf page 1",
                "status": "observed",
                "evidence_basis": "fixture",
                "notes": "",
            },
            {
                "evidence_id": "EVID-2",
                "use_id": "USE-1",
                "file_id": "FILE-A",
                "evidence_locator": "pdf page 2",
                "status": "observed",
                "evidence_basis": "fixture",
                "notes": "",
            },
            {
                "evidence_id": "EVID-3",
                "use_id": "USE-2",
                "file_id": "FILE-A",
                "evidence_locator": "pdf page 1",
                "status": "observed",
                "evidence_basis": "fixture",
                "notes": "same file supports another use",
            },
            {
                "evidence_id": "EVID-4",
                "use_id": "USE-3",
                "file_id": "FILE-B",
                "evidence_locator": "pdf page 3",
                "status": "observed",
                "evidence_basis": "fixture",
                "notes": "",
            },
        ]
        write_tsv(
            self.root / "projects" / "project-a" / "research" / "use-evidence.tsv",
            evidence_headers,
            evidence_rows,
        )

    def validate(self) -> tuple[list[str], list[str], dict]:
        return source_contract.validate(self.root, source_contract.load_contract(self.root))

    def test_multiple_functions_open_vocabulary_and_external_sources_pass(self) -> None:
        errors, _, cache = self.validate()
        self.assertEqual([], errors)
        functions = [
            row["research_function"]
            for row in cache["uses_by_project_source"][("project-a", "SRC-INTERNAL")]
        ]
        self.assertEqual(["principal", "notation-control"], functions)
        self.assertIn("USE-4", cache["source_uses"])

    def test_same_file_can_support_multiple_uses_and_one_use_multiple_evidence(self) -> None:
        errors, _, cache = self.validate()
        self.assertEqual([], errors)
        self.assertEqual(2, len(cache["evidence_by_use"]["USE-1"]))
        self.assertEqual("FILE-A", cache["evidence_by_use"]["USE-2"][0]["file_id"])

    def test_resolver_derives_structure_functions_evidence_and_source_projects(self) -> None:
        args = SimpleNamespace(root=str(self.root), project="project-a", source_id="SRC-OTHER-PROJECT", locus=None)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = source_contract.cmd_resolve(args)
        self.assertEqual(0, rc)
        resolved = json.loads(out.getvalue())
        self.assertEqual("external", resolved["structural_status"])
        self.assertEqual(["textual-comparison"], resolved["research_functions"])
        self.assertEqual(["project-b"], resolved["source_projects"])
        self.assertEqual("FILE-B", resolved["project_source_uses"][0]["evidence"][0]["file"]["file_id"])
        self.assertNotIn("project-a", resolved["source_projects"])

    def test_duplicate_project_anchor_is_not_a_hard_failure(self) -> None:
        self._write_project("project-c", "ROOT-B")
        errors, _, _ = self.validate()
        self.assertEqual([], errors)

    def test_missing_research_object_fails(self) -> None:
        path = self.root / "projects" / "project-a" / "project.yml"
        text = path.read_text(encoding="utf-8").replace('research_object: "Fixture scholarly investigation"\n', "")
        path.write_text(text, encoding="utf-8")
        errors, _, _ = self.validate()
        self.assertTrue(any("required project key research_object is missing or empty" in error for error in errors))

    def test_missing_declared_status_file_fails(self) -> None:
        (self.root / "projects" / "project-a" / "STATUS.md").unlink()
        errors, _, _ = self.validate()
        self.assertTrue(any("canonical_status_file points to missing file" in error for error in errors))

    def test_missing_declared_source_register_fails(self) -> None:
        (self.root / "projects" / "project-a" / "source-uses.tsv").unlink()
        errors, _, _ = self.validate()
        self.assertTrue(any("source_register points to missing file" in error for error in errors))

    def test_legacy_source_register_fails_closed(self) -> None:
        legacy = self.root / "projects" / "project-a" / "sources" / "sources.tsv"
        write_tsv(legacy, ["source_id"], [])
        errors, _, _ = self.validate()
        self.assertTrue(any("legacy Project source register is no longer allowed" in error for error in errors))

    def test_principal_source_id_legacy_key_fails(self) -> None:
        path = self.root / "projects" / "project-a" / "project.yml"
        path.write_text(path.read_text(encoding="utf-8") + "principal_source_id: SRC-INTERNAL\n", encoding="utf-8")
        errors, _, _ = self.validate()
        self.assertTrue(any("legacy project key principal_source_id is no longer allowed" in error for error in errors))

    def test_invalid_use_source_fails(self) -> None:
        path = self.root / "projects" / "project-a" / "source-uses.tsv"
        rows = read_tsv(path)
        rows[0]["source_id"] = "NO-SUCH-SOURCE"
        write_tsv(path, list(rows[0]), rows)
        errors, _, _ = self.validate()
        self.assertTrue(any("source_id NO-SUCH-SOURCE does not exist" in error for error in errors))

    def test_duplicate_use_id_fails(self) -> None:
        path = self.root / "projects" / "project-a" / "source-uses.tsv"
        rows = read_tsv(path)
        duplicate = dict(rows[-1])
        duplicate["use_id"] = "USE-1"
        rows.append(duplicate)
        write_tsv(path, list(rows[0]), rows)
        errors, _, _ = self.validate()
        self.assertTrue(any("duplicate use_id USE-1" in error for error in errors))

    def test_invalid_evidence_use_fails(self) -> None:
        path = self.root / "projects" / "project-a" / "research" / "use-evidence.tsv"
        rows = read_tsv(path)
        rows[0]["use_id"] = "NO-SUCH-USE"
        write_tsv(path, list(rows[0]), rows)
        errors, _, _ = self.validate()
        self.assertTrue(any("use_id NO-SUCH-USE does not exist" in error for error in errors))

    def test_invalid_evidence_file_fails(self) -> None:
        path = self.root / "projects" / "project-a" / "research" / "use-evidence.tsv"
        rows = read_tsv(path)
        rows[0]["file_id"] = "NO-SUCH-FILE"
        write_tsv(path, list(rows[0]), rows)
        errors, _, _ = self.validate()
        self.assertTrue(any("file_id NO-SUCH-FILE does not exist" in error for error in errors))

    def test_evidence_file_must_belong_to_use_source(self) -> None:
        path = self.root / "projects" / "project-a" / "research" / "use-evidence.tsv"
        rows = read_tsv(path)
        rows[0]["file_id"] = "FILE-B"
        write_tsv(path, list(rows[0]), rows)
        errors, _, _ = self.validate()
        self.assertTrue(
            any(
                "file_id FILE-B belongs to source SRC-OTHER-PROJECT, not use source SRC-INTERNAL" in error
                for error in errors
            )
        )

    def test_use_evidence_rejects_redundant_source_id_column(self) -> None:
        path = self.root / "projects" / "project-a" / "research" / "use-evidence.tsv"
        rows = read_tsv(path)
        headers = list(rows[0]) + ["source_id"]
        for row in rows:
            row["source_id"] = "SRC-INTERNAL"
        write_tsv(path, headers, rows)
        errors, _, _ = self.validate()
        self.assertTrue(any("source_id must not be duplicated in use-evidence" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
