#!/usr/bin/env python3
"""Check a bounded work-return claim against current Project owners and Git evidence.

Read-only and deliberately narrow: no worker dispatch, priority selection, document
reading, scientific acceptance, or new persistent status. Report claims are inputs,
not authority; current project.yml/STATUS.md and commit bytes are checked afresh.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

from source_contract import read_simple_yaml_scalars

SHA = re.compile(r"[0-9a-f]{40}\Z")
PROJECT = re.compile(r"[a-z0-9][a-z0-9-]*\Z")


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )


def _owner_change(root: Path, project_id: str, report: dict) -> bool:
    """Detect a committed Project research-owner change between the two claimed commits."""
    before = report.get("baseline_commit")
    after = report.get("result_commit")
    owner = report.get("research_owner")
    prefix = f"projects/{project_id}/research/"
    if not all(isinstance(x, str) for x in (before, after, owner)):
        return False
    if not SHA.fullmatch(before) or not SHA.fullmatch(after) or before == after:
        return False
    if not owner.startswith(prefix):
        return False
    path = Path(owner)
    if path.is_absolute() or ".." in path.parts or path.as_posix() != owner:
        return False
    changed = _git(root, "diff", "--name-only", before, after, "--", owner)
    if changed.returncode or owner not in changed.stdout.decode().splitlines():
        return False
    committed = _git(root, "show", f"{after}:{owner}")
    if committed.returncode:
        return False
    previous = _git(root, "show", f"{before}:{owner}")
    return previous.returncode != 0 or previous.stdout != committed.stdout


def evaluate(root: Path, project_id: str, report: dict) -> tuple[int, dict]:
    findings: list[str] = []
    failures: list[str] = []
    if not PROJECT.fullmatch(project_id):
        return 1, {"result": "Halt: ungueltige Project-ID", "owner_change": False,
                   "findings": ["ungueltige Project-ID"]}
    project_dir = root / "projects" / project_id
    project_file = project_dir / "project.yml"
    if not project_file.is_file():
        return 1, {"result": "Halt: Project-Owner fehlt", "owner_change": False,
                   "findings": ["project.yml nicht vorhanden"]}

    definition = read_simple_yaml_scalars(project_file)
    status_name = definition.get("canonical_status_file", "")
    rel = Path(status_name)
    if not status_name or rel.is_absolute() or ".." in rel.parts or len(rel.parts) != 1:
        return 1, {"result": "Halt: STATUS-Owner ungueltig", "owner_change": False,
                   "findings": ["canonical_status_file nicht aufloesbar"]}
    status_file = project_dir / rel
    if not status_file.is_file():
        return 1, {"result": "Halt: STATUS-Owner fehlt", "owner_change": False,
                   "findings": ["STATUS.md nicht vorhanden"]}
    status = status_file.read_text(encoding="utf-8")
    baseline = report.get("baseline_commit")
    if baseline is not None:
        if not isinstance(baseline, str) or not SHA.fullmatch(baseline):
            return 1, {"result": "Halt: ungueltiger Basiskommit", "owner_change": False,
                       "findings": ["baseline_commit ungueltig"]}
        base_status = _git(root, "show", f"{baseline}:{status_file.relative_to(root).as_posix()}")
        if base_status.returncode:
            return 1, {"result": "Halt: Basis-STATUS nicht lesbar", "owner_change": False,
                       "findings": ["STATUS am baseline_commit fehlt"]}
        recorded_bytes = base_status.stdout
    else:
        recorded_bytes = status_file.read_bytes()
    current_digest = hashlib.sha256(recorded_bytes).hexdigest()
    result_commit = report.get("result_commit")
    if result_commit is not None:
        if not isinstance(result_commit, str) or not SHA.fullmatch(result_commit):
            return 1, {"result": "Halt: ungueltiger Ergebniskommit", "owner_change": False,
                       "findings": ["result_commit ungueltig"]}
        result_status = _git(root, "show", f"{result_commit}:{status_file.relative_to(root).as_posix()}")
        if result_status.returncode:
            return 1, {"result": "Halt: Ergebnis-STATUS nicht lesbar", "owner_change": False,
                       "findings": ["STATUS am result_commit fehlt"]}
        anchor_status = result_status.stdout.decode("utf-8")
    else:
        anchor_status = status
    if report.get("recorded_status_sha256") != current_digest:
        findings.append("Project-Owner geaendert: statischen Auftrag nicht als aktuell behandeln; frischer Abgleich erforderlich")
        failures.append("stale-owner")

    anchor = report.get("continuation_anchor")
    stop_reason = report.get("stop_reason")
    stop_evidence = report.get("stop_evidence")
    # A continuation must have been written by this block, not merely found again.
    has_continuation = (
        isinstance(anchor, str) and bool(anchor.strip())
        and baseline is not None and result_commit is not None
        and anchor in anchor_status.splitlines()
        and anchor not in recorded_bytes.decode("utf-8").splitlines()
    )
    has_stop = isinstance(stop_reason, str) and bool(stop_reason.strip()) and (
        isinstance(stop_evidence, str) and bool(stop_evidence.strip())
    )
    if anchor and not has_continuation:
        findings.append("Fortsetzung nicht belegt: Verweis steht nicht im aktuellen STATUS-Owner")
        failures.append("continuation-not-verified")
    if stop_reason and not has_stop:
        findings.append("Halt ohne pruefbare Begruendung/Belegangabe")
        failures.append("stop-not-evidenced")
    if has_continuation and has_stop:
        findings.append("Fortsetzung und Halt gleichzeitig behauptet; Rueckgabe klaeren")
        failures.append("ambiguous-return")

    ended = report.get("run_status") == "completed" or report.get("local_pass") is True
    if ended and not (has_continuation or has_stop):
        findings.append("Fortsetzung nicht belegt und kein Halt mit Grund nach lokalem PASS/Arbeitsende")
        failures.append("missing-return")

    delta = _owner_change(root, project_id, report) if report.get("run_status") == "completed" else False
    if report.get("run_status") == "completed" and not delta:
        findings.append("keine Änderung im Forschungs-Owner: completed ist nur ein Laufzeitstatus; kein geaenderter Forschungs-Owner-Commit rueckgelesen")
        if not has_stop:
            failures.append("no-research-delta")

    if failures:
        result = "Halt: Rueckgabe/Owner-Widerspruch nicht geklaert"
    elif has_stop:
        result = "Halt mit Grund; kein wissenschaftlicher Erfolg behauptet"
    elif delta:
        result = "Änderung im Forschungs-Owner gespeichert; Lesegewinn nicht geprüft"
    else:
        result = "Kein Abschluss oder Forschungsfortschritt bestaetigt"
    return (1 if failures else 0), {
        "result": result,
        "owner_change": delta,
        "findings": findings,
        "project_status_owner": str(status_file.relative_to(root)),
        "claim_ceiling": "Only current owner/readback and Git file-change evidence; no manuscript truth, live host access or scientific acceptance.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate work-return evidence; no dispatch or scholarly judgement.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--project", required=True)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    try:
        rc, answer = evaluate(args.root.resolve(), args.project, json.loads(args.report.read_text(encoding="utf-8")))
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        rc, answer = 1, {"result": "Halt: unlesbare Eingabe", "owner_change": False, "findings": [str(exc)]}
    print(json.dumps(answer, ensure_ascii=False, indent=2))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
