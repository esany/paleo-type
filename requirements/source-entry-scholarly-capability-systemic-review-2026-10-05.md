# Systemic review — source-entry scholarly capability for an unfamiliar manuscript

**Status:** NON-NORMATIVE ANALYSIS → REQUIREMENTS → CONCEPT → PLANNING.  
**Authority boundary:** this artifact does **not** change METHOD, CORPUS, Project truth, Source/File contracts, Project scope, research priority or D-016 implementation admission.  
**Fresh repository baseline:** `main@2e1cb11cb4b8d709c44d28de072bda8b4af44f5c`.  
**Generic capability under review:** how `paleo-type` should move from an unfamiliar historical manuscript/archival unit to bounded, evidence-auditable scholarly work while supporting a non-specialist Human Owner transparently.  
**Wolkenburg role:** high-information falsification/validation fixture, not generic METHOD authority.

## 1. Repository-first basis

Freshly read for this review:

- `GOVERNING_OBJECTIVE.md`;
- `AGENTS.md`;
- `DECISIONS.md`, especially D-003, D-004, D-005, D-006, D-007, D-008, D-009, D-014, D-015, D-016, D-018 and D-019;
- `methodology/historical-source-workflow.md`;
- `methodology/research-gates.md`;
- `methodology/source-and-provenance.md`;
- `methodology/transcription-guidelines.md`;
- `methodology/evidence-policy.md`;
- `methodology/project-lifecycle.md`;
- `methodology/workflow.md`;
- `methodology/quality-and-learning.md`;
- `methodology/ai-governance.md`;
- `methodology/maintenance.md`;
- `requirements/domain-requirements.tsv`;
- current Issues #12, #115, #263, #265, #266, #267, #268, #269 and #270;
- draft PR #286 and `requirements/source-entry-reconnaissance-method-assistance-review-2026-10-05.md` as prior non-normative analysis provenance.

The repository already establishes several strong invariants:

- research activity is controlled by `research goal → research question → evidence needed → disciplinary method → claim type → permitted conclusion`;
- Source/File/Project/role/current-target meanings are separate;
- `OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION` must not collapse;
- S1–S9 are scholarly activities, not a rigid waterfall;
- G1–G6 are scope-bound maturity claims, not schedules;
- discovery, inspection, transcription and collation are distinct acts;
- source depth is open and evidence-driven rather than a fixed hierarchy;
- catalogue claims, direct inspection and textual/transmission claims have different evidential force;
- unresolved is a valid scholarly result;
- the Human Owner is not the default palaeographic/diplomatic/philological specialist;
- AI method compliance is not independent specialist validation;
- durable research state must be restartable without old chat.

The current source-entry problem is therefore **not** that `paleo-type` lacks evidence discipline or specialist-method principles. The problem is that the move from an *unfamiliar, internally unknown and partly unreadable source* into the existing S1–S9/G1–G6 model is not yet explicit and operational enough as one coherent scholarly capability.

## 2. External scholarly comparison used as falsification

The following current/authoritative or established professional references were used as methodological comparators, never as manuscript evidence:

- TEI P5 4.12.0 `<msPart>` / composite manuscript-part semantics: https://www.tei-c.org/Vault/P5/4.12.0/doc/tei-p5-doc/en/html/ref-msPart.html
- ICA Records in Contexts Conceptual Model 1.0: https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-conceptual-model/
- Association for Documentary Editing, *Minimum Standards for Electronic Editions*: https://documentaryediting.org/resources/about-documentary-editing/minimum-standards-for-electronic-editions/
- IDE, *Criteria for Reviewing Scholarly Digital Editions* 1.1: https://www.i-d-e.de/publikationen/weitereschriften/criteria-version-1-1/
- IDE/RIDE, tool/environment review criteria: https://www.i-d-e.de/publikationen/weitereschriften/criteria-tools-version-1/
- Cambridge, *English Handwriting 1500–1700*, conventions and alphabets: https://www.english.cam.ac.uk/ceres/ehoc/conventions.html and https://www.english.cam.ac.uk/ceres/ehoc/alphabets.html
- Folger, *Practical Paleography*: https://folgerpedia.folger.edu/Practical_Paleography
- DFG programme and digitisation guidance, including material-/goal-dependent full-text quality: https://www.dfg.de/de/foerderung/foerdermoeglichkeiten/programme/infrastruktur/lis/lis-foerderangebote/digitalisierung-erschliessung and https://www.dfg.de/resource/blob/176108/12-151-v1216-de.pdf

