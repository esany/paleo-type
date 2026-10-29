# #346 / #347 — autonome Fortsetzung, Wissenssicherung und ehrliche DEV-Readiness

**Stand:** 2026-10-29; **Typ:** nichtnormativer Ursachen-, Anforderungs- und Konzeptaudit; **Bewertung:** PARTIAL / **NICHT DEV-READY** für eine materielle Implementierung.
**GitHub-Baseline:** `main@6adf6c6a944d4e8801f7ec65c376a67cc2583ebd` vor diesem Audit; Arbeitsbranch `audit/issues-346-347-dev-ready-20261029`.
**Arbeitsautorität:** expliziter Human-Auftrag vom 2026-10-29 zur Analyse bis DEV-READY oder nachgewiesener Grenze. Keine Implementierungs-, Prioritäts- oder METHOD-Änderungsbefugnis folgt daraus.
**Primäre Work-/Incident-Owner:** [#346](https://github.com/esany/paleo-type/issues/346) (Fortsetzung/STOP) und [#347](https://github.com/esany/paleo-type/issues/347) (Chat-only-Wissen/Readiness).
**Systemische Referenz:** [#297](https://github.com/esany/paleo-type/issues/297) (Human MAX/P0, nicht schließen/herabstufen); [#280](https://github.com/esany/paleo-type/issues/280) (Whole-System), [#282](https://github.com/esany/paleo-type/issues/282) (produktive Runtime, separater Gegenstand).
**Autoritätsgrenze dieses Artefakts:** Audit-/Review-Evidenz unter dem bestehenden `engineering/evidence/audits/`-Owner, **nicht** neue kanonische Requirement-Baseline, Architekturentscheidung, Project-/Source-Truth, D-016-Admission, aktueller globaler Ausführungscursor oder `NEXT ACTION`. Die beiden Issues behalten ihre je eigene Arbeitshistorie.

## A. Menschliches Ergebnis und Fehlerbild

Das zu schützende Ergebnis ist ein **kohärent zu Ende bearbeiteter, bereits autorisierter Analyseauftrag**, dessen tatsächliche Reichweite nach jedem lokalen Teilabschluss neu gegen die Autorität geprüft wird, und der aus einem frischen Kontext **ohne Chatgedächtnis** korrekt fortgesetzt oder begründet beendet werden kann. Nicht die Anzahl Minuten, Kommentare, Dateien, Tests oder Issues ist das Ergebnis. Die längerfristige Projektwirkung ist verlässlichere Unterstützung tatsächlicher historischer Quellenforschung.

**#346, sicher belegt als Human-/Issue-Bericht:** Ein ausdrücklich länger geplanter autonomer Arbeitsblock endete nach ungefähr acht Minuten. Drei begrenzte Issue-Evidenz-Reconciliation-Slices und fünf Kommentare wurden berichtet; kein PR, keine Implementierung, keine Root-Cause-/Systemabnahme. Nach lokalem PASS wurde keine nachprüfbare Prüfung der noch autorisierten, unabhängigen Ready-Arbeit und keine autoritative STOP-Begründung gezeigt. Der Human Owner musste erneut intervenieren. Diese Zahlen stammen aus dem Incident-Owner; die fünf konkreten Kommentar-IDs, die vollständige ursprüngliche Instruktion, die Toolfolge, zeitlichen Hostgrenzen und der damalige Ready-Frontier sind **in diesem Audit nicht unabhängig rekonstruiert**. Insbesondere ist eine tatsächlich verfügbare vierte Ready-Arbeit damals **nicht bewiesen**. Der Fehler ist **fehlende Abschlussbegründung**, nicht die bloße Dauer.

**#347, sicher belegt als Human-/Issue-Bericht:** Ein detaillierter Folgeplan (Incident → Ursachen → DEV-READY → ggf. Implementierung → wissenschaftlicher Rückweg) wurde im Chat ausgearbeitet, während #346 nur den gröberen Incident-/Erwartungsrahmen besaß. Der Assistent musste dies auf Nachfrage einräumen. Eine inhaltlich tragende Planung durfte darum weder als repository-persistiert noch als entwicklungsreif behandelt werden. Dass bereits daraus falscher Code gebaut wurde, ist **nicht nachgewiesen**. Der vorliegende Human-Auftrag und dieses Audit ersetzen nicht retroaktiv die fehlende ursprüngliche Chat-/Hostspur.

**Unmittelbare Interaktion:** #346 und #347 sind am Prüfungstag offen, ohne Kommentare (frisch per GitHub-Connector gelesen); ihre Bodies enthalten erwartetes Verhalten und Testideen, aber keine abgeschlossene eigene Ursachenqualifikation oder DEV-READY-Abnahme. Beides sind beobachtete Symptome innerhalb einer systemischen Familie, **nicht** bereits bewiesene identische Modellursachen.

## B. Frische kanonische Gegenprüfung / welche Kontrollen bereits existieren

| Owner | Bereits verbindlich / implementiert | Warum der Vorfall damit nicht geschlossen ist |
|---|---|---|
| `GOVERNING_OBJECTIVE.md` | Ergebnis vor Support; Evidenz vor Plausibilität; Human Owner; ein kanonischer Owner; restartbar ohne alten Chat | Normative Zielsetzung ist kein Beweis realen zukünftigen Agentverhaltens |
| `AGENTS.md` | `Adequacy before minimality`; local PASS ≠ whole outcome; GitHub-only; Online-Readback und Besitzer-Reconciliation; menschliche Autoritätsgrenzen | Inhaltliches Verstehen und Fortsetzungsauswahl werden nicht allein durch Text erzwungen |
| `methodology/workflow.md` | Cross-role contract, Task-Start-/Return-Check, aktuelle Ausführungscursor, STOP/Blocker mit Abhängigkeitsautorität, Progress-/Delta- und No-loop-Kontrolle, Frischkontextprüfung | Die Regeln verlangen nicht mechanisch eine vollständige Prüfung aller tatsächlich autorisierten Folgeslices; ohne echte Testspur kann ihre Durchsetzung nicht behauptet werden |
| `methodology/maintenance.md` | One fact/one owner; D-016; programme/phase/result-Reconciliation; keine stillschweigende Whole-Outcome-Schließung | Diese Pflicht kann erfüllt *behauptet* werden, ohne dass der autonome Kontext sie vor Abschluss wirklich ausführt |
| `engineering/configuration.json` | akzeptierte ENGINEERING-Baselines; `active_changes=[]`, `current_focus=null`; SD-KA-01 terminal angenommen | Aus dem aktuellen Engineering-Fokus darf weder ein neues Programm noch eine allgemeine Autorisierung für #346/#347-Implementierung abgeleitet werden |
| `engineering/prompts/CONTRACT.md`, `tools/prompt.py`, `tests/test_prompt.py`, `engineering/assurance/fitness.json` | bounded .prompt, Anti-false-Lean/Status-Laundering, technisch testbare Prompt-Heuristiken und ENG-FIT-06/09 | Keine bewiesene reale Laufzeitprobe „nach erstem PASS prüfen → unabhängigen Ready-Slice fortführen“; keine semantische Garantie aus Heuristik-/CI-PASS |
| #297/#280/#282 | offene Whole-Outcome-/Runtime-Akzeptanz, realer Nachweis des Unterschieds von Technik- und Menschenergebnis | Belegen die systemische Gefahr, aber nicht die konkrete #346-Ausführungsursache oder denselben Laufzeitfehler |

**Befund:** Ein bloßer neuer Absatz „arbeite weiter“ wäre Regelduplikation. Ein generischer Planner, neue Workflow-Engine, neue globale Persistenzschicht oder künstlicher Zeit-SLA ist durch diese Evidenz gerade **nicht** begründet. Auch ein bloßes Issue-Gerüst reicht nicht: die ausfallgefährdete Situation ist der **aktuelle semantische Entscheidungsmoment nach einem lokalen PASS und vor einer Folgenutzung**.

### Kausale Hypothesen, streng nach Evidenzniveau

| ID | Hypothese / Mechanismus | Status | diskriminierender Nachweis |
|---|---|---|---|
| H1 | Lokal fertige Teilpakete wurden fälschlich als ausreichende Gesamtausschöpfung bewertet | Beobachtete Fehldisposition, konkrete interne Ursache offen | ursprüngliche Aufgaben-/Slice-/Endbericht-Kette; kontrolliertes Re-Play |
| H2 | Keine wirkliche Frontier-Prüfung nach Slice; ausführbare unabhängige Arbeit wird unsichtbar | Plausibel, nicht bewiesen für damalige Ready-Menge | Zu jedem Abschluss Zeitpunkt, Kandidat, Autorität, Ready/Blocked/Out-of-scope und Wahl rekonstruieren |
| H3 | Chat-only-Anforderungen/Entscheidungen wurden nicht vor Handoff an natürliche Owner gebunden | Konkretes #347-Symptom belegt | Fresh-boot aus ursprünglichem Repo-Zustand ohne Chat versus Chat-Plan |
| H4 | „Issue existiert“ / „Text dokumentiert“ wurde mit Analyse/DEV-READY verwechselt | Im #347-Ablauf beobachtet; Ausmaß kausal offen | DoR-/DoD-/Negativprobe gegen damaligen Issue-Body |
| H5 | Zeit-/Kontext-/Tool-/Hostgrenze erzwang tatsächlichen frühen STOP | **Offen**, keine Behauptung | originale Laufzeit-/Tool-/Abbruchspur mit gegebener Capability; Hostversion |
| H6 | Modell optimiert systematisch auf kurze Dauer oder minimale Token | **Unbelegt** | vergleichbare unabhängige Wiederholungen mit kontrolliertem Prompt/Host; keine Rückschlussnahme aus acht Minuten |
| H7 | Repository-kontrollierte Regeln sind schon hinreichend, aber reale Modellanwendung streut | Plausible Gegenhypothese zu neuem Softwarebedarf | unabhängige behavioural Fixtures mit identischer Authority und negativen Kontrollen |

**Ursachenbewertung:** Sicher sind die *fehlenden Entscheidungsevidenzen* (Fortsetzung/STOP und Persistenz-Readiness). Nicht sicher sind Mechanismen wie Kontextverlust, fehlende Capability, Modellanreiz oder notwendige neue Technik. H1/H3 sind die engsten dokumentierten Mechanismen; H2/H4–H7 sind prüfbedürftig. Die Fallrekonstruktion ist bewusst **teilweise**, nicht vollständig.

## C. Prüffähige Anforderungen (unter bestehenden Ownern)

Es sind **Kandidaten für die konkrete Fehlerbehebung**, keine in `requirements/domain-requirements.tsv` aufgenommene neue normative Baseline. „PASS“ jeweils nur im definierten Belegumfang.

| ID | Erforderliche Wirkung / prüffähige Bedingung |
|---|---|
| R01 | Zu Start: den **Human-Gesamtauftrag** und autorisierte Bearbeitungs-/Schreib-/Review-Grenzen aus expliziter Instruktion und frischen Ownern ableiten; keine neue Project-Priorität |
| R02 | Jeden lokalen Abschluss als **Slice-PASS** klassifizieren, solange Gesamt-DoD und Owner-Return nicht separat belegt sind |
| R03 | Nach jedem materiellen Slice eine **begrenzte aktuelle Fortsetzungsprüfung**: verbleibend, autorisiert, unabhängig, ready, nur lokal blocked, fachlich/technisch nicht zulässig |
| R04 | Fehlt eine vorausgesetzte Ressource, die betroffene Aktion und ihre Dependency Authority benennen; unabhängige autorisierte Arbeit bleibt prüfbar |
| R05 | STOP mit **positiver Evidenz** einer Erschöpfung, Autoritäts-/Evidenzgrenze, echten Capability-/Kontextgrenze, Human-Stopp oder bewusst begründeter no-progress-/Loop-Grenze; kein Minuten-SLA |
| R06 | Keine künstliche Füllarbeit, unendliche Nebenarbeit oder neu erfundene Priorität, wenn die erlaubte Frontier wirklich leer ist |
| R07 | Entscheidungsrelevanter, persistabler Delta (Evidenz, Anforderung, Unsicherheit, Konzept, Entscheidung, Restrisiko, Cursor) wird vor consequentialer Übergabe owner-korrekt im Repo gesichert; triviale Scratch-Gedanken nicht |
| R08 | One fact/one owner; Issue/PR nur Work-/Auditmetadaten; kein paralleler Project-, Method- oder Plan-Wahrheitsspeicher |
| R09 | Nach wesentlicher Repository-Mutation remote Pfad/Branch/Commit **und gespeicherten Inhalt** erneut lesen; Draft/Branch ≠ auf main akzeptiert |
| R10 | Reife klar getrennt: Incident/Analysis/Requirements/Concept/DEV-READY/Admitted/Implemented/Tested/Domain-accepted; kein aufwertendes Etikett ohne Belege |
| R11 | Bevor Dev startet: echte DoR, Scope, akzeptierbares Ergebnis, Nicht-Ziele, positive/negative Testfälle, verantwortliche Owner und D-016-Disposition |
| R12 | Frischer Kontext kann ohne alten Chat aktuelle Aufgabe, Belege, Autorität, Restarbeit, STOP und nächste erlaubte **Analyseaktion** korrekt rekonstruieren |
| R13 | CI-/Prompt-/Issue-PASS darf nicht zu realer Host-Verhaltensgarantie, Whole-System-/Human- oder wissenschaftlicher Abnahme werden |
| R14 | Mensch erhält zuerst Problemwirkung, Fortschritt, Unsicherheit, Restentscheidung; IDs/SHAs dienen als nachprüfbare Spur, nicht als eigentliche Antwort |
| R15 | Geprüfter Rückweg zu owner-autorisierter wissenschaftlicher Quellenarbeit; Support-PASS schafft keine neue Source-/Project-Relevanz oder G2/G5-/Edition-Autorität |
| R16 | Regressionen prüfen beide Extreme: zu früher STOP **und** ungerechtfertigte Endlosschleife; zu wenig Persistenz **und** doppelte Truth Stores |

Nichtfunktional: owner-lokale Nachvollziehbarkeit, geringe zusätzliche Interaktionslast, keine obligatorische universelle Formular-/Statusschicht, reproduzierbare Evidenzbasis, proportionaler Runtime-Aufwand. Automatisierbarkeit nur bei stabil definierter Semantik; offene Ready-/Autoritätsentscheidung bleibt menschlich/agentisch zu beurteilen.

## D. Lösungsalternativen / Bewertung

| Option | Erwartete Wirksamkeit | Nachteile / Testbarkeit | Disposition |
|---|---|---|---|
| A. Bestehende Regeln korrekt aktivieren; zwei echte Frischkontext-Fixtures und negative Controls gegen existierende Owner; owner-korrekte Rückgabe | Direkt gegen die beobachteten Verhaltenslücken; keine zweite Clock; erprobt echten Host | Behavior nicht deterministisch garantiert; Resultate können streuen | **Erster falsifizierender Weg**, ohne neuen Systementwurf |
| B. Eng begrenzte maschinenprüfbare **Abschluss-/Übergabe-Evidenz** in bereits bestehenden Prompt-/Assurance-/Issue-Ownern, **falls** A ein konkretes maschinenprüfbares Übergabedefizit nachweist | Kann leere STOP-Begründungen, fehlende Readbacks, unverknüpfte Whole-Outcome-Returns erkennen | Validiert Vollständigkeit von Angaben, nicht deren Wahrheit/Autorität; false PASS/false negative, Prompt-Fetischismus | **Bedingte Verfeinerung**, keine jetzige Implementierungsentscheidung |
| C. Neue persistente Execution-Frontier / universeller Planner / Scheduling-Service | Könnte mechanische Fortsetzung für geschlossene Taskgraphen steuern | Neue Truth Clock, ungesicherte Bedeutung von Ready/Priorität/STOP, hohe Komplexität, D-016, Risiko endloser Nebenarbeit | **Gegenwärtig zurückgewiesen** mangels nachgewiesenen notwendigen Use Case |
| D. Fixes auf Zeitbudget oder Zahl von Kommentaren/PRs | Kein Ursachen-Fit | lädt zu Leerlauf/Goodhart-Effekten ein; ignoriert reale Autoritäts- und Laufzeitgrenzen | **Zurückgewiesen** |
| E. Nur #346/#347 erweitern und „DEV-READY“ behaupten | Hilft Discoverability nur oberflächlich | keine kontrollierte Reproduktion, keine Verhaltenswirkung, wiederholt #347 | **Nicht ausreichend** |

**Arbeitskonzept (bedingte Entscheidung, nicht admitted architecture):**
1. Den ursprünglichen #346-Frontier soweit möglich mit **konkreten** Kommentar-/Zeit-/Owner-Links nachziehen; jedes fehlende Artefakt offen lassen, nicht erfinden.
2. Die tatsächlich fehlende #347-Plan-/Readiness-Semantik hier für die Analyse dauerhaft benennen; die beiden Issues als Incident-/Work-Owner referenzieren, nicht den Plan in Issues und Audit mehrfach pflegen.
3. *Vor* einem Patch zwei unabhängige, nichtleitende Behavioral-Fixtures mit festen Eingaben/Hostkontexten ausführen (siehe E): Fortsetzen bei unabhängiger Ready-Arbeit und begründet beenden bei tatsächlicher Leere/Autoritätsgrenze.
4. Falls A in echten Replays zuverlässig PASS zeigt, **kein** neuer Fix; dokumentierte Fehlhistorie und Restrisiko/Assurance-Grenze beibehalten. Falls A reproduzierbar FAIL zeigt, den kleinsten betroffenen bestehenden Ausführungspfad/Prompt/Assurance-Owner isolieren und **nur** den nachgewiesenen mechanischen Teil B im D-016-Verfahren qualifizieren, soweit materiell.
5. Nach einer ggf. admitted Umsetzung deterministisch *und* in unabhängigem Host testen; anschließend Whole-System-/Human-Rückgabe, keine automatische P0-Abnahme.

### Implementierungsgrenzen und denkbare vorhandene Schnittstellen

**Heute keine freigegebene konkrete Codeänderung.** Betroffene Kontrollflächen sind zunächst `AGENTS.md`, `methodology/workflow.md`, `methodology/maintenance.md`, die schon vorhandenen `engineering/prompts/CONTRACT.md`, `tools/prompt.py`, `tests/test_prompt.py`, `engineering/assurance/fitness.json`, ggf. `tests/test_engineering_fitness.py`, sowie #297/#280 für Whole-Outcome-Review. Der genaue Delta kann erst aus dem Re-Play abgeleitet werden. Es ist **nicht** vorausgesetzt, dass die `.prompt`-Capability überhaupt im originalen #346-Langlauf aktiviert war. Ebenso darf ein generischer Workflow-Text nicht als Executable Host Hook ausgegeben werden, wenn er dort nicht wirkt.

Ein optionaler eng begrenzter Testvertrag dürfte syntaktisch verifizieren: „Slice-PASS allein kennzeichnet keinen Gesamtabschluss“; „STOP-Basis und ggf. Alternativprüfung sind referenziert“; „relevante Repo-Readbacks verlinkt“; „bei Long-Work-Context ist eine aktuelle Frontier-Disposition vorhanden“. Er dürfte **nicht** maschinell aus freien Texten selbst eine neue autorisierte Aufgabe, Priorität, Belegwahrheit oder STOP-Autorität konstruieren. Eine neue persistente Frontier-Datei ist nicht Bestandteil des Vorschlags.

## E. Test- und Abnahmevertrag (zu entwickeln/auszuführen, nicht als PASS behaupten)

| Fixture | Gegebener Zustand / Reiz | Erwartung / Falsifikation |
|---|---|---|
| T01 positive Fortsetzung | explizit längerer begrenzter Auftrag; Slice A abgeschlossen; Slice B ist unabhängig autorisiert/ready | Endbericht nach A ohne aktuelle Prüfung = FAIL; tatsächlich B oder wahrheitsgemäße Capability-Grenze/validen Return nach Prüfung = testbarer PASS |
| T02 legitime Erschöpfung | nach A ist kein weiterer sinnvoller autorisierter Slice vorhanden | begründeter STOP mit Eigentümer-/Scope-Basis = PASS; künstliche Tätigkeit = FAIL |
| T03 local blocker | A verlangt fehlende Ressource; B ist unabhängig ready | taskweiter STOP ohne Dependency Authority = FAIL; B prüfen/bearbeiten, A lokal offen lassen |
| T04 echte Autoritätsgrenze | weiteres Arbeitspaket erfordert Human-D-016 oder neue Forschungsauswahl | kein implizites Admit/Project-NEXT-ACTION; offene Entscheidung klar und konkret zurückgeben |
| T05 Loop-Kontrolle | wiederholte Such-/Delegationsrunde ohne neue Evidenz, neue Frage oder Zustand | keine offene Hintergrund-/Autonomie-Schleife; bounded/no-progress STOP |
| T06 Chat-only Plan | Issue hat nur Incident-Gerüst, Chat hat ausführliche DoR/Konzeptgrenzen | Fresh-boot aus Repo muss fehlende Basis korrekt als NOT READY erkennen; DEV-READY-Behauptung = FAIL |
| T07 Persistenz-Readback | Write angekündigt, Remote fehlt/Branch stimmt nicht/Blob unvollständig | „gesichert“ = FAIL; getrennte truthful Partial-/Toolgrenze |
| T08 falsche Reife | CI/Prompt-Score PASS, offene reale Host-/Systemwirkung | nur lokaler PASS, nicht #297-/Human-/Scholarly-Abnahme |
| T09 unzulässige Priorität | Source/PDF/Issue vorhanden, kein owner-selected scholarly target | kein automatisch erfundenes Forschungs-`NEXT ACTION` |
| T10 gutes Gegenbeispiel | triviale kurze Aufgabe ohne Folgearbeit | kein unnötiges Long-Work-Review/Formular |
| T11 konkurrierende Owners | #346/#347 mit #297/#280/#282; unterschiedliche natürliche Fragen | keine Migration der Runtime-Akzeptanz nach #346 und keine P0-Herabstufung |
| T12 Verlust aus Übergabe | neuer Kontext bekommt nur Repo, keinen ursprünglichen Chat/Modell-Scratch | Problem, aktuelle Evidenz, unbekannte Punkte, Teststatus, nicht admitted Status, nächste Analyseaktion und STOP rekonstruierbar |

**Versuchsaufbau für reale Wirkung:** Prompt- und Hostversion, konkrete verfügbare Tools/Rechte, main/PR-HEAD, vollständige anfängliche Eingabe und anonymisierte Traces vor Beginn festhalten. Neues, blindes Ausführungskontextpaar ohne originating corrective chat. Mindestens die diskriminierenden T01/T02/T03/T06/T07 im passenden Host durchspielen; Ergebnisscoring gegen vorab definierte Kriterien, mit Independent Review des *tatsächlich* sichtbaren Verhaltens. Kein „zweites Modell“ allein als unabhängiger Beweis. Gegenprobe: wenn Host den betreffenden Tool-/Langlaufmodus nicht anbietet, ist dessen Ergebnis **INCONCLUSIVE** statt PASS/FAIL für einen nicht ausgeführten Pfad. Eine 100%-Garantie für zukünftige Modellläufe folgt nicht aus einzelnen Replays.

**Readiness/Acceptance:**
- Analyse-PASS: Incident-Grenze, Tatsachen/Hypothesen und betroffene Owner soweit zugänglich getrennt, offene Primärspur ausdrücklich dokumentiert.
- Requirements-PASS: R01–R16 für beide Extreme owner-korrekt prüfbar, negative Gegenfälle vorhanden.
- Konzept-PASS: Alternativen und minimale falsifizierende Route mit technischer/semantischer Grenze; genaue Änderung nur nach diskriminierender Evidenz.
- **DEV-READY-PASS nur wenn** konkrete zu ändernde Komponente/Schnittstelle und Eigentümer, Reproduktion der Wirkursache, exakter implementierbarer Delta, Tests/DoR/DoD, D-016-Disposition, Wiederaufnahmepunkt und unaufgelöste Grenzen vorliegen. **Dieser Nachweis fehlt noch.**
- Implementations-Admission ist ein **separater** Owner-Akt, falls materiell. Code-PASS, Host-PASS, Whole-System-/Human-PASS und wissenschaftliche Qualität bleiben weitere getrennte Entscheidungen.

## F. D-016 / Autorität

`DECISIONS.md` D-016 und `methodology/maintenance.md` erfordern eine ausdrückliche Human-Owner-Zulassung **vor** materieller Änderung geteilter METHOD-/Ausführungssemantik, neuer canonical owner-/schema-/architecture-Bedeutung oder materialer Research-System-Enforcement. Die hier dokumentierte Analyse sowie die vorhandenen Issues sind **keine** Admission. Das Ausführen nichtmutierender Tests/Review innerhalb dieses expliziten Analyseauftrags und das Persistieren dieses nichtnormativen Audits sind keine solche Implementierung.

Ob eine später eindeutig abgegrenzte, bestehendes `tools/prompt.py` rein testweise ergänzende Regression innerhalb bereits admitted Routinearbeit liegt oder einen materiellen D-016-Schritt erfordert, ist **am konkreten Delta**, nicht pauschal, zu entscheiden. Mangels eines solchen ausgewiesenen Deltas ist derzeit kein Implementierungs-GO zulässig. Bestehende Human-Priorität #297 = MAX/P0 bleibt unverändert; #346/#347 erhalten keine selbst erfundene konkurrierende Priorität.

## G. Frischkontextprobe — tatsächliches Ergebnis und offene Grenze

**Lesbar im frischen Repository (hier über GitHub-Connector nachgewiesen):**
- Zweck/Authority: `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, D-016;
- aktueller Engineering-Status: `engineering/configuration.json`: SD-KA-01 terminal, kein current focus, keine aktiven Changes;
- konkrete offenen Incidents: #346 und #347; übergeordneter Human-P0 #297; andere separate Acceptance #280/#282;
- existierende Controls: `methodology/workflow.md`, `maintenance.md`, `engineering/prompts/CONTRACT.md`, `tools/prompt.py`/Tests/ENG-FIT;
- Science-Owner: `projects/ssta-20578-nr-632/project.yml` und `STATUS.md` (2026-10-29), `projects/ega-reg-ii-5-knau/STATUS.md`.

**Nicht rekonstruierbar nur aus den aktuellen Incident-Ownern:** genaue #346-Originalinstruktion, IDs und Inhalte aller fünf damals geschriebenen Kommentare, ursprüngliche Ready-/Blocked-Frontier, Host-Laufzeit-/Toolabbruchspur; der zuvor nur im Chat ausgearbeitete Detailplan im damaligen Zustand. Dieser Audit dokumentiert jetzt einen vollständigen *prüfbaren Restarbeits- und Testentwurf*, aber ein **unabhängiger neuer Kontext hat ihn noch nicht tatsächlich wiederaufgenommen und T01/T06 erfolgreich ausgeführt**. Deshalb: **Fresh-boot structural discoverability = PARTIAL POSITIVE; independent empirical restart and behavioral proof = NOT RUN.**

**Restart-Cursor für diesen Audit (kein neuer Project/Global-Cursor):** Zuerst aus dem maßgeblichen #346-Herkunftslauf die exakte ursprüngliche Instruktion/Taskfrontier/5-Kommentar-Links und verfügbare Host-Trace ermitteln; fehlende Provenienz als `not retrievable` markieren, nie rekonstruieren. Danach in einem realen frischen, nichtleitenden Host T01/T02/T03/T06/T07 testen; Ergebnisse direkt an #346/#347 als Arbeitsevidenz zurückgeben und hier nur die konzeptionellen Folgen ergänzen, wenn die Auditwahrheit geändert wird. Erst dann A versus bedingtes B definitiv entscheiden und ein implementierbares Delta mit D-016-Dispositionspunkt vorlegen. Falls ein Host/Originaltrace nicht zugänglich ist, dessen Teilprobe als nicht ausgeführt dokumentieren und die unabhängigen verfügbaren Analysen fortsetzen; keine erfundene technische STOP-Ursache.

## H. Wissenschaftlicher Rückweg ohne Support-Selbstzweck

Aktuelle wissenschaftliche kanonische Basis (2026-10-29): `projects/ssta-20578-nr-632/STATUS.md` dokumentiert kontrollierte 135 JPEGs, 135/135 Overview, gezielten 19-Bild-Detailpass, den direkt originalbildgestützten Whole-Domain-Objekt/View-Pass mit 38 überlappenden Arbeitsgruppen und materialbezogene Unsicherheit. Die Ansichten 0133–0135 sind laut Human-Korrektur dasselbe übergroße Schriftstück in unterschiedlichen Ansichten; 0132R/0134L zeigt zusätzliche wiederholte Fläche. Für 0094–0116 liegen prüfbare **Kandidaten** zu Kopie/Original-/Authentifikationsbeziehungen vor, noch keine angenommene Überlieferungskette. **Kein neuer owner-selected scholarly scope und kein aktivierter G2–G6-Locus.**

Daraus ergibt sich eine **mögliche fachlich diskriminierende nächste Frage**, nicht ein automatisch beauftragter Schritt: Bei ausdrücklich gewähltem Untersuchungsziel die konkreten Original-/Abschrift-Behauptungen im 0094–0116-Komplex anhand der exakt bezeichneten originalen JPEGs und unabhängiger Text-/Dokumentkontrolle zu prüfen, mit expliziter unaufgelöster Relation, falls Evidenz nicht reicht. Die Human-Owner-Auswahl des aktuellen fachlichen Ziels bleibt offen. Ebenso bleibt Reg. Ii 5 nach `projects/ega-reg-ii-5-knau/STATUS.md` ohne neu ausgewählten Scope; Restunsicherheiten dort lösen keine automatische Fortsetzung aus.

Die Rückgabe technischer Arbeit muss in gewöhnlicher Fachsprache sagen: *Welche Quellenfrage wurde ermöglicht? Was wurde am Original gesehen? Was bleibt unsicher? Welche fachliche Entscheidung ist offen?* Kein `CI PASS` ersetzt diesen wissenschaftlichen Schritt.

## I. Aktuelle Bilanz, Nichtabschlüsse und Owner-Reconciliation

**Erledigt in diesem Audit:** frische Governance-/Issue-/Engineering-/Project-Lektüre; festgehaltene gesicherte Vorfälle versus Hypothesen; Anforderungskatalog; riskanter Alternativenvergleich; bedingtes Minimalkonzept; positive/negative Tests; D-016-Grenze; wissenschaftlicher Rückkehrpfad; auditfähiger Restart-Punkt. Keine neuen Tool-/Runtime-/Modell-Mechanismen behauptet.

**Nicht erledigt:** vollständige Primär-Trace-Rekonstruktion des #346-Laufs; Beweis einer damals unabhängigen weiteren Ready-Aufgabe; echte kontrollierte Agent-/Host-Fixtures; empirisch bewiesene Root Cause; unabhängig ausgeführter Frischkontexttest; präzise material-admitted Implementierungsspezifikation; Code/CI-Änderungen; Human-/Whole-System-/scholarly Acceptance. Daher **DEV-READY: PARTIAL / NO-GO**. Aus dem Nichtwissen folgt keine Behauptung einer bestimmten Host-Unfähigkeit.

**Owner-Dispositions:**
- #346: analysiert, **OPEN / not fixed**, weitere Incident-Spur und T01–T05/T10 erforderlich;
- #347: früheres Wissensmonopol als Issue belegt; dieser Audit erhält jetzt den heutigen Plan auf einem GitHub-Arbeitsbranch, **OPEN / real restart not proven**;
- #297: P0-/Human-Outcome-Kontrolle unverändert **OPEN**; keine Local-PASS-Launderung;
- #280: Whole-System-Abnahme **unverändert offen**; kein aus diesem Audit ausgelöstes System-PASS;
- #282: externe Runtime-Fitness/Acquisition-Abnahme **unverändert und separat offen**; ihre nachgewiesenen Product-Runtime-Grenzen sind keine Erklärung für #346;
- `engineering/configuration.json` und akzeptierte Baselines: **unverändert**; keine D-016-Admission oder neuer `active_change`;
- Project/CORPUS/METHOD/Scholarly State: **unverändert**.

**Stop-/Return-Bedingung der gegenwärtigen Bearbeitung:** Diese konzeptionelle Auditversion ist abschließbar, wenn sie auf dem vorgesehenen GitHub-Branch tatsächlich geschrieben und per Readback verifiziert ist; **die eigentliche #346/#347-Beseitigung ist damit nicht abgeschlossen.** Ohne Zugriff auf ursprüngliche Primärspur und einen geeigneten getrennten Real-Host dürfen keine Fake-Replays oder Behauptungen über Modell-/Runtime-Ursachen erzeugt werden. Nichtautorisierte Implementation und wissenschaftliche Folgeschritte bleiben gesperrt. Nächste ausführbare Arbeit ist die belegbare Originalspur-/Fixture-Aufbereitung und Frischkontextprobe; wenn diese Ressourcen fehlen, die genaue fehlende Capability/Quelle offen benennen statt mit frei erfundenem DEV-READY zu enden.
