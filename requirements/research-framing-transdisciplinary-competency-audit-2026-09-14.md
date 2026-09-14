# Research framing, transdisciplinary competency and role-absorption audit — 2026-09-14

Status: **analytical / audit evidence only; not normative METHOD, not a new Requirement owner, not a new Project priority, not implementation authority.**

Repository baseline reviewed: `main@f79b69eb9eaeee5d89a70b6c4e38a0c85587774b`.

## 1. Audit question

This audit asks whether `paleo-type` already contained sufficiently strong rules for:

- research framing before local problem execution;
- transdisciplinary competition/synthesis between relevant scholarly competencies;
- translation and authority boundaries between scholarly/domain work and technical/RSE work;
- Human-Owner control of purpose and priority without using the owner as a substitute specialist or engineer;
- preserving useful research structures when simplifying the repository/process;

and, if so, whether later consolidation/lean-down accidentally weakened those functions even when the underlying rules remained correct.

This audit is prompted by the observed risk that excellent local execution, provenance, assurance and task restartability can coexist with a scientifically too-small or badly framed research question.

## 2. Governing findings already present before this audit

### 2.1 Transdisciplinarity is a governing invariant, not a new proposal

`GOVERNING_OBJECTIVE.md` already defines the work as a **transdisciplinary research problem**. The research question and source determine which scholarly domains, methods and expertise are required; no pilot, discipline, standard, model or architecture is sufficient by default.

Its precedence is also explicit:

`GOVERNING OBJECTIVE → scholarly/research requirements → disciplinary/epistemic requirements → methodology/research gates → corpus/project information model → Human-in-the-loop/validation → software/AI/automation/GitHub/presentation`.

Therefore technical structure is subsidiary to scholarly meaning by design.

### 2.2 The repository previously modelled a real division of labour

The role/handoff programme in Issues #71–#79 was more than chat specialization. It described a reusable authority topology:

- **#72 Source Research** — direct evidence-bound manuscript/source work; applies palaeography, philology, editing, diplomatics/archival reasoning, source criticism, notation/metrology and material observation only as the actual problem requires; produces source-local/project findings and uncertainty.
- **#73 Domain Review** — cross-disciplinary scholarly synthesis and research sequencing; classifies findings, activates implicated disciplines, determines the next scholarly admissible step inside Human-Owner purpose, derives reusable requirements only where justified, and mediates the scholarship↔Dev boundary.
- **#74 Development / Implementation** — implements an already established/bounded technical requirement; must not reinterpret scholarly ambiguity into convenient architecture; returns work for scholarly adequacy review.
- **#75 Human Owner / Governance** — controls research purpose, priorities, project boundary, consequential use/publication and material-change admission; must not be used as fallback palaeographer, historian or software architect.
- **#76 independent specialist review** — remains distinct from AI-assisted scholarly/domain work.
- **#77 work-context/handoff scaffold** — aimed to standardize process/restartability, not scholarly outcome.
- **#79 RSE/AI-systems competency refinement** — established that technically correct research-system work requires Requirements Engineering, provenance/data stewardship, verification/semantic-loss testing, AI context/tool engineering, HITL, auditability and scholarly-interface literacy in addition to coding competence.

The important architecture was therefore not `many agents`. It was **competence- and authority-sensitive work decomposition with explicit handoff and return**.

## 3. The original transdisciplinary synthesis function

#73 is the clearest prior owner of the function now at risk of becoming implicit.

Its intended path was:

```text
source/research evidence
→ disciplinary review
→ consequence classification
→ next scholarly admissible step
→ if justified: reusable requirement
→ if justified: bounded Dev handoff
→ Dev return
→ scholarly adequacy review
→ return to research
```

It explicitly prohibited the inverse path:

```text
technical preference / existing architecture
→ inferred research requirement
→ source forced to fit
```

#73 also carried **research-sequencing authority** within the Human-Owner-defined purpose. It could change order or return to evidence when, for example:

- relevant source evidence had not been inspected;
- downstream interpretation contaminated upstream observation;
- implementation/representation was being chosen before semantic evidence existed;
- a relevant scholarly domain had not yet been applied;
- unresolved specialist judgement was being reframed as a software/completion problem;
- Dev/support work displaced the active scholarly action without a demonstrated need.

This was not mission-level authority. It was a transdisciplinary scholarly arbitration/synthesis function.

## 4. Concrete evidence that the model worked

`projects/ega-reg-ii-5-knau/research/g2-domain-review-checkpoint-b.md` demonstrates a real instance.

The review did not ask one discipline to decide everything. It evaluated each finding across:

```text
source-bound observation
→ demonstrated loss/adequacy
→ is scholarly information established?
→ applicable disciplinary requirements
→ current canonical support
→ actual remaining gap
→ source/project/method/system/specialist consequence
→ smallest justified action
```

Examples include physical line/order evidence reviewed jointly through editing, codicology and archival/addressing requirements; cancellations separated into observed phenomenon versus unresolved deleted wording; notation facts separated from metrological interpretation; and legacy representation limits separated from actual system requirements.

