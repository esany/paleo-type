# Anforderungskette

Erzeugt von `tools/anforderungskette.py` aus `requirements/beduerfnisse.tsv` und `requirements/domain-requirements.tsv`. Bitte nicht von Hand ändern; nach jeder Änderung an den beiden Tabellen `python3 tools/anforderungskette.py schreiben` ausführen. Die Prüfung schlägt fehl, wenn diese Ansicht veraltet ist.

**Was hier geprüft ist:** dass jeder O-Ton als ganze Wörter in einem Zitat des genannten Abschnitts von `docs/o-toene.md` steht und keine Knopfwahl ist, dass jede Anforderung einem Bedürfnis, Pain, einer Rahmenbedingung oder ausdrücklich nur einem Fach dient, dass jede eine Prüfangabe hat, dass jeder genannte Test existiert und dass keine Anforderung etwas braucht, das erst später gilt. **Was nicht geprüft ist:** ob ein genannter Test die Anforderung inhaltlich abdeckt, ob eine Ableitung den O-Ton richtig deutet, ob eine Anforderung fachlich erfüllt ist.

**Status der Zuordnungen:** Welchem Bedürfnis eine Anforderung dient, ab wann sie gilt, welcher Test sie betrifft, was sie zuerst braucht und womit sie sich überschneidet, hat Claude am 22.11.2026 aus Anforderungstext, Testnamen und Werkzeugbeschreibungen abgeleitet. Der Eigentümer hat es nicht bestätigt. Eine unabhängige Zweitprüfung fand Fehlzuordnungen; sie sind korrigiert, weitere sind möglich. Die Kurzbezeichnungen sind Übersetzungen und lassen Einschränkungen wie „folgenreich“ oder „wo machbar“ weg; maßgeblich ist der englische Wortlaut in der Tabelle.

**Prüfangaben:** *Test genannt (n)*: n Tests im Repo betreffen nach Einschätzung der KI einen Teil davon. *Fachurteil*: nur ein Urteil im jeweiligen Fach (Wissenschaft, Edition, Softwaretechnik) kann es beurteilen. *Prüfung im Gebrauch*: nur du kannst es beim Benutzen beurteilen. Ob solche Urteile stattgefunden haben, steht nicht in der Tabelle. ***kein Test bekannt***: prüfbar, aber kein Test im Repo ist bekannt, der es prüft.

## Auf einen Blick

| Gilt ab | Anforderungen | Test genannt | nur Urteil | kein Test bekannt |
|---|---:|---:|---:|---:|
| immer | 47 | 14 | 17 | 16 |
| G1 | 7 | 3 | 2 | 2 |
| G2 | 30 | 5 | 1 | 24 |
| G3 | 8 | 0 | 2 | 6 |
| G4 | 3 | 0 | 0 | 3 |
| G5 | 3 | 0 | 1 | 2 |
| G6 | 23 | 0 | 13 | 10 |
| Auslöser (bei Bedarf) | 14 | 1 | 5 | 8 |
| **alle** | **135** | 23 | 41 | 71 |

