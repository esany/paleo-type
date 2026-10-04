# Bugwave design closure — brownfield classification, target information architecture and migration — 2026-10-04

**Status:** NON-NORMATIVE DETAILED DESIGN / **#251 DESIGN COMPLETE / PHYSICAL MIGRATION NOT ADMITTED**  
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Work owner:** #251; parent #244  
**Depends on:** #245 finding coverage; #246 identity/configuration; #247 context/DevEx; #248 ADR inventory  
**This file is not:** a migration execution record, Current Configuration, D-016 admission, or permission to bulk-move files.

## 1. Brownfield conclusion

The current `requirements/` directory is not one information class. It contains a structured Requirement baseline alongside audits, research, concepts/designs, admissions/dispositions, results, learnings, prompts/work instructions, programme syntheses and coordination material.

The migration problem is therefore semantic before physical:

> **classify responsibility/currentness/authority first; establish stable identity and transition semantics; only then move files.**

A cleaner tree with the same implicit semantics would not solve the bugwave.

## 2. Current information classes

The full major audit/research/learning chain has already been coverage-checked in `system-development-bugwave-finding-coverage-2026-10-04.md`. For physical-IA purposes the current `requirements/` brownfield resolves into these classes.

| Semantic class | Representative current artifacts | Authority / lifecycle meaning | Target responsibility |
|---|---|---|---|
| accepted Requirement baseline | `domain-requirements.tsv` | structured current Requirement inventory for its owned domain | remain under narrowed `requirements/` or other explicitly accepted Requirement owner |
| requirements resolution | `*-requirements-resolution-*` | bounded historical/current evidence depending on its own status; not automatically global Requirements | accepted reusable requirements may promote into Requirement baseline; source resolution retained as evidence |
| problem frame / reconstruction | `human-need-to-scholarly-outcome-problem-frame-*`, `human-need-maturity-progress-reconstruction-*` | analysis evidence | engineering evidence / relevant change workspace |
| audit / adequacy review | `*-audit-*`, `*-self-review-*`, `*-deep-check-*` | non-normative evidence unless explicitly promoted | engineering evidence/audits; default-context off after disposition |
| research / comparator findings | `shared-fixture-research-findings-*`, `cross-source-research-findings-*`, `pre-synthesis-*`, `final-multi-question-generation-research-*` | research evidence, often historical programme evidence | engineering evidence/research or Project research owner where Project-specific |
| concept / competing approaches | `*-concept-*`, `*-concept-comparison-*`, `executable-*-concept-idea-*` | proposed/rejected/selected design evidence according to explicit status | bounded change concepts/design or historical engineering evidence |
| detailed architecture/design | `system-development-*-design-*`, target-state design artifacts | proposed/superseded design evidence until accepted | engineering architecture/change design; accepted baseline selected explicitly |
| accepted decision rationale | current `DECISIONS.md` references and admitted owner records | accepted authority only where owner says so | `DECISIONS.md` remains accepted cross-project decision owner; ADR layer adds rationale, not duplicate authority |
| owner admission / disposition | `*-owner-admission-*`, `*-owner-disposition-*` | durable Human material authority for bounded scope | bounded change/decision evidence; linked from configuration transition |
| programme/current-work synthesis | programme synthesis/completion/continuity artifacts | work/programme evidence; may be terminal/history | change/result/history; not default current configuration |
| result review | `*-result-review-*` | actual bounded result/assurance/return evidence | change `RESULT.md` or engineering evidence/result |
| learning | `*-learning-*`, claim-repair result/learning artifacts | failure/learning evidence; may confirm existing practice | engineering evidence/learning + promoted finding/decision/test consequence |
| work instruction / prompt | `*-prompt-*`, execution/work prompt artifacts | executable/historical instruction, not Requirement/Decision/Current State | engineering work-instructions/prompts; reusable capability only if separately admitted |
| coordination/bootstrap | `chatgpt-*-coordination-*`, coordination audits | transport/process evidence, mostly historical/deferred | engineering evidence/coordination history, default-context off |
| capability/role/handoff analysis | `ai-role-handoff-*`, phase ownership maps | analysis/design evidence | relevant change/evidence; promoted consequences indexed separately |
| managed finding/ADR/current-view artifacts from current bugwave | bugwave master/coverage/ADR/prompt candidate | current non-normative pre-admission engineering evidence | migrate into target engineering plane when admitted; do not pretend historical path was intended final home |
| ambiguous legacy | any file whose header/owner cannot establish one class confidently | unknown until inspected | retain in place/catalog as `ambiguous` until resolved; never move by filename guess |

The important classification is by **actual header/owner/status**, not by filename. Filename patterns above are navigation examples, not the classification algorithm.

## 3. Representation trade study

### Option A — central catalog only

All artifact identity/kind/authority/lifecycle/path metadata lives in a central table. Content remains in existing files.

**Strengths:** one queryable owner; works across Markdown/TSV/JSON/external evidence; path moves are explicit.  
**Risk:** manual catalog can become stale; direct file does not show all metadata.  
**Mitigation:** deterministic validation/freshness; generated views.

