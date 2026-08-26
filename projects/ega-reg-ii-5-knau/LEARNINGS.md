# LEARNINGS — Reg. Ii 5 / Knau

This file records project-specific lessons. It is not evidence for manuscript readings.

## L001 — whole-word silhouette guessing caused major errors

Observed failure: early readings such as `welch` versus later `wolff`, and other fluent-looking words, were produced before enough same-hand grapheme evidence existed.

Corrective practice: prefer local grapheme comparison and repeated same-hand forms. Do not promote a word because its silhouette and syntax look plausible.

Generalizable: yes; reflected in `methodology/quality-and-learning.md`.

## L002 — semantic coherence is dangerous during first transcription

Observed failure: incomplete clauses were turned into grammatically coherent historical German, then later treated as if read from the image.

Corrective practice: blind reading first; unresolved spans remain unresolved. Interpretation is a later layer.

Generalizable: yes.

## L003 — historical name knowledge can leak into manuscript spelling

Observed issue: historical `Gräfendorf` and manuscript working forms such as `grevendorff`/variants risked being conflated.

Corrective practice: manuscript reading and historical identification remain separate records.

Generalizable: yes.

## L004 — numerical/economic notation needs its own concordance

Observed issue: itemized income/measure passages were substantially harder than running prose and mixed Roman/Arabic or specialist notation.

Corrective practice: collect numerals, currency and measure signs across pages before interpreting individual tokens.

Generalizable: likely; currently implemented as a project workflow and palaeography table.

## L005 — metadata was overstated as source content

Observed failure: finding-aid/search information about possible parallel volumes was described too strongly before the actual pages were inspected.

Corrective practice: explicit P/E/F/K/R/S/H source status and passage-level audit.

Generalizable: yes.

## L006 — repeated AI readings are not independent confirmation

Observed issue: multiple model passes can reproduce the same contextual bias.

Corrective practice: treat repeated model output as one reader unless evidence source changes (new image detail, same-hand comparison, independent HTR, external primary parallel, human validation).

Generalizable: yes.

## L007 — the project must preserve a restart point

Observed failure: chat-based work repeatedly revisited method and lost the exact next task.

Corrective practice: `STATUS.md` contains one canonical `NEXT ACTION` and is updated when the research state changes.

Generalizable: yes.
