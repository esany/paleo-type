# Critical re-audit — deterministic control-layer recommendation

Status: CURRENT CRITICAL RE-AUDIT / prior control-layer recommendation superseded  
Repository: `esany/paleo-type`  
Baseline: `main@b7a77bc4d0415b9017e14f0513bef89c1f9a8722`  
Audit date: 2026-10-09  
Online source: GitHub connector only

## 1. Short verdict

The earlier recommendation to introduce a “small fail-closed control layer C1–C5” was itself too solution-oriented and therefore partially reproduced the False-Lean/Solution-first failure documented in #297.

The fail-closed principle remains valid for individual stable deterministic checks. The proposed generic layer is not currently implementation-justified.

The current evidence supports this conclusion:

> No new generic control layer, schema, state machine or workflow engine should be implemented now. Existing owners and accepted semantics must first be tested through the already-defined fresh-context and productive-runtime vertical acceptance paths.

The previous recommendation is therefore reclassified:

- not an implementation plan;
- not a D-016 admission;
- not a new architecture requirement;
- an unvalidated solution hypothesis, now superseded by this re-audit.

## 2. Fresh-state basis

Current online `main`:

`b7a77bc4d0415b9017e14f0513bef89c1f9a8722`

Freshly read canonical sources:

- `GOVERNING_OBJECTIVE.md` — `d65c4a81b4314b484c25e62aeae6ce43e27613c7`
- `AGENTS.md` — `323f94add2c9defc312d74d56af59977f77b2c58`
- `methodology/maintenance.md` — `e779954ced07aef2b6b4ae3d6aca230ee7f1c7dc`
- `methodology/workflow.md` — `40d14237cb50ecf19b78cc64c5b087586f8aa0d2`
- `DECISIONS.md` — `affc14167637c4e06dc0f3ede1335c04b3f0537e`
- prior control-layer audit — `f90e92841ebb95294aed7a2ed0677d8d65d263b7`
- Wissensarbeit authority — `94cbda7847a5b73a691dd5d2d2eb81ed369294fb`
- Wissensarbeit reconciliation — `a87dffaf3d70bdefef43bca4de0e007be79ea3d9`
- Wissensarbeit material state — `a2917b28f4fe71904598b8efe6fb2cf9e3dd7d3f`
- Wissensarbeit execution state — `33f612ad715ceb754adb7d211a5ffefb539a2a5e`

The current Wissensarbeit execution state still says:

- allowed actions: inspect, research, analyze, persist evidence, complete;
- implementation allowed: false;
- route: GitHub repository;
- current step: T5 Case-C trial;
- no successor trial selected.

This audit therefore remains analysis/evidence work. It does not grant implementation authority.

## 3. Complete current open-Issue inventory

Fresh online issue search returned 31 open Issues.

### Active execution, acceptance and operative-efficacy strand

#271, #272, #280, #282, #292, #296, #297, #306, #307, #308.

### Wolkenburg/source/discovery/model/evidence strand

#12, #263, #265, #266, #267, #268, #269, #270, #291, #293.

### Paused/deferred coordination or concept strand

#90, #162, #202.

### Trigger-based future strand

#1, #2, #3, #4, #6, #13, #22, #62.

The inventory shows that the system already separates:

- active acceptance work;
- source/evidence work;
- model questions;
- deferred concepts;
- future trigger-based infrastructure.

A new generic control layer would cut across these existing boundaries and risks becoming a second routing system.

## 4. Failure-family matrix

| Failure family | Root | Manifestation | Existing owner/evidence | Current disposition |
|---|---|---|---|---|
| False Lean / local PASS | slice completion leaks into parent outcome acceptance | coherent Human outcome is reduced to a convenient local patch | #297, #280, #272, historical #230/#250 | real recurrence; qualification and acceptance re-entry, not new generic architecture |
| Context/content leakage | semantic owner is not preserved across boundaries | Wolkenburg context is mistaken for Nr. 632 content or priority | #270, #293, #296, #306, #308, Source/Project owners | current distinction is explicit; discriminating real fixtures still matter |
| Provenance collapse | source facts, AI derivation and unresolved gaps share one narrative layer | catalogue claims become historical synthesis or hypothesis | #307, #292, evidence/AI-governance owners | existing semantics; operative efficacy remains partial |
| Access-to-direction drift | support task acquires scholarly direction authority | image access becomes synthesis, discovery or NEXT ACTION | #292, #306, #280 | existing boundary; fresh real-use acceptance required |
| Closure laundering | Issue/PR/CI state is read as whole-system acceptance | child or technical work appears to solve parent outcome | #225, #250, #272, #280, #281 | closure levels already distinguished; composition and currentness remain to be proven |
| Local-first execution | runtime route is not reliably constrained by online authority | local result can appear canonical | `AGENTS.md`, #281, #280, #297 | repository can document/prove remote writes; harness boundary remains separate |
| Productive-runtime gap | implementation exists but real destination/package acceptance is absent | list/probe/partial package called secured | #271, #282, #280 | productive acceptance open |
| Source-model ambiguity | real source cases expose distinctions not yet settled | scope, File/Source, form/stage or relation semantics are conflated | #12, #263, #265–#270, #291, #293 | evidence-triggered; no generic contract change authorized |

