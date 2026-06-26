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

/-- A state `s` **extends** the local pattern `s₀` on `B` if they agree on every member
of `B`. -/
def Extends (s s₀ : TwoValuedState d) (B : Block d) : Prop :=
  ∀ A ∈ B.sets, (s.Val A ↔ s₀.Val A)

/-- The **kernel** `K(s₀) = ⋂ {A ∈ B : s₀(A) = 1}`: the intersection of the
`s₀`-true members of `B`. -/
def kernel (s₀ : TwoValuedState d) (B : Block d) : Set Ω :=
  ⋂₀ {A | A ∈ B.sets ∧ s₀.Val A}

variable (s₀ : TwoValuedState d) (B : Block d)

/-- **Lemma (dirac-iff).** A point evaluation `δ_ω` extends `s₀` on `B` iff
`ω ∈ K(s₀)`.

Forward: if `δ_ω` agrees with `s₀` on `B`, then for each `s₀`-true `A` we get
`ω ∈ A`, so `ω ∈ K`. Backward: if `ω ∈ K` then `ω` lies in every `s₀`-true set;
for an `s₀`-false `A`, ⊥-closure puts `Aᶜ ∈ B` and complement-additivity makes
`Aᶜ` true, so `ω ∈ Aᶜ`, i.e. `ω ∉ A` — the false constraints are subsumed. -/
theorem dirac_iff (ω : Ω) :
    Extends (dirac ω) s₀ B ↔ ω ∈ kernel s₀ B := by
  constructor
  · -- δ_ω extends s₀  ⟹  ω ∈ K
    intro h
    rw [kernel, mem_sInter]
    rintro A ⟨hAB, hA1⟩
    -- agreement at A: (ω ∈ A) ↔ s₀.Val A; and s₀.Val A holds
    have := (h A hAB)
    -- (dirac ω).Val A is definitionally (ω ∈ A)
    exact (this.mpr hA1)
  · -- ω ∈ K  ⟹  δ_ω extends s₀
    intro hω
    rw [Extends]
    intro A hAB
    -- show (ω ∈ A) ↔ s₀.Val A
    by_cases hA : s₀.Val A
    · -- A is s₀-true: it is one of the intersected sets, so ω ∈ A
      have : ω ∈ A := by
        rw [kernel, mem_sInter] at hω
        exact hω A ⟨hAB, hA⟩
      simp only [dirac]
      exact ⟨fun _ => hA, fun _ => this⟩
    · -- A is s₀-false: Aᶜ ∈ B and is s₀-true, so ω ∈ Aᶜ, i.e. ω ∉ A
      have hcB : Aᶜ ∈ B.sets := B.compl_closed A hAB
      have hcHas : d.Has Aᶜ := B.mem_has _ hcB
      have hAHas : d.Has A := B.mem_has _ hAB
      have hc1 : s₀.Val Aᶜ := (s₀.val_compl hAHas).mpr hA
      have hωc : ω ∈ Aᶜ := by
        rw [kernel, mem_sInter] at hω
        exact hω Aᶜ ⟨hcB, hc1⟩
      have hωnA : ω ∉ A := by simpa [mem_compl_iff] using hωc
      simp only [dirac]
      exact ⟨fun h => absurd h hωnA, fun h => absurd h hA⟩

include d in
/-- **Corollary.** No Dirac extends `s₀` iff `K(s₀) = ∅`. -/
theorem no_dirac_extends_iff_kernel_empty :
    (¬ ∃ ω : Ω, Extends (dirac ω) s₀ B) ↔ kernel s₀ B = ∅ := by
  constructor
  · intro h
    rw [eq_empty_iff_forall_notMem]
    intro ω hω
    exact h ⟨ω, (dirac_iff s₀ B ω).mpr hω⟩
  · intro h
    rintro ⟨ω, hω⟩
    have : ω ∈ kernel s₀ B := (dirac_iff s₀ B ω).mp hω
    rw [h] at this
    exact notMem_empty ω this

end SigmaEssential
