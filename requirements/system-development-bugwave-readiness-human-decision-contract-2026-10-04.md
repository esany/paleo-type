# Bugwave design closure — activity-relative readiness and understandable Human decisions — 2026-10-04

**Status:** NON-NORMATIVE DETAILED DESIGN / **#249 DESIGN COMPLETE / D-016 DECISION NOT YET GIVEN**  
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Work owner:** #249; parent #244  
**Depends on:** #245 coverage, #246 configuration semantics, #247 context products, #248 ADR inventory  
**This file is not:** a universal workflow engine, an admission, an approval ceremony, or a Human comprehension score.

## 1. Problem

`DEV-READY` was previously used too globally. A piece of work can be ready for analysis, ready for design, ready for implementation, ready for verification, ready for specialist validation or ready for a Human material decision — these are not interchangeable.

A second failure was demonstrated in Human interaction: formal authorization can occur while the owner still lacks enough situational understanding of what stage the system is in and what the requested decision actually changes.

The correction must not create the opposite problem: forcing the Human to approve every routine transition or pass a knowledge test.

## 2. Readiness always names the next admissible activity

A readiness claim is valid only when it answers:

```text
Ready for WHAT activity?
Based on WHICH evidence/owners?
What remains outside this activity?
What would invalidate readiness?
Who may perform the activity?
What result/return is required?
```

Supported activity classes are descriptive, not a mandatory state machine:

```text
analysis / inquiry
design / architecture
implementation
verification
specialist validation
Human material decision
routine maintenance / propagation
```

Other task-specific activities are allowed when named precisely.

Never emit bare `DEV-READY` when the next activity matters materially.

## 3. Proportional bounded-work contract

Substantial work Issues should expose enough information for a capable executor to start and close reliably:

- demonstrated problem / required effect;
- material findings/Requirements/accepted decisions that constrain it;
- next activity and current readiness;
- dependencies and blocking uncertainty;
- non-goals / authority boundary;
- acceptance criteria;
- verification and validation mode;
- whole-system return.

Small routine tasks do not require empty fields or ceremony when these meanings are obvious from existing owners.

The purpose is **closure and transfer of meaning**, not template compliance.

## 4. Readiness invalidation

Readiness is sticky only while its basis remains valid. A material change to any of these can re-enter earlier work:

- problem/evidence basis;
- governing Requirement;
- accepted architecture/decision;
- prerequisite/dependency;
- implementation environment/capability where it affects feasibility;
- validation requirement;
- authority/admission;
- discovery of a material orphan finding relevant to the slice.

A new comment, branch, date or unrelated repository change does not invalidate readiness by itself.

## 5. Human material decision: plain-language contract

Do not ask the Human to `validate Human-Decision-Readiness`.

The practical requirement is:

> **Before asking for a material decision, present the situation so the Human can understand what is being decided and its consequences without reconstructing the audit history.**

The Human receives a decision brief, not a test.

### 5.1 Required brief content

For one material decision, show concisely:

1. **Why are we here?** — demonstrated problem, not implementation jargon.
2. **What is true now?** — accepted/current system state relevant to the decision.
3. **What remains wrong/open?** — material gap and consequences.
4. **What is proposed?** — selected architecture/change in understandable terms.
5. **What alternatives were seriously considered?** — including why not selected.
6. **Which decisions are already accepted?** — constraints that are not being reopened.
7. **Which decisions would this approval newly accept?**
8. **What would implementation actually change first?**
9. **What will not change?** — explicit non-goals, especially Project/manuscript authority.
10. **How reversible is it?** — migration/rollback and lock-in.
11. **How will we know it worked?** — verification vs validation.
12. **What uncertainty/residual risk remains?**
13. **Exact authority requested.**
14. **Consequences of `ADMIT`, `REFINE`, `DEFER`, `REJECT`.**

Uncommon abbreviations are expanded or avoided.

### 5.2 Human role

The Human Owner should only need to:

```text
understand
→ ask a focused question if desired
→ ADMIT / REFINE / DEFER / REJECT
```

The Human is **not** expected to:

- find or register Findings;
- sort Issues;
- reconstruct dependencies;
- compare Git history;
- choose technical sequencing;
- relay work between agents;
- prove understanding by answering a quiz;
- approve routine bounded work already within authority.

### 5.3 Comprehension evidence without a quiz

The decision surface is adequate when the Human interaction itself shows no unresolved material misunderstanding about:

- stage/readiness;
- problem being solved;
- exact proposed change;
- exact authority requested;
- major non-goals;
- residual material uncertainty.

A focused Human question indicates the brief should answer that point; it is not a failure by itself.

The system must not manufacture a numeric `comprehension score`.

## 6. Routine-work autonomy

Once a bounded activity is authorized and its prerequisites hold, AI/developers should execute it without repeated `weiter` / `ausführen` confirmation solely for ceremony.

Return to Human authority only when:

- a genuinely new material architecture choice appears;
- purpose/priority/scope would change;
- owner-reserved factual authority is missing;
- the admitted scope cannot contain the discovered consequence;
- Human consequential-use/publication decision is required.

A resource/tool limitation is surfaced as an action-local fact and does not automatically create a Human planning decision.

## 7. Anti-meta-loop rule

Anti-regression analysis must not become a permanent prerequisite to movement.

When a slice has:

```text
sufficient problem/evidence basis
+ solution-independent required effect
+ settled material design choices
+ resolved dependencies for its next activity
+ acceptance/verification defined
+ correct authority
```

then it must be declared ready for that activity even if unrelated historical questions remain.

New details are routed as follows:

- fits existing Requirement/design → update Issue/acceptance and continue;
- materially changes architecture → re-enter targeted design/ADR;
- historical context only → retain as evidence, keep out of default context;
- genuinely new Failure Family → reopen root-cause/Requirements work.

## 8. Activity-relative readiness for the current bugwave

At this design stage:

- #245 — coverage evidence exists; managed representation depends on #246/#251.
- #246 — **design complete; implementation awaits D-016**.
- #247 — **design complete; implementation awaits D-016**.
- #248 — inventory complete; final accepted/proposed ADR material enters the Human decision surface rather than being silently accepted.
- #249 — **this readiness/decision contract is design complete**.
- #250 — design follows stable semantics; implementation awaits D-016.
- #251 — migration representation/plan must be closed before implementation admission.
- #252 — candidate can be tested without activation; activation disposition must be explicit.
- #253 — orthogonal Generic-Fit; does not block EKCP unless its result changes shared architecture.

No global label should hide these differences.

## 9. Future D-016 decision readiness criteria

The EKCP change is ready to be presented for a Human D-016 decision only when all of the following are true:

- material finding coverage is accounted for at the current evidence state;
- current/configuration/reference semantics are fixed;
- role/context/applicability semantics are fixed;
- selected physical information representation and migration approach are fixed enough that the implementer will not invent material architecture;
- deterministic assurance/whole-return contract is fixed;
- accepted vs proposed ADRs are clear;
- implementation sequence and rollback are bounded;
- residuals F10/F17 and any newly found material residual are explicit;
- the Human brief can be generated from this state without audit genealogy.

## 10. Decision outcomes

### ADMIT

Authorizes only the exact material implementation programme named in the brief, under its non-goals and accepted/proposed ADR set. Routine implementation choices that preserve those semantics need no new Human loop.

### REFINE

Human names a material issue; design re-enters only the affected surface plus dependents.

### DEFER

Preserves the design/evidence without implementation. It does not make the proposal current architecture.

### REJECT

Rejects the proposed architecture/change. Underlying findings/Requirements remain evidence for a replacement response unless the rejection also explicitly re-dispositions them.

## 11. Readiness disposition

**#249 design is complete.**

The Human does not need to do anything now. A real D-016 decision should only be requested after #250/#251 and the prompt/orthogonal dispositions have been reconciled into a final implementation-ready brief.