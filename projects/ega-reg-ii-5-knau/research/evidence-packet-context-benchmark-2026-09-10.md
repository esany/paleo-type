# #142 Evidence-Packet context benchmark — 2026-09-10

## Status and authority

This is a bounded **research-support evaluation record**, not a diplomatic-reading owner, Project-status owner, methodology owner, or replacement for `tools/project_context.py`.

It measures the existing neutral Reg. Ii 5 Evidence Packet introduced in PR #144 and narrowed by #145 / PR #146. No manuscript reading, gate state, F1 readiness, candidate-selection permission, or `VISION-INSPECTABLE` claim is created here.

Benchmark baseline before this branch:

- `main`: `6e5fa070cea618f8a974408c2ea36e2f349657c9`
- active scholarly owner remains #123;
- scholarly cursor remains F1; F1 pixel work is not part of this benchmark;
- default packet candidate policy remains `NONE_ACTIVATED`.

## Question

Does the existing bounded packet materially reduce transmitted context relative to the current broad derived Project restart context while preserving the machine-checkable provenance/routing/authority boundaries needed to address the Reg. Ii 5 target?

This is deliberately **not** the stronger question whether the packet is already sufficient for every scholarly judgement. That still requires human/domain review in the actual task context.

## Reproducible measurement

Helper:

```text
python tools/regii5_packet_benchmark.py --line-ref 62r-L19 --phase blind
```

The comparison serializes both derived objects as compact, sorted UTF-8 JSON. No tokenizer dependency was added; token count is therefore explicitly unmeasured rather than estimated.

Concrete green CI measurement:

- PR #147, source-contract run #289 / `34463427040`;
- real-data fixture: `62r-L19`, `blind` phase;
- all benchmark machine-preservation checks: **PASS**.

| Payload | Characters | UTF-8 bytes | Role |
|---|---:|---:|---|
| existing `DERIVED_PROJECT_CONTEXT` | 64,364 | 64,744 | broad Project restart context; not a manuscript-task minimum |
| `canonical_status.text` contained inside that broad context | 39,178 | 39,479 | full STATUS payload copied by current `project_context.py` |
| existing `DERIVED_REGII5_EVIDENCE_PACKET` | 1,773 | 1,778 | bounded Reg. Ii 5 blind-phase task packet |

Derived comparison:

- packet share of broad context: **2.75%**;
- measured byte reduction relative to broad context: **62,966 bytes / 97.25%**;
- STATUS text alone accounts for **60.98%** of the broad derived context bytes in this fixture;
- token count: **not measured** (`NOT_MEASURED_NO_NEW_TOKENIZER_DEPENDENCY`).

These figures are measurements of the current serialized derived objects, not a claim that a real model invocation will save exactly 97.25% of all input tokens. A real research turn may require additional target pixels, neighbours, candidate output or bounded research context.

## Machine-preservation checks

The benchmark verifies for the concrete packet that:

- Project ID matches the broad context;
- canonical Source ID resolves in the broad context;
- canonical File ID resolves in the broad context;
- crosswalk owner resolves in the broad context;
- the packet does not claim `VISION-INSPECTABLE`;
- candidate activation remains explicitly `NONE_ACTIVATED`;
- no candidate source is implicitly exposed;
- full `canonical_status` / `DERIVED_PROJECT_CONTEXT` payload is not embedded;
- no Reg. Ii 4 / G4 / `308r-*` / `308v-*` material is embedded;
- in `blind`, current diplomatic reading remains withheld;
- separate regression coverage confirms that `explore` still requires and freezes caller-supplied observation and remains candidate-neutral.

The first PR-CI attempt (#288 / `34463353727`) failed only because an implementation-guard test incorrectly prohibited the literal string used by the benchmark to *check for* Reg. Ii 4 leakage. The guard was narrowed to actual Reg. Ii 4/G4 implementation dependencies; run #289 is green. This is test correction, not a change to the packet or research scope.

## Candidate-selection boundary

The benchmark keeps the following states conceptually separate:

```text
available generator
≠ activated generator
≠ candidate returned
≠ candidate adjudicated
≠ reading promoted
```

At this checkpoint:

- generator availability is **not inferred by the benchmark**;
- activated generators: none;
- candidates returned: none;
- no candidate adjudication occurs in the blind fixture;
- reading promotion by compiler: impossible.

This is intentional. #142 measures the neutral integration boundary before #141 introduces the first explicitly activated same-source candidate generator.

## Scholarly loss / sufficiency review

The measurement supports a strong **context-reduction** claim, but not automatic scholarly sufficiency. The following remain context-specific and cannot be certified by byte-size comparison or CI:

1. whether omitted context contains a consequential uncertainty or authority fact for the exact scholarly question;
2. whether target pixels are actually staged and vision-inspectable now;
3. whether a future generator is appropriate to activate for this question;
4. whether returned candidates are palaeographically useful;
5. whether any reading is carried by the target graph.

No `project_context.py` contract change is proposed from this measurement. The broad restart context and bounded task packet serve different purposes.

## Decision

**KEEP — as a bounded research-support path, not as a replacement restart contract.**

Reason:

- the measured payload reduction is large on a real canonical Reg. Ii 5 fixture;
- checked Source/File/crosswalk and authority boundaries remain intact;
- the packet does not import STATUS history, Reg. Ii 4/G4, or candidate context automatically;
- no new canonical truth owner is created;
- the remaining sufficiency questions can be tested by the next real support experiment rather than solved through more architecture now.

Do **not** expand the packet pre-emptively. Add only the smallest explicit interface/data needed when a demonstrated generator integration requires it.

## Authorized hand-off within the support experiment

#142's first measurement objective is satisfied well enough to allow the next support experiment:

**#141 — same-source visual comparanda retrieval, Reg. Ii 5 fol. 55v–66v only.**

#141 must remain explicitly activated and must not turn generator availability into automatic packet context. #140 HTR remains after #141 for a comparable second generator. #143 remains outside the critical path.

F1 remains the later real scholarly comparison target; this benchmark does not begin it.
