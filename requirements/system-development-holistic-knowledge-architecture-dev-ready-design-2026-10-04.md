# Holistic system-development knowledge architecture and practical developer infrastructure — 2026-10-04

**Status:** NON-NORMATIVE HOLISTIC DESIGN / **DEV-READY FOR D-016 DECISION / NOT ADMITTED**  
**Repository baseline:** `main@be497cb600dd90d78d6c473c5e173f0e010e1269`  
**Comparator baseline:** `esany/Wissensarbeit@b448915cf774c573dbf82cf2e17bcb03c10a9ed8`  
**Requalifies:** `requirements/system-development-information-architecture-dev-ready-design-2026-10-03.md`  
**Preserves as evidence:** all earlier audits, Requirements work, concepts, designs, admissions, result reviews and repository history.  
**This artifact is not:** D-016 admission, implementation permission, METHOD, manuscript Project scope, a scholarly `NEXT ACTION`, a workflow engine, a graph database, a developer portal, or proof of scholarly acceptance.

## A. Executive disposition

The previous `DEV-READY / D-016 DECISION READY` claim was **too narrow and is falsified as a sufficient whole-system architecture**.

The previous design correctly identified two real failures — history being used to reconstruct current planning meaning, and premature solution-shaped work — but it then selected a bounded `system-development/revisions/<id>/{REQUIREMENTS,DESIGN,PLAN,RESULT}` architecture while treating several wider questions as non-blocking or unnecessary. Fresh repository inspection and the Human Owner's challenge show that those questions are not peripheral. They are part of the demonstrated failure.

The deeper system problem is:

> **paleo-type has strong scholarly canonical owners and strong local engineering controls, but it does not yet have a coherent engineering information/configuration architecture that turns accumulated analysis, Requirements, research, decisions, design, work and learning into a queryable current system model with controlled lifecycle, promotion, supersession and role-specific context.**

This produces a recurring loss loop:

```text
real pain / failure
→ rich audit and analysis
→ many valuable findings exist simultaneously
→ some findings are promoted, some remain implicit, some are superseded
→ later work consumes only a compressed subset
→ the rich relation between problem, evidence, Requirements and design disappears from the active surface
→ current meaning must be reconstructed from dated files / Issues / prior analyses
→ another audit recovers the whole
```

The problem is therefore not merely `too much history`, `missing documentation`, `missing programme plan`, or `missing Context Compiler`.

It is a coupled failure of:

1. **Information Management** — engineering information assets have heterogeneous roles but insufficient explicit lifecycle/metadata/discovery semantics;
2. **Configuration Management** — the accepted current engineering configuration, active change state and target baselines are not first-class enough;
3. **Trace / promotion** — valuable findings do not have a systematic forward disposition into current Requirements, Decisions, Design, work or explicit non-action;
4. **Development method operationalization** — the logical path from problem framing to DEV-READY is described in pieces but not carried by an executable/restartable engineering work state;
5. **Developer / agent experience** — a new capable context has strong Project-context tooling for scholarship, but no equivalent bounded engineering bootstrap/query/context surface;
6. **Repository information architecture** — `requirements/` is a flat mixed-purpose namespace whose name no longer describes most of its contents, while the README has accumulated programme-history/current-state narration despite being designated only as orientation.

The selected target architecture is a **repository-native Engineering Knowledge & Configuration Plane (EKCP)** combined with a **risk-tailored Development Readiness Contract**.

It is deliberately larger than the previous SD-01 proposal because the demonstrated problem is larger. It remains bounded: Git remains provenance; Markdown/TSV/JSON remain canonical open formats; no external database, graph service, Backstage deployment, workflow engine or autonomous planner is required for the demonstrated scale.

After this pass, the candidate change described below is again judged:

> **HOLISTIC DEV-READY / D-016 DECISION READY / NOT ADMITTED**

The repository is **not yet operating this target architecture**. No implementation has started.

---

## B. Fresh authority and non-negotiable boundaries

Fresh current authority establishes:

- scholarly result/source understanding is the product; engineering infrastructure is subsidiary;
- evidence before plausibility and uncertainty as a valid result remain governing;
- complete **applicable** context is required, not indiscriminate whole-repository loading;
- one durable fact/decision/state has one canonical owner; generated views remain derived;
- Human Owner controls purpose, material priority/scope and D-016 implementation admission;
- AI/implementation agents own routine bounded work already authorized;
- GitHub Issues/PRs/Milestones are work/review/planning metadata, not scholarly truth;
- a fresh capable context must reconstruct authorized state without old chat;
- D-016 currently remains `analysis → requirements → concept → owner review / explicit implementation admission → development → tests/loss checks → result review`;
- all three manuscript Projects currently have no owner-selected active scholarly work, so this system design creates no manuscript `NEXT ACTION`.

This design does not alter those boundaries.

---

## C. Empirical repository / information-architecture audit

### C1. `requirements/` is not currently a coherent information class

Fresh tree inspection shows one flat directory containing, side by side:

- an actual structured Requirement baseline: `domain-requirements.tsv`;
- audits (`repository-knowledge-lifecycle-adequacy-audit-*`, `project-maturity-model-repository-audit-*`, `system-operationalization-audit-*`);
- research (`pre-synthesis-research-*`, `cross-source-research-findings-*`, `shared-fixture-research-findings-*`);
- concepts/design (`executable-transdisciplinary-research-system-concept-idea-*`, `phase2-integrated-concept-comparison-*`, `repository-target-state-*`, the previous DEV-READY design);
- owner admissions/dispositions;
- result reviews;
- prompts/work instructions;
- learnings;
- coordination bootstrap artifacts;
- problem frames and reconstructions.

Physical co-location alone is not the defect. The defect is that **semantic kind, authority, lifecycle, currentness, supersession and promotion are mostly inferred from filename/header/prose** rather than exposed through a consistent information architecture.

The top-level repository structure in the README does not even list `requirements/`, although `requirements/` is a major top-level directory and current cross-project system-development evidence surface. That is a concrete navigation/configuration drift, not a theoretical concern.

### C2. README has crossed its intended role boundary

The README states that it is an orientation/reading-path view and not a Project status store or second method manual. Yet its current research-system section now carries a substantial chronological/current narrative covering #206, #225, #230, multiple dated analyses, the latest DEV-READY claim, Route A, Route B and historical programme interpretation.

This is understandable adaptive maintenance, but structurally it means:

```text
orientation surface
+ current system-development interpretation
+ historical programme synthesis
+ audit catalog
```

have begun to coexist in one file.

The README is becoming a manually maintained projection of engineering state. That is exactly the role that should be derived from explicit engineering owners.

### C3. Project restart is better engineered than system-development restart

`tools/project_context.py` already proves an important pattern: Project context can be compiled read-only from canonical owners, with explicit canonical references and negative authority boundaries.

`tools/outcome_context.py` similarly compiles a bounded scholarly outcome-control view and deliberately refuses to manufacture scholarly `NEXT ACTION`.

There is no equivalent current mechanism for:

- engineering current configuration;
- active system investigation/change;
- applicable engineering Requirements;
- current architecture baseline;
- open material findings;
- design/readiness state;
- exact D-016 decision boundary;
- relevant historical evidence on demand.

