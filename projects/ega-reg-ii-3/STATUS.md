# STATUS — ThHStAW, EGA, Reg. Ii 3

Last checkpoint: 2026-08-31

## Project authority and root

The human owner has defined Reg. Ii 3 as one Project, anchored at `ACT-THHSTAW-EGA-REG-II-3`. The earlier AI/source-unit model that treated individual records as separate Projects is historical only.

`Knau` is an initial research focus, not the Project identity. Further sections may be added. No current research function or priority is inferred merely from a Source being internal to the act.

## Known internal sections/source nodes

Derived from canonical `part_of` relations:

1. `THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V` — *Visitation in Neustadt an der Orla*, fol. 41r–63v.
2. `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r.

These are structural/internal Source nodes, not fixed project roles. `source-uses.tsv` is intentionally empty until an actual project-relative research function needs to be recorded.

## Recovered prior work state

Historical snapshot `699fa6eada61db483dfca950193412715d9603a5` preserved two separate source-unit STATUS records:

- the 41r–63v export had been inspected and provenance-controlled; it was not activated for full diplomatic transcription and no detailed page/folio crosswalk had yet been curated;
- the 303r–306r income export had been inspected; `Knaw Kirch Einkommen` was localized at fol. 304r / export image 625; the source was not activated for source-wide transcription and was to be read only when a bounded research question required it.

Those source-unit Project files were later removed from `main`; the Source/File facts survive in `corpus/`, while this STATUS restores their work-state history as an explicit audit surface.

## Evidence / crosswalk state

- Exact inspected files are registered in `corpus/files.tsv` as `FILE-REG-II-3-00000197-EXPORT` and `FILE-REG-II-3-00000235-EXPORT`.
- `00000235` has a canonical crosswalk for export images 623–629 / fol. 303r–306r. Historical image 630 remains preserved as adjacent/unresolved context in the crosswalk note rather than being assigned a folio without evidence.
- The 41r–63v Source currently has no canonical page-level crosswalk.
- The repository does not currently preserve page-specific stable URNs for either Reg. Ii 3 section. This is a statement about repository state only; if a provider-side crosswalk supplied such URNs, recover them from that evidence rather than infer them.

## Research/gate state

No new source-research priority is asserted by this project-structure correction. Existing inspected evidence remains valid at the level originally recorded. Initial work may concern Knau-related loci, but the owner may activate other sections later.

## NEXT ACTION — canonical restart point

Do not infer a manuscript task from Project creation, Source order or prior AI roles. When the owner selects the next Reg. Ii 3 research question, activate only the required section/locus and record its project-relative function at that time.

## Restartability

A fresh context can identify one Reg. Ii 3 Project, its two currently known internal sections, their recovered prior work state, exact File provenance, current crosswalk limits and the absence of an owner-selected next manuscript task without recovering old chat.
