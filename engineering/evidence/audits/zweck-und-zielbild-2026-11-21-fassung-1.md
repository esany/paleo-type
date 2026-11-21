# Audit paleo-type: Zweck, Anspruch, Bedürfnisse, Zielbild — Fassung 1

**Stand:** 21.11.2026, `main@22b255b`. Erstellt von Claude (Prüfchat) auf Wunsch des Eigentümers, im Chat ausgeliefert und hier unverändert abgelegt. Die überarbeitete Fassung 2 liegt daneben: `zweck-und-zielbild-2026-11-21-fassung-2.md`. Diese Fassung wird nicht nachträglich verbessert, damit sichtbar bleibt, was Fassung 2 korrigiert.

**Status:** KI-Audit, keine Abnahme, keine Freigabe, keine Maßnahme.

---

## Wie ich gelesen habe

Damit sich #404 nicht wiederholt, hier die Abdeckung:

- **Ganz gelesen:**
  - `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `README.md`, `SPICKZETTEL.md`
  - `DECISIONS.md` (D-001 bis D-021)
  - `ARBEITSPLAN.md` zu Nr. 632
  - den Kern von `historical-source-workflow.md` (die Schritte S1–S9 und die Rollen)
  - die erste README vom 26.08.
- **In Teilen gelesen:**
  - das Audit vom 14.09. zum transdisziplinären Ansatz
  - der ChatGPT-Bericht zu #401 (Abschnitte 0–5 und 8)
  - Issues: #404, #405, #406, #407, #410, #411, #412, #353, #355, #358, #41, #166, #201
  - die Lesung von 0104R
  - die Gate-Tabellen der beiden Knau-Projekte
- **Maschinell durchsucht:** alle 215 Issues und 199 PRs mit Kommentaren, rund 4 Mio. Zeichen, nach deinen wörtlichen Aussagen.
- **Nicht gelesen:**
  - der Rest von `methodology/`
  - `engineering/` außer dem Audit vom 14.09.
  - `requirements/`
  - der Claude-Bericht zu #402
  - die meisten Diskussionsverläufe
  - die Lesungen in der Breite

Der gesamte Textbestand umfasst rund 2 Mio. Tokens. Gelesen habe ich davon einen kleinen, gezielt gewählten Teil.

**Belegstufen:**

| Kürzel | Bedeutung |
|---|---|
| **[W]** | Dein Wortlaut in Anführungszeichen. Fast immer hat eine KI ihn aus dem Chat ins Issue übertragen; die Chats selbst liegen nicht im Repo. |
| **[E]** | Deine dokumentierte Entscheidung, von einer KI formuliert. |
| **[R]** | Repo-Text von einer KI; ob du ihn so gewollt hast, ist im Einzelnen nicht belegt. |
| **[A]** | Meine Ableitung. |

**Vorweg:** Alle 1.054 Commits und fast alle Kommentare laufen über dein Konto. Das Repo hält selbst fest (D-017, D-018), dass Commits unter deinem Namen KI-Deutungen enthalten können. Deine eigene Stimme ist dünn: Ich finde rund zwei Dutzend wörtliche Sätze in 4 Mio. Zeichen. Alles Weitere über deine Absicht ist Auslegung.

---

## 1 · Worum es geht

Eine Arbeitsumgebung, in der KI frühneuzeitliche Archivhandschriften für dich erschließt: lesen, diplomatisch transkribieren, einordnen, und zwar so, dass jede Aussage an ihrer Bildstelle hängt. Das Material:

- Visitationsprotokolle aus dem Ernestinischen Gesamtarchiv in Weimar (Reg. Ii 3, 4, 5), mit dem Abschnitt zum Ort Knau als Schwerpunkt;
- eine Lehnsakte zum Lehngut Knau im Sächsischen Staatsarchiv (Bestand 20578, Nr. 632, 135 Bilder).

| Quelle | Umfang | Stand |
|---|---|---|
| Reg. Ii 5, fol. 61v–63r | 4 Seiten, 81 Zeilenanker | G1–G4 erreicht: Quelle gesichert, diplomatisch vollständig, intern geprüft, mit Reg. Ii 4 verglichen. G5/G6 (Edition) nicht. |
| Reg. Ii 4 Bd. II, fol. 306v–309r | 6 Seiten, 117 Einheiten | ebenso G1–G4 |
| Nr. 632 | KI-Arbeitslesungen zu rund 40 Bildhälften (0104R–0131R) | Liegt nur auf dem Branch von PR #359 (177 Commits, 30.10.–03.11.), nicht auf `main`. Stichproben fanden Fehler. G2 nicht erreicht. |

Ein Beispiel, was dabei herauskommt: Bild 0104R beginnt mit „4. Jul: 1760.“. Es ist eine Bittschrift an den „Durchlauchtigster … König und Chur-fürst“, geschrieben von einem Sohn des verstorbenen Hofmarschalls „Johann George Graf von Ein-siedel“. Die Lesung geht Zeile für Zeile, Unsicheres ist markiert, Abkürzungen sind nicht aufgelöst.

Daneben steht das System: Methode, Quellenvertrag, Werkzeuge mit Tests, CI und ein Engineering-Bereich. Dieser ist auf `main` gut doppelt so groß wie alle Projekte zusammen (1,9 MB gegenüber 0,8 MB).

## 2 · Zweck: wozu es da ist

**Am Anfang (26.08., erste README) [R]:** Das Tool soll einem Nicht-Spezialisten helfen, frühneuzeitliche Handschriften zuverlässig zu erschließen, *„without turning the research task into a software project“*. Dazu „No AI slop“, und Werkzeuge nur dann, wenn sie den Weg zu einer verlässlicheren Lesung verkürzen. Erster Prüfstein waren vier Bilder aus Knau.

**Am selben Tag [E, #41]:** Du hast vier Schwerpunkte bestätigt:
- transdisziplinär, von Quelle und Problem her;
- echter Mensch in der Schleife;
- Nachvollziehbarkeit vom Ergebnis bis zur exakten Quelle;
- schlanke Technik.

Daraus wurde das Leitziel (D-013).

**In deinen Worten (03.11.) [W]:** „Erstmal eigene Forschung“. Umfang: „offen, viele Quellen“.

**[A]** Der Zweck hat sich in drei Monaten nicht geändert: Erkenntnis aus Quellen für dich, die KI als Leser, Technik als Mittel. Gewachsen ist nur die Menge an Struktur dazwischen.

## 3 · Anspruch

Drei Ebenen, die nicht ganz deckungsgleich sind:

1. **Methode: hoch und streng** [R, als Leitziel bestätigt]
   - wissenschaftlich exzellent;
   - Beleg vor Plausibilität;
   - Lesung, Normalisierung, Identifizierung und Deutung bleiben getrennt;
   - Unsicherheit ist ein gültiges Ergebnis;
   - neun Arbeitsschritte bis zur Edition;
   - ein Dutzend Fachdisziplinen als Werkzeuge, je nach Quelle;
   - ein Dritter soll jede Aussage bis zur Bildstelle zurückverfolgen können, und du sollst als Nicht-Fachmann verstehen, wo es steht.
2. **Ergebnis für Nr. 632** [E, #358]: „möglichst vollständige diplomatische, quellenkritisch verantwortbare Transkription aller einzigartigen sichtbaren historischen Schriftflächen“, daraus eine interne PDF-Arbeitsedition, ohne öffentliche Bildweitergabe.
3. **Geltung** [E, ARBEITSPLAN 31.10.]: „Keine Fachleute nötig. Ergebnisse heißen ‚KI-Arbeitslesung, blind gegengeprüft‘.“ Zu Fachleuten sagst du selbst [W]: „Das sollte nicht relevant sein.“

**Spannung [A]:** Das Leitziel nennt Fachleute als Prüfebene und die Edition als Endstufe. Deine Praxis setzt die Obergrenze bei „intern, KI-gelesen, blind gegengeprüft“. Beides passt zusammen, wenn „exzellent“ die Sorgfalt meint und nicht die Publikationsreife. Ob das deine Lesart ist, steht nirgends ausdrücklich.

Dazu kommt ein Anspruch an die KI selbst (#405, von einer KI zusammengefasst, gestützt durch deine Einwände in #404): Gefragt ist Erkenntnisarbeit, die echte Fachkunde **transdisziplinär** nachbildet, nicht das Bild „eines Fachmanns“.

## 4 · Deine Bedürfnisse

Abgeleitet aus deinen Worten und vor allem aus deinen Eingriffen. Die Eingriffe sind der stärkste Beleg, weil sie zeigen, wo das System an dir vorbeiging.

| Bedürfnis | Beleg |
|---|---|
| **Fortschritt an der Quelle sehen, nicht Betrieb** | [W] „Wir haben einen Plan, der plausibel klingt, es läuft, einen Klick vor der Weltherrschaft, und dann läuft es ohne Fortschritte … Wir stehen auf der Stelle … Das ist zyklisch.“ Außerdem [W] „In den Visitationsprotokollen viel mehr als aktuell.“ Und [E] die Schließung von #410 am 15.11.: Meta-Arbeit lieferte nicht die „fachlich nutzbare Gesamterkenntnis“. |
| **Eine KI, die wirklich liest und Querbezüge nutzt**, statt Unsicherheit zu verwalten | [W] #407: „Du hast dich aber jetzt schon so viel gelesen.. dann müssen dich querbeziehungen erkenntnisse schaffen. Und wieso kannst du klar geschriebene nr4 nicht lesen“. Deine Hinweise „Gamse“ und „Dreba“ waren beide Male besser als die Vorschläge der KI. |
| **Nicht Bote, Bediener oder Fehlerfinder sein** | [W] „Die Arbeit nicht aufhalsen“. [E] „Ich (Eigentümer): Ziel, Reihenfolge, Freigaben.“ Das Gegenbild: sieben Einwände von dir in einer einzigen Sitzung (#404) und das Label `rettung-eigentümer`. |
| **Das Ganze durchschauen und früh gewarnt werden** | [W] #406: „ein wirkliches Big Picture des Systems … was wo vorhanden ist“ und „Kriterien und Prüfmechanismen, die dir erlauben, frühzeitig gewarnt zu werden“. [W] #411: „welche Regeln gibt es eigentlich? Wo findet sich überall der Diff?“ [W] „für mich nicht wirklich transparent“. |
| **Herkunft und Nachvollziehbarkeit, immer** | [W] 15.11.: „Immer Provinenz erhalten, Nachvollzihebarkeit.“ So durchgehend seit dem ersten Tag. |
| **Ehrlichkeit statt fertiger Wirkung** | [W] Einwände „Du rätst“ und „keinen Pfifferling wert“ zu einem Audit, das Lektüre nur vortäuschte (#404). |
| **Erst verstehen, dann planen, keine schnellen Lösungen** | [W] „Auf dieser Grundlage lohnt es erst, den nächsten Schritt zu planen. Ein Problem ist auch Solutionism.“ |
| **Sparsam mit Rechenkontingent und Kontext**, ohne Qualitätsverlust | [E] #355: „Token- und Kontingentsparsamkeit muss Prinzip sein“; normaler Chat statt Work oder Codex. [W] Befunde „super tokensparend“ weiterbearbeiten. |
| **Mitlesen dürfen, nicht müssen** | [E] Du liest freiwillig bis zu fünf Namensausschnitte je Durchgang, und deine Lesungen werden festgehalten (zuletzt zu 0115R). [A] Das widerspricht dem Satz „Ich lese keine Handschrift“ im Plan. Ich lese es so: Du hast Interesse und Ortskenntnis, willst aber nicht die Prüfinstanz sein. |

## 5 · Zielbild des Tools

Aus den Belegen oben zusammengesetzt [A]:

> Du nennst eine Quelle und ein Interesse. Die KI erschließt die Quelle: Sie liest Seite für Seite am Originalbild und nutzt dabei alles, was sie in derselben Schrift und Akte schon gelesen hat. Sie ordnet Dokumente und Vorgänge ein und zieht die Fächer zusammen, die die Quelle verlangt. Jede Aussage hängt an ihrer Bildstelle, Unsicheres bleibt sichtbar. Die Verwaltung (welche Datei, welche Seite, wo speichern, was ist schon abgedeckt) erledigt die Technik verlässlich und ohne dich. Du bedienst das Ganze mit wenigen Stichworten. Du siehst in Alltagssprache, was verstanden ist und was offen, und entscheidest über Ziel und Reihenfolge. Am Ende steht eine interne, lesbare Arbeitsedition. Ein frischer Chat kann jederzeit aus dem Repo weitermachen.

**Schon gebaut und tragfähig:**
- Identität von Quelle und Datei mit Prüfsummen;
- die Trennung der Aussageebenen (Lesung, Normalisierung, Identifizierung, Deutung);
- die Knau-Transkriptionen;
- die Bedienung über Stichworte;
- die Blind-Gegenlesung;
- der Neustart aus dem Repo.

**Offen im Zielbild.** Dazu finde ich keine Aussage von dir, und nur du kannst das festlegen:
1. **Geltung:** Reicht „intern, KI-gelesen, blind gegengeprüft“ auf Dauer, oder soll später etwas veröffentlicht werden? Davon hängt ab, ob Fachleute und die Stufen G5/G6 je eine Rolle spielen.
2. **Reichweite:** „offen, viele Quellen“. Ist das Tool für einen wachsenden Bestand vieler Akten gedacht oder zuerst für Nr. 632?
3. **Was du am Ende in der Hand hältst:** die PDF-Arbeitsedition (#358), die Website (#382) oder vor allem Verständnis in Alltagssprache, aus dem du Prioritäten setzt?
4. **Aufteilung zwischen den KIs:** Gehört „Astra baut, Claude prüft, ein frischer Chat liest gegen“ zum Zielbild? Oder ist es eine Notlösung, weil Astra weder Git noch Codeausführung hat (#368)?

## 6 · Wo das Repo heute vom Zweck abweicht

Das sind Befunde, keine Ursachenanalyse. Gegenbelege stehen jeweils dabei.

1. **Gewicht.**
   - Auf `main` ist Engineering gut doppelt so groß wie die Projekte.
   - Im September kamen 16.800 Zeilen Anforderungen dazu, aber nur 6.500 Zeilen in den Projekten.
   - *Gegenbeleg:* Die aktive Forschung liegt gar nicht auf `main`, sondern auf dem Branch von PR #359 (rund 2.800 Zeilen in fünf Tagen).
   - *Gegenbeleg:* Große Systemblöcke hast du ausdrücklich freigegeben (Arc B am 15.09. in #201, SD-KA nach D-016).

   Nicht jede Systemarbeit war also Abdriften. Die Erzählung „Verfahren verdrängt Forschung“ ist zu einfach; #404 zeigt, dass genau sie schon einmal ungeprüft bestätigt wurde.
2. **Das Repo spricht in deinem Namen.** Der Arbeitsplan steht in der Ich-Form („Ich lese keine Handschrift“), Freigaben stehen als Eigentümerentscheidung in KI-Sprache. Für dein Zielbild ist deshalb nicht der Repo-Text maßgeblich, sondern deine wörtlichen Sätze.
3. **Erschließung statt Fragestellung.**
   - Laut #405 (von einer KI zusammengefasst) setzt du Prioritäten aus Struktur und Einzeltexten mit grober Inhaltsidee; auch die Visitationsprotokolle hatten keine Forschungsfrage.
   - Die Methode verlangt „Ziel → Forschungsfrage → Beleg“, lässt aber eine erforderliche Quellendarstellung als Ersatz zu. Auf dem Papier passt das zusammen.
   - Trotzdem führte das Audit #402 „fehlende Forschungsfrage“ als Ursache an, und #404 verwarf das als Fehldeutung deiner Absicht.

   [A] Dein Arbeitsmodus ist: zuerst die Quelle erschließen. Wer daraus einen Mangel macht, verfehlt den Zweck.
4. **Sprache.** Von August bis Oktober sind die Issue-Texte fast nur englische Fachprosa (Oktober: 297 englisch, 49 deutsch). Erst im November kippt es (97 deutsch, 2 englisch). [A] Dein „für mich nicht wirklich transparent“ hat hier mindestens einen sichtbaren Grund.
5. **Lesen an der Quelle.**
   - In fünf Tagen hat die KI rund 40 Bildhälften angelesen.
   - Für 0108–0131 sah #359 die Kennzeichnung „ungeprüfter Entwurf – Stichprobe mit hoher Fehlerrate“ vor, und die Behauptung „substantielle Arbeitslesungen 0112–0116“ wurde widerlegt.
   - Deine Hinweise trafen besser als die Kandidaten der KI.

   [A] Dein Kernbedürfnis, eine KI, die wirklich liest, ist an der Quelle nicht erfüllt. Fehlende Struktur erklärt das nicht: Davon gibt es reichlich.
6. **Seit dem 03.11. steht die Forschung.**
   - Die Pause #399 hast du am 14.11. bestätigt.
   - Seither entstanden vor allem Audits, Ursachenanalysen und Rekonstruktionen von Aufträgen (#405, #408–#414).
   - #410 hast du am 15.11. als „nicht geplant“ geschlossen, weil es dich belastet hat.
   - #414 belegt, dass die KI genau die kritisierte Schleife wiederholt.

   Dieses Audit gehört zur selben Gattung. Deshalb schlage ich bewusst nichts vor und habe nichts angelegt.

## Grenzen

- Kein Urteil über die Richtigkeit einzelner Lesungen.
- Deinen Wortlaut kenne ich fast nur aus zweiter Hand, von KIs aus dem Chat übertragen.
- design-lab und Wissensarbeit habe ich nicht gelesen. „Handy first“ und Ähnliches stammt aus dem design-lab-Zielbild und ist hier bewusst nicht übertragen.
- Weite Teile von `engineering/` und `methodology/` sind ungelesen. Das könnte einzelne Punkte in Abschnitt 6 verschieben, kaum aber deine Bedürfnisse in Abschnitt 4, denn die stammen aus deinen eigenen Worten.
