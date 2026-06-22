# Next-session prompt — σ-essential descent (the two-hull lifting probe)

*Drop-in prompt for the next working session on the lone open problem. Written
2026-06-22 at the end of the construction-attempt session. Self-contained; the
detail lives in the files it points to.*

---

## Orientation (read these first, in order)

1. `sigma_duality_targets.md` §6–§7 — this session's findings (π–λ block, CE-leak,
   the two-hull relocation + its hedge). **§7's HEDGE block is the live edge.**
2. `[[sigma_essential_construction_attempt]]` memory, "THE POLE" block + Session 9 —
   standing orientation + what's closed. ⚠ **This file is at 39 KB / 40 KB cap.**
   **Before appending any Session-10 block, collapse Sessions 1–5b's SETTLED-FACTS
   SPINE further OR archive oldest verbatim sessions — ASK the user first** (the
   hygiene rule: collapsing discards reasoning-trail detail).
3. `program_overview.md` item 4 + the 2026-06-22 session block — authoritative state.

## The standing guardrails (do not violate)

- **`rem:dw` is STABLE.** The σ-essential cell is EMPTY for Polish/regular-representable
  OMLs (Derr–Williamson). The residue is the non-representable case = the σ-Loomis–
  Sikorski wall. Do NOT reopen or re-adjudicate this; restate its residue only.
- **Exit-B inclination is held OPEN, NOT a verdict.** ~22 reversals on record; the
  failure mode is tidying "no candidate" → "impossible," and (this session) tidying
  open things shut by switching spaces (P(A) vs S_df^σ) or smuggling assumptions
  (meet-closure→Floor, inner-regularity). **Run the red-flag rule:** any positive
  result, first ask *where did the smuggle enter?*
- All novel hand-work flagged `⟦HAND⟧` / `⟦HAND — unverified⟧`; user verifies.

## THE DECISIVE PROBE (lead with this — finite, yes/no)

> **Does `S_df(F) = {s|_F : s ∈ S_df}` for every finite sub-OML `F`?**
> I.e., does every dispersion-free state *on a finite sub-OML* lift to a global
> dispersion-free state on `L`?

Why it's decisive: the two-hull relocation (§7) says a witness is
`w ∈ conv̄(S_df) \ conv̄(S_df^σ)`. The membership `w ∈ conv̄(S_df)` (beyond the
survey's bare `w ∉ conv̄(S_df^σ)`) holds via Hahn–Banach **iff** finite df-states
lift. So:
- **Lifting HOLDS** ⟹ two-hull framing is valid; proceed to the Choquet geometry of
  `conv̄(S_df^σ) ⊊ conv̄(S_df)` (the convex-separation angle — a different toolkit than
  the all-dead lattice constructions).
- **Lifting FAILS** (some finite df-state has no global extension) ⟹ two-hull framing
  is not even a necessary characterization; a witness could sit outside `conv̄(S_df)`
  entirely. That itself is a finding (reshapes the search) and connects to KS/extension.

Either outcome is progress. This is finite combinatorics on sub-OMLs, likely
hand-tractable; check it against `∏ₙMO₂` (lifting should HOLD there — it's segregated)
and against Wright's pentagon (a finite contextual OML — does its df-state structure
lift in a larger σ-complete embedding?).

## Second direction (only if lifting holds)

The convex/Choquet geometry of the two compact hulls: when can `conv̄(S_df^σ)` be a
**strict** closed subset of `conv̄(S_df)`, off-center, for an irreducible concrete
σ-complete OML? `S_df^σ = S_df ∩ ⋂_{block B} O_B` (the landed sharp theorem; principal-
on-each-block). The strictness is exactly the CE-leak (§6): a barycentre charging the
phantoms `cl(S_df^σ)\S_df^σ`. Gate (§7): any escape must be a genuine df-state-set
separation, NOT charge-non-σ-additivity (= the ∏ₙMO₂ death).

## What's CLOSED (do not re-walk)

Faithful σ-tribe (Floor); all three binding modes (coordinatewise→reducible, atom-share→
chain/loop or band, subtractive→Navara/band); the entire band family (Session-8
dichotomy); loops/Greechie/KS-configs (finitely witnessed ⟹ fail σ-essential by
construction); the intrinsic π–λ route (§6). The carrier must be **non-loop,
non-central, non-band**, with contextuality of a **non-finite character** (no finite
contextual sub-OML). = HW Problem 2, untooled.