A crucial #73 clarification was:

> A representational gap is not automatically a Dev handoff.

The required decision path was:

```text
is the scholarly information itself established?
  no → continue research
  yes ↓
can an existing canonical owner carry it losslessly?
  yes → project/method use or no system change
  no ↓
is the missing distinction reusable/material enough to need system support?
  yes → candidate Dev handoff, subject to existing admission
```

This remains a strong generic model for avoiding technology-led reinterpretation.

## 5. What was intentionally absorbed rather than abandoned

The repository later closed #71–#79 as completed/absorbed rather than keeping a permanent role/process programme.

For #77 in particular, the recorded conclusion was that `methodology/workflow.md` had absorbed the necessary semantics and that no template family, master prompt, prompt registry, validator, agent framework or workflow engine was justified.

That consolidation was substantively sensible:

- it avoided duplicated governance;
- it prevented form-filling from displacing source work;
- it preserved model/session independence without forcing identical scholarly judgements;
- it moved stable operational semantics into one canonical workflow owner;
- it retained the principle `standardize the path, not the scholarly outcome`.

The current `methodology/workflow.md` still strongly preserves:

- role/task/stage/cursor semantics;
- semantic-boundary and meaning-preservation checks;
- source/domain→Dev handoff expectations;
- Dev→Domain return;
- technical PASS ≠ scholarly acceptance;
- resource state ≠ task authority;
- target authority and dependency provenance;
- repository-first persistence;
- no-progress-loop control.

Therefore the earlier role work was not simply lost.

## 6. What became less visible during lean-down

The consolidation preserved **cross-boundary execution** better than **pre-task scholarly framing**.

The present workflow is strong once a task, target and required domain meaning have already been established. It is less explicit about the prior operation:

> Which scholarly competencies should be activated before selecting the next research question, which one leads which sub-question, how conflicts between their perspectives are adjudicated, and how their synthesis affects research priority?

The older #73 role made this active cross-disciplinary synthesis visible. The current method still lists and routes expertise, but the operation that converts multiple relevant disciplinary perspectives into a **research-framing / research-selection judgement** is less operationally salient.

This is consistent with later project evidence: the system became increasingly good at executing a selected bounded task while still being vulnerable to selecting or protecting a scientifically too-small task.

## 7. Competency leadership should be question-relative, not permanently hierarchical

The evidence supports a generic principle that is already implicit but not yet fully operationalized:

**No discipline or technical competence is the permanent leader. Leadership is determined by the claim/question being adjudicated.**

Illustrative allocation:

| Question / decision type | Competence that normally leads | Required subordination / interface |
|---|---|---|
| What documentary object/process is this? | archival science / diplomatics / source-type history | technical metadata follows the established documentary semantics |
| What is the physical/material/textual organization? | codicology/material study + diplomatics/editing as relevant | palaeography/philology interpret only after structure is observed |
| What graph/sign is written? | palaeography | semantic plausibility may generate tests but cannot manufacture graphemes |
| What does a historical word/form mean? | historical philology/lexicography | depends on an evidentially supported reading |
| What does a number/unit/accounting sign mean? | notation/metrology/accounting history, after sign reading | written sign identity remains palaeographic evidence, normalized value is separate |
| What institutional/legal/social function does a passage perform? | source criticism + relevant domain history, with diplomatics | text/layout evidence constrains interpretation |
| How should established distinctions be represented computationally? | Requirements/RSE/information modelling | implementation must preserve domain semantics and may not redefine them |
| What is the project's purpose/priority/scope? | Human Owner | scholarly roles may recommend and explain; they do not silently substitute owner authority |

This is not a universal role registry. It is a **claim-sensitive subsidiarity rule**.

A competence may lead one sub-question and be subordinate on another.

## 8. Translation is itself a consequential interface

The current `workflow.md` correctly requires meaning-preservation checks whenever consequential meaning crosses:

- scholarly domain → scholarly domain;
- Domain → Dev/RSE;
- Dev/RSE → Domain;
- human language → structured value;
- machine token → human explanation;
- language translation.

Recent failures show why this matters. Several different mistakes share a common structure:

```text
cross-witness correspondence range → target-witness analysis unit
resource unavailable → task/roadmap blocker
technical/CI PASS → implied scholarly adequacy
legacy project/path organization → present project/priority authority
```

In each case, a fact valid in one semantic layer was silently promoted into another layer with greater authority.

This suggests a cross-cutting failure pattern:

> **semantic/authority laundering across competence or representation boundaries**.

This audit records the pattern; it does not create a new controlled taxonomy by itself.

## 9. Review of apparently orphaned / demoted repository structures

Not every currently inactive structure is a lost good idea.

### 9.1 `palaeography/` — correctly demoted as current owner

The directory remains for recovery/history. The useful principle of graphical/notational comparison is retained. What was correctly rejected was artifact-first research (`lexicon/concordance exists → extend it`) and the assumption that same Source/context establishes same hand.

Disposition: **good method retained; misleading authority/topology correctly demoted.**

