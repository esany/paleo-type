#!/usr/bin/env python3
"""Compile a small, read-only Reg. Ii 5 evidence packet for #139.

This is a project-bounded prototype, not a canonical research owner and not a
replacement for ``project_context.py``.  Its main safety property is phase
separation:

* ``blind`` exposes only target addressing/provenance needed to inspect pixels;
  it deliberately omits the current diplomatic reading and all candidate
  sources.
* ``explore`` requires a caller-supplied source-only observation, freezes it by
  digest, and only then exposes the compact current reading plus the existing
  G4 parallel-witness mapping as candidate-generation context.
* ``adjudicate`` exposes the same bounded material while stating the mandatory
  return-to-target boundary.  It never decides or persists a reading.

The output is disposable/rebuildable derived state.  Candidate material has
zero diplomatic evidence weight until a separate source adjudication is made.
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
G4_OWNER = Path(
    "projects/ega-reg-ii-4-bd-ii/research/knau-fol306v-309r-controlled-collation.md"
)
REGII4_READING_DIR = Path("projects/ega-reg-ii-4-bd-ii/transcription/first-reading")
REGII5_READING_DIR = Path("projects/ega-reg-ii-5-knau/transcription/first-reading")

# Reg. Ii 5 canonical anchors use ``62r-L19`` while the independently owned
# Reg. Ii 4 first-reading rows use ``308r-19``.  Treat both as line locators for
# ordering/range selection without rewriting either witness's canonical form.
LOCUS_REF_RE = re.compile(r"^(\d+)([rv])-(L)?(\d+)$")
INLINE_LOCUS_REF_RE = re.compile(r"(\d+)([rv])-(L)?(\d+)")


class PacketError(RuntimeError):
    """A bounded packet cannot be compiled from the current canonical state."""


def line_key(line_ref: str) -> tuple[int, int, int]:
    match = LOCUS_REF_RE.fullmatch(line_ref)
    if not match:
        raise PacketError(f"invalid line locator {line_ref!r}; expected e.g. 62r-L19 or 308r-19")
    folio_no = int(match.group(1))
    side = 0 if match.group(2) == "r" else 1
    line_no = int(match.group(4))
    return folio_no, side, line_no


def folio_from_line_ref(line_ref: str) -> str:
    match = LOCUS_REF_RE.fullmatch(line_ref)
    if not match or match.group(3) != "L":
        raise PacketError(f"invalid Reg. Ii 5 line_ref {line_ref!r}; expected e.g. 62r-L19")
    return f"{match.group(1)}{match.group(2)}"


def refs_in_text(text: str) -> list[str]:
    refs: list[str] = []
    for folio, side, marker, line in INLINE_LOCUS_REF_RE.findall(text):
        prefix = "L" if marker else ""
        refs.append(f"{folio}{side}-{prefix}{int(line):02d}")
    return refs


def range_contains(cell: str, target_ref: str) -> bool:
    refs = refs_in_text(cell)
    if not refs:
        return False
    target = line_key(target_ref)
    start = line_key(refs[0])
    end = line_key(refs[-1])
    return start <= target <= end


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


def find_g4_mapping(root: Path, target_ref: str) -> dict[str, str] | None:
    path = root / G4_OWNER
    if not path.is_file():
        return None
    in_current_mapping = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line == "### Current unit mapping":
            in_current_mapping = True
            continue
        if in_current_mapping and line.startswith("### "):
            break
        if not in_current_mapping or not line.startswith("| G4-"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 5:
            continue
        mapping = {
            "map_id": cells[0],
            "regii4_units": cells[1],
            "regii5_units": cells[2],
            "mapping_class": cells[3],
            "finding": cells[4],
        }
        if range_contains(mapping["regii5_units"], target_ref):
            return mapping
    return None


def load_regii4_mapped_rows(root: Path, units: str) -> tuple[list[str], list[dict[str, str]]]:
    refs = refs_in_text(units)
    if not refs:
        return [], []
    start = line_key(refs[0])
    end = line_key(refs[-1])
    owners: set[str] = set()
    selected: list[dict[str, str]] = []
    for path in sorted((root / REGII4_READING_DIR).glob("*.tsv")):
        _, rows = source_contract.read_tsv(path)
        for row in rows:
            ref = row.get("line_ref", "")
            try:
                key = line_key(ref)
            except PacketError:
                continue
            if start <= key <= end:
                owners.add(path.relative_to(root).as_posix())
                selected.append(compact_reading_row(row))
    selected.sort(key=lambda row: line_key(row["line_ref"]))
    return sorted(owners), selected


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

    evidence_rows = [
        row for row in cache["evidence_by_use"].get(PRINCIPAL_USE_ID, [])
        if row.get("status") == "active"
    ]
    if len(evidence_rows) != 1:
        raise PacketError(
            f"expected exactly one active evidence binding for {PRINCIPAL_USE_ID}, found {len(evidence_rows)}"
        )
    evidence = evidence_rows[0]
    file_row = cache["files"].get(evidence.get("file_id", ""))
    if not file_row:
        raise PacketError(f"evidence {evidence.get('evidence_id', '')} has no canonical File")

    source_id = use.get("source_id", "")
    source_row = cache["sources"].get(source_id)
    if not source_row:
        raise PacketError(f"principal Source {source_id} is unavailable")

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
        "research_function": use.get("research_function", ""),
        "relevant_locus": use.get("relevant_locus", ""),
        "source_id": source_id,
        "source_title": source_row.get("title", ""),
        "evidence_id": evidence.get("evidence_id", ""),
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
                "Inspect the target pixels and record only source-visible boundaries/features/uncertainties. "
                "Request an explore/adjudicate packet only after that observation exists."
            ),
        }
        packet["phase_boundary"] = {
            "current_reading_included": False,
            "candidate_sources_included": False,
            "note": "Current reading and candidate context are deliberately withheld during the blind pass.",
        }
        return packet

    if not observation or not observation.strip():
        raise PacketError(f"phase {phase!r} requires --blind-observation before candidate-bearing context is exposed")

    packet["blind_observation"] = frozen_observation(observation)
    packet["current_reading"] = compact_reading_row(reading_row)

    mapping = find_g4_mapping(root, line_ref)
    candidate_sources: list[dict] = []
    if mapping:
        mapping = dict(mapping)
        mapping["owner_path"] = G4_OWNER.as_posix()
        mapping["diplomatic_evidence_weight"] = 0
        mapping["role"] = "candidate_generation_only"
        owners["parallel_mapping"] = G4_OWNER.as_posix()

        mapping_is_secure = not mapping["mapping_class"].lower().startswith("no secure correspondence")
        mapping["candidate_text_exposed"] = mapping_is_secure
        if mapping_is_secure:
            parallel_owners, parallel_rows = load_regii4_mapped_rows(root, mapping["regii4_units"])
            candidate_sources.append(
                {
                    "type": "parallel_witness",
                    "role": "candidate_generation_only",
                    "diplomatic_evidence_weight": 0,
                    "mapping": mapping,
                    "reading_owners": parallel_owners,
                    "rows": parallel_rows,
                }
            )
        else:
            candidate_sources.append(
                {
                    "type": "parallel_witness_mapping",
                    "role": "non_secure_mapping_notice_only",
                    "diplomatic_evidence_weight": 0,
                    "mapping": mapping,
                    "reading_owners": [],
                    "rows": [],
                }
            )

    packet["candidate_sources"] = candidate_sources
    packet["phase_boundary"] = {
        "current_reading_included": True,
        "candidate_sources_included": True,
        "candidate_authority": "ZERO_DIPLOMATIC_EVIDENCE_WEIGHT",
        "note": (
            "Candidate material may suggest hypotheses only. It cannot change the Reg. Ii 5 reading "
            "without a separate return to and adjudication of the target graph."
        ),
    }

    if phase == "adjudicate":
        packet["adjudication"] = {
            "status": "PENDING_SOURCE_REINSPECTION",
            "required_action": (
                "Reinspect the target pixels and test each consequential candidate against the frozen "
                "blind observation and the target graph."
            ),
            "allowed_outcomes": ["promote", "retain current", "downgrade/reopen", "unresolved"],
            "compiler_can_decide": False,
            "compiler_can_persist_result": False,
        }
    return packet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compile a bounded read-only #139 evidence packet for one Reg. Ii 5 line."
    )
    parser.add_argument("--line-ref", required=True, help="Canonical Reg. Ii 5 line, e.g. 62r-L19")
    parser.add_argument(
        "--phase",
        choices=("blind", "explore", "adjudicate"),
        default="blind",
        help="blind withholds candidate-bearing context; later phases require --blind-observation",
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
