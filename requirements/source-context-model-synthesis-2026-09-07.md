# Source/context model synthesis — evidence, processing-state causes, standards alignment and generic concept

Status: **cross-project analysis / concept synthesis; no material model implementation is authorized by this document alone**.

Date: 2026-09-07

Baseline reviewed: `main` at `19e57e28a80dc3850beb206859968bc25c575e77` (merged PR #112).

Primary synthesis controller: GitHub Issue #25.

Standards evidence ledger: `requirements/source-context-standards-evidence-2026-09-07.tsv`.

Source-context evidence owners: `corpus/source-context-digiref-audit.md` and `corpus/source-context-digiref-evidence.tsv`.

This document consolidates the analyses, source-critical research, repository-state review, conceptual corrections and generic learnings that emerged from the Reg. Ii 3 / Reg. Ii 4 Bd. II / Reg. Ii 5 work through 2026-09-07. It is intentionally a **synthesis and decision-support artifact**, not a replacement truth store. Canonical Source/File/relationship facts remain in `corpus/`; Project purpose/state remains in `projects/<id>/project.yml` and `STATUS.md`; diplomatic readings remain in their owning transcription files; accepted cross-project architecture/method decisions remain in `DECISIONS.md` only after the normal admission/review path.

## 1. Why this synthesis was necessary

Several individually reasonable repair steps exposed a larger pattern:

1. Earlier repository structures sometimes treated a bounded DigiRef/provider record as if it represented the entire archival file/signature.
2. The later source-recovery work correctly separated Reg. Ii 4 and Reg. Ii 5 as distinct witnesses, but the protective quarantine of the legacy Reg. Ii 5/Knau path became too coarse for some later direct-image G2 artifacts.
3. The Reg. Ii 4 Knau workflow reached a much higher scholarly maturity than Reg. Ii 3 or the current Reg. Ii 5 state, for legitimate reasons that must not be flattened into a single generic `status` idea.
4. Personnel metadata remained a flat list even after the source-context audit demonstrated that visitator membership, sovereign/commissioning authority and possible scribal participation are different claims.
5. Dating work showed that archival-unit dating, event-cycle dating, local visit date and later copying/excerpting date must not be inherited across levels.
6. Current Project state contains small drift signals: a bounded Reg. Ii 4 `active_scope` still describes work that `STATUS.md` now records as complete; actual historical Source-use is underrepresented because the earlier system correctly rejected role→priority inference but overcorrected by leaving real research functions unrecorded.
7. The repository already has 130 domain requirements and a strong METHOD/CORPUS/PROJECT ownership architecture. The task is therefore not to invent a new ontology, but to reconcile the current evidence with those requirements and select the smallest generic corrections.

The resulting design question is not "How do we model visitation records?" but:

> **What is the smallest generic research model that remains valid across different manuscript and documentary source structures, while preserving archival provenance, direct observation, witness independence, editorial layers, contextual roles, uncertainty and research-state history?**

## 2. Evidence classes used in this synthesis

The source-critical context audit already distinguishes:

- `DIRECT-CATALOGUE` — official archival finding-aid statement;
- `DIRECT-DIGIREF` — DigiRef/provider metadata or project/index statement;
- `DIRECT-IMAGE` — conclusion from directly inspected manuscript images;
- `SECONDARY` — modern scholarship;
- `INFERENCE` — bounded inference from direct observations;
- `OPEN` — insufficient evidence for assertion.

For repository-state analysis this synthesis adds a separate descriptive layer:

- `REPO-CANONICAL` — current canonical repository state;
- `REPO-HISTORY` — Git/Issue/PR history explaining how that state arose;
- `MODEL-GAP` — demonstrated mismatch between current representation and the information the research actually needs;
- `CONCEPT-CANDIDATE` — proposed generic response, not yet admitted implementation.

This separation is important: a GitHub issue can prove that a workflow step happened, but it cannot establish what a manuscript says; an archive catalogue can identify and date an archival unit, but it cannot by itself establish the exact day represented by a bounded source group; a direct image can establish a visible cancellation, but not automatically the historical role of a named person.

## 3. Current archival/source hierarchy after PR #111 and #112

The current safe hierarchy is:

```text
archival unit / signature
  → bounded documentary/source group
    → research locus
      → source-order / diplomatic units as required by the source
```

Examples in the current corpus:

- `ACT-THHSTAW-EGA-REG-II-3` — archival unit `ThHStAW, EGA, Reg. Ii 3`;
  - `THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V` — bounded source group *Visitation in Neustadt an der Orla*, fol. 41r–63v;
  - `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — bounded source group *Pfarreinkommen Gössitz, Knau ...*, fol. 303r–306r.
- `ACT-THHSTAW-EGA-REG-II-4-BD-II` — archival unit `ThHStAW, EGA, Reg. Ii 4 Bd. II`;
  - `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — bounded source group *Visitation im Amt Ziegenrück*, fol. 294r–313r;
    - current completed Knau research locus fol. 306v–309r.
- `ACT-THHSTAW-EGA-REG-II-5` — archival unit `ThHStAW, EGA, Reg. Ii 5`;
  - `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — bounded source group *Visitation im Amt Ziegenrück*, fol. 55v–66v;
    - comparison/G2 Knau locus fol. 61v–63r.

The archival unit, bounded source group and research locus are different objects/levels. A DigiRef search hit can additionally be only an **entry point** into a larger place block; DigiRef itself distinguishes Akten and Visitationsprotokolle and explains that search hits often lead to the first page where a place occurs. Therefore portal navigation is not a sufficient documentary-boundary rule.

### Generic consequence

Do not make `source_group` a universal archival ontology class. It is a useful local type for the current corpus. The generic requirement is only that:

- stable documentary identity exists at the granularity justified by archival evidence and research need;
- structural membership/grouping is explicit and evidence-bearing;
- no lower-level title, date, extent or agent list is silently promoted to a higher level;
- no filesystem/project hierarchy is treated as archival hierarchy by inference.

## 4. Source-critical chronology and transmission findings

### 4.1 Earlier Neustadt/Ziegenrück context

Direct finding-aid evidence establishes a separate 1527 visitation file for Weida, Neustadt, Saalfeld and Pößneck. Reg. Ii 3 is a 525-leaf archival unit dated 1529 and contains separate Neustadt, Ziegenrück-income, Knau-income and *Recesse der Visitatoren 1529* groups.

The bounded Reg. Ii 3 Neustadt group has its own DigiRef visitation period, 23.5.–1.6.1529. The bounded Knau income group does **not** currently have a separate exact local date in the inspected DigiRef evidence. It can therefore be situated securely inside the 1529 archival-unit context without manufacturing the Neustadt group’s exact interval as its own.

### 4.2 Later Reg. Ii 4/5 context

The official finding aid identifies:

- Reg. Ii 4 Bd. II: *Visitation in Thüringen*, dated `1533 [1534–1536]`, 418 leaves, containing *Visitation im Amt Ziegenrück* at fol. 294r–313r;
- Reg. Ii 5: *Registratur für die Superintendentur Neustadt (Orla) (Auszug)*, dated `[1533–1536]`, 94 leaves, containing a serial sequence of Neustadt/Arnshaugk/Leuchtenburg-Ziegenrück/Ziegenrück/Ranis/Roda-Jüdewein material and later ordering/report material.

Separate official 1533 records connect the Thüringen visitation administration with Neustadt sequencing and Ziegenrück matters. The formerly normalized exact date `1533-03-03` for the Ziegenrück source groups was not supported by direct local evidence and has correctly been removed. The current supported statement is:

> Ziegenrück belongs to the later Thüringen visitation cycle with direct 1533 administrative evidence; the exact local visit day represented by the Reg. Ii 4/5 Ziegenrück source groups remains open.

### 4.3 Reg. Ii 4 ↔ Reg. Ii 5 transmission relation

The official title of Reg. Ii 5 already identifies the archival unit as an `Auszug`. Catalogue/provider metadata links the Reg. Ii 5 Ziegenrück group to corresponding Reg. Ii 4 material. The stronger direct-image result comes from completed #99:

- substantial shared Knau opening/account and decree sequence;
- demonstrable omissions/condensation in Reg. Ii 5;
- resegmentation across different physical lines/folios;
- no line-for-line identity;
- no same-hand conclusion;
- no Reg. Ii 4 diplomatic correction justified from the comparison witness.

The safe relation is therefore selective/condensed textual correspondence with omissions and resegmentation. The exact copying/redaction process, chronological direction at the working-document level, responsible hands and exact excerpt-production date remain open.

### Generic consequence

`part_of`, `extract`, `copy`, `textually_corresponds_to`, `same_event_context`, `derived_from`, etc. must remain **evidence-bearing relations**, not shortcuts that collapse identity or automatically transfer text, date, hand or personnel claims.

## 5. Current processing states and why they differ

The projects are not at different states because one is simply "better processed" than another. Their states reflect different research histories, evidence availability and owner-selected questions.

| Project/source area | Current scholarly state | Main cause |
|---|---|---|
| Reg. Ii 4 Bd. II / Knau 306v–309r | complete bounded first reading; G2 PASS; systematic internal adjudication complete; controlled Reg. Ii 5 collation complete | explicit owner selection as source-exact target; exact File/crosswalk; deliberately staged witness-independent workflow #96–#99 |
| Reg. Ii 3 | archival identity/context and File provenance established; one crosswalk partial/one absent; no current manuscript NEXT ACTION | currently no owner-selected source-research question; earlier material served context/control and intake/restartability work rather than full transcription |
| Reg. Ii 5 / current canonical witness state | strong Source/File/crosswalk provenance; direct-image G2 physical inventory exists for 61v–63r; no current canonical diplomatic transcription declared | legacy path was originally an AI-organized Knau benchmark and later shown to contain witness-attribution risk; current policy requires fresh witness-specific promotion |
| corpus source context | strong for current Reg. Ii 3/4/5 chronology and hierarchy | dedicated DigiRef/finding-aid audit in PR #112 after the source-group/whole-unit distinction was clarified |
| people/roles | incomplete/semantically flattened | `persons` fields predate the role-resolved evidence model and currently mix identity/association with role implications |

### 5.1 Reg. Ii 4: a completed bounded research workflow

`STATUS.md` records all 117 relevant visible Knau units, G2 completeness PASS, #98 internal adjudication complete, release gate PASS and #99 controlled external collation complete. This is the strongest current example of the intended research sequence:

```text
exact source/file/locus
→ independent witness reading
→ completeness audit
→ internal evidence/adjudication
→ controlled external comparison
→ explicit unresolved specialist limits
```

The bounded workflow is complete. The current `project.yml:active_scope` still describes the 2026-09-03 Knau target as active, which is now stale relative to `STATUS.md`. This is a state-reconciliation problem, not a research-content failure.

`source-uses.tsv` is also empty. Earlier methodology correctly prevented a Source from acquiring a permanent role merely because it was structurally internal or currently active. But the completed historical work now demonstrates real project-relative functions: the Reg. Ii 4 Ziegenrück/Knau source was the principal direct-reading target and the Reg. Ii 5 Ziegenrück/Knau source was used as a controlled comparison witness. Persisting those actual uses would not imply current priority if the model keeps `research_function` separate from `NEXT ACTION`.

### 5.2 Reg. Ii 3: intentionally partial, not deficient

The project contains two known internal source groups and exact File evidence, but no current source-research task. `source-uses.tsv` is empty and `STATUS.md` explicitly forbids inferring priority from Project creation, Source order or preserved Knau work.

This is a legitimate state. A dormant or context-only source can have high archival/provenance maturity without any reason to become fully transcribed. "Not active" and "not researched" are different propositions.

### 5.3 Reg. Ii 5: two evidential generations inside one legacy path

The legacy `projects/ega-reg-ii-5-knau/` directory contains at least two epistemically different generations:

**Generation A — legacy diplomatic/apparatus/palaeographic material**

- historical `transcription/132.tsv`–`135.tsv` and associated decisions/hypotheses;
- path/page labels are insufficient to guarantee line-by-line witness attribution after direct Reg. Ii 4/5 comparison exposed possible mixture or cross-witness contamination;
- safe use: checking/recovery/methodology fixture until a concrete reading receives fresh Source/File/locus attribution.

**Generation B — later direct Reg. Ii 5 source-inspection artifacts**

- `research/g2-baseline-provenance.md` binds exact Reg. Ii 5 File identity, SHA, folio↔image↔PDF correspondence and reproducible baseline renders;
- `research/g2-checkpoint-a-physical-inventory.md` records direct visual inspection of Reg. Ii 5 fol. 61v–63r and source-order/layout phenomena, including confirmed cancellations at 61v-L16 and 62r-L18;
- these artifacts are themselves witness-specific direct Reg. Ii 5 evidence at the level they actually claim, even though they live in the historically problematic path.

The current wildcard row `research/g2-*` in `legacy-witness-provenance.tsv` therefore overclassifies some later direct-image artifacts as if all G2 records inherited unresolved witness provenance. The general correction is not to trust the directory; it is to follow **claim-level evidence provenance**.

## 6. Processing-state learning: maturity must be multidimensional

A single scalar project/source status cannot adequately represent the observed states. The minimum conceptual dimensions evidenced by the real projects are:

1. **identity/provenance maturity** — Source/File/locus/crosswalk known and recoverable;
2. **direct inspection / representation maturity** — what material has actually been visually inspected and diplomatically represented;
3. **internal adjudication maturity** — difficult readings/phenomena tested against admissible same-witness/internal evidence;
4. **comparison/collation maturity** — external witnesses compared after witness independence is secured;
5. **validation maturity** — AI-assisted method review versus qualified independent specialist validation where required;
6. **current activity/priority** — whether the owner has currently activated a research question;
7. **historical use** — what role a Source actually played in completed research, independent of present activity.

These are not proposed as one mandatory new universal table or closed enum. They are **information dimensions** that the current evidence proves must not be collapsed. Existing Project `STATUS`, source-use and evidence structures may be sufficient after targeted reconciliation.

### Generic consequence

Canonical does not mean certain; complete does not mean all questions resolved; inactive does not mean immature; context does not mean secondary in archival importance; historical use does not imply current priority.

## 7. Persons, agents and roles: demonstrated modelling gap

Current `corpus/sources.tsv` person lists for the two later Ziegenrück source groups predate the source-context audit and list names without role semantics. The later event audit directly documents the appointed 1533 Thüringen visitators as:

- Justus Menius;
- Friedrich Myconius;
- Georg von Wangenheim;
- Georg von Denstedt;
- Johann Kothe (Cotta), mayor of Eisenach.

Johann Friedrich I appears in related administrative records as sovereign/commissioning/issuing/corresponding authority. He is not simply another member of the visitor commission.

This demonstrates that the following concepts must remain distinct:

```text
Person/Agent identity
≠ mentioned in a record
≠ participates in an event
≠ institutional/administrative role
≠ creator/author
≠ scribe/hand
≠ commissioner/sovereign
≠ subject of the recorded matter
```

A person can occupy different roles in different events/records. A named visitator is not automatically the scribe of a surviving manuscript page. A shared office or event context does not establish same hand. Hand identification is a separate palaeographic hypothesis with its own evidence.

### Generic concept candidate

Represent role as a contextual, evidence-bearing relation rather than a permanent Person property, conceptually:

```text
Agent --[role + context + evidence + status]--> Event / Source / production activity / claim
```

The role vocabulary should be open or only lightly controlled until recurring needs justify stronger normalization. Source-type-specific roles such as `Visitator` belong in the data, not in the generic architecture.

## 8. Dating: demonstrated modelling gap

The 1529/1533 work proves that several date classes must remain separable when the evidence distinguishes them:

- archival-unit/finding-aid dating;
- bounded source-group/document date;
- event/visit/circuit date;
- date mentioned within the document;
- production/copy/excerpt/redaction date;
- later registration/filing date;
- modern export/file timestamp or filename date.

The formerly used `1533-03-03` illustrates the failure mode: an exact-looking normalized date can be structurally valid while historically unsupported for the target source group.

### Generic concept candidate

Do not create one universal `date` field that silently absorbs all temporal claims. Preserve date **target/context**, precision/uncertainty and evidence basis. Exact dates may remain absent where only a broader archival/event-cycle interval is supported.

## 9. Source, File, Instantiation and research evidence

The current Source/File distinction is one of the strongest parts of the repository:

- Source = stable historical/documentary identity at justified granularity;
- File = exact inspected digital research instance, with checksum/coverage/storage/rights provenance;
- crosswalk = evidenced mapping among archival folio/locus, provider image/export identifier and PDF page;
- Project use = project-relative research function, not Source identity;
- direct observation/reading = claim made from a specific Source/File/locus evidence path.

This is domain-valid and strongly aligned with Records in Contexts, but not identical to a formal RiC implementation. In particular, `File` is a pragmatic local research-data concept; it should not be globally asserted as exactly equal to `rico:Instantiation` without an explicit mapping analysis. RiC instantiation semantics are broader than one checksum-controlled PDF export.

## 10. Diplomatic/editorial layer separation

The G2 work and existing domain requirements confirm that the following must remain separable where they occur:

```text
visible/written source form or sign
→ diplomatic reading
→ source phenomenon (e.g. cancellation, addition, damage)
→ editorial expansion/supply
→ normalization/regularization
→ lexical/historical identification
→ interpretation
```

The Reg. Ii 5 G2 physical inventory directly demonstrates why: a cancelled word can coexist on the same physical line with a surviving current reading; abbreviation marks can be visible while expansion remains undecided; numeral/accounting signs can be visibly present while their function/value remains unresolved.

TEI P5 and the DFG edition criteria strongly support these distinctions. The repository should remain free to use a lean internal TSV/Markdown/YAML representation if it preserves the necessary semantics and can later be mapped/exported. TEI should not become an authoring platform merely to claim standards compliance.

## 11. Addressing granularity must be source-driven

Reg. Ii 5 #64 and Reg. Ii 4 #96–#99 demonstrate physical line/source-order relevance for the current Knau material. They do **not** prove that every future Source must use `folio → line → span` as a universal hierarchy.

The generic requirement is:

> Every consequential claim must target an unambiguous recoverable source locus at the smallest granularity needed by that source and claim.

Possible source-specific addressing may be:

- folio → physical line → line-local span;
- page → paragraph → span;
- accounting entry → sign/amount field;
- charter → protocol/text/eschatocol → clause;
- table → row/cell;
- codex → surface/region/marginal zone;
- letter → page/line/paragraph;
- other evidence-specific structures.

The generic core should carry typed/recoverable locus references without imposing one source-form ontology.

## 12. Domain and standards validation

The concept has been rechecked against the repository’s existing domain requirements and current authoritative external references. The detailed reference ledger is `requirements/source-context-standards-evidence-2026-09-07.tsv`.

### 12.1 Archival science / diplomatics — RiC

Strong semantic alignment:

- stable record/resource identity separate from contextual entities;
- record resources, agents and activities are distinguishable;
- multiple contextual relations are first-class rather than compressed into one hierarchical description;
- instantiation/representation can be distinct from the archival/intellectual record resource;
- record/resource grouping can be flexible and contextual rather than one universal tree.

This supports our Source/context/relation approach and the correction from `whole act == DigiRef protocol record` to a layered archival-unit/source-group model.

**Boundary:** paleo-type does not claim formal RiC-CM/RiC-O conformance. A future RiC export would require an explicit mapping with loss/ambiguity notes.

### 12.2 Scholarly editing / manuscript representation — TEI P5 and DFG edition criteria

Strong semantic alignment:

- historical document/source representation distinct from abstracted text;
- Befund distinct from Deutung;
- addition/deletion/source phenomena distinct from surviving/edited text;
- abbreviation distinct from expansion;
- original/source form distinct from regularization;
- responsibility/source/certainty traceable;
- facsimile/surface/zone/line mechanisms available where spatial/physical addressing matters.

**Boundary:** the project is not currently TEI-XML conformant and should not claim it. TEI is a standards-aligned interoperability/export target unless a separate real use case justifies migration.

### 12.3 Good Research Practice — DFG

Strong alignment:

- research-relevant data, evidence, methods, uncertainty and decisions remain reconstructable;
- negative/unresolved results are legitimate and must not disappear;
- responsibility and validation level remain distinguishable;
- research results must be reviewable without reliance on transient chat state.

### 12.4 IIIF and W3C PROV

Both are useful interoperability references, not internal-architecture requirements:

- IIIF can support standardized image/canvas/range/annotation addressing and presentation if provider or publication integration requires it;
- W3C PROV can express Entity–Activity–Agent provenance for exchange if cross-system provenance interoperability becomes real.

Neither justifies a database/RDF/IIIF-native internal rewrite at current scale.

## 13. Fit to existing `REQ-*` requirements

No new requirement family is currently demonstrated. The synthesis mainly **refines operational consequences of existing requirements**, especially:

- `REQ-ARCH-001` — stable Source identity independent of project role/title shorthand/File;
- `REQ-ARCH-002` — provenance/context distinct from record and interpretation;
- `REQ-ARCH-003` — exact inspected instantiation distinct from archival/intellectual record;
- `REQ-ARCH-004` — folio/image/PDF/working locators remain separate mappings;
- `REQ-ARCH-005` — catalogue assertion, inference and direct inspection distinguishable;
- `REQ-ARCH-006` — Source relationships are evidence-bearing claims;
- `REQ-ARCH-007` — research function is project-relative;
- `REQ-ARCH-008` — completeness/absence claims require bounded search evidence;
- `REQ-ARCH-009` — consequential loci need unambiguous canonical addressing;
- `REQ-ARCH-010` — documentary form and record stage/status distinct where consequential;
- `REQ-PAL-003` — same context/record versus same hand;
- `REQ-PAL-005` — written sign/abbreviation/expansion/normalization/identification separation;
- `REQ-PAL-007` — alternatives/rejected readings/residual uncertainty survive;
- `REQ-PAL-008/009` — exact visual provenance and evidence-class separation;
- relevant `REQ-EDIT-*` requirements on independent witness representation, source order, intervention layering and explicit correspondence;
- relevant `REQ-GWP-*` requirements on canonical ownership, recoverability, provenance, revisions, responsibility and restartability;
- relevant `REQ-RSE-*` requirements on lean canonical structures, deterministic validation only for settled semantics, loss-checked migration and derived views;
- relevant `REQ-AI-*` requirements on evidence/AI/validation distinction and controlled canonical writes.

The current failure is therefore mostly **uneven implementation and stale state**, not missing domain theory.

## 14. Generic core proposed by this synthesis

The smallest reusable core should remain source-type neutral. Conceptually it needs only the following distinctions, not necessarily new tables for each:

### A. Documentary identity and structure

- stable Source/documentary object identity;
- explicit evidence-bearing membership/relationship to other documentary objects;
- source-type-specific structure only where the real material requires it.

### B. Digital evidence instance

- exact inspected File/representation identity where consequential;
- provenance/coverage/rights/storage/access;
- crosswalk from archival/documentary address to digital representation.

### C. Recoverable target/locus

- typed/source-appropriate target address;
- physical/spatial granularity only where needed;
- deterministic referential validation after the target has been scholarly established.

### D. Epistemic layers

- observation/source phenomenon;
- diplomatic reading;
- editorial intervention/expansion/supply;
- normalization/identification;
- interpretation/claim;
- evidence and uncertainty kept with the relevant layer.

### E. Contextual entities and roles

- Agent/person/institution identity separate from role;
- Event/activity/context separate from the Source itself;
- evidence-bearing role relation with status/limitations;
- hand/scribe hypothesis separate from named historical person unless independently established.

### F. Temporal context

- date attaches to a clearly identified target/context;
- precision/range/uncertainty and evidence basis retained;
- no inheritance from parent unit/event/file name without evidence.

### G. Research use and maturity

- project-relative Source use/history separate from current owner-selected priority;
- source/gate maturity represented by the relevant canonical evidence/state owners rather than one overloaded status;
- completed work remains valid history after the project moves on.

## 15. What must remain source/project specific

Do **not** genericize from the pilot:

- `Visitator`, `Pfarreinkommen`, `Kirchspiel`, `Knau`, `Ziegenrück`;
- the Reg. Ii signature hierarchy itself;
- 1529/1533 terminology;
- the 61v accounting-list structure;
- a mandatory `folio → line → span` hierarchy;
- fixed source-type roles;
- a universal hand registry;
- a universal numeral/metrology ontology;
- the current G1–G6 workflow as an archival description standard;
- project `principal/control/comparison/context` labels as intrinsic Source properties.

A generic architecture passes only if it remains sensible for a letter series, account book, charter, chronicle, copy book, mixed codex or other manuscript/documentary source without changing the generic epistemic core.

## 16. Demonstrated current inconsistencies / reconciliation queue

These are findings, not implementation authorization.

| Finding | Evidence | Risk | Smallest candidate response |
|---|---|---|---|
| Reg. Ii 4 `active_scope` still states the Knau task as active after #99 completion | `project.yml` vs `STATUS.md` | stale current-scope truth | reconcile Project scope/current-next-action semantics; preserve completed Knau history |
| Reg. Ii 4 `source-uses.tsv` empty despite completed principal-reading + controlled Reg. Ii 5 comparison use | #96–#99 and STATUS | research-use history disappears; earlier anti-inference protection overcorrects | persist actual historical research functions without using them to infer current priority |
| Reg. Ii 5 legacy provenance wildcard covers all `research/g2-*` | `legacy-witness-provenance.tsv` vs direct Reg. Ii 5 G2 baseline/inventory provenance | direct Reg. Ii 5 observations are wrongly downgraded by path | classify evidence at artifact/claim level; distinguish legacy mixed readings from later exact-source G2 observations |
| flat `sources.tsv:persons` versus role-resolved 1533 event evidence | source metadata vs `events.tsv`/CTX-E014 | sovereign, visitator and other associations can be conflated | role relations/context model; retain person identity separately |
| exact date inheritance previously produced `1533-03-03` | PR #112 audit | false precision | require date target/context + evidence; no automatic inheritance |
| Issue #100 remains open although its #96–#99 dependency chain is complete | #100 + current STATUS | planning surface can look like active research truth | close/supersede roadmap after owner/roadmap decision; GitHub remains planning, not research truth |
| Reg. Ii 3 processing state may look "behind" despite no active question | Reg. Ii 3 STATUS | activity can be mistaken for maturity requirement | preserve explicit no-current-task state; do not manufacture work merely for symmetry |

## 17. Learnings from the failure/recovery sequence

### L1 — Evidence provenance must be claim-level, not path-level

A directory can contain artifacts from different evidential generations. Filesystem history is useful audit context but cannot determine manuscript witness authority.

### L2 — Protective quarantine must be narrow

When provenance is uncertain, quarantine the affected claims/artifacts, not everything in the surrounding directory. Overbroad quarantine can erase later direct evidence as effectively as overconfident promotion can create false evidence.

### L3 — Research function and research priority are orthogonal

A Source can historically have served as principal/comparison/context without thereby remaining the next target. Preserve actual use; derive current activity only from the Project’s current owner-selected state.

### L4 — Processing asymmetry can be scientifically correct

Different Sources should not be forced to identical transcription/gate depth. Work follows a research question, not an aesthetic desire for uniform completion.

### L5 — Exact-looking metadata is especially dangerous

A precise date, role or locator can be more misleading than an explicit blank. Precision must be evidence-earned.

### L6 — Direct source observation outranks contextual plausibility for diplomatic claims

The completed Reg. Ii 4/5 collation confirms the repository’s central rule: a clearer parallel witness may generate a candidate, but it cannot overwrite a target witness without direct target evidence.

### L7 — Same event/source context is not same hand

Administrative association and textual similarity are not palaeographic proof. Hand identity remains a separately evidenced hypothesis.

### L8 — Generic architecture should encode distinctions, not source vocabulary

The transferable value lies in Source/File/locus/evidence/role/date/layer distinctions. `Visitator`, `Pfarreinkommen` and the Reg. Ii hierarchy are data/profile semantics.

### L9 — Standards should validate concepts at the boundary, not dictate premature internal technology

RiC, TEI, DFG GWP, IIIF and PROV provide strong semantic/interoperability reference points. The project should remain standards-aligned internally and claim formal conformance only for an explicitly mapped/validated export or profile.

### L10 — Deterministic validation should protect settled structure, not decide scholarship

Good candidates for code: ID/reference integrity, exact File hashes, part-of acyclicity, required evidence links, derived-view rebuildability, canonical/derived separation. Bad candidates: correct grapheme, correct historical identification, same hand, copying direction, sufficient evidence for a historical interpretation.

## 18. Standards-alignment vocabulary to use in future reviews

Use three distinct claims:

1. **domain-valid** — the conceptual distinction is supported by archival/diplomatic/editorial/GWP method;
2. **standards-aligned / mappable** — the local model can be mapped to a relevant standard without obvious semantic contradiction;
3. **formally conformant** — a concrete representation/export/profile has actually been implemented and validated against the relevant formal standard.

Do not use (3) when only (1) or (2) has been demonstrated.

## 19. Recommended implementation packages after explicit owner admission

The analysis supports a **targeted reconciliation**, not a platform refactor.

### Package A — current-state and provenance reconciliation

- reconcile Reg. Ii 4 `active_scope` with completed #99 state;
- persist actual completed project-relative Source uses without deriving priority from them;
- refine Reg. Ii 5 legacy provenance so later direct-image G2 artifacts retain their demonstrated witness-specific authority;
- clean/supersede stale GitHub planning surfaces only where current canonical state makes them obsolete.

### Package B — person/role/date semantics

- define the smallest contextual role representation needed by the real 1533 personnel case;
- separate person identity from role/event/source participation and from hand/scribe hypotheses;
- define how date target/context/evidence is represented where more than one temporal layer matters;
- migrate only demonstrated current cases; do not build a universal historical-agent ontology.

### Package C — targeted generic safeguards

- add/strengthen deterministic validation only for settled invariants exposed by A/B;
- retain open role/date vocabularies unless repeated cases justify controlled values;
- add a standards crosswalk/export test only when an actual interoperability deliverable is requested;
- do not introduce RDF, TEI authoring, IIIF infrastructure, workflow engine or database absent a separate real trigger.

## 20. Explicit non-changes

This synthesis does **not** authorize or imply:

- reopening #96/#97/#98/#99;
- changing any Reg. Ii 4 diplomatic reading;
- promoting legacy Reg. Ii 5 transcription rows into current canonical witness truth;
- asserting Reg. Ii 5 direct copying from Reg. Ii 4 in one demonstrated operation;
- asserting same hand across witnesses;
- assigning an exact Ziegenrück visit day;
- deciding the exact creator/scribe of Reg. Ii 4 or Reg. Ii 5;
- creating a corpus-wide person-role ontology;
- creating a universal Line/Span/Phenomenon ontology;
- migrating the corpus to RiC/RDF, TEI/XML, IIIF or W3C PROV;
- treating CI/validator success as scholarly or specialist validation.

## 21. Falsification / generic-fit tests for any implementation

Before promoting the concept to shared architecture, test that the proposed representation still works without semantic distortion for at least these source shapes:

1. a single letter with author/addressee/mentioned persons and uncertain date;
2. a multi-entry account book with values, units and recurring scribal hands;
3. a charter with documentary sections and later endorsements;
4. a copy book/registratur with excerpts from several earlier records;
5. a mixed or multi-hand chronicle/codex with additions and marginalia;
6. the existing Reg. Ii 3/4/5 visitation material.

A solution fails Generic-Fit if changing only the source type requires changing the epistemic core, or if a source-specific role/layout/category becomes a mandatory universal class without independent evidence of recurrence.

## 22. Current conclusion

The repository’s governing architecture remains fundamentally sound:

```text
GOVERNING OBJECTIVE
→ domain/source requirements
→ METHOD
→ CORPUS / PROJECT canonical ownership
→ evidence-aware research workflow
→ deterministic checks only for settled structure
→ human/specialist review where judgement remains epistemic
```

The recent difficulties are best understood as **reconciliation failures at the boundaries**, not a need for a new platform. The evidence supports four durable generic principles:

1. **Documentary identity, digital instance, research locus and project use are separate.**
2. **Contextual role/date/relationship claims must be attached to the correct target with evidence, not inherited from proximity or hierarchy.**
3. **Research authority follows the evidence chain of the concrete claim/artifact, not its directory name.**
4. **Research maturity, historical use and current activity are orthogonal dimensions.**

These principles are domain-valid, strongly standards-aligned and compatible with the existing `REQ-*` architecture. Formal RiC/TEI/IIIF/PROV conformance is neither required nor currently claimed.

The next legitimate step is the bounded implementation/admission decision under `methodology/maintenance.md`, using Packages A–C above and this document as the concept/evidence handoff. No additional architecture programme is justified by the current evidence.
