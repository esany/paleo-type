#!/usr/bin/env python3
"""Anforderungskette: Intent → Bedürfnis → Pain → Anforderung → Prüfung.

Prüft die Kette deterministisch und erzeugt daraus die Leseansicht
``requirements/kette.md``. Quellen sind genau zwei Tabellen:

- ``requirements/beduerfnisse.tsv``: Intent, Rahmen, Bedürfnisse und Pains,
  jeweils mit wörtlichem O-Ton und Fundstelle;
- ``requirements/domain-requirements.tsv``: die Anforderungen mit den
  Kettenspalten ``kurz``, ``need_ids``, ``applies_from``, ``verified_by``,
  ``depends_on`` und ``overlaps``;
- ``requirements/funktionen.tsv``: Funktionen, die Gruppen von Anforderungen
  absichern, mit Schmerz, Größe, Befunden je Perspektive, Abhängigkeiten,
  DOR, DOD, Iterationen und Rang.

Grenze: Das Werkzeug prüft, ob die Kette vollständig und widerspruchsfrei
verknüpft ist, ob jeder O-Ton wörtlich an seiner Fundstelle steht und ob jeder
genannte Test existiert. Es prüft nicht, ob ein Test die Anforderung inhaltlich
ganz abdeckt, ob eine Ableitung den O-Ton richtig deutet oder ob eine
Anforderung fachlich erfüllt ist.

Aufruf:
  python3 tools/anforderungskette.py pruefen     # Kette und Ansicht prüfen
  python3 tools/anforderungskette.py schreiben   # Ansicht neu erzeugen
  python3 tools/anforderungskette.py issue FN-01 # Titel und Text des Issues zu einer Funktion
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

FUNC_PATH = Path("requirements/funktionen.tsv")
FUNC_COLUMNS = ["id", "name", "zweck", "sichert", "lindert", "schmerz", "befunde", "ohne_befund", "groesse",
                "aufwand", "braucht", "bestand", "dor", "dod", "iteration", "rang", "begruendung", "status", "issue"]
PERSPECTIVES = ["Nutzer", "Fach", "Gestaltung", "Technik", "Recht"]
DIMENSIONS = ["Wissen", "Ressourcen", "Qualität", "Komplexität", "Strategie", "Nachhaltigkeit"]
ASPECTS = PERSPECTIVES + DIMENSIONS
FN_ID = re.compile(r"FN-\d{2}\Z")
SIZES = ["hoch", "mittel", "gering"]
EFFORTS = ["klein", "mittel", "groß"]
FN_STATUS = ["Vorschlag", "bestätigt", "in Arbeit", "fertig"]
FINDING = re.compile(r"(?P<aspect>[A-Za-zÄÖÜäöüß]+): (?P<text>.+?) \[(?P<status>belegt|abgeleitet|Hypothese)(?::(?P<refs>[^\]]*))?\]\Z")
FN_REF = re.compile(r"\bFN-\d{2}\b")
TEST_PATH = re.compile(r"tests/test_[a-z0-9_]+\.py")
MAX_ISSUE_CHARS = 3000
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
    if (root / FUNC_PATH).is_file():
        findings.extend(check_functions(root, reqs, by_id))
    return findings


def check_functions(root: Path, reqs: list[dict[str, str]], needs: dict[str, dict[str, str]]) -> list[str]:
    fields, funcs = read_tsv(root / FUNC_PATH)
    if fields != FUNC_COLUMNS:
        return [f"{FUNC_PATH}: Spalten müssen genau {FUNC_COLUMNS} sein"]
    out: list[str] = []
    req_by_id = {r["requirement_id"]: r for r in reqs}
    sections = o_ton_sections((root / O_TON_PATH).read_text(encoding="utf-8")) if (root / O_TON_PATH).is_file() else {}
    resolver = BelegResolver(root, needs, req_by_id, sections)
    ids = [f["id"] for f in funcs]
    known = set(ids)
    for fid in sorted({i for i in ids if ids.count(i) > 1}):
        out.append(f"{fid}: doppelte Funktion")
    ranks: dict[str, int] = {}
    owner_of: dict[str, list[str]] = defaultdict(list)
    for f in funcs:
        fid = f["id"]
        if not FN_ID.fullmatch(fid):
            out.append(f"{fid!r}: ungültige Funktions-ID (erwartet FN- mit zwei Ziffern)")
        for column in ("name", "zweck", "schmerz", "dor", "dod", "begruendung"):
            if not f[column].strip():
                out.append(f"{fid}: {column} fehlt")
        if not split(f["sichert"]) and not split(f["lindert"]):
            out.append(f"{fid}: sichert keine Anforderung und lindert kein Bedürfnis")
        for rid in split(f["sichert"]):
            owner_of[rid].append(fid)
            if rid not in req_by_id:
                out.append(f"{fid}: unbekannte Anforderung {rid}")
        for nid in split(f["lindert"]):
            if nid not in needs or needs[nid]["art"] == "Intent":
                out.append(f"{fid}: lindert unbekanntes Bedürfnis, Pain oder Rahmen {nid}")
        out.extend(check_aspects(fid, f, resolver))
        if f["groesse"] not in SIZES:
            out.append(f"{fid}: Größe muss {', '.join(SIZES)} sein")
        if f["aufwand"] not in EFFORTS:
            out.append(f"{fid}: Aufwand muss {', '.join(EFFORTS)} sein")
        dod_tests = TEST_PATH.findall(f["dod"])
        if not dod_tests:
            out.append(f"{fid}: DOD nennt keinen Test (tests/test_….py), an dem „fertig“ prüfbar ist")
        if f["status"] not in FN_STATUS:
            out.append(f"{fid}: Status muss {', '.join(FN_STATUS)} sein")
        if f["issue"] and not re.fullmatch(r"#\d+", f["issue"]):
            out.append(f"{fid}: Issue muss als #Nummer angegeben sein")
        if f["rang"].isdigit() and int(f["rang"]) > 0:
            ranks[fid] = int(f["rang"])
        else:
            out.append(f"{fid}: Rang muss eine positive Zahl sein")
        for column in ("zweck", "dor", "dod", "iteration", "begruendung", "bestand"):
            for ref in FN_REF.findall(f[column]):
                if ref not in known:
                    out.append(f"{fid}: {column} nennt unbekannte Funktion {ref}")
        for ref in FN_REF.findall(f["dor"]):
            if ref != fid and ref not in split(f["braucht"]):
                out.append(f"{fid}: DOR verlangt {ref}, aber {ref} steht nicht unter braucht")
        if f["status"] == "fertig":
            for path in dod_tests:
                if not (root / path).is_file():
                    out.append(f"{fid}: fertig, aber {path} gibt es nicht")
            for rid in split(f["sichert"]):
                named = {TEST_REF.fullmatch(t)["path"] for t in test_refs(req_by_id.get(rid, {}).get("verified_by", ""))}
                if rid in req_by_id and not named & set(dod_tests):
                    out.append(f"{fid}: fertig, aber {rid} nennt keinen Test aus der DOD")
        if len(issue_body(f, req_by_id, needs)) > MAX_ISSUE_CHARS:
            out.append(f"{fid}: Issue-Text länger als {MAX_ISSUE_CHARS} Zeichen; kürzen statt Kontextwurst")
    for rid, owners in sorted(owner_of.items()):
        if len(owners) > 1:
            out.append(f"{rid} wird von mehreren Funktionen gesichert: {', '.join(owners)}")
    for rank in sorted({r for r in ranks.values() if list(ranks.values()).count(r) > 1}):
        out.append(f"Rang {rank} ist mehrfach vergeben")
    graph = {f["id"]: split(f["braucht"]) for f in funcs}
    for fid, deps in graph.items():
        for dep in deps:
            if dep == fid:
                out.append(f"{fid}: braucht sich selbst")
            elif dep not in graph:
                out.append(f"{fid}: braucht unbekannte Funktion {dep}")
            elif fid in ranks and dep in ranks and ranks[dep] >= ranks[fid]:
                out.append(f"{fid} (Rang {ranks[fid]}) braucht {dep} (Rang {ranks[dep]}); was gebraucht wird, kommt zuerst")
    for f in funcs:
        for rid in split(f["sichert"]):
            for dep in split(req_by_id.get(rid, {}).get("depends_on", "")):
                for other in owner_of.get(dep, []):
                    if other != f["id"] and other not in graph.get(f["id"], []):
                        out.append(f"{f['id']}: {rid} braucht {dep}, das {other} sichert; {other} fehlt unter braucht")
    return out


class BelegResolver:
    """Löst Belege auf: Bedürfnis-ID, Anforderung (kurz), #Issue, Repo-Pfad oder „O-Ton Datum Überschrift“."""

    def __init__(self, root: Path, needs: dict, reqs: dict, sections: dict) -> None:
        self.root, self.needs, self.sections = root, needs, sections
        self.reqs = {short(r) for r in reqs}

    def problem(self, token: str) -> str | None:
        if token in self.needs or token in self.reqs or re.fullmatch(r"#\d+", token):
            return None
        if token.startswith("O-Ton "):
            _, problems = resolve_anchor(token.removeprefix("O-Ton "), self.sections)
            return problems[0] if problems else None
        path = Path(token.strip("`"))
        if "/" in token and not path.is_absolute() and ".." not in path.parts:
            return None if (self.root / path).exists() else f"Pfad {token} gibt es nicht"
        return f"Beleg {token!r} ist weder ID, Anforderung, #Issue, Repo-Pfad noch „O-Ton Datum Überschrift“"


