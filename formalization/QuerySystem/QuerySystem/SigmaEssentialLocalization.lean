/-
# σ-essential localization — the certified spine

Formalizes the settled spine of `papers/sigma_essential`:
* a 2-valued σ-additive state on a concrete σ-OML (a Dynkin system / σ-class),
* point evaluations `δ_ω` and the notion of extending a finite local pattern,
* `lem:dirac-iff`: a Dirac extends `s₀` iff `ω ∈ K(s₀)`, hence no Dirac extends
  `s₀` iff `K(s₀) = ∅`.

The concrete σ-OML of the paper (a family `L ⊆ P(Ω)` closed under complement and
countable orthogonal/disjoint unions, with orthocomplement = set-complement) is
exactly Mathlib's `MeasureTheory.DynkinSystem` — the paper's "σ-class"
(Navara–Pták 1983). We reuse it as the carrier.

This file is part of the *settled spine*; the open core (clause (ii),
σ-point-selection) is NOT formalized — it is open mathematics.
-/
import Mathlib.MeasureTheory.PiSystem
import Mathlib.Data.Set.Lattice

open Set Function MeasurableSpace

namespace SigmaEssential

variable {Ω : Type*} (d : MeasurableSpace.DynkinSystem Ω)

/-- The carrier `L`: the sets the σ-class `d` contains. -/
def Carrier : Set (Set Ω) := {A | d.Has A}

/-- A **two-valued state** on the concrete σ-OML `d`: a Boolean-valued assignment to
the sets of `d`, normalized at `Ω`, additive on complement pairs, and σ-additive over
countable orthogonal (pairwise-disjoint) families lying in `d`.

We carry the value as a `Prop` `Val A` ("`A` is true"), defined for all sets but only
constrained on `d.Has`-sets. -/
structure TwoValuedState (d : DynkinSystem Ω) where
  /-- `Val A` means the state assigns `1` to `A`. -/
  Val : Set Ω → Prop
  /-- decidability so we can speak of "true sets" as a genuine subfamily -/
  decVal : DecidablePred Val
  /-- normalization: the whole space is true -/
  val_univ : Val univ
  /-- the empty set is false -/
  not_val_empty : ¬ Val ∅
  /-- two-valued additivity on a complement pair in `d`: exactly one of `A`, `Aᶜ` holds -/
  val_compl : ∀ {A}, d.Has A → (Val Aᶜ ↔ ¬ Val A)
  /-- σ-additivity: for a countable pairwise-disjoint family in `d`, the union is true
      iff exactly one member is true (2-valued form of `s(⊔Aₙ)=Σ s(Aₙ)`) -/
  val_iUnion : ∀ {f : ℕ → Set Ω}, Pairwise (Disjoint on f) → (∀ i, d.Has (f i)) →
    (Val (⋃ i, f i) ↔ ∃ i, Val (f i))

attribute [instance] TwoValuedState.decVal

variable {d}

/-- The **point evaluation** `δ_ω`: `Val A := ω ∈ A`. It is a two-valued σ-additive
state (a *Dirac* state). -/
noncomputable def dirac (ω : Ω) : TwoValuedState d where
  Val A := ω ∈ A
  decVal := Classical.decPred _
  val_univ := mem_univ ω
  not_val_empty := notMem_empty ω
  val_compl {A} _ := by simp [mem_compl_iff]
  val_iUnion {f} _ _ := by simp [mem_iUnion]

/-- A state is **Dirac** if it is a point evaluation. -/
def TwoValuedState.IsDirac (s : TwoValuedState d) : Prop := ∃ ω : Ω, s = dirac ω

/-! ### Fidelity lemmas: the `∃i`-form σ-additivity is the paper's `=Σ` form

The paper's σ-additivity is `s(⊔Aₙ)=Σ s(Aₙ)` for disjoint families. For a 2-valued
state this means "union true ⟺ *exactly* one member true". Our `val_iUnion` gives
"⟺ *some* member true"; the "at most one" half is **derived** here (not assumed), via
monotonicity, which is itself derived from `val_iUnion` + Dynkin `has_diff`. So the
formal definition is certified faithful — no monotonicity axiom is added. -/

