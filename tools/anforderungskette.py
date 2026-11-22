#!/usr/bin/env python3
"""Anforderungskette: Intent → Bedürfnis → Pain → Anforderung → Prüfung.

Prüft die Kette deterministisch und erzeugt daraus die Leseansicht
``requirements/kette.md``. Quellen sind genau zwei Tabellen:

- ``requirements/beduerfnisse.tsv``: Intent, Rahmen, Bedürfnisse und Pains,
  jeweils mit wörtlichem O-Ton und Fundstelle;
- ``requirements/domain-requirements.tsv``: die Anforderungen mit den
  Kettenspalten ``kurz``, ``need_ids``, ``applies_from``, ``verified_by``,
  ``depends_on`` und ``overlaps``.

Grenze: Das Werkzeug prüft, ob die Kette vollständig und widerspruchsfrei
verknüpft ist, ob jeder O-Ton wörtlich an seiner Fundstelle steht und ob jeder
genannte Test existiert. Es prüft nicht, ob ein Test die Anforderung inhaltlich
ganz abdeckt, ob eine Ableitung den O-Ton richtig deutet oder ob eine
Anforderung fachlich erfüllt ist.

Aufruf:
  python3 tools/anforderungskette.py pruefen     # Kette und Ansicht prüfen
  python3 tools/anforderungskette.py schreiben   # Ansicht neu erzeugen
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

NEEDS_PATH = Path("requirements/beduerfnisse.tsv")
REQS_PATH = Path("requirements/domain-requirements.tsv")
VIEW_PATH = Path("requirements/kette.md")

NEED_COLUMNS = ["id", "art", "gehoert_zu", "aussage", "status", "o_ton", "fundstelle"]
CHAIN_COLUMNS = ["kurz", "need_ids", "applies_from", "verified_by", "depends_on", "overlaps"]
ART_BY_PREFIX = {"I": "Intent", "R": "Rahmen", "B": "Bedürfnis", "P": "Pain"}
PARENT_ART = {"Intent": None, "Rahmen": None, "Bedürfnis": "Intent", "Pain": "Bedürfnis"}
STATUS = {"wörtlich", "abgeleitet", "Hypothese"}
NEED_ID = re.compile(r"(?P<prefix>[IRBP])-\d{2}\Z")
REQ_ID = re.compile(r"REQ-[A-Z]+-\d{3}\Z")
STAGES = ["immer", "G1", "G2", "G3", "G4", "G5", "G6"]
TRIGGER = re.compile(r"Auslöser: \S.*\Z")
JUDGEMENTS = {"Fachurteil": "Fachurteil", "Gebrauch": "Prüfung im Gebrauch"}
TEST_REF = re.compile(r"(?P<path>tests/test_[a-z0-9_]+\.py)::(?P<name>test_[A-Za-z0-9_]+)\Z")
QUOTE_SEPARATOR = " || "
UNQUALIFIED_SUPPORT = re.compile(r"(adequate|strong)\Z")
O_TON_PATH = Path("docs/o-toene.md")
DATE_HEADING = re.compile(r"^## (?P<date>\d{2}\.\d{2}\.\d{4})\b")
BOLD_LABEL = re.compile(r"^\*\*(?P<label>[^*]+)\*\*")
ANCHOR_PART = re.compile(r"(?:(?P<date>\d{2}\.\d{2}\.\d{4}) )?(?P<label>\S.*)")


# ---------------------------------------------------------------- Einlesen

def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
        return list(reader.fieldnames or []), list(reader)


def split(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def normalized(text: str) -> str:
    lines = [re.sub(r"^\s*>\s?", "", line) for line in text.splitlines()]
    return " ".join(" ".join(lines).split())


def stage_of(applies: str) -> str:
    return applies if applies in STAGES else "Auslöser"


def stage_rank(applies: str) -> int:
    return STAGES.index(applies) if applies in STAGES else len(STAGES)


def test_refs(verified: str) -> list[str]:
    return [item for item in split(verified) if TEST_REF.fullmatch(item)]


# ---------------------------------------------------------------- Prüfen

def validate(root: Path) -> list[str]:
    findings: list[str] = []
    need_fields, needs = read_tsv(root / NEEDS_PATH)
    if need_fields != NEED_COLUMNS:
        return [f"{NEEDS_PATH}: Spalten müssen genau {NEED_COLUMNS} sein"]
    by_id: dict[str, dict[str, str]] = {}
    for row in needs:
        nid = row["id"]
        match = NEED_ID.fullmatch(nid)
        if match is None:
            findings.append(f"{nid!r}: ungültige ID (erwartet I-/R-/B-/P- mit zwei Ziffern)")
            continue
        if nid in by_id:
            findings.append(f"{nid}: doppelte ID")
        by_id[nid] = row
        if row["art"] != ART_BY_PREFIX[match["prefix"]]:
            findings.append(f"{nid}: Art {row['art']!r} passt nicht zur ID")
        if row["status"] not in STATUS:
            findings.append(f"{nid}: Status {row['status']!r} ist nicht wörtlich, abgeleitet oder Hypothese")
        if not row["aussage"].strip():
            findings.append(f"{nid}: Aussage fehlt")
        findings.extend(check_quote(root, nid, row))
    for nid, row in by_id.items():
        expected = PARENT_ART.get(row["art"])
        parents = split(row["gehoert_zu"])
        if expected is None and parents:
            findings.append(f"{nid}: {row['art']} gehört zu nichts, steht aber bei {parents}")
        if expected is not None and not parents:
            findings.append(f"{nid}: {row['art']} muss zu einem {expected} gehören")
        for parent in parents:
            if parent not in by_id:
                findings.append(f"{nid}: unbekannte ID {parent} in gehoert_zu")
            elif by_id[parent]["art"] != expected:
                findings.append(f"{nid}: {row['art']} muss zu einem {expected} gehören, nicht zu {parent}")

    req_fields, reqs = read_tsv(root / REQS_PATH)
    missing = [c for c in CHAIN_COLUMNS if c not in req_fields]
    if missing:
        return findings + [f"{REQS_PATH}: Kettenspalten fehlen: {missing}"]
    req_ids = [r["requirement_id"] for r in reqs]
    known = set(req_ids)
    for rid in sorted({r for r in req_ids if req_ids.count(r) > 1}):
        findings.append(f"{rid}: doppelte Anforderung")
    for row in reqs:
        findings.extend(check_requirement(root, row, by_id, known))
    findings.extend(check_relations(reqs))
    return findings


def o_ton_sections(text: str) -> dict[tuple[str, str], dict[str, object]]:
    """Abschnitte von docs/o-toene.md: (Datum, Fettüberschrift) → nur die Zitatzeilen.

    Gezählt werden nur Zeilen, die mit ``>`` beginnen; Überschriften und
    Anmerkungen der KI zählen nicht als O-Ton.
    """
    sections: dict[tuple[str, str], dict[str, object]] = {}
    date = ""
    current: dict[str, object] | None = None
    for line in text.splitlines():
        heading = DATE_HEADING.match(line)
        if heading:
            date, current = heading["date"], None
            continue
        label = BOLD_LABEL.match(line)
        if label and date:
            current = {"quotes": [], "button": "Antwortknopf" in line}
            sections[(date, label["label"].strip())] = current
            continue
        if current is not None and line.lstrip().startswith(">"):
            current["quotes"].append(re.sub(r"^\s*>\s?", "", line))
    return sections


def resolve_anchor(anchor: str, sections: dict[tuple[str, str], dict[str, object]]) -> tuple[list[dict[str, object]], list[str]]:
    """``Datum Überschrift[; [Datum ]Überschrift]``; ohne Datum gilt das vorige."""
    found, problems, date = [], [], ""
    for part in [p.strip() for p in anchor.split(";") if p.strip()]:
        match = ANCHOR_PART.fullmatch(part)
        if match is None:
            problems.append(f"Abschnitt {part!r} ist nicht lesbar")
            continue
        date = match["date"] or date
        hits = [key for key in sections if key[0] == date and key[1].startswith(match["label"])]
        if len(hits) != 1:
            problems.append(f"Abschnitt {part!r} {'gibt es nicht' if not hits else 'ist mehrdeutig'}")
            continue
        if sections[hits[0]]["button"]:
            problems.append(f"Abschnitt {part!r} ist eine Knopfwahl, kein eigener Wortlaut")
            continue
        found.append(sections[hits[0]])
    return found, problems


def check_quote(root: Path, nid: str, row: dict[str, str]) -> list[str]:
    path_text, _, anchor = row["fundstelle"].partition("#")
    if path_text.strip() != O_TON_PATH.as_posix():
        return [f"{nid}: Fundstelle muss {O_TON_PATH} sein, dort stehen die O-Töne"]
    target = root / O_TON_PATH
    if not target.is_file():
        return [f"{nid}: {O_TON_PATH} gibt es nicht"]
    if not anchor.strip():
        return [f"{nid}: Fundstelle nennt keinen Abschnitt (Datum und Überschrift nach #)"]
    found, problems = resolve_anchor(anchor, o_ton_sections(target.read_text(encoding="utf-8")))
    out = [f"{nid}: {problem}" for problem in problems]
    quotes = [q.strip() for q in row["o_ton"].split(QUOTE_SEPARATOR)]
    if not any(quotes):
        return out + [f"{nid}: O-Ton fehlt"]
    texts = [normalized("\n".join(section["quotes"])) for section in found]
    for quote in quotes:
        pattern = re.compile(r"(?<!\w)" + re.escape(normalized(quote)) + r"(?!\w)") if quote else None
        if pattern is None or not any(pattern.search(text) for text in texts):
            out.append(f"{nid}: O-Ton steht nicht wörtlich in einem Zitat des genannten Abschnitts: {quote!r}")
    return out


def check_requirement(root: Path, row: dict[str, str], needs: dict[str, dict[str, str]], known: set[str]) -> list[str]:
    rid = row["requirement_id"]
    out: list[str] = []
    if not REQ_ID.fullmatch(rid):
        out.append(f"{rid!r}: ungültige Anforderungs-ID")
    if not row["kurz"].strip():
        out.append(f"{rid}: deutsche Kurzbezeichnung fehlt")
    need_ids = split(row["need_ids"])
    if not need_ids:
        out.append(f"{rid}: dient keinem Bedürfnis und ist nicht als Fachanspruch („fach“) markiert")
    elif "fach" in need_ids and len(need_ids) > 1:
        out.append(f"{rid}: „fach“ steht allein; sonst die Bedürfnisse nennen")
    else:
        for nid in need_ids:
            if nid != "fach" and nid not in needs:
                out.append(f"{rid}: unbekanntes Bedürfnis {nid}")
    applies = row["applies_from"].strip()
    if applies not in STAGES and not TRIGGER.fullmatch(applies):
        out.append(f"{rid}: „gilt ab“ muss immer, G1–G6 oder „Auslöser: …“ sein, nicht {applies!r}")
    items = split(row["verified_by"])
    if not items:
        out.append(f"{rid}: keine Angabe, was die Anforderung prüft (Test, Fachurteil, Gebrauch oder keine)")
    tests = []
    for item in items:
        if item in JUDGEMENTS or item == "keine":
            continue
        match = TEST_REF.fullmatch(item)
        if match is None:
            out.append(f"{rid}: unbekannte Prüfangabe {item!r}")
            continue
        tests.append(item)
        test_file = root / match["path"]
        if not test_file.is_file():
            out.append(f"{rid}: Testdatei {match['path']} gibt es nicht")
        elif not re.search(rf"^\s*def {re.escape(match['name'])}\(", test_file.read_text(encoding="utf-8"), re.M):
            out.append(f"{rid}: Test {match['name']} steht nicht in {match['path']}")
    if "keine" in items and tests:
        out.append(f"{rid}: „keine“ widerspricht den genannten Tests")
    for column in ("depends_on", "overlaps"):
        for other in split(row[column]):
            if other == rid:
                out.append(f"{rid}: verweist in {column} auf sich selbst")
            elif other not in known:
                out.append(f"{rid}: unbekannte Anforderung {other} in {column}")
    return out


def check_relations(reqs: list[dict[str, str]]) -> list[str]:
    out: list[str] = []
    overlaps = {r["requirement_id"]: set(split(r["overlaps"])) for r in reqs}
    for rid, others in overlaps.items():
        for other in sorted(others):
            if other in overlaps and rid not in overlaps[other]:
                out.append(f"{rid}: Überschneidung mit {other} ist nicht beidseitig eingetragen")
    graph = {r["requirement_id"]: [d for d in split(r["depends_on"]) if d != r["requirement_id"]] for r in reqs}
    applies = {r["requirement_id"]: r["applies_from"].strip() for r in reqs}
    for rid, deps in graph.items():
        for dep in deps:
            if dep in applies and stage_rank(applies[dep]) > stage_rank(applies[rid]):
                out.append(f"{rid} gilt ab {applies[rid]}, braucht aber {dep}, das erst ab {applies[dep]} gilt")
    state: dict[str, int] = {}

    def visit(node: str, path: list[str]) -> None:
        state[node] = 1
        for nxt in graph.get(node, []):
            if state.get(nxt) == 1:
                out.append("Abhängigkeit im Kreis: " + " → ".join(path[path.index(nxt):] + [nxt]))
            elif nxt in graph and nxt not in state:
                visit(nxt, path + [nxt])
        state[node] = 2

    for node in graph:
        if node not in state:
            visit(node, [node])
    return out


# ---------------------------------------------------------------- Ansicht

def short(rid: str) -> str:
    return rid.removeprefix("REQ-")


def check_label(verified: str) -> str:
    items = split(verified)
    parts = []
    tests = test_refs(verified)
    if tests:
        parts.append(f"Test genannt ({len(tests)})")
    elif "keine" in items:
        parts.append("**kein Test bekannt**")
    parts.extend(JUDGEMENTS[i] for i in items if i in JUDGEMENTS)
    return ", ".join(parts)


def has_test(row: dict[str, str]) -> bool:
    return bool(test_refs(row["verified_by"]))


def untested_gap(row: dict[str, str]) -> bool:
    """Prüfbar, aber kein Test bekannt."""
    return not has_test(row) and "keine" in split(row["verified_by"])


def judgement_only(row: dict[str, str]) -> bool:
    return not has_test(row) and not untested_gap(row)


def components(reqs: list[dict[str, str]]) -> list[list[str]]:
    seen: set[str] = set()
    groups = []
    links = {r["requirement_id"]: set(split(r["overlaps"])) for r in reqs}
    for rid in links:
        if rid in seen or not links[rid]:
            continue
        stack, group = [rid], []
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            group.append(node)
            stack.extend(links.get(node, ()))
        groups.append(sorted(group))
    return groups


def render(root: Path) -> str:
    _, needs = read_tsv(root / NEEDS_PATH)
    _, reqs = read_tsv(root / REQS_PATH)
    by_req = {r["requirement_id"]: r for r in reqs}
    need_by_id = {n["id"]: n for n in needs}
    serves: dict[str, list[str]] = defaultdict(list)
    for r in reqs:
        for nid in split(r["need_ids"]):
            serves[nid].append(r["requirement_id"])

    lines = [
        "# Anforderungskette",
        "",
        "Erzeugt von `tools/anforderungskette.py` aus `requirements/beduerfnisse.tsv` und "
        "`requirements/domain-requirements.tsv`. Bitte nicht von Hand ändern; nach jeder Änderung an den beiden "
        "Tabellen `python3 tools/anforderungskette.py schreiben` ausführen. Die Prüfung schlägt fehl, wenn diese "
        "Ansicht veraltet ist.",
        "",
        "**Was hier geprüft ist:** dass jeder O-Ton als ganze Wörter in einem Zitat des genannten Abschnitts von "
        "`docs/o-toene.md` steht und keine Knopfwahl ist, dass jede Anforderung einem Bedürfnis, Pain, einer "
        "Rahmenbedingung oder ausdrücklich nur einem Fach dient, dass jede eine Prüfangabe hat, dass jeder genannte "
        "Test existiert und dass keine Anforderung etwas braucht, das erst später gilt. **Was nicht geprüft ist:** "
        "ob ein genannter Test die Anforderung inhaltlich abdeckt, ob eine Ableitung den O-Ton richtig deutet, ob "
        "eine Anforderung fachlich erfüllt ist.",
        "",
        "**Status der Zuordnungen:** Welchem Bedürfnis eine Anforderung dient, ab wann sie gilt, welcher Test sie "
        "betrifft, was sie zuerst braucht und womit sie sich überschneidet, hat Claude am 22.11.2026 aus "
        "Anforderungstext, Testnamen und Werkzeugbeschreibungen abgeleitet. Der Eigentümer hat es nicht bestätigt. "
        "Eine unabhängige Zweitprüfung fand Fehlzuordnungen; sie sind korrigiert, weitere sind möglich. Die "
        "Kurzbezeichnungen sind Übersetzungen und lassen Einschränkungen wie „folgenreich“ oder „wo machbar“ weg; "
        "maßgeblich ist der englische Wortlaut in der Tabelle.",
        "",
        "**Prüfangaben:** *Test genannt (n)*: n Tests im Repo betreffen nach Einschätzung der KI einen Teil davon. "
        "*Fachurteil*: nur ein Urteil im jeweiligen Fach (Wissenschaft, Edition, Softwaretechnik) kann es "
        "beurteilen. *Prüfung im Gebrauch*: nur du kannst es beim Benutzen beurteilen. Ob solche Urteile "
        "stattgefunden haben, steht nicht in der Tabelle. ***kein Test bekannt***: prüfbar, aber kein Test im Repo "
        "ist bekannt, der es prüft.",
        "",
        "## Auf einen Blick",
        "",
        "| Gilt ab | Anforderungen | Test genannt | nur Urteil | kein Test bekannt |",
        "|---|---:|---:|---:|---:|",
    ]
    order = STAGES + ["Auslöser"]

    def counts(rows: list[dict[str, str]]) -> str:
        return f"{sum(map(has_test, rows))} | {sum(map(judgement_only, rows))} | {sum(map(untested_gap, rows))}"

    for stage in order:
        rows = [r for r in reqs if stage_of(r["applies_from"]) == stage]
        if rows:
            label = "immer" if stage == "immer" else ("Auslöser (bei Bedarf)" if stage == "Auslöser" else stage)
            lines.append(f"| {label} | {len(rows)} | {counts(rows)} |")
    lines.append(f"| **alle** | **{len(reqs)}** | {counts(reqs)} |")
    claimed = [r for r in reqs if UNQUALIFIED_SUPPORT.fullmatch(r["current_support"].strip()) and not has_test(r)]
    lines += [
        "",
        f"Bei **{len(claimed)}** Anforderungen lautet die Selbstbewertung in der Spalte `current_support` ohne "
        "Einschränkung „adequate“ oder „strong“, aber kein Test ist genannt: "
        + ", ".join(short(r["requirement_id"]) for r in claimed) + ". Die Selbstbewertung stammt aus den Fachaudits "
        "vom August und September 2026 und ist eine Auskunft, kein Beleg.",
        "",
        "## Intent und Rahmen",
        "",
    ]
    for n in needs:
        if n["art"] in ("Intent", "Rahmen"):
            served = "; ".join(f"{short(rid)} {by_req[rid]['kurz']}" for rid in serves[n["id"]])
            lines.append(f"- **{n['id']}** {n['aussage']} ({n['status']}; O-Ton: „{first_quote(n)}“)"
                         + (f" Dient: {served}." if served else ""))
    lines += ["", "## Bedürfnisse, Pains und ihre Anforderungen", ""]
    for n in needs:
        if n["art"] != "Bedürfnis":
            continue
        pains = [p for p in needs if p["art"] == "Pain" and n["id"] in split(p["gehoert_zu"])]
        linked = list(dict.fromkeys(serves[n["id"]] + [rid for p in pains for rid in serves[p["id"]]]))
        lines += [f"### {n['id']} {n['aussage']}", "", f"O-Ton ({n['status']}): „{first_quote(n)}“", ""]
        for p in pains:
            lines.append(f"- Pain **{p['id']}** {p['aussage']} (O-Ton: „{first_quote(p)}“)")
        if pains:
            lines.append("")
        if not linked:
            lines += ["**Keine Anforderung dient diesem Bedürfnis.** Das ist eine Lücke.", ""]
            continue
        lines += ["| Anforderung | Kurz | gilt ab | Prüfung |", "|---|---|---|---|"]
        for rid in sorted(linked, key=lambda x: (order.index(stage_of(by_req[x]["applies_from"])), x)):
            r = by_req[rid]
            lines.append(f"| {short(rid)} | {r['kurz']} | {r['applies_from']} | {check_label(r['verified_by'])} |")
        lines.append("")

    lines += ["## Lücken nach Stufe", "", "Prüfbare Anforderungen ohne bekannten Test, geordnet danach, ab wann sie gelten.", ""]
    lines += ["| gilt ab | Anforderung | Kurz | dient | braucht zuerst |", "|---|---|---|---|---|"]
    for stage in order:
        for r in reqs:
            if stage_of(r["applies_from"]) == stage and untested_gap(r):
                needs_text = ", ".join(split(r["need_ids"]))
                deps = ", ".join(short(d) for d in split(r["depends_on"]))
                lines.append(f"| {r['applies_from']} | {short(r['requirement_id'])} | {r['kurz']} | {needs_text} | {deps} |")
    unserved = [n for n in needs if n["art"] == "Bedürfnis" and not (
        serves[n["id"]] or any(serves[p["id"]] for p in needs if p["art"] == "Pain" and n["id"] in split(p["gehoert_zu"])))]
    lines += ["", "## Bedürfnisse ohne Anforderung", ""]
    lines += [f"- **{n['id']}** {n['aussage']}" for n in unserved] or ["Keine."]
    fach = [r for r in reqs if split(r["need_ids"]) == ["fach"]]
    lines += ["", "## Reiner Fachanspruch", "", "Anforderungen, die nur ein Fach begründet, ohne eins deiner Bedürfnisse.", ""]
    lines += [f"- {short(r['requirement_id'])} {r['kurz']}" for r in fach] or ["Keine."]
    lines += ["", "## Überschneidungen", "", "Diese Anforderungen sagen aus verschiedenen Fächern fast dasselbe. "
              "Sie bleiben getrennt, weil jedes Fach seine eigene Begründung hat; umgesetzt werden sie gemeinsam.", ""]
    for group in components(reqs):
        lines.append("- " + "; ".join(f"{short(g)} {by_req[g]['kurz']}" for g in group))
    referenced = {TEST_REF.fullmatch(t)["path"] for r in reqs for t in test_refs(r["verified_by"])}
    present = sorted(p.relative_to(root).as_posix() for p in (root / "tests").glob("test_*.py"))
    orphans = [p for p in present if p not in referenced]
    lines += ["", "## Tests ohne Anforderung", "",
              "Testdateien, aus denen keine Anforderung einen Test nennt. Sie können trotzdem nötig sein; "
              "dann fehlt ihre Zuordnung.", ""]
    lines += [f"- `{p}`" for p in orphans] or ["Keine."]
    return "\n".join(lines) + "\n"


def first_quote(row: dict[str, str]) -> str:
    return row["o_ton"].split(QUOTE_SEPARATOR)[0].strip()


# ---------------------------------------------------------------- Aufruf

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("befehl", choices=["pruefen", "schreiben"])
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    findings = validate(root)
    if args.befehl == "schreiben":
        if findings:
            print("\n".join(findings), file=sys.stderr)
            return 1
        (root / VIEW_PATH).write_text(render(root), encoding="utf-8")
        print(f"geschrieben: {VIEW_PATH}")
        return 0
    view = root / VIEW_PATH
    if not view.is_file() or view.read_text(encoding="utf-8") != render(root):
        findings.append(f"{VIEW_PATH} ist veraltet: python3 tools/anforderungskette.py schreiben")
    if findings:
        print("\n".join(findings))
        return 1
    print("Anforderungskette: in Ordnung")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
