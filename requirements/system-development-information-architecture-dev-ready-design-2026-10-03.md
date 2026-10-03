# System-development information architecture and development-method design — 2026-10-03

**Status:** NON-NORMATIVE DEV-READY DESIGN / **D-016 DECISION READY / NOT ADMITTED**  
**Repository baseline:** `main@cdc70b04b848a8012d04c27ad9760972ee45c490`  
**Supersedes for current process status:** `requirements/human-decision-readiness-design-process-rebaseline-audit-2026-10-03.md` (`NOT READY FOR D-016 DECISION`)  
**Preserves:** all earlier lifecycle/D-016/target-state/Product/Human-proxy artifacts as evidence and prior solution hypotheses.  
**This artifact is not:** D-016 admission, METHOD, implementation permission, manuscript scope/`NEXT ACTION`, a workflow engine, or a Wirknetz Runtime/Skill/Bridge.

## A. Executive disposition

The requested re-baseline → analysis → Requirements → targeted Research → competing concepts → detailed design process has now reached the **DEV-READY** boundary.

The deepest supported diagnosis is not `too much history` and not `missing documentation`.

The coupled failure is:

> **system-development current/target/planning state is insufficiently separated from development evidence/history, while the method that should establish which upstream development work is sufficient before implementation is only partly operationalized.**

Two loops result:

```text
HISTORY-AS-SYNTHESIS
finding → audit/evidence → local closure
→ accepted/current programme meaning not fully promoted into a small current plan
→ next context reconstructs current/target/plan from history
→ more audit/evidence
```

```text
PREMATURE-WORK-SHAPING
finding → plausible solution family → bounded WP
→ analysis inside already narrowed solution space
→ locally excellent implementation/review
→ upstream sufficiency was never independently established
→ residual problem returns
```

The selected architecture is therefore a **bounded system-development revision architecture**, not a better archive or permanent mega-plan. It separates:

1. actual repository configuration — what is true now;
2. revision Requirements baseline — what must be achieved, solution-independently;
3. revision Design baseline — selected target solution;
4. bounded Programme Plan — remaining admitted delta from current to target;
5. Evidence/History — audits, research, Issues/PRs/Git retained on demand;
6. accepted consequential rationale — `DECISIONS.md`.

Orthogonally, every material revision needs **development-method coverage**: explicit evidence that the required problem-framing, analysis, Requirements, Research, concept and design work is sufficiently complete before implementation is shaped. This is risk/state-tailored, not a waterfall.

Current state after this artifact:

> **DEV-READY / D-016 DECISION READY / NOT ADMITTED.**

No implementation follows without explicit Human-Owner D-016 admission.

## B. Repository-first authority and boundary

Fresh authority confirms:

- scholarly result/source understanding is the product; system infrastructure is subsidiary;
- Human Owner controls material D-016 admission, purpose and material priority/scope;
- AI/tooling owns routine bounded work already authorized;
- one durable fact/state has one canonical owner;
- complete **applicable** context is required, not whole-history replay;
- GitHub Issues/PRs are work/audit metadata, not canonical scholarly truth;
- D-016 remains `analysis → requirements → concept → owner review / explicit implementation admission → development → tests/loss checks → result review`;
- Domain→Dev must carry problem/evidence/required meaning/scope/acceptance without forcing implementation guesses;
- fresh human/AI contexts must understand and challenge consequential state without old chat.

#225 and #230 remain closed work metadata; neither is reopened. All manuscript Projects remain without an owner-selected active scholarly task, so this design creates no manuscript `NEXT ACTION`.

## C. Transfer from Wissensarbeit — properties, not architecture

The comparator contributes two falsification lessons.

First, **History can grow correctly while the active programme map fails to shrink and mature**. The error is not preserving history; it is requiring history replay to determine current planning meaning.

Second, a repository can already describe a strong iterative lifecycle but still shape bounded work too early. The transferable property is:

