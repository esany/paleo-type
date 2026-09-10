# #141 same-source visual-comparanda retrieval spike — 2026-09-10

## Status and authority

This is a bounded **research-support evaluation record**, not a diplomatic-reading owner, palaeographic lexicon, same-hand register, Project-status owner or methodology owner.

The active scholarly owner remains #123 and the scholarly cursor remains F1. F1 pixel work is not part of this spike. No diplomatic reading is changed here, including `62r-L19 = ... 80 wolff ...`.

The first-run pool is strictly the canonical Reg. Ii 5 Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`, fol. 55v–66v / PDF pp. 2–24. No Reg. Ii 4/G4, external witness, lexicon/genre resource or HTR output is admitted.

## Question

Can a very small, text-free, explicitly activated visual-retrieval helper return a small ranked set of **same-source graphical comparanda** that makes a useful palaeographic discriminator easier to formulate than repeated manual browsing, while keeping reading authority at the target graph?

The experiment distinguishes:

```text
pool available
≠ pool activated
≠ crop returned
≠ crop scholarly-inspected
≠ comparator accepted
≠ reading promoted
```

Similarity rank is technical metadata only.

## Prototype

Helper: `tools/regii5_visual_retrieval.py`

The prototype deliberately uses a simple baseline rather than an embedding/index platform:

- exact caller-selected target rectangle from a rendered Reg. Ii 5 page;
- full same-source render pool only after explicit `--activate-same-source-pool`;
- raw grayscale OpenCV `matchTemplate` with `TM_CCOEFF_NORMED`;
- local non-maximum suppression;
- target self-match excluded;
- output contains Source/File/folio/PDF-page/crop coordinates, render SHA, score/rank and candidate-state flags;
- output contains **no candidate word/text** and loads no diplomatic reading owner;
- no same-hand/scribe inference;
- no comparator acceptance or reading promotion by the helper.

The helper verifies the supplied local source File against canonical File SHA before retrieval and derives the allowed PDF-page pool from the canonical Reg. Ii 5 crosswalk.

### Local software used for the spike

- source File SHA-256: `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f` — verified against `corpus/files.tsv`;
- rendering: repository PDF render helper, `pdfium`, 180 dpi, PDF pp. 2–24;
- local `pypdfium2`: 5.8.0;
- OpenCV Python package: 4.13.0.92, installed package metadata reports Apache-2.0;
- NumPy: 2.3.5;
- retrieval method identifier: `opencv.matchTemplate/TM_CCOEFF_NORMED/raw-grayscale/v1`.

180 dpi is used only for candidate retrieval. A returned comparator that later becomes consequential palaeographic evidence must be freshly inspected at adequate resolution under the #123 target/comparator rules; this spike does not transfer `VISION-INSPECTABLE` or a scholarly judgement from the retrieval render.

No source image/crop is committed to the repository by this spike. The archival File remains rights-controlled.

## Evaluation metrics

Following the post-#142 refinement in #141, evaluate:

1. **candidate utility per inspected result** — useful discriminatory/recurrence comparanda divided by the explicitly inspected top-k; false or silhouette-only matches remain counted;
2. **cost to first useful discriminator** — machine retrieval runtime plus rank/number of returned candidates inspected before the first useful discriminator. Human inspection wall-clock is not instrumented here and is therefore marked unmeasured rather than estimated.

A useful graphical comparator is not automatically a reading confirmation.

## Run A — recurrent `wolff` control

Target crop is the already-known `wolff` graph in `62r-L19`, used only as a control **after** retrieval, not supplied as retrieval text.

```text
PDF page 15 / fol. 62r
crop x=926 y=1160 w=85 h=55 @ 180 dpi
query pixel SHA-256 = 68ed8f2224630447f2d0df0d2873207459eb7d65676b6acaeb851bb2e6259ddb
```

Machine retrieval runtime: **4.450405 s** for the 23-page same-source pool.

Top five returned locations:

| rank | folio | PDF page | x,y | score | strict control review |
|---:|---|---:|---|---:|---|
| 1 | 61v | 14 | 679,1288 | 0.689120 | useful exact recurrence control; aligns with canonical 61v-L17 `... wolff ...` |
| 2 | 61v | 14 | 645,401 | 0.679033 | useful exact recurrence control; aligns with canonical 61v-L03 `wolff ...` |
| 3 | 62r | 15 | 702,815 | 0.636263 | useful exact recurrence control; aligns with canonical 62r-L12 `... wolff ...` |
| 4 | 56r | 3 | 611,1185 | 0.631315 | visually similar but not counted as an exact recurrence control |
| 5 | 61v | 14 | 904,401 | 0.596884 | terminal/shape similarity, but not counted as the whole-form recurrence |

Strict exact-recurrence utility among first five inspected: **3/5 = 0.60**. This deliberately under-counts feature-level usefulness rather than converting similarity into lexical identity.

First useful comparator: **rank 1**; one returned crop needed after retrieval. Human inspection wall-clock: **not measured**.

This is a positive control for the narrow claim that exact-shape retrieval can rapidly recover already-known same-source recurrences.

## Run B — recurrent `pfarrer` graphical control

Target crop is taken from the known `pfarrer` graph in `62r-L20`; no query text is supplied to the algorithm.

```text
PDF page 15 / fol. 62r
crop x=991 y=1210 w=130 h=50 @ 180 dpi
query pixel SHA-256 = 9c0b3600cf114d4219a79bfcdbd5fc09431c5dcd227b0fa80f73ac305d01201a
```

Machine retrieval runtime: **4.689285 s**.

Direct visual review of the first five returns found all five to contain a closely matching long-descender/compact-minim graphical configuration suitable as a **feature-level comparator**. This is intentionally not persisted as five new lexical readings. A canonical same-source `pfarrern` control is also returned within the top ten at fol. 61v / PDF p. 14, x=732 y=1016 (rank 8), consistent with the existing 61v-L12 reading.

Feature-level candidate utility among first five inspected: **5/5 = 1.00**. This metric means “useful to compare the target graph”, not “five independently proven occurrences of the same word”.

First useful graphical comparator: **rank 1**. Human inspection wall-clock: **not measured**.

## Run C — adversarial `80/So` sign-shape query

The target crop isolates only the disputed small sign sequence at `62r-L19`; the retrieval engine receives no `80` or `So` label.

```text
PDF page 15 / fol. 62r
crop x=856 y=1168 w=45 h=42 @ 180 dpi
query pixel SHA-256 = 6dbad460738d345c40c411f3b5574a1887bc5ff6588dc5d020d820ba6faf2312
```

Machine retrieval runtime: **5.093760 s**.

The top ten contain multiple close loop-plus-round-form matches. Their value is mixed:

- several are merely shape-near and do not by themselves distinguish numeral from letter use;
- rank 3 (fol. 58r / PDF p. 7, x=1000 y=1552) places the query-like loop in a plainly numeral-like two-character context and is useful for constructing a numeral-side comparator question;
- at least two further top-ten returns place a related loop in word-continuation/letter-like contexts, giving an opposing graphical-use class to inspect;
- therefore at least **3/10 = 0.30** of the first ten inspected provide a genuinely contrastive context rather than only silhouette similarity.

First contrastive discriminator-bearing return: **rank 3**; three returned crops needed after retrieval. Human inspection wall-clock: **not measured**.

Crucially, the already-known same-page `62r-L24` initial `So` is **not** recovered in the top 100 by this exact-template baseline. A local search around that known locus gives a score of about `0.38679`, below the top-100 retained-match threshold of about `0.50361` in this run.

This is a useful negative result: exact template matching is **not allograph-robust enough** to serve as the sole visual generator for the `80/So` problem. It can expose competing graphical contexts, but it must not be treated as an exhaustive form search.

No `80/So` adjudication is performed here. The current TSV remains unchanged.

## Context / process cost observation

The retrieval result itself is small metadata: the compact top-10 JSON outputs for these runs were approximately 5.8 KB each. Actual scholarly inspection additionally requires the target crop and returned candidate crops; image-token/cost equivalence is not estimated here.

For the two recurrent-form controls, the first useful visual comparator appeared at rank 1 after about 4.5–4.7 s local retrieval. For the adversarial sign query, a contrastive contextual comparator appeared by rank 3 after about 5.1 s retrieval.

This supports the user's proposed metric `time/context cost until first useful discriminator`, while keeping the uninstrumented human wall-clock explicitly separate.

## False-match / limitation analysis

Observed limitations of this v1 baseline:

- exact pixel/template similarity strongly favors near-repeated shapes and is sensitive to allographic deformation;
- same Source does not imply same hand, and this helper does not attempt hand attribution;
- common strokes/background/layout can create silhouette-like false matches;
- the returned coordinates are candidate locators, not line readings;
- 180-dpi discovery images are not a substitute for high-resolution source inspection;
- absence from top-k is not evidence that a comparator does not exist;
- the `62r-L24 So` miss demonstrates that an important viable comparator can rank outside a useful exact-template search.

No vector database, embedding index, segmentation model or persistent candidate store is justified by this one run.

## Decision

**KEEP, narrowly, as Generator A baseline; do not promote it into a general palaeographic retrieval system.**

Reason:

- the helper materially reduces manual browsing for recurrent graphical forms (`wolff`, `pfarrer` controls);
- it can surface contrastive visual contexts for a difficult sign query without generating text;
- candidate selection is explicit and same-source only;
- scores/ranks remain technical and no reading authority moves into the tool;
- the `So` miss exposes a clear, bounded failure mode rather than encouraging platform expansion.

For Phase 2, this is enough to compare against an independent Generator B (#140 HTR). Do **not** first build embeddings or a more elaborate visual index. If #140 and the later F1 real test show that exact-template retrieval is too brittle for the problem classes that matter, #141 can remain a documented narrow baseline rather than grow into infrastructure.

## Hand-off

The next support experiment is #140: one local/OSS HTR channel against comparable known controls/challenges, preserving the same separation between generator availability, explicit activation, returned candidates, scholarly adjudication and reading promotion.

After #140, compare Generator A and B by candidate utility and cost to first useful discriminator before any F1 real test.

F1 remains untouched at this checkpoint.