A system-development context therefore still depends substantially on human/agent semantic reconstruction.

### C4. Current engineering context cost is already material

On current `main`, the five root governing/orientation/decision/planning surfaces are approximately **68,418 characters** and the ten methodology files approximately **143,519 characters**: about **211,937 characters before Project state, `requirements/`, Issues/PRs or research evidence**.

This is not a claim that every task must load all of them; current governance correctly says the opposite. It is evidence that the repository needs a trustworthy applicability/query/context mechanism. Strong models can currently hide this repository cost by mentally compiling the system, but that is not a durable architecture.

### C5. CI is strong in its current domain and weak outside it

Current CI validates the Source/File/Project-use contract, runs deterministic/governance regressions, compiles all three Project contexts and checks real resolver fixtures. It explicitly states that a PASS establishes only the checked formal/deterministic properties.

There is currently no comparable deterministic assurance for engineering knowledge architecture, for example:

- artifact identity/kind/lifecycle metadata;
- current configuration references;
- superseded-but-current conflicts;
- orphan material findings;
- finding → Requirement/Decision/Design disposition coverage;
- active-change / D-016 state integrity;
- generated engineering-current-state freshness;
- context-profile validity;
- migration/path-link integrity.

### C6. Practical developer bootstrap is implicit

A capable developer can infer a workable environment from CI:

- Python 3.12;
- repository-local Python tools;
- `unittest` discovery;
- source-contract validation.

That is valuable simplicity. But there is no first-class developer entrypoint that says, in one bounded place:

- what the current system architecture is;
- what change is active;
- how to obtain the correct context;
- how to run the full local assurance suite;
- how engineering artifacts are classified;
- how to tell current target from historical evidence;
- how to add/change an engineering artifact without creating another orphan.

The absence of a package or devcontainer is **not** itself a defect. The missing developer contract is.

---

## D. Fresh-context / developer-journey audit

### D1. New manuscript-research context

This is comparatively mature:

```text
README
→ GO + AGENTS
→ Project project.yml / STATUS
→ project_context.py / source-contract resolution
→ applicable specialist method/evidence
```

The repository can explicitly represent absence of an authorized scholarly next action.

### D2. New system-development context — current failure

Today a careful new system developer or AI must effectively discover and compose:

```text
GO
+ AGENTS
+ README's system-programme narrative
+ DECISIONS / D-016
+ maintenance/workflow/quality
+ current dated design artifact
+ prior re-baseline if challenging the design
+ relevant lifecycle/product/Human-proxy audits
+ current tools/tests/CI
+ relevant Issue/PR history when provenance matters
```

The set is neither tiny nor inherently wrong. The failure is that **which subset is current/applicable and why is not itself a first-class queryable product**.

### D3. New architecture reviewer

A reviewer cannot reliably ask the repository:

- show current architecture baseline;
- show all Requirements supporting this design;
- show which material findings led to each Requirement;
- show alternatives rejected and why;
- show which findings from prior audits remain open;
- show what superseded the previous DEV-READY design.

The answers exist, but they are spread across prose and chronology.

### D4. Human D-016 decision context

The recent `ausführen` interaction already demonstrated that formal Human authority is insufficient without situational comprehension. A Human decision surface therefore needs to be generated from the same current engineering state that developers/reviewers consume, not manually compressed from chat.

### D5. Maintenance context

Current maintenance rules are strong, but an agent still has to discover which engineering information assets and accepted relations are affected. A structured impact/query layer would reduce that reconstruction without weakening canonical ownership.

---

## E. Insight-loss / promotion audit — the lost rich moment

The Human Owner's observation that "the moment when all the rich audit learnings were in front of us has passed" describes a real failure class.

Persistence of an audit file is not equivalent to persistence of its **current consequence**.

### E1. Concrete examples

1. The 2026-10-02 knowledge-lifecycle audit explicitly confirmed `requirements/` artifact-role heterogeneity and insufficient active-vs-persisted separation. The previous DEV-READY design then left `requirements/` physically unchanged and treated a historical index as a non-blocking future detail. The finding was remembered, but its architectural weight was compressed too aggressively.
2. The Human-decision re-baseline left whether existing owners are sufficient (`U9`) and whether an orchestration/execution layer may be needed (`U10`) unresolved. The next design selected existing owners unchanged and rejected several larger mechanisms without first broadening the practical developer/knowledge-infrastructure audit enough.
3. Human-proxy/context work established that context reduction must reduce reconstruction rather than evidence and that `outcome_context.py` stops before deterministic work generation. Those are still valid, but the previous design narrowed the response to revision files rather than a repository-wide engineering context architecture.
4. Product/co-development analysis correctly warned that Genericity ≠ Distribution and that Wirknetz is a trace/design lens rather than a runtime. Those negative constraints remain valuable and must survive the larger architecture.
5. `Wissensarbeit` independently falsified the necessity of a separate Wirknetz↔Skill Bridge for its frozen cases. This prevents the current audit from solving the problem with an attractive graph/bridge merely because relations matter.

### E2. Required correction

A material audit/finding must have an explicit durable disposition chain:

```text
source finding
→ current disposition
→ Requirement / Decision / Design / work / deferred trigger / rejection / supersession
```

and the reverse must be queryable:

```text
current Requirement / Decision / Design
→ supporting findings/evidence
→ source artifact / exact anchor
```

The full audit remains available for depth. The active system does not need to replay it merely to know what consequence survived.

### E3. Insight preservation rule

> **Preserve the source; promote the consequence; deactivate the source from default context when the consequence is integrated; retain a reversible trace between them.**

This is not documentation duplication. It is information lifecycle management.

---

## F. Causal system model

The observed failures are coupled but not one monolith.

| Failure family | Root mechanism | Observable consequence |
|---|---|---|
| IA-1 Semantic namespace collapse | heterogeneous engineering information assets lack explicit machine-queryable role/lifecycle metadata | filename/prose archaeology; `requirements/` becomes a catch-all |
| IA-2 Currentness/configuration weakness | engineering baselines/current change/current architecture not identified strongly enough | README/history carries current interpretation |
| IA-3 Promotion gap | audit findings persist without mandatory forward disposition | rich learnings become historical prose rather than active constraints |
| IA-4 Trace gap | relations are embedded in prose, Issue chronology and human memory | backward/forward rationale reconstruction is expensive |
| IA-5 Context/applicability gap | governance demands applicable context but system-dev applicability is not compiled | large context tax or context starvation |
| IA-6 DevEx gap | no engineering bootstrap/query/check contract | new developer must discover the operating model manually |
| M-1 Upstream method weakness | finding can become solution-shaped work before upstream sufficiency is independently established | local excellence inside prematurely narrowed solution space |
| M-2 Reconciliation without semantic promotion | local result/closure does not always update active system meaning | history grows faster than current model matures |
| H-1 Human situation-awareness gap | decision options can be compressed before Human can reconstruct their basis | Human formally authorizes without sufficiently understanding the loop |
| G-1 Meta-work feedback | distributed safeguards/audits increase reconstruction cost | pressure for narrow fixes → residual failure → another audit |

