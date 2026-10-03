# Human decision-readiness and design-process re-baseline audit — 2026-10-03

**Status:** NON-NORMATIVE META-AUDIT / PROCESS RE-BASELINE — **NOT READY FOR D-016 DECISION**  
**paleo-type baseline:** `main@aed044bbcb0351eaba51310ac5c1353d4f50c404`  
**Wissensarbeit comparator baseline:** `main@b448915cf774c573dbf82cf2e17bcb03c10a9ed8`  
**Re-evaluates:** `requirements/repository-knowledge-lifecycle-d016-decision-surface-2026-10-02.md`, `requirements/repository-target-state-implementation-readiness-2026-10-03.md`, `requirements/human-proxy-work-lifecycle-context-efficiency-audit-2026-10-03.md`, `requirements/repository-knowledge-lifecycle-d016-refinement-2026-10-03.md`  
**This artifact is not:** METHOD, a D-016 admission, a new Project/programme owner, manuscript scope, a scholarly `NEXT ACTION`, implementation permission, a runtime/workflow/Skill decision, or a replacement for the historical evidence in the artifacts it re-evaluates.

## A. Executive disposition

The current lifecycle revision is **not ready for a D-016 owner decision**.

Substantial repository-specific analysis has already happened. It would be inaccurate to say that analysis never took place. However, the work did not remain cleanly separated into `problem → analysis → requirements → research → concept → design`. The later artifacts increasingly mixed these stages:

- causal analysis and requirements were present;
- internal repository research and `Wissensarbeit` comparison were substantial;
- competing architecture concepts were already generated;
- the work then moved into partial design (`Authorized Work Contract`, `decision-needed`, bounded context compilation, result/return envelope, B0/B1 execution-state treatments);
- candidate work decomposition and admission framing introduced implementation-planning pressure;
- this happened before a fresh re-baselining of the newly exposed Human decision-comprehension failure and before targeted comparative research on that failure family.

The strongest prior architecture direction — Class B and the IC-01/02/03/06 family — remains valuable **solution-hypothesis / concept-design evidence**. It is no longer treated as a decision-ready default architecture by this current meta-audit.

The decisive new evidence is the recent Human interaction itself. The Human Owner replied only `ausführen` while later stating that he did not understand where the process stood, what had already been decided, what remained open, or what executing the request would actually do. No D-016 implementation was admitted by those acknowledgements, so this was not a material implementation-authority overreach. It was nevertheless a real system failure:

> the Human was formally kept in the loop while not being sufficiently equipped to understand the loop.

That failure invalidates the claim that the current architecture package is already ready for an `ADMIT | REFINE | DEFER | REJECT` decision.

Current disposition:

> **RE-BASELINE THE PROBLEM AND DESIGN PROCESS FIRST.**
>
> Preserve earlier solution work as evidence/hypotheses; do not discard it and do not promote it. Re-derive requirements after the Human decision-readiness failure is included, perform only the targeted research needed to close the remaining knowledge gaps, then generate/compare concepts and proceed to design. Implementation planning follows a sufficiently reviewed design, not the reverse.

---

## B. Fresh authority and current-state boundary

Fresh current authority for this pass establishes:

- the scholarly result and source understanding remain the product; software, AI and workflow are subsidiary;
- uncertainty is a valid result;
- the non-specialist Human Owner must be able to understand the active result, uncertainty, evidence basis, validation state and next meaningful action;
- AI owns routine bounded work already authorized, while non-derivable purpose, material priority/scope, D-016 admission and consequential use remain Human-owned;
- complete **applicable** context is required, not indiscriminate repository loading;
- the D-016 material-change path remains `analysis → requirements → concept → owner review / explicit implementation admission → development → tests/loss checks → result review`;
- Domain→Dev handoff is supposed to carry demonstrated problem, evidence, research consequence, established semantics, unresolved state, required system property, scope and return question **without handing Dev an implementation design**;
- Human/restartability review already asks whether a fresh human/AI context can understand and challenge consequential state without the originating chat.

