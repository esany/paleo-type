# Research-assistance interaction boundary — D-016 decision brief — 2026-10-06

**Status:** HUMAN-OWNER `ADMIT` SELECTED / implementation scope defined below  
**Decision surface:** GitHub #292, concept comment #6005064183  
**Evidence owners:** #296, #297, #280  
**Scholarly dependency:** #291  
**Existing execution-control comparator:** artifact:ENG-A-0112 / artifact:ENG-A-0053

This file is the repository-first decision brief for the Human-facing research-assistance residual demonstrated in fresh scholarly use. It does not own Source/File/Project truth, scholarly METHOD, research priority or manuscript `NEXT ACTION`.

## 1. Demonstrated problem

A clean fresh-context source-entry fixture showed that the assistant could preserve some correct scholarly semantics and still make a poor collaboration decision:

```text
Human selects archival catalogue object for scholarly work
→ source-entry/provenance is recognized
→ primary catalogue access route fails
→ assistant avoids fabricating metadata
→ assistant asks Human for screenshot/PDF/manual catalogue fields
→ Human has to recover the intended assistance boundary
```

The defect is not that Human help is forbidden. It is that the assistance layer did not perform an adequate intermediate professional assessment before translating a technical/access failure into Human work: what is established, what is not verified, what the failed route proves and does not prove, how technically ordinary/difficult the missing action is, which bounded options remain, and why Human involvement is the best continuation.

The corrected acceptance evidence is preserved in #296/#297/#280. The earlier bootstrap-heavy fixture is `INCONCLUSIVE / CONFOUNDED`; the later clean V1b fixture is `FAIL` with partial positives.

## 2. Existing coverage and residual

Current owners already establish:

- evidence before plausibility and uncertainty as a valid result;
- scholarly/source METHOD ownership in #291 and the canonical methodology;
- Human Owner versus specialist versus AI authority boundaries;
- action-local resource/capability failure and outcome-return semantics in `AGENTS.md` / `methodology/workflow.md`;
- REQ-AI-005 unresolved-outcome preservation;
- REQ-AI-007 consequence/write boundaries;
- REQ-UX-011 normal research without repository/software-operator burden;
- REQ-UX-012 ordinary-language explainability and challengeability.

#292 demonstrated the residual at their interface: these semantics were not explicit/operative enough to make technical capability assessment, uncertainty/claim ceiling and justified Human/specialist collaboration reliable in normal scholarly use.

## 3. Admitted target image

For consequential source work, when a technical/access limitation materially affects continuation, the assistance layer must preserve the scholarly outcome and support a bounded judgement with these meanings where material:

1. what is established/directly supported;
2. what remains not verified, provisional or unresolved;
3. what evidence/test is actually needed;
4. what technical route(s) were actually tried;
5. what the observed failure proves and does not prove;
6. which bounded viable options remain and their expected information gain;
7. the chosen next discriminating action;
8. the claim ceiling / what remains unestablished;
9. whether the correct continuation is internal action, truthful inability, bounded Human contribution, Human-Owner authority, or specialist/unresolved escalation.

These are semantic requirements, not a mandatory template, global enum or state machine.

## 4. Admitted change locus

### Shared canonical semantics

Refine only the existing cross-project owners needed to make the assistance boundary stable:

- `AGENTS.md` — universal research-assistance capability/uncertainty/Human-collaboration guardrail;
- `methodology/workflow.md` — bounded execution assessment connecting action-local technical/access failure to a justified continuation.

### Owner-local/runtime surfaces

An owner-local interaction adapter or skill may consume the shared rule only where the runtime/discovery path is actually demonstrated. This admission does not authorize inventing a new interaction platform merely to force activation.

Existing Project/outcome derived contexts may be consumed where applicable, but new-source/no-Project scholarly work must not be forced through Project state.

## 5. Alternatives disposition

- **SStA/source-specific patch only:** rejected; overfits the negative fixture.
- **Duplicate the rule into #291 scholarly METHOD:** rejected; current evidence does not demonstrate a missing provenance/source-entry METHOD semantic.
- **Copy the shared rule into every skill:** rejected; creates drift and duplicate owners.
- **Universal capability planner / workflow engine / uncertainty state machine:** rejected; disproportionate and risks technical machinery choosing scholarly action.
- **Pure CI/prose acceptance:** rejected; repository checks cannot certify future natural-language research-assistance behavior.
- **Declare platform limitation without attempting the shared refinement:** rejected at current evidence state; a repository-controlled assistance semantic gap is demonstrated.

## 6. Verification / falsification plan

Behavioral acceptance must use ordinary fresh-context research prompts without bug hints:

1. **F1 — archival URL / primary fetch failure:** preserve selected-source scholarly purpose; distinguish selected object from unverified catalogue details; make a proportionate assessment; progress internally or explain a real limit; targeted Human help is allowed only when justified.
2. **F2 — trivial/recoverable technical support:** one route fails while another ordinary authorized route is available; route internally without making the Human operate tools.
3. **F3 — genuine environment/evidence ceiling:** no adequate authorized route remains; state a truthful scoped ceiling and make only the minimal useful Human request/continuation boundary.
4. **F4 — specialist uncertainty:** evidence is accessible but specialist judgement remains; preserve `unresolved` / specialist routing instead of asking the non-specialist Human to adjudicate.

Acceptance evaluates the actual next action, Human burden, uncertainty and claim ceiling. Preferred vocabulary is not the criterion. Same-context correction is not independent acceptance.

Deterministic repository checks may verify only stable structural properties they actually execute: repository integrity, references/currentness and absence of duplicate truth stores. They do not certify model behavior or scholarly adequacy.

## 7. Definition of Done

This bounded change is done only when:

- admitted shared semantics are implemented in their correct owners;
- no new scholarly stage, evidence ontology, planner, workflow engine or parallel state store is introduced;
- repository-testable checks pass for their honest envelope;
- F1–F4 are executed in fresh contexts and dispositioned;
- Human-facing behavior makes material knowledge/uncertainty, technical possibility/limit, reason for Human contribution and residual claim ceiling understandable;
- #296/#297 and #280 receive the behavioral result;
- final Result Review states `solved | partial | residual platform/model limit` truthfully.

## 8. Explicit non-goals

No new source-entry stage or METHOD by convenience; no Source/File/Project/CORPUS semantic change; no uncertainty enum/state machine; no generic planner/orchestrator; no automatic exhaustive search loop; no rule that the Human may never be asked for help; no requirement that one Chat/runtime possess every capability; no specialist substitution by the non-specialist Human; no CI claim of future-model correctness; no absorption into completed SD-KA-01.

## 9. Admission boundary

The Human Owner selected **`ADMIT`** in ChatGPT on 2026-10-06 after the bounded #292 decision surface was presented.

Implementation is authorized only inside §§3–8. A genuinely new material semantic owner, architecture, schema, migration or authority choice outside this envelope must return through D-016 before implementation.
