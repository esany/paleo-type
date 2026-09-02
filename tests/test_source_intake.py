from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def write_tsv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=headers, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


class SourceIntakeRegressionTests(unittest.TestCase):
    def make_repo(self, tmp: str, known_bytes: bytes) -> Path:
        root = Path(tmp) / "repo"
        (root / "corpus").mkdir(parents=True)
        shutil.copy(REPO / "corpus" / "source-contract.json", root / "corpus" / "source-contract.json")
        contract = json.loads((root / "corpus" / "source-contract.json").read_text(encoding="utf-8"))

        source_headers = contract["tables"]["sources"]["required_columns"]
        source_rows = []
        for sid, stype, title in [
            ("ROOT-A", "archival_act", "Root A"),
            ("SRC-A", "protocol_record", "Source A"),
        ]:
            row = {header: "" for header in source_headers}
            row.update(source_id=sid, source_type=stype, archive="Archive", fonds="Fonds", signature="A", title=title)
            source_rows.append(row)
        write_tsv(root / "corpus" / "sources.tsv", source_headers, source_rows)

        relationship_headers = contract["tables"]["relationships"]["required_columns"]
        rel = {header: "" for header in relationship_headers}
        rel.update(
            relation_id="REL-A",
            subject_id="SRC-A",
            predicate="part_of",
            object_id="ROOT-A",
            status="observed",
            evidence_basis="fixture",
        )
        write_tsv(root / "corpus" / "relationships.tsv", relationship_headers, [rel])

        file_headers = contract["tables"]["files"]["required_columns"]
        if "repository_path" not in file_headers:
            file_headers = file_headers + ["repository_path"]
        file_row = {header: "" for header in file_headers}
        file_row.update(
            file_id="FILE-A",
            source_id="SRC-A",
            filename="known.pdf",
            sha256=hashlib.sha256(known_bytes).hexdigest(),
            role="archive export",
            coverage="fixture",
            storage_status="external-controlled",
            rights_status="fixture",
        )
        write_tsv(root / "corpus" / "files.tsv", file_headers, [file_row])

        project = root / "projects" / "project-a"
        project.mkdir(parents=True)
        (project / "project.yml").write_text(
            'id: project-a\nproject_source_id: ROOT-A\nsource_register: "source-uses.tsv"\ncanonical_status_file: STATUS.md\n',
            encoding="utf-8",
        )
        return root

    def run_intake(self, root: Path, input_file: Path) -> tuple[int, dict]:
        proc = subprocess.run(
            [sys.executable, str(REPO / "tools" / "source_intake.py"), str(input_file), "--root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )
        payload = json.loads(proc.stdout or proc.stderr)
        return proc.returncode, payload

    def test_current_canonical_file_rows_do_not_duplicate_exact_sha_identity(self) -> None:
        rows = read_tsv(REPO / "corpus" / "files.tsv")
        by_sha: dict[str, list[str]] = {}
        for row in rows:
            digest = row.get("sha256", "")
            if digest:
                by_sha.setdefault(digest, []).append(row["file_id"])
        duplicates = {digest: file_ids for digest, file_ids in by_sha.items() if len(file_ids) > 1}
        self.assertEqual({}, duplicates)

    def test_exact_sha_match_derives_file_source_and_structural_project_without_selecting_use(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            known = b"exact-fixture-bytes"
            root = self.make_repo(tmp, known)
            supplied = Path(tmp) / "supplied-any-name.pdf"
            supplied.write_bytes(known)

            rc, result = self.run_intake(root, supplied)

            self.assertEqual(0, rc)
            self.assertEqual("EXACT_FILE_MATCH", result["status"])
            self.assertEqual("FILE-A", result["exact_file_match"]["file_id"])
            self.assertEqual("SRC-A", result["source"]["source_id"])
            self.assertEqual(["project-a"], result["structurally_containing_projects"])
            self.assertTrue(result["project_routing"]["requires_explicit_decision"])
            self.assertIn("corpus-only", result["project_routing"]["allowed_outcomes"])
            self.assertIn("does not mean this File/Source is currently used", result["project_routing"]["note"])
            self.assertTrue(result["evidence_readiness"]["identifiable"])
            self.assertFalse(result["evidence_readiness"]["repository_available"])
            self.assertEqual("NOT_ESTABLISHED", result["evidence_readiness"]["research_ready_now"])
            self.assertIn("does not establish", result["evidence_readiness"]["basis"])

    def test_unmatched_file_stops_before_source_crosswalk_or_project_inference(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp, b"known")
            supplied = Path(tmp) / "looks-like-known.pdf"
            supplied.write_bytes(b"different bytes")

            rc, result = self.run_intake(root, supplied)

            self.assertEqual(0, rc)
            self.assertEqual("UNRESOLVED_FILE", result["status"])
            self.assertIsNone(result["exact_file_match"])
            self.assertIsNone(result["source"])
            self.assertEqual([], result["structurally_containing_projects"])
            self.assertFalse(result["crosswalk_available"])
            self.assertFalse(result["evidence_readiness"]["identifiable"])
            self.assertEqual("NOT_ESTABLISHED", result["evidence_readiness"]["research_ready_now"])
            self.assertTrue(result["project_routing"]["requires_explicit_decision"])
            self.assertIn("Do not infer Source identity", result["project_routing"]["note"])


if __name__ == "__main__":
    unittest.main()