def check_aspects(fid: str, f: dict[str, str], resolver: BelegResolver) -> list[str]:
    """Jede Perspektive und Dimension wird einmal bedacht: mit Befund oder ausdrücklich ohne.

    Die Nutzersicht braucht immer einen Befund. „belegt“ verlangt mindestens
    einen auflösbaren Beleg; genannte Belege müssen sich auflösen lassen.
    """
    out, seen, with_finding = [], [], []
    for part in [p.strip() for p in f["befunde"].split(" | ") if p.strip()]:
        match = FINDING.fullmatch(part)
        if match is None:
            out.append(f"{fid}: Befund {part[:40]!r} braucht die Form „Perspektive: Befund [belegt|abgeleitet|Hypothese]“")
            continue
        seen.append(match["aspect"])
        with_finding.append(match["aspect"])
        tokens = [t.strip() for t in (match["refs"] or "").split(",") if t.strip()]
        if match["status"] == "belegt" and not tokens:
            out.append(f"{fid}: {match['aspect']} ist als belegt markiert, nennt aber keinen Beleg")
        for token in tokens:
            problem = resolver.problem(token)
            if problem:
                out.append(f"{fid}: {match['aspect']}: {problem}")
    seen += split(f["ohne_befund"])
    for aspect in sorted(set(seen) - set(ASPECTS)):
        out.append(f"{fid}: unbekannte Perspektive oder Dimension {aspect}")
    for aspect in sorted({a for a in seen if seen.count(a) > 1}):
        out.append(f"{fid}: {aspect} steht doppelt")
    for aspect in ASPECTS:
        if aspect not in seen:
            out.append(f"{fid}: {aspect} ist nicht bedacht (Befund oder „ohne Befund“)")
    if "Nutzer" not in with_finding:
        out.append(f"{fid}: Die Nutzersicht braucht einen Befund")
    return out


