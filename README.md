# paleo-type

Lean, evidence-based workspace for transparent transcription, source criticism and scholarly analysis of early modern handwritten sources.

## Purpose

The highest-order purpose, precedence and Human Owner change authority are defined once in `GOVERNING_OBJECTIVE.md`.

This README is the repository **orientation and reading-path view**. It is not a second method manual, Project status store or executable contract. The research sources and scholarly result are the product; software, AI, GitHub and working formats are support infrastructure.

## Repository layers

- **METHOD** — `methodology/`, `AGENTS.md`, `DECISIONS.md`, `templates/`: reusable scholarly/operational rules, governance rationale and templates.
- **REQUIREMENTS** — `requirements/`: accepted reusable Requirement baselines plus namespace navigation. Historical engineering evidence no longer lives here after WP5.
- **ENGINEERING** — `engineering/`: engineering configuration, bounded changes, ADRs, assurance, semantic catalogs and non-default engineering evidence/history.
- **CORPUS** — `corpus/`, `entities/`: canonical Source/File identity, reusable source-wide mappings, evidenced relationships and normalized entities.
- **PROJECT** — `projects/<id>/`: durable scholarly state for one purpose-established investigation, including source use, evidence binding, transcription/analysis and current research state.

Project existence or priority is never inferred from Source/File structure or engineering state. Detailed semantics live in the owning methodology and Project files.

## Start here

### Human

1. Read this README for orientation.
2. Read `GOVERNING_OBJECTIVE.md` for purpose, precedence and Human Owner authority.
3. Open the relevant Project `project.yml` for purpose/scope/documentary anchor.
4. Open its `STATUS.md` for actual gate/evidence/restart state and authorized `NEXT ACTION` when one exists.
5. Open Project `source-uses.tsv` / `research/use-evidence.tsv` when Project→Source use or concrete File evidence matters.
6. Follow the owning methodology file for the specific question.

### AI / implementation agent

1. read `GOVERNING_OBJECTIVE.md` and `AGENTS.md`;
2. read the relevant Project/Corpus or engineering canonical state;
3. establish and load every canonical rule/requirement applicable to the concrete task;
4. use resolver/generated context where available instead of reconstructing structure/priority from names or chat;
5. continue only from an authorized task/`NEXT ACTION` when one exists.

Old chat must never be required to reconstruct durable research or engineering state.

## Current system-development navigation

The Human-visible system-development work/decision view is GitHub **#244**. SD-KA-01 implementation is decomposed as **#256–#261** under the recorded D-016 admission.

Canonical current owners:

- `engineering/configuration.json` — accepted baselines, active change, explicit current focus/absence and transition provenance;
- `engineering/changes/SD-KA-01/STATE.json` — bounded change/work-package lifecycle;
- `engineering/changes/SD-KA-01/RESULT.md` — completed work-package results and whole-system returns;
- `engineering/changes/SD-KA-01/D016-DECISION-BRIEF.md` and `D016-OWNER-ADMISSION.md` — admitted target/scope and Human-Owner admission;
- `engineering/catalog/` — managed identities, finding/coverage/relations and legacy-path continuity;
- `engineering/changes/SD-KA-01/MIGRATION.tsv` — WP5 migration classification, exact pre-move blob identity and rollback evidence.

Current process state:

> **D-016 ADMITTED / WP1–WP5 VERIFIED + RETURNED / WP6 QUALIFICATION + TERMINAL RESULT REVIEW IN PROGRESS / SD-KA-01 ACTIVE.**

**#261 / WP6 is the current bounded system-development focus:** adversarially qualify the engineering system and perform the terminal SD-KA-01 Result Review. It is executing inside the existing D-016 admission. Accepted architecture/Requirement baselines remain unchanged while qualification is in progress; technical PASS does not establish scholarly, specialist, Human or evidential-independence claims.

For a derived Human-readable rendering of the same repository state use:

`python tools/engineering_context.py --profile human-system-overview --format text`

A generic invocation may resolve context-relative current/next work, but the visible result must remain a meaningful action with scope and provenance. Ambiguity is surfaced rather than silently collapsed into one repository-global cursor.

## Post-WP5 information architecture

`requirements/` is now intentionally narrow: `README.md` plus the accepted reusable `domain-requirements.tsv` baseline. The historical mixed engineering corpus has moved to semantic owners without changing authority or currentness:

- SD-KA bounded change evidence: `engineering/changes/SD-KA-01/`;
- architecture rationale: `engineering/decisions/`;
- cross-project Human decision/admission evidence: `engineering/evidence/decisions/`;
- audits/reviews: `engineering/evidence/audits/`;
- research/design/problem evidence: `engineering/evidence/research/`;
- learning: `engineering/evidence/learning/`;
- historical work instructions/prompts: `engineering/evidence/work-instructions/`;
- coordination history retained as evidence: `engineering/evidence/coordination/`.

Moved managed artifacts keep stable `ENG-A-*` identity. `engineering/catalog/legacy-paths.tsv` resolves former paths; those locators are compatibility/navigation only and are not parallel truth stores. `engineering/changes/SD-KA-01/MIGRATION.tsv` records the three bounded WP5 migration slices and exact pre-move blob identities.

The current engineering configuration, context and Result owners should be read before deeper historical evidence. Historical evidence is loaded on demand, not as mandatory default context.

