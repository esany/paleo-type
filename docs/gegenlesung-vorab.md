# Gegenlesung vorab: Ablauf für jeden Chat

Eigentümerentscheidung vom 31.10.2026. Gilt für jedes Projekt, jede KI und jeden Chat.

**Auslöser:** Der Eigentümer schreibt **„vorab“** oder **„gegenlesen“**, optional mit Projekt-ID (z. B. „vorab ssta-20578-nr-632“). Beide Wörter bedeuten dasselbe: offene Gegenlese-Aufträge abarbeiten. Ein Chat braucht außer dieser Datei und den Projektparametern nichts aus früheren Unterhaltungen.

**Zweck:** Kommende Seiten werden **vor** ihrer Bearbeitung stichprobenweise gelesen. So ist die Gegenlesung blind, und der Hauptchat kann ohne Warten vergleichen.

## Projekt und Parameter bestimmen

1. **Projekt:** die genannte Projekt-ID. Ohne Angabe gelten die Projekte in `SPICKZETTEL.md`, Abschnitt „Aktive Projekte“, in der dort genannten Reihenfolge.
2. **Parameter** stehen in `projects/<id>/ARBEITSPLAN.md`, Abschnitt **„Parameter: Gegenlesung“**:
   - Bildquelle(n): File-ID und SHA-256
   - Vorab-Datei: Branch und Pfad
   - Hauptchat-Forschungsowner
   - Fehlerschwelle

   Fehlt der Abschnitt: anhalten und dem Eigentümer melden, dass das Projekt nicht für die Gegenlesung eingerichtet ist.

## Voraussetzungen

1. **GitHub:** lesender und schreibender Zugriff auf `esany/paleo-type`. Ohne Zugriff: anhalten und es dem Eigentümer sagen.
2. **Bildquelle:** Die Bilddateien liegen als **Projektquelle** des Chat-Projekts vor, nie im Repo. Die Datei nehmen, deren SHA-256 zu einer der Parameter-Bildquellen passt. Passt keine: anhalten und melden. Keine andere Bildquelle verwenden.
3. Seiten- und Bildnummern sind digitale Ansichtsadressen nach dem Crosswalk des Projekts, keine archivalische Foliierung.

## Schritt 1 · Offene Seiten bestimmen

- In der Vorab-Datei **nur** die Zeile `Vorab offen: …` ganz oben und die Überschriften `## <Seite>` lesen, keine Lesungen.
- **Offen** = Seiten aus `Vorab offen` ohne eigenen Abschnitt. Eine Angabe wie `0105L (Z. 14–16 von oben)` heißt: genau diese Zeilen lesen.
- Bis zu **5** offene Seiten in der genannten Reihenfolge übernehmen.
- Fehlt die Zeile oder ist nichts offen: dem Eigentümer „keine offenen Gegenlese-Aufträge“ melden und enden.

## Schritt 2 · Blindheit sichern

Für die übernommenen Seiten vor und während des Lesens **nichts öffnen, das Lesungstext dieser Seiten enthalten kann**:
- keine Forschungsdateien des Projekts außer der Vorab-Datei
- keine Kommentare in den Issues und PRs des Projekts
- keine Audits, keine Chat-Verläufe mit Lesungen

Hast du Lesungstext einer Seite schon gesehen: Seite **überspringen** und am Ende als „nicht blind, übersprungen“ melden.

## Schritt 3 · Lesen

Je Seite **2–3 Zeilen**:
- aus verschiedenen Bereichen (oben, Mitte, unten; wenn vorhanden auch Rand oder Vermerk)
- selbst gewählt, nicht nur die erste Zeile

Am Bild lesen, in voller Auflösung, mit vergrößerten Ausschnitten. Zeilen selbst zählen.

Diplomatisch lesen:
- Schreibung, Sonderzeichen (z. B. `ß`), Groß/klein, Abkürzungen, Zeilenendzeichen genau wie im Bild.
- Nichts vereinheitlichen, nichts auflösen, nichts aus Formelsprache, Grammatik oder Kontext ergänzen.
- `[Wort?]` = unsicher, `[a/b]` = nicht entschieden, `⟦…⟧` = sichtbar, aber nicht gelesen.

**Locator** je Zeile: Seite, Textblock, Zählung „von oben“ oder „von unten“.

## Schritt 4 · Speichern

Je Seite einen Abschnitt an die Vorab-Datei **anhängen**:

```
## <Seite>
- Datum: <JJJJ-MM-TT>
- Leser: <KI und Chat>
- Bildquelle: <File-ID>, Seite <n>
- Blind: ja
- <Textblock>, Z. <n> von oben/unten: `<Lesung>`
```

- **Ein Commit pro Durchgang**, nur die Vorab-Datei, Nachricht `vorab: <Seiten> (<Leser>)`.
- Die Zeile `Vorab offen` nicht ändern; sie pflegt der Hauptchat.
- Kein PR, kein Merge, keine andere Datei.
- Vorhandene Abschnitte nie ändern; Korrekturen nur als neuer Abschnitt mit Hinweis.

## Schritt 5 · Melden

Kurz an den Eigentümer, in Alltagssprache:
- gelesene Seiten
- übersprungene Seiten (mit Grund)
- wie viele Seiten in `Vorab offen` noch ohne Abschnitt sind
- Commit-SHA

---

## Pflichten des Hauptchats (Stichwort „weiter“)

- **Liste pflegen:** Am Ende jedes Durchgangs die Zeile `Vorab offen` in der Vorab-Datei auf die nächsten **10** Seiten in Planreihenfolge ohne Abschnitt setzen. Nur diese Zeile ändern.
- **Vergleich:** Seite lesen und committen, **erst dann** ihren Vorab-Abschnitt öffnen. Im Forschungsowner einen Vergleichsvermerk anlegen:
  - eigener Lesungs-Commit
  - verglichene Zeilen
  - unmarkierte Abweichungen, davon Vereinheitlichungen
  - Klärung am Bild
  - Urteil nach der Fehlerschwelle des Projekts
- **Seite ohne Vorab:** lesen und speichern, als „Gegenlesung offen“ führen. Kein „passt“.
- Ein Vergleich ist nur gültig, wenn der Vorab-Abschnitt **vor** dem Lesungs-Commit committet wurde.

## Ein Projekt einrichten

Im Projekt `projects/<id>/ARBEITSPLAN.md` den Abschnitt „Parameter: Gegenlesung“ anlegen. Die Vorab-Datei mit der Zeile `Vorab offen:` auf ihrem Branch anlegen. Das Projekt in `SPICKZETTEL.md` unter „Aktive Projekte“ eintragen.

## Grenzen

- KI-Gegenlesung, keine Fachprüfung, kein Gate.
- Die Gegenlesung entscheidet nicht allein: Abweichungen werden am Bild geklärt.
