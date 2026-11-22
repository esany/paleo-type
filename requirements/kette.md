# Anforderungskette

Erzeugt von `tools/anforderungskette.py` aus `requirements/beduerfnisse.tsv` und `requirements/domain-requirements.tsv`. Bitte nicht von Hand ändern; nach jeder Änderung an den beiden Tabellen `python3 tools/anforderungskette.py schreiben` ausführen. Die Prüfung schlägt fehl, wenn diese Ansicht veraltet ist.

**Was hier geprüft ist:** dass jeder O-Ton wörtlich an seiner Fundstelle steht, dass jede Anforderung einem Bedürfnis oder ausdrücklich einem Fachanspruch dient, dass jede eine Prüfangabe hat und dass jeder genannte Test existiert. **Was nicht geprüft ist:** ob ein Test die Anforderung inhaltlich ganz abdeckt, ob eine Ableitung den O-Ton richtig deutet, ob eine Anforderung fachlich erfüllt ist. Die Kurzbezeichnungen sind deutsche Übersetzungen; maßgeblich ist der englische Wortlaut in der Tabelle.

**Prüfangaben:** *Test (n)*: n Tests im Repo prüfen einen Teil davon. *Fachurteil*: nur Fachleute können es beurteilen. *Prüfung im Gebrauch*: nur du kannst es beim Benutzen beurteilen. ***keine***: prüfbar, aber nichts prüft es.

## Auf einen Blick

| Gilt ab | Anforderungen | mit Test | ohne jede Prüfung |
|---|---:|---:|---:|
| immer | 48 | 17 | 13 |
| G1 | 7 | 3 | 2 |
| G2 | 29 | 2 | 26 |
| G3 | 8 | 0 | 6 |
| G4 | 3 | 2 | 1 |
| G5 | 3 | 0 | 2 |
| G6 | 23 | 0 | 10 |
| Auslöser (bei Bedarf) | 14 | 1 | 8 |
| **alle** | **135** | **25** | **68** |

Bei **54** Anforderungen bewertet die Tabelle die Unterstützung selbst als „adequate“ oder „strong“, ohne dass ein Test sie prüft. Das ist eine Selbstauskunft, kein Beleg.

## Intent und Rahmen

- **I-01** Jede Quelle ediert haben und sie so einordnen, verstehen und lesen können wie ein Historiker ihrer Epoche. (wörtlich; O-Ton: „Mein Ziel, ist das ich jede Quelle editiert habe und im historischen Kontext, wie ein Historiker der entsprechenden Epoche einordnen“)
- **R-01** Wissenschaftlicher Anspruch für die eigene Forschung, keine Publikationsreife; veröffentlicht wird nicht direkt aus dem Repo. (wörtlich; O-Ton: „exelent meint Sorgfalt, nicht publikationsreife“)
- **R-02** Viele Quellen aus 800 Jahren, vorerst ohne Grenze. (wörtlich; O-Ton: „es gibt erstmal keine Grenze - Quellen aus 800 Jahren“)
- **R-03** Unabhängig von konkreten KI-Modellen und Anbietern. (wörtlich; O-Ton: „alles sollte erstmal unabhängig von konkreten Modellen gebaut sein“)
- **R-04** Alles, was der Eigentümer liest, ist Deutsch. (abgeleitet; O-Ton: „Englisch ist falsch“)
- **R-05** Der Eigentümer ist kein Softwareentwickler; er setzt um, was ihm einleuchtet. (wörtlich; O-Ton: „Ich bin kein Softwareentwickler .. wenn mir was vorgeschlagen wird, wo ich glaube das es hilft mache ich es“)
- **R-06** Das Repo wird repariert, nicht neu gestartet (D-022). (wörtlich; O-Ton: „reparieren statt neu starten“)
- **R-07** Zweck ist zuerst die eigene Forschung. (wörtlich; O-Ton: „erstmal eigene Forschung“)

## Bedürfnisse, Pains und ihre Anforderungen

### B-01 Lesen: wissen, was in der Quelle steht. Erst dann lässt sich eine Forschungsfrage stellen.

O-Ton (wörtlich): „Wenn ich gar nicht weiß, was da steht, kann ich keine. Forschungsfrage definieren“

