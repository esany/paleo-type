# Struktur S: Zeitachse der ganzen Laufzeit

Erzeugt mechanisch mit `analyse/struktur.py` aus Git (`main` und alle PR-Köpfe) und dem Export der Issues und PRs (#1–#405). Keine Deutung.

**Bereiche (Zuordnung ist eine Wahl):** F Forschung = `projects/**` außer Steuerdateien, `corpus/`, `entities/`, `source-entry/*.tsv` · P Projektsteuerung = `ARBEITSPLAN.md`, `GEGENLESUNG.md`, `MILESTONES.md`, `README.md` in `projects/` · M Methodik = `methodology/`, `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `DECISIONS.md` · V Verfahren und Engineering = `engineering/`, `requirements/`, `docs/`, `templates/`, `README.md`, `MILESTONES.md`, `SPICKZETTEL.md` und Übriges · C Code = `tools/`, `tests/`, `.github/`.

**Gezählt:** hinzugefügte Zeilen, Umbenennungen erkannt (`-M`), Merge-Commits ausgelassen. `main` = übernommen. `offen` = Commits nur in nicht übernommenen PRs (offen oder ohne Merge geschlossen), ohne Commits, die über andere PRs nach `main` kamen. Zeilen sind ein grobes Maß: Eine TSV-Zeile mit einer Lesung und eine Zeile Regelprosa zählen gleich.

Grundlage: 948 Commits auf `main` (ohne Merges), 396 Commits in 20 nicht übernommenen PRs, 405 Issues und PRs.

## 1. Wochen

| Woche ab | Commits | F | P | M | V | C | F-Anteil main | offen F | offen übrige | Issues | PRs | mit Claude-Signatur | Label `rettung-eigentümer` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-24 | 282 | 3023 | 407 | 4755 | 3018 | 1544 | 24 % | 0 | 0 | 65 | 19 | 0 |  |
| 2026-08-31 | 55 | 2493 | 320 | 1216 | 308 | 1307 | 44 % | 371 | 4046 | 13 | 15 | 1 |  |
| 2026-09-07 | 189 | 4461 | 35 | 242 | 1436 | 1983 | 55 % | 0 | 0 | 22 | 42 | 1 |  |
| 2026-09-14 | 95 | 533 | 0 | 30 | 14946 | 333 | 3 % | 0 | 0 | 27 | 25 | 0 |  |
| 2026-09-21 | 5 | 0 | 0 | 0 | 494 | 0 | 0 % | 0 | 0 | 0 | 0 | 0 |  |
| 2026-09-28 | 44 | 1 | 0 | 10 | 11176 | 889 | 0 % | 0 | 0 | 31 | 17 | 0 |  |
| 2026-10-05 | 247 | 676 | 7 | 234 | 6140 | 4096 | 6 % | 29 | 2747 | 15 | 38 | 1 |  |
| 2026-10-26 | 24 | 761 | 337 | 29 | 455 | 1032 | 29 % | 2355 | 3016 | 23 | 31 | 26 | #355, #358, #359 |
| 2026-11-02 | 7 | 0 | 61 | 0 | 30 | 508 | 0 % | 556 | 1081 | 13 | 9 | 20 |  |

## 2. Wendepunkte nach der vorab festgelegten Regel (ansatz.md, Abschnitt 5)

Regel: Der Forschungsanteil an den auf `main` hinzugefügten Zeilen steigt oder fällt gegenüber der Vorwoche um mindestens 30 Prozentpunkte, oder Systemarbeit (V+C) setzt nach mindestens einer Woche ohne Systemarbeit wieder ein; dazu alle Ereignisse mit Label `rettung-eigentümer`. Wochen mit weniger als 200 hinzugefügten Zeilen gelten als zu klein für einen Anteil und werden übersprungen (Ergänzung zur Regel, vor der Auswertung festgelegt, damit Ein-Commit-Wochen keine Ausschläge erzeugen).

| Woche ab | Anteil vorher | Anteil jetzt | Richtung |
|---|---|---|---|
| 2026-09-14 | 55 % (2026-09-07) | 3 % | zur Systemarbeit |

Wiedereinsetzen von Systemarbeit nach einer Woche Pause: keins.

Ereignisse mit Label `rettung-eigentümer`: #355 (2026-10-29, Issue), #358 (2026-10-30, Issue), #359 (2026-10-30, PR).

## 3. Wann entstanden Regeln, Werkzeuge und Abläufe (Fortschreibung der Systemkarte)

Erster Commit je Datei auf `main` (mit Umbenennungen verfolgt nur innerhalb des Bereichs), für `methodology/`, `tools/`, `.github/workflows/`, `docs/`, Wurzeldateien und die Projekt-Steuerdateien. `engineering/catalog/artifacts.tsv` führt Engineering-Artefakte bis ENG-A-0122 (09.10.); hier stehen nur Dateien, die bis heute auf `main` liegen.

**Methodik** (10): `methodology/ai-governance.md` 2026-08-26; `methodology/evidence-policy.md` 2026-08-26; `methodology/historical-source-workflow.md` 2026-08-26; `methodology/maintenance.md` 2026-08-26; `methodology/project-lifecycle.md` 2026-08-26; `methodology/quality-and-learning.md` 2026-08-26; `methodology/research-gates.md` 2026-08-26; `methodology/source-and-provenance.md` 2026-08-26; `methodology/transcription-guidelines.md` 2026-08-26; `methodology/workflow.md` 2026-08-26

**Werkzeuge** (16): `tools/source_contract.py` 2026-08-27; `tools/project_context.py` 2026-09-03; `tools/source_intake.py` 2026-09-03; `tools/regii5_evidence_packet.py` 2026-09-10; `tools/regii5_packet_benchmark.py` 2026-09-10; `tools/regii5_visual_retrieval.py` 2026-09-10; `tools/outcome_context.py` 2026-09-18; `tools/archival_source_acquisition.py` 2026-10-04; `tools/engineering.py` 2026-10-04; `tools/check.py` 2026-10-05; `tools/engineering_context.py` 2026-10-05; `tools/engineering_fitness.py` 2026-10-05; `tools/prompt.py` 2026-10-05; `tools/metrics.py` 2026-10-30; `tools/work_return.py` 2026-10-31; `tools/gegenlesung_check.py` 2026-11-02

**GitHub-Abläufe** (3): `.github/CODEOWNERS` 2026-08-27; `.github/workflows/source-contract.yml` 2026-08-27; `.github/workflows/nr632-gegenlesung.yml` 2026-11-02

**Abläufe in docs/** (2): `docs/archival-source-acquisition.md` 2026-10-04; `docs/gegenlesung-vorab.md` 2026-10-31

- `GOVERNING_OBJECTIVE.md`: angelegt 2026-08-27
- `AGENTS.md`: angelegt 2026-08-26
- `DECISIONS.md`: angelegt 2026-08-26
- `README.md`: angelegt 2026-08-26
- `MILESTONES.md`: angelegt 2026-08-26
- `SPICKZETTEL.md`: angelegt 2026-10-31

**Nr. 632 auf main** (13): `projects/ssta-20578-nr-632/STATUS.md` 2026-10-08; `projects/ssta-20578-nr-632/project.yml` 2026-10-08; `projects/ssta-20578-nr-632/research/use-evidence.tsv` 2026-10-08; `projects/ssta-20578-nr-632/source-uses.tsv` 2026-10-08; `projects/ssta-20578-nr-632/research/documentary-object-view-map-2026-10-29.md` 2026-10-29; `projects/ssta-20578-nr-632/research/targeted-boundary-reconciliation-2026-10-28.md` 2026-10-29; `projects/ssta-20578-nr-632/research/business-process-chronology-2026-10-30.md` 2026-10-30; `projects/ssta-20578-nr-632/research/content-document-function-inventory-2026-10-30.md` 2026-10-30; `projects/ssta-20578-nr-632/research/direct-transcription-experiment-iteration-02-2026-10-30.md` 2026-10-30; `projects/ssta-20578-nr-632/research/direct-transcription-iterations-03-04-2026-10-30.md` 2026-10-30; `projects/ssta-20578-nr-632/research/targeted-source-criticism-2026-10-30.md` 2026-10-30; `projects/ssta-20578-nr-632/ARBEITSPLAN.md` 2026-10-31; `projects/ssta-20578-nr-632/GEGENLESUNG.md` 2026-10-31


## 4. Umfang der Regeltexte über die Zeit

Zeilen von `AGENTS.md` und `methodology/` insgesamt am letzten Commit jeder Woche auf `main`.

| Woche ab | AGENTS.md | methodology/ | engineering/ (Dateien) | tests/ (Dateien) |
|---|---|---|---|---|
| 2026-08-24 | 375 | 1744 | 0 | 3 |
| 2026-08-31 | 197 | 2001 | 0 | 8 |
| 2026-09-07 | 224 | 2171 | 0 | 12 |
| 2026-09-14 | 224 | 2192 | 0 | 13 |
| 2026-09-21 | 224 | 2192 | 0 | 13 |
| 2026-09-28 | 224 | 2192 | 0 | 17 |
| 2026-10-05 | 323 | 2326 | 109 | 23 |
| 2026-10-26 | 345 | 2331 | 110 | 27 |
| 2026-11-02 | 345 | 2331 | 110 | 27 |

## 5. Erste Claude-Signatur

Früheste Issue oder PR mit Claude-Signatur im Text: #90 (2026-09-02); insgesamt 49 Einträge. Alle Einträge stammen vom Konto `esany`; unsignierte Einträge sind keinem Modell zuzuordnen.
