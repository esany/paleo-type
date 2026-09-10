# #140 local HTR candidate-generator spike — 2026-09-10

## Status and authority

This is a bounded **research-support evaluation record**, not a diplomatic-reading owner, Project-status owner or methodology owner.

The active scholarly owner remains #123. F1 is deliberately untouched. No diplomatic TSV row, STATUS, source relation or gate is changed by this benchmark.

Generator B is tested in isolation after completed #141 Generator A. No Reg. Ii 4/G4, lexicon/genre resource, cloud HTR service or A+B combination is admitted into this run.

The benchmark question is not whether HTR produces fluent transcription. It is whether one explicitly activated local HTR model helps produce the **next graphically testable scholarly question** at a reasonable cost.

## Epistemic order and anti-hindsight rule

For known controls the intended order is:

```text
raw HTR output
→ graph question/discriminator derivable from raw output
→ direct target-pixel check
→ only then control-reading comparison
```

The greedy raw output is therefore preserved verbatim below. Character confidence is used only as a **mechanical attention flag**, not as evidence or calibrated scholarly confidence. For this spike, a non-space output character with model confidence `< 0.75` is flagged before the control comparison. A flagged position can suggest where to ask a graphical question; it cannot decide the answer.

A useful discriminator must still survive direct target inspection. Fluent wording is not rewarded merely because it looks historically plausible. Fragmentary graph sequences can be more useful than a fluent but unsupported word.

### Blinding limitation

The execution order is procedurally separated, but this run is **not claimed as cognitively blinded**: the executing research context had prior access to the repository's known control readings. The immutable raw model output and the predeclared `<0.75` attention rule reduce post-hoc scoring freedom, but they are not a substitute for an independently blinded observer. Any later strict blinded benchmark must use a fresh context that has not seen the control owner before scoring.

## Source, model and local execution

Canonical source File:

- Source: `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`
- File: `FILE-REG-II-5-00000129-EXCERPT`
- source File SHA-256: `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f` — locally reverified before HTR
- rights remain controlled; no manuscript image was uploaded to an external HTR service

Generator B:

- Kraken `7.1.1` — Apache-2.0 software license
- model: PP-OCRv6 small multilingual handwritten/printed text recognition base model
- canonical release: Zenodo DOI `10.5281/zenodo.21788405`
- model license: Apache-2.0
- model file: `small.safetensors`
- model SHA-256: `3108259779f5abfed3908a1c9eafba64d17e4a2a169368c539ecfeff04c018f3`
- embedded model metadata: recognition task, `PPOCRv6Model`, variant `small`, minimum Kraken `7.0.0`
- PyTorch runtime: `2.10.0+cpu`
- decoding: default greedy CTC output; no language model, lexicon or candidate fusion
- line segmentation: supplied as exact line crops; no segmentation model is evaluated here

References:

- https://zenodo.org/records/21788405
- https://github.com/mittagessen/kraken

### Execution-environment caveat

The first uploaded offline wheelhouse was created on macOS ARM64. Its platform-specific `pyarrow` wheel is not installable in this Linux runtime. Kraken itself and the model can nevertheless execute here because the existing runtime already supplies the inference stack. Two environment-specific import edges were encountered:

1. the generic Kraken loader tries the optional CoreML loader before the safetensors loader and fails here because `coremltools` is absent;
2. Kraken's recognition-task import imports Arrow training/dataset code although Arrow is not used by this inference path.

For this spike only, the safetensors recognition loader was invoked directly and a transient minimal `pyarrow` import stub allowed the unused training-dataset module to import. No Arrow operation was called during inference. This workaround is **not** promoted into repository tooling and should not be mistaken for a supported deployment recipe. A future routine local HTR path would need a clean native installation rather than this execution-context shim.

## Rebuildable image inputs

PDF pages 15–16 were rendered with the repository PDF rendering helper using `pdfium` at 180 dpi for HTR and separately at 600 dpi for target inspection. The 180-dpi HTR crop rectangle uses `x=320..1375` and a 68-pixel line window around the detected line centre. The 600-dpi inspection crop is the exact `600/180` scale transform of the same rectangle.

No source image or crop is committed to the repository.

