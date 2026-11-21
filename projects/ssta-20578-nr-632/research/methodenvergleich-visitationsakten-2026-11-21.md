# Methodenvergleich: Visitationsakten (Reg. Ii 4/5) gegen Nr. 632 — wie wir Quellen erschließen, was verloren ging

**Stand:** 21.11.2026. Erstellt von Claude auf Wunsch des Eigentümers („mache einen deep research … erstmal im repo … schau in den visitationsakten … wie erschließen wir quellen, was legen wir wann an. da finde ich seit 632 auch ein methodenverlust passiert … schaue tiefer nach“).
**Geltung:** Befund aus dem Repo. Keine Regeländerung, keine neue Struktur, keine Abnahme.
**Gelesen:**
- alle Dateien der Projekte `ega-reg-ii-4-bd-ii` und `ega-reg-ii-5-knau`: ganz die READMEs, Prüftabellen, Sperr- und Kontaminationsdateien und die Werkzeugversuche; in Teilen die Vergleichsakte (Matrix und Ablauf) und `LEARNINGS.md` (Überschriften);
- die Git-Entstehungsfolge aller Dateien;
- die Issues #342, #394, #396, #397;
- die Forschungsdateien von Nr. 632 auf `research/nr632-transcription-t0-t1-20261030`.

**Nicht gelesen:** die Knau-Forschungsakten im vollen Wortlaut (u. a. die Bewertung G2/B, die Synthese zum Quellenverständnis) und der Nr.-632-`STATUS.md` ganz.

## 1 · Wie die Visitationsakten erschlossen wurden

Am klarsten bei **Reg. Ii 4 Bd. II, fol. 306v–309r** (Knau): sechs Seiten, G1–G4 in vier Tagen (04.–07.09.2026). Die Reihenfolge der angelegten Dateien (aus Git) ist zugleich der Ablauf:

| Schritt | Was angelegt wird | Datei | wann |
|---|---|---|---|
| 0 | Projekt mit Zweck und **begrenztem Umfang**, vom Eigentümer gewählt (6 Seiten) | `project.yml`, `STATUS.md` | 31.08. |
| 1 | **Beweissicherung:** genaue Datei und Pixel, Crosswalk, Regeln für den internen Vergleich, Freigabestufe für Parallelzeugen | `research/…-evidence-lock.md` | 04.09. |
| 2 | **Kontaminationsmatrix:** was vor der Erstlesung erlaubt oder verboten ist (Parallelzeuge, alte Lesungen, Chatentwürfe, Sachkontext nur zur Hypothesenbildung, „grapheme_replacement“ verboten) | `research/…-contamination-matrix.tsv` | 04.09. |
| 3 | **Erstlesung je Blattseite** als Tabelle mit 10 festen Spalten: Reihenfolge, diplomatische Lesung, physische Zeile, Bereich, Quellenerscheinung, Status, Alternativen, Abkürzungsebene, editorische Ergänzung, Beleg | `transcription/first-reading/<Blatt>.tsv` + `README.md` (Spaltenbedeutung) | 04.–06.09. |
| 4 | **G2-Vollständigkeitsprüfung** und daraus **abgeleitete Leseansicht** | `transcription/derived/…-first-reading.md` | 06.09. |
| 5 | **G3-Prüftabelle** je unsicherer Zeile: Problemklasse, Zielfrage, **interne Vergleichsstellen mit genauer Fundstelle**, stützende und widersprechende Merkmale, Kontexttest, Entscheidung, Änderung an der Lesung, Fachprüfung nötig ja/nein | `research/…-g3-adjudication.tsv` | 06.09. |
| 6 | **Kontrollierter Vergleich (G4)** mit dem Parallelzeugen, erst nach Freigabe | `research/…-controlled-collation.md` | 06.09. |
| 7 | **Lehren** | `LEARNINGS.md` | 07.09. |

**Reg. Ii 5, fol. 61v–63r**, ergänzt das um:
- **endliche Zielmatrix** für die Nachprüfung unsicherer Stellen (`research/internal-comparanda-relecture-61v-63r.md`): je Ziel eine grafische Frage, das sichtbare Merkmal, das entscheiden könnte, dann eine gezielte Suche nach Vergleichsstellen in derselben Quelle, dann die Nachprüfung am Ziel;
- **Werkzeugversuche mit Messung** (10.09.):
  - Bildsuche nach wiederkehrenden Formen in derselben Quelle („Generator A“, `tools/regii5_visual_retrieval.py`);
  - lokales HTR mit Kraken 7.1.1 und einem allgemeinen PP-OCRv6-Modell, ohne Hochladen geschützter Bilder („Generator B“);
  - Ergebnis: beide eng behalten, als Lieferanten von Kandidaten, nicht als Entscheider. HTR erzeugt teils „flüssige, aber vom Bild nicht getragene“ Wörter;
