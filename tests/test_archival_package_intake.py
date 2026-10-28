"""Fail-closed tests for the read-only archival package to Corpus bridge."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import archival_package_intake as intake


GUID = "8bdce320-0ce6-4ddb-b37a-eed8fe52cb94"
URL = f"https://www.archiv.sachsen.de/archiv/bestand.jsp?guid={GUID}"
BYTES = b"stand-in bytes for an independently tested provider original"
DIGEST = hashlib.sha256(BYTES).hexdigest()


class ArchivalPackageIntakeTests(unittest.TestCase):
    def make_package(self, tmp):
        base = Path(tmp)
        repo = base / "repo"
        repo.mkdir()
        package = base / "external" / "1303_SStA_10001_Nr_01739_fixture"
        package.mkdir(parents=True)
        (package / "0001.jpg").write_bytes(BYTES)
        source = {
            "archive": "Sächsisches Staatsarchiv",
            "fonds": "10001",
            "signature": "Nr. 01739",
            "title": "Urkunde",
            "date_label": "29. Oktober 1303",
            "guid": GUID,
            "page_url": URL,
        }
        image = {"filename": "0001.jpg", "sha256": DIGEST, "status": "downloaded"}
        manifest = {
            "status": "complete", "source": source, "images": [image],
            "package_name": package.name, "route": "fullsize",
            "progress_state": "ACQUISITION_STATE.json",
            "file_list_url": "https://www.archiv.sachsen.de/digitalisate/" + GUID + "/files.json",
            "file_list_sha256": "f" * 64,
        }
        progress = {
            "status": "complete",
            "plan": {
                "package_name": package.name,
                "route": "fullsize",
                "guid": GUID,
                "file_list_url": manifest["file_list_url"],
                "file_list_sha256": manifest["file_list_sha256"],
                "expected_filenames": ["0001.jpg"],
            },
            "images": [{**image, "status": "verified"}],
        }
        (package / "QUELLENINFO.json").write_text(json.dumps(manifest), encoding="utf-8")
        (package / "QUELLENINFO.txt").write_text("Archive source metadata\n", encoding="utf-8")
        (package / "ACQUISITION_STATE.json").write_text(json.dumps(progress), encoding="utf-8")
        (package / "SHA256SUMS.txt").write_text(DIGEST + "  0001.jpg\n", encoding="utf-8")
        row = {
            "source_id": "SSTA-ARCHIVIALE-8BDCE320",
            "record_id": GUID, "digital_url": URL,
            "archive": "Sächsisches Staatsarchiv – Hauptstaatsarchiv Dresden",
            "fonds": "10001 Ältere Urkunden",
            "signature": "Sächsisches Staatsarchiv, 10001 Ältere Urkunden, Nr. 01739",
        }
        cache = {"sources": {row["source_id"]: row}, "files": {}}
        return repo, package, cache, manifest, progress

    def inspect(self, package, repo, cache):
        with patch.object(intake.source_contract, "load_contract", return_value={}):
            with patch.object(intake.source_contract, "validate", return_value=([], [], cache)):
                return intake.inspect_package(package, repo)

    def test_real_bytes_and_manifest_yield_read_only_missing_file_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, _ = self.make_package(tmp)
            before = {p.name: p.read_bytes() for p in package.iterdir()}
            result = self.inspect(package, repo, cache)
            self.assertEqual("VERIFIED_BYTES_RECONCILIATION_PLAN", result["status"])
            self.assertEqual("SSTA-ARCHIVIALE-8BDCE320", result["source_id"])
            self.assertEqual([{"filename": "0001.jpg", "sha256": DIGEST}], result["unregistered"])
            self.assertTrue(result["read_only"])
            self.assertFalse(result["repo_write_completed"])
            self.assertFalse(result["project_created"])
            self.assertEqual("NOT_ESTABLISHED_BY_THIS_TOOL", result["external_durability"])
            self.assertEqual(before, {p.name: p.read_bytes() for p in package.iterdir()})

    def test_exact_file_identity_is_reused_without_duplicate(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, _ = self.make_package(tmp)
            cache["files"] = {"FILE-A": {
                "file_id": "FILE-A", "source_id": "SSTA-ARCHIVIALE-8BDCE320",
                "filename": "0001.jpg", "sha256": DIGEST,
            }}
            result = self.inspect(package, repo, cache)
            self.assertEqual([], result["unregistered"])
            self.assertEqual("FILE-A", result["already_registered"][0]["file_id"])

    def test_unrelated_source_sha_reuse_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, _ = self.make_package(tmp)
            cache["files"] = {"FILE-OTHER": {
                "file_id": "FILE-OTHER", "source_id": "OTHER",
                "filename": "0001.jpg", "sha256": DIGEST,
            }}
            with self.assertRaisesRegex(intake.PackageIntakeError, "different Source/File"):
                self.inspect(package, repo, cache)

    def test_mutated_original_rejected_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, _ = self.make_package(tmp)
            (package / "0001.jpg").write_bytes(b"corrupted")
            with self.assertRaisesRegex(intake.PackageIntakeError, "mutated original"):
                self.inspect(package, repo, cache)

    def test_partial_status_does_not_infer_success_or_trigger_resume(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, manifest, progress = self.make_package(tmp)
            progress["status"] = "partial-restartable"
            state = package / "ACQUISITION_STATE.json"
            state.write_text(json.dumps(progress), encoding="utf-8")
            before = state.read_bytes()
            with self.assertRaisesRegex(intake.PackageIntakeError, "not both complete"):
                self.inspect(package, repo, cache)
            self.assertEqual(before, state.read_bytes())

    def test_disagreement_with_provider_list_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, progress = self.make_package(tmp)
            progress["plan"]["expected_filenames"] = ["0001.jpg", "0002.jpg"]
            (package / "ACQUISITION_STATE.json").write_text(json.dumps(progress), encoding="utf-8")
            with self.assertRaisesRegex(intake.PackageIntakeError, "differ"):
                self.inspect(package, repo, cache)

    def test_catalogue_guid_conflict_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, _ = self.make_package(tmp)
            cache["sources"]["OTHER"] = {
                "source_id": "OTHER", "record_id": "unrelated",
                "digital_url": URL, "archive": "Different archive",
            }
            with self.assertRaisesRegex(intake.PackageIntakeError, "conflicting Source"):
                self.inspect(package, repo, cache)

    def test_absent_canonical_source_never_fabricates_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, _ = self.make_package(tmp)
            cache["sources"] = {}
            result = self.inspect(package, repo, cache)
            self.assertIsNone(result["source_id"])
            self.assertEqual("REQUIRES_EVIDENCED_SOURCE_RESOLUTION", result["source_resolution"])

    def test_actual_downloaded_progress_status_is_verified_from_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, progress = self.make_package(tmp)
            progress["images"][0]["status"] = "downloaded"
            (package / "ACQUISITION_STATE.json").write_text(json.dumps(progress), encoding="utf-8")
            result = self.inspect(package, repo, cache)
            self.assertEqual(1, result["originals_verified"])
            self.assertEqual("EXACT", result["package_naming"]["status"])

    def test_adopted_existing_progress_status_is_verified_from_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, progress = self.make_package(tmp)
            progress["images"][0]["status"] = "already-present-adopted"
            (package / "ACQUISITION_STATE.json").write_text(json.dumps(progress), encoding="utf-8")
            self.assertEqual(1, self.inspect(package, repo, cache)["originals_verified"])

    def test_legacy_package_separator_alias_is_warned_not_resumed(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, manifest, progress = self.make_package(tmp)
            # Real old packages can have a hyphenated physical/manifest name
            # and the original underscored plan without different source bytes.
            renamed = package.with_name(package.name.replace("_", "-"))
            package.rename(renamed)
            manifest["package_name"] = renamed.name
            (renamed / "QUELLENINFO.json").write_text(json.dumps(manifest), encoding="utf-8")
            before = {p.name: p.read_bytes() for p in renamed.iterdir()}
            result = self.inspect(renamed, repo, cache)
            self.assertEqual("LEGACY_SEPARATOR_ALIAS", result["package_naming"]["status"])
            self.assertEqual("UNVERIFIED_DO_NOT_RESUME", result["package_naming"]["resume_safety"])
            self.assertEqual([], result["already_registered"])
            self.assertEqual(1, result["originals_verified"])
            self.assertEqual(before, {p.name: p.read_bytes() for p in renamed.iterdir()})

    def test_legacy_separator_alias_not_allowed_for_other_source_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, progress = self.make_package(tmp)
            progress["plan"]["package_name"] = "1303_SStA_10001_Nr_01740_fixture"
            (package / "ACQUISITION_STATE.json").write_text(json.dumps(progress), encoding="utf-8")
            with self.assertRaisesRegex(intake.PackageIntakeError, "package identities conflict"):
                self.inspect(package, repo, cache)

    def test_legacy_separator_alias_does_not_hide_guid_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, manifest, progress = self.make_package(tmp)
            renamed = package.with_name(package.name.replace("_", "-"))
            package.rename(renamed)
            manifest["package_name"] = renamed.name
            (renamed / "QUELLENINFO.json").write_text(json.dumps(manifest), encoding="utf-8")
            progress["plan"]["guid"] = "not-the-real-source"
            (renamed / "ACQUISITION_STATE.json").write_text(json.dumps(progress), encoding="utf-8")
            with self.assertRaisesRegex(intake.PackageIntakeError, "acquisition plan and completed manifest disagree"):
                self.inspect(renamed, repo, cache)

    def test_unknown_progress_status_fails_even_with_correct_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, progress = self.make_package(tmp)
            progress["images"][0]["status"] = "planned"
            (package / "ACQUISITION_STATE.json").write_text(json.dumps(progress), encoding="utf-8")
            with self.assertRaisesRegex(intake.PackageIntakeError, "unverified original"):
                self.inspect(package, repo, cache)

    def test_repo_directory_cannot_be_source_preservation_package(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, cache, _, _ = self.make_package(tmp)
            with self.assertRaisesRegex(intake.PackageIntakeError, "inside repository"):
                self.inspect(repo, repo, cache)


if __name__ == "__main__":
    unittest.main()
