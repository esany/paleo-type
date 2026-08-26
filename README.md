# paleo-type

Lean, evidence-based workspace for the transparent transcription and scholarly analysis of early modern handwritten sources.

## Purpose

`paleo-type` helps a non-specialist reliably unlock early modern handwritten sources without turning the research task into a software project. It is a general method and lightweight workspace; each source is handled as a separate project.

The first benchmark is the Knau visitation material in ThHStAW, EGA, Reg. Ii 5 (working images 132–135).

## Non-negotiable principles

1. **Evidence before plausibility.** Never turn a plausible completion into a reading.
2. **Separate layers.** Observation, transcription, normalization, historical identification and interpretation are different claims.
3. **Source status is explicit.** A catalogue entry, snippet, review or table of contents is never treated as if the underlying source/full text had been read.
4. **Uncertainty stays visible.** Alternatives and unresolved graphemes are recorded rather than silently resolved.
5. **No AI slop.** Earlier AI output is not evidence. Repetition does not increase confidence. Fluent prose must not hide missing evidence.
6. **Reproducible decisions.** Material revisions are logged with reason and evidence.
7. **Lean by default.** Add tooling only when it shortens the path to a more reliable transcription or interpretation.
8. **Learning feeds back.** Proven project learnings may improve the general method, but project-specific facts never become general palaeographic rules.

## Evidence layers

`OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION`

A later layer may use earlier layers; it must never silently rewrite them.

## Source-status codes

| Code | Meaning |
|---|---|
| P | Primary source actually inspected |
| E | Scholarly edition actually inspected in full text/relevant pages |
| F | Research publication actually inspected in full text/relevant pages |
| K | Catalogue/finding aid/metadata only |
| R | Review only |
| S | Search result/snippet/table of contents only |
| H | Hypothesis/inference, not a source |

Only `P`, `E`, and `F` support claims about content, and only within the passages actually inspected.

## Lean file model

- **Markdown**: rules, status, reasoning, context and learnings.
- **TSV**: line-level transcriptions, source register, palaeographic concordances and decision logs. TSV is human-readable, diffable and spreadsheet-friendly.
- **YAML**: small project configuration/metadata where key-value structure is useful.
- **JSON**: deliberately avoided until machine validation or interchange creates a concrete need.

## Repository structure

```text
methodology/                 General rules that apply to every project
projects/
  ega-reg-ii-5-knau/         First benchmark/source project
    STATUS.md                Exact restart point and next action
    LEARNINGS.md             Project-specific lessons
    project.yml              Minimal project metadata
    sources/                 Source register
    transcription/           Page/line readings
    palaeography/            Empirical hand-specific concordances
    apparatus/               Revisions and adjudication decisions
    research/                Audit of external sources/publications
    context/                 Context kept separate from blind reading
```

## Working cycle

1. Register the source and what was actually inspected.
2. Segment by physical page/region/line.
3. Produce a blind graphematic reading from the image.
4. Record alternatives and unresolved tokens without semantic filling.
5. Build internal comparisons from repeated forms in the same hand.
6. Adjudicate only where evidence warrants it; log substantive changes.
7. Freeze a versioned transcription checkpoint.
8. Only then introduce parallel primary sources, editions and historical context.
9. Keep source-derived facts separate from inference and interpretation.
10. Feed genuinely generalizable lessons back into `methodology/`.

## Current benchmark

The active project is `projects/ega-reg-ii-5-knau/`. Its `STATUS.md` is the canonical restart point. At the current checkpoint, the next task is to collate numerical, monetary and measure notation across image 132 and the upper section of 133 before attempting further semantic reconstruction.

## Definition of useful output

The project succeeds when it produces a transcription and historical working basis that a user can inspect, cite, challenge and reuse. Tooling is secondary. If a proposed feature does not materially improve speed, traceability or correctness, it does not belong in the project yet.