- **Synthese zum Quellenverständnis** (S7) über die gelesene Stelle (`research/source-understanding-synthesis-61v-63r.md`);
- **29 Lehren** (L001–L029), u. a.:
  - L001: Wortumriss raten führte zu schweren Fehlern;
  - L002: Sinnzusammenhang ist bei der Erstlesung gefährlich;
  - L003: Namenskenntnis rutscht in die Schreibung;
  - L004: Zahl- und Maßnotation braucht eigene Behandlung;
  - L006: wiederholte KI-Lesungen sind keine unabhängige Bestätigung.

**Kern dieser Methode:** Der Umfang ist zuerst begrenzt. Was zählt, ist gesperrt, bevor gelesen wird. Jede Zeile hat ein festes Datenformat. Vollständigkeit wird geprüft. Unsicherheiten werden einzeln mit benannten Vergleichsstellen entschieden. Erst dann wird verglichen und eingeordnet.

## 2 · Was bei Nr. 632 anders lief

| Element | Visitationsakten | Nr. 632 (Forschungsbranch) |
|---|---|---|
| Umfang | bewusst begrenzte Stelle (4–6 Seiten) | ganze Akte, 135 Bilder (Eigentümerentscheidung 30.10.) |
| Beweissicherung, Kontaminationsmatrix | je Aufgabe eine Datei | keine; Regeln zur Blindheit nur im Gegenlese-Prompt |
| Datenformat der Lesung | 10 feste Spalten, eine Datei je Blattseite | **904 Tabellenzeilen** in einer 1.675-Zeilen-Markdown-Datei, **mindestens 6 verschiedene Kopfzeilen**, meist 3 Spalten („Lesung“, „Grenze/Status/Notiz“). Quellenerscheinung, Status, Alternativen und Abkürzung sind vermischt. Nie eine `first-reading/*.tsv`, nie `palaeography/` oder `apparatus/` |
| G2-Vollständigkeit | geprüft, je Zeile | nicht geprüft; „passt“ beruht auf 2–3 Zeilen je Seite |
| Leseansicht | aus den Daten erzeugt | Edition #382 liest Markdown (Entwurf) |
| G3: Unsicherheiten entscheiden | Zielmatrix, Vergleichsstellen mit Fundstelle, Prüftabelle | keine Prüftabelle. Stattdessen Methodentest F2 von Sehtechniken (alle drei gleich viele Fehler), Namenshinweise des Eigentümers, Einzelkorrekturen in Prosa |
| Werkzeuge für S4 | Bildsuche und lokales HTR erprobt, mit Messung | nicht genutzt; die Werkzeuge sind auf Reg. Ii 5 festgelegt (`regii5_*`) |
| Lehren | `LEARNINGS.md` | keine; dafür ein `STATUS.md` mit rund 51.000 Zeichen |
| Kontrolle | Fachprüfung, wo nötig, als benannte Grenze | KI gegen KI, gezählte Wortfehler in Stichproben |

