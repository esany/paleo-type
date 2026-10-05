# Adversarial review — source-entry reconnaissance, method explicitness and Human assistance

**Status:** NON-NORMATIVE ANALYSIS / REQUIREMENTS / CONCEPT REVIEW. This artifact does **not** change METHOD, CORPUS or Project truth, does not admit implementation under D-016, and does not create Wolkenburg Source/Project state.  
**Fresh repository baseline:** `main@37e59ee0871dacea87bbe9e3161a278e9a6bc1a6`.  
**Work owner / durable discussion surface:** #270.  
**Related live owners:** #265, #266, #267, #268, #269; #12/#263 where catalogue selection/completeness matters.  
**Review question:** Is the proposed small method patch — reconnaissance, explicit S2↔S3↔S4 iteration, provisional edition concept, and `inspection ≠ research scope ≠ transcription` — enough to solve the Wolkenburg problem and to make paleo-type a competent, transparent and trustworthy scholarly assistant for an unfamiliar manuscript?

## 1. Repository-first basis and prior-analysis lineage

This review starts from current repository authority rather than chat memory. Applicable owners inspected include:

- `GOVERNING_OBJECTIVE.md`;
- `AGENTS.md`;
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
- `requirements/domain-requirements.tsv`.

The existing generic method is already strong on:

- `research goal → research question → evidence needed → disciplinary method → claim type → permitted conclusion`;
- expertise routing before consequential specialist claims;
- `OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION` separation;
- non-waterfall S1–S9 iteration;
- scope-bound G1–G6 maturity claims;
- discovery, inspection, transcription and collation as distinct acts;
- unresolved evidence as a valid result;
- execution-context meanings for first/next bounded action, evidence requirement, access state and completion condition;
- the non-specialist Human Owner not being the default palaeographic/diplomatic/philological adjudicator.

The Wolkenburg analysis lineage already persisted in GitHub remains input/work metadata, not canonical manuscript truth:

1. #270 Block-1 synthesis: https://github.com/esany/paleo-type/issues/270#issuecomment-5984984817
2. #270 candidate physical/contract concept: https://github.com/esany/paleo-type/issues/270#issuecomment-5985020460
3. #270 correction after Human-Owner clarification: https://github.com/esany/paleo-type/issues/270#issuecomment-5985663441
4. #267 inspection-coverage refinement: https://github.com/esany/paleo-type/issues/267#issuecomment-5985666297
5. #266 form/granularity/stage/condition refinement: https://github.com/esany/paleo-type/issues/266#issuecomment-5985667584
6. #269 historical-event versus textual-transmission refinement: https://github.com/esany/paleo-type/issues/269#issuecomment-5985669179

The #270 correction supersedes the earlier idea that a complete-root relevance survey is itself the scholarly research scope. The controlling distinction is:

```text
Project root / documentary anchor
≠ discovery / inspection domain
≠ active scholarly research scope
≠ transcription scope
≠ inspection coverage
≠ NEXT ACTION
```

## 2. External scholarly comparison used in the adversarial check

Methodological comparators inspected for this review include:

- TEI P5 4.12.0, `<msPart>` / manuscript-part semantics: https://www.tei-c.org/Vault/P5/4.12.0/doc/tei-p5-doc/en/html/ref-msPart.html
- ICA Records in Contexts Conceptual Model 1.0: https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-conceptual-model/
- ICA RiC-O 1.1: https://www.ica.org/standards/RiC/RiC-O_1-1.html
- Association for Documentary Editing, Minimum Standards for Electronic Editions: https://documentaryediting.org/resources/about-documentary-editing/minimum-standards-for-electronic-editions/
- Association for Documentary Editing, excerpts from *Editing Historical Documents*: https://documentaryediting.org/resources/editing-education/excerpts-from-editing-historical-documents/
- Institut für Dokumentologie und Editorik, Criteria for Reviewing Scholarly Digital Editions 1.1: https://www.i-d-e.de/publikationen/weitereschriften/criteria-version-1-1/
- Cambridge, English Handwriting 1500–1700, course-design guidance: https://www.english.cam.ac.uk/ceres/ehoc/lessons/lessonhelp.html
- Folger, Practical Paleography: https://folgerpedia.folger.edu/Practical_Paleography

Methodological synthesis:

- manuscript/document boundaries and composite structure can require discovery and contextual judgement rather than being known in advance;
- selection, scope, purpose, audience and editorial method should be explicit in an edition project while remaining source-responsive;
- unfamiliar handwriting is learned iteratively through direct practice, secure/simple forms, recurring patterns, letterform comparison, abbreviations and close stroke-level inspection;
- transcription is not identical to edition, and selective editions must state their selection basis;
- no inspected comparator supports a rigid universal pre-transcription checklist, a fixed Source hierarchy, automatic Source segmentation or full-root diplomatic transcription before relevance is known.

## 3. Short verdict

**The four small changes are necessary but not sufficient as the complete solution.**

They repair a real **METHOD-EXPLICITNESS** problem: the authoritative workflow does not make the source-entry/reconnaissance situation explicit enough for a long, internally unknown archival unit, and S2→S3→S4 can still be read too linearly despite the existing non-waterfall rule.

But they do **not by themselves** produce the Human-facing scholarly tool requested. The repository already contains most competence/evidence semantics, but they are distributed across method, requirements and workflow. A fresh assistant could still say “do reconnaissance” or “iterate S2–S4” without visibly stating what is being tested, which discipline governs the test, what evidence is needed, what conclusion is currently permitted, what is explicitly *not* established, and why the next action is discriminating.

There is also an independent **DATA/STATE** gap: #267 shows that granular inspection coverage is not yet canonically/restartably represented, while #265/#270 require scholarly scope to remain distinct from the inspection domain. A prose method change cannot solve that persistence gap.

Finally, #266 and #269 remain **REAL-FIXTURE** questions. Method can govern evidence collection and explanation, but the smallest stable form/stage/relation representation still requires real Wolkenburg original-like and copy/extract cases.

## 4. Falsification of the four proposed changes

| Proposed change | Verdict | Reason |
|---|---|---|
| Explicit reconnaissance / source familiarisation | **PASS, but insufficient alone** | Scholarly sound and needed as a source-entry clarification. Much is implicit in S1/S2 and #267, but not explicit enough in METHOD. |
| Explicit S2↔S3↔S4 iteration | **PASS / mainly METHOD-EXPLICITNESS** | Current METHOD already rejects a rigid waterfall; unfamiliar-hand familiarisation before/while bounded transcription develops should be explicit. |
| Early provisional edition concept | **PARTIAL / REFINE** | Early purpose/scope/audience/selection thinking is warranted, but a full edition concept must not freeze an unknown source. Prefer a revisable **provisional editorial intent**; S9 finalizes conventions after the source basis is established. |
| `inspection ≠ research scope ≠ transcription` | **PASS / essential invariant** | Strongly supported by #270/#267 and scope-bound gates; it must be authoritative/operational enough that Human and restart state cannot confuse the three. |

**Alarm result:** implemented only as prose, the four changes would still fail the Human-assistance test. The system could remain scientifically correct in principle while operationally opaque.

## 5. The missing small scholarly-assistance property

Do **not** create a new ontology or workflow engine. The semantic pieces already exist. The smallest missing property is that, at source entry and consequential source-work transitions, the assistant compiles the existing method into a **Human-visible scholarly action claim**.

The action claim should make reconstructable, in ordinary scholarly language:

```text
CURRENT OBSERVATION / UNCERTAINTY
→ BOUNDED QUESTION
→ GOVERNING DOMAIN / COMPETENCE
→ EVIDENCE OR TEST NEEDED
→ CLAIM CEILING / WHAT THIS CANNOT ESTABLISH
→ NEXT DISCRIMINATING ACTION
→ SPECIALIST ESCALATION TRIGGER, if applicable
```

This is not a new canonical claim graph. It is a Human-facing execution projection of semantics already largely owned by:

- `historical-source-workflow.md` research-question control;
- the expertise-routing rule;
- `workflow.md` first/next bounded action + evidence required + completion condition;
- domain Requirements and specialist triggers;
- evidence-policy and claim-layer separation;
- quality-and-learning review questions.

Bad / black-box:

> “Now perform reconnaissance and S4 palaeographic analysis.”

Desired:

> “I am inspecting this page run for documentary boundaries, possible writing-characteristic changes and recurring letter/abbreviation forms. The immediate question is whether the candidate section is structurally distinct and sufficiently relevant to justify deeper reading. This is archival/diplomatic plus palaeographic work. A heading or visible writing change may generate a boundary hypothesis but does not yet establish a new Source. The next test compares starts/ends, layout, recurring forms and neighbouring material; if the evidence does not discriminate, the point remains unresolved or is escalated.”

