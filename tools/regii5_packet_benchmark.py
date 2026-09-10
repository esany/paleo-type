#!/usr/bin/env python3
"""Measure the existing Reg. Ii 5 evidence packet against the broad Project context.

This is a derived evaluation helper for #142. It does not change either context
contract, infer research truth, activate candidate generators, or establish
source-pixel readiness. The concrete comparison baseline is the existing
``project_context.py`` output because #138 identified its wholesale STATUS
payload as a measurable context-cost amplifier.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import project_context
import regii5_evidence_packet
import source_contract

PROJECT_ID = "ega-reg-ii-5-knau"


def json_metrics(payload: object) -> dict[str, int]:
    compact = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return {
        "characters": len(compact),
        "utf8_bytes": len(compact.encode("utf-8")),
    }


def percentage(part: int, whole: int) -> float | None:
    if not whole:
        return None
    return round((part / whole) * 100.0, 2)


def compile_benchmark(
    root: Path,
    line_ref: str,
    phase: str,
    observation: str | None,
) -> dict:
    rc, broad_context = project_context.compile_project_context(root, PROJECT_ID)
    if rc:
        raise regii5_evidence_packet.PacketError(
            f"project_context baseline failed with rc={rc}: {broad_context}"
        )

    packet = regii5_evidence_packet.compile_packet(root, line_ref, phase, observation)

    broad_metrics = json_metrics(broad_context)
    packet_metrics = json_metrics(packet)
    status_text = broad_context.get("canonical_status", {}).get("text", "")
    status_metrics = {
        "characters": len(status_text),
        "utf8_bytes": len(status_text.encode("utf-8")),
    }

    broad_bytes = broad_metrics["utf8_bytes"]
    packet_bytes = packet_metrics["utf8_bytes"]
    reduction_bytes = broad_bytes - packet_bytes

    serialized_packet = json.dumps(packet, ensure_ascii=False)
    source_id = packet["target"]["source_id"]
    file_id = packet["target"]["file_id"]
    crosswalk_path = packet["canonical_references"]["crosswalk"]

    machine_checks = {
        "project_id_matches": packet["target"]["project_id"] == broad_context["project_id"],
        "source_id_resolves_in_project_context": source_id
        in broad_context["canonical_references"]["source_ids"],
        "file_id_resolves_in_project_context": file_id
        in broad_context["canonical_references"]["file_ids"],
        "crosswalk_owner_resolves_in_project_context": crosswalk_path
        in broad_context["canonical_references"]["crosswalk_paths"],
        "packet_does_not_claim_vision_inspectable": packet["target"]["render_requirement"]
        ["vision_inspectable"]
        == "NOT_ESTABLISHED_BY_COMPILER",
        "candidate_activation_is_explicit_none": packet["phase_boundary"].get(
            "candidate_policy"
        )
        == "NONE_ACTIVATED",
        "candidate_sources_not_implicitly_exposed": packet["phase_boundary"].get(
            "candidate_sources_included"
        )
        is False,
        "status_payload_not_embedded": "canonical_status" not in packet,
        "project_context_payload_not_embedded": "DERIVED_PROJECT_CONTEXT"
        not in serialized_packet,
        "regii4_g4_not_embedded": all(
            marker not in serialized_packet
            for marker in ("ega-reg-ii-4", "G4-", "308r-", "308v-")
        ),
    }

    if phase == "blind":
        machine_checks["blind_withholds_current_reading"] = "current_reading" not in packet
    else:
        machine_checks["post_blind_current_reading_owner_is_explicit"] = bool(
            packet["canonical_references"].get("current_reading")
        )
        machine_checks["post_blind_observation_is_frozen"] = (
            packet.get("blind_observation", {}).get("status") == "FROZEN_CALLER_SUPPLIED"
        )

    return {
        "status": "OK",
        "view": "DERIVED_REGII5_PACKET_CONTEXT_BENCHMARK",
        "canonical": False,
        "fixture": {
            "project_id": PROJECT_ID,
            "line_ref": line_ref,
            "phase": phase,
            "observation_note": (
                "Caller-supplied only; benchmark mechanics do not establish that it is a valid "
                "scholarly source observation."
            ),
        },
        "baselines": {
            "broad": {
                "view": broad_context.get("view"),
                "role": "existing broad derived Project restart context; not a manuscript-task minimum",
                **broad_metrics,
            },
            "canonical_status_text_inside_broad_context": status_metrics,
            "evidence_packet": {
                "view": packet.get("view"),
                "role": "existing bounded Reg. Ii 5 task packet",
                **packet_metrics,
            },
        },
        "size_comparison": {
            "utf8_bytes_saved_vs_broad_context": reduction_bytes,
            "packet_share_of_broad_context_pct": percentage(packet_bytes, broad_bytes),
            "reduction_vs_broad_context_pct": percentage(reduction_bytes, broad_bytes),
            "status_text_share_of_broad_context_pct": percentage(
                status_metrics["utf8_bytes"], broad_bytes
            ),
            "token_count": "NOT_MEASURED_NO_NEW_TOKENIZER_DEPENDENCY",
        },
        "machine_preservation_checks": machine_checks,
        "machine_checks_all_pass": all(machine_checks.values()),
        "candidate_selection_state": {
            "available_generators": "NOT_INFERRED_BY_BENCHMARK",
            "activated_generators": [],
            "candidates_returned": len(packet.get("candidate_sources", [])),
            "candidate_adjudication": (
                packet.get("adjudication", {}).get("status", "NOT_IN_THIS_PHASE")
            ),
            "reading_promotion_by_compiler": False,
        },
        "human_review_required": [
            "Whether the bounded packet is sufficient for the actual scholarly task, not just machine-consistent.",
            "Whether omitted context contains a consequential uncertainty or authority fact for the intended task.",
            "Whether target pixels are actually staged and vision-inspectable in the current scholarly context.",
            "Whether any future candidate generator is appropriate to activate for the specific research question.",
        ],
        "boundary_note": (
            "A smaller payload and passing machine checks demonstrate context reduction and checked "
            "routing/provenance invariants only; they do not establish manuscript truth or scholarly sufficiency."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Measure the bounded Reg. Ii 5 evidence packet against the existing broad Project context."
    )
    parser.add_argument("--line-ref", required=True, help="Canonical Reg. Ii 5 line, e.g. 62r-L19")
    parser.add_argument(
        "--phase",
        choices=("blind", "explore", "adjudicate"),
        default="blind",
    )
    parser.add_argument(
        "--blind-observation",
        help="Required by the existing packet for explore/adjudicate. Benchmark use does not validate it as scholarship.",
    )
    parser.add_argument("--root", help="Repository root; defaults to the script's repository.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = source_contract.repo_root(args.root)
    try:
        result = compile_benchmark(
            root,
            args.line_ref,
            args.phase,
            args.blind_observation,
        )
    except regii5_evidence_packet.PacketError as exc:
        print(
            json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False, indent=2),
            file=sys.stderr,
        )
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
