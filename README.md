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

Durable scholarly state for a purpose-established investigation: Project purpose/scope, documentary Source anchor, Project→Source research use, evidence bindings, transcription/analysis/decisions and restart state.

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

### Research-system programme navigation

For cross-project research-system programme work, use GitHub Issue **#206** as the current programme/process navigation owner. It owns the programme-stage/cursor map; do not reconstruct programme priority from the newest closed Issue, a local D-016 `PASS`, or old chat.

The bounded P3A whole-map synthesis under **#207 is COMPLETE**. Its decision-ready result is persisted in `requirements/research-system-programme-synthesis-2026-09-15.md`.

**Route A is COMPLETE and RESOLVED at the current evidence state.** Its P2 Requirements resolution (#200), bounded P3B Concept (#211), explicitly admitted two-file METHOD implementation and Result Review (#212) are complete. `methodology/maintenance.md` now owns the narrow programme/phase/result-transition reconciliation semantics and `methodology/workflow.md` contains only the referential execution hook. The terminal review is persisted in `requirements/research-system-programme-continuity-result-review-2026-09-16.md`.

The current programme cursor is again **#206**, now for separate Route-B / #90 disposition and subsequent programme-completion review. No further Route-A work is current. Route B remains independent and is not active until explicitly selected; if selected, its first stage is only the fresh technical audit defined by #206/#90, not immediate configuration.

A local `STOP` closes only the bounded arc whose owner establishes that boundary. It does not by itself establish completion of the overall research-system programme. The programme-continuity evidence is persisted in `requirements/research-system-programme-continuity-audit-2026-09-16.md`.

## Cross-project analytical audit evidence

`requirements/` also contains non-normative audit/review evidence. Current orientation includes:

- `requirements/research-framing-transdisciplinary-competency-audit-2026-09-14.md`;
- `requirements/research-system-problem-landscape-2026-09-14.md`;
- `requirements/research-system-programme-continuity-audit-2026-09-16.md`;
- `requirements/research-system-programme-continuity-requirements-resolution-2026-09-16.md`;
- `requirements/research-system-programme-continuity-concept-2026-09-16.md`;
- `requirements/research-system-programme-continuity-result-review-2026-09-16.md`;
- `requirements/research-system-programme-synthesis-2026-09-15.md`;
- `requirements/post-research-problem-landscape-reconciliation-2026-09-14.md`;
- `requirements/pre-synthesis-research-program-2026-09-14.md`;
- `requirements/shared-fixture-research-findings-2026-09-14.md`;
- `requirements/cross-source-research-findings-2026-09-14.md`;
- `requirements/pre-synthesis-research-integration-2026-09-14.md`;
- `requirements/final-multi-question-generation-research-2026-09-14.md`;
- `requirements/post-research-synthesis-concept-approaches-2026-09-14.md`;
- `requirements/post-research-capability-requirement-synthesis-2026-09-14.md`;
- `requirements/executable-transdisciplinary-research-system-concept-idea-2026-09-14.md`;
- `projects/ega-reg-ii-5-knau/research/post-166-research-framing-review-2026-09-14.md`.

Use each according to its stated evidence/authority status. None creates Project priority or implementation authority by itself.

## Where truth lives

| Question | Canonical owner |
|---|---|
| Why does the repository exist / what has precedence? | `GOVERNING_OBJECTIVE.md` |
| What stable AI/research guardrails always apply? | `AGENTS.md` |
| What cross-project rationale/decision history matters? | `DECISIONS.md` |
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
| What is a Source/File/relationship/crosswalk fact? | `corpus/` |
| Why/what is one Project and what is its current scope? | Project `project.yml` |
| How does the Project currently use Sources? | Project `source-uses.tsv` |
| Which concrete File supports a Project use? | Project `research/use-evidence.tsv` |
| What is the current Project restart/gate/evidence state? | Project `STATUS.md` |
| What did the Project actually read/decide/observe? | owning Project research files |

Generated views such as `tools/project_context.py` are rebuildable navigation/restart aids, never canonical truth.

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
templates/
corpus/
entities/
projects/
tools/
tests/
```

Optional Project work directories exist only when real work requires them.

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
- for research-system programme work, which programme/process owner carries the current cursor and why a local arc terminal state does or does not affect programme completion.

If continuation requires stale orientation prose, duplicated state, inferred priority or recovery of the old chat, the repository has drifted and the owning surface must be repaired.