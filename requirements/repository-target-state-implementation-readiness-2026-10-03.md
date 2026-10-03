# Repository target state and implementation readiness — 2026-10-03

**Status:** NON-NORMATIVE ARCHITECTURE / IMPLEMENTATION-READINESS ANALYSIS  
**Parent analysis:** GitHub Issue #230  
**Refines:** `requirements/repository-knowledge-lifecycle-d016-decision-surface-2026-10-02.md`  
**Repository baseline:** `main@5d8178440d6406e39e1e6aff05359ee9d47fc403`  
**This artifact is not:** D-016 implementation admission, METHOD, Project scholarly state, a manuscript `NEXT ACTION`, #225 whole-system acceptance, a release decision, or authority to create a new product/repository.

## A. Executive finding

The next material step should not be another general audit and should not be a list of unrelated cleanup tasks. The repository now has enough evidence to define a concrete **target state** and use it as the qualification reference for a bounded system revision.

The strongest implementation direction remains the Class-B family from the 2026-10-02 adequacy audit, refined here as:

> **existing canonical research owners + explicit closable work/programme lifecycle + durable decision promotion + current/history/supersession semantics + rebuildable operational views + qualification against a persisted target state.**

This direction is supported because it closes the demonstrated lifecycle/composition failure family without requiring a second research-truth store. A larger restructuring remains valid if this design cannot satisfy the target-state tests; it is not rejected merely because it would be larger.

The repository should currently be treated as a **research-system development workspace with live reference research instances and reusable framework-like METHOD/contracts/tools**, not as an already qualified distributable template or versioned software product. There is no current external consumer contract, package boundary, GitHub Template state, release/tag history or compatibility/versioning contract. Therefore full product releases or SemVer are not currently justified. A qualified Git tag may become useful at the end of a material system revision as a stable baseline marker, but it is not required to begin the lifecycle revision.

The central operating-model correction is:

```text
current demonstrated failure
        ↓
accepted TARGET STATE
        ↓
traceable bounded work
        ↓
child/local result
        ↓
parent reconciliation
        ↓
durable meaning promoted to correct owner
        ↓
work closes
        ↓
history remains discoverable but inactive
        ↓
qualification against TARGET STATE
        ↓
programme closes
```

The target-state specification is an acceptance/qualification reference. It must not become a second current-state clock.

## B. Current repository baseline

Freshly resolved at the baseline above:

- `GOVERNING_OBJECTIVE.md` makes scholarly result/source understanding the product and requires auditability, canonical ownership and restartability.
- `AGENTS.md` requires complete applicable context rather than repository dumps, repository-first persistence, one durable fact/state per canonical owner and explicit D-016 admission for material research-system changes.
- `methodology/maintenance.md` owns D-016, propagation and programme/result reconciliation.
- `methodology/workflow.md` already requires reconstructable task owner, stage, bounded action, prerequisites, completion, non-goals and return condition.
- `methodology/quality-and-learning.md` already separates technical assurance, scholarly adequacy, specialist validation, Human/governance review and restartability.
- `MILESTONES.md` defines Issue = discrete work package and Milestone = optional planning/navigation grouping, never research authority.
- `DECISIONS.md` now includes D-021 for the already Human-admitted C1R architecture rationale.
- #225 remains the active Human-Owner-selected system programme; C1R is a LOCAL PASS ONLY and the positive real scholarly vertical fixture remains open.
- #230 remains open as the intentionally closable adequacy/lifecycle audit; its causal result is H3 / bounded mixed.
- all three manuscript Projects currently record no owner-selected active scholarly scope / `NEXT ACTION`.
- there are no open pull requests at this baseline.
- `main` is not protected and has no required status checks. The known promotion-enforcement gap is already explicitly deferred under #90 and is not silently reactivated by this analysis.
- the repository has one CI workflow, `source-contract.yml`, running Python 3.12, Source/Project validation, the unittest suite, fresh Project-context compilation and real-data regressions.
- the repository has no GitHub Releases and no Git tags.
- repository metadata reports `is_template=false`.
- there is no root Python packaging manifest such as `pyproject.toml`, `setup.py` or `requirements.txt`; current repository tooling is repo-local and largely standard-library Python.
- `.github/CODEOWNERS` currently routes only `GOVERNING_OBJECTIVE.md` to the Human Owner.
- `tools/` mixes reusable generic tooling (`source_contract.py`, `source_intake.py`, `project_context.py`, `outcome_context.py`) with Reg.-Ii.-5-specific research/fixture tooling. This is not itself a defect, but it makes the reusable-framework versus reference-fixture boundary worth keeping explicit.