```text
problem/state
→ determine which development capabilities are required
→ establish sufficiency
→ only then shape implementation work
```

not:

```text
finding → attractive solution class → WP → analyse within that class
```

`Wirknetz` remains useful only as a trace/design-method lens: preserve distinctions among source/Human statement, Intent, Gap, Requirement Candidate, accepted Requirement, Concept/Design, Work, Result, Verification/Validation, correction/supersession and uncertainty. No Runtime/Skill/Bridge/graph is justified.

## D. Failure families and root causes

| ID | Finding / hypothesis | Disposition |
|---|---|---|
| F1 | History is partly used as a query mechanism for current system meaning | confirmed |
| F2 | Current configuration, target design and programme plan are not cleanly distinct system-development information products | confirmed |
| F3 | `requirements/` contains Requirements, audits, concepts, admissions, result reviews and history with heterogeneous lifecycle roles | confirmed; physical co-location alone is not the defect |
| F4 | Local closure does not always make the programme consequence explicit/current | confirmed |
| F5 | bounded work can be solution-shaped before upstream sufficiency is established | confirmed failure risk; recent lifecycle work is a live fixture |
| F6 | strong admission/CI/review/restart controls can mask upstream framing/design weakness | supported |
| F7 | Human formal authority can remain intact while decision readiness is insufficient | demonstrated by recent `ausführen` interaction |
| F8 | meta-audits can become a growth loop when accepted meaning is not promoted/deactivated | supported |
| RC1 | `too much history` is the primary cause | falsified |
| RC2 | insufficient Current/Target/Plan/History separation | **primary root cause** |
| RC3 | missing programme layer is the whole problem | partial; does not explain premature solution shaping |
| RC4 | development-method operationalization is a coupled deeper gap | **primary root cause** |
| RC5 | better summaries alone are sufficient | falsified |
| RC6 | permanent global plan / event store / workflow engine required | not supported |
| RC7 | derived view alone can solve missing programme truth | falsified; derivation needs an owner to derive from |

## E. Targeted Best-Practice / SOTA findings

Only design-relevant sources were researched.

1. **ISO/IEC/IEEE 29148** treats Requirements Engineering/Management as life-cycle work and defines traceability between stakeholder needs, requirements and downstream implementation. Consequence: material revision Requirements need an independent traceable baseline.
2. **NASA Systems Engineering Handbook** separates stakeholder expectations, technical Requirements, logical decomposition and design solution; it also separates Technical Planning, Configuration Management, Technical Data Management, Technical Assessment and Decision Analysis. Consequence: plan, baseline/configuration, retained technical data and decisions are distinct responsibilities.
3. **NASA/SEBoK configuration-baseline guidance** treats an approved baseline as the reference for subsequent development while retaining change/history separately. Consequence: current/target work should consume a baseline, not replay chronology.
4. **SEBoK 2026 process guidance** explicitly treats lifecycle processes as concurrent, iterative, recursive and tailored. Consequence: use capability/sufficiency coverage, not a mandatory stage machine.
5. **NASA Human Systems guidance** requires decision aids to expose explanations/rationale and consequences for informed decisions and situation awareness; NIST likewise stresses differentiated Human/AI roles and role-appropriate transparency. Consequence: `ADMIT | REFINE | DEFER | REJECT` is only safe after the underlying decision state is understandable.
6. **ADR practice** supports keeping accepted decision context/rationale/consequences separate from implementation chronology. Consequence: retain `DECISIONS.md` as accepted cross-project rationale owner.
7. **CQRS/Event Sourcing** demonstrates the useful principle `history ≠ current projection`, but adds synchronization/runtime complexity. Git already provides development history here; an event store is not warranted.

No external framework is adopted wholesale.

## F. Solution-independent Requirements baseline

