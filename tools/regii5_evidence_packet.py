#!/usr/bin/env python3
"""Compile a small, read-only Reg. Ii 5 evidence packet.

This is a project-bounded prototype, not a canonical research owner and not a
replacement for ``project_context.py``.  PR #144 established the phase split;
#145 narrows the default packet back to the bounded Reg. Ii 5 Editionslocus
before any candidate-method policy is designed. A completed principal use may
remain addressable as historical evidence; packet compilation never selects a
current research priority.

* ``blind`` exposes only target addressing/provenance needed to inspect pixels;
  it deliberately omits the current diplomatic reading and all candidate
  sources.
* ``explore`` requires a caller-supplied source-only observation, freezes it by
  digest, and only then exposes the compact current Reg. Ii 5 reading.  No
  candidate source is activated by default.
* ``adjudicate`` preserves the same bounded material while stating the mandatory
  return-to-target boundary.  It never decides or persists a reading.

The output is disposable/rebuildable derived state.  Phase #145 intentionally
contains no automatic parallel-witness, HTR, lexicon, retrieval or other
candidate policy; those belong to a later, separately reviewed method step.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import source_contract

PROJECT_ID = "ega-reg-ii-5-knau"
PRINCIPAL_USE_ID = "USE-REGII5-00000129-PRINCIPAL"
REGII5_READING_DIR = Path("projects/ega-reg-ii-5-knau/transcription/first-reading")
LINE_REF_RE = re.compile(r"^(\d+)([rv])-L(\d+)$")
PACKET_USE_STATUSES = {"active", "historical"}


class PacketError(RuntimeError):
    """A bounded packet cannot be compiled from the current canonical state."""


def folio_from_line_ref(line_ref: str) -> str:
    match = LINE_REF_RE.fullmatch(line_ref)
    if not match:
        raise PacketError(f"invalid Reg. Ii 5 line_ref {line_ref!r}; expected e.g. 62r-L19")
    return f"{match.group(1)}{match.group(2)}"


def compact_reading_row(row: dict[str, str]) -> dict[str, str]:
    """Keep only locus-specific reading state; omit long evidence-note audit prose."""
    fields = (
        "line_ref",
        "diplomatic_reading",
        "research_status",
        "alternatives",
        "source_phenomena",
        "abbreviation_layer",
        "editorial_supply",
    )
    return {field: row.get(field, "") for field in fields}


def find_target_reading(root: Path, line_ref: str) -> tuple[str, dict[str, str]]:
    folio = folio_from_line_ref(line_ref)
    rel_path = REGII5_READING_DIR / f"{folio}.tsv"
    path = root / rel_path
    if not path.is_file():
        raise PacketError(f"missing canonical reading owner {rel_path}")
    _, rows = source_contract.read_tsv(path)
    matches = [row for row in rows if row.get("line_ref") == line_ref]
    if len(matches) != 1:
        raise PacketError(f"expected exactly one canonical reading row for {line_ref}, found {len(matches)}")
    return rel_path.as_posix(), matches[0]


def resolve_source_target(root: Path, line_ref: str) -> tuple[dict, list[str]]:
    errors, warnings, cache = source_contract.validate(root, source_contract.load_contract(root))
    if errors:
        raise PacketError("source contract is invalid: " + "; ".join(errors))

    project = cache["projects"].get(PROJECT_ID)
    if not project:
        raise PacketError(f"project {PROJECT_ID} has no valid project.yml")

    use = cache["source_uses"].get(PRINCIPAL_USE_ID)
    if not use or cache["use_project"].get(PRINCIPAL_USE_ID) != PROJECT_ID:
        raise PacketError(f"principal use {PRINCIPAL_USE_ID} is unavailable for {PROJECT_ID}")
    if use.get("research_function") != "principal" or use.get("status") not in PACKET_USE_STATUSES:
        raise PacketError(
            f"principal use {PRINCIPAL_USE_ID} is not an addressable active/historical principal Reg. Ii 5 use"
        )

    evidence_rows = [
        row for row in cache["evidence_by_use"].get(PRINCIPAL_USE_ID, [])
        if row.get("status") == use.get("status") and row.get("status") in PACKET_USE_STATUSES
    ]
    if len(evidence_rows) != 1:
        raise PacketError(
            f"expected exactly one status-matched evidence binding for {PRINCIPAL_USE_ID}, found {len(evidence_rows)}"
        )
    evidence = evidence_rows[0]
    file_row = cache["files"].get(evidence.get("file_id", ""))
    if not file_row:
        raise PacketError(f"evidence {evidence.get('evidence_id', '')} has no canonical File")

    source_id = use.get("source_id", "")
    source_row = cache["sources"].get(source_id)
    if not source_row:
        raise PacketError(f"principal Source {source_id} is unavailable")
    if file_row.get("source_id") != source_id:
        raise PacketError(
            f"File {file_row.get('file_id', '')} does not belong to principal Source {source_id}"
        )

    folio = folio_from_line_ref(line_ref)
    crosswalk_matches = [
        row for row in cache["crosswalks"].get(source_id, [])
        if row.get("archival_folio") == folio
    ]
    if len(crosswalk_matches) != 1:
        raise PacketError(
            f"expected exactly one crosswalk row for {source_id} {folio}, found {len(crosswalk_matches)}"
        )
    crosswalk = crosswalk_matches[0]

    target = {
        "project_id": PROJECT_ID,
        "line_ref": line_ref,
        "use_id": use.get("use_id", ""),
        "use_status": use.get("status", ""),
        "research_function": use.get("research_function", ""),
        "relevant_locus": use.get("relevant_locus", ""),
        "source_id": source_id,
        "source_title": source_row.get("title", ""),
        "evidence_id": evidence.get("evidence_id", ""),
        "evidence_status": evidence.get("status", ""),
        "file_id": file_row.get("file_id", ""),
        "file_sha256": file_row.get("sha256", ""),
        "filename": file_row.get("filename", ""),
        "storage_status": file_row.get("storage_status", ""),
        "rights_status": file_row.get("rights_status", ""),
        "archival_folio": crosswalk.get("archival_folio", ""),
        "export_image": crosswalk.get("export_image", ""),
        "pdf_page": crosswalk.get("pdf_page", ""),
        "mapping_status": crosswalk.get("mapping_status", ""),
        "render_requirement": {
            "recommended_dpi": 600,
            "artifact_identity": "NOT_COMPILED",
            "vision_inspectable": "NOT_ESTABLISHED_BY_COMPILER",
        },
    }
    return target, warnings


def frozen_observation(text: str) -> dict[str, str]:
    encoded = text.encode("utf-8")
    return {
        "status": "FROZEN_CALLER_SUPPLIED",
        "text": text,
        "sha256": hashlib.sha256(encoded).hexdigest(),
        "authority_note": (
            "Caller-supplied source-only observation. The compiler preserves the supplied text "
            "but does not itself verify the pixels or promote a reading."
        ),
    }


def compile_packet(root: Path, line_ref: str, phase: str, observation: str | None) -> dict:
    target, warnings = resolve_source_target(root, line_ref)
    reading_owner, reading_row = find_target_reading(root, line_ref)

    owners = {
        "file": "corpus/files.tsv",
        "crosswalk": f"corpus/source-data/{target['source_id']}/crosswalk.tsv",
        "project_use": f"projects/{PROJECT_ID}/source-uses.tsv",
        "use_evidence": f"projects/{PROJECT_ID}/research/use-evidence.tsv",
        "current_reading": reading_owner,
    }

    packet: dict = {
        "status": "OK",
        "view": "DERIVED_REGII5_EVIDENCE_PACKET",
        "canonical": False,
        "phase": phase,
        "target": target,
        "canonical_references": owners,
        "warnings": warnings,
    }

    if phase == "blind":
        packet["blind_observation"] = {
            "status": "REQUIRED_BEFORE_EXPLORATION",
            "text": None,
            "note": (
                "Inspect the Reg. Ii 5 target pixels and record only source-visible "
                "boundaries/features/uncertainties. Request an explore/adjudicate packet only "
                "after that observation exists."
            ),
        }
        packet["phase_boundary"] = {
            "current_reading_included": False,
            "candidate_sources_included": False,
            "candidate_policy": "NONE_ACTIVATED",
            "note": "Current reading and all candidate context are deliberately withheld during the blind pass.",
        }
        return packet

    if not observation or not observation.strip():
        raise PacketError(
            f"phase {phase!r} requires --blind-observation before post-blind context is exposed"
        )

    packet["blind_observation"] = frozen_observation(observation)
    packet["current_reading"] = compact_reading_row(reading_row)
    packet["candidate_sources"] = []
    packet["phase_boundary"] = {
        "current_reading_included": True,
        "candidate_sources_included": False,
        "candidate_policy": "NONE_ACTIVATED",
        "candidate_authority": "NO_CANDIDATE_SOURCE_ACTIVE",
        "note": (
            "#145 safe baseline: no parallel witness, HTR, lexicon, retrieval or other candidate "
            "source is activated automatically. Candidate policy is deferred to the next method step."
        ),
    }

    if phase == "adjudicate":
        packet["adjudication"] = {
            "status": "PENDING_SOURCE_REINSPECTION",
            "required_action": (
                "Reinspect the Reg. Ii 5 target pixels and test any externally supplied future "
                "candidate against the frozen blind observation and the target graph."
            ),
            "allowed_outcomes": ["promote", "retain current", "downgrade/reopen", "unresolved"],
            "compiler_can_decide": False,
            "compiler_can_persist_result": False,
        }
    return packet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile a bounded read-only Reg. Ii 5 evidence packet for one canonical line."
    )
    parser.add_argument("--line-ref", required=True, help="Canonical Reg. Ii 5 line, e.g. 62r-L19")
    parser.add_argument(
        "--phase",
        choices=("blind", "explore", "adjudicate"),
        default="blind",
        help="blind withholds reading/candidate context; later phases require --blind-observation",
    )
    parser.add_argument(
        "--blind-observation",
        help="Transient source-only observation text recorded before candidate contact.",
    )
    parser.add_argument("--root", help="Repository root; defaults to the script's repository.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = source_contract.repo_root(args.root)
    try:
        packet = compile_packet(root, args.line_ref, args.phase, args.blind_observation)
    except PacketError as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(packet, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
