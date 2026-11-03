# Infrastruktur und zentrale Systemfehler (Analyse #405, dritter Chat)

Stand: 03.11.2026, abends · Claude, Prüfer · Branch `analysis/ursachen-405-erhebung` (#408). **Nicht für `main`.** Keine Lösungen und keine Maßnahmen.

**Zweck (Eigentümer, 03.11.2026):** Grundlage für den Umbau (B) und die Weiterführung von Nr. 632 (C). Der Bedienmodus mit Stichworten bleibt, solange er ans Ziel führt.
**Zu prüfende Hypothese (Eigentümer):** Es gibt grundlegende Probleme der Infrastruktur, also zentrale Systemfehler, die sich gegenseitig aufschaukeln und verstärken.
**Rahmen (vom Chat festgelegt):** Die Karte umfasst nur die Infrastruktur: wer womit arbeitet, wo der Stand liegt, wie Übergaben, Prüfungen und Bildzugriff laufen. Auf dieser Karte wird die Hypothese gegen Gegenhypothesen geprüft.

**Belegstand:** *belegt* heißt, die Fundstelle wurde gelesen; *Aussage* heißt, ein Beteiligter sagt es (fast alle Texte stammen von KI-Chats unter dem Konto `esany`); *Deutung* ist die eigene Lesart dieses Chats; *offen* heißt, nicht geprüft.

## 1. Leseprotokoll

**Ganz gelesen:**
- Leitziel, `AGENTS.md` (als Systemhinweis), `SPICKZETTEL.md`, `README.md`, `DECISIONS.md` (D-001 bis D-021)
- `methodology/workflow.md`
- `projects/ssta-20578-nr-632/ARBEITSPLAN.md`
- #405, #404, #398, #399, #201, #368 und #353, jeweils mit allen Kommentaren
- #297, nur der Text ohne die 30 Kommentare; davon nur der Kommentar vom 08.10. über lokale Commits
- #389 mit Kommentaren
- #355, die ersten zwei Kommentare
- ChatGPT-Bericht #401 (`systemaudit-2026-11-chatgpt.md`)
- auf #408: `analyse/ansatz.md`, `analyse/pilot-w1.md`, `analyse/struktur.md`

**Nur gezielt gesucht** (Wortsuche, kein Volltext):
- „Codex“, „ChatGPT Work“, „connector“ in den Issue-Exporten
- Zeilen aus #123, #162, #166, #171 und #310

**Nicht gelesen:**
- die übrigen neun Dateien in `methodology/`
- `engineering/` und `requirements/`
- alle `STATUS.md` und `LEARNINGS.md`
- die Kommentare von #297 außer dem genannten
- der Rest von #355
- #358, #359, #375, #230, #225, #280
- `wissensarbeit` und `design-lab`
- alle Lesungen von Nr. 632; dieser Chat ist für alle Seiten blind

## 2. Karte der Infrastruktur

### 2a. Wer arbeitet womit

| Akteur | kann | kann nicht | Beleg |
|---|---|---|---|
| Astra (Hauptchat, normaler ChatGPT-Chat, seit 30.10.) | Repo über den GitHub-Connector lesen und schreiben; das PDF als Projektquelle sehen | Code ausführen, Git nutzen, Branches löschen, Tags setzen | belegt: #368 B1/B2; ARBEITSPLAN, Nachtrag „Chat-Rollen“ |
| Gegenlese-Chat (frischer Chat im ChatGPT-Projekt) | wie Astra, ohne Kenntnis der Lesung | wie Astra | belegt: ARBEITSPLAN, Nachtrag „Gegenlesung vorab“ |
| Claude (Prüfchat, Container) | Code, Git, REST-API, Merge auf `main` | Bilder nur, wenn das PDF als Anhang kommt | belegt: #368, Übergabe 31.10. („braucht … das PDF als Anhang“) |
| ChatGPT Work und Codex (bis Anfang Oktober Hauptweg) | Code ausführen, lokale Checkouts, PDF rendern (z. B. 600 dpi) | – | belegt: #123 (Rendern, lokale Tests bei Knau); #297, Kommentar 08.10. |
| GitHub CI (`validate`, `nr632-gegenlesung`) | Form, Commits und Tests prüfen | Lesungen beurteilen; feststellen, wann ein Chat etwas geöffnet hat | belegt: ARBEITSPLAN, Nachtrag #368 P1/#379 |
| Eigentümer | Stichwort je Durchgang, Entscheidungen, Chats öffnen | Handschrift lesen, Code beurteilen | belegt: Leitziel, SPICKZETTEL §1 |

### 2b. Wo der Stand liegt

- **Nur als Text auf GitHub** (D-006). Jeder Chat beginnt ohne Gedächtnis und muss den Stand erst lesen.
- **Pflichtlektüre beim Start:** `AGENTS.md` mit 345 Zeilen und `methodology/` mit 2.331 Zeilen (belegt, `struktur.md` §4). Dazu kommen Spickzettel, Arbeitsplan, STATUS und die Übergabe in Issue-Kommentaren.
- **Der STATUS von Nr. 632 auf dem Forschungsbranch** umfasst rund 51.000 Zeichen (Aussage, #401 §4; hier nicht nachgemessen).
- **Der Stand ist auf mehrere Orte verteilt** (belegt):
  - `main`: Methodik, Plan, Spickzettel
  - Forschungsbranch #359: Lesungen, STATUS
  - Branch `review/nr632-gegenlesung-vorab`: Gegenlesungen, Warteschlange
  - Issue #368: Übergabe des Prüfchats
  - Labels: Aufträge

  `main` und der Forschungsbranch widersprechen sich beim Auftrag. Auf `main` steht „kein aktiver Scope“, auf dem Branch der Auftrag zur Volltranskription (Aussage, #401 §5).

### 2c. Wie Übergaben laufen

- Zwischen den Chats gibt es keinen Kanal. Jede Übergabe ist ein Text im Repo, und erst ein Stichwort des Eigentümers startet den nächsten Chat (belegt: SPICKZETTEL §1).
- Versuche mit Slack haben die Lücke nicht geschlossen. Rückmeldungen erreichten keinen Chat von selbst (belegt: #162, #171).

### 2d. Wie Bilder zugänglich sind

- Die PDFs (97 und 201 MB) liegen außerhalb des Repos als Projektquelle der Chat-Projekte (belegt: ARBEITSPLAN, Abschnitt Parameter; SPICKZETTEL §2c).
- Über den Connector lassen sich private Bildanhänge nicht abrufen. Bei Knau hat der Eigentümer das PDF selbst geliefert (belegt: #166, Pilot W1).
- Ein Werkzeug für Bildausschnitte ist vorgeschlagen, bräuchte aber Codeausführung. Darüber ist nicht entschieden (belegt: #389).
- Ob und wie Astra Ausschnitte vergrößert: **offen.**

### 2e. Wie die Ausführungsumgebung wechselte

| Zeit | Umgebung | Auslöser | Beleg |
|---|---|---|---|
| bis 08.10. | Work und Codex mit lokalen Checkouts | – | belegt: #297, Kommentar 08.10. |
| 05.–08.10. | Acht lokale Commits erreichen GitHub nie | Plattform wählt lokalen Stand | belegt: ebd. |
| ab 08.10. | Work und Codex nur noch über den Connector | #310, Auftrag des Eigentümers | belegt: #310 |
| ab 30.10. | normaler Chat ohne Code; Work und Codex nur auf ausdrückliche Anweisung | Kontingent schonen (#355, 30.10.) | belegt: #355 Kommentar 2; ARBEITSPLAN |
| ab 30.10. | Claude als Prüfer mit Git, Astra als Bauer ohne Code | Empfehlung in #353 (verfasst vom Orchestrator-Chat von design-lab) | belegt: #353 („Wer baut? Empfehlung: Astra baut, Claude prüft“) |

## 3. Zentrale Systemfehler (Kandidaten)

### Z1 · Die Fähigkeiten für einen Arbeitsschritt sind auf mehrere Akteure verteilt
- **Was gebraucht wird:** Für eine geprüfte Seite braucht es das Bild, das Lesen, das Speichern, die Prüfung, den Merge und das Aufräumen.
- **Wer es hat:** Kein Akteur hat alles (2a). Astra hat Bild und Schreibzugang, aber keinen Code. Claude hat Code und Git, aber das Bild nur als Anhang. CI hat Code, aber kein Urteil.
- **Folgen (belegt):**
  - Werkzeuge liefen im echten Durchgang nie (#368 B1).
  - Prüfungen wurden in die CI verlagert, mit eigenen Fehlalarmen (#375; Reibungstabelle W0 laut #405 P8, hier nicht gelesen).
  - Aufräumen, Merge und Bildbeschaffung landen bei Claude oder beim Eigentümer.

### Z2 · Der Stand liegt als wachsender Text in einem Kanal, der nicht für kalte Starts gebaut ist
- **Ausgangslage:** Jeder Chat startet ohne Gedächtnis (D-006). Die Pflichtlektüre ist groß und wächst (2b).
- **Folgen:**
  - selektives Lesen und ungekennzeichnetes Kürzen (belegt: #404, Schritte 1–2)
  - Vorhandenes wird übersehen und neu gebaut (belegt als Einzelfälle: #394; #355, Kommentar 1 nennt für die „neuen“ Werkzeuge direkte Vorgänger wie #64, #139, #142, #95 und ein vorhandenes Werkzeug `regii5_evidence_packet.py`)
  - Übergaben werden als Wahrheit übernommen (Aussage: #401 RC4/RC6)
- **Verteilung:** Der Stand liegt auf drei Branches und in Issues. Ein frischer Chat muss diese Teile erst richtig zusammensetzen (belegt: 2b).

### Z3 · Die Umgebung wechselte zweimal, das System wurde nicht nachgezogen
- **Wofür das Werkzeug gebaut ist:** Das Werkzeug setzt Codeausführung voraus, etwa `tools/check.py` „shared local/CI“, die Engineering-Resolver, `work_return.py` und `outcome_context.py` (belegt: README).
- **Was danach geschah:**
  - Mit #310 (08.10.) entfiel der lokale Weg.
  - Am 30.10. entfiel der Code im Hauptchat ganz.
  - Ein Abgleich, welche Werkzeuge und Regeln damit nicht mehr ausführbar sind, ist in den gelesenen Quellen **nicht** zu finden. Ob es ihn woanders gibt, ist offen.
- **Folge (belegt):** Die Lücke zeigte sich erst im Betrieb (#368 B1) und wurde durch neue Abläufe überbrückt (#375, CI-Job, Meldedatei, Vergleichszeile).
- **Deutung:** Das Repo trägt die Annahmen einer Umgebung, die es nicht mehr gibt.

### Z4 · Gegenmittel werden als Text oder als neuer Ablauf gebaut, und Text wirkt im Modell nicht verlässlich
- **Text wirkt nicht verlässlich:** Regeln standen im Kontext und wurden trotzdem verletzt (belegt: #404 M6; Aussage: #297 H1/P8).
- **Gegenmittel sind fast immer neue Regeln oder Abläufe:**
  - #378, #380, #385, #386, #391, #393, #395 („alles Ablaufregeln“, belegt: Übergabe in #368 vom 03.11.)
  - #371 (belegt: #368)
  - #169 (belegt: Pilot W1)
  - #310 (belegt)
  - laut #401 auch die PRs #366–#395 (Aussage)
- **Wirkung:** Jedes Gegenmittel vergrößert Z2.

### Z5 · Abschlusssignale sind billig, das Ergebnis an der Quelle ist teuer
- **Was billig ist:** CI, Merge, eine geschlossene Issue und ein „PASS“ lassen sich in jeder Umgebung erzeugen.
- **Was teuer ist:** Eine geprüfte Zeile braucht Bild, Lesen und eine unabhängige Gegenlesung, also alle Fähigkeiten aus Z1.
- **Belegt:** #297 §6 (#225 geschlossen ohne eigene Abnahme T11); ARBEITSPLAN, Nachtrag #379 („kein … Wahrheitsprüfung“).
- **Deutung:** Die Infrastruktur macht die Ersatzsignale leichter erreichbar als das Ergebnis.

## 4. Verstärkung (Deutung, aus belegten Einzelgliedern)

```text
Umgebung oder Kontingent ändert sich (Z3)
  → eine Fähigkeit fehlt am Ort der Arbeit (Z1)
  → Ausgleich durch Regel, Ablauf, Übergabe oder CI-Job (Z4)
  → mehr Text, mehr Orte, mehr Pflichtlektüre (Z2)
  → kalter Start liest selektiv, übersieht Vorhandenes, übernimmt Übergaben
  → Fehler oder Leerlauf; der Eigentümer entdeckt ihn (P10)
  → neue Regel oder neuer Ablauf (Z4) …
und daneben:
  Ersatzsignale grün (Z5) → Plan wirkt erfolgreich → Stillstand fällt spät auf (E1, „einen Klick vor der Weltherrschaft“)
```

Jedes Glied ist einzeln belegt. Dass sie in dieser Reihenfolge **als Schleife** wirken, ist eine Deutung. Prüfbar wäre sie an der Zeitfolge der Wochen 26.10. bis 03.11.: Auf jede Fähigkeitslücke müsste ein neuer Ablauf folgen und darauf ein Vorfall. Das ist nicht geprüft.

## 5. Gegenhypothesen

| Gegenhypothese | Was dafür spricht | Was dagegen spricht | Stand |
|---|---|---|---|
| G1 Das Modellverhalten ist die eigentliche Ursache (vorschneller Abschluss, Flicken, Solutionism), unabhängig von der Infrastruktur. | #404 und #405 3b geschahen im Claude-Container, **dem nichts fehlte**: Code, Git, Zeit. Z1 und Z3 können diese Fälle nicht erklären. | Z2 wirkt auch dort: Pflichtlektüre und Grundstoff übersteigen den Kontext (#405 P11), und das lädt zum Überfliegen ein. | **teilweise gestützt.** Das Verhalten ist ein eigener Faktor. Die Infrastruktur verstärkt es, erzeugt es aber nicht allein. |
| G2 Die Lesearbeit selbst ist schwer; die Wand ist fachlich. | Blinde Proben zeigen Fehler (belegt: #368, #389 Punkte 2–3). | Damit lässt sich schlechte Lesequalität erklären, nicht aber das Wachstum der Abläufe und die Wellen. Die übernommenen PRs vom 01.–03.11. sind „alles Ablaufregeln“ (belegt: Übergabe in #368). | **gestützt für die Lesequalität, nicht für die Systemdynamik** |
| G3 Es fehlt die nächste Forschungsfrage (Pilot W1, H-F eng). | Belegt für den Umschlag am 14.09. (vorbelastet, `pilot-w1.md`) | Für Nr. 632 gab es einen Auftrag (#358, Plan vom 31.10.); trotzdem dieselbe Dynamik. | **gestützt für Knau, nicht für Nr. 632** |
| G4 Knau lief besser, weil die Infrastruktur dort passte (Work und Codex mit Code, Rendern in 600 dpi, lokale Tests). | #123 (belegt: Rendern und lokale Tests bei Knau) | Knau hatte zudem Paralleltexte als Prüfstein (Aussage: #398, Bericht Claude, verworfen). Beide Faktoren sind nicht getrennt. | **offen; ein entscheidender Prüfpunkt für C** |

## 6. Ergebnis, soweit gelesen

- **Die Hypothese des Eigentümers ist in einer bestimmten Form gestützt.** Es gibt zentrale Systemfehler der Infrastruktur, vor allem Z1, Z2 und Z3. Sie sind belegt, wirken aufeinander, und jedes Gegenmittel verstärkt sie (Z4). Z5 verdeckt die Wirkung.
- **Nicht gestützt ist, dass die Infrastruktur allein ursächlich ist.** Dieselbe Fehlerfamilie tritt in einer vollständig ausgestatteten Umgebung auf (G1). Die Lesequalität hat einen eigenen fachlichen Anteil (G2).
- **Neu gegenüber den vorhandenen Analysen:**
  - **Z3:** Der zweimalige Wechsel der Umgebung (08.10. und 30.10.) wurde nicht nachgezogen. #297, #401 und #404 nennen die Rollen- und Werkzeuglücke (P9), aber nicht den Wechsel als Auslöser.
  - Die Rollenverteilung ab 30.10. stammt aus einer Empfehlung des design-lab-Chats (#353). Ob die Umgebung sie trägt, wurde vorher nicht geprüft.

## 7. Offen und als Nächstes prüfbar (keine Maßnahmen)

1. **G4:** Wie war die Umgebung bei Knau G2–G4 genau? Wer hat gelesen, mit welchem Bildzugang und mit welchen Ausschnitten? Zu klären aus #64, #96–#99, #115, #123, `projects/ega-reg-ii-5-knau/STATUS.md` und LEARNINGS.
2. **Z3:** Gibt es einen Abgleich nach dem 08.10. oder dem 30.10., welche Werkzeuge und Regeln nicht mehr ausführbar sind? Zu prüfen in #310 (Volltext), #355 (Rest), #358, `engineering/configuration.json`.
3. **Schleife in §4:** Zeitfolge 26.10.–03.11. an #358, #359 (Kommentare) und den PRs #366–#395 prüfen.
4. **Astras Bildzugang:** Wie arbeitet der Hauptchat konkret am Bild (Ausschnitte, Auflösung)? Aus dem STATUS auf #359, nur die Arbeitsweise, ohne Lesungen.
5. **Vergleich:** design-lab und wissensarbeit auf dieselben fünf Kandidaten Z1–Z5 hin lesen.
