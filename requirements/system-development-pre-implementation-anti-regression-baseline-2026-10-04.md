# System-development pre-implementation anti-regression baseline — 2026-10-04

**Status:** NON-NORMATIVE PRE-IMPLEMENTATION / ANTI-REGRESSION / BASELINE EVIDENCE — **DEV-READY WITH BOUNDED REFINEMENT / NOT D-016 ADMISSION-READY / NOT ADMITTED**  
**Repository baseline:** `main@4468473aff4e89116ee1bd406de44d4cc15255b0`  
**Requalifies for current process state:** `requirements/system-development-holistic-knowledge-architecture-dev-ready-design-2026-10-04.md`  
**Preserves as evidence:** the holistic EKCP architecture class, all earlier lifecycle/knowledge/Product/Human-proxy/Human-decision audits and designs, #225/#230 history, current METHOD, Project/Corpus truth and Git history.  
**This artifact is not:** D-016 admission, implementation permission, METHOD, accepted engineering configuration, a new canonical engineering schema, a migration, a manuscript Project scope, a scholarly `NEXT ACTION`, a workflow engine, or a claim that #225 whole-system scholarly acceptance has been established.

## A. Executive disposition

The requested anti-regression pass changes the process disposition in one important way without overturning the current architecture class.

The 2026-10-04 holistic design was correct to widen the problem from a bounded revision-package problem to a coupled **Engineering Information Management + Configuration Management + finding/learning promotion + development-readiness + developer/agent context** problem. Its selected Engineering Knowledge & Configuration Plane (EKCP) remains the strongest architecture class found in the current evidence.

However, using the accumulated findings *before implementation* exposes several contract-level gaps that would otherwise be left for the implementer to invent. The current state is therefore:

> **DEV-READY WITH BOUNDED REFINEMENT — NOT YET D-016 ADMISSION-READY — NOT ADMITTED.**

This is not `NEEDS MATERIAL REDESIGN`: the principal responsibilities survive. It is also not `STILL DEV-READY` in the stronger admission-ready sense, because the remaining gaps affect information identity, finding-completeness, current-configuration transitions, context applicability and Human decision validation — precisely the semantics the architecture is meant to remove from ad-hoc reconstruction.

The implementation freeze remains in force. In particular, this pass does **not** create `engineering/`, move `requirements/`, change METHOD, introduce runtime/schema contracts, implement the Context Compiler, or begin SD-KA-01.

The most important correction is methodological and operational:

```text
not
latest synthesis → implementation

but
accumulated findings
→ active anti-regression register
→ current-gap baseline
→ brownfield classification
→ finding-promotion audit
→ architecture falsification / dry run
→ close bounded design contracts
→ Human-comprehensible D-016 surface
→ only then implementation admission
```

The first legitimate implementation, if later admitted, should be **a small in-place semantic contract/validator slice over representative brownfield artifacts**, not the physical repository migration.

---

## B. Fresh authority and current state

Fresh current repository authority at the baseline establishes:

- scholarly result/source understanding is the product; engineering infrastructure is subsidiary;
- one durable fact/decision/state has one canonical owner; generated views are derived;
- complete **applicable** context is required, not indiscriminate whole-repository loading;
- Human Owner retains material D-016 admission, purpose, priority/scope and consequential-use authority;
- routine bounded work already inside authority belongs to AI/implementation agents rather than to the Human as relay;
- Issues/PRs/Milestones are work/review/planning metadata, not scholarly truth;
- D-016 remains `analysis → requirements → concept → owner review / explicit implementation admission → development → deterministic tests / scholarly loss checks → result review`;
- technical verification, scholarly adequacy, specialist validation, Human/governance review and restartability are distinct assurance dimensions;
- current Project state is not inferred from system-development work.

Current GitHub work metadata resolves #230 as closed/completed and #225 as closed, while #225's body still contains its historical `ACTIVE` wording. The current README correctly refuses to infer whole-system #225 acceptance from closure alone.

All three manuscript Project restart owners currently expose **no owner-selected active scholarly work**. This pre-implementation pass therefore creates no manuscript task, gate progression or `NEXT ACTION`.

Current exact-head CI at `main@4468473aff4e89116ee1bd406de44d4cc15255b0` is green for the existing Source/File/Project-use contract and current regressions. That says nothing about the not-yet-implemented engineering knowledge/configuration plane.

---

## C. Activated finding register

The following register converts the accumulated audits from passive history into active design/qualification constraints.