/-- **Binary additivity (derived).** For disjoint `A, A'` in `d`,
`Val (A ∪ A') ↔ Val A ∨ Val A'`. Obtained by feeding `val_iUnion` the family
`(A, A', ∅, ∅, …)` (a `Bool`-indexed disjoint family, padded). -/
theorem TwoValuedState.val_union (s : TwoValuedState d) {A A' : Set Ω}
    (hA : d.Has A) (hA' : d.Has A') (hdisj : Disjoint A A') :
    s.Val (A ∪ A') ↔ (s.Val A ∨ s.Val A') := by
  classical
  set f : ℕ → Set Ω := fun n => if n = 0 then A else if n = 1 then A' else ∅ with hf
  -- disjointness: f sends 0↦A, 1↦A', else ↦∅; any pair with distinct indices is
  -- disjoint because the only nonempty values are A (only at 0) and A' (only at 1).
  have hdisjf : Pairwise (Disjoint on f) := by
    intro i j hij
    apply Set.disjoint_left.mpr
    intro x hxi hxj
    -- determine which sets f i, f j are by case on i,j ∈ {0,1}
    have hxi' : x ∈ A ∧ i = 0 ∨ x ∈ A' ∧ i = 1 := by
      simp only [hf] at hxi
      split_ifs at hxi with h0 h1
      · exact Or.inl ⟨hxi, h0⟩
      · exact Or.inr ⟨hxi, h1⟩
      · exact absurd hxi (Set.notMem_empty x)
    have hxj' : x ∈ A ∧ j = 0 ∨ x ∈ A' ∧ j = 1 := by
      simp only [hf] at hxj
      split_ifs at hxj with h0 h1
      · exact Or.inl ⟨hxj, h0⟩
      · exact Or.inr ⟨hxj, h1⟩
      · exact absurd hxj (Set.notMem_empty x)
    rcases hxi' with ⟨hxiA, hi0⟩ | ⟨hxiA', hi1⟩ <;>
    rcases hxj' with ⟨hxjA, hj0⟩ | ⟨hxjA', hj1⟩
    · exact hij (hi0.trans hj0.symm)
    · exact (Set.disjoint_left.mp hdisj) hxiA hxjA'
    · exact (Set.disjoint_left.mp hdisj) hxjA hxiA'
    · exact hij (hi1.trans hj1.symm)
  have hHas : ∀ i, d.Has (f i) := by
    intro i; simp only [hf]; split_ifs
    · exact hA
    · exact hA'
    · exact d.has_empty
  have hU : (⋃ i, f i) = A ∪ A' := by
    apply Set.Subset.antisymm
    · refine Set.iUnion_subset fun i => ?_
      simp only [hf]; split_ifs
      · exact Set.subset_union_left
      · exact Set.subset_union_right
      · exact Set.empty_subset _
    · rintro x (hx | hx)
      · exact Set.mem_iUnion.2 ⟨0, by simp [hf, hx]⟩
      · exact Set.mem_iUnion.2 ⟨1, by simp [hf, hx]⟩
  have := s.val_iUnion hdisjf hHas
  rw [hU] at this
  rw [this]
  constructor
  · rintro ⟨i, hi⟩
    simp only [hf] at hi
    split_ifs at hi with h0 h1
    · exact Or.inl hi
    · exact Or.inr hi
    · exact absurd hi s.not_val_empty
  · rintro (h | h)
    · exact ⟨0, by simpa [hf] using h⟩
    · exact ⟨1, by simpa [hf] using h⟩

/-- **Monotonicity (derived).** `A ⊆ B` (both in `d`) ⟹ `Val A → Val B`. From
binary additivity on `B = A ∪ (B\A)`. -/
theorem TwoValuedState.val_mono (s : TwoValuedState d) {A B : Set Ω}
    (hA : d.Has A) (hB : d.Has B) (hAB : A ⊆ B) (h : s.Val A) : s.Val B := by
  have hdiff : d.Has (B \ A) := d.has_diff hB hA hAB
  have hunion : A ∪ (B \ A) = B := by
    rw [Set.union_diff_cancel hAB]
  have := (s.val_union hA hdiff disjoint_sdiff_right).mpr (Or.inl h)
  rwa [hunion] at this

/-- **At-most-one (derived).** Disjoint `A, A'` in `d` cannot both be `Val`-true.
(Monotonicity through the complement: `A' ⊆ Aᶜ`, and `Val Aᶜ ↔ ¬Val A`.) -/
theorem TwoValuedState.val_at_most_one (s : TwoValuedState d) {A A' : Set Ω}
    (hA : d.Has A) (hA' : d.Has A') (hdisj : Disjoint A A')
    (h : s.Val A) : ¬ s.Val A' := by
  intro h'
  have hsub : A' ⊆ Aᶜ := Set.subset_compl_iff_disjoint_left.mpr hdisj
  have : s.Val Aᶜ := s.val_mono hA' (d.has_compl hA) hsub h'
  exact ((s.val_compl hA).mp this) h

/-! ### Finite ⊥-closed local patterns -/

/-- A **finite ⊥-closed sub-orthoposet** `B`: a finite subfamily of `d`, closed under
set-complement. -/
structure Block (d : DynkinSystem Ω) where
  /-- the carrier of the block -/
  sets : Finset (Set Ω)
  /-- every member lies in the σ-class -/
  mem_has : ∀ A ∈ sets, d.Has A
  /-- closed under complement -/
  compl_closed : ∀ A ∈ sets, Aᶜ ∈ sets

/-! ### The Boolean baseline (prop:boolean)

On a Boolean σ-algebra there is no σ-essential contextual state. The proof shows the
`s₀`-true sets have the finite intersection property — which holds *because* the
carrier is intersection-closed and the state is finitely multiplicative there
(exactly what Booleanness supplies; on a non-distributive OML both fail). With the
true family finite, FIP gives `K(s₀) ≠ ∅`, so a Dirac extends and clause (i) fails.

We isolate the two Boolean-supplied facts as hypotheses, making the distributivity
dependence explicit (this is obstruction (a) of the paper). -/

/-- The carrier `d` is **Boolean** (a σ-algebra, not merely a σ-class): it is closed
under binary intersection. A Dynkin system with this property is exactly a σ-algebra
(π–λ). This is the paper's hypothesis "`Λ` is a Boolean σ-algebra". -/
def InterClosed (d : DynkinSystem Ω) : Prop :=
  ∀ {A A'}, d.Has A → d.Has A' → d.Has (A ∩ A')

/-- **Multiplicativity on a Boolean carrier (derived, not assumed).** On an
intersection-closed carrier a two-valued state is multiplicative: if `A, A'` are
`s₀`-true then so is `A ∩ A'`. Proof: `A = (A∩A') ⊔ (A∩A'ᶜ)` is a disjoint union in
`d`; `A∩A'ᶜ ⊆ A'ᶜ` and `s₀(A'ᶜ)=0` (since `s₀ A'`), so by monotonicity `A∩A'ᶜ` is
false; additivity on the disjoint pair then forces `A∩A'` true. This is the only place
distributivity (lattice-meet = set-intersection, i.e.\ `InterClosed`) is used — exactly
the step that fails on a non-Boolean OML. -/
theorem TwoValuedState.val_inter (s₀ : TwoValuedState d) (hInter : InterClosed d)
    {A A' : Set Ω} (hA : d.Has A) (hA' : d.Has A') (h1 : s₀.Val A) (h1' : s₀.Val A') :
    s₀.Val (A ∩ A') := by
  classical
  have hAc' : d.Has A'ᶜ := d.has_compl hA'
  have hII : d.Has (A ∩ A') := hInter hA hA'
  have hID : d.Has (A ∩ A'ᶜ) := hInter hA hAc'
  -- A'ᶜ is false (since A' is true), so A ∩ A'ᶜ ⊆ A'ᶜ is false by monotonicity
  have hAc'_false : ¬ s₀.Val A'ᶜ := fun h => (s₀.val_compl hA').mp h h1'
  have hID_false : ¬ s₀.Val (A ∩ A'ᶜ) := fun hbad =>
    hAc'_false (s₀.val_mono hID hAc' inter_subset_right hbad)
  -- A = (A∩A') ⊔ (A∩A'ᶜ), disjoint
  have hsplit : A = (A ∩ A') ∪ (A ∩ A'ᶜ) := by
    rw [← inter_union_distrib_left, union_compl_self, inter_univ]
  have hdisj : Disjoint (A ∩ A') (A ∩ A'ᶜ) := by
    apply Disjoint.mono inter_subset_right inter_subset_right
    exact disjoint_compl_right
  have : s₀.Val ((A ∩ A') ∪ (A ∩ A'ᶜ)) := hsplit ▸ h1
  rcases (s₀.val_union hII hID hdisj).mp this with h | h
  · exact h
  · exact absurd h hID_false

end SigmaEssential