The deepest currently supported causal coupling is:

```text
weak engineering Information Management
+
weak engineering Configuration/Status Accounting
+
weak finding/decision trace promotion
+
partly operationalized development-method sufficiency
        ↓
current meaning must be reconstructed
        ↓
context grows / history re-enters
        ↓
whole-system understanding is episodic rather than continuously available
        ↓
premature local shaping becomes attractive
        ↓
new audit recreates the whole
```

---

## G. Targeted Best-Practice / SOTA synthesis

No external framework is adopted wholesale. The useful comparator properties are:

### G1. Requirements Engineering

ISO/IEC/IEEE 29148:2018 treats Requirements Engineering and its information items as lifecycle concerns across methodologies and project sizes. The relevant transfer is not a document template; it is explicit Requirements information, traceability and change/baseline discipline.

### G2. Systems Engineering: Configuration Management vs Information Management

Current SEBoK guidance sharply distinguishes the concerns that paleo-type has partially collapsed operationally:

- **Information Management** manages information through generation, collection, validation, transformation, retention, retrieval, dissemination and disposal; metadata, lifecycle, identification and obsolescence management are first-class.
- **Configuration Management** manages the significance/applicability of configuration information to the system as it evolves; baselines, change control, status accounting, traceability and audit establish the current approved configuration.

NASA's Systems Engineering Handbook likewise treats Technical Data Management and Configuration Management as complementary mechanisms for keeping project information safe, known and accessible.

This distinction maps unusually well to the current failure: `all information we retain` is not the same thing as `the approved/current system configuration we should operate from`.

### G3. Repository-native catalog / Developer Experience

Backstage's Software Catalog is useful here only as a **pattern**, not as a deployment recommendation: source-controlled metadata can remain the source of truth while a derived catalog makes ownership and discoverability uniform and queryable.

Platform-engineering practice adds a second useful property: reduce developer cognitive load without removing underlying context; provide paved/golden paths without making them cages.

At paleo-type's scale, those properties can be implemented locally without a portal service.

### G4. AI context engineering

Current agent-context practice emphasizes that context is a finite attention resource; effective contexts are high-signal and use progressive disclosure / just-in-time retrieval. The applicable lesson is exactly the repository's own principle:

> reduce reconstruction, not evidence.

A role/task context should contain current authoritative state and pointers sufficient for work, while deep provenance remains expandable.

### G5. ADRs / decision rationale

ADR practice reinforces a narrow point already owned by paleo-type: consequential architectural decisions need durable context, decision and consequences so future developers do not repeatedly reopen settled questions. This does not imply replacing `DECISIONS.md` now.

### G6. Evolutionary architecture / fitness functions

Architecture characteristics that matter can be guarded continuously with executable fitness functions. For paleo-type, information-lifecycle and restartability invariants are suitable candidates for deterministic CI checks, while semantic/Human validity remains outside pure automation.

### G7. Documentation architecture

Diátaxis is useful only for presentation/documentation roles (tutorial/how-to/reference/explanation). It does not solve canonical state, configuration management or traceability. It can inform later Human-facing docs after the engineering information model is sound.

---

## H. Solution-independent Requirements baseline

These Requirements are derived from the demonstrated failures before selecting a representation.

### H1. Currentness / configuration

| ID | Required property |
|---|---|
| EKR-01 | A fresh context can identify the approved/current engineering configuration without replaying audit or Issue chronology. |
| EKR-02 | Actual implemented state, accepted Requirements, accepted/current architecture, proposed target Design, active Plan/Work and History are distinguishable. |
| EKR-03 | Current configuration identification has one canonical owner and does not depend on a manually maintained README narrative. |
| EKR-04 | Zero active system changes is valid; multiple investigations/changes may coexist without inferring priority from recency. |
| EKR-05 | Material current-state change is traceable to the admitted change/result that established it. |

### H2. Information assets / lifecycle

| ID | Required property |
|---|---|
| EKR-06 | Material engineering information assets have stable identity, semantic kind, owner/authority role and lifecycle state independent of filename wording. |
| EKR-07 | Historical/superseded information remains retrievable but is excluded from default current context unless applicable. |
| EKR-08 | Obsolete/superseded/current distinctions are machine-checkable enough to prevent `latest file wins`. |
| EKR-09 | Physical repository location communicates semantic responsibility rather than accumulating unrelated artifact roles in a catch-all directory. |
| EKR-10 | Information can be reclassified/migrated without losing Git provenance or stable trace references. |

### H3. Insight / trace / promotion

| ID | Required property |
|---|---|
| EKR-11 | Every material audit/finding can be dispositioned as open, integrated/promoted, deferred, rejected, superseded, local-only or equivalent, with rationale. |
| EKR-12 | A closed material audit/change cannot silently leave material findings orphaned. |
| EKR-13 | Current Requirements/Decisions/Design can be traced backward to supporting evidence/findings at an appropriate level of detail. |
| EKR-14 | Findings can be traced forward to their current consequence or explicit non-consequence. |
| EKR-15 | Relation correctness and evidence outrank apparent graph completeness; uncertain relations remain candidate/unresolved. |
| EKR-16 | Verification, Human validation and specialist validation remain distinguishable relations. |

### H4. Development method / DEV-READY

| ID | Required property |
|---|---|
| EKR-17 | Material system work records which development capabilities are required, satisfied, not required with rationale, blocked or re-entered. |
| EKR-18 | Problem framing, analysis, Requirements, Research, concept comparison and Design remain semantically distinguishable even when iterative/interleaved. |
| EKR-19 | Findings/feedback cannot silently become implementation-shaped Requirements or Work. |
| EKR-20 | DEV-READY is derivable only when blocking architecture/semantic/migration/verification uncertainty is closed or explicitly exposed. |
| EKR-21 | DEV-READY, D-016 ADMITTED, IMPLEMENTING, VERIFIED and ACCEPTED remain distinct states. |
| EKR-22 | Trivial/routine work can reuse existing baselines and avoid ceremony; the mechanism must not impose a mandatory waterfall. |

### H5. Context / discoverability / Human & developer experience

| ID | Required property |
|---|---|
| EKR-23 | A role/task-specific context can be compiled from canonical state for manuscript research, system development, architecture review, Human decision, maintenance and specialist review. |
| EKR-24 | Context compilation uses progressive disclosure: current high-signal context first, evidence/history expansion on demand. |
| EKR-25 | The minimum bootstrap set does not grow proportionally with accumulated historical audits. |
| EKR-26 | A new developer has one documented path to current architecture/change state and one local command for full deterministic assurance. |
| EKR-27 | Human D-016 decision context exposes problem, evidence, Requirements, alternatives, uncertainty, selected Design, exact authority requested, non-goals, consequences and reversibility. |
| EKR-28 | Derived views are reproducible and detectably stale; they never become manual parallel truth stores. |
| EKR-29 | Semantic queries such as `what is current?`, `why?`, `what superseded this?`, `what remains open?`, and `what applies to this change?` are answerable without chronology replay. |

### H6. Engineering / migration / product boundary

