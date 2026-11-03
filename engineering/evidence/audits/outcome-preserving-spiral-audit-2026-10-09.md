# Outcome-preserving spiral audit — roots, manifestations and control requirements

Status: CURRENT SYSTEM AUDIT / D-016 ADMITTED / bounded implementation evidence
Repository: `esany/paleo-type`
Baseline: `main@256f12bc8894df6fefa7bc8e814e10cc755b9cd4`
Audit date: 2026-10-09
Online source: GitHub connector only

## 1. Executive finding

The recurring problem is not a single bad label, prompt or Issue comment. It is a reinforcing failure loop:

```
Human outcome / research need
→ broad coupled problem
→ assistant narrows to an attractive local step
→ local technical progress becomes the working cursor
→ owner/rule existence is treated as evidence of adequacy
→ local PASS or Issue progress is narrated as resolution
→ residual outcome remains open
→ fresh context inherits partial state and repeats the narrowing
→ Human has to recover the original cursor
→ more comments, audits and meta-work accumulate
```

The loop is demonstrated across the repository's existing failure families:

- False Lean and local-PASS substitution (#297, #280);
- context/content leakage (Wolkenburg as collection context versus Nr. 632 as archival unit);
- provenance collapse (#307);
- access/support drifting into scholarly direction (#292, #306);
- closure laundering (#272, #280);
- local-first or unproven execution route;
- productive-runtime and preservation gaps (#271, #282);
- Human-facing machine-state dominance (#308 and the 2026-10-09 audit).

The immediate error is the visible manifestation. The root is **loss of the higher-order outcome across decomposition, execution and acceptance boundaries**.

## 2. What this audit does and does not claim

This audit establishes a cross-family causal pattern and derives control requirements from it.

It does not claim:

- that one new generic workflow engine, state machine or schema is justified;
- that repository CI can guarantee model, connector or external-runtime behavior;
- that documenting a rule makes future use compliant;
- that a local, technical or GitHub PASS establishes scholarly or Human acceptance;
- that Wolkenburg identifies the content of Nr. 632;
- that the assistant can be made absolutely immune to future error.

The realistic target is stronger and narrower: make consequential work unable to silently convert a partial/local result into a whole-system result, and make recurrence produce a visible stop/escalation rather than another round of comments.

## 3. Root causes

### R1 — the implementation cursor displaces the outcome cursor

The assistant sees a tractable code, Issue, prompt or owner task and begins optimizing that slice. The slice is then used to decide what happens next.

This reverses the required order:

```
Human need → domain meaning → complete outcome → bounded work → evidence → acceptance
```

into:

```
available capability → smallest patch → local PASS → status narrative → residual discovered later
```

### R2 — semantic types leak at boundaries

Context, content, provenance, authority, priority, technical state and scholarly meaning are repeatedly exposed to the same untyped narrative channel.

The Wolkenburg/Nr. 632 error is the clearest example:

- Wolkenburg may describe fonds, collection or transmission context;
- Nr. 632 is the independently identified archival unit;
- neither the collection context nor the number alone establishes the content, Project purpose, research priority or scholarly interpretation.

The general failure is a field/value crossing a semantic boundary without an explicit owner and evidence bridge.

### R3 — “an owner exists” is used as a reason to defer a demonstrated failure

Existing owners are necessary for authority, but their existence does not prove operative adequacy. When a fresh use case violates the intended invariant, the result is evidence against current efficacy.

The invalid reasoning is:

```
rule/owner exists → no gap exists → continue locally
```

The required reasoning is:

```
observed outcome failure → identify violated property → test current owner/enforcement
→ repair at the smallest sufficient locus, or open a material decision
```

This prevents “existing-owner-first” from becoming a relativization mechanism.

### R4 — technical assurance is laundered into result assurance

Local tests, CI, a merged PR, a package listing, an Issue comment or a closed child task can be correct while the protected outcome remains unmet.

The recurring laundering step is not necessarily an explicit false statement. It often occurs through compression: the technically easiest state becomes the headline and the residual becomes a footnote or another comment.

### R5 — comments and chat history become the de facto state store

When no current, evidence-bounded result tuple is required, the Issue grows instead of resolving. Each new context must reconstruct:

- what the original outcome was;
- what was actually changed;
- which obligations remain coupled;
- which owner is authoritative;
- what evidence is missing;
- what would constitute closure.

This creates context gravity and makes another local step appear cheaper than a real result review.

### R6 — route and authority are described but not always enforced at the action boundary

The repository rules require GitHub-first work, remote proof and no local fallback. But instructions alone cannot guarantee the runtime route. A connector failure, local mirror or stale context can therefore create a result that looks coherent but is not canonical.

This boundary must be treated as an assurance ceiling unless the harness actually enforces it.

## 4. Manifestations

| Root | Typical manifestation | Why it survives |
|---|---|---|
| R1 | “small fix” or prompt before complete outcome framing | local work is easier to represent than the whole result |
| R2 | collection context presented as content/priority; source fact mixed with derivation | narrative channel lacks enforced semantic separation |
| R3 | “existing owner/rule covers this” after fresh recurrence | normative coverage is mistaken for operative efficacy |
| R4 | CI/PR/Issue/PASS presented as completion | acceptance levels are named but not always composed in the response/action |
| R5 | open Issue receives another analysis instead of finite disposition | comments are available immediately; closure requires evidence synthesis |
| R6 | local result or connector fallback treated as harmless staging | remote authority is not physically established by prose |

## 5. Systemic Wirknetz

Healthy path:

```
Human question or pain
→ domain meaning and protected outcome
→ semantic distinctions and coupled obligations
→ bounded action with authority, DOR and DOD
→ evidence at the correct owner
→ result review against the original outcome
→ explicit residual / acceptance / next action
→ technical traceability as subordinate proof
```

Observed spiral:

```
Human question
→ support/tool/Issue decomposition
→ convenient local task
→ local PASS or status signal
→ lower-layer state becomes narrative backbone
→ original meaning is compressed
→ Human corrects or reorients the system
→ new meta-work and comments
→ more context gravity
→ next local task
```

The key reinforcing edge is:

> Every unreturned local success increases the probability that the next context treats the local state as the problem definition.

## 6. Required mechanism: Outcome-Preserving Return Gate

The mechanism is a control contract built on the existing owners and admitted execution-control semantics. It is not a new universal workflow engine, Issue owner or parallel truth store.

Every consequential work block must carry a short **return tuple**:

1. **Protected outcome** — what Human/research/product result must be true.
2. **Semantic scope** — what the object is and is not; explicitly separate context, content, provenance, authority and priority.
3. **Coupled obligations** — which owners, evidence, runtime and acceptance surfaces cannot be dropped.
4. **Authorized action** — inspect, research, bounded reversible work, implementation, mutation or acceptance review.
5. **Definition of Ready** — authority, current remote state, evidence basis and prerequisites.
6. **Definition of Done** — observable result and acceptance owner; not merely code/Issue/CI state.
7. **Residual and return condition** — what remains unresolved and exactly where work returns.
8. **Claim ceiling** — what the evidence does not establish.

The tuple is not a second canonical state store. It is the minimum evidence required to cross an existing action or acceptance boundary.

### Gate A — before decomposition

The assistant must state the protected outcome and the semantic distinctions before proposing a small/lean step.

If either is missing, the work may analyse but may not present a local implementation as the next sufficient action.

### Gate B — before material action

The assistant must classify the action and verify the current authority/owner, remote state, DOR, DOD and stop condition.

A fresh recurrence of a documented failure is not “covered” merely because a rule or owner exists. It is a failed control observation and must be recorded for repair or decision.

### Gate C — after local work

The result must be returned to the protected outcome:

- what changed in the system;
- which coupled obligations were re-tested;
- what evidence supports the claim;
- what remains open;
- which acceptance level was reached;
- what was deliberately not changed.

A local/technical PASS cannot satisfy a whole-system or scholarly acceptance field.

### Gate D — before closure or handoff

Closure is blocked unless the return tuple is complete, the residual has a canonical owner, and a fresh context can recover the same outcome, evidence and return condition.

Issue/PR/CI status is traceability, not closure evidence by itself.

## 7. Hard-stop conditions

The mechanism must stop the consequential action and return a bounded failure when any of these occurs:

- the protected outcome cannot be stated;
- a context value is being promoted into content, authority, Project purpose or priority without an evidence bridge;
- a local/technical/CI/PASS is being used as whole-system acceptance;
- a documented failure recurs and is dismissed because an owner or rule exists;
- a material semantic, architecture, migration or authority choice is being absorbed without its decision boundary;
- remote execution/provenance cannot be proved for repository mutation;
- connector failure is being routed to local staging or later promotion;
- a parent outcome is declared complete while a coupled child obligation remains unresolved;
- the result has no explicit residual, claim ceiling or return condition.

A hard stop is not failure of the user’s work. It is the mechanism preventing the spiral from silently continuing.

## 8. Recurrence response

The response to recurrence is deterministic in direction, not in invented severity numbers:

```
recurrence observed
→ stop the affected transition
→ name the violated property and evidence
→ distinguish normative, enforcement, owner, runtime and model limits
→ repair the smallest sufficient existing locus
→ if material owner/enforcement architecture is required, open D-016 immediately
→ re-run the original vertical fixture
→ only then reconsider closure
```

No recurrence may be converted into “another comment” without a finite disposition:

- fixed and re-tested;
- bounded unresolved with explicit owner and return condition;
- superseded with provenance and reason;
- blocked by named external dependency;
- rejected with evidence and rationale.

## 9. Acceptance envelope

The mechanism itself is not accepted because this document exists. Its evidence envelope must include:

- fresh-context scholarly stage preservation when access fails;
- productive external destination/runtime and preservation acceptance;
- False-Lean/local-PASS fixture across a coupled parent outcome;
- context/content negative fixture for Wolkenburg versus Nr. 632;
- provenance separation fixture;
- Human-facing result explanation where meaning precedes identifiers;
- GitHub-first remote proof and connector-failure stop behavior;
- closure/rollover disposition with one unmet condition.

A green repository check proves only the executed deterministic properties. It does not prove universal future model behavior or scholarly truth.

## 10. Current disposition

D-016 is **ADMITTED** for the exact scope of esany/paleo-type PR #327 and branch `fix/outcome-preserving-spiral-breaker-2026-10-09`, based on explicit Human Owner authorization recorded on 2026-10-27.

The admission authorizes only the existing-owner implementation, deterministic tests and durable evidence for the Outcome-Preserving Return Gate. It does not activate a new architecture and does not authorize merge, Issue closure, scholarly/Human acceptance, Project-priority changes, changes to Nr. 632 identity or Wolkenburg meaning, global implementation enablement, or claims of future model immunity.

The technical carrier is now implemented on the admitted branch. The remaining acceptance residuals are explicit rather than deferred: fresh-context vertical evidence across the affected failure families, external connector enforcement beyond the tested repository path, and the separate acceptance decisions owned by the existing vertical owners.

The critical success criterion is not “the mechanism file exists.” It is:

> A future local success cannot be reported as resolution unless it returns to the protected outcome, preserves semantic type boundaries, names the residual and passes the correct acceptance owner.
