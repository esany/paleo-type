Eigentümerentscheidung vom 31.10.2026; gilt bis zu meiner nächsten Änderung

Dies ist mein Gesamtplan als Eigentümer für Nr. 632 und für Werkzeuge. Er ersetzt keine
Regeln des Repos. Er ordnet nur Reihenfolge und Zuständigkeit.

ROLLEN
- Ich (Eigentümer): Ziel, Reihenfolge, Freigaben. Ich lese keine Handschrift.
- Astra-Hauptchat (normaler Chat): liest, baut, sichert.
- Gegenlese-Chat (neuer normaler Chat): liest blind gegen (eigener Prompt, kennt deine Lesung nicht).
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

=== NACHTRAG 31.10.2026 · ARBEITSRHYTHMUS (vier Schritte) ===
Ergänzung zum Human-Owner-Rhythmus vom 31.10.2026 in #358; spätere
Rollenpräzisierung siehe datierten Nachtrag unten.

1. SEITE LESEN UND PRÜFPUNKTE FESTHALTEN
   Seite am registrierten Originalbild lesen, mit vergrößerten Ausschnitten.
   Die tatsächlich sichtbaren physischen Zeilen direkt am Bild zählen; keinen
   festen Zeilenraster voraussetzen. Titel, Datum, Ränder, Streichungen,
   Überlagerungen und Übergänge als eigene Prüfpunkte behandeln, soweit sichtbar.
   Historische Buchstaben-/Wortformen, Großschreibung, Abkürzungen und
   Zeilenendzeichen nicht normalisieren oder expandieren; fehlende Zeichen
   nicht nach einer bekannten Formel ergänzen. Unsicheres und Nicht-Sichtbares
   ausdrücklich unterscheiden und im bestehenden Forschungsowner auf #359
   mit der genauen Bild-/Zeilenfundstelle sichern.

2. ZUR BLINDEN GEGENLESUNG GEBEN
   Nach jeder Seite einen Commit auf dem Forschungsbranch von PR #359 sichern.
   Auf #359 ausschließlich die Zeile „bereit zur Gegenlesung: <Seite>“
   veröffentlichen, ohne Lesungstext. Ein frischer Gegenlese-Chat (neuer normaler Chat) erhält
   für die 2–3 ausgewählten Zeilen nur Bildquelle, Seite und Bild-/Zeilenlocator,
   niemals vorab die eigene Lesung. Claude kann gelegentlich zusätzlich prüfen.

3. ABWEICHUNGEN AM BILD KLÄREN
   Der Gegenlese-Chat hält seine unabhängige Lesung samt Unsicherheiten fest,
   bevor der Arbeitschat sie mit seinem Text vergleicht. Jede Abweichung an
   sichtbaren Buchstabenformen, Kürzungs- und Teilungszeichen prüfen, nicht an
   erwarteten Wörtern, Grammatik oder Lehensformeln entscheiden. Wo das Bild
   nicht unterscheidet, beide Alternativen offen markieren; stille
   Vereinheitlichungen eigens vermerken. Die Disposition samt Fundstellen
   im bestehenden Forschungsowner und Rückkehrpunkt sichern.

4. FEHLERSCHWELLE UND FORTSETZUNG
   Mehr als ein unmarkiert falsches Wort in der Stichprobe (einschließlich
   Normalisierung und stiller Abkürzungsauflösung): dieselbe Seite vor der
   nächsten Seite überarbeiten und erneut zur Gegenlesung geben.
   Andernfalls lautet das begrenzte Stichprobenurteil „passt“; es bedeutet
   weder vollständig geprüfte Seite noch fachwissenschaftliche Abnahme oder
   Gate. Offene Buchstaben, Ränder und Textübergänge bleiben offen. Qualität
   geht vor Menge; erst dann die nächste Seite im vorgegebenen Verlauf lesen.

=== NACHTRAG 31.10.2026 · PROMPT FÜR DEN GEGENLESE-CHAT ===
Den folgenden Prompt in einem NEUEN, unabhängigen normalen Chat verwenden.
Die Platzhalter werden nur mit Quelle und Bildlocators befüllt, nicht mit
Lesungstext. Es erfolgt keine automatische Chat-zu-Chat-Weitergabe.

BEGINN PROMPT
Du bist der unabhängige Gegenlese-Chat für eine KI-Arbeitslesung zu
Sächsisches Staatsarchiv Leipzig, Bestand 20578, Nr. 632.
Prüfe blind 2–3 physische Schriftzeilen der Seite <SEITE>,
Bild-/Zeilenbereich <BEREICH>, anhand der registrierten Originalbildquelle
<DATEI-ID / EXAKTE BILDQUELLE>. Die PDF-Seitennummer/Bildnummer ist
keine archivalische Foliierung.