## 6. Wolkenburg stress test — first 2–3 hours without invented source content

Assume one real archival unit from `20578 / 10 / 10.5 / 10.5.3`, roughly 50–300 pages, internal relevance unknown and handwriting initially difficult.

### Phase A — evidence and sequence preflight

- verify exact archival unit and exact visual evidence actually available;
- establish page/image order and missing/unavailable regions;
- do not infer internal Source identity from finding aid, filename, image sequence or topic;
- state the working question in Human-readable terms: which parts may be relevant, how is the unit internally structured, and what must be learned about the writing before reliable reading is possible?

### Phase B — broad reconnaissance in source order

Inspect enough of each available unit for the coverage claim being attempted. Retain provisional observations of:

- starts/ends, headings, layout shifts, tables/lists/register-like structures;
- candidate documentary boundaries;
- possible writing-characteristic changes without creating hand identities prematurely;
- obvious dates, names, place references or formulae only as leads at the evidential level actually visible;
- candidate relevant material;
- inspected-and-currently-not-relevant material;
- unreadable, missing, unavailable or unresolved material.

This phase is **not** full diplomatic transcription and does not make the entire root the active scholarly scope.

### Phase C — handwriting familiarisation / pilot reading

Choose clear or diagnostically useful loci from inspected material. Build local, exact comparison anchors for:

- recurring simple/secure word forms;
- discriminating letterforms in position;
- abbreviations/brevigraphs;
- numerals and special notation;
- recurring stroke combinations;
- possible writing-characteristic changes.

Use pilot transcription as an observation tool. Do not claim G2 merely because pilot rows exist. Revisit earlier uncertainty as internal evidence grows.

### Phase D — refine research boundary and next test

Legitimate first-pass outputs are provisional:

- likely documentary units/boundaries with evidence and uncertainty;
- candidate relevant Sources/loci versus inspected exclusions;
- what remains uninspected or unreadable;
- whether a narrower scholarly scope can now be proposed/confirmed;
- which palaeographic questions require another internal comparison pass;
- which documentary form/stage questions are now real enough to test.

### When #266 becomes genuinely testable

Only when direct inspection produces an actual internal object/witness where form, granularity, stage or condition would be semantically conflated by the current model. A catalogue label alone cannot establish the inspected stage.

### When #269 becomes genuinely testable

Only when an actual candidate related source/text or catalogue relation can be compared with direct inspection/collation. Same persons, place, date or ownership event do not establish textual dependence.

## 7. Competence and trustworthiness assessment

The competence framework is already broadly adequate. The gap is not missing discipline names; paleo-type already activates archival description/diplomatics, palaeography, historical philology, scholarly editing, source criticism and problem-triggered specialist domains.

For Human trust, competence must become visible in the action claim. The assistant should be able to say, for example:

- “This is primarily palaeographic; the relevant evidence is internal graphical comparison, not semantic plausibility.”
- “This is diplomatic/transmission-critical; the finding aid supports only a metadata-level claim until the witness/text relation is inspected.”
- “This is historical-legal interpretation; the reading may be secure while the legal role remains unresolved.”
- “This publication-consequential claim requires qualified specialist review; AI method compliance is not independent validation.”

The Human should not need to know in advance which auxiliary historical discipline to activate.

## 8. Gap classification

### METHOD-LÜCKE — small and bounded

- early edition work needs an explicitly revisable **provisional editorial intent** (purpose/selection/completeness aspiration/audience or use context at the level needed to guide source selection and representation) before S9 finalization;
- source-entry reconnaissance/familiarisation should be an explicit legitimate method condition when structure/relevance/legibility are unknown.

### METHOD-EXPLICITNESS

- S1/S2 already carry much of reconnaissance, but practical source-entry use is too implicit;
- S2↔S3↔S4 iteration already follows from the non-waterfall rule but should explicitly include unfamiliar-hand familiarisation and pilot transcription;
- inspection/scope/transcription separation is scattered across owners/Issues and should be visible in authoritative METHOD.

### EXECUTION / ASSISTANCE — central

- existing domain/evidence/claim semantics are not yet guaranteed to compile into a Human-readable scholarly action claim;
- a generic stage/cursor token is insufficient if the Human cannot see what is being tested, why, with what evidence and with what claim ceiling.

