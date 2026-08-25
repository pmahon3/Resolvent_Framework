/-
# The trace measure on a thick set (Border, Kolmogorov Extension Problem, Prop. 14)

Unit 1 of `notes/open_questions/aj_tower/SCOPE_trace_projective_layer.md`: the
first half of the layer `rmk:aj-remaining` names as separating the hand-checked
Andersen-Jessen refutation from a kernel-checked one.

## Why this cannot come from Mathlib

The natural route is `Measure.comap Subtype.val volume`. It does not work.
`Measure.comap` is

    if Injective f ∧ ∀ s, MeasurableSet s → NullMeasurableSet (f '' s) μ
    then ... else 0

and for `X` thick with thick complement, subsets of `X` are not generally
null-measurable, so the guard fails and comap returns **junk (0)**.
`Measure.Subtype.measureSpace` is defined as exactly that comap, so it
degenerates too, and `Subtype.volume_univ` needs `NullMeasurableSet X`, which a
thick-complement thick set cannot have. Mathlib has no thick-set trace measure.

## What is built here

The subtype carries the comap SIGMA-ALGEBRA (which is fine -- only the measure
degenerates), and the measure is built directly with `Measure.ofMeasurable`:

* `volume_eq_of_preimage_eq` -- well-definedness. Two measurable sets with the
  same trace differ by a measurable set disjoint from `X`, hence null. This is
  the only place thickness is used, and `X_thick` is exactly its hypothesis.
* `traceVal` -- the value function, `volume` of any representative.
* `traceVal_iUnion` -- sigma-additivity: disjoint traces come from sets whose
  overlap misses `X`, so the family is a.e.-disjoint and `measure_iUnion0`
  applies.
* `traceMeasure` / `traceMeasure_apply` -- the measure and its defining
  property `lambda_X (E n X) = lambda E`.
* `ajTrace` -- instantiated at every level of the Andersen-Jessen tower.

All axiom-free: [propext, Classical.choice, Quot.sound].

## What is NOT here

Units 2-4 of the scope doc: the projective system over `X_0 x ... x X_n` with
the diagonal maps, the contents, and the `EscapingTower` instantiation. Staged
rather than in the library because it is a work in progress.
-/
import QuerySystem.AndersenJessen
open MeasureTheory Set
open scoped ENNReal
namespace ThickTrace

def Thick (X : Set ℝ) : Prop :=
  ∀ ⦃E : Set ℝ⦄, MeasurableSet E → E ∩ X = ∅ → volume E = 0

variable {X : Set ℝ}