## C. Target state / Zielbild

### C1. Repository role

At the current evidence level, one repository remains appropriate. It contains four distinguishable roles:

1. **reusable research-system layer** — governing objective, METHOD, decisions, contracts, reusable tools and templates;
2. **live research instances** — concrete Corpus and Project state used to perform and falsify the method/system;
3. **historical development/audit evidence** — completed audits, rejected concepts, result reviews, superseded states and Git/Issue history;
4. **derived operational views** — rebuildable contexts/navigation that expose current applicable state without owning it.

These roles must be distinguishable even when physically co-located. No evidence currently requires repository splitting.

### C2. Knowledge lifecycle

Persistable knowledge must be able to move through a meaningful lifecycle without forcing all persistent history into the active context:

```text
working/candidate
→ reviewed/dispositioned
→ accepted meaning promoted to durable owner where applicable
→ work/result becomes closed historical evidence
→ current views stop loading that history by default
→ rationale/evidence remains reachable on demand
```

Persistence may grow. Default active context must not grow proportionally.

### C3. Work/programme lifecycle

A bounded programme/revision owns a **qualified target outcome**, not an unlimited topic. A bounded work package owns one independently reviewable contribution to that outcome.

A programme may be longer-lived than a work package, but it must have:

- WHY;
- TARGET;
- INVARIANTS;
- admitted scope/non-goals;
- current child/work state;
- qualification/exit criteria;
- explicit decision-needed surface;
- closure semantics.

Its work history remains in closed Issues/PRs/audit artifacts. The parent must not become the archive by copying all child history into itself.

### C4. Decision lifecycle

Consequential accepted cross-project rationale that a future maintainer would otherwise have to reconstruct belongs in the existing `DECISIONS.md` owner unless Generic-Fit proves that owner insufficient.

Work Issues and analysis artifacts retain evidence/history. They do not remain open merely to preserve accepted rationale.

### C5. Current versus historical state

A fresh reader must be able to distinguish at least:

- current;
- historical/completed;
- superseded;
- candidate/deferred;
- accepted decision;
- derived view.

The implementation need not impose one universal enum. The required property is unambiguous currentness and recoverable supersession for the object classes where ambiguity has caused real failures.

### C6. Active context

A normal fresh context should load approximately:

```text
purpose/authority
→ current programme or explicit absence
→ current bounded work or explicit absence
→ applicable accepted decisions/requirements
→ evidence/rationale pointers
→ completion/return condition
```

Deeper audit history, rejected alternatives and forensic evidence load on challenge or when required by the task.

### C7. Derived operational view

A current programme/work view should be rebuildable from established owners and GitHub work metadata. It may expose:

- active/terminal programme;
- current bounded work;
- accepted decisions relevant to it;
- qualification state;
- decision needed;
- exit criteria;
- pointers to evidence/history.

It must never invent Project priority, scholarly `NEXT ACTION` or accepted decisions.

A key design requirement remains unresolved before implementation: system-programme/work metadata currently lives legitimately in GitHub Issues while canonical research truth lives in repository files. Any derived view must define this GitHub/repository boundary explicitly rather than creating a duplicate persistent programme clock.

### C8. Software/tooling architecture

Current tools should remain repo-local scripts while that is sufficient. A package/API boundary is justified only when reuse, installation, external consumption or internal coupling demonstrates the need.

`src/` layout, packaging metadata, dependency management or a service/API must not be introduced as style normalization alone.

### C9. QA / qualification

The system must distinguish:

- technical correctness;
- repository/owner consistency;
- migration safety;
- restartability;
- Human usability;
- scholarly adequacy;
- specialist validation;
- product/release qualification where applicable.

A green CI run is never the whole-system Definition of Done.

### C10. Release / promotion / consumption

For current internal development, exact Git commit + PR/result review is sufficient as the technical identity of a qualified state. A named tag is optional until a real need exists for a durable human-readable baseline.

GitHub Releases, SemVer and separate template artifacts require a real consumer/compatibility contract first.

### C11. Human / AI / specialist interface

The Human Owner decides purpose, material priority/scope, material D-016 admission and consequential use. AI and deterministic tooling should resolve routine owner/state/context mechanics. Qualified specialists own independent domain judgement where triggered.

The Human Owner must not become the repository synchronizer, gate interpreter or substitute specialist.

### C12. Fresh-maintainer experience

A fresh capable maintainer without this chat must be able to reconstruct:

- what the repository currently is;
- current versus historical system programmes;
- current work or explicit absence;
- accepted architecture decisions;
- why those decisions exist;
- which material architecture is admitted versus only proposed;
- what can close now;
- what remains open and why;
- where deeper evidence lives;
- whether a release/qualified consumer baseline exists.

## D. System Definition of Done for the lifecycle revision

The material lifecycle revision is complete only when all applicable properties below are demonstrated:

1. current system programme/work state is discoverable without replaying Issue chronology;
2. historical programme/audit evidence remains recoverable without remaining mandatory default context;
3. programme, bounded work, audit and accepted decision roles are distinguishable;
4. bounded work can close after its result is persisted and its parent consequence is reconciled;
5. a programme can close without losing accepted rationale or spawning an implicit successor;
6. accepted cross-project decisions are promoted to the durable decision owner when warranted;
7. current/superseded/history ambiguity is eliminated on the operational surfaces that previously caused reconstruction debt;
8. parent/child completion cannot promote a local PASS into programme/system acceptance;
9. a rebuildable current-context view can expose the accepted target/current work without becoming a second authority;
10. active-context size is bounded by applicability/current work rather than accumulated historical volume;
11. deeper provenance/rationale can be expanded on demand;
12. exact-head technical assurance is run after final material mutation;
13. scholarly/Human/specialist boundaries remain intact;
14. no Project scope or scholarly `NEXT ACTION` is created from system-maintenance state;
15. a fresh-maintainer acceptance fixture passes without old chat;
16. product/release/consumer status is explicitly dispositioned rather than assumed;
17. the revision programme itself can close and leave no permanent meta-Issue required for normal operation.

## E. Implementation-candidate register