All three manuscript Projects currently record no owner-selected active scholarly scope. This meta-audit therefore creates no manuscript `NEXT ACTION`.

GitHub #225 and #230 are closed as work metadata. Their histories remain evidence, not current implementation authority. The accidental #236–#238 placeholder Issues are closed `not_planned` and explicitly carry no authority, priority, scope, D-016 or Project consequence.

---

## C. The interaction failure is a first-class system finding

### C1. What happened

The recent interaction sequence exposed this pattern:

```text
agent has a detailed internal/repository-backed model of the work stage
→ agent presents a compressed summary and a next decision/action surface
→ Human says “ausführen”
→ agent treats that acknowledgement as sufficient instruction for the proposed bounded repository action
→ later Human reports that the process stage and consequences were not understood
```

The repository changes were non-normative analysis/navigation changes and did not admit material lifecycle implementation. That limits the consequence, but it does not remove the failure.

### C2. Why this is not merely a wording problem

The system goal was to remove the Human as technical relay/dispatcher. The interaction instead risked making the Human a **semantic confirmation proxy**:

```text
Human no longer routes the mechanics
but
Human is asked to confirm a process state whose meaning is clearer to the agent than to the Human
```

A Human can therefore be formally in the loop while lacking sufficient situational awareness to exercise the authority reserved to that Human.

Candidate distinction exposed by the failure:

```text
AUTHORIZATION / ACKNOWLEDGEMENT
≠
INFORMED DECISION READINESS
```

and:

```text
HUMAN-IN-THE-LOOP
≠
HUMAN UNDERSTANDS THE LOOP
```

These are **problem/requirement candidates**, not promoted METHOD in this pass.

### C3. Why `ADMIT | REFINE | DEFER | REJECT` was premature as the next surface

A compact option token can be useful only after the Human can reconstruct at least:

- where the work stands;
- what is evidence versus inference;
- what has and has not been done;
- what is Requirement versus solution hypothesis;
- which alternatives remain materially open;
- what uncertainty remains;
- why Human authority is required at this point;
- what each option changes and what it does not change.

The recent interaction proves that this condition was not established for the lifecycle revision. The earlier decision surface was therefore too compressed for the actual Human decision context, even though it preserved formal D-016 authority.

---

## D. Stage audit — what has actually been done

The stage labels below describe the **actual semantic content** of the work, not merely document headings.

| Stage | Current disposition | Evidence-based interpretation |
|---|---|---|
| Problem / Need | **SUBSTANTIAL, REOPEN** | Human-proxy, reconstruction debt, closability/current-history and outcome-cursor problems are well evidenced, but Human decision-comprehension is newly demonstrated and was not integrated into the earlier problem frame. |
| Problem understanding / root-cause analysis | **PARTIAL–SUBSTANTIAL, NEEDS REOPENING** | #230 and later audits contain real causal analysis. They concentrated strongly on lifecycle/context/owner composition and did not sufficiently test HCI/decision-readiness and problem→requirement→solution separation for the new failure. |
| Requirements | **PARTIAL–SUBSTANTIAL, RE-DERIVE / RECLASSIFY** | AR-01…16 contain many strong outcome properties. AR-17…24 add useful concerns, but parts already encode a preferred solution shape. Requirements must be re-derived after the expanded problem analysis. |
| Research | **PARTIAL / INSUFFICIENT FOR ARCHITECTURE DECISION** | Repository history and `Wissensarbeit` comparison are strong internal evidence. Missing is a targeted external/comparative pass where needed on Human decision support, Requirements Engineering problem/solution traceability, agentic/durable execution and context engineering. |
| Concept generation | **SUBSTANTIAL BUT PREMATURE** | Class A/B/C and Options A–F are genuine concept work. Preserve them for later comparison; do not treat Class B as the default starting point. |
| Concept comparison / falsification | **PARTIAL** | Some alternatives were compared, and overengineering/second-clock risks were tested. The comparison preceded the newly expanded problem frame and did not include all necessary research dimensions. |
| Design | **PARTIAL BUT PREMATURE** | Work-contract meanings, `decision-needed`, Context Compiler shape, result/return envelope and B0/B1 are design-level hypotheses. |
| Implementation planning | **PARTIAL / PREMATURE** | Candidate work decomposition and “if ADMIT then…” sequencing already appeared before the design basis was fully requalified. |
| Implementation of this lifecycle revision | **NOT STARTED** | Recent PRs changed only non-normative analysis/navigation artifacts. Existing C1R is separate earlier bounded implementation under #225. |
| Verification / validation of proposed lifecycle architecture | **NOT SUFFICIENT** | CI proves repository mechanics only. No Human-comprehension validation, external research synthesis, or clean end-to-end concept/design review establishes the current architecture choice. |