| ID | Required property |
|---|---|
| SDR-01 | System-development architecture remains subsidiary to scholarly product and creates no manuscript priority. |
| SDR-02 | Fresh context identifies current material revision or explicit absence without audit/Issue chronology replay. |
| SDR-03 | History remains complete/retrievable but is not default current context. |
| SDR-04 | Current configuration, Requirements, Target Design, Plan, Work, Decision, Evidence and History have distinguishable roles/owners. |
| SDR-05 | One durable fact/state has one canonical owner; views reference/derive rather than copy. |
| SDR-06 | A bounded system revision can close and become inactive without losing rationale/evidence. |
| SDR-07 | Every material WP closure explicitly reconciles its programme consequence. |
| SDR-08 | The active Programme Plan shrinks/changes as work closes; remaining delta is not reconstructed from history. |
| SDR-09 | Requirements remain solution-independent and trace to demonstrated failure/need. |
| SDR-10 | Development-method coverage is risk/state-tailored rather than a fixed waterfall. |
| SDR-11 | Implementation WPs are shaped only when material design choices are sufficiently bound. |
| SDR-12 | Exploratory concepts may precede formal Requirements but cannot become admitted architecture without trace/support. |
| SDR-13 | Human material decisions expose stage, evidence, Requirements, alternatives, uncertainty and consequences. |
| SDR-14 | Routine work inside admitted authority does not require Human relay/confirmation. |
| SDR-15 | Context economy reduces reconstruction, never evidence/provenance/uncertainty. |
| SDR-16 | Uncertainty/non-conclusion may block DEV-READY where material. |
| SDR-17 | Issues/PRs remain bounded work/review containers; chronology is not programme state. |
| SDR-18 | Accepted consequential rationale is durable outside work chronology. |
| SDR-19 | No second execution clock: programme plan owns programme delta, work owner owns local execution detail. |
| SDR-20 | No event store/workflow engine/registry/graph/package without demonstrated need. |
| SDR-21 | Design survives materially different system-change fixtures. |
| SDR-22 | Exact-head assurance follows final material mutation. |
| SDR-23 | Existing Source/File/Project scholarly owners are untouched unless directly required. |
| SDR-24 | DEV-READY, ADMITTED, IMPLEMENTED and ACCEPTED remain distinct states. |

## G. Development-method coverage / DEV-READY contract

For each material system revision, assess these capabilities semantically:

```text
Problem framing
Root-cause / systems analysis
Requirements / acceptance
Research / SOTA / domain evidence
Concept exploration / trade study
Detailed design
Implementation planning
Implementation
Verification
Validation / Human or specialist acceptance
Integration / reconciliation
Learning / maintenance
```

Each is effectively `required-open | required-satisfied | not-required-with-rationale | blocked | re-entered`; literal enums are not mandated.

A material revision is DEV-READY only when:

1. problem/failure is bounded and evidence-linked;
2. competing material root-cause explanations are sufficiently dispositioned;
3. Requirements/acceptance are explicit and solution-independent;
4. material Research gaps are resolved or explicitly not required;
5. materially different concepts were compared where credible alternatives exist;
6. selected design is specific enough that implementation needs no new material architecture/semantic choice;
7. migration/compatibility/loss risks are defined;
8. verification/validation/fresh-context tests exist before implementation;
9. remaining uncertainty is non-blocking or exposed as exact Human/specialist decision;
10. Human can understand what admission would and would not authorize.

This does not create ceremony for trivial bugs. A small defect may legitimately use existing Requirements/design and mark Research/concept exploration `not-required-with-rationale`.

## H. Architecture options

### A — Better README/index/summaries
Rejected: freshness/history coupling remains; no programme truth owner.

### B — Derived current view from existing Issues/repo only
Rejected as root solution: a view cannot safely derive missing programme truth; optional later over stable owners.

### C — Permanent global programme plan
Rejected: reproduces immortal planning/history mega-owner.

### D — Bounded revision baselines + bounded Programme Plan + normal Git/Issue history
**SELECTED.** Separates target/plan/history, can close, maps to D-016, and supports method coverage.

### E — Event store/CQRS
Rejected for current scope: principle useful; runtime/storage complexity unsupported.

