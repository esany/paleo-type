# Quality and learning

## Quality gates

Before a reading is used as a comparison anchor:

- it must be visible in an inspected primary image;
- its status and alternatives must be recorded;
- it must not depend solely on historical plausibility;
- if it is important, seek at least one independent same-hand comparison or external primary parallel.

Before research literature affects interpretation:

- the relevant passage must actually have been read;
- source status and page/passage must be logged;
- distinguish the author's claim from our inference.

## Error taxonomy

When useful, classify failures as:

- `silhouette_guess` — whole-word shape guessed without grapheme control;
- `semantic_completion` — syntax/context filled missing signs;
- `context_leakage` — historical knowledge altered blind reading;
- `source_laundering` — metadata/snippet treated as read content;
- `false_consensus` — repeated model outputs treated as independent evidence;
- `normalization_leakage` — modern form substituted for manuscript form;
- `segmentation_error` — wrong line/region boundaries distorted reading;
- `notation_error` — numeral/currency/measure sign read as ordinary text.

## Learning loop

1. Log concrete project failure/correction in `LEARNINGS.md`.
2. State the observed failure mode and corrective practice.
3. Apply it to the current project.
4. Promote it to general methodology only if it is methodologically general, not a source-specific fact.
5. Remove or simplify rules that create overhead without preventing real errors.

The system should become more reliable, not merely larger.