| line | PDF page | 180-dpi crop `(x1,y1,x2,y2)` | 180-dpi crop SHA-256 |
|---|---:|---|---|
| `62r-L06` | 15 | `320,504,1375,572` | `73b09e92a7f3b29fa09d4b92f3a5ca13a15de323d26a45b2c4ec74015628d60e` |
| `62r-L09` | 15 | `320,636,1375,704` | `979999afe70ef36165c23cde11dd6f812661c0f7598b705692afbb3d9516cc5f` |
| `62r-L17` | 15 | `320,1041,1375,1109` | `eacc907a56fddb8c2116cfcfd120c9edf47f7c7c5b61ed51b11fd1fea78024a1` |
| `62r-L19` | 15 | `320,1160,1375,1228` | `de561eb155facb26d9963b06fb6a5fd9a1e054ffaab5e1d89827efa61ca449da` |
| `62r-L20` | 15 | `320,1205,1375,1273` | `7559517aa6f96316aa66236e584670f5bacb4a89f2d02de991873ea03811c095` |
| `62r-L23` | 15 | `320,1342,1375,1410` | `01c86ba5a9c50e993b5f27f007ec3291f379073819d6380dcc25652be89f3571` |
| `62v-L11` | 16 | `320,763,1375,831` | `efecf91570c00053f7b6929aaa900307a96c81afb16b021d6026535163966e21` |

## Raw isolated Generator-B runs

Each row below is a separate cold model load plus one line inference. Timings are internal model-load and inference timers and therefore exclude Python import/process-start overhead. Two externally timed representative one-line processes took about `5.08 s` (`62r-L19`) and `5.16 s` (`62r-L23`) wall time in this runtime; this larger figure includes Python/runtime imports.

Median across the seven cold runs:

- model load: `0.929 s`
- line inference: `0.264 s`
- load + inference: `1.195 s`

Human target-inspection wall-clock was not instrumented and is therefore **unmeasured**, not estimated.

| locus / role | raw HTR output | load + inference | mean char confidence | mechanically flagged `<0.75` positions relevant to target |
|---|---|---:|---:|---|
| `62r-L17` known control | `pflege was sans eianndernachar` | `1.157 s` | `0.779` | central `a/n/s` in `sans`; several letters in first token |
| `62r-L19` known + adversarial control | `Vor das pfarholtz, 8o walff van zwenen¬` | `1.182 s` | `0.886` | `8=0.521`; `a` in `walff=0.696` |
| `62r-L20` known control | `dorff im gennszrada dempfarrer` | `1.195 s` | `0.836` | one central `n=0.696`; several `pfarrer` letters |
| `62v-L11` known control | ` acker✳ zu semem steinbruch gemanche` | `1.121 s` | `0.852` | separator symbol; `m` in `semem`; final `gemanche` cluster |
| `62r-L06` unresolved challenge | `emer hufe kanndes vonn hanse taschen,` | `1.197 s` | `0.864` | several line-initial letters; final `n`; target surname itself mostly high-confidence |
| `62r-L09` unresolved challenge | `von hanns happen zu knawen von her` | `1.319 s` | `0.776` | `a/p/p` in `happen`; later `h` |
| `62r-L23` unresolved challenge | `seinemholgz✳ an der togfferleiz gwant` | `1.391 s` | `0.818` | `o/g` in target token; final `z`; neighboring `g` |

The full raw strings above are generator outputs only. They are not diplomatic transcriptions.

## Pre-control target checks and later control comparison

### `62r-L17` — stable-word control (`sonsten`)

**Question derivable before control comparison:** the model itself is unstable in the short central `sans` sequence. Does the target support only an `s`-initial plus round/minim cluster, or does the output preserve a sufficiently specific full graph sequence?

**Target check:** the 600-dpi target supports the `s`-initial and a more articulated internal/terminal structure than raw `sans`; the HTR sequence is not lossless enough to be a strong discriminator on its own.

**Later canonical comparison:** current owner has `pflegen was sonsten ein ander nachbar`. The model does not recover `sonsten` and also collapses later word boundaries.

**Utility:** **borderline / low**. It localizes uncertainty but does not add a sufficiently specific new discriminator.

**Failure character:** grapheme loss plus spacing collapse; not a fluent modernization, but insufficient candidate detail.

### `62r-L19` — `wolff` + adversarial sign control

