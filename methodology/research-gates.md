# Research gates — generic scholarly maturity model

## Purpose

These gates define **reusable scholarly maturity states** for projects in `paleo-type`. They are not schedules, task lists or project-specific milestone definitions. The authoritative end-to-end method is `historical-source-workflow.md`; these gates answer when a project may claim a given research state has been reached.

A concrete project records only its own status, unmet requirements and next action in `projects/<id>/STATUS.md`.

GitHub may use a project-scoped Milestone such as `<project> / G2 — Diplomatic representation` to group discrete Issues that contribute to one of these gates. That Milestone is a **work-planning mirror only**: its progress/closure does not establish scholarly gate attainment, and its description must not duplicate or redefine the generic requirements below. See `MILESTONES.md`.

> A project may advance only when the relevant gate requirements are demonstrably met. Activity alone does not complete a gate.

Later evidence may reopen an earlier gate. Consequential revision must remain traceable. Explicitly unresolved evidence is compatible with a passed gate when the gate requires representation/testing rather than forced resolution.

---

## G1 — Source and transmission basis secured

### Target state
The project's bounded source group can be reconstructed: every principal/comparison/control/context record is independently identified; project roles/loci are explicit; exact digital instantiations used as evidence are byte-identifiable and recoverable or have an explicit preservation blocker; archival description, digital instantiation and demonstrated textual relationships remain distinct.

### Requirements
- the project source group is explicit and human-readable in `projects/<id>/sources/sources.tsv`;
- principal source/witness has an unambiguous canonical identity;
- every material comparison/control/context source is independently identified rather than collapsed by shared archive/signature/topic;
- archive/fonds/signature/record/title/locus and persistent/digital identifiers are recorded where available;
- project-relevant locus is separated from the source's full archival extent;
- archival locus is mapped independently of portal/export/PDF numbering;
- each consequential digital file/instantiation has exact filename, SHA-256, coverage and preservation/storage state in `corpus/files.tsv`;
- the exact inspected export is recoverable from its controlled preservation location, or the repository states a concrete unresolved preservation blocker; URL/URN + checksum alone is not misrepresented as equivalent backup;
- reusable source-wide crosswalks distinguish folio/page, image, PDF/export and working identifiers and have one canonical source-data home;
- source roles in the project are distinguished from historical/source relationships;
- source relationships are stated only at the level supported by inspected evidence;
- catalogue/finding-aid claims remain distinguishable from manuscript/collation findings;
- project source basis can be reconstructed from repository state without chat.

### Exit gate
A competent third party can identify every material source record in the investigation, understand its project role/locus, recover or account for the exact inspected instantiation, and understand what is actually known about relevant source relationships.

### Permitted residual uncertainty
Textual dependence, scribal relationship, finer chronology or record-stage relationships may remain unresolved when explicitly labelled. A rights/access preservation blocker may remain only if the exact byte identity is controlled and the limitation is explicit; it is not silently treated as full repository preservation.

### Reopen when
Source identity, source-group membership/role, locus mapping, digital-file identity/preservation state, provenance, project boundary or a consequential source relationship is shown to be wrong or materially incomplete.

---

## G2 — Principal witness completely and diplomatically represented

### Target state
Every relevant physical text area of the principal witness is represented in a conservative, human-auditable diplomatic transcription conforming to `transcription-guidelines.md`. Completeness means complete **representation of the source**, not complete resolution of every sign.

