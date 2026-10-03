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

### Research-system programme navigation

The former research-system programme owned by **#206** is historical and terminal at its explicit 2026-09-17 `STOP`; its final disposition remains in `requirements/research-system-programme-completion-review-2026-09-17.md`. That terminal state did not itself create a successor programme.

The later, separately Human-Owner-selected system programme **#225** is now **CLOSED as GitHub work metadata** (2026-10-02). It owned the bounded end-to-end operationalization problem `Human need / desired scholarly outcome → authorized scope/state → applicable unmet requirements → responsibility/work composition → real scholarly execution → usable result or legitimate ceiling → persist/restart`. It did **not** create manuscript Project scope or scholarly `NEXT ACTION`.

Under #225, Phase 0/1 and Phase 2 completed; **C1R — Derived Outcome Control Context with bounded resolution** was explicitly admitted under D-016 and implemented as the read-only/rebuildable `tools/outcome_context.py`. The C1R implementation/result review is a **LOCAL PASS ONLY**. The current #225 issue body still carries its earlier `ACTIVE` wording and its T11 contract says programme closure requires full vertical-result/ceiling, restart, bounded-repair and materially-different-fixture evidence. The inspected current issue/comment evidence contains no terminal T11 record establishing those conditions as satisfied or re-dispositioned, so this README does **not** infer whole-system scholarly acceptance or failure from the GitHub closure alone. `requirements/product-co-development-boundary-deep-check-2026-10-03.md` records that evidence boundary and the navigation drift.

Issue **#230** is now **CLOSED / COMPLETED** as the bounded Human-Owner-requested audit owner for adequacy-first architecture, repository knowledge/work lifecycle, current-vs-historical separation, decision promotion and work-owner closability. Its causal audit is persisted in `requirements/repository-knowledge-lifecycle-adequacy-audit-2026-10-02.md`, and the follow-on target-state / implementation-readiness analysis is persisted in `requirements/repository-target-state-implementation-readiness-2026-10-03.md`.

Closing #230 did **not** admit implementation. The original D-016 surface, target-state analysis, Human-proxy/context audit and the bounded 2026-10-03 D-016 refinement remain valuable historical analysis/concept/design evidence. However, the subsequent meta-audit `requirements/human-decision-readiness-design-process-rebaseline-audit-2026-10-03.md` found that analysis, Requirements, concept and partial design had become too interleaved, targeted research remained incomplete, and the Human decision surface was not sufficiently understandable in practice. The current lifecycle-revision state is therefore **NOT READY FOR D-016 DECISION**. Class B, IC-01/02/03/06, `decision-needed`, B0/B1, bounded context and result/return constructs remain solution hypotheses for later comparison rather than a preselected implementation architecture. Re-baselining must proceed through problem/root-cause analysis → requirements → only necessary targeted research → competing concepts → design before another material admission request. No manuscript scope or scholarly `NEXT ACTION` follows from this system work.

The product/co-development deep check remains relevant to that future work: scholarly product primacy, current research as first real fixtures rather than system limits, Genericity ≠ Distribution, Wirknetz as a property/trace lens rather than a selected component, and an internal-coupling threshold for any future package/`src` move. `requirements/human-proxy-work-lifecycle-context-efficiency-audit-2026-10-03.md` and `requirements/repository-knowledge-lifecycle-d016-refinement-2026-10-03.md` are retained as prior evidence/hypotheses and must be read through the current re-baseline rather than as a present `ADMIT | REFINE | DEFER | REJECT` demand.

Historical programme detail must remain distinguishable from current programme state. Do not infer current priority from the newest Issue, a local D-016/CI `PASS`, Issue closure by itself, or old chat; resolve the explicit programme/Project owner and its current disposition.

The bounded P3A whole-map synthesis under **#207 is COMPLETE**. Its decision-ready result is persisted in `requirements/research-system-programme-synthesis-2026-09-15.md`.

**Route A is COMPLETE and RESOLVED at the current evidence state.** Its P2 Requirements resolution (#200), bounded P3B Concept (#211), explicitly admitted two-file METHOD implementation and Result Review (#212) are complete. `methodology/maintenance.md` now owns the narrow programme/phase/result-transition reconciliation semantics and `methodology/workflow.md` contains only the referential execution hook. The terminal review is persisted in `requirements/research-system-programme-continuity-result-review-2026-09-16.md`.

**Route B / #90 is explicitly DEFERRED at the GitHub Free/private-repository platform boundary by Human-Owner decision.** Analysis, Requirements, Concept and B-ADMIT remain valid history, but the native protection was not implemented. The known risk remains explicit: PR-only promotion, required `validate`, admin/direct-promotion prevention and force-push/delete protection are not technically enforced. `requirements/default-branch-promotion-enforcement-owner-disposition-2026-09-17.md` records the defer/risk disposition. This satisfies the P3A PC7 completion path by explicit Human-Owner re-disposition rather than by claiming enforcement.

The older #206 programme-level `STOP` above remains correct for that historical owner. It must not be generalized into a claim that no later separately authorized research-system programme can exist.

A local `STOP` closes only the bounded arc whose owner establishes that boundary. Programme completion/closure belongs to the applicable programme owner and does not generate a successor priority by itself.

## Cross-project analytical audit evidence

`requirements/` also contains non-normative audit/review evidence. Current orientation includes:

- `requirements/human-decision-readiness-design-process-rebaseline-audit-2026-10-03.md`;
- `requirements/repository-knowledge-lifecycle-d016-refinement-2026-10-03.md`;
- `requirements/human-proxy-work-lifecycle-context-efficiency-audit-2026-10-03.md`;
- `requirements/product-co-development-boundary-deep-check-2026-10-03.md`;
- `requirements/product-co-development-boundary-analysis-delta-2026-10-03.md`;
- `requirements/repository-target-state-implementation-readiness-2026-10-03.md`;
- `requirements/repository-knowledge-lifecycle-adequacy-audit-2026-10-02.md`;
- `requirements/repository-knowledge-lifecycle-d016-decision-surface-2026-10-02.md`;
- `requirements/research-framing-transdisciplinary-competency-audit-2026-09-14.md`;
- `requirements/research-system-problem-landscape-2026-09-14.md`;
- `requirements/research-system-programme-continuity-audit-2026-09-16.md`;
- `requirements/research-system-programme-continuity-requirements-resolution-2026-09-16.md`;
- `requirements/research-system-programme-continuity-concept-2026-09-16.md`;
- `requirements/research-system-programme-continuity-result-review-2026-09-16.md`;
- `requirements/default-branch-promotion-enforcement-requirements-resolution-2026-09-16.md`;
- `requirements/default-branch-promotion-enforcement-concept-2026-09-16.md`;
- `requirements/default-branch-promotion-enforcement-owner-admission-2026-09-17.md`;
- `requirements/default-branch-promotion-enforcement-owner-disposition-2026-09-17.md`;
- `requirements/research-system-programme-synthesis-2026-09-15.md`;
- `requirements/research-system-programme-completion-review-2026-09-17.md`;
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
- for research-system programme work, whether the applicable programme is active or terminal and which explicit owner disposition established that state.

If continuation requires stale orientation prose, duplicated state, inferred priority or recovery of the old chat, the repository has drifted and the owning surface must be repaired.