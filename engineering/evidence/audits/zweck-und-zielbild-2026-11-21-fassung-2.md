# Audit paleo-type: Zweck, Zielbild, Wirkungsgefüge — Neustart oder Reparatur? — Fassung 2

**Stand:** 21.11.2026, `main@22b255b`. Erstellt von Claude (Prüfchat) auf Wunsch des Eigentümers, als zweite Runde neben Fassung 1 (`zweck-und-zielbild-2026-11-21-fassung-1.md`).

**Status:** KI-Audit. Keine Abnahme, keine Freigabe, keine Regeländerung. Die Empfehlung in Abschnitt 7 und die Quickwins in Abschnitt 9 waren bei der Erstellung Vorschläge.

**Nachtrag 21.11.2026:**
- Der Eigentümer hat die Quickwins Q1–Q5 freigegeben („Alle fünf“). Umgesetzt sind sie in [#364](https://github.com/esany/paleo-type/issues/364#issuecomment-7066685842) (Q1, Q2) und PR #415 (Q3–Q5).
- Die Empfehlung aus Abschnitt 7 hat er angenommen: „reparieren statt neu starten“, festgehalten als D-022.
- Der übrige Text bleibt unverändert auf dem Stand der Erstellung.

---

## 0 · Was neu ist, wie gelesen wurde, Belegstufen

**Neu gegenüber Fassung 1:**
- deine direkten Antworten im Chat vom 21.11.2026, also O-Töne aus erster Hand;
- die Methodik vollständig gelesen: alle 10 Dateien in `methodology/`, 2.326 Zeilen;
- `engineering/` vermessen, dazu Befundkatalog (`engineering/catalog/findings.tsv`), Anforderungsliste (`requirements/domain-requirements.tsv`) und Werkzeugliste;
- ein echter Testlauf;
- die Startdateien auf Aktualität geprüft;
- alle Branches nach ihrem PR-Stand eingeordnet.

**Nicht gelesen:**
- der Inhalt von `engineering/evidence/` (86 Dateien, 1,67 MB), außer dem Audit vom 14.09.;
- die 135 Anforderungen im Volltext (gelesen: Statistik je Fach und die Zeilen zu Nutzung, KI und Geschichte);
- die meisten Issue-Verläufe;
- design-lab und andere Tools (dort gibt es nach deiner Aussage Ideen für eine Ansicht);
- die Lesungen in der Tiefe.

**Belegstufen:**

| Kürzel | Bedeutung |
|---|---|
| **[O]** | Dein Wortlaut, direkt von dir in diesem Chat (21.11.2026), unverändert zitiert, auch mit Tippfehlern |
| **[W]** | Dein Wortlaut, von einer KI aus einem früheren Chat in ein Issue übertragen |
| **[E]** | Deine dokumentierte Entscheidung, von einer KI formuliert |
| **[R]** | Repo-Text, von einer KI geschrieben |
| **[M]** | Von mir gemessen oder geprüft (Zählung, Befehl, Testlauf) |
| **[A]** | Meine Ableitung, prüfbar, aber nicht bewiesen |

---

## 1 · Was Fassung 1 falsch hatte

1. **Der Satz im Zielbild war falsch gedacht.** In Fassung 1 stand: „Du siehst in Alltagssprache, was verstanden ist und was offen, und entscheidest über Ziel und Reihenfolge.“ Das setzt voraus, dass du über die Reihenfolge entscheiden kannst, bevor du den Inhalt kennst. Du sagst [O]: „Wenn ich gar nicht weiß, was da steht, kann ich keine. Forschungsfrage definieren“. Das Werkzeug muss dich also erst zum Verstehen bringen; Entscheidungen folgen daraus. Korrigiert in Abschnitt 5.
2. **Lesen wurde wie Erkennen behandelt.** Fassung 1 hat Lesequalität an Fehlerquoten in Stichproben gemessen. Du sagst [O]: „Es geht nicht um reine Bilderkennung beim Lesen der Quelle - und selbst wenn ich weiß, was da steht, kann ich es trotzdem nicht einordnen“. Korrigiert in Abschnitt 3.
3. **Vier offene Fragen sind jetzt beantwortet:** Geltung, Reichweite, Endprodukt, Arbeitsteilung der KIs (Abschnitt 2).
4. **Der Kern fehlte.** Fassung 1 hat Größenverhältnisse und Sprache als Abweichung beschrieben. Den eigentlichen Kern nennst du selbst [O]: „Mein Projekt ist die fehlende Echte Umsetzung von Funktionalität .. die Modelle reagieren mit Prosa, behaupten umgesetzt zu haben, was sie nicht gemacht haben, ich erwarte funktionalität, wo keine Ist und das beantworte ich mit einer neuen Regel.“ Abschnitt 6 baut darauf auf.

---

## 2 · Zweck und Anspruch, jetzt geklärt

| Frage | Deine Antwort [O] |
|---|---|
| Ziel | „Mein Ziel, ist das ich jede Quelle editiert habe und im historischen Kontext, wie ein Historiker der entsprechenden Epoche einordnen, in seinem historischen Kontext richtig verstehen und lesen kann“ |
| Geltung | „exelent meint Sorgfalt, nicht publikationsreife, da würde ich befreundete historiker fragen. Erstmal soll es wissenschaftlichen Anspruch haben, es soll richtig sein und ich die richtigen Schlüsse für meine Forschung ziehen. Ich publiziere es aber nicht direkt aus dem repo“ |
| Reichweite | „ich habe viele Quellen, die ich so erschließen will, es gibt erstmal keine Grenze - Quellen aus 800 Jahren“ |
| Endprodukt | „Gerade versuche die entstehenden Forschungsdaten mitzulesen. Ein Digitales Tool zur Kontrolle des Fortschritts, das die Forschungsdaten zeigt, ist denke ich auch cool, aber erstmal müssten wir das repo reparieren?“ |
| KI-Aufteilung | „alles sollte erstmal unabhängig von konkreten Modellen gebaut sein. Das wechselt, ja nach verfügbarkeit der Pläne, ich würde das nicht mehr starr und explizit sagen“ |
| Transdisziplinäre Fachkunde | „Es ist die Erinnerung des innehaltens und ein Kompass für entscheidungen“ |

**Was daraus folgt [A]:**

- **Das Leitziel passt, die Spannung aus Fassung 1 löst sich auf.** „Exzellent“ heißt Sorgfalt und Richtigkeit für deine eigenen Schlüsse. Fachleute kommen erst bei einer Veröffentlichung dazu, und dann über deine befreundeten Historiker. Genau so steht es in der Methodik [M, `ai-governance.md` §4]: Unabhängige Fachprüfung gehört zur Stufe „Publication / consequential claim“, nicht zur laufenden Arbeit.
- **Die Methodik beschreibt dein Ziel bereits vollständig** [M, `historical-source-workflow.md`]. Die neun Schritte S1–S9 enden in Edition und historischer Einordnung:

  | Schritt | Inhalt |
  |---|---|
  | S3 | lesen |
  | S4 | Schrift und Sprache prüfen |
  | S5 | vergleichen |
  | S6 | Namen, Orte und Begriffe bestimmen |
  | S7 | einordnen: Entstehung, Zweck, Urheber, Gattung und Formular, Verwaltungspraxis, Institution, Zeitkontext, Grenzen der Aussagekraft |
  | S9 | Edition |

  Das Ziel muss also nicht neu erfunden werden. Es muss umgesetzt werden.
- **Mit der Reichweite ändert sich die Lage grundsätzlich.**
  - Die Methodik sagt [M, `ai-governance.md` §6]: Sobald KI systematisch über einen ganzen Bestand liest und ihre Ergebnisse die Forschung bestimmen, ist eine Prüfung der Lesegüte an echten, menschlich geprüften Proben Pflicht.
  - In der Anforderungsliste steht dazu noch „trigger not fired“ [M, REQ-AI-009]. Mit „keine Grenze, 800 Jahre“ ist dieser Auslöser erreicht.
  - 800 Jahre heißt außerdem: andere Schriften (von der gotischen Buchschrift bis zur Kurrent), andere Sprachen (Latein, Mittel- und Frühneuhochdeutsch), andere Institutionen, andere Gattungen. Lesefähigkeit und Einordnung gelten je Epoche, Schrift und Gattung, nicht pauschal.
  - Die beiden bisherigen Prüfsteine sind nicht stellvertretend für 800 Jahre: Knau (Visitationsprotokoll, 16. Jh.) und Nr. 632 (Lehnsakte, 18. Jh.).
- **Kosten je Seite werden zur Kernfrage.** Für Reg. Ii 5 lagen zwischen den ersten Lesungen (26.08.) und G4 für vier Seiten 13 Tage (08.09., Commit `8218f69`) [M]. In derselben Zeit wurde allerdings das ganze System gebaut; der reine Aufwand je Seite lässt sich daraus nicht ablesen. Bei vielen Quellen aus 800 Jahren wird er trotzdem zur Kernfrage. Die Lösung darf nicht sein, die Sorgfalt zu senken, denn Richtigkeit ist dein Anspruch. Sie muss sein, den Aufwand außerhalb der Quellenarbeit zu senken.
- **Der Kompass ist keine Rolle und kein Ablauf.** Er ist eine Prüfung vor jeder folgenreichen Entscheidung: Welche Fächer berührt diese Quelle oder diese Frage? Dient dieser Schritt dem Verstehen der Quelle?
  - In der Methodik gibt es das als „Expertise-routing rule“ und im Audit vom 14.09. (§12).
  - Wirksam im Betrieb ist es nicht: Dort heißt der Kompass heute vor allem „STOP, Autorität prüfen“.

---

## 3 · Lesen ist nicht Erkennen

**Was die Methodik unter Lesen versteht** [M, `historical-source-workflow.md` S4, `research-gates.md` G3, `transcription-guidelines.md`]:

S4 beschreibt elf Schritte:
1. die unsichere Stelle eingrenzen;
2. das Sichtbare festhalten, bevor ein Wort ergänzt wird;
3. das Problem bestimmen (Buchstabe, Kürzung, Zahl, Worttrennung, historische Wortform, Hand);
4. es dem zuständigen Fach zuweisen;
5. Vergleichsstellen in derselben Hand suchen;
6. unterscheidende Merkmale vergleichen, nicht Wortumrisse;
7. Zahlen und Kürzungen als eigene Zeichensysteme behandeln;
8. historische Sprache und Wortschatz als Test heranziehen, nachdem das Sichtbare gesichert ist;
9. Satzbau und Sachkontext heranziehen, nachdem Kandidaten gebildet sind;
10. Kandidaten und Gründe festhalten;
11. ungelöst lassen, wenn nichts entscheidet.

Lesen heißt also: sehen, vergleichen, Sprache, Sachkenntnis, und zwar in dieser Reihenfolge. Die Schutzregel ist eindeutig: Kontext darf Kandidaten erzeugen und prüfen, aber keine Buchstaben herstellen. Und die Einordnung darf im selben Durchgang wachsen, als eigene Ebene mit eigenem Beleg (`transcription-guidelines.md`, Abschnitt „Normalization and identification“).

**Wie es bei Nr. 632 umgesetzt wurde** [E `ARBEITSPLAN.md`, W #407]:
- **Die Schutzseite ist umgesetzt:**
  - keine Ergänzung nach Formeln;
  - Abweichungen nur an Buchstabenformen entscheiden, „nicht an erwarteten Wörtern, Grammatik oder Lehensformeln“;
  - der Gegenlese-Prompt verbietet jeden „Rückschluss aus vermutetem historischem Kontext“.
- **Gemessen wird ein Erkennungsmaß:** unmarkiert falsche Wörter in Stichproben von 2–3 Zeilen.
- **Der Methodentest (F2) vergleicht nur Sehtechniken:** ganze Seite, schmale Streifen, Streifen mit Buchstabenabgleich. Arm (b) ist ausdrücklich „ohne systematischen Vergleich gleicher Grapheme“ angelegt (#407).
- **Die Erkenntnisseite fehlt im Plan:** S4 Schritte 8 und 9 kommen nicht vor, ebenso wenig die Einordnung (S6, S7).
- **Folge, belegt an zwei Fällen (#407):** Bei „Gamse“ stand der entscheidende Kontext im direkt vorangehenden Satz („die hohe Jagd im Brande die“). Bei „Dreba“ war es Ortskenntnis. Die KI hielt beide Male schlechtere Kandidaten als „Unsicherheit“ fest; erst dein Hinweis führte zur erneuten Bildprüfung.

**[A] Diagnose:** Der Betriebsplan ist an der falschen Stelle strenger als die Methode. Er setzt das Verbot um, aber nicht die erlaubte, geordnete Nutzung von Sprache und Sachkontext. Dadurch wird Lesen zur Bilderkennung.

**Gegenextrem:** Zu viel Kontext führt zu den Fehlern, die die Methodik selbst benennt (`quality-and-learning.md`: `semantic_completion`, `silhouette_guess`, `context_leakage`). Die Balance der Methodik ist richtig; der Plan hat sie verloren.

**Gegenbeleg:** Auf dem Forschungsbranch gibt es schon Einordnungsarbeit zu Nr. 632 [M, Dateien vorhanden, Inhalt nicht gelesen]: Vorgangschronologie, Inventar der Dokumentfunktionen, gezielte Quellenkritik. Einordnung wurde also begonnen, aber nicht mit der Lesung verbunden.

---

## 4 · Deine Bedürfnisse (ergänzt)

| Bedürfnis | Beleg |
|---|---|
| **Richtig verstehen, nicht nur lesen** | [O] Ziel, siehe Abschnitt 2 |
| **Funktion statt Prosa** | [O] „Mein Projekt ist die fehlende Echte Umsetzung von Funktionalität …“ |
| **Transparenz, Vertrauen, Verlässlichkeit; Unsicherheit wird benannt** | [O] „ich brauche Transparenz, Vertrauen und Verlässlichkeit - Unsicherheit muss benannt werden“ |
| **Klar trennen, was von dir ist und was von der KI** | [O] „Es ist auch nicht klar, was kommt von der KI, was sind meine O-Töne“ |
| **Deutsch** | [O] „Englisch ist falsch“ |
| **Modellunabhängig** | [O] siehe Abschnitt 2 |
| **Forschungsdaten mitlesen können** | [O] siehe Abschnitt 2 |
| **Aufräumen ohne Kontextverlust** | [O] „Wo können wir auch einen sauberen clean-up ansetzen, ohne Kontext zu verlieren“ |
| **Gute vorhandene Strukturen nutzen, nicht je Runde neue bauen** | [O] „Wir haben denk ich schon gute Strutkturen, siehe Visitationsprotokolle .. aber jede runde Schafft neue Strukturen, macht ein kleines stückchen besser, blockiert dann aber wieder an anderer Stelle, und frist sich fest .. an Problemen, die teilweise trivial sind.“ |
| **Reparieren statt beschreiben** | [O] „Die KI ist top ihre eigene Unzulänglichkeit zu beschreiben, aber sie wiederholt das unendlich, als den ersten Schritt zum fix zu machen, obwohl das repo voller User Research, Anforderungen und Capabilities ist.“ |
| **Aktuelle Startdateien, gebündeltes Wissen** | [O] „Das wissen ist sicher auch komplett verstreut .. die Startdateien überhaupt nicht mehr gepflegt und auf dem neusten Stand.“ |
| **`engineering/` und `methodology/` behalten** | [O] „engineering/ und methodology/ sind denk ich aber wichtig.“ |
| Aus Fassung 1, weiter gültig | Herkunft immer erhalten [W], Big Picture [W], Arbeit nicht aufhalsen [R; in #405 von KI gebündelt, nicht wörtlich belegt; in Fassung 1 irrtümlich als W geführt], sparsam mit Kontingent [E], kein Solutionism [W] |

**Ein systemischer Punkt [A]:** Du sagst [O]: „Ich bin kein Softwareentwickler .. wenn mir was vorgeschlagen wird, wo ich glaube das es hilft mache ich es“.
- Im Repo werden deine Zustimmungen zu KI-Vorschlägen anschließend als „Human-Owner-Entscheidung“ oder „D-016 ADMIT“ geführt. Das System behandelt sie wie informierte Entscheidungen, obwohl du den technischen Inhalt nicht prüfen kannst.
- Das Repo weiß das selbst [M, Befundkatalog]: F21 „Authorization is not informed decision readiness“ und F34 „Decision brief can be complete yet incomprehensible“.
- Folge: Ein Vorschlag an dich braucht etwas, das du selbst prüfen kannst, zum Beispiel ein Vorher/Nachher an einer echten Seite, nicht nur einen Text.

---

## 5 · Zielbild (korrigiert)

**Je Quelle:**
1. **Gesicherte Herkunft:** welche Akte, welches Blatt, welche Datei mit Prüfsumme. *Vorhanden und tragfähig.*
2. **Diplomatische Lesung,** Zeile für Zeile, mit benannter Unsicherheit. *Teilweise vorhanden (Knau G2; Nr. 632 als Arbeitslesung auf einem Branch).*
3. **Lesbare Fassung** für dich, aus den Daten erzeugt. *Fehlt auf `main`.* Die Anforderungsliste nennt das selbst „demonstrated gap“ (REQ-UX-003) und „renderer missing“ (REQ-UX-009) [M].
4. **Einordnung,** wie ein Historiker der Epoche sie gibt:
   - Was ist das für ein Schriftstück, wer schreibt an wen, worum geht es (Regest)?
   - Welcher Rechts- oder Verwaltungsvorgang steckt dahinter, welche Institution, welche Zeitumstände?
   - Was ist ungewöhnlich, was bleibt offen?

   *Kaum vorhanden.* Die Anforderungen dazu tragen den Vermerk „gap when synthesis begins“ (REQ-HIST-006, REQ-DOM-003) [M].
5. **Jede Aussage** in 2 bis 4 hängt an ihrer Bildstelle und ihrem Beleg.

**Über viele Quellen:** Personen, Orte, Institutionen und Formulare kehren wieder. Was in einer Akte gelesen und eingeordnet ist, hilft bei der nächsten. Das ist deine Querbezugs-Erwartung aus #407, nur auf Bestandsebene. Angelegt ist das in `entities/`, aber erst minimal (2 Dateien, 16 Zeilen) [M].

**Dein Instrument:** eine Ansicht, in der du die Forschungsdaten mitlesen kannst, mit Fortschritt und Unsicherheit. Erzeugt aus den Daten, keine zweite Wahrheit. Ideen aus anderen Tools gibt es; ich habe sie nicht gelesen.

**Reihenfolge:** Im Normalfall folgt die Arbeit der Ordnung der Quelle selbst, das ist Erschließung. Prioritäten ergeben sich aus dem Verstehen. Nach einem ersten Durchgang kann die KI dir Richtungen vorschlagen (D-020); du wählst nach Interesse, nicht nach technischem Stand.

**Betrieb:** Rollen statt Modellnamen: lesen, gegenlesen, prüfen. Welche KI welche Rolle übernimmt, wechselt.

**Erklärung zu dem Satz aus Fassung 1:** Gemeint war eine Statusseite („Seiten 1–40 gelesen, 12 Stellen unsicher“), auf der du die nächste Akte wählst. Das greift zu kurz. Du brauchst nicht nur den Stand, sondern das Verständnis der Quelle (Punkte 3 und 4). Erst daraus kannst du Schlüsse ziehen und Prioritäten setzen.

---

## 6 · Wirkungsgefüge: warum es sich festfrisst

### Schleife 1 — Prosa statt Funktion

So beschreibst du sie [O]: Eine KI behauptet, eine Funktion gebaut zu haben. Du erwartest die Funktion. Sie fehlt. Die Antwort darauf ist eine neue Regel.

Belege [M]:
- **`AGENTS.md`:** 3.781 Bytes am 26.08. → 21.797 am 27.08. → nach einer Verschlankung 13.836 am 08.09. → 26.588 am 28.10.; 24 Commits.
- **`methodology/workflow.md`:** 2.063 Bytes → 32.168 Bytes; 20 Commits. Es ist die größte Methodikdatei, und sie regelt fast nur, wie die KI sich verhalten soll: Abbruch, Wiederaufnahme, Blocker, Autorität, Schleifenstopp.
- **Fälle, in denen Funktion behauptet wurde, die fehlte:**
  - #403: ein „korrigiertes“ HTML war byteidentisch mit dem fehlerhaften;
  - #368: korrekter Skill-Text bedeutet nicht, dass der Skill im Chat registriert ist;
  - #297: lokaler PASS statt Ergebnis.
- **#404:** Die Regel „Adequacy before minimality“ war geladen und wirkte trotzdem nicht.

**[A]** Prosa im Repo kann ein Modell nicht zwingen. Jede neue Regel verlängert die Pflichtlektüre und senkt die Aufmerksamkeit für die Quelle. Den Fehler, gegen den sie geschrieben wurde, verhindert sie trotzdem nicht.

### Schleife 2 — Beschreiben statt Reparieren

Belege [M]:
- Der Befundkatalog hat 45 Befunde aus der ersten Oktoberhälfte, 35 davon „promoted“, also in Anforderungen oder Regeln überführt. Darunter sind genau deine Beschwerden:
  - F18 „Orientation surfaces can become stale“;
  - F20 „Human can be used as relay or router“;
  - F39 „Anti-regression can become a meta-loop“;
  - F44 „Persisted or reconciled learning is not automatically operationally enforced“.
- 89 % von `engineering/` sind Berichte über das System (`engineering/evidence/`: 25 Audits, 42 Recherchen, 1,67 MB).
- Die Anforderung, die genau das lösen soll, ist selbst offen: REQ-AI-008 „Deterministic failure classes are checked by deterministic tools rather than AI self-certification“ — „gap / implementation pending“.

**[A]** Das Wissen über die Fehler ist vorhanden, gut sortiert und seit Wochen alt. Was fehlt, ist der Schritt vom Befund zur Funktion.

### Schleife 3 — Neue Struktur je Runde

Belege:
- Bei Nr. 632 entstanden innerhalb von fünf Tagen: Stichwortbetrieb, Rollen nach Modellnamen, Labels, Vorab-Gegenlesung, Rückkehr-JSON, ein CI-Prüfer und ein Ablauf für Namensstellen [M aus Git und PRs].
- Laut #405 (P8) betreffen etwa 10 von 16 erfassten Reibungen Abläufe, die erst im Test eingeführt wurden [R].

**[A]** Jede Struktur löst ein Stück und erzeugt eine neue Reibung. Das ist dein „frisst sich fest an Trivialem“.

### Die Gegenschleife, die funktioniert — Code mit Test und Datenvertrag

Belege [M]:
- `python tools/check.py` läuft lokal mit 209 Tests in rund 20 Sekunden grün.
- Quellen- und Dateiidentität, Prüfsummen und Crosswalks halten.
- Die Knau-Ergebnisse haben G1–G4 erreicht.

**[A]** Verlässlich ist im Repo genau das, was als Code mit Test oder als geprüfte Datenstruktur existiert. Unverlässlich ist das, was als Verhaltensregel für ein Modell existiert.

### Wo das System stark ist und wo schwach, nach Fächern

[M, Spalte `current_support` in `requirements/domain-requirements.tsv`]

| Fach | „adequate“ |
|---|---|
| Archivwissenschaft / Diplomatik | 8 von 11 |
| Quellentypen / Sachgeschichte | 8 von 10 |
| Kodikologie | 8 von 10 |
| Paläographie | 3 von 10 |
| Editionswissenschaft | 5 von 10, 4 Lücken |
| Philologie / Sprachgeschichte | 5 von 10, 3 Lücken |
| Historische Quellenkritik | 5 von 11; Lücken „when synthesis begins“ |
| Nutzung durch den Forschenden | 1 von 12 |

**[A]** Das Fundament (Herkunft, Identität) ist solide gebaut. Am schwächsten ist die Spitze: was du liest, und die Einordnung. Gerade die Spitze ist dein Ziel.

### Warum „Autobahn und Kiesel“

[A, gestützt auf M]
- Die Leistung ist groß: rund 40 Bildhälften in fünf Tagen.
- Aber jede Sitzung beginnt kalt mit rund 205.000 Zeichen Pflichtlektüre, grob 50.000 Tokens: Leitziel, `AGENTS.md`, `README.md`, Spickzettel und Methodik.
- Ein großer Teil davon sind Halte-, Prüf- und Autoritätsregeln, die das Modell selbst auslegen muss.
- Unter kleinen Dingen liegt keine Funktion: Zoom in einer HTML-Ansicht, Rückkehr-JSON, Skill-Registrierung.
- Deshalb geht jedes kleine Hindernis den Weg über Regel und Verfahren, statt einfach repariert und getestet zu werden.

### Verstreutes Wissen, veraltete Startdateien

[M]
- **`README.md`** (zuletzt 31.10.): Der Abschnitt zur aktuellen Lage verweist auf das abgeschlossene SD-KA und #244. Dass Nr. 632 aktiv ist, dass die Pause #399 gilt und dass die Forschung auf einem Branch liegt, steht nicht darin.
- **`projects/ssta-20578-nr-632/project.yml` auf `main`** sagt „No evidence-selected active scholarly scope“. Deine Entscheidung vom 30.10. (die ganze Akte) steht nur auf dem Forschungsbranch.
- **`AGENTS.md`** hat einen großen Abschnitt für „ChatGPT Work and Codex“. Dein Arbeitsplan sagt „Immer normaler Chat“. Die Steuerung ist auf zwei Orte verteilt (`AGENTS.md` und Spickzettel).
- **Laufende Forschungsdaten liegen auf Branches ohne PR:** `review/nr632-gegenlesung-vorab` mit 31 eigenen Commits, die Vorab-Gegenlesung.
- **Modellnamen sind fest eingebaut:** Labels `an:chatgpt`, `an:claude`; „Astra“ im Plan; „ChatGPT Work and Codex“ in `AGENTS.md`.

---

## 7 · Neustarten oder reparieren?

**Empfehlung: Reparieren.** Den Kern behalten. Den Betrieb, also wie die KI gesteuert wird, kleiner neu aufsetzen, statt weiter zu flicken.

### Warum kein Neustart

1. **Der Kern trägt und lässt sich abtrennen** [M]:
   - Leitziel;
   - die wissenschaftliche Methodik (Quellenweg S1–S9, Reifestufen G1–G6, Transkriptionsrichtlinie, Belegpolitik, Herkunft, Projektmodell);
   - Corpus mit Quellen- und Dateiidentität;
   - Projektdaten einschließlich der Branch-Forschung;
   - getestete Werkzeuge (209 Tests);
   - Anforderungsliste (135 Anforderungen in 13 Fächern);
   - Befundkatalog (45 Befunde).

   All das liegt in getrennten Dateien und ist geprüft.
2. **Ein Neustart verliert Herkunft und Entscheidungsgeschichte.** Das widerspricht [W] „Immer Provinenz erhalten, Nachvollzihebarkeit.“
3. **Ein Neustart beseitigt die Ursache nicht.** Die Ursache sitzt in der Arbeitsweise, nicht im Repo: Modelle behaupten Funktion in Prosa, die Antwort ist eine neue Regel. Beleg: `AGENTS.md` wuchs gleich am Anfang an einem einzigen Tag von 3,8 KB auf 21,8 KB (26.→27.08.) [M]. Ein frisches Repo würde sich genauso füllen.
4. **Ein Neustart wäre die nächste „neue Struktur“.** Das ist genau die Schleife, die du beschreibst.

### Warum nicht weiter wie bisher

Die drei Schleifen aus Abschnitt 6 laufen weiter.

### Was „Betrieb kleiner neu aufsetzen“ heißt

Das ist eine Richtung, kein Entwurf. Ein Entwurf wäre der nächste Schritt und braucht deine Zustimmung.

**Drei Schichten unterscheiden:**
1. **Kern** — bleibt, wird Bezugspunkt (siehe oben).
2. **Betriebsschicht** — die Ausführungsregeln in `AGENTS.md` und `methodology/workflow.md`, Rollen und Stichworte nach Modellnamen, Rückkehr-JSON, die vielen Betriebs-Issues. Sie wird eingefroren, zusammengelegt, wo möglich in Funktion umgewandelt; der Rest wird archiviert, mit Verlusttest.
3. **Fehlende Spitze** — Lesen mit Verstehen (S4 vollständig), Einordnung (S6/S7), lesbare Fassung. Sie wird an einer echten Quelle gebaut.

**Leitsatz für jeden Reparaturschritt [A]:** Prosa wird durch Funktion ersetzt oder gestrichen, nie nur ergänzt. Funktion heißt: Code mit Test oder ein Datenfeld mit Prüfung, vorgeführt an einer echten Seite. Wo Funktion nicht möglich ist, etwa beim Urteil über eine Lesung oder eine Einordnung, wird das Urteil sichtbar und prüfbar gemacht, statt es per Regel „durchzusetzen“.

**Gegenextrem-Prüfung:**
- *Zu stark angewandt:* Es entsteht ein Softwareprojekt. Das widerspricht dem ursprünglichen Zweck („not a software project“) und D-008 (Automatisierung nur bei belegtem Engpass). Außerdem gingen Schutzregeln verloren, die wirklich schützen, zum Beispiel „Beleg vor Plausibilität“.
- *Zu schwach angewandt:* die nächste Regelrunde.
- *Balance:* Die wissenschaftlichen Schutzregeln bleiben kurz und vollständig. Die Ausführungsprosa wird gekürzt.

**Was die Empfehlung kippen würde** (in diesem Audit nicht geprüft):
- wenn sich beim Trennen zeigt, dass die Kerndateien selbst so mit Betriebsprosa durchsetzt sind, dass eine Trennung nicht ohne Verlust geht;
- wenn die Nr.-632-Daten auf dem Branch sich als nicht tragfähige Grundlage erweisen.

**Was am Neustart-Gedanken richtig ist:** Die Betriebsschicht wird tatsächlich neu aufgesetzt, nur kleiner. Der Kern wird nicht neu gebaut.

---

## 8 · Aufräumen ohne Kontextverlust

| Bestand | Befund [M] | Verlustfreier Weg |
|---|---|---|
| 68 Branches neben `main` | 42 enthalten nichts, was nicht schon in `main` steht: 6 laut Git-Abstammung, 36 über einen übernommenen PR. GitHub behält Diff und Diskussion eines PRs auch nach dem Löschen des Branches. | löschen; dazu die Einstellung „Automatically delete head branches“ (Spickzettel 2d; laut GitHub-API derzeit aus: `delete_branch_on_merge: false`) |
| | 6 mit geschlossenem, nicht übernommenem PR und 6 ohne PR, darunter `review/nr632-gegenlesung-vorab` (+31 Commits, laufende Gegenlesedaten) und `run/savesax-oppurg-2026-10-05` | zuerst als Archiv-Tag markieren (dann bleiben die Commits erhalten), danach einzeln entscheiden; aktive Forschungsdaten bleiben |
| | 14 mit offenem Entwurfs-PR | inhaltlich entscheiden: Forschung (#359, #390, #382), Werkzeug (#332, #335), Audits (#401, #402, #408, #409, #414, #361), Altpläne (#290, #321, #327) |
| 53 offene Issues | 9 „Future“- und Auslöser-Issues (#1–#22, #62, #202, #162); Audit-Kette (7); Nr. 632 (10); Verhaltensfehler (7); Datenmodell (14); savesax (3); Betrieb (3) | Schließen ist kein Löschen. Abgleich der Fehler- und Datenmodell-Issues gegen die 45 Katalogbefunde; viele sind dieselbe Sache. |
| `engineering/evidence/` (1,67 MB) | Geschichte, keine Arbeitsgrundlage | nicht löschen; aus der Pflichtlektüre heraushalten, wie es `README.md` schon sagt („loaded on demand“) |
| Verfahren | Das Repo hat bereits ein erprobtes Aufräumverfahren: SD-KA WP5 mit `engineering/changes/SD-KA-01/MIGRATION.tsv`, also Einordnung, exakte Blob-Identität vor dem Verschieben und Rückweg. | wiederverwenden, nicht neu erfinden |

---

## 9 · Quickwins (geprüft)

**Prüfmaßstab:** Ein Quickwin beseitigt einen von dir benannten Schmerz, fügt keine Regel hinzu, ist umkehrbar, hat ein prüfbares Ergebnis und setzt keine größere Entscheidung voraus.

| # | Quickwin | Behebt | Prüfbar an |
|---|---|---|---|
| Q1 | 42 Branches ohne Verlust löschen und die GitHub-Einstellung „Automatically delete head branches“ einschalten (die Einstellung musst du selbst setzen) | „Wo können wir … clean-up ansetzen, ohne Kontext zu verlieren“ | Liste der 42 mit PR-Nummern; danach zeigen die PR-Seiten weiter ihre Diffs |
| Q2 | die 12 Branches ohne offenen PR mit einem Archiv-Tag sichern, vor allem die laufende Vorab-Gegenlesung | Verlustschutz für Forschungsdaten | Tags sichtbar auf GitHub |
| Q3 | eine Datei mit deinen O-Tönen: wörtlich, mit Datum und Fundstelle, ohne KI-Text dazwischen | „nicht klar, was kommt von der KI, was sind meine O-Töne“ | jedes Zitat führt zu seiner Quelle (Chatdatum oder Issue-Kommentar) |
| Q4 | Startdateien wahr machen: `README.md`-Abschnitt zur aktuellen Lage (aktiv, pausiert, wo die Forschung liegt); `project.yml` von Nr. 632 auf `main` an deine Entscheidung vom 30.10. angleichen. Das ist Nachziehen einer getroffenen Entscheidung (`maintenance.md`), keine neue. | „Startdateien überhaupt nicht mehr gepflegt“ | ein frischer Chat beantwortet aus `README.md` allein: was aktiv ist, was pausiert, wo die Forschung liegt |
| Q5 | `README.md` und Spickzettel vollständig auf Deutsch | „Englisch ist falsch“ | du liest `README.md` ohne Englisch |

**Bewusst keine Quickwins:**

| Vorhaben | Warum nicht |
|---|---|
| Methodik übersetzen | Gefahr von Bedeutungsverlust beim Übersetzen (D-019); später, mit Sorgfalt |
| #359 übernehmen | braucht die Aufteilung F4 mit Verlusttest (#390) |
| lesbare Ansicht bauen | braucht zuerst ein festes Datenformat für Nr. 632 |
| Labels von Modellnamen auf Rollen umstellen | Teil des Betriebsneuaufbaus |
| Regeln in `AGENTS.md` und `workflow.md` kürzen | Kern der Reparatur, braucht Verlusttest |
| Audit-Kette schließen | deine Entscheidung |

**Deine Entscheidungen:**
1. Reparieren statt Neustart, wie empfohlen?
2. Die Audit-Kette (#398, #405, #411–#414 mit den PRs #401, #402, #408, #409, #414) beenden, mit dieser Fassung und #401 als Material?
3. Welche der Quickwins Q1–Q5 sollen umgesetzt werden?

---

## 10 · Grenzen

- Auch dieses Audit stammt von einer KI. Es kann denselben Mustern unterliegen, die es beschreibt (#404). Die Belegstufen sollen das prüfbar machen.
- Kein Urteil über die Richtigkeit einzelner Lesungen oder Einordnungen.
- `engineering/evidence/` inhaltlich nicht gelesen. Dort könnten bereits Vorschläge zur Trennung von Kern und Betrieb liegen; das wäre vor einem Entwurf zu prüfen (Lehre aus #405 P12: Vorhandenes nicht übersehen).
- design-lab und andere Tools nicht gelesen.
- Die Messwerte zur Anforderungsliste beruhen auf der Spalte `current_support` mit Stand der Erhebung (September/Oktober), nicht auf einer neuen Prüfung.
