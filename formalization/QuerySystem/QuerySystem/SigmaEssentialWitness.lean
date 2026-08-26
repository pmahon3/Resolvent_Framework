/-
# The σ-essential witness: definition, localization, Boolean baseline

The pattern is a **local** state on the block `B` (a `LocalState`), not a global
σ-additive `TwoValuedState`. That distinction is the whole encoding: a witness is
a pattern that coheres locally and admits no global σ-additive extension, so
typing it globally would make it extend itself and the predicate would be
unsatisfiable.

* `FinAddState d` — a global **finitely additive** two-valued state (pair
  additivity; finite-family additivity is derived, since a σ-class is closed under
  finite disjoint unions).
* `LocalState d B` — a two-valued pattern on the block `B`, constrained by
  complement-additivity inside `B` (the constraint the spine consumes; on the
  paper's blocks — Navara–Pták's and the witness's — complement pairs are exactly
  the additivity constraints that exist in `B`).
* `FinitelyCoherent` — clause (0): some global finitely additive state extends the
  pattern. `IsSigmaEssential` — coherent but with NO global σ-additive extension.
* `dirac_iff`, `localization` — the spine re-proved: witness ⟺
  (0) coherent ∧ (i) `K(s₀) = ∅` ∧ (ii) no non-Dirac σ-state extends.
* `boolean_baseline` (Prop 1.6) — on an intersection-closed (Boolean) carrier,
  coherence alone produces a Dirac extension; hence `boolean_no_witness`: no
  witness on a Boolean carrier. Coherence is what does the work, and it has to:
  without it the baseline needs block intersection-closure as a separate
  hypothesis, which is the hole `Omega7Counterexample` walks through.
-/
import QuerySystem.SigmaEssentialLocalization

open Set Function MeasurableSpace

namespace SigmaEssential

open SigmaEssential

variable {Ω : Type*} {d : DynkinSystem Ω}

/-! ## §1. Global finitely additive states -/

