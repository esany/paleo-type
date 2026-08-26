# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Scope currently supported

Working material in the conversation consists of images 132–135 from the Reg. Ii 5 complex. The current working hypothesis is that the Knau entry begins on 132 and continues through the beginning of 135, where a new large heading appears. This boundary must remain a **working source observation** until exact folio/entry mapping is rechecked from the images.

## What has been learned reliably enough to continue

- The source contains repeated forms around `Knawe`, `pfarrer/pfarr-`, `wolff`, `von`, land/wood terms and economic obligations.
- The same-hand internal comparison is materially more reliable than whole-word silhouette guessing.
- Numerical/economic notation must be handled as a separate palaeographic subsystem rather than as ordinary running text.
- Earlier chat readings included semantic completion and source-status overstatement; those outputs are not evidence and must not be imported wholesale.

## Current transcription checkpoint

The TSV files preserve the current **working** readings recovered from the chat. They are not a validated edition. Rows that were previously over-smoothed have been downgraded or left unresolved.

Important working strings to recheck from source images before promotion:

- `Knawe`
- `wolff von grevendorff` (historical identification as Gräfendorf is separate)
- `hat ij filial ...`
- `Holtzmarck zu notturfft zu brennen / vnnd zu bawen`
- `pfarrlehen`
- the 132 household/groschen clause
- the 133 clause involving Wolf, descendants, holdings/hufen and peasants
- the 133 `80 ... holtz` notation
- 134 land/use clauses
- 135 opening three lines and boundary to next entry

## Active problem

The largest high-value unresolved block is the **numerical, monetary, grain and measure notation** in the itemized section of image 132 and comparable notation in the upper part of 133.

Do not solve these by semantic expectation.

## NEXT ACTION — canonical restart point

1. Reopen original images 132 and 133.
2. Isolate every occurrence relevant to numerals/money/measures: `i`, `j`, `ij`, arabic digits, `viertel`, `grosch`, `pfennig`, `gelt`, grain terms, measure signs and repeated item markers.
3. Build/update `palaeography/numerals.tsv` from directly inspected occurrences.
4. Compare the six unresolved economic tokens W1–W6 on image 132 against those secure forms.
5. Record each adjudication in `apparatus/decisions.tsv` with evidence and remaining uncertainty.
6. Only after this pass, freeze a coherent transcription checkpoint for 132–135.
7. Then audit direct parallel primary sources/editions. Do not use finding-aid descriptions as text witnesses.

## Stop conditions

Pause and mark `unresolved` rather than infer if:

- the image does not distinguish the graphemes;
- only syntax/context supports the completion;
- a supposed parallel has not actually been inspected;
- the reading depends on a historical identification rather than letter forms.

## User-facing result target

A usable transcription of the Knau entry with visible uncertainty, a compact critical apparatus, and historical commentary in which every substantive claim can be traced to inspected evidence or is explicitly marked as inference.
