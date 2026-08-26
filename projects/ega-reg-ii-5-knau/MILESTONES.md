# Research milestones — Knau

## Purpose

These milestones define **verifiable scholarly maturity states**, not task lists or a fixed waterfall. They implement `methodology/historical-source-workflow.md` for the Knau project.

A milestone is reached only when its requirements are satisfied. Later evidence may reopen an earlier milestone; consequential revision remains traceable.

> Every substantive activity must address an unmet requirement of the active milestone, repair an invalid prerequisite, or provide necessary evidence for doing so.

Uncertainty is not failure. A milestone may pass with `variant`/`unresolved` readings if those uncertainties have been represented and tested to the level the gate requires.

---

## M1 — Source and transmission basis secured

### Target state
The principal witness and already available comparison/control sources can be identified, recovered and related without chat, while archival metadata, digital instantiation and demonstrated textual relationships remain distinct.

### Requirements
- unambiguous canonical source identity for the principal witness;
- archive/fonds/signature/record/locus and persistent/digital identity recorded where available;
- project locus mapped independently of portal/export/PDF numbering;
- consequential digital files/instantiations represented in `corpus/files.tsv`;
- crosswalks distinguish folio, image, PDF/export and working IDs;
- comparison/control sources independently identified with explicit research roles;
- record relationships stated only at their demonstrated evidential level;
- catalogue claims distinguishable from manuscript/collation findings;
- project source basis reconstructable from repository alone.

### Exit gate
A competent researcher can identify and recover the exact principal witness/locus/instantiation and understand what is actually known about the other sources and their relationships.

### Permitted residual uncertainty
Textual dependence, scribal relationship or finer transmission chronology may remain unresolved if labelled.

### Current assessment
**Substantially reached.**

---

## M2 — Principal witness completely and diplomatically represented

### Target state
Every relevant physical text area of `Reg. Ii 5, fol. 61v–63r` is represented in a conservative, human-auditable diplomatic transcription that preserves the source structure required by `methodology/transcription-guidelines.md`.

Completeness means complete **representation of the source**, not complete resolution of every sign.

### Requirements
- archival folio/page is part of the primary scholarly address;
- physical manuscript lines are directly inspected and receive editor-assigned folio-local references; legacy export line IDs are not assumed to equal physical lines;
- folio/page breaks and physical lineation are preserved;
- reading order and layout region are represented where needed to preserve list/accounting/spatial meaning;
- every relevant visible line/text unit is represented; no prose paragraph summary substitutes for visible multi-line text;
- historical spelling, word forms, numerals/signs and materially relevant separators are preserved conservatively;
- uncertain positive reading is distinguishable from text that is illegible/missing/untranscribed (`unclear` vs `gap/illegible` concepts);
- editorial supply is distinguishable from written source text;
- additions, deletions/cancellations and damage are representable and recorded if actually observed;
- abbreviation sign and editor-provided expansion remain distinct;
- hand shift is recorded only if palaeographically supported;
- `observed`, `working`, `variant`, `unresolved` describe research status and are not used as substitutes for source-phenomenon description;
- normalized names/values and historical identification remain outside the diplomatic reading;
- every consequential unresolved/variant locus is discoverable from the structured transcription;
- a human-readable folio/line diplomatic witness view can be generated/derived from the canonical data without manual re-transcription or a second text truth;
- entry boundaries are sufficiently represented to establish the text's physical extent.

### Evidence/method allowed
Direct inspection of the principal witness and non-content-generating technical image enhancement. Internal comparison may assist recognition but may not replace source representation.

### Canonical outputs
Compliant principal-witness transcription data, provenance/crosswalk mapping, consequential decision log, and a derived human-readable diplomatic witness view.

Legacy `transcription/132.tsv`–`135.tsv` remain working/history inputs until directly re-inspected and migrated; they are not themselves sufficient proof of M2 compliance.

### Exit gate
A reviewer can move folio-by-folio and physical-line-by-physical-line through 61v–63r, locate every relevant source unit, distinguish written/unclear/illegible/supplied or other observed phenomena, and read a diplomatic witness view without interpreting machine-only fragments.

### Permitted residual uncertainty
Individual letters, words, abbreviations, numerals, measures, names and syntax may remain `variant`/`unresolved`. W1–W6 need not be solved.

### Reopen when
Omitted text, incorrect line/layout mapping, boundary error, misclassified source phenomenon or semantic reconstruction is discovered.

### Current assessment
**ACTIVE — not reached.** A standards audit found that the legacy working transcription requires direct folio/line/layout reinspection and minimal migration before M2 can pass.

---

## M3 — Internal palaeographic and notational analysis completed

### Target state
Consequential uncertainties in the principal witness have been systematically tested against relevant internal palaeographic evidence before stronger reliance on external parallels.

### Requirements
- all consequential uncertain loci inventoried by evidence class;
- grapheme/sign sequence localised before lexical completion;
- same-hand comparanda used only when hand relevance is actually supported; `same record` is not automatically `same hand`;
- repeated forms compared by discriminating graphical features;
- abbreviations, numerals, money/measure/accounting notation treated as potentially distinct sign systems;
- comparison anchors have exact loci and evidential status;
- competing readings preserved where evidence does not discriminate;
- rejected consequential readings remain traceable;
- domain knowledge generates candidate tests but does not prove manuscript readings;
- written sign, expansion, normalization and identification remain separate;
- promoted readings have explicit evidence notes;
- unresolved problems are handed forward rather than forced closed.

