/-
# The trace measure on a thick set

Border, *Kolmogorov Extension Problem*, Prop. 14: for `X` thick in `Ω` (every
measurable set disjoint from `X` is null), the traces `{E ∩ X : E measurable}`
carry a measure `λ_X (E ∩ X) = μ E`.

## Why this is not `Measure.comap`

`Measure.comap` is guarded:

    if Injective f ∧ ∀ s, MeasurableSet s → NullMeasurableSet (f '' s) μ
    then ... else 0

For `X` thick with thick complement, subsets of `X` are not generally
null-measurable, the guard fails, and comap returns **junk (`0`)**.
`Measure.Subtype.measureSpace` is defined as exactly that comap, so it
degenerates too, and `Subtype.volume_univ` needs `NullMeasurableSet X`, which a
thick-complement thick set cannot have. Mathlib has no thick-set trace measure.

The σ-algebra is fine -- it is Mathlib's `Subtype.instMeasurableSpace`, which is
definitionally `MeasurableSpace.comap Subtype.val`. Only the MEASURE has to be
built, which is done here with `Measure.ofMeasurable`.

## Base measure

Stated for an arbitrary base `μ`, not just `volume`. That generality is not
decoration: `NormalizedCompatibleContents` needs total mass 1, and
`λ_X (univ) = volume (univ) = ∞`. Confining the levels to `[0,1]` does NOT fix
it -- `X ∩ [0,1]` is not thick in `ℝ` (`Icc 2 3` is measurable, disjoint from
it, and has measure 1), so the construction would not apply at all. Restricting
the AMBIENT measure does fix it: `X` is thick for `volume.restrict (Icc 0 1)`,
which has mass 1, and the levels stay as `AndersenJessen.X` builds them, so
`X_antitone`, `X_iInter` and `X_thick` all still apply.

Graduated from `staging/` 2026-08-24. Axiom-free.
-/
import QuerySystem.AndersenJessen

open MeasureTheory Set
open scoped ENNReal

namespace ThickTrace
variable {Ω : Type*} [MeasurableSpace Ω] {X : Set Ω} {μ : Measure Ω}

/-- `X` is **thick for μ**: every measurable set disjoint from `X` is μ-null.
Generalizes `Thick` (μ = volume) and covers the restricted case. -/
def ThickFor (μ : Measure Ω) (X : Set Ω) : Prop :=
  ∀ ⦃E : Set Ω⦄, MeasurableSet E → E ∩ X = ∅ → μ E = 0