### What the external sources explicitly support

- scholarly editions need explicit aims, method, source/selection basis and transparent editorial practice;
- a selective edition is legitimate when the selection principle and extent are explicit;
- transcription is not identical to edition;
- composite manuscripts/documents may contain originally distinct parts and require part-sensitive description;
- records, agents, activities and instantiations are conceptually distinct;
- unfamiliar handwriting is learned through direct practice, recurring forms, alphabet/letterform comparison, abbreviations, numerals and stroke-level attention;
- transcription/full-text quality is purpose- and material-dependent rather than one universal level;
- tools/environments should be evaluated through real disciplinary use cases, not feature richness alone.

### Methodological synthesis, not direct quotations

Professional practice is compatible with an **adaptive source-entry loop** rather than `page 1 → full transcription → later palaeography`. A source may need broad reconnaissance before relevance is known; close pilot reading is itself a way of learning the hand and testing documentary structure; scope and editorial intent should be explicit but revisable; final editorial conventions belong later than initial orientation.

No inspected external reference justifies a fixed universal Source tree, a universal document ontology, automatic relevance classification, automatic copy/dependence detection or mandatory full-root diplomatic transcription before relevance is known.

## 3. Executive conclusion — the actual problem

The earlier formulation `reconnaissance + S2↔S3↔S4 iteration + provisional editorial intent + inspection ≠ scope ≠ transcription` was directionally correct but still described four local repairs.

The more accurate system-level diagnosis is:

> `paleo-type` lacks an explicit **adaptive source-entry research capability** that turns an initially unknown source into progressively warranted structure, reading competence, relevance, scholarly scope and next actions while exposing the governing discipline, evidence, claim ceiling and unresolved state to the Human.

That capability has four inseparable semantic functions:

1. **orient** — establish purpose/evidence and inspect broadly enough to understand what kind of source problem exists;
2. **learn** — acquire source-specific reading/structure competence through diagnostic inspection and pilot reading;
3. **bound** — distinguish inspection domain, discovered documentary structure, active scholarly scope and transcription scope without premature commitment;
4. **explain/persist** — make the current scholarly action intelligible to the Human and preserve enough research state to restart without replaying the chat.

The solution is therefore not one new stage and not one data table. It is a **conditional cross-cutting cycle over the existing S1–S4 region**, plus Human-facing action semantics and restartable state where the real case demonstrates that prose is insufficient.

This cycle must collapse to a light pass for a short, clear single document and expand only for complex, long, composite or hard-to-read material.

## 4. Target capability

When a previously unfamiliar historical manuscript/archival unit enters an authorized Project, a fresh capable context should be able to:

1. recover the research purpose/authority and exact evidence basis;
2. state a revisable **provisional editorial intent** sufficient to guide selection and representation without freezing the source prematurely;
3. determine the breadth/depth of reconnaissance required for the claim being attempted;
4. traverse the source in an order and depth adequate to notice relevant documentary boundaries, layout, missing material and candidate relevance;
5. identify what is merely observed, what is a provisional boundary/relevance hypothesis and what has enough evidence for a canonical Source/locus decision;
6. learn unfamiliar handwriting through exact internal comparison anchors and pilot reading before pretending that a full G2 transcription already exists;
7. form or revise a potentially empty, multiple, disjoint and evolving scholarly scope independently of inspection coverage;
8. enter bounded diplomatic transcription only for the scope where that depth is warranted;
9. activate the right specialist method from the observed problem without requiring the Human to know the discipline in advance;
10. state the evidence needed, claim ceiling and next discriminating action in ordinary scholarly language;
11. preserve `unresolved`, excluded-after-inspection and missing/unavailable states without converting them into absence or certainty;
12. escalate consequential unresolved specialist judgement rather than asking the Human to improvise expert validation;
13. persist restart-relevant state at its natural owner while avoiding universal ontologies and work-tracker bureaucracy.

## 5. End-to-end scholarly workflow — adaptive source-entry cycle

The existing S1–S9 method remains fundamentally sound. The missing capability is best understood as a **conditional source-entry cycle embedded across early S1–S4 activity**, not a new universal `S0` maturity gate.

