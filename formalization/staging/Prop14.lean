/-
# Proposition 14: the trace measure on a thick set

The next step of Andersen–Jessen after the thick tower. If `X ⊆ ℝ` is thick,
then `Σ_X = {E ∩ X : E measurable}` is a σ-algebra on `X` and
`λ_X (E ∩ X) = λ E` is a well-defined σ-additive probability measure.

`AndersenJessen.X_thick` is exactly the hypothesis this consumes.

Statements written 2026-08-22 as the honest test of the prover loop: goals whose
proofs did not exist. Overnight at budget 600 the loop closed **5 of 9**, all
verified by compiling. The five below carrying tactic proofs are its output,
unedited; the four `sorry`s are what it could not reach.

Notably the four it missed include `Thick.volume_eq`, the well-definedness
result that is the mathematical point of Proposition 14 — even though it closed
`Thick.diff_null`, from which `volume_eq` follows in a line or two.
-/
import QuerySystem.AndersenJessen

open MeasureTheory

namespace Prop14

/-- `X` is **thick**: every measurable set disjoint from it is null. -/
def Thick (X : Set ℝ) : Prop :=
  ∀ ⦃E : Set ℝ⦄, MeasurableSet E → E ∩ X = ∅ → volume E = 0

/-- The tower supplies thick sets. -/
theorem thick_X (α : ℝ) (hα : Irrational α) (k : ℕ) :
    Thick (AndersenJessen.X α k) := by
  unfold Prop14.Thick
  exact fun E hE h => AndersenJessen.X_thick α hα k hE h

/-- Two measurable sets with the same trace differ by a null set. -/
theorem Thick.diff_null {X E F : Set ℝ} (hX : Thick X)
    (hE : MeasurableSet E) (hF : MeasurableSet F) (h : E ∩ X = F ∩ X) :
    volume (E \ F) = 0 := by
  have h' := congr_arg (fun S => S ∩ X) h ; have hEF := congrArg (fun S => S \ X) h' ; simp only [Set.inter_comm _ X, Set.inter_assoc, Set.inter_self] at hEF ; aesop (add norm simp [Set.ext_iff, Set.mem_diff, h])

/-- **Well-definedness.** The trace determines the measure. -/
theorem Thick.volume_eq {X E F : Set ℝ} (hX : Thick X)
    (hE : MeasurableSet E) (hF : MeasurableSet F) (h : E ∩ X = F ∩ X) :
    volume E = volume F := by
  -- both differences are null, so both sets have the measure of their overlap
  have h1 : volume (E \ F) = 0 := hX.diff_null hE hF h
  have h2 : volume (F \ E) = 0 := hX.diff_null hF hE h.symm
  have e1 := measure_inter_add_diff (μ := volume) E hF
  have e2 := measure_inter_add_diff (μ := volume) F hE
  rw [h1, add_zero] at e1
  rw [h2, add_zero] at e2
  rw [← e1, ← e2, Set.inter_comm]

/-- Traces of measurable sets are closed under complement within `X`. -/
theorem trace_compl {X E : Set ℝ} :
    X \ (E ∩ X) = Eᶜ ∩ X := by
  aesop

/-- Traces are closed under countable union. -/
theorem trace_iUnion {X : Set ℝ} (E : ℕ → Set ℝ) :
    (⋃ n, E n ∩ X) = (⋃ n, E n) ∩ X := by
  exact?

/-- A thick set meets every measurable set of positive measure. -/
theorem Thick.inter_nonempty {X E : Set ℝ} (hX : Thick X)
    (hE : MeasurableSet E) (hpos : 0 < volume E) : (E ∩ X).Nonempty := by
  by_contra A ; have hX' := hX ; contrapose! hpos ; rw [Set.not_nonempty_iff_eq_empty] at A ; have hm := hE ; simp_all [Thick, volume]

/-- Disjoint traces come from sets whose overlap is null. -/
theorem Thick.disjoint_trace {X E F : Set ℝ} (hX : Thick X)
    (hE : MeasurableSet E) (hF : MeasurableSet F)
    (h : Disjoint (E ∩ X) (F ∩ X)) : volume (E ∩ F) = 0 := by
  have h' := h ; have h'' := h.symm ; rw [Set.disjoint_iff_inter_eq_empty] at h h'' ; clear h' ; have h' := h.symm ; aesop (add simp [Set.ext_iff, Set.mem_inter_iff])

/-- Countable additivity, in the form the trace measure needs: if the traces of
a sequence are pairwise disjoint, the measures add. -/
theorem Thick.volume_iUnion {X : Set ℝ} (hX : Thick X) (E : ℕ → Set ℝ)
    (hE : ∀ n, MeasurableSet (E n))
    (hdisj : Pairwise (fun m n => Disjoint (E m ∩ X) (E n ∩ X))) :
    volume (⋃ n, E n) = ∑' n, volume (E n) := by
  sorry

/-- A measurable set that covers a thick set on `[0,1]` is conull there.

The earlier form of this carried `hsub : X ⊆ Set.Icc 0 1`, which made it
vacuous: `Thick` quantifies over every measurable subset of `ℝ`, so a thick set
confined to `[0,1]` would force `volume (Set.Icc 2 3) = 0`. No `X` satisfies
both hypotheses, and the prover loop "proved" it by finding that contradiction
rather than the intended fact. `hsub` is not needed -- `hEX` already puts
`Set.Icc 0 1 \ E` outside `X`, and it is measurable, so thickness applies. -/
theorem Thick.volume_Icc {X : Set ℝ} (hX : Thick X)
    {E : Set ℝ} (hE : MeasurableSet E) (hEX : Set.Icc 0 1 \ E ⊆ Set.Icc 0 1 \ X) :
    volume (Set.Icc (0:ℝ) 1 \ E) = 0 := by
  refine hX (measurableSet_Icc.diff hE) ?_
  ext x
  simp only [Set.mem_inter_iff, Set.mem_empty_iff_false, iff_false, not_and]
  intro hx hxX
  exact (hEX hx).2 hxX

end Prop14