**Question derivable before control comparison:** two conspicuous model-confidence minima occur exactly in the small two-character sign (`8=0.521`) and the round vowel of `walff` (`a=0.696`). The resulting graphical questions are: numeral-like versus letter-like first graph, and which round vowel graph follows initial `w`?

**Target check:** those are genuinely inspectable ambiguities. The target first graph remains S-/8-like at this stage; the model's `8o` does not settle numeral versus `So`. The word-internal round graph also warrants direct checking rather than trusting `walff`.

**Later canonical comparison:** current owner remains `Von des pfarrholtz / 80 wolff von gemeinen /`. The model gives near-form `walff` rather than `wolff`, and `8o` is neither an exact `80` transcription nor an alternative `So` proposal.

**Utility:** **yes, discriminator localization**, but **no resolution and no `So` complementarity**.

**Failure character:** confusable glyph class plus vowel substitution; the greedy output exposes uncertainty but only one textual path.

### `62r-L20` — longer known lexical control (`gemeinswalde`)

**Question derivable before control comparison:** raw `gennszrada` proposes a concrete long central sequence. Does the target actually support that ordered graph sequence?

**Target check:** no. The target's internal tall/round/minim sequence and later strokes do not support the raw pseudo-word losslessly. The final `pfarrer` portion is much stronger, but that is incidental to the central benchmark target.

**Later canonical comparison:** current owner has `dorff / dem gemeinswalde dem pfarrer`; the central word is not recovered.

**Utility:** **no for the intended central target**.

**Failure character:** fluent-looking pseudo-lexical completion plus word-boundary collapse. This is a high-risk HTR failure because much of the wrong sequence carries moderate/high model confidence.

### `62v-L11` — known longer word-span control (`steinbruch`)

**Question derivable before control comparison:** the raw output sharply supports the central `steinbruch` sequence while confidence falls around the separator, the possessive sequence and the final word. The graph question is therefore whether the central long word is target-supported independently of the degraded surrounding words.

**Target check:** yes. The 600-dpi target directly supports the central `steinbruch` graph sequence; surrounding `semem` and `gemanche` remain visibly imperfect HTR renderings.

**Later canonical comparison:** current owner is `acker / zu seinem steinbruch gemacht`. The model recovers `acker`, `zu` and `steinbruch` strongly but not the entire line.

**Utility:** **yes** for a longer lexical candidate.

**Failure character:** useful central recognition coexisting with punctuation hallucination (`✳`) and local grapheme substitutions. Correct islands must not confer authority on neighboring output.

## Unresolved challenge cases — candidate utility only

These cases have no complete canonical ground truth and are therefore not scored as accuracy.

### `62r-L06`

Raw target-region output ends in `... hanse taschen,`.

Direct target inspection supports an `h`-initial graph for the token after `hanns`; the model's fluent `taschen` begins with a different graph and is not accepted as a viable full candidate. Notably, the model is not strongly uncertain across that lexical output despite the mismatch.

**Utility:** **no**.

**Failure character:** fluent lexical hallucination / overconfident wrong initial. This is more dangerous for scholarship than a visibly fragmentary result.

### `62r-L09`

Raw output gives `... hanns happen ...`, with low confidence concentrated on `a/p/p`.

The target does support an `h`-initial word, while the medial sequence remains difficult. The output therefore yields a bounded testable question of the form `h-[uncertain a/p/p-like cluster]-...` without justifying the whole word `happen`.

**Utility:** **yes, fragment-level only**.

**Failure character:** potentially useful initial/medial grapheme proposal with explicitly unstable core; whole-word promotion would be unjustified.

### `62r-L23`

Raw output gives `... an der togfferleiz gwant`, with low confidence on the `o/g` pair and final `z` of the long target token.

The 600-dpi target visibly contains a long token with paired long-stroke/`ff`-like structure and a medial/tail sequence for which the raw output provides a concrete fragment to test. The whole lexical form `togfferleiz` is not accepted; the useful result is the narrower graph question around the paired long strokes and following `-erlei-`-like sequence.

**Utility:** **yes, fragment-level**.

**Failure character:** useful partial grapheme recovery embedded in an over-specified whole-word envelope.

## Isolated Generator-B result

Do **not** reduce this to a single aggregate HTR score. Across the seven bounded cases:

- clearly useful discriminator/candidate output: `62r-L19`, `62v-L11`, `62r-L09`, `62r-L23`;
- borderline/low utility: `62r-L17`;
- not useful for the intended target: `62r-L20`, `62r-L06`.