### Requirements
- archival folio/page is part of the primary scholarly address;
- physical manuscript lines are directly inspected and receive editor-assigned local references where lineation is used;
- folio/page breaks and physical lineation are preserved;
- reading order and layout region are represented where needed to preserve spatial/list/tabular meaning;
- every relevant visible line/text unit is represented; prose summaries do not substitute for visible multi-line text;
- historical spelling, word forms, numerals/signs and materially relevant separators are preserved conservatively;
- uncertain positive reading is distinguishable from illegible/missing/untranscribed material;
- editorial supply/expansion is distinguishable from written source text;
- additions, deletions/cancellations and damage are representable and recorded when observed;
- abbreviation sign and editor-provided expansion remain separate;
- hand shifts are recorded only when palaeographically supported;
- research status is separate from source-phenomenon description;
- normalization/identification remains outside the diplomatic reading;
- consequential unresolved/variant loci are discoverable from the structured transcription;
- a human-readable folio/page and line-addressable diplomatic witness view can be derived from canonical data without manual re-transcription or a second text truth;
- text boundaries are sufficiently represented to establish scope.

### Evidence/method allowed
Direct inspection of the principal witness and non-content-generating technical image enhancement. Internal comparison may assist recognition but may not replace source representation.

### Canonical outputs
Compliant principal-witness transcription, provenance/crosswalk mapping, consequential decision trail, and a derived human-readable diplomatic witness view.

### Exit gate
A reviewer can traverse the source in physical order, locate every relevant source unit, distinguish written/uncertain/illegible/supplied or other observed phenomena, and read the diplomatic witness without interpreting machine-only fragments.

### Permitted residual uncertainty
Letters, words, abbreviations, numerals, measures, names and syntax may remain `variant` or `unresolved`.

### Reopen when
Omitted source text, incorrect physical-line/layout mapping, boundary error, misclassified source phenomenon or semantic reconstruction is discovered.

---

## G3 — Internal palaeographic and notational analysis completed

### Target state
Consequential uncertainties in the principal witness have been systematically tested against relevant internal palaeographic evidence before stronger reliance on external parallels.

### Requirements
- consequential uncertain loci are inventoried by evidence class;
- grapheme/sign sequence is localized before lexical completion;
- same-hand comparanda are used only when hand relevance is actually supported; same record is not automatically same hand;
- repeated forms are compared by discriminating graphical features;
- abbreviations, numerals, monetary/metrological/accounting notation are treated as potentially distinct sign systems;
- comparison anchors have exact loci and evidential status;
- competing readings are preserved where evidence does not discriminate;
- consequential rejected readings remain traceable;
- domain knowledge generates tests but does not prove manuscript readings;
- written sign, expansion, normalization and identification remain separate;
- promoted readings have explicit evidence basis;
- unresolved problems are handed forward rather than forced closed.

### Exit gate
For every consequential uncertainty, a reviewer can see what internal evidence was tested, why a conclusion followed or why the reading remains unresolved.

### Permitted residual uncertainty
Any reading may remain unresolved after adequate testing.

### Reopen when
New internal/same-hand evidence appears, an anchor is invalidated or later collation exposes a likely misreading requiring renewed palaeographic inspection.

---

## G4 — Comparison witnesses/controls independently assessed and collated

### Target state
Relevant comparison sources are used according to demonstrated evidential roles and independently read before systematic collation with the principal witness.

### Requirements
- each comparison/control source remains independently identified;
- relevant loci are archivally addressed, not only by export/image number;
- comparison witness text is independently represented/read sufficiently before collation;
- wording from one witness is never silently copied into another;
- corresponding textual units are explicitly mapped;
- material agreements/differences in wording, spelling, numerals, measures, additions, omissions, order and structure are recorded;
- contextual/control sources remain distinguished from textual witnesses;
- catalogue relationship claims remain distinct from findings of collation;
- source-relationship status is upgraded only when evidence justifies it;
- consequential changes to principal-witness readings are logged rather than silently overwritten.

### Exit gate
A reviewer can distinguish what each witness/source independently says, where they correspond/diverge and which transmission claims are warranted.

### Permitted residual uncertainty
Exact genetic dependence and individual variants may remain unresolved.

### Reopen when
A comparison witness is materially re-read, a locus mapping changes, a supposed correspondence fails or new evidence changes the transmission assessment.