Lies die geltenden Repo-Grenzen zur Quellenarbeit, aber sieh vor der eigenen
Lesung KEINE vorhandene Transkription, Zeilentabelle, frühere Gegenlesung
oder Formulierung des Arbeitschats zu diesen Zeilen an. Falls du solche
Lesungen bereits gesehen hast, melde das und bezeichne die Probe nicht
als blind. Betrachte das tatsächliche Schriftbild und vergrößerte
Originalausschnitte; zähle die sichtbaren physischen Zeilen selbst.
Schreibe nur, was die Buchstabenformen tragen. Behalte historische
Schreibung, Abbreviaturen, Groß-/Kleinschreibung und Zeilenendzeichen
bei. Keine Normalisierung, Expansion, Ergänzung durch Formeln oder
Rückschluss aus vermutetem historischem Kontext.

Gib für jede geprüfte Zeile ihre Bildfundstelle, deine unabhängige
diplomatische Arbeitslesung und ausdrücklich markierte Unsicherheiten
bzw. Alternativen an. Unlesbares, Verborgenes und nicht Versuchtes
nicht als sicher gelesen ausgeben. Halte deine Lesung zuerst fest,
ohne den Arbeitschat-Text einzusehen. Gib sie zur anschließenden
bildgebundenen Gegenüberstellung zurück; entscheide keine Abweichung
allein wegen sprachlicher oder juristischer Plausibilität.

Dies ist eine KI-Gegenlesung, keine unabhängige Fachprüfung.
ENDE PROMPT

=== NACHTRAG 31.10.2026 · „NICHTS LÖSCHEN“ UND #364 ===
Nichts löschen gilt für Forschungsinhalte; Branches werden nach #364 mit Tag
`archiv/…` aufgeräumt.
Vor dem Archivieren gilt der dort bestimmte Verlusttest. Dieser Nachtrag
ist keine Anweisung, aktive Forschungs-/Prüf-/Planbranches zu löschen.

=== NACHTRAG 31.10.2026 · CHAT-ROLLEN UND ARBEITSMODUS ===
Die Rollenbezeichnungen im Plan und im Gegenleseschritt wurden auf Anweisung
des Eigentümers vom 31.10.2026 präzisiert.
Alle Arbeit läuft in normalen Chats; Work oder Codex nur auf ausdrückliche
Anweisung des Eigentümers.

=== NACHTRAG 31.10.2026 · GEGENLESUNG VORAB (EIGENTÜMERENTSCHEIDUNG) ===
Dieser datierte Nachtrag ersetzt für die kommenden Seiten allein den bisherigen
zeitlichen Gegenleseablauf; F1–F5, Fehlergrenze, Quelle-vor-Plausibilität, Rollen,
unveränderte Forschungsowner und die Human-Übernahmeentscheidung bleiben bestehen.

1. Vorab, vor der Lesung des Astra-Hauptchats, liest eine beliebige unabhängige KI
   blind je 2–3 originale Schriftzeilen kommender Seiten am Bild und speichert
   ihre Lesung auf Branch `review/nr632-gegenlesung-vorab` in
   `projects/ssta-20578-nr-632/research/gegenlesung-vorab-claude.md`.
   Weitere KIs dürfen eigene Abschnitte oder eigene Dateien daneben anlegen.
   Die eigene Lesung der Hauptchat-Seite darf dem Gegenleser vor dessen
   Sicherung nicht bekannt sein.
2. Der Astra-Hauptchat liest eine ganze Seite direkt vom Originalbild und
   committet seine Arbeitslesung auf dem Forschungsbranch von PR #359.
   **Erst nach diesem Seiten-Commit** öffnet er den Vorab-Abschnitt genau
   dieser Seite und hält dessen Branch-/Quellstand fest.
3. Lesungen unter Nennung des eigenen Seiten-Commits vergleichen; Abweichungen
   allein am Schriftbild klären, Varianten offenlassen und bei mehr als einem
   unmarkiert falschen Wort (einschließlich stiller Normalisierung) die Seite
   vor Fortsetzung nachbessern und erneut prüfen. Die Vorab-Lesung darf die
   ursprüngliche Erstlesung nicht rückwirkend beeinflussen.
4. Nach der Disposition sofort zur nächsten Seite, ohne auf den Eigentümer zu
   warten. Fehlt ein Vorab-Abschnitt, die Seite dennoch lesen und sichern,
   im `STATUS.md` ausdrücklich als „Gegenlesung offen“ führen und fortsetzen.

Die jetzt beauftragten Vorab-Abschnitte betreffen 0105L, 0105R und 0107L.
0106L und 0106R erhalten mangels Vorab den Status „Gegenlesung offen“.
Arbeit in normalen Chats, kein Work/Codex ohne ausdrückliche Eigentümeranweisung.
Kein selbstständiger Merge, kein Gate, keine neue Transkriptionswahrheit
außerhalb des kanonischen Forschungsowners. `#364` bleibt separate Pflegearbeit.
