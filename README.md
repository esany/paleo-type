# paleo-type

Lean, evidence-based workspace for transparent transcription, source criticism and scholarly analysis of early modern handwritten sources.

## Purpose

The highest-order purpose, precedence and Human Owner change authority are defined once in `GOVERNING_OBJECTIVE.md`.

This README is the repository **orientation and reading-path view**. It is not a second method manual, Project status store or executable contract.

The research sources and scholarly result are the product. Software, AI models, GitHub, connectors and working formats are support infrastructure.

## Repository layers

### METHOD

`methodology/`, `AGENTS.md`, `DECISIONS.md`, `templates/`

Reusable scholarly/operational rules, governance rationale and templates. Concrete Source/File/Project research state does not belong here.

### CORPUS

`corpus/`, `entities/`

Canonical historical/documentary Source identity, exact digital File identity, reusable source-wide mappings, evidenced relationships and shared normalized entities.

### PROJECT

`projects/<id>/`

Durable scholarly state for a purpose-established investigation: Project purpose/scope, documentary Source anchor, Project→Source research use, evidence bindings, transcription/analysis/decisions and research state.

Project existence/priority is not inferred from Source/File structure. Detailed semantics live in `methodology/project-lifecycle.md`.

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
2. read the relevant Project/Corpus canonical state;
3. establish and load every canonical rule/requirement applicable to the concrete task;
4. use resolver/generated context where available instead of reconstructing structure/priority from names or chat;
5. continue only from an authorized task/`NEXT ACTION` when one exists.

Old chat must never be required to reconstruct durable research state.

## Current system-development navigation

The Human-visible current system-development work/decision view is GitHub **#244**. Pre-implementation analysis/design Issues **#245–#253 are complete**. SD-KA-01 implementation is decomposed as **#256–#261** under the recorded D-016 admission.

The current material decision surface is the managed SD-KA change evidence:

`engineering/changes/SD-KA-01/D016-DECISION-BRIEF.md`

The D-016 Human-Owner admission is durably recorded in:

`engineering/changes/SD-KA-01/D016-OWNER-ADMISSION.md`

Their previous `requirements/` locators remain compatibility mappings in `engineering/catalog/legacy-paths.tsv`; they are not parallel truth stores.

Cumulative work-package results and whole-system returns are durably recorded in:

`engineering/changes/SD-KA-01/RESULT.md`

Current process state:

> **D-016 ADMITTED / WP1–WP4 VERIFIED + RETURNED / WP5 IMPLEMENTING / WP6 NOT STARTED / SD-KA-01 ACTIVE.**

The current bounded system-development action is: **execute the loss-checked brownfield information-architecture migration under #260/WP5, preserving stable identities/currentness/traceability/rollback and refusing filename-only reclassification.** This is execution inside the already admitted SD-KA-01 scope; it creates no new D-016 decision and no scholarly priority.

For a derived Human-readable rendering of the same repository state use:

`python tools/engineering_context.py --profile human-system-overview --format text`

A generic invocation may resolve context-relative current/next work, but the visible result must remain a meaningful action with scope and provenance. If work is ambiguous, the derived view exposes the ambiguity rather than silently selecting one repository-global cursor.

The compact failure-family/bugwave map is now `engineering/evidence/research/system-development-bugwave-master-map-2026-10-04.md`. Its historical readiness wording remains evidence only where it differs from later admitted/result state. **The canonical engineering configuration/change/result owners and #244 own the current non-scholarly implementation/navigation interpretation.**

The repository-native Engineering Knowledge & Configuration Plane is partially implemented: WP1 established the semantic/catalog foundation; WP2 established explicit currentness/applicability/query semantics; WP3 established derived Human/Developer/Agent contexts, Senior Developer bootstrap, bounded prompt behavior and the shared full-check entrypoint; WP4 established the ENG-FIT mapping, seeded falsification suite and explicit local/CI assurance boundary. WP5 is now physically separating already-classified engineering evidence from the Requirement namespace without changing accepted baselines. The accepted architecture/Requirement baselines remain deliberately distinct from the still-active admitted SD-KA-01 target package.

#256/WP1, #257/WP2, #258/WP3 and #259/WP4 are verified for their bounded slices. #260/WP5 is executing. #261/WP6 remains terminal adversarial qualification/Result Review and is not started by WP5 execution.

The admission permits only the bounded SD-KA-01 target and WP1–WP6 scope. No manuscript scope or scholarly `NEXT ACTION` follows from it; physical migration and later terminal qualification remain bounded implementation work, not automatically accepted scholarly or architecture state.

### Historical programme boundaries