| ID | Required property |
|---|---|
| EKR-30 | The architecture remains repository-native and usable from a normal clone plus supported local runtime; external services are not required for canonical truth. |
| EKR-31 | Machine-checkable metadata/relations are validated in CI with the same explicit formal-vs-semantic assurance boundary as the Source Contract. |
| EKR-32 | Migration from the current brownfield repository is loss-checked, reversible and link/provenance preserving. |
| EKR-33 | Scholarly Source/File/Project owners remain untouched unless a demonstrated requirement directly requires change. |
| EKR-34 | System-development infrastructure creates no manuscript scope, priority or scholarly `NEXT ACTION`. |
| EKR-35 | Larger infrastructure (package, index DB, portal, graph service, workflow engine) remains addable under explicit evidence triggers rather than prohibited by a size preference. |

---

## I. Architecture concepts and trade study

### I1. Option A — previous SD-01 bounded revision files only

Shape: `system-development/revisions/<id>/{REQUIREMENTS,DESIGN,PLAN,RESULT}` plus METHOD refinements.

**Strengths:** current/target/plan separation; closable change unit; modest migration.  
**Failure:** no repository-wide information-asset model, finding promotion ledger, engineering current-configuration/status accounting, role-specific query/context system, legacy `requirements/` lifecycle or practical developer bootstrap.  
**Disposition:** **insufficient as whole-system architecture; preserve bounded-change idea as a component.**

### I2. Option B — documentation/physical reorganization only

Shape: split `requirements/` into audits/research/design/archive; shorten README.

**Strengths:** strong immediate discoverability; low runtime complexity.  
**Failure:** role/currentness still inferred from paths; forward/backward finding disposition remains manual; generated current state/context still absent; physical layout alone cannot answer configuration/status questions.  
**Disposition:** **insufficient.**

### I3. Option C — typed artifact catalog over existing paths only

Shape: stable metadata catalog + relations; no physical migration.

**Strengths:** queryability, lifecycle, traceability, brownfield-friendly.  
**Failure:** the visible repository remains semantically misleading; developer navigation still depends on a catch-all directory; current configuration/change state requires additional owner semantics.  
**Disposition:** **useful migration step, insufficient final target.**

### I4. Option D — repository-native Engineering Knowledge & Configuration Plane

Shape: explicit engineering configuration owner + typed information-asset/finding/relation catalog + bounded change state + semantically coherent physical IA + generated current/catalog views + context/query compiler + CI fitness checks.

**Strengths:** addresses both Information Management and Configuration Management; solves insight promotion; preserves Git-native/open-formats model; supports role-specific context; can migrate incrementally; no mandatory external service.  
**Costs:** larger initial migration and validator/tool surface; metadata itself must be disciplined; relation overproduction is a risk.  
**Disposition:** **SELECTED.**

### I5. Option E — Option D plus derived SQLite/search/graph index

**Strengths:** stronger local queries/traversal as scale grows.  
**Failure/cost:** adds cache/schema lifecycle and synchronization; current corpus does not demonstrate query-performance or relation-volume pressure requiring it.  
**Disposition:** **compatible derived optimization, not initial canonical architecture. Trigger only on measured query/scale need.**

### I6. Option F — full developer portal / Backstage-class service

**Strengths:** excellent human discoverability, ownership/catalog/UI patterns at organizational scale.  
**Failure/cost:** service deployment, plugins, runtime ownership and operations are disproportionate for one repo and do not improve canonical truth by themselves.  
**Disposition:** **not justified now; pattern evidence reused, product not adopted.**

### I7. Option G — event store / graph database / workflow engine as system of record

**Strengths:** rich event/history/relationship/runtime queries.  
**Failure/cost:** duplicates Git history, creates another persistence/runtime authority, increases migration/operations and risks formalizing uncertain semantic relations.  
**Disposition:** **rejected for current evidence.**

The selected architecture is therefore not selected because it is smallest. It is selected because it is the least architecture in this comparison that closes the whole demonstrated failure family without relocating integration work to a human/agent.

---

## J. Selected architecture — Engineering Knowledge & Configuration Plane (EKCP)

The target has six cooperating responsibilities.

### J1. Engineering Information Asset Catalog — Information Management

A small repository-native metadata plane identifies material engineering information assets independently of their prose filename.

Target canonical files:

```text
engineering/catalog/artifacts.tsv
engineering/catalog/findings.tsv
engineering/catalog/relations.tsv
```

`artifacts.tsv` owns **metadata about engineering information assets**, not their content.

Minimum columns:

```text
artifact_id
kind
path
owner_scope
authority_role
lifecycle_state
change_id
title
```

Initial `kind` families are deliberately broad:

```text
governance
method
requirement-set
problem-analysis
audit
research
concept
design
decision
plan
work-instruction
result
verification
validation
learning
generated-view
```

The exact implementation may combine closely related kinds if the migration proves they are not discriminating. A new kind needs action-relevant need, not taxonomic symmetry.

`authority_role` distinguishes at least:

```text
canonical
accepted-decision
admitted-change
non-normative-evidence
derived
work-metadata
```

`lifecycle_state` distinguishes at least active/closed/historical/superseded where meaningful. Kind-specific validation prevents a single universal state vocabulary from laundering semantics.

### J2. Material Finding / Learning disposition

`engineering/catalog/findings.tsv` is the missing bridge between rich audit moments and current meaning.

Minimum columns:

```text
finding_id
source_ref
summary
materiality
disposition
target_ref
rationale
```

Allowed disposition semantics include:

```text
open
integrated
promoted
deferred
rejected
superseded
local-only
no-change
```

A material finding may stay open. What is forbidden is accidental disappearance.

For a closed audit/change, every registered material finding must have either:

- a forward target/current consequence; or
- an explicit retained-open/deferred/rejected/superseded/local-only disposition.

This turns `audit persisted` into `learning lifecycle controlled`.

### J3. Material relation trace

`engineering/catalog/relations.tsv` records only **material, review-relevant relations**.

Minimum columns:

```text
relation_id
subject_ref
predicate
object_ref
relation_status
evidence_ref
```

Initial predicates should remain small, for example:

```text
supports
derived-from
refines
supersedes
implements
verifies
validates
affects
part-of
```

`relation_status` preserves candidate/accepted/historical distinctions where needed.

A complete relation graph is not a success criterion. Unsupported relations must be absent or candidate.

### J4. Engineering Configuration Identification — Configuration Management

`engineering/configuration.json` becomes the canonical owner of **which engineering baselines/change owners are current**, not a copy of all content.

Target shape:

```json
{
  "schema_version": 1,
  "architecture_baseline": "ENG-ARCH-...",
  "requirements_baselines": ["..."],
  "active_changes": ["SD-..."],
  "current_focus": null,
  "decision_owner": "DECISIONS.md"
}
```

Rules:

- `current_focus` may be null;
- recency does not choose focus;
- multiple investigations may coexist;
- an admitted/implementing change remains explicit;
- actual implementation is still the repository tree at the current commit;
- this file identifies semantic engineering baselines/current change owners, not a second Git history.

### J5. Bounded system-change workspaces

The useful part of the previous SD-01 design is retained but placed inside the larger knowledge/configuration architecture.

Target:

```text
engineering/changes/<change-id>/
  STATE.json
  PROBLEM.md
  REQUIREMENTS.md        # or TSV when tabular structure is materially useful
  RESEARCH.md            # only if a dedicated synthesis is needed
  CONCEPTS.md            # only if materially distinct alternatives exist
  DESIGN.md
  PLAN.md
  RESULT.md              # terminal only
```

Only `STATE.json` is structurally required for a material change. Empty ceremony files are forbidden.

`STATE.json` owns local material-change lifecycle/authority state, not global configuration.

Target semantics:

```json
{
  "change_id": "SD-KA-01",
  "lifecycle": "investigating|designing|dev-ready|implementing|verifying|closed|deferred|rejected",
  "admission": "not-admitted|admitted|revoked|not-required",
  "scope": "...",
  "non_goals": ["..."],
  "coverage": {
    "problem": {"state": "required-satisfied", "basis": "..."},
    "root_cause": {"state": "required-satisfied", "basis": "..."},
    "requirements": {"state": "required-satisfied", "basis": "..."},
    "research": {"state": "required-satisfied|not-required-with-rationale|re-entered", "basis": "..."},
    "concepts": {"state": "...", "basis": "..."},
    "design": {"state": "...", "basis": "..."},
    "implementation_plan": {"state": "...", "basis": "..."},
    "verification_plan": {"state": "...", "basis": "..."},
    "migration_plan": {"state": "...", "basis": "..."}
  },
  "blocking_uncertainties": [],
  "applicable_rules": [],
  "plan_ref": null
}
```

This is not a fixed lifecycle engine. Coverage is risk/state-tailored and may re-enter.

### J6. Generated current/read models and context/query tooling

Canonical source-controlled state feeds rebuildable views:

```text
engineering/generated/CURRENT_STATE.json
engineering/generated/CURRENT_STATE.md
engineering/generated/CATALOG.md
```

The Markdown files may be committed for GitHub/Human discoverability **only if CI proves exact regeneration**. Otherwise they must be generated on demand.

A new `tools/engineering.py` should provide a single coherent interface:

```text
validate
derive
query
context
decision-brief
promotion-audit
```

Illustrative uses:

```text
python tools/engineering.py context --profile system-development
python tools/engineering.py context --profile architecture-review --change SD-KA-01
python tools/engineering.py decision-brief --change SD-KA-01
python tools/engineering.py query --kind audit --lifecycle historical
python tools/engineering.py promotion-audit
```

The tool returns references/pointers rather than copying deep history into every context.

---

## K. Target physical repository information architecture

The current catch-all role of `requirements/` should end.

Target:

```text
GOVERNING_OBJECTIVE.md
AGENTS.md
README.md
DECISIONS.md
MILESTONES.md

requirements/
  README.md
  domain-requirements.tsv
  ... accepted reusable Requirement baselines only

methodology/
  ... reusable normative METHOD

corpus/
entities/
projects/

engineering/
  README.md
  configuration.json
  context-profiles.json

  architecture/
    SYSTEM.md

  catalog/
    artifacts.tsv
    findings.tsv
    relations.tsv
    legacy-paths.tsv          # migration support; removable when no longer useful

  changes/
    <change-id>/
      STATE.json
      PROBLEM.md
      REQUIREMENTS.md
      RESEARCH.md             # optional
      CONCEPTS.md             # optional
      DESIGN.md
      PLAN.md
      RESULT.md               # terminal only

  evidence/
    audits/
    research/
    learning/
    work-instructions/

  generated/
    CURRENT_STATE.json
    CURRENT_STATE.md
    CATALOG.md

tools/
tests/
.github/
```

### K1. `requirements/` after migration

`requirements/` becomes what its name says: accepted/reusable Requirement baselines, plus a small README explaining authority/lifecycle.

Historical audits, prompts, concepts, result reviews and design studies leave this namespace.

### K2. No separate physical `archive/` is required initially

`closed/historical/superseded` is an information-lifecycle property, not necessarily a directory move. Closed change packages and evidence remain at stable semantic paths and are excluded from default current context by catalog/configuration state.

Git owns revision history.

### K3. `DECISIONS.md` remains for v1

Its current size alone does not demonstrate a need for a new ADR repository. The catalog may index decision anchors/IDs. Split-per-decision ADR files become warranted only if review/edit/search friction or concurrency makes the monolith materially costly.

### K4. No forced `src/`/package move in v1

Current tools are small, repository-local and mostly standard-library Python. The new engineering tooling can begin in the existing `tools/` model. A package move becomes a triggered change if internal imports, test isolation, reuse, dependency management or distribution pressure materially worsens.

This is a trigger-based conclusion, not a permanent prohibition.

---

## L. Context / discovery architecture

### L1. Profiles

`engineering/context-profiles.json` defines **navigation/query composition**, never canonical content.

Required profiles:

1. `scholarly-project` — existing `project_context.py` remains primary;
2. `system-development` — GO/AGENTS + engineering current state + active change/current focus + applicable rules + open material findings + relevant baselines;
3. `architecture-review` — current change problem/Requirements/research/options/design + backward trace + unresolveds;
4. `human-decision` — decision-ready surface only, with expandable evidence;
5. `maintenance` — changed canonical owner + impacted relations/views/validators;
6. `specialist-review` — only where domain/scholarly validation is actually applicable.

### L2. Progressive disclosure contract

Initial context should contain:

```text
purpose / authority
current configuration
current change/focus or explicit absence
current stage/readiness/admission
applicable Requirements/rules
open blocking uncertainty
bounded work / decision boundary
references to evidence/history
```

Deep audit prose, closed changes and superseded designs are loaded only when the current question requires them.

### L3. Fresh-context target

A fresh developer/agent should not need to read the dated audit chain merely to answer:

- what is current;
- what is proposed;
- what is admitted;
- what is open;
- what applies;
- why a decision is needed;
- where evidence lives.

History remains immediately expandable by stable refs.

---

## M. Development method from problem framing to DEV-READY

The logical method and practical infrastructure are separate concerns but share state.

### M1. Method capabilities

For a material change, the system can require any of:

```text
Problem / stakeholder need
Root-cause / systems analysis
Requirements / acceptance
Research / SOTA / domain evidence
Concept exploration / trade study
Detailed design
Migration / compatibility design
Implementation planning
Verification planning
Validation planning
Operational/developer readiness
Human decision readiness
```

These are not a fixed stage pipeline.

### M2. Operational rule

For each capability, `STATE.json` records one of the semantic conditions:

```text
required-open
required-satisfied
not-required-with-rationale
blocked
re-entered
```

Literal persisted tokens may be adjusted during implementation if the same semantics are preserved.

### M3. Re-entry

Examples:

- Research falsifies a Requirement assumption → Requirements re-enter;
- Design reveals an untested root-cause alternative → analysis/research re-enter;
- migration trial exposes semantic loss → Design re-enters;
- verification failure re-enters Design/Implementation without rewriting the original Problem;
- Human feedback changes the understood Intent → Problem/Requirements may re-enter under the applicable authority.

### M4. DEV-READY derivation

A material change is DEV-READY only when:

1. the bounded problem and evidence are reconstructable;
2. material competing root causes are dispositioned;
3. solution-independent Requirements/acceptance exist;
4. required Research is closed or explicitly not required;
5. materially different concepts were compared where credible;
6. selected Design includes information ownership, interfaces, lifecycle/failure behavior and Human/AI/specialist boundaries;
7. physical repository impact and migration are defined;
8. developer/bootstrap/build/test impact is defined;
9. verification/validation/fitness fixtures are defined before implementation;
10. blocking uncertainty is empty or represented as the exact Human/specialist decision required;
11. implementation can proceed without inventing another material architecture/information-model decision;
12. the Human D-016 decision surface is derivable from this same state.

---

## N. Practical developer infrastructure

### N1. Developer entry path

Target Human/developer navigation:

```text
README
→ engineering/README
→ engineering/generated/CURRENT_STATE.md
→ active change context (if applicable)
→ one local assurance command
```

`engineering/README` is stable reference/how-to material, not current programme history.

### N2. Local runtime

Initial implementation should preserve the current low-dependency posture:

- Python 3.12, matching CI;
- standard library unless a demonstrated need requires a dependency;
- existing repository-local tools remain callable;
- no devcontainer/package manager/service is required simply to appear modern.

### N3. One developer check command

Add a thin `tools/check.py` (or an equivalent single command owned by `tools/engineering.py`) that executes the complete deterministic repository assurance set:

```text
Source Contract validation
engineering knowledge/configuration validation
all unit/regression tests
generated-view freshness check
internal reference/link/path checks in managed engineering assets
```

CI calls the same command rather than maintaining a second hidden developer contract.

### N4. Query before read-all

A developer should query the engineering plane first and expand only relevant owners. Full-text Git/GitHub search remains useful, but semantic currentness must not depend on guessing filenames/search terms.

---

## O. CI / architecture fitness functions

The target CI adds deterministic checks without pretending to validate scholarly meaning.

### O1. Catalog integrity

- unique artifact IDs;
- unique registered canonical paths;
- paths resolve;
- kinds/authority/lifecycle combinations valid;
- no generated view registered as canonical content owner;
- change IDs resolve.

### O2. Configuration integrity

- current architecture/Requirements refs resolve;
- active changes resolve;
- current focus is null or one of the explicitly active changes;
- superseded/rejected artifacts cannot be selected as current baselines;
- no recency-based inference.

### O3. Trace integrity

- relation endpoints resolve;
- relation predicates are controlled enough for deterministic meaning;
- candidate relations do not masquerade as accepted;
- no direct verification→Human-acceptance alias.

### O4. Promotion / orphan insight check

For every registered material finding in a closed source artifact/change:

- disposition must be explicit;
- a disposition that requires a target must resolve;
- `deferred` requires a trigger or rationale;
- `superseded` identifies the superseding referent where known.

This is the deterministic protection for the "lost rich moment" failure.

### O5. Generated-view freshness

Regenerate `CURRENT_STATE`/`CATALOG`; CI fails on diff if committed generated views are stale.

### O6. Fresh-context regressions

Tests assert that standard profile compilation does not require historical audit chronology for current state and that negative authority/current-focus cases remain explicit.

### O7. Existing assurance boundary remains

A green workflow proves the machine-checkable contracts only. It does not establish manuscript truth, specialist validity, Human understanding/acceptance or D-016 admission.

---

## P. Brownfield migration design

The current repository must not be "cleaned up" by deleting its history. Migration is semantic classification + controlled path change.

### P1. Stage M0 — classify before moving

Create the catalog and classify the current `requirements/` inventory in place.

At minimum distinguish:

- formal Requirement baselines;
- audits/problem analyses;
- Research;
- Concepts/Design;
- admissions/decisions;
- result reviews;
- learnings;
- work instructions/prompts;
- historical coordination artifacts.

No file is moved until every material file has a role, lifecycle state and target class.

### P2. Stage M1 — current configuration and finding disposition

Populate:

- current architecture/configuration refs;
- current active change state;
- material findings from the Oct-02→Oct-04 knowledge/lifecycle/design sequence;
- explicit forward dispositions.

This is the highest-value migration because it recovers current meaning before physical cleanup.

### P3. Stage M2 — physical IA migration

Use `git mv` and automated repo-wide reference repair.

Rules:

- `requirements/` retains only Requirement baselines;
- audits/research/learning move to `engineering/evidence/...`;
- programme/change-specific concept/design/admission/result artifacts move under semantically appropriate `engineering/changes/<id>/` history or evidence paths;
- ambiguous legacy files may remain temporarily at old paths but must be cataloged and excluded from current context;
- `engineering/catalog/legacy-paths.tsv` records old→new mapping during transition;
- no duplicate copies as compatibility shims unless an external stable-link requirement is demonstrated.

Git history preserves file genealogy.

### P4. Stage M3 — README reduction

After generated current state is reliable, remove research-system chronology from README. README becomes a stable map:

```text
Purpose
Research path
Engineering path
Where canonical truth lives
How to derive current context
```

Historical programme narrative remains discoverable through the engineering catalog/change history.

### P5. Stage M4 — context/query adoption

Add engineering profiles and make fresh system-development contexts use them instead of dated-audit replay.

### P6. Rollback

Each migration WP must be independently reversible by Git. The catalog provides path/meaning trace, so rollback does not depend on chat memory.

---

## Q. Disposition of major accumulated learnings

This matrix is intentionally included so the rich recent audit sequence does not disappear into another summary.

| Prior learning / evidence | Current disposition in this design |
|---|---|
| F07 `requirements/` heterogeneous roles | **PROMOTED** → EKR-06/09 + narrowed Requirements namespace + engineering IA |
| F08 active vs persisted knowledge insufficiently separated | **PROMOTED** → Information Asset lifecycle + generated default-current context |
| F04 Issue chronology can become restart/runtime context | **PROMOTED** → engineering Configuration + change state + derived views |
| F05 work/programme closability gap | **PROMOTED** → bounded change lifecycle + terminal Result + inactive history |
| F06 decision promotion incomplete | **PROMOTED/REFINED** → keep DECISIONS owner, index accepted rationale through catalog/relations |
| F12 adequacy/minimality bias | **PROMOTED AS DESIGN DISCIPLINE** → larger options evaluated; architecture selected by closure not size |
| derived views useful but downstream of clear owners | **RETAINED** → current/catalog/context are derived only after Configuration/IM owners |
| Human should not be workflow relay | **RETAINED** → change state/context allows routine continuation; no ceremonial confirmation |
| `AUTHORIZATION ≠ INFORMED DECISION READINESS` | **PROMOTED** → generated Human decision profile/brief and DEV-READY criterion |
| `Human-in-loop ≠ Human understands loop` | **PROMOTED** → Human decision readiness is validation requirement |
| `Reduce reconstruction, not evidence` | **PROMOTED** → progressive disclosure/context profiles |
| `outcome_context` deliberately has no generic work generation | **PRESERVED BOUNDARY** → scholarly context stays separate from engineering change state |
| Project context compilation is successful pattern | **GENERALIZED WITH FIT** → separate engineering context compiler over engineering owners |
| Genericity ≠ Distribution | **RETAINED** → no package/service/template productization requirement |
| package/src threshold not previously reached | **RETAINED AS CURRENT EVIDENCE, NOT PERMANENT RULE** → trigger-based package move |
| Wirknetz as trace/reconstruction lens | **RETAINED** → finding/relation trace semantics, no Wirknetz runtime |
| Track-B #76 `EXISTING MECHANISMS SUFFICIENT` for tested boundary | **NEGATIVE EVIDENCE PRESERVED** → no Bridge Skill/capability introduced |
| relation correctness > completeness | **PROMOTED** → material relation catalog only; candidate relations explicit |
| latest-wins prohibited | **PROMOTED** → lifecycle/supersession metadata + current Configuration owner |
| verification != validation | **PROMOTED** → distinct trace relations and DEV-READY/acceptance states |
| previous SD-01 bounded revision package | **PARTIALLY RETAINED** → bounded change workspace becomes one component, not whole architecture |
| previous rejection of requirements reorganization/index/context expansion | **SUPERSEDED** → fresh evidence shows these are material, not optional future details |

