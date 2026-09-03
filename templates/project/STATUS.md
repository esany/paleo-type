# STATUS — PROJECT TITLE

Last checkpoint: YYYY-MM-DD

## Research purpose and Project authority

State the scholarly research purpose for which this Project exists and the current owner-grounded Project boundary at the level that cannot be derived. Do not infer Project existence from Source/File/archival structure, `part_of`, upload order, evidence availability or an inherited AI working bundle.

## Documentary Source anchor

State the canonical documentary Source root identified by `project.yml: project_source_id`. This anchor is used for deterministic structural resolution **after Project selection**; it does not create the Project, define its research purpose or choose the current research priority.

## Active scope

State the current bounded working scope. It may be narrower than the documentary Source root and must not silently redefine Project identity.

## Sources used

Reference `source-uses.tsv`. Summarize only what a human needs to understand: the canonical Sources actually used, their project-relative `research_function` values and relevant source-relative loci. Internal/external status is derived from canonical `part_of` relations; canonical Source/File identity remains in `corpus/`.

When a concrete digital file/instance actually supports a use, reference the project-local use-evidence relation. Do not duplicate file identity/checksums or create a second folio truth in STATUS.

## Evidence and preservation state

State what has actually been inspected, at what level, and what remains metadata-only/not inspected/not observable. State whether every central original export used as evidence is actually preserved in the repository (or why preservation is currently blocked). A URL/URN alone is not equivalent to the exact inspected export.

## Generic gate state

Reference `../../methodology/research-gates.md`. Record only this project's current state and concrete gaps.

## Project relations

Reference `../relationships.tsv` only if this Project materially relates to another Project. Historical/source relations belong in `corpus/relationships.tsv`. Project→Source use never auto-creates a Project→Project relation.

## NEXT ACTION — canonical restart point

State one bounded next research action **only when an authorized next action exists**. If none has been selected, state that explicitly rather than inferring one from Source structure, research-function labels, File availability, old scopes or repository consistency.

## Restartability test

A new capable researcher must be able to identify the Project's scholarly purpose/authority basis, its documentary Source anchor, derive structural/internal/external status, identify Project→Source research functions and relevant loci, recover concrete use-evidence and exact source exports/preservation state, understand current gate/activity state and continue from the exact authorized next action—or recognize the explicit absence of one—without old chat.
