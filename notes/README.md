# Notes Index and Conventions

*Consolidation and naming pass - 2026-05-03*

## Purpose

This is the navigation layer for the active future-note system.  The current
notes should not be merged into one master document.  They now serve different
jobs:

- programme notes: orientation and sequencing;
- future notes: technical and conceptual development;
- literature notes: placement and citation scaffolding;
- investigation dossiers: proof-level work on a narrow open problem;
- archive notes: superseded or absorbed material.

When adding new material, prefer updating the note whose role matches the
material.  Create a new note only when the material has a distinct job.

## Naming Conventions

Use predictable paths over clever titles.

Directory conventions:

- directory names are lowercase `snake_case`;
- active multi-note directions live under
  `notes/future/<architecture_layer>/<topic>/`;
- topic-specific literature mirrors the same architecture layer when useful:
  `notes/literature/<architecture_layer>/<topic>/`;
- programme-wide reception reports live under
  `notes/literature/programme_reception/`;
- conceptual scaffolds that are not yet active theorem programmes live under an
  architectural area, usually `notes/conceptual/foundations/`;
- superseded material stays under `notes/archive/`.

Architectural layers:

| Layer | Directory | Meaning |
|---|---|---|
| Foundations | `foundations/` | logic, coherence, CE, Stone/Boolean support, rational-object probes |
| Dynamics and reconstruction | `dynamics_reconstruction/` | Paper II/Paper III bridge, fibre mixing, Lyapunov directions |
| Finite sample | `finite_sample/` | empirical witnesses, rates, observational resolution, interaction/certification |
| Programme reception | `programme_reception/` | field placement, novelty, audience-specific rhetoric |

This is intentionally not a perfect taxonomy.  Some directions are genuinely
cross-layer.  Place a note where its current mathematical work happens, and use
links for secondary affiliations.

File conventions:

- every multi-note active direction has an `index.md` front door;
- filenames inside a topic directory name the role, not the topic again:
  `mathematical_language.md`, `theorem_spec.md`, `failure_modes.md`;
- use `paper_sketch.md` only for exposition-shaped notes, not proof notebooks;
- use `*_lit_review.md` for literature surveys and `claim_map.md` for
  citation/claim discipline;
- use `step_01_...md`, `step_02_...md`, etc. for sequential investigations;
- use `snake_case.md`; avoid dates, spaces, CamelCase, and generated chat titles
  in active filenames;
- keep archived filenames stable unless reviving material into an active note.

Path examples:

- `notes/future/foundations/coherence_completion/index.md`;
- `notes/future/foundations/coherence_completion/mathematical_language.md`;
- `notes/future/finite_sample/observational_resolution/theorem_spec.md`;
- `notes/literature/foundations/coherence_completion/logic_lit_review.md`;
- `notes/literature/programme_reception/novelty_audit.md`.

## Active Clusters

The clusters below are organized by programme architecture first, then by
operational role inside each topic.

### Foundations: Coherence and Completion

Central question:

> When does local consistency fail to force the intended global completion, and
> what extra admissibility condition licenses closure?

Primary notes:

- `notes/future/foundations/coherence_completion/conceptual_schema.md` — conceptual seed and
  schema: consistency, coherence, admissibility, failure modes.
- `notes/future/foundations/coherence_completion/mathematical_language.md` — formal
  language, definitions, theorem templates, and candidate examples.
- `notes/future/foundations/coherence_completion/paper_sketch.md` — exposition/paper-shape
  sketch; not the proof notebook.
- `notes/literature/foundations/coherence_completion/logic_lit_review.md` — mathematical
  logic placement and opportunity map.
- `notes/literature/foundations/coherence_completion/philosophy_lit_review.md` —
  philosophical scaffold, to be compressed or discarded once the mathematical
  path is stable.

Do not merge these.  The clean division is:

| Need | Edit |
|---|---|
| conceptual vocabulary | `notes/future/foundations/coherence_completion/conceptual_schema.md` |
| definitions / lemmas / theorem targets | `notes/future/foundations/coherence_completion/mathematical_language.md` |
| eventual article narrative | `notes/future/foundations/coherence_completion/paper_sketch.md` |
| logic literature placement | `notes/literature/foundations/coherence_completion/logic_lit_review.md` |
| philosophical scaffolding | `notes/literature/foundations/coherence_completion/philosophy_lit_review.md` |

Current mathematical front:

- Strategy D, via Boolean algebra / Stone duality / Radon measure support.
- Possible second example later: fibre mixing in continuous or metric logic.

### Foundations: Strategy D and CE Non-Derivability

Central question:

> Does there exist a non-sigma-complete, non-atomic Boolean algebra admitting no
> sigma-additive probability, in the appropriate strictly-positive/support
> sense?

Primary notes:

- `notes/future/foundations/ce_nonderivability/index.md` — parent overview connecting the
  companion note, ultralimit representation, and Strategy D.
- `papers/paper_i/notes/ultralimit_investigation/strategy_d_dossier.md` —
  active launchpad for the Strategy D investigation.
- `papers/paper_i/notes/ultralimit_investigation/row5_candidate.md` — detailed
  row-5 history, corrections, and hierarchy.
- `papers/paper_i/notes/ultralimit_investigation/stone_geometric_translation.md`
  — Stone-space translation and support geometry.

Consolidation decision:

- Keep `strategy_d_dossier.md` as the entry point.
- Keep `row5_candidate.md` as the historical/detail note.
- Keep `stone_geometric_translation.md` as the dictionary/proof-translation
  note.
