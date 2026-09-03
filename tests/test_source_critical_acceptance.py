from __future__ import annotations

import csv
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        return list(reader.fieldnames or []), [{k: (v or "").strip() for k, v in row.items()} for row in reader]


class SourceCriticalAcceptanceTests(unittest.TestCase):
    """Failure-derived guards for recurring Source/witness boundary mistakes.

    These tests validate explicit state and provenance discipline only. They do
    not decide the scholarly truth of a Source boundary, mapping or witness
    attribution.
    """

    def test_every_canonical_source_has_explicit_boundary_state_and_basis(self) -> None:
        headers, rows = read_tsv(REPO / "corpus" / "sources.tsv")
        self.assertIn("boundary_status", headers)
        self.assertIn("boundary_basis", headers)
        allowed = {"established", "partial", "unresolved", "not-applicable"}
        for row in rows:
            self.assertIn(row["boundary_status"], allowed, row["source_id"])
            self.assertTrue(row["boundary_basis"], row["source_id"])

    def test_every_crosswalk_mapping_has_explicit_evidence_basis(self) -> None:
        allowed = {"observed", "inferred-high", "unresolved", "working"}
        crosswalks = sorted(REPO.glob("corpus/source-data/*/crosswalk.tsv"))
        self.assertTrue(crosswalks)
        for path in crosswalks:
            headers, rows = read_tsv(path)
            self.assertIn("mapping_status", headers, str(path))
            self.assertIn("evidence", headers, str(path))
            for row in rows:
                self.assertIn(row["mapping_status"], allowed, f"{path}:{row.get('archival_folio')}")
                self.assertTrue(row["evidence"], f"{path}:{row.get('archival_folio')}")

    def test_legacy_witness_provenance_is_generic_and_validated_when_present(self) -> None:
        template = REPO / "templates" / "project" / "research" / "legacy-witness-provenance.tsv"
        self.assertTrue(template.is_file())
        required = {
            "record_id",
            "legacy_path",
            "legacy_locator",
            "current_classification",
            "witness_attribution",
            "allowed_use",
            "promotion_rule",
            "notes",
        }
        template_headers, _ = read_tsv(template)
        self.assertEqual(required, set(template_headers))

        registers = sorted(REPO.glob("projects/*/research/legacy-witness-provenance.tsv"))
        for path in registers:
            headers, rows = read_tsv(path)
            self.assertEqual(required, set(headers), str(path))
            seen: set[str] = set()
            project_dir = path.parents[1]
            for row in rows:
                record_id = row["record_id"]
                self.assertTrue(record_id, str(path))
                self.assertNotIn(record_id, seen, record_id)
                seen.add(record_id)
                for field in (
                    "legacy_path",
                    "current_classification",
                    "witness_attribution",
                    "allowed_use",
                    "promotion_rule",
                ):
                    self.assertTrue(row[field], f"{path}:{record_id}:{field}")
                matches = list(project_dir.glob(row["legacy_path"]))
                self.assertTrue(matches, f"{path}:{record_id}: legacy_path has no recoverable target")

    def test_source_acceptance_guards_do_not_turn_unresolved_state_into_project_authority(self) -> None:
        source_readme = (REPO / "templates" / "source" / "README.md").read_text(encoding="utf-8")
        self.assertIn("CORPUS_ONLY / NO_PROJECT_YET", source_readme)
        self.assertIn("unresolved Source extent blocks only claims that require that boundary/locus", source_readme)
        self.assertIn("Unresolved witness provenance blocks witness-specific scientific promotion", source_readme)


if __name__ == "__main__":
    unittest.main()
