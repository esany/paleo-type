# Ursachenanalyse #405: Ansatz, Prüfung des Ansatzes, Leseprotokoll

Stand: 03.11.2026 · Verfasser: Claude (frischer Chat nach Handoff #405) · Ort: Analyse-Branch `analysis/ursachen-405-erhebung`, Entwurfs-PR #408. **Nicht für `main`.**

Dieses Dokument wurde **vor** der Auswertung geschrieben und committet. Die Hypothesen in Abschnitt 4 und die Auswahlregeln in Abschnitt 5 sind damit vorab festgelegt. Spätere Änderungen werden als Nachtrag mit Grund vermerkt, nicht stillschweigend eingearbeitet.

Keine Ursachen als Befund in diesem Dokument, keine Lösungen und keine Maßnahmen.

---

## 1. Leseprotokoll vor der Festlegung des Ansatzes (Auftrag A)

„ganz“ heißt: vollständig gelesen, ohne Kürzung. Gelesen mit `Read` oder `cat` am Stand `main@22b255b`, Issues über die REST-API am 03.11.2026.

| Quelle | gelesen | Vermerk |
|---|---|---|
| `GOVERNING_OBJECTIVE.md` | ganz | |
| `AGENTS.md` | ganz | als Systemhinweis nach `register_repo_root` |
| `SPICKZETTEL.md` | ganz | |
| `methodology/` (alle 10 Dateien: ai-governance, evidence-policy, historical-source-workflow, maintenance, project-lifecycle, quality-and-learning, research-gates, source-and-provenance, transcription-guidelines, workflow) | ganz | |
| `DECISIONS.md` (D-001 bis D-021) | ganz | |
| `engineering/README.md` | ganz | |
| `engineering/catalog/` (artifacts, coverage, findings, relations, legacy-paths) | ganz | |
| `engineering/evidence/audits/research-framing-transdisciplinary-competency-audit-2026-09-14.md` | ganz | |
| `engineering/evidence/audits/bug-intent-root-cause-wirknetz-plan-fit-audit-2026-10-07.md` (ENG-A-0118) | ganz | zusätzlich gewählt: vorhandene Ursachenanalyse |
| #230 mit Kommentar | ganz | |
| #297 mit allen 30 Kommentaren | ganz | abschnittsweise (4 Teile) |
| #404 mit 2 Kommentaren | ganz | |
| #405 mit 3 Kommentaren | ganz | |
| #368, nur jüngster Übergabestand | teilweise | Startroutine; übrige 13 Kommentare nicht gelesen |
| #398 mit allen Kommentaren | ganz | zusätzlich gewählt |
| #399, #406, #408 mit Kommentaren | ganz | zusätzlich gewählt |
| #401 Text und Bericht `systemaudit-2026-11-chatgpt.md` (Branch `audit/systemaudit-2026-11-chatgpt-400`) | ganz | zusätzlich gewählt; im Handoff als ungeöffnet geführt |
| `ursachen-405/README.md`, `export/STAND.md`, Kopf und Summen von `sollliste.tsv` | ganz bzw. ausgewertet | |
| PR #402 (Bericht Claude) | nicht | bewusst nicht: vom Eigentümer als unbrauchbar bewertet; Inhalt ist über #398 und #404 als Aussage bekannt |
| Lesungen von Nr. 632 | nicht | Blindheit |

**Nicht gelesen** und für den Ansatz bewusst offen: der übrige Grundstoff (rund 2,3 Mio. Tokens laut `sollliste.tsv`), darunter `engineering/evidence/` außer den zwei genannten Audits, `requirements/`, alle `STATUS.md` und `LEARNINGS.md`, die übrigen rund 400 Issues und PRs, `wissensarbeit`, `design-lab`. Was davon gelesen wird, legt der Ansatz fest (Abschnitt 5).

## 2. Was erklärt werden soll (Explananda)

Feste Liste. Am Ende muss jeder Punkt **erklärt**, **teilweise erklärt** oder **nicht erklärt** sein, mit Grund.

**Aus den Aussagen des Eigentümers (#405 §1):**
- E1 Die Arbeit verläuft in Wellen: Plan klingt plausibel, es läuft, dann kein Fortschritt, der für ihn nicht transparent ist.
- E2 Das ist zyklisch; er endet immer wieder „vor der Wand“.
- E3 Bei den Visitationsprotokollen kam die Arbeit „viel weiter“ als jetzt bei Nr. 632, obwohl auch dort keine Forschungsfrage vorlag.
- E4 Er muss Fehler selbst entdecken und Abläufe selbst anstoßen.

**Aus dem Handoff (P1–P13), zuerst als Phänomen zu prüfen, nicht als gegeben:** P1 Wellen · P2 wiederkehrende Fehlerfamilie · P3 Regeln wirken nicht · P4 Synthesefunktion kaum sichtbar · P5 Erfahrung mit Hand und Formular zurückgenommen · P6 Zerlegung in Bruchstücke · P7 formales Bestehen statt Ergebnis · P8 Kontrollabläufe erzeugen Reibung · P9 Rollen und Werkzeuge passen nicht · P10 Eigentümer als Bote und Entdecker · P11 Grundstoff größer als ein Kontext · P12 Vorhandenes wird übersehen und neu gebaut · P13 Solutionism.

## 3. Vorhandene Analysen und wie sie verwendet werden

Alle gelten als **Aussagen Beteiligter**. Sie liefern Hypothesen, keine Befunde.

| Analyse | Kernaussage (verkürzt, eigene Worte) | Verwendung |
|---|---|---|
| #230 (02.–03.10., Kommentar) | gemischtes Ergebnis H3: echte strukturelle Lücke im Lebenszyklus von Wissen und Arbeit, dazu getrennte Lücken | Hypothesenquelle; die fünf Fragen gegen das Verkürzen werden auf den Ansatz angewandt (Abschnitt 7) |
| #297 §4–§11 (05.10.) | gemischter Mechanismus H5: richtige Regeln, lokale Lösungen, zu schmale Abnahme, Abschluss-Signale lösen sich vom Bedarf, Modellgrenze; Eigenschaften P1–P8 | Hypothesenquelle (H-E unten) |
| ENG-A-0118 (07.10.) | Ursachenfamilien RC-1 bis RC-5 für die damals offenen Issues | Hypothesenquelle; zeigt den Stand vor Nr. 632 |
| Audit 14.09. | Rahmung der Forschungsfrage über mehrere Disziplinen ist nach der Verschlankung kaum noch wirksam | Hypothesenquelle (H-A) |
| `engineering/catalog/findings.tsv` | 45 Befunde der „Bugwave“, Abdeckung bis 09.10. | Systemkarte für Engineering bis 09.10.; danach nicht fortgeführt (eigener Befund für S) |
| #401 ChatGPT (03.11.) | RC1–RC6, zwei Fehlkreise (lokaler Kontrollgewinn verdrängt Ergebnis; Prämissen werden in Prüfungen vererbt) | Hypothesenquelle; beteiligte Modellfamilie |
| #404 (03.11.) | Mechanismen 1–8 im Prüfauftrag selbst | Hypothesenquelle; zugleich Fehlerliste für diesen Chat |
| #402 Claude | vom Eigentümer verworfen | nicht verwendet |

**Gemeinsamer blinder Fleck aller vorhandenen Analysen** (aus der Lektüre, als Beobachtung): Keine prüft ihre Ursachen gegen den **zeitlichen Verlauf** als Ganzes. Sie arbeiten mit Fallbeispielen, die zur jeweiligen These passen. Ob die Wendepunkte der Wellen tatsächlich von den genannten Mechanismen ausgelöst wurden, ist nirgends geprüft. Hier setzt der Ansatz an.

## 4. Konkurrierende Hypothesen (vorab festgelegt)

Jede Hypothese sagt etwas Prüfbares über die **Wendepunkte** voraus, also darüber, was unmittelbar vor dem Umschlagen von Forschungs- in Systemarbeit und zurück geschah. Die Hypothesen schließen sich nicht aus. Gewichtet wird erst nach der Prüfung.

| ID | Hypothese | Vorhersage am Wendepunkt | Herkunft |
|---|---|---|---|
| H-A | **Fachliche Wand:** Systemarbeit beginnt, wenn die Forschung an eine fachliche Grenze kommt (Lesung zu schwer, Gate erreicht, keine nächste Richtung). | Vor dem Umschlag: Gate erreicht, Ergebnisgrenze, offene Richtungsfrage. | Audit 14.09. §10, #402 U1 |
| H-B | **Vorfall → Struktur:** Ein konkreter Fehler wird mit neuer Regel, neuem Werkzeug oder Ablauf beantwortet; das erzeugt die Systemwelle. | Vor dem Umschlag: Fehlervorfall oder Einwand des Eigentümers; danach Regeln oder Werkzeuge zu genau diesem Vorfall. | #404 M5, P13 |
| H-C | **Auftrag des Eigentümers:** Die Systemarbeit wurde vom Eigentümer ausdrücklich beauftragt. | Systemissues tragen eine Eigentümerentscheidung oder einen Auftrag in seinen Worten. | Gegenhypothese zu „die KI ist abgedriftet“; Absicht prüfen (Fehler 4 in #405 §3) |
| H-D | **Plattform und Rollen:** Grenzen der Werkzeuge oder Rollen erzwingen Umgehungsabläufe. | Vor dem Umschlag: Wechsel von Chat, Rolle, Modus oder Werkzeug; danach Abläufe, die diese Grenze umgehen. | P9, #401 RC5, #297 (lokale Checkouts) |
| H-E | **Regeln ohne Wirkung:** Regeln ändern das Verhalten nicht, derselbe Fehler kehrt wieder, es folgt die nächste Regel. | Wiederkehr eines Fehlers nach einer Regel dagegen; Zahl der Regeln wächst stetig. | #297 H1/P8, P3 |
| H-F | **Fehlende Frage:** Ohne Forschungsfrage des Eigentümers füllt Systemverbesserung die Lücke. | Wendepunkt fällt mit dem Ende eines Auftrags ohne Nachfolger zusammen. | #402 U2 (zurückgezogen), D-020; der Eigentümer verneint sie für die Visitationsprotokolle |
| H-G | **Notwendige Investition (Nullhypothese):** Die Systemarbeit war für neue Aufgaben nötig, und die Wellen sind normale Phasen. Das Problem liegt in der Durchsichtigkeit, nicht in der Arbeit. | Nach einer Systemwelle läuft die Forschung schneller oder besser. | Gegenhypothese zu allen anderen |
| H-H | **Größe schlägt Kontext:** Das Repo wächst über den Kontext eines Chats hinaus; Vorhandenes wird übersehen und neu gebaut; das Repo wächst weiter. | Neubauten neben Vorhandenem häufen sich mit der Größe des Repos. | P11, P12, #401 RC4 |
| H-I | **Prämisse wird vererbt:** Ein späterer Chat übernimmt den letzten lokalen Erfolg oder die letzte Deutung als gegeben; Prüfungen bestätigen statt zu prüfen. | Am Wendepunkt beruht die neue Richtung auf einer ungeprüften Aussage des vorigen Chats. | #401 RC6, L023, #253 |

## 5. Der Ansatz: Struktur, Hypothesen, gezielte Tiefe

### S – Struktur (vollständig, aus Metadaten)

Ein Gesamtbild über die ganze Laufzeit (26.08.–03.11.2026), gewonnen **mechanisch und vollständig** aus Git und GitHub, ohne Inhalte zu deuten:
- Zeilen je Woche nach Bereich (Forschung, Methodik, Verfahren und Engineering, Werkzeug und Tests, Betrieb), Umbenennungen erkannt, damit Verschiebungen nicht als Neuarbeit zählen;
- Issues und PRs je Woche nach Art, Signatur (Claude, Codex, Astra, unbekannt) und Eingriffen des Eigentümers (Label `rettung-eigentümer`, Wiederöffnen, Einwände, soweit mechanisch erkennbar);
- wann welche Regel, welches Werkzeug, welcher Ablauf entstand (erste Commits je Datei in `methodology/`, `tools/`, `.github/`, `engineering/`, `docs/`, Spickzettel), als Fortschreibung der Systemkarte über den 09.10. hinaus, wo `engineering/catalog/` endet.

Die Zuordnung von Pfaden zu Bereichen ist eine Wahl. Sie wird im Ergebnis offengelegt. Metadaten zeigen, *dass* etwas geschah, nicht *warum*.

### T – Tiefe an Wendepunkten (gezielt, ganz gelesen)

**Auswahl, vorab festgelegt:** Ein Wendepunkt ist eine Woche, in der der Anteil der Forschungszeilen an allen hinzugefügten Zeilen gegenüber der Vorwoche um mindestens 30 Prozentpunkte steigt oder fällt, oder in der Systemarbeit nach mindestens einer Woche Pause wieder einsetzt. Dazu kommen alle Ereignisse mit Label `rettung-eigentümer`. Die Liste der Wendepunkte wird festgehalten, **bevor** Quellen dazu gelesen werden.

Je Wendepunkt werden **ganz** gelesen: die Issues und PRs, die in den sieben Tagen davor eröffnet oder kommentiert wurden und den Umschlag tragen (Auswahl über Commits und Verweise, nicht über Titel), sowie der jeweilige `STATUS.md`-Stand. Gefragt wird: Was geschah? Wer entschied? Was war die erklärte Absicht? Welche Hypothese sagt das voraus, welche nicht?

### Synthese

Ein Wirkungsgefüge entsteht nur aus Hypothesen, die an den Wendepunkten bestanden haben. Was nicht erklärt ist, bleibt als offen stehen. Erst danach folgen Rechercheauftrag zu Best Practice (#405 §6) und Maßnahmen, getrennt von dieser Analyse.

## 6. Frühwarnung, die den Inhalt prüft

| Prüfung | Woran sie erkennt, dass etwas schiefgeht |
|---|---|
| W1 Explananda | Am Ende fehlt zu einem Punkt aus Abschnitt 2 die Einordnung „erklärt / teilweise / nicht“. |
| W2 Gegenhypothese | Eine Ursachenaussage steht ohne die Hypothesen, die sie verdrängt, und ohne den Beleg, der zwischen ihnen entscheidet. |
| W3 Bekannte Erzählung | Das Ergebnis stimmt mit einer vorhandenen Analyse überein, ohne dass eine gezielte Suche nach Gegenbelegen dokumentiert ist (L023, #404 M3). |
| W4 Lesestand | Eine Aussage stützt sich auf eine Quelle, die im Leseprotokoll fehlt oder nur „teilweise“ steht. |
| W5 Auswahl | Wendepunkte oder Quellen wurden nach der Lektüre ausgewählt oder nachträglich ausgetauscht. |
| W6 Fundstelle | Eine Fundstelle lässt sich nicht auflösen oder ein Zitat steht nicht dort (mechanisch prüfbar mit F3/F4 aus `pruefung.py`). |
| W7 Lösungssprache | Maßnahmen oder Empfehlungen erscheinen in der Analyse. |
| W8 Blindheit | Eine Lesung von Nr. 632 wird zitiert oder geöffnet. |
| W9 Einwand | Auf einen Einwand folgt eine Teilberichtigung ohne erneute Prüfung aller betroffenen Grundannahmen (#404 M4). |

## 7. Prüfung des Ansatzes vor der Ausführung (Auftrag C)

### Gegen die Fragen aus #230, sinngemäß auf eine Analyse angewandt

1. *Welche Phänomene erfasst der Ansatz?* Alle Explananda in Abschnitt 2; W1 erzwingt die Rechenschaft je Punkt.
2. *Was bleibt offen?* Ursachen, die keine Spur im Repo hinterlassen haben (zum Beispiel der Inhalt nicht gespeicherter Chats und das Verhalten des Eigentümers außerhalb von GitHub). Sie werden als nicht prüfbar benannt.
3. *Verschwindet die Last oder wandert sie?* Die Lektüre wandert nicht an Astra und nicht an den Eigentümer. Der Eigentümer muss nichts anstoßen außer dem Start eines Folgechats, falls der Kontext dieses Chats endet; der Stand liegt dann auf dem Branch.
4. *Woran zeigt sich, dass der Ansatz genügt?* Am Pilot (Abschnitt 9): Er muss an einem Wendepunkt mindestens eine Hypothese von einer anderen unterscheiden können. Gelingt das nicht, ist der Ansatz nicht tragfähig, und es folgt der Rechercheauftrag.
5. *Was kann man danach weglassen?* Wenn S und T die Explananda tragen, ist das gleichmäßige Lesen aller 992 Quellen nicht nötig.

### Gegenextreme

- **Zu klein:** nur die vorhandenen Analysen zusammenfassen. Folge: Ihre gemeinsamen Prämissen würden vererbt (H-I), der zeitliche Verlauf bliebe ungeprüft. Ausgeschlossen durch S und T.
- **Zu groß:** alle 2,3 Mio. Tokens gleichmäßig lesen. Folge: Zerlegung in Einheiten nach Dateigröße, Befunde ohne Zusammenhang, viele Durchgänge mit Anstoß durch den Eigentümer, Prüfung nur der Form (Kommentar in #406). Ausgeschlossen durch Auswahl nach Wendepunkten.
- **Falsche Tiefe:** Wendepunkte nach Gefühl wählen. Folge: Die bekannte Erzählung bestätigt sich selbst. Ausgeschlossen durch die vorab festgelegte Regel (W5).

### Gegen die Fehlerliste in #405 §3

| Fehler des vorigen Chats | Wie der Ansatz ihn verhindert |
|---|---|
| 1 Urteil nach Titeln und Zählungen, Kürzung ungesagt | Zählungen sind nur die Struktur S und als Metadaten gekennzeichnet; Urteile nur nach Volllektüre in T; Leseprotokoll (W4). |
| 2 Bekannte Erzählung bestätigt | Neun konkurrierende Hypothesen, darunter die Nullhypothese H-G; W3. |
| 3 Antwort aus dem Allgemeinwissen | Befunde nur mit Fundstelle (W6). Die Methode (Hypothesen vorab, Prüfung am Verlauf) ist eine methodische Wahl und kein Befund; sie ist hier offengelegt und angreifbar. |
| 4 Absicht gedeutet statt geprüft | H-C prüft die erklärte Absicht an jedem Wendepunkt ausdrücklich. |
| 5 Flicken auf Einwände | W9. |
| 6 Billige Lösungen | Keine Lösungen in dieser Analyse (W7). |
| 7 Probleme weitergereicht | Umfang durch Auswahl gelöst statt weitergereicht; Entscheidung zu #406 trifft dieser Chat selbst. |
| 8 Neues Verfahren ohne Prüfung auf Vorhandenes | Sollliste und Exporte aus #408 werden weiterverwendet; `engineering/catalog/` ist Ausgangspunkt der Systemkarte; Prüfungen F3/F4 werden übernommen. |

### Grenzen, die bestehen bleiben

- **Unabhängigkeit nur teilweise.** Dieser Chat gehört zur Modellfamilie, die viele der untersuchten Abläufe gebaut hat, und hat die vorhandenen Analysen vor der Festlegung gelesen. Ausgleich: Hypothesen vorab, Nullhypothese, Auswahl nach Regel. Eine wirklich unabhängige Gegenprüfung (zum Beispiel ein zweiter Analyst ohne Kenntnis der Hypothesen an denselben Wendepunkten) ist möglich, aber nicht Teil des Pilots.
- **Methodenwahl ohne Rechercheabsicherung.** Hypothesen vorab festzulegen und am Verlauf zu prüfen, ist eine verbreitete Vorgehensweise der Ursachenforschung, hier aus allgemeinem methodischem Wissen gewählt und nicht recherchiert. Ob es bessere Verfahren gibt, klärt der spätere Rechercheauftrag (#405 §6).
- **Was keine Spur hinterließ, bleibt unsichtbar:** Chatverläufe außerhalb von GitHub, die Zeit des Eigentümers.

## 8. Entscheidung zu #406 und #408 (Auftrag D)

- **#406 (Erhebung durch Astra in 21 Einheiten): verworfen.** Gründe stehen im Kommentar des übergebenden Chats in #406 und treffen zu, nachgeprüft an `README.md` und `sollliste.tsv`: gleichmäßige Lektüre nach Dateigröße, Befunde auf 30 Wörter gekürzt, Prüfung nur der Form, viele Anstöße durch den Eigentümer. Hinzu kommt: Die vorab festgelegte Auswahl nach Wendepunkten macht die Volllektüre aller Quellen für die Ursachenfrage unnötig.
- **#408 / Branch:** bleibt Ort der Analyse. **Weiterverwendet:** `sollliste.tsv` (Bestand und Umfang), `export/` (auflösbare Fundstellen `pfad:Zeile`), aus `pruefung.py` die Prüfungen F3 und F4. **Nicht verwendet:** die Einheiten, das Befundformat und die übrigen Prüfungen.
- Die Pause #399 bleibt unberührt.

## 9. Pilot

1. **S vollständig:** Zeitachse und Fortschreibung der Systemkarte über die ganze Laufzeit (`analyse/struktur.md`, erzeugt durch `analyse/struktur.py`).
2. **Wendepunkte bestimmen** nach Abschnitt 5 und festhalten, bevor dazu gelesen wird.
3. **T am ersten Wendepunkt**, an dem Forschung in Systemarbeit umschlägt: Quellen ganz lesen, Hypothesen H-A bis H-I prüfen.
4. **Prüfung des Pilots:** Konnte er mindestens zwei Hypothesen voneinander unterscheiden? Wenn ja, ist der Ansatz tragfähig, und die übrigen Wendepunkte folgen. Wenn nein, wird begründet, welches Kriterium aus #405 §4B nicht erfüllbar ist, und der Rechercheauftrag angelegt.

---

## Nachträge

**N1 (03.11.2026, vor der Auswertung):** Ergänzung zur Wendepunktregel in Abschnitt 5: Wochen mit weniger als 200 auf `main` hinzugefügten Zeilen werden für den Anteil übersprungen. Grund: In Wochen mit einem einzigen kleinen Commit schwankt der Anteil zufällig zwischen 0 und 100 %. Festgelegt beim Schreiben von `struktur.py`, bevor die Wochenzahlen erzeugt wurden.
