from __future__ import annotations

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


JPEG_32X16 = (
    b"\xff\xd8"
    b"\xff\xc0\x00\x11\x08\x00\x10\x00\x20\x03"
    b"\x01\x11\x00\x02\x11\x00\x03\x11\x00"
    b"\xff\xd9"
)


def source(**overrides):
    values = {
        "archive": "Sächsisches Staatsarchiv",
        "fonds": "20578",
        "signature": "Nr. 632",
        "title": "Lehn zu gesamter Hand am Mann- und Weiberlehngut Knau samt Zubehör",
        "date_label": "1704-1781",
        "guid": "edd69aa1-eae4-4970-a695-94aaeccd6724",
        "page_url": "https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=edd69aa1-eae4-4970-a695-94aaeccd6724",
        "archive_code": "SStA",
        "name_key": "Lehn zu gesamter Hand Knau",
        "classification_path": "10.5.3 Oppurg, Knau, Grunau, Gröbitz",
        "image_count": 135,
    }
    values.update(overrides)
    return acquisition.SourceMetadata(**values)


class AcquisitionTests(unittest.TestCase):
    def test_two_archivalien_have_deterministic_distinct_plans(self):
        provider = acquisition.SaechsischesStaatsarchivProvider()
        first = provider.plan(source())
        second = provider.plan(
            source(
                signature="Nr. 754",
                title="Kauf-, Lehns- und Vererbungsurkunden über Oppurg und Knau",
                date_label="1627_1652-1668_1676_1690_1703-1720",
                guid="6e0423b3-880c-431c-9a1a-b9e12086b3a7",
                name_key="Kauf Lehns Vererbungsurkunden Oppurg Knau",
                image_count=61,
            )
        )
        self.assertEqual(135, len(first.images))
        self.assertEqual(61, len(second.images))
        self.assertEqual("0001.jpg", first.images[0].filename)
        self.assertEqual("0135.jpg", first.images[-1].filename)
        self.assertEqual("0061.jpg", second.images[-1].filename)
        self.assertNotEqual(first.package_name, second.package_name)
        self.assertIn("0001.jpg", first.images[0].url)
        self.assertIn("download.jsp", first.images[0].url)

    def test_ssta_viewer_structure_is_owned_by_provider_boundary(self):\n        self.assertEqual(\n            {\n                "thumbnail_strip_wrapper": "digitalisat-viewer-thumbnailstrip-wrapper",\n                "image_container": "viewer_digitalisate",\n            },\n            acquisition.SaechsischesStaatsarchivProvider.viewer_structure(),\n        )\n\n    def test_fullsize_route_is_explicit_and_distinct(self):
        plan = acquisition.SaechsischesStaatsarchivProvider().plan(
            source(), route="fullsize", count=2
        )
        self.assertIn("/digitalisate/", plan.images[0].url)
        self.assertIn("/fullsize/0001.jpg", plan.images[0].url)
        self.assertNotIn("thumbnail", plan.images[0].url.lower())

    def test_jpeg_dimensions_are_checked(self):
        self.assertEqual((32, 16), acquisition.jpeg_dimensions(JPEG_32X16))
        with self.assertRaises(acquisition.AcquisitionError):
            acquisition.jpeg_dimensions(b"not-a-jpeg")

    def test_acquire_writes_manifest_checksums_and_is_repeatable(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                source(), count=1
            )

            def fresh_response(_request, timeout=60.0):
                response = Mock()
                response.read.side_effect = [JPEG_32X16, b""]
                response.__enter__ = Mock(return_value=response)
                response.__exit__ = Mock(return_value=None)
                response.headers = {"Content-Type": "image/jpeg"}
                return response

            opener = Mock(side_effect=fresh_response)
            first = acquisition.acquire(plan, root, opener=opener, rate_limit_seconds=0)
            second = acquisition.acquire(plan, root, opener=opener, rate_limit_seconds=0)
            package = root / plan.package_name
            self.assertEqual("complete", first["status"])
            self.assertEqual("already-present", second["images"][0]["status"])
            self.assertTrue((package / "QUELLENINFO.json").is_file())
            self.assertTrue((package / "QUELLENINFO.txt").is_file())
            self.assertTrue((package / "SHA256SUMS.txt").is_file())
            self.assertFalse((package / "0001.jpg.part").exists())
            self.assertEqual(2, opener.call_count)

    def test_existing_different_file_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            plan = acquisition.SaechsischesStaatsarchivProvider().plan(
                source(), count=1
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


if __name__ == "__main__":
    unittest.main()
