# Human-Owner D-016 admission — Source-entry Option C

**Date:** 2026-10-08  
**Status:** `ADMITTED — bounded implementation`  
**Engineering artifact:** `artifact:ENG-A-0120`  
**Decision owner:** D-016 / `methodology/maintenance.md`  
**Current concept:** `artifact:ENG-A-0119`

## Exact Human decision

The Human Owner explicitly authorized:

> **D-016: zugelassen für Option C im in `requirements/source-entry-transition-coverage-concept-2026-10-08.md` dokumentierten Scope einschließlich der dort festgelegten Non-Goals, Acceptance-Kriterien und Loss-Checks. Keine darüber hinausgehende Architektur- oder Semantikerweiterung ist damit autorisiert.**

The referenced historical decision surface existed only in the recovered local Work state. It was
not a shared GitHub artifact. `artifact:ENG-A-0119` is the currentness-corrected shared
reconstruction of that admitted scope against the current repository and current #309/#267/#272
owner state.

This persistence **does not broaden the admission**. Currentness corrections may remove stale
assumptions and repair implementation defects inside the admitted transition/coverage semantics;
they may not introduce a new material architecture, Project/scope semantics, File model or migration.

## Admitted implementation envelope

Within the bounded Option C scope, implementation may:

- create one dedicated `source-entry/` owner for consequential route history and granular
  inspection/coverage state before and after Project routing;
- preserve Source/File identity by reference rather than duplication;
- preserve explicit `CORPUS_ONLY / NO_PROJECT_YET` behavior without Project creation;
- allow later explicit Project binding without rewriting pre-Project coverage;
- preserve inspection domain, locator domain/locus, purpose/depth, relevance, evidence status,
  claim layer, exclusions, unresolved state, continuation boundary and claim ceiling;
- integrate deterministic validation into the existing Source Contract entrypoint;
- use synthetic fixtures for contract verification and the existing Reg. Ii log for a no-migration
  semantic loss check;
- leave owner tables empty until real source-entry state is truthfully created.

## Boundaries retained

This admission does **not** authorize:

- #265 active scholarly-scope representation changes;
- Project purpose/boundary/priority/`NEXT ACTION` inference;
- File/package/rights representation changes;
- migration of Reg. Ii inspection logs;
- a universal workflow engine, event store, graph runtime, page tracker or planner;
- invented Nr. 632 coverage or a fabricated real Corpus-only fixture;
- activation of #266/#268/#269 without their evidence triggers;
- technical PASS being reported as scholarly/domain/specialist/Human acceptance.

A genuinely new material semantic or architecture choice outside this envelope returns to D-016.

## Currentness-specific correction boundary

The recovered local prototype contained stale Nr. 632 routing/rights assumptions and two
implementation defects relevant to the admitted semantics:

1. mutable `current=yes/no` contradicted its own append-only route-history requirement;
2. coverage could validate without an explicit resolved route, leaving the #309 omission case open.

Repairing those defects and retiring Nr. 632 as the Corpus-only acceptance fixture are treated as
currentness/implementation corrections inside the admitted Option C purpose. They do not authorize
additional architecture.

## Claim ceiling

This file persists Human implementation authority only. It is not Source evidence, Project
authority, Project scope, scholarly validation or implementation acceptance.