### DATA / STATE — already demonstrated

- #267: granular inspection coverage/restartability needs a truthful canonical owner;
- #265/#270: active scholarly scope must remain distinct from inspection domain and may be disjoint/evolving;
- method prose alone cannot preserve restartability of a 50–300-page survey.

### REAL-FIXTURE — still required

- #266 original-like plus copy/extract fixture;
- #269 copy/extract/textual-relation fixture plus Reg. Ii comparison;
- actual Wolkenburg source-boundary and hand/document observations.

## 9. Minimal coherent solution — not merely the smallest text patch

The smallest **complete** answer has three layers at their natural owners.

### Layer 1 — scholarly METHOD clarification

Without creating S0 or a universal stage system:

1. state a conditional reconnaissance/source-familiarisation rule in the authoritative historical-source workflow;
2. state explicitly that S2–S4 may iterate through structural observation, pilot transcription, handwriting familiarisation and renewed inspection before a selected locus reaches G2 representation completeness;
3. add/reframe an early **provisional editorial intent** that guides selection and representation but remains revisable; S9 finalizes the edition concept after research consolidation;
4. state the invariant `inspection domain/coverage ≠ active scholarly scope ≠ transcription scope`.

### Layer 2 — Human-facing scholarly assistance behavior

Require consequential source-entry/current-action explanation to expose:

`observation/uncertainty → question → domain → evidence test → claim ceiling → next discriminating action → escalation trigger`.

This should be derived/execution behavior, not a new canonical ontology or manually maintained parallel state.

### Layer 3 — restartable research state

Continue already-owned #265/#267 work so a fresh context can determine what was inspected, at what purpose/depth, what remained unresolved/unavailable, and which relevant Sources/loci form current scholarly scope. Do not encode this by overloading `active_scope`, crosswalks or transcription completeness.

Only all three layers together answer both the scholarly-method and Human-trust/restartability problem.

## 10. Explicit non-goals

- no universal diplomatics ontology;
- no fixed Source tree;
- no universal page tracker;
- no workflow engine;
- no permanent competence graph;
- no mandatory TEI authoring during research;
- no requirement to transcribe every inspected page;
- no automatic relevance classification;
- no HTR prerequisite;
- no automatic hand/scribe identification;
- no automatic copy/dependence decision;
- no requirement for the Human Owner to adjudicate specialist palaeography or diplomatics.

## 11. D-016 / authority boundary

This artifact is pre-admission analysis/requirements/concept work only.

Potential follow-up classification:

- explanatory/non-normative source-entry guidance that only restates already-owned semantics may be routine clarification if it changes no requirement;
- a new normative shared requirement that source-entry reconnaissance must occur under specified conditions, or that provisional editorial intent is required, is a **shared METHOD change** and requires the D-016 path before implementation;
- a normative cross-project Human-facing scholarly-action contract in shared workflow/tooling is **D-016-sensitive** unless demonstrated to be a pure derivation of existing admitted/current semantics;
- #265/#267 shared Project/research-state representation is already recognized as material/D-016-sensitive;
- #266/#269 shared CORPUS-contract changes are material and fixture-dependent under D-016.

No admission is created here.

## 12. Final answer to the Human-assistance question

**NEIN — not from the four textual method changes alone.**

They would make the method clearer and safer, but the Human could still work against a black box if the assistant does not expose domain, evidence test, claim ceiling and discriminating next action, and if survey state cannot be restarted from repository state.

The smallest coherent target is therefore:

> **explicit source reconnaissance + iterative handwriting familiarisation + revisable early editorial intent + Human-visible scholarly action claims + restartable inspection/scope state.**

With that package the answer becomes **JA, ABER**: paleo-type can guide a non-specialist owner in the manner of a strong historical/editorial research assistant while preserving uncertainty and specialist escalation, but real Wolkenburg fixtures and consequence-scaled qualified review remain necessary for claims the evidence/method alone cannot settle.

## 13. Next authorized analysis step

No METHOD or contract change should be implemented from this review alone.

Next: reduce Layer 1/Layer 2 to the smallest precise requirements/concept delta **and** test the scholarly-action-claim behavior against one real Wolkenburg archival unit. In parallel, #266/#269 remain source-fixture work rather than schema-design work.