```text
OWNER-GROUNDED PURPOSE / PROJECT AUTHORITY
        ↓
PROVISIONAL EDITORIAL INTENT
        ↓
EXACT SOURCE / FILE / ACCESS BASIS READY
        ↓
┌─────────────────────────────────────────────────────────────┐
│ ADAPTIVE SOURCE-ENTRY CYCLE                                │
│                                                             │
│ broad reconnaissance / sequence / completeness awareness    │
│        ↕                                                    │
│ documentary/material structure hypotheses                   │
│        ↕                                                    │
│ relevance discovery / exclusion / unresolved relevance      │
│        ↕                                                    │
│ palaeographic familiarisation + exact internal anchors       │
│        ↕                                                    │
│ pilot reading / pilot transcription                         │
│        ↕                                                    │
│ source/locus boundary adjudication where warranted          │
│        ↕                                                    │
│ active scholarly scope formation/revision                   │
└─────────────────────────────────────────────────────────────┘
        ↓ when sufficiently bounded for the current question
BOUNDED S2/S3 REPRESENTATION
        ↕
S4 INTERNAL PALAEOGRAPHIC / PHILOLOGICAL TESTING
        ↓
S5 INDEPENDENT COMPARISON / COLLATION
        ↓
S6 IDENTIFICATION / ENRICHMENT
        ↓
S7 SOURCE CRITICISM / HISTORICAL INTERPRETATION
        ↓
S8 CONSOLIDATION / VALIDATION
        ↓
FINAL EDITION CONCEPT + S9 / G6 EDITION
```

### Why this is not a new waterfall

- reconnaissance may continue on the uninspected remainder while a discovered relevant locus already enters deeper work;
- pilot transcription may precede full scope formation because close transcription is itself diagnostic;
- palaeographic familiarisation can occur before and during G2 construction;
- a later structure or relevance discovery can reopen an earlier boundary;
- the valid outcome of the cycle can be `no relevant locus found at the documented inspection coverage` rather than forced transcription.

## 6. What a very good historian/editor does at source entry

### First 10 minutes

- verify what archival/digital object is actually present and whether the required pixels are inspectable;
- recover why this object is under investigation and what the current research purpose is;
- look at beginning/end, pagination/folio/image order, obvious headings/layout and gross completeness;
- note whether the material appears single-document, composite, register-like, tabular/accounting, correspondence-like or unresolved;
- avoid deciding Source boundaries, document genre, hand identity or relevance from one visual cue;
- formulate the first bounded question in ordinary language.

### First 30 minutes

- sample enough distributed pages/folios to understand the source's variability and likely structure while preserving source order for any completeness claim;
- identify candidate starts/ends, layout shifts, additions, attachments, tables/registers, possible writing-characteristic changes and missing/unavailable areas;
- mark relevance only as `candidate`, `inspected-and-currently-not-relevant`, or `unresolved` where that is all the evidence supports;
- choose a few clear/diagnostic loci for closer reading;
- begin a local handwriting comparison basis from secure forms, recurring formulae, abbreviations, numerals and distinctive letter combinations.

### First 2 hours

- iterate between broader inspection and close diagnostic reading;
- use pilot transcription to test reading order, abbreviations, letterforms and documentary boundaries;
- revisit uncertain earlier loci as same-witness evidence grows;
- distinguish `possible writing-characteristic change` from a supported hand hypothesis and still further from named-scribe identification;
- refine candidate documentary units without creating a canonical Source for every heading or page break;
- decide whether any discovered relevant unit/locus is now stable enough to enter active scholarly scope;
- retain explicit open coverage, unreadable/missing material and negative findings.

### First work sessions

- continue ordered coverage to the breadth required by the relevance/completeness claim;
- progressively deepen only the portions that need source description, G2 representation or specialist analysis;
- persist consequential palaeographic anchors and decisions only when they materially support a reading/claim;
- establish internal Source identity only when stable identity/provenance/citation/relation/reuse/research requires it;
- route actual form/stage/transmission problems to #266/#269-type analysis only after direct-source fixtures exist;
- finalise neither a universal taxonomy nor publication conventions before the source has falsified or confirmed the provisional editorial intent.

## 7. Human scholarly-assistance model

A good METHOD is insufficient if the Human experiences only stage codes or generic cursor labels.

For consequential source work, the assistant should expose a **scholarly action claim** whose required meanings are:

```text
CURRENT OBSERVATION / UNCERTAINTY
→ BOUNDED SCHOLARLY QUESTION
→ GOVERNING DISCIPLINE / COMPETENCE
→ EVIDENCE OR TEST NEEDED
→ CLAIM CEILING / WHAT IS NOT ESTABLISHED
→ NEXT DISCRIMINATING ACTION
→ SPECIALIST ESCALATION TRIGGER, if applicable
```

This should be a Human-facing projection/compilation of existing owners, not a new canonical claim graph.

### Example

