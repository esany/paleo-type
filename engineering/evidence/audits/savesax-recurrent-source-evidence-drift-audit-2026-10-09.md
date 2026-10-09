# savesax — erneutes Fehlerbild: vermutete Bildfolge statt Quellenbeleg (2026-10-09)

**Status:** nichtnormativer Real-use-Fehlerbefund, keine Produktabnahme, keine Implementierungsfreigabe und keine neue Forschungspriorität.  
**Ausführung:** Quellen-/Systemanalyse, nicht erneute Codeentwicklung.  
**Geltende Repository-Basis:** `main@256f12bc8894df6fefa7bc8e814e10cc755b9cd4` (vor dieser Dokumentation).  
**Natürliche Arbeitseigentümer:** [#271](https://github.com/esany/paleo-type/issues/271) für `savesax`/Quellenpaket, [#282](https://github.com/esany/paleo-type/issues/282) für den realen produktiven Lauf, [#280](https://github.com/esany/paleo-type/issues/280) für End-to-End-Result-Review. Die bereits bestehende operative Wirksamkeitsproblematik ist mit [#297](https://github.com/esany/paleo-type/issues/297) und Audit [ENG-A-0118](bug-intent-root-cause-wirknetz-plan-fit-audit-2026-10-07.md) verwandt, wird dadurch aber nicht automatisch umpriorisiert oder umdefiniert.

## 1. Von der Human-Anforderung her

Erfolg heißt: Eine vorgegebene Sächsisches-Staatsarchiv-Archivalie wird über ihre echten Katalog-/Digitalisatdaten erschlossen; **jedes belegte und tatsächlich verfügbare hochauflösende Bild** wird verlustfrei, nachvollziehbar und dauerhaft an einen kontrollierten externen Zielort gesichert, mit Integritätsprüfung und wahrheitsgemäßem Abschluss. Eine Einzelbildquelle und ein umfangreicher Atlas dürfen keine verschiedenen improvisierten Verfahren erfordern.

Ein syntaktisch plausibler Link, eine geschätzte Anzahl, ein grüner CI-Lauf oder eine Codekorrektur sind **kein** Nachweis dieses Ergebnisses.

## 2. Anlass und belegte Beobachtungen — Ebenen bewusst getrennt

**Konversationsbeobachtung:** Als zweite unabhängige Testarchivalie nannte der Human Owner
`https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=112bd5fe-72e0-4694-9507-34a896b4583b&...#archivalie`.
Der Assistent setzte diese GUID ohne nachgewiesene `files.json`-Antwort in `/digitalisate/<GUID>/fullsize/` ein und präsentierte `0001.jpg`, `0002.jpg` und `0003.jpg` als Bildlinks. Der Human Owner stellte klar: „die Quelle besteht nur aus einem bild, wie kommst du auf 3 - hast du das nicht geprüft“. Der Assistent räumte ein, die Anzahl nicht geprüft zu haben.

**Evidenzgrenze:** Der Human Owner hat die Ein-Bild-Eigenschaft berichtet. Sie ist hier **nicht** durch eine unabhängig gelesene `files.json` oder archivseitige Bestands-/Digitalisatmetadaten technisch nachgewiesen. Auch der im Browser geöffnete `0001.jpg`-Link ist kein protokollierter HTTP-/JPEG-Integritätstest. Es ist **nicht** festgestellt, ob `0002.jpg` und `0003.jpg` HTTP-404 liefern; ihr Status ist unbekannt. Das Fehlerhafte ist bereits die unbelegte Behauptung einer Bildfolge.

**Wiederholung:** Für den Schenk'schen Atlas (`c52a0351-970a-4896-a349-918c35636cfc`) hatte der Assistent zuvor die Bilder `0001.jpg`, `0002.jpg`, `0003.jpg`, `0240.jpg` aus GUID und vermeintlicher Anzahl illustriert, ebenfalls ohne nachgewiesene vollständige Dateiliste. Die aus früherer Arbeit gemeldeten 240 bzw. 163/77 Einträge sind in dieser Konversation **nicht unabhängig nachverifiziert**.

**Repository-Fakt:** `.agents/skills/savesax/SKILL.md` verlangt bereits ausdrücklich `files.json` statt aus Zählungen erfundener Sequenzen: „Never fabricate a sequence from an image count.“ Die neue Halluzination ist deshalb **eine reale Ausführungs-/Evidenzdisziplin-Regression trotz vorhandener Regel**; es fehlt nicht nur eine weitere Skill-Anweisung.

**Separater Implementierungsbefund:** In `tools/archival_source_acquisition.py`, `SStaAdapter.plan()`, verlangt der aktuelle Adapter `typ == "jpg"` und `entry["istEinzelbild"] is True`. Das kann `jpg`-Einträge mit `istEinzelbild=false` aus dem Plan ausschließen bzw. die gesamte Liste ablehnen. Ob diese Einträge über `fullsize/<tatsächlicher Name>.jpg` vollwertige JPEGs liefern, ist **offen** und verlangt einen begrenzten direkten Provider-Test. Ebenso offen: ob Archivseiten-GUID und Digitalisat-GUID bei jeder Probe identisch sind.

**Bereits behobener, aber anderer Implementierungsfehler:** PR [#328](https://github.com/esany/paleo-type/pull/328), auf `main` als `256f12bc...`, verschob das Fortschritts-`complete` hinter die Paket-Manifeste. Der berichtete CI-Erfolg belegt die getestete Finalisierungssemantik, nicht die tatsächliche Bilderschließung oder produktive Speicherung.

## 3. Ursachenkette / Wirknetz

```text
Human Outcome: alle belegten verfügbaren Originalbilder einer konkreten Archivalie sichern
  -> Assistent orientiert sich an sichtbarem URL-Muster / internem Adapter / isolierten Bugs
  -> verwechselt syntaktisch konstruierbare Adresse mit archivalisch belegtem Bild
  -> ergänzt 0002/0003 beziehungsweise 0240 aus ungesicherter Sequenzannahme
  -> zeigt unbelegte Beispiele als konkreten Quellenumfang
  -> Human muss elementare Quellen-/Vollständigkeitskontrolle selbst übernehmen
  -> lokale Fehlerbehebung/technischer PASS verdrängen erneut das End-to-End-Produktziel
```

**Mechanismus A — Evidenzüberschreitung im Dialog (belegt):** Eine leicht erzeugbare URL wird als Dateiidentität präsentiert, ohne die tatsächliche Quelle zu lesen. Fehlende Dateilisten-/HTTP-Evidenz wird nicht konsequent als Grenze der Behauptung behandelt. Die Wiederholung trotz expliziter Skill-Regel spricht für unzureichende operative Anwendung und fehlende Wirksamkeitskontrolle, nicht für einen allein durch weiteres Prompt-Prosa heilbaren Syntaxfehler.

**Mechanismus B — mögliche semantische Fehlklassifikation im Adapter (im Code belegt, Wirkung offen):** Das Flag `istEinzelbild` ist gegenwärtig eine harte Abbruchbedingung. Die tatsächliche Bedeutung des Feldes und das Vorhandensein valider Fullsize-JPEGs bei `false` wurden für den Atlas in dieser Sitzung nicht direkt festgestellt. Eine pauschale Entfernung der Typ-/Sicherheitskontrollen wäre ebenso unbegründet wie die unveränderte Annahme, `false` bedeute kein Bild.

**Mechanismus C — falsche Arbeitsteilung (belegt im Verlauf):** Ein echter Finalisierungsfehler wurde isoliert gelöst, während die zentrale providerseitige Erschließung offen blieb. Ein lokaler PASS wurde zwar später korrekt begrenzt, dennoch dominierte Reparaturarbeit ohne frühzeitigen ganzheitlichen Ertragsnachweis. Das entspricht dem bei #297 dokumentierten Risiko „local PASS / false Lean statt kohärentem Human Outcome“, ohne diese Einzelbeobachtung bereits als generische Lösung zu zertifizieren.

## 4. Diskriminierende Prüfung vor weiterer Implementierung

1. **Objektidentität:** Für beide Archiv-URLs offiziellen Katalogeintrag, tatsächliche Digitalisat-GUID und verknüpfte `files.json` belegen; eine Bestand-GUID darf nicht ohne Prüfung mit der Digitalisat-GUID gleichgesetzt werden.
2. **Listenwahrheit:** Jede `files.json` tatsächlich lesen, Form und `name/typ/istEinzelbild` zählen, konkrete Dateinamen belegen, Dubletten/sonstige Typen darstellen. Kein Hochzählen bis zu einer angenommenen Menge.
3. **Begrenzte Antwortprüfung:** Bei geeigneten, tatsächlich gelisteten Namen wenige repräsentative `fullsize`-/`download.jsp`-Abrufe (einschließlich `istEinzelbild=false`, sofern vorhanden) auf Status, Typ, JPEG-Daten und Abmessungen prüfen; kein Massendownload. Auch einen negativen oder fehlenden Namen als Kontrolle testen, soweit providerverträglich.
4. **End-to-End-Modell:** Eine Einzelbildquelle und eine Mehrbildquelle durch denselben realen Planungspfad führen; nachweisen, dass keine nicht gelisteten Namen entstehen und keine verfügbaren JPEGs unbemerkt ausgeschlossen werden. Daten-, UI- und Speicherprobleme getrennt bewerten.
5. **Produktabnahme abgrenzen:** Vor produktivem Langlauf externes Ziel und Laufzeit-Fitness gemäß #282 vorprüfen; erst danach separater, ausdrücklich autorisierter und beobachtbarer Erwerb plus Manifest-/Checksum-Nachweis. Keine produktive Sicherung durch diesen Auditauftrag.

Wenn der direkte Providerzugriff fehlt, **genau diese Evidenzgrenze dokumentieren und keinen Datenbefund fingieren**. Eine unabhängige Review-Sitzung ist nur dann epistemisch unabhängig, wenn sie primäre Providerdaten und echten Repository-Code prüft, statt unsere Chat- oder Issue-Erzählung zu übernehmen.

## 5. Resultat-/Owner-Dispositionsgrenze

- **#271:** Bedarf an quellenbasierter Erschließungsprüfung belegt; Produktabnahme bleibt offen. Keine Codeänderung durch diesen Befund.
- **#282:** unverändert offen für kontrolliertes externes Ziellaufzeit-/Paket-Ergebnis.
- **#280:** End-to-End-Akzeptanz noch nicht erfüllt; auditierbarer zusätzlicher Real-use-Befund, keine automatische neue Entscheidung.
- **#297 / #272:** mögliches zusätzliches empirisches Material zur operativen Wirksamkeit/Plan-Fit; keine Prioritäts-, Status- oder Closure-Änderung durch dieses Dokument.
- **Source / File / Project / METHOD / Koordinationspolitik:** unverändert. Kein neuer `NEXT ACTION`, keine D-016-Freigabe.

Die unabhängige Erstprüfung wird mit dem getrennten neutral formulierten Handoff `savesax-independent-review-handoff-2026-10-09.md` beauftragt; ihr Ergebnis ist **noch nicht eingegangen**. Ein Bericht muss die hier beschriebenen Behauptungen ausdrücklich selbst falsifizieren dürfen und darf diese Notiz nicht als Quelle technischer Live-Wahrheit verwenden.