### Option B — local front matter/metadata only

Every file owns its own ID/kind/lifecycle/currentness metadata.

**Strengths:** locality; file travels with metadata.  
**Risks:** heterogeneous formats (`.tsv`, JSON, external Issues), mass brownfield rewrites, duplicated cross-cutting currentness queries, harder global conflict validation; local status can conflict with configuration authority.

**Disposition:** not selected as the primary representation.

### Option C — hybrid: central semantic registries + content in natural owners + local stable anchors only where needed

Central repository-native registries own cross-artifact metadata and material finding/relation lifecycle. Original content remains in the file/owner appropriate to its semantic class. Files need no duplicate lifecycle front matter merely to satisfy the catalog. Material sub-document evidence can carry a stable anchor marker where durable deep trace is required.

**Disposition: SELECTED for initial implementation.**

Why:

- query/currentness needs are cross-cutting;
- legacy formats are heterogeneous;
- finding disposition is a new promoted consequence, not a copy of source prose;
- relation trace is cross-artifact by nature;
- stable path-independent identity can be centralized without moving content first;
- deterministic validation can prevent a stale catalog;
- it avoids rewriting every historical Markdown file just to introduce metadata.

This is a representation selection, not acceptance/admission. D-016 still governs implementation.

## 4. Selected logical target information architecture

The holistic target is refined to:

```text
GOVERNING_OBJECTIVE.md
AGENTS.md
README.md
DECISIONS.md
MILESTONES.md

requirements/
  README.md
  domain-requirements.tsv
  ... other accepted reusable Requirement baselines only

methodology/
corpus/
entities/
projects/

engineering/
  README.md
  configuration.json
  context-profiles.json

  architecture/
    SYSTEM.md

  decisions/
    README.md
    ADR-....md

  catalog/
    artifacts.tsv
    findings.tsv
    relations.tsv
    legacy-paths.tsv

  changes/
    <change-id>/
      STATE.json
      PROBLEM.md        # when needed
      REQUIREMENTS.md   # when needed
      RESEARCH.md       # optional
      CONCEPTS.md       # optional
      DESIGN.md         # when material design exists
      PLAN.md           # bounded implementation/migration plan
      RESULT.md         # terminal result/return when work completes

  evidence/
    audits/
    research/
    learning/
    work-instructions/
    coordination/       # only if retained evidence warrants a distinct class

  prompts/              # only reusable prompt assets/capability material if #252 earns activation

  generated/
    CURRENT_STATE.json
    CURRENT_STATE.md    # only if exact regeneration/freshness is enforced
    CATALOG.md          # same condition

tools/
tests/
.github/
```

### 4.1 ADR location

Architecture ADRs belong under `engineering/decisions/` because they are engineering rationale, not a replacement for top-level accepted `DECISIONS.md`.

- accepted `D-*` remains the governing cross-project decision owner;
- retrospective ADR may point to a `D-*` and explicitly say it records rather than caused the historical decision;
- proposed ADRs remain proposals until accepted by the applicable authority;
- configuration references accepted ADRs/baselines but ADR files do not own currentness.

### 4.2 Prompts

Prompt is a distinct information class:

```text
Prompt != Requirement != Plan != METHOD != Current State != Decision
```

Historical one-off prompts/work instructions migrate to `engineering/evidence/work-instructions/` and leave default context after their consequence is integrated.

Reusable prompt capability/assets go under `engineering/prompts/` only if #252 earns operational activation. Do not create a top-level generic `skills/` framework merely because Wissensarbeit has one.

## 5. Canonical metadata ownership in the selected hybrid

### `artifacts.tsv`

Canonical owner for managed engineering artifact identity and cross-cutting metadata such as:

```text
artifact_id
kind
current_path
owner_scope
authority_role
lifecycle_state
change_id
title
```

The table describes the asset; it does not copy its content.

### `findings.tsv`

Canonical owner for the current **disposition** of material findings extracted from source evidence:

```text
finding_id
source_ref
summary
materiality
disposition
target_ref
rationale
```

The source audit remains the detailed evidence owner. The finding row owns the promoted lifecycle consequence.

### `relations.tsv`

Canonical owner for a small set of explicit material cross-artifact relations:

```text
relation_id
subject_ref
predicate
object_ref
relation_status
evidence_ref
```

No graph completeness target.

### `legacy-paths.tsv`

Migration compatibility/navigation only:

```text
legacy_path
artifact_id
current_path
migration_commit
```

It should be removable/reducible when no active consumer requires legacy-path lookup, while Git continues to preserve history.

## 6. Representative migration dry runs

### A. accepted Requirement set — `domain-requirements.tsv`

- stays under `requirements/`;
- receives/uses a managed artifact identity in catalog without rewriting Requirement rows solely for EKCP;
- configuration may reference it as an accepted Requirements baseline where applicable;
- no migration merely for visual consistency.

