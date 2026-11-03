#!/usr/bin/env python3
"""Frühwarnprüfung der Erhebung für #405/#406.

Aufruf aus der Repo-Wurzel, Analyse-Branch ausgecheckt:
    python3 engineering/evidence/audits/ursachen-405/pruefung.py <Einheit> [--alle-stichproben N]

Prüft die von Astra erhobenen Dateien einer Einheit mechanisch (F1–F8). Zusätzlich
zieht sie eine Zufallsstichprobe (F9) und zeigt dazu nur die Zeilen der Fundstelle.
Die Prüfung beurteilt keinen Befund inhaltlich und stellt keine Ursache fest. Sie
gehört nicht zu tools/ und wird nicht auf main übernommen.
Exit-Code 1 bei rot.
"""
from __future__ import annotations

import csv
import random
import re
import subprocess
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
WURZEL = HIER.parents[3]
EINHEITEN = HIER / "einheiten"

LESEN = ["einheit", "quelle", "gelesen", "vermerk", "datum"]
BEFUNDE = ["id", "einheit", "art", "phaenomen", "fundstelle", "zitat", "zeitpunkt", "akteur", "bezug", "stichwort"]
KARTE = ["element", "typ", "pfad", "zweck_laut_quelle", "fundstelle", "entstanden", "status_laut_repo",
         "haengt_ab_von", "genutzt_von", "ueberschneidung_mit"]
ARTEN = {"beobachtet", "aussage", "deutung"}
KAUSAL = re.compile(r"\b(weil|daher|deshalb|dadurch|führt(e)? zu|verursach\w*|ursache\w*|wegen|because|caused?|leads? to|due to)\b", re.I)
LOESUNG = re.compile(r"\b(sollte[n]?|vorschlag\w*|vorschlagen|maßnahme\w*|lösung\w*|empfehl\w*|should|recommend\w*|proposal)\b", re.I)
BLIND = re.compile(r"(ssta-20578-nr-632/research/transcription|first-reading|transcription-pilot|gegenlesung-vorab)", re.I)


def tsv(pfad: Path, spalten: list[str], fehler: list[str]) -> list[dict]:
    if not pfad.exists():
        fehler.append(f"F2 Datei fehlt: {pfad.relative_to(WURZEL)}")
        return []
    zeilen = pfad.read_text(encoding="utf-8").splitlines()
    if not zeilen or zeilen[0].split("\t") != spalten:
        fehler.append(f"F2 Kopfzeile falsch in {pfad.name}: erwartet {'|'.join(spalten)}")
        return []
    aus = []
    for nr, z in enumerate(zeilen[1:], 2):
        if not z.strip():
            continue
        teile = z.split("\t")
        if len(teile) != len(spalten):
            fehler.append(f"F2 {pfad.name}:{nr} hat {len(teile)} statt {len(spalten)} Spalten")
            continue
        d = dict(zip(spalten, teile))
        d["_zeile"] = nr
        aus.append(d)
    return aus


def stand_sha(stand: str) -> str | None:
    m = re.search(r"@([0-9a-f]{7,40})", stand)
    if m:
        return m.group(1)
    if re.fullmatch(r"[0-9a-f]{7,40}", stand.strip()):
        return stand.strip()
    return None  # Analyse-Branch: Arbeitsbaum


def datei_text(pfad: str, stand: str | None) -> str | None:
    if stand:
        r = subprocess.run(["git", "show", f"{stand}:{pfad}"], cwd=WURZEL, capture_output=True, text=True)
        return r.stdout if r.returncode == 0 else None
    p = WURZEL / pfad
    return p.read_text(encoding="utf-8", errors="replace") if p.is_file() else None


