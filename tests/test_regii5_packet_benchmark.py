from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "tools" / "regii5_packet_benchmark.py"


class RegII5PacketBenchmarkTests(unittest.TestCase):
    def run_benchmark(
        self,
        line_ref: str,
        phase: str = "blind",
        observation: str | None = None,
        expect_rc: int = 0,
    ) -> dict:
        cmd = [sys.executable, str(SCRIPT), "--line-ref", line_ref, "--phase", phase]
        if observation is not None:
            cmd.extend(["--blind-observation", observation])
        proc = subprocess.run(cmd, check=False, capture_output=True, text=True)
        self.assertEqual(expect_rc, proc.returncode, proc.stderr or proc.stdout)
        raw = proc.stdout if expect_rc == 0 else proc.stderr
        return json.loads(raw)

    def test_blind_packet_is_materially_smaller_than_existing_broad_context(self) -> None:
        result = self.run_benchmark("62r-L19")
        self.assertEqual("DERIVED_REGII5_PACKET_CONTEXT_BENCHMARK", result["view"])
        self.assertFalse(result["canonical"])
        self.assertTrue(result["machine_checks_all_pass"])

        broad = result["baselines"]["broad"]["utf8_bytes"]
        packet = result["baselines"]["evidence_packet"]["utf8_bytes"]
        self.assertGreater(broad, packet)
        self.assertGreater(result["size_comparison"]["utf8_bytes_saved_vs_broad_context"], 0)
        self.assertLess(result["size_comparison"]["packet_share_of_broad_context_pct"], 100.0)
        self.assertEqual(
            "NOT_MEASURED_NO_NEW_TOKENIZER_DEPENDENCY",
            result["size_comparison"]["token_count"],
        )

        state = result["candidate_selection_state"]
        self.assertEqual("NOT_INFERRED_BY_BENCHMARK", state["available_generators"])
        self.assertEqual([], state["activated_generators"])
        self.assertEqual(0, state["candidates_returned"])
        self.assertFalse(state["reading_promotion_by_compiler"])

        # Emit one exact real-data measurement into CI logs so the first #142
        # result record can cite observed numbers rather than estimates.
        print(
            "REGII5_PACKET_BENCHMARK_BLIND="
            + json.dumps(
                {
                    "line_ref": result["fixture"]["line_ref"],
                    "baselines": result["baselines"],
                    "size_comparison": result["size_comparison"],
                    "machine_checks_all_pass": result["machine_checks_all_pass"],
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )

    def test_explore_measurement_preserves_neutral_candidate_state(self) -> None:
        observation = "BENCHMARK-ONLY structural fixture; not a scholarly source observation"
        result = self.run_benchmark(
            "62r-L17",
            phase="explore",
            observation=observation,
        )
        self.assertTrue(result["machine_checks_all_pass"])
        checks = result["machine_preservation_checks"]
        self.assertTrue(checks["post_blind_current_reading_owner_is_explicit"])
        self.assertTrue(checks["post_blind_observation_is_frozen"])
        self.assertTrue(checks["candidate_activation_is_explicit_none"])
        self.assertTrue(checks["candidate_sources_not_implicitly_exposed"])
        self.assertTrue(checks["regii4_g4_not_embedded"])
        self.assertEqual([], result["candidate_selection_state"]["activated_generators"])
        self.assertEqual(0, result["candidate_selection_state"]["candidates_returned"])

    def test_post_blind_benchmark_cannot_bypass_packet_observation_boundary(self) -> None:
        result = self.run_benchmark("62r-L17", phase="explore", expect_rc=2)
        self.assertEqual("ERROR", result["status"])
        self.assertIn("requires --blind-observation", result["error"])

    def test_benchmark_does_not_modify_or_wrap_project_context_contract(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("project_context.compile_project_context", source)
        self.assertNotIn("canonical_status", source.split("def compile_benchmark", 1)[0])
        self.assertNotIn("ega-reg-ii-4", source)
        self.assertNotIn("G4-", source)


if __name__ == "__main__":
    unittest.main()