def issue_body(f: dict[str, str], req_by_id: dict[str, dict[str, str]], needs: dict[str, dict[str, str]]) -> str:
    def bullets(value: str) -> list[str]:
        return [part.strip() for part in value.split(" | ") if part.strip()]

    rows = [req_by_id[r] for r in split(f["sichert"]) if r in req_by_id]
    tally = (f"Test genannt: {sum(map(has_test, rows))}, nur Urteil: {sum(map(judgement_only, rows))}, "
             f"kein Test bekannt: {sum(map(untested_gap, rows))}")
    eased = [f"{n} {needs[n]['aussage'].split(':')[0]}" for n in split(f["lindert"]) if n in needs]
    lines = [
        f"**Zweck:** {f['zweck']}", "",
        f"**Schmerz ohne sie** (Größe: {f['groesse']}): {f['schmerz']}", "",
        (f"**Sichert {len(rows)} Anforderungen** ({tally}): " + "; ".join(f"{short(r['requirement_id'])} {r['kurz']}" for r in rows))
        if rows else "**Sichert:** noch keine Anforderung", "",
        "**Lindert:** " + "; ".join(eased), "",
        "**Befunde je Perspektive:**",
    ]
    lines += [f"- {part}" for part in bullets(f["befunde"])]
    lines += [f"- Ohne Befund bedacht: {', '.join(split(f['ohne_befund']))}", "",
              f"**Braucht:** {', '.join(split(f['braucht'])) or 'nichts'} · **Aufwand:** {f['aufwand']} · "
              f"**Rang:** {f['rang']} ({f['status']}): {f['begruendung']}", "",
              f"**Bestand:** {f['bestand']}", "", "**DOR (bereit, wenn):**"]
    lines += [f"- [ ] {part}" for part in bullets(f["dor"])]
    lines += ["", "**DOD (fertig, wenn):**"]
    lines += [f"- [ ] {part}" for part in bullets(f["dod"])]
    lines += ["", "**Iterationen:** " + " · ".join(bullets(f["iteration"])), "",
              f"_Erzeugt aus `{FUNC_PATH}`; Änderungen dort, nicht hier. Größe, Rang und Befunde sind ein Vorschlag "
              "der KI. „Test genannt“: ein Test im Repo prüft einen Teil davon; „kein Test bekannt“: nichts prüft es; "
              "„nur Urteil“: nur Fachleute oder du beim Benutzen können es beurteilen._"]
    return "\n".join(lines) + "\n"


