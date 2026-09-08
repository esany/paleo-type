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

For every gate claim, make the **evaluated scope/locus explicit**. A gate reached for one bounded locus is not a claim that the whole Source, Project root or archival act has reached that gate.

Keep activity/task completion and scholarly maturity separate. Where useful, use a compact project-specific summary such as:

| Gate/activity | State | Evaluated scope | Meaning / residual limit |
|---|---|---|---|
| G2 | `reached` | exact locus | source representation complete for this locus; unresolved readings remain |
| work package #… | `complete` | exact task | task finished; no automatic higher-gate claim |
| G5 | `not reached` | same edition target | consolidation/validation still outstanding |
| G6 | `not reached` | declared edition scope | no scholarly edition produced yet |

Do not use bare `complete` as a synonym for all of `task complete`, `representation complete`, `reading resolved`, `gate reached` and `edition produced`. State which meaning is intended. Explicit unresolved evidence may remain compatible with a reached gate when `research-gates.md` permits it.

If no owner-selected bounded scholarly scope exists, say that no current gate progression/claim is being activated rather than inferring maturity from Source/File/crosswalk availability alone.

## Project relations

Reference `../relationships.tsv` only if this Project materially relates to another Project. Historical/source relations belong in `corpus/relationships.tsv`. Project→Source use never auto-creates a Project→Project relation.

## NEXT ACTION — canonical restart point

State one bounded next research action **only when an authorized next action exists**. If none has been selected, state that explicitly rather than inferring one from Source structure, research-function labels, File availability, old scopes or repository consistency.

## Restartability test

A new capable researcher must be able to identify the Project's scholarly purpose/authority basis, its documentary Source anchor, derive structural/internal/external status, identify Project→Source research functions and relevant loci, recover concrete use-evidence and exact source exports/preservation state, distinguish gate attainment from work-package completion and residual unresolved evidence, and continue from the exact authorized next action—or recognize the explicit absence of one—without old chat.
