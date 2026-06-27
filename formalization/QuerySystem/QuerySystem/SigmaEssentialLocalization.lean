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

/-! ### The Localization Theorem -/

/-- `s₀` is a **σ-essential contextual state** if it extends to *no* global state
(Dirac or non-Dirac). -/
def IsSigmaEssential (s₀ : TwoValuedState d) (B : Block d) : Prop :=
  ¬ ∃ s : TwoValuedState d, Extends s s₀ B

/-- Clause **(ii)**: no *non-Dirac* state extends `s₀`. -/
def NoNonDiracExtends (s₀ : TwoValuedState d) (B : Block d) : Prop :=
  ¬ ∃ s : TwoValuedState d, ¬ s.IsDirac ∧ Extends s s₀ B

include d in
/-- **Localization Theorem.** `s₀` is σ-essential iff
**(i)** `K(s₀) = ∅` (no Dirac extends) *and* **(ii)** no non-Dirac state extends.

The content is the exhaustive Dirac/non-Dirac partition: "no global state extends"
is equivalent to "no Dirac extends ∧ no non-Dirac extends", and the first conjunct
is `K(s₀) = ∅` by `dirac-iff`. -/
theorem localization :
    IsSigmaEssential s₀ B ↔ (kernel s₀ B = ∅ ∧ NoNonDiracExtends s₀ B) := by
  rw [IsSigmaEssential, NoNonDiracExtends, ← no_dirac_extends_iff_kernel_empty]
  constructor
  · -- no state extends ⟹ (no Dirac) ∧ (no non-Dirac)
    intro h
    refine ⟨?_, ?_⟩
    · rintro ⟨ω, hω⟩; exact h ⟨dirac ω, hω⟩
    · rintro ⟨s, _, hs⟩; exact h ⟨s, hs⟩
  · -- (no Dirac) ∧ (no non-Dirac) ⟹ no state extends
    rintro ⟨hDir, hNon⟩ ⟨s, hs⟩
    by_cases hd : s.IsDirac
    · obtain ⟨ω, rfl⟩ := hd
      exact hDir ⟨ω, hs⟩
    · exact hNon ⟨s, hd, hs⟩

/-! ### The Boolean baseline (prop:boolean)

On a Boolean σ-algebra there is no σ-essential contextual state. The proof shows the
`s₀`-true sets have the finite intersection property — which holds *because* the
carrier is intersection-closed and the state is finitely multiplicative there
(exactly what Booleanness supplies; on a non-distributive OML both fail). With the
true family finite, FIP gives `K(s₀) ≠ ∅`, so a Dirac extends and clause (i) fails.

We isolate the two Boolean-supplied facts as hypotheses, making the distributivity
dependence explicit (this is obstruction (a) of the paper). -/

/-- `B` is **multiplicative for `s₀`**: the carrier is closed under the binary
intersections of `s₀`-true members, and `s₀` is multiplicative there
(`s₀(A∩A')=1` when both are true). Both hold on a Boolean σ-algebra; both fail on a
non-distributive OML (lattice meet ≠ set intersection). -/
def BooleanLocal (s₀ : TwoValuedState d) (B : Block d) : Prop :=
  ∀ A A', A ∈ B.sets → A' ∈ B.sets → s₀.Val A → s₀.Val A' →
    (A ∩ A') ∈ B.sets ∧ s₀.Val (A ∩ A')

/-- **FIP core.** A finite family of `s₀`-true sets, closed under binary intersection
with the intersection staying `s₀`-true, "folds" to a single `s₀`-true set contained
in every member. (The Boolean multiplicative closure, applied finitely.)

