#!/usr/bin/env python3
"""Verify blind-review metadata and immutable Git evidence, not handwriting.

Issue #368 P1, amended by #371: no chronological prerequisite between the
independent review and source-reading commits.  The reading commit must exist,
change the named canonical research owner, and be cited verbatim in a
machine-readable comparison row.  This cannot establish that a chat really
opened one text before another; the human declaration 'Blind: ja' remains a
declared provenance claim, not technically independently provable blindness.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

SHA = re.compile(r"[0-9a-f]{40}\Z")
PAGE = re.compile(r"\d{4}[LR]\Z")
HEADER = re.compile(r"^## (\d{4}[LR])\s*$", re.M)
COMPARISON = re.compile(
    r"^Vergleich: (?P<page>\d{4}[LR]) \| "
    r"Lesung (?P<reading>[0-9a-f]{40}) \| "
    r"Vorab (?P<review>[0-9a-f]{40}) \| "
    r"Abweichungen (?P<errors>\d+) \| "
    r"davon Vereinheitlichung (?P<normalized>\d+) \| "
    r"Urteil (?P<judgement>passt|überarbeiten)$"
)
REVIEW_LABELS = ("Datum:", "Leser:", "Bildquelle:", "Blind:")


def git(root: Path, *args: str) -> tuple[bool, str]:
    result = subprocess.run(
        ["git", "-C", str(root), *args], text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    return result.returncode == 0, result.stdout


def safe_project_path(root: Path, name: str) -> Path:
    path = Path(name)
    if path.is_absolute() or ".." in path.parts or not name.startswith("projects/"):
        raise ValueError("owner/review must be a relative Project path")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root):
        raise ValueError("Project path escapes repository")
    return resolved


def review_sections(contents: str, findings: list[str], *, all_sections: bool = True) -> dict[str, str]:
    matches = list(HEADER.finditer(contents))
    result: dict[str, str] = {}
    for i, match in enumerate(matches):
        page = match.group(1)
        section = contents[match.end():matches[i + 1].start() if i + 1 < len(matches) else len(contents)]
        if page in result:
            # Subsequent correction sections are permitted in general, but ambiguity
            # about which one to compare is not. Use distinct names/ref and trace.
            findings.append(f"duplicate review heading: {page}")
        result[page] = section
        if all_sections:
            for label in REVIEW_LABELS:
                if not re.search(r"^-\s*" + re.escape(label) + r"\s*\S+", section, re.M):
                    findings.append(f"{page}: missing {label} in review section")
            if not re.search(r"^-\s*Blind:\s*ja(?:[\s;,.]|$)", section, re.M):
                findings.append(f"{page}: reviewer did not declare Blind: ja")
            has_numbered_line = bool(re.search(
                r"^-\s*(?:.*\bZ\.\s*\d+\b.*):\s*.+", section, re.M
            ))
            # Some photographed views show only bleed-through and therefore
            # have no independently transcribable physical lines. Do not force
            # fabricated graphemes or numbered lines to satisfy a format check.
            # This validates an explicit ZERO observation, not a 2-3-line PASS.
            zero_line_observation = bool(
                re.search(r"^-\s*Stichprobe:\s*0(?:\s|$)", section, re.M)
                and re.search(r"^-\s*Bildbefund[^:]*:\s*\S+", section, re.M)
            )
            if not (has_numbered_line or zero_line_observation):
                findings.append(f"{page}: no numbered physical-line locus or evidenced zero-line observation")
    return result


def owner_changed_at_reading(root: Path, sha: str, owner_path: str) -> bool:
    if not SHA.fullmatch(sha):
        return False
    ok, _ = git(root, "cat-file", "-e", sha + "^{commit}")
    if not ok:
        return False
    # The claimed reading SHA must itself change the named owner file, not
    # merely point to an existing tree or a review-only commit.
    ok, paths = git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", sha)
    if not ok or owner_path not in paths.splitlines():
        return False
    ok, _ = git(root, "show", f"{sha}:{owner_path}")
    return ok


def run(root: Path, owner_path: str, review_path: str, review_ref: str) -> tuple[int, dict]:
    findings: list[str] = []
    try:
        safe_project_path(root, owner_path)
        safe_project_path(root, review_path)
    except ValueError as err:
        return 1, {"result": "FAIL", "checked": 0, "findings": [str(err)]}
    owner_file = root / owner_path
    if not owner_file.is_file():
        return 1, {"result": "FAIL", "checked": 0, "findings": ["research owner missing"]}
    ok, latest = git(root, "show", f"{review_ref}:{review_path}")
    if not ok:
        return 1, {"result": "FAIL", "checked": 0, "findings": ["review ref/file missing"]}
    active = review_sections(latest, findings)
    checked = 0
    for line in owner_file.read_text(encoding="utf-8").splitlines():
        if not line.startswith("Vergleich:"):
            continue
        checked += 1
        match = COMPARISON.fullmatch(line)
        if match is None:
            findings.append("malformed comparison line (expected 6 literal fields)")
            continue
        data = match.groupdict()
        page, reading, pre = data["page"], data["reading"], data["review"]
        n, normalized = int(data["errors"]), int(data["normalized"])
        if normalized > n:
            findings.append(f"{page}: normalized count exceeds errors")
        if data["judgement"] == "passt" and n > 1:
            findings.append(f"{page}: 'passt' contradicts >1 unmarked errors")
        if page not in active:
            findings.append(f"{page}: no review section in active review branch")
        if not owner_changed_at_reading(root, reading, owner_path):
            findings.append(f"{page}: reading commit absent or does not change research owner")
        ok, recorded = git(root, "show", f"{pre}:{review_path}")
        if not ok:
            findings.append(f"{page}: cited review commit/file missing")
            continue
        historical = review_sections(recorded, [], all_sections=False)
        if page not in historical or not re.search(
            r"^-\s*Blind:\s*ja(?:[\s;,.]|$)", historical[page], re.M
        ):
            findings.append(f"{page}: cited review snapshot lacks a Blind: ja section")
    return (1 if findings else 0), {
        "result": "FAIL" if findings else "PASS",
        "checked": checked,
        "review_sections": len(active),
        "findings": findings,
        "claim_ceiling": "Git commit/format and declared blindness only; no source reading accepted.",
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--research-owner", required=True)
    p.add_argument("--review-path", required=True)
    p.add_argument("--review-ref", required=True)
    args = p.parse_args()
    rc, result = run(args.root.resolve(), args.research_owner, args.review_path, args.review_ref)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
