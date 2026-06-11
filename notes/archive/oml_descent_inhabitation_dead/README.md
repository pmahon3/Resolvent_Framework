# Archived — L_MO₂ descent-inhabitation worksheets (dead lead)

*Archived 2026-06-11. These are the by-hand and computational worksheets that
supported the **L_MO₂ (= L₂) descent-inhabitation lead**, which was killed and
parked on 2026-06-10 by `/audit full`. They are kept for derivation history; none
bears on a live question.*

## Why dead

The lead asked whether L_MO₂ (Navara's stateless-block construction with the
block swapped for state-rich MO₂) is concrete and satisfies the (★) interleaving
condition — which, if so, would have falsified "richness starves concreteness"
and furnished a concrete σ-orthocomplete non-Boolean OML exercising descent. The
audit verdict: L_MO₂ **is** concrete (so the conjecture is false as worded), but
the lead is dead anyway —
- the load-bearing premise was false: V is a **Kalmbach horizontal sum** (glued
  only at {0,1}), not atom-sharing Greechie pasting, so it never destroyed states;
- the result is **trivial** (plain ∏ₙ MO₂ carries the whole bundle); and
- it was **already characterized** — Pták–Pulmannová 1994 (subadditivity, not
  σ-additivity, is the Boolean-forcing property).

Canonical kill record: `../../covered_leads/descent_axis_residue_post_kill.md`.

## Contents

- `beta_swap_worksheet.{md,tex,pdf}` — the by-hand (★)/β-swap closure + hinge +
  finite→limit degeneration derivation.
- `beta_swap_finite_hinge.py` — finite-truncation test of the (★) hinge.
- `inhabitation_check.md` — the inhabitation orientation history (the (★)
  discriminator, the two near-misses, the segregation analysis).
- `navara_separation_check.py` — verifies Navara's *original* non-concreteness.
- `l2_states.py`, `diag_hom.py` — finite-stage state / homomorphism checks on L₂.

## What did NOT come here (still live, in `../../open_questions/verification/`)

The still-open **Q1 / structural** question (Loomis–Sikorski / σ-Stone for a
σ-complete OML) and the **point-free classification** question (L(H)+Gleason as a
point-free non-distributive σ-additive witness; PR_dual vs PR_lattice) are NOT
addressed by these worksheets — their support files (Bell synthesis, MB primeness,
meagre-vs-measure, pr_dual_inhabitation, and the settled extension-axis records)
remain in `open_questions/verification/`. See `open_questions/oml_onboarding.md`
(the standing problem-statement survey, still in open_questions).
