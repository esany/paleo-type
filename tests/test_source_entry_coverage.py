from __future__ import annotations

import csv
import importlib.util
import json
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


class SourceEntryCoverageTests(unittest.TestCase):
    def make_repo(self, tmp: str, with_project: bool = False) -> Path:
        root = Path(tmp) / "repo"
        (root / "corpus").mkdir(parents=True)
        shutil.copy(REPO / "corpus" / "source-contract.json", root / "corpus" / "source-contract.json")
        (root / "source-entry").mkdir()
        shutil.copy(REPO / "source-entry" / "contract.json", root / "source-entry" / "contract.json")

        owner = json.loads((root / "source-entry" / "contract.json").read_text(encoding="utf-8"))
        write_tsv(root / "source-entry" / "routes.tsv", owner["tables"]["routes"]["required_columns"], [])
        write_tsv(root / "source-entry" / "inspection-coverage.tsv", owner["tables"]["coverage"]["required_columns"], [])

        base = source_contract.load_contract(root)
        sh = base["tables"]["sources"]["required_columns"]
        sources = []
        for sid, typ in [("ROOT-A", "archival_act"), ("SRC-A", "protocol_record")]:
            row = {h: "" for h in sh}
            row.update(source_id=sid, source_type=typ, archive="Fixture", fonds="Fixture", signature=sid, title=sid)
            sources.append(row)
        write_tsv(root / "corpus" / "sources.tsv", sh, sources)

        rh = base["tables"]["relationships"]["required_columns"]
        rel = {h: "" for h in rh}
        rel.update(relation_id="REL-A", subject_id="SRC-A", predicate="part_of", object_id="ROOT-A",
                   status="observed", evidence_basis="fixture")
        write_tsv(root / "corpus" / "relationships.tsv", rh, [rel])

        fh = base["tables"]["files"]["required_columns"]
        file_row = {h: "" for h in fh}
        file_row.update(file_id="FILE-A", source_id="SRC-A", filename="a.pdf", sha256="a" * 64,
                        role="fixture", coverage="fixture", storage_status="external-controlled",
                        rights_status="fixture")
        write_tsv(root / "corpus" / "files.tsv", fh, [file_row])

        if with_project:
            p = root / "projects" / "project-a"
            p.mkdir(parents=True)
            (p / "project.yml").write_text(
                'id: project-a\n'
                'title: "Fixture"\n'
                'project_source_id: ROOT-A\n'
                'research_object: "Fixture investigation"\n'
                'active_scope: "No active scope"\n'
                'source_register: "source-uses.tsv"\n'
                'canonical_status_file: STATUS.md\n',
                encoding="utf-8",
            )
            (p / "STATUS.md").write_text("# Fixture\n", encoding="utf-8")
            write_tsv(p / "source-uses.tsv", base["tables"]["project_source_uses"]["required_columns"], [])
        return root

    def route(self, **kw: str) -> dict[str, str]:
        row = {
            "route_id": "ROUTE-1", "source_id": "SRC-A", "transition_sequence": "1",
            "route_state": "UNRESOLVED", "project_id": "", "authority_status": "UNRESOLVED",
            "authority_basis": "fixture", "recorded_at": "2026-10-08", "notes": "",
        }
        row.update(kw)
        return row

    def coverage(self, **kw: str) -> dict[str, str]:
        row = {
            "inspection_id": "INS-1", "source_id": "SRC-A", "route_id": "ROUTE-1",
            "file_id": "FILE-A", "project_id": "", "inspection_domain": "fixture domain",
            "locator_domain": "provider-image", "coverage_locus": "fixture locus",
            "purpose": "fixture", "depth": "orientation", "coverage_status": "PARTIAL",
            "relevance_status": "UNRESOLVED", "evidence_status": "P", "claim_layer": "OBSERVATION",
            "result": "fixture observation", "exclusions": "none", "unresolved_or_partial": "open",
            "unavailable_or_unreadable": "none", "continuation_boundary": "fixture boundary",
            "claim_ceiling": "fixture only", "evidence_basis": "synthetic fixture",
            "recorded_at": "2026-10-08", "responsibility": "fixture", "notes": "",
        }
        row.update(kw)
        return row

    def write_owner(self, root: Path, routes: list[dict[str, str]], rows: list[dict[str, str]],
                    extra_coverage_header: str | None = None) -> None:
        owner = json.loads((root / "source-entry" / "contract.json").read_text(encoding="utf-8"))
        write_tsv(root / "source-entry" / "routes.tsv", owner["tables"]["routes"]["required_columns"], routes)
        headers = owner["tables"]["coverage"]["required_columns"][:]
        if extra_coverage_header:
            headers.append(extra_coverage_header)
        write_tsv(root / "source-entry" / "inspection-coverage.tsv", headers, rows)

    def validate(self, root: Path):
        return source_contract.validate(root, source_contract.load_contract(root))

    def test_empty_owner_is_valid_and_fabricates_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp)
            errors, _, cache = self.validate(root)
            self.assertEqual([], errors)
            self.assertEqual([], cache["source_entry_routes"])
            self.assertEqual([], cache["source_entry_coverage"])

    def test_coverage_without_route_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp)
            self.write_owner(root, [], [self.coverage()])
            errors, _, _ = self.validate(root)
            self.assertTrue(any("route_id ROUTE-1 does not exist" in e for e in errors))

    def test_unresolved_or_candidate_route_does_not_authorize_coverage(self) -> None:
        for state in ("UNRESOLVED", "CANDIDATE_NEW_PROJECT"):
            with self.subTest(state=state), tempfile.TemporaryDirectory() as tmp:
                root = self.make_repo(tmp)
                self.write_owner(root, [self.route(route_state=state)], [self.coverage()])
                errors, _, _ = self.validate(root)
                self.assertTrue(any("durable coverage requires a resolved" in e for e in errors))

    def test_corpus_only_route_accepts_preproject_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp)
            route = self.route(route_state="CORPUS_ONLY / NO_PROJECT_YET",
                               authority_status="HUMAN-OWNER-CONFIRMED")
            self.write_owner(root, [route], [self.coverage(project_id="")])
            errors, _, cache = self.validate(root)
            self.assertEqual([], errors)
            self.assertEqual({}, cache["projects"])

    def test_append_only_transition_preserves_preproject_row(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp, with_project=True)
            r1 = self.route(route_id="ROUTE-1", route_state="CORPUS_ONLY / NO_PROJECT_YET",
                            authority_status="HUMAN-OWNER-CONFIRMED")
            r2 = self.route(route_id="ROUTE-2", transition_sequence="2", route_state="EXISTING_PROJECT",
                            project_id="project-a", authority_status="HUMAN-OWNER-CONFIRMED")
            before = self.coverage(inspection_id="INS-BEFORE", route_id="ROUTE-1", project_id="")
            after = self.coverage(inspection_id="INS-AFTER", route_id="ROUTE-2", project_id="project-a")
            self.write_owner(root, [r1, r2], [before, after])
            errors, _, cache = self.validate(root)
            self.assertEqual([], errors)
            self.assertEqual("ROUTE-2", cache["source_entry_current_routes"]["SRC-A"]["route_id"])
            self.assertEqual({"ROUTE-1", "ROUTE-2"}, {r["route_id"] for r in cache["source_entry_coverage"]})

    def test_project_binding_must_match_existing_project_route(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp, with_project=True)
            r1 = self.route(route_state="CORPUS_ONLY / NO_PROJECT_YET",
                            authority_status="HUMAN-OWNER-CONFIRMED")
            self.write_owner(root, [r1], [self.coverage(project_id="project-a")])
            errors, _, _ = self.validate(root)
            self.assertTrue(any("Project-bound coverage requires its route_id" in e for e in errors))

    def test_route_sequences_are_contiguous(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp, with_project=True)
            r1 = self.route(route_state="CORPUS_ONLY / NO_PROJECT_YET",
                            authority_status="HUMAN-OWNER-CONFIRMED")
            r3 = self.route(route_id="ROUTE-3", transition_sequence="3", route_state="EXISTING_PROJECT",
                            project_id="project-a", authority_status="HUMAN-OWNER-CONFIRMED")
            self.write_owner(root, [r1, r3], [])
            errors, _, _ = self.validate(root)
            self.assertTrue(any("transition_sequence must be contiguous" in e for e in errors))

    def test_epistemic_and_scope_collapses_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp)
            route = self.route(route_state="CORPUS_ONLY / NO_PROJECT_YET",
                               authority_status="HUMAN-OWNER-CONFIRMED")
            self.write_owner(root, [route], [self.coverage(evidence_status="H", claim_layer="OBSERVATION")])
            errors, _, _ = self.validate(root)
            self.assertTrue(any("H evidence cannot be claim_layer OBSERVATION" in e for e in errors))

            bad = self.coverage()
            bad["active_scope"] = "must fail"
            self.write_owner(root, [route], [bad], extra_coverage_header="active_scope")
            errors, _, _ = self.validate(root)
            self.assertTrue(any("must not contain Project/scholarly state column active_scope" in e for e in errors))

    def test_not_inspected_primary_evidence_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp)
            route = self.route(route_state="CORPUS_ONLY / NO_PROJECT_YET",
                               authority_status="HUMAN-OWNER-CONFIRMED")
            self.write_owner(
                root,
                [route],
                [self.coverage(coverage_status="NOT_INSPECTED", evidence_status="P")],
            )
            errors, _, _ = self.validate(root)
            self.assertTrue(any("NOT_INSPECTED cannot claim P" in e for e in errors))

    def test_all_forbidden_project_state_headers_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp)
            route = self.route(route_state="CORPUS_ONLY / NO_PROJECT_YET",
                               authority_status="HUMAN-OWNER-CONFIRMED")
            for header in ("active_scope", "gate", "next_action", "scholarly_scope"):
                with self.subTest(header=header):
                    bad = self.coverage()
                    bad[header] = "must fail"
                    self.write_owner(root, [route], [bad], extra_coverage_header=header)
                    errors, _, _ = self.validate(root)
                    self.assertTrue(
                        any(f"must not contain Project/scholarly state column {header}" in e for e in errors)
                    )

    def test_locator_domains_remain_structurally_distinct(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp)
            route = self.route(route_state="CORPUS_ONLY / NO_PROJECT_YET",
                               authority_status="HUMAN-OWNER-CONFIRMED")
            rows = [
                self.coverage(
                    inspection_id="INS-IMG",
                    locator_domain="provider-image",
                    coverage_locus="0001.jpg",
                ),
                self.coverage(
                    inspection_id="INS-PDF",
                    locator_domain="pdf-page",
                    coverage_locus="PDF p. 1",
                ),
                self.coverage(
                    inspection_id="INS-FOL",
                    locator_domain="archival-folio",
                    coverage_locus="fol. 1r",
                ),
            ]
            self.write_owner(root, [route], rows)
            errors, _, cache = self.validate(root)
            self.assertEqual([], errors)
            self.assertEqual(
                {"provider-image", "pdf-page", "archival-folio"},
                {row["locator_domain"] for row in cache["source_entry_coverage"]},
            )
            self.assertEqual(
                {"0001.jpg", "PDF p. 1", "fol. 1r"},
                {row["coverage_locus"] for row in cache["source_entry_coverage"]},
            )

    def test_simple_source_does_not_require_source_entry_state_until_used(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = self.make_repo(tmp)
            errors, _, cache = self.validate(root)
            self.assertEqual([], errors)
            self.assertEqual([], cache["source_entry_routes"])
            self.assertEqual([], cache["source_entry_coverage"])

    def test_regii_loss_check_maps_legacy_meanings_without_migration(self) -> None:
        path = REPO / "projects" / "ega-reg-ii-5-knau" / "sources" / "inspection-log.tsv"
        with path.open("r", encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
        self.assertTrue(rows)

        mapped_count = 0
        for row in rows:
            if not row["corpus_source_id"]:
                # The legacy row without a canonical Source ID is intentionally not migration-ready.
                continue
            mapped = self.coverage(
                inspection_id=f"LOSS-{row['inspection_id']}",
                source_id=row["corpus_source_id"],
                coverage_locus=row["unit_inspected"],
                evidence_status=row["status"],
                result=row["what_it_supports"],
                evidence_basis=row["access_basis"],
                claim_ceiling=row["limitations"],
                unresolved_or_partial=row["limitations"],
            )
            self.assertEqual(row["corpus_source_id"], mapped["source_id"])
            self.assertEqual(row["unit_inspected"], mapped["coverage_locus"])
            self.assertEqual(row["status"], mapped["evidence_status"])
            self.assertEqual(row["access_basis"], mapped["evidence_basis"])
            self.assertEqual(row["what_it_supports"], mapped["result"])
            self.assertEqual(row["limitations"], mapped["claim_ceiling"])
            mapped_count += 1

        self.assertGreater(mapped_count, 0)
        # Loss checking does not migrate/copy legacy rows into the canonical owner.
        self.assertEqual(1, len((REPO / "source-entry" / "inspection-coverage.tsv").read_text().splitlines()))


if __name__ == "__main__":
    unittest.main()