---

## R. Qualification fixtures for this architecture

The implementation is not acceptable merely because files/tools exist.

Required fixtures:

1. **New-chat scholarly bootstrap** — existing Project path remains correct.
2. **New-chat system-development bootstrap** — current system state without dated-audit replay.
3. **New developer bootstrap** — from clone to current architecture/change state + full local validation using the documented path.
4. **History-heavy repo** — add closed/historical artifacts; default system-dev context size/semantics do not grow proportionally.
5. **Rich multi-audit synthesis** — multiple material findings survive closure with individual dispositions.
6. **Finding promotion** — finding → accepted Requirement/Decision/Design relation is queryable.
7. **Finding rejection/defer** — rejected/deferred finding remains visible with rationale/trigger but absent from current target.
8. **Requirement backward trace** — current Requirement → source findings/evidence.
9. **Decision backward trace** — decision → context/alternatives/evidence.
10. **Local result → whole system** — child work changes configuration/plan consequence before closure.
11. **Closed change deactivation** — Result/history remain retrievable but leave default current context.
12. **Concurrent investigations** — two investigations coexist without recency implying priority or one overwriting the other's state.
13. **Tiny bug** — existing baseline permits direct bounded repair without artificial Research/Concept artifacts.
14. **Material architecture change** — full capability coverage and D-016 boundary required.
15. **Different manuscript Project** — engineering architecture remains generic and does not encode current manuscript fixtures.
16. **Human decision surface** — Human can state what admission changes/does not change and which uncertainty remains.
17. **Specialist decision surface** — domain validation is not mislabeled as Human governance or technical verification.
18. **Context starvation trap** — compiler may not omit material uncertainty/authority/evidence merely to reduce size.
19. **Stale-current trap** — generated view and configuration conflict causes CI failure.
20. **Orphan insight trap** — closed audit with undispositioned material finding causes CI failure.
21. **False relation trap** — plausible unsupported relation cannot be promoted merely to complete the trace.
22. **Migration loss test** — legacy path/content/provenance remains recoverable after `git mv` and link repair.

---

## S. Developer-ready implementation programme — candidate `SD-KA-01`

If Human Owner later chooses `ADMIT`, the material change authorized should be bounded as:

> **SD-KA-01 — Repository-native Engineering Knowledge & Configuration Plane + Development Readiness Operationalization**

### S1. WP1 — engineering information/configuration contracts

Create:

- `engineering/README.md`;
- `engineering/configuration.json`;
- catalog TSVs and schemas/contracts;
- minimal validator/query runtime;
- initial current architecture baseline.

Exit: current configuration and information-asset roles are machine-resolvable without moving legacy files yet.

### S2. WP2 — legacy classification + finding promotion baseline

Classify the existing `requirements/` inventory and register the material Oct-02→Oct-04 findings/dispositions.

Exit: no current system-development claim depends on an unclassified dated file; material recent findings have forward disposition.

### S3. WP3 — physical repository IA migration

Narrow `requirements/` to Requirements, migrate system-development evidence/change artifacts to `engineering/`, repair internal references, keep a migration path map.

Exit: repository top-level semantics match content responsibilities; Git provenance intact.

### S4. WP4 — current-state/catalog derivation + context/query compiler

Implement generated `CURRENT_STATE`/`CATALOG`, profiles and `engineering.py context/query/decision-brief`.

Exit: Fresh system-development/developer/Human-decision contexts no longer require audit chronology.

### S5. WP5 — Development Readiness operationalization

Refine `maintenance.md`, `workflow.md` and `quality-and-learning.md` only as needed so material-change `STATE.json` coverage/readiness/admission semantics are canonical and proportional.

Exit: tiny bug remains lightweight; material coupled change cannot jump from Finding to implementation-shaped Work.

### S6. WP6 — developer contract + CI fitness

Add unified local check command and CI checks for engineering catalog/config/trace/promotion/generated-view invariants.

Exit: developer and CI run the same deterministic contract; stale/current/orphan fixtures fail.

### S7. WP7 — adversarial qualification + terminal result review

Run all Section-R fixtures, exact-head assurance and Human/restartability validation. Promote consequential accepted rationale to `DECISIONS.md`; create terminal Result; close the change without automatically creating a successor.

---

## T. Expected material implementation surface

The developer must not need to invent the following scope after admission.

### Create

```text
engineering/README.md
engineering/configuration.json
engineering/context-profiles.json
engineering/architecture/SYSTEM.md
engineering/catalog/artifacts.tsv
engineering/catalog/findings.tsv
engineering/catalog/relations.tsv
engineering/catalog/legacy-paths.tsv       # migration-time
engineering/changes/SD-KA-01/STATE.json
engineering/changes/SD-KA-01/PROBLEM.md
engineering/changes/SD-KA-01/REQUIREMENTS.md
engineering/changes/SD-KA-01/DESIGN.md
engineering/changes/SD-KA-01/PLAN.md
engineering/changes/SD-KA-01/RESULT.md      # terminal only
engineering/generated/CURRENT_STATE.json
engineering/generated/CURRENT_STATE.md
engineering/generated/CATALOG.md
tools/engineering.py
tools/check.py                              # or equivalent single check entrypoint
```

### Update

```text
README.md
requirements/README.md                     # create if absent during migration
requirements/domain-requirements.tsv       # content only if migration/IDs require; no semantic rewrite by default
methodology/maintenance.md
methodology/workflow.md
methodology/quality-and-learning.md
DECISIONS.md                               # accepted rationale only
.github/workflows/source-contract.yml       # or split workflow if clearer
existing tests + new engineering tests
internal links/references affected by migration
```

### Move after classification

Current non-Requirement `requirements/*.md` artifacts into semantically appropriate `engineering/evidence/...` or `engineering/changes/...` locations using `git mv` + verified link rewrite. Exact mapping is generated in WP2 before movement; ambiguous legacy items may remain cataloged in place until disposition is safe.

### Explicit non-goals for SD-KA-01

