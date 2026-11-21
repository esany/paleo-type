# Transkription — Nr. 632, Gesuch 0104R–0107L

Dieses Verzeichnis enthält die diplomatische Erstlesung des Gesuchs auf den Bildern 0104R–0107L samt angehängter Beglaubigung. Das Datenmodell ist das der Visitationsakten (Vorbild: `projects/ega-reg-ii-4-bd-ii/transcription/README.md`), eingeführt nach der Eigentümerentscheidung zu #394 und dem Auftrag #397 (Umsetzung 21.11.2026).

Diese README regelt **nur Konventionen und Navigation** der Transkriptionsebene. Projektumfang, Stand, Gates und nächste Schritte stehen in `../project.yml` und `../STATUS.md`. Die Zuordnung Bild ↔ PDF-Seite ↔ Datei steht in `corpus/source-data/SSTA-ARCHIVIALE-EDD69AA1/digital-crosswalk.tsv`.

## Ablage

```text
transcription/
├── README.md
└── first-reading/
    ├── 0104R.tsv   # Anfang des Gesuchs
    ├── 0105L.tsv
    ├── 0105R.tsv
    ├── 0106L.tsv
    ├── 0106R.tsv   # Schluss, Datum, Unterschrift, Beginn der Beglaubigung
    └── 0107L.tsv   # Beglaubigung der Kanzlei
```

Eine Datei je **sichtbarer Schriftfläche**: Anbieterbild plus linke (L) oder rechte (R) Bildhälfte. Das ist eine Ablage, keine archivalische Gliederung. Bildnummer und L/R sind digitale Ansichtsadressen, **keine Foliierung** (siehe Abschnitt Foliierung).

## Spalten

Gleiche Reihenfolge und Bedeutung wie bei den Visitationsakten:

1. `reading_order` — Lesereihenfolge auf der Fläche.
2. `diplomatic_reading` — die aktuelle diplomatische Lesung. Kennzeichnung: `[Wort?]` unsicher, `[a/b]` oder `[a/b?]` nicht entschieden, `⟦…⟧` sichtbar, aber nicht gelesen.
3. `line_ref` — Zeilenadresse: `<Bild><L/R>-<Bereich><Nr>`, z. B. `0104R-A01`.
4. `region` — Bereich auf der Fläche (`kopfvermerk`, `titel`, `anrede`, `haupttext`, `randstreifen`, `zierzeichen`, `datum`, `unterschrift`, `beglaubigung`, `kanzleizeile`, `namenszeile_unten`).
5. `source_phenomena` — sichtbare Quellenerscheinungen, getrennt vom Status.
6. `research_status` — `observed`, `working`, `variant`, `unresolved` (`methodology/transcription-guidelines.md`).
7. `alternatives` — grafisch mögliche Konkurrenzlesungen.
8. `abbreviation_layer` — editorische Angabe zu einer Abkürzung, nie anstelle der geschriebenen Form.
9. `editorial_supply` — ausdrückliche editorische Ergänzung, nur wenn vorhanden.
10. `evidence_note` — Grenze und Beleg der Lesung; Hinweise des Eigentümers stehen hier, nie in der Lesung.

Identifizierungen von Orten und Personen gehören nicht in die Lesung (Knau L003).

## Wie die Dateien entstanden sind (Überführung #397, 21.11.2026)

Die 97 Zeilen stammen 1:1 aus den Tabellen in `../research/gesuch-0104R-0107L.md` (Blöcke `F4-START`/`F4-END`). Lesung und Grenze sind unverändert übernommen; das prüft `tests/test_nr632_first_reading_migration.py`. Es wurde **keine Lesung geändert und nichts neu am Bild geprüft**.

Mechanisch abgeleitet, nicht neu untersucht:

- `region` aus dem Buchstaben der Zeilenadresse und den Beschreibungen der Markdown-Abschnitte (z. B. 0106R: A Haupttext, D Datum, B Unterschrift, C Beglaubigung; 0104R: H01 Kopfvermerk, H02–H03 Titel, H04 Anrede).
- `source_phenomena` aus den Zeichen der Lesung:
  - `unclear`, wenn `[` oder `⟦` vorkommt;
  - `abbreviation_mark` bei Doppelpunkt- oder Punktkürzung;
  - `line_end_division` bei Trennzeichen am Zeilenende.
  - Streichung, Zusatz und Schaden sind in der bisherigen Fassung nicht untersucht worden. Deshalb steht bei jeder Zeile `deletion_addition_damage:not_investigated`.
- `research_status`: `working` für Arbeitslesungen, `unresolved` für ganz ungelesene Bereiche, `observed` für das Zierzeichen.
- `alternatives` aus eingebetteten `[a/b?]`-Gruppen der Lesung.

## Was die Lesungen sind

KI-Arbeitslesungen mit begrenzten Blindproben, **keine Fachprüfung**. G2 (vollständige diplomatische Darstellung) ist nicht erreicht.

Vorschläge zur Änderung einzelner Lesungen aus der Prüfung am Bild vom 21.11.2026 und der Vergleich mit der Blindprobe stehen in `../research/gesuch-0104R-0107L.md`. Sie sind **noch nicht** in diese Dateien übernommen. Nach dem Vorbild der Visitationsakten gehört das in eine eigene Prüftabelle je unsicherer Stelle (G3), mit Vergleichsstellen und dem Ergebnis für die Lesung.

## Foliierung

Für jede der sechs Flächen ist am Bild festzustellen, ob eine Blattzahl sichtbar ist. Das Ergebnis steht in `corpus/source-data/SSTA-ARCHIVIALE-EDD69AA1/digital-crosswalk.tsv` (Spalte `notes`). Nichts wird erschlossen.

## Was hier nicht steht

Fortschritt, aktueller Arbeitsstand und Gate-Stand gehören nicht in diese README; sie stehen in `../STATUS.md`.
