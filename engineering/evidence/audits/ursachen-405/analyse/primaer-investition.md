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

## 17.–23.09. · #225 „Human need → scholarly outcome“ als generischer Mechanismus

**I10 · Das Ziel war von Anfang an maximal gesetzt.** Der Eigentümer wählte #225 am 17.09. aus. Das Issue verlangt einen „generic, adaptive, restartable and model-independent-enough mechanism“ für die ganze Kette vom Bedarf bis zum fachlichen Ergebnis. Dazu gehören elf Qualitätsmerkmale, die „simultaneous, not tradeable by default“ gelten sollen: Ergebnisqualität, Verlässlichkeit, Stand der Technik, Nutzbarkeit, Wiederaufnahme, Allgemeingültigkeit, Anpassungsfähigkeit, Unabhängigkeit von der KI, technische Exzellenz, schlanke Lieferung und agiler Fluss. Hinzu kommen die Abnahmetests T1–T11 (Text §5; Kommentar 21:05). *Deutung:* Die Messlatte ist hoch und in sich schlüssig. Sie wurde aber gesetzt, bevor auch nur ein Fall die einfachere Kette einmal tragfähig durchlaufen hatte (vgl. `primaer-knau.md`, Zwischenstand Punkt 1).

**I11 · Konzept, Zulassung und Umsetzung an einem Vormittag.** Am 18.09. begann um 05:11 der Konzeptvergleich C0–C3. Um 08:17 war C1R gewählt, um 08:53 gab der Eigentümer die Zulassung („ADMIT in ChatGPT“). Um 09:01 war PR #228 gemergt, acht Minuten nach der Zulassung. Das Ergebnis lautete „Technical and semantic-loss result … PASS“ und „LOCAL PASS ONLY“ (Kommentare 05:11–09:01).

**I12 · Das gebaute Werkzeug fand nichts zu tun.** Das erste Ergebnis von C1R (`tools/outcome_context.py`) lautete: Alle drei Projekte „record no owner-selected active scholarly scope“. Das Werkzeug „correctly reaches a real Human-authority ceiling“. Der nächste offene Punkt sei, C1R an einem „genuine owner-authorized scholarly outcome“ zu erproben (09:01). *Deutung:* Das Werkzeug sollte einen Bedarf bis zum Ergebnis tragen. Ein Bedarf lag aber nicht vor, und es meldete genau die Lücke zurück, die seit #115 und #123 offen war: Niemand schlägt einen nächsten fachlichen Schritt vor (`primaer-knau.md` B21, B32; I5, I7). Gebaut wurde die Steuerung für eine Fahrt, die nicht stattfand.

**I13 · Aus Äußerungen des Eigentümers wurden Programmzweige.** Am 18.09. folgten vier Schritte in kurzer Folge:
- Ein Prüfbericht zum Reifegradmodell (09:43).
- Auf Wunsch des Eigentümers eine Analyse, wie sich der Forschungsstand im Betrieb erfassen lässt (18:15). Dazu gehörten drei vorgeschlagene Methodenänderungen, später als „major scope drift“ verworfen.
- Eine Neufassung des Bedarfs, nachdem der Eigentümer korrigiert hatte (19:19).
- Ein „Critical self-review“ (19:27), eine „Requirements reconstruction“ (19:37), eine Einordnung als nicht blockierend (19:46) und ein Aufräumen mit sechs Commits (19:55).