### F — Workflow engine / autonomous development-path compiler
Rejected for current implementation: select method-coverage semantics, not a universal engine.

### G — Bulk reorganization of historical `requirements/`
Rejected: physical neatness does not solve currentness and creates churn/link risk.

## I. Selected target information architecture

Existing owners remain unchanged:

```text
GOVERNING_OBJECTIVE.md   purpose / precedence
AGENTS.md                stable guardrails
DECISIONS.md             accepted shared rationale
methodology/             reusable METHOD
corpus/ + projects/      scholarly truth/current Project state
Git                      version/change history
GitHub Issues/PRs        bounded work/review metadata
requirements/            existing historical analysis/research/design evidence
```

After D-016 admission, add only the missing material system-development revision role:

```text
system-development/
  README.md
  revisions/
    <revision-id>/
      REQUIREMENTS.md
      DESIGN.md
      PLAN.md
      RESULT.md        # terminal only
```

### `system-development/README.md`
Stable contract/navigation only: role/lifecycle of revision files, D-016 relation, closure/inactivation, GitHub/Git/DECISIONS boundaries. No current WP details or history diary.

### `<revision>/REQUIREMENTS.md`
Canonical solution-independent revision Requirements baseline: problem/evidence pointers, scope/non-goals, assumptions/uncertainty, Requirement→acceptance trace, method-coverage/research disposition. After admission, material Requirement change triggers re-baselining/review.

### `<revision>/DESIGN.md`
Canonical selected target Design baseline: current baseline reference, alternatives/disposition, owner/information roles, interfaces/transitions, Human/AI/specialist boundaries, failure behavior, migration, qualification design and candidate admission scope. It does not own current WP status. Material admitted Design change returns to D-016.

### `<revision>/PLAN.md`
Canonical bounded current programme/change plan for the admitted revision. It owns only target link, remaining outcome/WP slices, current work selection, real dependencies, exit/proof, programme consequence and whole-revision closure state.

Recommended semantics:

| WP | contribution/target property | status | work owner | exit/proof | programme consequence |
|---|---|---|---|---|---|

PLAN is updated in place, not append-only; Git owns history. Closed child details leave the active plan after their programme consequence is incorporated. Evidence is linked, never copied.

### `<revision>/RESULT.md`
Created only at terminal result review: exact final SHA, Requirement results, technical assurance, migration/loss check, fresh-context/Human usability result, residuals, decisions promoted, closure disposition. A closed revision becomes historical/on-demand.

### No global `CURRENT.md` in v1
A separate global pointer was considered and rejected because it risks another clock. README navigation may point to the one admitted active revision. If real use later proves deterministic discovery fragile, a rebuildable index/view can be justified separately.

## J. Information lifecycle

```text
CAPTURE      preserve raw observation/audit/research evidence
DISPOSITION  establish meaning/non-meaning
PROMOTION    move accepted meaning into Requirement | Design | Decision | Plan | canonical research owner
INTEGRATION  update affected current configuration/remaining plan
DEACTIVATION completed working evidence leaves default current context
RETRIEVAL    expand history/provenance only when needed
```

Therefore:

```text
persistence ≠ promotion ≠ currentness ≠ default context
```

The desired feedback is:

```text
Work Result
→ actual repo configuration changes
→ Requirement/Design consequence verified
→ PLAN remaining delta changes/shrinks
→ accepted rationale promoted if needed
→ local work closes
→ history grows in Git/Issue/PR
```

not `history grows → next context reconstructs current/target/plan`.

## K. Human decision-readiness contract

Before material D-016 admission, the surface must answer:

1. where we are in the process;
2. proven problem/evidence;
3. remaining uncertainty;
4. accepted Requirements;
5. Research conclusions/non-conclusions;
6. credible alternatives and disposition;
7. selected Design and rationale;
8. exact authority requested;
9. explicit non-goals;
10. expected changed files/contracts/owners;
11. verification/validation plan;
12. defer/reject/refine consequence and reversibility.

