/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.DescentWitnessConsistency

/-!
# Closure legs of the descent witness (Rung 3, hand-legs)

Three "hand-legs" that close out the descent-witness argument on top of the
concrete model `M = ℕ → MO₂` of `DescentWitnessConsistency.lean`. Each leg is a
small, self-contained verification feeding the (★) descent statement.

* **Leg (ii)** — the `⊥`-test and the orthogonality-test *localize per
  coordinate* even for arbitrary (union-of-block) supports, not just
  single-block elements: `meet_bot_iff_blockwise`, `ortho_iff_blockwise`.
* **Leg (iii)(a)** — the `MO₂` *cap-at-2* fact: a pairwise-orthogonal triple of
  `MO₂` elements has at least one `⊥` member (`mo2_cap_two`,
  `mo2_pairwise_ortho_one_zero`).
* **Leg (iii)(b)** — *witness-scoped* closure: the witness family `aW` is a
  genuinely infinite **orthogonal** family (`aW_pairwise_ortho`), the
  precondition for (★) being a *descent* statement.

## Main results
* `meet_bot_iff_blockwise`, `ortho_iff_blockwise` — Leg (ii).
* `mo2_cap_two`, `mo2_pairwise_ortho_one_zero` — Leg (iii)(a).
* `aW_pairwise_ortho` — Leg (iii)(b).

All proofs are `decide`/`Pi`-lemma one-liners. **Zero sorry, zero new axioms.**
-/

namespace QuerySystem
namespace ClosureLegs

open MO2
open QuerySystem.ConsistencyModel

-- ===========================================================================
-- §1. Leg (ii): per-coordinate localization for arbitrary supports
-- ===========================================================================

/-- **Leg (ii), `⊥`-test localization.** In the model `M = ℕ → MO₂`, two elements
meet at `⊥` iff they meet at `⊥` blockwise — for *arbitrary* (union-of-block)
supports, not only single-block-supported elements. Just `funext_iff` plus the
coordinatewise `Pi` lemmas (`⊥` is the constant `⊥` function). -/
theorem meet_bot_iff_blockwise (x y : M) :
    x ⊓ y = ⊥ ↔ ∀ n, x n ⊓ y n = ⊥ := by
  rw [funext_iff]
  simp only [Pi.inf_apply, Pi.bot_apply]

/-- **Leg (ii), orthogonality-test localization.** In the model, `x` is
orthogonal to `y` (`x ≤ mOrtho y`) iff this holds blockwise — again for arbitrary
supports. This is exactly the coordinatewise `Pi` order (`Pi.le_def`), since
`(mOrtho y) n = (y n)ᗮ` definitionally. -/
theorem ortho_iff_blockwise (x y : M) :
    x ≤ mOrtho y ↔ ∀ n, x n ≤ (y n)ᗮ := Pi.le_def

-- ===========================================================================
-- §2. Leg (iii)(a): the MO₂ cap-at-2 fact
-- ===========================================================================

/-- **Leg (iii)(a), cap-at-2.** A pairwise-orthogonal triple `x, y, z` of *nonzero*
`MO₂` elements is impossible: `MO₂` admits no orthogonal family of three nonzero
elements (its blocks are 2-dimensional). A finite case-check after reverting the
hypotheses. -/
theorem mo2_cap_two (x y z : MO2)
    (hxy : x ≤ yᗮ) (hyz : y ≤ zᗮ) (hxz : x ≤ zᗮ)
    (hx : x ≠ ⊥) (hy : y ≠ ⊥) (hz : z ≠ ⊥) : False := by
  revert hxy hyz hxz hx hy hz
  cases x <;> cases y <;> cases z <;> decide

/-- **Leg (iii)(a), corollary.** Any pairwise-orthogonal triple in `MO₂` has a
`⊥` member: at most two of `x, y, z` can be nonzero. Immediate from
`mo2_cap_two`. -/
theorem mo2_pairwise_ortho_one_zero (x y z : MO2)
    (hxy : x ≤ yᗮ) (hyz : y ≤ zᗮ) (hxz : x ≤ zᗮ) :
    x = ⊥ ∨ y = ⊥ ∨ z = ⊥ := by
  by_contra h
  push Not at h
  obtain ⟨hx, hy, hz⟩ := h
  exact mo2_cap_two x y z hxy hyz hxz hx hy hz

-- ===========================================================================
-- §3. Leg (iii)(b): witness-scoped closure into the constancy sublogic
-- ===========================================================================

/-- **Leg (iii)(b), witness family is infinitely orthogonal.** The witness family
`aW n` (`a` on block `n`, `⊥` elsewhere) is *pairwise orthogonal*: for `n ≠ m`,
`aW n ≤ mOrtho (aW m)`. Blockwise (via `ortho_iff_blockwise`): at block `k`, the
only failing case `k = n = m` is excluded by `n ≠ m`; the remaining cases are
`a ≤ ⊤`, `⊥ ≤ a'`, `⊥ ≤ ⊤`, all true. This makes `{aW n}` a genuinely **infinite
orthogonal family**, the precondition for (★) being a *descent* statement.

**Closure is witness-scoped.** The family uses singleton blocks `Cₙ = {n}` on
which Navara's constancy clause is vacuous (each block is its own `C`), so the
coordinatewise join `pW = ⨆ₙ b|Cₙ` lands in the sublogic `L₂` automatically; its
block-values are exactly `b` (`model_blockVal_pWitness`). The general-`C`
σ-orthocompleteness of Navara's construction (arbitrary `C ⊆ M`) is the cited
classical result (Navara, PAMS 115, 1992, p. 428) and is axiomatized in
`DescentWitnessInfinite.lean`, not re-proved here. -/
theorem aW_pairwise_ortho (n m : ℕ) (h : n ≠ m) :
    aW n ≤ mOrtho (aW m) := by
  rw [ortho_iff_blockwise]
  intro k
  rcases eq_or_ne k n with hkn | hkn <;> rcases eq_or_ne k m with hkm | hkm
  · exact absurd (hkn.symm.trans hkm) h
  · simp only [aW, if_pos hkn, if_neg hkm]; decide
  · simp only [aW, if_neg hkn, if_pos hkm]; decide
  · simp only [aW, if_neg hkn, if_neg hkm]; decide

end ClosureLegs
end QuerySystem