We do not assert the fold lies in `B` — the empty fold is `univ`, possibly outside
`B` — but it is `s₀`-true and `⊆` every member, which is all the caller needs.
The fold *of a nonempty family* does lie in `B`; we carry the `B`-membership only as
an auxiliary so the inductive `s₀`-multiplicativity step has something to apply. -/
theorem fold_meet (s₀ : TwoValuedState d) (B : Block d) (hBool : BooleanLocal s₀ B)
    (s : Finset (Set Ω)) (hs : ∀ A ∈ s, A ∈ B.sets ∧ s₀.Val A) :
    ∃ M, s₀.Val M ∧ (∀ A ∈ s, M ⊆ A) ∧ (s.Nonempty → M ∈ B.sets) := by
  classical
  induction s using Finset.induction with
  | empty =>
    exact ⟨univ, by simp [TwoValuedState.val_univ], by simp, by simp⟩
  | @insert A t hA ih =>
    obtain ⟨hAB, hA1⟩ := hs A (Finset.mem_insert_self A t)
    obtain ⟨M, hM1, hMsub, hMB⟩ := ih (fun C hC => hs C (Finset.mem_insert_of_mem hC))
    rcases t.eq_empty_or_nonempty with rfl | htne
    · -- fold over {A}: just A
      refine ⟨A, hA1, ?_, fun _ => hAB⟩
      intro C hC
      rcases Finset.mem_insert.1 hC with rfl | hCt
      · exact subset_rfl
      · exact absurd hCt (Finset.notMem_empty C)
    · -- fold over insert A t (t nonempty): M ∈ B, apply multiplicativity to M ∩ A
      obtain ⟨hInterB, hInter1⟩ := hBool M A (hMB htne) hAB hM1 hA1
      refine ⟨M ∩ A, hInter1, ?_, fun _ => hInterB⟩
      intro C hC
      rcases Finset.mem_insert.1 hC with rfl | hCt
      · exact inter_subset_right
      · exact inter_subset_left.trans (hMsub C hCt)

include d in
/-- **Proposition (Boolean baseline).** If `B` is multiplicative for `s₀` (the
Boolean case) then the `s₀`-true family has the finite intersection property, so
`K(s₀) ≠ ∅`, so a Dirac extends `s₀` — `s₀` is **not** σ-essential. -/
theorem boolean_not_sigma_essential (hBool : BooleanLocal s₀ B) :
    ¬ IsSigmaEssential s₀ B := by
  classical
  -- the s₀-true subfamily of B
  set T : Finset (Set Ω) := B.sets.filter (fun A => s₀.Val A) with hT
  have hTmem : ∀ A ∈ T, A ∈ B.sets ∧ s₀.Val A := by
    intro A hA; rw [hT, Finset.mem_filter] at hA; exact hA
  -- fold the true family to a single s₀-true M ⊆ every true set
  obtain ⟨M, hM1, hMsub, _⟩ := fold_meet s₀ B hBool T hTmem
  -- M is s₀-true ⟹ M ≠ ∅ (since s₀ ∅ = False) ⟹ pick x ∈ M ⊆ K(s₀)
  have hMne : M.Nonempty := by
    rw [nonempty_iff_ne_empty]; rintro rfl; exact s₀.not_val_empty hM1
  obtain ⟨x, hxM⟩ := hMne
  have hxK : x ∈ kernel s₀ B := by
    rw [kernel, mem_sInter]
    rintro A ⟨hAB, hA1⟩
    exact hMsub A (by rw [hT, Finset.mem_filter]; exact ⟨hAB, hA1⟩) hxM
  intro hess
  exact hess ⟨dirac x, (dirac_iff s₀ B x).mpr hxK⟩

/-! ### Clause (i) is freely arrangeable (Navara–Pták)

The Localization Theorem isolates that clause (i) `K(s₀) = ∅` carries no
difficulty: it is *freely arrangeable*. The witness is the **Navara–Pták 1983**
example — a concrete σ-class on `ℚ₀ × ℚ₀` with a local pattern whose true sets have
empty intersection (`C_f ∩ C_g ∩ C_{f+g} = ∅`). This is a *cited published example*,
not a result of ours, so we axiomatize its existence (per the programme's "don't
formalize known results; `axiom` with citation" rule). Formalizing the ℚ²
construction is possible but adds rigor where it is not needed.

Reference: Navara & Pták, *Two-valued measures on σ-classes*, Čas. Pěst. Mat. 108
(1983) 225–229. -/
axiom navara_ptak_kernel_empty :
    ∃ (Ω : Type) (d : DynkinSystem Ω) (s₀ : TwoValuedState d) (B : Block d),
      kernel s₀ B = ∅

/-- **Clause (i) is freely arrangeable** (immediate from the Navara–Pták axiom):
there is a carrier and a local pattern with no Dirac extension. -/
theorem kernel_empty_arrangeable :
    ∃ (Ω : Type) (d : DynkinSystem Ω) (s₀ : TwoValuedState d) (B : Block d),
      ¬ ∃ ω : Ω, Extends (dirac ω) s₀ B := by
  obtain ⟨Ω, d, s₀, B, hK⟩ := navara_ptak_kernel_empty
  exact ⟨Ω, d, s₀, B, (no_dirac_extends_iff_kernel_empty s₀ B).mpr hK⟩

end SigmaEssential
