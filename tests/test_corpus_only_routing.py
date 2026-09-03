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


class CorpusOnlyRoutingRegressionTests(unittest.TestCase):
    def test_source_file_and_part_of_structure_validate_without_any_project(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "corpus").mkdir(parents=True)
            shutil.copy(REPO / "corpus" / "source-contract.json", root / "corpus" / "source-contract.json")
            contract = source_contract.load_contract(root)

            source_headers = contract["tables"]["sources"]["required_columns"]
            source_rows = []
            for sid, source_type, title in [
                ("ROOT-CORPUS-ONLY", "archival_act", "Corpus-only root"),
                ("SRC-CORPUS-ONLY", "protocol_record", "Corpus-only protocol"),
            ]:
                row = {header: "" for header in source_headers}
                row.update(
                    source_id=sid,
                    source_type=source_type,
                    archive="Archive",
                    fonds="Fonds",
                    signature="Signature",
                    title=title,
                )
                source_rows.append(row)
            write_tsv(root / "corpus" / "sources.tsv", source_headers, source_rows)

            relationship_headers = contract["tables"]["relationships"]["required_columns"]
            relationship = {header: "" for header in relationship_headers}
            relationship.update(
                relation_id="REL-CORPUS-ONLY",
                subject_id="SRC-CORPUS-ONLY",
                predicate="part_of",
                object_id="ROOT-CORPUS-ONLY",
                status="observed",
                evidence_basis="fixture",
            )
            write_tsv(root / "corpus" / "relationships.tsv", relationship_headers, [relationship])

            file_headers = contract["tables"]["files"]["required_columns"]
            # repository_path is optional in the contract but retained here because it is a normal files.tsv column.
            if "repository_path" not in file_headers:
                file_headers = file_headers + ["repository_path"]
            file_row = {header: "" for header in file_headers}
            file_row.update(
                file_id="FILE-CORPUS-ONLY",
                source_id="SRC-CORPUS-ONLY",
                filename="corpus-only.pdf",
                sha256="a" * 64,
                role="archive export",
                coverage="fixture",
                storage_status="external-controlled",
                rights_status="fixture",
            )
            write_tsv(root / "corpus" / "files.tsv", file_headers, [file_row])

            errors, warnings, cache = source_contract.validate(root, contract)

            self.assertEqual([], errors)
            self.assertEqual([], warnings)
            self.assertEqual({}, cache["projects"])
            self.assertIn("SRC-CORPUS-ONLY", cache["sources"])
            self.assertIn("FILE-CORPUS-ONLY", cache["files"])

    def test_part_of_root_does_not_imply_project_materialization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "corpus").mkdir(parents=True)
            shutil.copy(REPO / "corpus" / "source-contract.json", root / "corpus" / "source-contract.json")
            contract = source_contract.load_contract(root)

            source_headers = contract["tables"]["sources"]["required_columns"]
            root_source = {header: "" for header in source_headers}
            root_source.update(
                source_id="ROOT-A",
                source_type="archival_act",
                archive="Archive",
                fonds="Fonds",
                signature="A",
                title="Root A",
            )
            child_source = {header: "" for header in source_headers}
            child_source.update(
                source_id="SRC-A",
                source_type="protocol_record",
                archive="Archive",
                fonds="Fonds",
                signature="A",
                title="Source A",
            )
            write_tsv(root / "corpus" / "sources.tsv", source_headers, [root_source, child_source])

            relationship_headers = contract["tables"]["relationships"]["required_columns"]
            relation = {header: "" for header in relationship_headers}
            relation.update(
                relation_id="REL-A",
                subject_id="SRC-A",
                predicate="part_of",
                object_id="ROOT-A",
                status="observed",
                evidence_basis="fixture",
            )
            write_tsv(root / "corpus" / "relationships.tsv", relationship_headers, [relation])

            file_headers = contract["tables"]["files"]["required_columns"]
            write_tsv(root / "corpus" / "files.tsv", file_headers, [])

            errors, _, cache = source_contract.validate(root, contract)

            self.assertEqual([], errors)
            self.assertEqual({}, cache["projects"])
            self.assertEqual(["ROOT-A"], cache["parents_by_source"]["SRC-A"])


if __name__ == "__main__":
    unittest.main()
