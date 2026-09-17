# Human need → scholarly outcome continuity — cross-project problem frame (2026-09-17)

Status: **non-normative problem frame / requirements-analysis input. Not METHOD, not a Requirement owner, not implementation admission, not Project priority, and not authority to create a new workflow layer.**

## Why this problem frame exists

The Reg. Ii 5 pilot exposed a failure mode that can survive even when many local safeguards are correct: the system may preserve evidence, authority, restartability and process integrity while the Human Owner's stable practical research need remains unmet for too long.

Project-local evidence is preserved in:

`projects/ega-reg-ii-5-knau/research/human-need-to-outcome-control-gap-2026-09-17.md`

Related pilot learnings include L026–L029 and the post-#166 routing regression fixture. This file does not promote those project-specific findings into generic METHOD. It preserves a cross-project question that later projects can test.

## Human-Owner role assumption

The target user may be neither a domain specialist nor a software/research-infrastructure engineer. The system therefore cannot treat the Human Owner as the routine solver of questions such as:

- which scholarly maturity transition is technically/factually next;
- which discipline should lead a source-reading problem;
- which deterministic validator or representation is appropriate;
- which internal workflow step is required to achieve a stated scholarly output;
- whether a domain uncertainty requires specialist escalation.

The Human Owner should control non-derivable purpose, priority, scope, rights/authority facts, consequential use/publication and material research-system admission. Specialists/AI/software must prepare the rest of the decision surface at the appropriate level.

## Candidate quality principle under test

A mature generic system should preserve a traceable control chain:

```text
Human need / intended scholarly outcome
→ owner-authorized Project purpose and scope
→ current canonical evidence / maturity state
→ unmet scholarly and system requirements
→ smallest appropriate next work
→ deterministic execution/validation where possible
→ AI-assisted non-deterministic scholarly reasoning where needed
→ specialist validation where consequence requires it
→ usable scholarly outcome
```

This is a **problem-frame hypothesis**, not an admitted universal workflow.

## Failure condition to observe across projects

The problem recurs when all or most of the following are true:

1. a stable owner-authorized scholarly outcome exists;
2. the relevant source/work scope is sufficiently bounded for ordinary research progress;
3. local safeguards correctly prevent unsupported claims or unauthorized scope changes;
4. nevertheless the system repeatedly stops, re-routes into support/meta work, or asks the non-specialist owner to choose technical/domain steps that should be derivable from the intended outcome + current maturity/evidence state;
5. usable scholarly output is delayed without a corresponding unresolved evidential, authority or specialist-validation reason.

A legitimate evidence ceiling, unavailable required evidence, unresolved owner decision or specialist escalation is **not** this failure. The issue is unnecessary loss of outcome continuity.

## Quality dimensions that must remain simultaneous

Do not collapse overall quality into process correctness alone. A candidate generic solution must preserve all of these together:

- **scholarly outcome quality** — scientifically usable result appropriate to the source/problem;
- **epistemic reliability** — evidence before plausibility, uncertainty preserved, claim layers separated;
- **current best practice / State of the Art** — relevant disciplinary and technical expertise activated at the level warranted by consequence;
- **human usability** — a non-specialist owner is not required to substitute for missing expert synthesis or engineering design;
- **auditability / restartability** — result and continuation state reconstructable without old chat;
- **efficiency / lean delivery** — no unnecessary ceremony, infrastructure or repeated rechecking;
- **AI independence** — stable semantics/state/control progressively migrate to deterministic owners when they can be represented safely;
- **genericity** — one pilot/source type must not define the universal architecture.

A system that maximizes one dimension while materially degrading another has not yet met the combined need.

## Automation allocation question

For every recurring step needed to turn an authorized scholarly need into a result, test:

- Is the meaning stable enough to encode deterministically?
- Can current state or the next admissible transition be resolved mechanically from canonical owners?
- Can a regression test prevent a demonstrated recurrence?
- Does the step genuinely require AI interpretation/synthesis?
- Does it require qualified specialist judgement?
- Is it a non-derivable Human-Owner decision?

Where deterministic software can faithfully replace model memory, prompt discipline or repeated AI inference, prefer the deterministic mechanism. Do not automate scholarly judgement by forcing unstable semantics into code.

## Relation to gates

Research maturity gates are candidate inputs to this control chain, not mere reporting labels and not priority selectors by themselves.

A later generic design should test whether, given:

- an owner-authorized desired outcome,
- an owner-authorized scope,
- and a current gate/evidence state,

the system can derive the **unmet requirements** and appropriate bounded work without asking the Human Owner to translate the desired outcome into specialist gate jargon or implementation steps.

This must preserve the rule that gates do not invent scope or priority.

## Lean + agile interpretation

`Lean` does not mean lower quality. `State of the art` does not mean maximal machinery.

The intended combination is:

> highest appropriate scholarly/technical quality for the consequence, delivered through the smallest mechanism that preserves the required evidence, semantics, auditability, human usability and future adaptability.

Incremental implementation should be driven by demonstrated failure/need, tested on real fixtures, and stopped when the smallest intervention satisfies the frozen requirement.

## Generic-Fit protocol

This frame should be carried into materially different future manuscript/source projects as an observation question, not a mandatory workflow.

Evidence for promotion strengthens if multiple projects show the same failure independent of Reg. Ii 5 specifics. Evidence against promotion strengthens if existing owners/gates already produce reliable outcome continuity once Project purpose/scope are adequately represented.

Before any normative METHOD or architectural consequence:

1. compare at least one materially different manuscript/source fixture;
2. identify the exact recurring semantic/control failure;
3. distinguish missing canonical purpose/scope from missing execution derivation;
4. test the smallest possible intervention;
5. prefer deterministic enforcement if the recurring rule is stable and safely formalizable;
6. preserve AI/specialist/Human boundaries;
7. PASS → STOP rather than expanding architecture speculatively.

## Current disposition

**Retain and test across projects.**

No new generic METHOD, workflow engine, candidate-object schema, orchestration layer or automatic priority mechanism is authorized by this file.

The practical reason to preserve the frame now is restartability: future capable contexts and future projects should be able to discover that reliable support is judged not only by absence of epistemic/process errors, but by whether the system can convert an owner-authorized scholarly need into a high-quality usable result without hidden dependence on one chat/model or on the Human Owner acting as substitute expert.