def fundstelle_zerlegen(f: str) -> tuple[str, int, int] | None:
    f = f.split("@PR#")[0].strip()
    m = re.fullmatch(r"(.+?):(\d+)(?:-(\d+))?", f)
    if not m:
        return None
    a = int(m.group(2))
    return m.group(1), a, int(m.group(3) or a)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    einheit = sys.argv[1]
    n_stich = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[2] == "--alle-stichproben" else 5
    rot: list[str] = []
    gelb: list[str] = []

    soll_alle = list(csv.DictReader(open(HIER / "sollliste.tsv", encoding="utf-8"), delimiter="\t"))
    soll = [s for s in soll_alle if s["einheit"] == einheit]
    stand_von = {s["quelle"]: s["stand"] for s in soll_alle if "(PR #" not in s["stand"]}
    stand_von.update({s["quelle"]: s["stand"] for s in soll})
    stand_pr = {(s["quelle"], m.group(1)): s["stand"] for s in soll_alle
                for m in [re.search(r"\(PR #(\d+)\)", s["stand"])] if m}
    if not soll:
        print(f"Einheit {einheit} nicht in sollliste.tsv")
        return 2
    d = EINHEITEN / einheit
    lesen = tsv(d / "lesen.tsv", LESEN, rot)
    befunde = tsv(d / "befunde.tsv", BEFUNDE, rot)
    karte = tsv(d / "systemkarte.tsv", KARTE, rot)
    if not (d / "kurzbild.md").exists():
        gelb.append("kurzbild.md fehlt (erst am Ende der Einheit nötig)")

    # F1 Abdeckung
    gelesen = {z["quelle"]: z for z in lesen}
    fehlt = [s["quelle"] for s in soll if s["quelle"] not in gelesen]
    if fehlt:
        rot.append(f"F1 {len(fehlt)} von {len(soll)} Quellen ohne Leseeintrag, z. B. {fehlt[:3]}")
    for z in lesen:
        if z["gelesen"] not in {"ganz", "teilweise", "nicht"}:
            rot.append(f"F2 lesen.tsv:{z['_zeile']} ungültiger Wert gelesen={z['gelesen']}")
        elif z["gelesen"] != "ganz" and not z["vermerk"].strip():
            rot.append(f"F1 lesen.tsv:{z['_zeile']} {z['gelesen']} ohne Begründung: {z['quelle']}")
        if z["quelle"] not in {s["quelle"] for s in soll}:
            gelb.append(f"F1 lesen.tsv:{z['_zeile']} Quelle nicht in Sollliste dieser Einheit: {z['quelle']}")

    # F2 Befunde formal
    ids = set()
    for b in befunde:
        if b["id"] in ids:
            rot.append(f"F2 doppelte ID {b['id']}")
        ids.add(b["id"])
        if not b["id"].startswith(einheit + "-"):
            rot.append(f"F2 {b['id']}: ID passt nicht zur Einheit")
        if b["art"] not in ARTEN:
            rot.append(f"F2 {b['id']}: art={b['art']!r} ungültig")
        for feld in ("phaenomen", "fundstelle"):
            if not b[feld].strip():
                rot.append(f"F2 {b['id']}: {feld} leer")
        if len(b["phaenomen"].split()) > 30:
            gelb.append(f"F2 {b['id']}: phaenomen länger als 30 Wörter")
        if b["zitat"] and len(b["zitat"].split()) > 15:
            gelb.append(f"F2 {b['id']}: zitat länger als 15 Wörter")

    # F3/F4 Fundstelle und Zitat
    cache: dict[tuple, list[str] | None] = {}
    for b in befunde + karte:
        name = b.get("id") or b.get("element")
        for f in [x for x in b.get("fundstelle", "").split(";") if x.strip()]:
            z = fundstelle_zerlegen(f)
            if not z:
                rot.append(f"F3 {name}: Fundstelle nicht im Format pfad:Zeile: {f!r}")
                continue
            pfad, a, e = z
            st = stand_sha(stand_von.get(pfad, "")) if pfad in stand_von else (None if (WURZEL / pfad).is_file() else stand_sha(soll[0]["stand"]))
            m = re.search(r"@PR#(\d+)", f)
            if m:
                st = stand_sha(stand_pr.get((pfad, m.group(1)), ""))
            key = (pfad, st)
            if key not in cache:
                t = datei_text(pfad, st)
                cache[key] = t.splitlines() if t is not None else None
            zeilen = cache[key]
            if zeilen is None:
                rot.append(f"F3 {name}: {pfad} am Stand {st or 'Arbeitsbaum'} nicht lesbar (ggf. git fetch)")
                continue
            if a < 1 or e > len(zeilen) or a > e:
                rot.append(f"F3 {name}: Zeilen {a}-{e} außerhalb von {pfad} ({len(zeilen)} Zeilen)")
                continue
            if b.get("zitat"):
                fenster = norm(" ".join(zeilen[max(0, a - 4):min(len(zeilen), e + 3)]))
                if norm(b["zitat"].strip('„“"')) not in fenster:
                    rot.append(f"F4 {name}: Zitat nicht an {pfad}:{a}-{e} gefunden")

    # F5/F6 Sprache
    for b in befunde:
        if b["art"] == "beobachtet" and KAUSAL.search(b["phaenomen"]):
            gelb.append(f"F5 {b['id']}: Kausalsprache in beobachtet: {b['phaenomen'][:80]}")
        if LOESUNG.search(b["phaenomen"]):
            gelb.append(f"F6 {b['id']}: Lösungssprache: {b['phaenomen'][:80]}")
    for k in karte:
        if LOESUNG.search(k["zweck_laut_quelle"]) and "„" not in k["zweck_laut_quelle"]:
            gelb.append(f"F6 Systemkarte {k['element']}: Lösungssprache im Zweck")

    # F7 Dichte
    belegt = {fundstelle_zerlegen(x)[0] for r in befunde + karte for x in r.get("fundstelle", "").split(";")
              if x.strip() and fundstelle_zerlegen(x)} | {k["pfad"] for k in karte}
    for s in soll:
        z = gelesen.get(s["quelle"])
        if z and z["gelesen"] == "ganz" and int(s["ca_tokens"]) > 5000 and s["quelle"] not in belegt:
            gelb.append(f"F7 {s['quelle']} (~{s['ca_tokens']} Tokens) als ganz gelesen, aber ohne Befund/Karteneintrag")

    # F8 Pflichtelemente der Systemkarte (über alle Einheiten)
    alle_karte = []
    for p in EINHEITEN.glob("*/systemkarte.tsv"):
        alle_karte += tsv(p, KARTE, [])
    vorhanden = {k["pfad"] for k in alle_karte} | {k["element"] for k in alle_karte}
    pflicht = [s["quelle"] for s in soll_alle if re.match(r"(methodology/|tools/[^/]+\.py$|\.github/workflows/)", s["quelle"])]
    labels = HIER / "export" / "labels.tsv"
    if labels.exists():
        pflicht += ["label:" + r["label"] for r in csv.DictReader(open(labels, encoding="utf-8"), delimiter="\t")]
    fehlend = [p for p in pflicht if p not in vorhanden and p.removeprefix("label:") not in vorhanden]
    if fehlend:
        gelb.append(f"F8 {len(fehlend)} Pflichtelemente noch nicht in der Systemkarte (alle Einheiten), z. B. {fehlend[:4]}")

    # Bericht
    print(f"Einheit {einheit}: Soll {len(soll)} · gelesen ganz {sum(z['gelesen']=='ganz' for z in lesen)} · "
          f"teilweise {sum(z['gelesen']=='teilweise' for z in lesen)} · nicht {sum(z['gelesen']=='nicht' for z in lesen)} · "
          f"Befunde {len(befunde)} (beobachtet {sum(b['art']=='beobachtet' for b in befunde)}, aussage "
          f"{sum(b['art']=='aussage' for b in befunde)}, deutung {sum(b['art']=='deutung' for b in befunde)}) · "
          f"Systemkarte {len(karte)}")
    print(f"ROT {len(rot)}")
    for x in rot[:40]:
        print("  " + x)
    print(f"GELB {len(gelb)}")
    for x in gelb[:40]:
        print("  " + x)

    # F9 Stichprobe
    if befunde:
        rnd = random.Random(f"{einheit}-{len(befunde)}")
        print(f"F9 Stichprobe ({min(n_stich, len(befunde))}):")
        for b in rnd.sample(befunde, min(n_stich, len(befunde))):
            print(f"- {b['id']} [{b['art']}] {b['phaenomen']}  ⟶ {b['fundstelle']}")
            z = fundstelle_zerlegen(b["fundstelle"].split(";")[0])
            if not z:
                continue
            pfad, a, e = z
            if BLIND.search(pfad):
                print("    (Blindheit: Inhalt nicht angezeigt)")
                continue
            st = stand_sha(stand_von.get(pfad, "")) if pfad in stand_von else None
            t = datei_text(pfad, st)
            if t:
                for i, zeile in enumerate(t.splitlines()[a - 1:min(e, a + 7)], a):
                    print(f"    {i}: {zeile[:200]}")
    return 1 if rot else 0


if __name__ == "__main__":
    sys.exit(main())