Black-box form:

> `S4 / reconnaissance continues`.

Required scholarly form:

> I am comparing these inspected pages for documentary starts/ends, writing-characteristic changes and recurring letter/abbreviation forms because we do not yet know whether this candidate section is structurally distinct or sufficiently relevant for deeper work. This is archival/diplomatic plus palaeographic analysis. A heading or script change can support a hypothesis but does not establish a new Source or named hand. The next discriminating action is to compare neighbouring boundaries and exact same-witness letterform anchors. If the evidence does not discriminate, the boundary/hand question remains provisional or unresolved.

### Competence routing

The Human should not have to know which auxiliary discipline to request. The assistant should route from the observed problem:

```text
source phenomenon / question
→ governing domain
→ method
→ required evidence
→ admissible claim
→ escalation threshold
```

Examples:

- hard grapheme → palaeography → exact same-witness graphical comparison → reading candidate / unresolved → specialist review if publication-consequential and evidence cannot discriminate;
- document function/stage → diplomatics → structure/formula/material/context evidence → bounded classification with evidence level → specialist review when legal/diplomatic classification is consequential and contested;
- historical term → philology/lexicography → inspected historical-language evidence after the graphematic basis → lexical/semantic claim only → specialist review if consequential and unresolved;
- accounting notation → palaeography + metrology/accounting history → raw sign + relevant system evidence → interpreted value kept separate from written sign;
- copy/extract claim → diplomatics/textual criticism → catalogue claim plus independent witness inspection/collation → relation only at demonstrated strength;
- owner/scribe/recipient role → archival/diplomatic/historical analysis → contextual evidence → role claim separate from mention/identity.

## 8. Persistent research-state model — semantic requirements only

A 200-page source investigation must survive interruption without turning every observation into a database entity.

The minimum restart-relevant semantic states are:

### A. Evidence and coverage basis

- exact Source/File/sequence evidence used;
- missing/unavailable/uninspectable regions;
- which loci/ranges/units were actually inspected;
- inspection purpose/depth sufficient to understand what the inspection can support.

### B. Relevance state

- candidate relevant;
- inspected and currently excluded for the research question;
- unresolved relevance;
- not yet inspected.

These are Project-relative research states, not Source identity properties.

### C. Documentary structure state

- observed structural cue;
- provisional boundary/unit hypothesis;
- confirmed/accepted Source or locus decision only when the existing Source rule is triggered;
- explicit unresolved boundary where necessary.

Do not require every provisional cue to become a persistent canonical Source object.

### D. Palaeographic learning state

Persist only consequential/reused evidence, for example:

- exact comparison anchors that materially support a promoted/rejected reading;
- observed discriminating/non-discriminating features;
- unresolved alternatives;
- supported hand hypotheses where they actually become consequential.

Do **not** require a universal hand registry or full alphabet table for every source.

### E. Reading/transcription maturity

Keep distinct:

- exploratory/pilot reading used for familiarisation/structure testing;
- canonical diplomatic representation contributing to G2;
- later internal analysis and consolidation.

A pilot line must not silently become a G2 completeness claim.

### F. Scholarly scope and current action

- Project root;
- inspection domain/coverage;
- active scholarly scope, including empty, multiple, disjoint and evolving Source/locus targets;
- historical/completed scope where needed;
- current bounded next action and its authority;
- specialist-review need/status where consequential.

## 9. Granularity and Source identity

The following is a **possible observational continuum**, not a fixed hierarchy:

```text
Archivale / documentary root
→ documentary complex
→ document
→ embedded copy / attachment / register / account / compilation
→ section / paragraph
→ locus
```

The current generic rule is retained:

> create a canonical Source only when stable identity, provenance, relation, citation, reuse or research actually requires it; otherwise the structure may remain a locus/observation.

A page break, heading, hand change, topic shift or catalogue phrase can generate a boundary hypothesis. None is individually sufficient to manufacture Source identity.

This area is **not** a generic METHOD gap at present. It becomes a representation or fixture problem only when a real case cannot be carried by the flexible Source/locus rule.

## 10. Where #266 and #269 belong in the end-to-end process

### #266 form / function / stage / condition

This is not the source-entry method itself. It is a **downstream representation consequence** triggered when direct inspection has produced a concrete documentary object/witness for which current metadata would collapse:

- documentary form/function;
- Source granularity;
- transmission/record stage;
- preservation/condition;
- evidence level.

The source-entry cycle is what creates the real fixture needed to decide the smallest stable representation.

### #269 relationship evidence strength