### B. large audit — knowledge-lifecycle / holistic / bugwave audits

- content moves to `engineering/evidence/audits/` after the catalog/legacy mapping exists;
- material Findings already promoted into `findings.tsv` retain source refs to stable artifact/anchor identity;
- audit becomes historical/non-default after dispositions are integrated;
- generated current view points to consequences, not the full audit.

### C. research/comparator artifact

- moves to `engineering/evidence/research/` if cross-system engineering research;
- Project-specific scholarship remains with its Project, not pulled into engineering merely because it informed a design;
- relation/trace points across owner boundaries without copying content.

### D. superseded design

- moves to relevant change/history/evidence location;
- `lifecycle_state=superseded` and explicit `supersedes` relation identifies replacement;
- excluded from current architecture context by default.

### E. Human D-016 admission

- preserved as material decision/admission evidence under bounded change/decision evidence;
- configuration transition references it;
- Issue/PR state cannot substitute for it.

### F. Result Review

- moves/normalizes to change `RESULT.md` when it is the terminal result of that change;
- Result reconciles actual/current consequence and whole-system return;
- historical result remains immutable evidence after closure except corrective append/superseding record under existing rules.

### G. learning

- moves to `engineering/evidence/learning/`;
- current consequence is promoted to finding/decision/test/method as applicable;
- `persisted learning` alone is not represented as `enforced`.

### H. prompt/work instruction

- historical one-off prompt → evidence/work-instructions;
- reusable candidate `.prompt` contract → prompt capability area only if admitted/activated;
- completed prompt never becomes an open task merely because the file exists.

### I. ambiguous artifact

- remains in place with catalog kind/lifecycle `ambiguous` or equivalent;
- no move until header/authority is inspected;
- ambiguity is visible in migration validation rather than guessed from name.

### J. finding with several consequences

- one finding row may have multiple explicit relation rows/targets when evidence supports them;
- do not force one `target_ref` to encode all semantics if multiple consequences are genuinely material;
- relation status/evidence controls prevent a speculative dense graph.

## 7. Migration programme

### M0 — in-place identification/classification

- assign stable IDs to managed current/legacy engineering artifacts;
- populate artifact class/authority/lifecycle with explicit `ambiguous` where unresolved;
- create no physical moves;
- validate duplicate IDs/missing paths.

### M1 — finding/decision/current-config baseline

- import current material finding coverage F01–F45 and any source-audit coverage records required to prove completeness;
- encode accepted vs proposed ADR/decision relations;
- establish current engineering configuration from explicit accepted owners, not latest files;
- prove generated current view from this in-place brownfield state.

### M2 — bounded physical migration

- use `git mv` for classified files by semantic class;
- update catalog current paths and `legacy-paths.tsv` in the same bounded change;
- repair managed repository links/references;
- preserve Git history and deep material anchors;
- do not add duplicate compatibility copies unless a real consumer requires them.

### M3 — developer/context adoption

- introduce `engineering/README.md`, architecture/ADR navigation, context/query commands and one local assurance entrypoint;
- replace README programme-history burden with stable navigation after the generated current view is trustworthy.

### M4 — cleanup / deactivation

- historical evidence remains retrievable but leaves default current contexts;
- reduce temporary migration mappings only when tests show no supported consumer needs them;
- do not delete provenance to make the tree look clean.

## 8. Migration acceptance/loss checks

A migration slice fails if any of these occur:

- stable finding/decision/evidence reference no longer resolves;
- accepted/current meaning changes merely because a file moved;
- historical audit disappears before material findings are dispositioned;
- Human/reviewer discoverability becomes worse even though bytes are preserved;
- a useful review/cognitive function is removed without replacement/explicit disposition (F45);
- old path is still required but no compatibility lookup exists;
- Project-specific scholarship is sucked into system-engineering ownership;
- duplicated copies become parallel truth;
- default context grows because the new structure mechanically loads all evidence;
- rollback cannot restore pre-migration paths/state.

## 9. Rollback

Each physical migration work package is a Git-bounded change. Rollback means reverting that migration commit/PR and its catalog/path-reference changes together.

Do not attempt partial manual rollback that leaves catalog/current paths inconsistent with the tree.

## 10. Senior Developer verdict after target migration

A fresh developer should be able to determine, without chronology replay:

- current accepted architecture/configuration;
- active/proposed material changes;
- accepted/proposed ADRs;
- Requirements relevant to the change;
- where evidence/history lives;
- how to run the full local check;
- how a new artifact/finding/result is classified;
- which directory may be ignored for the current task.

This is the acceptance target for physical IA, not visual neatness.

## 11. Readiness disposition

**#251 design is complete.**

The semantic representation is selected as a repository-native hybrid with central cross-artifact registries and natural content owners; the physical target tree, prompt/ADR placement, migration stages, continuity strategy and loss/rollback checks are specified.

Physical creation/migration remains D-016-gated. The implementer should not need to choose between central/local/hybrid metadata or invent the migration order during coding.