- Pain **P-12** Klares bleibt ungelesen: Auch klar Geschriebenes wird nicht gelesen. (O-Ton: „wieso kannst du klar geschriebene nr4 nicht lesen“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| PHIL-001 | Handschriftliche Form bleibt vorrangig | immer | **keine**, Fachurteil |
| PHIL-004 | Historische Schreibung bleibt erhalten | immer | **keine** |
| COD-001 | Materielles nur, wenn sichtbar und relevant | G1 | Fachurteil |
| COD-004 | Layout, Randnotizen, Lesefolge darstellbar | G2 | **keine** |
| COD-005 | Schaden getrennt von Leseunsicherheit | G2 | **keine** |
| EDIT-001 | Diplomatischer Text getrennt von Ansicht | G2 | **keine** |
| EDIT-002 | Seiten, Zeilen, Lesefolge bleiben erhalten | G2 | **keine** |
| EDIT-003 | Text, Befund, Ergänzung, Normalform getrennt | G2 | **keine** |
| MET-001 | Geschriebene Zahl getrennt vom Wert | G2 | **keine** |
| MET-004 | Rechnungszeichen bleiben Befund | G2 | Fachurteil |
| ONO-001 | Namensform getrennt von Person oder Ort | G2 | **keine** |
| PAL-001 | Unsichere Zeichen erst verorten | G2 | **keine** |
| PAL-005 | Zeichen, Kürzung, Auflösung getrennt | G2 | **keine** |
| PAL-006 | Zahlen und Maße als eigene Zeichensysteme | G2 | **keine**, Fachurteil |
| PHIL-002 | Kürzel und Auflösung getrennt | G2 | **keine** |
| PHIL-003 | Unsichere Worttrennung darstellbar | G2 | **keine** |
| UX-003 | Diplomatischer Text in Lesefolge lesbar | G2 | **keine**, Prüfung im Gebrauch |

### B-02 Einordnen: das Gelesene im historischen Kontext verstehen; Bilderkennung allein genügt nicht.

O-Ton (wörtlich): „Es geht nicht um reine Bilderkennung beim Lesen der Quelle - und selbst wenn ich weiß, was da steht, kann ich es trotzdem nicht einordnen“

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| UX-006 | Aussagearten erkennbar | immer | Prüfung im Gebrauch |
| ARCH-010 | Schriftstückart und Stufe unterscheiden | G1 | Fachurteil |
| ONO-001 | Namensform getrennt von Person oder Ort | G2 | **keine** |
| ONO-002 | Identifizierungsstatus unabhängig von Lesung | G2 | **keine** |
| PHIL-008 | Wort, Normalform, Identifizierung mit eigenem Status | G2 | **keine** |
| HIST-003 | Überlieferung nur mit Beleg, nicht aus Kontext | G4 | Test (1), Fachurteil |
| ARCH-011 | Erwähnung, Mitwirkung, Amt, Schreiber trennen | G6 | **keine**, Fachurteil |
| DOM-003 | Fachaussagen mit eingesehenem Beleg | G6 | **keine** |
| DOM-005 | Quellenbegriff getrennt von Fachbegriff | G6 | Fachurteil |
| HIST-002 | Entstehungskontext nur so weit belegt | G6 | Fachurteil |
| HIST-006 | Weg von der Aussage zum Beleg | G6 | **keine** |
| HIST-011 | Bei Datierung sagen, was datiert wird | G6 | **keine**, Fachurteil |
| MET-002 | Menge, Einheit, Buchungszweck getrennt | G6 | **keine**, Fachurteil |
| MET-006 | Umrechnungen nur für Zeit und Ort belegt | G6 | Fachurteil |
| ONO-005 | Gleichnamige nach Zeit, Ort, Amt trennen | G6 | Fachurteil |
| PHIL-007 | Bedeutung nach Zeit und Kontext | G6 | Fachurteil |

### B-03 Richtigkeit: Ergebnisse sind richtig, damit er die richtigen Schlüsse für seine Forschung zieht.

O-Ton (wörtlich): „es soll richtig sein und ich die richtigen Schlüsse für meine Forschung ziehen“

- Pain **P-13** Raten: Die KI ergänzt, statt zu belegen. (O-Ton: „Du rätst“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-005 | KI lässt Offenes offen statt zu vervollständigen | immer | **keine** |
| ARCH-001 | Stabile Identität jeder Quelle | immer | Test (1), Fachurteil |
| ARCH-002 | Provenienz getrennt von Quelle und Deutung | immer | Fachurteil |
| COD-009 | Materialbefund getrennt von Schluss | immer | Fachurteil |
| DOM-002 | Gattungswissen ist kein Lesebeleg | immer | Fachurteil |
| HIST-001 | Befund, Katalog, Identifizierung, Deutung getrennt | immer | Test (1), Fachurteil |
| MET-009 | Wirtschaftliche Plausibilität erst nach Zeichenbefund | immer | Fachurteil |
| PAL-009 | Schriftbefund getrennt von Kontextschluss | immer | Fachurteil |
| PHIL-001 | Handschriftliche Form bleibt vorrangig | immer | **keine**, Fachurteil |
| PHIL-004 | Historische Schreibung bleibt erhalten | immer | **keine** |
| PHIL-006 | Plausibilität erst nach Schriftbefund | immer | Fachurteil |
| RSE-010 | Automatik schreibt weniger, als Fachurteil entscheidet | immer | Fachurteil |
| ARCH-006 | Quellenbeziehungen sind belegte Aussagen | G1 | Test (2), Fachurteil |
| AI-004 | Blindlesung ohne Vorwissen | G2 | Test (2) |
| EDIT-001 | Diplomatischer Text getrennt von Ansicht | G2 | **keine** |
| EDIT-002 | Seiten, Zeilen, Lesefolge bleiben erhalten | G2 | **keine** |
| EDIT-003 | Text, Befund, Ergänzung, Normalform getrennt | G2 | **keine** |
| ONO-004 | Identifizierung mit Beleg, nicht nach Gleichklang | G2 | **keine** |
| PAL-005 | Zeichen, Kürzung, Auflösung getrennt | G2 | **keine** |
| PAL-006 | Zahlen und Maße als eigene Zeichensysteme | G2 | **keine**, Fachurteil |
| PAL-007 | Alternativen und Verworfenes bleiben sichtbar | G2 | **keine** |
| PAL-003 | Gleicher Kontext ist nicht gleiche Hand | G3 | Fachurteil |
| PAL-004 | Unterscheidende Schriftmerkmale festhalten | G3 | **keine**, Fachurteil |
| PHIL-005 | Wortbedeutung mit eingesehenem Beleg | G3 | **keine** |
| EDIT-004 | Jeder Textzeuge erst für sich gelesen | G4 | Test (1), Fachurteil |
| EDIT-005 | Entsprechungen zwischen Zeugen belegt zuordnen | G4 | **keine** |
| HIST-003 | Überlieferung nur mit Beleg, nicht aus Kontext | G4 | Test (1), Fachurteil |
| ARCH-011 | Erwähnung, Mitwirkung, Amt, Schreiber trennen | G6 | **keine**, Fachurteil |
| HIST-002 | Entstehungskontext nur so weit belegt | G6 | Fachurteil |
| HIST-004 | Bestätigung nur durch unabhängige Belege | G6 | Fachurteil |
| HIST-011 | Bei Datierung sagen, was datiert wird | G6 | **keine**, Fachurteil |
| MET-002 | Menge, Einheit, Buchungszweck getrennt | G6 | **keine**, Fachurteil |
| MET-006 | Umrechnungen nur für Zeit und Ort belegt | G6 | Fachurteil |
| ARCH-008 | Fehlanzeige nur mit dokumentierter Suche | Auslöser: Vollständigkeits- oder Fehlanzeige | **keine** |
| GWP-007 | Vollständigkeit nur mit Suchgrenzen | Auslöser: Vollständigkeits- oder Fehlanzeige | **keine** |
| HIST-005 | Schweigen der Quellen nur mit Suchgrenzen | Auslöser: Vollständigkeits- oder Fehlanzeige | **keine** |

### B-04 Mitlesen: die entstehenden Forschungsdaten lesen und den Fortschritt sehen können.

O-Ton (wörtlich): „Gerade versuche die entstehenden Forschungsdaten mitzulesen.“

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| UX-002 | Aktive Quelle und Stelle ohne Technikwissen sichtbar | immer | Prüfung im Gebrauch |
| UX-007 | Stufe, Lücken, nächster Schritt ohne Chat sichtbar | immer | **keine**, Prüfung im Gebrauch |
| EDIT-008 | Lesbare Ansicht aus den Daten erzeugt | G2 | **keine** |
| GWP-010 | Ausgaben aus den Daten erzeugt, nie von Hand doppelt | G2 | **keine** |
| RSE-006 | Ansichten werden erzeugt, nicht gepflegt | G2 | **keine** |
| UX-003 | Diplomatischer Text in Lesefolge lesbar | G2 | **keine**, Prüfung im Gebrauch |
| UX-004 | Unsicheres, Ergänztes, Eingriffe sichtbar | G2 | **keine**, Prüfung im Gebrauch |
| UX-009 | Ansichten sind abgeleitet, keine zweite Wahrheit | G2 | **keine** |

### B-05 Verlässlichkeit: Transparenz, Vertrauen und Verlässlichkeit; Unsicherheit wird benannt.

O-Ton (wörtlich): „ich brauche Transparenz, Vertrauen und Verlässlichkeit - Unsicherheit muss benannt werden“

- Pain **P-03** Fehler summieren sich: KI-Fehler häufen sich, Behobenes kommt wieder. (O-Ton: „Das repo ist auch schon voll großer und kleiner KI Bugs, die sich aufsummieren“)
- Pain **P-05** Kreisen ohne Transparenz: Pläne klingen plausibel, dann kommt kein Fortschritt; das wiederholt sich. (O-Ton: „dieser ist für mich nicht wirklich transparent“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-005 | KI lässt Offenes offen statt zu vervollständigen | immer | **keine** |
| AI-008 | Feste Fehlerklassen prüft ein Werkzeug, nicht die KI | immer | Test (3) |
| ARCH-005 | Katalog, Schluss und Autopsie unterscheiden | immer | Test (2) |
| DOM-009 | Erfahrungswissen als offene Fragen, nicht als Schluss | immer | **keine** |
| GWP-003 | Beleg, Metadaten, Hinweis, KI-Hypothese unterscheidbar | immer | Test (1) |
| HIST-001 | Befund, Katalog, Identifizierung, Deutung getrennt | immer | Test (1), Fachurteil |
| RSE-010 | Automatik schreibt weniger, als Fachurteil entscheidet | immer | Fachurteil |
| UX-005 | Vom Ergebnis zum Beleg durchklicken | immer | **keine** |
| UX-007 | Stufe, Lücken, nächster Schritt ohne Chat sichtbar | immer | **keine**, Prüfung im Gebrauch |
| COD-002 | Nicht untersucht, nicht sichtbar, nicht vorhanden unterscheiden | G2 | **keine** |
| COD-005 | Schaden getrennt von Leseunsicherheit | G2 | **keine** |
| ONO-002 | Identifizierungsstatus unabhängig von Lesung | G2 | **keine** |
| ONO-003 | Mehrere Kandidaten und Verworfenes darstellbar | G2 | **keine** |
| PAL-001 | Unsichere Zeichen erst verorten | G2 | **keine** |
| PAL-007 | Alternativen und Verworfenes bleiben sichtbar | G2 | **keine** |
| PHIL-003 | Unsichere Worttrennung darstellbar | G2 | **keine** |
| PHIL-008 | Wort, Normalform, Identifizierung mit eigenem Status | G2 | **keine** |
| UX-004 | Unsicheres, Ergänztes, Eingriffe sichtbar | G2 | **keine**, Prüfung im Gebrauch |
| PAL-010 | Offene Lesung ist gültig; Fachprüfung benennen | G3 | Fachurteil |
| UX-008 | Fachprüfstatus getrennt von KI-Arbeit sichtbar | G3 | **keine** |
| DOM-006 | Mehrere Deutungen zulassen | G6 | Fachurteil |
| HIST-007 | Alternative Deutungen bleiben sichtbar | G6 | Fachurteil |
| HIST-008 | Vorläufige Kontextannahmen behalten Status | G6 | **keine** |
| MET-003 | Unsicherheit je Schritt der Wertbestimmung | G6 | **keine** |
| MET-008 | Alternative Einheiten sichtbar | G6 | Fachurteil |
| ONO-006 | Widersprüchliche Identifizierungen nebeneinander | G6 | **keine** |
| ARCH-008 | Fehlanzeige nur mit dokumentierter Suche | Auslöser: Vollständigkeits- oder Fehlanzeige | **keine** |
| GWP-007 | Vollständigkeit nur mit Suchgrenzen | Auslöser: Vollständigkeits- oder Fehlanzeige | **keine** |
| HIST-005 | Schweigen der Quellen nur mit Suchgrenzen | Auslöser: Vollständigkeits- oder Fehlanzeige | **keine** |

### B-06 Herkunft: Es bleibt nachvollziehbar, woher jede Aussage stammt (Quelle, KI oder Eigentümer).

O-Ton (abgeleitet): „Immer Provinenz erhalten, Nachvollzihebarkeit.“

- Pain **P-10** Unklare Herkunft: Es ist nicht erkennbar, was von der KI kommt und was O-Ton ist. (O-Ton: „Es ist auch nicht klar, was kommt von der KI, was sind meine O-Töne“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-003 | KI-Ausgabe, Beleg, Schluss, Prüfung unterscheiden | immer | **keine** |
| AI-006 | KI-Schritte mit angemessener Herkunft | immer | **keine** |
| ARCH-001 | Stabile Identität jeder Quelle | immer | Test (1), Fachurteil |
| ARCH-002 | Provenienz getrennt von Quelle und Deutung | immer | Fachurteil |
| ARCH-003 | Geprüfte Datei getrennt vom Archivale | immer | Test (3) |
| ARCH-005 | Katalog, Schluss und Autopsie unterscheiden | immer | Test (2) |
| ARCH-007 | Forschungsfunktion gilt nur im Projekt | immer | Test (2) |
| COD-006 | Objekt getrennt vom Digitalisat | immer | Test (2) |
| GWP-002 | Belege bis zu Quelle, Datei, Stelle rückverfolgbar | immer | Test (2) |
| GWP-003 | Beleg, Metadaten, Hinweis, KI-Hypothese unterscheidbar | immer | Test (1) |
| GWP-004 | Revisionen bleiben rekonstruierbar | immer | Test (1) |
| GWP-005 | Sichtbar, wer was gemacht und geprüft hat | immer | Test (1) |
| RSE-004 | Stabile IDs mit Referenzprüfung | immer | Test (2) |
| RSE-008 | Umwandlungen behalten Herkunft und Entscheidungen | immer | **keine** |
| UX-005 | Vom Ergebnis zum Beleg durchklicken | immer | **keine** |
| ARCH-004 | Folio, Bild, PDF-Seite getrennt zuordnen | G1 | Test (3) |
| ARCH-006 | Quellenbeziehungen sind belegte Aussagen | G1 | Test (2), Fachurteil |
| COD-001 | Materielles nur, wenn sichtbar und relevant | G1 | Fachurteil |
| COD-003 | Zählung aus dem Befund, nicht aus der PDF | G1 | Test (2) |
| COD-007 | Bildableitungen behalten ihre Herkunft | G1 | **keine** |
| ARCH-009 | Eindeutige Adresse für jede Belegstelle | G2 | **keine** |
| EDIT-006 | Lesentscheidungen und Revisionen nachvollziehbar | G2 | Test (2) |
| ONO-009 | Entscheidungen zu Namen mit Begründung | G2 | **keine** |
| MET-005 | Zahlschlüsse mit Stelle und Vergleich | G3 | **keine** |
| PAL-002 | Vergleichsstellen genau wiederfinden | G3 | **keine** |
| PAL-008 | Bildvergleich auf genaues Bild zurückführen | G3 | **keine** |
| PHIL-005 | Wortbedeutung mit eingesehenem Beleg | G3 | **keine** |
| EDIT-007 | Apparat, wenn das Editionskonzept ihn verlangt | G5 | **keine** |
| EDIT-010 | Jede Ausgabe führt zum Beleg zurück | G5 | **keine** |
| DOM-003 | Fachaussagen mit eingesehenem Beleg | G6 | **keine** |
| HIST-006 | Weg von der Aussage zum Beleg | G6 | **keine** |
| HIST-009 | Sekundärliteratur mit eingesehener Stelle | G6 | **keine** |
| MET-007 | Umrechnungsquelle genau angeben | G6 | **keine** |
| ONO-008 | Normdaten sind Verknüpfung, kein Beleg | Auslöser: Verknüpfung mit Normdaten | **keine** |

### B-07 Echte Funktion: Was als umgesetzt gilt, funktioniert tatsächlich und ist prüfbar.

O-Ton (abgeleitet): „ich erwarte funktionalität, wo keine Ist“

- Pain **P-01** Prosa statt Funktion: Modelle antworten mit Text und behaupten Umsetzungen, die es nicht gibt. (O-Ton: „die Modelle reagieren mit Prosa, behaupten umgesetzt zu haben, was sie nicht gemacht haben“)
- Pain **P-02** Regel statt Lösung: Auf fehlende Funktion folgt eine neue Regel. (O-Ton: „und das beantworte ich mit einer neuen Regel.“)
- Pain **P-03** Fehler summieren sich: KI-Fehler häufen sich, Behobenes kommt wieder. (O-Ton: „Das repo ist auch schon voll großer und kleiner KI Bugs, die sich aufsummieren“)
- Pain **P-06** Beschreiben statt beheben: Die KI beschreibt ihre Mängel, statt den ersten Schritt zur Behebung zu tun. (O-Ton: „Die KI ist top ihre eigene Unzulänglichkeit zu beschreiben“)
- Pain **P-14** Tun statt Funktion: Nach erkannten Grundproblemen geht die laufende Arbeit weiter, ohne fehlende Funktionen nachzulegen. (O-Ton: „und du sagst gerade weiter im text“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-008 | Feste Fehlerklassen prüft ein Werkzeug, nicht die KI | immer | Test (3) |
| RSE-001 | Jedes Werkzeug dient einer Anforderung | immer | Test (1) |
| EDIT-008 | Lesbare Ansicht aus den Daten erzeugt | G2 | **keine** |
| GWP-010 | Ausgaben aus den Daten erzeugt, nie von Hand doppelt | G2 | **keine** |
| RSE-006 | Ansichten werden erzeugt, nicht gepflegt | G2 | **keine** |
| UX-009 | Ansichten sind abgeleitet, keine zweite Wahrheit | G2 | **keine** |

### B-08 Fachkunde: echte Fachkunde transdisziplinär nachbilden, als Innehalten und Kompass für Entscheidungen.

O-Ton (wörtlich): „die echte Fachkunde transdisziplinär nachbildet“

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-001 | Vor dem Handeln alles Geltende laden | immer | Test (2) |
| DOM-001 | Zuständige Fachgebiete benennen | immer | **keine** |
| DOM-009 | Erfahrungswissen als offene Fragen, nicht als Schluss | immer | **keine** |
| GWP-011 | Begriffe behalten beim Übersetzen ihre Bedeutung | immer | Fachurteil |

### B-09 Verstehen und entscheiden: Vorschläge so verstehen, dass er über sie entscheiden kann.

O-Ton (abgeleitet): „wenn mir was vorgeschlagen wird, wo ich glaube das es hilft mache ich es“

- Pain **P-11** Unverständlich: Sätze und Vorschläge sind für ihn nicht verständlich. (O-Ton: „DAs verstehe ich nicht“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-007 | Schreibgrenzen nach Tragweite | immer | **keine** |
| GWP-011 | Begriffe behalten beim Übersetzen ihre Bedeutung | immer | Fachurteil |
| UX-006 | Aussagearten erkennbar | immer | Prüfung im Gebrauch |
| UX-011 | Forschen, ohne Repo-Technik zu bedienen | immer | Prüfung im Gebrauch |
| UX-012 | Jeder Schritt in Alltagssprache erklärbar | immer | Prüfung im Gebrauch |

### B-10 Ursachen: bei Problemen die eigentliche Ursache finden, nicht das Symptom behandeln.

O-Ton (wörtlich): „Zentral: sind es symtome, oder die tatsächlichen Ursachen“

- Pain **P-02** Regel statt Lösung: Auf fehlende Funktion folgt eine neue Regel. (O-Ton: „und das beantworte ich mit einer neuen Regel.“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| RSE-001 | Jedes Werkzeug dient einer Anforderung | immer | Test (1) |

### B-11 Methodik und Bestand: sorgfältig und behutsam arbeiten und auf vorhandener Methodik und Struktur aufbauen.

O-Ton (abgeleitet): „Wir haben denk ich schon gute Strutkturen, siehe Visitationsprotokolle“

- Pain **P-06** Beschreiben statt beheben: Die KI beschreibt ihre Mängel, statt den ersten Schritt zur Behebung zu tun. (O-Ton: „Die KI ist top ihre eigene Unzulänglichkeit zu beschreiben“)
- Pain **P-08** Methodenverlust: Seit Nr. 632 ist Methode aus den Visitationsakten verloren gegangen. (O-Ton: „da finde ich seit 632 auch ein methodenverlust passiert“)
- Pain **P-09** Vollgas ohne Behutsamkeit: ungesehen losarbeiten, ohne sich der Risiken bewusst zu sein. (O-Ton: „das du ungesehen da mit vollgas reingelaufen bist“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-001 | Vor dem Handeln alles Geltende laden | immer | Test (2) |
| AI-002 | Kürzen ohne geltende Regel zu verlieren | immer | **keine** |
| AI-007 | Schreibgrenzen nach Tragweite | immer | **keine** |
| GWP-009 | Methoden und Standards mit Fassung benannt | immer | **keine** |

### B-12 Auffindbar und aktuell: Wissen ist auffindbar, Startdateien sind aktuell; aufräumen, ohne Kontext zu verlieren.

O-Ton (abgeleitet): „Wo können wir auch einen sauberen clean-up ansetzen, ohne Kontext zu verlieren“

- Pain **P-07** Verstreut und veraltet: Wissen ist verstreut, Startdateien sind nicht gepflegt. (O-Ton: „Das wissen ist sicher auch komplett verstreut“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| GWP-001 | Jeder Stand hat genau einen Ort | immer | Test (3) |
| GWP-008 | Ohne alten Chat wieder aufnehmbar | immer | Test (2) |
| RSE-002 | Daten einfach, lesbar, portabel | immer | Fachurteil |
| RSE-003 | Forschungsstand getrennt von Ansichten | immer | Test (1) |
| UX-001 | Kurzer Weg vom Zweck zum Ergebnis | immer | Prüfung im Gebrauch |
| RSE-007 | Vor Formatwechsel Verlusttest | Auslöser: Wechsel des Datenformats | Test (1) |

### B-13 Fortschritt und Frühwarnung: erkennbarer Fortschritt statt Kreisen; früh gewarnt werden, wenn es hängt.

O-Ton (abgeleitet): „Erhebe Kriterien und Prüfmechanismen, die dir erlauben, frühzeitig gewarnt zu werden.“

- Pain **P-04** Festfahren: Jede Runde baut neue Strukturen und frisst sich an teils trivialen Problemen fest. (O-Ton: „aber jede runde Schafft neue Strukturen“)
- Pain **P-05** Kreisen ohne Transparenz: Pläne klingen plausibel, dann kommt kein Fortschritt; das wiederholt sich. (O-Ton: „dieser ist für mich nicht wirklich transparent“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| RSE-001 | Jedes Werkzeug dient einer Anforderung | immer | Test (1) |
| RSE-005 | Feste Wertlisten nur für Wiederkehrendes | immer | Fachurteil |
| UX-007 | Stufe, Lücken, nächster Schritt ohne Chat sichtbar | immer | **keine**, Prüfung im Gebrauch |

### B-14 Lesewerkzeug: für Handschriften das nötige Werkzeug, Erfahrungswissen und den Stand der Technik.

O-Ton (wörtlich): „hast du überhaupt das nötige tooling für das lesen der handschriften .. das erfahrungswissen und sota?“

- Pain **P-12** Klares bleibt ungelesen: Auch klar Geschriebenes wird nicht gelesen. (O-Ton: „wieso kannst du klar geschriebene nr4 nicht lesen“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| GWP-009 | Methoden und Standards mit Fassung benannt | immer | **keine** |
| MET-005 | Zahlschlüsse mit Stelle und Vergleich | G3 | **keine** |
| PAL-002 | Vergleichsstellen genau wiederfinden | G3 | **keine** |
| PAL-003 | Gleicher Kontext ist nicht gleiche Hand | G3 | Fachurteil |
| PAL-004 | Unterscheidende Schriftmerkmale festhalten | G3 | **keine**, Fachurteil |
| PAL-008 | Bildvergleich auf genaues Bild zurückführen | G3 | **keine** |
| AI-009 | KI-Lesen im großen Stil vorher erproben | Auslöser: KI- oder HTR-Lesung in großem Umfang | **keine** |

### B-15 Fachleute fragen: bei Bedarf gezielt befreundete Historiker fragen können.

O-Ton (abgeleitet): „da würde ich befreundete historiker fragen“

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| PAL-010 | Offene Lesung ist gültig; Fachprüfung benennen | G3 | Fachurteil |
| UX-008 | Fachprüfstatus getrennt von KI-Arbeit sichtbar | G3 | **keine** |
| DOM-010 | Fachprüfung der Domänenaussage ausweisen | G6 | Fachurteil |
| HIST-010 | Historische Fachprüfung ausweisen | G6 | Fachurteil |
| MET-010 | Fachprüfung bei seltenen Zeichen ausweisen | G6 | Fachurteil |
| ONO-010 | Fachprüfung bei strittigen Namen ausweisen | G6 | Fachurteil |
| AI-010 | Fachprüfung mit genauen Belegpaketen; Eigentümer ist kein Fachprüfer | Auslöser: folgenreiche Fachfrage | **keine** |
| COD-008 | Lagen, Bindung, Wasserzeichen nur mit Befund | Auslöser: Frage nach Lage, Bindung oder Wasserzeichen | Fachurteil |
| COD-010 | Vor-Ort-Prüfung als ausdrückliche Eskalation | Auslöser: digital nicht entscheidbar | Fachurteil |
| PHIL-010 | Sprachliche Fachprüfung ausweisen | Auslöser: folgenreiche sprachliche Bestimmung | **keine**, Fachurteil |
| UX-010 | Fachprüfung sieht Stelle, Kandidaten, Belege | Auslöser: folgenreiche Fachfrage | **keine** |

### B-16 Vom Bedürfnis zur prüfbaren Lösung: Entwicklung geht vom Bedürfnis aus, wird umgesetzt und ist prüfbar; jede Perspektive wird einmal bedacht.

O-Ton (wörtlich): „In meiner Welt ist user research der zentrale Motor für entwicklung“

- Pain **P-14** Tun statt Funktion: Nach erkannten Grundproblemen geht die laufende Arbeit weiter, ohne fehlende Funktionen nachzulegen. (O-Ton: „und du sagst gerade weiter im text“)
- Pain **P-15** Absicht ungeprüft: Prüfungen zeigen nicht, ob die Absicht erreicht ist. (O-Ton: „Absicht nicht geprüft“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| RSE-001 | Jedes Werkzeug dient einer Anforderung | immer | Test (1) |
| RSE-005 | Feste Wertlisten nur für Wiederkehrendes | immer | Fachurteil |
| RSE-009 | Aufwand und Abhängigkeiten nach echtem Bedarf | immer | Fachurteil |

### B-17 Querbeziehungen: was schon gelesen ist, hilft beim Lesen und Verstehen der nächsten Stellen.

O-Ton (abgeleitet): „dann müssen dich querbeziehungen erkenntnisse schaffen“

**Keine Anforderung dient diesem Bedürfnis.** Das ist eine Lücke.

## Lücken nach Stufe

Prüfbare Anforderungen, die nichts prüft, geordnet danach, ab wann sie gelten.

| gilt ab | Anforderung | Kurz | dient | braucht zuerst |
|---|---|---|---|---|
| immer | PHIL-001 | Handschriftliche Form bleibt vorrangig | B-01, B-03 |  |
| immer | PHIL-004 | Historische Schreibung bleibt erhalten | B-01, B-03 |  |
| immer | DOM-001 | Zuständige Fachgebiete benennen | B-08 |  |
| immer | DOM-009 | Erfahrungswissen als offene Fragen, nicht als Schluss | B-08, B-05 |  |
| immer | GWP-009 | Methoden und Standards mit Fassung benannt | B-14, B-11 |  |
| immer | RSE-008 | Umwandlungen behalten Herkunft und Entscheidungen | B-06 |  |
| immer | AI-002 | Kürzen ohne geltende Regel zu verlieren | B-11 |  |
| immer | AI-003 | KI-Ausgabe, Beleg, Schluss, Prüfung unterscheiden | B-06, P-10 |  |
| immer | AI-005 | KI lässt Offenes offen statt zu vervollständigen | B-05, P-13 |  |
| immer | AI-006 | KI-Schritte mit angemessener Herkunft | B-06 |  |
| immer | AI-007 | Schreibgrenzen nach Tragweite | B-09, P-09 |  |
| immer | UX-005 | Vom Ergebnis zum Beleg durchklicken | B-06, B-05 | GWP-002, EDIT-006 |
| immer | UX-007 | Stufe, Lücken, nächster Schritt ohne Chat sichtbar | B-13, B-04, P-05 | GWP-008 |
| G1 | COD-007 | Bildableitungen behalten ihre Herkunft | B-06 |  |
| G1 | GWP-006 | Rechte und Zugangsgrenzen ausdrücklich | fach |  |
| G2 | ARCH-009 | Eindeutige Adresse für jede Belegstelle | B-06 |  |
| G2 | PAL-001 | Unsichere Zeichen erst verorten | B-01, B-05 | ARCH-009 |
| G2 | PAL-005 | Zeichen, Kürzung, Auflösung getrennt | B-01, B-03 |  |
| G2 | PAL-006 | Zahlen und Maße als eigene Zeichensysteme | B-01, B-03 |  |
| G2 | PAL-007 | Alternativen und Verworfenes bleiben sichtbar | B-05, P-13 |  |
| G2 | PHIL-002 | Kürzel und Auflösung getrennt | B-01 |  |
| G2 | PHIL-003 | Unsichere Worttrennung darstellbar | B-01, B-05 |  |
| G2 | PHIL-008 | Wort, Normalform, Identifizierung mit eigenem Status | B-05, B-02 |  |
| G2 | EDIT-001 | Diplomatischer Text getrennt von Ansicht | B-01, B-03 |  |
| G2 | EDIT-002 | Seiten, Zeilen, Lesefolge bleiben erhalten | B-01, B-03 |  |
| G2 | EDIT-003 | Text, Befund, Ergänzung, Normalform getrennt | B-01, B-03 |  |
| G2 | EDIT-008 | Lesbare Ansicht aus den Daten erzeugt | B-04, B-07 | EDIT-001, EDIT-002, EDIT-003 |
| G2 | COD-002 | Nicht untersucht, nicht sichtbar, nicht vorhanden unterscheiden | B-05 |  |
| G2 | COD-004 | Layout, Randnotizen, Lesefolge darstellbar | B-01 |  |
| G2 | COD-005 | Schaden getrennt von Leseunsicherheit | B-05, B-01 |  |
| G2 | ONO-001 | Namensform getrennt von Person oder Ort | B-01, B-02 |  |
| G2 | ONO-002 | Identifizierungsstatus unabhängig von Lesung | B-02, B-05 |  |
| G2 | ONO-003 | Mehrere Kandidaten und Verworfenes darstellbar | B-05 |  |
| G2 | ONO-004 | Identifizierung mit Beleg, nicht nach Gleichklang | B-03, P-13 | ONO-001, ONO-002 |
| G2 | ONO-009 | Entscheidungen zu Namen mit Begründung | B-06 | ONO-003 |
| G2 | MET-001 | Geschriebene Zahl getrennt vom Wert | B-01 |  |
| G2 | GWP-010 | Ausgaben aus den Daten erzeugt, nie von Hand doppelt | B-04, B-07 |  |
| G2 | RSE-006 | Ansichten werden erzeugt, nicht gepflegt | B-04, B-07 |  |
| G2 | UX-003 | Diplomatischer Text in Lesefolge lesbar | B-04, B-01 | EDIT-008, EDIT-002 |
| G2 | UX-004 | Unsicheres, Ergänztes, Eingriffe sichtbar | B-04, B-05 | UX-003, EDIT-003, PAL-001, PAL-007 |
| G2 | UX-009 | Ansichten sind abgeleitet, keine zweite Wahrheit | B-04, B-07 |  |
| G3 | PAL-002 | Vergleichsstellen genau wiederfinden | B-06, B-14 | ARCH-009 |
| G3 | PAL-004 | Unterscheidende Schriftmerkmale festhalten | B-03, B-14 | PAL-001, PAL-002 |
| G3 | PAL-008 | Bildvergleich auf genaues Bild zurückführen | B-06, B-14 | COD-007 |
| G3 | PHIL-005 | Wortbedeutung mit eingesehenem Beleg | B-06, P-13 |  |
| G3 | MET-005 | Zahlschlüsse mit Stelle und Vergleich | B-06, B-14 | PAL-002 |
| G3 | UX-008 | Fachprüfstatus getrennt von KI-Arbeit sichtbar | B-15, B-05 | GWP-005 |
| G4 | EDIT-005 | Entsprechungen zwischen Zeugen belegt zuordnen | B-03 | EDIT-004, ARCH-009 |
| G5 | EDIT-007 | Apparat, wenn das Editionskonzept ihn verlangt | R-01, B-06 | EDIT-005, EDIT-009 |
| G5 | EDIT-010 | Jede Ausgabe führt zum Beleg zurück | R-01, B-06 | EDIT-009, EDIT-006 |
| G6 | ARCH-011 | Erwähnung, Mitwirkung, Amt, Schreiber trennen | B-02, B-03 |  |
| G6 | HIST-006 | Weg von der Aussage zum Beleg | B-06, B-02 | HIST-001, GWP-002 |
| G6 | HIST-008 | Vorläufige Kontextannahmen behalten Status | B-05 |  |
| G6 | HIST-009 | Sekundärliteratur mit eingesehener Stelle | B-06 |  |
| G6 | HIST-011 | Bei Datierung sagen, was datiert wird | B-02, B-03 |  |
| G6 | DOM-003 | Fachaussagen mit eingesehenem Beleg | B-02, B-06 |  |
| G6 | ONO-006 | Widersprüchliche Identifizierungen nebeneinander | B-05 |  |
| G6 | MET-002 | Menge, Einheit, Buchungszweck getrennt | B-02, B-03 | MET-001 |
| G6 | MET-003 | Unsicherheit je Schritt der Wertbestimmung | B-05 |  |
| G6 | MET-007 | Umrechnungsquelle genau angeben | B-06 |  |
| Auslöser: Vollständigkeits- oder Fehlanzeige | ARCH-008 | Fehlanzeige nur mit dokumentierter Suche | B-03, B-05 |  |
| Auslöser: folgenreiche sprachliche Bestimmung | PHIL-010 | Sprachliche Fachprüfung ausweisen | B-15 |  |
| Auslöser: Vollständigkeits- oder Fehlanzeige | HIST-005 | Schweigen der Quellen nur mit Suchgrenzen | B-03, B-05 |  |
| Auslöser: Verknüpfung mit Normdaten | ONO-008 | Normdaten sind Verknüpfung, kein Beleg | B-06 |  |
| Auslöser: Vollständigkeits- oder Fehlanzeige | GWP-007 | Vollständigkeit nur mit Suchgrenzen | B-03, B-05 |  |
| Auslöser: KI- oder HTR-Lesung in großem Umfang | AI-009 | KI-Lesen im großen Stil vorher erproben | R-02, R-03, B-14 |  |
| Auslöser: folgenreiche Fachfrage | AI-010 | Fachprüfung mit genauen Belegpaketen; Eigentümer ist kein Fachprüfer | B-15, R-05 | UX-010 |
| Auslöser: folgenreiche Fachfrage | UX-010 | Fachprüfung sieht Stelle, Kandidaten, Belege | B-15 | PAL-007 |

## Bedürfnisse ohne Anforderung

- **B-17** Querbeziehungen: was schon gelesen ist, hilft beim Lesen und Verstehen der nächsten Stellen.

## Reiner Fachanspruch

Anforderungen, die nur ein Fach begründet, ohne eins deiner Bedürfnisse.

- GWP-006 Rechte und Zugangsgrenzen ausdrücklich

## Überschneidungen

Diese Anforderungen sagen aus verschiedenen Fächern fast dasselbe. Sie bleiben getrennt, weil jedes Fach seine eigene Begründung hat; umgesetzt werden sie gemeinsam.

- ARCH-003 Geprüfte Datei getrennt vom Archivale; COD-006 Objekt getrennt vom Digitalisat
- ARCH-004 Folio, Bild, PDF-Seite getrennt zuordnen; COD-003 Zählung aus dem Befund, nicht aus der PDF
- ARCH-008 Fehlanzeige nur mit dokumentierter Suche; GWP-007 Vollständigkeit nur mit Suchgrenzen; HIST-005 Schweigen der Quellen nur mit Suchgrenzen
- ARCH-009 Eindeutige Adresse für jede Belegstelle; RSE-004 Stabile IDs mit Referenzprüfung
- EDIT-003 Text, Befund, Ergänzung, Normalform getrennt; PAL-005 Zeichen, Kürzung, Auflösung getrennt; PHIL-002 Kürzel und Auflösung getrennt
- MET-001 Geschriebene Zahl getrennt vom Wert; PAL-006 Zahlen und Maße als eigene Zeichensysteme
- AI-005 KI lässt Offenes offen statt zu vervollständigen; DOM-006 Mehrere Deutungen zulassen; HIST-007 Alternative Deutungen bleiben sichtbar; MET-008 Alternative Einheiten sichtbar; ONO-003 Mehrere Kandidaten und Verworfenes darstellbar; PAL-007 Alternativen und Verworfenes bleiben sichtbar
- COD-007 Bildableitungen behalten ihre Herkunft; PAL-008 Bildvergleich auf genaues Bild zurückführen
- COD-009 Materialbefund getrennt von Schluss; HIST-001 Befund, Katalog, Identifizierung, Deutung getrennt; PAL-009 Schriftbefund getrennt von Kontextschluss
- COD-010 Vor-Ort-Prüfung als ausdrückliche Eskalation; DOM-010 Fachprüfung der Domänenaussage ausweisen; HIST-010 Historische Fachprüfung ausweisen; MET-010 Fachprüfung bei seltenen Zeichen ausweisen; ONO-010 Fachprüfung bei strittigen Namen ausweisen; PAL-010 Offene Lesung ist gültig; Fachprüfung benennen; PHIL-010 Sprachliche Fachprüfung ausweisen; UX-008 Fachprüfstatus getrennt von KI-Arbeit sichtbar
- DOM-003 Fachaussagen mit eingesehenem Beleg; HIST-009 Sekundärliteratur mit eingesehener Stelle; MET-007 Umrechnungsquelle genau angeben; PHIL-005 Wortbedeutung mit eingesehenem Beleg
- ONO-002 Identifizierungsstatus unabhängig von Lesung; PHIL-008 Wort, Normalform, Identifizierung mit eigenem Status
- DOM-008 Fachwissen erst nach Mehrfachnutzen verallgemeinern; ONO-007 Eigene Einträge nur für wiederkehrende Namen; PHIL-009 Wortwissen erst nach Mehrfachnutzen verallgemeinern
- COD-004 Layout, Randnotizen, Lesefolge darstellbar; EDIT-002 Seiten, Zeilen, Lesefolge bleiben erhalten
- EDIT-008 Lesbare Ansicht aus den Daten erzeugt; GWP-010 Ausgaben aus den Daten erzeugt, nie von Hand doppelt; RSE-006 Ansichten werden erzeugt, nicht gepflegt; UX-009 Ansichten sind abgeleitet, keine zweite Wahrheit
- GWP-001 Jeder Stand hat genau einen Ort; RSE-003 Forschungsstand getrennt von Ansichten

## Tests ohne Anforderung

Testdateien, aus denen keine Anforderung einen Test nennt. Sie können trotzdem nötig sein; dann fehlt ihre Zuordnung.

- `tests/test_archival_source_acquisition.py`
- `tests/test_engineering_context.py`
- `tests/test_metrics.py`
- `tests/test_prompt.py`
- `tests/test_regii3_crosswalk_restart.py`
- `tests/test_regii5_evidence_packet.py`
- `tests/test_regii5_packet_benchmark.py`
- `tests/test_regii5_visual_retrieval.py`
- `tests/test_sd_ka_wp6_qualification.py`
