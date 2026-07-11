/-
# Theorem-lets R and P: what inner regularity is

Formalizes attack note §10b (proof-read SOUND s13+s14, receipt
`PROOF_READ_2026-07-10_attack_s10.md`); ratification kit item 3, gaps 3.1,
3.2 (two-valued instance), 3.6 (two-valued instance), and the Hausdorff
red-flag check of 3.1.

## PROVED (all axiom-free)
* `SetField` / `FieldState` — a FIELD of sets (finite closure only — R is a
  finitely additive statement; no σ-structure anywhere) and a two-valued
  finitely additive state on it, with the derived Boolean toolkit.
* **Theorem-let R (`dirac_forcing`; kit gap 3.1)**: a two-valued f.a. state
  on a field of subsets of a HAUSDORFF space satisfying the two-valued
  (8.1) has: `𝒦₁` (the value-1 in-field compacts) nonempty, `D = ⋂𝒦₁`
  nonempty — both as CONCLUSIONS, per the ✎s14 rewrite — and the state is
  `δ_ω` on the field for EVERY `ω ∈ D`. The FIP step is the machine-checked
  content: value-1 in-field compacts are ∩-stable (compact ∩ closed;
  Hausdorff makes compacts closed), finite intersections are value-1 hence
  nonempty, and compactness of a fixed member turns an empty total
  intersection into an empty finite one. NO σ-additivity anywhere.
* **Theorem-let P, two-valued instance (`cocountable_fails_81_at`; kit gap
  3.2)**: on an uncountable SECOND-COUNTABLE Hausdorff space (subsuming
  Polish — a strengthening), the co-countable state fails (8.1) at the
  specific set `F = X ∖ {x}`, `x` a condensation point. The topological
  content is machine-checked via `exists_condensation_point` (second
  countability + uncountability), REPLACING the note's Cantor–Bendixson
  route: "closed co-countable ⊇ perfect kernel" is consumed only at the
  chosen point, where "no countable open neighbourhood" suffices.
* **The all-Hausdorff strengthening, two-valued instance
  (`cocountable_fails_81_hausdorff`; kit gap 3.6)**: on ANY uncountable
  Hausdorff space the co-countable state fails (8.1) SOMEWHERE — the
  reduction to R (the state is no Dirac restriction), exactly as banked
  s14. (The general diffuse-mass `c ∈ (0,1)` version is real-valued
  measure theory — not formalized, stays ⟦HAND⟧ with the kit.)
* **The Hausdorff red flag (kit gap 3.1)**: on `CofiniteTopology X`
  (infinite `X`; NOT Hausdorff) with the finite/cofinite field and the
  cofinite state, every set is compact (`isCompact_cofiniteTopology`), the
  two-valued (8.1) holds (`cofinite_81_holds`), and the state is
  non-Dirac; hence — via R itself — `not_t2Space_cofiniteTopology`. The
  receipt's counterexample, machine-checked, plus the topology fact it
  implies.

## NOT formalized (recorded)
Kit gaps 3.3 (choice flag — witnessed moot in context), 3.4 (DW fn-29
verbatim reading), 3.5 (Maharam anatomy) are source-reading; no Lean
content exists for them. P's real-valued decomposition (`Σᵢaᵢδ_xᵢ + c·ν`)
is not encoded.

## Receipts
`#print axioms` at file end; everything `[propext, Classical.choice,
Quot.sound]`.
-/
import QuerySystem.MarczewskiTransport
import Mathlib.Topology.Separation.Hausdorff
import Mathlib.Topology.Bases
import Mathlib.Topology.Constructions

open Set Function

namespace SigmaEssential.Blocks

/-! ## §1. Fields of sets and two-valued f.a. states on them -/

/-- A **field of sets**: contains `univ`, closed under complement and
binary intersection (hence `∅`, unions, differences). Finite closure ONLY —
this is the honest hypothesis class of theorem-let R. -/
structure SetField (X : Type*) where
  /-- membership -/
  mem : Set X → Prop
  mem_univ : mem univ
  mem_compl : ∀ {A}, mem A → mem Aᶜ
  mem_inter : ∀ {A B}, mem A → mem B → mem (A ∩ B)