The correct interpretation is therefore neither `nothing has been analysed` nor `the solution is decision-ready`.

It is:

> **substantial analysis and premature concept/design became interleaved; the new failure requires a clean re-baseline before architecture admission.**

---

## E. Reclassification of the existing solution package

### E1. Original D-016 surface / Class B

Current classification: **USEFUL HYPOTHESIS / PREMATURE CONCEPT FOR CURRENT DECISION PURPOSE**.

Class B remains plausible and well motivated by prior lifecycle/knowledge evidence. Its earlier `recommended architecture class` status is retained as historical reasoning, not current admission readiness.

### E2. IC-01 / IC-02 / IC-03 / IC-06

Current classification: **CANDIDATE CONCEPT/WORK AREAS — KEEP FOR LATER COMPARISON**.

They trace to demonstrated failure families, but the current meta-audit does not establish that this decomposition is the only or best design after the Human-comprehension problem and targeted research are included.

### E3. Phase-neutral Authorized Work Contract

Current classification: **USEFUL DESIGN HYPOTHESIS**.

The underlying requirement candidate — substantive work before implementation must be restartable/understandable and not require artificial Human relay — is strongly supported. The specific contract shape is not yet a requirement.

### E4. `decision-needed`

Current classification: **REQUIREMENT CANDIDATE + DESIGN HYPOTHESIS**.

The system clearly needs to discriminate genuine Human authority from routine execution. Whether this should be represented as `decision-needed`, derived via another interface, or handled by a different design remains open.

### E5. Context Compiler / bounded operational view

Current classification: **PLAUSIBLE CONCEPT, NOT YET SELECTED**.

Applicability-bounded context is a strong requirement candidate. A `Context Compiler` is one possible solution form.

### E6. Result/Return Envelope

Current classification: **PLAUSIBLE INTERFACE/DESIGN HYPOTHESIS**.

The requirement candidate is continuity without Human message transport and without replaying whole history. A particular envelope shape is not yet established.

### E7. B0/B1 cursor test

Current classification: **USEFUL LATER DESIGN EXPERIMENT, NOT CURRENT ARCHITECTURE ORDER**.

It remains sensible to test derivation before adding a second state owner, but even that framing belongs after requirements/research/concept comparison rather than defining the planning baseline now.

---

## F. Whole-system perspective — what was covered and what remains weak

The previous audits were strong in:

- repository knowledge lifecycle;
- current/history/supersession;
- canonical ownership;
- restartability;
- programme/work closability;
- AI/Human/specialist authority separation;
- token/context reconstruction cost;
- local PASS versus parent/programme closure;
- anti-overfit/Generic-Fit;
- second-clock/duplicate-state risk;
- basic agentic continuation and repair/return ideas.

They were weaker or incomplete in:

### F1. Human / HCI / decision support

The key newly demonstrated gap is not merely `ask Human less` but `make a necessary Human decision genuinely understandable`. Situational awareness, decision framing, progressive disclosure, automation surprise and comprehension/validation need explicit analysis.

### F2. Requirements Engineering process integrity

The earlier work identified problem and requirements, but later artifacts blurred:

```text
problem property
→ requirement candidate
→ preferred architecture concept
→ design interface
```

