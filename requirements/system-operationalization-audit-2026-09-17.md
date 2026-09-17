# System operationalization audit — 2026-09-17

Status: **cross-project requirements / system audit. Not METHOD, not Project priority, not implementation admission, and not authority to create a new workflow layer.**

## 1. Audit question

The Human Owner reports a repeated failure: the repository contains extensive methodological, disciplinary, governance, quality and system-design reasoning, yet the practical research experience repeatedly falls back to local fixes, support loops, scope questions and chat-dependent interpretation. The system therefore feels unreliable for a non-specialist owner with a larger backlog of manuscripts.

This audit asks:

> Which parts of the intended holistic research system are already conceptually defined, normatively binding, deterministically executable and actually demonstrated in practice — and where does the operational chain still break?

The audit is intentionally system-level. It does not treat a successful local regression fix as evidence that the larger Human-need → scholarly-outcome problem is solved.

## 2. Governing target is already explicit

`GOVERNING_OBJECTIVE.md` already defines the correct top-level target:

- scholarly result and source understanding are the product;
- the work is a transdisciplinary research problem;
- current authoritative disciplinary practice must be used where consequential;
- the Human Owner is non-specialist and must not substitute for specialist adjudication;
- the system must remain human-auditable;
- technical structure must be lean/subsidiary;
- consequential durable state must be canonical and restartable.

`AGENTS.md` reinforces the same mission operationally: reliable usable scholarly results with minimal tooling overhead, expert methods activated as needed, deterministic validation where appropriate, repository-first persistence, and direct research outcome before infrastructure.

Therefore the repeated pilot failure is **not primarily a missing mission statement**.

## 3. The scholarly method and maturity model are also already explicit

`methodology/historical-source-workflow.md` provides an end-to-end S1–S9 scholarly method from source/provenance through diplomatic transcription, palaeographic/philological analysis, comparison, normalization/identification, source criticism, critical consolidation and edition.

`methodology/research-gates.md` separately defines scope-bound G1–G6 maturity states and explicitly distinguishes:

- work-package completion;
- representation completeness;
- internal analysis completeness at the evidence level;
- gate attainment;
- edition production.

For the current Reg. Ii 5 locus 61v–63r, Project status records G2–G4 as reached and G5/G6 as not reached. The generic system therefore already has a vocabulary for the difference between a working representation and a consolidated/validated scholarly text.

The recurring practical failure is **not primarily absence of scholarly process modelling**.

## 4. Quality, role and authority safeguards are comparatively mature

The repository contains strong explicit safeguards for:

- evidence before plausibility;
- observation/reading/normalization/identification/interpretation separation;
- uncertainty as a valid result;
- independent evidence vs repeated AI output;
- Source/File/Project/use/priority separation;
- Human Owner vs specialist vs AI vs Dev authority;
- resource state vs task/roadmap authority;
- semantic-boundary preservation across scholarly/technical domains;
- support/no-progress loop control;
- Domain→Dev and Dev→Domain handoff;
- canonical ownership and restartability;
- cross-role assurance separation;
- adversarial scholarly spot-checking;
- Generic-Fit and failure-derived learning.

These protections are not merely discussed: multiple are encoded in deterministic validators, fixtures and regression tests.

## 5. Deterministic implementation exists — but is concentrated in the control/support plane

The repository currently contains executable tooling for:

- Source/File/Project/use contract validation and structural resolution (`tools/source_contract.py`);
- deterministic Source/File intake inspection (`tools/source_intake.py`);
- rebuildable Project context generation (`tools/project_context.py`);
- Reg. Ii 5 evidence/retrieval/benchmark support helpers.

The tests directory is correspondingly rich in:

- Source contract and assurance checks;
- Project-context checks;
- Corpus-only routing checks;
- governance ownership checks;
- recovery/restartability checks;
- Source-critical acceptance/provenance checks;
- Reg. Ii 5 evidence/retrieval/packet regressions.