def o_ton_sections(text: str) -> dict[tuple[str, str], dict[str, object]]:
    """Abschnitte von docs/o-toene.md: (Datum, Fettüberschrift) → nur die Zitatzeilen.

    Gezählt werden nur Zeilen, die mit ``>`` beginnen; Überschriften und
    Anmerkungen der KI zählen nicht als O-Ton. Jedes Zitat ist ein eigener
    Absatz: Ein neuer beginnt nach einer Zeile ohne ``>``, nach einer leeren
    Zitatzeile und an einer Auslassung ``[…]``, damit ein O-Ton nicht über
    zwei Zitate hinweg zusammengesetzt werden kann.
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
            current = {"paragraphs": [], "button": "Antwortknopf" in line, "open": False}
            sections[(date, label["label"].strip())] = current
            continue
        if current is None:
            continue
        if not line.lstrip().startswith(">"):
            current["open"] = False
            continue
        content = re.sub(r"^\s*>\s?", "", line).strip()
        if not content or content == "[…]":
            current["open"] = False
            continue
        if not current["open"]:
            current["paragraphs"].append([])
            current["open"] = True
        current["paragraphs"][-1].append(content)
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
        label = match["label"]
        hits = [key for key in sections if key[0] == date and key[1] == label] or [
            key for key in sections
            if key[0] == date and key[1].startswith(label) and not key[1][len(label)].isalnum()]
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
    texts = [normalized(" ".join(par)) for section in found for par in section["paragraphs"]]
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
        "Zwei Prüfrunden durch einen frischen Kontext desselben Modells fanden Fehlzuordnungen; sie sind korrigiert. "
        "Modellfehler und geteilte Annahmen hat noch kein anderes Modell geprüft, weitere Fehler sind möglich. Die "
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
        + ", ".join(short(r["requirement_id"]) for r in claimed) + ". Die Selbstbewertung stammt aus KI-Fachaudits "
        "(#26–#37; Tabelle angelegt am 27.08.2026, vor dieser Änderung zuletzt am 08.09.2026 geändert) und ist eine "
        "Auskunft, kein Beleg.",
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
    if (root / FUNC_PATH).is_file():
        lines += render_functions(root, reqs, by_req)
    return "\n".join(lines) + "\n"


def render_functions(root: Path, reqs: list[dict[str, str]], by_req: dict[str, dict[str, str]]) -> list[str]:
    _, funcs = read_tsv(root / FUNC_PATH)
    funcs = sorted(funcs, key=lambda f: int(f["rang"]) if f["rang"].isdigit() else 999)
    lines = ["", "## Funktionen nach Rang", "",
             "Welche Funktion welche Anforderungen absichert und welchen Schmerz sie lindert. Größe, Rang und "
             "Befunde je Perspektive sind ein Vorschlag der KI (`requirements/funktionen.tsv`); entscheiden tust du. "
             "**Größe:** *hoch* hält die laufende Arbeit auf oder lässt Fehler in Forschungsdaten unbemerkt; *mittel* "
             "verlangsamt oder macht intransparent; *gering* betrifft erst spätere Stufen.", "",
             "| Rang | Funktion | Größe | Aufwand | sichert | lindert | braucht | Stand | Issue |",
             "|---:|---|---|---|---|---|---|---|---|"]
    for f in funcs:
        lines.append(f"| {f['rang']} | {f['id']} {f['name']} | {f['groesse']} | {f['aufwand']} | "
                     f"{', '.join(short(r) for r in split(f['sichert']))} | {', '.join(split(f['lindert']))} | "
                     f"{', '.join(split(f['braucht']))} | {f['status']} | {f['issue']} |")
    covered = {r for f in funcs for r in split(f["sichert"])}
    open_now = [r for r in reqs if stage_rank(r["applies_from"]) <= STAGES.index("G3") and untested_gap(r)
                and r["requirement_id"] not in covered]
    lines += ["", "## Lücken bis G3 ohne Funktion", "",
              "Prüfbare Anforderungen bis zur Stufe G3 ohne bekannten Test, die noch keine Funktion absichert.", ""]
    lines += [f"- {short(r['requirement_id'])} {r['kurz']} ({r['applies_from']})" for r in open_now] or ["Keine."]
    return lines


def first_quote(row: dict[str, str]) -> str:
    return row["o_ton"].split(QUOTE_SEPARATOR)[0].strip()


# ---------------------------------------------------------------- Aufruf

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("befehl", choices=["pruefen", "schreiben", "issue"])
    parser.add_argument("funktion", nargs="?", help="bei issue: Funktions-ID, z. B. FN-01")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    findings = validate(root)
    if args.befehl == "issue":
        _, funcs = read_tsv(root / FUNC_PATH)
        _, reqs = read_tsv(root / REQS_PATH)
        _, needs = read_tsv(root / NEEDS_PATH)
        match = [f for f in funcs if f["id"] == args.funktion]
        if not match:
            print(f"unbekannte Funktion {args.funktion!r}", file=sys.stderr)
            return 1
        if findings:
            print("Erst die Kette in Ordnung bringen:\n" + "\n".join(findings), file=sys.stderr)
            return 1
        print(f"{match[0]['id']} {match[0]['name']}")
        print(issue_body(match[0], {r["requirement_id"]: r for r in reqs}, {n["id"]: n for n in needs}), end="")
        return 0
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
