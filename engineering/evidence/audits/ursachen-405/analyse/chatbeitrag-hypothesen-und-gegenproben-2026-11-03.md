# Gesprächshypothesen und Gegenproben: transdisziplinäres Editionsziel, KI und Systementwicklung

**03.11.2026, abends · Gesprächsherkunft: ChatGPT / Human Owner · analytischer Beitrag zu [#405](https://github.com/esany/paleo-type/issues/405) und [#408](https://github.com/esany/paleo-type/pull/408).**

**Status: vorläufig, nichtnormativ, nicht unabhängig validiert.** Keine Ursachenabnahme, kein Forschungsurteil, keine neue Aufgabe, kein Architektur- oder Implementierungsauftrag. Ziel ist, die vorläufigen Beobachtungen dieses Chats mit Fundstellen, Gegenbelegen und offenen Prüfbedingungen außerhalb des Chats verfügbar zu halten. Diese Notiz ersetzt weder das bestehende Analyseprotokoll in #408 noch seine Systemkarte. Die überlieferte Unterhaltung ist ein Hinweis auf Fragen, **keine Primärevidenz für deren Ursachen**. Nr.-632-Lesungen wurden hierfür nicht eingesehen.

## A. Fachliches Ziel als Maßstab, nicht als Motto

Das [Governing Objective](https://github.com/esany/paleo-type/blob/main/GOVERNING_OBJECTIVE.md) stellt die quellengebundene wissenschaftliche Erschließung frühneuzeitlicher Handschriften ins Zentrum. Ein transdisziplinäres Editionsprojekt braucht die für die konkrete Frage maßgebliche Erfahrung aus Paläographie, historischer Philologie, Archivwissenschaft/Diplomatik, Editionswissenschaft/Textkritik, historischer Quellenkritik und gegebenenfalls Kodikologie, Onomastik, Metrologie und weiteren Domänen. Die Domänen sind **unterschiedliche Erkenntnis- und Prüfkompetenzen**, keine beliebig kombinierbaren Textetiketten. Technische RSE-/Datenarbeit dient diesen Grenzen und darf sie nicht für die eigene Bequemlichkeit umdeuten.

Belege: [#73 Domain Review](https://github.com/esany/paleo-type/issues/73), [historical-source-workflow](https://github.com/esany/paleo-type/blob/main/methodology/historical-source-workflow.md), [domain-requirements.tsv](https://github.com/esany/paleo-type/blob/main/requirements/domain-requirements.tsv), darunter REQ-DOM-009: erfahrungsbasiertes Fachwissen führt zu expliziten Fragen, Kandidaten und Tests, nicht zu unsichtbaren Behauptungen. [#73](https://github.com/esany/paleo-type/issues/73) beschreibt ausdrücklich die Funktion **Quellenbefund → disziplinäre Prüfung/Synthese → nächste wissenschaftlich zulässige Handlung → nur begründet Anforderung/Entwicklung → fachliche Rückprüfung → Rückkehr zur Forschung**. Das reale [Knau-Domain-Review](https://github.com/esany/paleo-type/blob/main/projects/ega-reg-ii-5-knau/research/g2-domain-review-checkpoint-b.md) erprobte sie. Der [Audit 14.09.](https://github.com/esany/paleo-type/blob/main/engineering/evidence/audits/research-framing-transdisciplinary-competency-audit-2026-09-14.md) benannte bereits ihre verminderte operative Sichtbarkeit. **Das ist kein neuer Befund dieses Chats.** Welche späteren Fehlentscheidungen dadurch verursacht wurden, ist unbewiesen.

**Fachlicher Grenzfall:** Die legitime Zurückhaltung bei historischen Identifikationen und nicht bewiesener Handgleichheit darf nicht in den Verzicht auf jede sachgerechte graphische, formularbezogene oder domänenspezifische Vergleichsarbeit umschlagen. Umgekehrt ist ein älteres Lexikon kein automatisch wiederverwendbarer Lesungsbeweis. [Knau LEARNINGS](https://github.com/esany/paleo-type/blob/main/projects/ega-reg-ii-5-knau/LEARNINGS.md) L001/L004 und [#124](https://github.com/esany/paleo-type/issues/124) zeigen die qualifizierte Unterscheidung: problemgebundene Vergleiche ja; unbelegte gleiche Hand und ungeklärte Legacy-Witness-Provenienz nein.

## B. Gesprächshinweise: Herkunft und vorsichtige Gegenprüfung

| Vorläufiger Gesprächspunkt | Status und Repository-Anker | Noch **nicht** belegt |
|---|---|---|
| Gute Software wurde verworfen und parallel neu entwickelt. | **Eigentümerhinweis.** [#353](https://github.com/esany/paleo-type/issues/353) W1–W5, die bewusste [Supersession](https://github.com/esany/paleo-type/issues/353#issuecomment-6533380500), [#376](https://github.com/esany/paleo-type/issues/376), [PR #382](https://github.com/esany/paleo-type/pull/382) und [#394](https://github.com/esany/paleo-type/issues/394) sind konkrete Spuren. | **Nicht** belegt ist vollständige Verwerfung: #353 enthielt auch Vorschläge, keine fünf fertigen Tools; die Schließung diente ausdrücklich dem Beenden paralleler Roadmaps. Ursache und Folgen der Nichtnutzung bestehender Funktionen müssen im Entwicklungsverlauf geprüft werden. |
| Viele Bugs/Tickets sind Symptome derselben Ursache. | **Eigentümerhypothese.** [#230](https://github.com/esany/paleo-type/issues/230), [#297](https://github.com/esany/paleo-type/issues/297), [#404](https://github.com/esany/paleo-type/issues/404) dokumentieren wiederkehrende Familien und lokales Bestehen ohne Gesamtwirkung. | Ob alle oder welche Fälle tatsächlich eine gemeinsame **Kausalursache** haben; die Ticketmenge allein beweist dies nicht. |
| Liegt es am Prompten? | **Offene Frage.** [AGENTS.md](https://github.com/esany/paleo-type/blob/main/AGENTS.md) verlangt schon angemessene Lösungen, [#404](https://github.com/esany/paleo-type/issues/404) zeigt einen Rückfall trotz geladener Regel. [SPICKZETTEL](https://github.com/esany/paleo-type/blob/main/SPICKZETTEL.md) verteilt Rollen und Stichwortaktionen. | Weder „mehr Prompt ist die Lösung“ noch „Prompts sind die Hauptursache“ folgt daraus. Formulierungs-, Anwendungs-, Kontext- und Capability-Defekte sind zu unterscheiden. |
| Methodisch wirksames Tooling fehlt – das ist seit Langem bekannt. | **Eigentümerkorrektur** an einer Wiederholung durch ChatGPT. Siehe [#355](https://github.com/esany/paleo-type/issues/355), [#353](https://github.com/esany/paleo-type/issues/353) und [#394](https://github.com/esany/paleo-type/issues/394). | Die bloße Diagnose erklärt **nicht**, warum bekannte Funktionen/Teillösungen nicht zuverlässig integriert und genutzt wurden. |
| Fachlich-transdisziplinäres Erfahrungswissen und die domänenspezifischen Analysen/Anforderungen bilden das eigentliche Zielbild. | **Ausdrückliche Eigentümerpräzisierung dieser Unterhaltung**, deckungsgleich mit dem Governing Objective, [#73](https://github.com/esany/paleo-type/issues/73) und der Requirements-Baseline. | Welche fachlichen Funktionen an welchen **konkreten** Arbeitsübergängen fehlen, wäre noch zu ermitteln. |

Die zusätzlichen Formulierungen „falsche Einheit des Erfolgs“, „Ticket-Reparaturschleife“, „fehlende Lösungskontinuität“ und „Prompt-Abhängigkeit“ stammen zunächst **vom Assistenten**. Sie dürfen nicht als unabhängig belegte Ursachen, neue Erkenntnisse des Human Owners oder empirische Resultate ausgegeben werden. Vergleichbare Thesen stehen bereits in #230/#297 sowie im Entwurf #408.

## C. Konkurrierende Hypothesen – die Verbindungsglieder müssen geprüft werden

### K1 · Fachübergreifende Synthese wirkt nur unzuverlässig

**Mechanismus als Hypothese:** Quellenbeobachtungen und Fachanforderungen existieren einzeln, werden aber nicht zuverlässig zu einer angemessenen wissenschaftlichen Frage, einer fachübergreifenden Abwägung und einem tragfähigen nächsten Handlungsschritt verbunden.

**Stütze:** [#73](https://github.com/esany/paleo-type/issues/73) beschreibt genau diese operative Funktion; der [Audit vom 14.09.](https://github.com/esany/paleo-type/blob/main/engineering/evidence/audits/research-framing-transdisciplinary-competency-audit-2026-09-14.md) kritisierte ihre spätere geringere Sichtbarkeit.

**Gegenbefund:** [#166](https://github.com/esany/paleo-type/issues/166) erzielte durch differenzierte Quellen- und Vergleichsarbeit eine echte, quellengebundene Struktur-/Funktionsklärung; die Funktion ist also nicht generell unmöglich oder verschwunden. **Prüffrage:** Wo wurde eine tatsächlich relevante Disziplin/eine konkurrierende Deutung in Nr. 632 oder anderen Fällen trotz vorhandener Evidenz nicht aktiviert? Wo gelang es?

### K2 · Domänenerfahrung und erprobte Lesepraxis werden zwischen Fällen nicht sachgerecht übertragen

**Mechanismus:** Fachlich gebundene Vergleiche, Experimente und lessons learned bleiben lokal; ein späterer Chat erfindet Verfahren neu oder verwirft Erfahrungen aufgrund übervorsichtiger Generalisierung.

**Stütze:** [LEARNINGS](https://github.com/esany/paleo-type/blob/main/projects/ega-reg-ii-5-knau/LEARNINGS.md), [#124](https://github.com/esany/paleo-type/issues/124), [#394](https://github.com/esany/paleo-type/issues/394).

**Gegenbefund:** Die historische Lexikon- und Vergleichspraxis hatte echte **Quellen-/Handprovenienzgrenzen**; alte Arbeitsdaten dürfen nicht unkritisch zum aktuellen Prüfmaßstab erhoben werden. **Prüffrage:** In welchen realen Nr.-632-Loci scheiterte die Verwendung eines *zulässigen* Vergleichs – und lag das an Nichtauffindbarkeit, technischem Zugang, falschem fachlichem Urteil oder einer begründeten Unterlassung? Diese Notiz prüft keine Handschriftenlesung.

### K3 · Wissenschaftlicher Bedarf erreicht die Softwareentwicklung, kehrt aber nicht als fachlich passende Fähigkeit zurück

**Mechanismus:** Der lokale Entwicklungsauftrag optimiert Eingaben, Parser und CI seines gegenwärtigen Formats statt eine quellen- und disziplinadäquate wiederverwendbare Funktion; dadurch entstehen parallele Ansätze/Migrationskosten.

**Stütze:** [#353](https://github.com/esany/paleo-type/issues/353), [#355](https://github.com/esany/paleo-type/issues/355), [#376](https://github.com/esany/paleo-type/issues/376), [PR #382](https://github.com/esany/paleo-type/pull/382), [#394](https://github.com/esany/paleo-type/issues/394). Das erprobte Knau-Modell der zeilenweisen TSV-Lesung und die Markdown-Lesungen als aktueller Editionsbuilder-Eingang sind verschiedene Ansätze.

**Gegenbefund:** #353 W1–W5 waren teils nur Kandidaten; eine kleine Vorschau aus vorhandenen Markdown-Daten kann in einem eng begrenzten Stadium legitim sein. Nr. 632 besitzt nicht automatisch evidenzgesicherte Archivfoliierung. **Prüffrage:** Pro Funktion den Weg **fachlicher Bedarf → vorhandener Bestand → Eignungs-/Verlustprüfung → Designentscheidung → tatsächliche Implementierung → fachlicher Rücklauf** rekonstruieren, nicht nur Dateinamen vergleichen.

### K4 · Lokaler technischer Erfolg ersetzt die Prüfung des wissenschaftlichen Gesamtzwecks

**Mechanismus:** Ticketabschluss, CI-Status oder PR-Review sind leicht verfügbar; der viel schwierigere Nachweis, dass ein Forschungs- oder Systemziel tatsächlich erreicht wurde, bleibt offen. Anschließend folgen weitere Bugtickets.

**Stütze:** [#230](https://github.com/esany/paleo-type/issues/230), [#297](https://github.com/esany/paleo-type/issues/297), [#404](https://github.com/esany/paleo-type/issues/404).

**Gegenbefund:** Das Repository unterscheidet ausdrücklich schon technische und wissenschaftliche Abnahme, und [#166](https://github.com/esany/paleo-type/issues/166) ist ein legitimer, begrenzt abgeschlossener Erkenntnisschritt. **Prüffrage:** Für konkrete „PASS“-Fälle die wirklich getestete Geltung, die höhere Anforderung, Folgevorfälle und alternative Erklärungen rekonstruieren.

### K5 · Kontexte/Reviews vererben fehlerhafte Prämissen

**Mechanismus:** Ein neuer KI-Kontext übernimmt die frühere Problemfassung oder prüft einen PR nur gegen den selbst erzeugten Auftrag; scheinbare Unabhängigkeit ersetzt keine neue Evidenz.

**Stütze:** [#394](https://github.com/esany/paleo-type/issues/394), [#404](https://github.com/esany/paleo-type/issues/404), [#405](https://github.com/esany/paleo-type/issues/405) §3b, [#297](https://github.com/esany/paleo-type/issues/297).

**Gegenbefund:** [#166](https://github.com/esany/paleo-type/issues/166) gelang durch eine eigenständige Primärquellenprüfung; nicht jede Übergabe ist fehlerhaft. **Prüffrage:** Bei jedem geprüften Fall trennen zwischen Quellenzugang, tatsächlich gelesenen Grundlagen, übernommenen Hypothesen, frischer Prüfung und zulässiger Aussageebene. „Frischer Chat“ und „andere KI“ allein sind keine Unabhängigkeitskriterien.

### K6 · Rollen, Plattform und konkrete Werkzeuge passen nicht zusammen

**Mechanismus:** Bildzugang, Code/Tests, GitHub-Persistenz und fachliche Review-Aufgaben werden auf verschiedene Kontexte verteilt. Fähigkeitslücken werden durch Übergaberituale oder zusätzliche CI-Kontrollen kompensiert, die selbst Reibung erzeugen.

**Stütze:** Bildzugriffsgrenze in [#166](https://github.com/esany/paleo-type/issues/166); [#355](https://github.com/esany/paleo-type/issues/355); [#368](https://github.com/esany/paleo-type/issues/368); bereits vorliegende [Infrastrukturuntersuchung #408](https://github.com/esany/paleo-type/blob/analysis/ursachen-405-erhebung/engineering/evidence/audits/ursachen-405/analyse/infrastruktur.md).

**Gegenbefund:** [#404](https://github.com/esany/paleo-type/issues/404) trat auch in einem codefähigen Claude-Kontext auf. **Prüffrage:** Wechsel von Arbeitsumgebung, jeweils *tatsächlich* vorhandene Fähigkeiten, neu entstandene Ausgleichsarbeit und fachliches Resultat entlang einer Zeitfolge prüfen. Die Modusbezeichnung allein erklärt nichts.

### K7 · Die Reparaturorganisation wird zum konkurrierenden Arbeitsgegenstand

**Mechanismus:** Vorfall → neue Regel/Ticket/Prüfung → mehr Übergabe- und Kontextaufwand → höheres Risiko weiterer Auslassungen → nächster Vorfall. Das technische Signalsystem kann gleichzeitig „grün“ sein.

**Stütze:** [#230](https://github.com/esany/paleo-type/issues/230), [#297](https://github.com/esany/paleo-type/issues/297), [#404](https://github.com/esany/paleo-type/issues/404). Der [SPICKZETTEL](https://github.com/esany/paleo-type/blob/main/SPICKZETTEL.md) kennt eine Issue-Reihenfolge für den gewöhnlichen „weiter“-Weg.

**Gegenbefund:** Die Schließung von [#353](https://github.com/esany/paleo-type/issues/353#issuecomment-6533380500) war eine **bewusste** Reduktion paralleler Planung; [#399](https://github.com/esany/paleo-type/issues/399) hält „weiter“ derzeit an. Vor allem [#166](https://github.com/esany/paleo-type/issues/166)/[#201](https://github.com/esany/paleo-type/issues/201) zeigen, dass ein Teil des Wechsels zur Systemarbeit ausdrücklich gewählt wurde. **Prüffrage:** Kausalfolge und Gegenfälle statt bloßer Ticketanzahl vergleichen.

## D. Wirkungsgefüge – bislang Prüfobjekt, keine Schlussfolgerung

~~~text
Quelle + fachliches / transdisziplinäres Erfahrungswissen
  ↓ [K1/K2: angemessen aktiviert und an Primärmaterial geprüft?]
wissenschaftliche Frage, Beobachtung, Konkurrenzhypothesen
  ↓ [K3: Bedarf richtig in technisches oder fachliches Handeln übersetzt?]
verfügbare Methoden, bestehendes Tooling, ggf. Entwicklung
  ↓ [K6: passt die konkrete Ausführungsumgebung?]
Forschung und Erstellung von Quellen-/Editionsdaten
  ↓ [K4/K5: tragfähiger Geltungsnachweis oder nur formaler PASS?]
fachlich sinnvolles, überprüfbares Resultat
  ↖ Rückbezug auf Quellen und nächste wissenschaftliche Frage

Vermutete, noch nicht zeitlich nachgewiesene Neben-Rückkopplung:
Fähigkeitslücke / lokale Fehlentscheidung
→ neues Ticket, Prompt, CI oder Übergabe
→ mehr Kontext, Abhängigkeiten und Friktion
→ höhere Wahrscheinlichkeit fehlerhafter Prämissen / lokalen PASS
→ erneuter Vorfall
~~~ 

Es **kann** mehrere gekoppelte Ursachen geben, die nicht in jedem Fall zugleich wirken. Die Hypothesen erklären auch nicht ohne zusätzliche Belege, wie gut die KI Handschrift lesen kann oder wie die fachliche Validierung im Einzelnen ausfiel.

## E. Anschließende Prüfungen innerhalb der bereits laufenden Analyse

Diese Punkte sind **mögliche Prüffragen**, kein neues Verfahren und kein fremder Arbeitsauftrag.

1. **Wendepunkt September:** [#166](https://github.com/esany/paleo-type/issues/166), [#183](https://github.com/esany/paleo-type/issues/183), [#201](https://github.com/esany/paleo-type/issues/201), D-020, Audit vom 14.09. Die bereits vorhandene [W1-Analyse in #408](https://github.com/esany/paleo-type/blob/analysis/ursachen-405-erhebung/engineering/evidence/audits/ursachen-405/analyse/pilot-w1.md) ist **vorläufiges Material**; keinesfalls ohne Quellenprüfung neu als unabhängigen Befund verkaufen.
2. **Knau → Nr. 632:** Die gleiche **fachliche Funktion**, nicht nur das gleiche TSV-Format, verfolgen: Zeilenbindung, Schreibvergleich, Quellenprovenienz, Unsicherheitsrepräsentation, Editionsableitung, fachliche Rückprüfung. Gegenbeleg #124 bewahren.
3. **30.10.–03.11.:** #353, #355, #358, #376, PR #382 und #394 **mit Kommentaren/Änderungen** auswerten: Vorschlag, Freigabe, Implementierung, fachliche Abnahme, Rücknahme/Anhaltung strikt unterscheiden.
4. **Wiederkehr trotz Regel:** #297 und #404 gegen auch wirklich erfolgreiche, begrenzt abgeschlossene Fälle testen. „Regel war vorhanden“ und „Regel wirkte“ sind zwei unterschiedliche Beobachtungen.
5. **Andere Repos:** Die in [#408](https://github.com/esany/paleo-type/pull/408) verfügbaren Exporte von wissensarbeit/design-lab wurden **hier nicht selbstständig geprüft**. Kein repoübergreifender Ursache-Befund.

## F. Abdeckung, Selbstprüfung und Grenzen

**Direkt gesehen bzw. gezielt nachgesehen:** Governing Objective, AGENTS, README, ausgewählte Passagen/Gliederung DECISIONS, zentrale METHOD- und Requirements-Passagen; Audit 14.09. (Struktur und ausgewählte Abschnitte); Knau LEARNINGS (Auszüge); #73, #124, #166, #171, #183, #201, #230, #297 (Body / Auszüge), #353, #355, #376, PR #382, #394, #396, #398, #400, #404, #405, PR #408 sowie dessen Ansatz, Infrastrukturtext und W1-Pilot (teils in Auszügen). Einzelne echte Reg.-Ii.-5-Transkriptions-/Werkzeugdateien und der Nr.-632-Editionsbuilder wurden auf den entsprechenden Branches angesehen, nicht in der Tiefe getestet.

**Nicht eigenständig vollständig geprüft:** gesamte Git-/Issue-/PR-Geschichte; alle Engineering-/Requirements-/Methodikartefakte; komplette Fachdokumentation; alle Originalbild- und Lesebelege; fachliche Expertise von Dritten; gesamter Inhalt von wissensarbeit und design-lab. Die aus #405/#408 übernommenen Beobachtungen stammen ebenfalls aus KI-Arbeit und sind ohne Nachprüfung keine unabhängige Kausalbestätigung.

**Fazit dieser Notiz:** Gesprächshypothesen sind jetzt **als angreifbare Fragen mit Fundstellen und Gegenbelegen** gesichert. Eine abgeschlossene systemische Ursachenanalyse ist damit **nicht** erstellt. Eine spätere Untersuchung darf und soll die Hypothesen verwerfen, wenn die Primärbelege nicht tragen.

**Keine Änderungen/Autorität:** kein main, keine Forschungstranskription, kein Project NEXT ACTION, keine Fachannahme, keine neue Methodenregel, keine Veränderung an Issues/Labels, kein Merge in #408.