The important pattern is problem-type dependent:

| problem type | Generator-B observation |
|---|---|
| stable/recurrent form | mixed: strong on `steinbruch`, weak on `sonsten`, near-form on `wolff` |
| variable/allographic form | not demonstrated as a general strength; fragment-level help appears in unresolved spans |
| number/sign ambiguity | confidence flags the ambiguity but greedy HTR does **not** supply the missing `So` alternative |
| supplied-line segmentation | line segmentation itself not tested; word-boundary collapse still occurs inside recognized lines |
| longer uncertain word span | potentially useful: `62r-L23` produces a testable partial sequence, but with over-specified lexical envelope |
| name-like unresolved span | mixed/risky: `62r-L09` gives a useful unstable fragment; `62r-L06` produces a fluent wrong candidate |

## Failure character is a primary result

The model's most important negative behavior is not simply character error. It sometimes emits **fluent or word-like strings with moderate/high confidence where the target does not support the whole form** (`gennszrada`, `taschen`). Conversely, the most useful challenge outputs are the ones where uncertainty remains visible and a partial graph sequence can be tested (`happen` core, `togfferleiz` core).

For this research use, fragmentary-but-testable output is therefore preferable to fluent unsupported completion.

## Cost and operational burden

Once loaded, line inference is cheap (`~0.22–0.30 s` for these crops). The median load+inference timer is about `1.20 s`. In this execution environment, however, actual cold one-line process wall time is about `5.1 s` because imports/runtime startup dominate.

The initial setup burden was materially higher than Generator A: an offline wheelhouse of about 241 MB plus a ~13 MB model had to be supplied because this runtime has no package/model network access, and the macOS wheelhouse was not platform-complete for Linux. This burden matters in any later keep/drop comparison.

No recurring service cost or manuscript upload was required.

## Post-isolated complementarity check against #141

This comparison is made only **after** the isolated B observations above were recorded.

Generator A's established narrow strength is rapid recovery of near-recurrent same-source shapes; its known failure is allographic robustness, demonstrated by missing the known `62r-L24 So` comparator even in top 100.

Generator B does **not** repair that critical `80/So` failure in this run: it emits `8o`, with low confidence on `8`, but no `So` alternative. Therefore HTR is not justified merely as a fix for A's adversarial weakness.

B does add a different kind of candidate breadth on some longer unresolved word spans: `62r-L23` yields a testable partial grapheme sequence where exact recurrence search is not the natural task. That is genuine potential complementarity, but it comes with a failure class A largely avoids: fluent textual hallucination.

So the observed relationship is not `B > A`:

```text
A: cheap and strong for near-recurrent local shapes; brittle under allographic change
B: can produce useful partial lexical/grapheme hypotheses on longer spans;
   also capable of fluent unsupported completions; did not solve 80/So
```

## Decision

**KEEP CONDITIONALLY as a bounded Generator-B candidate source for the next controlled A-vs-B evaluation; DO NOT integrate HTR into the default Evidence Packet and DO NOT build broader HTR infrastructure from this result.**

Rationale:

- positive: one known long-word control (`steinbruch`) and two unresolved challenge cases (`62r-L09`, `62r-L23`) show that local HTR can add graphically testable candidate material;
- negative: `gemeinswalde` and `62r-L06` demonstrate serious fluent/over-specified failure modes;
- adversarial: the model does not supply the `So` alternative and therefore does not cover Generator A's most important demonstrated failure;
- cost: local inference is fast, but setup/dependency burden is non-trivial in the present execution context;
- authority: all useful outputs remain candidate material with zero diplomatic evidential authority until target return.

This is sufficient to close the isolated #140 spike with a bounded KEEP/conditional decision. It is **not** sufficient to authorize A+B fusion, default HTR activation, a second model, training, or corpus-wide HTR.

## Next hand-off

The next Phase-2 step is a small **problem-type comparison** of the already isolated A and B results using:

- useful-candidate yield;
- cost/rank or amount of material to first useful discriminator;
- failure character;
- complementarity relative to added setup/adjudication cost.

Do not collapse that matrix into one total score. Only if the comparison shows justified complementary value should an A+B trial be admitted.

F1 remains the untouched prospective real test after that comparison.