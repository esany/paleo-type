# Requirements

This directory is the repository surface for **accepted reusable Requirement baselines**. Cross-project Human-owner decision/admission evidence is preserved under `engineering/evidence/decisions/`; moving that evidence does not absorb its authority into SD-KA-01.

## Current accepted baseline

`domain-requirements.tsv` is the current structured reusable Requirement inventory referenced by the canonical engineering configuration.

A file's presence under `requirements/` is **not** by itself evidence that it is accepted/current. Authority and lifecycle come from the owning contract and canonical configuration.

## Anforderungskette (seit 22.11.2026)

Hier steht die Kette **Intent → Bedürfnis → Pain → Anforderung → Prüfung** an einer Stelle:

- `beduerfnisse.tsv`: Intent, Rahmenbedingungen, Bedürfnisse und Pains des Eigentümers. Jede Zeile nennt den O-Ton und seinen Abschnitt in `docs/o-toene.md`. Die Aussage daneben ist eine Ableitung der KI, gekennzeichnet als `wörtlich` (gibt den O-Ton nur wieder), `abgeleitet` (deutet ihn) oder `Hypothese`.
- `domain-requirements.tsv`: die Anforderungen der Fächer, ergänzt um sechs Spalten:
  - `kurz`: deutsche Kurzbezeichnung;
  - `need_ids`: welchem Bedürfnis, Pain oder welcher Rahmenbedingung die Anforderung dient, oder `fach`, wenn nur ein Fach sie begründet;
  - `applies_from`: ab welcher Reifestufe sie gilt (G1–G6), `immer` oder `Auslöser: …`;
  - `verified_by`: Tests als `tests/…py::test_…`, `Fachurteil`, `Gebrauch` oder `keine` (prüfbar, kein Test bekannt);
  - `depends_on` und `overlaps`.

  Die Spalten haben verschiedene Rollen und stehen nicht in Konkurrenz: `validation_mode` sagt, wie die Anforderung laut Fachaudit zu prüfen wäre; `current_support` ist die Selbstbewertung aus den KI-Fachaudits #26–#37 (Tabelle angelegt am 27.08.2026, vor dieser Änderung zuletzt am 08.09.2026 geändert); `verified_by` sagt, was sie heute im Repo prüft.
- `funktionen.tsv`: Funktionen, die Gruppen von Anforderungen absichern. Je Funktion stehen dort: welchen Schmerz ihr Fehlen verursacht und wie groß er ist, Befunde je Perspektive und Dimension (jede mit Befund und Herkunft oder ausdrücklich ohne Befund), Abhängigkeiten, DOR, DOD mit dem Test, an dem „fertig“ prüfbar ist, Iterationen und Rang. Größe, Rang und Befunde sind ein Vorschlag der KI; über die Reihenfolge entscheidet der Eigentümer. Die Issues zu den Funktionen werden mit `tools/anforderungskette.py issue FN-…` aus dieser Tabelle erzeugt und sind kurz zu halten (höchstens 4000 Zeichen).
- `kette.md`: daraus erzeugte Leseansicht mit Lücken, Überschneidungen und Tests ohne Anforderung. Nicht von Hand ändern.

**Status der Zuordnungen:** Die neuen Spalten hat Claude am 22.11.2026 abgeleitet, aus Anforderungstext, Testnamen und Werkzeugbeschreibungen. Der Eigentümer hat sie nicht bestätigt.

`tools/anforderungskette.py pruefen` prüft die Kette und ob die Ansicht aktuell ist. `tests/test_anforderungskette.py` gehört zur Gesamtprüfung `tools/check.py`.

Was geprüft wird:
- ob ein O-Ton als ganze Wörter in einem einzelnen Zitat des genannten Abschnitts steht (KI-Wortlaut, den der Eigentümer innerhalb eines Zitats wiedergibt, erkennt die Prüfung nicht);
- ob jede Anforderung verknüpft ist;
- ob die genannten Tests existieren.

Nicht geprüft wird, ob ein Test die Anforderung inhaltlich abdeckt und ob sie fachlich erfüllt ist.

## WP5 migration result in this namespace

WP5 has removed the former mixed audit/research/design/learning/work-instruction/coordination/decision-evidence accumulation from this namespace after inspecting actual status and ownership. Classified engineering material now lives under semantic `engineering/` owners while retaining stable managed IDs and legacy-path compatibility mappings.

Current managed migration/rollback evidence lives in:

- `engineering/catalog/artifacts.tsv`
- `engineering/catalog/legacy-paths.tsv`
- `engineering/changes/SD-KA-01/MIGRATION.tsv`

The SD-KA-01 admission material itself lives with the bounded change under `engineering/changes/SD-KA-01/`. Separately owned cross-project Human decision/admission records live under `engineering/evidence/decisions/`; their `owner_scope`, authority role and lifecycle remain unchanged by relocation.

Old paths for migrated managed artifacts are compatibility locators only; they are not parallel copies or currentness owners. Use the legacy-path catalog to resolve them.

No Project purpose, scholarly priority, manuscript state or scholarly `NEXT ACTION` is owned by this directory.