This is real operationalization. It protects identity, provenance, authority boundaries, routing, persistence, recovery and specific demonstrated failure classes.

However, `tools/project_context.py` explicitly refuses to infer scholarly `NEXT ACTION`, research function, Project purpose, evidence access, witness attribution or scholarly interpretation not already represented by canonical owners. This is correct as a safeguard, but it exposes the central asymmetry: the deterministic system assembles and protects state; it does not yet convert an owner-authorized scholarly outcome plus current maturity/evidence into the bounded work required to reach that outcome.

## 6. The repository itself already diagnosed this asymmetry

`requirements/research-system-problem-landscape-2026-09-14.md` explicitly distinguishes conceptual maturity from operational maturity and records the asymmetry:

- strong execution, assurance, persistence and restartability once a task exists;
- weaker research framing / question selection / transdisciplinary activation before and between tasks;
- Human-Owner authority is strong, but the decision surface is less mature;
- Domain↔Dev translation is mature, but does not solve research-framing quality;
- support controls are strong, but can protect a scientifically weak or incomplete trajectory;
- local high-maturity mechanisms do not imply the larger system problem is solved.

Its R0–R4 maturity vocabulary is especially revealing: many local mechanisms are R3–R4, while system-level research framing and competency integration remain R1–R2.

The current Human-need → outcome finding extends that asymmetry beyond pre-priority question formation: even after the user need and target material are understood, the system can lose outcome continuity because local guardrails do not compose into a reliable end-to-end execution path.

## 7. A coherent holistic architecture has already been designed conceptually

`requirements/executable-transdisciplinary-research-system-concept-idea-2026-09-14.md` already describes most of the system now being requested:

- generic transdisciplinary research system;
- claim/question-relative competence activation;
- Human Owner controls purpose/priority without becoming substitute specialist or software architect;
- AI used for genuinely non-deterministic synthesis/interpretation;
- deterministic software owns structured state, provenance, dependency/authority resolution, admissible state transitions, context assembly, consistency and regression where semantics are stable;
- less hand-maintained state prose;
- explicit Human / AI / specialist / deterministic allocation;
- HCI/HITL and cognitive ergonomics;
- requirements engineering and scholarly-computational translation;
- verification engineering;
- cross-fixture validation;
- success criterion that scientific expressiveness and auditability increase while less state depends on AI remembering prose rules.

This is not a missing-concept problem. The concept is explicitly marked non-normative and not implementation-admitted.

## 8. Main audit finding: the integration layer is not operational

The repository currently has many strong layers:

```text
Governing Objective              strong / normative
Domain & system requirements     extensive
Scholarly S1–S9 method           strong / normative
G1–G6 maturity model             strong / normative
Authority / epistemic guards     strong / normative
Canonical state model            substantial / partly executable
Source/Project validators         substantial / executable
Restart/context generation       substantial / executable
Failure-specific regressions     substantial / executable
```

But the following control chain is not yet a first-class operational mechanism:

```text
Human need / desired scholarly outcome
→ owner-authorized purpose + bounded scope
→ current evidence + maturity state
→ unmet requirements for that desired outcome
→ question-/claim-relative competence activation
→ smallest coherent scholarly/technical work slice
→ deterministic execution/validation where possible
→ AI reasoning only where non-deterministic
→ specialist escalation where consequence requires it
→ consolidated usable scholarly result
→ return to the same higher-level outcome cursor after local repair
```

Today, much of this chain is reconstructed by the current AI from prose, Project state and conversation context. When the model overweights one local rule, the system can become locally compliant but globally ineffective.

That is the principal operationalization gap.

## 9. Why repeated local fixes do not solve the problem

The pilot has repeatedly followed a pattern like:

```text
systemic failure observed
→ one concrete failure mode isolated
→ smallest local repair
→ deterministic or fresh-context PASS
→ local STOP
→ higher-level outcome cursor not mechanically restored
→ next context re-enters from canonical local state
→ another local rule becomes dominant
→ new support/meta correction
```