| ID | Candidate | Primary disposition | Why |
|---|---|---|---|
| IC-01 | Generic work/programme lifecycle + closure contract | **READY FOR D-016 ADMISSION** | Directly closes the demonstrated closability/result→owner→parent→history gap. Material METHOD/work semantics. |
| IC-02 | Current/history/supersession + durable decision-promotion semantics | **READY FOR D-016 ADMISSION; likely fuse with IC-01** | Same failure family; accepted decisions and currentness must stop depending on chronology. |
| IC-03 | Rebuildable research-system operational status / bounded context | **NEEDS DESIGN AFTER IC-01/02 SEMANTICS** | Strong target-state fit, but source-of-current-work/GitHub boundary must be explicit before code. |
| IC-04 | Deterministic stale/current/closure/supersession checks | **CONDITIONAL IMPLEMENTATION** | Valuable only after stable semantics exist; otherwise code would freeze an immature taxonomy. |
| IC-05 | Existing-surface migration/reconciliation | **CONDITIONAL IMPLEMENTATION** | Required after the accepted lifecycle representation is known; should not lead the design. |
| IC-06 | Fresh-maintainer + programme-closure qualification fixture | **KNOWN NECESSARY WORK** | This is the proof that the revision removed reconstruction debt instead of moving it. |
| IC-07 | Review-premise / evidence-basis provenance | **NEEDS SEPARATE DESIGN / GENERIC-FIT** | Real gap, but partly scholarly and not proven to share the same lifecycle representation. |
| IC-08 | Qualified baseline Git tag after revision | **CONDITIONAL** | Useful only if a stable named consumption/rollback/qualification marker adds value beyond exact SHA. |
| IC-09 | GitHub Release / SemVer / distributable framework-template | **NOT READY** | No current consumer/API/compatibility contract, package boundary or template product. |
| IC-10 | Python package / `pyproject.toml` / `src/` refactor | **NOT WARRANTED NOW** | Current tools are repo-local stdlib scripts; no demonstrated install/distribution/coupling need. |
| IC-11 | Native branch protection / required checks | **REAL GAP, EXPLICITLY DEFERRED UNDER #90** | Do not create a substitute or silently reactivate the Human-deferred platform decision. |
| IC-12 | #225 positive real scholarly vertical fixture | **SEPARATE OPEN PROGRAMME GAP** | Required for #225 acceptance; not a lifecycle-architecture implementation task and no manuscript scope may be fabricated. |
| IC-13 | Framework/template/consumer product boundary | **NEEDS REAL CONSUMER / HUMAN PRODUCT DECISION** | Current repository is not a GitHub template and carries live research/history; external consumption requirements are absent. |
| IC-14 | Requirements/audit artifact reorganization | **NEEDS DESIGN EVIDENCE; NOT STANDALONE WORK** | Artifact heterogeneity is real, but physical directory movement is justified only if target lifecycle/currentness cannot be achieved through role/status/pointers. |

### IC-01 / IC-02 proposed material scope

These are best treated as one integrated design unless falsification shows independent lifecycles. The admitted semantics should cover:

- durable normative/canonical owner;
- accepted decision;
- bounded programme/revision;
- bounded work package;
- execution cursor;
- audit/analysis evidence;
- candidate/deferred work;
- historical evidence;
- rebuildable view;
- DoR/DoD for programme and work;
- parent reconciliation;
- result promotion;
- closure;
- supersession/currentness sufficient for fresh-reader resolution.

They do **not** require a universal database or lifecycle enum.

### IC-03 design question that must be resolved before coding

The repository currently permits GitHub Issues/PRs to own work/audit metadata while forbidding them from becoming canonical research truth. #225 itself is the work/programme owner. Therefore the operational status design must choose explicitly between:

1. deriving current system-work state from GitHub work owners plus repository decisions/method;
2. adding a new repository programme-state owner;
3. another mechanism justified by evidence.

Option 2 risks creating the second planning clock the audits repeatedly rejected. The default design hypothesis should therefore remain **derive from existing work owner + repository canonical owners**, but implementation must prove restartability and availability rather than assume it.

## F. Target-state ↔ candidate traceability

| Target property | Current gap | Candidate | Closure proof |
|---|---|---|---|
| bounded closable programmes/work | incomplete generic semantics | IC-01/02 | programme + child fixture can close with durable result retained |
| currentness without archaeology | chronology/stale surfaces | IC-01/02/03 | fresh reader identifies current state without replay |
| history preserved but inactive | history and current mixed on some surfaces | IC-01/02/05 | closed historical fixture remains reachable but absent from default context |
| durable decision rationale | prior C1R gap showed reconstruction need | IC-02 | accepted result resolvable through `DECISIONS.md` without issue archaeology |
| bounded active context | persistent corpus/audit growth | IC-03 | fresh task context contains applicable pointers, not historical dump |
| deterministic currentness checks | no generic stable contract yet | IC-04 | seeded stale/superseded fixture is detected without semantic invention |
| full revision closure proof | local PASS risk | IC-06 | independent fresh-maintainer target-state test passes |
| evidence-basis independence | #171 premise-inheritance gap | IC-07 | reviewer can distinguish directly inspected vs inherited basis |
| named consumption baseline | none today | IC-08 | only if consumer/qualification use case demonstrates benefit |
| distributable product | no present contract | IC-09/13 | future real consumer passes clean bootstrap/upgrade/compatibility tests |

## G. Open-problem freshness / anti-drift model

