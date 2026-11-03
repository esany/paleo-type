# Erhebung für die Ursachenanalyse #405

Dieses Verzeichnis gehört dem Auftrag **#406** (Erhebung durch Astra) und dient der Analyse **#405**. Es liegt auf dem Branch `analysis/ursachen-405-erhebung` und wird **nicht** auf `main` übernommen.

Die Rollen auf einen Blick:
- **Erhebung (Astra):** vollständig lesen und festhalten, *was* da ist und *was* geschah, mit Fundstelle.
- **Bewertung (Claude):** prüft die Erhebung mit `pruefung.py` und Stichproben und führt später die Ursachenanalyse durch.

**Keine Ursachen als Befund, keine Lösungen, keine Maßnahmen.**

## Inhalt

| Datei | Zweck | Wer |
|---|---|---|
| `sollliste.tsv` | Alle zu lesenden Quellen, eingeteilt in Einheiten, mit Stand und Größe. Maßgeblich für die Abdeckung. | Claude, mechanisch erzeugt |
| `export/issues/NNNN.md` | Alle Issues und PRs mit allen Kommentaren als Datei mit Zeilennummern. Abgeleitete Kopie, Stand siehe `export/STAND.md`. Kanonisch bleibt GitHub. | Claude, mechanisch erzeugt |
| `export/commits.tsv`, `export/labels.tsv` | Commit-Zeitlinie von `main` und die Labels | Claude, mechanisch erzeugt |
| `export/wissensarbeit/`, `export/design-lab/` | Textdateien der Vergleichsrepos (Stand in `.stand-sha`). Anweisungsdateien sind umbenannt (`AGENTS.md.txt`, `CLAUDE.md.txt`, `_claude/` …), damit kein Chat sie als eigene Anweisung lädt. | Claude, mechanisch erzeugt |
| `einheiten/<Einheit>/lesen.tsv` | Leseprotokoll | Astra |
| `einheiten/<Einheit>/befunde.tsv` | Phänomene mit Fundstelle | Astra |
| `einheiten/<Einheit>/systemkarte.tsv` | Was ist wo vorhanden (Big Picture) | Astra |
| `einheiten/<Einheit>/kurzbild.md` | Höchstens 15 Zeilen: Was enthält die Einheit? Nur Beschreibung, keine Deutung. | Astra |
| `pruefung.py` | Frühwarnprüfungen für die Bewertung | Claude |

## Arbeitsweise je Quelle (wichtig wegen der Kontextgröße)

Eine Einheit muss **nicht** auf einmal in den Chat passen:
1. Eine Quelle aus `sollliste.tsv` **vollständig** lesen.
2. Sofort ihre Zeilen in `lesen.tsv`, `befunde.tsv` und gegebenenfalls `systemkarte.tsv` schreiben und committen.
3. Dann die nächste Quelle.

Ein Durchgang darf jederzeit enden. Der nächste setzt bei der ersten Quelle der Einheit fort, die noch nicht in `lesen.tsv` steht. Passt eine einzelne Quelle nicht vollständig in den Kontext, wird sie abschnittsweise gelesen und `gelesen=ganz` mit dem Vermerk `abschnittsweise` eingetragen. Wird ein Teil nicht gelesen, gilt `teilweise` mit Begründung.

## Formate (Tabulator-getrennt, UTF-8, eine Kopfzeile, keine Tabulatoren und Zeilenumbrüche in Feldern)

### `lesen.tsv`

```
einheit	quelle	gelesen	vermerk	datum
```
- `quelle` genau wie in `sollliste.tsv`
- `gelesen`: `ganz` · `teilweise` · `nicht`
- `vermerk`: bei `teilweise` oder `nicht` die Pflichtbegründung; bei `ganz` optional (z. B. `abschnittsweise`)
- `datum`: JJJJ-MM-TT

### `befunde.tsv`

```
id	einheit	art	phaenomen	fundstelle	zitat	zeitpunkt	akteur	bezug	stichwort
```
- `id`: `<Einheit>-<laufende Nummer, 3-stellig>`, z. B. `U02-eng-audits-007`
- `art`, genau einer der Werte:
  - `beobachtet`: was in der Quelle steht oder geschah
  - `aussage`: was ein Beteiligter (Chat, Modell, Eigentümer, Audit) über Ursachen, Erfolg oder Bedeutung sagt
  - `deutung`: eigene Deutung des Lesers, sparsam einsetzen
- `phaenomen`: höchstens 30 Wörter, in eigenen Worten
- `fundstelle`:
  - bei Dateien: `pfad:Zeile` oder `pfad:Zeile-Zeile` am Stand der Sollliste
  - bei PR-Dateien: zusätzlich `@PR#n`
  - Zeilennummern beziehen sich auf die Datei, wie sie auf dem genannten Stand liegt
- `zitat`: optional, **wörtlich**, höchstens 15 Wörter, nur aus der Fundstelle. **Keine Lesungen von Nr. 632 zitieren** (Blindheit der Prüfer).
- `zeitpunkt`: Datum des Vorgangs, falls belegt, sonst leer
- `akteur`: nur wenn in der Quelle belegt (z. B. Signatur `Claude`, `Codex`, Eigentümerentscheidung), sonst `unbekannt`. Alle Beiträge stammen vom Konto `esany`.
- `bezug`: IDs anderer Befunde oder Issue-Nummern, durch Komma getrennt
- `stichwort`: höchstens 3 freie Stichworte zum Wiederfinden. Sie sind eine Einordnung des Lesers, keine Kategorie.

