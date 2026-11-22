# Requirements

This directory is the repository surface for **accepted reusable Requirement baselines**. Cross-project Human-owner decision/admission evidence is preserved under `engineering/evidence/decisions/`; moving that evidence does not absorb its authority into SD-KA-01.

## Current accepted baseline

`domain-requirements.tsv` is the current structured reusable Requirement inventory referenced by the canonical engineering configuration.

A file's presence under `requirements/` is **not** by itself evidence that it is accepted/current. Authority and lifecycle come from the owning contract and canonical configuration.

## Anforderungskette (seit 22.11.2026)

Hier steht die Kette **Intent → Bedürfnis → Pain → Anforderung → Prüfung** an einer Stelle:

- `beduerfnisse.tsv`: Intent, Rahmenbedingungen, Bedürfnisse und Pains des Eigentümers. Jede Zeile nennt den wörtlichen O-Ton und seine Fundstelle (`docs/o-toene.md`); die Aussage daneben ist eine Ableitung mit Status `wörtlich`, `abgeleitet` oder `Hypothese`.
- `domain-requirements.tsv`: die Anforderungen der Fächer, ergänzt um `kurz` (deutsche Kurzbezeichnung), `need_ids` (welchem Bedürfnis oder Pain sie dient, oder `fach`), `applies_from` (ab welcher Reifestufe G1–G6, `immer` oder `Auslöser: …`), `verified_by` (Tests als `tests/…py::test_…`, `Fachurteil`, `Gebrauch` oder `keine`), `depends_on` und `overlaps`.
- `kette.md`: daraus erzeugte Leseansicht mit Lücken, Überschneidungen und Tests ohne Anforderung. Nicht von Hand ändern.

`tools/anforderungskette.py pruefen` prüft die Kette und ob die Ansicht aktuell ist; `tests/test_anforderungskette.py` läuft in der Gesamtprüfung mit. Die Prüfung belegt Verknüpfung, wörtliche O-Töne und vorhandene Tests, nicht die fachliche Erfüllung einer Anforderung.

## WP5 migration result in this namespace

WP5 has removed the former mixed audit/research/design/learning/work-instruction/coordination/decision-evidence accumulation from this namespace after inspecting actual status and ownership. Classified engineering material now lives under semantic `engineering/` owners while retaining stable managed IDs and legacy-path compatibility mappings.

Current managed migration/rollback evidence lives in:

- `engineering/catalog/artifacts.tsv`
- `engineering/catalog/legacy-paths.tsv`
- `engineering/changes/SD-KA-01/MIGRATION.tsv`

The SD-KA-01 admission material itself lives with the bounded change under `engineering/changes/SD-KA-01/`. Separately owned cross-project Human decision/admission records live under `engineering/evidence/decisions/`; their `owner_scope`, authority role and lifecycle remain unchanged by relocation.

Old paths for migrated managed artifacts are compatibility locators only; they are not parallel copies or currentness owners. Use the legacy-path catalog to resolve them.

No Project purpose, scholarly priority, manuscript state or scholarly `NEXT ACTION` is owned by this directory.