Bei **18** Anforderungen lautet die Selbstbewertung in der Spalte `current_support` ohne Einschränkung „adequate“ oder „strong“, aber kein Test ist genannt: ARCH-007, PHIL-001, PHIL-004, PHIL-006, PHIL-009, DOM-002, DOM-004, DOM-007, ONO-001, ONO-007, ONO-008, MET-009, GWP-006, RSE-002, RSE-009, AI-003, UX-002, UX-007. Die Selbstbewertung stammt aus KI-Fachaudits (#26–#37; Tabelle angelegt am 27.08.2026, vor dieser Änderung zuletzt am 08.09.2026 geändert) und ist eine Auskunft, kein Beleg.

## Intent und Rahmen

- **I-01** Jede Quelle ediert haben und sie so einordnen, verstehen und lesen können wie ein Historiker ihrer Epoche. (wörtlich; O-Ton: „Mein Ziel, ist das ich jede Quelle editiert habe und im historischen Kontext, wie ein Historiker der entsprechenden Epoche einordnen“)
- **R-01** Wissenschaftlicher Anspruch für die eigene Forschung, keine Publikationsreife; veröffentlicht wird nicht direkt aus dem Repo. (wörtlich; O-Ton: „exelent meint Sorgfalt, nicht publikationsreife“) Dient: EDIT-007 Apparat, wenn das Editionskonzept ihn verlangt; EDIT-009 Editionskonzept vor der Endfassung; EDIT-010 Jede Ausgabe führt zum Beleg zurück.
- **R-02** Viele Quellen aus 800 Jahren, vorerst ohne Grenze. (wörtlich; O-Ton: „es gibt erstmal keine Grenze - Quellen aus 800 Jahren“) Dient: PHIL-009 Wortwissen erst nach Mehrfachnutzen verallgemeinern; DOM-004 Methode allgemein, Pilotwissen im Projekt; DOM-007 Projekthypothesen bleiben lokal; DOM-008 Fachwissen erst nach Mehrfachnutzen verallgemeinern; ONO-007 Eigene Einträge nur für wiederkehrende Namen; RSE-009 Aufwand und Abhängigkeiten nach echtem Bedarf; AI-009 KI-Lesen im großen Stil vorher erproben.
- **R-03** Unabhängig von konkreten KI-Modellen. (wörtlich; O-Ton: „alles sollte erstmal unabhängig von konkreten Modellen gebaut sein“) Dient: RSE-002 Daten einfach, lesbar, portabel; AI-009 KI-Lesen im großen Stil vorher erproben.
- **R-04** Alles, was der Eigentümer liest, ist Deutsch. (abgeleitet; O-Ton: „Englisch ist falsch“) Dient: GWP-011 Begriffe behalten beim Übersetzen ihre Bedeutung.
- **R-05** Der Eigentümer ist kein Softwareentwickler; er setzt um, was ihm einleuchtet. (wörtlich; O-Ton: „Ich bin kein Softwareentwickler .. wenn mir was vorgeschlagen wird, wo ich glaube das es hilft mache ich es“) Dient: AI-010 Fachprüfung mit genauen Belegpaketen; Eigentümer ist kein Fachprüfer; UX-011 Forschen, ohne Repo-Technik zu bedienen.
- **R-06** Das Repo wird repariert, nicht neu gestartet (D-022). (wörtlich; O-Ton: „reparieren statt neu starten“) Dient: RSE-007 Vor Formatwechsel Verlusttest.
- **R-07** Zweck ist zuerst die eigene Forschung. (wörtlich; O-Ton: „erstmal eigene Forschung“)
- **R-08** Geplant wird transparent in Issues, die kurz bleiben und keine Kontextwürste werden. (wörtlich; O-Ton: „Transparent aufgeplant als Issues .. die keine Kontextwürsten werden dürfen“)

## Bedürfnisse, Pains und ihre Anforderungen

### B-01 Lesen: wissen, was in der Quelle steht. Erst dann lässt sich eine Forschungsfrage stellen.

O-Ton (wörtlich): „Wenn ich gar nicht weiß, was da steht, kann ich keine. Forschungsfrage definieren“

- Pain **P-12** Klares bleibt ungelesen: Bei Nr. 632 wurde auch klar Geschriebenes nicht gelesen. (O-Ton: „wieso kannst du klar geschriebene nr4 nicht lesen“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| PHIL-001 | Handschriftliche Form bleibt vorrangig | immer | **kein Test bekannt**, Fachurteil |
| PHIL-004 | Historische Schreibung bleibt erhalten | immer | **kein Test bekannt** |
| COD-001 | Materielles nur, wenn sichtbar und relevant | G1 | Fachurteil |
| COD-004 | Layout, Randnotizen, Lesefolge darstellbar | G2 | **kein Test bekannt** |
| COD-005 | Schaden getrennt von Leseunsicherheit | G2 | **kein Test bekannt** |
| EDIT-001 | Diplomatischer Text getrennt von Ansicht | G2 | **kein Test bekannt** |
| EDIT-002 | Seiten, Zeilen, Lesefolge bleiben erhalten | G2 | **kein Test bekannt** |
| EDIT-003 | Text, Befund, Ergänzung, Normalform getrennt | G2 | **kein Test bekannt** |
| MET-001 | Geschriebene Zahl getrennt vom Wert | G2 | **kein Test bekannt** |
| MET-004 | Rechnungszeichen bleiben Befund | G2 | Fachurteil |
| ONO-001 | Namensform getrennt von Person oder Ort | G2 | **kein Test bekannt** |
| PAL-001 | Unsichere Zeichen erst verorten | G2 | **kein Test bekannt** |
| PAL-005 | Zeichen, Kürzung, Auflösung getrennt | G2 | **kein Test bekannt** |
| PAL-006 | Zahlen und Maße als eigene Zeichensysteme | G2 | **kein Test bekannt**, Fachurteil |
| PHIL-002 | Kürzel und Auflösung getrennt | G2 | **kein Test bekannt** |
| PHIL-003 | Unsichere Worttrennung darstellbar | G2 | **kein Test bekannt** |
| UX-003 | Diplomatischer Text in Lesefolge lesbar | G2 | **kein Test bekannt**, Prüfung im Gebrauch |

### B-02 Einordnen: das Gelesene im historischen Kontext verstehen; Bilderkennung allein genügt nicht.

O-Ton (wörtlich): „Es geht nicht um reine Bilderkennung beim Lesen der Quelle - und selbst wenn ich weiß, was da steht, kann ich es trotzdem nicht einordnen“

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| UX-006 | Aussagearten erkennbar | immer | Prüfung im Gebrauch |
| ARCH-010 | Schriftstückart und Stufe unterscheiden | G1 | Fachurteil |
| ONO-001 | Namensform getrennt von Person oder Ort | G2 | **kein Test bekannt** |
| ONO-002 | Identifizierungsstatus unabhängig von Lesung | G2 | **kein Test bekannt** |
| PHIL-008 | Wort, Normalform, Identifizierung mit eigenem Status | G2 | **kein Test bekannt** |
| HIST-003 | Überlieferung nur mit Beleg, nicht aus Kontext | G4 | **kein Test bekannt**, Fachurteil |
| ARCH-011 | Erwähnung, Mitwirkung, Amt, Schreiber trennen | G6 | **kein Test bekannt**, Fachurteil |
| DOM-003 | Fachaussagen mit eingesehenem Beleg | G6 | **kein Test bekannt** |
| DOM-005 | Quellenbegriff getrennt von Fachbegriff | G6 | Fachurteil |
| HIST-002 | Entstehungskontext nur so weit belegt | G6 | Fachurteil |
| HIST-006 | Weg von der Aussage zum Beleg | G6 | **kein Test bekannt** |
| HIST-011 | Bei Datierung sagen, was datiert wird | G6 | **kein Test bekannt**, Fachurteil |
| MET-002 | Menge, Einheit, Buchungszweck getrennt | G6 | **kein Test bekannt**, Fachurteil |
| MET-006 | Umrechnungen nur für Zeit und Ort belegt | G6 | Fachurteil |
| ONO-005 | Gleichnamige nach Zeit, Ort, Amt trennen | G6 | Fachurteil |
| PHIL-007 | Bedeutung nach Zeit und Kontext | G6 | Fachurteil |

### B-03 Richtigkeit: Ergebnisse sind richtig, damit er die richtigen Schlüsse für seine Forschung zieht.

O-Ton (wörtlich): „es soll richtig sein und ich die richtigen Schlüsse für meine Forschung ziehen“

- Pain **P-13** Raten: Die KI ergänzt, statt zu belegen. (O-Ton: „Du rätst“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-005 | KI lässt Offenes offen statt zu vervollständigen | immer | **kein Test bekannt** |
| ARCH-001 | Stabile Identität jeder Quelle | immer | Test genannt (1), Fachurteil |
| ARCH-002 | Provenienz getrennt von Quelle und Deutung | immer | Fachurteil |
| COD-009 | Materialbefund getrennt von Schluss | immer | Fachurteil |
| DOM-002 | Gattungswissen ist kein Lesebeleg | immer | Fachurteil |
| HIST-001 | Befund, Katalog, Identifizierung, Deutung getrennt | immer | Test genannt (1), Fachurteil |
| MET-009 | Wirtschaftliche Plausibilität erst nach Zeichenbefund | immer | Fachurteil |
| PAL-009 | Schriftbefund getrennt von Kontextschluss | immer | Fachurteil |
| PHIL-001 | Handschriftliche Form bleibt vorrangig | immer | **kein Test bekannt**, Fachurteil |
| PHIL-004 | Historische Schreibung bleibt erhalten | immer | **kein Test bekannt** |
| PHIL-006 | Plausibilität erst nach Schriftbefund | immer | Fachurteil |
| RSE-010 | Automatik schreibt weniger, als Fachurteil entscheidet | immer | **kein Test bekannt**, Fachurteil |
| ARCH-006 | Quellenbeziehungen sind belegte Aussagen | G1 | Test genannt (2), Fachurteil |
| AI-004 | Blindlesung ohne Vorwissen | G2 | Test genannt (2) |
| EDIT-001 | Diplomatischer Text getrennt von Ansicht | G2 | **kein Test bekannt** |
| EDIT-002 | Seiten, Zeilen, Lesefolge bleiben erhalten | G2 | **kein Test bekannt** |
| EDIT-003 | Text, Befund, Ergänzung, Normalform getrennt | G2 | **kein Test bekannt** |
| ONO-004 | Identifizierung mit Beleg, nicht nach Gleichklang | G2 | **kein Test bekannt** |
| PAL-005 | Zeichen, Kürzung, Auflösung getrennt | G2 | **kein Test bekannt** |
| PAL-006 | Zahlen und Maße als eigene Zeichensysteme | G2 | **kein Test bekannt**, Fachurteil |
| PAL-007 | Alternativen und Verworfenes bleiben sichtbar | G2 | **kein Test bekannt** |
| PAL-003 | Gleicher Kontext ist nicht gleiche Hand | G3 | Fachurteil |
| PAL-004 | Unterscheidende Schriftmerkmale festhalten | G3 | **kein Test bekannt**, Fachurteil |
| PHIL-005 | Wortbedeutung mit eingesehenem Beleg | G3 | **kein Test bekannt** |
| EDIT-004 | Jeder Textzeuge erst für sich gelesen | G4 | **kein Test bekannt**, Fachurteil |
| EDIT-005 | Entsprechungen zwischen Zeugen belegt zuordnen | G4 | **kein Test bekannt** |
| HIST-003 | Überlieferung nur mit Beleg, nicht aus Kontext | G4 | **kein Test bekannt**, Fachurteil |
| ARCH-011 | Erwähnung, Mitwirkung, Amt, Schreiber trennen | G6 | **kein Test bekannt**, Fachurteil |
| HIST-002 | Entstehungskontext nur so weit belegt | G6 | Fachurteil |
| HIST-004 | Bestätigung nur durch unabhängige Belege | G6 | Fachurteil |
| HIST-011 | Bei Datierung sagen, was datiert wird | G6 | **kein Test bekannt**, Fachurteil |
| MET-002 | Menge, Einheit, Buchungszweck getrennt | G6 | **kein Test bekannt**, Fachurteil |
| MET-006 | Umrechnungen nur für Zeit und Ort belegt | G6 | Fachurteil |
| ARCH-008 | Fehlanzeige nur mit dokumentierter Suche | Auslöser: Vollständigkeits- oder Fehlanzeige | **kein Test bekannt** |
| GWP-007 | Vollständigkeit nur mit Suchgrenzen | Auslöser: Vollständigkeits- oder Fehlanzeige | **kein Test bekannt** |
| HIST-005 | Schweigen der Quellen nur mit Suchgrenzen | Auslöser: Vollständigkeits- oder Fehlanzeige | **kein Test bekannt** |

### B-04 Mitlesen: die entstehenden Forschungsdaten lesen und den Fortschritt sehen können; zuerst aber das Repo reparieren.

O-Ton (abgeleitet): „Gerade versuche die entstehenden Forschungsdaten mitzulesen.“

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| UX-002 | Aktive Quelle und Stelle ohne Technikwissen sichtbar | immer | Prüfung im Gebrauch |
| UX-007 | Stufe, Lücken, nächster Schritt ohne Chat sichtbar | immer | **kein Test bekannt**, Prüfung im Gebrauch |
| EDIT-008 | Lesbare Ansicht aus den Daten erzeugt | G2 | **kein Test bekannt** |
| GWP-010 | Ausgaben aus den Daten erzeugt, nie von Hand doppelt | G2 | Test genannt (2) |
| RSE-006 | Ansichten werden erzeugt, nicht gepflegt | G2 | **kein Test bekannt** |
| UX-003 | Diplomatischer Text in Lesefolge lesbar | G2 | **kein Test bekannt**, Prüfung im Gebrauch |
| UX-004 | Unsicheres, Ergänztes, Eingriffe sichtbar | G2 | **kein Test bekannt**, Prüfung im Gebrauch |
| UX-009 | Ansichten sind abgeleitet, keine zweite Wahrheit | G2 | Test genannt (2) |

### B-05 Verlässlichkeit: Transparenz, Vertrauen und Verlässlichkeit; Unsicherheit wird benannt.

O-Ton (wörtlich): „ich brauche Transparenz, Vertrauen und Verlässlichkeit - Unsicherheit muss benannt werden“

- Pain **P-03** Fehler summieren sich: KI-Fehler häufen sich, Behobenes kommt wieder. (O-Ton: „Das repo ist auch schon voll großer und kleiner KI Bugs, die sich aufsummieren“)
- Pain **P-05** Kreisen ohne Transparenz: Pläne klingen plausibel, dann kommt kein Fortschritt; das wiederholt sich. (O-Ton: „dieser ist für mich nicht wirklich transparent“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-005 | KI lässt Offenes offen statt zu vervollständigen | immer | **kein Test bekannt** |
| AI-008 | Feste Fehlerklassen prüft ein Werkzeug, nicht die KI | immer | Test genannt (3) |
| ARCH-005 | Katalog, Schluss und Autopsie unterscheiden | immer | Test genannt (2) |
| DOM-009 | Erfahrungswissen als offene Fragen, nicht als Schluss | immer | **kein Test bekannt** |
| GWP-003 | Beleg, Metadaten, Hinweis, KI-Hypothese unterscheidbar | immer | Test genannt (1) |
| HIST-001 | Befund, Katalog, Identifizierung, Deutung getrennt | immer | Test genannt (1), Fachurteil |
| RSE-010 | Automatik schreibt weniger, als Fachurteil entscheidet | immer | **kein Test bekannt**, Fachurteil |
| UX-007 | Stufe, Lücken, nächster Schritt ohne Chat sichtbar | immer | **kein Test bekannt**, Prüfung im Gebrauch |
| COD-002 | Nicht untersucht, nicht sichtbar, nicht vorhanden unterscheiden | G2 | Test genannt (1) |
| COD-005 | Schaden getrennt von Leseunsicherheit | G2 | **kein Test bekannt** |
| ONO-002 | Identifizierungsstatus unabhängig von Lesung | G2 | **kein Test bekannt** |
| ONO-003 | Mehrere Kandidaten und Verworfenes darstellbar | G2 | **kein Test bekannt** |
| PAL-001 | Unsichere Zeichen erst verorten | G2 | **kein Test bekannt** |
| PAL-007 | Alternativen und Verworfenes bleiben sichtbar | G2 | **kein Test bekannt** |
| PHIL-003 | Unsichere Worttrennung darstellbar | G2 | **kein Test bekannt** |
| PHIL-008 | Wort, Normalform, Identifizierung mit eigenem Status | G2 | **kein Test bekannt** |
| UX-004 | Unsicheres, Ergänztes, Eingriffe sichtbar | G2 | **kein Test bekannt**, Prüfung im Gebrauch |
| UX-005 | Vom Ergebnis zum Beleg durchklicken | G2 | **kein Test bekannt** |
| PAL-010 | Offene Lesung ist gültig; Fachprüfung benennen | G3 | Fachurteil |
| UX-008 | Fachprüfstatus getrennt von KI-Arbeit sichtbar | G3 | **kein Test bekannt** |
| DOM-006 | Mehrere Deutungen zulassen | G6 | Fachurteil |
| HIST-007 | Alternative Deutungen bleiben sichtbar | G6 | Fachurteil |
| HIST-008 | Vorläufige Kontextannahmen behalten Status | G6 | **kein Test bekannt** |
| MET-003 | Unsicherheit je Schritt der Wertbestimmung | G6 | **kein Test bekannt** |
| MET-008 | Alternative Einheiten sichtbar | G6 | Fachurteil |
| ONO-006 | Widersprüchliche Identifizierungen nebeneinander | G6 | **kein Test bekannt** |
| ARCH-008 | Fehlanzeige nur mit dokumentierter Suche | Auslöser: Vollständigkeits- oder Fehlanzeige | **kein Test bekannt** |
| GWP-007 | Vollständigkeit nur mit Suchgrenzen | Auslöser: Vollständigkeits- oder Fehlanzeige | **kein Test bekannt** |
| HIST-005 | Schweigen der Quellen nur mit Suchgrenzen | Auslöser: Vollständigkeits- oder Fehlanzeige | **kein Test bekannt** |

### B-06 Herkunft: Es bleibt nachvollziehbar, woher jede Aussage stammt (Quelle, KI oder Eigentümer).

O-Ton (abgeleitet): „Immer Provinenz erhalten, Nachvollzihebarkeit.“

- Pain **P-10** Unklare Herkunft: Es ist nicht erkennbar, was von der KI kommt und was O-Ton ist. (O-Ton: „Es ist auch nicht klar, was kommt von der KI, was sind meine O-Töne“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-003 | KI-Ausgabe, Beleg, Schluss, Prüfung unterscheiden | immer | **kein Test bekannt** |
| AI-006 | KI-Schritte mit angemessener Herkunft | immer | **kein Test bekannt** |
| ARCH-001 | Stabile Identität jeder Quelle | immer | Test genannt (1), Fachurteil |
| ARCH-002 | Provenienz getrennt von Quelle und Deutung | immer | Fachurteil |
| ARCH-003 | Geprüfte Datei getrennt vom Archivale | immer | Test genannt (3) |
| ARCH-005 | Katalog, Schluss und Autopsie unterscheiden | immer | Test genannt (2) |
| ARCH-007 | Forschungsfunktion gilt nur im Projekt | immer | **kein Test bekannt** |
| COD-006 | Objekt getrennt vom Digitalisat | immer | Test genannt (2) |
| GWP-002 | Belege bis zu Quelle, Datei, Stelle rückverfolgbar | immer | Test genannt (2) |
| GWP-003 | Beleg, Metadaten, Hinweis, KI-Hypothese unterscheidbar | immer | Test genannt (1) |
| GWP-004 | Revisionen bleiben rekonstruierbar | immer | Test genannt (1) |
| GWP-005 | Sichtbar, wer was gemacht und geprüft hat | immer | **kein Test bekannt** |
| RSE-004 | Stabile IDs mit Referenzprüfung | immer | Test genannt (2) |
| RSE-008 | Umwandlungen behalten Herkunft und Entscheidungen | immer | **kein Test bekannt** |
| ARCH-004 | Folio, Bild, PDF-Seite getrennt zuordnen | G1 | Test genannt (3) |
| ARCH-006 | Quellenbeziehungen sind belegte Aussagen | G1 | Test genannt (2), Fachurteil |
| COD-001 | Materielles nur, wenn sichtbar und relevant | G1 | Fachurteil |
| COD-003 | Zählung aus dem Befund, nicht aus der PDF | G1 | Test genannt (2) |
| COD-007 | Bildableitungen behalten ihre Herkunft | G1 | **kein Test bekannt** |
| ARCH-009 | Eindeutige Adresse für jede Belegstelle | G2 | **kein Test bekannt** |
| EDIT-006 | Lesentscheidungen und Revisionen nachvollziehbar | G2 | Test genannt (2) |
| ONO-009 | Entscheidungen zu Namen mit Begründung | G2 | **kein Test bekannt** |
| UX-005 | Vom Ergebnis zum Beleg durchklicken | G2 | **kein Test bekannt** |
| MET-005 | Zahlschlüsse mit Stelle und Vergleich | G3 | **kein Test bekannt** |
| PAL-002 | Vergleichsstellen genau wiederfinden | G3 | **kein Test bekannt** |
| PAL-008 | Bildvergleich auf genaues Bild zurückführen | G3 | **kein Test bekannt** |
| PHIL-005 | Wortbedeutung mit eingesehenem Beleg | G3 | **kein Test bekannt** |
| EDIT-007 | Apparat, wenn das Editionskonzept ihn verlangt | G5 | **kein Test bekannt** |
| EDIT-010 | Jede Ausgabe führt zum Beleg zurück | G5 | **kein Test bekannt** |
| DOM-003 | Fachaussagen mit eingesehenem Beleg | G6 | **kein Test bekannt** |
| HIST-006 | Weg von der Aussage zum Beleg | G6 | **kein Test bekannt** |
| HIST-009 | Sekundärliteratur mit eingesehener Stelle | G6 | **kein Test bekannt** |
| MET-007 | Umrechnungsquelle genau angeben | G6 | **kein Test bekannt** |
| ONO-008 | Normdaten sind Verknüpfung, kein Beleg | Auslöser: Verknüpfung mit Normdaten | **kein Test bekannt** |

### B-07 Echte Funktion: Was als umgesetzt gilt, funktioniert tatsächlich und ist prüfbar.

O-Ton (abgeleitet): „ich erwarte funktionalität, wo keine Ist“

- Pain **P-01** Prosa statt Funktion: Modelle antworten mit Text und behaupten Umsetzungen, die es nicht gibt. (O-Ton: „die Modelle reagieren mit Prosa, behaupten umgesetzt zu haben, was sie nicht gemacht haben“)
- Pain **P-02** Regel statt Lösung: Wo er Funktion erwartet und keine ist, antwortet er mit einer neuen Regel; die Lücke bleibt. (O-Ton: „ich erwarte funktionalität, wo keine Ist und das beantworte ich mit einer neuen Regel.“)
- Pain **P-03** Fehler summieren sich: KI-Fehler häufen sich, Behobenes kommt wieder. (O-Ton: „Das repo ist auch schon voll großer und kleiner KI Bugs, die sich aufsummieren“)
- Pain **P-06** Beschreiben statt beheben: Die KI beschreibt ihre Mängel, statt den ersten Schritt zur Behebung zu tun. (O-Ton: „Die KI ist top ihre eigene Unzulänglichkeit zu beschreiben“)
- Pain **P-14** Tun statt Funktion: Nach erkannten Grundproblemen geht die laufende Arbeit weiter, ohne fehlende Funktionen nachzulegen. (O-Ton: „und du sagst gerade weiter im text“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-008 | Feste Fehlerklassen prüft ein Werkzeug, nicht die KI | immer | Test genannt (3) |
| RSE-001 | Jedes Werkzeug dient einer Anforderung | immer | **kein Test bekannt** |
| EDIT-008 | Lesbare Ansicht aus den Daten erzeugt | G2 | **kein Test bekannt** |
| GWP-010 | Ausgaben aus den Daten erzeugt, nie von Hand doppelt | G2 | Test genannt (2) |
| RSE-006 | Ansichten werden erzeugt, nicht gepflegt | G2 | **kein Test bekannt** |
| UX-009 | Ansichten sind abgeleitet, keine zweite Wahrheit | G2 | Test genannt (2) |

### B-08 Fachkunde: die echte Fachkunde der beteiligten Fächer nachbilden, nicht das Bild eines Fachmanns, als Innehalten und Kompass für Entscheidungen. Die Formulierung stammt aus Claudes Audit; der Eigentümer greift sie auf.

O-Ton (abgeleitet): „Das sollten wir versuchen“

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-001 | Vor dem Handeln alles Geltende laden | immer | Test genannt (2) |
| DOM-001 | Zuständige Fachgebiete benennen | immer | **kein Test bekannt** |
| DOM-009 | Erfahrungswissen als offene Fragen, nicht als Schluss | immer | **kein Test bekannt** |
| GWP-011 | Begriffe behalten beim Übersetzen ihre Bedeutung | immer | Fachurteil |

### B-09 Verstehen und entscheiden: Vorschläge so verstehen, dass er über sie entscheiden kann.

O-Ton (abgeleitet): „wenn mir was vorgeschlagen wird, wo ich glaube das es hilft mache ich es“

- Pain **P-11** Unverständlich: Sätze und Vorschläge sind für ihn nicht verständlich. (O-Ton: „DAs verstehe ich nicht“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-007 | Schreibgrenzen nach Tragweite | immer | **kein Test bekannt** |
| GWP-011 | Begriffe behalten beim Übersetzen ihre Bedeutung | immer | Fachurteil |
| UX-006 | Aussagearten erkennbar | immer | Prüfung im Gebrauch |
| UX-011 | Forschen, ohne Repo-Technik zu bedienen | immer | Prüfung im Gebrauch |
| UX-012 | Jeder Schritt in Alltagssprache erklärbar | immer | Prüfung im Gebrauch |

### B-10 Ursachen: bei Problemen die eigentliche Ursache finden, nicht das Symptom behandeln.

O-Ton (wörtlich): „Zentral: sind es symtome, oder die tatsächlichen Ursachen“

- Pain **P-02** Regel statt Lösung: Wo er Funktion erwartet und keine ist, antwortet er mit einer neuen Regel; die Lücke bleibt. (O-Ton: „ich erwarte funktionalität, wo keine Ist und das beantworte ich mit einer neuen Regel.“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| RSE-001 | Jedes Werkzeug dient einer Anforderung | immer | **kein Test bekannt** |

### B-11 Methodik und Bestand: sorgfältig und behutsam arbeiten und auf vorhandener Methodik und Struktur aufbauen.

O-Ton (abgeleitet): „Wir haben denk ich schon gute Strutkturen, siehe Visitationsprotokolle“

- Pain **P-06** Beschreiben statt beheben: Die KI beschreibt ihre Mängel, statt den ersten Schritt zur Behebung zu tun. (O-Ton: „Die KI ist top ihre eigene Unzulänglichkeit zu beschreiben“)
- Pain **P-08** Methodenverlust: Er sieht seit Nr. 632 einen Verlust an Methode. (O-Ton: „da finde ich seit 632 auch ein methodenverlust passiert“)
- Pain **P-09** Vollgas ohne Behutsamkeit: ungesehen losarbeiten, ohne sich der Risiken bewusst zu sein. (O-Ton: „das du ungesehen da mit vollgas reingelaufen bist“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| AI-001 | Vor dem Handeln alles Geltende laden | immer | Test genannt (2) |
| AI-002 | Kürzen ohne geltende Regel zu verlieren | immer | **kein Test bekannt** |
| AI-007 | Schreibgrenzen nach Tragweite | immer | **kein Test bekannt** |
| GWP-009 | Methoden und Standards mit Fassung benannt | immer | **kein Test bekannt** |

### B-12 Auffindbar und aktuell: Wissen ist auffindbar, Startdateien sind aktuell; aufräumen, ohne Kontext zu verlieren.

O-Ton (abgeleitet): „Wo können wir auch einen sauberen clean-up ansetzen, ohne Kontext zu verlieren“

- Pain **P-07** Verstreut und veraltet: Wissen ist verstreut, Startdateien sind nicht gepflegt. (O-Ton: „Das wissen ist sicher auch komplett verstreut“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| GWP-001 | Jeder Stand hat genau einen Ort | immer | Test genannt (2) |
| GWP-008 | Ohne alten Chat wieder aufnehmbar | immer | Test genannt (2) |
| RSE-002 | Daten einfach, lesbar, portabel | immer | Fachurteil |
| RSE-003 | Forschungsstand getrennt von Ansichten | immer | Test genannt (1) |
| UX-001 | Kurzer Weg vom Zweck zum Ergebnis | immer | Prüfung im Gebrauch |
| RSE-007 | Vor Formatwechsel Verlusttest | Auslöser: Wechsel des Datenformats | Test genannt (1) |

### B-13 Fortschritt und Frühwarnung: erkennbarer Fortschritt statt Kreisen; früh gewarnt werden, wenn es hängt.

O-Ton (abgeleitet): „Erhebe Kriterien und Prüfmechanismen, die dir erlauben, frühzeitig gewarnt zu werden.“

- Pain **P-04** Festfahren: Jede Runde baut neue Strukturen und frisst sich an teils trivialen Problemen fest. (O-Ton: „aber jede runde Schafft neue Strukturen“)
- Pain **P-05** Kreisen ohne Transparenz: Pläne klingen plausibel, dann kommt kein Fortschritt; das wiederholt sich. (O-Ton: „dieser ist für mich nicht wirklich transparent“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| RSE-001 | Jedes Werkzeug dient einer Anforderung | immer | **kein Test bekannt** |
| RSE-005 | Feste Wertlisten nur für Wiederkehrendes | immer | Fachurteil |
| UX-007 | Stufe, Lücken, nächster Schritt ohne Chat sichtbar | immer | **kein Test bekannt**, Prüfung im Gebrauch |

### B-14 Lesewerkzeug: für Handschriften das nötige Werkzeug, Erfahrungswissen und den Stand der Technik.

O-Ton (abgeleitet): „hast du überhaupt das nötige tooling für das lesen der handschriften .. das erfahrungswissen und sota?“

- Pain **P-12** Klares bleibt ungelesen: Bei Nr. 632 wurde auch klar Geschriebenes nicht gelesen. (O-Ton: „wieso kannst du klar geschriebene nr4 nicht lesen“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| GWP-009 | Methoden und Standards mit Fassung benannt | immer | **kein Test bekannt** |
| MET-005 | Zahlschlüsse mit Stelle und Vergleich | G3 | **kein Test bekannt** |
| PAL-002 | Vergleichsstellen genau wiederfinden | G3 | **kein Test bekannt** |
| PAL-003 | Gleicher Kontext ist nicht gleiche Hand | G3 | Fachurteil |
| PAL-004 | Unterscheidende Schriftmerkmale festhalten | G3 | **kein Test bekannt**, Fachurteil |
| PAL-008 | Bildvergleich auf genaues Bild zurückführen | G3 | **kein Test bekannt** |
| AI-009 | KI-Lesen im großen Stil vorher erproben | Auslöser: KI- oder HTR-Lesung in großem Umfang | **kein Test bekannt** |

### B-15 Fachleute fragen: bei Bedarf gezielt befreundete Historiker fragen können.

O-Ton (abgeleitet): „da würde ich befreundete historiker fragen“

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| PAL-010 | Offene Lesung ist gültig; Fachprüfung benennen | G3 | Fachurteil |
| UX-008 | Fachprüfstatus getrennt von KI-Arbeit sichtbar | G3 | **kein Test bekannt** |
| DOM-010 | Fachprüfung der Domänenaussage ausweisen | G6 | Fachurteil |
| HIST-010 | Historische Fachprüfung ausweisen | G6 | Fachurteil |
| MET-010 | Fachprüfung bei seltenen Zeichen ausweisen | G6 | Fachurteil |
| ONO-010 | Fachprüfung bei strittigen Namen ausweisen | G6 | Fachurteil |
| AI-010 | Fachprüfung mit genauen Belegpaketen; Eigentümer ist kein Fachprüfer | Auslöser: folgenreiche Fachfrage | **kein Test bekannt** |
| COD-008 | Lagen, Bindung, Wasserzeichen nur mit Befund | Auslöser: Frage nach Lage, Bindung oder Wasserzeichen | Fachurteil |
| COD-010 | Vor-Ort-Prüfung als ausdrückliche Eskalation | Auslöser: digital nicht entscheidbar | Fachurteil |
| PHIL-010 | Sprachliche Fachprüfung ausweisen | Auslöser: folgenreiche sprachliche Bestimmung | **kein Test bekannt**, Fachurteil |
| UX-010 | Fachprüfung sieht Stelle, Kandidaten, Belege | Auslöser: folgenreiche Fachfrage | **kein Test bekannt** |

### B-16 Vom Bedürfnis zur prüfbaren Lösung: Entwicklung geht vom Bedürfnis aus, wird umgesetzt und ist prüfbar; jede Perspektive wird einmal bedacht.

O-Ton (abgeleitet): „In meiner Welt ist user research der zentrale Motor für entwicklung“

- Pain **P-14** Tun statt Funktion: Nach erkannten Grundproblemen geht die laufende Arbeit weiter, ohne fehlende Funktionen nachzulegen. (O-Ton: „und du sagst gerade weiter im text“)
- Pain **P-15** Absicht ungeprüft: Prüfungen zeigen nicht, ob die Absicht erreicht ist. (O-Ton: „Absicht nicht geprüft“)

| Anforderung | Kurz | gilt ab | Prüfung |
|---|---|---|---|
| RSE-001 | Jedes Werkzeug dient einer Anforderung | immer | **kein Test bekannt** |
| RSE-005 | Feste Wertlisten nur für Wiederkehrendes | immer | Fachurteil |
| RSE-009 | Aufwand und Abhängigkeiten nach echtem Bedarf | immer | Fachurteil |

### B-17 Querbeziehungen: was schon gelesen ist, hilft beim Lesen und Verstehen der nächsten Stellen.

O-Ton (abgeleitet): „dann müssen dich querbeziehungen erkenntnisse schaffen“

**Keine Anforderung dient diesem Bedürfnis.** Das ist eine Lücke.

## Lücken nach Stufe

Prüfbare Anforderungen ohne bekannten Test, geordnet danach, ab wann sie gelten.

| gilt ab | Anforderung | Kurz | dient | braucht zuerst |
|---|---|---|---|---|
| immer | ARCH-007 | Forschungsfunktion gilt nur im Projekt | B-06 |  |
| immer | PHIL-001 | Handschriftliche Form bleibt vorrangig | B-01, B-03 |  |
| immer | PHIL-004 | Historische Schreibung bleibt erhalten | B-01, B-03 |  |
| immer | DOM-001 | Zuständige Fachgebiete benennen | B-08 |  |
| immer | DOM-009 | Erfahrungswissen als offene Fragen, nicht als Schluss | B-08, B-05 |  |
| immer | GWP-005 | Sichtbar, wer was gemacht und geprüft hat | B-06, P-10 |  |
| immer | GWP-009 | Methoden und Standards mit Fassung benannt | B-14, B-11 |  |
| immer | RSE-001 | Jedes Werkzeug dient einer Anforderung | B-16, P-02, P-04 |  |
| immer | RSE-008 | Umwandlungen behalten Herkunft und Entscheidungen | B-06 |  |
| immer | RSE-010 | Automatik schreibt weniger, als Fachurteil entscheidet | B-03, B-05 |  |
| immer | AI-002 | Kürzen ohne geltende Regel zu verlieren | B-11 |  |
| immer | AI-003 | KI-Ausgabe, Beleg, Schluss, Prüfung unterscheiden | B-06, P-10 |  |
| immer | AI-005 | KI lässt Offenes offen statt zu vervollständigen | B-05, P-13 |  |
| immer | AI-006 | KI-Schritte mit angemessener Herkunft | B-06 |  |
| immer | AI-007 | Schreibgrenzen nach Tragweite | B-09, P-09 |  |
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
| G2 | COD-004 | Layout, Randnotizen, Lesefolge darstellbar | B-01 |  |
| G2 | COD-005 | Schaden getrennt von Leseunsicherheit | B-05, B-01 |  |
| G2 | ONO-001 | Namensform getrennt von Person oder Ort | B-01, B-02 |  |
| G2 | ONO-002 | Identifizierungsstatus unabhängig von Lesung | B-02, B-05 |  |
| G2 | ONO-003 | Mehrere Kandidaten und Verworfenes darstellbar | B-05 |  |
| G2 | ONO-004 | Identifizierung mit Beleg, nicht nach Gleichklang | B-03, P-13 | ONO-001, ONO-002 |
| G2 | ONO-009 | Entscheidungen zu Namen mit Begründung | B-06 | ONO-003 |
| G2 | MET-001 | Geschriebene Zahl getrennt vom Wert | B-01 |  |
| G2 | RSE-006 | Ansichten werden erzeugt, nicht gepflegt | B-04, B-07 |  |
| G2 | UX-003 | Diplomatischer Text in Lesefolge lesbar | B-04, B-01 | EDIT-008, EDIT-002 |
| G2 | UX-004 | Unsicheres, Ergänztes, Eingriffe sichtbar | B-04, B-05 | UX-003, EDIT-003, PAL-001, PAL-007 |
| G2 | UX-005 | Vom Ergebnis zum Beleg durchklicken | B-06, B-05 | GWP-002, EDIT-006 |
| G3 | PAL-002 | Vergleichsstellen genau wiederfinden | B-06, B-14 | ARCH-009 |
| G3 | PAL-004 | Unterscheidende Schriftmerkmale festhalten | B-03, B-14 | PAL-001, PAL-002 |
| G3 | PAL-008 | Bildvergleich auf genaues Bild zurückführen | B-06, B-14 | COD-007 |
| G3 | PHIL-005 | Wortbedeutung mit eingesehenem Beleg | B-06, P-13 |  |
| G3 | MET-005 | Zahlschlüsse mit Stelle und Vergleich | B-06, B-14 | PAL-002 |
| G3 | UX-008 | Fachprüfstatus getrennt von KI-Arbeit sichtbar | B-15, B-05 | GWP-005 |
| G4 | EDIT-004 | Jeder Textzeuge erst für sich gelesen | B-03 | EDIT-001 |
| G4 | EDIT-005 | Entsprechungen zwischen Zeugen belegt zuordnen | B-03 | EDIT-004, ARCH-009 |
| G4 | HIST-003 | Überlieferung nur mit Beleg, nicht aus Kontext | B-02, B-03 |  |
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
- AI-003 KI-Ausgabe, Beleg, Schluss, Prüfung unterscheiden; GWP-003 Beleg, Metadaten, Hinweis, KI-Hypothese unterscheidbar

## Tests ohne Anforderung

Testdateien, aus denen keine Anforderung einen Test nennt. Sie können trotzdem nötig sein; dann fehlt ihre Zuordnung.

- `tests/test_archival_source_acquisition.py`
- `tests/test_engineering_context.py`
- `tests/test_governance_ownership.py`
- `tests/test_metrics.py`
- `tests/test_prompt.py`
- `tests/test_recovery_assurance.py`
- `tests/test_regii3_crosswalk_restart.py`
- `tests/test_regii5_evidence_packet.py`
- `tests/test_regii5_packet_benchmark.py`
- `tests/test_regii5_visual_retrieval.py`
- `tests/test_sd_ka_wp6_qualification.py`

## Funktionen nach Rang

Welche Funktion welche Anforderungen absichert und welchen Schmerz sie lindert. Größe, Rang und Befunde je Perspektive sind ein Vorschlag der KI (`requirements/funktionen.tsv`); entscheiden tust du. **Größe:** *hoch* hält die laufende Arbeit auf oder lässt Fehler in Forschungsdaten unbemerkt; *mittel* verlangsamt oder macht intransparent; *gering* betrifft erst spätere Stufen.

| Rang | Funktion | Größe | Aufwand | sichert | lindert | braucht | Stand | Issue |
|---:|---|---|---|---|---|---|---|---|
| 1 | FN-01 Zeilenformat-Prüfer | hoch | klein | EDIT-001, EDIT-002, EDIT-003, ARCH-009, PAL-001, PAL-005, PAL-006, PAL-007, PHIL-002, PHIL-003, COD-004, COD-005, MET-001, AI-005 | B-01, B-03, B-05, P-01, P-08 |  | Vorschlag |  |
| 2 | FN-02 Leseansicht | hoch | mittel | EDIT-008, RSE-006, UX-003, UX-004, UX-005, PHIL-001, PHIL-004 | B-04, B-01, P-01, P-11 | FN-01 | Vorschlag |  |
| 3 | FN-03 G3-Prüftabelle für strittige Stellen | hoch | mittel | PAL-002, PAL-004, PAL-008, PAL-010, MET-005 | B-03, B-14, B-15, P-13 | FN-01 | Vorschlag |  |
| 4 | FN-04 Namen: Lesung und Identifizierung getrennt | mittel | mittel | ONO-001, ONO-002, ONO-003, ONO-004, ONO-009, PHIL-008 | B-02, B-06, P-13 | FN-01 | Vorschlag |  |
| 5 | FN-05 Querbezüge im Gelesenen | mittel | mittel | PHIL-005 | B-17, P-12, B-14 | FN-01 | Vorschlag |  |
| 6 | FN-06 Gegenlesung zielgenau, Lesequalität messbar | mittel | klein | AI-004, EDIT-006, UX-008, GWP-005 | B-03, B-05, B-13, P-12, P-13 | FN-01, FN-03 | Vorschlag |  |
| 7 | FN-07 Stand auf einen Blick | mittel | mittel | UX-007, UX-001 | B-12, B-13, B-04, P-05, P-07 | FN-01, FN-06 | Vorschlag |  |
| 8 | FN-08 Bildausschnitt für jedes Projekt | mittel | groß | COD-007 | B-14, B-01 | FN-01 | Vorschlag |  |
| 9 | FN-09 Rückbau | mittel | mittel | RSE-001 | P-02, P-04, B-12 |  | Vorschlag |  |

## Lücken bis G3 ohne Funktion

Prüfbare Anforderungen bis zur Stufe G3 ohne bekannten Test, die noch keine Funktion absichert.

- ARCH-007 Forschungsfunktion gilt nur im Projekt (immer)
- DOM-001 Zuständige Fachgebiete benennen (immer)
- DOM-009 Erfahrungswissen als offene Fragen, nicht als Schluss (immer)
- GWP-006 Rechte und Zugangsgrenzen ausdrücklich (G1)
- GWP-009 Methoden und Standards mit Fassung benannt (immer)
- RSE-008 Umwandlungen behalten Herkunft und Entscheidungen (immer)
- RSE-010 Automatik schreibt weniger, als Fachurteil entscheidet (immer)
- AI-002 Kürzen ohne geltende Regel zu verlieren (immer)
- AI-003 KI-Ausgabe, Beleg, Schluss, Prüfung unterscheiden (immer)
- AI-006 KI-Schritte mit angemessener Herkunft (immer)
- AI-007 Schreibgrenzen nach Tragweite (immer)
