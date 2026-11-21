# paleo-type

Schlanke, belegorientierte Arbeitsumgebung für nachvollziehbare Transkription, Quellenkritik und wissenschaftliche Auswertung frühneuzeitlicher Handschriften.

## Zweck

Oberster Zweck, Rangfolge und die Änderungsbefugnis des Eigentümers stehen an genau einer Stelle: `GOVERNING_OBJECTIVE.md`.

Diese README ist die **Orientierungs- und Leseweg-Ansicht** des Repos. Sie ist kein zweites Methodenhandbuch, kein Speicher für Projektstände und kein ausführbarer Vertrag. Das Produkt sind die Quellen und das wissenschaftliche Ergebnis; Software, KI, GitHub und Arbeitsformate sind Hilfsmittel.

Die wörtlichen Aussagen des Eigentümers stehen gesammelt in [`docs/o-toene.md`](docs/o-toene.md), getrennt von allem KI-Text.

## Aktuelle Lage

Stand: 21.11.2026. Hier stehen nur Hinweise, wo der jeweilige Stand liegt; der Stand selbst steht bei seinem Eigentümer.

- **Aktives Projekt:** `projects/ssta-20578-nr-632/` (Sächsisches Staatsarchiv, 20578, Nr. 632), laut [`SPICKZETTEL.md`](SPICKZETTEL.md).
- **Forschungspause:** Die Forschung an Nr. 632 ruht seit dem 03.11.2026; der Eigentümer hat das am 14.11.2026 bestätigt. Maßgeblich ist Issue [#399](https://github.com/esany/paleo-type/issues/399). Seit dem 21.11.2026 gilt eine einzige Ausnahme: ein Durchgang am Gesuch 0104R–0107L. Was dazu gehört, steht in [#399](https://github.com/esany/paleo-type/issues/399#issuecomment-7066954647). Ganz endet die Pause erst durch Entscheidung des Eigentümers.
- **Wo die Forschung zu Nr. 632 liegt:** nicht auf `main`, sondern auf dem Branch `research/nr632-transcription-t0-t1-20261030` (Entwurfs-PR [#359](https://github.com/esany/paleo-type/pull/359)). Der Rückkehrpunkt ist die dortige `projects/ssta-20578-nr-632/STATUS.md`. Die gleichnamige Datei auf `main` ist vom 30.10.2026 und nicht der aktuelle Stand. Die Vorab-Gegenlesung liegt auf dem Branch `review/nr632-gegenlesung-vorab`.
- **Prüfung des Gesamtsystems:** Am 21.11.2026 hat der Eigentümer entschieden: reparieren statt neu starten (D-022 in `DECISIONS.md`). Grundlage ist `engineering/evidence/audits/zweck-und-zielbild-2026-11-21-fassung-2.md`. Die Audit-Kette ([#398](https://github.com/esany/paleo-type/issues/398), [#405](https://github.com/esany/paleo-type/issues/405), [#411](https://github.com/esany/paleo-type/issues/411)–[#413](https://github.com/esany/paleo-type/issues/413) und die Entwurfs-PRs #401, #402, #408, #409, #414) ist auf seine Entscheidung hin beendet: geschlossen, nicht abgenommen, die Branches als `archiv/…` gesichert. Jeder einzelne Reparaturschritt braucht weiter seine Freigabe. Die Ursachenanalyse der bekannten Bugs (Warum-Ketten, Hypothese) steht in `engineering/evidence/audits/warum-ketten-bekannte-bugs-2026-11-21.md`.
- **Systementwicklung:** Das Vorhaben SD-KA-01 ist abgeschlossen. Laut `engineering/configuration.json` gibt es keinen aktuellen Engineering-Fokus und keine laufende Änderung.
- **Übergabestand des Prüfchats:** das offene Issue mit Label `uebergabe` ([#368](https://github.com/esany/paleo-type/issues/368)), jüngster Kommentar.

## Schichten des Repos

- **METHODE** — `methodology/`, `AGENTS.md`, `DECISIONS.md`, `templates/`: wiederverwendbare wissenschaftliche und operative Regeln, Begründungen der Steuerung und Vorlagen.
- **ANFORDERUNGEN** — `requirements/`: angenommene wiederverwendbare Anforderungs-Baselines und Navigation. Historische Engineering-Belege liegen seit WP5 nicht mehr hier.
- **ENGINEERING** — `engineering/`: Engineering-Konfiguration, begrenzte Änderungen, ADRs, Absicherung, Kataloge sowie Engineering-Belege und -Geschichte.
- **CORPUS** — `corpus/`, `entities/`: kanonische Identität von Quelle und Datei, wiederverwendbare quellenweite Zuordnungen, belegte Beziehungen und normalisierte Entitäten.
- **QUELLENEINGANG** — `source-entry/`: angenommene, nur fortgeschriebene Eingangsgeschichte von Quellen sowie feingranularer Stand von Sichtung und Abdeckung. Verweist auf Corpus-Identität und optional auf ein Projekt, besitzt aber weder Projektzweck noch wissenschaftlichen Umfang, Gates oder `NEXT ACTION`.
- **PROJEKT** — `projects/<id>/`: dauerhafter wissenschaftlicher Stand einer Untersuchung, die aus einem Forschungszweck eingerichtet wurde: Quellennutzung, Belegbindung, Transkription und Auswertung sowie aktueller Forschungsstand.

Ob ein Projekt existiert und welchen Vorrang es hat, wird nie aus der Struktur von Quellen und Dateien oder aus dem Engineering-Stand abgeleitet. Die genaue Bedeutung steht in der zuständigen Methodikdatei und in den Projektdateien.

## Hier anfangen

### Mensch

0. **Bedienung, Stichworte und Prompts: [`SPICKZETTEL.md`](SPICKZETTEL.md).**
1. Diese README zur Orientierung lesen.
2. `GOVERNING_OBJECTIVE.md` für Zweck, Rangfolge und Befugnis des Eigentümers.
3. Die `project.yml` des Projekts für Zweck, Umfang und dokumentarischen Anker.
4. Dessen `STATUS.md` für den tatsächlichen Stand von Gates, Belegen und Wiedereinstieg, und für die freigegebene `NEXT ACTION`, wenn es eine gibt.
5. `source-uses.tsv` und `research/use-evidence.tsv` des Projekts, wenn es darum geht, wie das Projekt Quellen nutzt und welche Datei etwas belegt.
6. Für die konkrete Frage der zuständigen Methodikdatei folgen.

### KI / ausführender Agent

1. `GOVERNING_OBJECTIVE.md` und `AGENTS.md` lesen;
2. den einschlägigen kanonischen Stand von Projekt, Corpus oder Engineering lesen;
3. jede für die konkrete Aufgabe geltende kanonische Regel und Anforderung ermitteln und laden;
4. vorhandene erzeugte Kontexte und Resolver nutzen, statt Struktur oder Vorrang aus Namen oder Chat zu rekonstruieren;
5. nur von einer freigegebenen Aufgabe oder `NEXT ACTION` aus weiterarbeiten, wenn es eine gibt.

Alter Chat darf nie nötig sein, um den dauerhaften Forschungs- oder Engineering-Stand zu rekonstruieren.

## Navigation zur Systementwicklung

Die für Menschen sichtbare Arbeits- und Entscheidungsansicht der Systementwicklung war GitHub **#244**. Die Umsetzung von SD-KA-01 war unter der dokumentierten D-016-Freigabe in **#256–#261** gegliedert.

Kanonische Eigentümer:

- `engineering/configuration.json` — angenommene Baselines, laufende Änderung, ausdrücklicher aktueller Fokus oder dessen Fehlen, Herkunft der Übergänge;
- `engineering/changes/SD-KA-01/STATE.json` — Lebenszyklus der begrenzten Änderung und ihrer Arbeitspakete;
- `engineering/changes/SD-KA-01/RESULT.md` — Ergebnisse der abgeschlossenen Arbeitspakete und Rückmeldungen an das Gesamtsystem;
- `engineering/changes/SD-KA-01/D016-DECISION-BRIEF.md` und `D016-OWNER-ADMISSION.md` — freigegebenes Ziel, freigegebener Umfang und Freigabe durch den Eigentümer;
- `engineering/catalog/` — verwaltete Identitäten, Befunde, Abdeckung, Beziehungen und Kontinuität alter Pfade;
- `engineering/changes/SD-KA-01/MIGRATION.tsv` — Einordnung der WP5-Migration, exakte Blob-Identität vor dem Verschieben und Rückweg.

Prozessstand von SD-KA-01:

> **WP1–WP6 verifiziert / abschließende Ergebnisprüfung angenommen / Engineering-Baseline aktualisiert / keine SD-KA-Arbeit aktuell.**

SD-KA-01 ist abgeschlossen. Die abschließende Ergebnisprüfung hat ADR-0001 / `artifact:ENG-A-0031` nach genauer Qualifizierung als Engineering-Architektur-Baseline angenommen; die angenommene wiederverwendbare Anforderungs-Baseline bleibt `artifact:ENG-A-0008`. Es gibt keinen SD-KA-Fokus und keine automatisch erzeugte Folgearbeit. Ausdrücklich außerhalb dieser Engineering-Abnahme bleiben: F10 (Unabhängigkeit von Belegen), F17/#225 (wissenschaftliche Abnahme von Anfang bis Ende) sowie Aussagen über externe Laufzeitumgebungen und Fachprüfung.

Eine erzeugte, für Menschen lesbare Darstellung desselben Stands liefert:

`python tools/engineering_context.py --profile human-system-overview --format text`

Ein allgemeiner Aufruf kann kontextabhängig aktuelle oder nächste Arbeit ermitteln; das sichtbare Ergebnis muss aber eine sinnvolle Handlung mit Umfang und Herkunft bleiben. Mehrdeutigkeit wird offengelegt und nicht stillschweigend auf einen einzigen repoweiten Arbeitsstand verengt.

## Informationsarchitektur nach WP5

`requirements/` ist jetzt bewusst schmal: `README.md` und die angenommene wiederverwendbare Baseline `domain-requirements.tsv`. Der frühere gemischte Engineering-Bestand ist zu seinen inhaltlichen Eigentümern umgezogen, ohne dass sich Befugnis oder Aktualität geändert haben:

- Belege der begrenzten Änderung SD-KA: `engineering/changes/SD-KA-01/`;
- Architekturbegründungen: `engineering/decisions/`;
- projektübergreifende Entscheidungs- und Freigabebelege des Eigentümers: `engineering/evidence/decisions/`;
- Audits und Prüfungen: `engineering/evidence/audits/`;
- Recherche-, Entwurfs- und Problembelege: `engineering/evidence/research/`;
- Lernen: `engineering/evidence/learning/`;
- historische Arbeitsanweisungen und Prompts: `engineering/evidence/work-instructions/`;
- als Beleg aufbewahrte Koordinationsgeschichte: `engineering/evidence/coordination/`.

Verschobene verwaltete Artefakte behalten ihre stabile `ENG-A-*`-Identität. `engineering/catalog/legacy-paths.tsv` löst frühere Pfade auf; diese Fundstellen dienen nur der Kompatibilität und Navigation und sind keine zweiten Wahrheitsspeicher. `engineering/changes/SD-KA-01/MIGRATION.tsv` hält die drei begrenzten WP5-Migrationsschritte und die exakten Blob-Identitäten vor dem Verschieben fest.

Vor tieferen historischen Belegen sind die aktuellen Eigentümer für Engineering-Konfiguration, Kontext und Ergebnis zu lesen. Historische Belege werden bei Bedarf geladen und gehören nicht zur Pflichtlektüre.

## Grenze der Engineering-Prüfung

`python tools/check.py` ist der gemeinsame lokale und CI-Einstiegspunkt für die vollständige deterministische Prüfung. Er umfasst Prüfung des Quellenvertrags, Engineering-Prüfung, die Zuordnungen und Schutzmechanismen der Engineering-Eignung, Regressionstests, Projektkontexte in frischen Prozessen und Resolver-Prüfungen an echten Daten.

Eine grüne Prüfung belegt nur die formalen, deterministischen Eigenschaften, die an genau diesem Stand tatsächlich geprüft wurden. Sie belegt **nicht**: die Richtigkeit von Handschriftenlesungen, fachliche Gültigkeit, Unabhängigkeit von Belegen, Abnahme durch den Eigentümer, Eignung externer Laufzeit- oder Sicherungsumgebungen oder den Abschluss des Gesamtsystems oder eines Programms.

## Grenzen früherer Programme

- **#225** ist als GitHub-Arbeitsmetadatum geschlossen. F17 hält aber die offene wissenschaftliche Abnahme des Gesamtsystems fest; Engineering-CI kann daraus kein wissenschaftliches PASS machen.
- **#230** ist als begrenzter Audit-Eigentümer abgeschlossen, der zur damaligen Engineering-Arbeit führte; seine Schließung hat selbst keine Umsetzung freigegeben.
- Das frühere Programm **#206** bleibt historisch und an seinem ausdrücklichen STOP beendet; später gesondert freigegebene Arbeit schreibt diese Geschichte nicht um.
- **Route B / #90** bleibt nach der Entscheidung des Eigentümers zurückgestellt.
- Die gesondert freigegebene Familie der ergebniserhaltenden Ausführungssteuerung bleibt bei ihren eigenen Eigentümern (#280/#285 usw.); die SD-KA-Absicherung übernimmt davon nur repo-prüfbare Folgen, die in ihren freigegebenen Umfang passen.

## Wo die Wahrheit liegt

| Frage | Kanonischer Eigentümer |
|---|---|
| Warum gibt es das Repo, was hat Vorrang? | `GOVERNING_OBJECTIVE.md` |
| Was hat der Eigentümer wörtlich gesagt? | `docs/o-toene.md` |
| Welche festen KI- und Forschungsregeln gelten? | `AGENTS.md` |
| Welche angenommenen projektübergreifenden Entscheidungen zählen? | `DECISIONS.md` |
| Was ist die maßgebliche wissenschaftliche Methode von Anfang bis Ende? | `methodology/historical-source-workflow.md` |
| Was sind die allgemeinen Forschungs-Gates? | `methodology/research-gates.md` |
| Wie werden Projekte eingerichtet, verankert und priorisiert? | `methodology/project-lifecycle.md` |
| Wie werden Identität, Herkunft und Sicherung von Quelle und Datei behandelt? | `methodology/source-and-provenance.md` |
| Welche Beleg- und Quellenstatus gelten? | `methodology/evidence-policy.md` |
| Wie wird diplomatisch transkribiert? | `methodology/transcription-guidelines.md` |
| Wie werden Ausführungskontext, Voraussetzungen, Wiederholungen und Schleifen behandelt? | `methodology/workflow.md` |
| Wie werden Qualität, Falsifikation und Prüfdimensionen behandelt? | `methodology/quality-and-learning.md` |
| Wie werden Zuständigkeit, D-016-Freigabe und Weitergabe von Änderungen behandelt? | `methodology/maintenance.md` |
| Welche festen Regeln gelten maschinenprüfbar für Quelle, Datei und Projektnutzung? | `corpus/source-contract.json` + `tools/source_contract.py` |
| Wer verwaltet Eingangsgeschichte und feingranulare Sichtung und Abdeckung? | `source-entry/README.md` + `source-entry/contract.json` + `tools/source_contract.py` |
| Was ist die freigegebene und aktuelle Entscheidungsgrundlage für Option C? | `artifact:ENG-A-0119` + `artifact:ENG-A-0120` |
| Welche wiederverwendbaren Anforderungen sind angenommen? | `requirements/domain-requirements.tsv` |
| Welche Engineering-Baseline, laufende Änderung und welcher Fokus gelten? | `engineering/configuration.json` |
| Wie ist der Lebenszyklus von SD-KA? | `engineering/changes/SD-KA-01/STATE.json` |
| Was hat die abgeschlossene SD-KA-Arbeit ergeben? | `engineering/changes/SD-KA-01/RESULT.md` |
| Welche Engineering-Artefakte, Befunde und Beziehungen werden verwaltet? | `engineering/catalog/` |
| Wer verwaltet die Kompatibilität verschobener Pfade? | `engineering/catalog/legacy-paths.tsv` |
| Wer verwaltet Migrations- und Rückweg-Belege von WP5? | `engineering/changes/SD-KA-01/MIGRATION.tsv` |
| Wer verwaltet das Verhalten erzeugter Engineering-Kontexte? | `engineering/context/README.md` |
| Wer verwaltet das Verhalten begrenzter `.prompt`-Aufrufe? | `engineering/prompts/CONTRACT.md` |
| Wer verwaltet die deterministischen Zuordnungen der Engineering-Eignung? | `engineering/assurance/fitness.json` + `tools/engineering_fitness.py` |
| Was ist eine Tatsache über Quelle, Datei, Beziehung oder Zuordnung? | `corpus/` |
| Was ist ein Projekt und sein aktueller Umfang? | `project.yml` des Projekts |
| Wie nutzt ein Projekt Quellen? | `source-uses.tsv` des Projekts |
| Welche konkrete Datei belegt eine Projektnutzung? | `research/use-evidence.tsv` des Projekts |
| Wie ist der aktuelle Stand von Wiedereinstieg, Gates und Belegen im Projekt? | `STATUS.md` des Projekts |

Eine dauerhafte Tatsache oder ein Stand hat genau einen kanonischen Eigentümer. Zusammenfassungen für Menschen, erzeugte Kontexte, Issues und Chat dürfen darauf verweisen, aber keine zweiten Wahrheitsspeicher werden.

## Aktuelle Projektverzeichnisse

Das Repo enthält derzeit:

- `projects/ega-reg-ii-3/`;
- `projects/ega-reg-ii-4-bd-ii/`;
- `projects/ega-reg-ii-5-knau/`;
- `projects/ssta-20578-nr-632/`.

Der Pfad `ega-reg-ii-5-knau` ist ein altes Verzeichnis bzw. eine alte ID, die aus Gründen der Kontinuität bleibt. Bedeutung, Umfang und Vorrang des Projekts ergeben sich nur aus seinen kanonischen Projektdateien, nicht aus dem Namen.

**Den aktuellen Projektumfang, Gate-Stand oder `NEXT ACTION` nicht in diese README kopieren.** Direkt beim Projekt-Eigentümer lesen oder die neu erzeugbare Projektkontext-Ansicht nutzen.

## Aufbau des Repos

```text
GOVERNING_OBJECTIVE.md
AGENTS.md
DECISIONS.md
MILESTONES.md
README.md
SPICKZETTEL.md
docs/
methodology/
requirements/
engineering/
  architecture/
  assurance/
  catalog/
  changes/
  context/
  decisions/
  evidence/
  prompts/
templates/
source-entry/
corpus/
entities/
projects/
tools/
tests/
```

## Prüfmaßstab für Wiederaufnahme

Eine andere fähige Forscherin, ein anderer Forscher oder Agent soll mit Repo und freigegebenen Belegen, ohne alten Chat, feststellen können:

- Zweck des Repos und Grenzen der Befugnisse;
- Zweck und Umfang eines Projekts und seinen dokumentarischen Anker;
- kanonische Identität von Quellen und Dateien und ihre strukturellen Beziehungen;
- projektbezogene Quellennutzung und konkrete Belegbindungen;
- tatsächlichen Forschungs-, Gate- und Belegstand eines Projekts und ob es eine freigegebene `NEXT ACTION` gibt;
- welche Ausgaben kanonisch und welche abgeleitet sind;
- für die Systementwicklung: angenommene Engineering-Baselines, Stand laufender freigegebener Änderungen, ausdrückliche aktuelle oder nächste Arbeit mit Herkunft, geltender Kontext, abgeschlossene Ergebnisse, Kompatibilität nach Migrationen und den nächsten zulässigen begrenzten Übergang.

Wenn die Fortsetzung veraltete Orientierungsprosa, doppelten Stand, abgeleiteten Vorrang oder alten Chat braucht, ist die zuständige Stelle abgedriftet und muss repariert werden.
