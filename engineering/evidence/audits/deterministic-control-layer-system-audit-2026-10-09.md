# System audit — deterministic control layer and failure-family roots

Status: ONLINE SYSTEM AUDIT / recommendation and implementation admission boundary  
Repository: `esany/paleo-type`  
Baseline: `main@9a9824028b5eeb819b6e1a2f1a94719adf9b826c`  
Audit date: 2026-10-09  
Scope: current Issue reconciliation, historical requirements, execution guardrails, provenance/semantic boundaries, Issue lifecycle and the recurring local-first / false-PASS / context-leakage patterns.

## 1. Executive finding

The repository already contains a coherent set of authority, evidence, workflow, provenance and GitHub-first requirements. PR #322 and the subsequent reconciliation packet materially improved the written control surface.

The system is not yet fully closed-loop deterministic.

The remaining systemic gap is not primarily a missing instruction. It is the missing enforceable boundary between:

1. an AI proposal or interpretation;
2. an authorized state transition;
3. a repository mutation;
4. an accepted result.

Today, several of these are well specified in prose and regression expectations, but the runtime path can still produce a locally coherent result that is not a valid online, owner-authorized, evidence-bounded system result. The recurring symptoms therefore reappear as new comments, repeated audits and apparently unfinished Issues.

The smallest adequate correction is a fail-closed control layer around consequential actions. It should extend existing owners and CI rather than create a new workflow engine, ontology or second authority store.

## 2. Evidence base and historical requirements

This audit was derived from the current online repository, not from local files or chat reconstruction:

- `GOVERNING_OBJECTIVE.md`
- `AGENTS.md`
- `methodology/workflow.md`
- `methodology/maintenance.md`
- `DECISIONS.md`
- `engineering/evidence/audits/open-issue-reconciliation-2026-10-09.md`
- the current open Issue inventory (31 Issues after #320 was closed)
- `esany/Wissensarbeit/system/authority.json`
- `esany/Wissensarbeit/system/reconciliation.json`
- `esany/Wissensarbeit/system/material_state.json`
- `esany/Wissensarbeit/project/execution_state.json`

The historical requirements converge on the following stable obligations:

| Requirement | Existing owner/intent | Audit assessment |
|---|---|---|
| Human controls non-derivable purpose, meaning, priority and material risk | Wissensarbeit authority model; paleo governance | Correct boundary; needs executable mutation gate |
| AI may inspect, research, classify, structure, validate and perform bounded reversible work | Wissensarbeit authority model | Correct; needs explicit allowed-action/transition input |
| Material state must be persisted before continuity boundaries | material-state model | Correct; needs automated completeness check |
| All materially affected canonical surfaces must reconcile | reconciliation model | Correct; needs machine-checkable affected-surface manifest |
| Technical PASS is not scholarly acceptance | workflow, Issues, maintenance | Correct; needs anti-laundering assertions in acceptance paths |
| Online GitHub is canonical for repository work | `AGENTS.md`, workflow | Correct; needs runtime/harness enforcement, not only agent instruction |
| Context/collection is not content/priority/Project identity | workflow, source/project rules, current Nr. 632 correction | Correct; needs typed-field and negative regression checks |
| Open Issue comments are provenance, not durable current state | reconciliation packet | Correct; needs finite disposition and closure/rollover gate |

## 3. Root causes, manifestations and feedback loops

### Root A — semantic type leakage across boundaries

The Wolkenburg/Nr. 632 error is a concrete instance of a general type failure:

- collection/fonds/Überlieferung context is treated as if it were content identity;
- source/file identity is treated as if it were Project purpose or priority;
- structural relation is treated as if it were textual dependence;
- technical labels are treated as if they were scholarly claims.

The immediate manifestation was the wrong `Wolkenburg` assignment. The deeper cause is not the spelling of that label. It is that the system permits a context-bearing value to flow into a field with a different semantic owner without a hard rejection.

Required invariant:

> A collection/holding/context value may explain provenance or location, but cannot populate content identity, Project purpose, research function or NEXT ACTION unless an owning contract explicitly authorizes that mapping and evidence supports it.

This must be represented as a typed cross-field invariant, with a negative fixture for the Nr. 632/Wolkenburg distinction. Prose alone is insufficient.

### Root B — state laundering between technical and scholarly layers

The repository explicitly warns that local PASS, CI PASS, package existence, merge or Issue closure do not establish productive, scholarly or whole-system acceptance. The audit shows that the warning is necessary because the system repeatedly approaches this invalid conversion.

Typical chain:

`local execution PASS → technical confidence → compressed report → apparent closure → residual remains in comments`

The symptom is an Issue that is “worked on” but never genuinely closed. The root is the absence of a mandatory acceptance tuple that names:

- the exact property tested;
- the canonical owner;
- evidence reference;
- claim ceiling;
- remaining unmet condition;
- allowed disposition.

A technical result must be unable to satisfy a scholarly acceptance field by shape alone.

### Root C — provenance collapse

The current Issues identify recurring confusion between:

- source-derived fact;
- AI-derived interpretation/structure;
- unresolved or unavailable evidence.

When these are rendered in one undifferentiated narrative, the system can accidentally promote an AI derivation or an unresolved gap into apparent source truth.

Required invariant:

> Every material claim carries provenance class, evidence reference, status and claim ceiling; a derived value cannot overwrite a source-derived value without an explicit owner-authorized revision event.

W3C PROV is useful as a conceptual model here, but the repository should adopt only the minimum local representation required for traceability.

### Root D — execution-route non-enforcement

The GitHub-first rule is now explicit and strong. However, an agent instruction is not itself a technical barrier. A runtime can still select a local mirror, a worktree or a shell route before the instruction is interpreted or can silently treat a local result as canonical.

Therefore the repository can test the expected proof shape, but it cannot by itself guarantee the connector was used. The hard guarantee must exist at the execution harness/connector boundary:

- repository mutations are exposed through the authorized connector only;
- local repository access is denied or treated as non-authoritative;
- a consequential action without a remote base/head/commit proof is rejected;
- connector failure fails closed rather than routing to local fallback.

This is the most important boundary that remains outside `AGENTS.md`.

### Root E — Issue lifecycle as narrative accumulation

Open Issues currently serve as history, routing and acceptance surface at once. Repeated comments then become a substitute for a current state machine.

Symptoms:

- comments grow while the actual unmet condition remains ambiguous;
- technical work is repeated because the current owner/next evidence is not a single machine-readable state;
- closure feels unsafe because “done” means different things to different layers.

The existing reconciliation packet is a substantial improvement: one disposition and one unmet condition per Issue. The next deterministic step is to validate a finite disposition vocabulary and require a terminal evidence-bounded disposition before closure or provenance-preserving rollover.

### Root F — assistance-to-direction drift

Issues #292 and #306 show a distinct failure family: access/support work grows into synthesis, direction or NEXT ACTION without authority.

The root is a missing boundary between:

- information/access support;
- evidence interpretation;
- scholarly direction formation;
- Human-Owner priority/meaning decision.

This cannot be solved by making the assistant more verbose. It needs an action contract that names the permitted stage and rejects output that creates a new scholarly target without authority.

## 4. Systemic network

These are not independent bugs. They form a reinforcing network:

`semantic leakage`
→ wrong object/context mapping  
→ wrong target or evidence scope  
→ technically coherent but semantically invalid work  
→ local PASS / compressed status  
→ Issue remains open  
→ comments become the state store  
→ next context reads narrative rather than typed state  
→ leakage and false minimality recur.

The highest-leverage intervention is therefore at the transition boundary, not at every downstream symptom.

## 5. Assessment of the current approach

### What is already strong

- Clear separation of Human Owner, AI, implementation and scholarly specialist authority.
- Explicit distinction among Project, Source, File, research function, evidence and priority.
- Explicit prohibition of local-first repository work.
- Explicit restartability, remote commit proof and reconciliation requirements.
- Explicit distinction between technical, scholarly and whole-system acceptance.
- Issue reconciliation packet with current dispositions and one unmet condition.
- Useful residual routing for #271, #272, #280, #282, #292, #296, #297, #306, #307 and #308.
- Correct preservation of Wolkenburg as context and Nr. 632 as the independently identified archival unit.

### What is still insufficient

1. Guardrails are distributed across long prose documents and prompt/agent behavior.
2. The current engineering-fitness guard is evidence and regression support, not a universal admission gate.
3. There is no single machine-checkable action/transition contract for consequential mutations.
4. Evidence refs and claim ceilings are not yet mandatory for every material state transition.
5. The Issue disposition model is documented but not yet enforced as a finite-state transition system.
6. The repository cannot alone enforce which external runtime/connector actually performed a mutation.
7. Fresh-context real-use acceptance remains open for the principal behavior families.

Conclusion:

> The present approach is conceptually sound but operationally under-enforced. Adding more prose would increase surface area without closing the loop.

## 6. Best-practice comparison

### GitHub protected branches, rulesets and required checks

GitHub's current guidance supports protected branches/rulesets, required status checks, review/conversation gates and merge queues. This is directly applicable to the final repository admission boundary.

Use:

- required validation for schema, disposition and evidence manifests;
- strict up-to-date checks where stale base state could invalidate evidence;
- required review for material contract changes;
- no bypass for the canonical main branch where feasible.

This is a repository control, not a replacement for semantic or scholarly acceptance.

### Policy-as-code and default deny

OPA's policy-as-code model separates policy decisions from enforcement and documents default-deny/fail-closed behavior as appropriate for safety-sensitive operations. The useful principle is not “install OPA”; it is:

- evaluate a structured action request;
- return explicit allow/deny reasons;
- default to deny when required context, authority or evidence is absent;
- keep enforcement at the caller boundary.

A small JSON/YAML contract plus a repository validator is likely sufficient initially. OPA should remain an option only if the rule set grows beyond a transparent local validator.

### Provenance and traceability

NIST SSDF recommends preserving integrity/provenance data and updating it when components change. W3C PROV models entities, activities and agents involved in producing or influencing an object. SLSA similarly treats provenance as a verifiable link between source, process and resulting artifact.

For this repository, the minimal useful form is:

`source/authority → action → derived result → validation → owner/acceptance`

with immutable remote commit and Issue/Project references. Do not add a general provenance graph until this minimal chain demonstrably fails.

### AI governance and human oversight

NIST AI RMF and its Generative AI Profile emphasize continuous governance, measurement, management, documentation, change control, provenance and appropriately scaled human review. That aligns with the existing Wissensarbeit rule:

- automate routine operational necessity;
- reserve material meaning, purpose, priority, risk and consequences for the Human Owner;
- make uncertainty and claim ceilings visible.

The repository already has the right values; the missing part is executable routing at the point of mutation.

## 7. Recommended target: minimal deterministic control layer

Implement only the following five controls, extending current owners:

### C1. Action admission contract

Before any consequential repository or canonical-state mutation, require a structured request containing:

- action type;
- target repository/path/Issue/Project;
- canonical owner;
- current base commit;
- authorized working branch/PR;
- applicable DOR;
- expected evidence;
- expected affected surfaces;
- claim ceiling;
- STOP criteria;
- implementation-authority flag.

Reject when any required field is missing, stale or contradictory.

### C2. Finite transition validator

Define machine-checkable transitions for:

- Issue disposition;
- evidence status;
- technical acceptance;
- scholarly acceptance;
- whole-system acceptance;
- implementation admission.

No transition may skip a required predecessor. “Comment added” is never a state transition. “Merged” is never scholarly acceptance.

### C3. Evidence/provenance envelope

Every material transition must reference:

- immutable repository/Issue/PR/commit evidence;
- provenance class: source-derived, AI-derived, unresolved, implementation/assurance;
- exact property established;
- claim ceiling;
- owner/review level;
- residual condition.

### C4. Remote-only mutation proof

The execution harness must provide or reject:

- remote base/head/commit identity;
- connector route identity;
- post-mutation remote read-back;
- fresh current-main verification;
- affected-owner reconciliation.

If the connector is unavailable, the action stops. Local work may be exploratory but cannot become canonical state or a claimed PASS.

### C5. Acceptance and closure gate

An Issue can close only if:

- its current disposition is terminal;
- all required evidence refs resolve remotely;
- no unmet condition remains;
- affected canonical owners are reconciled;
- the closure claim is scoped to the Issue's owner;
- residuals are either routed to an existing owner or explicitly rolled into a new provenance-linked Issue.

## 8. Deterministic versus judgement boundary

### Deterministic and suitable for code/CI

- reference exists and resolves;
- repository/path/branch/commit are current;
- allowed transition exists;
- required fields are present;
- schema and vocabulary are valid;
- context value is not used as content/priority without an explicit mapping;
- provenance class is present;
- source-derived and AI-derived fields are not silently conflated;
- one current unmet condition maximum;
- closure evidence is complete;
- main branch protection/checks pass.

### Human or qualified specialist judgement

- what a documentary object means;
- whether a relation is textual dependence;
- palaeographic/philological interpretation;
- research purpose, priority or material scope;
- material architecture admission under D-016;
- whether evidence is sufficient for scholarly acceptance;
- consequential publication/use/risk decisions.

The validator must block unsupported promotion; it must not manufacture a scholarly answer.

## 9. Implementation admission and DoD

This audit is a recommendation, not an implementation admission for a material new control contract. The next implementation can be admitted only with a bounded Issue/decision owner and the following DoD:

1. A single action-admission schema exists under the current engineering contract owner.
2. The validator rejects missing/stale owner, base commit, evidence, transition and claim-ceiling fields.
3. Negative tests cover:
   - Wolkenburg context incorrectly assigned to Nr. 632 content;
   - local PASS presented as scholarly/whole-system acceptance;
   - AI-derived value presented as source-derived;
   - access/support task manufacturing NEXT ACTION;
   - connector failure falling back to local mutation;
   - closure with an unmet condition.
4. Positive tests demonstrate legitimate lean simplification still passes.
5. GitHub CI executes the validator and the required check is protected on main.
6. A remote-only fresh-context trial proves the control behaves correctly in a new session.
7. The implementation records exact remote commit and affected-owner reconciliation.
8. Human Owner reviews only the material contract/architecture decision, not routine test or evidence maintenance.
9. Existing Issues #271/#272/#280/#282/#292/#296/#297/#306/#307/#308 receive evidence-bounded updates; no comment-only “progress” is accepted as closure.
10. The final audit returns to #272 and records what is solved, what remains and why.

## 10. Explicit non-goals

Do not:

- create a second workflow engine;
- create a universal ontology or glossary;
- move canonical truth into chat, Issues or generated reports;
- close scholarly Issues because technical CI is green;
- infer content or priority from collection context;
- make the Human operate routine connector/tooling work;
- use OPA/SLSA/W3C PROV as branding without a concrete local control;
- broaden this audit into new Project purpose or research priority.

## 11. Decision requested from the owning process

The evidence supports admitting a bounded implementation issue for C1–C5, but does not itself grant material architecture authority.

The next canonical decision should answer only:

> May the repository and its authorized execution harness introduce the minimal deterministic control layer C1–C5, reusing current owners and without creating a second authority system?

If yes, implementation should begin with C1, C2 and C5 in the repository, while C4 is enforced at the connector/harness boundary and C3 is implemented as the smallest evidence envelope needed by the current Issues.

## 12. Audit conclusion

The system is not suffering from a shortage of intelligence or from a single bad label. It is suffering from a recurrent control failure at semantic and operational boundaries.

The correct repair is:

`typed meaning → admitted action → evidence-bounded transition → remote proof → scoped acceptance`

The existing repository rules provide most of the conceptual model. The next step is to make the high-risk transitions fail closed, prove them with negative fixtures and keep scholarly judgement outside the deterministic layer.

This audit does not close the open acceptance Issues. It creates a durable, bounded basis for the next implementation decision.


## 13. External primary sources consulted

- [GitHub — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches): required status checks, reviews, conversation resolution and merge-queue controls.
- [Open Policy Agent — documentation](https://www.openpolicyagent.org/docs): policy-as-code, structured decisions and separation of policy decision from enforcement.
- [Open Policy Agent — agent tool calling](https://www.openpolicyagent.org/docs/agent-tool-calling): deny-reason decisions at the tool boundary and explicit enforcement behavior.
- [NIST SP 800-218, SSDF](https://csrc.nist.gov/pubs/sp/800/218/final): change accountability, integrity and provenance preservation.
- [W3C PROV Model Primer](https://www.w3.org/TR/prov-primer/): provenance as entities, activities and agents involved in producing or influencing an object.
- [SLSA — security levels](https://slsa.dev/spec/v1.0/levels): verifiable build/source/process provenance as a supply-chain control.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf): continuous governance, documentation, provenance, change control and scaled human oversight.

These sources inform the control principles only. They do not override the repository's governing objective, canonical owners, D-016 admission boundary or scholarly acceptance rules.
