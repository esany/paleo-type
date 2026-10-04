from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

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
JPEG_32X16 = (
    b"\xff\xd8"
    b"\xff\xc0\x00\x11\x08\x00\x10\x00\x20\x03"
    b"\x01\x11\x00\x02\x11\x00\x03\x11\x00"
    b"\xff\xd9"
)


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


def one_image(name="0001", typ="jpg", single=True):
    return json.dumps(
        [{"name": name, "typ": typ, "istEinzelbild": single}]
    ).encode("utf-8")


class AcquisitionTests(unittest.TestCase):
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

    def test_jpeg_dimensions_are_checked(self):
        self.assertEqual((32, 16), acquisition.jpeg_dimensions(JPEG_32X16))
        with self.assertRaises(acquisition.AcquisitionError):
            acquisition.jpeg_dimensions(b"not-a-jpeg")

    def test_acquire_writes_provenance_checksums_and_revalidates_existing_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                source(image_count=1), one_image()
            )

            def fresh_response(_request, timeout=60.0):
                response = Mock()
                response.read.side_effect = [JPEG_32X16, b""]
                response.__enter__ = Mock(return_value=response)
                response.__exit__ = Mock(return_value=None)
                return response

            opener = Mock(side_effect=fresh_response)
            first = acquisition.acquire(plan, root, opener=opener, rate_limit_seconds=0)
            second = acquisition.acquire(plan, root, opener=opener, rate_limit_seconds=0)
            package = root / plan.package_name
            self.assertEqual("complete", first["status"])
            self.assertEqual("already-present", second["images"][0]["status"])
            self.assertEqual(plan.file_list_url, second["file_list_url"])
            self.assertEqual(plan.file_list_sha256, second["file_list_sha256"])
            self.assertIn("acquired_at_utc", second)
            self.assertTrue((package / "QUELLENINFO.json").is_file())
            self.assertTrue((package / "QUELLENINFO.txt").is_file())
            self.assertTrue((package / "SHA256SUMS.txt").is_file())
            self.assertFalse((package / "0001.jpg.part").exists())
            self.assertEqual(2, opener.call_count)

    def test_existing_different_file_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                source(image_count=1), one_image()
            )
            response = Mock()
            response.read.side_effect = [JPEG_32X16, b""]
            response.__enter__ = Mock(return_value=response)
            response.__exit__ = Mock(return_value=None)
            opener = Mock(return_value=response)
            package = root / plan.package_name
            package.mkdir(parents=True)
            (package / "0001.jpg").write_bytes(b"different")
            with self.assertRaises(acquisition.AcquisitionError):
                acquisition.acquire(plan, root, opener=opener, rate_limit_seconds=0)
            self.assertEqual(b"different", (package / "0001.jpg").read_bytes())


if __name__ == "__main__":
    unittest.main()
