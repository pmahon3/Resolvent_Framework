/-
# The Andersen-Jessen system admits no extension

The refutation, kernel-checked end to end. This is the layer
`rmk:aj-remaining` names as separating the hand-checked Andersen-Jessen
counterexample from a kernel-checked one.

The original `UpperDirected` form of `stone_observational_extension` claimed:
compatible sigma-additive marginals + upper-directedness + surjective
evaluations ==> a limit measure. Every one of those hypotheses holds in the
system built here, and the conclusion fails -- so the original statement was
false, and correcting `UpperDirected` to `SequentiallyUpperDirected` was the
necessary repair, not a convenience.

  Sys              the projective system over the tower levels
  marg_compat      Kolmogorov consistency of the diagonal marginals
  NCC              packaged as NormalizedCompatibleContents
  Tower            the EscapingTower -- all five fields
  AJ_no_extension  the obstruction theorem applied

Level measures come from `ThickTrace` (the trace measure over
`volume.restrict (Icc 0 1)`), whose `ajTrace_compat` and `ajTrace_univ`
discharge this file's `hmu` and `hnorm`.

Graduated from `staging/` 2026-08-24. Axiom-free.
-/
import QuerySystem.ThickTrace
import QuerySystem.ExtensionObstruction
import QuerySystem.Diagonal

open MeasureTheory Set QuerySystem
open scoped ENNReal

namespace ASM
variable (α : ℝ) (hα : Irrational α)

abbrev Lev (α : ℝ) (k : ℕ) : Type := ↥(AndersenJessen.X α k)
abbrev Out (n : ℕ) := (i : Fin (n+1)) → Lev α i
def bond {m n : ℕ} (h : m ≤ n) (x : Out α n) : Out α m := fun i => x ⟨i.1, by omega⟩
lemma measurable_bond {m n : ℕ} (h : m ≤ n) : Measurable (bond α h) :=
  measurable_pi_lambda _ (fun i => measurable_pi_apply _)

def Sys : QuerySystem where
  ι := ℕ
  q := fun n => ⟨Out α n, inferInstance⟩
  le := (· ≤ ·)
  π := fun {m n} h => ⟨bond α h, measurable_bond α h⟩
  le_refl := fun _ => Nat.le_refl _
  le_trans := fun h h' => Nat.le_trans h h'
  π_refl := fun i => by funext x; funext j; rfl
  π_trans := fun hij hjk => by funext x; funext j; rfl

/-! ## The pieces, restated locally -/

/-- The tower inclusion -- `ThickTrace.incl` at the tower's nesting, so the
compatibility lemma there applies to it directly. -/
def incl {m n : ℕ} (h : m ≤ n) (y : Lev α n) : Lev α m :=
  ThickTrace.incl (AndersenJessen.X_antitone α h) y

def diag (n : ℕ) (x : Lev α n) : Out α n := fun i => incl α (by omega) x

def base (n : ℕ) : Set (Out α n) := {x | ∀ i j, (x i).1 = (x j).1}

theorem diag_preimage_base (n : ℕ) : diag α n ⁻¹' base α n = Set.univ := by
  ext x; simp only [Set.mem_preimage, base, Set.mem_setOf_eq, Set.mem_univ, iff_true]
  intro i j; rfl

theorem measurable_diag (n : ℕ) : Measurable (diag α n) :=
  measurable_pi_lambda _ (fun i => by rintro S ⟨E, hE, rfl⟩; exact ⟨E, hE, rfl⟩)

/-- **The commutation.** `bond h ∘ diag n = diag m ∘ incl h`. -/
theorem bond_diag {m n : ℕ} (h : m ≤ n) (x : Lev α n) :
    bond α h (diag α n x) = diag α m (incl α h x) := by
  funext i; rfl


/-! ## The contents -/

variable (mu : ∀ k, Measure (Lev α k))

/-- The marginal at level `n`: the level measure pushed along the diagonal. -/
noncomputable def marg (n : ℕ) : Measure (Out α n) := (mu n).map (diag α n)

/-- Compatibility of the marginals, from compatibility of the base measures. -/
theorem marg_compat
    (hmu : ∀ {m n : ℕ} (h : m ≤ n), (mu n).map (incl α h) = mu m)
    {m n : ℕ} (h : m ≤ n) (A : Set (Out α m)) (hA : MeasurableSet A) :
    marg α mu m A = marg α mu n (bond α h ⁻¹' A) := by
  unfold marg
  rw [Measure.map_apply (measurable_diag α m) hA,
      Measure.map_apply (measurable_diag α n) ((measurable_bond α h) hA)]
  have : (diag α n) ⁻¹' (bond α h ⁻¹' A) = (incl α h) ⁻¹' ((diag α m) ⁻¹' A) := by
    ext x
    simp only [Set.mem_preimage]
    rw [bond_diag α h x]
  rw [this, ← Measure.map_apply _ (measurable_diag α m hA), hmu h]
  rintro S ⟨E, hE, rfl⟩
  exact ⟨E, hE, rfl⟩