- Do not fold these into the coherence notes; Strategy D is a concrete
  subproblem with its own technical trail.

Immediate next tasks:

1. Verify the exact Stone duality equivalence between sigma-completeness and
   basic disconnectedness.
2. Separate "no sigma-additive probability" from "no strictly positive
   sigma-additive probability".
3. Check the set-theoretic topology literature around measure-free compact
   zero-dimensional spaces.

### Finite Sample: Observational Resolution Dimension

Central question:

> Can the exponent in rates of the form \(n^{-s/(2s+D)}\) be read as
> distinguishability growth per unit observational valuation, rather than as
> topological dimension alone?

Primary notes:

- `notes/future/finite_sample/observational_resolution/index.md` — conceptual and
  technical overview.
- `notes/future/finite_sample/observational_resolution/theorem_spec.md` — theorem target and
  proof skeleton.
- `notes/future/finite_sample/observational_resolution/failure_modes.md` — guardrails and
  known ways the idea can overreach.
- `notes/future/finite_sample/observational_resolution/paper_iii_integration.md` — editorial
  boundary for Paper III.
- `notes/literature/finite_sample/observational_resolution/dimension_lit_review.md` —
  literature placement.
- `notes/literature/finite_sample/observational_resolution/claim_map.md` — safe/unsafe claim
  map.

Consolidation decision:

- Keep all six notes.  They are short and role-separated.
- Add only a modest Paper III remark until a theorem is actually proved.
- Use the theorem spec, not the overview, as the source of formal claims.

Immediate next tasks:

1. Decide which entropy \(H\) and valuation \(\Lambda\) are used in the first
   theorem.
2. Prove one clean balanced-partition specialization.
3. Only then decide whether Paper III should include more than a remark.

### Dynamics and Reconstruction: Fibre Mixing Investigation

Central question:

> Is fibre mixing an independent admissibility condition, or can it be derived
> from structural hypotheses already present in the reconstruction framework?

Primary notes:

- `notes/future/dynamics_reconstruction/fibre_mixing/index.md`
- `notes/future/dynamics_reconstruction/fibre_mixing/step_06_derivability.md`
- `notes/future/dynamics_reconstruction/fibre_mixing/step_07_bridge_theorem.md`

Consolidation decision:

- Keep this as its own investigation.
- Use it as the likely second worked example for the coherence/completion
  schema only after the derivability question is settled.

### Foundations: Zeta / Rational Mathematical Objects

Primary note:

- `notes/future/foundations/zeta/observational_question.md`

Role:

- Boundary probe for whether valuation of refinement can be internal to a
  purely mathematical object.
- Philosophically relevant to the open-horizon language, but not yet ready for
  theorem-level integration.

### Conceptual Foundations: Topology from Vanishing Distinction

Primary note:

- `notes/conceptual/foundations/topology_from_vanishing_distinction.md`

Role:

- Conceptual and proto-mathematical scaffold for deriving nearness/topology from
  observational indistinguishability.
- Adjacent to the zeta and future foundational-topology directions.
- Keep separate from the coherence/completion cluster unless it yields a clean
  theorem about completion, admissibility, or failure of fit.

### Programme Reception: General Literature and Reception Reports

Primary notes:

- `notes/literature/programme_reception/historical_placement.md`
- `notes/literature/programme_reception/field_by_field.md`
- `notes/literature/programme_reception/novelty_audit.md`
- `notes/literature/programme_reception/novelty_summary.md`

Role:

- Programme-level positioning across probability, logic, ergodic theory,
  reconstruction, statistics, and philosophy of science.
- Use these for rhetoric discipline, novelty checks, and audience-specific
  presentation choices.
- Do not merge into the newer coherence or observational-resolution literature
  reviews; those are narrower technical scaffolds.

## Programme-Level Notes

- `notes/programme/program_overview.md` — public-facing repository overview and
  submission status.
- `notes/programme/program_synthesis.md` — internal architecture and dependency
  structure.
- `notes/programme/arxiv_prep.md` — submission logistics.
- `notes/programme/lean_flight_log.md` — Lean-specific work log.

These should stay high-level.  They should link to active future notes rather
than absorb their content.

## Archive Policy

`notes/archive/` contains superseded or absorbed material.  These files should
not be edited as active sources unless we intentionally revive a direction.

Important archived clusters:

- `notes/archive/flagship_examples_absorbed.md` — earlier example bank, mostly
  absorbed into the papers and programme notes.
- `notes/archive/interstitial_reframing_superseded.md` — older paper-transition
  architecture.
- `notes/archive/break_reading_superseded.md` — earlier reading plan.
- `notes/archive/fibre_mixing_investigation/` — steps 1-5 of the fibre-mixing
  investigation, superseded by the active `notes/future/dynamics_reconstruction/fibre_mixing/`
  notes.

Keep archived notes as provenance.  If an archived argument becomes active
again, copy the relevant claim into an active note with attribution to the
archive rather than editing the archive in place.

## Consolidation Rule

Before adding material, ask:

1. Is this a theorem/proof target? Put it in the relevant mathematical-language
   or theorem-spec note.
2. Is this a source/literature placement issue? Put it in `notes/literature/`.
3. Is this a philosophical scaffold? Put it in the relevant philosophy note, and
   mark what should eventually be discarded.
4. Is this a live proof investigation? Put it in the narrow investigation
   dossier.
5. Is this a broad orientation claim? Put it in a programme note and link out.

This keeps the notes Claude-compatible and human-readable: short front-door
files, explicit roles, and no hidden dependency on chat history.
