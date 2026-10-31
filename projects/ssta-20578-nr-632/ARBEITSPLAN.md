Eigentümerentscheidung vom 31.10.2026; gilt bis zu meiner nächsten Änderung

Dies ist mein Gesamtplan als Eigentümer für Nr. 632 und für Werkzeuge. Er ersetzt keine
Regeln des Repos. Er ordnet nur Reihenfolge und Zuständigkeit.

ROLLEN
- Ich (Eigentümer): Ziel, Reihenfolge, Freigaben. Ich lese keine Handschrift.
- Astra-Arbeitschat (du): liest, baut, sichert.
- Astra-Gegenlese-Chat: liest blind gegen (eigener Prompt, kennt deine Lesung nicht).
- Claude: prüft jeden PR, macht gelegentlich Stichproben, prüft Zwischenstände vor dem
  Übernehmen auf main.
Keine Fachleute nötig. Ergebnisse heißen „KI-Arbeitslesung, blind gegengeprüft“.

=== SPUR F · FACHLICHE ARBEIT (Vorrang) ===

F1 · Gesuch 0104R–0107L fertigstellen
  Seite für Seite im Arbeitsrhythmus aus #358, beginnend mit der Gegenlesung von 0104R.
  Fertig, wenn alle sechs Seiten „passt“ haben und die Übergänge am Bild bestätigt
  oder als offen markiert sind.

F2 · Methodentest (frei, aber begrenzt und gesichert)
  Ziel: herausfinden, welche Leseweise die wenigsten Fehler macht.
  Neue Datei projects/ssta-20578-nr-632/research/methodenprotokoll.md, eine Tabelle:
  Seite | Leseweise | Bildquelle (kompakt/voll) | Zeilen | Fehler in der Gegenlesung
  | davon Vereinheitlichung | grobe Dauer | Bemerkung.
  Dabei je zwei Seiten aus 0108–0131 mit verschiedenen Leseweisen neu lesen, z. B.:
    (a) ganze Seite, dann Zeilen
    (b) Zeile für Zeile in schmalen Streifen
    (c) wie (b), dazu Abgleich gleicher Buchstaben auf derselben Seite
  Danach die Leseweise mit der niedrigsten Fehlerquote zum Standard machen; das steht
  als Zeile in #358 und im STATUS.
  Das Protokoll ist Forschungsstand dieses Projekts, keine neue allgemeine Regel.

F3 · Neu lesen statt ausbessern
  0108–0131 Texteinheit für Texteinheit im Rhythmus neu lesen (Reihenfolge nach #358
  und der Objekt-/Ansichtskarte). Danach die noch offenen Bereiche aus 0001–0101.
  Mehrfachaufnahmen derselben Fläche nur einmal lesen; die anderen Aufnahmen verweisen.

F4 · Zwischenstände auf main
  Nach F1 und danach nach je etwa zwei Texteinheiten: ein Zwischenstands-PR.
  Davor:
  - Die große Datei teilen: eine Datei je Texteinheit mit passendem Namen.
    Verlusttest: Jede Zeile, Alternative und Grenze steht danach in genau einer Datei.
  - Den STATUS kurz halten.
  Claude prüft Aufbau, Herkunft und Verlusttest (nicht die Lesungen). Ich entscheide
  über das Übernehmen. Danach ein neuer Forschungsbranch.

F5 · Lesefassung erproben
  Für das fertige Gesuch eine lesbare diplomatische Fassung allein aus den
  Forschungsdateien erzeugen (zuerst von Hand oder mit einem kleinen Skript).
  Prüfen: Geht dabei etwas verloren (Zeilen, Unsicherheit, Ränder, Streichungen,
  Fundstelle)? Ergebnis ins Methodenprotokoll.

=== SPUR W · WERKZEUGE (nur aus belegter Reibung) ===

W0 · Reibung sammeln (ab sofort, kein Werkzeug)
  Jeder Abschlusskommentar eines Arbeitsblocks in #359 enthält höchstens drei Zeilen
  „Reibung:“: was Zeit, Kontext oder Fehler gekostet hat, mit Zahl, wenn möglich.
  Du überträgst sie in eine zweite Tabelle im Methodenprotokoll:
  Reibung | wie oft | Folge (Fehler/Zeit/Kontext) | möglicher Ausweg.

W1 · Entscheidungspunkt
  Nach F1 und danach alle etwa zehn Seiten: Du fasst die drei häufigsten Reibungen
  in Alltagssprache zusammen und schlägst höchstens EIN Werkzeug vor:
  - Nutzen, gemessen an der Reibungstabelle
  - Aufwand in Arbeitssitzungen
  - was es nicht darf
  Ich entscheide (das ist die Freigabe nach D-016). Ohne meine Freigabe wird nichts
  gebaut.

W2 · Bauen, wenn freigegeben, immer so:
  - eigener PR, Tests zuerst (rot, dann grün), an einer echten Seite aus Nr. 632 erprobt
  - liest nur vorhandene Projektdateien, erzeugt nur Abgeleitetes, keine zweite Wahrheit
  - in tools/check.py eingebunden; beurteilt nie eine Lesung, meldet nie ein Gate
  - Erfolg im Methodenprotokoll messen: weniger Fehler, weniger Zeit oder weniger Kontext
    als vorher. Sonst wieder entfernen.
  - Claude prüft; erst dann wird übernommen.

  Wahrscheinliche Kandidaten (nur Hinweis, Reihenfolge entscheidet die Reibung):
  - Bildausschnitt-Helfer: erzeugt aus registrierter Datei + Seite feste Zeilenstreifen,
    damit Arbeits- und Gegenlese-Chat dieselben Ausschnitte nutzen (spart Tokens).
  - Zeilendatensatz + Prüfer: feste Felder je Zeile (Fundstelle, Lesung, Status,
    Alternativen), Prüfung auf fehlende Felder und uneinheitliche Marken.
  - Lesefassung aus dem Datensatz (nach F5).
  - Abdeckungsübersicht: welche Flächen gelesen, offen, mehrfach fotografiert sind.

W3 · Einbindung
  Jedes übernommene Werkzeug: eine Zeile im Rückkehrpunkt des STATUS („so wird gelesen“).
  Keine neue Regeldatei, keine Workflow-Engine, keine Automation.

=== SOFORT ===
1. #361: Den Audit nur mit einem Nachtrag sichern (höchstens zehn Zeilen): Ergebnis der
   Stichproben 1 und 2 aus #359, und dass Abschnitt 3.4 („substantielle Arbeitslesungen“
   0112–0116) dadurch widerlegt ist. Sonst nicht übernehmen.
2. Gegenlesung 0104R durch den Gegenlese-Chat anstoßen (Zeile „bereit zur Gegenlesung“
   steht schon im STATUS); dann F1 fortsetzen.

GRENZEN
Nichts löschen. Keine neuen Regeln außerhalb dieses Projekts. Kein Gate.
Kein Übernehmen auf main ohne Claudes Prüfung und meine Entscheidung.
Jeder Block endet mit tools/work_return.py; die Ausgabe gehört in den Abschlusskommentar.

RÜCKMELDUNG
Nach jedem Block kurz in Alltagssprache: welche Seiten fertig sind, die Fehlerquote der
Gegenlesung, Reibungen, nächster Schritt.