## 5. Causal Wirknetz

The current evidence supports this network:

```
Human-Outcome / research need
        ↓
real friction or evidence gap
        ↓
correct normative diagnosis
        ↓
bounded local implementation or audit
        ↓
local PASS / Issue progress
        ↓
currentness or closure signal becomes easier to consume than residual outcome
        ↓
fresh context composes rules, evidence and runtime under new conditions
        ↓
composition/authority/provenance failure reappears
        ↓
Human has to recover the intended cursor and correct the system
        ↓
new regression / audit / comment growth
```

The causal defect is not simply “missing control”. It is the gap between:

- normative sufficiency;
- acceptance-coverage sufficiency;
- operative cross-context efficacy;
- model/platform assurance.

The repository already contains strong normative rules. The missing evidence is whether those rules compose reliably in the relevant real flows.

## 6. Critical audit of the prior control-layer proposal

### 6.1 Why it looked plausible

The previous proposal correctly identified useful properties:

- remote proof;
- evidence-bounded claims;
- separation of technical and scholarly acceptance;
- provenance visibility;
- refusal of local fallback;
- explicit closure scope.

These remain valid requirements or assurance questions.

### 6.2 Why it was still False Lean

The proposal then compressed these different questions into one “small control layer” before proving that they required a new shared owner.

That is the same error family as #297:

```
broad system problem
→ attractive common abstraction
→ small technical recommendation
→ apparent control completeness
→ real vertical efficacy remains untested
```

The proposal also mixed different control locations:

- repository contracts and CI;
- GitHub branch protection;
- connector/harness routing;
- Human-facing scholarly interaction;
- source/provenance semantics;
- Issue closure and result review.

Those are not one coherent implementation slice.

### 6.3 Existing evidence against immediate implementation

The current Issues explicitly state:

- #297: no new lifecycle/schema owner is yet justified; immediate work is qualification/falsification, not new implementation or D-016.
- #280: the remaining work is productive runtime acceptance plus fresh-context scholarly stage preservation; no new D-016 is required unless falsification demonstrates a genuinely new shared owner or enforcement architecture.
- #292: the bounded interaction refinement is implemented, but operative efficacy is partial; selected-object authority still failed in F1.
- #296: a fresh regression occurred after shared rules and technical PASS; the required return is to #280, not automatic duplication of the rule.
- #306/#307: the existing scholarly-control and provenance owners remain the natural owners; no automatic METHOD/system change follows.
- #271/#282: the real product/runtime acceptance remains open despite strong deterministic implementation assurance.
- #263/#265–#269: actual source/model triggers and D-016 decisions are explicitly required before contract changes.

These are direct counterevidence to a generic new layer as the immediate next action.

## 7. Owner and coverage analysis

### Already covered by existing owners

- Human authority and material-change admission;
- Project/Source/File/priority distinction;
- source/provenance semantics;
- technical versus scholarly acceptance;
- status/read versus retry/resume/new mutation;
- online-only repository persistence rule;
- deferred-trigger discipline;
- closure with explicit residuals;
- no automatic Project/CORPUS/METHOD mutation.

### Covered, but operative efficacy not yet proven

- fresh-context stage preservation;
- selected-object authority versus evidence bridge;
- provenance separation in real use;
- access task staying within intended scholarly scope;
- Human-facing mapping of internal codes;
- cross-context currentness and affected-owner return;
- real productive external destination/runtime behavior.

### Connector-/harness-boundary questions

- physically preventing local repository access;
- proving which route performed a mutation;
- failing closed when the connector is unavailable;
- observing and containing long-running external side effects.

The repository may define the evidence required for these properties, but it cannot itself prove all runtime facts.

### Evidence-triggered domain/model questions