Es gibt keinen festen Ursachenkatalog. Bitte keine Einordnung in vorgegebene Schemata, auch nicht in die Muster früherer Audits (#230, #297, #402, #404 …). Diese gelten als Aussagen Beteiligter.

### `systemkarte.tsv` (das Big Picture: was wo vorhanden ist)

```
element	typ	pfad	zweck_laut_quelle	fundstelle	entstanden	status_laut_repo	haengt_ab_von	genutzt_von	ueberschneidung_mit
```
- `typ`, z. B.: `regel`, `methode`, `werkzeug`, `test`, `datenmodell`, `datei-typ`, `ablauf`, `rolle`, `label`, `stichwort`, `entscheidung`, `audit`, `issue-art`
- `zweck_laut_quelle`: höchstens 20 Wörter, wie die Quelle selbst den Zweck angibt
- `entstanden`: Datum und Issue- oder PR-Nummer, falls belegt
- `status_laut_repo`: `aktiv` · `historisch` · `abgelöst` · `ruhend` · `unklar`, jeweils mit Fundstelle
- `haengt_ab_von`, `genutzt_von`, `ueberschneidung_mit`: Namen anderer Elemente, nur wenn belegt

Jedes Element wird **einmal** aufgeführt, und zwar in der Einheit, in der es definiert ist. Andere Einheiten verweisen über `genutzt_von` und `ueberschneidung_mit`.

## Regeln

- Nichts gekürzt lesen, ohne es in `lesen.tsv` zu vermerken.
- Vor einer Deutung die erklärte **Absicht** in der Quelle festhalten (`art=aussage`).
- Keine Lösungs- oder Maßnahmesprache („sollte“, „Vorschlag“, „Maßnahme“, „Lösung“, „empfehlen“), außer im wörtlichen Zitat einer Quelle.
- Ursache-Wirkungs-Aussagen nur als `aussage` (mit Quelle) oder `deutung`, nie als `beobachtet`.
- Astra ist an vielen Quellen selbst beteiligt. Diese Befunde bleiben trotzdem vollständig; die Bewertung berücksichtigt das.
- Am Ende jeder Einheit `kurzbild.md` schreiben und in #406 eine Zeile melden: Einheit, Commit, Anzahl der Quellen nach `ganz/teilweise/nicht`, Anzahl der Befunde und Elemente.

## Frühwarnung (für die Bewertung durch Claude)

`python3 pruefung.py <Einheit>` (Repo-Wurzel als Arbeitsverzeichnis, Analyse-Branch ausgecheckt) prüft:

| Prüfung | Was sie erkennt | Folge |
|---|---|---|
| F1 Abdeckung | Quellen der Sollliste ohne Eintrag in `lesen.tsv`; `teilweise/nicht` ohne Begründung | rot, bis nachgetragen |
| F2 Format | falsche Spaltenzahl, fehlende Pflichtfelder, ungültige `art`, doppelte IDs | rot |
| F3 Fundstelle | Pfad nicht vorhanden oder Zeile außerhalb der Datei | rot je Befund |
| F4 Zitattreue | Zitat steht nicht an der Fundstelle (±3 Zeilen) | **rot: möglicher erfundener Beleg** |
| F5 Ebenen | Kausalsprache in `art=beobachtet` | gelb, Sichtprüfung |
| F6 Lösungssprache | Lösungs- oder Maßnahmesprache außerhalb von Zitaten | gelb, Sichtprüfung |
| F7 Dichte | große, als `ganz` gelesene Quellen ohne jeden Befund oder Systemkarten-Eintrag | gelb: Hinweis auf Überfliegen |
| F8 Systemkarte | Pflichtelemente (jede Datei in `methodology/`, `tools/*.py`, `.github/workflows/`, jedes Label) fehlen in der Systemkarte | gelb, bis zur letzten Einheit |
| F9 Stichprobe | zieht zufällig 5 Befunde und zeigt nur die Zeilen der Fundstelle | Claude prüft, ob der Befund die Stelle trifft |

**Regel bei rot:** Die Einheit wird nicht geflickt. Betroffene Quellen werden vollständig neu gelesen. Ab dem ersten erfundenen Zitat (F4) wird die ganze Einheit neu gelesen.

**Pilot:** Zuerst wird nur `U01-grundlage` erhoben und von Claude bewertet. Erst danach folgen die übrigen Einheiten. Das Format darf nach dem Pilot einmal angepasst werden.

**Tokensparend weiterbearbeiten:** Claude liest nie alle Befunde auf einmal. Gearbeitet wird mit `pruefung.py`, mit Abfragen über Stichwort, Bezug oder Fundstelle (`grep`, `awk`) und mit Stichproben. Wo eine Aussage es erfordert, geht Claude zur Quelle zurück.

## Hinweis für die Prüfung von U08 und U09

Für PR-Dateien liegt der Stand auf fremden Branches. Vor der Prüfung lädt man ihn mit `git fetch origin pull/<n>/head` für die in `sollliste.tsv` genannten PRs.
