#!/usr/bin/env python3
"""Run the repository's shared deterministic full check used locally and by CI."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


class CheckFailure(RuntimeError):
    pass


def run_step(name: str, command: list[str]) -> str:
    print(f"== {name} ==")
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.stdout:
        print(completed.stdout.rstrip())
    if completed.stderr:
        print(completed.stderr.rstrip(), file=sys.stderr)
    if completed.returncode != 0:
        raise CheckFailure(f"{name} failed with exit code {completed.returncode}: {' '.join(command)}")
    return completed.stdout


def require(condition: bool, message: str, payload: Any | None = None) -> None:
    if condition:
        return
    detail = f"; payload={payload!r}" if payload is not None else ""
    raise CheckFailure(message + detail)


def check_project_contexts() -> None:
    for project in ("ega-reg-ii-3", "ega-reg-ii-4-bd-ii", "ega-reg-ii-5-knau"):
        output = run_step(
            f"compile fresh-process Project context: {project}",
            [PYTHON, "tools/project_context.py", "--project", project],
        )
        parsed = json.loads(output)
        require(isinstance(parsed, dict), f"Project context for {project} must be a JSON object")


def check_real_source_resolution() -> None:
    internal_output = run_step(
        "resolve real-data internal Project/Source fixture",
        [
            PYTHON,
            "tools/source_contract.py",
            "resolve",
            "--project",
            "ega-reg-ii-5-knau",
            "--source-id",
            "THHSTAW-EGA-REG-II-5-STAT-VIS-00000129",
            "--locus",
            "62r",
        ],
    )
    external_output = run_step(
        "resolve real-data external Project/Source fixture",
        [
            PYTHON,
            "tools/source_contract.py",
            "resolve",
            "--project",
            "ega-reg-ii-5-knau",
            "--source-id",
            "THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089",
        ],
    )
    internal = json.loads(internal_output)
    external = json.loads(external_output)

    require(internal.get("project_scope") == "internal", "internal fixture project_scope drift", internal)
    require(internal.get("structural_status") == "internal", "internal fixture structural_status drift", internal)
    require(internal.get("legacy_primary_file") is None, "internal fixture legacy primary file returned", internal)
    require(internal.get("research_functions") == ["principal"], "internal fixture research function drift", internal)
    require(len(internal.get("project_source_uses", [])) == 1, "internal fixture use count drift", internal)
    iuse = internal["project_source_uses"][0]
    require(iuse["use"].get("status") == "historical", "internal fixture use status drift", iuse)
    require(iuse["use"].get("relevant_locus") == "fol. 61v–63r", "internal fixture locus drift", iuse)
    require(iuse["evidence"][0]["evidence"].get("status") == "historical", "internal evidence status drift", iuse)
    require(
        iuse["evidence"][0]["file"].get("file_id") == "FILE-REG-II-5-00000129-EXCERPT",
        "internal evidence File drift",
        iuse,
    )

    require(external.get("project_scope") == "external", "external fixture project_scope drift", external)
    require(external.get("structural_status") == "external", "external fixture structural_status drift", external)
    require(external.get("research_functions") == ["textual-comparison"], "external fixture research function drift", external)
    require(len(external.get("project_source_uses", [])) == 1, "external fixture use count drift", external)
    euse = external["project_source_uses"][0]
    require(euse["use"].get("status") == "historical", "external fixture use status drift", euse)
    require(
        euse["evidence"][0]["file"].get("file_id") == "FILE-REG-II-4-II-00000089-EXPORT",
        "external evidence File drift",
        euse,
    )


def main() -> int:
    try:
        run_step("validate canonical Source/File/Project-use contract", [PYTHON, "tools/source_contract.py", "validate"])
        run_step("validate engineering contracts", [PYTHON, "tools/engineering.py", "validate"])
        run_step(
            "run deterministic and governance regressions",
            [PYTHON, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"],
        )
        check_project_contexts()
        check_real_source_resolution()
    except (CheckFailure, json.JSONDecodeError) as exc:
        print(f"FULL CHECK FAIL: {exc}", file=sys.stderr)
        return 1

    print("== assurance boundary ==")
    print("PASS: deterministic contracts, regressions, fresh-process contexts and real-data resolver fixtures passed.")
    print("NON-CLAIM: this does not establish manuscript truth, specialist validity, Human acceptance or release authority.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
