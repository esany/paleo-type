# AI role, handoff and engineering analysis

Status: **analytical synthesis / planning evidence, not normative method and not a new truth owner**.

Primary work owners: #71 (generic role/handoff blueprint), #77 (model-independent work-context/handoff scaffold), #74 (Development/Implementation role), #79 (Dev/RSE/AI-systems competency and assurance refinement).

Canonical authority remains `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, applicable `REQ-*`, authoritative methodology and canonical corpus/project state. This file documents the current analysis so that its rationale does not remain only in chat. If any conclusion becomes a generic rule, it must be promoted through the existing owner/generalisation path rather than treated as normative merely because it appears here.

## 1. Question

What does the emerging role/ownership/handoff architecture imply for AI engineering and development in `paleo-type`, and what additional competencies, risks and deterministic controls are needed to make work less dependent on a particular model/session without falsely determinising scholarship?

## 2. Current repository direction

The repository is not converging on a multi-agent system. It is converging on a **replaceable work-context model**:

```text
canonical governing context + canonical project/source state
        ↓
explicit bounded role/function
        ↓
role-appropriate work
        ↓
explicit handoff at authority/competence boundary
        ↓
receiving role + review/return condition
        ↓
canonical persistence / project NEXT ACTION
```

The important property is not that every model produces the same answer. The important property is that a capable replacement model/session can determine:

- what role it is performing;
- which evidence/state applies;
- what it may and may not decide;
- when it must stop or hand off;
- where durable state belongs;
- how returned work is reviewed;
- what the next scholarly action is;

without recovering the old chat.

This follows the current #71/#77 principle:

> **Standardize the path, not the scholarly outcome.**

## 3. Three different dependencies that must remain distinct

### 3.1 Chat/state dependency

A chat must not be the sole owner of consequential state. The repository already addresses this strongly through D-006, `STATUS.md`, canonical Source/File/Project owners, decision records and restartability rules.

### 3.2 Model/process dependency

A new session can still fail even when all canonical facts exist if it reconstructs its role, required context, authority boundary or handoff differently. #71/#77 address this by deriving a small procedural contract rather than a master prompt.

### 3.3 Scholarly judgement variability

This must not be eliminated by software. Manuscript reading, hand attribution, interpretation, historical identification and similar questions may legitimately remain disputed or `unresolved`.

The correct deterministic target is therefore not:

`same evidence → same scholarly judgement`.

It is:

`same canonical process boundary → no silent authority drift / no silent canonical overwrite / reconstructable handoff and transition`.

## 4. Consequence for the Dev role

The current #74 `Development / Research Software Implementation` function is broader than ordinary full-stack software development.

A technically correct implementation can still be research-system incorrect if it:

- changes scholarly meaning for implementation convenience;
- collapses uncertainty or alternatives;
- moves information to the wrong canonical owner;
- treats derived output as canonical truth;
- passes tests while losing provenance or decision history;
- encodes a contested judgement as deterministic truth;
- asks the human owner to make routine software decisions;
- allows a new model run to overwrite prior research state;
- exposes restricted source material through tests/tooling;
- depends on unrecorded chat/prompt knowledge.

The suitable competence profile is therefore closer to **Research Software & AI Systems Engineering / Implementation** than generic “Fullstack Developer”. This is a competency refinement, not a new authority layer.

## 5. Required Dev/RSE/AI-systems competencies

Use only as required by the admitted task.

| Competency | Why it matters in `paleo-type` |
|---|---|
| Research Software Engineering | scholarly correctness/provenance outrank platform elegance; choose the smallest adequate mechanism |
| Requirements Engineering | consume Domain Review requirements without re-deriving scholarship; return semantic ambiguity instead of inventing it |
| Information/Data Modelling | preserve METHOD/CORPUS/PROJECT ownership, identity/reference semantics and canonical-vs-derived separation |
| Provenance / Research Data Stewardship | exact evidence identity, transformations, decision history, rights/preservation and restartability |
| Verification & Validation Engineering | executable invariants, regression fixtures, semantic-loss/migration tests, rebuildability |
| AI Context / Tool Engineering | derive task context from canonical state; prefer deterministic tools for deterministic questions; avoid master-prompt dependence |
| Human-in-the-loop Engineering | distinguish owner-reserved decisions, specialist judgement, Domain Review and bounded autonomous implementation |
| Human Auditability / Information Architecture | returned technical work must be understandable/challengeable without forcing the owner to reverse-engineer code |
| Reproducibility / Preservation-aware Engineering | preserve scientifically material inputs/tool versions/parameters and controlled evidence availability |
| Rights/Security-aware Engineering | source material must stay within authorized storage/tooling boundaries |
| Scholarly-interface literacy | recognize when a distinction is scholarly semantics that must be preserved/returned, without claiming specialist authority |

The last competency is deliberately bounded: Dev needs enough scholarly interface literacy to avoid destroying or inventing semantics, not enough authority to adjudicate the manuscript.

## 6. Existing deterministic direction

The repository already demonstrates the preferred approach in `corpus/source-contract.json`, `tools/source_contract.py`, tests and CI: stable, settled recurring rules are represented once and validated/derived where justified.

This supports a three-level control model already analysed in #66:

1. **deterministic structure/invariants** — IDs, references, ancestry, required provenance, rebuildability, migration completeness;
2. **non-deterministic scholarly judgement** — reading, interpretation, hand attribution, historical identification;
3. **deterministically governed canonical-state transition** — a different judgement may become a candidate/challenge, but canonical mutation requires an explicit reconstructable transition path.

This distinction should be consumed by Dev rather than recreated as a parallel engineering taxonomy.

## 7. Research-ready evidence availability adds an engineering requirement

#78 exposes an important operational distinction:

```text
IDENTIFIABILITY
REPRODUCIBILITY
RESEARCH-READY AVAILABILITY
```

A checksum, canonical File ID, crosswalk and reproducible render recipe can identify/reproduce evidence while a fresh authorized work context still cannot actually open the evidence needed for the active `NEXT ACTION`.

For Dev/RSE/AI-systems work this means restartability must be tested at the level required by the task. For visual manuscript work, a fresh authorized context must be able to obtain/open the exact source representation, not merely know which representation should exist.

This does not imply a media platform. It does imply that context/start-resume logic, tooling and provenance cannot treat “known evidence” and “available evidence now” as identical states.

## 8. Risk and challenge register

| Risk | Failure | Current/likely control | Control type |
|---|---|---|---|
| role drift | Source Research/Dev/Domain Review silently expands authority | #71–#77 role boundaries + handoff | procedural; partly structurally checkable |
| context omission | required governing state/REQ/evidence omitted in a new session | canonical reading path + #77 context fragment | structural completeness may be checkable |
| prompt dependency | old chat/master prompt becomes de-facto governance | canonical repo state + restart test | process/restart validation |
| semantic reinterpretation by Dev | implementation convenience changes requirement meaning | #73→#74 handoff + #74 stop + return | scholarly review + loss fixtures |
| false determinism | contested judgement becomes validator truth | #66 distinction + #73 review | methodological boundary; negative tests where known |
| CI-as-scholarship | test success treated as scholarly acceptance | #74→#73 scholarly adequacy return | procedural/human scholarly review |
| silent canonical overwrite | rerun/model difference mutates prior research state | #66 transition discipline | deterministic transition/history control where feasible |
| handoff information loss | evidence, uncertainty, non-goals or return state disappears | #77 HANDOFF | required structure potentially checkable |
| owner fallback overload | user asked technical/specialist questions | #75 + UX-011/012 | routing + human walkthrough |
| specialist-status confusion | AI self-review presented as independent validation | #76 + AI governance | validation-status distinction |
| source/context contamination | later contextual knowledge contaminates upstream reading | #72/#73 stage boundaries | context composition partly controllable |
| research evidence unavailable in fresh context | provenance exists but active source pixels cannot be opened | #78 + source/provenance + task-start check | access/retrieval checks where technically meaningful |
| rights/data leakage | restricted evidence enters public repo/tool/model path | source/provenance + AI governance | deterministic path/storage checks + human authority where needed |
| role proliferation | every skill becomes a new agent/role | #71 lean blueprint | governance/architecture judgement |
| process/form bloat | handoff ceremony displaces source work | #77 falsification | measure real burden before adding tools |
| technical self-assurance | implementer is sole technical correctness judge for high-consequence change | deterministic tests + Domain Review; possible later independent technical review trigger | trigger-based, not routine |
| tool/model drift | material behavior changes between versions | provenance + regression/evaluation when triggered | versioned fixture/evaluation |

## 9. Conceptual control stack

Prefer a layered control stack rather than one large prompt or workflow engine:

```text
Governing Objective / canonical method / REQ-*
        ↓