Open work should be kept fresh **event-driven**, not by a second periodically maintained status database.

### Programme parent

A closable programme/revision parent should maintain only a compact current control view:

```text
WHY
TARGET
INVARIANTS
ADMITTED SCOPE / NON-GOALS
CHILD WORK / RESULTS (links)
CURRENT
DECISION NEEDED
QUALIFICATION / EXIT
```

Do not append audit history into this control view. GitHub history and linked closed work already preserve it.

### Child work

Each child must have:

```text
PARENT TARGET
TARGET PROPERTY / CONTRIBUTION
INPUT OWNERS
BOUNDED RESULT
NON-GOALS
DoR
ACCEPTANCE
DoD
RETURN / RECONCILIATION
WHAT IT CANNOT ESTABLISH
```

A child closes independently when its DoD is met. Parent state changes only through explicit reconciliation.

### Freshness triggers

Update/reconcile parent/current surfaces only when a material event occurs:

- child closes or materially changes result;
- accepted decision changes;
- D-016 admission/disposition changes;
- programme qualification changes;
- work is superseded/deferred/reactivated;
- a current pointer becomes stale;
- a new dependency/authority ceiling is established.

No calendar heartbeat is required merely to keep the system looking active.

### Deferred backlog

Existing trigger-based issues (#1/#2/#3/#4/#6/#12/#13/#22/#62/#90/#162/#202) are generally the right pattern: problem/benefit, why not now, observable trigger and DoD. They should remain inactive until their trigger actually fires. A future lifecycle mechanism should make this distinction easy to read, not auto-schedule them.

## H. Work/programme lifecycle target model

```text
authorized problem / target-state gap
        ↓
D-016 admission if material
        ↓
closable programme/revision parent
        ↓
only necessary bounded work packages admitted on demand
        ↓
branch / implementation / evidence / review
        ↓
local result
        ↓
correct durable owner(s) updated
        ↓
parent reconciliation
        ↓
child closed / history inactive
        ↓
qualification matrix re-evaluated
        ↓
programme DONE or exact residual/ceiling
        ↓
programme closed; no implicit successor
```

A Milestone is useful only if several admitted children need grouping. It remains navigation, not authority. A permanent open Issue is not required to preserve the programme once accepted results are promoted and qualification is recorded.

## I. Release / tag / qualification assessment

### What is the current product?

The governing product is scholarly result/source understanding. The repository is currently a **research-system development workspace**, not a separately packaged software/library/template product.

### Current evidence

- no Git tags;
- no GitHub Releases;
- repository `is_template=false`;
- no package manifest or public API/version compatibility contract;
- reusable tools are repo-local scripts;
- live scholarly Corpus/Project state and development/audit history coexist in the repository.

### Options

#### R0 — `main` + exact SHA + PR/result review

**Current default; sufficient for internal development.**

Strength: no false product boundary; exact state is already addressable.

Limit: no human-readable named qualification baseline for future consumers.

#### R1 — qualified Git tag

**Conditional candidate after a material revision closes.**

Use only if a named stable baseline materially improves rollback, consumer bootstrap or qualification reference. A tag must point only to a fully qualified exact commit and must not imply scholarly publication truth beyond its stated qualification.

#### R2 — GitHub Release

**Not currently justified.**

Useful when there is a release artifact, external/internal consumer handoff or changelog/consumption contract. None is established today.

#### R3 — SemVer framework release

**Not ready.**

SemVer requires a defined compatibility surface/API and consumers. The repository currently has neither.

#### R4 — development repo + separately qualified template/consumer artifact

**Potential future architecture, not current work.**

This becomes serious only if a clean consumer starting state must exclude development history/live research and if upgrades need a defined migration/compatibility model.

### Release conclusion

Do **not** create releases merely to look like professional software. First finish the target-state/qualification design. At revision close, re-evaluate whether an annotated qualification tag has a concrete consumer/rollback benefit. Full GitHub Release/SemVer/template product remains trigger-based.

## J. Framework / template / consumer assessment

The repository already contains reusable framework-like components, but that does not make the whole repository a template product.

### Current best-supported classification

```text
paleo-type repository
├─ reusable research-system layer
├─ live/reference research instances
├─ research-system development history/evidence
└─ internal project/source templates
```

The internal `templates/project/` and `templates/source/` directories are object/bootstrap templates inside the research system, not evidence that the GitHub repository itself is a qualified clone-and-go template.

### No split now

A separate framework/template repository is not justified by current evidence. Splitting would add compatibility/versioning/migration obligations without a demonstrated consumer.

### Trigger for productization

Re-open the product-boundary decision when a real consumer must:

- start a new research repository without current live-project/development history;
- receive framework updates across repositories;
- rely on compatibility guarantees;
- install/use tooling independently;
- consume a formally qualified baseline.

Before external distribution, licensing, documentation, compatibility policy and data/source-rights boundaries would also require explicit treatment. The current repository metadata has no license.

## K. Senior engineering review

| Area | Finding | Disposition |
|---|---|---|
| branch protection / required checks | `main` unprotected; known deterministic risk | **REAL GAP, already DEFERRED #90** |
| rulesets | unavailable under current private/free capability | **PLATFORM BOUNDARY; do not work around silently** |
| CI | one clear Python 3.12 workflow runs contract + unit/governance + context + real-data checks | **GOOD CURRENT BASELINE** |
| exact-head assurance | PR and main-push CI support exact-state checking, but enforcement is voluntary | **GOOD MECHANISM + KNOWN #90 RISK** |
| test layering | deterministic, governance, real-data and source-critical tests already exist | **GOOD; add lifecycle tests only after semantics stabilize** |
| package/dependencies | no `pyproject`/dependency manifest; tools are stdlib/repo-local | **NOT A CURRENT DEFECT** |
| `src/` layout | no demonstrated installable runtime/package | **OVERENGINEERING RISK NOW** |
| tooling cohesion | generic and Reg.-Ii.-5 fixture tools coexist under `tools/` | **MAKE ROLE EXPLICIT; MOVE ONLY IF MAINTENANCE FAILURE APPEARS** |
| CODEOWNERS | only Governing Objective is explicitly routed | **CURRENTLY PROPORTIONAL; broader rules matter only with real reviewer topology/enforcement** |
| merge modes | merge/squash/rebase all enabled | **NICE-TO-HAVE POLICY QUESTION, not current correctness gap** |
| branch cleanup | merged branches are not auto-deleted | **MINOR HYGIENE ONLY** |
| repository template state | `is_template=false` | **CONSISTENT WITH CURRENT NON-PRODUCTIZED STATE** |
| releases/tags | none | **NOT A DEFECT absent consumer/qualification need** |
| license | none | **PRODUCTIZATION/DISTRIBUTION GAP, not current internal-research blocker** |
| diagnostics | current CLI tools return explicit errors/status and CI states assurance limits | **GOOD BASELINE** |
| YAML parsing | custom simple scalar parser fits current project.yml shape | **TRIGGER-BASED TECHNICAL DEBT if metadata becomes structurally richer** |
| stale/current surfaces | historically demonstrated and partly repaired | **REAL LIFECYCLE GAP** |
| operational status | Project contexts exist; cross-programme current work still partly Issue/navigation based | **REAL DESIGN CANDIDATE IC-03** |
| review evidence basis | premise inheritance remains possible | **REAL SEPARATE DESIGN GAP IC-07** |

## L. Qualification strategy

A future admitted revision should qualify separately:

### Technical correctness

- existing full deterministic/unit/governance suite green;
- lifecycle/status checks green if added;
- final head/merge state rechecked.

### Repository/owner consistency

- one fact/state per owner;
- no duplicated programme/research truth;
- all references/current pointers resolve;
- historical artifacts cannot masquerade as current owners.

### Migration safety

- historical Issues/audits/decisions remain reachable;
- current Project/Corpus truth unchanged unless separately admitted;
- no loss of prior decision/provenance chain;
- rollback does not lose canonical research state.

### Restartability

Independent fresh context can reconstruct the programme target, current/terminal work, accepted decisions, residuals and no-active-work states without old chat.

### Human usability

Human Owner sees target, current state, real decisions needed and qualification—not repository archaeology or internal gate/tool choice.

### Scholarly adequacy

No lifecycle/read-model change launders technical status into scholarly truth or changes open interpretation.

### Specialist validation

Triggered only where actual scholarly meaning/evidence topology requires independent specialist judgement.

### Release/template qualification

Not triggered now. If a future consumer product exists, add fresh-consumer/bootstrap/upgrade/compatibility fixtures before naming a release.

## M. Candidate work graph

Do not create all of these Issues now. This is the smallest currently justified dependency graph **after Human D-016 admission**:

```text
REVISION TARGET / QUALIFICATION PARENT
│
├─ WP-A  Lifecycle + current/history + decision-promotion contract
│        (IC-01 + IC-02; material design/METHOD)
│
├─ WP-B  Operational current-state / bounded-context design
│        depends on WP-A
│
├─ WP-C  Stable enforcement + necessary existing-surface reconciliation
│        only the checks/migration justified by WP-A/B
│
└─ WP-D  Fresh-maintainer + closure qualification
         proves the revision against the target state
```

Separate tracks, not automatically children of this revision:

- Review-Premise/Evidence-Basis provenance (IC-07) unless Generic-Fit proves it shares the same accepted representation;
- #225 positive scholarly vertical fixture (IC-12);
- #90 branch-protection risk, still deferred;
- template/release/productization work, trigger-based only.

### Work-package readiness

**WP-A** may be created only after explicit D-016 admission.  
**WP-B** is not implementation-ready until WP-A fixes the semantic owner/currentness model.  
**WP-C** is not specifiable until the stable semantics and migration set are known.  
**WP-D** can be designed now as acceptance criteria but executes against the final integrated state.

## N. READY NOW versus NOT READY

### Ready now without material admission

- preserve this target-state/readiness analysis as decision support;
- keep #230 bounded and do not turn it into the implementation parent;
- keep known deferred issues deferred unless their trigger fires;
- perform ordinary stale-pointer maintenance if a newly found statement is unambiguously wrong and no semantics change.

### Ready for Human D-016 decision

- integrated IC-01/IC-02 lifecycle/currentness/decision-promotion revision;
- target-state-driven programme model above;
- explicit principle that operational views derive from work/canonical owners and do not become a new research-truth store.

### Not ready for implementation

- operational cross-programme status tool (owner/GitHub boundary unresolved until lifecycle contract is accepted);
- lifecycle validators/status enums;
- broad repository-directory migration;
- Review-Premise topology implementation;
- template split;
- Python packaging/src refactor;
- SemVer/GitHub Release.

### Deferred by existing authority

- native promotion enforcement under #90;
- direct cross-chat coordination under #162;
- plural-direction mechanism under #202 until its real-use trigger fires;
- other future feature issues until their explicit triggers fire.

## O. Human-Owner decision surface

### Decision 1 — lifecycle revision admission

**Question:** May the repository proceed from analysis into a material revision implementing the target-state properties represented by IC-01/IC-02 and then, conditionally, IC-03–IC-06?

**Recommendation:** **ADMIT the bounded target-state/lifecycle revision**, provided the admission preserves the staged falsification rule below rather than pre-authorizing every candidate implementation.

Recommended admitted boundary:

1. establish explicit generic closable programme/work roles and DoR/DoD/return semantics;
2. establish current/history/supersession and accepted-decision-promotion semantics sufficient for fresh-reader resolution;
3. retain GitHub Issues/PRs as work/audit metadata rather than creating a new research-truth store;
4. design a rebuildable operational current-state/context view only after those semantics are stable;
5. add deterministic checks only for semantics proven stable;
6. reconcile only existing surfaces proven necessary;
7. finish with independent fresh-maintainer and closure qualification;
8. permit a larger architecture if this class is falsified as insufficient, but require a return to D-016 for a genuinely new canonical state architecture.

Owner choice remains:

`ADMIT | REFINE | DEFER | REJECT`

### Decision 2 — release/product boundary

**Recommendation:** **DEFER a product/release architecture.** Continue using exact Git commits/PR qualification. Re-evaluate an annotated qualification tag at revision closure. Do not adopt GitHub Releases/SemVer/template split until a real consumer and compatibility contract exist.

No Human decision is required now unless the intended product is in fact to distribute `paleo-type` immediately as a reusable template/framework to other repositories/users. If that intent exists, it changes the requirements and must be stated explicitly before the lifecycle implementation is finalized.

### Decision 3 — #230 closure

#230 should remain a bounded audit owner, not become the revision programme. After the Human Owner dispositions Decision 1, its causal/decision purpose is complete and it should close. Any admitted implementation should receive a new closable programme/revision owner with the target state above.

## P. What should not be built now

Absent new evidence/admission, do not build:

- universal workflow engine;
- central scholarly state machine;
- event-sourced research store;
- new programme database;
- capability/discipline registry;
- generic planner;
- universal lifecycle enum merely for neatness;
- new ADR framework replacing `DECISIONS.md`;
- physical `requirements/` reorganization for aesthetics alone;
- Python package/src layout without a real runtime/distribution boundary;
- GitHub Release/SemVer without a consumer contract;
- template repository split without a fresh-consumer/upgrade use case;
- substitute branch-protection machinery that circumvents #90's explicit defer;
- an immortal parent Issue that stores both current state and all history.

## Q. What can now close

- **#230:** analytically complete and closure-ready **after** Human disposition of the D-016 lifecycle decision. Its implementation work should not be appended to #230.
- historical local audits/work packages already marked complete should remain history and need not be reopened merely to fit the new target model.

No claim is made here that #225 can close.

## R. What must remain open / explicitly unresolved

- #225 until its whole-system Definition of Done, especially the real positive scholarly end-to-end fixture, is satisfied or otherwise Human-dispositioned;
- the lifecycle architecture until Human D-016 disposition;
- Review-Premise/Evidence-Basis provenance as a distinct design question unless Generic-Fit later fuses it;
- #90 risk under its explicit defer state;
- product/template/release questions until a real consumer/qualification trigger exists;
- scholarly Project scopes remain explicitly absent until Human Owner selection or another canonical authority establishes one.

## S. Next bounded action after admission

If Decision 1 is `ADMIT`, the first bounded work package should be **WP-A — Lifecycle + current/history + decision-promotion contract**.

### WP-A DoR

- Human D-016 admission references this target-state analysis and the 2026-10-02 D-016 surface;
- target state and System DoD above are accepted as the qualification reference;
- no manuscript Project scope is activated;
- #225 acceptance remains unchanged;
- existing work/audit owner semantics in maintenance/workflow/MILESTONES are treated as inputs, not discarded.

### WP-A required result

A concrete, reviewable generic contract answering:

- which owner classes are durable versus closable;
- what programme/work DoR and DoD mean;
- exact parent reconciliation semantics;
- when accepted decisions are promoted;
- how current/history/superseded state is resolved;
- what survives after closure;
- how a successor can be authorized without extending the old parent;
- which semantics are deterministic enough for tooling;
- which current surfaces require migration;
- whether the proposed Class-B architecture still closes the demonstrated failure family.

### WP-A DoD

- semantics are precise enough to design WP-B without inventing a second state clock;
- alternatives/falsifiers are recorded;
- affected canonical owners are explicit;
- no speculative tooling is implemented;
- parent target-state contribution is reconciled;
- a fresh maintainer can understand the accepted contract without old chat.

## Final disposition

The repository has moved beyond the stage where another broad audit is the main need. The most important missing control is now a **target-state-driven, closable implementation programme** whose children are admitted only when they close a traced target property.

The correct next architecture decision is not "which small fix next?" It is whether to admit the bounded lifecycle/currentness/decision-promotion revision above and then force every implementation package to prove a target-state contribution.

Releases are currently secondary: qualification is necessary; product releases are not. A named Git tag may later be useful as a qualified baseline, but the repository first needs a clearly qualified system state and a real consumer reason to name/distribute it.