namespace SetField

variable {X : Type*} (F : SetField X)

theorem mem_empty : F.mem ∅ := by
  simpa using F.mem_compl F.mem_univ

theorem mem_union {A B : Set X} (hA : F.mem A) (hB : F.mem B) :
    F.mem (A ∪ B) := by
  have := F.mem_compl (F.mem_inter (F.mem_compl hA) (F.mem_compl hB))
  simpa [Set.compl_inter] using this

theorem mem_diff {A B : Set X} (hA : F.mem A) (hB : F.mem B) :
    F.mem (A \ B) := by
  rw [Set.diff_eq]
  exact F.mem_inter hA (F.mem_compl hB)

end SetField

/-- A **two-valued finitely additive state** on a field of sets. -/
structure FieldState {X : Type*} (F : SetField X) where
  /-- `Val A` means the state assigns `1` to `A`. -/
  Val : Set X → Prop
  val_univ : Val univ
  not_val_empty : ¬ Val ∅
  val_compl : ∀ {A}, F.mem A → (Val Aᶜ ↔ ¬ Val A)
  val_union : ∀ {A B}, F.mem A → F.mem B → Disjoint A B →
    (Val (A ∪ B) ↔ (Val A ∨ Val B))

namespace FieldState

variable {X : Type*} {F : SetField X} (ν : FieldState F)

theorem val_mono {A B : Set X} (hA : F.mem A) (hB : F.mem B) (hAB : A ⊆ B)
    (h : ν.Val A) : ν.Val B := by
  have hdiff : F.mem (B \ A) := F.mem_diff hB hA
  have hunion : A ∪ (B \ A) = B := Set.union_diff_cancel hAB
  have := (ν.val_union hA hdiff disjoint_sdiff_right).mpr (Or.inl h)
  rwa [hunion] at this