The local repairs are often valid and should remain. The failure is treating their completion as if it completed or materially advanced the higher-level Human need/system capability.

`maintenance.md` already contains a programme/phase/result-transition reconciliation rule stating that a local `PASS`, `STOP` or closeout does not establish whole-programme completion. In practice, however, no durable programme/outcome control surface currently keeps the manuscript-result trajectory active and mechanically reconnects a finished repair to it.

Thus the repository contains the principle but lacks a sufficiently operational owner/state/mechanism for the end-to-end outcome cursor.

## 10. Human usability failure

The Governing Objective and quality rules state that the Human Owner is a non-specialist and should not become substitute specialist or repository operator.

Nevertheless the pilot repeatedly returns questions such as:

- which gate should be pursued next;
- which scholarly method step is appropriate;
- whether to choose a new locus or consolidate the existing one;
- which technical/support route should be taken;
- whether a residual uncertainty deserves another research programme.

Some of these are genuine owner decisions. Many are not: once the owner-authorized scholarly outcome and scope are clear, they should be derived or prepared by the system from maturity, evidence and disciplinary requirements.

The system therefore has **authority boundaries without an equally mature owner decision surface / expert delegation mechanism**.

## 11. Lean/agile failure mode

The project currently often applies `smallest intervention` correctly at the local defect level but not as a vertical system slice.

Healthy lean/agile system development should mean:

```text
stable end-to-end outcome and quality attributes
→ small vertical slice through all required layers
→ real manuscript result
→ inspect/falsify
→ repair smallest demonstrated systemic bottleneck
→ resume same slice
→ stop when user-visible outcome and quality criteria are met
```

The observed pattern instead often becomes horizontal/local optimization:

```text
authority defect → fix authority
resource defect → fix resource semantics
restart defect → fix restartability
routing defect → fix routing
```

Each improvement is useful, but the integrated scholarly outcome remains unfinished. This is local optimization without durable system-level flow control.

## 12. The current pilot is therefore an end-to-end system acceptance fixture

For Reg. Ii 5 fol. 61v–63r, the appropriate system-level question is not whether one more local mechanism can PASS.

It is:

> Can `paleo-type` take the already bounded real manuscript locus, apply the appropriate current scholarly and technical best practice, preserve all required evidence/uncertainty/authority boundaries, and produce a scientifically usable diplomatic/consolidated text state without requiring the non-specialist owner to design the method or system?

This end-to-end fixture must remain distinct from any single G2/G3/G4/G5 or technical regression claim. A local PASS is evidence about one component only.

## 13. Operationalization gap matrix

| Capability | Concept / requirement | Normative owner | Executable support | Demonstrated practice | Audit |
|---|---|---|---|---|---|
| Source/File identity + provenance | strong | strong | strong | strong | operational |
| Project/Source/use separation | strong | strong | strong | strong after corrections | operational with history of failures |
| Evidence/claim-layer discipline | strong | strong | partial deterministic + scholarly process | substantially demonstrated | operational but AI-dependent in judgement |
| Restartability / canonical context | strong | strong | strong | strong | operational |
| Resource/task authority separation | strong | strong | regression-protected | demonstrated | operational for known failure |
| Support/no-progress control | strong | strong | partly procedural/tests | demonstrated but recurrent | partial |
| G1–G6 maturity semantics | strong | strong | little direct state derivation | manually interpreted | **under-operationalized** |
| S1–S9 competency activation | strong | strong | no generic router/resolver | AI reconstructs | **under-operationalized** |
| Human need → desired scholarly outcome | now explicit in pilot/problem frame | no canonical structured system owner | none | chat-/AI-mediated | **major gap** |
| Outcome + scope + gate → unmet requirements | conceptually implied | distributed | none generic | AI reasoning | **major gap** |
| unmet requirements → next bounded work | conceptually implied | distributed authority | none generic | AI reasoning / owner questions | **major gap** |
| question-relative competence activation | strong concept | partial METHOD | none generic | inconsistent | **major gap** |
| specialist escalation preparation | clear principle | quality/gates | no generic mechanism | case-by-case | partial |
| AI/deterministic allocation | strong concept | not fully normative | isolated tools only | inconsistent | **major gap** |
| return from local repair to higher-level outcome cursor | rule exists conceptually | workflow/maintenance fragments | no explicit executable owner | repeatedly failed | **major gap** |
| cross-project portability | required | conceptual | not demonstrated | Reg. Ii 5 dominated | open |