A terse Human response is safe only after this context exists.

## L. DEV-READY implementation design — SD-01

If Human Owner later selects `ADMIT`, the admitted revision should be:

> **SD-01 — System-development information lifecycle + development-readiness operationalization**

### Material scope

1. Add the `system-development/` bounded revision architecture above.
2. Add first SD-01 Requirements/Design/Plan baselines from this admitted design; preserve old evidence in place.
3. Refine `methodology/maintenance.md`: distinguish DEV-READY from ADMITTED and require proportional method-coverage/sufficiency for material change.
4. Refine `methodology/workflow.md`: Pre-Dev work must derive from an admitted Design baseline; Findings cannot silently become implementation-shaped requirements.
5. Refine `methodology/quality-and-learning.md`: add upstream-development sufficiency and Human decision-readiness review dimensions.
6. Update README orientation so current system-development work uses the bounded revision owner rather than dated-audit replay.
7. Promote accepted consequential architecture rationale to `DECISIONS.md` as appropriate.
8. Qualify fresh-context/current-history/Human-decision/local→programme closure behavior.

### Explicit non-goals

No manuscript scope/NEXT ACTION; Source/File/Project redesign; workflow engine; planner; event store; registry; graph/Wirknetz runtime; universal task compiler; bulk historical migration; package/src move; release/SemVer/template work; #90 reactivation; automatic successor revision; inference that #225 achieved whole-system scholarly acceptance.

### Expected implementation surface

```text
CREATE  system-development/README.md
CREATE  system-development/revisions/SD-01/REQUIREMENTS.md
CREATE  system-development/revisions/SD-01/DESIGN.md
CREATE  system-development/revisions/SD-01/PLAN.md
CREATE  system-development/revisions/SD-01/RESULT.md   # terminal only
UPDATE  methodology/maintenance.md
UPDATE  methodology/workflow.md
UPDATE  methodology/quality-and-learning.md
UPDATE  README.md
UPDATE  DECISIONS.md                                  # accepted rationale only
```

No old audit file is moved/deleted.

### Post-admission Work Packages

**WP1 — revision IA bootstrap.** Create contract + SD-01 baselines/plan. Exit: roles non-overlapping; current programme readable without history replay.

**WP2 — development-readiness METHOD integration.** Add proportional coverage, re-entry, Requirements→Design trace and Human decision-readiness semantics. Exit: tiny-bug case remains lightweight; coupled-system case cannot jump from Finding to implementation-shaped work.

**WP3 — navigation/current-meaning migration.** README/current navigation points to SD-01; prior target/D-016/rebaseline artifacts become historical evidence rather than competing plan. #225/#230 remain closed.

**WP4 — adversarial qualification.** Required fixtures:
- history-heavy fresh start;
- premature-solution trap;
- tiny bug/direct-fix control;
- child result→PLAN consequence;
- Human decision-readiness;
- closed revision leaves default context;
- materially different system-change fixture.

**WP5 — terminal result review.** Create RESULT, exact-head assurance, promote decisions, close SD-01. No successor is automatic.

## M. Acceptance / qualification

A fresh Senior Engineer/agent without old chat must determine from normal navigation:

- product/purpose;
- whether a material revision exists and its admission state;
- revision Requirements;
- selected Design;
- remaining Plan delta/current work or explicit absence;
- what has closed and its programme consequence;
- exact Human decision needed, if any;
- where deeper evidence/history lives;
- which history does **not** need loading.

FAIL if #225/#230 chronology or the dated audit chain is required merely to establish current programme state.

Also require:

- **information-role test:** material items classify as Requirement/Design/Plan/Work/Decision/Evidence/History/Result without incompatible mutable ownership;
- **reconstruction-cost test:** minimum current bootstrap does not grow proportionally with historical audit volume;
- **anti-waterfall test:** trivial bug, unclear defect, research-dependent question, coupled system problem and no-change case receive proportionate different coverage;
- **no-second-clock test:** PLAN owns programme delta, Issue/PR local work, Git history, DECISIONS accepted rationale, README navigation only;
- **exact-head assurance** after final mutation.