The current process needs stronger protection against deriving Requirements backwards from an attractive design.

### F3. Targeted external/SOTA research

`Wissensarbeit` is a valuable internal comparator but cannot substitute for the external/domain research needed where the problem crosses HCI, Requirements Engineering, systems/control and agentic execution.

### F4. Human decision readiness as validation dimension

The repository already separates technical assurance, scholarly adequacy, specialist validation, Human/governance review and restartability. For this system problem, the Human surface also needs to demonstrate that reserved Human authority is exercisable with sufficient understanding rather than merely available as a choice token.

### F5. Solution-space freshness

Class B may still win. The process must allow it to lose.

A clean concept phase should be able to return:

- a simpler existing-owner/process solution;
- a derived/context solution;
- a stronger explicit state model;
- an execution harness/orchestration solution;
- a semantic trace/decision-support solution;
- a combination;
- or a different architecture supported by research.

No candidate is rejected or selected because of size.

---

## G. Uncertainty register

| ID | Proposition | Current status | What would materially reduce uncertainty |
|---|---|---|---|
| U1 | Human relay/proxy arises primarily from missing operational work state | **PARTLY SUPPORTED / OPEN** | distinguish relay cases caused by work-state loss from cases caused by Human comprehension, platform/evidence or genuine authority. |
| U2 | Class B is the right architecture class | **UNRESOLVED** | re-derived requirements + targeted research + fresh competing-concept comparison. |
| U3 | an explicit Authorized Work Contract is required | **PLAUSIBLE, UNPROVEN AS FORM** | compare contract-based, derived and alternative representations against same requirements. |
| U4 | `decision-needed` can be derived reliably enough for safe continuation | **UNRESOLVED** | adversarial cases with ambiguous authority/materiality and Human comprehension validation. |
| U5 | a persisted execution cursor is needed | **UNRESOLVED** | later derivation-vs-cursor comparison after semantics are established. |
| U6 | context compilation will materially reduce token/Human burden without loss | **SUPPORTED IN PRINCIPLE, EFFECT SIZE UNPROVEN** | baseline measurement on fresh-context reconstruction and loss/adversarial tests. |
| U7 | Human decision-comprehension is part of the same lifecycle failure family | **PARTLY SUPPORTED** | root-cause analysis across multiple interaction cases; may be coupled HCI/semantic layer rather than identical mechanism. |
| U8 | semantic trace / Wirknetz properties are useful here | **SUPPORTED AS ANALYTICAL/DESIGN-METHOD LENS** | apply to the current work genealogy and compare whether it exposes materially wrong relations/solutionism. |
| U9 | existing paleo-type owners are sufficient for the final solution | **UNRESOLVED** | requirements/concept testing; avoid both second-clock assumption and existing-owner dogma. |
| U10 | no orchestration/workflow layer is required | **UNRESOLVED** | universal engine remains unsupported, but a smaller durable execution mechanism may become warranted after design evidence. |

---

## H. Fresh `Wissensarbeit` findings relevant to the re-baseline

### H1. Current product/lifecycle evidence

`Wissensarbeit` explicitly requires that purpose, problem understanding, meaning, priority and material acceptance remain Human-understandable; automation should relieve the Problem Owner and meta-work must not become the product.

Its current lifecycle is non-linear:

```text
bootstrap → discover → understand → research → model → decide
→ build → verify → use → learn → maintain → archive
```

This is useful evidence that planning/design work is broader than implementation, but it is not a lifecycle to copy into paleo-type.

### H2. The most relevant Skill-system safeguard is not a runtime

Issue #52 states:

- `state != operator`;
- state/event driven, not fixed pipeline;
- authority remains external;
- growth only from observed necessity;
- trace correctness > completeness;
- verification != validation;
- architecture must not follow an interesting concept merely because it is attractive.

Most relevant to this audit is its `requirement-driven-concept` principle:

> exploratory concept work may precede formal Requirements, but canonical solution concepts, architecture and implementation must remain driven by demonstrated needs/gaps, evidence and accepted requirements/acceptance conditions.

That is a direct warning against treating the current Class-B/design package as the planning baseline.

### H3. Intent/Gap Semantic Fidelity is highly relevant as a lens

Issue #53 explicitly separates:

```text
primary Human statement
≠ paraphrase
≠ inference/derivation
≠ confirmed meaning
```

and states that Intent is not identical to:

- proposed solution;
- Requirement;
- task packet;
- implementation choice;
- later AI paraphrase.

Its failure classes `Semantic Shift` and `False Traceability` map directly to the present risk:

```text
Human says “ausführen”
→ agent binds that to a process interpretation
→ downstream work treats the interpretation as sufficiently understood Human direction
```

The important safeguard is not “never act on terse input”. It is to preserve the evidence/meaning boundary and ask only when material meaning is genuinely unresolved.

### H4. Task Compilation / bounded interaction exposes a useful but incomplete analogy

Issue #55 says a terse acknowledgement is meaningful only through a visible pending interaction envelope; exactly one bound action may proceed without re-asking; authority does not cascade.

That is useful. The current paleo-type failure adds a further question:

> Is a pending action merely visible, or is it sufficiently understandable for the Human to exercise the authority attached to it?

This is a **candidate extension of the problem analysis**, not evidence that paleo-type needs a Task Compilation Skill.

### H5. `Wirknetz` is not currently a Skill/runtime

The fresh `skills/README.md` lists only the prompt and failure-pattern-check candidates. Current Wirknetz work is a source-/provenance-aware reconstruction method. #56/#58 explicitly prohibit turning it into solution, architecture, ontology or automatic Requirement promotion.

The useful chain is analytical:

```text
source / statement
→ Intent
→ Gap
→ Need / Pain / Goal
→ Requirement / Requirement Candidate
→ Constraint / protection
→ Acceptance / Verification / Validation
→ Feedback / correction / supersession
→ uncertainty / non-conclusion
```

### H6. Track-B negative evidence still matters

The independent #76 review concluded `EXISTING MECHANISMS SUFFICIENT` for its frozen Wirknetz↔Skill handoff cases and falsified the writer's stronger necessity claim for contract sharpening. It supported no new Bridge/Interface Skill/Capability/Building Block and explicitly separated semantic sufficiency from runtime maturity.

Current consequence for paleo-type:

> **Do not add a Wirknetz Runtime, Bridge or Skill because this audit finds Wirknetz useful.**

Use its properties as a reconstruction/trace/design-method lens first.

---

## I. Wirknetz / Skill synergy disposition

| Property | Relevance to current problem | Current disposition for paleo-type |
|---|---|---|
| Human/Stakeholder Intent preserved separately from solution wording | very high | **ANALYTICAL / REQUIREMENTS-TRACE PROPERTY** |
| Gap typing | high, especially Human Understanding/Judgement vs System/Capability | **ANALYTICAL LENS; do not force taxonomy** |
| Requirement Candidate ≠ accepted Requirement | very high | **DESIGN-METHOD / PROCESS PROPERTY** |
| Requirement ≠ Concept/Design | very high | **DESIGN-METHOD PROPERTY** |
| primary wording ≠ AI paraphrase ≠ inference ≠ confirmed meaning | very high | **DECISION-SUPPORT / TRACE PROPERTY** |
| provenance/source role | high | **ALREADY CORE, REUSE** |
| correction/supersession; `latest wins` prohibited | high | **CURRENT/HISTORY / TRACE PROPERTY** |
| uncertainty/non-conclusion | very high | **ALREADY CORE; APPLY TO SYSTEM DESIGN TOO** |
| relation correctness > completeness | very high | **QUALIFICATION PROPERTY** |
| verification ≠ Human validation | very high | **ALREADY CORE; APPLY TO DECISION READINESS** |
| state != operator | medium-high | **ARCHITECTURE LENS, NOT COMPONENT** |
| Wirknetz graph/runtime/Skill/Bridge | no demonstrated need | **NOT JUSTIFIED** |