---

## G5 — Critically consolidated and proportionally validated text state

### Target state
The principal witness has a complete, coherent and evidence-auditable transcription incorporating internal analysis and controlled comparison, with uncertainty, revision history and validation status preserved.

### Requirements
- relevant G1–G4 requirements are satisfied or explicitly reopened;
- principal transcription remains G2-compliant and conventionally consistent;
- every consequential reading has appropriate research/source-phenomenon status;
- important working readings/relationships undergo adversarial falsification attempts proportional to consequence;
- rejected semantic/fluent reconstructions do not re-enter without new evidence;
- palaeographic/collation-driven changes are traceable;
- source relationships remain stated at demonstrated level;
- manuscript forms remain separate from normalization/identification;
- consequential numeral/currency/measure readings use the strongest available relevant evidence;
- residual uncertainties are discoverable and evidential limits explained where consequential;
- bounded consistency checking confirms coherence among transcription, apparatus, palaeography, source audit, corpus relations and project status;
- the project states which consequential specialist claims have or have not received **independent qualified human review**;
- method-compliant AI-assisted work is never labelled expert-validated without such review.

### Exit gate
A third party can audit consequential readings from consolidated text back to source and decision history; the remaining work is editorial representation rather than missing core source work.

### Permitted residual uncertainty
Explicit unresolved readings, expansions and transmission questions are allowed.

### Reopen when
A material source-reading error, provenance error, invalid comparison anchor or consequential undocumented decision is discovered.

---

## G6 — Scholarly edition produced and quality-controlled

### Target state
A usable scholarly edition is produced from G5 without erasing distinctions among manuscript evidence, editorial intervention, normalization/identification and historical commentary.

### Requirements
- an explicit edition concept states purpose, audience, scope, source/witness basis, edition type and presentation strategy;
- editorial/transcription conventions actually used are declared;
- edition text is derived from G5 and introduces no undocumented manuscript readings;
- expansions, supplied text, uncertain/illegible material and other interventions remain distinguishable;
- material witness variants appear in an apparatus or equivalent transparent form where relevant;
- normalized names/places/values and historical identifications are not presented as diplomatic manuscript text;
- source/transmission note distinguishes catalogue metadata from findings of collation;
- historical/sachliche commentary is evidence-based and separable from transcriptional claims;
- consequential editorial claims trace back to source locus/evidence/decision history;
- residual uncertainty remains visible;
- final source-to-output audit includes difficult passages and adversarial checking;
- independent specialist review appropriate to consequential palaeographic/editorial claims is recorded, or its absence explicitly disclosed;
- publication/data format is selected for actual scholarly use and preservation/interoperability; additional infrastructure is introduced only when justified by a concrete dissemination requirement.

### Exit gate
A reader can use the edition while a specialist can distinguish source text, uncertainty, editorial intervention, variant evidence, normalization/identification and interpretation, and can audit consequential claims.

### Permitted residual uncertainty
Publication does not convert unresolved evidence into certainty.

### Reopen when
Post-publication/source review reveals a material error, new evidence changes a consequential reading/relationship, or a new edition version intentionally incorporates further research.

---

## Progression and project usage

`G1 source basis → G2 diplomatic representation → G3 internal analysis → G4 controlled comparison → G5 critical consolidation/validation → G6 edition`

The sequence expresses dependency, not an irreversible waterfall. Projects may perform supporting work from a later gate when necessary, but the active gate remains the controlling maturity claim.

Project `STATUS.md` records only:
- overall project goal;
- gate state (`reached`, `active`, `not reached`, `reopened`);
- project-specific unmet requirements/blockers;
- validation/review state where consequential;
- exact next action.

GitHub project-gate Milestones may group scheduled Issues for human navigation, but they do not alter this ownership model or the evidence required to change gate state.

Do not duplicate these generic gate requirements inside individual projects or GitHub Milestone descriptions.