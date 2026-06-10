> **⚠ SUPERSEDED 2026-06-10 — see `HANDOFF_separation_audit.md`.** The lattice ★
> ATTACK described below is DONE (rungs + hand-legs (ii)/(iii) all Lean-verified,
> 0 sorry). The active frontier moved to the STATE level: L₂ has dispersion-free
> states that aren't homomorphisms — a candidate Type-4 contribution now awaiting
> `/audit full`. This file is retained as the lattice-side audit trail.

# HANDOFF — descent inhabitation, ATTACK phase (2026-06-10)

Everything below is durable + committed; working tree clean. This file is the
single entry point for resuming.

## Where the lead stands

The descent-inhabitation question (does a concrete σ-orthocomplete non-Boolean
OML genuinely *exercise descent*?) flipped from "leans park" to **ATTACK**:

- **Swap fixed as (β)**: MO₂ the primitive atom, Navara's T×S/stateless-S
  scaffold discarded (chosen on programme grounds — genealogy_vision.md
  anti-smuggler: structure must emerge, not be imported).
- **Hinge = YES** (the (★) element-vs-family interleaving holds in L₂). Rests on
  **leg (i), user-verified from Navara p.428**: L₂ is a *sublogic of the
  product* (subset + constancy), order = coordinatewise, NOT a completion ⟹ the
  witness p = ⋁ₙ b|Cₙ transfers and ★ holds.
- This **refutes "richness starves concreteness"**: L₂ is a 2nd (concrete)
  witness alongside L(H).

## What is DONE (committed)

**Lean ★ formalization** — `formalization/QuerySystem/QuerySystem/`, all **0 real
sorry**, builds via `~/.elan/bin/lake build QuerySystem.<Module>`:
| Module | What |
|--------|------|
| `OrthomodularMO2` | Rung 1: `OrthomodularLattice` class (Mathlib has none) + MO₂ + `MO2.gap` |
| `DescentWitnessFinite` | Rung 2: `star_finite` — ★ at every finite `Fin N → MO2` |
| `DescentWitnessInfinite` | Rung 3: `star_infinite` — ★ at ∞, proved on 11 cited Navara-p.428 axioms |
| `DescentWitnessConsistency` | concrete ℕ→MO2 model realizes all axioms ⟹ ★ non-vacuous |

**Worksheets/scripts** (`notes/open_questions/verification/`):
`beta_swap_worksheet.{md,tex,pdf}` (full derivation + leg-(i) confirmation),
`beta_swap_finite_hinge.py` (Path B finite enum), `bell_synthesis.md` +
`bell_deepresearch_partial.json` (Bell↔σ-OML map).

**Survey** `oml_onboarding.{tex,md,pdf}`: Q1/Q2 split, Bell-as-extension-axis
citation (Budroni–Morchio), all committed.

## What is OPEN — the actual next moves

1. **★ is the GATEWAY, not the prize.** ★ proves L₂ *exercises descent* (class
   non-empty / descent-relevant). It does NOT yet give the programme prize:
   a **point-free σ-additive PROBABILITY theory** on L₂. That is Q1 —
   Loomis–Sikorski / σ-Stone representation for L₂; characterize states on L₂;
   does a σ-additive state concentrate on the physical points? This is the
   real ATTACK target and is wide open (no partial construction).

2. **Residual hand-legs** (consistency-tidying, NOT verdict reversals; the
   verdict stands without them): (ii) ⊥ coordinatewise for *union-of-block*
   supports (only single-block checked); (iii) closure Claim 1 (family-cap-at-2,
   `beta_swap_worksheet.md` VERIFY 1).

3. **Optional polish**: Lean files build standalone, NOT wired into the
   `QuerySystem.lean` root (each is its own lib module — fine, but could be
   imported into a root index).

## Token-economy reminders (per [[feedback_token_economy]] memory)

- Lean tactic-debugging → delegate to a subagent with the toolchain, don't
  iterate in main context.
- Literature scans → one sonnet scout, NOT deep-research Workflow.
- `lake build` (not `lake env lean`) to produce oleans so imports resolve.
- `~/.elan/bin/lake` (lake not on PATH); macOS has no `timeout`.

## Key memories
[[oml_descent_inhabitation]] (full lead history + ★-Lean update),
[[formalization_status]] (descent-witness suite table),
[[feedback_token_economy]], [[feedback_verify_by_building]].
