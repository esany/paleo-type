# Workflow

## Goal

Produce a traceable corpus map, transcription and source-based historical working basis with the least process necessary to keep results reliable.

## Stages

### -1. Discover and bound the source field
When the task extends beyond a single known manuscript, record candidate archival records in `corpus/sources.tsv` without pretending they have been inspected. Keep discovery scope explicit: repository/catalogue, date/geographic limits, query/filter and access limits when completeness matters.

Do not transcribe everything merely because it was discovered. Prioritize by expected research value.

### 0. Register source identity and provenance
Follow `methodology/source-and-provenance.md`.

Distinguish archival unit, record, witness, locus and digital instantiation. Record archive/fonds/signature/record ID, folio/locus, digital URL/identifier and inspection status where available. Keep portal image numbers, PDF pages, export sequence and archival foliation separate.

If a new source relation matters (extract/copy/parallel/event membership), record it in `corpus/relationships.tsv` with the actual evidence status. Do not convert catalogue metadata into demonstrated textual dependence.

Preserve enough identity that substantive work does not depend on recovering a transient chat attachment. Check rights/access constraints before external AI processing where relevant.

### 1. Observe
Record page structure, regions, physical lines, headings, marginalia and obvious numerical/list structures. Do not interpret lexical content unnecessarily.

### 2. Blind read
Transcribe from the image before consulting contextual identifications or external parallels. Preserve historical spelling. Mark unresolved/variant material explicitly.

### 3. Internal palaeographic comparison
Use repeated forms in the same hand/source to test graphemes, abbreviations, numerals and words. Store reusable hand/source-specific evidence in `palaeography/`.

### 4. Adjudicate
Change a working reading only when evidence improves. Log material revisions and rejected readings. If AI materially shaped a consequential decision, record proportional research provenance as defined in `ai-governance.md`.

### 5. Freeze witness checkpoint
Create a coherent page/section transcription version before importing broad contextual or parallel-witness wording. A checkpoint may still contain unresolved tokens.

### 6. Collate / external control
For a possible parallel witness:

1. identify both records independently;
2. locate corresponding loci;
3. inspect/read each without importing the other's spelling;
4. compare structure and wording;
5. record correspondence/divergence;
6. upgrade the source relationship only as far as the evidence warrants.

For external controls generally, prefer direct parallel primary sources and scholarly editions before research literature. Audit access level before using content.

### 7. Identify and interpret
Link readings to persons, places, institutions, legal/economic concepts and historical context. Keep normalized identities separate from manuscript forms. Keep source-derived facts separate from inference.

### 8. Publish usable result
Produce a readable transcription, uncertainty/apparatus, source/provenance basis and concise historical commentary whose claims can be traced. Raise validation to match the consequence of error; consequential claims that remain dependent on unresolved specialist judgement require appropriate independent human review.

### 9. Persist research state
Whenever a work session changes research truth, persist the minimum changed state in its canonical repository records before relying on the result for future continuation.

In particular:

- corpus source identity/inspection stage → `corpus/sources.tsv`;
- source/event/entity relationship → `corpus/relationships.tsv`;
- event context → `corpus/events.tsv`;
- repeated normalized identity → `entities/` where useful;
- project-specific image/folio/export mapping → project `sources/`;
- changed readings → `transcription/` and substantive replacements/rejections → decision log;
- changed comparison evidence → `palaeography/`;
- changed external-source access/status → `research/`;
- changed active problem/scope/next action → `STATUS.md`;
- project-specific failure/correction → `LEARNINGS.md`;
- general method/structure → owning methodology/guardrail file.

Do not make a future agent recover durable research state from chat.

### 10. Research integrity gate
Before treating a consequential changed result or substantive work block as complete, run the relevant branches of `methodology/quality-and-learning.md`.

The gate tests evidence actually inspected, claim-layer separation, genuine independence of corroboration, persistence of changed research truth and goal alignment.

For archival/corpus work also ask:

- is the exact record/locus/instantiation identifiable?
- did I confuse image/PDF/export numbering with foliation?
- is a relationship observed/textually demonstrated, or only metadata-supported?
- did a clearer parallel witness overwrite the witness under transcription?

A consequential unresolved result may pass. An unsupported resolved result may not.

At useful checkpoints, actively try to falsify a small sample of important `working` readings or relationships rather than merely confirm repository consistency.

## Corpus expansion cycle

Once the starting project is stable enough, corpus growth follows:

`discover → register → deduplicate without forced merging → inspect structure → prioritize → selectively transcribe/collate → update relations → return to active research question`

A source may remain `metadata-inspected` or `images-inspected`; full transcription is not a default requirement.

## AI governance triggers

Ordinary AI assistance stays lean. Do not create evaluation infrastructure for routine candidate generation, comparison or critique.

Formal evaluation is triggered when AI/HTR/automation materially determines corpus-level findings such as bulk transcription, classification, extraction, coding or quantitative counts. Then follow `methodology/ai-governance.md`: representative human-checked material, appropriate metrics, qualitative failure analysis, validated scope and explicit exclusions.

## Priority rule

At every stage choose the next action with the highest expected reduction of consequential uncertainty per unit effort. Direct source comparison beats generic tooling when it answers the question faster.

Validation is proportional: use the lightest check sufficient for the consequence of being wrong.

## Checkpoint rule

Project `STATUS.md` is the canonical continuation point for active work. It should point to corpus/source records rather than duplicate them.

A valid checkpoint is restartable: another capable agent should be able to continue correctly from the repository without the old chat.

## Deferred improvement rule

When a useful future technical/methodological extension is not justified now, preserve it as a GitHub Issue with:

`problem/benefit → why not now → trigger → acceptance criteria`.

Do not implement it merely to complete a roadmap.

## Maintenance rule

Maintenance is event-driven. Follow `methodology/maintenance.md` and update only records whose truth changed. Repository maintenance is normally an assistant responsibility.