A particularly useful current hypothesis is that the latest interaction exposed **coupled gaps**:

- an `Understanding/Judgement Gap`: the Human did not have enough process/decision understanding;
- a `System/Capability Gap`: the system did not reliably produce the decision context needed to exercise Human authority.

This classification is provisional; it must not become a schema merely because the comparator has these terms.

---

## J. Requirement candidates after re-baselining

The following are **candidate requirements for later derivation/review**, not accepted generic requirements in this artifact:

1. A Human-facing material decision must expose enough current process state, evidence, uncertainty and open alternatives for the Human to understand what is actually being decided.
2. A terse acknowledgement such as `ausführen` must not silently gain authority beyond a uniquely bound, sufficiently understandable pending action.
3. Routine work already inside established authority should not require Human confirmation merely for continuation.
4. Problem statement, inference, Requirement Candidate, accepted Requirement, concept, design and implementation authority must remain traceably distinguishable.
5. A solution hypothesis must not be backfilled into the requirement set as if it were problem evidence.
6. Material uncertainty and credible alternatives remain visible until evidence or an authorized decision resolves them.
7. A fresh capable context can reconstruct the current bounded work and its evidence/authority without old chat or archaeology.
8. Context reduction targets reconstruction overhead, not evidence, uncertainty, provenance or Human/specialist authority.
9. Child/result return to a parent/work context does not require the Human to act as message bus.
10. A material D-016 admission request is presented only after the problem/analysis/requirements/necessary research/concept/design basis is sufficiently mature and the Human can understand that basis.

These candidates must be re-derived from the complete problem analysis and may be fused, revised or rejected.

---

## K. Targeted research still needed before concept selection

Do not create a broad research programme by taxonomy. The following are the currently justified research questions; each should be bounded by the gap it must close.

### R-A — Human decision support / automation interaction

Investigate only enough current evidence to answer:

- what makes a Human materially decision-ready rather than merely presented with choices;
- how situational awareness, automation surprise and progressive disclosure affect safe Human-on/in-the-loop control;
- how to verify comprehension without turning every action into ceremony.

### R-B — Requirements Engineering / solutionism control

Investigate:

- problem vs need vs Requirement vs solution/design separation;
- traceability from stakeholder evidence to requirements and rationale;
- mechanisms for preventing architecture concepts from backfilling requirements;
- how uncertainty and competing interpretations remain explicit.

### R-C — Agentic / durable execution systems

Investigate only after R-A/R-B clarify the semantics:

- resumable bounded execution;
- state/event/workflow approaches;
- deterministic transitions vs AI judgement;
- escalation and Human decision gates;
- failure/retry/reconciliation without a second authority clock.

### R-D — Context engineering

Investigate:

- applicability-bounded context;
- progressive disclosure and provenance expansion;
- externalization/compaction/handoff;
- how context efficiency is measured without semantic starvation.

### R-E — semantic trace / rationale models

Use `Wissensarbeit` and external/established approaches only to test whether relation/provenance semantics improve problem→requirement→design traceability enough to justify any additional mechanism. No graph/runtime presumption.

If existing repository evidence already answers one of these questions sufficiently, document that and do not perform research theatre.

---

## L. Methodical work plan — not an implementation plan

### Phase 1 — Problem re-baseline

Goal: one evidence-bound problem map including the new Human decision-comprehension failure.

Deliverables:

- observed failures/symptoms;
- stakeholder/Human consequences;
- system boundaries;
- distinct/coupled failure families;
- explicit unknowns/non-conclusions;
- old solution hypotheses separated out.

Exit: problem statement does not depend on Class B, a cursor, a compiler, or another preferred solution.

### Phase 2 — Root-cause / systems analysis

Test competing causal models, including at least:

- work-state/continuation deficit;
- Human decision-support/semantic-binding deficit;
- current/history/context reconstruction deficit;
- mixed model;
- alternative explanations discovered during analysis.

