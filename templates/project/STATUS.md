# STATUS — PROJECT TITLE

Last checkpoint: YYYY-MM-DD

## Historical project root

State the historically independent source structure identified by `project.yml: project_source_id`. Do not redefine the project from the current narrow research question.

## Research purpose and active scope

State the scholarly purpose and current bounded working scope within the project root. The active scope may be narrower than the full project source structure.

## Sources used

Reference `source-uses.tsv`. Summarize only what a human needs to understand: the canonical Sources actually used, their project-relative `research_function` values and relevant source-relative loci. Internal/external status is derived from canonical `part_of` relations; canonical Source/File identity remains in `corpus/`.

When a concrete digital file/instance actually supports a use, reference the project-local use-evidence relation. Do not duplicate file identity/checksums or create a second folio truth in STATUS.

## Evidence and preservation state

State what has actually been inspected, at what level, and what remains metadata-only/not inspected/not observable. State whether every central original export used as evidence is actually preserved in the repository (or why preservation is currently blocked). A URL/URN alone is not equivalent to the exact inspected export.

## Generic gate state

Reference `../../methodology/research-gates.md`. Record only this project's current state and concrete gaps.

## Project relations

Reference `../relationships.tsv` only if this historically independent project materially relates to another project. Historical/source relations belong in `corpus/relationships.tsv`. Project→Source use never auto-creates a Project→Project relation.

## NEXT ACTION — canonical restart point

State one bounded next research action.

## Restartability test

A new capable researcher must be able to identify the historical project root, derive structural/internal/external status, identify the Project→Source research functions and relevant loci, recover concrete use-evidence and exact source exports/preservation state, understand current gate/activity state and continue from the exact next action without old chat.