| ID | Finding / demonstrated failure | Risk if ignored now | Required property / current disposition | EKCP consequence / proof |
|---|---|---|---|---|
| F01 | AI semantic integration debt | capable model repeatedly recompiles semantics differently | stable deterministic owners where semantics are mature; explicit unresolved reasoning boundaries | configuration/catalog/context must reduce reconstruction, not merely summarize it; Fresh Context fixture |
| F02 | Current / Historical / Supersession drift | stale prose/history can look current | explicit currentness and recoverable supersession | configuration + lifecycle validation; stale-current fixture |
| F03 | Programme/owner discoverability gap | current owner found only by chronology | current programme/change owner or explicit absence directly discoverable | configuration/change state + current view |
| F04 | Issue chronology becomes restart/runtime context | Fresh Context must replay threads | work metadata/history not required to reconstruct current configuration | derived current view + change state; history-heavy fixture |
| F05 | Bounded work/programme closability gap | owners stay alive to preserve useful meaning | result/reconciliation promotes consequences, then bounded owner can close | change Result + configuration/plan reconciliation; closure fixture |
| F06 | Durable decision promotion incomplete | rationale remains scattered in chronology | consequential accepted rationale promoted to durable decision owner | keep `DECISIONS.md`; index/trace it rather than invent new truth store |
| F07 | `requirements/` contains heterogeneous artifact roles | path/name ceases to communicate responsibility | semantic role/lifecycle/authority independent of filename; physical IA eventually matches responsibility | brownfield classification first, migration later |
| F08 | Active knowledge and persisted knowledge insufficiently separated | persistence growth becomes default-context growth | persistence != currentness; historical evidence leaves default context after integration | context profiles + lifecycle; history-growth fixture |
| F09 | Derived-state reification | summaries/views become second truth | generated views rebuild from canonical owners and fail if stale | exact derivation/freshness check |
| F10 | **Review Premise Inheritance** | Fresh reviewer can inherit the same false premise from derived owners | review provenance/evidence basis must remain visible; Fresh Context is not automatically independent evidence | **OPEN ORTHOGONAL GAP. EKCP trace can help but SD-KA-01 must not claim this failure closed without separate Generic-Fit/design evidence** |
| F11 | Local correctness / global misframing | technically correct child becomes system conclusion | local PASS never implies parent/system closure; mandatory whole-system consequence | result→whole reconciliation fixture |
| F12 | Minimality/adequacy bias | elegant small fix truncates required functionality | sufficient architecture first; simplify without loss second | every retained component traces to failure/requirement; every removed component needs sufficiency proof |
| F13 | Parent/child + return semantics already exist in bounded forms | unnecessary reinvention | reuse proven semantics and generalize only after fit | bounded change/result return; no new universal engine by default |
| F14 | Derived/rebuildable operational views are useful | manual README becomes current-state clock | current/read models derived after canonical currentness owners exist | Current State/Context views only after configuration semantics |
| F15 | Exact-head/post-mutation assurance matters | tests on stale SHA create false confidence | final qualification on exact merged head | exact-head CI fixture |
| F16 | Authority laundering | resource/state/metadata can be promoted into task authority | descriptive state cannot manufacture scope/priority/admission | authority-negative tests; context compiler must preserve this boundary |
| F17 | **#225 positive real scholarly end-to-end fixture remains unproven** | engineering IA could be mislabeled as scholarly whole-system acceptance | preserve as separate unresolved acceptance gap; no manuscript scope fabricated to close it | **NOT CLOSED BY EKCP**; explicit residual in Result/decision surface |
| F18 | Orientation surfaces can become stale | README becomes manually maintained projection | README stable navigation only; current system-development meaning comes from current owner/derived view | README-reduction only after replacement current surface works |
| F19 | Repo-first is stronger than `persisted somewhere` | chat/sandbox/history can become hidden working truth | restart-relevant results persist in intended owner and remain reachable without originating context | repository-first qualification |
| F20 | Human used as relay/router despite no Human decision | routine work stalls on `weiter`/transport/reconstruction | distinguish execution-only continuation from genuine Human/specialist/evidence gates | bounded change state/context; Human-relay fixture |
| F21 | `AUTHORIZATION != INFORMED DECISION READINESS` | Human formally decides without understanding stage/consequence | decision surface must establish situational awareness before decision token | Human comprehension validation before D-016 |
| F22 | Development stages became interleaved and solution-shaped too early | Requirements get derived backwards from attractive design | risk/state-tailored development coverage; design may lose | change coverage + pre-implementation architecture falsification |
| F23 | Context economy can become context starvation | compact packet omits authority/evidence/uncertainty | reduce reconstruction, not evidence; progressive disclosure | context-starvation adversarial fixture |
| F24 | Wirknetz/relations are useful analytical trace but not proven runtime | attractive graph model becomes speculative platform | relation correctness > completeness; uncertain relations stay candidate | minimal material relations only; no graph/Bridge runtime |
| F25 | Genericity != Distribution | package/template/product work could displace scholarly product | repository-internal genericity only unless real consumer contract appears | no package/portal/template requirement by default |
| F26 | Generic-Fit remains incomplete across materially different source structures | current fixture assumptions masquerade as generic | materially different fixture before strong generic acceptance | qualification fixture, without inventing manuscript priority |
| F27 | Developer bootstrap for system development is weak | new developer must infer entry path/check set | one current engineering entry path + one deterministic local assurance command | developer bootstrap fixture |
| F28 | Engineering CI does not check engineering IA/currentness/promotion | new knowledge plane can drift silently | catalog/config/trace/promotion/freshness fitness functions | CI qualification after contracts exist |
| F29 | Rich-audit insight can disappear even when source file persists | registered history gives false sense of learning preservation | every **material finding source** needs a closure/coverage account, not just every already-registered finding | **new bounded design refinement: material-finding registration completeness contract** |
| F30 | Proposed trace refs are underspecified | migration/relations can point ambiguously or break after moves | stable target-reference semantics for file/artifact/section/decision/work evidence | **new bounded design refinement: stable reference/anchor contract** |
| F31 | Context profile applicability is underspecified | compiler becomes manual reading-list clock or silently omits material rules | applicability provenance must be explicit: derived where formal, selected with source/basis where judgement is required | **new bounded design refinement: context-applicability contract** |
| F32 | Proposed configuration shape lacks full transition semantics | `configuration.json` could become another stale clock | define who/what can move proposed→accepted/current and when result changes current baselines | **new bounded design refinement: configuration transition contract** |
| F33 | Central TSV representation was selected before brownfield dry run | information responsibilities may be right but physical representation may duplicate data unnecessarily | preserve responsibilities, test central TSV vs local metadata/hybrid representation on real artifacts | representation is **open bounded design detail**, not architecture-class reversal |
| F34 | Human decision brief can be complete yet incomprehensible | documentation quality is mistaken for informed decision readiness | actual comprehension challenge/validation required before admission | decision-readiness fixture must be run, not merely specified |

### C1. Findings that must remain explicit residuals rather than being absorbed into EKCP

Two older findings are especially important because a knowledge/configuration architecture could make them easier to trace while still not solving them:

1. **F10 Review Premise Inheritance** is epistemic/review-provenance work. A new context can still inherit the same derived premise. EKCP must not claim `fresh context = independent evidence`.
2. **F17 #225 positive scholarly vertical acceptance** remains a separate system-acceptance gap. Current Issue closure metadata does not prove its historical T11 contract. No manuscript work may be manufactured to make the engineering revision look complete.

Keeping these residuals explicit is itself an anti-regression requirement: system infrastructure must not launder adjacent unresolved problems into `solved` merely because traceability improved.

---

## D. Current EKR requirement gap baseline

The 35 EKR properties from the holistic design were rechecked against current `main`, not against the proposed target.

| Requirement | Current state | Fresh disposition |
|---|---|---|
| EKR-01 current engineering configuration directly identifiable | **UNSATISFIED** | current system-development meaning still depends on README + dated design interpretation |
| EKR-02 actual/current/target/plan/work/history distinguishable | **PARTIALLY SATISFIED** | distinctions exist in prose/governance but not as first-class engineering current state |
| EKR-03 one canonical current-configuration owner | **UNSATISFIED** | no engineering configuration owner exists |
| EKR-04 zero/multiple system changes without recency priority | **PARTIALLY SATISFIED** | authority rules support absence; engineering change/focus model is absent |
| EKR-05 current-state change traces to admitted change/result | **PARTIALLY SATISFIED** | Git/PR/DECISIONS provide pieces, not systematic status accounting |
| EKR-06 stable identity/kind/authority/lifecycle for engineering assets | **UNSATISFIED** | mostly inferred from path/header/prose |
| EKR-07 history retrievable but excluded from default current context | **PARTIALLY SATISFIED** | Project side is stronger; system-development reading path still history-heavy |
| EKR-08 superseded/current machine-checkable enough to prevent latest-wins | **UNSATISFIED** | prose requalification is current mechanism |
| EKR-09 physical location communicates semantic responsibility | **UNSATISFIED** | `requirements/` remains mixed-purpose |
| EKR-10 migration/reclassification without lost provenance/refs | **PARTIALLY SATISFIED** | Git preserves file history, but stable engineering IDs/ref migration are undefined |
| EKR-11 material findings have explicit forward disposition | **UNSATISFIED** | some audits contain disposition matrices, no generic lifecycle |
| EKR-12 closed audit/change cannot leave orphan material findings | **UNSATISFIED** | no completeness/coverage mechanism |
| EKR-13 current Requirement/Decision/Design traces backward | **PARTIALLY SATISFIED** | possible manually via prose/issues/files, not a reliable semantic query |
| EKR-14 findings trace forward to consequence/non-consequence | **UNSATISFIED** | this pass had to reconstruct it manually |
| EKR-15 relation correctness outranks completeness | **PARTIALLY SATISFIED** | strong principle/evidence, no engineering relation contract |
| EKR-16 verification/Human/specialist validation distinguished | **SATISFIED SEMANTICALLY** | current quality/governance owners already distinguish them |
| EKR-17 required development capabilities explicitly dispositioned | **UNSATISFIED** | only proposed in non-normative design |
| EKR-18 development capabilities remain distinct while iterative | **PARTIALLY SATISFIED** | method language supports distinction; prior rebaseline proved practical interleaving |
| EKR-19 finding cannot silently become implementation-shaped Requirement/Work | **PARTIALLY SATISFIED** | D-016/Domain→Dev guard helps; no engineering finding→work trace control |
| EKR-20 DEV-READY derived only after blocking uncertainty closed/exposed | **PARTIALLY SATISFIED** | candidate criteria exist; current pass demonstrates no canonical/executable derivation |
| EKR-21 DEV-READY/ADMITTED/IMPLEMENTING/VERIFIED/ACCEPTED distinct | **PARTIALLY SATISFIED** | conceptual governance distinction exists, no change-state owner |
| EKR-22 tiny/routine work avoids ceremony | **SATISFIED SEMANTICALLY** | current maintenance/workflow deliberately preserve proportionality |
| EKR-23 role/task-specific contexts compile from canonical state | **PARTIALLY SATISFIED** | Project and outcome contexts exist; system-development/architecture/Human-decision profiles do not |
| EKR-24 progressive disclosure / current-first context | **PARTIALLY SATISFIED** | principle exists, system-development mechanism absent |
| EKR-25 bootstrap size does not grow with audit history | **UNSATISFIED for system development** | this very pass required substantial dated-history reconstruction |
| EKR-26 one new-developer path + one local full check | **UNSATISFIED** | current CI commands exist but no first-class system-development developer contract |
| EKR-27 Human D-016 surface exposes decision basis/consequence | **PARTIALLY SATISFIED** | holistic design is rich, but actual comprehension remains unvalidated and new bounded gaps were found |
| EKR-28 derived views reproducible/detectably stale | **PARTIALLY SATISFIED** | Project contexts satisfy pattern; no engineering current/catalog views |
| EKR-29 `current/why/superseded/open/applicable` queryable without chronology | **UNSATISFIED** | currently semantic reconstruction is required |
| EKR-30 repository-native normal-clone operation | **SATISFIED** | current repo-local Python/Git model already supports this |
| EKR-31 engineering metadata/relations validated in CI | **UNSATISFIED** | current CI is Source/Project focused |
| EKR-32 brownfield migration loss-checked/reversible | **PARTIALLY SATISFIED AT DESIGN LEVEL** | high-level stages exist; stable refs and representative dry run still needed |
| EKR-33 scholarly Source/File/Project semantics untouched unless required | **SATISFIED NOW** | this pass changes none of them |
| EKR-34 engineering work creates no manuscript priority | **SATISFIED** | governance plus all three current Project states preserve explicit absence |
| EKR-35 larger mechanisms remain triggerable rather than size-prohibited | **PARTIALLY SATISFIED** | holistic design states this; not yet an admitted operating contract |

