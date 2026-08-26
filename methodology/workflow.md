# Workflow — operational map

## Authority

The authoritative scholarly end-to-end method is `methodology/historical-source-workflow.md`. This file is only the **operational execution map**. Detailed transcription requirements live in `methodology/transcription-guidelines.md`; provenance in `source-and-provenance.md`; evidence/source-status rules in `evidence-policy.md`; AI validation rules in `ai-governance.md`.

If an operational shortcut conflicts with the scholarly method, the scholarly method wins and the conflict must be repaired.

## Goal

Produce a traceable, human-auditable historical source transcription and analysis with the least process necessary to keep it reliable. Research activity must advance an explicit project milestone requirement rather than merely generate more tooling or notes.

## Operational sequence

### S1 — Identify source/provenance
Register canonical source identity, archival locus and digital instantiation. Keep folio, portal/export image, PDF page and working IDs distinct. Record source relationships at their actual evidential level.

### S2 — Inspect document/material structure
Before claiming complete transcription, inspect the working locus for foliation/boundaries, physical lineation, reading order, layout/list/table structure, headings/marginalia, additions/deletions/corrections, damage/illegibility, abbreviation practice and evidence of hand shifts where relevant.

Do not mark unexamined phenomena absent; use `not investigated` where necessary.

### S3 — Diplomatic transcription
Transcribe the principal witness by archival folio and directly inspected physical line. Preserve source structure and written forms. Distinguish uncertainty/source phenomena according to `transcription-guidelines.md`. Do not replace visible multi-line source text with semantic summaries.

A human-readable folio/line witness view must be derivable from canonical transcription data; machine-oriented TSV fragments alone are not sufficient as an M2 result.

### S4 — Internal palaeographic analysis
For consequential uncertainty, localise the sign sequence, classify the problem, seek appropriate controlled internal comparanda, compare graphical features and record candidates/evidence. Same record is not automatically same hand. Context follows graphematic candidate formation rather than replacing it.

### S5 — Freeze/review principal-witness checkpoint
Before strong external-witness influence, ensure the principal witness has a coherent source-based checkpoint. It may contain unresolved readings.

### S6 — Independent external control and collation
Identify/read related witnesses and controls independently, then map corresponding loci and collate. Record agreements/divergences and upgrade source relationships only as far as evidence warrants. Never copy a clearer witness into the principal witness transcription.

### S7 — Normalize/identify/interpret
Only after source readings are explicit, link manuscript forms to normalized people/places/institutions/values/concepts and perform historical source criticism. Keep manuscript form, expansion, normalization, identification and interpretation distinct.

### S8 — Critical consolidation/validation
Run the relevant scholarly and technical integrity gates: complete source representation, decision traceability, adversarial checking, provenance/referential consistency, witness-contamination check and explicit independent-human-review status for consequential specialist claims.

An unresolved but well-tested result may pass; an unsupported resolved result may not.

### S9 — Edition/publication
Define an explicit edition concept, then derive the user-facing edition from the consolidated research state. Do not introduce new manuscript readings at the presentation stage. Match publication/interchange technology to a concrete scholarly need.

## Research-state persistence

When research truth changes, update its canonical owner during the same work block when practical:

- source identity/inspection stage → `corpus/sources.tsv`;
- external/digital file identity/recoverability → `corpus/files.tsv`;
- source/event/entity relationship → `corpus/relationships.tsv`;
- event context → `corpus/events.tsv`;
- project source/folio/image mapping → project `sources/`;
- diplomatic reading → project `transcription/`;
- consequential reading revision/rejection → `apparatus/decisions.tsv`;
- palaeographic evidence → `palaeography/`;
- external-source inspection status → `research/`;
- active gate/next action → `STATUS.md`;
- project-specific failure/lesson → `LEARNINGS.md`;
- general scholarly method → `historical-source-workflow.md` or relevant detailed methodology;
- durable cross-project architecture rationale → `DECISIONS.md`.

Do not make a future researcher recover durable state from chat.

## Project milestone rule

Project milestones define scholarly maturity states, not schedules. `STATUS.md` must identify the active milestone and the smallest next source/evidence action that advances an unmet requirement.

If a proposed activity cannot be tied to an unmet gate requirement, an invalid prerequisite or necessary evidence, do not perform it as current research work.

## Validation proportionality

Use the lightest check sufficient for the consequence of being wrong, but never omit distinctions required for scholarly source representation. Tooling can remain lean; evidence semantics cannot.

Independent specialist validation is not the same as method-compliant AI work. Record which occurred.

## Corpus expansion

Corpus discovery is separate from the active transcription/edition workflow. Discovered sources may remain metadata/images inspected. Full transcription is never automatic merely because a source exists.

## Deferred technology

When useful technology is not required by a current scholarly gate, preserve it as a trigger-based GitHub Issue rather than implementing it speculatively.

## Maintenance

Follow `methodology/maintenance.md`: propagate material truth changes across dependent records, run a bounded consistency pass when warranted, then return to source research.
