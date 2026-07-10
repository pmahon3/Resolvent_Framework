# verification/ — worksheets supporting the OML descent survey

*Working/verification artifacts for `../oml_onboarding.tex` (the standing OML
descent problem-statement). After the 2026-06-11 archive sweep, the files here
support either a **still-open** question or a **settled-reference** fact — the
worksheets specific to the now-dead **L_MO₂ inhabitation lead** were moved to
`../../archive/oml_descent_inhabitation_dead/`.*

## What's here

**Live-relevant** (bear on the open Q1/structural or point-free classification
questions — see the survey §6):
- `bell_synthesis.md`, `bell_deepresearch_partial.json` — Bell ↔ σ-additive-OML;
  confirm the finitary extension axis does NOT touch the σ-additive descent axis
  (Q1 gap is real). (The self-closed `RESUME_bell_research.md` → archived
  `notes/archive/RESUME_bell_research_closed.md`, 2026-07-10; content absorbed
  into `bell_synthesis.md`.)
- `gunji_pushout_check.py` — Gunji et al. Prop 8 FALSE as stated (verdict used as
  `kill.gunji_dropped` in `paper_ii_taxonomy.json` and the large-cardinal bounds
  note). Added to inventory 2026-07-10.
- `mb_primeness_check.md` — McDonald–Bimbó duality / σ-primeness; PR_dual vs
  PR_lattice nesting is not free.
- `meagre_vs_measure_check.md` — meagre vs measure route on the OML dual; ends on
  the explicit open Q1 sub-problem.
- `pr_dual_inhabitation.py` — PR_dual inhabitation on finite non-distributive OML.

**Settled-reference** (closed extension-axis records; kept for reference):
- `lh_singular_dichotomy.md`, `lh_singular_finite_obstruction.{md,py}`,
  `lh_infinite_extension.py`, `mo3_extension.py` — the L(H) no-state-extends
  results (finite n=4 obstruction; clustering argument).
- `singular_defect_tie_check.md` — bridge: singular-extension residue vs descent
  defect are disjoint objects.

**Foundational** (general facts, referenced by both dead and live work):
- `verify_mo2_state.py` — MO₂ has a genuine state that is not a homomorphism.
- `concrete_meetzero_vs_orthogonal.py` — refutes "concrete ⟹ meet-zero =
  orthogonal" (MO₂ counterexample).
- `mo3_extension.py` — MO₃ computation; also confirms (this session) that MO₃ is
  NON-contextual (dispersion-free states = all 8 cube vertices ⇒ hull = whole cube),
  the basis for "non-distributivity ≠ contextuality" in the survey figure.

**Prior-art / leads (the 2026-06-19/20/21 external-deep-research cycle):**
- `../sigma_essential_prior_art_verdict.md` *(in the parent `open_questions/`, not here)*
  — hostile prior-art verdict: NOT plainly open; settled NEGATIVELY in the
  Polish-representable case (Derr–Williamson 2023 via Maharam 1972 §8); residue =
  non-Polish-representability = the σ-LS wall. CONVERGED, primary-source adjudicated.
  Authoritative for the current verdict.
- `topos_route_read_2026-06-19.md` — topos/Bohrification route: same-wall-with-machinery
  (σ-additivity on a distributive object / per-context Boolean blocks).
- `residue_attack_leads.md` — leads from the attack-the-problem deep-research + the
  construction push: the flawed Riesz reduction (FLAGGED — S_df^σ-not-compact), the
  descriptive-tameness lever (Bishop–de Leeuw/MacGibbon, UNVERIFIED), the operational
  "off-center = non-central Boolean subalgebra" reframing, the Reyes Spec-functor
  citation. Research leads, NOT survey material; verdict UNMOVED.

## Archived (dead L_MO₂ inhabitation lead)

`beta_swap_worksheet.{md,tex,pdf}`, `beta_swap_finite_hinge.py`,
`inhabitation_check.md`, `navara_separation_check.py`, `l2_states.py`,
`diag_hom.py` → `../../archive/oml_descent_inhabitation_dead/` (see its README).
