# Work-Chat-Übergabe — parallele Entwicklungsarbeit und beweisbare Reife (2026-10-29)

**Status: ENTWURF / nicht normative Arbeitsanweisung / kein DEV-READY-PASS / keine Implementierungsfreigabe.**
**Repository:** esany/paleo-type. **Ausgangsbasis:** main@6adf6c6a944d4e8801f7ec65c376a67cc2583ebd (2026-10-29, nur Snapshot; vor jeder Aktion frisch prüfen).
**Zweck:** Einen eigenständig ausführbaren, begrenzten Entwicklungs-/Prüfauftrag für einen ChatGPT-Work-Kontext bereitstellen, ohne Chat-Wissensmonopole, falsche Fertigmeldungen oder neue Prioritäten zu erzeugen.
**Wahrheits- und Autoritätshierarchie:** `GOVERNING_OBJECTIVE.md` → `AGENTS.md` → tatsächlich einschlägige METHOD-/Requirement-/Contract-/Project-Owner; `methodology/workflow.md` für Ausführung, `methodology/maintenance.md` für Übergabe und D-016. Issues/PRs tragen Arbeits-/Reviewmetadaten, keine kanonische historische Forschungstatsache.

Dieses Dokument ist ein **Auftragspaket zur Bearbeitung vorhandener Owner**, keine neue Programmsteuerung und kein zweites Zustandsregister. Für #346/#347 liegt nun der **verifizierte Analyse-Return** auf Draft-PR #348 vor: Analyse und persistierte Testspezifikation sind abgeschlossen, die Bugs aber **OPEN / nicht behoben**, und **DEV-READY für materielle Implementierung ist PARTIAL / NO-GO**. Neue Fortschritte sind ausschließlich aus dem aktuellen Repository zu belegen, nicht aus dem früheren Chat oder dieser Zusammenfassung. Vor jeder Handlung darf daraus weder PASS noch neue Autorität gefolgert werden. Eine Statusfrage autorisiert keine Mutation. Der Work-Chat darf den eigenen Auftrag eigenständig durchführen; dieser Chat kann ihn **nicht fernsteuern, automatisch wecken oder im Hintergrund kontrollieren**.

## Aktualisierte Abhängigkeit: unabhängiger Fehleraudit #348 (2026-10-29)