### D1. Interpretation

The matrix supports the EKCP **responsibility set** but also falsifies a premature implementation start. The majority of unmet properties are not code bugs in existing tools; they are the not-yet-admitted engineering information/configuration responsibilities themselves. Four of them (EKR-10/12/24/27) expose design refinements that must be tightened before implementation is asked to invent semantics.

---

## E. Fresh-context and developer-journey baseline

### E1. Fresh Chat — system development

A capable new context can learn the governing purpose and current candidate from `README.md`, but a defensible answer to `what is current, why, what is still open, and what has been superseded?` still requires a chain equivalent to:

```text
GOVERNING_OBJECTIVE
+ AGENTS
+ README
+ maintenance/workflow/quality
+ current holistic design
+ selected predecessor/rebaseline audits
+ current Issues/PR state where chronology/currentness diverged
```

That is already better than old-chat dependence, but it remains **history-as-synthesis** for the system-development domain. Important residuals such as Review Premise Inheritance and the separate #225 positive-vertical gap are easy to lose if only the latest holistic design is read.

**Baseline result: FAIL EKR-01/25/29 for system-development bootstrap.**

### E2. New developer

Current `tools/` has strong repo-local scripts for Source/Project concerns (`source_contract.py`, `source_intake.py`, `project_context.py`, `outcome_context.py`) plus fixture-specific tools. There is no engineering-system entry point, no current engineering configuration query and no single documented local command corresponding to the whole CI/developer assurance contract.

The current workflow itself shows the required checks, but the developer must discover and reconstruct them from CI configuration.

**Baseline result: FAIL EKR-26; partial evidence for the feasibility of a repository-native solution.**

### E3. Human D-016 decision

The holistic design contains a much richer Human decision surface than earlier work, but repository history has already demonstrated that a formally complete compressed decision surface can still fail Human comprehension. This pass also identified design contracts that materially affect what an admission would authorize.

**Baseline result: NOT YET ADMISSION-READY. The Human decision brief must be regenerated after bounded refinements and tested for comprehension.**

### E4. Finding promotion journey

Real historical findings can be reconstructed — for example F07 (`requirements/` heterogeneity), F12 (minimality bias), F20 (Human relay) — but their forward consequence is still discovered by reading later audits/designs. There is no deterministic answer to `what happened to finding X?` or reverse answer `which findings materially support this current design property?`.

**Baseline result: FAIL EKR-11/12/14/29.**

---

## F. Brownfield information inventory

The current `requirements/` tree is flat but semantically heterogeneous. This pass enumerated it in place before any migration. The role classes below describe current content; they do not create new canonical taxonomy.

### F1. Structured Requirement baseline

- `domain-requirements.tsv` — actual structured cross-disciplinary Requirement inventory; canonical input to `outcome_context.py` for selected Requirement metadata.

### F2. Problem frames / reconstructions / operational analyses

- `human-need-to-scholarly-outcome-problem-frame-2026-09-17.md`
- `human-need-maturity-progress-reconstruction-2026-09-18.md`
- `research-state-decision-analysis-operationalization-2026-09-18.md`
- `system-operationalization-audit-2026-09-17.md`
- `phase0-1-end-to-end-capability-ownership-map-2026-09-17.md`

### F3. Audits / rebaselines / deep checks

- `ai-role-handoff-engineering-control-audit.md`
- `project-maturity-model-repository-audit-2026-09-18.md`
- `maturity-transparency-self-review-2026-09-18.md`
- `parallel-chat-coordination-audit-2026-09-12.md`
- `parallel-chat-human-control-findings-2026-09-13.md`
- `research-framing-transdisciplinary-competency-audit-2026-09-14.md`
- `repository-knowledge-lifecycle-adequacy-audit-2026-10-02.md`
- `human-proxy-work-lifecycle-context-efficiency-audit-2026-10-03.md`
- `human-decision-readiness-design-process-rebaseline-audit-2026-10-03.md`
- `product-co-development-boundary-analysis-delta-2026-10-03.md`
- `product-co-development-boundary-deep-check-2026-10-03.md`

### F4. Research / evidence syntheses

- `cross-source-research-findings-2026-09-14.md`
- `shared-fixture-research-findings-2026-09-14.md`
- `pre-synthesis-research-program-2026-09-14.md`
- `pre-synthesis-research-integration-2026-09-14.md`
- `final-multi-question-generation-research-2026-09-14.md`
- `post-research-problem-landscape-reconciliation-2026-09-14.md`
- `post-research-capability-requirement-synthesis-2026-09-14.md`
- `source-context-standards-evidence-2026-09-07.tsv`

### F5. Concepts / architecture / design / target-state evidence

- `source-context-model-synthesis-2026-09-07.md`
- `executable-transdisciplinary-research-system-concept-idea-2026-09-14.md`
- `post-research-synthesis-concept-approaches-2026-09-14.md`
- `phase2-integrated-concept-comparison-2026-09-18.md`
- `repository-knowledge-lifecycle-d016-decision-surface-2026-10-02.md`
- `repository-knowledge-lifecycle-d016-refinement-2026-10-03.md`
- `repository-target-state-implementation-readiness-2026-10-03.md`
- `system-development-information-architecture-dev-ready-design-2026-10-03.md` — now superseded as sufficient whole-system design
- `system-development-holistic-knowledge-architecture-dev-ready-design-2026-10-04.md` — current architecture candidate, requalified by this pass

### F6. Admissions / owner dispositions

- `source-project-owner-admission-2026-09-02.md`
- `default-branch-promotion-enforcement-owner-admission-2026-09-17.md`
- `default-branch-promotion-enforcement-owner-disposition-2026-09-17.md`

### F7. Result reviews / programme results