/-- A global **finitely additive** two-valued state on the σ-class `d`: normalized,
complement-additive, and additive over disjoint pairs in `d`. Finite-family
additivity follows (a σ-class is closed under finite disjoint unions), and
σ-additivity is NOT required — this is the object clause (0) quantifies over. -/
structure FinAddState (d : DynkinSystem Ω) where
  /-- `Val A` means the state assigns `1` to `A`. -/
  Val : Set Ω → Prop
  /-- decidability, as in `TwoValuedState` -/
  decVal : DecidablePred Val
  /-- normalization: the whole space is true -/
  val_univ : Val univ
  /-- the empty set is false -/
  not_val_empty : ¬ Val ∅
  /-- exactly one of `A`, `Aᶜ` holds -/
  val_compl : ∀ {A}, d.Has A → (Val Aᶜ ↔ ¬ Val A)
  /-- pair additivity over disjoint members -/
  val_union : ∀ {A A'}, d.Has A → d.Has A' → Disjoint A A' →
    (Val (A ∪ A') ↔ (Val A ∨ Val A'))

attribute [instance] FinAddState.decVal

namespace FinAddState

variable (μ : FinAddState d)

/-- Monotonicity, derived exactly as for `TwoValuedState`. -/
theorem val_mono {A B : Set Ω} (hA : d.Has A) (hB : d.Has B) (hAB : A ⊆ B)
    (h : μ.Val A) : μ.Val B := by
  have hdiff : d.Has (B \ A) := d.has_diff hB hA hAB
  have hunion : A ∪ (B \ A) = B := by rw [Set.union_diff_cancel hAB]
  have := (μ.val_union hA hdiff disjoint_sdiff_right).mpr (Or.inl h)
  rwa [hunion] at this

/-- Disjoint true sets cannot coexist. -/
theorem val_at_most_one {A A' : Set Ω} (hA : d.Has A) (hA' : d.Has A')
    (hdisj : Disjoint A A') (h : μ.Val A) : ¬ μ.Val A' := by
  intro h'
  have hsub : A' ⊆ Aᶜ := Set.subset_compl_iff_disjoint_left.mpr hdisj
  have : μ.Val Aᶜ := μ.val_mono hA' (d.has_compl hA) hsub h'
  exact ((μ.val_compl hA).mp this) h

/-- **Multiplicativity on an intersection-closed carrier** (the Boolean step),
same derivation as `TwoValuedState.val_inter`. `InterClosed` is the spine's
Boolean-carrier predicate. -/
theorem val_inter (hInter : InterClosed d)
    {A A' : Set Ω} (hA : d.Has A) (hA' : d.Has A') (h1 : μ.Val A) (h1' : μ.Val A') :
    μ.Val (A ∩ A') := by
  classical
  have hAc' : d.Has A'ᶜ := d.has_compl hA'
  have hII : d.Has (A ∩ A') := hInter hA hA'
  have hID : d.Has (A ∩ A'ᶜ) := hInter hA hAc'
  have hAc'_false : ¬ μ.Val A'ᶜ := fun h => (μ.val_compl hA').mp h h1'
  have hID_false : ¬ μ.Val (A ∩ A'ᶜ) := fun hbad =>
    hAc'_false (μ.val_mono hID hAc' inter_subset_right hbad)
  have hsplit : A = (A ∩ A') ∪ (A ∩ A'ᶜ) := by
    rw [← inter_union_distrib_left, union_compl_self, inter_univ]
  have hdisj : Disjoint (A ∩ A') (A ∩ A'ᶜ) := by
    apply Disjoint.mono inter_subset_right inter_subset_right
    exact disjoint_compl_right
  have : μ.Val ((A ∩ A') ∪ (A ∩ A'ᶜ)) := hsplit ▸ h1
  rcases (μ.val_union hII hID hdisj).mp this with h | h
  · exact h
  · exact absurd h hID_false

end FinAddState

/-- Every σ-additive state is in particular finitely additive. -/
def _root_.SigmaEssential.TwoValuedState.toFinAdd (s : TwoValuedState d) :
    FinAddState d where
  Val := s.Val
  decVal := s.decVal
  val_univ := s.val_univ
  not_val_empty := s.not_val_empty
  val_compl := s.val_compl
  val_union hA hA' hdisj := s.val_union hA hA' hdisj

/-! ## §2. Local patterns (the encoding fix) -/

/-- A **local** two-valued pattern on the block `B`: values constrained only by
complement-additivity inside `B`. This is the encoding (pattern as a
global σ-additive state). On the paper's blocks — the ⊥-closure of the Navara–Pták
triple and of the witness's cores — complement pairs are exactly the additivity
constraints that exist inside `B`, so this IS Def 1.2 restricted to `B` there. -/
structure LocalState (d : DynkinSystem Ω) (B : Block d) where
  /-- `Val A` means the pattern assigns `1` to `A`. -/
  Val : Set Ω → Prop
  /-- decidability -/
  decVal : DecidablePred Val
  /-- complement-additivity inside `B` -/
  val_compl : ∀ {A}, A ∈ B.sets → (Val Aᶜ ↔ ¬ Val A)

attribute [instance] LocalState.decVal

variable {B : Block d}

/-- A global finitely additive state **extends** the local pattern. -/
def ExtendsF (μ : FinAddState d) (s₀ : LocalState d B) : Prop :=
  ∀ A ∈ B.sets, (μ.Val A ↔ s₀.Val A)

/-- A global σ-additive state **extends** the local pattern. -/
def ExtendsS (s : TwoValuedState d) (s₀ : LocalState d B) : Prop :=
  ∀ A ∈ B.sets, (s.Val A ↔ s₀.Val A)

/-- Restriction of a global σ-additive state to a local pattern on `B`. -/
def TwoValuedState.restrictLocal (s : TwoValuedState d) (B : Block d) :
    LocalState d B where
  Val := s.Val
  decVal := s.decVal
  val_compl hA := s.val_compl (B.mem_has _ hA)

/-- The kernel of a local pattern: `⋂ {A ∈ B : s₀(A) = 1}`. -/
def kernel (s₀ : LocalState d B) : Set Ω :=
  ⋂₀ {A | A ∈ B.sets ∧ s₀.Val A}

/-- **dirac-iff, local form.** `δ_ω` extends `s₀` iff `ω ∈ K(s₀)`. Same proof as
the spine's `dirac_iff`, now consuming only the LOCAL complement-additivity. -/
theorem dirac_iff (s₀ : LocalState d B) (ω : Ω) :
    ExtendsS (dirac ω) s₀ ↔ ω ∈ kernel s₀ := by
  constructor
  · intro h
    rw [kernel, mem_sInter]
    rintro A ⟨hAB, hA1⟩
    exact ((h A hAB).mpr hA1)
  · intro hω
    intro A hAB
    by_cases hA : s₀.Val A
    · have : ω ∈ A := by
        rw [kernel, mem_sInter] at hω
        exact hω A ⟨hAB, hA⟩
      exact ⟨fun _ => hA, fun _ => this⟩
    · have hcB : Aᶜ ∈ B.sets := B.compl_closed A hAB
      have hc1 : s₀.Val Aᶜ := (s₀.val_compl hAB).mpr hA
      have hωc : ω ∈ Aᶜ := by
        rw [kernel, mem_sInter] at hω
        exact hω Aᶜ ⟨hcB, hc1⟩
      have hωnA : ω ∉ A := by simpa [mem_compl_iff] using hωc
      exact ⟨fun h => absurd h hωnA, fun h => absurd h hA⟩

/-- No Dirac extends `s₀` iff the kernel is empty. -/
theorem no_dirac_extends_iff_kernel_empty (s₀ : LocalState d B) :
    (¬ ∃ ω : Ω, ExtendsS (dirac ω) s₀) ↔ kernel s₀ = ∅ := by
  constructor
  · intro h
    rw [eq_empty_iff_forall_notMem]
    intro ω hω
    exact h ⟨ω, (dirac_iff s₀ ω).mpr hω⟩
  · intro h
    rintro ⟨ω, hω⟩
    have : ω ∈ kernel s₀ := (dirac_iff s₀ ω).mp hω
    rw [h] at this
    exact notMem_empty ω this

/-! ## §3. The σ-essential definition and localization -/

/-- Clause (0): the pattern is **finitely coherent** — some global finitely
additive two-valued state extends it (paper v2 `def:coherence`). -/
def FinitelyCoherent (s₀ : LocalState d B) : Prop :=
  ∃ μ : FinAddState d, ExtendsF μ s₀

/-- **σ-essential contextual state** (`def:sigma-essential`): finitely coherent,
but NO global σ-additive two-valued state extends it. -/
def IsSigmaEssential (s₀ : LocalState d B) : Prop :=
  FinitelyCoherent s₀ ∧ ¬ ∃ s : TwoValuedState d, ExtendsS s s₀

/-- Clause (ii): no non-Dirac σ-additive state extends. -/
def NoNonDiracExtends (s₀ : LocalState d B) : Prop :=
  ¬ ∃ s : TwoValuedState d, ¬ s.IsDirac ∧ ExtendsS s s₀

/-- **Localization** (`thm:localization`) — the three-clause form: witness ⟺
(0) coherent ∧ (i) `K(s₀)=∅` ∧ (ii) no non-Dirac σ-state extends. -/
theorem localization (s₀ : LocalState d B) :
    IsSigmaEssential s₀ ↔
      (FinitelyCoherent s₀ ∧ kernel s₀ = ∅ ∧ NoNonDiracExtends s₀) := by
  unfold IsSigmaEssential NoNonDiracExtends
  rw [← no_dirac_extends_iff_kernel_empty]
  constructor
  · rintro ⟨hcoh, h⟩
    refine ⟨hcoh, ?_, ?_⟩
    · rintro ⟨ω, hω⟩; exact h ⟨dirac ω, hω⟩
    · rintro ⟨s, _, hs⟩; exact h ⟨s, hs⟩
  · rintro ⟨hcoh, hDir, hNon⟩
    refine ⟨hcoh, ?_⟩
    rintro ⟨s, hs⟩
    by_cases hd : s.IsDirac
    · obtain ⟨ω, rfl⟩ := hd
      exact hDir ⟨ω, hs⟩
    · exact hNon ⟨s, hd, hs⟩

/-- **Ψ** — the existence sentence: some carrier, block and pattern is
σ-essential. Proved by the Product Ulam Carrier development (`Ulam.psi_ZFC`);
the surviving open form is the lattice one, `Ulam.PsiOML`. -/
def Psi : Prop :=
  ∃ (Ω : Type) (d : DynkinSystem Ω) (B : Block d) (s₀ : LocalState d B),
    IsSigmaEssential s₀

/-! ## §4. The Boolean baseline (Prop 1.6)

On an intersection-closed carrier, coherence alone produces a Dirac extension —
no block-intersection-closure hypothesis is needed. (Without coherence one
cannot state this: the
baseline needed the block itself intersection-closed, which is exactly the hole
the Ω₇ example exposes.) -/

/-- Fold the μ-true sets of `B` into a single μ-true set contained in all of them
(finite intersection via multiplicativity on a Boolean carrier). Shape follows the
spine's `fold_meet`. -/
private theorem fold_true_sets (hInter : InterClosed d)
    (μ : FinAddState d) (s : Finset (Set Ω)) (hs : ∀ A ∈ s, d.Has A ∧ μ.Val A) :
    ∃ M, μ.Val M ∧ (∀ A ∈ s, M ⊆ A) ∧ (s.Nonempty → d.Has M) := by
  classical
  induction s using Finset.induction with
  | empty =>
    exact ⟨univ, μ.val_univ, by simp, by simp⟩
  | @insert A t hA ih =>
    obtain ⟨hAd, hA1⟩ := hs A (Finset.mem_insert_self A t)
    obtain ⟨M, hM1, hMsub, hMd⟩ := ih (fun C hC => hs C (Finset.mem_insert_of_mem hC))
    rcases t.eq_empty_or_nonempty with rfl | htne
    · refine ⟨A, hA1, ?_, fun _ => hAd⟩
      intro C hC
      rcases Finset.mem_insert.1 hC with rfl | hCt
      · exact subset_rfl
      · exact absurd hCt (Finset.notMem_empty C)
    · refine ⟨M ∩ A, μ.val_inter hInter (hMd htne) hAd hM1 hA1, ?_,
        fun _ => hInter (hMd htne) hAd⟩
      intro C hC
      rcases Finset.mem_insert.1 hC with rfl | hCt
      · exact inter_subset_right
      · exact inter_subset_left.trans (hMsub C hCt)

/-- **Boolean baseline (Prop 1.6).** On an intersection-closed (Boolean)
carrier, a finitely coherent local pattern has nonempty kernel — a Dirac extends
it. Coherence does the work distributivity converts into a point. -/
theorem boolean_baseline (hInter : InterClosed d)
    (s₀ : LocalState d B) (hcoh : FinitelyCoherent s₀) :
    ∃ ω : Ω, ExtendsS (dirac ω) s₀ := by
  classical
  obtain ⟨μ, hμ⟩ := hcoh
  -- the μ-true (= s₀-true) sets of B
  set T : Finset (Set Ω) := B.sets.filter (fun A => μ.Val A) with hT
  have hTmem : ∀ A ∈ T, d.Has A ∧ μ.Val A := by
    intro A hA
    rw [hT, Finset.mem_filter] at hA
    exact ⟨B.mem_has _ hA.1, hA.2⟩
  obtain ⟨M, hM1, hMsub, _⟩ := fold_true_sets hInter μ T hTmem
  have hMne : M.Nonempty := by
    rw [nonempty_iff_ne_empty]
    rintro rfl
    exact μ.not_val_empty hM1
  obtain ⟨x, hxM⟩ := hMne
  refine ⟨x, (dirac_iff s₀ x).mpr ?_⟩
  rw [kernel, mem_sInter]
  rintro A ⟨hAB, hA1⟩
  have hAT : A ∈ T := by
    rw [hT, Finset.mem_filter]
    exact ⟨hAB, (hμ A hAB).mpr hA1⟩
  exact hMsub A hAT hxM

/-- **No witness on a Boolean carrier (Prop 2.1, machine-checked).** The
meaningfulness certificate for the new encoding: with coherence in the definition,
the Boolean baseline is restored — no `BooleanLocal` crutch, no Ω₇ hole. -/
theorem boolean_no_witness (hInter : InterClosed d)
    (s₀ : LocalState d B) : ¬ IsSigmaEssential s₀ := by
  rintro ⟨hcoh, hno⟩
  obtain ⟨ω, hω⟩ := boolean_baseline hInter s₀ hcoh
  exact hno ⟨dirac ω, hω⟩

end SigmaEssential
