# savesax — integrierte DEV-READY-Planung nach parallelem Outcome-Review
**Datum:** 2026-10-27  
**Status:** **DEV READY für den kohärenten evidenzgeleiteten Entwicklungs-Arbeitsblock unter #271**; **Provider-Semantikänderung nur nach tatsächlicher Beobachtung**; **PRODUKT-ABNAHME NICHT READY**. Kein Implementierungs-PASS und kein Merge/Owner-Acceptance-Status.  
**Planungsträger:** Draft [PR #329](https://github.com/esany/paleo-type/pull/329), Branch `audit/savesax-evidence-first-system-review-20261009`. Diese Datei ist ein nichtnormativer, derzeit **ungeprüfter Planungskandidat**; sie erzeugt keine neue Architektur, keinen neuen Issue-Owner und keinen neuen D-016-Entscheid.  
**Frisch gelesene Basis:** `paleo-type/main@256f12bc8894df6fefa7bc8e814e10cc755b9cd4`; aktuelle `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `methodology/workflow.md`, `methodology/maintenance.md`, `.agents/skills/savesax/SKILL.md`, `tools/archival_source_acquisition.py`, `tests/test_archival_source_acquisition.py` und `docs/archival-source-acquisition.md`. **Vor Umsetzung erneut gegen HEAD prüfen.**

## 1. Paralleler Review — tatsächlich gelesen, nicht als eigene Freigabe missverstanden

- **Paralleler systemischer Review:** [PR #327](https://github.com/esany/paleo-type/pull/327), Draft/offen am 2026-10-27, Branch `fix/outcome-preserving-spiral-breaker-2026-10-09`. Insbesondere `engineering/evidence/audits/outcome-preserving-spiral-audit-2026-10-09.md` und `engineering/evidence/decisions/outcome-preserving-return-gate-d016-decision-brief-2026-10-09.md` wurden frisch gelesen; außerdem der vorgeschlagene `engineering/prompts/CONTRACT.md` mit Invarianten 17–20.
- **Ergebnis des Reviews:** Wiederkehrende Fehler dürfen **nicht** dadurch als gelöst gelten, dass ein Owner/eine Regel existiert. Lokale technische PASSes müssen über einen **Outcome-Preserving Return Gate** an das geschützte Mensch-/Produktziel zurückgeführt werden. Für jeden konsequentiellen Block sind Outcome, semantische Grenzen, gekoppelte Pflichten, autorisierte Aktion, DoR, DoD, Residual/Rückkehrbedingung und Claim Ceiling sichtbar zu halten. Ein neuer Kommentar ist kein Wirksamkeitsnachweis.
- **Exakte Autoritätsgrenze:** D-016 ist **nur für PR #327 / den dortigen exakt beschriebenen Branch/Carrier** als ADMITTED dokumentiert; kein Merge, keine globale Freigabe und keine vertikale Produkt-/Runtimeabnahme. Das korrespondierende [Wissensarbeit PR #88](https://github.com/esany/Wissensarbeit/pull/88) hält `implementation_allowed=false` auf globaler Ebene. **Diese Zulassung wird nicht auf #271, #329 oder neue METHOD-/Architekturarbeit übertragen.**
- **Weiterer Planungsbezug:** [PR #321](https://github.com/esany/paleo-type/pull/321), Draft/Phase A, bündelt #271/#282 als echten Produkt-/Runtime-Akzeptanzstrang und #280 als System-Rückkehr; #297 fordert die Unterscheidung „kleinste hinreichende komplette Lösung“ statt „kleinster lokaler Patch“.
- **Auswirkung hier:** Bestehenden Provider-Adapter und restartable Core dort weiterverwenden, wo sie tragen. Änderungen werden nicht nach Dateigröße/CI-Status, sondern nach vollständigem `Archiv-URL → tatsächliche Dateien → öffentliches Fullsize → dauerhaftes Paket` bewertet. **PR #327 bleibt ein parallel zu beachtender, nicht gemergter Review-/Assurance-Carrier.**

### Frische Gegenprüfung der parallelen Carrier am 2026-10-27 (zweiter Abgleich)

- **PR #327** wurde nicht nur anhand seiner PR-Zusammenfassung, sondern an den aktuellen Dateien `outcome-preserving-spiral-audit-2026-10-09.md`, `outcome-preserving-return-gate-d016-decision-brief-2026-10-09.md` und `engineering/prompts/CONTRACT.md` auf Branch `fix/outcome-preserving-spiral-breaker-2026-10-09@ebd3f100c9fb1d74e07a44d8e7da7af663518f43` gegengeprüft. Seine Kernfolgerung: **Eine erneute beobachtete Fehlleistung ist eine operative Kontrolllücke trotz vorhandener Regel; eine rein dokumentarische Wiederholung der Regel ist kein Fix.** Seine Admission bleibt exakt auf #327 begrenzt.
- **PR #321**, `audit/systemic-closure-backlog-2026-10-09@4276441e369f1e8742516fc3a0cc825cd5cd06e3`, wurde an `systemic-closure-backlog-reconciliation-2026-10-09.md` gegengeprüft. #271/#282 gehören dort zum **produktiven** Abnahmestrang, #280 zur **Whole-System**-Rückkehr; PR #321 selbst ist eine ungemergte Phase-A-Planung, kein Abschluss.
- **PR #329** wurde auf eigenem Arbeitsbranch gegen `paleo-type/main@256f12bc8894df6fefa7bc8e814e10cc755b9cd4` geprüft. Diese Planung wird **an einer Stelle weitergeführt**, statt einen zweiten DEV-READY-Carrier oder konkurrierende Arbeitsaufforderungen anzulegen.
- **Genuine Delta dieser Gegenprüfung:** Die W0-Ausgabe wird unten explizit als beweisbarer, repositoryseitig referenzierter Providerbericht definiert, der neue Fix wird nach Beobachtung an seiner **echten Ausführungsgrenze** gegen Einbild-/Atlasfall getestet, und der ausführende Kontext muss vor Codeeingriffen alle inzwischen veränderten Review-HEADs neu prüfen. **Keine neue Freigabe, Priorität, Source/File/Project/METHOD-Wahrheit oder Produktabnahme** folgt daraus.

## 2. Outcome-Preserving Return Tuple für #271 / savesax

| Feld | Verbindlicher Inhalt dieses Arbeitsblocks |
|---|---|
| **Geschütztes Human Outcome** | Human gibt eine Sächsisches-Staatsarchiv-Archiv-URL und erhält **alle tatsächlich gelisteten, öffentlich online einzeln herunterladbaren hochauflösenden Bilder** vollständig und überprüfbar in einem kontrollierten externen Ordner samt Archiv-Quellenangabe. Ein Einbilddatensatz und Mehrbildatlas durchlaufen denselben Ablauf. |
| **Semantische Grenzen** | Archiv-Katalogeintrag ≠ Digitalisat-GUID ohne Evidenz; konstruiertes URL-Muster ≠ existierende Datei; `istEinzelbild` ≠ ohne Prüfung Bildverfügbarkeit; öffentlicher Fullsize-Download ≠ archivalischer Master auf Bestellung; technischer CI-PASS ≠ reale Archivpaketsicherung; Quellensicherung ≠ automatische CORPUS-/Project-Registrierung oder Nutzungslizenz für spätere Publikation. |
| **Gekoppelte Pflichten** | Offizielle Objekt-/Bildlistenidentität, wirkliche Namen/Anzahl/Reihenfolge, valider Bildabruf und nachprüfbare öffentlich verfügbare Bildqualität, lokale JPEG-Integrität, externes progressives Speichern, Resume/Stop, Manifeste/Checksum, Human-lesbare Rückgabe, Runtime-Fitness und korrekte Owner-Dispositionsprüfung. |
| **Autorisiertes Handeln** | Vorbereitende Quellen-/Code-Prüfung und kohärente, bereits von #271 getragene **bounded provider/downloader/skill-fix**-Arbeit; GitHub-Arbeit nur über autorisierten Connector. Keine aus PR #327 geliehene globale D-016-Admisson, keine automatisch neue METHOD-/Schema-Änderung, kein langlaufender Erwerb ohne #282-Vorprüfung. |
| **Definition of Ready** | Siehe §5, getrennt in `Start DEV-Arbeitsblock` und `Start verhaltensändernde Provider-Implementierung`; nicht miteinander verwechseln. |
| **Definition of Done** | Siehe §7; vollständige Providerliste/Endpunkte und technische Artefakte nachgewiesen; wirklicher Produktivlauf erst mit #282-externem Ziel; fachlicher/Whole-System Review unter #271/#280 getrennt. |
| **Residual / Rückkehr** | `istEinzelbild=false`-Semantik und ggf. Katalog-/Digitalisat-GUID und reale Pixel/Bytes sind LIVE noch unbewiesen. Der Arbeitsblock kehrt mit Primärbefund → minimal hinreichender Fix → Repository-CI → vollständiger Produkt-Nachweis oder präziser, begrenzter Evidenzhürde zu #271 zurück; #282/#280 erhalten nur ihre materiellen Folgen. |
| **Claim Ceiling** | Dieses Dokument ist **DEV-Ready-Planung**, kein erfolgreiches JPEG-Acquisition-Testresultat, kein unabhängiger Providerbeweis, keine bestätigten Bildzahlen, kein externes erhaltenes Paket, keine erfolgreiche vertikale Akzeptanz. |

## 3. Sachliches Ziel und Testquellen

**Belegtes Produktziel nach ausdrücklicher Human-Korrektur 2026-10-27:** Exakt die hochauflösenden Bilder, die im Web über die normalen SStA-`fullsize`-/Downloadwege manuell herunterladbar sind, automatisch, einzeln und verlustfrei sichern; Archivquelle angeben. Keine Masteranforderung, keine abstrakte Lizenz-/Rights-Debatte als Ermittlungssperre. Offen zu haltende Fragen betreffen die **technische Dateivollständigkeit und Laufzeit**, nicht erfundene rechtliche Hindernisse.

- **T1 — Vergleichsarchivalie:** Human-verlinkte Katalog-URL `https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=112bd5fe-72e0-4694-9507-34a896b4583b`. Human berichtet **ein Bild**. Dateiliste/Digitalisat-GUID noch nicht unabhängig live gelesen. Die im Ursprungschat präsentierten `0002.jpg` und `0003.jpg` waren **unbelegt**, nicht nachgewiesen 404; kein neuer Bildname ohne Listeneintrag.
- **T2 — Schenk'scher Atlas:** Digitalisat-GUID `c52a0351-970a-4896-a349-918c35636cfc`, `/digitalisate/<GUID>/files.json`; früher berichtete 240 Einträge (163 `true`, 77 `false`) bleiben **unverifizierte Hypothese**. Nachweis mit echten `files.json`-Bytes und repräsentativen öffentlich zugänglichen JPEGs erforderlich.
- **T3 — bestehende Kontrollen:** Vom Repository bereits belegte Nr. 632 (135), Nr. 754 (61) und Oppurg (139) als Offline-Fallback-/Regressionen. Ihre Zahl bedeutet **keinen** unabhängigen Vollbild-Paket-Nachweis.
- **Datenbeweis pro Quelle:** archivischer Objektlink, tatsächlich zugeordnete Digitalisat-GUID, `files.json`-Antwort-Hash, Roh-`name`/`typ`/`istEinzelbild`-Population, eindeutige Namen, tatsächliche Anzahl und begründete Ordnungsregel, wenige HTTP-/Bildbeweise über die korrekte Route. Kein fortlaufendes `0001…N` als Ersatz.

## 4. Geänderter Entwicklungsplan als **ein** kohärenter Arbeitsblock

### W0 — primäre Datenprüfung und Entscheidungs-Gate (read-only, ab jetzt DEV-fähig)

1. **Aktuellen Stand & URLs** bei #271 und in Providerdaten neu prüfen. Erst das Katalogobjekt, die Digitalisat-Verknüpfung und `files.json` beider Zielquellen belegen. Falls die Katalog-GUID nicht die Digitalisat-GUID ist: Beziehung aus echter Archivseite nachweisen.
2. Einträge zählen, `name`, `typ`, `istEinzelbild`, Dubletten, Ordinal-/Listenordnung und unerkannte Formen **aus realer Antwort**, nicht aus Chatannahmen berichten. **W0-Liefergegenstand:** eine überprüfbare, nichtnormative Provider-Evidenznotiz im vorhandenen `engineering/evidence/`-Bereich auf dem neuen Entwicklungsbranch, mit je Quelle **Katalog-URL, tatsächlicher Digitalisat-GUID, Request-URL, UTC-Abrufzeit, HTTP-/Access-Ergebnis, `files.json`-SHA-256, Eintragszählung je `typ` und `istEinzelbild`, exakten Namen/Ordnungsbelegen, repräsentativen Bildrouten-/JPEG-Messwerten sowie offenem Claim Ceiling**. Nur wirklich gelesene Bytes zählen als Providerbefund. Keine Archivbild-Binaries ins Git-Repo. Bei fehlendem Zugriff stattdessen explizit `UNVERIFIED` und die genaue scheiternde Route; kein fingierter Rohbeleg.
3. Nur **tatsächlich gelistete** Beispiele probeweise gegen `/fullsize/<exact-name>.jpg` und bei Bedarf `download.jsp` prüfen, ausdrücklich auch `false`, falls gelistet. HTTP/Redirect, Typ, Länge, JPEG-Bytes, vollständige Dekodierbarkeit, Pixelmaß/Route prüfen; keine großflächige Sicherung oder bezahlten Browseragenten.
4. Falls `false` als gültiges öffentliches JPEG nachgewiesen: Parserkriterium gezielt nach Datenform korrigieren; falls es andere Darstellungsform/Tiles meint: separaten, belegten Datenpfad beschreiben und kein falsches JPEG-Versprechen abgeben; falls uneindeutig: **FELDSEMANTIK UNVERIFIED**, keine Blindänderung. Zugriffsmangel bleibt **lokal**, nicht „Archiv nicht erreichbar“.
5. Einbild- und Mehrbildquelle mit exakt den gelieferten Datensätzen modellieren. Negativfall: `0002`/`0003` müssen ohne Listeneintrag im Plan unmöglich sein.

**Gate W0→W1:** Die W0-Evidenznotiz muss auf dem tatsächlichen Entwicklungsbranch nachweisbar persistiert und im PR referenziert sein. Für eine semantikändernde Providerparser-Korrektur müssen echte `files.json`-Feldpopulation und mindestens ein diskriminierender bildbezogener Gegenbeleg vorliegen. Kann W0 nicht erfüllt werden, darf die Änderung **nicht** als validiert implementiert werden; nur datenunabhängige Prüf-/Sicherungsverbesserungen und offene Evidenzgrenze sind zulässig.

### W1 — providerlokale Fixes am wirklichen Datenfluss (nach W0-Gate)

- `tools/archival_source_acquisition.py` — `SaechsischesStaatsarchivProvider.plan` und URL-Bildrouten nur soweit Providerbelege einen Defekt zeigen. Nicht katalogisierte Dateinamen bleiben ausgeschlossen. `typ`-/Pfadsicherheit und explizite Unknown-/Tile-Fehler bleiben erhalten. Bei gemischter Liste **keine stille Auslassung**; Planergebnis muss ohne Hochrechnen vollständig zur gestützten Quelle passen.
- **GUID/Metadaten-Einstieg:** zuerst den **Human-facing Skill** end-to-end mit ausschließlich der Archiv-URL und dem bereits im Kontext zulässig vorhandenen Ziel prüfen. Die sieben CLI-Metadatenfelder sind ein **internes Interface**, nicht automatisch ein Nutzerfehler. Nur wenn die beobachtete Skill-Ausführung das Mapping nicht leisten kann, minimal nötigen Adapter/Skillpfad ändern; keine neue allgemeine Catalog-Plattform.
- **Reihenfolge:** prüfen, ob von `files.json` normativ/faktisch gelieferte Sequenz gilt oder lexikografisch sortierte Namen die real richtige Reihenfolge herstellen. Keine generische Reihenfolge ändern, bevor ein Fehlerbeleg vorliegt.
- **Route/Pixel:** wähle den belegten Web-Download mit gesicherten Pixelmaßen und ohne Vorschau-/Tile-Ersatz; interne Wahl transparent halten. Weder „fullsize“ per URI-Name noch `download.jsp` per historischem Default beweisen automatisch die beste verfügbare Online-Datei.
- **Integrität:** `jpeg_dimensions()` + `_inspect_jpeg()` prüfen derzeit nur Start/SOF und SHA der empfangenen Bytes; mit geeigneten begrenzten Regressionen Erkennung abgeschnittener/nicht vollständig dekodierbarer JPEGs herstellen. Keine ungerechtfertigte Behauptung „archival Master“. Externe Abmessungs-/Längenbelege soweit zugänglich berücksichtigen, keine falsche Guarantee auf unverfügbare Originalhashes.

### W2 — vollständige Produktpfad-Regression und Sichtbarmachung (untrennbar mit W1)

- Tests: Einbild aus **einem gelisteten Namen**, keine 0002/0003; reale nicht-kontinuierliche Mehrbildliste; true/false-Mischung nach belegter Semantik; unbekannte Formate/DZI/Tile/nicht sichere Namen; Dubletten; falsche/abweichende GUID; truncated JPEG mit vorhandenem SOF; tatsächliche Webroute/Pixel; korruptes Bild; Netzwerk-/Resume-/Cancel/Sidecarfehler; `--status` read-only; keine Git-/Runner-„Preservation“; durchgängiger Human-Fall nur mit Archiv-URL.
- Bereits bestandene Finalisierungs-/Fortschrittstests (PR #328) müssen **weiterhin** funktionieren. `complete` erst nach allen einzelnen Bildern und Manifest-/Checksummenartefakten.
- Ergebnisorientierte Fehlertexte: nennen **welches** Bild/Beleg fehlt und warum die Quelle **noch nicht vollständig gesichert** ist; keine Pseudo-Links und kein CI-PASS als Produktresultat. **Wirksamkeits-Retest an der tatsächlichen Bediengrenze:** Aus einer URL für die Einbildquelle dürfen ohne echten Listennachweis niemals 0002/0003 als Bilder präsentiert werden; aus einer gemischten Atlasliste darf keine durch `false` erreichbare JPEG-Datei still verschwinden. Regeltext allein oder ein lokaler Parser-Unit-Test ohne beobachteten End-to-End-Effekt ist kein bestandenes Review.
- Code/Doku/Skill-Änderungen werden als ein gemeinsames, vollständig betrachtetes #271-PR-Paket umgesetzt. GitHub-Connector, PR-Head und exakter CI-Lauf verpflichtend, aber nicht „Produkt fertig“.

### W3 — getrennte **produktive Abnahme** erst nach #282-Fitness und realem Auftrag

- Bevor der lange Download beginnt: **beabsichtigten externen Zielordner**, dauerhaftes Schreiben, Neustart, beobachtbaren Lauf, stop/containment und realen Providerzugriff prüfen. Kein Default in Chat-Sandbox, GitHub Actions oder Repository.
- Wenn Runtime/Destination und Startautorität vorhanden: eine reale Quellenpaketsicherung durchführen, danach Anzahl/Dateinamen gegen `files.json`, pro-Datei JPEG/Pixel/Hash, alle Sidecars und `ACQUISITION_STATE.json` kontrollieren.
- **#271 Produktabnahme** nur nach echtem Paket. **#282** dokumentiert Laufzeit-Fitness und kontrollierten Erwerb. **#280** führt den gesonderten Whole-System Result Review. Die PR-#327-Vertikalwirksamkeitsprüfung ist ein paralleler Kontrollstrang, kein automatisch erzielter PASS.

## 5. Definition of Ready (DoR), getrennte Eintrittsschwellen

| Eintritt | Kontrollanforderung | Ergebnis |
|---|---|---|
| **Start #271-DEV-Arbeitsblock W0** | Menschliches Ergebnis, die zwei Quellen, echtes Repo-/Code-/Owner-Lesen, definierter GitHub-Branch/PR, Umfang, W0-Evidenzartefakt, Negativfälle, Stop- und Review-Bedingung; keine Image-Bulk-Side-Effects | **READY** — dieser Plan ist ein ausführbarer Startauftrag für die kleinste **kohärente** evidence-first Qualifikation; **noch kein W0-PASS**. |
| **Start providersemantik-ändernden Code W1** | Primärquellennachweis für `files.json` und `istEinzelbild`, diskriminierender Live-JPEG-Befund oder gleichwertige konkret belegte Providerbytes; bekannte richtige Bildliste/GUID | **CONDITIONAL / EVIDENCE PENDING** — keine regelwidrige `false`-Umdeutung nur aus Chat-/Schemaannahmen. |
| **Start vollständige technische Integrationsabnahme W2** | Konkreter Provider-/Metadaten-/Bild-Fix einschließlich testbarer Eingabe-/Ausgabekriterien, akzeptable unbekannte Formate, angepasste Fixtures; aktuelle Arbeitsbranch und CI | **NACH W1**, keine Abnahme durch Prompt. |
| **Produktiver Langlauf W3 / #282** | Tatsächlich gewähltes externes Ziel, persistente Runtime, Observe/Stop/Resume-Fitness, autorisierter Erwerb, gespeicherte Quellenidentität | **NICHT READY** — diese Voraussetzungen dürfen nicht fingiert werden. |

**Wichtig:** „DEV READY“ heißt hier **bereit zum Beginn des vollständigen evidenzgeleiteten Entwicklungsblocks**, **nicht**, dass die unbewiesene Flag-Semantik bereits zu Code gemacht werden darf. Keine neue Human-Entscheidung über das Produktziel erforderlich. Human-Eingabe erst bei tatsächlich unbekanntem externen Dauerziel bzw. materiell neuer Autorität, nicht bei intern lösbarer Archiv-/Toolroutingfrage.

## 6. Fehlerhypothesen / falsifizierbare Entscheidungen

| Hypothese | Beweis/Gegenbeweis | Konsequenz |
|---|---|---|
| H1: Der Atlas enthält JPGs mit `false` und gültigem öffentlichem Fullsize-JPEG. | Original-`files.json` + HTTP + vollständige JPEG-Probe für einen gelisteten `false`-Eintrag | Datengetriebene Parserkorrektur; gemischte fixture; keine neue Providerarchitektur. |
| H2: `false` bezeichnet ausschließlich komplexe Nicht-JPEG-/Tile-Repräsentationen. | Echte Entry-/Route-/Content-Belege, die H1 widerlegen | Kein blinder „alles JPG“-Fix; betroffene Dateien explizit als außerhalb belegter JPEG-Modus-Semantik kennzeichnen; erforderlichen zusätzlichen Bildpfad separat begründen. |
| H3: Archiv-Katalog-GUID = Digitalisat-GUID der zweiten Quelle. | Offizieller Record-Link + korrekte `files.json`-Antwort | Nur dann `/digitalisate/<GUID>/...` direkt nutzen; sonst echte Verlinkung auflösen. |
| H4: `download.jsp` und `fullsize` liefern gleiche Bildqualität. | Repräsentative Pixel-/Bytes-Probe pro Route | Routenregel mit Daten statt pauschalem Default begründen. |
| H5: JPEG mit SOF aber abgebrochener Rest wird zu Unrecht akzeptiert. | Konstruierter minimaler Regressionfall und vollständiger Bilddecoder | Prüflogik gezielt härten ohne notwendige legitime Provider-JPEGs zu verwerfen. |
| H6: Bestehender `savesax`-Aufruf kann Metadaten vollständig intern auflösen. | Fresh-context URL-only-Interaktion mit aktuellem Skill und realem Archivdatensatz | Falls PASS: keine neue CLI-/Catalog-Architektur; falls FAIL: Owner-lokale Minimalreparatur. |

## 7. Definition of Done / Abnahmematrix

| Nachweis | Objekt/Owner | Bestehen bedeutet |
|---|---|---|
| E1 — Quellenidentität und Bildlistenevidenz | #271, für T1 & T2 | Tatsächliche GUID, genaue Entry-Liste, Hash, Anzahl, Reihenfolge, keine erfundene Datei. |
| E2 — verfügbare öffentlich gelieferte Bildbytes | #271, Provider-Route | Eindeutige gelistete Namen, HTTP/JPEG-/Pixelbelege aus `true`/`false` soweit vorhanden; kein stilles Verlieren verfügbarer JPEGs. |
| E3 — deterministische Regression | #271, Test/CI | T1 als ein Bild, T2 als belegte Mehrbildliste, Negativfälle, Dekodierbarkeit/Resuming/Sidecars/Read-only und bestehende Suite; exakter GitHub-Commit+CI. |
| E4 — menschlicher natürlicher Einstieg | #271, frischer Ausführungskontext | Eine echte Archiv-URL genügt; Human muss keine Dateinamen, internen Adapter, CLI-Felder oder Metadatenfolge liefern. |
| E5 — kontrolliertes echtes externes Archivpaket | #271 + #282 | Genau alle erwarteten JPEGs nach realer Providerliste und voller Prüfung auf dauerhaftem Ziel, korrektes Status-/Manifest-Paket, reproduzierbarer Resume/Stop. |
| E6 — Return-Gate/Whole-System Review | #280, betroffene Owner | Kein lokaler PASS als Gesamtprodukt, klare Residuals/negative Abgrenzungen; PR #327-Vorschlag als noch nicht gemergter paralleler Mechanismus berücksichtigt; keine fremde D-016-Zulassung übernommen. |

`DEV` ist vollständig, wenn E1–E4 nachgewiesen, alle zugehörigen Änderungen gepusht/über GitHub bestätigt, technisch geprüft und zum geschützten Ergebnis zurückgeführt sind; **das Produkt ist erst ab E5 plus einschlägigem E6-Review als gesichert/akzeptiert zu bezeichnen**. Ein E1-Fehlschlag macht Datensemantikänderung ausdrücklich **NICHT READY**, statt eine blinde Teilreparatur zu legitimieren.

## 8. Konkreter Start- und Rückkehrprompt (frischer Dev-Kontext)

```text
DU BIST DER #271 SAVESAX-DEV-/QUALIFIKATIONS-KONTEXT.
Lies online via autorisiertem GitHub-Connector aktuell GOVERNING_OBJECTIVE.md,
AGENTS.md, #271/#282/#280/#297, SKILL.md, Downloadcode, Tests und diese
integrierte Planung. ENTDECKE UND LESE auch inzwischen neue/revidierte
parallele Reviews, statt PR-Titel/alte Chat-Zusammenfassungen als Autorität
zu übernehmen. Prüfe mindestens PR #327 (Audit, D-016, Contract),
PR #321 (Phase-A-Evidenz) und PR #329 auf dem jeweiligen aktuellen HEAD;
notiere exakt ihre Delta-/Admission-/Akzeptanzgrenzen. Eine D-016-
Admission auf #327 wird NICHT zur Freigabe für #271/#329. Prüfe
aktuelles main, Issue-Owner und Arbeitsbranch vor jeder Mutation.

Dein geschütztes Ergebnis: Alle real gelisteten und öffentlich einzeln
herunterladbaren SStA-Fullsize-JPEGs einer per Archiv-URL bezeichneten
Archivalie vollständig, verlustfrei und überprüfbar extern sichern.
Nie Bildnamen aus N/URLs erfinden. Keine zusätzlichen Lizenz-/Master-
Voraussetzungen für den normalen öffentlichen Download.

Arbeite den kohärenten Block W0→W1→W2 durch; vor W1 die echte Provider-
Semantik belegen. Nutze Atlas c52a0351-970a-4896-a349-918c35636cfc und
die Einbild-Katalogquelle 112bd5fe-72e0-4694-9507-34a896b4583b.
Nicht belegte Counts/GUID-Verknüpfungen/istEinzelbild-Bedeutungen bleiben
offen, nicht erfunden. Schreibe eine überprüfbare W0-Provider-Evidenznotiz
mit HTTP-/JPEG-Messungen, wirklichen Dateien und Restgrenzen in den
GitHub-Arbeitsbranch, verifiziere Datei/Commit/PR. Falls Livezugang fehlt:
benenne die konkrete Route/Grenze, protokolliere UNVERIFIED, führe nur
beweisbare datenneutrale Verbesserungen aus und erkläre W1 nicht für
abgeschlossen.

Implementiere die kleinste HINREICHENDE KOHÄRENTE Reparatur im bisherigen
#271-Owner, mit diskriminierenden Tests und streng erhaltenen Safety-/
Resume-/Sidecar-Eigenschaften, über GitHub-Branch+PR+exakten Remote-Test.
Kein Material-/METHOD-/Projektmodell-Change ohne eigene Autorität.
Nicht automatisch die PR-#327-D-016-Zulassung übernehmen.

Nach jeder technischen Teilkorrektur prüfe das Outcome-Return-Tuple:
Schutzziel, Semantikgrenzen, gekoppelte Pflichten, autorisierte Handlung,
DoR, DoD, Residual/Rückkehrbedingung und Claim Ceiling.
Melde keine Lösung aus lokaler CI; überprüfe das gesamte Resultat.

Die produktive Archivsicherung W3 darf erst nach echter #282-Runtime-/
Zielort-Fitness und validem Erwerbsauftrag ausgeführt und danach exakt
gegen Anbieter-Liste, JPEGs und Manifeste geprüft werden.

Rückgabe: primäre Evidenz, Codeänderungen, exakter Branch/Commit/PR,
Remote-CI, verifiziertes End-to-End-Verhalten, #271/#282/#280-Dispositions-
matrix, bewusst unveränderte Owner und präzise offene Restbedingungen.
```

## 9. Reconciliation / Anti-Flickenteppich-Dispositionsmatrix

| Owner/PR | Disposition durch diesen Plan |
|---|---|
| [#271](https://github.com/esany/paleo-type/issues/271) | **Planung konkretisiert:** DEV-READY-Qualifikations-/Integrationsblock, reale Produktabnahme offen; keine Änderung am Code oder an der Owner-Priorität. |
| [#282](https://github.com/esany/paleo-type/issues/282) | **Unverändert:** produktive Runtime/externes Ziel und ergebnisbezogene Abnahme offen. |
| [#280](https://github.com/esany/paleo-type/issues/280) | **Unverändert:** Whole-System Result Review offen; braucht echten Rücknachweis statt PR-Status. |
| [#297](https://github.com/esany/paleo-type/issues/297) | **Falsifikations-Kriterium angewandt:** ein Teil-PASS ersetzt nicht den Gesamtauftrag; keine Schließung/Abstufung. |
| [PR #327](https://github.com/esany/paleo-type/pull/327) | **Berücksichtigt, nicht übernommen:** paralleler Draft, technische Zulassung/Tests im exakt eigenen Scope; vertikale Akzeptanz offen. |
| [PR #321](https://github.com/esany/paleo-type/pull/321) | **Berücksichtigt:** Phase-A-Eigentümer-/Closure-Strang, nicht automatisch aktueller oder angenommen. |
| [PR #329](https://github.com/esany/paleo-type/pull/329) | Dieser ausgearbeitete Planungskandidat zur Sichtbarkeit und Review; kein Merge und keine unabhängige Review-Rückgabe impliziert. |
| Source/File/Project/METHOD / Wissensarbeit `implementation_allowed` | **Unverändert:** keine Registrierung, keine D-016-Ausweitung, globale Sperre nicht überschrieben. |

**Verbindlicher einziger Ausführungsprompt:** §8 dieser Datei ersetzt die älteren, voneinander abweichenden Ausführungsvorschläge aus `savesax-independent-review-handoff-2026-10-09.md` und `savesax-functional-contract-bug-audit-and-fix-prompt-2026-10-27.md` **für die weitere #271-Implementierung**. Die historischen Analysen behalten ihre Evidenzfunktion, sind aber kein zweiter aktueller Arbeitsplan.

**Stop-/Rückkehrbedingung:** Die Arbeit endet nicht nach einer isolierten Patcherfolgsmeldung. Sie kehrt als nachgewiesene, ganze #271-Lösung mit ausdrücklich separatem #282/#280-Endresultat zurück, oder mit einer präzisen, überprüfbaren einzigen externen Evidenz-/Autoritätsgrenze. Weitere Kommentare/Handoffs ohne neues Material sind kein Fortschritt.
