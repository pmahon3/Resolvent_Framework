import QuerySystem.ConcreteOMLPatterns

/-! # Relational boundary descent: compatible local-state gluing -/

open Set Function MeasurableSpace

namespace SigmaEssential.Blocks

variable {Ω : Type*} {d : DynkinSystem Ω} {M C : Set (Set Ω)}

/-- A two-valued state whose laws are required only inside one maximal block. -/
structure BlockState (d : DynkinSystem Ω) (M : Set (Set Ω)) where
  Val : Set Ω → Prop
  decVal : DecidablePred Val
  val_univ : Val univ
  not_val_empty : ¬ Val ∅
  val_compl : ∀ {A}, A ∈ M → (Val Aᶜ ↔ ¬ Val A)
  val_union : ∀ {A B}, A ∈ M → B ∈ M → Disjoint A B →
    (Val (A ∪ B) ↔ Val A ∨ Val B)
  val_iUnion : ∀ {f : ℕ → Set Ω}, Pairwise (Disjoint on f) →
    (∀ n, f n ∈ M) → (Val (⋃ n, f n) ↔ ∃ n, Val (f n))

attribute [instance] BlockState.decVal

/-- Restriction of a global σ-state to a maximal block. -/
def TwoValuedState.restrictBlock (ν : TwoValuedState d) (M : Set (Set Ω))
    (hM : IsMaxBlock d M) :
    BlockState d M where
  Val := ν.Val
  decVal := ν.decVal
  val_univ := ν.val_univ
  not_val_empty := ν.not_val_empty
  val_compl hA := ν.val_compl (hM.has hA)
  val_union hA hB hd := ν.val_union (hM.has hA) (hM.has hB) hd
  val_iUnion hd hf := ν.val_iUnion hd (fun n => hM.has (hf n))

/-- The local σ-state obtained by evaluating sets at a carrier point. -/
noncomputable def pointBlockState (ω : Ω) (M : Set (Set Ω))
    (hM : IsMaxBlock d M) : BlockState d M :=
  TwoValuedState.restrictBlock (dirac ω : TwoValuedState d) M hM

/-- Every carrier event is contained in a maximal block. -/
theorem exists_maxBlock_mem {A : Set Ω} (hA : d.Has A) :
    ∃ M, IsMaxBlock d M ∧ A ∈ M := by
  have hfam : IsCompatFamily d ({A} : Set (Set Ω)) := by
    refine ⟨?_, ?_⟩
    · intro B hB
      simpa only [Set.mem_singleton_iff] using hB ▸ hA
    · intro B hB C hC hne
      simp only [Set.mem_singleton_iff] at hB hC
      exact absurd (hB.trans hC.symm) hne
  obtain ⟨M, hsub, hM⟩ := exists_isMaxBlock_superset hfam
  exact ⟨M, hM, hsub (Set.mem_singleton A)⟩

/-- A family of local block states agrees on every block overlap. -/
def CompatibleBlockStates
    (u : ∀ M, IsMaxBlock d M → BlockState d M) : Prop :=
  ∀ M (hM : IsMaxBlock d M) C (hC : IsMaxBlock d C) A,
    A ∈ M → (A ∈ C → ((u M hM).Val A ↔ (u C hC).Val A))

/-- The existential presentation of the value glued from compatible local states. -/
def gluedVal (u : ∀ M, IsMaxBlock d M → BlockState d M) (A : Set Ω) : Prop :=
  ∃ M, ∃ hM : IsMaxBlock d M, A ∈ M ∧ (u M hM).Val A

theorem gluedVal_iff_local
    (u : ∀ M, IsMaxBlock d M → BlockState d M)
    (hu : CompatibleBlockStates u) (hM : IsMaxBlock d M) {A : Set Ω}
    (hA : A ∈ M) : gluedVal u A ↔ (u M hM).Val A := by
  constructor
  · rintro ⟨C, hC, hAC, hv⟩
    specialize hu C hC M hM A
    have hagree : (u C hC).Val A ↔ (u M hM).Val A := hu hAC hA
    exact hagree.mp hv
  · intro hv
    exact ⟨M, hM, hA, hv⟩