/-- Preimage under `val` determines the Lebesgue measure, for thick `X`. -/
theorem volume_eq_of_preimage_eq (hX : Thick X) {E F : Set ℝ}
    (hE : MeasurableSet E) (hF : MeasurableSet F)
    (h : (Subtype.val ⁻¹' E : Set ↥X) = Subtype.val ⁻¹' F) :
    volume E = volume F := by
  -- E ∩ X = F ∩ X follows from the preimage equality
  have hinter : E ∩ X = F ∩ X := by
    ext x
    constructor
    · rintro ⟨hxE, hxX⟩
      have : (⟨x, hxX⟩ : ↥X) ∈ (Subtype.val ⁻¹' E : Set ↥X) := hxE
      rw [h] at this
      exact ⟨this, hxX⟩
    · rintro ⟨hxF, hxX⟩
      have : (⟨x, hxX⟩ : ↥X) ∈ (Subtype.val ⁻¹' F : Set ↥X) := hxF
      rw [← h] at this
      exact ⟨this, hxX⟩
  -- symmetric differences are measurable and miss X, hence null
  have h1 : volume (E \ F) = 0 := by
    refine hX (hE.diff hF) ?_
    ext x
    simp only [mem_inter_iff, mem_diff, mem_empty_iff_false, iff_false, not_and]
    rintro ⟨hxE, hxF⟩ hxX
    exact hxF ((Set.ext_iff.mp hinter x).mp ⟨hxE, hxX⟩).1
  have h2 : volume (F \ E) = 0 := by
    refine hX (hF.diff hE) ?_
    ext x
    simp only [mem_inter_iff, mem_diff, mem_empty_iff_false, iff_false, not_and]
    rintro ⟨hxF, hxE⟩ hxX
    exact hxE ((Set.ext_iff.mp hinter x).mpr ⟨hxF, hxX⟩).1
  have e1 := measure_inter_add_diff (μ := volume) E hF
  have e2 := measure_inter_add_diff (μ := volume) F hE
  rw [h1, add_zero] at e1
  rw [h2, add_zero] at e2
  rw [← e1, ← e2, Set.inter_comm]


/-- The subtype carries the comap σ-algebra. -/
instance : MeasurableSpace ↥X := MeasurableSpace.comap Subtype.val inferInstance

theorem measurableSet_subtype_iff (S : Set ↥X) :
    MeasurableSet S ↔ ∃ E : Set ℝ, MeasurableSet E ∧ Subtype.val ⁻¹' E = S :=
  Iff.rfl

/-- Pick a measurable representative of a trace-measurable set. -/
noncomputable def rep {S : Set ↥X} (hS : MeasurableSet S) : Set ℝ :=
  ((measurableSet_subtype_iff S).mp hS).choose

theorem rep_spec {S : Set ↥X} (hS : MeasurableSet S) :
    MeasurableSet (rep hS) ∧ Subtype.val ⁻¹' (rep hS) = S :=
  ((measurableSet_subtype_iff S).mp hS).choose_spec

/-- The trace measure's value function: λ of any representative. -/
noncomputable def traceVal (S : Set ↥X) (hS : MeasurableSet S) : ℝ≥0∞ :=
  volume (rep hS)

/-- Independent of the representative -- this is where thickness is spent. -/
theorem traceVal_eq (hX : Thick X) {S : Set ↥X} (hS : MeasurableSet S)
    {E : Set ℝ} (hE : MeasurableSet E) (hpre : Subtype.val ⁻¹' E = S) :
    traceVal S hS = volume E :=
  volume_eq_of_preimage_eq hX (rep_spec hS).1 hE ((rep_spec hS).2.trans hpre.symm)


theorem traceVal_empty (hX : Thick X) :
    traceVal (∅ : Set ↥X) MeasurableSet.empty = 0 := by
  rw [traceVal_eq hX _ MeasurableSet.empty (by simp)]
  simp

/-- **σ-additivity of the trace value.** Disjoint traces come from sets whose
overlaps miss `X`, hence are null; so Lebesgue additivity transfers. -/
theorem traceVal_iUnion (hX : Thick X) {f : ℕ → Set ↥X}
    (hf : ∀ i, MeasurableSet (f i)) (hd : Pairwise (Function.onFun Disjoint f)) :
    traceVal (⋃ i, f i) (MeasurableSet.iUnion hf) = ∑' i, traceVal (f i) (hf i) := by
  -- representatives
  set E : ℕ → Set ℝ := fun i => rep (hf i) with hE
  have hEmeas : ∀ i, MeasurableSet (E i) := fun i => (rep_spec (hf i)).1
  have hEpre : ∀ i, Subtype.val ⁻¹' (E i) = f i := fun i => (rep_spec (hf i)).2
  -- the union of representatives represents the union
  have hUpre : Subtype.val ⁻¹' (⋃ i, E i) = ⋃ i, f i := by
    rw [Set.preimage_iUnion]; exact iUnion_congr hEpre
  rw [traceVal_eq hX _ (MeasurableSet.iUnion hEmeas) hUpre]
  -- pairwise a.e.-disjoint: E i ∩ E j misses X
  have hae : Pairwise (fun i j => MeasureTheory.AEDisjoint volume (E i) (E j)) := by
    intro i j hij
    refine hX ((hEmeas i).inter (hEmeas j)) ?_
    ext x
    simp only [Set.mem_inter_iff, Set.mem_empty_iff_false, iff_false, not_and]
    rintro ⟨hxi, hxj⟩ hxX
    have hi : (⟨x, hxX⟩ : ↥X) ∈ f i := by rw [← hEpre i]; exact hxi
    have hj : (⟨x, hxX⟩ : ↥X) ∈ f j := by rw [← hEpre j]; exact hxj
    exact (Set.disjoint_left.mp (hd hij)) hi hj
  rw [measure_iUnion₀ hae (fun i => (hEmeas i).nullMeasurableSet)]
  exact tsum_congr fun i => (traceVal_eq hX (hf i) (hEmeas i) (hEpre i)).symm

/-- **The trace measure λ_X on a thick set (Border Prop. 14).**
Not obtainable from `Measure.comap`: that is guarded by "every measurable subset
has null-measurable image" and returns 0 when the guard fails, which it does for
a thick set with thick complement. Built directly instead. -/
noncomputable def traceMeasure (hX : Thick X) : Measure ↥X :=
  Measure.ofMeasurable (fun S hS => traceVal S hS) (traceVal_empty hX)
    (fun _ hf hd => traceVal_iUnion hX hf hd)

/-- **The defining property.** `λ_X (E ∩ X) = λ E`. -/
theorem traceMeasure_apply (hX : Thick X) {E : Set ℝ} (hE : MeasurableSet E) :
    traceMeasure hX (Subtype.val ⁻¹' E) = volume E := by
  have hm : MeasurableSet (Subtype.val ⁻¹' E : Set ↥X) := ⟨E, hE, rfl⟩
  rw [traceMeasure, Measure.ofMeasurable_apply _ hm]
  exact traceVal_eq hX hm hE rfl


/-- Total mass: `λ_X(univ) = λ(univ)`. For `X ⊆ [0,1]` thick *in* `[0,1]` one
gets 1; stated here in the general form. -/
theorem traceMeasure_univ (hX : Thick X) :
    traceMeasure hX (Set.univ : Set ↥X) = volume (Set.univ : Set ℝ) := by
  have : (Set.univ : Set ↥X) = Subtype.val ⁻¹' (Set.univ : Set ℝ) := rfl
  rw [this, traceMeasure_apply hX MeasurableSet.univ]



/-- **The AJ tower supplies thick sets.** `X_thick` is exactly `Thick`. -/
theorem thick_X (α : ℝ) (hα : Irrational α) (k : ℕ) :
    Thick (AndersenJessen.X α k) :=
  fun E hE h => AndersenJessen.X_thick α hα k hE h

/-- **The trace measure exists on every level of the AJ tower.** This is the
first half of the layer `rmk:aj-remaining` names as missing. -/
noncomputable def ajTrace (α : ℝ) (hα : Irrational α) (k : ℕ) :
    Measure ↥(AndersenJessen.X α k) :=
  traceMeasure (thick_X α hα k)

theorem ajTrace_apply (α : ℝ) (hα : Irrational α) (k : ℕ)
    {E : Set ℝ} (hE : MeasurableSet E) :
    ajTrace α hα k (Subtype.val ⁻¹' E) = volume E :=
  traceMeasure_apply (thick_X α hα k) hE

#print axioms ajTrace
#print axioms ajTrace_apply
end ThickTrace