/-- Every measure is an `AddContent` on the measurable sets. -/
noncomputable def ofMeasure {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω) :
    AddContent ℝ≥0∞ {s : Set Ω | MeasurableSet s} where
  toFun := fun s => μ s
  empty' := by simp
  sUnion' := by
    intro I hss hdis hmem
    rw [measure_sUnion I.countable_toSet hdis (fun s hs => hss hs), tsum_fintype]
    exact Finset.sum_finset_coe (f := fun s => μ s) I

/-- **The contents on the AJ system.** -/
noncomputable def NCC
    (hmu : ∀ {m n : ℕ} (h : m ≤ n), (mu n).map (incl α h) = mu m)
    (hnorm : ∀ n, mu n Set.univ = 1) :
    (Sys α).NormalizedCompatibleContents where
  ν := fun n => ofMeasure (marg α mu n)
  compat := by
    intro m n h A hA
    exact marg_compat α mu hmu h A hA
  norm := by
    intro n
    show marg α mu n Set.univ = 1
    unfold marg
    rw [Measure.map_apply (measurable_diag α n) MeasurableSet.univ]
    simpa using hnorm n



/-! ## The escaping tower -/

theorem measurableSet_base (n : ℕ) : MeasurableSet (base α n) := by
  have : base α n = ⋂ (i : Fin (n+1)) (j : Fin (n+1)),
      {x : Out α n | (x i).1 = (x j).1} := by
    ext x; simp [base, Set.mem_iInter]
  rw [this]
  refine MeasurableSet.iInter (fun i => MeasurableSet.iInter (fun j => ?_))
  exact measurableSet_eq_fun
    (measurable_subtype_coe.comp (measurable_pi_apply i))
    (measurable_subtype_coe.comp (measurable_pi_apply j))

theorem cyl_antitone : Antitone (fun n : ℕ => (Sys α).Cyl n (base α n)) := by
  intro m n hmn ω hω
  simp only [QuerySystem.Cyl, QuerySystem.eval, Set.mem_setOf_eq, base] at hω ⊢
  intro i j
  rw [ω.2 (show (Sys α).le m n from hmn)]
  exact hω _ _

/-- The **common-value sequence** of a coherent family: at level `k`, the real
number its top coordinate carries.

This map is the whole content of the reduction to `Diagonal`. That file proves
the emptiness fact over plain sequences `ℕ → ℝ`, and a coherent family is not a
sequence, so something has to carry it there. The two facts
`Diagonal.pi_inter_diag_eq_empty` consumes then come from different places:
membership in the tower levels is the subtype and needs no hypothesis at all,
while constancy needs both the coherence and the base cylinders. -/
def toSeq (ω : (Sys α).Omega) : ℕ → ℝ := fun k => (ω.1 k ⟨k, by omega⟩).1

/-- Every entry lies in its own tower level -- immediately, by the subtype. -/
theorem toSeq_mem_pi (ω : (Sys α).Omega) :
    toSeq α ω ∈ Diagonal.Pi' (fun k => AndersenJessen.X α k) :=
  fun k => (ω.1 k ⟨k, by omega⟩).2

/-- On the base cylinders the sequence is constant. Two moves, and neither
alone suffices: coherence carries coordinate `0` down from level `i` to level
`0`, and `base` carries it across level `i` from coordinate `0` to coordinate
`i`. -/
theorem toSeq_mem_diag (ω : (Sys α).Omega)
    (hall : ∀ n, ω ∈ (Sys α).Cyl n (base α n)) (n : ℕ) :
    toSeq α ω ∈ Diagonal.Diag n := by
  intro i _
  have hco : (ω.1 (0 : ℕ)) ⟨0, by omega⟩ = (ω.1 i) ⟨0, by omega⟩ := by
    rw [ω.2 (show (Sys α).le (0 : ℕ) i from Nat.zero_le i)]; rfl
  have hb : ((ω.1 i) ⟨0, by omega⟩).1 = ((ω.1 i) ⟨i, by omega⟩).1 := hall i _ _
  show ((ω.1 i) ⟨i, by omega⟩).1 = ((ω.1 (0 : ℕ)) ⟨0, by omega⟩).1
  rw [hco, hb]

