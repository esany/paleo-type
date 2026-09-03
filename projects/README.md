# Projects — purpose-established research containers

A Source, archival act, protocol, PDF, place focus, upload or AI work bundle does **not** become a Project by inference. A Project exists because a concrete scholarly investigation/research purpose has been established. Once that decision is made, `project_source_id` records the canonical Source used as the Project's documentary anchor; internal Source structure remains derived from `corpus/relationships.tsv` `part_of` relations.

The current Human Owner decision of **2026-09-02** is:

- `ega-reg-ii-3` is the current Project for scholarly work on Reg. Ii 3, anchored to `ACT-THHSTAW-EGA-REG-II-3`;
- `ega-reg-ii-4-bd-ii` is the current Project for scholarly work on Reg. Ii 4 Bd. II, anchored to `ACT-THHSTAW-EGA-REG-II-4-BD-II`;
- `ega-reg-ii-5-knau` is the current Project for scholarly work on Reg. Ii 5, anchored to `ACT-THHSTAW-EGA-REG-II-5`; the legacy directory/id is retained for path continuity and does not make Knau the current research priority.

This present decision does not retroactively certify every earlier repository statement about Project authority. Historical authority claims remain audit evidence; the 2026-09-02 decision is the current forward authority.

Each Project's current purpose and scope are owned by its `project.yml`; gate/restart state and any authorized `NEXT ACTION` are owned by its `STATUS.md`. Project-relative Source functions are owned by `source-uses.tsv`, with exact Project-use→File evidence in `research/use-evidence.tsv` when needed. Do not reconstruct current priority from this orientation file, Source identity, `part_of`, a historic `principal` use or old chat.

## Canonical Source hierarchy for the current visitation material

These are Source/CORPUS facts, not research-role or Project-priority assignments:

1. **ThHStAW, EGA, Reg. Ii 3** — overlying archival act `ACT-THHSTAW-EGA-REG-II-3`
   - `THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V` — *Visitation in Neustadt an der Orla*, fol. 41r–63v;
   - `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r.
2. **ThHStAW, EGA, Reg. Ii 4 Bd. II** — overlying archival act `ACT-THHSTAW-EGA-REG-II-4-BD-II`
   - `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — *Visitation im Amt Ziegenrück*, fol. 294r–313r; Knau passage fol. 306v–309r / export images 667–672.
3. **ThHStAW, EGA, Reg. Ii 5** — overlying archival act `ACT-THHSTAW-EGA-REG-II-5`
   - `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — *Visitation im Amt Ziegenrück*, fol. 55v–66v; a separate transmission described by archival metadata as an extract related to the Reg. Ii 4 Bd. II Ziegenrück record.

The two Ziegenrück records in Reg. Ii 4 Bd. II and Reg. Ii 5 are separate material Sources/witnesses. Textual correspondence or an extract relation does not merge their identity, foliation, image numbering, File provenance or diplomatic readings. The two Reg. Ii 3 records are likewise separate Sources inside the same Reg. Ii 3 act.

Additional sections may be registered as evidence establishes them. Structural membership does not itself assign a research function, create a Project or set a priority.

## Legacy Knau/G2 diplomatic material

The older Knau/G2 material currently preserved under `projects/ega-reg-ii-5-knau/` was created as an AI-organized research/benchmark strand before the present Source/Project separation was stabilized. On 2026-09-02 the owner clarified that this old material is needed primarily for **checking, recovery and methodology validation**, not as the basis for current Source structure.

Direct comparison of the separately supplied Reg. Ii 4 Bd. II and Reg. Ii 5 Ziegenrück PDFs showed that the old diplomatic corpus cannot safely be assigned wholesale to Li 5 from legacy path/page labels alone. The parallel transmissions are close enough that earlier work may contain imported/comparison readings or mixed witness assumptions.

Therefore:

- `projects/ega-reg-ii-5-knau/transcription/132.tsv`–`135.tsv`, related apparatus/palaeography and G2 research records are **legacy verification/recovery evidence**;
- they are not canonical current Li 5 transcription truth;
- witness-specific scientific use requires fresh Source/File/locus verification;
- legacy readings remain preserved and must not be silently reassigned to Li 4 or Li 5 merely because they resemble one witness;
- new diplomatic work starts from the explicitly targeted canonical Source and exact File.

This quarantine is semantic, not destructive: old research history remains inspectable, but it no longer determines current Source identity, Project scope or transcription authority.

## Historical-state recovery / audit

The old work state was not erased from Git, but part of it ceased to be visible on `main` during the earlier model transition.

At commit `699fa6eada61db483dfca950193412715d9603a5` the repository contained separate `source-unit` Project directories for:

- `projects/ega-reg-ii-3-00000197/`;
- `projects/ega-reg-ii-3-00000235/`;
- `projects/ega-reg-ii-4-bd-ii-00000089/`;
- `projects/ega-reg-ii-5-00000129/`;
- plus the AI-organized `projects/ega-reg-ii-5-knau/` research-scope Project.

The source-unit directories were then removed in a sequence of commits titled `Remove source record masquerading as project`. Their Source/File identities and most reusable crosswalk data were moved to `corpus/`, but their separate STATUS surfaces — including dormant/activation state, evidence limits and restart points — were not preserved as equivalent current Project state. The current act-level Project STATUS files recover the consequential historical work state without reinstating source-as-project semantics.

Important historical checkpoints:

- `699fa6eada61db483dfca950193412715d9603a5` — merged source-unit/research-scope model, useful as a recovery snapshot;
- `c7273c1a1254e3821bb499fcc9833a3a5791ec16` and adjacent same-message commits — beginning of source-unit Project STATUS/project-file removal;
- `f560dcaef754a8401022c07870513e9c2d9a0401` — later historical-root Project model;
- `e8a7235bff875bf2c191c96c41638c4095f7ec76` — useful scholarly comparison checkpoint before the investigated later interpretation/authority series, not baseline truth or a rollback target.

Git history is an audit source, not current Project authority.

## Reg. Ii 5 legacy-use migration

The former Reg. Ii 5 `sources/sources.tsv` compatibility register has been loss-checked and migrated. It is no longer an accepted Project source-use owner.

The four preserved historical research functions now live in `projects/ega-reg-ii-5-knau/source-uses.tsv`, with their exact historical File bindings in `projects/ega-reg-ii-5-knau/research/use-evidence.tsv`. Those rows preserve how the historical Knau strand used Sources; they do **not** establish the witness provenance of every line in the legacy diplomatic corpus.

Their historical `active/identified` state is retained as migration evidence without promoting those uses to current Project scope or `NEXT ACTION`. `principal_source_id` is no longer part of the target Project contract.

## Crosswalk/URN recovery facts

- Reg. Ii 4 Bd. II fol. 306v–309r / export images 667–672 has six page-specific `urn:nbn:...` values in the canonical crosswalk. Those URNs were already present when the Reg. Ii 4 Knau crosswalk was first created and remain preserved.
- The canonical Reg. Ii 5 crosswalk currently has no values in `stable_image_urn`; it preserves folio/export/PDF mapping plus provider derivative/TIFF labels observed in the PDF footer. If a separate provider/export crosswalk supplied page URNs for Reg. Ii 5, that evidence is not currently preserved in the repository and must be recovered rather than inferred.
- The current Reg. Ii 3 / `00000235` crosswalk has no page URNs; the `41r–63v` Reg. Ii 3 Source currently has no canonical page crosswalk at all.

Do not generalize one Source's identifier availability, page numbering, readings or work-state to another.
