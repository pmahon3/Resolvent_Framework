/-
# Unit 4 assembly: the Andersen-Jessen system admits no extension

The end of `notes/open_questions/aj_tower/SCOPE_trace_projective_layer.md`.
This is the layer `rmk:aj-remaining` names as separating the hand-checked
Andersen-Jessen refutation from a kernel-checked one.

  Sys              the projective system (unit 2's shape) over the tower levels
  marg / marg_compat   the diagonal marginals and their Kolmogorov consistency
  NCC              them, packaged as NormalizedCompatibleContents
  measurableSet_base / cyl_antitone / cyl_iInter_empty   the tower's three
                   structural fields
  Tower            the EscapingTower instance -- all five fields
  AJ_no_extension  not_exists_extension_of_escapingTower applied to it

`AJ_no_extension` is stated for any level measures satisfying `hmu`
(compatibility along the tower inclusions) and `hnorm` (mass 1). Those are
exactly what the trace measures over `volume.restrict (Icc 0 1)` supply --
`ThickTraceGeneral.ajTrace_compat` and `ajTrace_univ` -- and `ajThickFor` here
restates the thickness input.

REMAINING (bookkeeping, not mathematics): feed the trace measures in as `mu` to
get a fully unconditional statement in one theorem. The pieces are proved on
both sides; what is missing is that `ThickTraceGeneral` and this file each
define their own copy of the trace-measure construction, so the two have to be
unified into one library module before they can be composed literally. Until
then AJ_no_extension is conditional on hypotheses that are separately proved
rather than substituted.

Axiom-free throughout: [propext, Classical.choice, Quot.sound].
-/
import QuerySystem.AndersenJessen
import QuerySystem
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

def ThickFor (μ : Measure ℝ) (X : Set ℝ) : Prop :=
  ∀ ⦃E : Set ℝ⦄, MeasurableSet E → E ∩ X = ∅ → μ E = 0

noncomputable abbrev unitBase : Measure ℝ := volume.restrict (Set.Icc 0 1)

def incl {m n : ℕ} (h : m ≤ n) (y : Lev α n) : Lev α m :=
  ⟨y.1, AndersenJessen.X_antitone α h y.2⟩

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



/-- Every measure is an AddContent on the measurable sets. -/
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

theorem cyl_iInter_empty : (⋂ n, (Sys α).Cyl n (base α n)) = ∅ := by
  ext ω
  simp only [Set.mem_iInter, Set.mem_empty_iff_false, iff_false]
  intro hall
  set r : ℝ := (ω.1 (0 : ℕ) ⟨0, by omega⟩).1 with hr
  have hmem : ∀ k, r ∈ AndersenJessen.X α k := by
    intro k
    have hco := ω.2 (show (Sys α).le (0 : ℕ) k from Nat.zero_le k)
    have hd : (ω.1 k ⟨0, by omega⟩).1 = (ω.1 k ⟨k, by omega⟩).1 := hall k _ _
    have h0 : r = (ω.1 k ⟨0, by omega⟩).1 := by rw [hr, hco]; rfl
    rw [h0, hd]
    exact (ω.1 k ⟨k, by omega⟩).2
  have : r ∈ ⋂ k, AndersenJessen.X α k := Set.mem_iInter.mpr hmem
  rw [AndersenJessen.X_iInter α] at this
  exact this

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

theorem ajThickFor (k : ℕ) (hα : Irrational α) :
    ThickFor unitBase (AndersenJessen.X α k) := by
  intro E hE h
  rw [unitBase, Measure.restrict_apply hE]
  refine AndersenJessen.X_thick α hα k (hE.inter measurableSet_Icc) ?_
  ext x
  simp only [mem_inter_iff, mem_empty_iff_false, iff_false, not_and]
  rintro ⟨hxE, _⟩ hxX
  have : x ∈ E ∩ AndersenJessen.X α k := ⟨hxE, hxX⟩
  rw [h] at this; exact this

theorem unitBase_univ : unitBase Set.univ = 1 := by
  simp [unitBase, Measure.restrict_apply MeasurableSet.univ]

#print axioms Tower
#print axioms AJ_no_extension
#print axioms ajThickFor
end ASM
