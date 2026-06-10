/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.OrthomodularMO2

/-!
# The descent witness at finite truncation (Rung 2)

Second rung of the (β)-swap formalization. We build the finite truncation
`L2N N = Fin N → MO₂` (Navara's construction with `MO₂` blocks, restricted to
`N` blocks), give it the coordinatewise orthocomplement, and prove the **star
condition** `(★)` for the explicit witness:

* `p`  := `b` on every block,
* `aᵢ` := `a` on block `i`, `⊥` elsewhere.

`(★)` is `∀ i, p ⊓ aᵢ = ⊥ ∧ ¬ p ≤ aᵢᗮ` — `p` shares no content with any `aᵢ`
yet is orthogonal to none. This is **Path B as Lean ground truth**: the finite
enumeration that, under the coordinatewise (sublogic-of-product) order Navara
uses, settles the hinge in the YES direction.

The order/meet on `Fin N → MO₂` is coordinatewise (`Pi` instances); the
orthocomplement is defined coordinatewise here. Everything reduces to the
single-block fact `MO2.gap`.

## Main definitions
* `L2N N` — the finite truncation `Fin N → MO₂`.
* `Pi.ortho`, witness `p`, family `aFam`.

## Main results
* `star_finite` — `(★)` holds at every finite truncation `N`. **Zero sorry.**
-/

namespace QuerySystem

open MO2

-- ===========================================================================
-- §1. The finite truncation and its coordinatewise orthocomplement
-- ===========================================================================

/-- The finite truncation: functions from `N` blocks to `MO₂`, with the
coordinatewise (product) lattice order from `Pi.instLattice`. -/
abbrev L2N (N : ℕ) := Fin N → MO2

/-- Coordinatewise orthocomplement on the product: `(fᗮ) i = (f i)ᗮ`. -/
def piOrtho {N : ℕ} (f : L2N N) : L2N N := fun i => (f i)ᗮ

@[inherit_doc] postfix:max "ᗮᵖ" => piOrtho

@[simp] lemma piOrtho_apply {N : ℕ} (f : L2N N) (i : Fin N) :
    (fᗮᵖ) i = (f i)ᗮ := rfl

-- ===========================================================================
-- §2. The witness: p = b everywhere, aᵢ = a on block i
-- ===========================================================================

/-- The single element `p`: the atom `b` on every block. -/
def p (N : ℕ) : L2N N := fun _ => MO2.b

/-- The orthogonal family: `aFam i` is `a` on block `i` and `⊥` elsewhere. -/
def aFam {N : ℕ} (i : Fin N) : L2N N := fun j => if j = i then MO2.a else ⊥

@[simp] lemma p_apply {N : ℕ} (j : Fin N) : p N j = MO2.b := rfl

@[simp] lemma aFam_apply_self {N : ℕ} (i : Fin N) : aFam i i = MO2.a := by
  simp [aFam]

lemma aFam_apply_ne {N : ℕ} {i j : Fin N} (h : j ≠ i) : aFam i j = ⊥ := by
  simp [aFam, h]

-- ===========================================================================
-- §3. (★) at finite truncation
-- ===========================================================================

/-- **Fact (1):** `p ⊓ aᵢ = ⊥` — `p` shares no content with `aᵢ`. On block `i`,
`b ⊓ a = ⊥` (the `MO₂` gap); off block `i`, `aᵢ = ⊥`. Coordinatewise. -/
theorem p_inf_aFam {N : ℕ} (i : Fin N) : p N ⊓ aFam i = ⊥ := by
  funext j
  rw [Pi.inf_apply]
  by_cases h : j = i
  · subst h; simp only [p_apply, aFam_apply_self]
    -- b ⊓ a = ⊥ in MO₂ (symmetric gap)
    exact (MO2.gap_symm).1
  · rw [aFam_apply_ne h]; simp

/-- **Fact (2):** `¬ p ≤ aᵢᗮ` — `p` is *not* orthogonal to `aᵢ`. The product
order is coordinatewise (`Pi.le_def`); on block `i`, `aᵢᗮ = aᗮ = a'`, and
`b ≤ a'` is false (the `MO₂` gap). So the coordinate-`i` test already fails. -/
theorem not_p_le_aFam_ortho {N : ℕ} (i : Fin N) : ¬ p N ≤ (aFam i)ᗮᵖ := by
  intro hle
  -- hle is coordinatewise; instantiate at block i
  have hi := hle i
  rw [piOrtho_apply, aFam_apply_self, p_apply] at hi
  -- hi : MO2.b ≤ (MO2.a)ᗮ = a', contradicting the gap
  exact (MO2.gap_symm).2 hi

/-- **(★) at every finite truncation `N`.** For the witness `p` and family
`aFam`, each block `i` has `p ⊓ aᵢ = ⊥` (meet-zero) yet `¬ p ≤ aᵢᗮ` (not
orthogonal). This is the element-vs-family interleaving, holding under the
coordinatewise order — Path B as Lean ground truth. **Zero sorry.** -/
theorem star_finite {N : ℕ} (i : Fin N) :
    p N ⊓ aFam i = ⊥ ∧ ¬ p N ≤ (aFam i)ᗮᵖ :=
  ⟨p_inf_aFam i, not_p_le_aFam_ortho i⟩

/-- The family is genuinely infinite-capable: for any `N`, the witness works at
*every* one of the `N` blocks simultaneously (the quantifier is over all `i`),
so the interleaving is not confined to a single block. -/
theorem star_finite_all {N : ℕ} :
    ∀ i : Fin N, p N ⊓ aFam i = ⊥ ∧ ¬ p N ≤ (aFam i)ᗮᵖ :=
  fun i => star_finite i

end QuerySystem
