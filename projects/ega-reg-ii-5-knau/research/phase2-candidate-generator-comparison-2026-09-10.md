# Phase-2 candidate-generator comparison — 2026-09-10

## Status and authority

This is a bounded **research-support comparison record** for #150. It is not a diplomatic-reading owner, Project-status owner, methodology owner, HTR/visual-retrieval integration contract, or authority to inspect/adjudicate F1.

The scholarly owner remains #123. The prospective scholarly cursor remains F1 (`62v-L01`–`L06`, with the separately governed surname component at L06 excluded from that cluster decision). F1 pixels are not inspected in this comparison and no canonical reading, STATUS, gate, `project_context.py` contract, Evidence-Packet default, or generic METHOD rule changes here.

Inputs are the already isolated and merged support experiments:

- Generator A: `same-source-visual-retrieval-spike-2026-09-10.md` (#141);
- Generator B: `local-htr-candidate-generator-spike-2026-09-10.md` (#140);
- bounded context/authority baseline: #142/#145.

The comparison asks which generator, for which problem type, improves the **next graphically testable scholarly question per added effort**. It does not ask which tool has the higher generic recognition score.

## Comparison constraints

The isolated experiments have different output modalities:

- A returns ranked same-source crop loci and technical similarity scores, with no text;
- B returns one greedy HTR string plus character confidences for an explicitly supplied line crop.

Therefore `candidate utility per inspected result` is comparable only at the downstream level (did inspection produce a useful graph question/discriminator?), not as a raw-output-count metric. Human inspection wall-clock was not instrumented in either experiment and remains **unmeasured**.

No single aggregate A-vs-B score is constructed.

## Problem-type matrix

| problem type | Generator A — isolated evidence | Generator B — isolated evidence | effort / failure character | comparison disposition |
|---|---|---|---|---|
| **stable / near-recurrent local form** | Strongest demonstrated A class. `wolff`: strict recurrence utility 3/5, first useful result rank 1; `pfarrer`: feature-level utility 5/5, first useful result rank 1. Retrieval ~4.45–4.69 s across the 23-page same-source pool. | Mixed. `62r-L17 sonsten` is low/borderline; `62r-L19 wolff` becomes near-form `walff`; `62v-L11 steinbruch` is strong but is not an exact recurrence-search test. | A failure is mainly silhouette/allograph brittleness; B adds grapheme loss/word-boundary collapse and textual over-specification. B also has materially higher setup burden. | **A PRIMARY / KEEP narrow.** B is not justified as routine second pass for a stable recurrence problem. |
| **variable / allographic form** | Demonstrated weakness: exact-template A misses the known `62r-L24 So` comparator even in top 100 for the adversarial `62r-L19` sign query. | No general allographic strength demonstrated. On the same adversarial locus B emits `8o`, flags the first graph as uncertain, but does not generate `So`. | Both fail the strongest shared allographic/sign adversarial test in different ways. | **NO WINNER; no automatic generator.** Direct palaeographic target work remains primary. Do not build embeddings or a second HTR model merely to erase this negative control. |
| **number / sign ambiguity** | Some exploratory value: at least 3/10 top-ten returns supplied contrastive numeral-like vs letter-like contexts; first contrast-bearing return rank 3 after ~5.09 s. But A did not recover the known `So` control. | Localizes uncertainty: `62r-L19` first graph has low model confidence and output `8o`, but the greedy path does not provide the missing competing class. | A broadens visual comparison classes; B is vulnerable to forcing one textual path. Neither resolves the ambiguity. | **A OPTIONAL for contrastive comparanda; B adds insufficient complementarity here.** Any result remains zero-authority until target return. |
| **segmentation / layout problem** | Requires an exact caller-selected crop; segmentation itself was not solved by A. | Line segmentation was supplied, not evaluated. Word-boundary collapse still occurred inside recognized lines. | Neither isolated run demonstrates a reliable segmentation solution. | **NO GENERATOR DEFAULT.** Establish source-only segmentation/layout anchors first. |
| **longer uncertain lexical / grapheme span** | Not demonstrated as A's natural strength unless a concrete recurring graphical subform is already available to query. Exact-template retrieval can search a crop, but the isolated evidence does not show robust lexical-span discovery. | Genuine added breadth. `62v-L11` recovers the target-supported island `steinbruch`; unresolved `62r-L23` yields a testable partial grapheme sequence. | B's benefit is paired with a serious risk: useful fragments may sit inside fluent, over-specified pseudo-words. Cold process wall time was ~5.1 s per line; setup required ~241 MB offline wheelhouse + ~13 MB model and an execution-context import workaround. | **B CONDITIONAL PRIMARY** when the blind target observation yields a bounded longer span and no exact recurrent-form discriminator. Treat fragments, not fluent whole words, as the useful unit. |
| **name-like unresolved span** | No isolated #141 benchmark establishes a reliable A result for this class, despite recurrence being conceptually available in the source. | Mixed/risky: `62r-L09` gives a useful unstable `h-[a/p/p-like]-...` fragment; `62r-L06` gives fluent wrong `taschen` despite target-supported h-initial morphology. | B can generate a testable fragment but can also produce overconfident lexical hallucination. Person identity remains outside scope. | **NO DEFAULT.** B may be activated only as fragment-level candidate support after a target-defined graph question; whole-word/name acceptance is prohibited. |

## Shared time / context observation

The measured machine latencies are of the same practical order in this execution environment but represent different work:

- A: ~4.45–5.09 s to search the full 23-page same-source pool, then inspect ranked crops; compact top-10 metadata was ~5.8 KB per run;
- B: median internal model-load + inference ~1.20 s, but representative cold one-line process wall time ~5.1 s; then inspect one raw string/attention pattern and return to the target.

Because human inspection time was not instrumented, neither run supports a claim that one generator is globally faster for scholarship. What is supported is narrower:

- A reaches useful same-source recurrence comparanda at rank 1 for its demonstrated strong class;
- B can immediately provide a testable partial sequence for some longer spans, but its setup and adjudication burden is higher and its fluent-error failure mode is scientifically costly.

## Complementarity test

B is **different** from A, but difference alone is not sufficient for KEEP.

The strongest demonstrated complementarity is problem-type specific: B can provide fragment-level lexical/grapheme hypotheses on longer uncertain spans where exact recurrence retrieval is not the natural first task. This justifies retaining B as an explicitly activated conditional source.

The strongest shared adversarial test does **not** show complementarity: neither A nor B supplies the missing `So` comparator/candidate at `62r-L19`. Therefore B is not justified as a generic repair layer for A's allographic weakness.

The additional HTR burden is justified only when the target problem falls inside B's demonstrated useful class. It is not justified as an automatic second opinion on every target.

## Keep / drop / combine decision

### Generator A

**KEEP narrowly.** Use as the primary support tool for compact, target-defined same-source recurrence/shape questions. Its known allographic brittleness remains an explicit ceiling.

### Generator B

**KEEP conditionally.** Use only when a bounded longer lexical/grapheme span lacks a useful exact-recurrence discriminator, or when a target-defined fragment question makes HTR output mechanically inspectable. Preserve raw output. Prefer uncertain/testable fragments over fluent whole-word suggestions. Do not treat model confidence as scholarly confidence.

### A+B

**DO NOT create an automatic A+B fusion or run both generators by default.** The isolated evidence does not justify paying both costs for every problem, and the shared `80/So` adversarial case shows no complementary rescue.

A **sequential conditional escalation** is admissible for the prospective real test only if attribution remains explicit:

1. source-only target observation and problem-type classification are frozen first;
2. activate the predeclared primary generator for that problem type;
3. record its output, useful-discriminator disposition, machine cost and failure character before any second generator is seen;
4. activate the second generator only if the primary result is explicitly `NO_USEFUL_DISCRIMINATOR` and the second generator has a demonstrated relevant strength;
5. record the second generator's **marginal** contribution and added effort separately;
6. return to the target graph before any reading promotion.

This is escalation, not fusion. Candidate material from A and B does not gain authority by agreement.

## Prospective F1 support rule

The comparison supports a problem-type selector, not a universal pipeline:

```text
blind/source-only observation
→ freeze exact target feature + problem type
→ choose zero or one primary generator
    compact recurrence/shape question → A
    bounded longer uncertain grapheme/word span → B (fragment-level)
    segmentation/layout without stable anchor → neither yet
    variable/allographic or sign ambiguity → source-first; A only for contrastive visual contexts
    name-like span → no default; B only for a pre-bounded fragment question
→ freeze primary-generator result/disposition
→ optional second generator only under the explicit escalation rule above
→ target return
→ only then expose/compare current reading owner and adjudicate
```

The final ordering is intentionally stronger than simply compiling an `explore` packet immediately after blind observation: current-reading content should remain withheld until the generator/discriminator result has been frozen for the prospective test. This requires no change to the packet compiler; the caller can remain in `blind` while running an explicitly activated candidate generator.

## Anti-hindsight / fresh-context gate for F1

This comparison **must not execute F1 in the current context**. The present execution context has already seen the canonical `62v.tsv` reading owner during Phase-2 development. Procedural ordering inside the same context would therefore not constitute a credible anti-hindsight prospective test.

A strict F1 run should begin in a genuinely fresh context that has not seen `62v.tsv`, the derived 62v reading, or equivalent target-reading content before the blind observation/candidate stage. That fresh context may read source-contract/crosswalk/File metadata and the #150 selector contract, but must not read the current F1 reading owner until the primary-generator result and target-return observation are frozen.

Because project-level conversation summaries can themselves carry prior reading knowledge, a new chat **outside the existing paleo-type project conversation context** is the safest execution environment for the strict F1 anti-hindsight run.

## Decision

**Phase-2 isolated-generator comparison: PASS, with conditional routing and no automatic A+B.**

The evidence supports complementary *problem-type roles*, not a combined tool stack:

```text
A = recurrence/shape search specialist
B = conditional fragment/long-span candidate generator with fluent-error risk
neither = reliable allograph/sign resolver
```

The next scholarly action remains #123 F1, but only after handing the predeclared selector and anti-hindsight rules to a genuinely fresh execution context and freshly establishing exact File/SHA/crosswalk/p16 `STAGED` + `VISION-INSPECTABLE` readiness there.
