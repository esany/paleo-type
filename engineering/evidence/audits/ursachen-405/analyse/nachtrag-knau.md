# Nachtrag zur Analyse #405: Knau war kein Gegenbeispiel

> **Vorläufig, abgelöst durch `primaer-knau.md`.** Dieser Nachtrag stützt sich nur auf Zusammenfassungen (LEARNINGS, STATUS) und ist am Primärmaterial nicht geprüft.

Stand: 03.11.2026, abends · Claude, Prüfer, vierter Chat · Branch `analysis/ursachen-405-erhebung` (#408). **Nicht für `main`.** Keine Lösungen und keine Maßnahmen.

## Anlass

`infrastruktur.md` §5 G4 und §7.1 behandeln Knau als erfolgreichen Fall, an dem sich ablesen lässt, welche Fähigkeiten getragen haben. Dieselbe Annahme steckt in der Projektnotiz des Claude-Projekts („Vorbild mit erreichtem G2–G4“) und im Start-Ablauf von `SPICKZETTEL.md` §1.

Der Eigentümer hat das am 03.11.2026 so berichtigt (sinngemäß): Knau lief gut, wesentlich besser als jetzt, hatte aber auch seine Probleme. Die sind schon dokumentiert, die Issues sind voll davon.

## Leseprotokoll

- **Ganz gelesen:** `projects/ega-reg-ii-5-knau/LEARNINGS.md` (L001–L029) und `STATUS.md` (Checkpoint 13.09.)
- **Exportiert, aber nicht gelesen:** #64, #68, #84, #85, #96–#100, #115, #122, #123, #124, #129, #138, #141, #142, #150, #166. Zusammen rund 490.000 Zeichen.
- Die Aussagen unten stützen sich deshalb auf die **Selbstbeschreibung des Projekts**. Sie ist von KI-Chats verfasst (*Aussage*) und nicht an den Issues gegengeprüft.

## Was dokumentiert ist (Aussage, Fundstelle LEARNINGS)

Die Knau-Probleme gehören weitgehend **derselben Familie** an wie die heutigen Kandidaten:

| heutiger Kandidat / heutiges Phänomen | schon bei Knau festgehalten |
|---|---|
| Z5 / P7: das Signal tritt an die Stelle des Ergebnisses | L024: Ein Ablauf kann einen fachlich schiefen Umfang effizient absichern; ein bestandener Backtest belegt den Umfang nicht. |
| Z4 / P8: Gegenmittel erzeugen Reibung | L025: Ein fehlendes PDF wurde über Wartung, Tests und Restart-Stand zu einem kanonischen „STOP“ ausgebaut. |
| P13 / L028: auf ein Problem folgt Struktur | L028: Das Übergewicht der Systemarbeit ist eine **Folge**: Die KI-gestützte Arbeit erholt sich nicht zuverlässig von einem Fehler und kehrt nicht zur Quelle zurück. |
| P1 / Wellen | L007: Die Chatarbeit hat die Methode immer wieder neu aufgerollt und den nächsten Schritt verloren. |
| Z2 / P12: Vorhandenes wird übersehen, Altes wieder aktiviert | L013: Bei einer Migration ging die sichtbare Prüffläche verloren. L020: Verzeichnisnamen holen eine überholte Methode zurück. |
| P10 / Übergaben werden als Wahrheit übernommen | L012, L023: Frische Kontexte reproduzierten eine in sich stimmige KI-Erzählung; eine unabhängige Prüfung übernahm dieselbe abgeleitete Prämisse. |
| G5: der Fall wird zum Zweck | L008, L027: Der Pilot durfte die allgemeine Methode und den Systemzweck bestimmen. |
| Leistungsfähigkeit | L029: Sicherer, aber nicht nachweislich leistungsfähiger. Laut Eigentümer war der Chat vor dem Repo fachlich ergiebiger. |

**Ergebnis laut STATUS:** In der Knau-Phase (etwa 27.08.–13.09.) wurden die Fol. 61v–63r bearbeitet, 81 Zeilen. G2, G3 und G4 gelten dafür als erreicht, G5 und G6 nicht. Danach war kein nächster Schritt mehr festgelegt.

## Folgen für `infrastruktur.md` (Deutung)

1. **G4 in der bisherigen Form entfällt.** Knau ist kein Gegenbeispiel, an dem sich eine „passende Umgebung“ als Erfolgsgrund ablesen ließe, sondern eine frühere, mildere Ausprägung derselben Fehlerfamilie. Die Fähigkeiten und die Umgebung von Knau können die Familie also nicht verhindert haben. Offen bleibt, warum sie milder verlief.
2. **Der Eigentümer beschreibt ein Gefälle:** Der Chat vor dem Repo war ergiebiger als Knau, und Knau war besser als heute (L029 und Aussage vom 03.11.). Die Systemmenge ist in derselben Zeit gewachsen. Das passt zu Z2 und Z4, ist aber nur eine zeitliche Gleichläufigkeit, kein Kausalbeleg. Gegenlesart: Auch die Aufgaben wurden schwerer (Nr. 632 ist größer, Umgebungswechsel Z3).
3. **Die Hypothese der Infrastrukturfehler ist nicht neu.** L028 (Stand Mitte September) benennt im Kern schon die Schleife aus `infrastruktur.md` §4: Störung, dann Ausgleich durch weitere Systemarbeit, ohne Rückkehr zur Quelle. Die dritte Lesart hat L025–L029 nicht zitiert. Dass ein dokumentierter Befund nicht gefunden wird, ist selbst ein Fall von P12/Z2, und mein eigener Vorschlag, bei G4 anzusetzen, hätte ihn wiederholt.
4. **Die Frage verschiebt sich.** Nicht mehr „Was sind die Ursachen?“ ist offen, denn Kandidaten sind seit September aufgeschrieben. Offen ist, **warum dokumentierte Lehren nicht wirken** (P2, #297 H1–H5). Genau dort setzen Z2 und Z4 an: Lehren werden als Text abgelegt, Text wirkt im Modell nicht verlässlich, und jede neue Lehre vergrößert den Text.

## Nicht geprüft

- ob die Issues der Knau-Phase die LEARNINGS bestätigen oder ihnen widersprechen
- warum Knau milder verlief, etwa durch kleineren Umfang, Paralleltext, Umgebung oder die Zeit vor dem Aufwuchs
- ob L028 und L029 je eine Folge hatten
