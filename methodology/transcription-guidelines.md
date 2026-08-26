# Transcription guidelines

## Aim

Create a conservative working transcription close enough to the manuscript to remain auditable, while avoiding unnecessary diplomatic complexity.

## Rules

- Preserve historical spelling in the `reading` field.
- Preserve physical line IDs; do not silently reflow source lines in the working data.
- Use `/` only when a visible separator is being represented or when the project explicitly documents that convention.
- Do not silently expand abbreviations. Record expansion separately if needed.
- Do not modernize names inside the reading.
- Do not replace historical numerals, currency or measure signs with interpreted values until the sign has been identified.
- Use `alternatives` for graphically viable competing readings.
- Use `unresolved` status rather than invented completion.
- Record uncertain token spans as compact local problems; avoid replacing whole lines with vague ellipses when visible graphemes can be preserved.

## Minimal line schema

TSV columns:

`page_id  line_id  region  reading  status  alternatives  evidence_note`

The schema is deliberately small. Add columns only when repeated work proves they are needed.

## Confidence language

Avoid pseudo-precision percentages. Use evidence-bearing statuses and explain the reason. “Working because two same-hand parallels support the `ff` form” is more useful than “90% confident”.

## Normalization

Normalization belongs outside the transcription TSV unless a concrete edition output needs it. A normalized `Gräfendorf` must never overwrite a manuscript reading such as `grevendorff`.
