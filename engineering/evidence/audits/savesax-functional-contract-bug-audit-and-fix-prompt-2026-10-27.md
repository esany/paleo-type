# savesax — funktionaler Systemaudit und ausführbarer Selbst-Reparaturauftrag (2026-10-27)

**Ausführungsstand nach parallelem Review (2026-10-27):** Der in §5 dokumentierte ältere Selbst-Reparaturprompt ist ein historischer Entwurf. **Aktueller, einziger DEV-READY-Ausführungsprompt** für #271 ist §8 in [`savesax-dev-ready-integrated-plan-2026-10-27.md`](savesax-dev-ready-integrated-plan-2026-10-27.md) auf [Draft-PR #329](https://github.com/esany/paleo-type/pull/329). Dieser frühere Audit bleibt als Fehler-/Ursachenbeleg erhalten; er darf die integrierte W0→W3-Reihenfolge und deren Evidenz-Gates nicht überschreiben.


**Status:** nichtnormativer, evidenzbegrenzter technischer/operativer Audit mit konkretem Ausführungsauftrag; **nicht** implementiert, produktiv abgenommen oder unabhängig bestätigt.  
**Kontrollbasis:** `main@256f12bc8894df6fefa7bc8e814e10cc755b9cd4` am 2026-10-27 über autorisierten GitHub-Connector erneut gelesen; Issue #271/#282/#280/#297 offen; Draft-PR #329 offen. Vor jeder späteren Implementierung aktuelle HEAD-/Owner-Version frisch auflösen.  
**Verwandte vorläufige Dokumente:** `savesax-recurrent-source-evidence-drift-audit-2026-10-09.md`; `savesax-independent-review-handoff-2026-10-09.md`. Dieses Dokument ersetzt deren Behauptungen nicht durch neue Quellenbelege.

## 1. Präzises zu schützendes Ergebnis (keine Rückfrage nötig)

Ein Human gibt nur eine reale Archivalien-/Digitalisat-URL. `savesax` stellt selbständig die Identität des Archivobjekts und seine verlinkten tatsächlichen Digitalisatdaten fest, enumeriert **nur real nachgewiesene** Bilddateien, wählt für jeden belegten Eintrag die tatsächlich verfügbare hochauflösende Provider-Repräsentation und bewahrt **alle dadurch belegten und erreichbaren** Bilder ohne Bildverlust in einem kontrollierten **externen** Zielordner auf. Ein-Bild-Archivalie und Mehrbild-Atlas folgen demselben Verfahren. Eine überprüfbare Bildmenge, gültige vollständige Bildbytes, nachvollziehbare Reihenfolge, Quellenidentität, Prüfsummen und wahrhaftiger Fortschritts-/Endstatus sind Pflicht.

**Korrigierter Produktumfang nach Human-Owner-Feedback (2026-10-27):** Gesichert werden die hochauflösenden Bilder, die das Sächsische Staatsarchiv **bereits öffentlich im Web über seine normalen Download-/Fullsize-Adressen bereitstellt und die ein Mensch dort auch manuell herunterladen kann**. `savesax` soll genau diesen manuellen Einzelbild-Download anhand der echten Dateiliste zuverlässig automatisieren. **Keine Masterdatei-Anfrage, keine gesonderte Rechte-/Lizenzprüfung und keine erfundene Zugangshürde als Voraussetzung für diesen normalen Abruf.** Die Archiv-URL und die richtige Quellenangabe werden im Paket dokumentiert. Dass andere, eventuell noch größere Archivreproduktionen auf Anfrage denkbar sind, ist **nicht Teil dieser Aufgabe** und darf die Arbeit weder aufhalten noch mit Prosa überlagern. „Online-Fullsize“ ist kein archivischer Mastertitel; prüfe die tatsächlich geladenen Bildpixel/Bytes, statt die Wortwahl der URL als technischen Qualitätsnachweis zu verwenden. Diese Eingrenzung ist ein Produkt-/Arbeitsumfang, **keine pauschale Aussage über eine weitergehende Veröffentlichungs- oder Verwertungslizenz**.

## 2. Beobachtete und im Code nachgewiesene Fehler

