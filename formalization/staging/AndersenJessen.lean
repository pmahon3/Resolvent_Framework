/-
# Andersen–Jessen, stage two: the thick tower

Goal: a decreasing sequence of THICK subsets of `[0,1]` (full outer measure)
with empty intersection. Feeding it through `QuerySystem.EscapingTower` refutes
observational extension under plain `UpperDirected`.

Staging file: NOT under the lake globs, so `sorry`s here do not touch CI.
Lemmas land in the library only once closed.

Route (Border, *Kolmogorov Extension Problem*, §6–8, after Halmos pp. 68–70):
  A = ℤ + αℤ, α irrational        -- countable dense subgroup
  Bₖ = {n+mα ∈ A : |n| ≥ k, n even}   -- dense, decreasing, ⋂ₖ Bₖ = ∅
  V  = transversal of ℝ ⧸ A       -- Quotient.out'
  Mₖ = V + Bₖ                     -- λ*(E ∩ Mₖ) = λ(E), by Steinhaus
  Xₖ = Mₖ ∩ [0,1]                 -- thick, and Xₖ ↓ ∅
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.RingTheory.Int.Basic
import Mathlib.NumberTheory.Real.Irrational

namespace AndersenJessen

variable (α : ℝ)

/-- `A = ℤ + αℤ`, a countable dense subgroup of `ℝ` when `α` is irrational. -/
def A : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α}

/-- `Bₖ`: the elements of `A` whose integer coordinate is even with `|n| ≥ k`.
Decreasing in `k`, with empty intersection -- this is what eventually forces
`Xₖ ↓ ∅`. -/
def B (k : ℕ) : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α ∧ (k : ℤ) ≤ |n| ∧ Even n}

/-! ### Step 1: the representation is unique (distinctness) -/

/-- If `α` is irrational, `n + mα` determines `n` and `m`. Everything about
`Bₖ ↓ ∅` rests on this: it is what gives each element of `A` a well-defined
integer coordinate. -/
theorem repr_unique (hα : Irrational α) {n m n' m' : ℤ}
    (h : (n : ℝ) + m * α = (n' : ℝ) + m' * α) : n = n' ∧ m = m' := by
  sorry

theorem repr_unique_left (hα : Irrational α) {n m n' m' : ℤ}
    (h : (n : ℝ) + m * α = (n' : ℝ) + m' * α) : n = n' :=
  (repr_unique α hα h).1

/-! ### Step 2: `Bₖ` is decreasing with empty intersection -/

theorem B_antitone : Antitone (B α) := by
  sorry

theorem B_iInter_eq_empty (hα : Irrational α) : (⋂ k : ℕ, B α k) = ∅ := by
  sorry

/-! ### Step 3: closure properties used for density

`Bₖ` is closed under negation and under multiplication by even integers; these
are what let the standard equidistribution argument conclude density from a
single small element. -/

theorem B_neg_mem {k : ℕ} {x : ℝ} (hx : x ∈ B α k) : -x ∈ B α k := by
  sorry

theorem B_even_smul_mem {k : ℕ} {x : ℝ} (j : ℤ) (hj : Even j) (hx : x ∈ B α k) :
    (j : ℝ) * x ∈ B α k := by
  sorry

theorem A_mem_sub {x y : ℝ} (hx : x ∈ A α) (hy : y ∈ A α) : x - y ∈ A α := by
  sorry

theorem B_sub_mem_A {k : ℕ} {x y : ℝ} (hx : x ∈ B α k) (hy : y ∈ B α k) :
    x - y ∈ A α := by
  sorry

/-! ### Step 4: parity separation

`B₀` and `C₀` (odd coordinate) are disjoint. This is the contradiction that
closes Proposition 13: a difference of two `Bₖ` elements has even coordinate,
so it cannot lie in the odd part. -/

/-- The odd half of `A`. -/
def C (k : ℕ) : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α ∧ (k : ℤ) ≤ |n| ∧ ¬ Even n}

theorem B_disjoint_C (hα : Irrational α) : Disjoint (B α 0) (C α 0) := by
  sorry

end AndersenJessen