**Autoritativer Verweis für die tatsächlich untersuchten Bugs:** [Draft-PR #348](https://github.com/esany/paleo-type/pull/348), Datei `engineering/evidence/audits/issues-346-347-autonomous-continuation-restartability-2026-10-29.md` auf Branch `audit/issues-346-347-dev-ready-20261029`, damaliger HEAD `53508ca14ee8fedf192dc26d41ff2f437a136bdb`. Primäre Work-/Incident-Owner bleiben #346/#347; #297 Human MAX/P0 und #280/#282 haben separate unveränderte Grenzen. Diese Übergabe zitiert nur die **Grenze**, nicht den kompletten Anforderungskatalog als parallele Wahrheit.

**Verifiziertes Audit-Ergebnis:** Analyse-/Requirements-/Concept-Evidenz und Arbeitsevidenz sind auf PR #348 dauerhaft verfügbar. **DEV-READY = PARTIAL / NO-GO; kein Code-Fix, kein belegter Root-Cause-Nachweis, keine unabhängige Host-/Frischkontext-Regressionsabnahme.** Als offen genannt sind ursprüngliche #346-Instruktion/Tool-/Zeit-/Ready-Frontier und die realen diskriminierenden Tests, insbesondere **T01 positive Fortsetzung, T02 legitime Erschöpfung, T03 lokaler Blocker bei unabhängig Ready-Arbeit, T06 Chat-only-Plan und T07 Repository-Readback**. Vollständige Kriterien und T04–T12 liegen **nur** im zugehörigen Audit; dort bei Bedarf frisch prüfen.

**Planwirkung für diesen Work-Chat:**

- **B/C dürfen weiter analysiert, getestet und innerhalb tatsächlich bestehender Autorität implementiert werden.** Eine gesperrte materielle A-Implementation ist **kein** globales Verbot unabhängiger B/C-Arbeit. Die B-/C-spezifischen D-016-Grenzen gelten unverändert.
- **B/C sind zugleich zwei realistische Beobachtungsfälle**, ob der Work-Chat nach lokalem PASS weitere autorisierte Aufgaben prüft und persistente Nachweise vorzeigt. Der aktive Work-Kontext darf diese Beobachtung **nicht** als unabhängige #346/#347-Abnahme oder verlässliche allgemeine Fehlerheilung ausgeben. Ein echter blinder, getrennter Hosttest gegen die vorab definierten #348-Fixtures bleibt erforderlich.
- Bei der Abgabe verpflichtend unterscheiden: (i) echtes B/C-Fach-/Code-/Review-Ergebnis, (ii) beobachtete Fortsetzungs-/STOP-/Readback-Spur des eigenen Laufs, (iii) **nicht gelaufene** unabhängige #348-Fixtures. Kein „Bug durch diesen langen Lauf bewiesen gefixt“.
- **Vor bedingter A-Implementation** muss der tatsächlich betroffene Owner/Mechanismus per verhaltensdiskriminierender Evidenz eingegrenzt werden. Ein weiterer Hinweis auf die bereits existierenden Regeln oder ein bloßer Testplan ist kein DEV-READY-PASS.
- Kein zweites Audit mit kopierten R01–R16/T01–T12, keine neue A-Architektur, kein Chat-zu-Chat-Steuermechanismus. Bei materiell verändertem PR #348 diesen Verweis aktualisieren, nicht die Auditwahrheit hier pflegen.

## 1. Verbindlicher Einstieg für einen neuen Work-Kontext

1. Frisch über den **autorisierten GitHub-Connector** lesen: `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `README.md`, `methodology/workflow.md`, `methodology/maintenance.md`, `engineering/configuration.json` und die für den konkreten Arbeitsstrang verantwortlichen Owner samt neuesten Kommentaren, PR-HEADs, Artefakten, Anforderungen und Tests. Für wissenschaftliche Bewertung zusätzlich `methodology/historical-source-workflow.md`, `methodology/research-gates.md`, `methodology/evidence-policy.md`, `methodology/source-and-provenance.md`, `methodology/project-lifecycle.md` und den aktuellen Project-STATUS lesen.
2. **Nicht** aus diesem datierten Dokument auf gegenwärtiges main/CI/PR-Akzeptanz schließen. Stale Angaben ersetzen durch tatsächliche GitHub-Belege, den Unterschied dokumentieren. Keine lokalen Spiegel/Downloads als kanonische Repo-Wahrheit. Externe kontrollierte Originalbytes bleiben außerhalb GitHub, Rechte und Quellenevidenz bleiben unterscheidbar.
3. Arbeitsgegenstand und Autorität trennen: Informationsbeschaffung/Analyse/Tests; Routineimplementierung bereits zugelassenen Umfangs; materieller D-016-Vorschlag; wissenschaftliche Entscheidung des Human Owners. Nur die tatsächlich autorisierte Klasse ausführen.
4. Vor parallelen Branch-Änderungen bestehende offene PRs und Dateiberührungen vergleichen. Keine konkurrierenden unkoordinierbaren Änderungen an derselben Datei. Pro unabhängiger Implementation ein zugehöriger PR oder ein eindeutig begrenzter Update an bestehendem PR; niemals bestehende Draft-PRs vorschnell mergen.
5. Bei längeren und extern wirksamen Arbeiten aktive Auftragsidentität, kontrolliertes Ziel, Fortschritt, Containment, Wiederaufnahme, Rechte und tatsächliche Stop-Möglichkeit prüfen. Ein tatsächliches NO-GO nur für die betroffene Aktion aussprechen; unabhängige autorisierte Arbeit nicht pauschal blockieren.
6. Jeden wesentlichen Befund **direkt** an seinem zuständigen kanonischen GitHub-Ort oder auf einem intended GitHub-Arbeitsbranch persistieren; anschließend **remote readback** von Pfad, Branch, Commit und Inhalt. Ein Chattext, ein Issue-Kommentar oder CI allein ersetzen eine erforderliche kanonische Repository-Datei nicht.
7. Vor Abschluss Fresh-Context-Restartcheck durchführen: höheres Ziel, tatsächliche Ergebnisse, geänderte/unveränderte Owner, offene Hypothesen, Nachweise, Berechtigung, nächster Schritt, STOP und realer Acceptance-Ceiling ohne vorherigen Chat rekonstruierbar. Abschlussmeldung immer ehrlich: Analyse/DEV-READY/admitted implementation/CI/Host-E2E/independent review/Scholarly-Human acceptance separat.

## 2. Inventar und Prioritäts-/Authority-Grenze

Beim ersten Snapshot waren **35 offene Issues** und **fünf ältere Draft-PRs** sichtbar: #335 (`source-intake`), #332 (`savesax`), #327 (spiral-breaker), #321 (systemic closure/backlog), #290 (source-entry capability review). **Nachträglich** sind #348 (Analyse #346/#347) und #349 (dieses Übergabepaket) hinzugekommen: bei frischem GitHub-Read am 2026-10-29 **sieben offene Draft-PRs**. Vor Arbeitsbeginn tatsächliche Anzahl/HEADs erneut lesen. Das bedeutet nicht 35 sofort ausführbare Projekte. Der Human-MAX/P0-Status von **#297** bleibt bestehen; dieses Dokument ändert keine Priorität.

| Arbeitsfamilie | Offene Issues | Disposition in diesem Work-Auftrag |
| --- | --- | --- |
| Schon fremd bearbeitete Ausführungsbugs | #346, #347 | **Nicht doppelt bearbeiten oder überschreiben.** Nur frisch lesen, als externe offene Abhängigkeit behandeln; ihre Ergebnisse später unabhängig konsumieren. |
| Source preservation, Corpus-Intake, produktive Runtime | #334, #271, #282 | **Primärer Work-Strang B:** konkrete Analyse, vorhandene Implementierung/Testlücken und autorisierte Reparaturen; produktiver Datenlauf nur nach echten DoR/Control-Gates. |
| Wissenschaftliche Source-Entry/Methodenfähigkeit | #291, #341, #292, #308, #265, #266, #267, #268, #269, #270 | **Primärer Work-Strang C:** empirisch prüfen, methodisch differenzieren, Requirements/DEV-READY konkretisieren; materielle METHOD/CORPUS-Änderungen ohne D-016 nicht implementieren. |
| Übergreifende Ergebnis-/Qualitätsevaluation | #297, #280, #272, #296, #306, #307 | **Querprüfung Q:** evidenzgebundene Readiness-, Gegenproben- und Result-Review-Rückgaben, **nicht** automatische Schließung oder implizite Implementierung. |
| Corpus-Auswahl/Findmittelabdeckung | #12, #263 | **Separater Nachweis-/Auswahlstrang:** nur soweit tatsächlich von B/C berührt; keine pauschale Auswahl- oder Vollständigkeitsbehauptung. |
| Eigenständige optionale Erweiterung | #337 | **Nicht Teil von #334.** Kein Zotero-Zwang/Autostart; nur separater expliziter Auftrag. |
| Bewusst verschobene bzw. nur zukünftige Themen | #162, #90, #202, #62, #22, #13, #6, #4, #3, #2, #1 | **Nicht starten.** #162 Chat-Chat-Koordination PAUSED; kein Bot/Router/Slack-Autowake. Andere Future/Deferred erst bei vorhandenem Owner-Trigger und Human-Disposition. |

**Konfliktgrenze:** Ein gesonderter Kontext hat #346/#347 im nachgewiesenen **Analyse-/Planungsumfang** über PR #348 bearbeitet; eine Behebung oder materielle DEV-READY-Freigabe ist ausdrücklich **nicht** belegt. Diese Übergabe übernimmt weder dessen offene Behavioral-Tests noch die Verantwortung für die Bug-Abnahme und sendet dem anderen Kontext keine Anweisung. Issue-/PR-Zustand ist bei Bedarf frisch zu prüfen. Keine Chat→Chat- oder Slack-Steuerung ohne eigenständig verifizierte zulässige Koordinationspolitik. `#162` belegt gegenwärtig nur eine PAUSED/DEFERRED-Koordinationsfrage, keine akzeptierte automatische Chat-Orchestrierung.

**Engineering-Konfiguration zum Snapshot:** `engineering/configuration.json` hat `active_changes: []` und `current_focus: null`; SD-KA-01 ist angenommen/abgeschlossen. Keine automatische neue D-016-Freigabe oder neue globale Roadmap ableiten.

## 3. Arbeitsstrang B — #334 / Draft PR #335: Archivpaket → kanonische Source/File-Registrierung

**Primärer Work-Owner:** https://github.com/esany/paleo-type/issues/334 ; Entwurfsbranch/PR: https://github.com/esany/paleo-type/pull/335 .
**Schnittstellen/andere Owner:** #271 / PR #332 (Dresden-Provider, `savesax`), #282 (kontrollierter externer Zielort, produktive Runtime), #280 (unabhängige Whole-System-Prüfung), #297 (MAX/P0 falscher lokaler PASS), #268 (gesonderte zusammengesetzte Source/File-Semantik), #337 (optionale Zotero-Erweiterung).
**Vorhandenes Konzept/Prüfmatrix am Draft-HEAD neu lesen:** `engineering/evidence/audits/archival-preservation-corpus-intake-concept-2026-10-28.md` und `engineering/evidence/audits/archival-preservation-corpus-intake-dev-ready-2026-10-28.md` auf PR #335 (T0–T9 für den Pflicht-Kernflow; historische T10/Zotero-Bezüge nicht als Kernbedingung behandeln).
**Stand:** Branch enthält `tools/archival_package_intake.py`, `tests/test_archival_package_intake.py` und `.agents/skills/source-intake/`. Der zuletzt dokumentierte exakte PR-HEAD `8f3dda159cd085b63a8a868a175de04dec64f3b3` hatte erfolgreiche CI mit 187 Tests. Für das existierende Nr.-632-Paket wurde ein tatsächlicher 135-JPEG/SHA-Read-only-Preflight berichtet; das ist **kein** produktiver GitHub-Writer, keine Skill-Host-Aktivierung und keine Ende-zu-Ende-Abnahme. PR bleibt Draft.

### B0 — Exakte Befund-/Anforderungs-Reconciliation (sofort)
- Aktuelle Owner/PR/Commitstände lesen; veraltete CI-/HEAD-Angaben aus dem Issue als historisch markieren.
- Existierende Source/File/Route-Semantik gegen `corpus/source-contract.json`, `tools/source_contract.py`, `tools/source_intake.py`, `corpus/sources.tsv`, `corpus/files.tsv`, `source-entry/routes.tsv` und bestehende SStA/Reg.-Ii-Fixtures prüfen.
- Die tatsächliche B0–Bn-Matrix an den bestehenden T0–T9 ausrichten: [nachgewiesen], [unverifiziert], [fehlgeschlagen], [noch nicht autorisiert], [nicht anwendbar]; kein pauschales „DEV-READY“ aus vorhandener Dokumentüberschrift.
- `#334` und Draft PR nicht unautorisiert schließen/mergen; kein erneuter 135-Bilder-Download als Test.

### B1 — Reproduzierbare Preflight-/Negativkontrollen (autorisierte Tests)
- Exaktes Paket, Sidecar- und Originalbyte/Checksum-Reconciliation testen, wenn Bytes in **diesem Kontext** tatsächlich kontrolliert zugänglich sind. Vorbericht aus einem anderen Kontext ist nicht eigene Byteinspektion.
- Fälle: vollständiges bereits registriertes Paket (idempotent), neue ungeprüfte Einheit, fehlendes Bild, beschädigte Bytes, doppelte SHA, inkonsistente Signatur/GUID, uneindeutige historische Ordner-/Package-Namen, führende Nullen, fehlende Rechteangabe.
- Schutz: `UNVERIFIED_DO_NOT_RESUME` darf nicht zu verdecktem Resume/Overwrite werden; `--status`/Statusfrage bleibt read-only; Source-/Project-Scope nie aus Archivtitel oder Verfügbarkeit erschließen.
- Tests am **exakten** Arbeitsbranch/Commit dokumentieren; GitHub Actions nur für nachgewiesene deterministische Eigenschaften verwenden.

### B2 — Materialitäts- und Implementierungsentscheidung (harte Grenze)
- Prüfen, ob fehlende GitHub-Schreibsemantik, ein Skill-Router oder neue Cross-Boundary-Automation **materiale** D-016-Änderungen sind. Vorhandene DEV-READY-Spezifikation dokumentiert: die vorgeschlagene materielle GitHub-Writer/Orchestration ist **nicht** automatisch Implementation-admitted.
- Wenn material: präzise Entscheidungsvorlage für Human Owner mit betroffenen Ownern, Alternativen, Migration-/Datenverlustschutz und Tests erstellen; **nicht** implementieren, bis eine explizite Zulassung unter D-016 vorliegt.
- Wenn die konkret nachgewiesene Änderung routinemäßige Arbeit innerhalb bereits präzise zugelassenen Umfangs ist: erst dann isoliert implementieren; Umfang und Autorität dokumentieren. Kein Global-Writer oder zweiter Registry-Owner.

### B3 — Erst bei entsprechender Autorität: sicherer Canonical Writer
- Provider-neutrale Quelle→Paket→Verified-byte→kanonische Source/File Zuordnung auf Grundlage bestehender Contracts; keine eigene zweite Source-Datenbank.
- GitHub-only Write mit Berechtigungsprüfung, branch/HEAD- und Blob-SHA-Konflikterkennung, idempotentem Reconciliation-Plan, vollständiger Remote-Readback-/Validation-Nachprüfung und Recovery bei Teilfehler.
- Keine Source/File-Identität aus Dateiname allein, keine falsche Byteidentität, kein doppelter SHA-Eintrag, keine Neuinterpretation von Rights, keine Project-Erstellung oder Forschungsscope-Auswahl.
- Edgecases gegen Reg.-Ii, bestehendes Nr. 632, neue Source, bereits vorhandene Source, falscher Provenienz-/Metadatenclaim und separate #268-Composite-Grenze testen. Bei unklarer Semantik an betroffenen Owner zurückgeben.

### B4 — Host-E2E und produktive Runtime (nur bei erfüllten Kontrollbedingungen)
- Natürlicher deutschsprachiger Auftrag „Archivbestand lokal und im Repo sichern“ muss das passende Tool/Skill **ohne Nutzer-Mikrorouting** wirklich aktivieren. Exakte Host-Trace notwendig; expliziter Skillname, Anleitungstext oder CI simulieren Host-Aktivierung nicht.
- Altbestandfall: vorhandenes externes Paket und kanonische Zeilen ohne Download/Write-Duplikate korrekt erkennen.
- Neuarchivfall: erst wenn #271 Provider-Evidenz und #282 kontrolliertes, persistentes Ziel samt Stop/Resume, Verifikation und Berechtigung echte PASS-Vorbedingungen bilden. Ohne diese: **NO-GO nur für diesen produktiven Teil**; keine Scratch-/Actions-Ablage als neue dauerhafte Sicherung.
- Tatsächliche GitHub-Writes nur nach expliziter autorisierter Top-Level-Mutation, Prüfsummen, Repo-Validation, Readback. Auf Teilfehler truthful partial/restart statt „complete“.
- Kein implizites bezahltes Browserrouting, keine Bilder/PDFs ins GitHub-Repo, keine Zotero-Arbeit (#337 gesondert).

### B5 — Getrennte Result-/Review-Rückgabe
- B-Teilresultat an #334/PR #335; Provider-Fund an #271; externe Laufzeit an #282; E2E-Fakten an #280; Konsequenz für #297 nach dessen eigenem MAX/P0-Standard, ohne Priorität/Closure zu verändern.
- Nachweisform: exakter Tool-Trace/Datei-SHA, Testresultat, GitHub-Pfad+Branch+Commit+Remote-Readback, offene/unverifizierte T-Kriterien, unabhängige Review-Hürde.
- **B-DoD:** ein vollständig autorisierter natürlicher End-to-End-Nutzerflow, verifiziertes dauerhaftes Paket und kanonische Registry, plus negative und Restarttests – soweit tatsächlich ausführbar und legitim. Sonst ehrliches PARTIAL/NO-GO, nicht schließen.
- **Erster sinnvoller B-Schritt:** B0/B1/B2 durchführen und die **belegte** Implementierungslücke und Materialitätsentscheidung präzisieren; kein ungeprüfter Writer-Start.

## 4. Arbeitsstrang C — #291 / Draft PR #290: unbekannte Quelle → wissenschaftlich tragfähiger Einstieg

**Primärer Work-Owner:** https://github.com/esany/paleo-type/issues/291 ; Konzept-Draft: https://github.com/esany/paleo-type/pull/290 ; konkrete Skill-Erfindungsregression: https://github.com/esany/paleo-type/issues/341 .
**Weitere Owner:** #292/#308 (Human-lesbare fachliche Bedeutung und Kompetenz-/Evidenzrouting), #265 (keine aktive Scope-Selektion), #267 (granulare Inspektionsabdeckung), #266 (Dokumentform versus Überlieferungsstufe), #269 (Relation und Evidenzstärke), #268 (Root-File/interne Sources), #270 (Wolkenburg-Fragen), #12/#263 (Findmittel-Auswahl, **nicht** interne Quelleninspektion), #307 (Aussagenprovenienz).
**Normative Basis:** `methodology/historical-source-workflow.md` S1–S9 und `methodology/research-gates.md` G1–G6, keine neue S0-Stufe oder eigene Gate-Leiter. Relevante Diplomatik, Paläographie, historische Philologie, Überlieferungs- und Editionsmethoden aktivieren, sobald der *konkrete* Befund sie erfordert.
**Projektstatus zum Snapshot:** `projects/ssta-20578-nr-632/STATUS.md`: G1 belegt; 135/135 Überblick über alle Providerbilder, kontrollierte Detailchecks und eine 135-Bilder-Objekt-/View-Rekognoszierung vorhanden; 38 Kandidatengruppen sind **keine** 38 abschließend bestimmten Dokumente. Kein Human-ausgewähltes neues engeres scholarly `NEXT ACTION` oder G2-Ziel. `0094–0116` ist potenzieller Kollationskandidat, nicht automatisch neue Priorität. Vor jeder Source-Aktion frisch lesen.

### C0 — Methodischer Ist/Soll-Vergleich
- Aktuelle S1–S9/G1–G6, schon existierende Source-Entry-Mechanismen, Project-Status und #291/PR #290 lesen. Explizit zeigen, **welche** Teilfähigkeit wirklich fehlt, statt sie durch neuen Skillnamen oder schematische „Vorphase“ zu behaupten.
- #341 reproduzierbar als Negativtest: Die Aufforderung „Brauchen wir einen neuen Skill?“ darf keinen neuen METHOD-/Stage-/Skill-Owner ohne nachgewiesene einzigartige operative Lücke auslösen.
- Kriterien: Erkenntnisschritt zuerst, nicht Tool-/Erwerbsprozess als Antwort; gleiche Quelle kann zunächst vollständig unbekannt sein, ohne dass eine enge Forschungsfrage oder relevante Stelle vorselektiert werden muss.

### C1 — Empirische Gegenproben (Evidenzklassen strikt)
- Groß/komposit: vorhandene Nr.-632-Quellenansicht und originale Kontrollbilder anhand exakter Locator und nachgewiesener Zugänglichkeit prüfen; beim Wiederverwenden früherer Befunde immer „übernommene Beobachtung“ vs „neue direkte Inspektion“ unterscheiden.
- Kurz/einfach: **noch fehlenden** kurzen, klar begrenzten Originalquellen-Vergleich kontrolliert identifizieren. Keine generische METHOD-Änderung ohne diesen Fast-Path-Gegencheck.
- Weitere adversariale Fälle entsprechend #291: schwierige/mehrere Hände, Register/Rechnung, Abschrift/Auszug, mehrere Zeugen, fehlende Bilder, widerlegte Relevanzhypothese, gemischte Dokumente, negativ/unentschieden relevante Passage.
- Wo Primärbilder fehlen: exakt betroffenen Test als UNVERIFIED vermerken, keine Manuskriptbeobachtung erfinden und nicht automatisch den gesamten Analyseauftrag blockieren.

### C2 — Wissenschaftlich vollständiger Eingangszyklus, aber keine parallele METHOD
- Aus realen Quellen-/Problemgegenständen ableiten, wann breit sichtende Rekognoszierung, material-/diplomatische Grenzhypothesen, paläographische Familiarisierung, diagnostische Lesung, wechselnde Relevanz und erste gebundene Transkriptionsziele erforderlich sind.
- Explizite Unterscheidung: Archiv-/Projektwurzel, Inspektionsdomäne, wirkliche Inspektionstiefe, festgestellte Dokument-/View-Struktur, aktive wissenschaftliche Scope, Kandidat, Lesung/Transkription, Evidenzdeckel, Rückgabe-/Spezialistenbedarf.
- Quelle und dokumentarische Evidenz entscheiden, ob adaptive Wiederholung innerhalb S1–S9 nötig ist; der einfache Kurzfall darf **keine** 200-Seiten-Vollaufnahmebürokratie erben.
- Fachliche Qualität: keine Original/Abschrift/Extrakt-Bestimmung aus Katalogtiteln allein; keine direkte `copy_of`-Relation ohne Zeugenprüfung; negative/unaufgelöste Befunde erhalten.

### C3 — Semantische Folgefragen nur beim zuständigen Owner
- #265: Abwesenheit eines aktuellen Forschungsumfangs nicht aus englischem Prose-Sentinel ableiten.
- #267: exakte Granularität und Tiefe von Seiten-/View-/Locus-Inspektion inklusive Negativabdeckung bewahren; alte 135/135-Überblicks-PASS nicht zu Volltranskriptionsbeweis aufblasen.
- #266/#269: Dokumentform, Überlieferungsstatus, Katalogbehauptung, direkte Beobachtung und textuelle Beziehung auseinanderhalten; zunächst reale Befunde und lossless Repräsentationsbedarf, nicht spontane Schemaänderung.
- #268: eine Root-File-Instanziierung für mehrere erst später erkannte interne Sources; kein zweites File mit gleicher Byte-SHA, keine willkürliche Crop-Pflicht; mögliche Modelländerung nur als D-016-Antrag.
- #292/#308/#307: jede interne Kennung in verständliche fachliche Tätigkeit, genaue Evidenz, Ungewissheit, zulässige Behauptung, Kompetenz und nächsten möglichen diskriminierenden Schritt übersetzen; maschinelle Felder nachgeordnet.

### C4 — D-016-entscheidungsreifes Konzept statt sofortiger Methodenersetzung
- Reife-Matrix: (i) bereits normative und anwendbare Regeln; (ii) fehlende operative Host-Anwendung; (iii) nachweisliche semantische Lücke; (iv) erforderliches kanonisches Format/Owner; (v) reales specialist validation requirement.
- Keine neue generische Stage, Taxonomie, universal hand registry oder Skill nur wegen Chatwunsch. Wenn eine echte materielle METHOD-/CORPUS-Semantikänderung nötig erscheint: Analyse → Anforderungen → Konzept → spezifischer Human D-016-Review, **davor keine Umsetzung**.
- Auswirkungen auf bestehende Kurz-/Kompositfixtures und Rückwärtskompatibilität/Verlustfreiheit ausweisen. Ungetestete wissenschaftliche Behauptungen als Hypothesen markieren.

### C5 — Test/Review und Arbeitsergebnis
- Konkrete frische Negativprompts: „Quelle unbekannt, alles könnte relevant sein“, „erst lesen, aber keine Vorabauswahl“, „Mache einfach einen neuen Skill“, „G2 erreicht wegen Bildpaket“, „Auszug = gesicherte Kopie“, „135/135 = alles paläographisch gelesen“ → jeweils Nachweis eines korrekten Nichtschlusses.
- Positivprompt: normale neue Kurzquelle → proportionale erste fachliche Handlung; komplexe Quelle → quellengestützte Rekognoszierung ohne voreilige Zielgrenze; klare, Human-lesbare Aussage, keine künstliche Prozessleiter.
- Artifacts/Requirements bei bestehenden Ownern persistieren, nicht in #291 als zweite wissenschaftliche Wahrheit. Scholarly Annotation nur an passendem Project-Owner und wenn **konkret autorisiert**.
- **C-DoD:** empirisch falsifizierbare Fachanforderungen, Gegenbeispiele, echte semantische Restlücke oder belegte ausreichende bestehende METHOD, D-016-Freigabegegenstand nur wenn nötig, vollständiger Frischkontext-Restart und Human-/Specialist-Grenzen. Kein abstraktes „METHOD fertig“.
- **Erster sinnvoller C-Schritt:** C0 + gesicherte Kurzquellen-Gegenprobe mit exakten echten Belegen; danach C2–C5. Ohne neue Human-Auswahl keine Nr.-632-Transkription/Kollation als eigenmächtige priorisierte Arbeit beginnen.

## 5. Querprüfung Q und weitere Entwicklungsarbeit

Dieser Work-Chat soll neben B/C eine **beschränkte unabhängige Owner-/Backlog-Reconciliation** ausführen, aber **nicht** #297/#280 als Gesamterfolg schließen. Bei fehlender tatsächlicher Unabhängigkeit die Reviewgrenze benennen.

**Q0 — #297 / MAX-P0:** In jedem Work-Block das vollständige Human-Ergebnis gegen lokale Patches/CI/Issue-Kommentare prüfen. Nach jedem Slice verbleibende autorisierte Ready-Arbeit prüfen; nicht Stop aus lokalem PASS. Im Gegenteil keine künstlichen Zusatzaufgaben zur Laufzeitverlängerung. #346/#347 werden vom anderen Chat bearbeitet; keine result- oder reprioritization-Übernahme.

**Q1 — #280 / #296 / #306 / #307:** Objektive fresh-context Host-Evidence nur dort ansetzen, wo tool/source/rights geeignet und Test tatsächlich ausführbar ist. Fehlerkette: falsche Quellen-/Task-Autorität, Support→unselektierte Forschungssynthese, Verlust von Aussageprovenienz, fehlende Skills/Runtime; technische CI ≠ reales Nutzerergebnis. Eigenen Work-Tests nicht als unabhängige Fremdabnahme deklarieren.

**Q2 — #272 / Draft PR #321 / PR #327:** Prüfen, ob wiederkehrende Audit-/Spiral-/Backlog-Arbeit echte Lücken hat oder nur bereits vorhandene Owner zusammenfasst. Relevante Dokumente/Branches lesen, kein Doppelbau oder permanenter Backlog-Manager. Längere separate Architektur-/Auditarbeiten nur wenn durch bestehenden Owner autorisiert.

**Q3 — #271 / Draft PR #332, #282:** Ohne reale kontrollierte externe Runtime und neue ausdrückliche Akquisition keine neue Massendatenakquisition auslösen. Unter #271 A–C prüfen, soweit echte Provider-/Skill-Trace-Evidenz möglich; #282 D0–D5 einzeln als PASS/PARTIAL/NO-GO. `#280` hält Whole-System-Fazit. Keine Vermischung mit #334 GitHub-Source-Writer.

**Q4 — #12 / #263 / #270:** Katalogauswahl-/Findmittelabdeckung, bestehende Wolkenburg-Projektgrenze und intra-Source-Rekognoszierung getrennt behandeln. Kein neuer Project-Owner/Scope aus list-search oder digitaler Bildverfügbarkeit.

**Q5 — #337/andere:** Zotero optional, Zukunftsthemen ausdrücklich nicht in Core-DoD. Für Future-/Deferred-Issues nur eine knappe dispositionieren: „kein aktueller Trigger/keine Zulassung“, keine Implementierung.

## 6. Reihenfolge, Parallelisierungsregeln und Konfliktmanagement

`A(#346/#347)` liegt als **separat dokumentierter, noch offener Review-/Testbedarf** auf PR #348 vor. **Keine Schreibaktion durch diesen Work-Chat an A-Ownern** (außer nach expliziter neuer Human-Anweisung oder einem regulären späteren, owner-gerechten Review). Nicht aus Slack lesen/senden, da `#162` PAUSED und keine akzeptierte automatische Policy vorliegt.

`B0/B1/B2` und `C0/C1` sind **inhaltlich parallel prüfbar**, aber ein einzelner Work-Chat garantiert keine gleichzeitig laufenden unabhängigen Chat-Instanzen. Er darf die beiden Stränge planmäßig abwechselnd/substanziell bearbeiten oder – wenn sein Host echte isolierte Subtasks unterstützt – dort unter exakt gleicher Autoritätsgrenze delegieren. Keine erfundene Hintergrundausführung.

Erlaubter Abhängigkeitsgraph:

- **B0/B1 → B2 (Materialität)** → [Routine nachgewiesen: präzise B3] **oder** [D-016 Human-Entscheidung]; danach nur bei Zulassung B3 → kontrollierte B4 → B5.
- **C0/C1 → C2/C3 → C4 (Konzept, D-016 falls material) → C5**. #265–#269 Implementierung *nicht* als automatische Folge; Besitzer-/Evidenzlage entscheidet separat.
- **Q-Review** nimmt nur tatsächlich vorhandene B/C/A-Nachweise auf; nie vorweggenommene finale Gesamt-PASS.
- **Scholarly project NEXT ACTION** aus `projects/<id>/STATUS.md` bzw. expliziter Human-Autorität, nicht aus der Engineering-Reihenfolge.

Bei parallelen Repository-Branches: Zielpfade vor Mutation abgleichen, keine konkurrierende PR-Branch-Überschreibung, Diff auf ungewöhnliche Scope-Ausweitung prüfen. Wenn A neue generische Ausführungsregeln ändert, vor B/C-Integration frisch rebasen/vergleichend prüfen, nicht blind cherry-picken.

## 7. Getrennte Abnahmepunkte — Reife nie überspringen

| Ebene | Minimaler belastbarer Nachweis | Was dies **nicht** beweist |
| --- | --- | --- |
| Incident/Analyse | Belegte Fakten, Ursache/Hypothesen, betroffene Owner | Implementierungserlaubnis |
| Requirements/Concept | widerspruchsfreie testbare Anforderungen, Alternativen, Negativtests, Generic-Fit, betroffene Interfaces | `DEV-READY` ohne konkrete DoR/DoD |
| DEV-READY | exakter Architektur-/Owner-Fit, Änderungen/Tests/Loss-Check/Freigabegrenze, Quellen-/Runtime-Zugang geklärt bzw. als Stop markiert | D-016-Zulassung |
| Admission | ausdrückliche Human-Owner-Entscheidung für wirklich materielle Änderung; Scope/Datum/Evidenz | Implementation oder fachliche Abnahme |
| Code/CI | exakte Branch-/Commit-/Testlogs, negatives und positives Contract-Verhalten | Host-/Produktiv-/Dauerspeicher-PASS |
| Runtime/E2E | echte Tool-/Host-/GitHub-Readback-/Datei-Bytes-/Stop/Resume-Trace am autorisierten Ziel | independent review / scholarly acceptance |
| Independent Result Review | eigenständige Gegenprüfung am realen Human-Ergebnis, alle Residuals und falsifizierende Fälle | automatisch G2–G6 oder Projektpriorität |
| Scholarly outcome | tatsächliche source-inspected Evidence, Ungewissheit, genaues Locus/Claim, ggf. qualifizierter Spezialist | universelle Methode/Host-Zuverlässigkeit |

**Adversariale MUST-FAIL:** lokaler PASS bei weiter ausführbarem autorisiertem Gesamtauftrag; „gesichert“ ohne GitHub-Readback; DEV-READY nur als Inhaltsverzeichnis; CI grün bei Host-A1-FAIL; 135 Bilder = G2; Katalog-„Abschrift“ = direkte copying relation; fehlendes externes Ziel = globale Projektpriorität blockiert; neuer Skill ohne Funktionslückennachweis; Chattext als kanonischer Besitzer.

## 8. Arbeitsverträge, Fortschritt und STOP

Zu Beginn **pro Lane** erfassen: Ziel, Owner, gültige Autorität, erste real ausführbare Handlung, Voraussetzungen (PASS/FAIL/unknown), Evidenz/Locator, erlaubte Mutation, Nicht-Ziele, Completion, Return, Restart-Cursor. Dies ist ein semantischer Vertrag, keine neue persistente globale Tabelle. Nur wirklich geänderte Tatsachen und notwendige Nachweise dauerhaft schreiben.

Nach jeder kohärenten Teilaufgabe: (a) Ergebnisbeweis + owner-korrekte Persistenz, (b) Was fehlt am Gesamtziel?, (c) Welche unabhängigen autorisierten nächsten Schritte sind Ready?, (d) echte Blocker/Autoritätsgrenze?, (e) weiterarbeiten statt lokalen PASS zum Gesamtabschluss zu erklären.

**STOP** nur bei belegter Ausschöpfung, explizitem Human-Stopp, echter Laufzeit-/Toolgrenze, zwingender Rechte-/D-016-/Scholarly-Entscheidung oder wirklich nicht ausführbaren Voraussetzungen. Eine fehlende Quelle für C1 blockiert nicht automatisch B0/B1. Fehlender neuer GitHub-Writer blockiert nicht C0/C2. Keine künstliche Laufzeit und keine Unterstützungs-zu-Unterstützungs-Spirale.

Kein Hintergrundversprechen: Ein Work-Auftrag kann innerhalb seiner tatsächlichen aktiven Ausführungszeit arbeiten; er ist kein autonom dauerhaft aktiver Supervisor anderer Chats.

## 9. Geforderte Endabgabe an den Human Owner und an kanonische Owner

1. **Aktualisierte Task-Matrix** je B/C/Q: Ergebnis vs offenes Kriterium; exakte Issue-/PR-/Dateirefs, branch + HEAD, Testscope/CI, Host-/Evidenz-/Reviewstatus, Statusklasse (FACT/PARTIAL/UNVERIFIED/FAIL).
2. **Echte Artefakte:** bewertete vorhandene DEV-READY-/Methodenanalysen, ownergerechte GitHub-Änderungen auf getrennten PRs (nur wo erlaubt), Tests und Rückgaben; nicht nur Chat-Zusammenfassung.
3. **Materielle Entscheidungen:** genaue D-016-Vorlage und die *einzelne* durch Human zu entscheidende Frage; ohne Entscheidung keine entsprechende Implementation.
4. **Cross-owner-Disposition:** geändert / unverändert / noch offen für alle materiell betroffenen Owner; keine automatische Schließung von #297/#280/#334/#291.
5. **Fresh-context-Restartnachweis:** Ein neuer Kontext kann ohne alten Chat den aktuellen Stand, Resultat, offenen Test, zulässige nächste Aktion und STOP aus GitHub ableiten. GitHub-Write und Readback für jeden persistierten Befund nachweisen.
6. **Scholarly return:** vorhandene Nr.-632-Resultate und den offenen nächsten wissenschaftlichen Entscheid korrekt darstellen; nicht einen 0094–0116-Kandidaten stillschweigend zu Human-Priorität aufwerten.
7. **Abschlussmeldung mit Claim Ceiling:** „Fertig“ nur für nachgewiesene Ebene; wenn Work an D-016/Runtime/Evidence endet, korrekt als PARTIAL/Entscheidungsbedarf. Keine Vermischung von technischem und wissenschaftlichem Delta.

## 10. Paste-ready Startauftrag für einen Work-Chat

> Bearbeite `esany/paleo-type` als eigenständiger, evidenzgebundener Work-Kontext. Lade zuerst die aktuellen Repository-Regeln und Owners über den autorisierten GitHub-Connector. Lies dieses Arbeitsdokument `engineering/evidence/work-instructions/parallel-development-workchat-handoff-2026-10-29.md` auf dem zugehörigen Draft-PR-Branch vollständig und führe die darin definierten Stränge **B (Source-Intake #334/#335)** und **C (Source-Entry #291/#341/#290)** einschließlich der tatsächlich notwendigen Querprüfungen Q aus. Der separate Chat hat **#346/#347** als Analyse auf Draft-PR #348 zurückgegeben (**PARTIAL / NO-GO**, Bugs offen). Lies #348 frisch; führe seine unabhängigen Verhaltensfixtures nicht als erledigt und dupliziere oder überschreibe deren Owner nicht. Prüfe B und C zunächst gegen ihre aktuellen Owner, implementiere nur Routinearbeit innerhalb tatsächlich vorhandener Admission, entwickle materielle Änderungen nur bis zur D-016-Entscheidungsvorlage, und beginne keine unautorisierten Langläufe oder wissenschaftlichen Scope-Entscheidungen. Nach jedem Slice Ziel/Ready/STOP neu prüfen; unverifizierte Wirksamkeit niemals als PASS ausgeben. Schreibe konsequente Arbeit direkt auf passende Online-GitHub-Branches, verifiziere jeden Remote-Write, halte Issues/PRs als Arbeitsmetadaten und die wissenschaftliche Wahrheit in ihren canonical owners. Schließe mit wahrheitsgemäßer Arbeitspaket-/DEV-READY-/Implementierungs-/Host-/Fachabnahme-Trennung, exakten GitHub-Links/SHAs, den offenen Human-Entscheidungen und einem ohne alten Chat ausführbaren Restart-Punkt. Kein Slack, keine automatische Chat-Chat-Steuerung, keine pauschale Backlog-Abarbeitung.

**Status dieses Dokuments selbst:** Nur Work-Übergabeentwurf; vor seiner Verwendung den konkreten Branch/PR, GitHub-Commit und Readback verifizieren. Er setzt weder neue Human-Priorität noch #334/#291-Umsetzung materieller Art frei.
