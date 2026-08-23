/-
# The diagonal layer: toward the Andersen–Jessen escaping tower

After Proposition 14 (the trace measure on a thick set) the construction needs
the diagonal cylinders

    Dₙ = { ω : ω₀ = ω₁ = ⋯ = ωₙ }

inside the product of the tower sets. Two facts drive the contradiction:
`Pₙ(Dₙ) = 1` for every `n` (by construction, the measure is a diagonal
pushforward), and `⋂ₙ Dₙ = ∅` on the product — because a sequence with all
coordinates equal has its common value in every `Xₖ`, and `⋂ₖ Xₖ = ∅`.

This file states the second half plus the measurability needed to talk about it.
Sequences are `ℕ → ℝ` with the product σ-algebra, deliberately phrased in
Mathlib vocabulary rather than over the project's own definitions — the prover
loop does markedly better there.

**Statements written cold; the proofs do not exist yet.**
-/
import Mathlib.MeasureTheory.Constructions.Pi
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic

open MeasureTheory

namespace Diagonal

/-- Sequences whose first `n+1` coordinates all agree. -/
def Diag (n : ℕ) : Set (ℕ → ℝ) := {ω | ∀ i ≤ n, ω i = ω 0}

/-- Sequences lying coordinatewise in a given family. -/
def Pi' (Y : ℕ → Set ℝ) : Set (ℕ → ℝ) := {ω | ∀ k, ω k ∈ Y k}

/-- The diagonal cylinders shrink. -/
theorem Diag_antitone : Antitone Diag := by
  sorry

/-- Their intersection is the fully constant sequences. -/
theorem Diag_iInter : (⋂ n, Diag n) = {ω : ℕ → ℝ | ∀ i, ω i = ω 0} := by
  sorry

/-- **The key emptiness fact.** If the family shrinks to nothing, no sequence in
the product is constant — so the diagonal cylinders have empty intersection
there. This is what makes the tower escape. -/
theorem pi_inter_diag_eq_empty {Y : ℕ → Set ℝ} (hY : (⋂ k, Y k) = ∅) :
    Pi' Y ∩ (⋂ n, Diag n) = ∅ := by
  sorry

/-- Coordinate evaluation is measurable. -/
theorem measurable_coord (i : ℕ) : Measurable (fun ω : ℕ → ℝ => ω i) := by
  sorry

/-- Agreement of two coordinates is a measurable condition. -/
theorem measurableSet_eq_coord (i j : ℕ) :
    MeasurableSet {ω : ℕ → ℝ | ω i = ω j} := by
  sorry

/-- Each diagonal cylinder is measurable, being a finite intersection. -/
theorem measurableSet_Diag (n : ℕ) : MeasurableSet (Diag n) := by
  sorry

/-- The diagonal embedding of `ℝ` into sequences is measurable. -/
theorem measurable_const_seq : Measurable (fun x : ℝ => (fun _ : ℕ => x)) := by
  sorry

/-- The diagonal embedding lands in every diagonal cylinder. -/
theorem const_seq_mem_Diag (x : ℝ) (n : ℕ) : (fun _ : ℕ => x) ∈ Diag n := by
  sorry

/-- A sequence in `Diag n` is determined on `[0,n]` by its first coordinate. -/
theorem Diag_eq_of_le {n : ℕ} {ω : ℕ → ℝ} (hω : ω ∈ Diag n) {i j : ℕ}
    (hi : i ≤ n) (hj : j ≤ n) : ω i = ω j := by
  sorry

/-- Continuity from above, in the form the contradiction uses: a probability
measure cannot give every term of an antitone sequence mass one when the
intersection is null. -/
theorem no_mass_one_of_iInter_empty {α : Type*} [MeasurableSpace α]
    (μ : Measure α) [IsProbabilityMeasure μ] (S : ℕ → Set α)
    (hmeas : ∀ n, MeasurableSet (S n)) (hanti : Antitone S)
    (hempty : (⋂ n, S n) = ∅) : ¬ (∀ n, μ (S n) = 1) := by
  sorry

end Diagonal
