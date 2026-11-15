# Pilot: Wendepunkt W1 (12.–15.09.2026), Forschung schlägt in Systemarbeit um

Stand: 03.11.2026 · Claude · gehört zu `ansatz.md` (Abschnitt 9) und `struktur.md`. Keine Lösungen, keine Maßnahmen.

**Belegstand:** *beobachtet* heißt, es steht so in der Quelle. *Aussage* heißt, ein Beteiligter sagt es; fast alle Texte stammen von KI-Chats unter dem Konto `esany`, auch wenn sie den Eigentümer wiedergeben. *Deutung* ist meine eigene Lesart und als solche angreifbar.

## 1. Was gelesen wurde

Ganz gelesen, wie in Nachtrag N3 vorab festgelegt: `export/issues/0165.md`, `0166.md`, `0169.md`, `0171.md`, `0183.md`, `0201.md`, `0203.md`, `0204.md`; `projects/ega-reg-ii-5-knau/research/post-166-research-framing-review-2026-09-14.md` (`main@22b255b`); `projects/ega-reg-ii-5-knau/STATUS.md` am Commit `5b865d9`, Abschnitte „Project authority and current scope“ und „#166 terminal scholarly result“ (Zeilen 1–60).
Zusätzlich ganz gelesen, weil #183 die Audits vom 14.09. als Anlass nennt: `0177.md` (PR, mit dem diese Audits auf `main` kamen).
Das Audit vom 14.09. selbst war schon vorher gelesen (Leseprotokoll in `ansatz.md`).

## 2. Ablauf, belegt

