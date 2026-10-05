from __future__ import annotations

import csv
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools import engineering, engineering_context


REPO = Path(__file__).resolve().parents[1]


class EngineeringContextTests(unittest.TestCase):
    def test_human_overview_resolves_semantic_ready_next_wp6_work(self) -> None:
        errors, packet = engineering_context.compile_context(REPO, "human-system-overview")
        self.assertEqual([], errors)
        work = packet["current_work"]
        self.assertEqual("ready-next", work["state"])
        self.assertIn("WP6 adversarial qualification", work["statement"])
        self.assertEqual("github-issue:esany/paleo-type#261", work["work_ref"])
        rendered = engineering_context.render_human_cursor(packet)
        self.assertIn("Next eligible work:", rendered)
        self.assertIn("#261", rendered)

    def test_execution_profile_exposes_shared_check_and_ready_next_authority(self) -> None:
        errors, packet = engineering_context.compile_context(REPO, "system-development-execution")
        self.assertEqual([], errors)
        execution = packet["execution_contract"]
        self.assertEqual("ready-next", execution["requested_activity"])
        self.assertEqual("python tools/check.py", execution["technical_verification"])
        self.assertIn("path:GOVERNING_OBJECTIVE.md", execution["authority_reads"])
        self.assertIn("path:AGENTS.md", execution["authority_reads"])
        self.assertIn("github-issue:esany/paleo-type#261", execution["authority_reads"])
        self.assertEqual("github-issue:esany/paleo-type#244", execution["whole_system_return"])

    def test_context_starvation_is_detected(self) -> None:
        errors, packet = engineering_context.compile_context(REPO, "system-development-execution")
        self.assertEqual([], errors)
        packet.pop("authority")
        starvation = engineering_context.context_adequacy_errors(packet)
        self.assertTrue(any("context starvation" in item for item in starvation), starvation)

    def test_review_profile_does_not_fake_independence(self) -> None:
        errors, packet = engineering_context.compile_context(REPO, "architecture-review")
        self.assertEqual([], errors)
        basis = packet["review_evidence_basis"]
        self.assertEqual("unknown/not-established", basis["basis_class"])
        self.assertEqual("not-established", basis["independence_claim"])
        self.assertTrue(basis["inherited_premises"])
        self.assertIn("fresh context or second model", basis["remaining_evidence_depth_limit"].lower())

    def test_unrelated_history_growth_does_not_expand_default_packet(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            errors, before = engineering_context.compile_context(fixture, "system-development-execution")
            self.assertEqual([], errors)
            artifact_path = fixture / "engineering" / "catalog" / "artifacts.tsv"
            rows = self._read_rows(artifact_path)
            rows.append({
                "artifact_id": "ENG-A-9998",
                "kind": "audit",
                "path": "engineering/changes/SD-KA-01/DESIGN.md",
                "owner_scope": "SD-KA-01",
                "authority_role": "non-normative-evidence",
                "lifecycle_state": "historical",
                "change_id": "SD-KA-01",
                "title": "Unrelated historical context growth fixture",
            })
            self._write_rows(artifact_path, rows)
            errors, after = engineering_context.compile_context(fixture, "system-development-execution")
            self.assertEqual([], errors)
            self.assertEqual(before["applicability"], after["applicability"])
            self.assertNotIn("ENG-A-9998", json.dumps(after, sort_keys=True))

    def test_ambiguous_next_work_is_exposed_not_silently_selected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._copy_contract_fixture(Path(directory))
            config_path = fixture / "engineering" / "configuration.json"
            config = json.loads(config_path.read_text(encoding="utf-8"))
            config["current_focus"] = None
            config["applicability"] = []
            config_path.write_text(json.dumps(config), encoding="utf-8")

            artifact_path = fixture / "engineering" / "catalog" / "artifacts.tsv"
            artifacts = self._read_rows(artifact_path)
            artifacts.append({
                "artifact_id": "ENG-A-9999",
                "kind": "work-metadata",
                "path": "github://github.com/esany/paleo-type/issues/999",
                "owner_scope": "SD-KA-01",
                "authority_role": "work-metadata",
                "lifecycle_state": "active",
                "change_id": "SD-KA-01",
                "title": "Competing ready-next fixture",
            })
            self._write_rows(artifact_path, artifacts)
            relation_path = fixture / "engineering" / "catalog" / "relations.tsv"
            relations = self._read_rows(relation_path)
            relations.append({
                "relation_id": "REL-9999",
                "subject_ref": "artifact:ENG-A-0032",
                "predicate": "transitions-to",
                "object_ref": "github-issue:esany/paleo-type#999",
                "relation_status": "accepted",
                "evidence_ref": "artifact:ENG-A-0032",
            })
            self._write_rows(relation_path, relations)
            errors, packet = engineering_context.compile_context(fixture, "human-system-overview")
            self.assertEqual([], errors)
            work = packet["current_work"]
            self.assertEqual("ambiguous", work["state"])
            self.assertEqual(2, len(work["candidates"]))
            self.assertIn("no repository-global work item was silently selected", work["statement"])

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
    def _write_rows(path: Path, rows: list[dict[str, str]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    unittest.main()
