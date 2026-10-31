# Spickzettel für den Eigentümer

Alle Stichworte, Prompts und Handgriffe an einem Ort. Stand: **31.10.2026**.

**Pflege:** Wer ein Stichwort, einen Prompt oder einen Ablauf einführt oder ändert (Astra, Claude oder eine andere KI), ändert ihn **hier im selben PR**. Ältere Fassungen stehen in der Git-Historie dieser Datei. Was hier fehlt, gilt als nicht eingeführt.

Dieser Zettel erklärt nur die Bedienung. Was gilt, steht in den verlinkten Dateien:
- [`ARBEITSPLAN.md`](projects/ssta-20578-nr-632/ARBEITSPLAN.md): Plan für Nr. 632
- [`GEGENLESUNG.md`](projects/ssta-20578-nr-632/GEGENLESUNG.md): Ablauf der Gegenlesung
- `STATUS.md`: Rückkehrpunkt der Forschung

---

## 1 · Stichworte

| Du schreibst | an wen | was passiert |
|---|---|---|
| **weiter** | Astra (Hauptchat) | Astra liest Plan und Rückkehrpunkt und arbeitet den nächsten Durchgang selbständig ab: lesen, speichern, mit Vorab vergleichen, nachbessern. Am Ende kommt eine kurze Meldung an dich. |
| **vorab** oder **gegenlesen** | jeder Chat, jede KI | Der Chat führt `GEGENLESUNG.md` aus: Er liest bis zu 5 offene Seiten blind vorab und legt das Ergebnis im Repo ab. |
| **weiter mit #364** | Astra | Branches und PRs aufräumen (Pflegeticket). |
| **Prüfen** + PR-Nummer | Claude | Claude prüft den PR gegen Plan und Regeln, führt Tests selbst aus und schreibt ein Urteil in den PR. |
| **übernehmen** | Claude | Nach bestandener Prüfung übernimmt Claude den PR auf `main`. |
| **Stichprobe** | Claude | Claude liest eine Seite, deren Lesung es noch nicht kennt, blind gegen und trägt das Ergebnis in den Forschungs-PR ein. |

Ein normaler Chat arbeitet nur, solange er antwortet. Darum braucht jeder Durchgang einen Anstoß von dir. Innerhalb eines Durchgangs läuft alles ohne dich.

---

## 2 · Einmal einrichten

**a) Projekt-Anweisung.** Diese Zeile gehört in die Projekt-Anweisungen: in ChatGPT in das Projekt mit den Astra-Chats, in Claude unter „Instructions“ des Projekts.

```
paleo-type / Nr. 632: Bei „vorab“ oder „gegenlesen“: im GitHub-Repo esany/paleo-type die Datei projects/ssta-20578-nr-632/GEGENLESUNG.md auf main lesen und vollständig ausführen. Bei „weiter“: ARBEITSPLAN.md auf main und den Rückkehrpunkt in STATUS.md lesen und den Plan fortsetzen. Immer normaler Chat, kein Work/Codex.
```

**b) PDF bereitstellen.** Das PDF von Nr. 632 einmal in die Projektdateien legen (voll oder kompakt, siehe Prüfsummen in `GEGENLESUNG.md`). Die Bilder liegen bewusst nicht im Repo.

**c) GitHub:** Settings → General → „Automatically delete head branches“ einschalten. Dann verschwinden Branches nach dem Übernehmen von selbst.

---

## 3 · Prompts zum Kopieren

### Neuer Hauptchat für Astra
Für einen frischen Start oder wenn der alte Chat zu lang geworden ist.
```
Repo: esany/paleo-type. Du bist der Astra-Hauptchat für Nr. 632.
Lies nur:
1. AGENTS.md (nur den Start)
2. projects/ssta-20578-nr-632/ARBEITSPLAN.md auf main: das ist mein Plan
3. projects/ssta-20578-nr-632/STATUS.md auf dem aktuellen Forschungsbranch: der
   Rückkehrpunkt steht ganz oben
Arbeite den Plan selbständig ab, beginnend mit dem Rückkehrpunkt. Frag nur bei:
Forschungsinhalt löschen, Übernahme auf main, neues Werkzeug, Widerspruch zum Plan.
Jeder Durchgang endet mit tools/work_return.py (und tools/gegenlesung_check.py, sobald
vorhanden) und einer kurzen Meldung an mich in Alltagssprache.
Normaler Chat; kein Work, kein Codex.
```

### Gegenlesung ohne Projekt-Anweisung
Falls ein Chat das Stichwort „vorab“ nicht kennt.
```
Lies im GitHub-Repo esany/paleo-type die Datei
projects/ssta-20578-nr-632/GEGENLESUNG.md auf main und führe sie vollständig aus.
Das PDF von Nr. 632 ist angehängt.
```

### Prüfauftrag an Claude
Für einen PR, wenn „Prüfen“ allein nicht reicht.
```
Repo: esany/paleo-type. Du bist Prüfer, nicht Bauer.
Prüfe PR #<Nummer> gegen ARBEITSPLAN.md und den Schritt, den er umsetzt:
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

- **Zwischenstand auf `main`:** nach dem Gesuch 0104R–0107L, danach etwa alle zwei Texteinheiten. Claude prüft, du entscheidest.
- **Werkzeug-Vorschlag:** Astra legt höchstens ein Werkzeug vor, mit Nutzen und Aufwand in Alltagssprache. Du sagst ja oder nein.
- **Alte Entwürfe (#364, Gruppe D):** einmal entscheiden.
- **Lesungen beurteilen musst du nie.**

## 5 · Rettungseingriff festhalten

Wenn du eingreifen musstest, weil die Arbeit in die falsche Richtung lief, setze das Label `rettung-eigentümer` an das betroffene Issue oder den PR. Die Anzahl erscheint in der automatischen PR-Prüfung. So siehst du, ob das System besser wird.

## 6 · Wo steht was

| Was | Wo |
|---|---|
| Plan für Nr. 632 | `projects/ssta-20578-nr-632/ARBEITSPLAN.md` |
| Ablauf Gegenlesung | `projects/ssta-20578-nr-632/GEGENLESUNG.md` |
| Rückkehrpunkt, offene Vorab-Seiten | `STATUS.md` im aktuellen Forschungsbranch (oben) |
| Vorab-Lesungen | Branch `review/nr632-gegenlesung-vorab`, Datei `research/gegenlesung-vorab.md` |
| Laufende Forschung | PR #359 |
| Forschungsplan (Übersicht) | Issue #358 |
| Aufräumen | Issue #364 |