- catalogue-bounded selection (#12/#263);
- active scope representation (#265);
- form versus transmission stage (#266);
- granular inspection coverage (#267);
- root File versus internal Source (#268);
- relation strength/evidence (#269);
- generic source-entry fit (#291);
- real Nr. 632 source-entry cycle (#293).

These must be answered by real source/evidence work, not by a generic control layer.

### Genuine owner gap?

Not established.

The current evidence demonstrates incomplete composition and acceptance coverage, but not that the existing canonical owners cannot represent the requirements. Therefore a new shared owner, state machine or control layer is not justified.

## 8. Deterministic versus non-deterministic boundary

### Suitable for existing deterministic checks

- remote branch/commit exists;
- file/reference resolves;
- schema and current controlled values are valid;
- a known accepted transition is not skipped;
- evidence reference exists;
- current and historical records are not silently confused;
- a context value is not copied into a content field where an existing contract forbids it;
- technical and scholarly acceptance fields remain separate.

These should be implemented only where an existing semantic owner and demonstrated failure already exist.

### Not deterministically solved by a new repository layer

- whether a documentary relation is historically or textually true;
- whether a source interpretation is scholarly adequate;
- whether a Human-facing response preserves the intended research outcome in all contexts;
- whether an LLM will compose existing rules correctly in a future conversation;
- whether a productive external runtime is fit before a long run;
- whether all consequential chat knowledge has already reached its canonical owner.

These require fresh real-use evidence, specialist or Human judgement, or an explicit assurance ceiling.

## 9. Vertical-first qualification plan

Do not create a new generic test programme. Use current owners and fixtures.

### V1 — fresh-context scholarly stage preservation

Owner: #280, with #296/#297 evidence and #292 assistance semantics.

Fixture:

```
Human selects a concrete archival catalogue object
→ current task is original-page/image access and Source/provenance establishment
→ primary access route fails
```

Expected:

- preserve the higher-order scholarly cursor;
- keep route failure action-local;
- use derivable read-only alternatives where appropriate;
- do not pull forward synthesis, vision or unselected research direction;
- do not promote Human selection into verified Source/Project authority without the evidence bridge;
- preserve source-derived, AI-derived and unresolved states;
- leave a bounded access/provenance ceiling if recovery fails;
- allow a fresh context to reconstruct the valid continuation.

This is not a PASS for the generic model. It is evidence for the tested envelope only.

### V2 — productive runtime acceptance

Owners: #271/#282, returned to #280.

Required:

- intended external destination/runtime;
- persistence, interruption/resume, observation, control and containment fitness before the long run;
- deliberate real archival processing;
- complete preserved package;
- integrity verification and truthful source/package information;
- fresh Human-facing entry;
- result review separating technical, package, source and scholarly claims.

A list probe, partial package, CI PASS or one downloaded image is not sufficient.

### V3 — false-Lean acceptance

Owner: #297/#280.

Check whether the current work block preserves:

- the complete intended outcome;
- every materially coupled owner;
- evidence and restart state;
- return condition;
- the difference between slice progress and parent acceptance.

Do not create a new generic Lean framework. Test the current work block against the existing #297 requirements.

## 10. Decision

Current decision:

> Existing owners are sufficient for the present analysis and qualification stage. The evidence does not justify implementing a new generic fail-closed control layer.

More precisely:

- retain fail-closed as a property of already-stable deterministic checks;
- do not create C1–C5 as a shared contract;
- do not create a new universal state machine;
- do not create a second Issue/acceptance owner;
- do not close or reopen historical Issues automatically;
- route the next work through #280, #271/#282, #292/#296/#297 and #272 as already defined;
- return to D-016 only if vertical falsification demonstrates that existing owners cannot express or enforce the required property.

## 11. What remains unresolved

- operative efficacy in a genuinely fresh context;
- composition of existing rules across access, provenance, authority and Human-facing assistance;
- real productive destination/runtime acceptance;
- final whole-system Result Review;
- source/model questions triggered by real Wolkenburg evidence;
- the assurance ceiling for behavior that cannot be mechanically guaranteed by the repository.

These are not evidence for a new layer by themselves.

## 12. External best-practice disposition

The previously consulted practices remain useful as comparison, not as local implementation authority:

- GitHub rulesets/checks can enforce repository admission properties, but do not establish scholarly or Human-outcome acceptance.
- Policy-as-code/default-deny principles can inform stable tool-boundary checks, but do not prove that a generic policy layer is needed here.
- Provenance models support traceability, but existing repository provenance owners must be tested before introducing another representation.
- AI-governance frameworks support scaled Human oversight, but do not replace fresh efficacy evidence.
- SLSA/W3C PROV/OPA are not reasons to add infrastructure without a demonstrated local failure requiring them.

## 13. Audit DoD

This re-audit is complete because:

- the complete current open-Issue inventory was checked;
- the previous control-layer recommendation was tested against current owners and current issue state;
- root causes, symptoms, manifestations and assurance limits are separated;
- False Lean, Solution-first, context leakage, provenance collapse, local-first execution, closure laundering and assistance-to-direction drift were checked;
- existing owners were tested before proposing a new owner;
- vertical qualification paths were identified;
- no new architecture or implementation was authorized;
- the superseded recommendation is explicitly marked as such;
- current unresolved work remains visible and routable without relying on this chat.

## 14. Final conclusion

The correct next action is not:

> Build a small fail-closed control layer.

The correct next action is:

> Use the existing owners to perform the fresh-context scholarly and productive-runtime qualification that is already open. Measure whether the existing rules compose into the Human outcome. Only if that real evidence proves an owner or enforcement gap should a precise D-016 decision surface be opened.

This is the adequacy-first correction:

`understand the full outcome → test existing composition → identify the exact missing property → admit only the necessary change → simplify only after sufficiency`

No new control layer is currently justified.