Likewise, this is not the early orientation method itself. It becomes actionable when an actual catalogue relation and/or independently inspected/collated text pair exists.

Keep distinct:

```text
same/related historical event or state
≠ same/similar wording
≠ textually corresponds to
≠ copy/extract/direct dependence
≠ structural part_of
```

The source-entry/independent-reading method supplies the evidence; #269 determines the smallest stable relation semantics/validation needed to prevent later misinterpretation.

## 11. Stress-test against materially different cases

| Case | Required behavior | Result for target model |
|---|---|---|
| A. short, clear single charter | reconnaissance/structure learning collapses to a light pass; proceed quickly to bounded G2 | **PASS** if no mandatory heavy survey bureaucracy is imposed |
| B. 250-page composite file with few relevant passages | ordered relevance coverage + structural discovery + disjoint scope + restartable coverage | **PASS**, requires #267/#265 state support |
| C. one difficult hand | familiarisation/pilot reading precedes/iterates with complete G2 | **PASS** |
| D. several writing-characteristic groups | observe first; hand hypotheses only after comparison | **PASS** |
| E. later extract of older document | present witness, earlier act/text, form/stage and relation remain distinct | **PASS conceptually; #266/#269 fixture required** |
| F. register/account instead of prose | layout/notation/domain routing activated; no prose-centric workflow | **PASS** |
| G. two records about same event with no textual dependence | event relation not upgraded to transmission | **PASS** |
| H. several related witnesses | each independently established/read before collation | **PASS under S5/G4** |
| I. missing/unavailable images | incomplete coverage explicit; no false absence/completeness | **PASS** |
| J. expected relevance not found | complete/adequate inspection may yield an evidenced negative result and no active scholarly scope | **PASS only if scope/coverage state supports this without filler** |

## 12. Gap map against current repository

Classification:

- **A** already adequately supported
- **B** METHOD clarification
- **C** genuinely new METHOD requirement
- **D** Human-assistance / execution requirement
- **E** persistent research-state requirement
- **F** CORPUS / Source / relation representation requirement
- **G** Project-state requirement
- **H** UI/context/navigation requirement
- **I** real-fixture / empirical validation only
- **J** specialist-review boundary
- **K** no action / overengineering risk

| Capability | Class | Current support | Actual gap / action |
|---|---|---|---|
| evidence before plausibility / layer separation | A | GO, AGENTS, evidence/transcription/method | no redesign |
| flexible Source depth / Source vs locus rule | A/I | source-and-provenance | validate on real Wolkenburg, no fixed tree |
| source-entry reconnaissance when relevance/structure unknown | B/C | implicit in S1/S2 and #267 | make conditional source-entry use explicit in authoritative method |
| palaeographic familiarisation before/during full G2 | B | S4 + non-waterfall rule | explicitly state S2–S4/pilot-reading iteration |
| provisional editorial intent | B/C | research-question control + S9 final concept | define only early revisable purpose/selection/representation intent; do not freeze final conventions |
| inspection domain ≠ scholarly scope ≠ transcription scope | B/G/E | gates + #265/#267/#270 comments | promote stable distinction to authoritative method/state semantics |
| Human-visible scholarly action claim | D/H | GO human auditability + workflow context pieces | explicit assistance contract; generic stage token is insufficient |
| competence/evidence/escalation routing | A/D/J | expertise-routing + domain requirements | make it visible in Human-facing source action, not new ontology |
| granular inspection coverage | E | #267 demonstrates gap | retain separate Project-local restart owner concept |
| empty/disjoint/evolving active scholarly scope | G | #265 corrected analysis demonstrates gap | reframe #265 around scope semantics, not `whole-root` enum |
| structural boundary hypotheses | A/E only on trigger | method supports observations/unresolved | do not prebuild universal boundary registry; persist only when restart/consequence requires it |
| pilot reading vs G2 representation | B/E on trigger | gates/transcription imply but do not name pilot state clearly | clarify method; add persistence only if real workflow loses the distinction |
| form/stage/condition representation | F/I | REQ-ARCH-010 + #266 | real fixture first |
| relation evidence strength | F/I | D-005 + #269 | real fixture first |
| root File supporting internal Source evidence | F/I | #268 | downstream once internal Source fixture exists |
| catalogue-bounded cross-Project selection | F | #263 | separate corpus-selection problem; do not absorb into source-entry method |
| corpus enumeration/completeness | E/F | #12 | separate discovery-coverage problem; do not absorb |
| independent specialist validation | J/A | GO/AI governance/gates | retain consequence-scaled escalation, no universal mandatory review |
| universal ontology/workflow engine/automatic relevance | K | explicitly rejected by method/GO | do not build |