theorem measure_eq_of_preimage_eq (hX : ThickFor μ X) {E F : Set Ω}
    (hE : MeasurableSet E) (hF : MeasurableSet F)
    (h : (Subtype.val ⁻¹' E : Set ↥X) = Subtype.val ⁻¹' F) : μ E = μ F := by
  have hinter : E ∩ X = F ∩ X := by
    ext x
    constructor
    · rintro ⟨hxE, hxX⟩
      have : (⟨x, hxX⟩ : ↥X) ∈ (Subtype.val ⁻¹' E : Set ↥X) := hxE
      rw [h] at this; exact ⟨this, hxX⟩
    · rintro ⟨hxF, hxX⟩
      have : (⟨x, hxX⟩ : ↥X) ∈ (Subtype.val ⁻¹' F : Set ↥X) := hxF
      rw [← h] at this; exact ⟨this, hxX⟩
  have h1 : μ (E \ F) = 0 := by
    refine hX (hE.diff hF) ?_
    ext x; simp only [mem_inter_iff, mem_diff, mem_empty_iff_false, iff_false, not_and]
    rintro ⟨hxE, hxF⟩ hxX
    exact hxF ((Set.ext_iff.mp hinter x).mp ⟨hxE, hxX⟩).1
  have h2 : μ (F \ E) = 0 := by
    refine hX (hF.diff hE) ?_
    ext x; simp only [mem_inter_iff, mem_diff, mem_empty_iff_false, iff_false, not_and]
    rintro ⟨hxF, hxE⟩ hxX
    exact hxE ((Set.ext_iff.mp hinter x).mpr ⟨hxF, hxX⟩).1
  have e1 := measure_inter_add_diff (μ := μ) E hF
  have e2 := measure_inter_add_diff (μ := μ) F hE
  rw [h1, add_zero] at e1
  rw [h2, add_zero] at e2
  rw [← e1, ← e2, Set.inter_comm]


theorem measurableSet_subtype_iff (S : Set ↥X) :
    MeasurableSet S ↔ ∃ E : Set Ω, MeasurableSet E ∧ Subtype.val ⁻¹' E = S := Iff.rfl

noncomputable def rep {S : Set ↥X} (hS : MeasurableSet S) : Set Ω :=
  ((measurableSet_subtype_iff S).mp hS).choose

theorem rep_spec {S : Set ↥X} (hS : MeasurableSet S) :
    MeasurableSet (rep hS) ∧ Subtype.val ⁻¹' (rep hS) = S :=
  ((measurableSet_subtype_iff S).mp hS).choose_spec

noncomputable def traceVal (μ : Measure Ω) (S : Set ↥X) (hS : MeasurableSet S) : ℝ≥0∞ :=
  μ (rep hS)

theorem traceVal_eq (hX : ThickFor μ X) {S : Set ↥X} (hS : MeasurableSet S)
    {E : Set Ω} (hE : MeasurableSet E) (hpre : Subtype.val ⁻¹' E = S) :
    traceVal μ S hS = μ E :=
  measure_eq_of_preimage_eq hX (rep_spec hS).1 hE ((rep_spec hS).2.trans hpre.symm)

theorem traceVal_empty (hX : ThickFor μ X) :
    traceVal μ (∅ : Set ↥X) MeasurableSet.empty = 0 := by
  rw [traceVal_eq hX _ MeasurableSet.empty (by simp)]; simp

theorem traceVal_iUnion (hX : ThickFor μ X) {f : ℕ → Set ↥X}
    (hf : ∀ i, MeasurableSet (f i)) (hd : Pairwise (Function.onFun Disjoint f)) :
    traceVal μ (⋃ i, f i) (MeasurableSet.iUnion hf) = ∑' i, traceVal μ (f i) (hf i) := by
  set E : ℕ → Set Ω := fun i => rep (hf i) with hE
  have hEmeas : ∀ i, MeasurableSet (E i) := fun i => (rep_spec (hf i)).1
  have hEpre : ∀ i, Subtype.val ⁻¹' (E i) = f i := fun i => (rep_spec (hf i)).2
  have hUpre : Subtype.val ⁻¹' (⋃ i, E i) = ⋃ i, f i := by
    rw [Set.preimage_iUnion]; exact iUnion_congr hEpre
  rw [traceVal_eq hX _ (MeasurableSet.iUnion hEmeas) hUpre]
  have hae : Pairwise (fun i j => MeasureTheory.AEDisjoint μ (E i) (E j)) := by
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

/-- **The trace measure over an arbitrary base measure.** -/
noncomputable def traceMeasure (hX : ThickFor μ X) : Measure ↥X :=
  Measure.ofMeasurable (fun S hS => traceVal μ S hS) (traceVal_empty hX)
    (fun _ hf hd => traceVal_iUnion hX hf hd)

theorem traceMeasure_apply (hX : ThickFor μ X) {E : Set Ω} (hE : MeasurableSet E) :
    traceMeasure hX (Subtype.val ⁻¹' E) = μ E := by
  have hm : MeasurableSet (Subtype.val ⁻¹' E : Set ↥X) := ⟨E, hE, rfl⟩
  rw [traceMeasure, Measure.ofMeasurable_apply _ hm]
  exact traceVal_eq hX hm hE rfl

/-- **Total mass.** `λ_X(univ) = μ(univ)`. With `μ = volume.restrict (Icc 0 1)`
that is 1. -/
theorem traceMeasure_univ (hX : ThickFor μ X) :
    traceMeasure hX (Set.univ : Set ↥X) = μ Set.univ := by
  have : (Set.univ : Set ↥X) = Subtype.val ⁻¹' (Set.univ : Set Ω) := rfl
  rw [this, traceMeasure_apply hX MeasurableSet.univ]



/-! ## The AJ tower over the unit interval -/

/-- The base measure: Lebesgue restricted to `[0,1]`, a probability measure. -/
noncomputable abbrev unitBase : Measure ℝ := volume.restrict (Set.Icc 0 1)

theorem unitBase_univ : unitBase Set.univ = 1 := by
  simp [unitBase, Measure.restrict_apply MeasurableSet.univ]

/-- **Each tower level is thick for the restricted measure.** Thickness in `ℝ`
gives it: a measurable `E` missing `X` has `E ∩ [0,1]` measurable and missing
`X`, hence null. -/
theorem ajThickFor (α : ℝ) (hα : Irrational α) (k : ℕ) :
    ThickFor unitBase (AndersenJessen.X α k) := by
  intro E hE h
  rw [unitBase, Measure.restrict_apply hE]
  refine AndersenJessen.X_thick α hα k (hE.inter measurableSet_Icc) ?_
  ext x
  simp only [mem_inter_iff, mem_empty_iff_false, iff_false, not_and]
  rintro ⟨hxE, _⟩ hxX
  have : x ∈ E ∩ AndersenJessen.X α k := ⟨hxE, hxX⟩
  rw [h] at this; exact this

/-- **The tower's trace measures are probability measures.** This is what
`full` needs, and what thickness-in-`ℝ` alone could not give. -/
theorem ajTrace_univ (α : ℝ) (hα : Irrational α) (k : ℕ) :
    traceMeasure (ajThickFor α hα k) (Set.univ) = 1 := by
  rw [traceMeasure_univ, unitBase_univ]


/-! ## Compatibility along inclusions, in the general setting

Unit 3's `ajTrace_compat` was stated for `Thick` (i.e. `volume`), while mass 1
needs `ThickFor unitBase`. `NormalizedCompatibleContents` wants `compat` AND
`norm` on ONE family, so compatibility is re-proved here over the same base
measure. The proof is verbatim -- `Measure.ext` plus `traceMeasure_apply`
twice -- since nothing in it used any property of `volume`. -/

/-- Inclusion of subtypes induced by `Y ⊆ X`. -/
def incl {X Y : Set Ω} (h : Y ⊆ X) (y : ↥Y) : ↥X := ⟨y.1, h y.2⟩

theorem measurable_incl {X Y : Set Ω} (h : Y ⊆ X) : Measurable (incl h) := by
  rintro S ⟨E, hE, rfl⟩
  exact ⟨E, hE, rfl⟩

theorem incl_preimage {X Y : Set Ω} (h : Y ⊆ X) (E : Set Ω) :
    incl h ⁻¹' (Subtype.val ⁻¹' E : Set ↥X) = (Subtype.val ⁻¹' E : Set ↥Y) := rfl

/-- The inclusion preserves underlying values -- needed by `full`. -/
theorem incl_val {X Y : Set Ω} (h : Y ⊆ X) (y : ↥Y) : (incl h y).1 = y.1 := rfl

/-- **Trace measures are compatible along inclusions, over any base measure.** -/
theorem map_incl_traceMeasure {X Y : Set Ω} (hX : ThickFor μ X) (hY : ThickFor μ Y)
    (h : Y ⊆ X) : (traceMeasure hY).map (incl h) = traceMeasure hX := by
  refine Measure.ext fun S hS => ?_
  obtain ⟨E, hE, rfl⟩ := (measurableSet_subtype_iff S).mp hS
  rw [Measure.map_apply (measurable_incl h) hS, incl_preimage,
      traceMeasure_apply hY hE, traceMeasure_apply hX hE]

/-- **The tower instance, over the unit base.** Now `compat` and `norm` live on
the same family. -/
theorem ajTrace_compat (α : ℝ) (hα : Irrational α) {m n : ℕ} (h : m ≤ n) :
    (traceMeasure (ajThickFor α hα n)).map (incl (AndersenJessen.X_antitone α h))
      = traceMeasure (ajThickFor α hα m) :=
  map_incl_traceMeasure (ajThickFor α hα m) (ajThickFor α hα n) _

end ThickTrace
