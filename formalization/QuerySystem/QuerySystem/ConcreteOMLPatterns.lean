/-
# The B′(i) reduction ladder: patterns, clusters, P⁼, T4, Φ-density

Formalizes attack note §11a–§11d and §11f (proof-read SOUND at s12 standard,
receipt `PROOF_READ_2026-07-11_attack_s11.md`); ratification kit item 4,
gaps 4.1, 4.2, and the clean half of 4.5. Patterns enter as finite
⊥-closed `Block`s
with values read off a global state — never as global states in disguise
(the encoding-defect discipline).

## PROVED (all axiom-free)
* Conversions: `FinAddState.toTwoValued` (a f.a. state satisfying the
  global σ-condition IS a σ-state), `TwoValuedState.isSigmaOn_toFinAdd`.
* **P⁼ (§11c / kit gap 4.1)**, split honestly:
  - (⟸, `isSigmaOn_of_blockwisePointed`) blockwise-pointed ⟹ σ-additive —
    NO countable generation, NO latticehood (the banked sharpening);
  - (⟹, `blockwisePointed_of_isSigmaOn`) σ-additive ⟹ every block kernel
    nonempty — needs `MeetsExist` + countably generated blocks (T3);
  - `pointed_iff_sigma` — the iff, and `phiCluster_iff_pointedSelection`
    (σ-selections = pointed selections, the "B′(i) is a pure selection
    problem" reading).
* **2BR (§11a, `two_block_rescue`)**: a pattern whose value-1 part lies in
  two maximal blocks is Dirac-rescued. The only use of latticehood is
  in-block ∩-closure (A2), exactly as the note says.
* **Cluster machinery (§11b)**: `FACoherentCluster`, `PhiCluster`,
  `phi_iff_phiCluster` (Φ ⟺ the cluster form — latticehood-free both
  ways), `cluster_extension` (a σ-state ≡ 1 on a cluster dominating the
  value-1 part of a pattern reproduces the whole trace: monotonicity +
  ⊥-closure).
* **The ladder's named targets (§11f)**: `Phi`, `BPrimeI` (open), `T4At`/
  `T4` (open), `IsAtomOf`, and the PROVED necessity direction
  `t4At_of_phi` / `bPrimeI_implies_T4`: B′(i) ⟹ T4 — the σ-extension
  points every block (P⁼/T3) and the T3 kernel IS an atom of the block.
  The converse (T4 + completion principle ⟹ B′(i)) is OPEN — the s16
  scope note stands; nothing here claims it.
* **Φ-density (§11d / kit gap 4.2)**: states are points of the Cantor cube
  `↥(Carrier d) → Bool`; `phi_iff_dense`: Φ ⟺ σ-states are dense in the
  f.a. states. Plus the bank: `isClosed_stFA` (the f.a. states are exactly
  the closed constraint set — kit gap 4.2(a), with the onto/"nonempty
  trace" reading built into the proof) and `isCompact_stFA` (Tychonoff —
  BPI-strength, fine in ZFC, flagged per the kit).

## Open Props (named, never `sorry`)
`BPrimeI`, `T4` (global, universe-polymorphic) and their per-carrier forms.
The crux (one-block repointing at arbitrary support) is NOT stated as a
theorem anywhere — kit gap 4.5's red flag respected.

## Receipts
`#print axioms` at file end; everything `[propext, Classical.choice,
Quot.sound]`.
-/
import QuerySystem.MarczewskiTransport
import Mathlib.Topology.Constructions
import Mathlib.Topology.Separation.Basic

open Set Function MeasurableSpace

namespace SigmaEssential.Blocks

variable {Ω : Type*} {d : DynkinSystem Ω} {A B : Set Ω} {M : Set (Set Ω)}

/-! ## §1. Conversions between the σ- and f.a. state types -/

/-- A finitely additive state satisfying the GLOBAL σ-condition is a
σ-additive state. -/
def _root_.SigmaEssential.FinAddState.toTwoValued
    (μ : FinAddState d) (h : IsSigmaOn μ (Carrier d)) :
    TwoValuedState d where
  Val := μ.Val
  decVal := μ.decVal
  val_univ := μ.val_univ
  not_val_empty := μ.not_val_empty
  val_compl := μ.val_compl
  val_iUnion hdisj hf := h _ hdisj hf

/-- Conversely, a σ-additive state is finitely additive with the global
σ-condition. -/
theorem _root_.SigmaEssential.TwoValuedState.isSigmaOn_toFinAdd
    (ν : TwoValuedState d) : IsSigmaOn ν.toFinAdd (Carrier d) :=
  fun _ hdisj hf => ν.val_iUnion hdisj hf

/-! ## §2. Block kernels and P⁼ -/

/-- The **kernel** of a state on a block: the intersection of its value-1
members (`D_Bl` of the note). -/
def blockKernel (μ : FinAddState d) (M : Set (Set Ω)) : Set Ω :=
  ⋂₀ {A | A ∈ M ∧ μ.Val A}

/-- A state is **blockwise pointed** if every maximal block's kernel is
inhabited. -/
def BlockwisePointed (μ : FinAddState d) : Prop :=
  ∀ M, IsMaxBlock d M → (blockKernel μ M).Nonempty

/-- All maximal blocks are countably generated (as the σ-fields A2 makes
them). The hypothesis of B′(i) and of P⁼'s forward leg. -/
def CountablyGeneratedBlocks (d : DynkinSystem Ω) (hMeets : MeetsExist d) :
    Prop :=
  ∀ M (hM : IsMaxBlock d M), ∃ G : ℕ → Set Ω,
    hM.toMeasurableSpace hMeets = MeasurableSpace.generateFrom (Set.range G)

/-- **P⁼, backward leg (§11c; kit gap 4.1(c))** — blockwise-pointed states
are σ-additive. NO countable generation and NO latticehood: of a disjoint
union covering the kernel point, exactly one member absorbs it, and
blockwise σ globalizes by A1c. -/
theorem isSigmaOn_of_blockwisePointed (μ : FinAddState d)
    (h : BlockwisePointed μ) : IsSigmaOn μ (Carrier d) := by
  rw [isSigmaOn_carrier_iff_maxBlocks]
  intro M hM f hdisj hf
  have hu : (⋃ n, f n) ∈ M := hM.iUnion_mem hdisj hf
  constructor
  · intro hval
    obtain ⟨ω, hω⟩ := h M hM
    have hωu : ω ∈ ⋃ n, f n := Set.mem_sInter.mp hω _ ⟨hu, hval⟩
    obtain ⟨k, hk⟩ := Set.mem_iUnion.mp hωu
    refine ⟨k, ?_⟩
    by_contra hnk
    have hkc : μ.Val (f k)ᶜ := (μ.val_compl (hM.has (hf k))).mpr hnk
    exact Set.mem_sInter.mp hω _ ⟨hM.compl_mem (hf k), hkc⟩ hk
  · rintro ⟨n, hn⟩
    exact μ.val_mono (hM.has (hf n)) (hM.has hu) (Set.subset_iUnion f n) hn

/-- **P⁼, forward leg (§11c; kit gap 4.1(a))** — σ-additive states are
blockwise pointed on countably generated blocks (T3 run on a countable
generating family; the kernel contains the T3 witness set). -/
theorem blockwisePointed_of_isSigmaOn (hMeets : MeetsExist d)
    (hgen : CountablyGeneratedBlocks d hMeets) (μ : FinAddState d)
    (hσ : IsSigmaOn μ (Carrier d)) : BlockwisePointed μ := by
  intro M hM
  obtain ⟨G, hG⟩ := hgen M hM
  obtain ⟨D, hD, hDne, hDval, hiff, hpt⟩ :=
    hM.dirac_realization hMeets (μ.toTwoValued hσ) G hG
  obtain ⟨ω, hω⟩ := hDne
  exact ⟨ω, Set.mem_sInter.mpr fun A hA => (hpt ω hω A hA.1).mp hA.2⟩

/-- **P⁼ (theorem-let, §11c).** On carriers with countably generated
blocks: σ-additive ⟺ blockwise pointed. `St_σ` = coherent atomic
selections; B′(i) is a pure selection problem. -/
theorem pointed_iff_sigma (hMeets : MeetsExist d)
    (hgen : CountablyGeneratedBlocks d hMeets) (μ : FinAddState d) :
    IsSigmaOn μ (Carrier d) ↔ BlockwisePointed μ :=
  ⟨blockwisePointed_of_isSigmaOn hMeets hgen μ,
    isSigmaOn_of_blockwisePointed μ⟩

/-! ## §3. Φ, clusters, and the cluster reduction -/

/-- **Φ, the conjectured property** (the corpus's finite-trace
σ-liftability): every finite trace of a finitely additive two-valued state
is reproduced by some σ-additive two-valued state. -/
def Phi (d : DynkinSystem Ω) : Prop :=
  ∀ (B : Block d) (μ : FinAddState d),
    ∃ ν : TwoValuedState d, ∀ A ∈ B.sets, (ν.Val A ↔ μ.Val A)

/-- A finite carrier family that some f.a. state values 1 throughout —
the "f.a.-coherent cluster" of §11b (normal-form optimizations like
pairwise incompatibility are NOT built in; they are reductions, not part
of the notion). -/
def FACoherentCluster (d : DynkinSystem Ω) (𝒞 : Finset (Set Ω)) : Prop :=
  (∀ E ∈ 𝒞, d.Has E) ∧ ∃ μ : FinAddState d, ∀ E ∈ 𝒞, μ.Val E

/-- **Φ, cluster form** (§11b): every f.a.-coherent cluster carries a
σ-state that is 1 on it. -/
def PhiCluster (d : DynkinSystem Ω) : Prop :=
  ∀ 𝒞 : Finset (Set Ω), FACoherentCluster d 𝒞 →
    ∃ ν : TwoValuedState d, ∀ E ∈ 𝒞, ν.Val E

/-- ⊥-closure of a finite carrier family into a pattern. -/
noncomputable def closeCompl (s : Finset (Set Ω)) (h : ∀ A ∈ s, d.Has A) :
    Block d := by
  classical
  exact
    { sets := s ∪ s.image compl
      mem_has := by
        intro A hA
        rcases Finset.mem_union.mp hA with h' | h'
        · exact h A h'
        · obtain ⟨E, hE, rfl⟩ := Finset.mem_image.mp h'
          exact d.has_compl (h E hE)
      compl_closed := by
        intro A hA
        rcases Finset.mem_union.mp hA with h' | h'
        · exact Finset.mem_union_right _ (Finset.mem_image_of_mem compl h')
        · obtain ⟨E, hE, rfl⟩ := Finset.mem_image.mp h'
          rw [compl_compl]
          exact Finset.mem_union_left _ hE }

theorem mem_closeCompl_left {s : Finset (Set Ω)} {h : ∀ A ∈ s, d.Has A}
    (hA : A ∈ s) : A ∈ (closeCompl s h).sets := by
  classical
  simp only [closeCompl]
  exact Finset.mem_union_left _ hA

/-- **Φ ⟺ its cluster form** (§11b's reduction, both directions
latticehood-free): traces determine and are determined by their value-1
parts, complements coming along by ⊥-closure. -/
theorem phi_iff_phiCluster : Phi d ↔ PhiCluster d := by
  constructor
  · intro hphi 𝒞 hcoh
    classical
    obtain ⟨h𝒞, μ, hμ⟩ := hcoh
    obtain ⟨ν, hν⟩ := hphi (closeCompl 𝒞 h𝒞) μ
    exact ⟨ν, fun E hE => (hν E (mem_closeCompl_left hE)).mpr (hμ E hE)⟩
  · intro hcl B μ
    classical
    obtain ⟨ν, hν⟩ := hcl (B.sets.filter fun A => μ.Val A)
      ⟨fun E hE => B.mem_has E (Finset.mem_filter.mp hE).1,
        μ, fun E hE => (Finset.mem_filter.mp hE).2⟩
    refine ⟨ν, fun A hA => ?_⟩
    by_cases hval : μ.Val A
    · exact iff_of_true (hν A (Finset.mem_filter.mpr ⟨hA, hval⟩)) hval
    · have hAc : μ.Val Aᶜ := (μ.val_compl (B.mem_has A hA)).mpr hval
      have hνAc : ν.Val Aᶜ :=
        hν Aᶜ (Finset.mem_filter.mpr ⟨B.compl_closed A hA, hAc⟩)
      exact iff_of_false ((ν.val_compl (B.mem_has A hA)).mp hνAc) hval

/-- **Cluster extension (§11b)**: a σ-state that is 1 on a cluster sitting
below the value-1 part of a pattern reproduces the pattern's WHOLE trace —
monotonicity upward, ⊥-closure for the zeros. (The "any σ-state ≡ 1 on the
cluster extends `s` on `B`" step of the cluster normal form.) -/
theorem cluster_extension (B : Block d) (μ : FinAddState d)
    {𝒞 : Finset (Set Ω)} (h𝒞 : ∀ E ∈ 𝒞, d.Has E)
    (habove : ∀ A ∈ B.sets, μ.Val A → ∃ E ∈ 𝒞, E ⊆ A)
    (ν : TwoValuedState d) (hν : ∀ E ∈ 𝒞, ν.Val E) :
    ∀ A ∈ B.sets, (ν.Val A ↔ μ.Val A) := by
  intro A hA
  by_cases hval : μ.Val A
  · obtain ⟨E, hE, hsub⟩ := habove A hA hval
    exact iff_of_true
      (ν.val_mono (h𝒞 E hE) (B.mem_has A hA) hsub (hν E hE)) hval
  · have hAc : μ.Val Aᶜ := (μ.val_compl (B.mem_has A hA)).mpr hval
    obtain ⟨E, hE, hsub⟩ := habove Aᶜ (B.compl_closed A hA) hAc
    have : ν.Val Aᶜ :=
      ν.val_mono (h𝒞 E hE) (d.has_compl (B.mem_has A hA)) hsub (hν E hE)
    exact iff_of_false ((ν.val_compl (B.mem_has A hA)).mp this) hval

/-! ## §4. 2BR: the two-block rescue (§11a) -/

/-- **Theorem-let 2BR (§11a; kit gap 4.6's general-Ω half).** If the
value-1 part of a finite ⊥-closed pattern is covered by TWO maximal
blocks, the pattern is Dirac-rescued. The only use of latticehood is A2's
in-block ∩-closure (`val_finsetInf`); consequently B′(i)'s open locus is
patterns whose value-1 part needs ≥ 3 blocks, and the product-Ulam
witness's |V| = 3 is optimal. -/
theorem two_block_rescue (hMeets : MeetsExist d) {M₁ M₂ : Set (Set Ω)}
    (hM₁ : IsMaxBlock d M₁) (hM₂ : IsMaxBlock d M₂)
    (B : Block d) (μ : FinAddState d)
    (hcover : ∀ A ∈ B.sets, μ.Val A → A ∈ M₁ ∨ A ∈ M₂) :
    ∃ ω : Ω, ∀ A ∈ B.sets, ((dirac ω : TwoValuedState d).Val A ↔ μ.Val A) := by
  classical
  set V₁ := B.sets.filter fun A => μ.Val A ∧ A ∈ M₁ with hV₁
  set V₂ := B.sets.filter fun A => μ.Val A ∧ A ∈ M₂ with hV₂
  have hE := hM₁.val_finsetInf hMeets μ (D := id) (s := V₁)
    (fun A hA => (Finset.mem_filter.mp hA).2.2)
    (fun A hA => (Finset.mem_filter.mp hA).2.1)
  have hF := hM₂.val_finsetInf hMeets μ (D := id) (s := V₂)
    (fun A hA => (Finset.mem_filter.mp hA).2.2)
    (fun A hA => (Finset.mem_filter.mp hA).2.1)
  obtain ⟨ω, hω⟩ := pattern_pair_overlap_nonempty μ
    (hM₁.has hE.1) (hM₂.has hF.1) hE.2 hF.2
  refine ⟨ω, fun A hA => ?_⟩
  by_cases hval : μ.Val A
  · refine iff_of_true ?_ hval
    rcases hcover A hA hval with h | h
    · exact (Finset.inf_le (f := id)
        (Finset.mem_filter.mpr ⟨hA, hval, h⟩)) hω.1
    · exact (Finset.inf_le (f := id)
        (Finset.mem_filter.mpr ⟨hA, hval, h⟩)) hω.2
  · refine iff_of_false (fun hωA => ?_) hval
    have hAc : μ.Val Aᶜ := (μ.val_compl (B.mem_has A hA)).mpr hval
    rcases hcover Aᶜ (B.compl_closed A hA) hAc with h | h
    · exact (Finset.inf_le (f := id)
        (Finset.mem_filter.mpr ⟨B.compl_closed A hA, hAc, h⟩)) hω.1 hωA
    · exact (Finset.inf_le (f := id)
        (Finset.mem_filter.mpr ⟨B.compl_closed A hA, hAc, h⟩)) hω.2 hωA

/-! ## §5. Atoms, T4, B′(i), and the necessity direction of the ladder -/

/-- An **atom** of a block: a nonempty member with no proper nonempty
member below it. (On countably generated blocks these are the signature
cells; the T3 kernel is one.) -/
def IsAtomOf (M : Set (Set Ω)) (D : Set Ω) : Prop :=
  D ∈ M ∧ D.Nonempty ∧ ∀ E ∈ M, E ⊆ D → E = ∅ ∨ E = D

open Classical in
/-- **T4, per carrier (§11f — the finitary shadow of B′(i))**: for every
f.a.-coherent cluster and every maximal block, some atom of the block
extends the cluster f.a.-coherently. σ-free; the sharpest cheap
falsification target for B′(i). OPEN as a global claim. -/
def T4At (d : DynkinSystem Ω) : Prop :=
  ∀ 𝒞 : Finset (Set Ω), FACoherentCluster d 𝒞 →
    ∀ M, IsMaxBlock d M →
      ∃ D, IsAtomOf M D ∧ FACoherentCluster d (insert D 𝒞)

universe u

/-- **Conjecture B′(i) (OPEN)**: every concrete σ-class OML all of whose
maximal blocks are countably generated satisfies Φ. -/
def BPrimeI : Prop :=
  ∀ (Ω : Type u) (d : DynkinSystem Ω) (hMeets : MeetsExist d),
    CountablyGeneratedBlocks d hMeets → Phi d

/-- **T4 (OPEN)**, quantified over the B′(i)-hypothesis carriers. -/
def T4 : Prop :=
  ∀ (Ω : Type u) (d : DynkinSystem Ω) (hMeets : MeetsExist d),
    CountablyGeneratedBlocks d hMeets → T4At d

/-- **The necessity direction of the ladder (kit gap 4.5, clean half)**:
Φ ⟹ T4 on any carrier with meets and countably generated blocks. The
σ-state provided by Φ on the cluster points every block (P⁼/T3), and the
T3 kernel is an atom of the block charged by the state. The CONVERSE
(T4 + a completion principle ⟹ B′(i)) is open — not stated. -/
theorem t4At_of_phi (hMeets : MeetsExist d)
    (hgen : CountablyGeneratedBlocks d hMeets) (hphi : Phi d) : T4At d := by
  intro 𝒞 hcoh M hM
  classical
  obtain ⟨ν, hν⟩ := (phi_iff_phiCluster.mp hphi) 𝒞 hcoh
  obtain ⟨G, hG⟩ := hgen M hM
  obtain ⟨D, hD, hDne, hDval, hiff, hpt⟩ :=
    hM.dirac_realization hMeets ν G hG
  refine ⟨D, ⟨hD, hDne, fun E hE hsub => ?_⟩, ?_, ν.toFinAdd, ?_⟩
  · by_cases hval : ν.Val E
    · exact Or.inr (subset_antisymm hsub fun x hx => (hpt x hx E hE).mp hval)
    · refine Or.inl (Set.eq_empty_iff_forall_notMem.mpr fun x hx => ?_)
      exact hval ((hpt x (hsub hx) E hE).mpr hx)
  · intro E hE
    rcases Finset.mem_insert.mp hE with rfl | h
    · exact hM.has hD
    · exact hcoh.1 E h
  · intro E hE
    rcases Finset.mem_insert.mp hE with rfl | h
    · exact hDval
    · exact hν E h

/-- The global wrapper: **B′(i) ⟹ T4**. -/
theorem bPrimeI_implies_T4 : BPrimeI.{u} → T4.{u} :=
  fun h Ω d hMeets hgen => t4At_of_phi hMeets hgen (h Ω d hMeets hgen)

/-- **The pointed-selection reading of the cluster form** (§11c's upshot,
via P⁼): on B′(i)-hypothesis carriers, σ-selections and blockwise-pointed
f.a. selections are the same thing. -/
theorem phiCluster_iff_pointedSelection (hMeets : MeetsExist d)
    (hgen : CountablyGeneratedBlocks d hMeets) :
    PhiCluster d ↔
      ∀ 𝒞 : Finset (Set Ω), FACoherentCluster d 𝒞 →
        ∃ μ : FinAddState d,
          (∀ E ∈ 𝒞, μ.Val E) ∧ BlockwisePointed μ := by
  constructor
  · intro h 𝒞 hcoh
    obtain ⟨ν, hν⟩ := h 𝒞 hcoh
    exact ⟨ν.toFinAdd, hν,
      blockwisePointed_of_isSigmaOn hMeets hgen _ ν.isSigmaOn_toFinAdd⟩
  · intro h 𝒞 hcoh
    obtain ⟨μ, hμ, hpt⟩ := h 𝒞 hcoh
    exact ⟨μ.toTwoValued (isSigmaOn_of_blockwisePointed μ hpt), hμ⟩

/-! ## §6. Φ-density: the Stone-topological reframe (§11d)

States are points of the Cantor cube on the carrier's coordinates; a
state's trace on a finite pattern is its restriction to finitely many
coordinates. Density of `St_σ` in `St_fa` is then literally Φ. -/

variable (d)

/-- The Boolean value function of a f.a. state, as a point of the Cantor
cube over the carrier. -/
noncomputable def valFun (μ : FinAddState d) :
    ↥(Carrier d) → Bool :=
  fun A => decide (μ.Val A.1)

/-- The finitely additive states, as a subset of the cube. -/
noncomputable def stFA : Set (↥(Carrier d) → Bool) :=
  Set.range fun μ : FinAddState d => valFun d μ

/-- The σ-additive states, as a subset of the cube. -/
noncomputable def stSigma : Set (↥(Carrier d) → Bool) :=
  Set.range fun ν : TwoValuedState d => valFun d ν.toFinAdd

variable {d}

/-- **Theorem-let Φ-density (§11d)**: Φ(L) ⟺ St_σ(L) is dense in
St_fa(L) (in the product topology of the Cantor cube). For
B′(i)-hypothesis carriers, by P⁼: blockwise-pointed states are dense among
the two-valued f.a. states. -/
theorem phi_iff_dense :
    Phi d ↔ ∀ g ∈ stFA d, g ∈ closure (stSigma d) := by
  constructor
  · intro hphi g hg
    obtain ⟨μ, rfl⟩ := hg
    rw [mem_closure_iff]
    intro U hU hgU
    rw [isOpen_pi_iff] at hU
    obtain ⟨I, u, hu, hsub⟩ := hU _ hgU
    classical
    -- the coordinates named by I, ⊥-closed into a pattern
    obtain ⟨ν, hν⟩ := hphi
      (closeCompl (I.image Subtype.val)
        (fun A hA => by
          obtain ⟨a, _, rfl⟩ := Finset.mem_image.mp hA
          exact a.2)) μ
    refine ⟨valFun d ν.toFinAdd, hsub ?_, ⟨ν, rfl⟩⟩
    rw [Set.mem_pi]
    intro a ha
    have hcoord : valFun d ν.toFinAdd a = valFun d μ a := by
      simp only [valFun]
      exact decide_eq_decide.mpr (hν a.1
        (mem_closeCompl_left (Finset.mem_image_of_mem Subtype.val ha)))
    rw [hcoord]
    exact (hu a ha).2
  · intro hdense B μ
    classical
    -- the agreement neighbourhood on the pattern's coordinates
    set T : Finset ↥(Carrier d) :=
      B.sets.attach.image
        (fun A => (⟨A.1, B.mem_has A.1 A.2⟩ : ↥(Carrier d))) with hT
    set U : Set (↥(Carrier d) → Bool) :=
      {h | ∀ a ∈ T, h a = valFun d μ a} with hUdef
    have hUopen : IsOpen U := by
      have hUeq : U = ⋂ a ∈ T, {h : ↥(Carrier d) → Bool | h a = valFun d μ a} := by
        ext h
        simp [hUdef, Set.mem_iInter]
      rw [hUeq]
      refine isOpen_biInter_finset fun a _ => ?_
      have he : {h : ↥(Carrier d) → Bool | h a = valFun d μ a} =
          (fun h : ↥(Carrier d) → Bool => h a) ⁻¹' {valFun d μ a} := rfl
      rw [he]
      exact (isOpen_discrete _).preimage (continuous_apply a)
    obtain ⟨h', hh'⟩ := mem_closure_iff.mp (hdense _ ⟨μ, rfl⟩) U hUopen
      (fun a _ => rfl)
    obtain ⟨ν, hνeq⟩ := hh'.2
    refine ⟨ν, fun A hA => ?_⟩
    have haT : (⟨A, B.mem_has A hA⟩ : ↥(Carrier d)) ∈ T := by
      rw [hT]
      exact Finset.mem_image.mpr ⟨⟨A, hA⟩, B.sets.mem_attach _, rfl⟩
    have := hh'.1 _ haT
    rw [← hνeq] at this
    simpa only [valFun, decide_eq_decide] using this

private theorem decide_irrel {P : Prop} (i₁ i₂ : Decidable P) :
    @decide P i₁ = @decide P i₂ := by
  cases i₁ <;> cases i₂ <;> first | rfl | exact absurd ‹P› ‹¬P›

/-- Single-coordinate constraint sets are closed (clopen). -/
private theorem isClosed_coord (a : ↥(Carrier d)) (c : Bool) :
    IsClosed {g : ↥(Carrier d) → Bool | g a = c} := by
  have h : {g : ↥(Carrier d) → Bool | g a = c} =
      (fun g : ↥(Carrier d) → Bool => g a) ⁻¹' {c} := rfl
  rw [h]
  exact (isClosed_discrete _).preimage (continuous_apply a)

/-- Two-coordinate constraint sets are closed: preimages of (discrete,
hence closed) relations under the continuous pair evaluation. -/
private theorem isClosed_rel₂ (a b : ↥(Carrier d))
    (R : Bool → Bool → Prop) :
    IsClosed {g : ↥(Carrier d) → Bool | R (g a) (g b)} := by
  have : {g : ↥(Carrier d) → Bool | R (g a) (g b)} =
      (fun g : ↥(Carrier d) → Bool => (g a, g b)) ⁻¹' {p | R p.1 p.2} := rfl
  rw [this]
  exact (isClosed_discrete _).preimage
    ((continuous_apply a).prodMk (continuous_apply b))

/-- Three-coordinate constraint sets are closed. -/
private theorem isClosed_rel₃ (a b c : ↥(Carrier d))
    (R : Bool → Bool → Bool → Prop) :
    IsClosed {g : ↥(Carrier d) → Bool | R (g a) (g b) (g c)} := by
  have : {g : ↥(Carrier d) → Bool | R (g a) (g b) (g c)} =
      (fun g : ↥(Carrier d) → Bool => (g a, g b, g c)) ⁻¹'
        {p : Bool × Bool × Bool | R p.1 p.2.1 p.2.2} := rfl
  rw [this]
  exact (isClosed_discrete _).preimage
    ((continuous_apply a).prodMk
      ((continuous_apply b).prodMk (continuous_apply c)))

/-- **The f.a. states are a CLOSED constraint set** (kit gap 4.2(a)): a
point of the cube is a f.a. state iff it satisfies the normalization,
complementation, and disjoint-additivity constraints, each involving at
most three coordinates; so `stFA` is an intersection of clopen constraint
sets. (The "onto, not injective / nonempty traces" reading of the
pattern–clopen correspondence is the ⊇ direction: a constraint-satisfying
point IS the value function of a state built from it.) -/
theorem isClosed_stFA : IsClosed (stFA d) := by
  classical
  have hchar : stFA d =
      ({g : ↥(Carrier d) → Bool | g ⟨univ, d.has_univ⟩ = true} ∩
        {g | g ⟨∅, d.has_empty⟩ = false} ∩
        (⋂ A : ↥(Carrier d),
          {g | g ⟨A.1ᶜ, d.has_compl A.2⟩ = !g A}) ∩
        ⋂ A : ↥(Carrier d), ⋂ B : ↥(Carrier d),
          ⋂ hd : Disjoint A.1 B.1,
            {g | g ⟨A.1 ∪ B.1, d.has_union A.2 B.2 hd⟩ = (g A || g B)}) := by
    apply Set.Subset.antisymm
    · rintro g ⟨μ, rfl⟩
      refine ⟨⟨⟨?_, ?_⟩, ?_⟩, ?_⟩
      · exact decide_eq_true μ.val_univ
      · exact decide_eq_false μ.not_val_empty
      · refine Set.mem_iInter.mpr fun A => ?_
        change decide (μ.Val A.1ᶜ) = !decide (μ.Val A.1)
        by_cases h : μ.Val A.1
        · rw [decide_eq_true h,
            decide_eq_false (fun hc => (μ.val_compl A.2).mp hc h)]
          rfl
        · rw [decide_eq_false h, decide_eq_true ((μ.val_compl A.2).mpr h)]
          rfl
      · refine Set.mem_iInter.mpr fun A => Set.mem_iInter.mpr fun B =>
          Set.mem_iInter.mpr fun hdisj => ?_
        change decide (μ.Val (A.1 ∪ B.1)) = (decide (μ.Val A.1) || decide (μ.Val B.1))
        rw [← Bool.decide_or, decide_eq_decide]
        exact μ.val_union A.2 B.2 hdisj
    · rintro g ⟨⟨⟨h1, h2⟩, h3⟩, h4⟩
      refine ⟨{ Val := fun A => ∃ h : d.Has A, g ⟨A, h⟩ = true
                decVal := Classical.decPred _
                val_univ := ⟨d.has_univ, h1⟩
                not_val_empty := ?_
                val_compl := ?_
                val_union := ?_ }, ?_⟩
      · rintro ⟨h, hg⟩
        rw [h2] at hg
        exact Bool.false_ne_true hg
      · intro A hA
        have h3A := Set.mem_iInter.mp h3 ⟨A, hA⟩
        simp only [Set.mem_setOf_eq] at h3A
        constructor
        · rintro ⟨hc, hgc⟩ ⟨hA', hgA⟩
          rw [h3A, hgA] at hgc
          exact Bool.false_ne_true hgc
        · intro hnA
          refine ⟨d.has_compl hA, ?_⟩
          rw [h3A]
          have hfalse : g ⟨A, hA⟩ = false := by
            cases hgA : g ⟨A, hA⟩
            · rfl
            · exact absurd ⟨hA, hgA⟩ hnA
          rw [hfalse]
          rfl
      · intro A A' hA hA' hdisj
        have h4A := Set.mem_iInter.mp (Set.mem_iInter.mp
          (Set.mem_iInter.mp h4 ⟨A, hA⟩) ⟨A', hA'⟩) hdisj
        simp only [Set.mem_setOf_eq] at h4A
        constructor
        · rintro ⟨hu, hgu⟩
          rw [h4A] at hgu
          rcases Bool.or_eq_true_iff.mp hgu with h | h
          · exact Or.inl ⟨hA, h⟩
          · exact Or.inr ⟨hA', h⟩
        · intro h
          refine ⟨d.has_union hA hA' hdisj, ?_⟩
          rw [h4A, Bool.or_eq_true_iff]
          rcases h with ⟨h', hg'⟩ | ⟨h', hg'⟩
          · exact Or.inl hg'
          · exact Or.inr hg'
      · funext A
        simp only [valFun]
        refine (decide_irrel _ (Classical.propDecidable _)).trans ?_
        cases hgA : g A
        · exact @decide_eq_false _ (Classical.propDecidable _) (by
            rintro ⟨h, hg⟩
            rw [show (⟨A.1, h⟩ : ↥(Carrier d)) = A from rfl, hgA] at hg
            exact Bool.false_ne_true hg)
        · exact @decide_eq_true _ (Classical.propDecidable _) ⟨A.2, hgA⟩
  rw [hchar]
  refine (((isClosed_coord _ _).inter (isClosed_coord _ _)).inter
    (isClosed_iInter fun A => ?_)).inter
    (isClosed_iInter fun A => isClosed_iInter fun B =>
      isClosed_iInter fun hd => ?_)
  · exact isClosed_rel₂ _ _ fun x y => x = !y
  · exact isClosed_rel₃ _ _ _ fun x y z => x = (y || z)

/-- **The f.a. states are COMPACT** (Tychonoff on the Cantor cube — kit
gap 4.2(b): BPI-strength, fine in ZFC). -/
theorem isCompact_stFA : IsCompact (stFA d) :=
  isClosed_stFA.isCompact

/-! ## §7. Receipts -/

#print axioms SigmaEssential.FinAddState.toTwoValued
#print axioms SigmaEssential.TwoValuedState.isSigmaOn_toFinAdd
#print axioms isSigmaOn_of_blockwisePointed
#print axioms blockwisePointed_of_isSigmaOn
#print axioms pointed_iff_sigma
#print axioms phi_iff_phiCluster
#print axioms cluster_extension
#print axioms two_block_rescue
#print axioms t4At_of_phi
#print axioms bPrimeI_implies_T4
#print axioms phiCluster_iff_pointedSelection
#print axioms phi_iff_dense
#print axioms isClosed_stFA
#print axioms isCompact_stFA

/-! ## §7. Segregation, and the fourth admissibility conjunct

`rem:segregated` calls a carrier *segregated* when every countable orthogonal
family lies in a single block whose σ-additive two-valued states rescue every
finite trace, and `lem:horizontal` shows segregated carriers satisfy Φ -- so a
witness must be non-segregated.

Stated structurally, segregation is exactly blockwise-pointedness of every
finitely additive state, and then `lem:horizontal` is *derived* rather than
assumed: `isSigmaOn_of_blockwisePointed` (§11c) is the gluing step.

This retires the `IsNonSegregated` conjunct of `SigmaEssentialOpenCore.Admissible`
in the honest direction -- as a forcing theorem about witnesses, not as a
definition handed to the predicate. Same shape as `witness_not_polish` and
`witness_not_intersection_closed`. -/

/-- **Segregated carrier (`rem:segregated`), structural form.** Every finitely
additive state is blockwise pointed: each maximal block supplies a kernel point,
so blockwise σ-additive states are available to rescue any trace. -/
def SegregatedStructural (d : DynkinSystem Ω) : Prop :=
  ∀ μ : FinAddState d, BlockwisePointed μ

/-- **`lem:horizontal`, derived.** On a segregated carrier every finitely
additive state is σ-additive. The content is `isSigmaOn_of_blockwisePointed`:
blockwise σ globalizes, no cross-block constraint existing. -/
theorem isSigmaOn_of_segregated (hseg : SegregatedStructural d)
    (μ : FinAddState d) : IsSigmaOn μ (Carrier d) :=
  isSigmaOn_of_blockwisePointed μ (hseg μ)

/-- **Φ holds on a segregated carrier.** A finitely coherent pattern has a
finitely additive realization, which segregation upgrades to a genuine
σ-additive two-valued state -- so the pattern is not σ-essential. -/
theorem no_witness_of_segregated {B : Block d} (hseg : SegregatedStructural d)
    (s₀ : LocalState d B) (hcoh : FinitelyCoherent s₀) :
    ¬ IsSigmaEssential s₀ := by
  rintro ⟨_, hno⟩
  obtain ⟨μ, hμ⟩ := hcoh
  exact hno ⟨μ.toTwoValued (isSigmaOn_of_segregated hseg μ), by
    intro A hA; exact (hμ A hA)⟩

/-- **A witness carrier is non-segregated (the forcing lemma).** One of the six
admissibility conjuncts of `prop:adm`, proved rather than assumed. -/
theorem witness_not_segregated {B : Block d} {s₀ : LocalState d B}
    (hw : IsSigmaEssential s₀) : ¬ SegregatedStructural d :=
  fun hseg => no_witness_of_segregated hseg s₀ hw.1 hw

#print axioms witness_not_segregated

/-! ## Finite carriers: an exact slice of Φ

On a finite carrier there is nothing for σ-additivity to add. A pairwise
disjoint family in a finite space has only finitely many nonempty members, so a
countable disjoint union is a finite one and a finitely additive state is
already σ-additive. Coherence then hands over the global state directly.

This is `shovel_plan.md` #4 at its smallest: an exactly-characterized subclass on
which Φ holds. It is not the Boolean baseline in disguise — `mo2Class` is finite
and *not* intersection-closed, so `boolean_no_witness` does not reach it — and it
says structurally why the Ulam construction needs `ω₁`: the carrier has to be
infinite before a countable disjoint family can escape finite additivity. -/

/-- **On a finite carrier every finitely additive state is σ-additive.** Only
finitely many members of a pairwise disjoint family are nonempty, so the union is
a finite sup. -/
theorem isSigmaOn_of_finite [Finite Ω] (μ : FinAddState d) :
    IsSigmaOn μ (Carrier d) := by
  classical
  intro f hdisj hf
  constructor
  · intro hU
    by_contra hno
    push_neg at hno
    haveI : Finite ↑{n : ℕ | (f n).Nonempty} := by
      refine Finite.of_injective
        (fun p : ↑{n : ℕ | (f n).Nonempty} => p.2.choose) ?_
      rintro ⟨n, hn⟩ ⟨m, hm⟩ h
      by_contra hne
      have hnm : n ≠ m := fun e => hne (Subtype.ext e)
      have hd := hdisj hnm
      have h1 : hn.choose ∈ f n := hn.choose_spec
      have h2 : hm.choose ∈ f m := hm.choose_spec
      have h' : hn.choose = hm.choose := h
      rw [← h'] at h2
      exact (Set.disjoint_left.mp hd h1) h2
    have hfin : {n : ℕ | (f n).Nonempty}.Finite := Set.toFinite _
    have hEq : (⋃ n, f n) = hfin.toFinset.sup f := by
      rw [Finset.sup_set_eq_biUnion]
      ext x
      simp only [Set.mem_iUnion, Set.Finite.mem_toFinset,
        Set.mem_setOf_eq, exists_prop]
      exact ⟨fun ⟨n, hn⟩ => ⟨n, ⟨x, hn⟩, hn⟩, fun ⟨n, _, hn⟩ => ⟨n, hn⟩⟩
    rw [hEq] at hU
    exact μ.not_val_finsetSup hdisj hf hfin.toFinset (fun i _ => hno i) hU
  · rintro ⟨n, hn⟩
    exact μ.val_mono (hf n) (d.has_iUnion_nat hdisj hf) (Set.subset_iUnion f n) hn

/-- **Φ holds on every finite carrier: no finite σ-class admits a σ-essential
witness.** Coherence supplies a finitely additive state, and on a finite carrier
that state is already σ-additive, so it extends the pattern globally. -/
theorem no_witness_of_finite [Finite Ω] {B : Block d} (s₀ : LocalState d B) :
    ¬ IsSigmaEssential s₀ := by
  rintro ⟨hcoh, hno⟩
  obtain ⟨μ, hμ⟩ := hcoh
  exact hno ⟨μ.toTwoValued (isSigmaOn_of_finite μ), by
    intro A hA; exact (hμ A hA)⟩

/-- **So a witness carrier is infinite.** The contrapositive, in the shape the
other forcing lemmas take. -/
theorem witness_carrier_infinite {B : Block d} {s₀ : LocalState d B}
    (hw : IsSigmaEssential s₀) : Infinite Ω := by
  rcases finite_or_infinite Ω with hfin | hinf
  · exact absurd hw (no_witness_of_finite s₀)
  · exact hinf

#print axioms isSigmaOn_of_finite
#print axioms no_witness_of_finite
#print axioms witness_carrier_infinite

/-! ## The bottom rung of the block-count axis

`shovel_plan.md` #4 names "σ-classes with countably many blocks" as a candidate
subclass. The bottom of that axis is exact and settles cleanly: having a single
maximal block is not a weak form of Booleanness, it *is* Booleanness. -/

/-- **One block iff Boolean.** A carrier has a unique maximal block exactly when
it is intersection-closed. Forward: if every pair is compatible then the whole
carrier is a compatible family, and maximality forces every maximal block to be
all of it. Backward: each singleton `{A}` extends to a maximal block, uniqueness
puts every `A` and `B` in the same one, and members of a block are compatible. -/
theorem interClosed_iff_maxBlock_unique :
    InterClosed d ↔ ∀ M M', IsMaxBlock d M → IsMaxBlock d M' → M = M' := by
  constructor
  · intro hIC M M' hM hM'
    have hfam : IsCompatFamily d (Carrier d) :=
      ⟨fun A hA => hA, fun A hA B hB _ => hIC hA hB⟩
    have hMall : M = Carrier d :=
      Set.Subset.antisymm (fun A hA => hM.has hA) (hM.2 hfam (fun A hA => hM.has hA))
    have hM'all : M' = Carrier d :=
      Set.Subset.antisymm (fun A hA => hM'.has hA) (hM'.2 hfam (fun A hA => hM'.has hA))
    rw [hMall, hM'all]
  · intro huniq A B hA hB
    obtain ⟨MA, hAMA, hMA⟩ := exists_isMaxBlock_superset
      (F := ({A} : Set (Set Ω))) ⟨fun _ hx => hx ▸ hA, by simp⟩
    obtain ⟨MB, hBMB, hMB⟩ := exists_isMaxBlock_superset
      (F := ({B} : Set (Set Ω))) ⟨fun _ hx => hx ▸ hB, by simp⟩
    have : MA = MB := huniq MA MB hMA hMB
    exact hMA.compat_mem (hAMA rfl) (this ▸ hBMB rfl)

/-- **So Φ holds on one-block carriers**, by the Boolean baseline. The Φ
consequence is not new -- it is `boolean_no_witness` reached by a different
description -- but the characterization above is. -/
theorem no_witness_of_maxBlock_unique {B : Block d} (s₀ : LocalState d B)
    (huniq : ∀ M M', IsMaxBlock d M → IsMaxBlock d M' → M = M') :
    ¬ IsSigmaEssential s₀ :=
  boolean_no_witness (interClosed_iff_maxBlock_unique.mpr huniq) s₀

#print axioms interClosed_iff_maxBlock_unique
#print axioms no_witness_of_maxBlock_unique



end SigmaEssential.Blocks
