# Transcription guidelines

## Authority and aim

This file implements the diplomatic-transcription stage of `historical-source-workflow.md` and the G2 requirements in `research-gates.md`.

Aim: create a conservative diplomatic transcription of a concrete historical witness that is **human-auditable, archivally addressable and capable of loss-minimising later mapping to an established scholarly representation such as TEI P5**. The working format may remain lean TSV; lean does not permit collapsing distinct source phenomena into one ambiguous marker.

## Scholarly address

The primary scholarly location of a transcription unit is:

`canonical source_id + archival folio/page + editor-assigned physical line reference`

Conceptual example:

`SOURCE-ID : fol. 12v : line 07`

Portal/export image, PDF page and legacy working IDs remain separate provenance/crosswalk values. They must not become the sole scholarly address.

Editor-assigned line numbers describe the physical manuscript line sequence and are not historical manuscript numbering. Establish/re-establish them only by direct source inspection; never convert legacy line IDs mechanically when their physical correspondence has not been checked.

## Preserve physical/documentary structure

For the diplomatic layer:
- preserve folio/page boundaries;
- preserve physical lineation;
- record reading order and layout region where relevant;
- preserve headings, lists, marginalia, columns or spatial arrangements when position affects interpretation/transcription;
- do not silently reflow the source into modern paragraphs;
- use a later derived view for reading convenience rather than altering the diplomatic record.

## Preserve written forms

- Preserve historical spelling.
- Preserve word division/joining where discriminable.
- Preserve numerals, currency/measure signs and other special signs rather than replacing them with interpreted values.
- Preserve materially relevant punctuation/separators.
- Use `/` only when it represents an observed source separator or an explicitly documented project convention; never use it ambiguously for a line break if lineation is structurally recorded.
- Do not modernize names inside the diplomatic reading.

## Distinguish source phenomena from reading confidence

A research status (`observed`, `working`, `variant`, `unresolved`, `rejected`) answers **how the research currently assesses a reading**. It is not a substitute for describing **what source phenomenon is present**.

The transcription model must distinguish at least these concepts when they occur:

### Positive but uncertain reading — `unclear`
Text/signs are visible and a reading is proposed, but uncertain. Record the proposed reading plus uncertainty; do not replace it with a generic gap.

### Present but not legibly transcribed — `gap/illegible`
Textual material is present/expected in the source area but cannot be responsibly transcribed. Record reason and approximate extent where possible. Do not use `...` as an untyped substitute.

### Editorial supply — `supplied`
Text not securely present/legible in the surviving source but supplied by the editor must be explicitly separate from the diplomatic reading and carry reason/evidence. Contextual completion is never silently supplied.

### Deletion/cancellation — `deletion`
Cancelled/deleted text remains a source phenomenon and must not simply disappear if relevant/legible.

### Addition — `addition`
Interlinear, marginal or other added text must retain addition status and location/reading order.

### Damage — `damage`
Physical/material damage affecting the text must be distinguished from an ordinary uncertain reading.

### Abbreviation and expansion
The written abbreviation/sign belongs to the diplomatic source layer. Any editor-provided expansion is a separate editorial value/layer. Do not silently replace abbreviation with expansion.

### Writing-characteristic change, hand hypothesis and scribe identity
Observable differences or changes in writing characteristics may be recorded conservatively as direct source observations or a `possible hand shift` when the image supports that description. This does **not** by itself create a discrete hand identity.

Promote an observed change to a distinct-hand hypothesis only after palaeographic comparison of discriminating graphical features and exact comparison loci. Any identification of that hypothesized hand with a named historical person/scribe is a further, separately evidenced claim.

Same record/date/office, textual similarity or an event/administrative role is not hand identity.

## Uncertainty and alternatives

- Use `alternatives` only for graphically viable competing readings.
- Use `unresolved` rather than invented completion.
- Localize uncertain spans as narrowly as source evidence permits.
- Preserve partial strings/graphemes where visible rather than replacing a whole line/paragraph with a prose summary.
- Do not use syntax, historical identification or a parallel witness to rewrite graphemes in the witness under transcription.

## Document/material observation before transcription completion

Before declaring a locus completely represented, check the source for relevant transcription phenomena:
- folio/page and text boundary;
- reading order;
- headings/list/table/accounting layout;
- marginalia/interlinear text;
- additions/deletions/corrections;
- damage/illegibility;
- abbreviation practices;
- observable writing-characteristic changes / possible hand shifts.

Record `not investigated` rather than assuming absence if the question has not actually been checked.

## Working data model requirements

A lean compliant principal-witness model must be able to represent, without ambiguity:
- canonical `source_id`;
- archival `folio`/page;
- editor-assigned physical `line_no` or equivalent local line reference;
- `region`/reading-order information when needed;
- diplomatic written `reading`;
- source phenomenon type(s) when not ordinary continuous text (`unclear`, `gap/illegible`, `addition`, `deletion`, `damage`, etc.);
- research `status`;
- graphically viable `alternatives`;
- explicit abbreviation expansion/editorial supply only in a separate field/record/layer when needed;
- evidence/decision note or reference where consequential;
- provenance back to digital/export/legacy IDs through crosswalk or explicit fields.

Do **not** add every possible TEI category as a TSV column. Choose the smallest representation that preserves the phenomena actually found in the source and a loss-minimising conceptual mapping.

A project with legacy working transcription must reinspect physical lineation/source phenomena before migrating identifiers or collapsing/expanding rows. Existing research history is preserved; unverified structural mappings are not inferred.

## Human-readable diplomatic witness view

A principal-witness transcription is not G2-complete if a human must reconstruct its text by interpreting machine-oriented fragments.

Canonical structured data must support a deterministic or clearly derived view showing at least:
- full archival source/locus citation;
- explicit folio/page breaks;
- editor-assigned physical line numbers where used;
- diplomatic text in reading order;
- visible markers for uncertainty/unreadability/editorial intervention according to documented conventions;
- no hidden normalization.

The view is not a second manually maintained transcription truth.

## Confidence language

Avoid pseudo-precision percentages. Use evidence-bearing statuses and explain reasons. A reason tied to inspected graphical evidence is more useful than a confidence percentage.

## Normalization and identification

Normalization, person/place identification and historical interpretation belong outside the diplomatic transcription. A normalized historical identity must never overwrite a manuscript reading.

`Outside the diplomatic transcription` is an **epistemic-layer rule, not a mandatory chronological deferral**. Text-near annotation and editorical identification/contextualization may grow in the same source-work pass when they are persisted as separate claims/layers with their own evidence and status. They do not become diplomatic text merely because they are investigated concurrently.

## G2 exit condition

A locus passes the diplomatic-representation gate only when a reviewer can inspect the source folio/page by folio/page and find every relevant visible physical line/text unit represented at the correct archival address, with source phenomena and uncertainty distinguished according to this guideline and without paragraph-level semantic placeholders standing in for visible text.