### Evidence/method allowed
Principal-witness images; relevant internally controlled palaeographic comparanda; explicit notation concordances. C2 may serve only as a separately labelled comparison/control source unless stronger relation/hand evidence is established.

### Exit gate
For every consequential uncertainty, a reviewer can see what evidence was tested, why a conclusion followed or why the reading remains unresolved.

### Permitted residual uncertainty
Any reading may remain unresolved after adequate testing.

---

## M4 — Existing comparison witnesses/controls independently assessed and collated

### Target state
Already available comparison sources are used according to demonstrated evidential roles, and the Reg. Ii 4 parallel is independently read and systematically collated with the principal witness without contamination.

### Requirements
- each comparison/control source remains independently identified;
- relevant loci are addressed archivally, not only by export number;
- Reg. Ii 4 `306v–309r` is independently represented/read sufficiently before collation with Reg. Ii 5 `61v–63r`;
- wording from one witness is never silently copied into another;
- corresponding textual units are explicitly mapped;
- agreements/differences in wording, spelling, numerals, measures, additions, omissions, order and structural features are recorded where material;
- contextual/control sources such as C2 remain distinguished from textual witnesses;
- catalogue extract claims remain distinct from findings of collation;
- relationship status is upgraded only when evidence justifies it;
- consequential changes to the principal reading are logged rather than overwritten.

### Exit gate
A reviewer can distinguish what each witness/source actually says, where they correspond/diverge and what transmission claims are warranted.

### Permitted residual uncertainty
Exact genetic dependence or some variants may remain unresolved.

---

## M5 — Critically consolidated and proportionally validated text state

### Target state
The principal witness has a complete, coherent and evidence-auditable transcription incorporating internal analysis and controlled comparison, with uncertainty, revision history and validation status preserved.

### Requirements
- relevant M1–M4 requirements are satisfied or explicitly reopened;
- principal transcription is fully M2-compliant and conventionally consistent;
- every consequential reading has appropriate research/source-phenomenon status;
- important working readings/relationships undergo adversarial falsification attempts proportional to consequence;
- rejected semantic/fluent reconstructions do not re-enter without new evidence;
- palaeographic/collation-driven changes are traceable;
- source relationships remain stated at demonstrated level;
- manuscript forms remain separate from normalization/identification;
- consequential numeral/currency/measure readings use the strongest available relevant evidence;
- residual uncertainties are discoverable and their evidential limits explained where consequential;
- bounded consistency check confirms transcription/apparatus/palaeography/source audit/corpus relations/status coherence;
- the repository states explicitly which consequential specialist claims have or have not received **independent qualified human review**;
- method-compliant AI-assisted work is not labelled expert-validated without such review.

### Exit gate
A third party can audit consequential readings back to source and decision history; the remaining question is editorial representation, not missing core source work.

### Permitted residual uncertainty
Explicitly documented unresolved readings, expansions and transmission questions are permitted.

---

## M6 — Scholarly edition produced and quality-controlled

### Target state
A usable scholarly edition is produced from M5 without erasing distinctions among manuscript evidence, editorial intervention, normalization/identification and historical commentary.

### Requirements
- an explicit edition concept states purpose, user group, scope, source/witness basis, edition type and presentation strategy;
- editorial/transcription conventions actually used are declared;
- edition text is derived from M5 and introduces no undocumented manuscript readings;
- expansions, supplied text, uncertain/illegible material and other interventions are distinguishable;
- material variants from relevant witnesses appear in an apparatus or equivalent transparent form;
- normalized names/places/values and historical identifications are not presented as diplomatic manuscript text;
- source/transmission note distinguishes catalogue metadata from findings of collation;
- historical/sachliche commentary is evidence-based and separable from transcriptional claims;
- consequential editorial claims trace back to source locus/evidence/decision history;
- residual uncertainty remains visible;
- final source-to-output audit includes difficult passages and adversarial checking;
- independent specialist review appropriate to consequential palaeographic/editorial claims is recorded, or its absence explicitly disclosed;
- publication/data format is selected for actual scholarly use and preservation/interoperability; TEI or additional infrastructure is introduced only when justified by a concrete dissemination requirement.

### Exit gate
A reader can use the edition while a specialist can distinguish source text, uncertainty, editorial intervention, variant evidence, normalization/identification and interpretation, and audit consequential claims.

### Permitted residual uncertainty
Publication does not convert unresolved evidence into certainty.

---

## Milestone progression and iteration

`M1 source basis → M2 diplomatic representation → M3 internal analysis → M4 controlled comparison → M5 critical consolidation/validation → M6 edition`

Later evidence may reopen earlier states. The rule is controlled revision with provenance, not immutability.

Do not advance because activity occurred; advance only when the gate requirements are demonstrably met.

## STATUS relationship

`STATUS.md` records overall goal, reached/active milestone, unmet active-gate requirements, validation status and exact next action. Detailed milestone requirements live here and should not be duplicated there.