## N. Migration / transition

No bulk archive migration.

At SD-01 bootstrap, promote **current meaning**, not files:

- re-express accepted Requirements from this DEV-READY baseline;
- capture selected Design in the new Design baseline with evidence links;
- build PLAN from admitted implementation outcomes;
- keep earlier audits at stable paths as history/provenance.

After the revision architecture exists, normal current system-development navigation becomes:

```text
README
→ system-development/README
→ active revision REQUIREMENTS + DESIGN + PLAN
→ applicable METHOD / DECISIONS
→ evidence/history only on demand
```

On terminal result:

```text
PLAN work complete
→ Requirement/result reconciliation
→ durable decisions promoted
→ RESULT created
→ revision closes and becomes historical
→ no successor inferred
```

## O. Sufficiency / complexity justification

Selected components map directly to demonstrated failures:

- Requirements baseline → solutionism/premature Requirements;
- Design baseline → implementation inventing material architecture;
- bounded Programme Plan → history-as-planning + local closure without whole consequence;
- terminal Result → closability/inactivation;
- method-coverage semantics → premature work shaping without rigid waterfall;
- decision-readiness semantics → formal Human loop without sufficient understanding.

Deliberately absent: permanent roadmap, global state DB, event store, workflow engine, planner, registry, graph, context compiler, bulk archive migration, new package/repository split.

## P. Residual uncertainty

Non-blocking implementation details remain: exact revision naming; whether a later derived context/index tool proves useful; whether historical `requirements/` ever needs an index; future concurrent revision semantics; future deterministic validation beyond existing CI.

These do not require a material architecture choice to begin SD-01. Any later material expansion would require its own demonstrated need/admission.

**Blocking uncertainty for implementation:** only the Human D-016 admission itself.

## Q. D-016 decision surface

Process state:

```text
Problem re-baseline        sufficient
Root-cause analysis        sufficient
Requirements               sufficient
Targeted Research          sufficient
Concept alternatives       compared
Detailed Design            sufficient
Implementation planning    bounded/explicit
Implementation             NOT STARTED
D-016 admission            NOT GIVEN
```

`ADMIT` would authorize only SD-01 scope/WPs above, including routine implementation choices inside those semantics.

`REFINE` means one or more material Requirement/Design points must change before implementation.

`DEFER` preserves this DEV-READY design without implementation.

`REJECT` preserves the evidence but rejects the selected architecture and requires a replacement design.

## R. External research references

Consulted authoritative/current sources: ISO/IEC/IEEE 29148:2018 (Requirements Engineering); NASA Systems Engineering Handbook (Requirements, Design, Technical Planning, Configuration/Data Management, Assessment/Decision Analysis); NASA Human Systems Integration / Decision Aid Clarity guidance; NIST AI RMF/AIRC Human-AI interaction guidance; SEBoK v2.14 (2026) process iteration/tailoring, configuration baselines, information management and design definition; AWS ADR guidance; Microsoft Azure CQRS/Event Sourcing patterns as contrast evidence only.

## S. Final verdict

The repository has not lost the governing whole. It still has strong purpose, METHOD, scholarly owners, decisions, evidence and quality boundaries. The weak layer was the **active engineering configuration between durable truth and local work**.

The correction is not `document more`:

```text
preserve evidence/history
≠ make it current

accepted Requirement
→ selected Design baseline
→ bounded Programme Plan
→ work/result
→ programme disposition
→ actual configuration + smaller remaining delta
```

and:

```text
material problem
→ determine required development capabilities
→ establish sufficiency proportionally
→ bind Design
→ DEV-READY
→ Human D-016 admission
→ implement
→ verify / validate / reconcile
```

This reaches the requested boundary: **DEV-READY, but not admitted and not implemented.**
