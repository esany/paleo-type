# Spickzettel für den Eigentümer

Alle Stichworte, Prompts und Handgriffe an einem Ort. Gilt für jedes Projekt. Stand: **01.11.2026**.

**Pflege:** Wer ein Stichwort, einen Prompt oder einen Ablauf einführt oder ändert (Astra, Claude oder eine andere KI), ändert ihn **hier im selben PR**. Hier stehen nur allgemeine Regeln; was ein einzelnes Projekt betrifft, steht in dessen `projects/<id>/ARBEITSPLAN.md`. Ältere Fassungen stehen in der Git-Historie.

## Aktive Projekte

| Projekt-ID | Plan |
|---|---|
| `ssta-20578-nr-632` | [`ARBEITSPLAN.md`](projects/ssta-20578-nr-632/ARBEITSPLAN.md) |

Ohne Angabe beziehen sich die Stichworte auf diese Projekte, in dieser Reihenfolge.

---

## 1 · Stichworte

| Du schreibst | an wen | was passiert |
|---|---|---|
| **weiter** | Hauptchat (Astra) | Der Chat erledigt zuerst offene Issues mit Label `an:chatgpt` (älteste zuerst), dann den nächsten Durchgang nach Plan und Rückkehrpunkt im `STATUS.md`. Am Ende kommt eine kurze Meldung an dich. |
| **vorab** / **gegenlesen** | jeder Chat | Der Chat führt [`docs/gegenlesung-vorab.md`](docs/gegenlesung-vorab.md) aus: Er liest offene Seiten blind vorab und legt das Ergebnis im Repo ab. |
| **Prüfen** + PR-Nummer | Prüfchat (Claude) | Der Chat prüft den PR gegen Plan und Regeln, führt Tests selbst aus und schreibt ein Urteil in den PR. |
| **übernehmen** | Prüfchat | Nach bestandener Prüfung wird der PR auf `main` übernommen. |
| **Stichprobe** | Prüfchat | Der Chat liest eine Seite, deren Lesung er noch nicht kennt, blind gegen und trägt das Ergebnis im Forschungs-PR ein. |
| **Entscheidungen** | Prüfchat | Der Chat legt dir alle offenen Issues mit Label `an:mensch` in Alltagssprache vor. Du antwortest je Punkt mit ja oder nein (oder einem Satz); der Chat setzt es um oder legt den Auftrag für den Hauptchat an. |
| **Pflege** + Issue-Nummer | Prüfchat | Aufräumen von Branches und PRs nach dem Pflegeticket (braucht Git, das der Hauptchat nicht hat). |
| **paleo-type** | neuer Prüfchat | Der Chat startet als Prüfer: Er liest diesen Spickzettel, den jüngsten Übergabestand und seine offenen Issues mit `an:claude` und nennt Stand und nächsten Schritt in zwei Sätzen. |
| **Abschluss** | jeder Chat | Der Chat beendet seine Sitzung sauber: Er schreibt seinen Übergabestand fort (Hauptchat: Rückkehrpunkt im `STATUS.md`; Prüfchat: Kommentar im Issue mit Label `uebergabe`) und nennt den Start-Satz für den nächsten Chat. |

Optional mit Projekt-ID, z. B. „weiter ssta-20578-nr-632“. Ein normaler Chat arbeitet nur, solange er antwortet; jeder Durchgang braucht einen Anstoß von dir. Innerhalb eines Durchgangs läuft alles ohne dich.

## 1b · Wie Aufträge laufen: du kopierst nie Auftragstexte

Die Labels sind dieselben wie im Labor (design-lab):

| Label | wer ist dran |
|---|---|
| `an:chatgpt` | Hauptchat (Astra), bei „weiter“ zuerst |
| `an:claude` | Prüfchat, bei „paleo-type“ genannt |
| `an:mensch` | du, bei „Entscheidungen“ vorgelegt |

- **Findet der Prüfchat etwas**, das der Hauptchat im Rahmen des Plans erledigen soll, legt er ein Issue mit `an:chatgpt` an. Der Hauptchat erledigt es beim nächsten „weiter“ von selbst und schließt es mit einem Kommentar (was, wo, Commit).
- **Braucht es deine Entscheidung** (Ziel, Reihenfolge, neues Werkzeug, Übernahme auf `main`, Löschen), bekommt das Issue `an:mensch`. Du sagst „Entscheidungen“ und antwortest mit ja oder nein; danach wechselt das Label auf den, der umsetzt.
- **Freigabe:** In paleo-type ist ein `an:chatgpt`- oder `an:claude`-Issue freigegeben, wenn es im Plan des Projekts oder in einer im Issue genannten Eigentümerentscheidung Deckung hat. Widerspricht es dem Plan: nicht ausführen, im Issue begründen und `an:mensch` setzen.
- Ein Issue trägt immer genau ein `an:`-Label. Wer fertig ist oder abgibt, wechselt das Label oder schließt das Issue.
- Prompts aus Abschnitt 3 sind nur noch Notfall-Werkzeuge, z. B. ohne Projekt-Anweisung.

---

## 2 · Einmal einrichten