## 13. Reassessment of the prior four-part / three-layer proposal

### Reconnaissance

**Retain, but reframe.** The important concept is not a new named stage for every Project. It is a conditional source-entry research mode when structure, relevance or legibility are insufficiently known for the current claim.

### S2↔S3↔S4 iteration

**Retain.** This is mostly METHOD explicitness, not a new research phase. Close diagnostic reading and palaeographic familiarisation may precede complete G2 representation.

### Provisional editorial intent

**Retain with corrected terminology.** A full early `edition concept` is too strong. The early requirement is revisable intent sufficient to state purpose, selection/completeness aspiration, intended use/audience and the required fidelity of source representation. S9/G6 finalises the actual edition concept/conventions.

### `inspection ≠ scope ≠ transcription`

**Retain and broaden.** Also keep Project root, inspection coverage, historical/completed scope and NEXT ACTION separate.

### Human-visible action claim

**Promote from optional presentation idea to central assistance requirement.** This is the main answer to the Human's black-box concern.

### #265/#267 state

**Retain as two distinct natural owners.** Scope and inspection coverage must not be merged merely because source entry uses both.

### #266/#269 fixtures

**Retain, but move explicitly downstream of a real source-entry pilot.** Their representation decision cannot be derived from abstract source-entry METHOD.

## 14. Existing Issue disposition

| Issue | New-system role | Disposition | Reason |
|---|---|---|---|
| #12 | catalogue/repository discovery-completeness evidence | **UNCHANGED / separate** | different level from source-internal reconnaissance |
| #263 | catalogue-bounded Source-set ownership | **KEEP / separate** | corpus-selection owner, not source-entry method |
| #265 | active scholarly scope semantics | **REFRAME** | original prose-sentinel bug is real but target must support empty + multiple/disjoint/evolving scope and must not model inspection breadth |
| #266 | documentary form/stage/condition representation | **KEEP / REFINE as downstream fixture-driven representation** | only decidable after direct Wolkenburg fixtures |
| #267 | granular inspection coverage/restartability | **REFINE / KEEP** | natural owner of source-internal coverage; remove any implication that whole-root inspection is scholarly scope |
| #268 | root File ↔ later internal Source evidence | **KEEP / downstream representation** | triggered after internal Source identity is actually established |
| #269 | evidence-bearing textual/transmission relation semantics | **KEEP / REFINE as downstream fixture-driven representation** | real copy/extract/correspondence fixture first |
| #270 | Wolkenburg integrated fixture/model hub | **REFRAME, not generic METHOD owner** | retain Human Owner input and fixture integration; generic source-entry capability gets a separate owner |
| #115 | empirical predecessor for source-driven semantic-loss / role/date/hand separation | **HISTORICAL FIXTURE / reuse** | do not reopen as current Wolkenburg owner |
| PR #286 | prior adversarial analysis provenance | **SUPERSEDE as planning surface, preserve history** | its findings are incorporated here; avoid parallel current plans |

## 15. Minimal coherent Issue architecture

The revised plan should **not** create a new Issue for every semantic dimension. Existing Issues already own most downstream state/representation gaps. Three new Issues are sufficient.

### NEW ISSUE A — generic outcome/method owner

**Title**  
`[METHOD / SOURCE ENTRY] Unknown manuscript → bounded, auditable scholarly research cycle`

**Type**  
analysis | method | planning

**Problem claim**  
The authoritative S1–S9 method is strong once source group, relevant structure and transcription target are sufficiently known, but it does not explicitly enough govern the adaptive source-entry condition where internal structure, relevance and handwriting are initially unknown. Without that clarification a fresh assistant may prematurely freeze scope, treat S3→S4 as linear, over-transcribe, or leave reconnaissance as an undefined generic token.

**Desired outcome**  
A generic, conditional, lean source-entry method that guides purpose/evidence preflight, reconnaissance, documentary-structure/relevance hypotheses, palaeographic familiarisation, pilot reading, scope formation and entry into bounded G2 work while preserving negative/unresolved outcomes.

**In scope**

- conditional trigger for source-entry mode;
- provisional editorial intent;
- reconnaissance depth tied to the claim attempted;
- S2–S4 iteration/pilot reading;
- distinction among Project root, inspection domain/coverage, scholarly scope and transcription scope;
- negative relevance outcome;
- simple-source fast path;
- A–J stress-test cases.