- `c1r-outcome-context-result-review-2026-09-18.md`
- `research-system-programme-continuity-result-review-2026-09-16.md`
- `research-system-programme-completion-review-2026-09-17.md`
- `learning-integration-claim-repair-result-2026-09-23.md`

### F8. Learnings

- `design-product-development-methodology-learning-2026-09-19.md`
- `human-feedback-intent-classification-learning-2026-09-18.md`

### F9. Work instructions / prompts / coordination bootstrap evidence

- `ai-role-handoff-engineering-analysis.md`
- `human-need-maturity-progress-analysis-prompt-2026-09-18.md`
- `learning-integration-claim-repair-work-prompt-2026-09-19.md`
- `learning-integration-claim-repair-execution-prompt-2026-09-23.md`
- `chatgpt-global-coordination-bootstrap-2026-09-14.md`
- `chatgpt-project-coordination-bootstrap-proposal-2026-09-14.md`

### F10. Programme continuity / Generic-Fit / synthesis evidence

- `research-system-problem-landscape-2026-09-14.md`
- `research-system-programme-synthesis-2026-09-15.md`
- `research-system-programme-continuity-audit-2026-09-16.md`
- `research-system-programme-continuity-requirements-resolution-2026-09-16.md`
- `research-system-programme-continuity-concept-2026-09-16.md`
- `outcome-continuity-under-decomposition-generic-fit-2026-09-18.md`

### F11. Branch-promotion Requirements/concept sequence

- `default-branch-promotion-enforcement-requirements-resolution-2026-09-16.md`
- `default-branch-promotion-enforcement-concept-2026-09-16.md`
- the admission/disposition records above.

### F12. Inventory conclusion

The mixed directory is not merely visually untidy. It contains materially different authority and lifecycle classes — including a real Requirement table, completed prompts, non-normative audits, admitted-change records, superseded designs, research evidence and local result reviews. Currentness must therefore not be inferred from directory membership, filename date or lexical `requirements` proximity.

The target responsibility to separate these roles survives. The exact physical move map remains a post-contract migration concern.

---

## G. Finding-promotion / orphan-insight audit

The recent Oct-02→Oct-04 chain was checked specifically for forward effect.

| Finding / learning | Forward effect today | Current anti-regression disposition |
|---|---|---|
| F02 current/history/supersession drift | EKR-01/02/07/08; configuration/lifecycle target | **PROMOTED** |
| F04 issue chronology as restart context | EKR-01/25/29; current/change context target | **PROMOTED** |
| F05 closability | bounded change/Result/reconciliation semantics | **PROMOTED** |
| F06 decision promotion | preserve `DECISIONS.md`; trace accepted rationale | **PROMOTED WITH EXISTING OWNER** |
| F07 heterogeneous `requirements/` | EKR-06/09; brownfield classification + later IA migration | **PROMOTED** |
| F08 active vs persisted knowledge | EKR-07/24/25; progressive disclosure | **PROMOTED** |
| F10 Review Premise Inheritance | not materially closed by EKCP | **OPEN / EXPLICIT RESIDUAL; must not disappear** |
| F11 local correctness/global misframing | whole-system reconciliation + qualification | **PROMOTED** |
| F12 minimality/adequacy | architecture selection discipline | **PROMOTED AS DESIGN RULE** |
| F13 parent/child return | bounded work/change result semantics | **REUSED / GENERALIZED WITH FIT** |
| F14 rebuildable operational views | generated Current/Context/Catalog views | **PROMOTED AFTER OWNER SEMANTICS** |
| F15 exact-head assurance | CI/result qualification | **PROMOTED** |
| F16 authority laundering | negative-authority context/validation tests | **PROMOTED / EXISTING CONTROLS RETAINED** |
| F17 positive #225 scholarly vertical fixture | no EKCP closure | **OPEN SEPARATE ACCEPTANCE GAP** |
| Human relay | bounded continuation/genuine decision discrimination | **PROMOTED** |
| Human decision comprehension | decision readiness + Human validation | **PROMOTED, NOT YET VALIDATED** |
| Reduce reconstruction, not evidence | context profile/progressive disclosure | **PROMOTED** |
| Genericity != Distribution | no package/portal/template product by default | **PROMOTED BOUNDARY** |
| Wirknetz as trace lens | relation semantics, candidate uncertainty, no runtime | **PROMOTED AS ANALYTICAL PROPERTY ONLY** |
| verification != validation | distinct relations/states/review outcomes | **PROMOTED / ALREADY OWNED SEMANTICALLY** |
| previous narrow SD-01 design | bounded change package retained inside EKCP | **PARTIALLY RETAINED; WHOLE-DESIGN STATUS SUPERSEDED** |

### G1. New orphan-insight discovery: registration completeness

The holistic design's proposed CI check says, in effect, `every registered material finding from a closed source must have a disposition`. That protects **registered** findings, but it does not prove that all material findings from the source were registered.

Without a source-level completeness/closure statement, the system can reproduce the exact original failure while passing its own validator:

```text
rich audit contains findings A B C D
→ register A B
→ disposition A B
→ validator PASS
→ C D silently disappear
```

This is a real bounded design gap, not a reason to abandon finding promotion. The refinement must define how a material source declares the complete set of material findings (or how review attests there are none beyond the registered set) without forcing every paragraph into a finding ontology.

---

## H. Failure → architecture sufficiency matrix