/-- **Compatible block-state gluing.** Overlap-compatible local σ-states
glue to a global σ-state. -/
noncomputable def glueBlockStates
    (u : ∀ M, IsMaxBlock d M → BlockState d M)
    (hu : CompatibleBlockStates u) : TwoValuedState d where
  Val := gluedVal u
  decVal := Classical.decPred _
  val_univ := by
    obtain ⟨M, hM, hmem⟩ := exists_maxBlock_mem d.has_univ
    exact (gluedVal_iff_local u hu hM hmem).mpr (u M hM).val_univ
  not_val_empty := by
    obtain ⟨M, hM, hmem⟩ := exists_maxBlock_mem d.has_empty
    rw [gluedVal_iff_local u hu hM hmem]
    exact (u M hM).not_val_empty
  val_compl := by
    intro A hA
    obtain ⟨M, hM, hAM⟩ := exists_maxBlock_mem hA
    have hAcM := hM.compl_mem hAM
    rw [gluedVal_iff_local u hu hM hAcM,
      gluedVal_iff_local u hu hM hAM]
    exact (u M hM).val_compl hAM
  val_iUnion := by
    intro f hdisj hf
    have hfam : IsCompatFamily d (Set.range f) := by
      constructor
      · rintro A ⟨n, rfl⟩
        exact hf n
      · rintro A ⟨i, rfl⟩ B ⟨j, rfl⟩ hne
        exact compat_of_disjoint (hdisj fun hij => hne (by rw [hij]))
    obtain ⟨M, hsub, hM⟩ := exists_isMaxBlock_superset hfam
    have hfi : ∀ n, f n ∈ M := fun n => hsub ⟨n, rfl⟩
    have huM : (⋃ n, f n) ∈ M := hM.iUnion_mem hdisj hfi
    rw [gluedVal_iff_local u hu hM huM]
    constructor
    · intro hv
      obtain ⟨n, hn⟩ := ((u M hM).val_iUnion hdisj hfi).mp hv
      exact ⟨n, (gluedVal_iff_local u hu hM (hfi n)).mpr hn⟩
    · rintro ⟨n, hn⟩
      apply ((u M hM).val_iUnion hdisj hfi).mpr
      exact ⟨n, (gluedVal_iff_local u hu hM (hfi n)).mp hn⟩

theorem glueBlockStates_agrees
    (u : ∀ M, IsMaxBlock d M → BlockState d M)
    (hu : CompatibleBlockStates u) (hM : IsMaxBlock d M) {A : Set Ω}
    (hA : A ∈ M) :
    (glueBlockStates u hu).Val A ↔ (u M hM).Val A :=
  gluedVal_iff_local u hu hM hA

/-! ## Finite traces and relational boundaries -/

/-- A finite trace of a finitely additive state inside a Boolean block is
realized by a carrier point. This is the finite augmented-boundary atom
argument in concrete form. -/
theorem finite_trace_dirac (hMeets : MeetsExist d) (μ : Amended.FinAddState d)
    (hM : IsMaxBlock d M) {s : Set (Set Ω)} (hs : s.Finite)
    (hsub : s ⊆ M) :
    ∃ ω : Ω, ∀ A ∈ s, (ω ∈ A ↔ μ.Val A) := by
  classical
  let t : Finset (Set Ω) := hs.toFinset
  let D : Set Ω → Set Ω := fun A => if μ.Val A then A else Aᶜ
  have hDmem : ∀ A ∈ t, D A ∈ M := by
    intro A hAt
    have hAs : A ∈ s := by simpa [t] using hAt
    by_cases hv : μ.Val A
    · simpa [D, hv] using hsub hAs
    · simpa [D, hv] using hM.compl_mem (hsub hAs)
  have hDval : ∀ A ∈ t, μ.Val (D A) := by
    intro A hAt
    have hAs : A ∈ s := by simpa [t] using hAt
    by_cases hv : μ.Val A
    · simpa [D, hv] using hv
    · have hc : μ.Val Aᶜ := (μ.val_compl (hM.has (hsub hAs))).mpr hv
      simpa [D, hv] using hc
  have hI := hM.val_finsetInf hMeets μ hDmem hDval
  have hne : (t.inf D : Set Ω).Nonempty := by
    rw [Set.nonempty_iff_ne_empty]
    intro he
    exact μ.not_val_empty (he ▸ hI.2)
  obtain ⟨ω, hω⟩ := hne
  refine ⟨ω, ?_⟩
  intro A hAs
  have hAt : A ∈ t := by simpa [t] using hAs
  have hωD : ω ∈ D A := by
    have hsubset : t.inf D ⊆ D A := Finset.inf_le hAt
    exact hsubset hω
  by_cases hv : μ.Val A
  · simp only [D, if_pos hv] at hωD
    exact ⟨fun _ => hv, fun _ => hωD⟩
  · simp only [D, if_neg hv, Set.mem_compl_iff] at hωD
    exact ⟨fun h => absurd h hωD, fun h => absurd h hv⟩

/-- Events shared by a maximal block with some other maximal block. The
Boolean boundary is generated by these events; when the generated boundary
is finite, this raw overlap family is finite as a subset of it. -/
def overlapEvents (d : DynkinSystem Ω) (M : Set (Set Ω)) : Set (Set Ω) :=
  {A | A ∈ M ∧ ∃ C, IsMaxBlock d C ∧ C ≠ M ∧ A ∈ C}

theorem overlapEvents_subset (M : Set (Set Ω)) : overlapEvents d M ⊆ M :=
  fun _ h => h.1

def augmentedTrace (d : DynkinSystem Ω) (B : Block d) (M : Set (Set Ω)) :
    Set (Set Ω) := overlapEvents d M ∪ (↑B.sets ∩ M)

theorem augmentedTrace_finite (B : Block d) {M : Set (Set Ω)}
    (hfin : (overlapEvents d M).Finite) :
    (augmentedTrace d B M).Finite :=
  hfin.union (B.sets.finite_toSet.inter_of_left M)

