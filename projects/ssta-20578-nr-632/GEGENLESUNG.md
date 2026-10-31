# Nr. 632 — Gegenlesung: Anleitung für jeden Chat

Eigentümerentscheidung vom 31.10.2026. Gilt für jede KI und jeden Chat.

Diese Datei wird ausgeführt, wenn der Eigentümer **„vorab“** oder **„gegenlesen“** schreibt. Beide Wörter bedeuten dasselbe: offene Gegenlese-Aufträge abarbeiten. Ein Chat braucht außer dieser Datei nichts aus früheren Unterhaltungen.

Zweck: Kommende Seiten werden **vor** ihrer Bearbeitung stichprobenweise gelesen. So ist die Gegenlesung blind, und der Hauptchat kann ohne Warten vergleichen (siehe `ARBEITSPLAN.md`).

## Voraussetzungen (vor dem Start prüfen)

1. **GitHub:** lesender und schreibender Zugriff auf `esany/paleo-type`. Ohne Zugriff: anhalten und dem Eigentümer sagen, dass GitHub fehlt. Nicht ausweichen.
2. **Bildquelle:** eines der registrierten PDFs von Nr. 632 muss angehängt oder zugänglich sein. Prüfsumme (SHA-256) berechnen und vergleichen:
   - voll: `FILE-SSTA-20578-NR632-FULL-PDF-20261030`, `d89cf32d488122e274729be4388e2fd0f3bc7c6201d5d2293d04cfb33531d88e`
   - kompakt: `FILE-SSTA-20578-NR632-COMPACT-PDF-20261029`, `8cc44ccf25b78a1174fa78da26f617fb1af39cea4ccb6999c2a616041a5d1a7f`

   Wenn keine Datei vorliegt oder die Prüfsumme nicht passt: anhalten und den Eigentümer bitten, das PDF anzuhängen. Keine andere Bildquelle verwenden.
3. Die PDF-Seitenzahl ist die Bildnummer (z. B. Seite 105 = `0105`). `L`/`R` ist die linke bzw. rechte Hälfte der Aufnahme, keine Foliierung.

## Schritt 1 · Offene Seiten bestimmen

- In `projects/ssta-20578-nr-632/STATUS.md` auf dem aktuellen Forschungsbranch (Rückkehrpunkt oben nennt ihn) **nur** die Zeile `Vorab offen: …` lesen.
- Auf dem Branch `review/nr632-gegenlesung-vorab` die Datei `projects/ssta-20578-nr-632/research/gegenlesung-vorab.md` lesen: Welche Seiten haben schon einen Abschnitt?
- **Offen** = Seiten aus `Vorab offen`, die dort noch keinen Abschnitt haben.
- Bis zu **5** offene Seiten in der genannten Reihenfolge übernehmen.
- Ist nichts offen: dem Eigentümer „keine offenen Gegenlese-Aufträge“ melden und enden.

## Schritt 2 · Blindheit sichern

Für die übernommenen Seiten vor und während des Lesens **nichts öffnen, das Lesungstext dieser Seiten enthalten kann**:
- keine Dateien unter `projects/ssta-20578-nr-632/research/` außer `gegenlesung-vorab.md`
- keine Kommentare in den Issues und PRs zu Nr. 632
- keine Audits, keine Chat-Verläufe mit Lesungen

Hast du Lesungstext einer Seite schon gesehen: Diese Seite **überspringen** und am Ende als „nicht blind, übersprungen“ melden.

## Schritt 3 · Lesen

Je Seite **2–3 Zeilen**:
- aus verschiedenen Bereichen der Seite (oben, Mitte, unten; wenn vorhanden auch Rand oder Kanzleivermerk)
- selbst gewählt, nicht nur die erste Zeile

Am Bild lesen, in voller Auflösung, mit vergrößerten Ausschnitten. Die Zeilen selbst zählen.

Diplomatisch lesen:
- Schreibung, `ß`, Groß/klein, Abkürzungen und Abkürzungszeichen, Zeilenendzeichen (`-`, `=`) genau wie im Bild.
- Nichts vereinheitlichen, nichts auflösen, nichts aus Formelsprache, Grammatik oder Rechtskontext ergänzen.
- `[Wort?]` = unsicher, `[a/b]` = nicht entschieden, `⟦…⟧` = sichtbar, aber nicht gelesen.

**Locator** je Zeile: Seite, Textblock (z. B. „Haupttext rechts“, „Kanzleivermerk unter dem Siegel“), Zählung „von oben“ oder „von unten“ mit Nummer.

## Schritt 4 · Speichern

In `projects/ssta-20578-nr-632/research/gegenlesung-vorab.md` auf dem Branch `review/nr632-gegenlesung-vorab` je Seite einen Abschnitt **anhängen**, genau in dieser Form:

```
## 0105R
- Datum: 2026-10-31
- Leser: <KI und Chat, z. B. „Claude“ oder „Astra, Gegenlese-Chat“>
- Bildquelle: <File-ID>, PDF-Seite <n>
- Blind: ja
- Haupttext rechts, Z. 2 von oben: `fordert mein pflicht-`
- Haupttext rechts, Z. 4 von oben: `der respective Lehn und`
```

Regeln:
- **Ein Commit pro Durchgang**, nur diese Datei, Nachricht `vorab: <Seiten> (<Leser>)`.
- Kein PR, kein Merge, keine andere Datei ändern.
- Vorhandene Abschnitte nie ändern; Korrekturen nur als neuer Abschnitt mit Hinweis.

## Schritt 5 · Melden

Kurz an den Eigentümer, in Alltagssprache:
- gelesene Seiten
- übersprungene Seiten (mit Grund)
- wie viele Seiten in `Vorab offen` noch ohne Abschnitt sind
- Commit-SHA

---

## Für den Hauptchat (Auslöser „weiter“)

- **Liste pflegen:** Am Ende jedes Durchgangs die Zeile `Vorab offen: …` im STATUS auf die nächsten **10** Seiten in Planreihenfolge setzen, die noch keinen Vorab-Abschnitt haben.
- **Vergleich:** Eine Seite lesen und committen, **erst dann** ihren Vorab-Abschnitt öffnen. Im Forschungsowner einen Vergleichsvermerk anlegen:
  - eigener Lesungs-Commit (SHA)
  - verglichene Zeilen
  - unmarkierte Abweichungen, davon Vereinheitlichungen
  - Klärung am Bild
  - Urteil nach der Fehlerschwelle in `ARBEITSPLAN.md`
- **Seite ohne Vorab:** lesen und speichern, aber als „Gegenlesung offen“ führen. Kein „passt“.
- Ein Vergleich ist nur gültig, wenn der Vorab-Abschnitt **vor** dem Lesungs-Commit committet wurde. Das prüft `tools/gegenlesung_check.py`, sobald es übernommen ist.

## Grenzen

- KI-Gegenlesung, keine Fachprüfung, kein Gate.
- Die Gegenlesung entscheidet nicht allein: Abweichungen werden am Bild geklärt.
