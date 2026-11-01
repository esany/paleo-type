#!/usr/bin/env python3
"""Rebuildable text-only Nr. 632 edition; source files remain canonical (#376)."""
from __future__ import annotations
import argparse
import csv
import html
import re
from collections import defaultdict
from pathlib import Path

PROJECT = Path("projects/ssta-20578-nr-632")
GUID = "edd69aa1-eae4-4970-a695-94aaeccd6724"
SOURCE_ID = "SSTA-ARCHIVIALE-EDD69AA1"
LINE_ID = re.compile(r"^(?:\d{4}[LR]|1781-CH-(?:FRONT|REVERSE))-[A-Z]\d{2}[LR]?$")
PAGE_ID = re.compile(r"^\d{4}[LR]$")
CHECK = re.compile(
    r"^Vergleich: (?P<page>\d{4}[LR](?:-\d+)?) \| Lesung [0-9a-f]{40}"
    r" \| Vorab [0-9a-f]{40} \| Abweichungen (?P<errors>\d+)"
    r" \| davon Vereinheitlichung (?P<normalized>\d+)"
    r" \| Urteil (?P<decision>passt|überarbeiten)$"
)
UNCLEAR = re.compile(r"(⟦[^⟧]*⟧|\[[^\]]*\])")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def table_cells(line: str) -> list[str]:
    if not line.startswith("|") or not line.rstrip().endswith("|"):
        return []
    return [part.strip() for part in line.strip().strip("|").split("|")]


def strip_code(value: str) -> str:
    backtick = chr(96)
    return value[1:-1] if len(value) >= 2 and value.startswith(backtick) and value.endswith(backtick) else value


def read_inventory(root: Path) -> list[dict[str, str]]:
    file = root / PROJECT / "research/content-document-function-inventory-2026-10-30.md"
    if not file.is_file():
        raise FileNotFoundError(f"canonical document inventory missing: {file}")
    out = []
    for line in file.read_text(encoding="utf-8").splitlines():
        cols = table_cells(line)
        if len(cols) != 5 or not re.match(r"^\d{4}", cols[0]):
            continue
        area, function, date, evidence, unresolved = cols
        slug = re.sub(r"[^a-z0-9]+", "-", area.lower()).strip("-")
        out.append({"anchor": f"doc-{slug}", "area": area, "function": function,
                    "date": date or "offen", "evidence": evidence,
                    "open": unresolved or "offen"})
    return out


def read_lines(root: Path) -> tuple[dict[str, tuple[str, str]], dict[str, bool]]:
    files = sorted((root / PROJECT / "research").glob("transcription-pilot-*.md"))
    if not files:
        raise FileNotFoundError("no canonical transcription-pilot-*.md sources")
    latest: dict[str, tuple[str, str]] = {}
    checked: dict[str, bool] = {}
    for file in files:
        for line in file.read_text(encoding="utf-8").splitlines():
            cols = table_cells(line)
            if len(cols) >= 3:
                key = strip_code(cols[0])
                reading = strip_code(cols[1])
                if LINE_ID.fullmatch(key):
                    latest[key] = (reading, " | ".join(cols[2:]))
            m = CHECK.fullmatch(line)
            if m and int(m["normalized"]) <= int(m["errors"]):
                checked[m["page"]] = m["decision"] == "passt" and int(m["errors"]) <= 1
    return latest, checked


def status_lines(root: Path) -> dict[str, str]:
    file = root / PROJECT / "STATUS.md"
    values = {}
    if file.is_file():
        for line in file.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^- \*\*(Forschungsstand|Nächste fachliche Aktion|Sperre):\*\* (.+)$", line)
            if m and m[1] not in values:
                values[m[1]] = m[2].replace(chr(96), "").replace("**", "")
    return values


def catalog_url(root: Path) -> str:
    file = root / "corpus/sources.tsv"
    if file.is_file():
        with file.open(encoding="utf-8", newline="") as fp:
            for row in csv.DictReader(fp, delimiter="\t"):
                if row.get("source_id") == SOURCE_ID:
                    value = row.get("digital_url", "")
                    if value.startswith("https://www.archiv.sachsen.de/"):
                        return value
    return ""


def line_page(line_id: str) -> str:
    if line_id.startswith("1781-CH-"):
        return line_id.rsplit("-", 1)[0]
    return line_id.split("-", 1)[0]


def sort_page(page: str) -> tuple[int, int, str]:
    if PAGE_ID.fullmatch(page):
        return (int(page[:4]), 0 if page.endswith("L") else 1, "")
    return (9999, 0, page)