**Gewonnen hat Nr. 632 auch etwas:**
- die Unterscheidung von Objekt und Ansicht bei einem gebundenen Mischband (#342, `documentary-object-view-map-2026-10-29.md`);
- die Zuordnung ohne Foliierung (`digital-crosswalk.tsv`, #345);
- Vorarbeiten zu Inhalt, Funktion und Vorgangsfolge.

Das sind sinnvolle Ergänzungen für eine andere Quellenart. Verloren ging die Lesemethode selbst.

## 3 · Wann der Bruch kam

Commits zu Nr. 632 je Tag (`main` und Forschungsbranch):

| Datum | Commits | Inhalt |
|---|---|---|
| 08.10. | 8 | Wiederherstellung, Übersicht, Prüfplan |
| 29.10. | 4 | Objekt- und Ansichtskarte, Zuordnung ohne Foliierung, Korrektur der Großurkunde |
| **30.10.** | **58** | Sprung von der Struktur zur **Massenlesung in Markdown** (0071R, 0102R–0131R, Experimente); zugleich #353 (Umbauplan), #355 (Werkzeuginventur), #358 (neuer Plan) |
| 31.10.–03.11. | 124 | vor allem Ablauf: Gegenlesung, Prüfskripte, Rückkehrmeldungen, Namensstellen, Spickzettel |

**Der Bruch liegt am 30.10.:** Nach einer methodisch sauberen Strukturphase begann das Lesen ohne die Schritte 1–5 aus Abschnitt 1. Ab dem 31.10. kam Ablaufsicherung hinzu, nicht Lesemethode.

## 4 · Warum (belegte Ursachen und Hypothesen)

1. **Der Prüf- und Startweg führte an der Methodik vorbei** (belegt, #394, Ursachenkommentar vom 03.11.): Die Startroutine las Spickzettel und Übergabe, nicht `methodology/` und den Bestand. Geprüft wurde, ob ein PR seinen Auftrag erfüllt, nicht ob der Auftrag zur Methodik passt.
2. **Werkzeug und Rolle passten nicht** (belegt als Aussage, #396 Punkt 4, #368): Der Lese-Chat arbeitete ohne Codeausführung und ohne Git. Markdown-Tabellen sind im Chat leichter zu schreiben als geprüfte Tabellendateien; CI und Belegrituale traten an die Stelle von Ausführung.
3. **Die Lehren und Werkzeuge waren projektgebunden** (belegt, #396 Punkt 1 und 3):
   - `LEARNINGS.md` liegt im Knau-Ordner und wird bei einem neuen Projekt nicht gelesen;
   - die S4-Werkzeuge heißen `regii5_*`;
   - `palaeography/` wurde am 08.09. als „legacy“ zurückgestuft (L020), ohne dass ein projektübergreifender Ersatz für die Sammlung von Vergleichsformen entstand.
4. **Der Plan setzte auf Durchsatz und ein Fehlermaß statt auf Vollständigkeit und Prüfung** (belegt, `ARBEITSPLAN.md` F1–F5, #396 Punkt 7): Seite für Seite mit 2–3 Zeilen Stichprobe und Wortfehlerschwelle; G2-Vollständigkeit und G3-Prüfung kamen im Plan nicht vor.
5. **Fehlende Foliierung** (Hypothese): Die Knau-Adresse ist Blatt + Zeile. Nr. 632 hat nur Bildnummern. Das hat vermutlich zum Ausweichen auf freie Markdown-Tabellen beigetragen. Ein echtes Hindernis war es nicht: Die Zuordnung ohne Foliierung existierte seit dem 29.10., und eine Zeilenadresse wie `0104R-A01` passt in die Spalte `line_ref`.

## 5 · Was das Repo dazu schon entschieden hatte

- **#394 (03.11.):** „Nr. 632 an die bestehende Methodik zurückbinden“. Mit Gegenüberstellung wie oben. **Eigentümerentscheidung: Ja.**
- **#397 (03.11.):** Umsetzung — Gesuch 0104R–0107L in `projects/ssta-20578-nr-632/transcription/first-reading/<Fläche>.tsv` mit den Knau-Spalten, Foliierung prüfen, Verlusttest, README; **#390 schließen**. Angehalten durch die Pause #399.
- **#396 (03.11.):** Analyse mit drei offenen Entscheidungen:
  - Ansicht aus den Tabellendateien statt #382;
  - Gegenlesung auf riskante Zeilen durch eine andere KI, dazu eine menschliche Stichprobe;
  - Rückbau von Regeln und Werkzeugen ohne Beitrag zur Edition.

## 6 · Eigener Fehler in diesem Durchgang (21.11.2026)

Ich habe heute **dieselben Verluste wiederholt**:
- **PR #417 legt erneut eine Markdown-Datei an** (`gesuch-0104R-0107L.md`) und „ersetzt #390“. #397 hatte genau das ausgeschlossen und das Knau-Format verlangt. #394 und #397 hatte ich vorher nicht gelesen.
- Die **Prüfung am Bild** lief ohne Zielmatrix, ohne vollständige Vergleichsstellen und ohne Prüftabelle (Abschnitt 1, Schritt 5). Daher der Fehlschluss „Ebersdorff“ und das zu sichere „B“.
- Die **Hinweise des Eigentümers** (Ebersdorf, Bahren) kannte ich vor meiner eigenen Lesung. Die Kontaminationsmatrix der Visitationsakten hätte Orts- und Namenskenntnis bis nach der Erstlesung gesperrt (vgl. L003).
- Die **Werkzeuge für Vergleichsformen** (`regii5_visual_retrieval.py`) habe ich nicht geprüft und nicht genutzt.

Was aus dem Durchgang tragfähig bleibt:
- der verlustfreie Abtrennungstest;
- die geprüften Prüfsummen;
- die Blindprobe mit Vergleich (6 Vergleichszeilen, Prüfer PASS);
- die einzeln begründeten Lesevorschläge als Rohmaterial für eine G3-Prüftabelle.

## 7 · Folgerung (Befund, keine Maßnahme)

Die Methode für das Erschließen ist im Repo vorhanden, erprobt und dokumentiert. Bei Nr. 632 wurde sie nicht weiterentwickelt, sondern umgangen. Die Ursachen liegen im Startweg, in der Rollen- und Werkzeuglage und in der Planlogik, nicht in der Methodik. Die Reparatur (D-022) braucht deshalb zuerst keine neue Methode. Sie muss:
- die vorhandene auf Nr. 632 anwenden; das hat der Eigentümer in #394 bereits entschieden, Umsetzung #397;
- die projektgebundenen Teile (Lehren, Vergleichswerkzeuge) für jedes Projekt erreichbar machen;
- dafür sorgen, dass der Start einer Arbeit am Bestand beginnt.