**Out of scope**

- physical schema/table design;
- universal document/hand ontology;
- Human UI implementation;
- copy/extract model implementation;
- automatic relevance classification;
- new gate sequence.

**Acceptance**

- a fresh researcher can explain the first source-entry actions for both a one-page clear charter and a 250-page composite unit without two separate methods;
- close/pilot reading may support familiarisation without being mislabeled G2 complete;
- broad inspection never automatically becomes scholarly scope;
- no relevant material is a representable, evidence-bounded outcome;
- the method identifies when #265/#267 state is needed rather than embedding its schema;
- real Wolkenburg and Reg. Ii fixtures are used for Generic-Fit;
- any normative METHOD change proceeds through D-016.

### NEW ISSUE B — Human scholarly assistance

**Title**  
`[ASSISTANCE] Human-visible scholarly action claim and competence/evidence routing for source work`

**Type**  
analysis | assistance | context

**Problem claim**  
Existing method, workflow and domain Requirements contain the required scholarly semantics, but a Human can still be shown opaque labels such as `S4`, `reconnaissance` or a generic cursor without seeing the question, governing competence, evidence test, claim ceiling and why the next action is discriminating.

**Desired outcome**  
For consequential source work, a Human-readable current-action explanation exposes:

`observation/uncertainty → question → domain/competence → evidence/test → claim ceiling → next discriminating action → specialist escalation trigger`.

**In scope**

- semantic contract for Human-facing scholarly action explanation;
- competence routing from source problem rather than Human discipline selection;
- claim ceiling and explicit non-result;
- specialist escalation visibility;
- compatibility with repository current-action/context work without making engineering views scholarly truth.

**Out of scope**

- universal claim graph;
- fixed UI;
- new AI role hierarchy;
- automatic specialist certification;
- duplicate canonical research state.

**Acceptance**

- a non-specialist Human can understand what is being tested and why without decoding stage codes;
- the explanation does not upgrade catalogue metadata, pilot readings or technical PASS into scholarly claims;
- the assistant identifies the governing discipline itself where derivable;
- `unresolved` includes the reason/evidence ceiling when consequential;
- a fresh context can derive/reference the explanation from canonical state/method rather than chat memory;
- later engineering/context implementation, if material, occurs only after the domain semantics are stable and admitted.

### NEW ISSUE C — real Wolkenburg empirical source-entry pilot

**Title**  
`[RESEARCH FIXTURE] Run one real Wolkenburg Archivale through the source-entry cycle`

**Type**  
research fixture | empirical validation

**Problem claim**  
The remaining method/state/representation questions cannot be responsibly closed from catalogue metadata or abstract modelling. A real 50–300-page archival unit must be worked from exact evidence far enough to demonstrate source-entry behavior, documentary boundaries, relevance, handwriting familiarisation and actual semantic-loss triggers.

**Desired outcome**  
Persist an evidence-controlled first source-entry pass on one Human-authorized Wolkenburg Archivale that records inspection coverage, candidate/excluded/unresolved relevance, provisional/confirmed documentary boundaries as warranted, consequential palaeographic anchors, pilot-vs-G2 distinctions and the exact observed triggers (or non-triggers) for #266/#268/#269.

**Authority prerequisite**

- the Human Owner selects or confirms which independent Archivale is the pilot/current scholarly target; do **not** infer it from easiest access, Nr. 632/754 availability or issue recency;
- exact evidence must be research-ready/vision-inspectable in the execution context.

**Acceptance**

- source work is from exact controlled evidence, not finding-aid text alone;
- ordered inspection coverage and gaps are restartable;
- candidate relevance is distinct from research scope and from exclusion;
- difficult handwriting is approached through exact internal anchors/pilot reading rather than semantic guessing;
- Source nodes are created only on existing evidence-driven criteria;
- #266/#269 receive at least the real fixtures their acceptance criteria require, or the pilot explicitly shows that the trigger has not yet occurred;
- #268 is tested only if a real internal Source is established against broader File evidence;
- no generic METHOD/schema change is smuggled in through the fixture.

## 16. Dependency / order graph

```text
SYSTEMIC REVIEW (this artifact)
        ↓
NEW ISSUE A — generic source-entry METHOD semantics
        ├──────────────→ NEW ISSUE B — Human scholarly-assistance semantics
        │                         ↓
        │                  later implementation owner only after semantics/admission
        │
        └──────────────→ NEW ISSUE C — real Wolkenburg source-entry pilot
                                  ↓
                       observed state / semantic-loss fixtures
                                  ↓
             ┌────────────────────┼────────────────────┐
             ↓                    ↓                    ↓
          #265/#267            #266/#269             #268
      scope + inspection     form/stage + relation   File/internal Source
             └────────────────────┼────────────────────┘
                                  ↓
                       precise D-016 package(s)
                                  ↓
                    bounded implementation + loss checks
                                  ↓
                         real-source Result Review
```