## 14. Root-level interpretation

The strongest current explanation is not that the repository lacks methods, requirements or safeguards. It is that the repository has **a rich set of individually mature components without an operational system integration/control plane connecting the Human need to the scholarly outcome**.

The AI therefore acts as the de facto integration layer.

That creates exactly the dependency the system is supposed to reduce:

- a good model may reconstruct the intended holistic architecture;
- another context may over-weight a local guardrail;
- the repository can deterministically reject many bad transitions but cannot yet deterministically assemble the correct end-to-end progression;
- repeated prose can improve guidance but does not remove the integration dependency.

This is why the same systemic discussion can recur despite many correct local fixes.

## 15. Consequence for system development

The next system-development question should therefore not be another isolated failure rule.

It should be a requirements/concept consolidation around the already-demonstrated missing capability:

> **How does an owner-authorized scholarly need/outcome remain a durable higher-level control objective through Project scope, maturity/gates, scholarly method, local support/repair, AI reasoning, deterministic validation and specialist escalation until the usable scholarly result is reached or a real evidence/authority ceiling is exposed?**

This should reuse existing owners and concepts rather than invent a parallel architecture.

Any material implementation still requires D-016 admission. The audit itself does not admit a specific design.

## 16. Acceptance criteria for a future operational solution

A future integrated mechanism should be falsifiable on real source work. At minimum it should demonstrate that:

1. the Human Owner can state the desired scholarly outcome in ordinary domain-facing language without knowing internal gate/workflow jargon;
2. the system can resolve the canonical Project/scope/evidence/maturity state;
3. it can derive and explain the unmet requirements for that desired outcome without inventing new scope/priority;
4. it can allocate each required step to deterministic software, AI scholarly reasoning, specialist judgement or genuine Human-Owner decision;
5. stable derivations and invariants do not depend on model memory;
6. local support/repair returns to the same higher-level outcome cursor unless authority/evidence actually invalidates it;
7. local PASS/STOP states cannot masquerade as whole-outcome completion;
8. a fresh capable context can continue without the originating chat;
9. the owner is not forced to adjudicate specialist or software-engineering details;
10. the real manuscript fixture reaches the intended usable scholarly result at the appropriate State-of-the-Art quality level with proportionate overhead;
11. the same control model survives at least one materially different manuscript/source project without importing Reg. Ii 5-specific ontology;
12. deterministic mechanisms replace AI inference wherever the semantics have proved stable and safely formalizable.

## 17. Current disposition

**Audit result: SYSTEMIC OPERATIONALIZATION GAP CONFIRMED.**

The repository already contains substantial holistic analysis, method, requirements and architectural concepts. The main deficiency is not further problem discovery in the abstract. It is the lack of an admitted and executable integration mechanism that makes those layers work together as normal practice.

No claim is made that all missing integration should become one workflow engine or one universal state machine. The required next design step is to consolidate existing requirements/owners into the smallest coherent end-to-end control model, then test it as a vertical slice on the actual 61v–63r manuscript outcome and at least one materially different fixture.

Until that integration exists, treat successful local fixes as component-level results only and explicitly return to the governing Human need / scholarly outcome after each bounded repair.
