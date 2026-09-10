from __future__ import annotations

import importlib.util
import sys
import unittest
from argparse import Namespace
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "tools" / "regii5_visual_retrieval.py"

spec = importlib.util.spec_from_file_location("regii5_visual_retrieval", SCRIPT)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class RegII5VisualRetrievalTests(unittest.TestCase):
    def test_contract_is_same_source_opt_in_and_text_free(self) -> None:
        contract = module.describe_contract()
        self.assertFalse(contract["canonical"])
        self.assertTrue(contract["pool_available"])
        self.assertFalse(contract["pool_activated"])
        self.assertEqual(module.SOURCE_ID, contract["authorized_source_id"])
        self.assertEqual("55v-66v", contract["authorized_folia"])
        self.assertFalse(contract["candidate_text_generated"])
        self.assertFalse(contract["reading_owner_loaded"])
        self.assertFalse(contract["same_hand_inferred"])
        self.assertFalse(contract["reading_promotion_possible"])

    def test_real_crosswalk_resolves_only_authorized_regii5_pool(self) -> None:
        pool = module.authorized_pool(REPO)
        self.assertEqual(list(range(2, 25)), [row["pdf_page"] for row in pool])
        self.assertEqual("55v", pool[0]["folio"])
        self.assertEqual("66v", pool[-1]["folio"])
        self.assertEqual({module.SOURCE_ID}, {row["source_id"] for row in pool})

    def test_pool_availability_does_not_auto_activate_generator(self) -> None:
        args = Namespace(activate_same_source_pool=False)
        with self.assertRaises(module.RetrievalError):
            module.run(args)

    def test_candidate_record_carries_provenance_not_reading(self) -> None:
        candidate = module.candidate_record(
            1,
            {"folio": "61v", "pdf_page": 14},
            (10, 20, 30, 40),
            0.75,
            "a" * 64,
        )
        self.assertEqual("same-source", candidate["pool"])
        self.assertEqual(module.SOURCE_ID, candidate["source_id"])
        self.assertEqual(module.FILE_ID, candidate["file_id"])
        self.assertFalse(candidate["scholarly_inspected"])
        self.assertFalse(candidate["comparator_accepted"])
        self.assertFalse(candidate["reading_promoted"])
        serialized = repr(candidate).lower()
        self.assertNotIn("diplomatic_reading", serialized)
        self.assertNotIn("candidate_text", serialized)

    def test_box_parser_rejects_invalid_shapes(self) -> None:
        self.assertEqual((1, 2, 3, 4), module.parse_box("1,2,3,4"))
        for value in ("1,2,3", "1,2,0,4", "-1,2,3,4", "a,2,3,4"):
            with self.assertRaises(module.RetrievalError):
                module.parse_box(value)


if __name__ == "__main__":
    unittest.main()