theorem augmentedTrace_subset (B : Block d) (M : Set (Set Ω)) :
    augmentedTrace d B M ⊆ M := by
  rintro A (hA | hA)
  · exact hA.1
  · exact hA.2

theorem exists_boundary_preserving_point (hMeets : MeetsExist d)
    (μ : Amended.FinAddState d) (B : Block d) (hM : IsMaxBlock d M)
    (hfin : (overlapEvents d M).Finite) :
    ∃ ω : Ω, ∀ A ∈ augmentedTrace d B M, (ω ∈ A ↔ μ.Val A) :=
  finite_trace_dirac hMeets μ hM (augmentedTrace_finite B hfin)
    (augmentedTrace_subset B M)

noncomputable def quarantinePoint (hMeets : MeetsExist d)
    (μ : Amended.FinAddState d) (B : Block d)
    (hfin : ∀ M, IsMaxBlock d M → (overlapEvents d M).Finite)
    (M : Set (Set Ω)) (hM : IsMaxBlock d M) : Ω :=
  Classical.choose (exists_boundary_preserving_point hMeets μ B hM (hfin M hM))

theorem quarantinePoint_agrees (hMeets : MeetsExist d)
    (μ : Amended.FinAddState d) (B : Block d)
    (hfin : ∀ M, IsMaxBlock d M → (overlapEvents d M).Finite)
    (hM : IsMaxBlock d M) {A : Set Ω} (hA : A ∈ augmentedTrace d B M) :
    (quarantinePoint hMeets μ B hfin M hM ∈ A ↔ μ.Val A) :=
  Classical.choose_spec
    (exists_boundary_preserving_point hMeets μ B hM (hfin M hM)) A hA

theorem quarantinePoints_compatible (hMeets : MeetsExist d)
    (μ : Amended.FinAddState d) (B : Block d)
    (hfin : ∀ M, IsMaxBlock d M → (overlapEvents d M).Finite) :
    CompatibleBlockStates
      (fun M hM => pointBlockState (quarantinePoint hMeets μ B hfin M hM) M hM) := by
  intro M hM C hC A hAM hAC
  by_cases hMC : M = C
  · subst C
    rfl
  · have hAbM : A ∈ overlapEvents d M := ⟨hAM, C, hC, fun h => hMC h.symm, hAC⟩
    have hAbC : A ∈ overlapEvents d C := ⟨hAC, M, hM, hMC, hAM⟩
    change (quarantinePoint hMeets μ B hfin M hM ∈ A ↔
      quarantinePoint hMeets μ B hfin C hC ∈ A)
    exact (quarantinePoint_agrees hMeets μ B hfin hM (Or.inl hAbM)).trans
      (quarantinePoint_agrees hMeets μ B hfin hC (Or.inl hAbC)).symm

/-- **Finite-interface quarantine.** Finite overlap interfaces force `Phi`.
A finite generated Boolean boundary implies this hypothesis since it contains
all raw overlap events. -/
theorem finite_interface_quarantine (hMeets : MeetsExist d)
    (hfin : ∀ M, IsMaxBlock d M → (overlapEvents d M).Finite) : Phi d := by
  intro B μ
  let u : ∀ M, IsMaxBlock d M → BlockState d M := fun M hM =>
    pointBlockState (quarantinePoint hMeets μ B hfin M hM) M hM
  have hu : CompatibleBlockStates u :=
    quarantinePoints_compatible hMeets μ B hfin
  let ν : TwoValuedState d := glueBlockStates u hu
  refine ⟨ν, ?_⟩
  intro A hAB
  obtain ⟨M, hM, hAM⟩ := exists_maxBlock_mem (B.mem_has A hAB)
  have hAt : A ∈ augmentedTrace d B M := Or.inr ⟨hAB, hAM⟩
  rw [show ν.Val A ↔ (u M hM).Val A from glueBlockStates_agrees u hu hM hAM]
  exact quarantinePoint_agrees hMeets μ B hfin hM hAt

/-- An abstract finite-boundary certificate. The paper's finite Boolean
algebra `∂M` supplies such a certificate by taking `F = ∂M`. -/
def HasFiniteBoundary (d : DynkinSystem Ω) : Prop :=
  ∀ M, IsMaxBlock d M → ∃ F : Set (Set Ω), F.Finite ∧ overlapEvents d M ⊆ F

/-- The theorem in the boundary-algebra formulation: any finite family
containing every overlap event is enough for quarantine. -/
theorem finite_boundary_quarantine (hMeets : MeetsExist d)
    (hboundary : HasFiniteBoundary d) : Phi d := by
  apply finite_interface_quarantine hMeets
  intro M hM
  obtain ⟨F, hF, hsub⟩ := hboundary M hM
  exact hF.subset hsub

#print axioms finite_boundary_quarantine
#print axioms finite_interface_quarantine
#print axioms quarantinePoints_compatible
#print axioms finite_trace_dirac

#print axioms glueBlockStates
#print axioms glueBlockStates_agrees

end SigmaEssential.Blocks