| Ebene | Befund | Sicherheit | Erforderliche Korrektureigenschaft |
|---|---|---|---|
| Dialog/Evidenz | Der Assistent produzierte für GUID `112bd5fe-72e0-4694-9507-34a896b4583b` Links `0002.jpg` und `0003.jpg`, ohne eine Dateiliste zu lesen; der Human gab eine Ein-Bild-Quelle an. | **BELEGTES Chat-Verhalten**; unabhängige Ein-Bild-Quellenprüfung **OFFEN** | URL-Muster nie als Existenz-/Vollständigkeitsbeleg; kein Beispielbild als konkretes Fundstück ohne primären Dateieintrag und Verfügbarkeitsprüfung. |
| Assistenz / Regelwirksamkeit | Die bestehende `.agents/skills/savesax/SKILL.md` enthält „Never fabricate a sequence from an image count“. Trotz Regel trat genau das Gegenteil ein. | **BELEGT** | End-to-End-Fresh-Context-/Interaktionstest statt bloß weitere Prosa. |
| Providerparser | `SaechsischesStaatsarchivProvider.plan()` in `tools/archival_source_acquisition.py` lehnt jedes Objekt mit `typ != "jpg"` **oder** `istEinzelbild is not True` mit Exception ab; es wird nicht automatisch nur der Eintrag übersprungen. | **CODE-BEFUND BELEGT** | Semantik `false` zuerst an echten Providerantworten ermitteln; gültige JPGs nicht allein aufgrund unzureichend verstandenen Flags ausschließen; unbekannte Varianten sichtbar und sicher behandeln. |
| Quellen-/GUID-Identität | Tool übernimmt `source.guid` aus angelieferter Metadatenstruktur als Digitalisat-GUID und fragt `/digitalisate/<guid>/files.json`. Die CLI benötigt derzeit sieben Pflicht-Metadatenfelder; aus der URL wird dies nicht intern vollständig aufgelöst. | **CODE-BEFUND BELEGT**; Identität der zwei konkreten Archiv-/Digitalisat-GUIDs **OFFEN** | Natürlicher URL-Einstieg ohne erfundene Katalogdaten oder manuellen Provider-Workflow; Identität prüfbar. |
| Reihenfolge/Vollständigkeit | `plan()` sortiert aus `name + ".jpg"` konstruierte Dateinamen lexikografisch; `source.image_count` (auch extern übernommener Wert) dient als harte Konsistenzprüfung, falls ungleich 0. | **CODE-BEFUND BELEGT**; Fehlreihenfolge konkreter Objekte **NICHT BELEGT** | Aus Providerdaten rekonstruierbare Originalreihenfolge dokumentieren; Zählwert nicht zur Dateigenerierung verwenden; Herkunft/Verbindlichkeit eines Kontrollzählwerts unterscheiden. |
| Bildintegrität | `_inspect_jpeg()` ruft `jpeg_dimensions()` auf; die Funktion liest JPEG-Anfang und SOF-Abmessungen und gibt ohne Endmarker-/vollständige JPEG-Dekodierprüfung zurück. Der Test nutzt `JPEG_32X16` als stark verkürzte synthetische Markersequenz. SHA-256 schützt nur die **bereits geladenen** Bytes, nicht die Vollständigkeit gegenüber dem echten entfernten Bild. | **CODE-BEFUND BELEGT** | Unterschied zwischen Marker-/Dimensions-Plausibilität, vollständiger JPEG-Dekodierbarkeit und Vollständigkeit gegen einen Provider-Referenzwert explizit prüfen. Fehlende Referenzgrenze offenlegen. |
| Auflösung/Route | CLI-Default ist `--route download`; `fullsize` ist wählbar, aber die Logik misst vor der Routewahl keinen Auflösungs-/Inhaltsvergleich. | **CODE-BEFUND BELEGT**; tatsächlicher Qualitätsunterschied der Endpunkte **OFFEN** | Begrenzte repräsentative Direktprüfung, danach evidenzbasiert richtige Route für öffentliches hochauflösendes Ergebnis. |
| Endstatus | PR #328 hat `ACQUISITION_STATE.json.status=complete` hinter Paketmanifeste verlegt; Tests für Finalisierung/Resume liegen auf `main`. | **IMPLEMENTIERT / DETERMINISTISCH GEPRÜFT**, kein Paketnachweis | Lösung erhalten; nicht als Ersatz für volle Paketabnahme präsentieren. |
| Produktiver Speicher | #271/#282 führen komplette verifizierte externe Sicherung weiterhin als offen. | **GEMÄSS AKTUELLEN OWNER-ISSUES OFFEN** | Erst nach Kontrolle von externem Ziel, Persistenz, Wiederanlauf, Steuerbarkeit und ausdrücklicher Erwerbsautorität realen Lauf starten. |

