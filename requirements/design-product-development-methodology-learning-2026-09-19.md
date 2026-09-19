# Learning — design / project-development methodology weakness — 2026-09-19

Status: **SYSTEM LEARNING / CROSS-PROJECT EVIDENCE ONLY.**  
Not METHOD, Project priority, implementation admission or a new #225 branch.

## Finding

The recent maturity/transparency failure exposed a broader weakness than Human-intent classification alone:

> The system is comparatively strong at governance, evidence/authority boundaries, traceability, reconciliation and cleanup, but weaker at the **methodical discovery, framing and design of the right product/research-system change**.

In practice this allowed a sequence of locally reasonable but globally wrong reframings:
- Human symptom feedback;
- premature reinterpretation of the problem;
- premature solution framing;
- branch growth;
- later governance-driven cleanup.

The problem was not that safeguards were absent. The problem was that **design reasoning before commitment was too weak**.

## What this means

For future system/product work, Human input must be treated as research evidence before it is treated as design authority.

The reasoning surface should distinguish:
- observed Human statement/behavior;
- underlying need or pain;
- symptom versus root problem;
- constraint/quality expectation;
- current governing objective;
- assumptions/hypotheses;
- alternative problem framings;
- alternative solution concepts;
- evidence that discriminates among them;
- validated learning;
- actual Human decision/authority.

This is not a new canonical taxonomy. It is a reminder of the distinctions a competent design process must preserve.

## Cross-repository confirmation

Fresh audit of `esany/Wissensarbeit` found:
- lifecycle and competence catalogs already mention discovery, problem framing, experiment design, requirements, design and learning;
- but the operational methodology connecting these concepts is substantially thinner than the repository's governance/assurance machinery;
- there is no equally explicit current method for user research, need synthesis, symptom/root-cause distinction, design-space exploration, concept/prototype testing and learning-driven iteration.

Generic audit evidence is persisted in:

`esany/Wissensarbeit/project/audits/WA-AUDIT-2026-09-19-DESIGN-PROJECT-DEVELOPMENT-METHOD-DELTA.md`

## Generic-Fit disposition

This does **not** currently justify:
- a new paleo-type METHOD;
- a new #225 subprogramme;
- a new generic Building Block;
- a fixed design framework;
- automatic product decisions.

It is evidence that future generic system development should evaluate whether the existing `Wissensarbeit` blocks for bootstrap/context/research/integration/requirements/design/assurance/learning need stronger, evidence-based design methodology.

## Practical learning for current work

When Human feedback arrives during a valid workstream:

1. preserve the repo-backed objective;
2. determine whether the feedback exposes a symptom, need, constraint, or explicit requested change;
3. do not jump directly from symptom to solution;
4. if materially ambiguous, ask what decision/meaning the Human intends;
5. correct local execution failures without replacing the higher-level product;
6. return to the valid cursor unless purpose/priority/scope was actually changed.

This extends, but does not replace, the 2026-09-18 Human-feedback intent learning.
