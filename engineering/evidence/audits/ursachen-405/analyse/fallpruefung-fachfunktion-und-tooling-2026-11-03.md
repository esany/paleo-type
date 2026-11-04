# Fallprüfung: Von fachübergreifender Kompetenz zur Forschungssoftware – Kontinuität und Brüche

**03.11.2026 · unabhängiger, eng begrenzter Analysebeitrag zu #405/#408; keine kausale Gesamtbewertung.** Zu lesen zusammen mit [Gesprächshypothesen](chatbeitrag-hypothesen-und-gegenproben-2026-11-03.md). Der Human Owner fragte ausdrücklich nach der Verbindung aus fachlich-transdisziplinärem Erfahrungswissen, bekannter methodischer Tooling-Lücke, wiederholter Softwareentwicklung und Bug-/Ticket-Spiralen. Hier wird **eine** quellennahe Übergangskette geprüft, ohne daraus die Ursache des Gesamtsystems abzuleiten.

## 1. Wissenschaftliche Funktion war inhaltlich beschrieben – doch welche Teilfunktion wurde später umgesetzt?

- [#73 Domain Review](https://github.com/esany/paleo-type/issues/73) definierte eine **übergreifende fachliche Übersetzungs- und Rückprüffunktion**: Befund an der Quelle → betroffene Fächer und deren Kompetenzgrenzen → angemessene Frage/Forschungsreihenfolge → erst bei nachgewiesener Lücke Softwareanforderung → Rückprüfung, ob die technische Antwort fachlich genügt → Forschung. Ein Beispiel ist [Knau G2 Checkpoint B](https://github.com/esany/paleo-type/blob/main/projects/ega-reg-ii-5-knau/research/g2-domain-review-checkpoint-b.md).
- Der [Audit 14.09.](https://github.com/esany/paleo-type/blob/main/engineering/evidence/audits/research-framing-transdisciplinary-competency-audit-2026-09-14.md) benannte die operativ weniger sichtbare **Forschungsrahmung/Synthese vor Aufgabenwahl**. Das war ausdrücklich eine **analytische Aussage**, keine neue normative Methode.
- [D-020](https://github.com/esany/paleo-type/blob/main/DECISIONS.md) wurde am 15.09. angenommen: **Wenn** eine neue Prioritätsentscheidung tatsächlich ansteht und noch keine wissenschaftliche Richtung ausgewählt ist, mehrere evidenzgebundene ernsthafte Richtungen kritisch prüfen, **dann** Eigentümerentscheidung. D-020 enthält **keine** festgelegte Domänenrolle, kein automatisches Ranking und keinen universellen Forschungslayer.

**Feststellbar:** #73 und D-020 sind **nicht deckungsgleich**. D-020 regelt einen bestimmten Entscheidungsauslöser (vor neuer Forschungspriorität), während #73 auch laufende interdisziplinäre Adäquanzprüfung, fachliche Kontrolle an der Software-Grenze und Rückkehr zur Forschung thematisiert. Aus der engen Reichweite von D-020 folgt **nicht**, dass die anderen Funktionen abgeschafft oder nie in anderen Regeln aufgefangen wurden. Genau diese behauptete Abdeckung ist offen und wäre anhand des aktuellen METHOD-Gesamtkontexts und tatsächlicher Arbeit zu prüfen.

**Gegenprobe:** [#166](https://github.com/esany/paleo-type/issues/166) erbrachte im September ein begrenztes, quellenkritisch tragfähiges Ergebnis (zwei getrennte Absätze/Regeln statt falsch vereinter Einheit) und ist kein Beispiel allgemeiner fachlicher Untauglichkeit. [#201](https://github.com/esany/paleo-type/issues/201) dokumentiert zudem **bewusst gewählte** anschließende Systemarbeit. Eine Diagnose „die KI driftete immer ungefragt ab“ ist damit unhaltbar.

## 2. Bereits funktionierende Software war vorhanden – aber nicht automatisch generisch

**Direkt an der Implementierung festgestellt:**

| Bestand auf main | Tatsächlicher technischer Geltungsbereich | Bedeutung / Grenze |
|---|---|---|
| [Reg.-Ii.-5-TSV (61v)](https://github.com/esany/paleo-type/blob/main/projects/ega-reg-ii-5-knau/transcription/first-reading/61v.tsv) | Physische Zeilen mit Lesung, Region, Phänomen, Status, Alternativen, Belegnotiz. | Belegt ein **praktisch verwendetes strukturiertes Muster**. Es beweist allein noch keine generische, automatisch einsatzfähige Forschungsumgebung. |
| [regii5_evidence_packet.py](https://github.com/esany/paleo-type/blob/main/tools/regii5_evidence_packet.py) | Der Dateiheader bezeichnet einen **projektgebundenen Prototyp**; Blind/Explore/Adjudicate haben verschiedene Quellen-/Lesungszugriffe. Die Standardausgabe wählt nicht automatisch Kandidaten, HTR oder Lexikon. | Eine echte quellen- und prüfbewusste Fähigkeit; **keine** universelle Fähigkeit für Nr. 632 ohne Anpassung und neue Eignungsprüfung. |
| [regii5_visual_retrieval.py](https://github.com/esany/paleo-type/blob/main/tools/regii5_visual_retrieval.py) | Explizit auf Reg. Ii 5, Quelle und PDF-Loci beschränkt; Kandidatenstellen/Ähnlichkeitswerte statt Lesungen oder Handidentifizierung. | Vergleichsfunktion vorhanden, aber **hart auf diesen Quellenausschnitt begrenzt**. Die Aussage „fehlendes Tooling“ muss deshalb zwischen fehlender Funktion, fehlender Portierbarkeit und fehlender Nutzung unterscheiden. |
| [#124](https://github.com/esany/paleo-type/issues/124) und [LEARNINGS](https://github.com/esany/paleo-type/blob/main/projects/ega-reg-ii-5-knau/LEARNINGS.md) | Frühere Lexikon-/Gleichhand- und Notationsannahmen wurden wegen ungesicherter Vergleichs- und Witness-Provenienz qualifiziert. | Ein vermeintliches „einfach wiederverwenden“ könnte neue **wissenschaftliche** Fehler erzeugen. Reusable ist die Prüfidee, nicht automatisch jeder alte Befund. |

**Erste differenzierte Erkenntnis:** Die Alternative „Tooling existiert“ vs. „Tooling fehlt“ ist zu grob. Im untersuchten Fall sind **funktionsfähige, bewusst begrenzte Pilotteile** vorhanden, aber deren Übertragbarkeit und Aktivierung für einen neuen Quellenfall wurden nicht durch den bloßen Besitz der Dateien hergestellt. Ob dies einer der wesentlichen Ursachenfaktoren ist, bleibt eine Hypothese.

## 3. Vom Tooling-Kandidaten zur neuen parallel entstehenden Ableitung

- [#353](https://github.com/esany/paleo-type/issues/353) bot unter W1–W5 Locus-Paket, Transkriptionsdaten/Validierung, Coverage, Leseansicht und Gate-Bereitschaft als **geplantes** integriertes Konzept. Sein [Supersession-Kommentar](https://github.com/esany/paleo-type/issues/353#issuecomment-6533380500) schloss die parallele Roadmap auf **ausdrücklichen Wunsch des Eigentümers**. S0 blieb abgeschlossen, S1 separat aktiv; W1–W5 wurden als historische **Kandidaten** bewahrt, **nicht** als fünf fertig implementierte Tools behandelt.
- Der [Website-Auftrag #376](https://github.com/esany/paleo-type/issues/376) wollte eine automatisch abgeleitete Ansicht und spezifizierte die **vorhandenen Nr.-632-Markdown-Tabellen** als Eingabe, kein neues Format. Das schien den lokalen Auftrag zu erfüllen. [PR #382](https://github.com/esany/paleo-type/pull/382) enthielt tatsächlich den auf diese Forschungs-Markdown-Dateien zugeschnittenen Builder; technische Tests/Vorschauen wurden gemeldet und geprüft. Das belegt eine Implementierung, **keinen** wissenschaftlich angemessenen Formatentscheid und keine fertige Edition.
- [#394](https://github.com/esany/paleo-type/issues/394) registrierte am 03.11. rückblickend den Kontrast zu Knau und den initialen Review-Fehler, den lokalen Entwurf nicht zuerst gegen die bestehende Methode/Werkzeuglandschaft geprüft zu haben. PR #382 wurde deshalb angehalten. [#397](https://github.com/esany/paleo-type/issues/397) schlug eine Migration vor, war seinerseits zum Gesamtaudit angehalten.

**Beobachteter Ablauf:** Ein alter, wissenschaftlich begründeter Datenansatz bestand; ein neuer Auftrag band die Ableitung dennoch zunächst an die aktuelle Markdown-Forschungsrepräsentation; dieser Pfad wurde technisch umgesetzt und anschließend wegen methodischer Fehlpassung angehalten. **Unbewiesen** bleiben die verursachenden Entscheidungsknoten: Wer hatte welches Vorwissen tatsächlich im Kontext? Wurde fachliche Eignung bewusst hintangestellt, nicht erkannt oder wegen Tool-/Runtime-Grenzen nicht praktisch verfügbar? War ein begrenzter Markdown-Prototyp damals vertretbar? Die dokumentierten Aussagen stammen teilweise von beteiligten KIs.

## 4. Was dieser Fall gegen einfache Erklärungen zeigt

- **„Alle guten Werkzeuge wurden weggeworfen“:** zu stark; manche waren nur konzipiert, manche absichtlich quellengebunden, manche tatsächlich vorhanden und nicht genutzt.
- **„Es fehlt nur ein strengerer Prompt“:** nicht belegt; #394 berichtet Prüfversagen trotz bekannter Architektur und #404 trotz geladener Regeln. Das Verhalten und das aktivierte Wissen sind gesondert zu testen.
- **„Die KI kann das fachlich grundsätzlich nicht“:** widerlegt als Pauschalurteil durch #166 und die Knau-Ergebnisse. Umgekehrt genügt ein erfolgreicher Quellenfall nicht als Beweis generischer Zuverlässigkeit.
- **„Die ganzen Systemwellen waren unerwünscht“:** falsch als universelle Aussage; #201 und die #353-Dispositionsentscheidung enthalten Eigentümerentscheidungen.
- **„Nur die Architektur muss jetzt umgebaut werden“:** nicht aus diesem Fall ableitbar. Schon die Trennung **wissenschaftlich gute, aber quellenspezifische Funktion / generische Softwarefähigkeit / richtige Aktivierung im konkreten Chat** ist noch nicht kausal geprüft.

## 5. Noch offene kausale Unterscheidung

Welche **genau nachweisbare** Übergangsstörung verband fachlichen Bedarf mit einer lokal richtigen, aber möglicherweise ungeeigneten Implementierung?

1. **Informations-/Kontextproblem:** Vorhandene Fachfunktion oder Pilottool wurde im konkreten Entscheidungs-/Prüfkontext nicht gefunden.
2. **Eignungs-/Generalitätsproblem:** Die Funktion war gefunden, aber zu quellengebunden und nicht angemessen übertragbar.
3. **Fachliches Übersetzungsproblem:** Die Repräsentation/Softwarevorgabe erhielt ihre normative Wirkung, bevor die Editions- und Quellenanforderungen am Fall gegengeprüft wurden.
4. **Rollen-/Runtimeproblem:** Verantwortlicher Arbeitskontext konnte die passenden Tools nicht tatsächlich ausführen und wich deshalb aus.
5. **Bewusster, begrenzter Prototyp:** Die lokale Lösung war angemessen und erst später änderte sich der erforderliche wissenschaftliche Geltungsbereich.

Diese Alternativen **dürfen gleichzeitig** anteilig zutreffen. Ohne die konkrete Sequenz aus Auftrag, Entwurfsentscheidung, geladenem Kontext, Code, Tests, Review und fachlicher Rückgabe wäre das Etikett „eine tiefe gemeinsame Ursache“ voreilig.

**Abdeckung:** Direkt gelesen: Inhalte von #73, #124, #166, #201, #353/Disposition, #376, #394, #397, Auswahl der METHOD-/DECISIONS-Quellen, TSV 61v und Header/Implementierungsausschnitte der beiden Reg.-Ii.-5-Werkzeuge sowie des Editionsbuilders. Nicht geprüft: vollständige Commit-/Review-/Chat-Trace, alle Domänenanalysen, Originalbild-/Lesungsqualität, weitere Quellen und die Vergleichsrepos. Status der zugehörigen Analysebeiträge in #408 ist nicht als unabhängig bestätigt übernommen. Keine Umsetzung oder Prioritätsänderung.
