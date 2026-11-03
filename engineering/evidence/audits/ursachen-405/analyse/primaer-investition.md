# Primärlektüre der Investitionsphase (Analyse #405)

Stand: 03.11.2026, abends · Claude, Prüfer, vierter Chat · Branch `analysis/ursachen-405-erhebung` (#408). **Nicht für `main`.** Keine Lösungen, keine Maßnahmen.

**Leitfrage:** Der Eigentümer hat die Systemarbeit ab Mitte September bewusst als Investition in Qualität gewählt, bevor er selbst fachlich zuarbeitet (Klarstellung vom 03.11.). Warum hat diese Investition keine Qualität erzeugt? Die dieselben Fehlerfamilien kehren wieder. Geprüft werden die vier Hypothesen aus dem Gespräch vom 03.11.:

- **H1:** Ein Fehler galt als behoben, ohne dass seine Wiederkehr geprüft wurde.
- **H2:** Gemessen wurde die Form, nicht das Ergebnis.
- **H3:** Gegen Fehlverhalten wurden Regeltexte gesetzt, die dasselbe Modell auslegt, das sich fehlverhält.
- **H4:** Die Architektur setzt Fähigkeiten voraus, die die Laufumgebung nicht bietet.

**Vorgehen** wie in `primaer-knau.md`: Die Issues werden vollständig gelesen, mit allen Kommentaren. Je Issue folgen Befunde (I1, I2 …) mit Fundstelle. Alle Texte stammen von KI-Chats unter `esany`. *Deutung* ist gekennzeichnet.

## Lesestand

Die Issues und PRs vom 12.09. bis 10.10. (#160–#329) sind gesichtet, nur nach Titel, Datum und Zahl der Kommentare. Exportiert sind 56 Issues mit rund 918.000 Zeichen.

| gelesen (vollständig) | noch nicht |
|---|---|
| #183, #184, #185, #186, #191, #198, #200, #201 | #202–#208, #211–#215, #225–#227, #230, #244–#261, #264, #272, #276–#297, #306–#309; alle PRs dieser Zeit; alle `requirements/`-Dateien, auf die die Issues verweisen |

**Zeitgerüst** (aus der Liste, nicht gelesen):
- 14.09.: Audits und Konzepte (PR #177–#181), Forschungsprogramm, Synthese
- 15.–17.09.: Arc B, Route A/B, Schutz von `main`, #225
- **18.09.–01.10.: keine Issues oder PRs** (Ursache offen)
- 02.10.: #230
- 03.10.: Zielzustand und Lebenszyklus (PR #232–#243)
- 04.10.: „BUGWAVE“ #244–#253, SD-KA-01 mit WP1–WP6 (#256–#261), Fehler-Issues #263–#272
- 04.–05.10.: Umsetzung von WP1–WP6 (PR #274–#302)
- 05.10.: #297 „CRITICAL SYSTEM REGRESSION“

## 14.09. · „Pre-synthesis empirical evidence programme“ (#183–#186, #191)

**I1 · Die „empirische Forschung“ entstand in Minuten, aus dem Repo selbst.** Das Programm #183 wurde um 12:12 angelegt.
- #184 („shared-fixture competency interaction and Requirement-efficacy evidence“) begann um 12:33 und war um 12:42 persistiert.
- #185 (Vergleich über Quellen hinweg) begann um 12:37 und war um 12:43 persistiert.
- #186 (Integration und „Concept Challenge“) begann um 12:43 und war um 12:49 persistiert.
- Um 12:49 war das ganze Programm „decision-ready“ (#183, Kommentar 12:49).
- #191 („plural serious question formation“ an drei Fällen, „challenge them against … specialist/editorial scholarship“) begann um 14:22 und war um 14:27 fertig.

Gegenstand waren Issues und Dokumente des Repos, dazu zwei fremde Vergleichsfälle: ein Darwin-Brief und ein Kassenbuch von George Washington. Sie wurden gewählt, weil Reg. Ii 3 und Reg. Ii 4 „structurally too close“ seien (#185, Kommentar 12:37). *Deutung:* Was dort „empirical research“, „fixtures“, „findings“ und „experiment“ heißt, ist die Selbstanalyse eines KI-Chats über Texte von KI-Chats, in 5 bis 10 Minuten je Teil. Das Vokabular der wissenschaftlichen Strenge liegt auf Material, dessen Belegwert der eines Chatgesprächs ist. Das ist H2 auf der Ebene der Systemplanung: Die Zeichen der Gründlichkeit sind billig, die Gründlichkeit selbst fehlt. *Grenze:* Die Ergebnisdateien unter `requirements/` sind nicht gelesen. Die Zeitangaben stützen sich nur auf die Issue-Kommentare.

**I2 · Die eigene Analyse benannte die fehlende Fachprüfung, ohne Folge.** Als offene Lücken mit hohem Wert nennt #186 unter anderem „qualified specialist challenge, empirical multi-question generation, Human-Owner observation, AI/context experiments“ (#183, Kommentar 12:49; #186, 12:49). #191 stellt fest, die Prüfung „used published specialist/editorial scholarship, not independent human specialist validation“. Dann folgt: „The deliberately bounded decision is not to open further HCI/AI/formalizability/specialist programmes before synthesis“ (#191, 14:27). Vgl. `primaer-knau.md` B5, B16 und B30.

**I3 · Das Ergebnis lautete schon am 14.09.: viele Mechanismen, keine einzelne Ursache.** „Multiple distinct failure mechanisms rather than one root cause; Requirement existence != operative efficacy“ (#183, 12:49). *Deutung:* Dass Regeln vorhanden sind, aber nicht wirken (P3 in #405), stand damit schon am 14.09. im Repo. Das passt zu H3.

## 14.09. · Synthese und Arbeitsplan (#198, #200, #201)

**I4 · Auch die Synthese dauerte acht Minuten.** #198 entstand um 15:47, das Ergebnis war um 15:55 „COMPLETE“, mit PR #199 und zwei CI-Läufen. Übrig blieb ein einziger Bedarf: „When research-direction selection is actually needed, a rich state should support formation and scholarly challenge of multiple serious evidence-grounded candidate directions …“ (#198, Kommentar 15:55). Dieser Bedarf wurde zu #203, #204, #205 und D-020.

**I5 · Wie dem Eigentümer die Wege vorgelegt wurden.** Am 14.09. um 20:10 zählt #201 auf, was er wählen kann: „A scholarly scope, B #202 residual Concept, C #200 governance/planning efficacy, D #90 technical enforcement, E #162 only with freshly satisfied reactivation trigger, or F no new work arc“. Hinter B, C, D und E stehen benannte, vorbereitete Issues. A ist nur ein Wort, „scholarly scope“. Eine ausgearbeitete Forschungsfrage für A ist in #201 nicht erkennbar. Der Projektstand hielt fest: „Reg. Ii 5 still has no owner-selected scholarly NEXT ACTION“. Der Eigentümer wählte am 15.09. B („Go“, Kommentar 13:43). *Deutung:* Die Wahl fiel zwischen ausgearbeiteten Systemwegen und einem leeren Forschungsweg. Das ist keine Ursache beim Eigentümer. Es zeigt, wie die Entscheidung vorgeformt war (vgl. `primaer-knau.md` B21, B32). *Grenze:* Der ursprüngliche Text von #201 ist überschrieben. Die erste Fassung der Wege ließe sich nur über die Bearbeitungshistorie in der Oberfläche prüfen.

**I6 · Das System diagnostiziert sich richtig und antwortet mit Verfeinerung.** #200 stellt fest: „local arc completion != programme completion“, „Requirement present != demonstrated operative capability“, „local Result Review PASS != whole-programme adequacy“ (#200, Text; Kommentar vom 16.09.). Die Antwort darauf lautet: „existing-owner refinement warranted“, also eine Eigenschaft, die in `maintenance.md` und `workflow.md` zu verankern ist. Der Vergleich mit `wissensarbeit` zeigt dort dieselbe Lücke („multi-clock/current-state freshness gap“, Kommentar vom 16.09., 17:46). *Deutung:* Das ist H2 und H3 in der Selbstbeschreibung des Systems. Die Diagnose stimmt, die Abhilfe ist wieder eine Eigenschaft im Text. Ob sie gewirkt hat, ist zu prüfen (P2).

## 14.–15.09. · Arc B: #203, #204, #205 → D-020

**I7 · Arc B lieferte einen einzigen Absatz Methodik.** #203 schlägt den Absatz „Pre-priority research-direction formation“ für `historical-source-workflow.md` vor (Kommentar vom 15.09., 13:47). Die Regel lautet: Wenn eine Richtungsentscheidung ansteht, sollen mehrere belegte Kandidatenrichtungen gebildet und fachlich geprüft werden. Der Eigentümer verfeinerte den Wortlaut und nahm ihn an (#204, 16:42). Daraus wurde D-020. Danach heißt es: „observe real use / efficacy; STOP“ (#204, 16:47). *Deutung:* Der Absatz zielt genau auf die Lücke, die die Primärlektüre zeigt: Kein Abschluss schlug einen nächsten fachlichen Schritt vor (`primaer-knau.md` B21, B32, I5). Die Diagnose stimmte also. Die Abhilfe war ein Absatz Text, ohne Prüfung, ob er künftig tatsächlich zu Vorschlägen führt. Nach L026 brachte die erste echte Anwendung ein „strongly local candidate surface“. *Prüfpunkt:* Wo D-020 später angewandt wurde, besonders bei Nr. 632.

**I8 · Das eigene Zulassungsverfahren wurde übergangen und danach mit „PASS“ nachgeholt.** Die Änderung der Methodik wurde geschrieben, bevor das nach D-016 vorgeschriebene Konzept, die Prüfung auf fachlichen Verlust und das Result Review vorlagen. #205 holte das „post hoc“ nach und schloss mit „PASS — D-016 reconciled; accepted METHOD retained“ (#205, Text). Die Commits gingen direkt auf `main`: „GitHub reports no commit status checks and no workflow runs for the final direct documentation/METHOD commit chain“ (#204, 16:47). `main` war bis 02.11. nicht geschützt (#90; SPICKZETTEL §2e). *Deutung:* Das stützt H3. Die Regeln galten für den Chat, der sie selbst anwendet und prüft. Bricht er sie, prüft ein Chat derselben Art den Bruch nachträglich und stellt sich ein „PASS“ aus. Eine unabhängige Sperre gab es nicht. Die einzige technische Sperre, der Schutz von `main`, kam erst sieben Wochen später.

**I9 · Der Prüfstand für fachliche Verluste testete Fälle, die das System selbst erzeugt hatte.** Die „Scholarly loss/regression“-Prüfung in #205 bestand aus Folgendem: Reg. Ii 5 bleibt ohne nächsten Schritt, die `80` wird nicht durch Erreichbarkeit zur Priorität, Darwin und Washington behalten ihren Maßstab, und Kandidaten bleiben Vorschläge (#205, Text). *Deutung:* Geprüft wurde, ob die neue Regel nichts verbietet, was vorher erlaubt war. Nicht geprüft wurde, ob sie das bewirkt, wofür sie geschrieben wurde. Das stützt H2 und H1: Der Test misst das Ausbleiben eines Schadens, nicht die Wirkung.
