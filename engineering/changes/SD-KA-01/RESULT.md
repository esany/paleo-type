# SD-KA-01 work-package results and whole-system returns

**Status:** `WP1 VERIFIED / WP2 VERIFIED + RETURNED / WP3 VERIFIED + RETURNED / WP4 READY-NEXT / SD-KA-01 ACTIVE`

## WP1 — semantic contracts and in-place managed baseline

### Exact result basis

- Merge: PR [#274](https://github.com/esany/paleo-type/pull/274), merge commit `c66ef075acdde1f592886086403439507d6cc618`.
- Post-merge CI: [source-contract run #502](https://github.com/esany/paleo-type/actions/runs/37239899698), successful on `main` at that exact merge head.
- Deterministic local reproduction at the same head: `python3 tools/engineering.py validate` PASS; full test discovery PASS, 91 tests.
- Validator result: 32 engineering artifacts, 45 findings, 1 coverage account and 55 explicit relations.

### Actual state change

WP1 provides the repository-native `engineering/` semantic/configuration/catalog foundation, admitted-change state, ADR trace surface and deterministic structural validation. The Human Owner's D-016 admission is persisted in the canonical owner-admission record. The accepted engineering baseline remains the existing governance/decision layer; SD-KA-01 remains admitted and active, not silently promoted to accepted current architecture.

### Findings and requirement consequences

- F01–F45 are represented exactly once in the coverage/disposition owners.
- F10 remains an unresolved review-premise-independence residual; F17 remains the unresolved scholarly #225 residual.
- Deferred and controlled dispositions remain explicit; WP1 does not claim that the bugwave is closed.
- P-001–P-012 remain the admitted SD-KA-01 target package. ADR-0001 remains admitted-for-implementation and is not an accepted current baseline.
- No `requirements/` bulk migration occurred. No Project, manuscript or scholarly `NEXT ACTION` state changed.

### Whole-system return

**Changed:** the parent system-development surface no longer requires chronology-only reconstruction of WP1's semantic owners, D-016 admission, F01–F45 coverage or exact verification basis. #244 remains the programme/whole-system owner; the local technical PASS is not programme closure, scholarly acceptance or specialist validation.

**Downstream readiness at WP1 return:** #257/WP2 became the next eligible implementation cursor within the already admitted SD-KA-01 scope.

---

## WP2 — accepted engineering configuration and derived current/query views

### Exact result basis

- Implementation PR: [#278](https://github.com/esany/paleo-type/pull/278).
- Exact PR head: `a33c148e1f1ef213aa39d2b3ae25fa5e08c4b167`.
- PR-head assurance: [source-contract run #526](https://github.com/esany/paleo-type/actions/runs/37325872290), successful on that exact head.
- Merge commit on `main`: `e10a51a56a6db1924d4500698d2dd2be2b222bc4`.
- Exact post-merge assurance: [source-contract run #527](https://github.com/esany/paleo-type/actions/runs/37325991648), successful on that exact `main` head.
- PR review: exact-head writer-context technical/fresh-context self-review recorded on PR #278; explicitly not claimed as independent review.

### Actual state change

WP2 implements the previously designed engineering-currentness slice without creating a second truth clock:

- `engineering/configuration.json` now distinguishes accepted architecture/Requirement baselines, admitted/implemented change state, optional current focus and applicability provenance;
- `tools/engineering.py current` derives a current-first engineering view on demand from canonical configuration/change/catalog owners;
- the query surface can filter managed engineering artifacts without using chronology as semantics;
- explicit absence of active focus is representable and does not manufacture substitute work;
- proposed/admitted artifacts, work metadata, Git recency and CI status cannot by themselves become accepted current architecture;
- transition vocabulary and validation distinguish proposed, admitted, implemented, verified, accepted, no-change and re-entry/rejection/supersession paths;
- the bounded change state now points to the actual managed implementation plan rather than the target-package ADR;
- stale WP1-only CI wording was removed while the existing scoped assurance boundary remains unchanged.

After the merged implementation, the configuration-level SD-KA-01 transition is recorded as `implemented`: repository implementation has occurred, but the broader accepted SD-KA-01 consequence remains `pending`. The accepted architecture and Requirement baselines themselves are unchanged by WP2.

### Adversarial/currentness assurance

The deterministic regression set now exercises at least:

- a newer/proposed artifact cannot win currentness by recency;
- work metadata cannot become an accepted baseline;
- an admitted/proposed ADR cannot become accepted current architecture without the required transition;
- concurrent investigation/change state does not steal an explicitly selected focus;
- explicit absence remains absence rather than inventing a replacement focus;
- invalid applicability provenance and invalid transition state fail validation;
- direct transitions such as proposed→accepted or admitted→accepted are not accepted by the transition contract.

The exact PR-head and post-merge workflows also reran the pre-existing Source/File/Project-use contract, deterministic/governance regressions, fresh-process Project-context compilation and real-data resolver fixture. Their PASS is technical assurance for those checked properties only.

### Fresh-context / reconstruction-cost result

Before WP2, a fresh system-development context still had to manually compose currentness from configuration, bounded change state, #246/#247 design semantics and work/navigation metadata. After WP2, accepted baselines, active change state, explicit focus/absence and applicability provenance are available through the canonical configuration/change owners and one rebuildable `current` view; deeper evidence remains expandable rather than default-loaded.

This is a qualitative reconstruction-cost reduction. WP2 does not claim a universal token/count benchmark or the full Human/Developer/Agent journey improvements reserved for WP3.

### Finding / ADR consequence

- WP2 operationalizes the currentness/reference and current-first/applicability consequences designed under #246/#247.
- Existing F01–F45 dispositions are not rewritten merely because their safeguards now have executable support.
- F10 review-premise independence remains a review/qualification residual; F17/#225 positive scholarly vertical acceptance remains wholly unresolved by this engineering work.
- ADR-0001 and P-001–P-012 remain the admitted target package; WP2 does not promote ADR-0001 or the full SD-KA-01 target to accepted architecture baseline.

### Whole-system return

**Changed:** the programme now has repository-native currentness/query/applicability primitives that remove a material part of chronology reconstruction and protect against latest-wins/currentness laundering. The whole bugwave is not closed: WP3–WP6 remain admitted work, and final SD-KA-01 Result Review remains outstanding.

**Downstream readiness:** WP1 and WP2 required owners now exist and are verified for their bounded slices. #258/WP3 is therefore the next eligible implementation cursor within the already-existing D-016 admission, but it is not started by this return. #259/WP4 remains later because its context/`.prompt`-dependent fitness surface still depends on WP3 as applicable.

**Deliberate non-changes:** no manuscript Project purpose, priority, scope, gate or scholarly `NEXT ACTION`; no #225 acceptance; no #90 reactivation; no physical brownfield migration; no autonomous planner/workflow engine; no specialist or Human acceptance inferred from CI.

### Review boundaries

Technical currentness/reference/rebuildability assurance and repository restartability pass for the properties stated above. The exact-head review was writer-context self-review, not independent evidence. Scholarly adequacy, specialist validation, Human-reserved consequences and final SD-KA-01 acceptance remain distinct and are not claimed by WP2.

---

## WP3 — Human/developer/Agent contexts, bootstrap and bounded prompt capability

### Exact result basis

- Implementation PR: [#283](https://github.com/esany/paleo-type/pull/283).
- Final exact PR head: `88884b4ba35d55df0d9b9d84dbe0518fd764eef6`.
- PR-head assurance: [source-contract run #534](https://github.com/esany/paleo-type/actions/runs/37331932323), successful on that exact head through the shared `python tools/check.py` entrypoint.
- Merge commit on `main`: `c6575ff0c30d70fbfe64b2767d8db68351e7a8ee`.
- Exact post-merge assurance: [source-contract run #535](https://github.com/esany/paleo-type/actions/runs/37332214116), successful on that exact `main` head.
- PR review: exact-head writer-context technical/restartability self-review recorded on PR #283; explicitly not claimed as independent evidence.
- The first PR-head assurance attempt exposed that three WP3 applicability inputs were referenced as unmanaged raw paths and therefore disappeared from isolated contract fixtures. The implementation was corrected by promoting those inputs to managed artifacts `ENG-A-0045`–`ENG-A-0047`; the final exact-head and post-merge runs then passed. This failure/fix is part of the assurance record rather than hidden history.

### Actual state change

WP3 implements the admitted interaction/context slice without making generated views, prompts or CI into authority:

- `engineering/context/README.md` now owns the derived context/profile and Human-visible work-resolution contract;
- `tools/engineering_context.py` derives Human overview, system-development execution, architecture-review, Human material-decision and maintenance-review packets from canonical engineering owners;
- a generic current/start affordance may resolve context-relative work, but the visible result is a meaningful action with scope and authority/basis provenance rather than only an Issue or work-package token;
- ambiguous current/next work fails closed into explicit candidates instead of silently creating one repository-global cursor;
- applicability provenance remains visible and unrelated historical catalog growth does not automatically enlarge the default execution packet;
- `engineering/prompts/CONTRACT.md` and `tools/prompt.py` implement bounded prompt create/review/test behavior without executing the requested task, choosing priority or manufacturing admission/acceptance;
- simple non-repository prompt requests remain simple, while consequential paleo-type prompt construction requires fresh governing/current-owner resolution and repository-first completion behavior;
- architecture/maintenance review profiles expose review target, evidence-basis class, inherited/re-tested premises, independence claim and evidence-depth limit; freshness of context/model alone never establishes independence;
- `tools/check.py` is now the single documented deterministic full-check entrypoint used both locally and by CI.

The shared check runs Source Contract validation, Engineering validation, the complete regression suite, fresh-process Project contexts and managed real-data Project/Source resolver fixtures. Its PASS remains technical assurance only.

### Human / Developer / Agent reconstruction result

WP3 materially reduces relay/reconstruction burden while preserving provenance:

- a Human can ask for the current system-development view and receive a semantic action statement with scope and authority basis instead of replaying dated Issues/audits;
- a Senior Developer has one bounded navigation path from repository orientation to current engineering state, role/task context, active owners, one full-check command and deeper provenance on demand;
- an execution Agent receives current/applicable authority, requirements/context, non-goals, verification and whole-system-return information rather than the full engineering history by default;
- context-starvation and history-growth regressions protect against both over-compression and indiscriminate historical payload growth.

This is a qualitative reconstruction/Human-burden improvement. It does not claim a universal token benchmark or replace judgement about substantive adequacy.

### Prompt / review evidence-basis result

The bounded prompt capability now has executable regression coverage for simple non-repository behavior, consequential repository authority bootstrap, open-ended/read-everything failure patterns, recency-as-authority pressure, self-review handling and independence overclaim.

F10's generic safeguard is therefore operationalized: consequential review contexts can state what evidence was inspected, what premise remained inherited and whether independence is established. F10 is **not** reclassified as solved evidence merely because the safeguard exists; the final qualification/review still has to demonstrate the needed evidence basis. F17/#225 remains unchanged and wholly outside this engineering PASS.

### Whole-system return

**Changed:** Human/Developer/Agent context products, developer bootstrap, bounded prompt behavior, review-evidence-basis semantics and a shared local/CI assurance entrypoint are now repository-native, rebuildable and restartable. The current implementation no longer requires the Human to translate a raw `WP3`/Issue token into the actual action/scope by hand.

**Downstream readiness:** #259/WP4 is now the next eligible bounded implementation package within the existing D-016 admission because the context/`.prompt` surfaces it depends on exist and are exactly post-merge verified. WP4 is not started by this return. #260/WP5 remains not-started because its migration design explicitly depends on the semantic/configuration/context/**fitness** prerequisites from earlier work packages; WP4 therefore remains a prerequisite before WP5 migration can be treated as ready.

**Deliberate non-changes:** accepted architecture/Requirement baselines remain unchanged; no manuscript Project purpose, priority, scope, gate or scholarly `NEXT ACTION`; no #225 acceptance; no #90 reactivation; no physical brownfield migration; no autonomous planner/global current-work singleton; no specialist, independent-review or Human acceptance inferred from context generation or CI.

### Review boundaries

WP3's exact-head and post-merge technical assurance establish the deterministic/restartability properties above. The review was writer-context self-review, not independent evidence. Final SD-KA-01 acceptance, F10 evidential qualification, F17 scholarly acceptance, specialist validation and any Human-reserved consequence remain distinct and pending under their existing owners.
