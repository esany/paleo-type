# Bugwave design closure — bounded context, Human overview and developer bootstrap — 2026-10-04

**Status:** NON-NORMATIVE DETAILED DESIGN / **#247 DESIGN COMPLETE / CONTEXT-COMPILER IMPLEMENTATION NOT ADMITTED**  
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Work owner:** #247; parent #244  
**Depends on:** #246 configuration/reference semantics; #245 finding coverage  
**This file is not:** a generated Current State, a canonical work owner, a mega-prompt, a new Human approval layer, or implementation permission.

## 1. Design objective

A fresh Human, Senior Developer or AI execution context must not need audit chronology to reconstruct current engineering meaning. At the same time, context reduction must not delete authority, uncertainty or provenance.

The target property is:

> **bounded default context + explicit applicability provenance + expandable evidence/history.**

Human strategic understanding and Agent task execution are different views over the same owners. They must not be forced into one document or one token budget.

## 2. Three-layer context model

### Layer A — mandatory orientation/authority

Small, stable and rarely changing:

- repository purpose/precedence;
- AI/Human/specialist authority boundaries;
- canonical-vs-derived rule;
- current engineering configuration owner reference;
- assurance-boundary rule.

For repository-capable agents this normally means pointers to freshly read owners (`GOVERNING_OBJECTIVE.md`, `AGENTS.md`, applicable METHOD/Requirements), not pasted copies of all prose.

### Layer B — role/task current context

Compiled for the current role and activity:

- accepted engineering baseline relevant to the task;
- active/admitted/proposed change relevant to the task, or explicit absence;
- bounded Issue/work owner;
- activity-relative readiness;
- applicable Requirements;
- accepted ADRs/decisions and materially relevant proposed ADRs;
- blockers/uncertainties;
- evidence inputs required now;
- exact write/authority boundary;
- acceptance/verification/validation/whole-return contract.

### Layer C — expandable provenance/history

Loaded only on demand or when the task requires it:

- source audits/findings;
- rejected alternatives;
- superseded designs;
- deep rationale;
- Issue/PR/Git chronology;
- historical prompts/work instructions;
- comparator evidence.

A Layer-C item may become Layer B for a review task. `history` is therefore not globally low-value; it is simply not default current context.

## 3. Applicability provenance

Every item placed into a compiled context must expose **why it is applicable**. The context compiler may not become an opaque reading-list maintainer.

Minimum applicability-basis classes:

```text
formal-derived
owner-declared
work-contract
selected-with-basis
candidate/unresolved
```

Meaning:

- `formal-derived`: deterministic relation from canonical state/contract;
- `owner-declared`: an owning canonical artifact explicitly declares applicability;
- `work-contract`: bounded Issue/change/admission explicitly requires it;
- `selected-with-basis`: judgement was needed; record selector, source/basis and scope;
- `candidate/unresolved`: possibly applicable but not settled; expose rather than silently omit or treat as binding.

Do not invent a claim that all scholarly/engineering applicability can be deterministic.

### 3.1 Omission discipline

The system does not need an exhaustive list of every excluded repository artifact. It needs enough information to explain the inclusion boundary:

- role/profile;
- work/change scope;
- canonical owners queried;
- formal selection rules applied;
- any judgement-based additions;
- unresolved candidate applicability.

If a consumer asks `why was X absent?`, the query layer should be able to distinguish `out of scope by formal rule`, `not selected`, `unresolved`, and `unknown/not catalogued` where the data supports it.

## 4. Human strategic overview

The Human view is not the Agent packet with more prose. It answers strategic/current questions.

Minimum sections:

```text
WHY / demonstrated problem
CURRENT accepted engineering state
PROPOSED material changes
ACTIVE bounded work and next activity
WHAT IS READY NOW
WHAT NEEDS HUMAN DECISION
WHAT IS BLOCKED and by what
MATERIAL FINDINGS / residual risks
ACCEPTED decisions constraining the work
PROPOSED decisions still open
VERIFICATION / VALIDATION meaning
DEEPER EVIDENCE pointers
```

The Human view must not require:

- sorting Issues;
- reconstructing dependency order;
- replaying audit genealogy;
- choosing technical sequencing;
- manually routing work between agents;
- decoding unexplained internal status abbreviations.

It is derived/navigation only. The authoritative facts remain in their owning Requirements, decisions, configuration/change state and evidence.

## 5. Agent / Senior Developer execution packet

For one bounded work item, compile only what is required to execute and return it correctly.

Minimum logical packet:

```text
work_id / Issue
requested next activity
purpose / required effect
exact scope
non-goals
dependencies and their state
canonical authority/rule owners to read freshly
applicable Requirements + basis
accepted ADRs/decisions + basis
material proposed ADRs if the task is design/decision work
inputs/evidence + provenance
blocking uncertainty
write/authority boundary
acceptance criteria
technical verification
specialist/Human validation if any
whole-system return contract
on-demand evidence/history refs
```