| EKCP responsibility | Failure families closed | Current disposition after falsification |
|---|---|---|
| Engineering artifact identity/lifecycle catalog | F02/F07/F08/F18 | **SURVIVES**; exact physical central-TSV representation remains open to dry-run evidence |
| Material finding disposition | F06/F08/F12/Insight Loss | **SURVIVES AND MUST BE STRENGTHENED** with registration-completeness/coverage semantics |
| Material relation trace | F06/F10-partly/F24 | **SURVIVES**; needs stable reference/anchor semantics; must not claim F10 fully closed |
| Engineering configuration owner | F02/F03/F04 | **SURVIVES**; needs accepted/current transition semantics and exact relation to repository tree/Git |
| Bounded change state | F05/F11/F20/F22 | **SURVIVES**; admission/currentness transitions must be explicit without universal workflow engine |
| Generated Current/Catalog views | F03/F04/F08/F14/F18 | **SURVIVES** only downstream of configuration/identity owners |
| Context profiles/compiler | F01/F04/F20/F23/F27 | **SURVIVES**; applicability provenance must be specified so profiles do not become manual reading-list truth |
| Query surface | F01/F03/F14/F27 | **SURVIVES**; read-only/derived |
| Human decision brief | F21/F34 | **SURVIVES**; actual comprehension validation required |
| Developer entry + unified check | F27/F28 | **SURVIVES** |
| CI fitness functions | F02/F09/F15/F28/F29 | **SURVIVES**; only after stable semantics exist |
| Physical IA migration | F07/F18 | **SURVIVES AS LATER STEP**; must not lead implementation |
| Development-readiness coverage | F12/F20/F22 | **SURVIVES**; risk/state-tailored, not waterfall |
| SQLite/graph/portal/workflow engine/package move | no current demonstrated need sufficient to require them | **REMAINS TRIGGER-BASED, NOT SELECTED NOW** |

### H1. Architecture class verdict

The larger EKCP architecture class remains supported because no smaller compared mechanism closes Information Management, Configuration Management, promotion/trace and bootstrap together. The new findings do **not** support an external database, graph store, portal or orchestration engine.

What changed is the proof burden at its internal contracts: we cannot implement `artifacts.tsv`, `findings.tsv`, `relations.tsv`, `configuration.json` and `context-profiles.json` merely because those filenames were in the latest design. The semantic responsibilities are supported; their exact representation must survive the brownfield dry run and the four bounded contract refinements below.

---

## I. Migration dry run over representative real artifacts

No file was moved. Representative current artifacts were analytically projected through the candidate responsibilities.

| Brownfield case | Required future semantic treatment | Dry-run result / discovered constraint |
|---|---|---|
| `requirements/domain-requirements.tsv` | current structured Requirement baseline; stable identity; applicability remains separate from existence | **PASS conceptually**. Likely remains under narrowed `requirements/`; context must not infer applicability automatically |
| `repository-knowledge-lifecycle-adequacy-audit-2026-10-02.md` | non-normative audit evidence; closed/historical; material F01–F19 forward-dispositioned; not default current state | **PASS only with finding-coverage contract**; merely registering selected findings is insufficient |
| `pre-synthesis-research-integration-2026-09-14.md` / related research | historical research evidence supporting later Requirements/concepts | **PASS conceptually**; historical research should be retrievable by trace, not default-loaded |
| `system-development-information-architecture-dev-ready-design-2026-10-03.md` | non-normative design evidence; explicitly superseded as sufficient whole design by 2026-10-04 work | **PASS only with stable supersession references**; date/filename must not define status |
| `default-branch-promotion-enforcement-owner-admission-2026-09-17.md` | genuine admitted-change evidence with exact scope/non-authorizations, followed by later platform defer/disposition | **HIGH-VALUE FIXTURE**: admission and current executability are distinct; a catalog must represent current consequence without rewriting the historical admission |
| `c1r-outcome-context-result-review-2026-09-18.md` | terminal local Result with explicit `LOCAL PASS; #225 acceptance not established` | **HIGH-VALUE FIXTURE**: result→parent consequence must preserve non-achievement boundary |
| `human-feedback-intent-classification-learning-2026-09-18.md` | system-learning/failure evidence; largely confirms existing authority semantics; candidate regression not fully deterministic | **PASS conceptually**: learning may be integrated without becoming new METHOD/schema; needs explicit forward disposition |
| `human-need-maturity-progress-analysis-prompt-2026-09-18.md` | completed historical work instruction that explicitly points to its result and is not an open cursor | **PASS conceptually**: lifecycle/status must exclude it from default active context |
| coordination bootstrap proposal/history artifacts | historical coordination/work evidence, not current authority | **AMBIGUITY RISK**: future classification must make non-authority/currentness unmistakable; current policy must be resolved from current owner, not nearest bootstrap filename |
| F12 minimality/adequacy finding | source audit finding with design/process consequence across later designs | **TRACE FIXTURE**: one finding can support several Requirements/design decisions; relation model cannot force one finding→one target |

### I1. Dry-run conclusions

The dry run does **not** require a new architecture class. It does require four pre-admission contract refinements:

1. **Material-finding coverage contract** — how a closed material source demonstrates that its material findings are completely dispositioned, without requiring exhaustive atomization of all prose.
2. **Stable engineering reference contract** — how artifact IDs and relation endpoints address whole files, stable internal anchors/decision IDs, GitHub work evidence and moved legacy paths without depending on mutable filenames alone.
3. **Configuration transition contract** — what event/authority moves a proposed baseline/change into accepted/current configuration, how current semantic baseline relates to actual repository tree at a Git SHA, and how terminal Result reconciles current configuration.
4. **Context applicability contract** — which applicable rules/Requirements can be derived deterministically, which require explicit selection/judgement, how that basis is recorded, and how omission is detectable without creating another manual context clock.

A fifth refinement is validation rather than information-model semantics:

5. **Human decision comprehension fixture must actually run** before D-016 admission; a complete document alone is not proof.

---

## J. Pattern-regression guard — mandatory for later material work

Before every material future work package, run this check against the fresh current state:

1. Am I reconstructing Current State from History?
2. Am I creating a second truth owner?
3. Am I confusing persistence with promotion/currentness?
4. Am I confusing documentation with state or planning?
5. Is a finding being converted into a solution-shaped Requirement/work item before requirements are established?
6. Is a local PASS being promoted into whole-system PASS?
7. Is integration/reconstruction burden merely moved to Human, AI or maintainer?
8. Is context economy removing material evidence, uncertainty or authority?
9. Does this local detail have an explicit return/reconciliation to the whole?
10. Can a material finding disappear when its source/work closes?
11. Am I preferring `small` before proving sufficiency?
12. Am I adding a larger mechanism without a demonstrated responsibility?
13. Am I creating runtime/schema merely because a relation is modellable?
14. Are verification, specialist validation and Human acceptance still distinct?
15. Does Current State become clearer, or does only History get larger?
16. Can a Fresh Context understand more directly after this step?
17. Did the Target gap / remaining Plan actually change, and is that consequence recorded?
18. Did this step create a new immortal meta-owner or manual synchronization clock?

A material `YES` to a failure question is not a checklist warning to ignore. It is a **re-entry trigger**: disposition the failure, refine Design/Plan as needed, then continue.

---

## K. Qualification baseline — before implementation changes the starting point

The holistic design's 22 fixtures are retained, but their current baseline is now explicit.

| Fixture | Current baseline before implementation |
|---|---|
| 1 New-chat scholarly bootstrap | **STRONG/PASS-LIKE**: Project `STATUS` + `project_context.py` provide current restart; not a claim of scholarly correctness |
| 2 New-chat system-development bootstrap | **FAIL**: current state/rationale/open residuals still require dated artifact synthesis |
| 3 New developer bootstrap | **FAIL**: no engineering entry/current-state query/unified local check |
| 4 History-heavy repository | **FAIL/RISK**: system-development default reading burden grows with history |
| 5 Rich multi-audit synthesis | **FAIL**: findings persist, but no complete forward-disposition contract |
| 6 Finding promotion | **FAIL**: no generic queryable finding→consequence mechanism |
| 7 Finding reject/defer/supersede | **PARTIAL**: prose examples exist, no common engineering mechanism |
| 8 Requirement backward trace | **PARTIAL**: some structured evidence/source fields, no engineering trace plane |
| 9 Decision backward trace | **PARTIAL**: `DECISIONS.md` + history, often manual reconstruction |
| 10 Local result→whole system | **PARTIAL**: maintenance semantics exist; generic engineering current-config reconciliation absent |
| 11 Closed change deactivation | **PARTIAL/FAIL system-side**: Git/issues close, but historical surfaces can remain in default orientation |
| 12 Concurrent investigations | **UNPROVEN** for proposed engineering state |
| 13 Tiny bug / no ceremony | **PASS SEMANTICALLY** under current maintenance/workflow; must not regress |
| 14 Material architecture change full coverage | **PARTIAL**: this design process shows need, but no canonical coverage state |
| 15 Different manuscript Project | **PARTIAL POSITIVE EVIDENCE** from existing generic Project tooling; EKCP genericity not implemented/qualified |
| 16 Human decision surface | **FAIL VALIDATION** until comprehension is demonstrated |
| 17 Specialist decision surface | **SEMANTICALLY SUPPORTED**, no EKCP-specific runtime needed yet |
| 18 Context-starvation trap | **UNPROVEN**; principle exists |
| 19 Stale-current detection | **FAIL** for engineering currentness; README/current artifact drift is manual |
| 20 Orphan-insight detection | **FAIL**; new completeness loophole identified |
| 21 False-relation trap | **SEMANTICALLY SUPPORTED**, future relation contract not implemented |
| 22 Migration-loss test | **UNPROVEN**; Git gives rollback basis, stable semantic refs not yet defined |

### K1. Acceptance-fixture correction

Fixture 20 must be refined from `all registered findings are dispositioned` to a stronger two-part test:

```text
source-level material-finding coverage is closed/reviewed
AND
every declared material finding has an explicit disposition
```

Otherwise the new system can pass while reproducing Insight Loss.

---

## L. Revised DEV-READY disposition and bounded pre-admission work

### L1. Disposition

```text
Fresh authority / state baseline          COMPLETE
Activated finding register                COMPLETE FOR MATERIAL CURRENT FAILURE SET
Current EKR gap baseline                  COMPLETE
Fresh-context baseline                    COMPLETE
Brownfield semantic inventory             COMPLETE AT MATERIAL CLASS / CURRENT REQUIREMENTS TREE LEVEL
Finding promotion / orphan audit          COMPLETE; NEW COVERAGE GAP FOUND
Failure→architecture falsification        COMPLETE
Representative migration dry run          COMPLETE; FOUR CONTRACT GAPS FOUND
Qualification baseline                    COMPLETE
Architecture class                        SURVIVES
Admission-ready detailed design           NEEDS BOUNDED REFINEMENT
D-016 implementation admission            NOT GIVEN
Implementation                            NOT STARTED
```

Formal disposition from the requested set:

> **DEV-READY WITH BOUNDED REFINEMENT**

Operational meaning here is deliberately strict:

> the architecture responsibility set is sufficiently established to avoid reopening the whole solution space, but implementation must remain frozen until the bounded semantic refinements below are completed and the Human decision surface is regenerated/validated.

### L2. Pre-admission blockers

Before a responsible D-016 decision on SD-KA-01, close these bounded items:

**BR-01 — Material Finding Coverage**  
Define source/audit closure semantics that prove material findings were inventoried/dispositioned rather than merely validating already-registered rows.

**BR-02 — Stable Reference / Identity Semantics**  
Define stable engineering artifact IDs and valid reference forms for file/anchor/decision/work evidence, including migration and legacy path behavior.

**BR-03 — Engineering Configuration Transition Semantics**  
Define current vs proposed/accepted/admitted/implemented configuration transitions, owner/authority, exact Git-state relation and Result reconciliation.