role + task context composed from repository state
        ↓
evidence availability and stage/context boundary
        ↓
bounded handoff with established + unresolved + non-goals + return
        ↓
deterministic tools for settled failure classes
        ↓
implementation
        ↓
regression / semantic-loss / provenance / rebuildability checks
        ↓
Domain Review scholarly adequacy review
        ↓
canonical persistence / NEXT ACTION
```

This makes model capability useful while ensuring that correctness-critical process knowledge is not monopolized by the model.

## 10. What can become deterministic

Good candidates, only when semantics are settled and repeated need justifies enforcement:

- IDs/references/ownership resolution;
- project/source ancestry and deterministic structural status;
- exact File identity and provenance relationships;
- presence of required handoff/task metadata;
- explicit FROM/TO/owner/return condition;
- required evidence pointer/access status where material;
- migration completeness and loss fixtures;
- rebuildability of derived outputs;
- canonical-vs-derived separation;
- transition/history preservation mechanics;
- scope/admission references for material implementation.

Do **not** determinise:

- manuscript readings;
- historical interpretations;
- hand attribution;
- specialist agreement;
- whether a single local finding is sufficiently general to become METHOD;
- one mandatory implementation design when several satisfy the requirement.

## 11. Technical assurance boundary

No separate technical-assurance role is currently justified.

First rely on:

- bounded Dev implementation;
- deterministic tests/regression/loss fixtures;
- Domain Review for scholarly adequacy when research semantics are carried;
- normal code review where useful;
- D-016 owner admission only for material change scope.

Reconsider a distinct independent technical review function only if real evidence appears, for example repeated high-consequence failures surviving Dev's own tests, institutionally required independent assurance, or sufficiently consequential systematic AI infrastructure where implementation/evaluation independence materially improves reliability.

## 12. Current issue routing

- **#71** — generic role/handoff blueprint and authority topology.
- **#72** — Source Research role fixture.
- **#73** — Domain Review / requirement derivation / scholarly sequencing.
- **#74** — Development/Implementation role and return contract.
- **#75** — Human Owner/Governance boundary.
- **#76** — independent qualified specialist review.
- **#77** — model-independent task/handoff fragments and real handoff tests.
- **#78** — research-ready evidence availability/fresh-context restartability.
- **#79** — Dev/RSE/AI-systems competency and technical-assurance refinement derived from this analysis.
- **#66** — deterministic/epistemic/transition-control architecture.
- **#64** — first real source fixture whose eventual Domain Review→Dev cycle should falsify the handoff/competency model.

No additional role or workflow Issue should be opened merely for symmetry. New Issues should correspond to a demonstrated responsibility gap, recurring deterministic failure, or separately triggered implementation need.

## 13. Recommended next falsification sequence

Use real #64 work rather than invented role examples:

```text
#72 Source Research
→ material Checkpoint-B evidence / semantic-loss finding
→ #73 Domain Review classification
→ if real deterministic/system gap: bounded handoff
→ #74 / #79 competency boundary applied
→ deterministic implementation checks
→ #73 scholarly adequacy review
→ #64 NEXT ACTION
```

Test at the same time whether #77's minimal handoff content is sufficient and whether #78's fresh-context evidence availability is satisfied where source inspection is required.

The process passes only if the receiving session can act correctly from repository state/evidence without replaying the sender's chat and without silently expanding authority.
