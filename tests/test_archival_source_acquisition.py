from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
from contextlib import redirect_stdout
import unittest
from io import BytesIO, StringIO
from PIL import Image
from pathlib import Path
from unittest.mock import Mock, patch

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "archival_source_acquisition",
    REPO / "tools" / "archival_source_acquisition.py",
)
assert SPEC.loader is not None
acquisition = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = acquisition
SPEC.loader.exec_module(acquisition)

FIXTURES = REPO / "tests" / "fixtures"
GUID_632 = "edd69aa1-eae4-4970-a695-94aaeccd6724"
GUID_754 = "6e0423b3-880c-431c-9a1a-b9e12086b3a7"
GUID_OPPURG = "e741423e-c9f2-4f52-ad43-3cbbe9a7b1af"
# Genuine compressed JPEG fixture generated with the same declared decoder,
# rather than the earlier SOF-only pseudo-JPEG (which has no image pixel stream).
_buffer = BytesIO()
Image.new("RGB", (32, 16), (80, 122, 157)).save(
    _buffer, format="JPEG", quality=80
)
JPEG_32X16 = _buffer.getvalue()



def fixture(label: str) -> bytes:
    return (FIXTURES / f"ssta-files-{label}.json").read_bytes()


def source(**overrides):
    values = {
        "archive": "Sächsisches Staatsarchiv",
        "fonds": "20578",
        "signature": "Nr. 632",
        "title": "Lehn zu gesamter Hand am Mann- und Weiberlehngut Knau samt Zubehör",
        "date_label": "1704-1781",
        "guid": GUID_632,
        "page_url": f"https://www.archiv.sachsen.de/archiv/bestand.jsp?guid={GUID_632}",
        "archive_code": "SStA",
        "name_key": "Lehn zu gesamter Hand Knau",
        "classification_path": "10.5.3 Oppurg, Knau, Grunau, Gröbitz",
        "image_count": 135,
    }
    values.update(overrides)
    return acquisition.SourceMetadata(**values)


def images(*names: str) -> bytes:
    return json.dumps(
        [
            {"name": name, "typ": "jpg", "istEinzelbild": True}
            for name in names
        ]
    ).encode("utf-8")


def one_image(name="0001", typ="jpg", single=True):
    return json.dumps(
        [{"name": name, "typ": typ, "istEinzelbild": single}]
    ).encode("utf-8")


def response_for(data: bytes = JPEG_32X16):
    response = Mock()
    response.read.side_effect = [data, b""]
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=None)
    return response


