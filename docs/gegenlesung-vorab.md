# Gegenlesung vorab: Ablauf für jeden Chat

Eigentümerentscheidung vom 31.10.2026. Gilt für jedes Projekt, jede KI und jeden Chat.

**Auslöser:** Der Eigentümer schreibt **„vorab“** oder **„gegenlesen“**, optional mit Projekt-ID (z. B. „vorab ssta-20578-nr-632“). Beide Wörter bedeuten dasselbe: offene Gegenlese-Aufträge abarbeiten. Ein Chat braucht außer dieser Datei und den Projektparametern nichts aus früheren Unterhaltungen.

**Zweck:** Seiten werden von einem zweiten Chat stichprobenweise blind gelesen, möglichst **vor** ihrer Bearbeitung. So kann der Hauptchat ohne Warten vergleichen.

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
- **Offen** = Einträge aus `Vorab offen` ohne eigenen Abschnitt. Eine Angabe wie `0105L (Z. 14–16 von oben)` heißt: genau diese Zeilen lesen.
- **Nachprobe:** Ein Eintrag mit Zusatz, z. B. `0105L-2 (Z. 14–16 von oben)`, ist eine zweite Probe einer schon geprüften Seite. Sie ist offen, solange es keinen Abschnitt `## 0105L-2` gibt. Ältere Abschnitte derselben Seite enthalten Lesungstext und werden nicht geöffnet. Nachproben heißen `<Seite>-<n>` (z. B. `0105L-2`); der Abschnitt `## 0105L-2` und eine spätere `Vergleich: 0105L-2 | …`-Zeile müssen exakt diese eigenständige ID verwenden, nicht die ursprüngliche `0105L`.
- Bis zu **10** offene Einträge in der genannten Reihenfolge übernehmen (Eigentümerentscheidung 02.11.2026: ein „gegenlesen“ je „weiter“). Wird der Kontext knapp, nach den fertigen Einträgen committen und melden, wie viele offen blieben.
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

- **Hinweis an den Eigentümer:** Wann immer der Hauptchat auf „gegenlesen“ verweist (Meldung, `Stand für den Eigentümer`, Website), schreibt er wörtlich dazu: **„in einem frischen Chat im ChatGPT-Projekt, nicht in diesem Chat“**.

- **Liste pflegen:** Am Ende jedes Durchgangs die Zeile `Vorab offen` in der Vorab-Datei setzen: **zuerst alle Nachproben**, die der Plan nach einer Korrektur verlangt (z. B. `0112L-2 (2–3 Zeilen)`), dann die nächsten Seiten in Planreihenfolge ohne Abschnitt, zusammen höchstens **10** Einträge. Nur diese Zeile ändern.
- **Vergleich:** Seite lesen und committen, **erst dann** ihren Vorab-Abschnitt öffnen. Im Forschungsowner einen Vergleichsvermerk anlegen:
  - eigener Lesungs-Commit
  - verglichene Zeilen
  - unmarkierte Abweichungen, davon Vereinheitlichungen
  - Klärung am Bild
  - Urteil nach der Fehlerschwelle des Projekts
- **Seite ohne Vorab:** lesen und speichern, als „Gegenlesung offen“ führen. Kein „passt“.
- **Gültig ist ein Vergleich**, wenn
  1. der Gegenleser „Blind: ja“ erklärt hat (er kannte den Lesungstext nicht), und
  2. der Hauptchat den Lesungsstand vergleicht, den er **vor dem Öffnen** des Abschnitts committet hatte (Commit im Vermerk nennen).

  Ob der Vorab-Abschnitt vor oder nach diesem Lesungs-Commit entstand, spielt keine Rolle. Auch früher gelesene Seiten lassen sich so gültig gegenprüfen.
- **Mehrere Seiten je Durchgang:** Der Hauptchat arbeitet in einem Durchgang alle Seiten ab, für die ein Vorab-Abschnitt vorliegt, höchstens so viele, wie der Plan des Projekts je Durchgang erlaubt. Danach meldet er sich.

## Namensstellen für den Eigentümer (freiwillig, je Projekt)

Nur, wenn `ARBEITSPLAN.md` unter „Parameter: Gegenlesung“ eine Zahl für **Namensstellen je Durchgang** nennt.

- **Was:** Personen- und Ortsnamen, bei denen die eigene Lesung unsicher ist oder von der Vorab-Lesung abweicht. Unsichere zuerst.
- **Wie:** Am Ende von „weiter“ zeigt der Hauptchat dem Eigentümer je Stelle **nur einen Bildausschnitt** mit Seite und Zeile. Er zeigt keine eigene Lesung und keine Vorschläge. Der Eigentümer tippt, was er liest, oder „?“.
- **Vorher:** Die eigene Lesung der Stelle ist schon committet.
- **Bildausschnitte** nur im Chat, nie im Repo.
- **Festhalten** im Forschungsowner, je Stelle eine Zeile:
  `Namenshinweis: <Seite> <Locator> | Eigentümer: <Text> | Lesung <sha> | Klärung am Bild: <Ergebnis>`
- **Gewicht:** Ein Hinweis, keine Gegenlesung. Er zählt nicht für die Fehlerschwelle. Abweichungen werden am Bild geklärt. Bleibt es offen, als `[a/b]` stehen lassen.
- Antwortet der Eigentümer nicht, weiterarbeiten; die Stellen bleiben offen.

## Ein Projekt einrichten

Im Projekt `projects/<id>/ARBEITSPLAN.md` den Abschnitt „Parameter: Gegenlesung“ anlegen. Die Vorab-Datei mit der Zeile `Vorab offen:` auf ihrem Branch anlegen. Das Projekt in `SPICKZETTEL.md` unter „Aktive Projekte“ eintragen.

## Grenzen

- KI-Gegenlesung, keine Fachprüfung, kein Gate.
- Die Gegenlesung entscheidet nicht allein: Abweichungen werden am Bild geklärt.

**Nullzeilen-Bildbefund (kein positives Gegenleseergebnis):** Trägt eine
Fotoansicht tatsächlich **keine** mit eigener Leserichtung sicher
diplomatisch lesbare physische Schriftzeile (z. B. nur Durchschein-/Spiegelschrift),
dürfen weder Buchstaben noch Zeilenlocator erfunden werden. Der unabhängige
Gegenleser notiert stattdessen im Abschnitt die genaue Bildquelle, `Blind: ja`,
einen ausdrücklich ortsbezogenen `- Bildbefund, …: …` und
`- Stichprobe: 0 eigenständige Schriftzeilen …`. Der CI-Formatcheck erkennt
dies als **dokumentierte Nullbeobachtung**, **nicht** als positive
2–3-Zeilen-Gegenlesung, Fehlerquote, bestandenen Vergleich oder fachliche
Flächenabnahme. Für tatsächlich lesbare Schrift bleiben nummerierte physische
Zeilenlocators zwingend. Eine Nullbeobachtung ist nicht automatisch
quellenkritisch bewiesen; sie bleibt eine überprüfbare KI-Aussage am Bild.