| Zeit | Was geschah | Fundstelle | Belegstand |
|---|---|---|---|
| 12.09. | Der Eigentümer wählt #166, eine eng begrenzte Forschungsfrage zu zwei Absätzen in Reg. Ii 5. | `STATUS.md@5b865d9`, Abschnitt „#166 terminal scholarly result“ | Aussage |
| 12.–13.09. | Parallel laufen Versuche, mehrere ChatGPT-Chats über Slack zu koordinieren, vom Eigentümer freigegeben. Ergebnis: Rückmeldungen des Eigentümers in Slack erreichen keinen Chat von selbst. | `0171.md:49`, `0171.md:110-118` | beobachtet |
| 12.–13.09. | #166 scheitert zunächst am Bildzugriff: Der Connector liefert die privaten Bildanhänge nicht. Daraus wird ein Regelvorhaben (#169), vom Eigentümer ausdrücklich angeordnet („make this change directly at all necessary places“). | `0166.md:263-298`, `0169.md:105`, `0169.md:216` | beobachtet |
| 13.09. | Der Eigentümer liefert die PDF selbst. #166 wird am Original geprüft und beantwortet: zwei getrennte Absätze, zwei Regeln; Rest bleibt als Ergebnisgrenze offen. | `0166.md:30`, `0166.md:110-119` (R6) | beobachtet |
| 13.09., 21:55 | Abschluss mit dem kanonischen Satz, dass **keine nächste Forschungsfrage ausgewählt** ist; ein Test sichert ausdrücklich, dass keine automatisch startet (Commit `181bd89`, „without auto-next scope“). | `0166.md:144-146`; `git log 181bd89` | beobachtet |
| 14.09., 08:46 | Zwei Audits kommen auf `main`, laut PR „vom Eigentümer angefordert“: das Audit zum transdisziplinären Ansatz und eine Rückschau nach #166. | `0177.md:10` | Aussage |
| 14.09. | Die Rückschau hält zwei Klarstellungen des Eigentümers fest: Vorrang bleibt beim begrenzten Knau-Abschnitt; `paleo-type` ist ein **allgemeines Forschungswerkzeug** für sehr verschiedene künftige Projekte. Sie erklärt, warum die Forschung „wie Stillstand“ wirkte, und nennt fünf Familien möglicher nächster Forschungsfragen im Knau-Abschnitt. | `post-166-research-framing-review-2026-09-14.md:55-56`, `:60-66`, `:270` | Aussage |
| 14.09. | Am selben Tag entstehen ein Forschungsprogramm über das System (#183–#191) und eine Synthese (#198), alle noch am 14.09. abgeschlossen. | `0183.md`; `struktur.md` Abschnitt 1 | beobachtet |
| 14.09. | Dem Eigentümer werden sechs Wege vorgelegt, darunter **A: eine Forschungsfrage** und **B: Systemanforderungen klären**. | `0201.md:71` | beobachtet |
| 15.09. | Der Eigentümer wählt **B** („Go“). Daraus entsteht eine Methodenregel (D-020) zur Bildung mehrerer Forschungsrichtungen vor einer Prioritätsentscheidung; danach „beobachten, dann STOP“. | `0201.md:84-86`, `0204.md` | beobachtet |
| bis heute | Für Reg. Ii 5 ist seit dem 13.09. keine nächste Forschungsfrage ausgewählt. | `projects/ega-reg-ii-5-knau/STATUS.md:153` (`main@22b255b`) | beobachtet |

## 3. Prüfung der Hypothesen an W1

| Hypothese | Ergebnis an W1 | Begründung |
|---|---|---|
| H-A fachliche Wand | **nicht gestützt als Auslöser** | #166 endete mit Erkenntnis und benannter Ergebnisgrenze, nicht an einer Lesegrenze. Die Rückschau vom 14.09. nennt fünf weiterführende Fragen im selben Abschnitt. Die Forschung hätte weitergehen können. |
| H-B Vorfall → Struktur | **gestützt für #169, nicht für die große Welle** | Der Bildzugriffsfehler wurde sofort zur Regel. Die Welle ab 14.09. folgt aber keinem Vorfall, sondern dem Abschluss von #166. |
| H-C Auftrag des Eigentümers | **gestützt, mit Einschränkung** | Audits „vom Eigentümer angefordert“ (Aussage), Weg B vom Eigentümer gewählt (beobachtet), #169 vom Eigentümer angeordnet. Einschränkung: Die Wege hat ein KI-Chat formuliert; warum der Eigentümer B statt A wählte, steht nirgends. Die Absicht ist **nicht prüfbar** aus dem Repo. |
| H-D Plattform und Rollen | **gestützt als Nebenstrang** | Connector ohne Zugriff auf Bildanhänge (#166), Chats ohne gegenseitige Verbindung (#162, #171); in beiden Fällen springt der Eigentümer ein (PDF liefern, Nachrichten weiterreichen). Das ist E4/P10 schon am 12.–13.09. |
| H-E Regeln ohne Wirkung | **an W1 nicht prüfbar** | Erst spätere Wiederkehr kann das zeigen. |
| H-F fehlende Frage | **gestützt in enger Form** | Nicht eine übergeordnete Forschungsfrage fehlte, sondern die **nächste ausgewählte Frage**. Das System hält an dieser Stelle absichtlich an und wartet auf den Eigentümer (`0166.md:144-146`, Test `181bd89`). In genau diese Lücke fällt die Systemwelle. |
| H-G notwendige Investition | **offen** | Prüfbar erst am weiteren Verlauf: Hat D-020 später eine Forschungsrichtung hervorgebracht? Für Reg. Ii 5 nicht (`STATUS.md:153`); für Nr. 632 noch ungeprüft. |
| H-H Größe schlägt Kontext | **an W1 nicht entscheidend** | Das Repo war am 14.09. klein im Vergleich zu später (`struktur.md` Abschnitt 4). |
| H-I Prämisse vererbt | **teilweise gestützt** | Die Diagnose „Rahmung der nächsten Frage fehlt“ vom Morgen des 14.09. wurde am selben Tag zum Rahmen des ganzen Forschungsprogramms #183–#191. #183 warnt selbst vor genau diesem Risiko („Concept Bias“, `0183.md:25`). |

## 4. Befund des Pilots

**Beobachtet:** Der Umschlag von Forschung in Systemarbeit am 14.09. folgt unmittelbar auf eine **abgeschlossene** Forschungsfrage, an einer Stelle, an der das System bewusst auf eine Auswahl durch den Eigentümer wartet. Die Systemarbeit wurde vom Eigentümer angefordert und gewählt; eine Forschungsfrage stand als Weg A zur Wahl.

**Deutung (angreifbar):** Die Rückschau vom 14.09. hat das Fehlen einer Funktion erkannt, nämlich mögliche nächste Fragen zu bilden und zu vergleichen. Sie hat diese Funktion für den Knau-Abschnitt sogar schon skizziert (fünf Fragefamilien). Die Antwort darauf war eine **Regel** über diese Funktion (D-020), nicht ihre **Ausübung** am Fall. Danach wurde keine der fünf Fragen weiterverfolgt. Damit wird an W1 ein fachlicher Entscheidungsbedarf in Systemarbeit übersetzt, mit Zustimmung des Eigentümers.

**Gegenprobe zur bekannten Erzählung (W3):** Die Erzählung „Verfahren verdrängt Forschung“ (#89, #129, #394, #402) unterstellt, die KI sei gegen das Ziel abgedriftet. An W1 trifft das so nicht zu: Die Forschung war fertig, und der Wechsel war gewählt. Gestützt wird eine andere Lesart: An Entscheidungspunkten nach einer abgeschlossenen Frage fehlt ein Weg zur nächsten Frage, der leichter wäre als der Weg zur Systemarbeit.

**Was dies nicht zeigt:** ob dasselbe an späteren Wendepunkten gilt; warum der Eigentümer B wählte; ob D-020 später bei Nr. 632 wirkte.

## 5. Prüfung des Pilots (Kriterium aus `ansatz.md`, Abschnitt 9.4)

Der Pilot unterscheidet Hypothesen: H-C und H-F (eng) sind gestützt, H-A ist als Auslöser nicht gestützt, H-B nur für den Nebenstrang. **Der Ansatz ist damit tragfähig.** Ein Rechercheauftrag nach #405 §4E ist nicht nötig.

Schwächen, die der Pilot gezeigt hat:
1. Die Wendepunktregel misst nur `main`. Forschung auf offenen Branches (Nr. 632) entgeht ihr (Nachtrag N2). Für W2 muss das berücksichtigt werden.
2. Die Absicht des Eigentümers ist nur über Wiedergaben von KI-Chats im Repo. Wo sie entscheidend ist, bleibt sie offen.
3. Ein einzelner Analyst. Die Auswahl der Quellen war vorab festgelegt, die Bewertung nicht unabhängig geprüft.

## 6. Nächste Schritte der Analyse

1. W2 (Woche ab 26.10., nachträglich benannt) und die Ereignisse mit `rettung-eigentümer` (#355, #358, #359), mit Quellenauswahl vorab wie in N3.
2. Übergang 09.10. → zwei Wochen ohne Aktivität → 26.10.: Was endete am 09.10., was begann am 26.10.?
3. H-G am Verlauf prüfen: Hat die Systemarbeit vom 14.09. bis 09.10. die spätere Forschung an Nr. 632 erkennbar gestützt?
4. H-E an einer Fehlerfamilie über die Zeit prüfen (zum Beispiel Ressource als Blocker: #169 am 13.09., #296 am 05.10., #297).
5. Danach Synthese gegen die Explananda E1–E4 und P1–P13.