theorem val_at_most_one {A B : Set X} (hA : F.mem A) (hB : F.mem B)
    (hdisj : Disjoint A B) (h : ν.Val A) : ¬ ν.Val B := by
  intro h'
  have hsub : B ⊆ Aᶜ := Set.subset_compl_iff_disjoint_left.mpr hdisj
  exact (ν.val_compl hA).mp (ν.val_mono hB (F.mem_compl hA) hsub h') h

theorem val_inter {A B : Set X} (hA : F.mem A) (hB : F.mem B)
    (h1 : ν.Val A) (h2 : ν.Val B) : ν.Val (A ∩ B) := by
  have hII : F.mem (A ∩ B) := F.mem_inter hA hB
  have hID : F.mem (A ∩ Bᶜ) := F.mem_inter hA (F.mem_compl hB)
  have hBc_false : ¬ ν.Val Bᶜ := fun h => (ν.val_compl hB).mp h h2
  have hID_false : ¬ ν.Val (A ∩ Bᶜ) := fun hbad =>
    hBc_false (ν.val_mono hID (F.mem_compl hB) Set.inter_subset_right hbad)
  have hsplit : A = (A ∩ B) ∪ (A ∩ Bᶜ) := by
    rw [← Set.inter_union_distrib_left, Set.union_compl_self, Set.inter_univ]
  have hdisj : Disjoint (A ∩ B) (A ∩ Bᶜ) :=
    Disjoint.mono Set.inter_subset_right Set.inter_subset_right
      disjoint_compl_right
  rcases (ν.val_union hII hID hdisj).mp (hsplit ▸ h1) with h | h
  · exact h
  · exact absurd h hID_false

/-- Value-1 finite infs (over any finite index family). -/
theorem val_finsetInf {ι : Type*} {D : ι → Set X} {s : Finset ι}
    (hD : ∀ i ∈ s, F.mem (D i)) (hval : ∀ i ∈ s, ν.Val (D i)) :
    F.mem (s.inf D) ∧ ν.Val (s.inf D) := by
  classical
  induction s using Finset.cons_induction with
  | empty =>
    refine ⟨?_, ?_⟩ <;> simp only [Finset.inf_empty, Set.top_eq_univ]
    · exact F.mem_univ
    · exact ν.val_univ
  | cons a s ha ih =>
    rw [Finset.inf_cons]
    have ih' := ih (fun i hi => hD i (Finset.mem_cons_of_mem hi))
      (fun i hi => hval i (Finset.mem_cons_of_mem hi))
    exact ⟨F.mem_inter (hD a (Finset.mem_cons_self a s)) ih'.1,
      ν.val_inter (hD a (Finset.mem_cons_self a s)) ih'.1
        (hval a (Finset.mem_cons_self a s)) ih'.2⟩

end FieldState

/-! ## §2. Theorem-let R: (8.1) forces Dirac restrictions on Hausdorff -/

/-- **Maharam's (8.1), two-valued form**: every value-1 field member has a
value-1 COMPACT IN-FIELD subset (the `K ∈ 𝒜` membership DW's footnote 29
drops — kept here, exactly as in Maharam p. 145). -/
def InnerRegular81 {X : Type*} [TopologicalSpace X] (F : SetField X)
    (ν : FieldState F) : Prop :=
  ∀ E, F.mem E → ν.Val E → ∃ K, F.mem K ∧ IsCompact K ∧ K ⊆ E ∧ ν.Val K

/-- **Theorem-let R (Dirac forcing; attack note §10b).** On a Hausdorff
space, a two-valued FINITELY ADDITIVE state with (8.1) has nonempty
`𝒦₁ = {value-1 in-field compacts}`, nonempty `D = ⋂ 𝒦₁`, and equals `δ_ω`
on the field for every `ω ∈ D`. No σ-additivity used anywhere. -/
theorem dirac_forcing {X : Type*} [TopologicalSpace X] [T2Space X]
    (F : SetField X) (ν : FieldState F) (h81 : InnerRegular81 F ν) :
    ({K | F.mem K ∧ IsCompact K ∧ ν.Val K}).Nonempty ∧
    (⋂₀ {K | F.mem K ∧ IsCompact K ∧ ν.Val K}).Nonempty ∧
    ∀ ω ∈ ⋂₀ {K | F.mem K ∧ IsCompact K ∧ ν.Val K},
      ∀ E, F.mem E → (ν.Val E ↔ ω ∈ E) := by
  classical
  set 𝒦₁ : Set (Set X) := {K | F.mem K ∧ IsCompact K ∧ ν.Val K} with h𝒦₁
  -- 𝒦₁ is nonempty: (8.1) at the whole space
  obtain ⟨K₀, hK₀mem, hK₀cpt, _, hK₀val⟩ :=
    h81 univ F.mem_univ ν.val_univ
  have hK₀ : K₀ ∈ 𝒦₁ := ⟨hK₀mem, hK₀cpt, hK₀val⟩
  refine ⟨⟨K₀, hK₀⟩, ?_, ?_⟩
  · -- D ≠ ∅ : the FIP step
    rw [Set.nonempty_iff_ne_empty]
    intro hD
    -- K₀ is covered by the (open) complements of the members of 𝒦₁
    have hcover : K₀ ⊆ ⋃ K : ↥𝒦₁, (K.1)ᶜ := by
      intro x hx
      have hxD : x ∉ ⋂₀ 𝒦₁ := by
        rw [hD]
        exact Set.notMem_empty x
      have hex : ∃ K ∈ 𝒦₁, x ∉ K := by
        by_contra hcon
        push Not at hcon
        exact hxD (Set.mem_sInter.mpr fun K hK => hcon K hK)
      obtain ⟨K, hK, hxK⟩ := hex
      exact Set.mem_iUnion.mpr ⟨⟨K, hK⟩, hxK⟩
    obtain ⟨t, ht⟩ := hK₀cpt.elim_finite_subcover (fun K : ↥𝒦₁ => (K.1)ᶜ)
      (fun K => (K.2.2.1.isClosed).isOpen_compl) hcover
    -- but the corresponding finite intersection is value-1, hence nonempty
    have hinf := ν.val_finsetInf (D := fun K : ↥𝒦₁ => K.1) (s := t)
      (fun K _ => K.2.1) (fun K _ => K.2.2.2)
    have hval : ν.Val (K₀ ∩ t.inf fun K : ↥𝒦₁ => K.1) :=
      ν.val_inter hK₀mem hinf.1 hK₀val hinf.2
    have hne : (K₀ ∩ t.inf fun K : ↥𝒦₁ => K.1).Nonempty := by
      rw [Set.nonempty_iff_ne_empty]
      intro hcon
      exact ν.not_val_empty (hcon ▸ hval)
    obtain ⟨z, hzK₀, hzinf⟩ := hne
    obtain ⟨K, hKt, hzKc⟩ := Set.mem_iUnion₂.mp (ht hzK₀)
    exact hzKc ((Finset.inf_le hKt : _ ≤ K.1) hzinf)
  · -- Dirac agreement at every point of D
    intro ω hω E hE
    constructor
    · intro hval
      obtain ⟨K, hKmem, hKcpt, hKE, hKval⟩ := h81 E hE hval
      exact hKE (Set.mem_sInter.mp hω K ⟨hKmem, hKcpt, hKval⟩)
    · intro hωE
      by_contra hnval
      have hcval : ν.Val Eᶜ := (ν.val_compl hE).mpr hnval
      obtain ⟨K, hKmem, hKcpt, hKE, hKval⟩ :=
        h81 Eᶜ (F.mem_compl hE) hcval
      exact hKE (Set.mem_sInter.mp hω K ⟨hKmem, hKcpt, hKval⟩) hωE

/-! ## §3. The countable/co-countable field as a `SetField`, and the
co-countable state as a `FieldState` -/

/-- Bridge: a σ-field is in particular a field of sets. -/
def SetField.ofMeasurableSpace {X : Type*} (m : MeasurableSpace X) :
    SetField X where
  mem := m.MeasurableSet'
  mem_univ := MeasurableSet.univ (m := m)
  mem_compl h := MeasurableSet.compl (m := m) h
  mem_inter hA hB := MeasurableSet.inter (m := m) hA hB

/-- Bridge: a two-valued σ-additive state is in particular a two-valued
finitely additive field state. -/
def FieldState.ofTwoValued {X : Type*} {m : MeasurableSpace X}
    (ν : TwoValuedState (MeasurableSpace.DynkinSystem.ofMeasurableSpace m)) :
    FieldState (SetField.ofMeasurableSpace m) where
  Val := ν.Val
  val_univ := ν.val_univ
  not_val_empty := ν.not_val_empty
  val_compl hA := ν.val_compl hA
  val_union hA hB hdisj := ν.val_union hA hB hdisj

/-! ## §4. Theorem-let P (two-valued instance) and the all-Hausdorff
strengthening -/

/-- **Condensation points exist** in an uncountable second-countable space:
otherwise every point has a countable open neighbourhood, and a countable
basis makes the whole space a countable union of countable sets. -/
theorem exists_condensation_point {X : Type*} [TopologicalSpace X]
    [SecondCountableTopology X] [Uncountable X] :
    ∃ x : X, ∀ U : Set X, IsOpen U → x ∈ U → ¬ U.Countable := by
  by_contra h
  push Not at h
  obtain ⟨b, hbc, -, hbasis⟩ := TopologicalSpace.exists_countable_basis X
  have huniv : (univ : Set X).Countable := by
    have hcover : (univ : Set X) ⊆ ⋃₀ {s | s ∈ b ∧ s.Countable} := by
      intro x _
      obtain ⟨U, hUopen, hxU, hUc⟩ := h x
      obtain ⟨s, hs, hxs, hsU⟩ :=
        hbasis.exists_subset_of_mem_open hxU hUopen
      exact ⟨s, ⟨hs, hUc.mono hsU⟩, hxs⟩
    exact Set.Countable.mono hcover
      ((hbc.mono (Set.sep_subset _ _)).sUnion fun s hs => hs.2)
  exact not_countable (Set.countable_univ_iff.mp huniv)

/-- **Theorem-let P, two-valued instance (§10b; kit gap 3.2)** — on an
uncountable second-countable Hausdorff space (in particular any uncountable
Polish space), the co-countable state fails (8.1) AT the specific member
`F = X ∖ {x}`, `x` a condensation point: any compact in-field `K ⊆ F` is
closed with `x ∈ Kᶜ` open, so `Kᶜ` countable would contradict condensation
— `K` is countable and gets value 0. -/
theorem cocountable_fails_81_at {X : Type*} [TopologicalSpace X] [T2Space X]
    [SecondCountableTopology X] [Uncountable X] :
    ∃ E, (SetField.ofMeasurableSpace (cocountableMeasurableSpace X)).mem E ∧
      (FieldState.ofTwoValued (cocountableState X)).Val E ∧
      ∀ K, (SetField.ofMeasurableSpace (cocountableMeasurableSpace X)).mem K →
        IsCompact K → K ⊆ E →
          ¬ (FieldState.ofTwoValued (cocountableState X)).Val K := by
  obtain ⟨x, hx⟩ := exists_condensation_point (X := X)
  refine ⟨{x}ᶜ, Or.inr (by rw [compl_compl]; exact Set.countable_singleton x),
    by simp [FieldState.ofTwoValued, cocountableState], ?_⟩
  intro K _ hKcpt hKE hKval
  have hxKc : x ∈ Kᶜ := fun hxK => hKE hxK rfl
  exact hx Kᶜ hKcpt.isClosed.isOpen_compl hxKc hKval

/-- **The all-Hausdorff strengthening, two-valued instance (kit gap 3.6)**:
on ANY uncountable Hausdorff space, the co-countable state fails (8.1)
somewhere — by reduction to R: (8.1) would make it a Dirac restriction, but
it values every co-singleton 1. -/
theorem cocountable_fails_81_hausdorff {X : Type*} [TopologicalSpace X]
    [T2Space X] [Uncountable X] :
    ¬ InnerRegular81 (SetField.ofMeasurableSpace (cocountableMeasurableSpace X))
      (FieldState.ofTwoValued (cocountableState X)) := by
  intro h81
  obtain ⟨-, hDne, hpt⟩ := dirac_forcing _ _ h81
  obtain ⟨ω, hω⟩ := hDne
  obtain ⟨A, hA, hval, hnω⟩ := cocountableState_not_dirac X ω
  exact hnω ((hpt ω hω A hA).mp hval)

/-! ## §5. The Hausdorff red flag: the cofinite-topology counterexample

On `CofiniteTopology X` (`X` infinite; NOT Hausdorff) every subset is
compact, so the two-valued (8.1) holds trivially for the cofinite state on
the finite/cofinite field — yet the state is no Dirac restriction. R's
Hausdorff hypothesis is load-bearing; indeed R itself then proves the
space is not Hausdorff. -/

section Cofinite

variable (X : Type*) [Infinite X]

instance : Infinite (CofiniteTopology X) := ‹Infinite X›

omit [Infinite X] in
/-- Every subset of a cofinite-topology space is compact: one cover member
grabs a point, its complement is finite, finitely many more members finish. -/
theorem isCompact_cofiniteTopology (s : Set (CofiniteTopology X)) :
    IsCompact s := by
  classical
  refine isCompact_of_finite_subcover fun {ι} U hUopen hcover => ?_
  rcases Set.eq_empty_or_nonempty s with rfl | ⟨x, hx⟩
  · exact ⟨∅, by simp⟩
  obtain ⟨i₀, hi₀⟩ := Set.mem_iUnion.mp (hcover hx)
  have hfin : (s \ U i₀).Finite :=
    ((CofiniteTopology.isOpen_iff.mp (hUopen i₀)) ⟨x, hi₀⟩).subset
      fun y hy => hy.2
  have hex : ∀ y : ↥(s \ U i₀), ∃ i, (y : CofiniteTopology X) ∈ U i :=
    fun y => Set.mem_iUnion.mp (hcover y.2.1)
  choose f hf using hex
  haveI : Fintype ↥(s \ U i₀) := hfin.fintype
  refine ⟨insert i₀ (Finset.univ.image f), fun z hz => ?_⟩
  by_cases hzU : z ∈ U i₀
  · exact Set.mem_biUnion (Finset.mem_insert_self _ _) hzU
  · exact Set.mem_biUnion
      (Finset.mem_insert_of_mem
        (Finset.mem_image_of_mem f (Finset.mem_univ ⟨z, ⟨hz, hzU⟩⟩)))
      (hf ⟨z, ⟨hz, hzU⟩⟩)

/-- The finite/cofinite field. -/
def finiteCofiniteField : SetField (CofiniteTopology X) where
  mem A := A.Finite ∨ Aᶜ.Finite
  mem_univ := Or.inr (by simp)
  mem_compl h := by
    rcases h with h | h
    · exact Or.inr (by rwa [compl_compl])
    · exact Or.inl h
  mem_inter hA hB := by
    rcases hA with h | h
    · exact Or.inl (h.subset Set.inter_subset_left)
    · rcases hB with h' | h'
      · exact Or.inl (h'.subset Set.inter_subset_right)
      · exact Or.inr (by rw [Set.compl_inter]; exact h.union h')

variable {X}

theorem cofinite_not_both {A : Set (CofiniteTopology X)} (hA : A.Finite)
    (hAc : Aᶜ.Finite) : False := by
  have : (univ : Set (CofiniteTopology X)).Finite := by
    rw [← Set.union_compl_self A]
    exact hA.union hAc
  exact Set.infinite_univ (α := CofiniteTopology X) this

variable (X)

/-- The cofinite state: value 1 exactly on cofinite sets. -/
def cofiniteState : FieldState (finiteCofiniteField X) where
  Val A := Aᶜ.Finite
  val_univ := by simp
  not_val_empty := by
    simp only [Set.compl_empty]
    exact fun h => Set.infinite_univ (α := CofiniteTopology X) h
  val_compl {A} hA := by
    rw [compl_compl]
    constructor
    · exact fun h hc => cofinite_not_both h hc
    · intro h
      rcases hA with hc | hc
      · exact hc
      · exact absurd hc h
  val_union {A B} hA hB hdisj := by
    constructor
    · intro h
      by_contra hnone
      push Not at hnone
      have hAfin : A.Finite := by
        rcases hA with hc | hc
        · exact hc
        · exact absurd hc hnone.1
      have hBfin : B.Finite := by
        rcases hB with hc | hc
        · exact hc
        · exact absurd hc hnone.2
      exact cofinite_not_both (hAfin.union hBfin) h
    · rintro (h | h)
      · exact h.subset (by rw [Set.compl_union]; exact Set.inter_subset_left)
      · exact h.subset (by rw [Set.compl_union]; exact Set.inter_subset_right)

/-- **(8.1) holds trivially on the cofinite topology**: every set is its
own value-1 compact in-field witness. -/
theorem cofinite_81_holds :
    InnerRegular81 (finiteCofiniteField X) (cofiniteState X) :=
  fun E hE hval => ⟨E, hE, isCompact_cofiniteTopology X E, subset_rfl, hval⟩

/-- The cofinite state is no Dirac restriction. -/
theorem cofiniteState_not_dirac :
    ∀ ω : CofiniteTopology X, ∃ A,
      (finiteCofiniteField X).mem A ∧ (cofiniteState X).Val A ∧ ω ∉ A :=
  fun ω => ⟨{ω}ᶜ,
    Or.inr (by rw [compl_compl]; exact Set.finite_singleton ω),
    by simp [cofiniteState],
    fun h => h rfl⟩

/-- **The Hausdorff red-flag check, closed by R itself**: since (8.1) holds
and the cofinite state is non-Dirac, the cofinite topology on an infinite
set cannot be Hausdorff. (Corroborates that R's `T2Space` hypothesis is
load-bearing — drop it and the theorem is false.) -/
theorem not_t2Space_cofiniteTopology : ¬ T2Space (CofiniteTopology X) := by
  intro hT2
  obtain ⟨-, hDne, hpt⟩ := dirac_forcing _ _ (cofinite_81_holds X)
  obtain ⟨ω, hω⟩ := hDne
  obtain ⟨A, hA, hval, hnω⟩ := cofiniteState_not_dirac X ω
  exact hnω ((hpt ω hω A hA).mp hval)

end Cofinite

/-! ## §6. Receipts -/

#print axioms dirac_forcing
#print axioms exists_condensation_point
#print axioms cocountable_fails_81_at
#print axioms cocountable_fails_81_hausdorff
#print axioms isCompact_cofiniteTopology
#print axioms cofinite_81_holds
#print axioms not_t2Space_cofiniteTopology

end SigmaEssential.Blocks
