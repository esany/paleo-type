# Workflow

## Goal

Produce a traceable transcription and source-based historical working basis with the least process necessary to keep results reliable.

## Stages

### 0. Register
Record provenance, file/page identifiers, access route, inspection status and source-status code. Preserve enough source identity that substantive work does not depend on recovering a transient chat attachment. Check rights/access constraints before external AI processing where relevant.

### 1. Observe
Record page structure, regions, physical lines, headings, marginalia and obvious numerical/list structures. Do not interpret lexical content unnecessarily.

### 2. Blind read
Transcribe from the image before consulting contextual identifications or external parallels. Preserve historical spelling. Mark unresolved/variant material explicitly.

### 3. Internal palaeographic comparison
Use repeated forms in the same hand/source to test graphemes, abbreviations, numerals and words. Store reusable hand-specific evidence in `palaeography/`.

### 4. Adjudicate
Change a working reading only when evidence improves. Log material revisions and rejected readings. If AI materially shaped a consequential decision, record proportional research provenance as defined in `ai-governance.md`.

### 5. Freeze checkpoint
Create a coherent page/section transcription version before introducing broad historical context. A checkpoint may still contain unresolved tokens.

### 6. External control
Search for direct parallel primary sources and scholarly editions first; research literature second. Audit access level before using content.

### 7. Identify and interpret
Link readings to persons, places, institutions, legal/economic concepts and historical context. Keep these claims separate from the transcription.

### 8. Publish usable result
Produce a readable transcription, uncertainty/apparatus, source audit and concise historical commentary whose claims can be traced. Raise validation to match the consequence of error; consequential claims that remain dependent on unresolved specialist judgement require appropriate independent human review.

### 9. Persist research state
Whenever a work session changed research truth, persist the minimum changed state in its canonical repository records before relying on the result for future continuation. Follow `methodology/maintenance.md`.

In particular:

- changed readings belong in `transcription/` and substantive replacements/rejections in the decision log;
- changed source knowledge belongs in `sources/` or `research/`;
- changed comparison evidence belongs in `palaeography/`;
- changed active problem, scope or next action belongs in `STATUS.md`;
- learned project-specific failure modes belong in `LEARNINGS.md`;
- general method/structure changes belong in their owning methodology/guardrail files and, where needed, the README.

Do not make a future agent recover durable research state from chat.

### 10. Research integrity gate
Before treating a consequential changed result or substantive work block as complete, run the relevant branches of the continuous integrity check in `methodology/quality-and-learning.md`.

The gate tests five things: evidence actually inspected, separation of claim layers, genuine independence of corroboration, persistence of changed research truth, and alignment with the research goal. A consequential unresolved result may pass; an unsupported resolved result may not.

At useful checkpoints, add a small adversarial evidence spot-check of consequential `working` items. Try to falsify them rather than merely confirm repository consistency. Keep this proportional to novelty, observed error and consequence.

## AI governance triggers

Ordinary AI assistance stays lean. Do not create evaluation infrastructure for routine candidate generation, comparison or critique.

A formal evaluation step is triggered when AI/HTR/automation becomes a systematic research method whose outputs materially determine corpus-level findings, such as bulk transcription, classification, entity extraction, coding or quantitative counts. Then follow `methodology/ai-governance.md`: use representative human-checked material, measure relevant errors and failure patterns, document the validated scope and avoid generalizing beyond it.

## Priority rule

At every stage choose the next action with the highest expected reduction of consequential uncertainty per unit effort. Do not spend time building generic tooling while a direct image comparison or source check would answer the question faster.

Validation is also proportional: use the lightest check sufficient for the consequence of being wrong.

## Checkpoint rule

`STATUS.md` is the canonical continuation point. Update it whenever the active task, corpus boundary, major unresolved problem or next action changes.

A valid checkpoint is restartable: another capable agent should be able to continue correctly from the repository without needing the old chat. This does not require duplicating all research detail into `STATUS.md`; it should point to the relevant canonical records and state the exact next action.

## Maintenance rule

Maintenance is event-driven. Follow `methodology/maintenance.md` and update only records whose truth changed. Repository maintenance is normally an assistant responsibility; the user should not be asked to synchronize files or adjudicate specialist questions merely to keep the system coherent.