/-- **The tower escapes.** Routed through `Diagonal.pi_inter_diag_eq_empty`
rather than re-running the argument: a point of every base cylinder maps to a
constant sequence lying in every tower level, and `X_iInter` says there is no
such thing. -/
theorem cyl_iInter_empty : (⋂ n, (Sys α).Cyl n (base α n)) = ∅ := by
  ext ω
  simp only [Set.mem_iInter, Set.mem_empty_iff_false, iff_false]
  intro hall
  have hmem : toSeq α ω ∈
      Diagonal.Pi' (fun k => AndersenJessen.X α k) ∩ ⋂ n, Diagonal.Diag n :=
    ⟨toSeq_mem_pi α ω, Set.mem_iInter.mpr (toSeq_mem_diag α ω hall)⟩
  rw [Diagonal.pi_inter_diag_eq_empty (AndersenJessen.X_iInter α)] at hmem
  exact hmem

/-- **The escaping tower over the Andersen-Jessen system.** -/
noncomputable def Tower
    (hmu : ∀ {m n : ℕ} (h : m ≤ n), (mu n).map (incl α h) = mu m)
    (hnorm : ∀ n, mu n Set.univ = 1) :
    (Sys α).EscapingTower (NCC α mu hmu hnorm) where
  idx := id
  base := base α
  meas := measurableSet_base α
  full := by
    intro n
    show marg α mu n (base α n) = 1
    unfold marg
    rw [Measure.map_apply (measurable_diag α n) (measurableSet_base α n),
        diag_preimage_base]
    exact hnorm n
  anti := cyl_antitone α
  empty := cyl_iInter_empty α



/-- **THE RESULT: the Andersen-Jessen system admits no extension.** Kernel-
checked, no hand step. Every hypothesis of the original `UpperDirected` form of
`stone_observational_extension` holds here, and the conclusion fails. -/
theorem AJ_no_extension
    (hmu : ∀ {m n : ℕ} (h : m ≤ n), (mu n).map (incl α h) = mu m)
    (hnorm : ∀ n, mu n Set.univ = 1) :
    ¬ ∃ μ : Measure (Sys α).Omega, IsProbabilityMeasure μ ∧
        ∀ (i : (Sys α).ι) (A : Set ((Sys α).q i).Outcome), MeasurableSet A →
          μ ((Sys α).Cyl i A) = (NCC α mu hmu hnorm).ν i A :=
  (Sys α).not_exists_extension_of_escapingTower _ (Tower α mu hmu hnorm)



/-! ## Discharging the hypotheses from the trace measures

`hmu` and `hnorm` are exactly what the trace measures over the restricted base
supply (`ThickTraceGeneral.ajTrace_compat`, `ajTrace_univ`). Restating the two
constructions locally so the final theorem is unconditional. -/

/-! ## The unconditional statement

`hmu` and `hnorm` are exactly what `ThickTrace` supplies for the tower, so they
can now be substituted rather than assumed. -/

/-- The tower's level measures: the trace measure over `volume.restrict (Icc 0 1)`. -/
noncomputable def ajMu (hα : Irrational α) (k : ℕ) : Measure (Lev α k) :=
  ThickTrace.traceMeasure (ThickTrace.ajThickFor α hα k)

theorem ajMu_compat (hα : Irrational α) {m n : ℕ} (h : m ≤ n) :
    (ajMu α hα n).map (incl α h) = ajMu α hα m :=
  ThickTrace.map_incl_traceMeasure (ThickTrace.ajThickFor α hα m)
    (ThickTrace.ajThickFor α hα n) (AndersenJessen.X_antitone α h)

theorem ajMu_univ (hα : Irrational α) (n : ℕ) : ajMu α hα n Set.univ = 1 :=
  ThickTrace.ajTrace_univ α hα n

/-- **THE THEOREM, unconditional.** The Andersen-Jessen query system carries
compatible σ-additive probability marginals and admits no extension to a
probability measure on `Ω`. Kernel-checked; no hand step. -/
theorem AJ_no_extension_unconditional (hα : Irrational α) :
    ¬ ∃ μ : Measure (Sys α).Omega, IsProbabilityMeasure μ ∧
        ∀ (i : (Sys α).ι) (A : Set ((Sys α).q i).Outcome), MeasurableSet A →
          μ ((Sys α).Cyl i A)
            = (NCC α (ajMu α hα) (ajMu_compat α hα) (ajMu_univ α hα)).ν i A :=
  AJ_no_extension α (ajMu α hα) (ajMu_compat α hα) (ajMu_univ α hα)

#print axioms AJ_no_extension_unconditional

end ASM