class AcquisitionTests(unittest.TestCase):
    def test_metadata_can_be_passed_on_stdin_without_a_sidecar_file(self):
        metadata_json = json.dumps(acquisition.asdict(source()), ensure_ascii=False)
        with patch.object(sys, "stdin", StringIO(metadata_json)):
            loaded = acquisition.load_source(Path("-"))
        self.assertEqual(source(), loaded)

    def test_dresden_metadata_stdin_cli_dry_run_uses_list_only_fullsize(self):
        guid = "8bdce320-0ce6-4ddb-b37a-eed8fe52cb94"
        metadata = source(
            guid=guid, signature="Nr. 01739", image_count=0,
            page_url=f"https://www.archiv.sachsen.de/archiv/bestand.jsp?guid={guid}",
        )
        with tempfile.TemporaryDirectory() as tmp:
            listing = Path(tmp) / "files.json"
            listing.write_bytes(images("0002", "0001"))
            output_root = Path(tmp) / "external-source-root"
            buffer = StringIO()
            argv = [
                "archival_source_acquisition.py", "--metadata", "-",
                "--file-list", str(listing), "--output-root", str(output_root),
                "--route", "fullsize", "--dry-run",
            ]
            with patch.object(sys, "argv", argv):
                with patch.object(sys, "stdin", StringIO(json.dumps(acquisition.asdict(metadata)))):
                    with redirect_stdout(buffer):
                        self.assertEqual(0, acquisition.main())
            planned = json.loads(buffer.getvalue())
            self.assertEqual("fullsize", planned["route"])
            self.assertEqual(["0001.jpg", "0002.jpg"],
                             [item["filename"] for item in planned["images"]])
            self.assertEqual([
                f"https://www.archiv.sachsen.de/digitalisate/{guid}/fullsize/0001.jpg",
                f"https://www.archiv.sachsen.de/digitalisate/{guid}/fullsize/0002.jpg",
            ], [item["url"] for item in planned["images"]])
            self.assertFalse(output_root.exists())

    def test_real_files_json_fixtures_drive_three_distinct_plans(self):
        provider = acquisition.SaechsischesStaatsarchivProvider()
        cases = (
            ("nr632", source(), 135, "0135.jpg"),
            (
                "nr754",
                source(
                    signature="Nr. 754",
                    title="Kauf-, Lehns- und Vererbungsurkunden über Oppurg und Knau",
                    date_label="1627_1652-1668_1676_1690_1703-1720",
                    guid=GUID_754,
                    name_key="Kauf Lehns Vererbungsurkunden Oppurg Knau",
                    image_count=61,
                ),
                61,
                "0061.jpg",
            ),
            (
                "oppurg-pilot",
                source(
                    guid=GUID_OPPURG,
                    signature="Technischer Test ohne bestätigte Signatur",
                    image_count=139,
                ),
                139,
                "0139.jpg",
            ),
        )
        packages = set()
        for label, metadata, expected_count, last_name in cases:
            raw = fixture(label)
            plan = provider.plan(metadata, raw)
            self.assertEqual(expected_count, len(plan.images))
            self.assertEqual("0001.jpg", plan.images[0].filename)
            self.assertEqual(last_name, plan.images[-1].filename)
            self.assertEqual(
                [f"{index:04d}.jpg" for index in range(1, expected_count + 1)],
                [image.filename for image in plan.images],
            )
            self.assertEqual(hashlib.sha256(raw).hexdigest(), plan.file_list_sha256)
            self.assertTrue(plan.file_list_url.endswith(f"/{metadata.guid}/files.json"))
            packages.add(plan.package_name)
        self.assertEqual(3, len(packages))

    def test_fetch_file_list_uses_guid_derived_endpoint(self):
        raw = fixture("nr632")
        response = Mock()
        response.read.return_value = raw
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=None)
        opener = Mock(return_value=response)
        provider = acquisition.SaechsischesStaatsarchivProvider()
        self.assertEqual(raw, provider.fetch_file_list(source(), opener=opener))
        self.assertEqual(
            f"https://www.archiv.sachsen.de/digitalisate/{GUID_632}/files.json",
            opener.call_args.args[0].full_url,
        )

    def test_manifest_entries_not_supplied_count_determine_images(self):
        provider = acquisition.SaechsischesStaatsarchivProvider()
        plan = provider.plan(source(image_count=0), one_image(name="0042"))
        self.assertEqual(["0042.jpg"], [image.filename for image in plan.images])
        with self.assertRaisesRegex(acquisition.AcquisitionError, "differs"):
            provider.plan(source(image_count=135), one_image(name="0042"))

    def test_unsupported_or_unsafe_file_lists_fail_closed(self):
        provider = acquisition.SaechsischesStaatsarchivProvider()
        metadata = source(image_count=0)
        invalid = (
            b"not-json",
            b"[]",
            one_image(name="../0001"),
            one_image(typ="png"),
            one_image(single=False),
            json.dumps(
                [
                    {"name": "0001", "typ": "jpg", "istEinzelbild": True},
                    {"name": "0001", "typ": "jpg", "istEinzelbild": True},
                ]
            ).encode(),
        )
        for raw in invalid:
            with self.subTest(raw=raw[:40]):
                with self.assertRaises(acquisition.AcquisitionError):
                    provider.plan(metadata, raw)
        with self.assertRaises(acquisition.AcquisitionError):
            provider.file_list_url("../invalid")

    def test_fullsize_route_uses_list_names_and_not_preview(self):
        plan = acquisition.SaechsischesStaatsarchivProvider().plan(
            source(image_count=0), one_image(name="0042"), route="fullsize"
        )
        self.assertEqual(
            f"https://www.archiv.sachsen.de/digitalisate/{GUID_632}/fullsize/0042.jpg",
            plan.images[0].url,
        )

    def test_dresden_1303_record_preserves_exact_two_real_listed_jpegs(self):
        # Captured from official files.json for 10001 Ältere Urkunden
        # Nr. 01739 on 2026-10-27. The original list is unsorted.
        guid = "8bdce320-0ce6-4ddb-b37a-eed8fe52cb94"
        actual_list = json.dumps([
            {"name": "0002", "typ": "jpg", "istEinzelbild": True},
            {"name": "0001", "typ": "jpg", "istEinzelbild": True},
        ]).encode()
        provider = acquisition.SaechsischesStaatsarchivProvider()
        metadata = source(guid=guid, signature="Nr. 01739",
                          page_url=f"https://www.archiv.sachsen.de/archiv/bestand.jsp?guid={guid}",
                          image_count=0)
        plan = provider.plan(metadata, actual_list, route="fullsize")
        self.assertEqual(["0001.jpg", "0002.jpg"],
                         [image.filename for image in plan.images])
        self.assertEqual([
            f"https://www.archiv.sachsen.de/digitalisate/{guid}/fullsize/0001.jpg",
            f"https://www.archiv.sachsen.de/digitalisate/{guid}/fullsize/0002.jpg",
        ], [image.url for image in plan.images])
        self.assertEqual(2, len(plan.images))
        self.assertNotIn("0003.jpg", [image.filename for image in plan.images])

    def test_fullsize_from_nonsequential_list_never_invents_intermediate_names(self):
        provider = acquisition.SaechsischesStaatsarchivProvider()
        plan = provider.plan(source(image_count=0), images("0042", "0001"),
                             route="fullsize")
        self.assertEqual(["0001.jpg", "0042.jpg"],
                         [image.filename for image in plan.images])
        self.assertTrue(all("/fullsize/" in image.url for image in plan.images))
        self.assertTrue(all("/preview/" not in image.url for image in plan.images))
        self.assertTrue(all(image.url.startswith("https://www.archiv.sachsen.de/")
                            for image in plan.images))

    def test_jpeg_dimensions_are_checked(self):
        self.assertEqual((32, 16), acquisition.jpeg_dimensions(JPEG_32X16))
        with self.assertRaises(acquisition.AcquisitionError):
            acquisition.jpeg_dimensions(b"not-a-jpeg")
        with self.assertRaisesRegex(acquisition.AcquisitionError, "truncated JPEG"):
            acquisition.jpeg_dimensions(JPEG_32X16[:-2])
        with self.assertRaises(acquisition.AcquisitionError):
            acquisition.jpeg_dimensions(JPEG_32X16[:70] + bytes.fromhex("ffd9"))

    def test_complete_repeat_run_is_network_free_and_revalidates_persisted_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                source(image_count=1), one_image()
            )
            opener = Mock(side_effect=lambda *_args, **_kwargs: response_for())
            first = acquisition.acquire(plan, root, opener=opener, rate_limit_seconds=0)
            second = acquisition.acquire(plan, root, opener=opener, rate_limit_seconds=0)
            package = root / plan.package_name
            self.assertEqual("complete", first["status"])
            self.assertEqual("verified-existing", second["images"][0]["status"])
            self.assertEqual(plan.file_list_url, second["file_list_url"])
            self.assertEqual(plan.file_list_sha256, second["file_list_sha256"])
            self.assertTrue((package / "QUELLENINFO.json").is_file())
            self.assertTrue((package / "QUELLENINFO.txt").is_file())
            self.assertTrue((package / "SHA256SUMS.txt").is_file())
            self.assertTrue((package / acquisition.PROGRESS_FILENAME).is_file())
            self.assertFalse((package / "0001.jpg.part").exists())
            self.assertEqual(1, opener.call_count)

    def test_manifest_failure_keeps_restartable_state_and_resume_finishes_package(self):
        for failed_sidecar in ("QUELLENINFO.json", "QUELLENINFO.txt", "SHA256SUMS.txt"):
            with self.subTest(failed_sidecar=failed_sidecar):
                with tempfile.TemporaryDirectory() as temp:
                    root = Path(temp)
                    metadata = source(image_count=1)
                    plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                        metadata, one_image()
                    )
                    opener = Mock(side_effect=lambda *_args, **_kwargs: response_for())
                    original_writer = acquisition._write_text_atomic

                    def interrupted_writer(path, content):
                        if path.name == failed_sidecar:
                            raise OSError("simulated manifest finalization interruption")
                        return original_writer(path, content)

                    with patch.object(
                        acquisition, "_write_text_atomic", side_effect=interrupted_writer
                    ):
                        with self.assertRaisesRegex(
                            OSError, "simulated manifest finalization interruption"
                        ):
                            acquisition.acquire(
                                plan, root, opener=opener, rate_limit_seconds=0
                            )

                    target = root / plan.package_name
                    state = json.loads(
                        (target / acquisition.PROGRESS_FILENAME).read_text(
                            encoding="utf-8"
                        )
                    )
                    self.assertEqual("partial-restartable", state["status"])
                    self.assertNotIn("completed_at_utc", state)
                    self.assertEqual(
                        "manifest-finalization", state["last_failure"]["phase"]
                    )
                    self.assertEqual(1, len(state["images"]))
                    self.assertEqual(
                        "partial-restartable",
                        acquisition.status_for_source(metadata, root)["status"],
                    )
                    self.assertFalse((target / failed_sidecar).exists())

                    opener.reset_mock()
                    manifest = acquisition.acquire(
                        plan, root, opener=opener, rate_limit_seconds=0
                    )
                    opener.assert_not_called()
                    self.assertEqual("complete", manifest["status"])
                    self.assertEqual("verified-existing", manifest["images"][0]["status"])
                    final_state = json.loads(
                        (target / acquisition.PROGRESS_FILENAME).read_text(
                            encoding="utf-8"
                        )
                    )
                    self.assertEqual("complete", final_state["status"])
                    self.assertIsNone(final_state["last_failure"])
                    self.assertTrue(final_state["completed_at_utc"])
                    for sidecar in (
                        "QUELLENINFO.json", "QUELLENINFO.txt", "SHA256SUMS.txt"
                    ):
                        self.assertTrue((target / sidecar).is_file())
                    self.assertIn(
                        manifest["images"][0]["sha256"],
                        (target / "SHA256SUMS.txt").read_text(encoding="utf-8"),
                    )

    def test_interruption_persists_verified_progress_and_resume_skips_completed_image(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                source(image_count=3), images("0001", "0002", "0003")
            )
            first_urls: list[str] = []

            def first_opener(request, timeout=60.0):
                first_urls.append(request.full_url)
                if request.full_url.endswith("filename=0002.jpg"):
                    raise OSError("simulated network interruption")
                return response_for()

            with self.assertRaisesRegex(acquisition.AcquisitionError, "0002.jpg"):
                acquisition.acquire(
                    plan,
                    root,
                    opener=first_opener,
                    retries=1,
                    rate_limit_seconds=0,
                )
            package = root / plan.package_name
            state = json.loads(
                (package / acquisition.PROGRESS_FILENAME).read_text(encoding="utf-8")
            )
            self.assertEqual("partial-restartable", state["status"])
            self.assertEqual(["0001.jpg"], [item["filename"] for item in state["images"]])
            self.assertEqual("0002.jpg", state["last_failure"]["filename"])
            self.assertTrue((package / "0001.jpg").is_file())
            self.assertFalse((package / "0002.jpg").exists())

            resumed_urls: list[str] = []

            def resumed_opener(request, timeout=60.0):
                resumed_urls.append(request.full_url)
                return response_for()

            result = acquisition.acquire(
                plan,
                root,
                opener=resumed_opener,
                retries=1,
                rate_limit_seconds=0,
            )
            self.assertEqual("complete", result["status"])
            self.assertEqual("verified-existing", result["images"][0]["status"])
            self.assertEqual(2, len(resumed_urls))
            self.assertTrue(all("0001.jpg" not in url for url in resumed_urls))
            final_state = json.loads(
                (package / acquisition.PROGRESS_FILENAME).read_text(encoding="utf-8")
            )
            self.assertEqual("complete", final_state["status"])
            self.assertEqual(3, len(final_state["images"]))

    def test_corruption_of_recorded_progress_fails_closed_without_network(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                source(image_count=1), one_image()
            )
            acquisition.acquire(
                plan,
                root,
                opener=lambda *_args, **_kwargs: response_for(),
                rate_limit_seconds=0,
            )
            package = root / plan.package_name
            (package / "0001.jpg").write_bytes(b"corrupt")
            opener = Mock(side_effect=AssertionError("network must not be used"))
            with self.assertRaises(acquisition.AcquisitionError):
                acquisition.acquire(plan, root, opener=opener, rate_limit_seconds=0)
            opener.assert_not_called()

    def test_status_is_read_only_and_does_not_start_or_resume_acquisition(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            metadata = source(image_count=1)
            before = acquisition.status_for_source(metadata, root)
            self.assertEqual("not-started", before["status"])
            self.assertTrue(before["read_only"])
            self.assertFalse((root / acquisition.package_name(metadata)).exists())

            plan = acquisition.SaechsischesStaatsarchivProvider().plan(metadata, one_image())
            acquisition.acquire(
                plan,
                root,
                opener=lambda *_args, **_kwargs: response_for(),
                rate_limit_seconds=0,
            )
            state_path = root / plan.package_name / acquisition.PROGRESS_FILENAME
            state_before = state_path.read_bytes()
            status = acquisition.status_for_source(metadata, root)
            state_after = state_path.read_bytes()
            self.assertEqual("complete", status["status"])
            self.assertTrue(status["read_only"])
            self.assertEqual(state_before, state_after)

    def test_operator_cancellation_leaves_restartable_state(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                source(image_count=1), one_image()
            )
            with self.assertRaises(KeyboardInterrupt):
                acquisition.acquire(
                    plan,
                    root,
                    opener=Mock(side_effect=KeyboardInterrupt()),
                    rate_limit_seconds=0,
                )
            package = root / plan.package_name
            state = json.loads(
                (package / acquisition.PROGRESS_FILENAME).read_text(encoding="utf-8")
            )
            self.assertEqual("cancelled-restartable", state["status"])
            self.assertEqual("0001.jpg", state["last_failure"]["filename"])

    def test_existing_different_file_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                source(image_count=1), one_image()
            )
            opener = Mock(return_value=response_for())
            package = root / plan.package_name
            package.mkdir(parents=True)
            (package / "0001.jpg").write_bytes(b"different")
            with self.assertRaises(acquisition.AcquisitionError):
                acquisition.acquire(plan, root, opener=opener, rate_limit_seconds=0)
            self.assertEqual(b"different", (package / "0001.jpg").read_bytes())

    def test_repository_worktree_is_rejected_as_output_root(self):
        plan = acquisition.SaechsischesStaatsarchivProvider().plan(
            source(image_count=1), one_image()
        )
        with self.assertRaisesRegex(acquisition.AcquisitionError, "repository/worktree"):
            acquisition.acquire(
                plan,
                REPO / "never-create-this",
                opener=Mock(side_effect=AssertionError("no network")),
                rate_limit_seconds=0,
            )
        self.assertFalse((REPO / "never-create-this").exists())


if __name__ == "__main__":
    unittest.main()
