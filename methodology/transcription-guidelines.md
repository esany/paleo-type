# Transcription guidelines

## Authority and aim

This file implements the transcription stage of `methodology/historical-source-workflow.md`.

Aim: create a conservative diplomatic transcription of a concrete historical witness that is **human-auditable, archivally addressable and capable of loss-minimising later mapping to an established scholarly representation such as TEI P5**. The working format may remain lean TSV; lean does not permit collapsing distinct source phenomena into one ambiguous marker.

## Scholarly address

The primary scholarly location of a transcription unit is:

`canonical source_id + archival folio/page + editor-assigned physical line reference`

For example, conceptually:

`THHSTAW-EGA-REG-II-5-STAT-VIS-00000129 : 61v : 07`

Portal/export image, PDF page and legacy working IDs remain separate provenance fields/crosswalk values. They must not become the sole scholarly address.

Editor-assigned line numbers describe the physical manuscript line sequence and are not historical manuscript numbering. Re-establish them only by direct image inspection; never convert legacy line IDs mechanically if their physical correspondence has not been checked.

## Preserve physical/documentary structure

For the diplomatic layer:

- preserve folio/page boundaries;
- preserve physical lineation;
- record reading order and layout region where relevant;
- preserve headings, lists, marginalia, columns or spatial arrangements when their position affects interpretation/transcription;
- do not silently reflow the source into modern paragraphs;
- use a later derived view for reading convenience rather than altering the diplomatic record.

## Preserve written forms

- Preserve historical spelling.
- Preserve word division/joining as read from the source where discriminable.
- Preserve numerals, currency/measure signs and other special signs rather than replacing them with interpreted values.
- Preserve materially relevant punctuation/separators.
- Use `/` only when it represents an observed source separator or an explicitly documented project convention; never use it ambiguously for a line break if physical lineation is already structurally recorded.
- Do not modernize names inside the diplomatic reading.

## Distinguish source phenomena from reading confidence

A reading status (`observed`, `working`, `variant`, `unresolved`, `rejected`) answers **how the research currently assesses the reading**. It is not a substitute for describing **what source phenomenon is present**.

The transcription model must distinguish at least these concepts when they occur:

### Positive but uncertain reading — `unclear`
Text/signs are visible and a reading is proposed, but the reading is uncertain.

Record the proposed visible reading plus uncertainty; do not replace it with a generic gap.

### Present but not legibly transcribed — `gap/illegible`
Textual material is present or expected in the source area but cannot be responsibly transcribed (for example illegibility, loss, or intentionally untranscribed content). Record reason and approximate extent where the source permits.

Do not use `...` as an untyped substitute for illegibility.

### Editorial supply — `supplied`
Text not securely present/legible in the surviving source but supplied by the editor must be explicitly separate from the diplomatic reading and carry a reason/evidence basis. Contextual completion is never silently supplied.

### Deletion/cancellation — `deletion`
Text cancelled/deleted in the witness remains a source phenomenon and must not simply disappear from the transcription if relevant/legible.

### Addition — `addition`
Interlinear, marginal or other added text must retain its addition status and location/reading order.

### Damage — `damage`
Physical/material damage affecting the text must be distinguished from an ordinary uncertain reading.

### Abbreviation and expansion
The written abbreviation/sign belongs to the diplomatic source layer. Any editor-provided expansion is a separate editorial layer/value. Do not silently replace abbreviation with expansion.

### Hand shift
Record a hand shift only when palaeographic evidence supports a distinct hand. Same record/date/office or textual similarity is not hand identity.

## Uncertainty and alternatives

- Use `alternatives` only for graphically viable competing readings.
- Use `unresolved` rather than invented completion.
- Localize uncertain spans as narrowly as source evidence permits.
- Preserve partial strings/graphemes where visible rather than replacing a whole line/paragraph with a prose summary.
- Do not use syntax, historical identification or a parallel witness to rewrite the graphemes of the witness under transcription.

## Document/material observation before transcription completion

Before declaring a locus completely represented, check the source for relevant transcription phenomena:

- folio/page and entry boundary;
- reading order;
- headings/list/table/accounting layout;
- marginalia/interlinear text;
- additions/deletions/corrections;
- damage/illegibility;
- abbreviation practices;
- possible hand shifts.

Record `not investigated` rather than assuming absence if the question has not actually been checked.

## Working data model requirements

The previous minimal working schema

`page_id  line_id  region  reading  status  alternatives  evidence_note`

is now classified as a **legacy working schema**: useful for preserving existing research history but not sufficient as the final M2 scholarly representation.

The compliant lean model for new/migrated principal-witness data must be able to represent, without ambiguity:

- canonical `source_id`;
- archival `folio`/page;
- editor-assigned physical `line_no` or equivalent stable local line reference;
- `region`/reading-order information when needed;
- diplomatic written `reading`;
- source phenomenon type(s) when not ordinary continuous text (`unclear`, `gap/illegible`, `addition`, `deletion`, `damage`, etc.);
- research `status`;
- graphically viable `alternatives`;
- explicit abbreviation expansion/editorial supply only in separate field/record/layer when needed;
- evidence/decision note or reference where consequential;
- provenance back to digital/export/legacy IDs through crosswalk or explicit fields.

**Do not add every possible TEI category as a TSV column.** Choose the smallest fields/record structure that represents the phenomena actually found in the source while preserving a non-lossy conceptual mapping.

Before migrating legacy Knau rows, directly reinspect the images for physical lineation and phenomena. Do not generate folio-line IDs from old export line numbers by assumption.

## Human-readable diplomatic witness view

A principal-witness transcription is not M2-complete if a human must reconstruct its text by interpreting machine-oriented fragments.

The canonical structured data must support a deterministic or clearly derived view showing at least:

- full archival source/locus citation;
- explicit folio breaks;
- editor-assigned physical line numbers;
- diplomatic text in reading order;
- visible markers for uncertainty/unreadability/editorial intervention according to documented conventions;
- no hidden normalization.

The view is not a second manually maintained transcription truth.

## Confidence language

Avoid pseudo-precision percentages. Use evidence-bearing statuses and explain reasons. “Working because controlled comparison supports the internal grapheme sequence” is more useful than “90% confident”.

## Normalization and identification

Normalization, person/place identification and historical interpretation belong outside the diplomatic transcription. A normalized `Gräfendorf` must never overwrite an unresolved/variant manuscript surname form.

## M2 exit condition

A locus passes the diplomatic-representation gate only when a reviewer can inspect the source folio by folio and find every relevant visible physical line/text unit represented at the correct archival address, with source phenomena and uncertainty distinguished according to this guideline and without paragraph-level semantic placeholders standing in for visible text.