#263/#12 remain a parallel corpus-selection/completeness strand and are dependencies only when the claim concerns complete membership of the Wolkenburg 10.5.3 selection, not for the generic source-entry method itself.

## 17. D-016 map

| Work | Classification |
|---|---|
| this systemic analysis / Issue planning | analysis/planning; no D-016 implementation admission needed |
| real source inspection under existing authorized Project/method | routine bounded scholarship; no new D-016 merely for inspection |
| clarify wording/examples without changing METHOD semantics | routine documentation only if genuinely non-normative; otherwise treat as METHOD change |
| add authoritative conditional source-entry / provisional-intent semantics to `historical-source-workflow.md` | material shared METHOD change → D-016 before development/merge of normative change |
| add Human scholarly-action semantic requirement if it materially changes shared HITL/workflow behavior | material research-system/HITL change → D-016 before implementation |
| change active-scope representation | Project architecture/state semantics → D-016 |
| standardise canonical inspection-coverage owner | shared Project research-state semantics → D-016 |
| alter Source form/stage or relation contract | CORPUS contract semantics → D-016 |
| alter File↔Source evidence contract | CORPUS/Project evidence semantics → D-016 |
| create source-specific observations/readings during authorized fixture work | ordinary Project/CORPUS scholarship at natural owner; not D-016 unless a new shared semantic is introduced |

Do not force all later changes into one giant D-016 package. Group only changes whose semantics and loss checks are genuinely coupled. Source-entry METHOD, Human assistance, Project state and CORPUS relation/File representation have different natural owners and may require separate admissions even when one real fixture informs them all.

## 18. Repo-first persistence plan

1. Keep this artifact as the current **non-normative systemic analysis/plan** on a dedicated draft PR until reviewed.
2. Create exactly the three new Issues above; each owns only its stated problem/outcome and references this artifact rather than copying all analysis.
3. Add concise disposition comments to #265–#270 so a fresh context sees how each existing Issue maps into the new target model.
4. Keep #263/#12 separate and do not rewrite their corpus-selection semantics.
5. Mark PR #286 as superseded by this systemic review once this new artifact/Issue map exists; preserve it as analysis history rather than merging two competing current plans.
6. Do not edit normative METHOD from this planning action.
7. After Human review/admission, update the relevant canonical owner first (`historical-source-workflow.md`, Project state contract, CORPUS contract, etc.), then use Issues/analysis only as provenance.
8. A future context must be able to reconstruct the plan from repository + Issues without this chat.

## 19. Final test

Question:

> If a fresh chat tomorrow receives a wholly new 200-page early-modern archival unit, can it from repository + source, without old chat, competently determine what to do first, why, which expertise/evidence are needed, what may be claimed, what remains unknown, what has been inspected, what comes next and when specialist escalation is required?

**Answer: YES, WITH EXPLICIT REMAINING CONDITIONS.**

The existing repository already supplies most epistemic and disciplinary rules. The target source-entry method and Human-action semantics defined here are sufficient to make those rules operationally coherent. However, two implementation conditions remain before the answer becomes true in practice for long unfamiliar sources:

1. the source-entry METHOD/assistance semantics must be normatively admitted and propagated at their proper owners rather than remaining planning prose;
2. restartable inspection/scope state and downstream representation gaps must be resolved only to the extent demonstrated by real Wolkenburg/Reg.-Ii fixtures.

Qualified specialist validation remains consequence-triggered and cannot be replaced by AI or by repository consistency.

## 20. Deliberate non-solutions

Do not solve this problem with:

- a universal manuscript workflow engine;
- a mandatory S0 gate for every source;
- a universal document/genre/stage ontology;
- a universal hand/alphabet registry;
- automatic relevance classification;
- automatic copy/dependence inference;
- one giant `current_state` schema;
- forcing all 50–300 pages into diplomatic transcription;
- treating a Human-readable explanation as a second truth store;
- one monolithic D-016 package merely because the same Wolkenburg fixture exposed several natural-owner gaps.

The target is the **smallest fachlich complete, adaptive and restartable scholarly capability**, not the smallest text patch and not the largest architecture.