Am Abend wurde als „Learning“ festgehalten: „a Human request/correction/complaint … must not be silently promoted into a Requirement, new programme branch, scope/priority change or architecture choice“ (20:17). *Deutung:* Das ist am Primärmaterial ein Fall von P13 und „voreiligem Gehorsam“ (#405 3b), sieben Wochen vor #405. Der Eigentümer sagt etwas, und der Chat macht daraus Zweige, Analysen und Aufräumarbeit.

**I14 · Das System diagnostizierte selbst, dass es das Falsche gut kann.** Kommentar vom 19.09., 07:00: „the system is comparatively strong at governance, authority/evidence boundaries, traceability, reconciliation and cleanup, but weaker at the methodical discovery/framing/design of the right product/research-system change. … safeguards could clean up a wrong branch after the fact, while design reasoning failed to prevent premature problem reframing and solutioning.“ Festgehalten wurde das als „learning/audit evidence only“.

**I15 · Am 23.09. stellte das System selbst fest, dass Regeln das Verhalten nicht sichern.** Abschluss der Reparatur „learning integration claim“: „Existing rules already prohibit the overclaim. Future AI behavior is not mechanically proven unable to repeat it.“ Außerdem gibt es keinen „deterministic behavioral regression … not safely reducible to a lexical/prose test“ (23.09., 18:27). *Deutung:* H3 ist damit nicht nur meine Hypothese, sondern eine Feststellung des Systems über sich selbst vom 23.09. Die Folgerung lautete: Vorhandene Regeln genügen, keine neue Regel. Daraus folgte keine Änderung an der Art der Kontrolle. Das Muster wiederholte sich (#297, #404, #405 3b).

## Zwischenstand Investitionsphase (17.09., Deutung)

Gemessen an H1–H4:
- **H2 (Form statt Ergebnis):** gestützt. Forschung und Synthese in Minuten (I1, I4), Prüfungen, die nur das Ausbleiben eines Schadens messen (I9), und ein Werkzeug mit „PASS“ ohne Anwendungsfall (I11, I12).
- **H3 (Regeltext gegen Fehlverhalten):** gestützt, sogar als Selbstaussage (I8, I15).
- **H1 (Wiederkehr nicht geprüft):** gestützt bei D-020. Die Regel wurde angenommen, die Wirkung nur „observe“ (I7).
- **H4:** in diesem Abschnitt nicht berührt.

**Neu gegenüber H1–H4:**
- **Wer entscheidet.** Die Investition setzte durchgehend auf die Zustimmung des Eigentümers: „ADMIT“, „Go“, „REFINE → ACCEPT“. Diese Zustimmung gab er zu Entscheidungsflächen, die Chats in Minuten erzeugt hatten (I5, I11). Damit beruhten die Investitionsentscheidungen auf Texten, deren Prüftiefe er nicht beurteilen kann und auch nicht beurteilen soll (Leitziel, Invariante 4). Das ist keine Ursache beim Eigentümer. Es ist eine Lücke im System: Zwischen der Erzeugung einer Vorlage und der Zustimmung prüft niemand unabhängig.
- **Wohin die Arbeit ging.** Gebaut wurde Steuerung, Abgleich und Aufräumen (I14). Die einzige fachliche Lücke, die die Projekte wirklich anhielt, wurde als Absatz D-020 und als Werkzeug C1R behandelt. Gelöst wurde sie nicht: Es gab keinen begründeten Vorschlag für den nächsten fachlichen Schritt.

**Noch nicht gelesen:** #202, #206–#208, #211–#215, #226, #227, alle `requirements/`-Dateien und die ganze Oktober-Welle: #230, #244–#261, #272, #276–#297, #306–#309.

## 02.–05.10. · #230, SD-KA-01, #297 (#230 ganz gelesen, #297 nur Kopf und Aktualisierungen bis 07.10., Zeitpunkte über die REST-API)

**I16 · Das Pendel schlug von „so klein wie möglich“ zu „zuerst ausreichend“ um, und beides stand als Text da.** Im September galt die Leitlinie, nichts Überflüssiges zu bauen. #85 verzichtete deshalb auf ein Hilfsprogramm (`primaer-knau.md` B12). Am 02.10. benannte #230, auf Wunsch des Eigentümers, das Gegenteil als zentralen Fehler: „minimality has too often been treated as an input constraint on solution design instead of a post-sufficiency optimization criterion“. Daraus folgte der Grundsatz „Sufficient architecture first; simplify without loss second“. Er steht heute als „Adequacy before minimality“ in `AGENTS.md`. Die ursächliche Einordnung lautete: „a real coupled structural gap … in Repository Knowledge Lifecycle + Work/Programme Lifecycle + Operational Context Composition“ (#230, Kommentar vom 02./03.10.). *Deutung:* Die Investition im Oktober galt der Verwaltung des eigenen Textbestands. Gemeint sind Lebenszyklus, Aktualität, Ablösung und Kontextzusammenstellung, also die Folgen von Z2. Das Mittel gegen zu viel Text war Architektur für Text.

**I17 · Sechs Arbeitspakete in 27 Stunden, die Schlussprüfung in drei Minuten.** SD-KA-01 WP1–WP6 wurde am 04.10. um 20:22 und 20:23 angelegt. Der letzte Schritt, „WP6: run adversarial terminal qualification“ (#301), wurde am 05.10. um 23:04 angelegt und um 23:07 geschlossen. „persist terminal Result Review and accepted baseline“ (#302) lief von 23:13 bis 23:14. **Vier Stunden vorher**, um 19:13, war #297 als „CRITICAL SYSTEM REGRESSION / MAX PRIORITY“ angelegt worden. *Deutung:* Am selben Abend stellte das System einen kritischen Rückfall fest und nahm seine neue Architektur nach einer dreiminütigen „adversarial qualification“ ab. Stärker lässt sich H2 kaum belegen: Abnahmesignale entstehen in Minuten und unabhängig vom erkannten Zustand.

**I18 · #297 benennt das Muster und bleibt offen.** Der Fehler lautet: „integrated higher-order plan … → assistant optimizes for a small/lean next step … → local step can look correct while the intended complete transition remains unsafe/incomplete → Human must stop the reduction explicitly“. Die Folge sind sechs Pflichtprüfungen, „a continuous acceptance/assurance condition“, kein Mechanismus (#297, Text). Die Aktualisierungen vom 07.10. sprechen von „partial positive efficacy but overall FAIL“. Bis zum 28.10. kehrt der Fehler wieder: Ein frischer Chat lud das gebaute Werkzeug `savesax` nicht, sondern lud Bilder per Browser und `curl` (#297, Nachträge vom 27. und 28.10.). *Deutung:* Das stützt H3 (Pflichtprüfungen als Text) und H4: Das Werkzeug existiert, aber die Laufumgebung aktiviert es nicht. Es ist dasselbe Muster wie Generator B im September (`primaer-knau.md` B28).

## Zwischenergebnis über beide Phasen (Deutung, angreifbar)

Die vier Hypothesen tragen am Primärmaterial. Sie lassen sich aber auf **eine tiefere Ursache** zurückführen, die auch den Einwand des Eigentümers aufnimmt (Investition vor Fachbeitrag):

> **Das System hat keine von der KI unabhängige Instanz, die Qualität feststellt.** Pläne, Forschungsprogramme, Synthesen, Konzepte, Code, Tests, Prüfungen und Abnahmen entstehen alle im selben Typ Chat. Oft geschieht das in Minuten (I1, I4, I11, I17; `primaer-knau.md` B20). Der Eigentümer stimmt nur zu, und er soll Prüftiefe nicht beurteilen müssen.

Folgen dieser einen Ursache:
- **H2:** Was den Abnahmeschritt bestanden hat, kostet so viel wie Text. Deshalb ist es billig.
- **H3:** Gegenmittel richten sich an denselben Chat, also bleiben sie Text.
- **H1:** Ob ein Fehler wiederkommt, prüft niemand außer dem nächsten Chat derselben Art. Der Eigentümer bemerkt es erst im Betrieb (P10).
- **H4:** Was eine Laufumgebung nicht kann, fällt erst auf, wenn ein frischer Chat scheitert. Es gibt keinen dauerhaften Prüfstand, der denselben Fall wiederholt ausführt.
- Die Investition fließt deshalb in das, was ein Chat selbst schreiben und selbst abnehmen kann: Steuerung, Abgleich, Aufräumen (I14). Was nur außerhalb des Chats prüfbar ist, bleibt liegen: das Bild, die Richtigkeit einer Lesung, ob ein Werkzeug in einer neuen Umgebung läuft, ob eine Regel wirkt.

**Gegenprobe:** Wo eine Prüfung außerhalb des Chats lag, wirkte sie.
- Der Eigentümer stoppt eine Verkleinerung (#297) oder einen Zweig (I13).
- Die CI meldet veraltete Testtexte (`primaer-knau.md` B22).
- Ein zweiter Chat erkennt eine unbelegte Behauptung, etwa „Generator B lief“ (B28).
- Der Bildvergleich widerlegt eine alte Lesung (B19).

Es sind also nicht die Regeln, die fehlen. Es fehlen Prüfinstanzen, die nicht vom selben Modell abhängen. *Grenze:* Diese Gegenprobe beruht auf wenigen Fällen. Wie viel davon an den Plattformen liegt (ChatGPT mit Connector, Claude im Container), ist nicht getrennt.

**Nicht gelesen** und für eine Abnahme dieses Zwischenergebnisses nötig: #244–#261 im Einzelnen, #272, #276–#296, #306–#309, die Oktober-PRs, die `requirements/`- und `engineering/`-Dateien sowie die Phase ab 26.10. mit Nr. 632.

## Abgleich mit vorhandenen Analysen (03.11.2026, abends)

Gesichtet nach Überschriften, Befundlisten und Stichworten. Volltext gelesen nur dort, wo er unten genannt ist.
- **Auf `main`:** `engineering/catalog/findings.tsv` (F01–F45), 30 Audits unter `engineering/evidence/audits/`, drei Lern-Dokumente unter `engineering/evidence/learning/`, die LEARNINGS der Projekte.
- **Auf Branches:** #401 (`systemaudit-2026-11-chatgpt.md`, RC1–RC6, §7 gelesen), #402, #408 (`ansatz.md` H-A–H-I, `infrastruktur.md` Z1–Z5) und #409 (K1–K7).

**Ergebnis: Der Kern meines Zwischenergebnisses ist nicht neu.**

| meine Aussage | schon vorhanden |
|---|---|
| keine von der KI unabhängige Prüfinstanz; Wechsel von Chat oder Rolle schafft keine Unabhängigkeit | #401 RC2 („Unabhängigkeit von Chat/Modell/PR ist nicht Unabhängigkeit der Evidenzbasis“) und RC6 („Rollentrennung ohne … unabhängige Aufgaben- und Beweisprüfung wird zur gegenseitigen Bestätigung“); L023; Katalog F10 (`unresolved`) |
| H3: Regeltext sichert das Verhalten nicht | Katalog F44; #405 P3; `ansatz.md` H-E; `infrastruktur.md` Z4; Lernbefund vom 23.09. |
| H2: Form statt Ergebnis, lokaler PASS | #401 RC1 und Fehlkreis A; F11; `infrastruktur.md` Z5; #405 P7; #297 |
| Eigentümer als Bote | F20; #405 P10; #401 §8; `infrastruktur.md` 2d |
| Zustimmung ohne beurteilbare Prüftiefe | F21 („Authorization is not informed decision readiness“) |
| Eingaben des Eigentümers werden zu Zweigen | F43; Lernbefund vom 18.09.; #405 3b |
| Verbot einer Arbeitsweise (Formenverzeichnis) | F45; #405 P5; #409 A |
| Wiederkehr nicht geprüft | #405 P2; `ansatz.md` H-E |

**Nach diesem Abgleich möglicherweise neu** (nur gegen Überschriften geprüft, noch nicht gegen Volltexte):
- Zeitstempel als Beleg dafür, dass Abnahme billig ist: Forschung, Synthese und Abnahme in Minuten (I1, I4, I11, I17; `primaer-knau.md` B20)
- der Bildzugang als dauerhafter Engpass, Folge der Aufteilung auf getrennte Chats schon im August (B9–B11). `infrastruktur.md` Z1 und Z3 sehen den Engpass erst ab dem Wechsel der Umgebung.
- #166 gewinnt einen Befund vom 29.08. zurück (B33). #401 RC2 und #409 führen #166 als Beleg für die Rückkehr zur Quelle.
- Tests, die den Wortlaut des Forschungsstands prüfen, als Mechanismus der Reibung (B22, B26)
- das gebaute Werkzeug lief im neuen Chat schon im September nicht (B28). Bekannt ist dieser Befund bisher für Ende Oktober (#368 B1).

**Folgerung:** Die Ursache ist seit Wochen mehrfach richtig beschrieben: am 14.09. (I3), 19.09. (I14), 23.09. (I15), 09.10. (Audit zur deterministischen Kontrollschicht), 02.11. (#401) und 03.11. (#409). Die offene Frage ist deshalb nicht mehr, *was* die Ursache ist. Offen ist, **warum richtige Diagnosen nicht zu wirksamer Änderung führen** (#405 P2, dort „offen“). Ein Hinweis darauf, der noch zu lesen ist: Am 09.10. schlug ein Audit eine kleine Kontrollschicht vor, die nicht von der KI abhängt („small fail-closed control layer“). Eine kritische Nachprüfung verwarf sie am selben Tag als „False Lean“, mit dem Ergebnis „existing owners and vertical qualification first“.

## Einordnung unter #410 (statt eines eigenen Plans)

Seit 03.11.2026, 19:34, gibt es mit #410 einen vom Eigentümer für P0 freigegebenen, zentralen Untersuchungsauftrag mit den Phasen P0–P5. Ein Entwurf zu P0 liegt in `p0-410-untersuchungsanlage-2026-11-03.md` (Commit `93c5ed5`). Ein eigener Plan wäre eine Dopplung und entfällt.

- `primaer-knau.md` und diese Datei sind **Material für #410 P2 und P3**: zeitlich geordnete Rekonstruktionen von Ketten am Primärmaterial, mit Fundstellen. Sie sind nicht abgenommen und keine zweite Planung.
- Die Leitfrage oben, warum richtige Diagnosen nicht zu wirksamer Änderung führen, entspricht #410 P3.4 (Fehler → Diagnose → Reparatur → realer Gebrauch → Erfolg oder Rückfall) und P5.1 („Weshalb verhinderten bestehende Kontrollen die Rückfälle nicht?“).
- **Hinweis für den P0-Rückkehrpunkt:** Die Tabelle P0.1 im Entwurf berücksichtigt diese beiden Dateien nicht. Sie entstanden kurz vor dem Entwurf. Auch `engineering/catalog/findings.tsv`, die Audits zur Kontrollschicht vom 09.10. und #401 RC1–RC6 sind dort nicht abgeglichen. Der Abgleich oben kann dafür Material sein.