## 3. Ursache statt Symptombehandlung

**R1 (demonstriert):** Syntaktische URL-Generierbarkeit wurde in der Assistenz in Quellenexistenz überführt. Die fehlende primäre Dateiliste wurde nicht als epistemische Sperre behandelt. **Dies ist nicht identisch mit R2.**

**R2 (Code nachgewiesen, Live-Auswirkung offen):** Ein Provider-Metadatenflag wurde als harter Typ-/Existenzfilter kodiert, obwohl seine tatsächliche Bildrouten-Semantik für `false` nicht geklärt ist. Eine blinde Entfernung kann Tile-/Manifest-Daten fälschlich als Einzel-JPEGs behandeln. Die Heilung braucht Gegenbeispiele mit echten gelisteten Dateinamen und echten Antwortbytes.

**R3 (weiterer Produktmangel im Code):** „JPEG-Datei gültig“ und „wirklich vollständig dekodierbares JPEG“ werden vermischt; Hashes belegen die Gleichheit zu heruntergeladenen Bytes, nicht zwingend ihre vollständige Lieferung durch den Webserver. Eine brauchbare Prüfung muss technisch beschädigte/abgeschnittene Bilder erkennen und die tatsächlich öffentlich gelieferte Auflösung festhalten; **keine Debatte über zusätzliche Archivmaster als Ersatz für den Download**.

**R4 (systemisch):** Das Gesamtziel `Archiv-URL → belegte Daten → vollständiges externes Paket` wurde in lokal unabhängige technische Erfolge zerlegt; die durch den Human schon mehrfach korrigierte falsche-Lean-/lokaler-PASS-Verschiebung ist bei #297 als Risiko bereits beschrieben. Zusätzliche Prompt-Sätze allein sind kein Wirksamkeitsnachweis.

## 4. Noch offene entscheidende Primärbelege

- **Atlas:** `c52a0351-970a-4896-a349-918c35636cfc`. Die früher genannten „240 / 163 true / 77 false“ sind **unbestätigte Hypothesen**, keine abgenommene Dateiliste.
- **Vergleichsarchivalie:** Katalogseite `https://www.archiv.sachsen.de/archiv/bestand.jsp?guid=112bd5fe-72e0-4694-9507-34a896b4583b`; der Human berichtet genau ein Bild; die GUID-Gleichheit zum Digitalisatpfad und tatsächliche `files.json`-Einträge sind unabhängig zu prüfen.
- Direkte Abrufe von beiden `files.json`-Adressen und der Vergleichs-Katalogseite waren mit dem hier verfügbaren Webabruf **nicht möglich**; das ist eine lokale Tool-Grenze, **kein Provider-Ausfall**.
- Keine automatische Mehrbildbehauptung bis zur Quellevidenz. Online abrufbare Fullsize-Bilder sind der konkrete Erwerbsgegenstand; höher aufgelöste Sonderanfertigungen auf Anfrage und allgemeine Lizenzfragen sind kein vorgeschalteter Task.

## 5. Ausführbarer Prompt an denselben künftigen Reparaturkontext

~~~text
AUFTRAG: SAVESAX ALS KOHÄRENTE QUELLENBASIERTE FUNKTION REPARIEREN UND WIRKSAMKEIT BELEGEN

Du reparierst esany/paleo-type/.agents/skills/savesax plus den vorhandenen
tools/archival_source_acquisition.py und dessen Tests, soweit die Reparatur
dies tatsächlich benötigt. Du bist verantwortlich für das Ergebnis, nicht
für die Verteidigung der bisherigen Architektur und nicht für kosmetische
Issue-/Test-Erfolge.