## Engineering verification boundary

`python tools/check.py` is the shared local/CI deterministic full-check entrypoint. It covers Source Contract validation, Engineering validation, the engineering-fitness mapping/safeguards, regressions, fresh-process Project contexts and managed real-data resolver fixtures.

A green check establishes only the formal/deterministic properties actually exercised at that exact head. It does **not** establish manuscript truth, specialist validity, evidential independence, Human Owner acceptance, external runtime/preservation fitness or whole-system/programme closure.

## Historical programme boundaries

- **#225** is closed as GitHub work metadata, but F17 preserves the unresolved scholarly whole-system acceptance boundary; engineering CI cannot convert it into a scholarly PASS.
- **#230** is completed as the bounded audit owner that led into the current engineering work; closing it did not itself admit implementation.
- the former **#206** programme remains historical/terminal at its explicit STOP; later separately authorized work does not rewrite that history.
- **Route B / #90** remains deferred under its Human-Owner disposition.
- the separately admitted outcome-preserving execution-control family remains under its own owners (#280/#285 etc.); SD-KA assurance consumes only repository-testable consequences that fit its admitted scope.

## Where truth lives

| Question | Canonical owner |
|---|---|
| Why does the repository exist / what has precedence? | `GOVERNING_OBJECTIVE.md` |
| What stable AI/research guardrails apply? | `AGENTS.md` |
| What accepted cross-project decision history matters? | `DECISIONS.md` |
| What is the authoritative scholarly end-to-end method? | `methodology/historical-source-workflow.md` |
| What are the generic research gates? | `methodology/research-gates.md` |
| How are Projects established, anchored and prioritized? | `methodology/project-lifecycle.md` |
| How are Source/File identity, provenance and preservation handled? | `methodology/source-and-provenance.md` |
| What evidence/source-status semantics apply? | `methodology/evidence-policy.md` |
| How is diplomatic transcription handled? | `methodology/transcription-guidelines.md` |
| How are execution context, prerequisites, retries and loops handled? | `methodology/workflow.md` |
| How are quality/falsification/review dimensions handled? | `methodology/quality-and-learning.md` |
| How are ownership, D-016 admission and propagation handled? | `methodology/maintenance.md` |
| What stable Source/File/Project-use constraints apply? | `corpus/source-contract.json` + `tools/source_contract.py` |
| What is the accepted reusable Requirement inventory? | `requirements/domain-requirements.tsv` |
| What is the accepted engineering baseline / active change / explicit focus? | `engineering/configuration.json` |
| What is the bounded SD-KA lifecycle? | `engineering/changes/SD-KA-01/STATE.json` |
| What did completed SD-KA work establish? | `engineering/changes/SD-KA-01/RESULT.md` |
| What managed engineering artifacts/findings/relations exist? | `engineering/catalog/` |
| What owns moved-path compatibility? | `engineering/catalog/legacy-paths.tsv` |
| What owns WP5 migration/rollback evidence? | `engineering/changes/SD-KA-01/MIGRATION.tsv` |
| What owns derived engineering context behavior? | `engineering/context/README.md` |
| What owns bounded `.prompt` behavior? | `engineering/prompts/CONTRACT.md` |
| What owns deterministic engineering-fitness mappings? | `engineering/assurance/fitness.json` + `tools/engineering_fitness.py` |
| What is a Source/File/relationship/crosswalk fact? | `corpus/` |
| What is one Project and its current scope? | Project `project.yml` |
| How does a Project use Sources? | Project `source-uses.tsv` |
| Which concrete File supports a Project use? | Project `research/use-evidence.tsv` |
| What is current Project restart/gate/evidence state? | Project `STATUS.md` |

One durable fact/state has one canonical owner. Human summaries, generated context, Issues and chat may point to it but must not become parallel truth stores.

## Current Project directories

The repository currently contains:

- `projects/ega-reg-ii-3/`;
- `projects/ega-reg-ii-4-bd-ii/`;
- `projects/ega-reg-ii-5-knau/`.

The last path is a legacy directory/id retained for continuity. Its current Project meaning, scope and priority are defined only by its canonical Project files, not by the slug.

**Do not copy current Project scope/gate/`NEXT ACTION` into this README.** Read the Project owner directly or use the rebuildable Project-context view.

## Repository structure

```text
GOVERNING_OBJECTIVE.md
AGENTS.md
DECISIONS.md
MILESTONES.md
README.md
methodology/
requirements/
engineering/
  architecture/
  assurance/
  catalog/
  changes/
  context/
  decisions/
  evidence/
  prompts/
templates/
corpus/
entities/
projects/
tools/
tests/
```

## Restartability acceptance

Another capable researcher/agent, given repository + authorized evidence and no old chat, should be able to determine:

- repository purpose and authority boundaries;
- Project purpose/scope and documentary anchor;
- canonical Source/File identity and structural relationships;
- Project-relative Source use and concrete evidence bindings;
- actual Project research/gate/evidence state and whether an authorized `NEXT ACTION` exists;
- which outputs are canonical versus derived;
- for system-development work, accepted engineering baselines, active admitted change state, explicit current/next work with provenance, applicable context, completed results, migration compatibility and the next permitted bounded transition.

If continuation requires stale orientation prose, duplicated state, inferred priority or recovery of old chat, the owning surface has drifted and must be repaired.
