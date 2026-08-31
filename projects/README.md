# Projects — owner-defined research containers

A Source, archival act, protocol, PDF, place focus or AI work bundle does **not** become a Project by inference. The human owner decides whether a Project exists and what its boundary is. Once that decision is made, `project_source_id` records the canonical Source root used to anchor that Project; internal Source structure remains derived from `corpus/relationships.tsv` `part_of` relations.

For the current church-visitation material the owner decision of 2026-08-31 is:

- `ega-reg-ii-3` → `ACT-THHSTAW-EGA-REG-II-3`;
- `ega-reg-ii-4-bd-ii` → `ACT-THHSTAW-EGA-REG-II-4-BD-II`;
- Reg. Ii 5 → `ACT-THHSTAW-EGA-REG-II-5` (currently stored under legacy directory/id `ega-reg-ii-5-knau`; `Knau` is not the owner-defined Project identity).

Initial research may focus on Knau-related material, but further sections may be added. Project-relative research functions are dynamic and must not be inferred from Source identity, `part_of`, project root, upload order or an earlier AI-selected scope.

## Known internal sections/source nodes

These are current Corpus facts, not project-role assignments:

- **Reg. Ii 3** contains at least two separately identified internal Source nodes:
  - `THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V` — *Visitation in Neustadt an der Orla*, fol. 41r–63v;
  - `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r.
- **Reg. Ii 4 Bd. II** currently has the identified internal Ziegenrück Source node `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`, fol. 294r–313r.
- **Reg. Ii 5** currently has the identified internal Ziegenrück Source node `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`, fol. 55v–66v.

Additional sections may be registered as evidence establishes them. Structural membership does not itself assign a research function or priority.

## Historical-state recovery / audit

The old work state was not erased from Git, but part of it ceased to be visible on `main`.

At commit `699fa6eada61db483dfca950193412715d9603a5` the repository contained separate `source-unit` project directories for:

- `projects/ega-reg-ii-3-00000197/`;
- `projects/ega-reg-ii-3-00000235/`;
- `projects/ega-reg-ii-4-bd-ii-00000089/`;
- `projects/ega-reg-ii-5-00000129/`;
- plus the AI-organized `projects/ega-reg-ii-5-knau/` research-scope project.

The source-unit directories were then removed in a sequence of commits titled `Remove source record masquerading as project`. Their Source/File identities and most reusable crosswalk data were moved to `corpus/`, but their separate STATUS surfaces — including dormant/activation state, evidence limits and restart points — were not preserved as equivalent current Project state. This file and the act-level Project STATUS files restore a visible audit path without reinstating the old source-as-project ontology.

Important historical checkpoints:

- `699fa6eada61db483dfca950193412715d9603a5` — merged source-unit/research-scope model, useful as a recovery snapshot;
- `c7273c1a1254e3821bb499fcc9833a3a5791ec16` and adjacent same-message commits — beginning of source-unit Project STATUS/project-file removal;
- `f560dcaef754a8401022c07870513e9c2d9a0401` — later historical-root Project model.

Git history is an audit source, not the current canonical Project model.

## Crosswalk/URN recovery facts

- Reg. Ii 4 Bd. II fol. 306v–309r / export images 667–672 has six page-specific `urn:nbn:...` values in the canonical crosswalk. Those URNs were already present when the Reg. Ii 4 Knau crosswalk was first created and remain preserved.
- The canonical Reg. Ii 5 crosswalk currently has no values in `stable_image_urn`; it preserves folio/export/PDF mapping plus provider derivative/TIFF labels observed in the PDF footer. The earliest repository crosswalk for this export likewise did not contain per-page URNs. If a separate provider/export crosswalk supplied page URNs for Reg. Ii 5, that evidence is not currently preserved in the repository and must be recovered from that source rather than inferred.
- The current Reg. Ii 3 / `00000235` crosswalk has no page URNs; the earlier project crosswalk also lacked them. The `41r–63v` Reg. Ii 3 Source currently has no canonical page crosswalk at all; its historical STATUS explicitly said that a detailed page/folio crosswalk had not yet been curated.

Do not generalize one Source's identifier availability to another.