1. Beginne mit dem HUMAN OUTCOME:
   Eine Archiv-URL -> echte Katalog-/Digitalisatidentität -> echte gelistete
   Bilddateien -> beste unterstützte öffentlich zugängliche hochaufgelöste
   Bildbytes -> kontrollierte externe vollständige und integritätsgeprüfte
   Sicherung -> wahrhaftiger Human-Status. Eine Quelle mit exakt einem
   belegten Bild erzeugt einen Einbild-Plan, eine Mehrbildquelle nur die
   tatsächlich belegten Dateien. Keine aus N oder Mustern erfundenen Namen.

2. Frisch rehydrieren: GOVERNING_OBJECTIVE.md, AGENTS.md, #271, #282,
   #280, #297, methodology/workflow.md, methodology/maintenance.md,
   .agents/skills/savesax/SKILL.md, tools/archival_source_acquisition.py,
   tests/test_archival_source_acquisition.py, docs/archival-source-acquisition.md
   und aktuelle HEAD-/PRs. Repository nur über GitHub-Connector; kein
   lokaler Checkout, Git/HTTP-Surrogat, Slack-Zustand oder Chat-Memory als
   Autorität. Prüfe aktuellen Implementierungs- und Abnahmestand neu.

3. Bevor du Providerlogik änderst: offizielle Identität und wirkliche
   files.json beider Testquellen nachweislich lesen. Atlas:
   c52a0351-970a-4896-a349-918c35636cfc. Zweite offizielle
   Katalog-GUID: 112bd5fe-72e0-4694-9507-34a896b4583b;
   prüfe explizit die Digitalisat-GUID-Verknüpfung. Pro Fall echte
   Eintragsanzahl, Name, Typ, istEinzelbild, Dubletten und Ordnung.
   240/163/77 und „nur ein Bild“ gelten vor unabhängiger Datenprüfung
   als berichtete, nicht selbst bewiesene Hypothesen.

4. Führe nur wenige begrenzte Live-Proben aus, zunächst ohne Bulk-
   Download. Teste ausschließlich tatsächlich gelistete JPG-Namen
   über /fullsize/<exakter Name> und gegebenenfalls download.jsp.
   Vergleiche true/false, sofern vorhanden; HTTP-Status, Redirect,
   Inhaltstyp, Byteumfang, vollständige JPEG-Dekodierung,
   Pixelabmessungen sowie Route. Ein bloß konstruiertes URL-Muster,
   Browser-Sichtbarkeit oder frühere Chat-Aussage ist kein Nachweis.
   Wenn Providerzugriff in dieser Ausführung fehlt, benenne genaue
   Grenze und teste offline gegen belegte Fixtures; ändere die
   Feldsemantik nicht auf Verdacht. Keine teuren Browseragenten ohne
   gesonderte Human-Erlaubnis.

5. Diagnostiziere vollständig:
   a) unbelegte Bildfolgen in der Assistenz trotz Skill-Verbot;
   b) istEinzelbild=true als harter Planungsfilter;
   c) GUID-/Katalogauflösung und sieben-Metadatenfelder-CLI vs.
      menschenverständliche Archiv-URL-Eingabe;
   d) tatsächliche Bildreihenfolge, Typ-/Namensvalidierung und
      optionale count-Konsistenz;
   e) fehlende vollständige JPEG-Prüfung (SOF allein genügt nicht);
   f) Beleg für die gewählte Web-Fullsize-/Download-Route und
      die tatsächlich gelieferten Pixel/Bytes; **keine** Anfragen
      nach Sonder-Masterdateien und **keine** Lizenzdebatte als
      Voraussetzung für öffentlich angebotene manuelle Downloads;
   g) Ende-zu-Ende-Zustand bis zur vollständig gesicherten externen Ablage.
   Die nachgewiesene Archivquelle im Paket korrekt ausweisen;
   keine ungeprüften Aussagen über weitergehende Nutzungsrechte.