- **#225** is CLOSED as GitHub work metadata. C1R (`tools/outcome_context.py`) is a bounded local PASS; repository evidence does **not** establish whole-system scholarly T11 acceptance merely from Issue closure. F17 preserves this residual explicitly.
- **#230** is CLOSED / COMPLETED as the bounded audit owner that led into the current knowledge/configuration work. Closing it did not admit implementation.
- The former **#206** programme remains historical/terminal at its explicit 2026-09-17 `STOP`; later separately authorized system-development work does not rewrite that history.
- **Route A** programme-continuity work is complete/resolved under its existing owners.
- **Route B / #90** remains explicitly DEFERRED under its Human-Owner disposition. The current bugwave does not reactivate branch-protection implementation.

Historical programme detail is evidence on demand, not the default current-work surface. Do not infer priority from the newest Issue, local CI `PASS`, Issue closure, filename date or old chat; resolve the applicable owner and current disposition.

## System-development evidence / deeper provenance

`requirements/` is being narrowed under WP5. The accepted reusable Requirement baseline remains there; already-classified SD-KA design/audit/research/admission material has moved to semantic engineering owners. Remaining historical, cross-project or still-unclassified `requirements/` material is not silently reclassified by filename and remains non-default until its actual owner/status supports a loss-checked destination.

Current navigation artifacts:

- current Human decision/admission surface: `engineering/changes/SD-KA-01/D016-DECISION-BRIEF.md` plus `engineering/changes/SD-KA-01/D016-OWNER-ADMISSION.md`;
- current engineering configuration/change/result owners: `engineering/configuration.json`, `engineering/changes/SD-KA-01/STATE.json`, `engineering/changes/SD-KA-01/RESULT.md`;
- WP5 migration/rollback evidence: `engineering/changes/SD-KA-01/MIGRATION.tsv` plus `engineering/catalog/legacy-paths.tsv`;
- derived context/profile contract and developer path: `engineering/context/README.md`;
- bounded prompt capability contract: `engineering/prompts/CONTRACT.md`;
- engineering fitness contract: `engineering/assurance/fitness.json` plus `engineering/assurance/README.md`;
- whole bugwave/failure-family map: `engineering/evidence/research/system-development-bugwave-master-map-2026-10-04.md`;
- source-audit finding coverage: `engineering/evidence/audits/system-development-bugwave-finding-coverage-2026-10-04.md`;
- finding promotion design: `engineering/evidence/research/system-development-bugwave-finding-promotion-design-2026-10-04.md`;
- architecture-decision inventory: `engineering/evidence/research/system-development-bugwave-adr-inventory-2026-10-04.md`;
- ADR surface design: `engineering/evidence/research/system-development-bugwave-adr-surface-design-2026-10-04.md`;
- configuration/reference design: `engineering/evidence/research/system-development-bugwave-configuration-reference-design-2026-10-04.md`;
- context/developer design: `engineering/evidence/research/system-development-bugwave-context-developer-design-2026-10-04.md`;
- readiness/Human decision contract: `engineering/evidence/research/system-development-bugwave-readiness-human-decision-contract-2026-10-04.md`;
- engineering assurance design: `engineering/evidence/research/system-development-bugwave-assurance-closure-design-2026-10-04.md`;
- brownfield migration design: `engineering/evidence/research/system-development-bugwave-brownfield-migration-design-2026-10-04.md`;
- bounded prompt transfer test evidence: `engineering/evidence/audits/prompt-skill-transfer-test-result-2026-10-04.md`;
- Review Premise Inheritance disposition: `engineering/evidence/research/review-premise-inheritance-generic-fit-2026-10-04.md`;
- underlying holistic architecture design: `engineering/evidence/research/system-development-holistic-knowledge-architecture-dev-ready-design-2026-10-04.md`;
- anti-regression baseline: `engineering/evidence/audits/system-development-pre-implementation-anti-regression-baseline-2026-10-04.md`.

The finding-coverage artifact links/dispositions the deeper September–October audit/research/learning chain. Load those source artifacts when reviewing the finding or its provenance, not as mandatory default context.

Use every artifact according to its stated evidence/authority status. None creates Project priority or implementation authority merely by existing or moving.

## Where truth lives