Exit: root causes and uncertainties are sufficient to derive solution-independent requirements.

### Phase 3 — Requirements

Derive outcome/quality/constraint requirements from Phase 1/2 evidence.

For every material requirement keep trace to:

```text
source / observed failure
→ problem consequence
→ required property
```

Do not include component names unless they are genuine external constraints.

### Phase 4 — targeted Research

Execute only the research streams needed to resolve material design uncertainty from Phases 1–3. Persist findings with evidence/source roles and non-conclusions.

### Phase 5 — Concept generation

Generate multiple materially distinct concepts from the requirements. Reintroduce Class B, contracts, derived context, cursor/harness, semantic-trace approaches and other prior ideas only here as candidates alongside new options from research.

### Phase 6 — Concept comparison / falsification

Use the same requirements, fixtures and failure cases across concepts. A candidate may win because it is larger or smaller only insofar as that changes requirement fit, risk and burden.

### Phase 7 — Design

Only the selected/surviving concept is turned into:

- owners;
- state/relationship semantics;
- interfaces;
- transitions;
- Human surfaces;
- persistence;
- tests/qualification;
- migration/reversibility.

### Phase 8 — Design review / Human decision-readiness

Before asking for D-016 admission, establish that the Human can see:

- current stage;
- problem/evidence;
- accepted requirements;
- research conclusions and uncertainty;
- concepts considered/rejected;
- selected design and consequences;
- what remains open;
- exact scope that admission would authorize;
- what happens if the decision is deferred.

Only if this is sufficiently understandable does `ADMIT | REFINE | DEFER | REJECT` become an appropriate material decision surface.

### Phase 9 — Implementation planning

Only after an adequately reviewed design and any required D-016 admission:

- work packages;
- dependency order;
- migration;
- rollout;
- exact tests;
- rollback/reversibility.

### Phase 10 — Implementation

Implement only admitted design scope.

### Phase 11 — Verification / Validation / Reconciliation

Keep separate:

- technical verification;
- repository/currentness/restartability;
- Human decision/use effectiveness;
- scholarly/domain consequences where relevant;
- specialist validation where triggered;
- parent/programme closure.

---

## M. Current Human decision surface

There is **no material architecture decision required from the Human Owner now**.

The current correct state is:

```text
NOT READY FOR D-016 DECISION
```

The next bounded work is analytical/research preparation, not implementation and not owner selection among Class-B variants.

The Human may of course challenge or change the purpose of this analysis. In the absence of such a change, the repository already contains enough authority to continue the non-normative re-baselining work without asking for a ceremonial `continue` after every substep.

---

## N. What remains valid from earlier work

This re-baseline does **not** erase the previous audits.

Still-valid evidence includes:

- the #230 adequacy-first correction: establish sufficiency before simplifying;
- current/history/supersession and closability as demonstrated problem families;
- canonical-owner and restartability invariants;
- artificial Human relay as a real usability/system failure;
- token/context reconstruction cost as a real burden;
- Genericity ≠ Distribution and live research as first real/falsification fixtures;
- no automatic Project priority from system work;
- no `Wirknetz` Runtime/Bridge based on current evidence;
- no package/`src` move absent its own trigger;
- technical PASS ≠ Human/scholarly acceptance.

What changes is their **process status**: prior architecture and design constructs become evidence/hypotheses to be re-tested after the problem/requirements/research baseline is clean.

---

## O. Persistence consequence

Repository navigation should no longer describe the current lifecycle package as `decision-ready` without qualification.

The original D-016 surface, target-state artifact, Human-proxy audit and 2026-10-03 refinement remain preserved as historical analytical/concept/design evidence. Their original claims are not rewritten out of history.

Current interpretation after this audit:

> **decision-readiness claim superseded for the present lifecycle revision; no D-016 admission; re-baselining required before the next owner architecture decision.**

No GO, AGENTS, METHOD, Project state, schema, runtime, source truth or manuscript research state is changed by this conclusion.