### 9.2 `apparatus/` — correctly historicized

`decisions.tsv` preserves old adjudication/recovery state but cannot establish present Reg. Ii 5 witness readings because of witness-provenance uncertainty.

Disposition: **decision-history value retained; old truth-owner authority correctly removed.**

### 9.3 old source-unit Projects — concept corrected, but audit-surface loss occurred

Treating individual Sources/records as Projects was wrong and was correctly removed. However, their separate STATUS surfaces carried evidence limits, dormant/activation state and restart points. Their removal created a real visibility loss later documented in Project `LEARNINGS.md` L013 and partly repaired through current STATUS/historical audit pointers.

Disposition: **correct semantic migration with acknowledged functional information loss.**

This is an important precedent for the current role/competency question: simplifying the model can be right while still losing a useful review function.

### 9.4 G2 Domain Review artifacts — completed fixture, but their reasoning operation remains valuable

`g2-domain-review-checkpoint-b.md` should not become a standing controller or parallel method owner. Its completed project-specific conclusions remain historical/research evidence.

However, the operation it demonstrates — transdisciplinary classification, semantic-gap testing, smallest-action selection, scholarly-vs-system distinction — is still generically valuable.

Disposition: **artifact correctly completed; cognitive/decision function may be underrepresented in current research framing.**

### 9.5 `context/context-notes.md` — epistemically protected, but potentially under-integrated into research framing

The file correctly isolates Human-supplied historical leads from blind transcription and states that they must not determine manuscript graphemes.

That separation is essential. The risk is a later overcorrection in which contextual/domain knowledge becomes so isolated that it no longer helps generate research questions after source observation.

Disposition: **contamination guard is correct; post-observation reactivation of domain/context expertise needs to remain available for question generation and interpretation.**

### 9.6 `source-understanding-synthesis-61v-63r.md` — current high-value research owner, but not itself a research-selection mechanism

The synthesis materially changed understanding of the locus and showed that many residual `unclear` spans are not understanding blockers. It now contains the corrected #166 structural/function result.

It is strong research evidence. What it does not by itself provide is a generic mechanism to ask relevant disciplines to generate and compare the next high-information research questions from that synthesis.

Disposition: **retained/current research asset; downstream framing function remains separate.**

## 10. Research-framing gap identified by this audit

The current architecture is strongest at:

```text
selected task
→ evidence control
→ bounded execution
→ handoff
→ technical/scholarly review
→ canonical persistence
```

It is weaker at:

```text
Project purpose
+ current source understanding
+ source-native structure
+ unresolved uncertainty landscape
+ relevant disciplinary perspectives
+ contextual/domain knowledge at the permitted stage
        ↓
competing/compatible research questions
        ↓
consequentiality / expected information gain / evidential tractability
        ↓
Human-Owner-informed priority / authorized next scholarly scope
```

This gap helps explain why excellent local controls can protect a low-leverage research question.

It also explains why later corrections risked oscillating between:

- micro-reading backlog;
- larger structural unit;
- source-wide survey;
- process/assurance work;

instead of preserving stable purpose while changing only the analytical scale required by the actual question.

## 11. What should not be restored

This audit does **not** recommend restoring:

- permanent per-discipline agents;
- #71–#79 as standing open programme;
- a workflow engine;
- a role registry;
- mandatory handoff templates;
- a universal source ontology;
- a permanent `Domain Review` truth owner separate from existing METHOD/Project owners;
- technical orchestration merely to simulate interdisciplinarity.

The earlier anti-bloat corrections remain valid.

## 12. Function that should remain visible in future review

The function worth preserving is smaller:

> Before a consequential new scholarly scope is selected, current Project purpose and source understanding should be reviewed through the actually implicated scholarly competencies; each competence should lead only the claim types it owns, conflicts should be translated at explicit semantic boundaries, and the resulting candidate research questions should be compared for scientific consequentiality before priority is set.

Technology participates only after the scholarly information requirement is sufficiently established, except where technical feasibility itself is part of the bounded question.

Human Owner retains purpose/priority authority, but should receive a research-facing decision surface rather than being asked to perform specialist synthesis or technical design.

This is recorded here as an audit conclusion, not yet a new METHOD rule or automatic next task.

## 13. Current disposition

Classification of the reviewed architecture:

- **Governing transdisciplinary objective:** retained and correct.
- **Source Research / Domain Review / Dev / Human Owner authority distinctions:** substantively retained; original role Issues completed/absorbed.
- **Domain↔Dev meaning-preservation and subsidiarity:** strongly retained in current workflow.
- **Research-framing / research-selection synthesis across multiple scholarly competencies:** present in principle and historical fixtures, but operationally less visible after lean-down.
- **Old project artifact directories:** mixed; some correctly demoted, some retain valuable evidence, and at least one earlier migration demonstrated that semantic simplification can lose useful audit surfaces.
- **Need demonstrated by this audit:** preserve/recover the transdisciplinary framing function without recreating the previous role/process bureaucracy.

No Project `NEXT ACTION`, METHOD change or implementation is authorized by this audit alone.