| Question | Canonical owner |
|---|---|
| Why does the repository exist / what has precedence? | `GOVERNING_OBJECTIVE.md` |
| What stable AI/research guardrails always apply? | `AGENTS.md` |
| What cross-project accepted rationale/decision history matters? | `DECISIONS.md` |
| What is the authoritative scholarly end-to-end method? | `methodology/historical-source-workflow.md` |
| What are the generic G1–G6 maturity requirements? | `methodology/research-gates.md` |
| How are Projects established/anchored/related to Sources and priority? | `methodology/project-lifecycle.md` |
| How are Source/File identity, provenance, preservation and access handled? | `methodology/source-and-provenance.md` |
| What evidence/source-status semantics apply? | `methodology/evidence-policy.md` |
| How is diplomatic/source-phenomenon transcription handled? | `methodology/transcription-guidelines.md` |
| How are execution context, prerequisites, evidence staging and loops handled? | `methodology/workflow.md` |
| How are quality/falsification/review dimensions handled? | `methodology/quality-and-learning.md` |
| How are ownership, D-016 admission and propagation handled? | `methodology/maintenance.md` |
| How are GitHub Milestones interpreted? | `MILESTONES.md` |
| What stable machine-checkable Source/File/Project-use constraints apply? | `corpus/source-contract.json` + `tools/source_contract.py` |
| What is the current structured cross-disciplinary Requirement inventory used by outcome-context resolution? | `requirements/domain-requirements.tsv` |
| What is the accepted engineering baseline / active change / explicit current focus? | `engineering/configuration.json` |
| What is the bounded SD-KA-01 lifecycle/work-package state? | `engineering/changes/SD-KA-01/STATE.json` |
| What did completed SD-KA-01 work packages actually establish? | `engineering/changes/SD-KA-01/RESULT.md` |
| What managed engineering artifacts/findings/relations exist? | `engineering/catalog/` |
| What owns migrated-path compatibility and move evidence? | `engineering/catalog/legacy-paths.tsv` + `engineering/changes/SD-KA-01/MIGRATION.tsv` |
| What owns derived engineering context/profile behavior? | `engineering/context/README.md` |
| What owns bounded `.prompt` interaction behavior? | `engineering/prompts/CONTRACT.md` |
| What owns deterministic engineering-fitness mappings and PASS boundaries? | `engineering/assurance/fitness.json` + `tools/engineering_fitness.py` |
| What is a Source/File/relationship/crosswalk fact? | `corpus/` |
| Why/what is one Project and what is its current scope? | Project `project.yml` |
| How does the Project currently use Sources? | Project `source-uses.tsv` |
| Which concrete File supports a Project use? | Project `research/use-evidence.tsv` |
| What is the current Project restart/gate/evidence state? | Project `STATUS.md` |
| What did the Project actually read/decide/observe? | owning Project research files |

The engineering configuration/catalog/change owners are implemented for the admitted SD-KA-01 scope. Their accepted-baseline/currentness semantics are canonical where explicitly owned; `tools/engineering.py current`, `tools/engineering_context.py` and other generated/query views remain rebuildable navigation/restart aids, never parallel truth stores. ADR-0001/P-001–P-012 remain the admitted target package and are not thereby promoted to accepted architecture baseline.

## Current Project directories

The repository currently contains:

- `projects/ega-reg-ii-3/`;
- `projects/ega-reg-ii-4-bd-ii/`;
- `projects/ega-reg-ii-5-knau/`.

The last path is a legacy directory/id retained for continuity. Its current Project meaning, scope and priority are defined only by its canonical Project files, not by the `knau` slug.

Do not copy current Project scope/gate/`NEXT ACTION` into this README. Read the Project owner directly or use the rebuildable Project-context view.

## Canonical-versus-derived rule

One durable fact/state has one canonical owner. Human-facing summaries, generated context, GitHub Issues/Milestones and chat may point to that state but must not become parallel truth stores.

When stable structure can be resolved deterministically, use the executable resolver/validator instead of asking AI to infer it repeatedly.

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
templates/
corpus/
entities/
projects/
tools/
tests/
```

Optional Project work directories exist only when real work requires them. `engineering/` carries the admitted SD-KA-01 configuration/catalog/change foundation plus the verified WP2 current/query, WP3 context/prompt/bootstrap and WP4 engineering-fitness/assurance capabilities; WP5 is the current bounded migration and WP6 remains later terminal qualification.

## Restartability acceptance

Another capable researcher/agent, given repository + authorized evidence and no old chat, should be able to determine:

- repository purpose/authority boundaries;
- Project purpose/scope and documentary anchor;
- canonical Source/File identity and structural relationships;
- Project-relative Source use and concrete evidence bindings;
- actual Project research/gate/evidence state;
- whether required evidence is merely identifiable/reproducible or actually ready for the target task;
- whether an authorized `NEXT ACTION` exists;
- which outputs are canonical versus derived;
- which GitHub items are only planning/review metadata;
- for current system-development work, accepted engineering baselines, active admitted change state, semantically explicit current/scoped work with provenance, applicable context, completed work-package results, migration compatibility and the next permitted bounded transition.

If continuation requires stale orientation prose, duplicated state, inferred priority or recovery of the old chat, the repository has drifted and the owning surface must be repaired.
