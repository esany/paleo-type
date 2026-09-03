from __future__ import annotations

import csv
import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

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


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


class SourceContractAssuranceRegressionTests(unittest.TestCase):
    """Negative fixtures for stable validator rules that protect research-system ownership/provenance."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self._write_valid_fixture()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _contract(self) -> dict:
        return source_contract.load_contract(self.root)

    def _write_valid_fixture(self) -> None:
        (self.root / "corpus").mkdir(parents=True)
        shutil.copy(REPO / "corpus" / "source-contract.json", self.root / "corpus" / "source-contract.json")
        contract = source_contract.load_contract(REPO)

        source_headers = contract["tables"]["sources"]["required_columns"]
        source_rows = []
        for sid, source_type, signature, title in [
            ("ROOT-A", "archival_act", "A", "Root A"),
            ("SRC-A", "protocol_record", "A", "Source A"),
            ("ROOT-B", "archival_act", "B", "Root B"),
            ("SRC-B", "protocol_record", "B", "Source B"),
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

        relationship_headers = contract["tables"]["relationships"]["required_columns"]
        relationship_rows = [
            dict.fromkeys(relationship_headers, "")
            | {
                "relation_id": "REL-A",
                "subject_id": "SRC-A",
                "predicate": "part_of",
                "object_id": "ROOT-A",
                "status": "observed",
                "evidence_basis": "fixture",
            },
            dict.fromkeys(relationship_headers, "")
            | {
                "relation_id": "REL-B",
                "subject_id": "SRC-B",
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
                "source_id": "SRC-A",
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
                "source_id": "SRC-B",
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

        use_headers = contract["tables"]["project_source_uses"]["required_columns"]
        for project_id, root_id in [("project-a", "ROOT-A"), ("project-b", "ROOT-B")]:
            project = self.root / "projects" / project_id
            project.mkdir(parents=True)
            (project / "project.yml").write_text(
                f'id: {project_id}\n'
                f'project_source_id: {root_id}\n'
                'research_object: "Fixture scholarly investigation"\n'
                'active_scope: "Fixture active scope"\n'
                'source_register: "source-uses.tsv"\n'
                'canonical_status_file: STATUS.md\n',
                encoding="utf-8",
            )
            (project / "STATUS.md").write_text("# Fixture status\n", encoding="utf-8")

        write_tsv(
            self.root / "projects" / "project-a" / "source-uses.tsv",
            use_headers,
            [
                {
                    "use_id": "USE-A",
                    "source_id": "SRC-A",
                    "research_function": "principal",
                    "relevant_locus": "1r",
                    "status": "active",
                    "evidence_basis": "fixture",
                    "notes": "",
                }
            ],
        )
        write_tsv(
            self.root / "projects" / "project-b" / "source-uses.tsv",
            use_headers,
            [
                {
                    "use_id": "USE-B",
                    "source_id": "SRC-B",
                    "research_function": "textual-comparison",
                    "relevant_locus": "2r",
                    "status": "active",
                    "evidence_basis": "fixture",
                    "notes": "",
                }
            ],
        )

    def validate(self) -> tuple[list[str], list[str], dict]:
        return source_contract.validate(self.root, self._contract())

    def test_part_of_cycle_is_rejected(self) -> None:
        path = self.root / "corpus" / "relationships.tsv"
        headers, rows = read_tsv(path)
        rows.append(
            dict.fromkeys(headers, "")
            | {
                "relation_id": "REL-CYCLE",
                "subject_id": "ROOT-A",
                "predicate": "part_of",
                "object_id": "SRC-A",
                "status": "observed",
                "evidence_basis": "fixture",
            }
        )
        write_tsv(path, headers, rows)

        errors, _, _ = self.validate()
        self.assertTrue(any("part_of cycle detected" in error for error in errors))

    def test_use_evidence_cannot_reference_use_from_another_project(self) -> None:
        evidence_headers = self._contract()["tables"]["project_use_evidence"]["required_columns"]
        write_tsv(
            self.root / "projects" / "project-a" / "research" / "use-evidence.tsv",
            evidence_headers,
            [
                {
                    "evidence_id": "EVID-CROSS-PROJECT",
                    "use_id": "USE-B",
                    "file_id": "FILE-B",
                    "evidence_locator": "pdf page 1",
                    "status": "observed",
                    "evidence_basis": "fixture",
                    "notes": "",
                }
            ],
        )

        errors, _, _ = self.validate()
        self.assertTrue(any("use_id USE-B belongs to another project" in error for error in errors))

    def test_repo_preserved_claim_requires_existing_matching_bytes(self) -> None:
        path = self.root / "corpus" / "files.tsv"
        headers, rows = read_tsv(path)
        rows[0]["storage_status"] = "repo-preserved"
        rows[0]["repository_path"] = "corpus/source-files/SRC-A/original/a.pdf"
        write_tsv(path, headers, rows)

        errors, _, _ = self.validate()
        self.assertTrue(any("repo-preserved file missing" in error for error in errors))

        binary = self.root / rows[0]["repository_path"]
        binary.parent.mkdir(parents=True, exist_ok=True)
        binary.write_bytes(b"not-the-recorded-bytes")
        errors, _, _ = self.validate()
        self.assertTrue(any("sha256 mismatch" in error for error in errors))

    def test_research_function_is_open_vocabulary_but_syntax_checked(self) -> None:
        path = self.root / "projects" / "project-a" / "source-uses.tsv"
        headers, rows = read_tsv(path)
        rows[0]["research_function"] = "custom-research-function"
        write_tsv(path, headers, rows)
        errors, _, _ = self.validate()
        self.assertEqual([], errors)

        rows[0]["research_function"] = "Custom Research Function"
        write_tsv(path, headers, rows)
        errors, _, _ = self.validate()
        self.assertTrue(any("must be lowercase kebab-case; vocabulary remains open" in error for error in errors))

    def test_crosswalk_row_source_must_match_source_data_owner(self) -> None:
        path = self.root / "corpus" / "source-data" / "SRC-A" / "crosswalk.tsv"
        write_tsv(
            path,
            ["source_id", "archival_folio", "export_image", "pdf_page", "stable_image_urn", "mapping_status"],
            [
                {
                    "source_id": "SRC-B",
                    "archival_folio": "1r",
                    "export_image": "10",
                    "pdf_page": "1",
                    "stable_image_urn": "",
                    "mapping_status": "observed",
                }
            ],
        )

        errors, _, _ = self.validate()
        self.assertTrue(any("row source_id 'SRC-B' must match directory SRC-A" in error for error in errors))

    def test_crosswalk_requires_at_least_one_digital_locator(self) -> None:
        path = self.root / "corpus" / "source-data" / "SRC-A" / "crosswalk.tsv"
        write_tsv(
            path,
            ["source_id", "archival_folio", "export_image", "pdf_page", "stable_image_urn", "mapping_status"],
            [
                {
                    "source_id": "SRC-A",
                    "archival_folio": "1r",
                    "export_image": "",
                    "pdf_page": "",
                    "stable_image_urn": "",
                    "mapping_status": "observed",
                }
            ],
        )

        errors, _, _ = self.validate()
        self.assertTrue(any("at least one digital locator is required" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
