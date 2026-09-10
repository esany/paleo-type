from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "tools" / "regii5_evidence_packet.py"


class RegII5EvidencePacketTests(unittest.TestCase):
    def run_packet(
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

    def test_blind_packet_withholds_current_reading_and_candidate_context(self) -> None:
        result = self.run_packet("62r-L17")
        self.assertEqual("DERIVED_REGII5_EVIDENCE_PACKET", result["view"])
        self.assertFalse(result["canonical"])
        self.assertEqual("blind", result["phase"])
        self.assertEqual("62r-L17", result["target"]["line_ref"])
        self.assertEqual("THHSTAW-EGA-REG-II-5-STAT-VIS-00000129", result["target"]["source_id"])
        self.assertEqual("FILE-REG-II-5-00000129-EXCERPT", result["target"]["file_id"])
        self.assertEqual("133", result["target"]["export_image"])
        self.assertEqual("15", result["target"]["pdf_page"])
        self.assertEqual("NOT_ESTABLISHED_BY_COMPILER", result["target"]["render_requirement"]["vision_inspectable"])
        self.assertNotIn("current_reading", result)
        self.assertNotIn("candidate_sources", result)
        self.assertFalse(result["phase_boundary"]["current_reading_included"])
        self.assertFalse(result["phase_boundary"]["candidate_sources_included"])
        serialized = json.dumps(result, ensure_ascii=False)
        self.assertNotIn("sonst", serialized.lower())
        self.assertNotIn("canonical_status", serialized)

    def test_candidate_bearing_phase_requires_prior_blind_observation(self) -> None:
        result = self.run_packet("62r-L17", phase="explore", expect_rc=2)
        self.assertEqual("ERROR", result["status"])
        self.assertIn("requires --blind-observation", result["error"])

    def test_explore_freezes_observation_and_exposes_compact_reading_afterward(self) -> None:
        observation = "bounded word; initial round/tall form; medial joins; terminal -en-like cluster uncertain"
        result = self.run_packet("62r-L17", phase="explore", observation=observation)
        frozen = result["blind_observation"]
        self.assertEqual("FROZEN_CALLER_SUPPLIED", frozen["status"])
        self.assertEqual(observation, frozen["text"])
        self.assertEqual(hashlib.sha256(observation.encode("utf-8")).hexdigest(), frozen["sha256"])

        current = result["current_reading"]
        self.assertEqual("62r-L17", current["line_ref"])
        self.assertIn("sonsten", current["diplomatic_reading"])
        self.assertNotIn("evidence_note", current)
        self.assertEqual("ZERO_DIPLOMATIC_EVIDENCE_WEIGHT", result["phase_boundary"]["candidate_authority"])

        candidates = result["candidate_sources"]
        self.assertEqual(1, len(candidates))
        parallel = candidates[0]
        self.assertEqual("parallel_witness", parallel["type"])
        self.assertEqual(0, parallel["diplomatic_evidence_weight"])
        self.assertEqual("G4-007", parallel["mapping"]["map_id"])
        self.assertEqual("candidate_generation_only", parallel["role"])
        self.assertEqual(
            [f"308r-L{line:02d}" for line in range(11, 19)],
            [row["line_ref"] for row in parallel["rows"]],
        )
        self.assertTrue(all("evidence_note" not in row for row in parallel["rows"]))

    def test_adversarial_80_so_control_is_anchor_neutral_until_exploration(self) -> None:
        blind = self.run_packet("62r-L19", phase="blind")
        self.assertNotIn("current_reading", blind)
        self.assertNotIn("candidate_sources", blind)

        observation = "first graph is S-/8-like; followed by a small round graph; lexical value not assigned"
        explore = self.run_packet("62r-L19", phase="explore", observation=observation)
        self.assertIn("80", explore["current_reading"]["diplomatic_reading"])
        parallel = explore["candidate_sources"][0]
        self.assertEqual("G4-008", parallel["mapping"]["map_id"])
        regii4_l19 = next(row for row in parallel["rows"] if row["line_ref"] == "308r-L19")
        self.assertIn("so wolff", regii4_l19["diplomatic_reading"].lower())
        self.assertEqual(0, parallel["diplomatic_evidence_weight"])

    def test_adjudicate_packet_cannot_decide_or_persist(self) -> None:
        result = self.run_packet(
            "62r-L19",
            phase="adjudicate",
            observation="S-/8-like initial graph plus round following graph",
        )
        adjudication = result["adjudication"]
        self.assertEqual("PENDING_SOURCE_REINSPECTION", adjudication["status"])
        self.assertFalse(adjudication["compiler_can_decide"])
        self.assertFalse(adjudication["compiler_can_persist_result"])
        self.assertEqual(
            ["promote", "retain current", "downgrade/reopen", "unresolved"],
            adjudication["allowed_outcomes"],
        )

    def test_known_control_rows_resolve_without_status_or_evidence_note_payload(self) -> None:
        controls = {
            "62r-L13": "nachkomung",
            "62r-L17": "sonsten",
            "62r-L19": "wolff",
            "62r-L20": "gemeinswalde",
            "62v-L11": "steinbruch",
            "63r-L05": "Beuelh",
        }
        for line_ref, token in controls.items():
            with self.subTest(line_ref=line_ref):
                result = self.run_packet(
                    line_ref,
                    phase="explore",
                    observation=f"control source-only observation for {line_ref}",
                )
                self.assertIn(token, result["current_reading"]["diplomatic_reading"])
                self.assertNotIn("evidence_note", result["current_reading"])
                self.assertNotIn("canonical_status", result)

    def test_nonsecure_g4_mapping_does_not_expose_parallel_text(self) -> None:
        result = self.run_packet(
            "63r-L05",
            phase="explore",
            observation="display/prose target inspected without candidate text",
        )
        self.assertEqual(1, len(result["candidate_sources"]))
        parallel = result["candidate_sources"][0]
        self.assertEqual("parallel_witness_mapping", parallel["type"])
        self.assertEqual("G4-012", parallel["mapping"]["map_id"])
        self.assertFalse(parallel["mapping"]["candidate_text_exposed"])
        self.assertEqual([], parallel["rows"])


if __name__ == "__main__":
    unittest.main()
