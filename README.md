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

The Human-visible current system-development work/decision view is GitHub **#244**. Pre-implementation analysis/design Issues **#245–#253 are complete**. SD-KA-01 implementation is decomposed as **#256–#261**; after the recorded D-016 admission, #256/WP1 is the active bounded implementation cursor and later Issues remain ordered by the admitted dependencies.

The current material decision surface is:

`requirements/system-development-bugwave-d016-decision-brief-2026-10-04.md`

The D-016 admission is durably recorded in:

`requirements/system-development-bugwave-d016-owner-admission-2026-10-04.md`

Current process state:

> **D-016 ADMITTED / SD-KA-01 IMPLEMENTATION IN PROGRESS / WP1 ACTIVE.**

The compact failure-family/bugwave map remains `requirements/system-development-bugwave-master-map-2026-10-04.md`; its pre-closure readiness wording is historical evidence where it differs from the later D-016 brief. **The D-016 brief and #244 own the current non-normative readiness/navigation interpretation.**

The proposed target is still a repository-native Engineering Knowledge & Configuration Plane plus risk-tailored Development Readiness semantics. Detailed design now covers material-finding promotion, engineering configuration/reference transitions, context/Developer Experience, Architecture Decision Records (ADRs), activity-relative readiness/Human decision surfaces, engineering assurance, brownfield migration, `.prompt` capability and the Review Premise Inheritance safeguard.

The admitted first implementation is #256: establish semantic contracts and an in-place managed brownfield baseline. Physical migration is deliberately later (#260), after semantics/currentness/trace/fitness are working.

The admission permits only the bounded SD-KA-01 target and WP1–WP6 scope. No manuscript scope or scholarly `NEXT ACTION` follows from it; the target `engineering/` structure, physical migration, METHOD change, schema/runtime and Context Compiler remain bounded implementation work, not already-accepted current configuration.

### Historical programme boundaries

- **#225** is CLOSED as GitHub work metadata. C1R (`tools/outcome_context.py`) is a bounded local PASS; repository evidence does **not** establish whole-system scholarly T11 acceptance merely from Issue closure. F17 preserves this residual explicitly.
- **#230** is CLOSED / COMPLETED as the bounded audit owner that led into the current knowledge/configuration work. Closing it did not admit implementation.
- The former **#206** programme remains historical/terminal at its explicit 2026-09-17 `STOP`; later separately authorized system-development work does not rewrite that history.
- **Route A** programme-continuity work is complete/resolved under its existing owners.
- **Route B / #90** remains explicitly DEFERRED under its Human-Owner disposition. The current bugwave does not reactivate branch-protection implementation.

Historical programme detail is evidence on demand, not the default current-work surface. Do not infer priority from the newest Issue, local CI `PASS`, Issue closure, filename date or old chat; resolve the applicable owner and current disposition.

## System-development evidence / deeper provenance

`requirements/` is currently a brownfield mixed-purpose namespace. That is a documented information-architecture defect and not the intended target state. Until a separately admitted migration occurs, use these current navigation artifacts rather than replaying files chronologically:

- current Human decision surface: `requirements/system-development-bugwave-d016-decision-brief-2026-10-04.md`;
- whole bugwave/failure-family map: `requirements/system-development-bugwave-master-map-2026-10-04.md`;
- source-audit finding coverage: `requirements/system-development-bugwave-finding-coverage-2026-10-04.md`;
- finding promotion design: `requirements/system-development-bugwave-finding-promotion-design-2026-10-04.md`;
- architecture-decision inventory: `requirements/system-development-bugwave-adr-inventory-2026-10-04.md`;
- ADR surface design: `requirements/system-development-bugwave-adr-surface-design-2026-10-04.md`;
- configuration/reference design: `requirements/system-development-bugwave-configuration-reference-design-2026-10-04.md`;
- context/developer design: `requirements/system-development-bugwave-context-developer-design-2026-10-04.md`;
- readiness/Human decision contract: `requirements/system-development-bugwave-readiness-human-decision-contract-2026-10-04.md`;
- engineering assurance design: `requirements/system-development-bugwave-assurance-closure-design-2026-10-04.md`;
- brownfield migration design: `requirements/system-development-bugwave-brownfield-migration-design-2026-10-04.md`;
- `.prompt` transfer candidate/result: `requirements/prompt-skill-transfer-candidate-2026-10-04.md` and `requirements/prompt-skill-transfer-test-result-2026-10-04.md`;
- Review Premise Inheritance disposition: `requirements/review-premise-inheritance-generic-fit-2026-10-04.md`;
- underlying holistic architecture: `requirements/system-development-holistic-knowledge-architecture-dev-ready-design-2026-10-04.md`;
- anti-regression baseline: `requirements/system-development-pre-implementation-anti-regression-baseline-2026-10-04.md`.

The finding-coverage artifact links/dispositions the deeper September–October audit/research/learning chain. Load those source artifacts when reviewing the finding or its provenance, not as mandatory default context.

Use every artifact according to its stated evidence/authority status. None creates Project priority or implementation authority merely by existing.

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
| What is a Source/File/relationship/crosswalk fact? | `corpus/` |
| Why/what is one Project and what is its current scope? | Project `project.yml` |
| How does the Project currently use Sources? | Project `source-uses.tsv` |
| Which concrete File supports a Project use? | Project `research/use-evidence.tsv` |
| What is the current Project restart/gate/evidence state? | Project `STATUS.md` |
| What did the Project actually read/decide/observe? | owning Project research files |

The proposed engineering configuration/ADR/catalog owners above are **not canonical yet**; they become operative only after explicit D-016 admission, implementation and accepted Result Review. Generated views such as `tools/project_context.py` are rebuildable navigation/restart aids, never canonical truth.

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
templates/
corpus/
entities/
projects/
tools/
tests/
```

Optional Project work directories exist only when real work requires them. The proposed `engineering/` target is designed but **not implemented or current** until a separate D-016 admission, implementation and Result Review establish it.

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
- for current system-development work, which material decision is actually pending and which repository artifact/Issue owns that decision surface.

If continuation requires stale orientation prose, duplicated state, inferred priority or recovery of the old chat, the repository has drifted and the owning surface must be repaired.