A packet must never say merely `read the repo` or paste every prior audit.

## 6. Context profiles

The holistic design's profile idea survives with clearer products:

1. **scholarly-project** — existing Project-focused context; use existing mechanisms where applicable.
2. **system-development-execution** — bounded engineering work packet.
3. **architecture-review** — current baseline + proposal + Requirements + alternatives + findings/evidence needed to challenge it.
4. **human-system-overview** — strategic bugwave/current-work/decision view in plain language.
5. **human-material-decision** — only the information needed to understand one material decision and its consequences.
6. **maintenance-impact** — changed owner + dependents + propagation/loss checks.
7. **specialist-review** — claim/evidence/uncertainty/review basis, without pretending technical state is specialist judgement.

Profiles are query/selection policies over common owners, not separate manually maintained truth documents.

## 7. Senior Developer bootstrap

### 7.1 Target entry path

After the engineering plane exists, a new developer should normally need this path:

```text
README
→ engineering README / generated current engineering view
→ architecture baseline / accepted ADR index
→ active bounded Issue/change context
→ one local assurance command
→ deeper provenance only if needed
```

The developer should not have to choose the `latest` dated audit.

### 7.2 Interim current path before implementation

Until that target exists, the current bounded path is:

```text
README
→ bugwave master map + #244
→ relevant child Issue
→ applicable accepted decisions / proposed ADR inventory
→ issue-specific design/evidence artifact
→ existing CI command set
```

This is intentionally transitional and should shrink after the derived engineering current surface is implemented.

### 7.3 Current exact assurance commands

The current workflow proves the local commands already in use:

```bash
python tools/source_contract.py validate
python -m unittest discover -s tests -p 'test_*.py' -v
python tools/project_context.py --project ega-reg-ii-3
python tools/project_context.py --project ega-reg-ii-4-bd-ii
python tools/project_context.py --project ega-reg-ii-5-knau
```

The workflow also runs concrete resolver fixtures. A developer may mirror those when changing resolver semantics.

### 7.4 Target one-command developer contract

After engineering semantics are admitted/implemented, add one repository-local command (candidate `python tools/check.py`) that invokes:

- Source Contract validation;
- deterministic/governance regressions;
- engineering catalog/config/reference/finding checks;
- generated-view freshness checks;
- managed link/path/legacy-reference checks;
- any seeded engineering fitness fixtures.

CI should call the same entrypoint rather than maintain a divergent hidden test recipe.

The exact filename is implementation detail; **one documented local full-check entrypoint shared with CI** is the required property.

## 8. Reconstruction-cost baseline and acceptance measure

Do not optimize to an arbitrary token number. Measure work required for representative journeys.

For each fixture record:

```text
mandatory entry files
historical files required before action
manual semantic joins
ambiguous currentness choices
manually duplicated state statements encountered
approximate context bytes/tokens where useful
```

Required target direction:

- current-state/current-work discovery should require no history replay;
- default context size should remain roughly bounded as historical audit count grows;
- deeper provenance remains one/few explicit expansions away;
- no authority/uncertainty is omitted solely to reduce context.

## 9. Fresh-context acceptance fixtures

### FCTX-1 — system developer

Given repo + no chat, identify current accepted architecture, proposed architecture, active work, readiness and D-016 state without reading dated audits in chronological order.

### FCTX-2 — Human overview

Given the Human view, explain the bugwave, what is ready, what is not, what needs a material decision and why. No issue sorting/audit replay.

### FCTX-3 — architecture reviewer

From proposal/requirements/finding trace, challenge a design and expand to supporting evidence/rejected alternatives without loading unrelated Project history.

### FCTX-4 — context starvation

Remove a material authority/uncertainty/evidence item from the packet and require the test/reviewer to detect that the context is inadequate rather than praise compactness.

### FCTX-5 — history growth

Add many historical/superseded artifacts. The current execution packet must not grow unless they become applicable.

### FCTX-6 — applicability ambiguity

Where two plausible rule/evidence inclusions remain, context marks `candidate/unresolved` or records a judgement basis rather than silently selecting/omitting.

## 10. Anti-context-swamp rules

1. No profile may default-load every audit merely because it is related to system development.
2. Generated summaries cannot own state.
3. Historical provenance is never deleted just to improve context cost.
4. Human and Agent views must not be maintained independently by hand.
5. A prompt is not a substitute for context compilation.
6. `README` remains navigation, not a manually synchronized engineering status database.
7. Context selection cannot manufacture task priority or material authority.
8. Strong model capability is not an excuse to leave repository reconstruction implicit.

## 11. Readiness disposition

**#247 design is complete enough to specify the target context/query/developer surface and to support #249/#250/#251.**

Actual Context Compiler/current-view/check-command implementation remains D-016-gated. The material role split, applicability provenance, Human-vs-Agent views, developer path and context acceptance fixtures no longer need to be invented during coding.