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

**Statements written cold; all ten now proved and Lean-checked.** Six came from
the prover loop (three by `exact?`, three by the model). The remaining four --
the two measurability facts, the emptiness fact, and continuity from above --
were done by hand after the loop failed them twice, at budget 400 and again at
1200. Two of those four had the loop's search frontier empty out in seven
seconds, which is the signature of missing vocabulary rather than insufficient
search: `measurableSet_eq_fun` and `MeasurableSet.biInter` close them at once.
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
  intro a b c d h
  unfold Diag at h ⊢
  exact (fun x hx ↦ h x <| le_trans hx c)

/-- Their intersection is the fully constant sequences. -/
theorem Diag_iInter : (⋂ n, Diag n) = {ω : ℕ → ℝ | ∀ i, ω i = ω 0} := by
  ext x
  refine ⟨?_, fun h => ?_⟩
  intro hω i
  by_cases hi : i = 0
  all_goals simp [Set.mem_iInter, Set.mem_setOf_eq] at *
  all_goals tauto

/-- **The key emptiness fact.** If the family shrinks to nothing, no sequence in
the product is constant — so the diagonal cylinders have empty intersection
there. This is what makes the tower escape. -/
theorem pi_inter_diag_eq_empty {Y : ℕ → Set ℝ} (hY : (⋂ k, Y k) = ∅) :
    Pi' Y ∩ (⋂ n, Diag n) = ∅ := by
  ext ω
  simp only [Set.mem_inter_iff, Set.mem_empty_iff_false, iff_false, not_and]
  intro hpi hdiag
  -- a point of every diagonal cylinder is constant, so its common value
  -- lies in every `Y k` -- but that intersection is empty.
  rw [Diag_iInter] at hdiag
  have : ω 0 ∈ ⋂ k, Y k := Set.mem_iInter.mpr fun k => (hdiag k) ▸ hpi k
  rw [hY] at this
  exact this

/-- Coordinate evaluation is measurable. -/
theorem measurable_coord (i : ℕ) : Measurable (fun ω : ℕ → ℝ => ω i) := by
  exact measurable_pi_apply i

/-- Agreement of two coordinates is a measurable condition. -/
theorem measurableSet_eq_coord (i j : ℕ) :
    MeasurableSet {ω : ℕ → ℝ | ω i = ω j} := by
  exact measurableSet_eq_fun (measurable_pi_apply i) (measurable_pi_apply j)

/-- Each diagonal cylinder is measurable, being a finite intersection. -/
theorem measurableSet_Diag (n : ℕ) : MeasurableSet (Diag n) := by
  have : Diag n = ⋂ i ∈ Finset.range (n + 1), {ω : ℕ → ℝ | ω i = ω 0} := by
    ext ω
    simp [Diag]
  rw [this]
  exact MeasurableSet.biInter (Finset.range (n + 1)).countable_toSet
    fun i _ => measurableSet_eq_coord i 0

/-- The diagonal embedding of `ℝ` into sequences is measurable. -/
theorem measurable_const_seq : Measurable (fun x : ℝ => (fun _ : ℕ => x)) := by
  exact measurable_pi_lambda _ fun _ => measurable_id

/-- The diagonal embedding lands in every diagonal cylinder. -/
theorem const_seq_mem_Diag (x : ℝ) (n : ℕ) : (fun _ : ℕ => x) ∈ Diag n := by
  intro i _
  rfl

/-- A sequence in `Diag n` is determined on `[0,n]` by its first coordinate. -/
theorem Diag_eq_of_le {n : ℕ} {ω : ℕ → ℝ} (hω : ω ∈ Diag n) {i j : ℕ}
    (hi : i ≤ n) (hj : j ≤ n) : ω i = ω j := by
  cases n
  all_goals simp_all [Diag]

/-- Continuity from above, in the form the contradiction uses: a probability
measure cannot give every term of an antitone sequence mass one when the
intersection is null. -/
theorem no_mass_one_of_iInter_empty {α : Type*} [MeasurableSpace α]
    (μ : Measure α) [IsProbabilityMeasure μ] (S : ℕ → Set α)
    (hmeas : ∀ n, MeasurableSet (S n)) (hanti : Antitone S)
    (hempty : (⋂ n, S n) = ∅) : ¬ (∀ n, μ (S n) = 1) := by
  intro hone
  have hfin : ∃ i, μ (S i) ≠ ⊤ := ⟨0, by simp [hone 0]⟩
  have htend := tendsto_measure_iInter_atTop (μ := μ)
    (fun n => (hmeas n).nullMeasurableSet) hanti hfin
  rw [hempty, measure_empty] at htend
  -- every term has mass one, so the limit is both 0 and 1
  have hconst : (⇑μ ∘ S) = fun _ : ℕ => (1 : ENNReal) := funext hone
  rw [hconst] at htend
  exact one_ne_zero (tendsto_nhds_unique htend tendsto_const_nhds).symm

end Diagonal