- no manuscript Project scope/NEXT ACTION;
- no Source/File/Project scholarly model redesign;
- no database or graph service as canonical truth;
- no Backstage/developer-portal deployment;
- no workflow engine/autonomous planner;
- no Wirknetz runtime/Skill/Bridge;
- no mandatory new package/src layout;
- no release/template/productization work;
- no #90/branch-protection reactivation;
- no inference that #225 achieved whole-system scholarly acceptance;
- no automatic successor system programme.

---

## U. Residual uncertainty and explicit future triggers

These are **non-blocking for SD-KA-01 architecture**, but remain visible.

| Question | Current disposition | Trigger for larger mechanism |
|---|---|---|
| Derived SQLite/search index? | not needed initially | catalog/query performance or relation traversal becomes materially costly |
| Graph database? | unsupported | repeated queries require graph operations that TSV/derived index cannot satisfy without correctness/maintenance loss |
| Developer portal? | unsupported | multiple teams/repos/personas create sustained discoverability/self-service burden not served by Git/GitHub/static views |
| `src/` package? | not required now | internal runtime coupling/import/test/distribution friction crosses observed threshold |
| per-decision ADR files? | keep `DECISIONS.md` | decision edit/review/search/concurrency friction becomes material |
| workflow/orchestration engine? | unsupported | repeated observable execution-state failures remain after explicit change state/context and cannot be handled by bounded tooling |
| richer semantic relation model? | start minimal | action-relevant distinctions cannot be represented without ambiguity or false traceability |
| concurrent admitted implementations? | supported conceptually, not yet exercised | first real overlapping admitted change requires conflict/affected-configuration refinement |

No option is excluded because it is "too big". Each waits for the evidence that makes its additional responsibility necessary.

---

## V. DEV-READY qualification of this design

| Dimension | Result |
|---|---|
| Problem framing | sufficient; includes History, lost audit insight, IA, DevEx and method/infrastructure coupling |
| Root-cause analysis | sufficient for architecture choice; multiple causal families preserved |
| Requirements | solution-independent baseline established in Section H |
| Targeted Research | sufficient for decision; RE/SE-CM/IM/DevEx/context/decision/fitness/documentation comparators covered |
| Competing concepts | materially distinct A–G compared |
| Selected architecture | explicit and falsifiable |
| Information model | artifact/finding/relation/config/change ownership defined |
| Physical repository target | defined |
| Context/query design | defined |
| Developer/bootstrap contract | defined |
| migration | staged, loss-controlled, rollback-capable |
| CI/fitness functions | defined |
| implementation WPs | bounded and ordered by dependency, not by arbitrary ceremony |
| verification/validation fixtures | defined before implementation |
| Human decision surface | defined below |
| material implementation | **NOT STARTED** |
| D-016 admission | **NOT GIVEN** |

The key DEV-READY test is satisfied at design level:

> a competent implementer should not need to invent a new material information-architecture, state-ownership, lifecycle, migration, query/context or assurance decision in order to implement SD-KA-01 as specified.

Routine representation choices remain implementation-owned. Any genuinely new material semantic/architecture choice returns to D-016.

---

## W. Human D-016 decision surface

### Exact current state

```text
Prior narrow DEV-READY claim        FALSIFIED / SUPERSEDED AS SUFFICIENT WHOLE DESIGN
Holistic problem re-baseline        SUFFICIENT
Repository / IA / DevEx audit       SUFFICIENT
Insight-promotion audit             SUFFICIENT
Root-cause analysis                 SUFFICIENT
Targeted SOTA / comparator research SUFFICIENT
Solution-independent Requirements   SUFFICIENT
Competing architecture trade study  COMPLETE
Detailed target architecture        SUFFICIENT
Migration / CI / developer design   SUFFICIENT
Implementation plan                 BOUNDED
Implementation                      NOT STARTED
D-016 admission                     NOT GIVEN
```

### `ADMIT`

Authorizes only **SD-KA-01** Sections S/T under the stated non-goals, including routine implementation/migration choices that preserve these semantics.

It does **not** authorize manuscript work, a portal/service, graph DB, workflow engine, productization, branch protection, or unrelated architecture changes.

### `REFINE`

Means one or more material Requirements/architecture/migration/operating-model points above should change before development. The exact point should be named; the rest remains evidence.

### `DEFER`

Preserves this holistic DEV-READY design as non-normative evidence/current candidate without implementation.

### `REJECT`

Rejects the selected EKCP architecture; evidence/Requirements remain available for a replacement concept/design pass.

---

## X. External/comparator references used

Authoritative/current external comparators consulted for this pass:

- ISO/IEC/IEEE 29148:2018 — Requirements Engineering: https://www.iso.org/standard/72089.html
- NASA Systems Engineering Handbook — Technical Data / Configuration Management: https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf
- SEBoK v2.14 — Configuration Management: https://sebokwiki.org/wiki/Configuration_Management
- SEBoK v2.14 — Configuration Baselines: https://sebokwiki.org/wiki/Configuration_Baselines
- SEBoK v2.14 — Information Management: https://sebokwiki.org/wiki/Information_Management
- Backstage Software Catalog — source-controlled metadata/catalog pattern: https://backstage.io/docs/features/software-catalog/
- Anthropic — effective context engineering for agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- AWS Prescriptive Guidance — Architectural Decision Records: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/introduction.html
- Thoughtworks — evolutionary architecture / fitness functions: https://www.thoughtworks.com/en-de/insights/books/building-evolutionaryarchitectures-second-edition
- Diátaxis — documentation user-needs separation: https://diataxis.fr/start-here/

Internal comparator evidence from `esany/Wissensarbeit` was used only as falsification/property evidence, especially current generated state/execution state, the design-methodology delta, #52/#53/#54/#55, Wirknetz reconstruction #56/#58 and Track-B #76 independent result.

---

## Y. Final verdict

The repository has not lost its scholarly governing whole. Its scholarly Source/File/Project architecture and evidence discipline are materially stronger than its current **engineering knowledge/configuration architecture**.

The previous response attempted to solve a systemic information/configuration/development problem mainly with a better bounded change package. That was not enough.

The sufficient target is now:

```text
SCHOLARLY PRODUCT / GOVERNING OBJECTIVE
        ↓
formal Requirements + METHOD + Project/Corpus truth
        ↓
ENGINEERING INFORMATION MANAGEMENT
  artifacts + findings + relations + lifecycle
        ↕
ENGINEERING CONFIGURATION MANAGEMENT
  approved current baselines + active changes
        ↕
BOUNDED CHANGE STATE
  problem → needed development capabilities → Requirements → Research
  → Concepts → Design → DEV-READY → D-016 → implementation → result
        ↕
DERIVED CURRENT / QUERY / CONTEXT SURFACES
        ↕
DEVELOPER / AGENT / HUMAN / SPECIALIST USE
```

The whole no longer depends on replaying every detail, and detail is not discarded from the whole:

```text
capture evidence
→ register material information
→ analyse
→ disposition material findings
→ promote accepted/current consequence
→ baseline/configure
→ execute bounded change
→ verify / validate
→ reconcile current configuration
→ deactivate historical working context
→ retain exact provenance for expansion
```

This is the requested boundary: **a holistic, practical, repository-first architecture is now DEV-READY for a Human D-016 decision, but it is not admitted and nothing in the target architecture has been implemented.**
