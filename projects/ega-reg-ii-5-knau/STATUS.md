# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Scope currently supported

Working material consists of images 132–135 from the Reg. Ii 5 complex. The current working hypothesis is that the Knau entry begins on 132 and continues through the beginning of 135, where a new large heading appears. This boundary remains a **working source observation** until exact folio/entry mapping is rechecked from the images.

## What has been learned reliably enough to continue

- The source contains repeated forms around `Knawe`, `pfarrer/pfarr-`, `wolff`, `von`, land/wood terms and economic obligations.
- The same-hand internal comparison is materially more reliable than whole-word silhouette guessing.
- Numerical/economic notation must be handled as a separate palaeographic subsystem rather than as ordinary running text.
- Earlier chat readings included semantic completion and source-status overstatement; those outputs are not evidence and must not be imported wholesale.
- The first adversarial integrity check proved useful: it promoted one directly visible numeral (`80`) while **downgrading** the exact spelling of the repeated Wolf surname token. Repetition across pages establishes a repeated form, not automatically its exact graphematic reading.

## Current transcription checkpoint

The TSV files preserve current **working/variant/unresolved** readings. They are not a validated edition. The first adversarial check has been persisted in the transcription files and `apparatus/decisions.tsv`.

Important current anchors/limits:

- `Knawe` — working; still to be formally frozen from source.
- `wolff von` — visually supported across repeated occurrences.
- repeated surname-like token after `wolff von` — **variant/unresolved exact spelling**; current candidate strings include `grevendorff`, `greuendorff`, `grefendorff`. Historical identification as Gräfendorf is a separate claim.
- top quantity in `hat ij filial ...` — current working reading `ij`; exact glyph decomposition is not independently validated.
- arabic `1` — directly visible in image 132 economic clauses; surrounding notation is not resolved by that fact.
- arabic `80` — directly reinspected twice in the lower paragraph of image 133 and now `observed` as a numeral form; its unit/meaning remains unresolved.
- `Holtzmarck zu notturfft zu brennen / vnnd zu bawen`, `pfarrlehen`, household/groschen clause, 133 Wolf/descendants/hufen clause, 134 land/use clauses and 135 boundary remain working material requiring later checkpoint control.

## Active problem

The largest high-value unresolved block remains the **numerical, monetary, grain and measure notation** in the itemized section of image 132 and comparable notation in the upper part of 133.

The first notation pass confirmed that W1–W6 are real distinct economic/value tokens or groups, but the internal evidence inspected so far does **not** safely expand them. Do not solve them by semantic expectation.

## FIRST INTEGRITY-CHECK RESULT

The continuous research-integrity routine was applied to consequential anchors before further reconstruction.

Passed/promoted:

- image 133 contains the same clear arabic `80` form twice; numeral form promoted to `observed` only.

Downgraded:

- exact manuscript spelling of the repeated surname token after `wolff von`; prior preference for `grevendorff` was not sufficiently independent from repeated model/context reading. It is now represented as `[surname-token]` with explicit candidates until grapheme-level adjudication.

Preserved unresolved:

- W1–W6 on image 132;
- upper economic passage of 133;
- surrounding units/syntax around the `80` occurrences.

This is a successful integrity check: it changed confidence in both directions rather than merely confirming the repository.

## NEXT ACTION — canonical restart point

1. Continue the notation-first pass on image 132 and upper 133.
2. For W1–W6, record **visible sign structure** before assigning lexical/monetary meaning; do not reuse semantic labels as evidence.
3. Search the currently inspected pages 132–135 for genuinely comparable value/currency/measure signs and update `palaeography/numerals.tsv` only when a visual parallel exists.
4. If internal comparison does not discriminate W1–W6, move to the shortest external control: an actually inspected contemporary/near-contemporary primary parallel or reliable scholarly edition that reproduces the relevant notation. A finding-aid description is not sufficient.
5. Adjudicate each W token separately in `apparatus/decisions.tsv`; `unresolved` is an acceptable result.
6. After the notation block is stable enough, run another small adversarial sample on consequential running-text anchors, then freeze a coherent transcription checkpoint for 132–135.
7. Only after that checkpoint, proceed to historical identification/context and broader parallel-source audit.

## Stop conditions

Pause and mark `unresolved` rather than infer if:

- the image does not distinguish the graphemes/signs;
- only syntax/context supports the completion;
- a supposed parallel has not actually been inspected;
- the reading depends on a historical identification rather than letter/sign forms;
- repeated AI/model readings are the only apparent corroboration.

## User-facing result target

A usable transcription of the Knau entry with visible uncertainty, a compact critical apparatus, and historical commentary in which every substantive claim can be traced to inspected evidence or is explicitly marked as inference.