**BR-04 — Context Applicability Provenance**  
Define deterministic derivation vs judgement-selected applicability and the provenance needed to make omissions/reconstruction auditable without a second manual context clock.

**BR-05 — Brownfield Representation Choice Confirmation**  
Use the above contracts to compare centralized TSVs, local typed metadata/front matter and a hybrid on the representative dry-run cases. Preserve the EKCP responsibilities; select the representation that avoids duplication while remaining queryable/validatable.

**BR-06 — Human Decision Comprehension Validation**  
Regenerate the D-016 brief after BR-01…05 and validate that the Human Owner can explain stage, problem, architecture, admission effect, non-goals and residual uncertainty without replaying the audit chain.

### L3. Non-blocking residuals that must remain visible

- F10 Review Premise Inheritance — separate epistemic/review-provenance gap unless Generic-Fit later couples it.
- F17 #225 positive scholarly end-to-end acceptance — separate system-acceptance gap; no manuscript work invented.
- future SQLite/graph/portal/package/workflow mechanisms — evidence-triggered only.
- exact future physical path map for every historical file — produced only after stable identity/representation semantics are fixed.

### L4. First legitimate implementation after refinement + explicit D-016 admission

Do **not** begin with repository-wide `git mv`.

The first admitted vertical engineering slice should be:

```text
representative existing brownfield files remain in place
→ establish stable engineering artifact/reference semantics
→ establish configuration/change currentness semantics
→ establish material-finding coverage + disposition semantics
→ implement the smallest validator/query needed to prove those contracts
→ seed a frozen representative inventory using real current paths
→ prove no second truth/current clock and no orphan-insight loophole
→ only then expand classification / generated views / context
→ physical migration later after semantics are stable
```

This sequence changes the earlier WP ordering in one useful way: **semantic contracts and brownfield proof precede physical IA migration, and context/query can be validated against legacy paths before moves are allowed to hide design errors.**

---

## M. Direct answers to the required closing questions

### 1. Which earlier errors would recur if SD-KA-01 implementation started now?

At least:

- a selected representation (`*.tsv`, `configuration.json`) could harden before its identity/transition semantics are proven;
- the new orphan-finding check could pass while unregistered material findings disappear;
- a Context Compiler could become a new manual reading-list clock because applicability provenance is underspecified;
- physical cleanup could make the repository look better while merely relocating unresolved currentness/trace semantics;
- a green engineering CI could be over-read as system closure;
- the latest holistic synthesis could again compress away F10/F17 and other residuals;
- a formally complete D-016 brief could again ask the Human to decide before understanding the loop.

### 2. Which findings must be operationalized before implementation?

At minimum F02/F04/F05/F06/F07/F08/F11/F12/F14/F15/F16/F20/F21/F22/F23/F24/F29/F30/F31/F32/F34, while F10/F17 remain explicit residuals rather than silently absorbed.

### 3. Which preliminaries are true blockers for Development/Admission Readiness?

BR-01 through BR-06 above. They are bounded refinements, not a new full architecture exploration.

### 4. Which EKCP parts survived?

The complete responsibility spine survives: Engineering Information Management, Engineering Configuration Management, material Finding disposition/trace, bounded change state, derived current/query/context views, developer entry/check, CI fitness and controlled brownfield migration.

### 5. Which parts were refined/falsified/expanded?

- `registered findings all dispositioned` is insufficient; finding **coverage completeness** is added.
- relation/source refs require stable identity/anchor semantics.
- configuration needs explicit transition/currentness semantics.
- context profiles need applicability provenance.
- central TSV files are no longer treated as pre-decided physical representation; responsibilities survive while representation is rechecked on brownfield cases.
- Human decision readiness requires observed comprehension, not document completeness.
- EKCP is explicitly prevented from claiming Review Premise Inheritance or #225 scholarly vertical acceptance closed.

### 6. Is the architecture still sufficient?

**Architecture class: yes, best-supported and still sufficient in responsibility coverage.**  
**Detailed admission-ready design: not yet.** Bounded refinements are required before implementation can proceed without inventing material semantics.

### 7. What is the first legitimate implementation work?

After BR-01…06 and explicit D-016 admission: an **in-place semantic contract + validator/query slice over representative real brownfield artifacts**, proving identity/currentness/finding-coverage/trace before any repository-wide migration.

### 8. Can a new Chat / Senior Developer understand this decision without replaying all audit history?

After this artifact, substantially more so: the current anti-regression findings, gap matrix, residuals, blockers, architecture disposition and first legitimate future slice are consolidated here. But the underlying repository still lacks the target engineering current/configuration/context mechanisms, so this pass itself does not claim EKR-01/25/29 are operationally solved. That is precisely what the later admitted implementation must prove.

---

## N. Anti-regression rule carried forward

For all subsequent work on this change:

> **Do not ask `what is the next component of the latest design?`**
>
> Ask: **which demonstrated failure are we closing, which prior finding constrains the work, which Requirement requires it, what proves closure, what returns to the whole, and which burden must not be transferred to the next Human/AI context?**

And after every material result:

```text
Result
→ changed owner/current truth
→ finding disposition changes
→ Requirement consequence
→ target-gap consequence
→ remaining-plan consequence
→ whole-system reconciliation
→ history/default-context consequence
→ new uncertainty / design re-entry if needed
```

`Current truth is not History.`  
`Persistence is not Promotion.`  
`Documentation is not Planning.`  
`Planning is not Execution.`  
`Evidence is not Decision.`  
`Verification is not Validation.`  
`Local PASS is not System Closure.`  
`Reduce reconstruction, not evidence.`  
`Relation correctness outranks relation completeness.`  
`Human is not the integration layer.`  
`Sufficient architecture first; simplify without loss second.`