**a) Projekt-Anweisung im ChatGPT-Projekt** (Hauptchat und Gegenlese-Chats):
```
paleo-type: Bei „vorab“ oder „gegenlesen“: im GitHub-Repo esany/paleo-type docs/gegenlesung-vorab.md auf main lesen und vollständig ausführen. Bei „weiter“: SPICKZETTEL.md auf main lesen, dann ARBEITSPLAN.md und den Rückkehrpunkt im STATUS.md des Projekts, und den Plan fortsetzen. Bei „Abschluss“: Rückkehrpunkt im STATUS.md fortschreiben und den Start-Satz für den nächsten Chat nennen. Immer normaler Chat, kein Work/Codex.
```

**b) Anweisung im Claude-Projekt** (Prüfchat):
```
paleo-type: Bei „paleo-type“: Du bist Prüfer, nicht Bauer. Lies im GitHub-Repo esany/paleo-type SPICKZETTEL.md auf main und den jüngsten Kommentar „Übergabestand“ im offenen Issue mit Label uebergabe. Nenne Stand und nächsten Schritt in zwei Sätzen und warte auf den Auftrag. Bei „Abschluss“: Übergabestand als neuen Kommentar in diesem Issue fortschreiben. Bei „vorab“ oder „gegenlesen“: docs/gegenlesung-vorab.md ausführen.
```

**c) Bildquellen:** Die Bilddateien (z. B. PDFs) eines Projekts liegen als **Projektquelle** in beiden Chat-Projekten, nie im Repo. Welche Datei gilt, steht mit Prüfsumme im Projekt-Abschnitt „Parameter: Gegenlesung“.

**d) GitHub:** Settings → General → „Automatically delete head branches“ einschalten.

---

## 2b · Chat wechseln

1. Im alten Chat **„Abschluss“** schreiben und auf die Bestätigung warten.
2. Neuen Chat öffnen:
   - Hauptchat: „weiter“
   - Prüfchat: „paleo-type“
   - Gegenlese-Chat: „gegenlesen“
3. Nichts aus dem alten Chat hineinkopieren. Alles Nötige steht im Repo.

---

## 3 · Prompts zum Kopieren

### Hauptchat ohne Projekt-Anweisung
```
Repo: esany/paleo-type. Du bist der Hauptchat (Bauer).
Lies SPICKZETTEL.md auf main, dann für das aktive Projekt projects/<id>/ARBEITSPLAN.md
und den Rückkehrpunkt oben im STATUS.md. Arbeite den Plan selbständig ab. Frag nur bei:
Forschungsinhalt löschen, Übernahme auf main, neues Werkzeug, Widerspruch zum Plan.
Jeder Durchgang endet mit einer kurzen Meldung an mich in Alltagssprache.
Normaler Chat; kein Work, kein Codex.
```

### Gegenlesung ohne Projekt-Anweisung
```
Lies im GitHub-Repo esany/paleo-type docs/gegenlesung-vorab.md auf main und führe sie
vollständig aus.
```

### Prüfauftrag, ausführlich
```
Repo: esany/paleo-type. Du bist Prüfer, nicht Bauer.
Prüfe PR #<Nummer> gegen den Plan des Projekts und den Schritt, den er umsetzt:
- tut er genau seinen Schritt?
- bleibt Geschütztes unangetastet (Provenienz, Quelle/Datei, Unsicherheit,
  Aussageebenen, Gates)?
- Tests selbst ausführen: Gegenfall rot, richtiger Fall grün
- keine neuen Regeln, Audits, Löschungen
- Angaben im PR mit GitHub abgleichen
Ergebnis als Kommentar im PR: Urteil (übernehmen / nachbessern / ablehnen), Abnahme in
drei Ebenen (Build · frischer Kontext · tatsächliches Ergebnis), geprüft/nicht geprüft,
höchstens drei Fragen an mich in Alltagssprache.
Übernehmen nur, wenn alles grün ist und ich es sage.
```

---

## 4 · Wann du gefragt bist

- **Zwischenstände auf `main`:** wann, steht im Plan des Projekts. Der Prüfchat prüft, du entscheidest.
- **Werkzeug-Vorschlag:** höchstens ein Werkzeug auf einmal, mit Nutzen und Aufwand in Alltagssprache. Du sagst ja oder nein.
- **Alte Entwürfe aufräumen:** einmal entscheiden, was bleibt.
- **Lesungen beurteilen musst du nie.** Freiwillig: Am Ende von „weiter“ zeigt dir Astra bis zu 5 Bildausschnitte mit Namen, ohne ihre Lesung. Du tippst, was du liest, oder „?“. Keine Antwort ist auch in Ordnung.

## 5 · Rettungseingriff festhalten

Wenn du eingreifen musstest, weil die Arbeit in die falsche Richtung lief, setze das Label `rettung-eigentümer` an das Issue oder den PR. Die Anzahl erscheint in der automatischen PR-Prüfung.

## 6 · Wo steht was

| Was | Wo |
|---|---|
| Plan eines Projekts | `projects/<id>/ARBEITSPLAN.md` |
| Parameter (Bildquellen, Vorab-Datei, Fehlerschwelle) | dort, Abschnitt „Parameter: Gegenlesung“ |
| Rückkehrpunkt | `STATUS.md` des Projekts (oben), im aktuellen Forschungsbranch |
| Ablauf der Gegenlesung | `docs/gegenlesung-vorab.md` |
| Übergabestand des Prüfchats | offenes Issue mit Label `uebergabe` |
| Aufträge | offene Issues mit `an:chatgpt` / `an:claude` |
| Offene Entscheidungen für dich | offene Issues mit `an:mensch` |
