# AGENTS.md — mandatory research guardrails

These rules apply to every AI-assisted action in this repository.

## Mission

Help the user reach reliable, usable scholarly results from early modern handwritten sources with minimal tooling overhead. The user is not expected to supervise software engineering or historical method; the assistant must make its evidence, uncertainty and method inspectable.

## Hard stops

- Never invent missing text because it makes semantic sense.
- Never promote an earlier model answer to evidence.
- Never call a reading “secure”, “confirmed” or “gold” merely because the same model repeated it.
- Never treat metadata, a finding aid, TOC, abstract, snippet, review or publisher description as a read primary source/full text.
- Never cite a publication for a claim that was not checked in the relevant passage.
- Never let historical identification silently alter the diplomatic/graphematic reading.
- Never silently normalize spelling, names, numerals, currencies or measures in the transcription layer.
- Never hide disagreement between readings; record it.
- Never add infrastructure “for later” without a current research need.

## Required claim separation

Every substantive statement must belong to one of these layers:

1. `OBSERVATION` — visible layout/marks/features without lexical resolution.
2. `READING` — proposed graphematic/lexical transcription.
3. `NORMALIZATION` — modern/expanded form derived from a reading.
4. `IDENTIFICATION` — linkage to a historical person/place/institution/object.
5. `INTERPRETATION` — historical meaning or explanation.

Do not collapse these layers.

## Reading statuses

Use only:

- `observed` — directly visible feature or highly local sign description.
- `working` — current best reading, not independently validated.
- `variant` — two or more graphically viable readings remain.
- `unresolved` — evidence is insufficient for a useful reading.
- `rejected` — an earlier reading failed reinspection/comparison.

Do not use `gold` unless an explicit external validation protocol is later defined and met.

## Source discipline

Use source-status codes from `methodology/evidence-policy.md`. For every external source, record what was actually opened/read and the exact pages/passages when possible.

A source can support only what was actually inspected. A catalogue can establish existence/metadata, not manuscript content. A searchable copy of uncertain provenance must be labeled as such.

## Workflow discipline

Before continuing an existing project:

1. Read its `STATUS.md`.
2. Read relevant rows in `apparatus/decisions.tsv`.
3. Read `LEARNINGS.md` for known failure modes.
4. Continue from `next_action`; do not restart broad exploration unless evidence requires it.

When changing a substantive reading:

1. preserve the prior reading in the decision log;
2. state the new reading;
3. cite the evidence type (image reinspection, intra-hand parallel, external primary parallel, etc.);
4. state what remains uncertain.

## Anti-slop check before committing research output

Ask:

- Did I see the source or am I relying on metadata?
- Is this text actually visible, or am I completing syntax?
- Did context influence a supposedly blind reading?
- Am I overstating confidence because a phrase sounds coherent?
- Can another person trace why this decision was made?
- Does this new file/tool directly accelerate reliable source work?

If any answer is problematic, revise before committing.

## Learning loop

Project-specific lessons go first into the project's `LEARNINGS.md` with an example and corrective rule. Promote a lesson into `methodology/` only after it is demonstrably general across cases or expresses a standard methodological safeguard.