6. Entwirf den kleinsten HINREICHENDEN kohärenten Fix. Behalte
   nachgewiesen funktionierende Restart-/Checksum-/Paketmechanik bei,
   aber lass bestehende Architektur und Scope-Floskeln nicht den
   vollständigen Funktionsvertrag ersetzen. Ändere keine unbekannten
   Providerformate blind: valide Bilder berücksichtigen; tatsächlich
   nicht unterstützte Typen sichtbar und wahrheitsgemäß behandeln.
   Kein neues Universalarchivsystem, kein Job-/Workflow-Framework,
   keine automatische CORPUS- oder Project-Mutation.

7. Implementiere nach Datenbelegen innerhalb des bereits zugelassenen
   #271-Scopes über autorisierten GitHub-Branch/PR. Wenn ein neuer
   wesentlicher Architektur-/METHOD-Entscheid unvermeidbar wäre:
   präzise den Entscheidpunkt melden, nicht still admission fingieren.
   Füge diskriminierende Tests hinzu:
   - Einbildquelle: genau eine reale Datei, nie 0002/0003 erfunden;
   - Mehrbildquelle mit konkreten, nicht zwingend fortlaufenden Namen;
   - gemischte istEinzelbild true/false, mit datenbegründetem Verhalten;
   - nicht-JPEG/Tile/fehlende Daten, Duplikate, falsche GUID;
   - unvollständiges/korruptes JPEG trotz vorhandenen SOF-Markers;
   - Route/Auflösung/HTTP-Fehlerfälle und keine stille Auslassung;
   - Restart/Cancel, Sidecar-Schreibfehler, Checksum, read-only Status;
   - fresh-context/natürlicher savesax-Aufruf mit nur einer Archiv-URL.

8. Abnahme nur am Human Outcome:
   Der Plan enthält ausschließlich und vollständig die belegten,
   nachweislich zugänglichen Einzelbilder. Die technische Menge
   stimmt zur belegten Quelldatenbasis; alle Bildbytes sind valide;
   Auflösung/Route ist dokumentiert; externe Paketdateien, Hashes
   und Status sind stimmig. Die Einbildquelle und der Atlas bestehen
   denselben Weg. Produktive Langläufe nur nach kontrolliertem
   externem Ziel/Laufzeit-Fitness #282; kein CI-/Sandbox-Artefakt als
   dauerhafte Sicherung behaupten. Ein grüner CI-Lauf ist nur
   technischer PASS; ohne Realpaket bleibt Produktabnahme OFFEN.

9. Ergebnis zurückgeben: Was wurde real beobachtet? Welche Fehler
   reproduziert? Was geändert und auf welchem GitHub-Commit/PR
   nachweislich gespeichert? Welche Tests exakt bestanden? Welche
   Live-/Produktivprüfung offen? Welcher Betrag an Dateien ist
   wirklich vollständig an welchem externen Ziel gesichert?
   Rückmeldung an #271/#282/#280 und ggf. #297 nur nach
   zutreffender Owner-Dispositionsprüfung; keinen Status hochstufen.
   Keine selbstgenerierenden Chat-Handoff-/Slack-Schleifen.
~~~

## 6. Abschlussgrenzen dieses Audits

**Audit-Befund:** Gesprächsfehler sicher belegt; harte Providerfilterung, fehlende vollständige JPEG-Dekodierung, fehlende belegte Route-/Auflösungsvergleichsprüfung im Code sicher sichtbar; providerseitige Bedeutung von `false` und tatsächliche Live-Auswirkungen ungeprüft.

**Implementierung in diesem Block:** keine Codeänderung, keine CI-Ausführung, keine externe Archivspeicherung. **Offener nächster ausführbarer Arbeitsblock:** datenbasierte, zusammenhängende Reparatur unter #271 mit separatem produktivem #282-End-to-End-Nachweis. Kein autonomer zweiter Chat wurde gestartet und keine Slack-Übergabe behauptet.

**Involvierte Owner unverändert:** #271 Arbeit/Produkt und Paketergebnis offen; #282 Runtime-/Außenspeicherabnahme offen; #280 Gesamt-Result-Review offen; #297 mögliche operative Wiederholung; keine neue Issue-Priorität, METHOD-, Source-, File-, Project- oder D-016-Änderung.
