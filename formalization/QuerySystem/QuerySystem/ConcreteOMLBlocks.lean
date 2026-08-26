/-
# Concrete-OML block layer — the §9 gluing reduction, machine-checked

Formalizes §9b–§9c of
`notes/open_questions/oml_attack/oml_lattice_regularity_attack.md`
(proof-read SOUND at s12 standard; receipts `PROOF_READ_2026-07-10_attack_s9.md`,
`PROOF_READ_2026-07-11_attack_s11.md`). Ratification target: kit item 2 of
`notes/open_questions/kits/ratification_kit_2026-07-11.pdf` (gaps 2.1–2.5).

Setting: a concrete σ-class `L` on `Ω` = Mathlib's `DynkinSystem Ω` (as in
`SigmaEssentialLocalization`). Compatibility is the CONCRETE test
`Compat d A B := d.Has (A ∩ B)` (justified by L0, proved both ways below).
"Block" (note's sense) = maximal pairwise-compatible family = `IsMaxBlock`
(the name `Block` is taken by the finite-pattern notion in
`SigmaEssentialLocalization`).

## PROVED (no axioms beyond Mathlib's classical base)
* **Compat API**: symmetry, disjoint ⟹ compatible, difference decomposition
  `A\B ∈ L`, complement invariance.
* **A1a** (`exists_isMaxBlock_superset`): every pairwise-compatible family —
  in particular every pairwise-disjoint family — extends to a maximal block
  (Zorn, chain-union argument).
* **A1b** (`IsMaxBlock.empty_mem/univ_mem/compl_mem/iUnion_mem`): maximal
  blocks contain `∅, Ω`, are complement-closed, and are closed under countable
  pairwise-disjoint unions (the ⊍-closure argument `u∩b = ⊍(cₙ∩b)` +
  maximality).
* **A1c** (`isSigmaOn_carrier_iff_maxBlocks`): a finitely additive two-valued
  state satisfies the σ-condition globally iff it does on every maximal block
  — the blockwise reduction (every countable disjoint family, with its union,
  lives in a single block).
* **C1′** (`pattern_pair_overlap_nonempty`, `pattern_pair_dirac_rescue`):
  the |V| ≤ 2 Dirac rescue, no latticehood — a f.a. state putting 1 on `A`
  and `B` forces `A ∩ B ≠ ∅`, and any point of the overlap gives a Dirac
  agreeing with the state on `{A, B, Aᶜ, Bᶜ}`.
* **L0 bridge** (`Compat.isGreatest_inter`, `compat_of_commuting_decomp`):
  concrete compatibility ⟹ `A ∩ B` is the lattice meet; conversely a
  commuting decomposition `X = m ∪ mc` (`m ⊆ Y`, `mc ⊆ Yᶜ`, `m ∈ L`) ⟹
  concrete compatibility. So on σ-class OMLs concrete and lattice
  compatibility coincide.
* Monotonicity of f.a. states needs no latticehood: already
  `FinAddState.val_mono` (`SigmaEssentialWitness`), reused as-is.

## Phase B — ALSO PROVED (the anticipated Foulis–Holland axiom was
## unnecessary)
* The session design expected the FH/commutant-closure step to enter as a
  cited axiom (Kalmbach 1983 Thm 5 p. 25; Bruns–Harding 2000 Props 2.2–2.8),
  because the σ-class operations alone (complement, nested difference,
  disjoint union) conserve sign-pattern parity over `{A,B,C}` and cannot
  isolate the triple-intersection atom. What they CANNOT do, the meet CAN,
  in one squeeze (`compat_of_locally_resolved`): the meet of `X, S` contains
  every carrier subset of `X ∩ S`, so a pointwise carrier cover of `X ∩ S`
  forces meet `= X ∩ S ∈ L`. With the cover `{A∩B, A∩C}` of `A ∩ (B∪C)`
  (set distributivity — the concreteness that abstract OMLs lack) this gives
  `compat_union_right`, then complements give `compat_inter_right/left`:
  the full commutant-closure instance, axiom-free.
* Downstream, therefore also axiom-free: A2 (`inter_mem`, σ-field closure,
  `toMeasurableSpace`), block overlaps (`overlapMeasurableSpace`), T1
  (`compat_of_singletons`, `interClosed_of_singletons`), P1 (`PoorPair`
  anatomy), and the composite `IsMaxBlock.dirac_realization`.

## Receipts
`#print axioms` for every theorem above, at file end. EVERYTHING in this
file depends on `[propext, Classical.choice, Quot.sound]` only — plain ZFC,
no cited axioms, no sorry.
-/
import QuerySystem.SigmaEssentialWitness
import Mathlib.Order.Zorn
import Mathlib.Order.Disjointed

open Set Function MeasurableSpace

namespace SigmaEssential.Blocks

variable {Ω : Type*} {d : DynkinSystem Ω} {A B C M : Set Ω}

/-! ## §1. Concrete compatibility -/

/-- **Concrete compatibility** (attack note §9, setting): `A ↔ B` iff the
set-intersection already lies in the σ-class. L0 (§6 below) certifies this is
the lattice notion whenever meets exist. -/
def Compat (d : DynkinSystem Ω) (A B : Set Ω) : Prop := d.Has (A ∩ B)

theorem compat_symm : Symmetric (Compat d) := fun A B h =>
  show d.Has (B ∩ A) from Set.inter_comm A B ▸ h

theorem Compat.symm (h : Compat d A B) : Compat d B A := compat_symm h

/-- Disjoint elements are compatible (`A ∩ B = ∅ ∈ L`). -/
theorem compat_of_disjoint (h : Disjoint A B) : Compat d A B :=
  show d.Has (A ∩ B) from h.inter_eq ▸ d.has_empty

/-- Every element is compatible with itself. -/
theorem compat_self (hA : d.Has A) : Compat d A A := by
  change d.Has (A ∩ A)
  rwa [Set.inter_self]

/-- **The orthomodular-difference decomposition**: if `A ↔ B` then
`A \ B ∈ L` (via `A \ B = A \ (A ∩ B)`, a nested difference). -/
theorem Compat.has_diff_left (h : Compat d A B) (hA : d.Has A) :
    d.Has (A \ B) :=
  Set.diff_self_inter ▸ d.has_diff hA h Set.inter_subset_left

/-- Compatibility is complement-invariant in the first slot:
`Aᶜ ∩ B = B \ A = B \ (B ∩ A)`, a nested difference. -/
theorem Compat.compl_left (h : Compat d A B) (hB : d.Has B) :
    Compat d Aᶜ B := by
  have hBA : d.Has (B ∩ A) := h.symm
  have : d.Has (B \ A) :=
    Set.diff_self_inter ▸ d.has_diff hB hBA Set.inter_subset_left
  change d.Has (Aᶜ ∩ B)
  rwa [← Set.diff_eq_compl_inter]

/-! ## §2. Maximal blocks and A1a (Zorn) -/

/-- A pairwise-compatible family inside the carrier. -/
def IsCompatFamily (d : DynkinSystem Ω) (F : Set (Set Ω)) : Prop :=
  (∀ A ∈ F, d.Has A) ∧ F.Pairwise (Compat d)

/-- A **maximal block**: a maximal pairwise-compatible family. (The attack
note's "block"; named `MaxBlock` because `Block` is the finite-pattern notion
of `SigmaEssentialLocalization`.) -/
def IsMaxBlock (d : DynkinSystem Ω) (M : Set (Set Ω)) : Prop :=
  Maximal (IsCompatFamily d) M

namespace IsMaxBlock

variable {F M : Set (Set Ω)}

theorem has (hM : IsMaxBlock d M) (hA : A ∈ M) : d.Has A := hM.1.1 A hA

/-- Any two members of a maximal block are compatible (including `A = B`). -/
theorem compat_mem (hM : IsMaxBlock d M) (hA : A ∈ M) (hB : B ∈ M) :
    Compat d A B := by
  rcases eq_or_ne A B with rfl | hne
  · exact compat_self (hM.has hA)
  · exact hM.1.2 hA hB hne

end IsMaxBlock

/-- **A1a (extension to a maximal block, Zorn).** Every pairwise-compatible
family — in particular every pairwise-orthogonal family — extends to a
maximal block. Chain unions of pairwise-compatible families are
pairwise-compatible: any two members share a chain link. -/
theorem exists_isMaxBlock_superset {F : Set (Set Ω)}
    (hF : IsCompatFamily d F) : ∃ M, F ⊆ M ∧ IsMaxBlock d M := by
  obtain ⟨M, hFM, hmax⟩ :=
    zorn_subset_nonempty {G | IsCompatFamily d G}
      (fun c hc hchain _ => by
        refine ⟨⋃₀ c, ⟨?_, ?_⟩, fun s hs => subset_sUnion_of_mem hs⟩
        · rintro A ⟨G, hGc, hAG⟩
          exact (hc hGc).1 A hAG
        · rintro A ⟨G, hGc, hAG⟩ B ⟨H, hHc, hBH⟩ hAB
          rcases eq_or_ne G H with rfl | hGH
          · exact (hc hGc).2 hAG hBH hAB
          · rcases hchain hGc hHc hGH with h | h
            · exact (hc hHc).2 (h hAG) hBH hAB
            · exact (hc hGc).2 hAG (h hBH) hAB)
      F hF
  exact ⟨M, hFM, hmax⟩

/-! ## §3. A1b: closure properties of maximal blocks (no latticehood) -/

namespace IsMaxBlock

variable {M : Set (Set Ω)}

/-- Maximality, packaged: anything in the carrier compatible with the whole
block is in the block. -/
theorem mem_of_forall_compat (hM : IsMaxBlock d M) (hA : d.Has A)
    (h : ∀ B ∈ M, Compat d A B) : A ∈ M := by
  have hins : IsCompatFamily d (insert A M) := by
    constructor
    · rintro B (rfl | hB)
      · exact hA
      · exact hM.has hB
    · exact (Set.pairwise_insert_of_symmetric compat_symm).mpr
        ⟨hM.1.2, fun B hB _ => h B hB⟩
  exact hM.2 hins (Set.subset_insert A M) (Set.mem_insert A M)

theorem empty_mem (hM : IsMaxBlock d M) : ∅ ∈ M :=
  hM.mem_of_forall_compat d.has_empty fun _ _ => compat_of_disjoint disjoint_bot_left

theorem univ_mem (hM : IsMaxBlock d M) : univ ∈ M :=
  hM.mem_of_forall_compat d.has_univ fun _ hB => by
    simpa [Compat] using hM.has hB

/-- Maximal blocks are complement-closed. -/
theorem compl_mem (hM : IsMaxBlock d M) (hA : A ∈ M) : Aᶜ ∈ M :=
  hM.mem_of_forall_compat (d.has_compl (hM.has hA)) fun _ hB =>
    (hM.compat_mem hA hB).compl_left (hM.has hB)

/-- **The ⊍-closure argument**: maximal blocks are closed under countable
pairwise-disjoint unions (`u ∩ b = ⊍ (cₙ ∩ b)`, then maximality). -/
theorem iUnion_mem (hM : IsMaxBlock d M) {f : ℕ → Set Ω}
    (hdisj : Pairwise (Disjoint on f)) (hf : ∀ n, f n ∈ M) :
    (⋃ n, f n) ∈ M := by
  refine hM.mem_of_forall_compat
    (d.has_iUnion_nat hdisj fun n => hM.has (hf n)) fun B hB => ?_
  change d.Has ((⋃ n, f n) ∩ B)
  rw [Set.iUnion_inter]
  exact d.has_iUnion_nat
    (hdisj.mono fun i j h => h.mono Set.inter_subset_left Set.inter_subset_left)
    fun n => hM.compat_mem (hf n) hB

end IsMaxBlock

/-! ## §4. A1c: the blockwise σ-reduction -/

/-- The σ-condition for a finitely additive state, relativized to a family
`F`: countable pairwise-disjoint families inside `F` are σ-additively
evaluated. `IsSigmaOn μ (Carrier d)` is the GLOBAL σ-condition (the extra
clause turning `FinAddState` into the σ-additive `TwoValuedState`). -/
def IsSigmaOn (μ : FinAddState d) (F : Set (Set Ω)) : Prop :=
  ∀ f : ℕ → Set Ω, Pairwise (Disjoint on f) → (∀ n, f n ∈ F) →
    (μ.Val (⋃ n, f n) ↔ ∃ n, μ.Val (f n))

/-- **A1c (blockwise reduction).** A finitely additive two-valued state is
σ-additive globally iff it is σ-additive on every maximal block: every
countable disjoint family, with its union, lives inside a single maximal
block (A1a extends the family; A1b puts the union in the same block). -/
theorem isSigmaOn_carrier_iff_maxBlocks (μ : FinAddState d) :
    IsSigmaOn μ (Carrier d) ↔ ∀ M, IsMaxBlock d M → IsSigmaOn μ M := by
  constructor
  · intro h M hM f hdisj hf
    exact h f hdisj fun n => hM.has (hf n)
  · intro h f hdisj hf
    have hfam : IsCompatFamily d (Set.range f) := by
      constructor
      · rintro A ⟨n, rfl⟩
        exact hf n
      · rintro A ⟨i, rfl⟩ B ⟨j, rfl⟩ hne
        exact compat_of_disjoint (hdisj fun hij => hne (by rw [hij]))
    obtain ⟨M, hsub, hM⟩ := exists_isMaxBlock_superset hfam
    exact h M hM f hdisj fun n => hsub ⟨n, rfl⟩

/-! ## §5. C1′: the |V| ≤ 2 Dirac rescue (no latticehood) -/

/-- **C1′, part 1.** A finitely additive two-valued state putting `1` on both
`A` and `B` forces `A ∩ B ≠ ∅` (else the pair is disjoint and two disjoint
sets carry value 1, contradicting derived at-most-one). -/
theorem pattern_pair_overlap_nonempty (μ : FinAddState d)
    (hA : d.Has A) (hB : d.Has B) (h1 : μ.Val A) (h2 : μ.Val B) :
    (A ∩ B).Nonempty := by
  rw [Set.nonempty_iff_ne_empty]
  intro hcon
  exact μ.val_at_most_one hA hB (Set.disjoint_iff_inter_eq_empty.mpr hcon) h1 h2

/-- **C1′, part 2.** Any point of the (nonempty) overlap gives a Dirac state
agreeing with `μ` on the ⊥-closed pattern `{A, B, Aᶜ, Bᶜ}`. -/
theorem pattern_pair_dirac_rescue (μ : FinAddState d)
    (hA : d.Has A) (hB : d.Has B) (h1 : μ.Val A) (h2 : μ.Val B) :
    ∃ ω ∈ A ∩ B, ∀ E ∈ ({A, B, Aᶜ, Bᶜ} : Set (Set Ω)),
      ((dirac ω : TwoValuedState d).Val E ↔ μ.Val E) := by
  obtain ⟨ω, hω⟩ := pattern_pair_overlap_nonempty μ hA hB h1 h2
  refine ⟨ω, hω, ?_⟩
  have hdA : ∀ E : Set Ω, (dirac ω : TwoValuedState d).Val E ↔ ω ∈ E :=
    fun E => Iff.rfl
  rintro E (rfl | rfl | rfl | rfl)
  · simpa [hdA] using ⟨fun _ => h1, fun _ => hω.1⟩
  · simpa [hdA] using ⟨fun _ => h2, fun _ => hω.2⟩
  · rw [hdA]
    constructor
    · intro hc
      exact absurd hω.1 hc
    · intro hc
      exact absurd h1 ((μ.val_compl hA).mp hc).elim
  · rw [hdA]
    constructor
    · intro hc
      exact absurd hω.2 hc
    · intro hc
      exact absurd h2 ((μ.val_compl hB).mp hc).elim

/-! ## §6. L0: the concrete/lattice compatibility bridge -/

/-- **L0, forward.** If `A ∩ B ∈ L` then `A ∩ B` IS the lattice meet: it is
the greatest element of `L` below both `A` and `B`. -/
theorem Compat.isGreatest_inter (h : Compat d A B) :
    IsGreatest {C | d.Has C ∧ C ⊆ A ∧ C ⊆ B} (A ∩ B) :=
  ⟨⟨h, Set.inter_subset_left, Set.inter_subset_right⟩,
    fun _ hC => Set.subset_inter hC.2.1 hC.2.2⟩

/-- **L0, converse.** A commuting decomposition forces concrete
compatibility: if `X = m ∪ mc` with `m ∈ L`, `m ⊆ Y`, `mc ⊆ Yᶜ` (the lattice
statement `X = (X∧Y) ∨ (X∧Yᶜ)`, joins of disjoint elements being unions),
then `X ∩ Y = m ∈ L`. -/
theorem compat_of_commuting_decomp {X Y m mc : Set Ω} (hm : d.Has m)
    (hmY : m ⊆ Y) (hmcY : mc ⊆ Yᶜ) (hX : X = m ∪ mc) : Compat d X Y := by
  have hXY : X ∩ Y = m := by
    subst hX
    rw [Set.union_inter_distrib_right, Set.inter_eq_left.mpr hmY,
      (Set.subset_compl_iff_disjoint_right.mp hmcY).inter_eq, Set.union_empty]
  change d.Has (X ∩ Y)
  rw [hXY]
  exact hm

/-! ## §7. Phase B: latticehood and the Foulis–Holland step — PROVED

Latticehood enters ONLY as `MeetsExist` (design decision 3): binary meets
exist in the carrier poset. No abstract OML class is built.

The session design anticipated citing the Foulis–Holland/commutant-closure
step as an axiom. It turned out to be UNNECESSARY on a concrete carrier:
the needed instance follows from a three-line **meet squeeze**
(`compat_of_locally_resolved`): the meet of `X` and `S` contains every
carrier subset of `X ∩ S`, so if `X ∩ S` is pointwise covered by carrier
subsets the meet is squeezed into equality with `X ∩ S`, which is therefore
itself in the carrier. Applied with the cover `{A∩B, A∩C}` of
`A ∩ (B∪C)` — set distributivity, unavailable abstractly — this yields
commutant closure with no orthomodular calculus at all. Concreteness
supplies what Foulis–Holland supplies abstractly. (The abstract theorem is
of course still Kalmbach 1983 Thm 5 / Bruns–Harding 2000 Props 2.2–2.8;
nothing here re-proves it beyond the concrete instance the corpus needs.)

The same squeeze IS the note's T1 (singleton quarantine) in its s12
sharpened form: "every point of the overlap lies in some member of `L`
inside the overlap" forces compatibility. -/

/-- **Latticehood, concrete form**: any two carrier elements have a
`⊆`-greatest carrier element below their intersection (a lattice meet). -/
def MeetsExist (d : DynkinSystem Ω) : Prop :=
  ∀ ⦃A B : Set Ω⦄, d.Has A → d.Has B →
    ∃ m, IsGreatest {C | d.Has C ∧ C ⊆ A ∧ C ⊆ B} m

/-- **The meet squeeze (= T1, sharpened form).** If every point of `X ∩ S`
lies in some carrier member inside `X ∩ S`, then the meet of `X` and `S` is
squeezed into equality with `X ∩ S`, so `X ↔ S` concretely. No exhaustion
hypothesis: the covering members need not exhaust anything — each is below
the meet, and their union already covers `X ∩ S`. -/
theorem compat_of_locally_resolved (hMeets : MeetsExist d) {X S : Set Ω}
    (hX : d.Has X) (hS : d.Has S)
    (h : ∀ ω ∈ X ∩ S, ∃ E, d.Has E ∧ E ⊆ X ∩ S ∧ ω ∈ E) :
    Compat d X S := by
  obtain ⟨m, ⟨hm, hmX, hmS⟩, hub⟩ := hMeets hX hS
  have hsub : X ∩ S ⊆ m := fun ω hω => by
    obtain ⟨E, hE, hEsub, hωE⟩ := h ω hω
    exact hub ⟨hE, hEsub.trans Set.inter_subset_left,
      hEsub.trans Set.inter_subset_right⟩ hωE
  have heq : m = X ∩ S := subset_antisymm (Set.subset_inter hmX hmS) hsub
  change d.Has (X ∩ S)
  rw [← heq]
  exact hm

/-- Compatibility is complement-invariant in the second slot
(`A ∩ Bᶜ = A \ B`, a nested difference — no latticehood). -/
theorem Compat.compl_right (h : Compat d A B) (hA : d.Has A) :
    Compat d A Bᶜ := by
  have hd : d.Has (A \ B) := h.has_diff_left hA
  change d.Has (A ∩ Bᶜ)
  rwa [← Set.diff_eq]

/-- Pairwise-compatible unions stay in the carrier (no latticehood:
`B ∪ C = B ⊍ (C \ B)`, both pieces in `L` by compatibility). -/
theorem has_union_of_compat (hB : d.Has B) (hC : d.Has C)
    (hBC : Compat d B C) : d.Has (B ∪ C) := by
  have hCB : d.Has (C \ B) := hBC.symm.has_diff_left hC
  rw [← Set.union_diff_self]
  exact d.has_union hB hCB disjoint_sdiff_right

/-- **Commutant closure with the join, concrete Foulis–Holland instance.**
For pairwise-compatible `A, B, C`: `A ↔ B ∪ C`. Proof = the meet squeeze
with the two-element cover `{A∩B, A∩C}` of `A ∩ (B∪C)`. -/
theorem compat_union_right (hMeets : MeetsExist d)
    (hA : d.Has A) (hB : d.Has B) (hC : d.Has C)
    (hAB : Compat d A B) (hAC : Compat d A C) (hBC : Compat d B C) :
    Compat d A (B ∪ C) := by
  refine compat_of_locally_resolved hMeets hA
    (has_union_of_compat hB hC hBC) fun ω hω => ?_
  rcases hω.2 with hωB | hωC
  · exact ⟨A ∩ B, hAB,
      Set.inter_subset_inter_right A Set.subset_union_left, ⟨hω.1, hωB⟩⟩
  · exact ⟨A ∩ C, hAC,
      Set.inter_subset_inter_right A Set.subset_union_right, ⟨hω.1, hωC⟩⟩

/-- **Commutant closure with the meet** (the Foulis–Holland instance the
blocks need): pairwise-compatible `A, B, C` give `A ↔ B ∩ C`, via
`compat_union_right` on complements and De Morgan. -/
theorem compat_inter_right (hMeets : MeetsExist d)
    (hA : d.Has A) (hB : d.Has B) (hC : d.Has C)
    (hAB : Compat d A B) (hAC : Compat d A C) (hBC : Compat d B C) :
    Compat d A (B ∩ C) := by
  have h4 : Compat d A (Bᶜ ∪ Cᶜ) :=
    compat_union_right hMeets hA (d.has_compl hB) (d.has_compl hC)
      (hAB.compl_right hA) (hAC.compl_right hA)
      ((hBC.compl_left hC).compl_right (d.has_compl hB))
  have h5 : Compat d A (Bᶜ ∪ Cᶜ)ᶜ := h4.compl_right hA
  rwa [Set.compl_union, compl_compl, compl_compl] at h5

/-- **Commutant closure, concrete** (fully proved — no axiom): pairwise
compatibility of `A, B, C` upgrades to `A ∩ B ∩ C ∈ L` when meets exist. -/
theorem compat_inter_left (hMeets : MeetsExist d)
    (hA : d.Has A) (hB : d.Has B) (hC : d.Has C)
    (hAB : Compat d A B) (hAC : Compat d A C) (hBC : Compat d B C) :
    Compat d (A ∩ B) C := by
  have h := compat_inter_right hMeets hA hB hC hAB hAC hBC
  change d.Has (A ∩ B ∩ C)
  rw [Set.inter_assoc]
  exact h

/-! ## §8. A2: maximal blocks of a σ-class OML are σ-fields -/

namespace IsMaxBlock

variable {M : Set (Set Ω)}

/-- **A2, the ∩-closure step**: on a σ-class OML, maximal blocks are closed
under binary intersection (the axis-2 upgrade; kit gap 2.1). -/
theorem inter_mem (hM : IsMaxBlock d M) (hMeets : MeetsExist d)
    (hA : A ∈ M) (hB : B ∈ M) : A ∩ B ∈ M := by
  refine hM.mem_of_forall_compat (hM.compat_mem hA hB) fun C hC => ?_
  exact compat_inter_left hMeets (hM.has hA) (hM.has hB) (hM.has hC)
    (hM.compat_mem hA hB) (hM.compat_mem hA hC) (hM.compat_mem hB hC)

theorem diff_mem (hM : IsMaxBlock d M) (hMeets : MeetsExist d)
    (hA : A ∈ M) (hB : B ∈ M) : A \ B ∈ M := by
  rw [Set.diff_eq]
  exact hM.inter_mem hMeets hA (hM.compl_mem hB)

theorem union_mem (hM : IsMaxBlock d M) (hMeets : MeetsExist d)
    (hA : A ∈ M) (hB : B ∈ M) : A ∪ B ∈ M := by
  have : Aᶜ ∩ Bᶜ ∈ M := hM.inter_mem hMeets (hM.compl_mem hA) (hM.compl_mem hB)
  simpa [Set.compl_inter] using hM.compl_mem this

theorem finsetSup_mem (hM : IsMaxBlock d M) (hMeets : MeetsExist d)
    {ι : Type*} {s : Finset ι} {f : ι → Set Ω} (hf : ∀ i ∈ s, f i ∈ M) :
    s.sup f ∈ M := by
  classical
  induction s using Finset.cons_induction with
  | empty => simpa [Finset.sup_empty, Set.bot_eq_empty] using hM.empty_mem
  | cons a s ha ih =>
    rw [Finset.sup_cons]
    exact hM.union_mem hMeets (hf a (Finset.mem_cons_self a s))
      (ih fun i hi => hf i (Finset.mem_cons_of_mem hi))

/-- **A2, σ-closure**: maximal blocks are closed under ARBITRARY countable
unions (disjointification through the block's finite Boolean operations,
then A1b's ⊍-closure). -/
theorem iUnion_mem' (hM : IsMaxBlock d M) (hMeets : MeetsExist d)
    {f : ℕ → Set Ω} (hf : ∀ n, f n ∈ M) : (⋃ n, f n) ∈ M := by
  rw [← iUnion_disjointed]
  refine hM.iUnion_mem (disjoint_disjointed f) fun n => ?_
  simp only [disjointed]
  exact hM.diff_mem hMeets (hf n) (hM.finsetSup_mem hMeets fun i _ => hf i)

theorem iInter_mem (hM : IsMaxBlock d M) (hMeets : MeetsExist d)
    {f : ℕ → Set Ω} (hf : ∀ n, f n ∈ M) : (⋂ n, f n) ∈ M := by
  rw [← compl_compl (⋂ n, f n), Set.compl_iInter]
  exact hM.compl_mem (hM.iUnion_mem' hMeets fun n => hM.compl_mem (hf n))

/-- **A2, packaged**: every maximal block of a concrete σ-class OML is a
σ-field of sets on `Ω`. -/
@[reducible]
def toMeasurableSpace (hM : IsMaxBlock d M) (hMeets : MeetsExist d) :
    MeasurableSpace Ω where
  MeasurableSet' A := A ∈ M
  measurableSet_empty := hM.empty_mem
  measurableSet_compl _ hA := hM.compl_mem hA
  measurableSet_iUnion _ hf := hM.iUnion_mem' hMeets hf

@[simp]
theorem measurableSet_toMeasurableSpace (hM : IsMaxBlock d M)
    (hMeets : MeetsExist d) :
    @MeasurableSet Ω (hM.toMeasurableSpace hMeets) A ↔ A ∈ M := Iff.rfl

end IsMaxBlock

/-! ## §8b. T1 corollaries, P1 poor-pair anatomy, block overlaps -/

/-- **T1, singleton form**: if every point of `A ∩ B` has its singleton in
`L`, the pair is compatible. Contrapositive = the singleton quarantine: on a
lattice, an incompatible overlap contains a point whose singleton (indeed,
every `L`-member inside the overlap through it) is missing from `L`. -/
theorem compat_of_singletons (hMeets : MeetsExist d)
    (hA : d.Has A) (hB : d.Has B) (h : ∀ ω ∈ A ∩ B, d.Has {ω}) :
    Compat d A B :=
  compat_of_locally_resolved hMeets hA hB fun ω hω =>
    ⟨{ω}, h ω hω, Set.singleton_subset_iff.mpr hω, rfl⟩

/-- **T1, global form**: a concrete σ-class OM lattice containing all
singletons is a Boolean σ-field (`InterClosed` is the spine's Boolean
predicate; with π–λ it is a σ-algebra). -/
theorem interClosed_of_singletons (hMeets : MeetsExist d)
    (h : ∀ ω : Ω, d.Has {ω}) : InterClosed d :=
  fun hA hB => compat_of_singletons hMeets hA hB fun ω _ => h ω

/-- **P1's poor pair**: nonempty set-intersection but no nonempty carrier
member inside it (lattice meet `0` while the intersection is inhabited). -/
def PoorPair (d : DynkinSystem Ω) (A B : Set Ω) : Prop :=
  (A ∩ B).Nonempty ∧ ∀ E, d.Has E → E ⊆ A ∩ B → E = ∅

/-- Poor pairs are incompatible … -/
theorem PoorPair.not_compat (h : PoorPair d A B) : ¬ Compat d A B :=
  fun hc => h.1.ne_empty (h.2 _ hc subset_rfl)

/-- … hence lie in no common maximal block. -/
theorem PoorPair.not_mem_common_block {M : Set (Set Ω)}
    (hM : IsMaxBlock d M) (h : PoorPair d A B)
    (hA : A ∈ M) (hB : B ∈ M) : False :=
  h.not_compat (hM.compat_mem hA hB)

/-- Poor regions are singleton-free. -/
theorem PoorPair.singleton_notMem (h : PoorPair d A B) {ω : Ω}
    (hω : ω ∈ A ∩ B) : ¬ d.Has {ω} := fun hs =>
  Set.singleton_ne_empty ω (h.2 {ω} hs (Set.singleton_subset_iff.mpr hω))

/-- **P1, propagation down σ-decompositions**: if `(A, B)` is poor and
`A = ⊍ₙ fₙ` then every `(fₙ, B)` has meet `0` while some `fₙ ∩ B ≠ ∅` —
poor pairs propagate down every σ-decomposition. -/
theorem PoorPair.propagate {f : ℕ → Set Ω} (h : PoorPair d A B)
    (hA : A = ⋃ n, f n) :
    (∀ n E, d.Has E → E ⊆ f n ∩ B → E = ∅) ∧ ∃ n, (f n ∩ B).Nonempty := by
  constructor
  · intro n E hE hsub
    exact h.2 E hE (hsub.trans (Set.inter_subset_inter_left B
      (hA ▸ Set.subset_iUnion f n)))
  · obtain ⟨ω, hωA, hωB⟩ := h.1
    rw [hA] at hωA
    obtain ⟨n, hn⟩ := Set.mem_iUnion.mp hωA
    exact ⟨n, ω, hn, hωB⟩

/-- **P1, σ-superadditivity of meets** (light form): a disjoint union of
carrier lower bounds of the `(fₙ ∩ B)` is a carrier lower bound of
`(⋃ fₙ) ∩ B` — so `⊍ₙ (fₙ ∧ B) ≤ (⊍ₙ fₙ) ∧ B` at every meet. -/
theorem sigma_superadditive_lower_bound {f g : ℕ → Set Ω}
    (hdisj : Pairwise (Disjoint on f)) (hg : ∀ n, d.Has (g n))
    (hsub : ∀ n, g n ⊆ f n ∩ B) :
    d.Has (⋃ n, g n) ∧ (⋃ n, g n) ⊆ (⋃ n, f n) ∩ B := by
  constructor
  · exact d.has_iUnion_nat
      (hdisj.mono fun i j hij => hij.mono
        ((hsub i).trans Set.inter_subset_left)
        ((hsub j).trans Set.inter_subset_left)) hg
  · exact Set.iUnion_subset fun n => (hsub n).trans
      (Set.inter_subset_inter_left B (Set.subset_iUnion f n))

/-- **Block overlaps are σ-fields** (the second clause of A2): the overlap
of two maximal blocks, packaged as a σ-field of sets. -/
@[reducible]
def IsMaxBlock.overlapMeasurableSpace {M₁ M₂ : Set (Set Ω)}
    (hM₁ : IsMaxBlock d M₁) (hM₂ : IsMaxBlock d M₂) (hMeets : MeetsExist d) :
    MeasurableSpace Ω where
  MeasurableSet' A := A ∈ M₁ ∩ M₂
  measurableSet_empty := ⟨hM₁.empty_mem, hM₂.empty_mem⟩
  measurableSet_compl _ hA := ⟨hM₁.compl_mem hA.1, hM₂.compl_mem hA.2⟩
  measurableSet_iUnion _ hf :=
    ⟨hM₁.iUnion_mem' hMeets fun n => (hf n).1,
      hM₂.iUnion_mem' hMeets fun n => (hf n).2⟩

/-! ## §9. T3: Dirac realization on countably generated σ-fields

The note's T3 (§9c), split cleanly: the Dirac-realization engine is a pure
σ-field statement (THIS section — no latticehood, NO axioms), and latticehood
enters only through A2 (blocks ARE σ-fields, §8). The two compose in §10. -/

/-- Restriction of a global σ-additive two-valued state to a sub-σ-field of
the carrier: same values, constraints inherited (every family the σ-field
sees, the σ-class saw). -/
def _root_.SigmaEssential.TwoValuedState.restrict (s : TwoValuedState d)
    (m : MeasurableSpace Ω) (h : ∀ A : Set Ω, m.MeasurableSet' A → d.Has A) :
    TwoValuedState (DynkinSystem.ofMeasurableSpace m) where
  Val := s.Val
  decVal := s.decVal
  val_univ := s.val_univ
  not_val_empty := s.not_val_empty
  val_compl {A} hA := s.val_compl (h A hA)
  val_iUnion {f} hdisj hf := s.val_iUnion hdisj fun i => h (f i) (hf i)

/-- The σ-subfield step of T3: `{A : D ⊆ A or D ∩ A = ∅}` contains the
generators and is a σ-algebra, hence contains the generated σ-field.
(Stated by induction over `GenerateMeasurable`.) -/
private theorem dichotomy_of_generateMeasurable {G : ℕ → Set Ω} {D : Set Ω}
    (hGdich : ∀ n, D ⊆ G n ∨ D ∩ G n = ∅) {A : Set Ω}
    (hA : MeasurableSpace.GenerateMeasurable (Set.range G) A) :
    D ⊆ A ∨ D ∩ A = ∅ := by
  induction hA with
  | basic u hu =>
    obtain ⟨n, rfl⟩ := hu
    exact hGdich n
  | empty => exact Or.inr (Set.inter_empty D)
  | compl s _ ih =>
    rcases ih with h | h
    · exact Or.inr (Set.eq_empty_iff_forall_notMem.mpr
        fun x ⟨hxD, hxs⟩ => hxs (h hxD))
    · exact Or.inl (Set.subset_compl_iff_disjoint_right.mpr
        (Set.disjoint_iff_inter_eq_empty.mpr h))
  | iUnion f _ ih =>
    by_cases hex : ∃ i, D ⊆ f i
    · obtain ⟨i, hi⟩ := hex
      exact Or.inl (hi.trans (Set.subset_iUnion f i))
    · push Not at hex
      refine Or.inr ?_
      rw [Set.inter_iUnion, Set.iUnion_eq_empty]
      intro i
      rcases ih i with h | h
      · exact absurd h (hex i)
      · exact h

/-- **T3 (Dirac realization; latticehood re-supplies inner regularity).**
Every two-valued σ-additive state on a countably generated σ-field of sets is
point-realized: there is a nonempty measurable kernel `D` (the decreasing
intersection of the generators' value-1 sides) with `ν(A) = 1 ⟺ D ⊆ A`, and
`ν` agrees with the point evaluation `δ_ω` at EVERY `ω ∈ D`. Both hypotheses
of the note's T3 are visible: σ-additivity powers the continuity-from-above
step (`ν(D) = 1`), countable generation supplies the kernel. NO axioms. -/
theorem dirac_realization_of_countablyGenerated
    (m : MeasurableSpace Ω) (G : ℕ → Set Ω)
    (hgen : m = MeasurableSpace.generateFrom (Set.range G))
    (ν : TwoValuedState (DynkinSystem.ofMeasurableSpace m)) :
    ∃ D : Set Ω, (DynkinSystem.ofMeasurableSpace m).Has D ∧ D.Nonempty ∧
      ν.Val D ∧
      (∀ A : Set Ω, (DynkinSystem.ofMeasurableSpace m).Has A →
        (ν.Val A ↔ D ⊆ A)) ∧
      ∀ ω ∈ D, ∀ A : Set Ω, (DynkinSystem.ofMeasurableSpace m).Has A →
        (ν.Val A ↔ ω ∈ A) := by
  classical
  subst hgen
  revert ν
  set d' : DynkinSystem Ω :=
    DynkinSystem.ofMeasurableSpace
      (MeasurableSpace.generateFrom (Set.range G)) with hd'
  intro ν
  have hInter : InterClosed d' := fun {P Q} hP hQ =>
    @MeasurableSet.inter Ω (MeasurableSpace.generateFrom (Set.range G)) P Q hP hQ
  have hGmeas : ∀ n, d'.Has (G n) := fun n =>
    MeasurableSpace.measurableSet_generateFrom ⟨n, rfl⟩
  -- the value-1 sides of the generators
  obtain ⟨side, hside⟩ :
      ∃ side : ℕ → Set Ω,
        ∀ n, side n = if ν.Val (G n) then G n else (G n)ᶜ :=
    ⟨_, fun _ => rfl⟩
  have hsideHas : ∀ n, d'.Has (side n) := fun n => by
    rw [hside]
    by_cases h : ν.Val (G n)
    · rw [if_pos h]; exact hGmeas n
    · rw [if_neg h]; exact d'.has_compl (hGmeas n)
  have hsideVal : ∀ n, ν.Val (side n) := fun n => by
    rw [hside]
    by_cases h : ν.Val (G n)
    · rwa [if_pos h]
    · rw [if_neg h]; exact (ν.val_compl (hGmeas n)).mpr h
  -- the decreasing partial intersections Fₙ
  obtain ⟨F, hF0, hFs⟩ :
      ∃ F : ℕ → Set Ω, F 0 = side 0 ∧ ∀ n, F (n + 1) = F n ∩ side (n + 1) :=
    ⟨fun n => Nat.rec (side 0) (fun k Fk => Fk ∩ side (k + 1)) n,
      rfl, fun _ => rfl⟩
  have hFHas : ∀ n, d'.Has (F n) := by
    intro n
    induction n with
    | zero => rw [hF0]; exact hsideHas 0
    | succ k ih => rw [hFs]; exact hInter ih (hsideHas (k + 1))
  have hFVal : ∀ n, ν.Val (F n) := by
    intro n
    induction n with
    | zero => rw [hF0]; exact hsideVal 0
    | succ k ih =>
      rw [hFs]
      exact ν.val_inter hInter (hFHas k) (hsideHas (k + 1)) ih (hsideVal (k + 1))
  have hFanti : Antitone F :=
    antitone_nat_of_succ_le fun n => by rw [hFs]; exact Set.inter_subset_left
  have hFside : ∀ n, F n ⊆ side n := fun n => by
    cases n with
    | zero => rw [hF0]
    | succ k => rw [hFs]; exact Set.inter_subset_right
  -- the kernel D and σ-continuity from above
  set D : Set Ω := ⋂ n, F n with hD
  have hDsub : ∀ n, D ⊆ F n := fun n => Set.iInter_subset F n
  have hDmeas : d'.Has D :=
    @MeasurableSet.iInter Ω ℕ (MeasurableSpace.generateFrom (Set.range G)) _
      F fun n => hFHas n
  obtain ⟨g, hg0, hgs⟩ :
      ∃ g : ℕ → Set Ω, g 0 = D ∧ ∀ n, g (n + 1) = F n \ F (n + 1) :=
    ⟨fun n => Nat.rec D (fun k _ => F k \ F (k + 1)) n, rfl, fun _ => rfl⟩
  have hgHas : ∀ n, d'.Has (g n) := fun n => by
    cases n with
    | zero => rw [hg0]; exact hDmeas
    | succ k =>
      rw [hgs]
      exact @MeasurableSet.diff Ω (MeasurableSpace.generateFrom (Set.range G))
        _ _ (hFHas k) (hFHas (k + 1))
  have hgdisj : Pairwise (Disjoint on g) := by
    have key : ∀ i j, i < j → Disjoint (g i) (g j) := by
      intro i j hij
      obtain ⟨k, rfl⟩ : ∃ k, j = k + 1 :=
        ⟨j - 1, (Nat.succ_pred_eq_of_pos (Nat.pos_of_ne_zero
          fun h => by omega)).symm⟩
      have hgj : Disjoint (F (k + 1)) (g (k + 1)) := by
        rw [hgs]; exact disjoint_sdiff_right
      cases i with
      | zero =>
        rw [hg0]
        exact hgj.mono_left (hDsub (k + 1))
      | succ l =>
        have hlk : l + 1 ≤ k := by omega
        have : g (k + 1) ⊆ F (l + 1) := by
          rw [hgs]
          exact Set.diff_subset.trans (hFanti hlk)
        rw [hgs]
        exact (disjoint_sdiff_left.mono_right this).symm.symm
    intro i j hne
    rcases lt_or_gt_of_ne hne with h | h
    · exact key i j h
    · exact (key j i h).symm
  have hUg : (⋃ n, g n) = F 0 := by
    apply Set.Subset.antisymm
    · refine Set.iUnion_subset fun n => ?_
      cases n with
      | zero => rw [hg0]; exact hDsub 0
      | succ k => rw [hgs]; exact Set.diff_subset.trans (hFanti (Nat.zero_le k))
    · intro x hx
      by_cases hall : ∀ n, x ∈ F n
      · exact Set.mem_iUnion.mpr ⟨0, by rw [hg0]; exact Set.mem_iInter.mpr hall⟩
      · push Not at hall
        have hspec : x ∉ F (Nat.find hall) := Nat.find_spec hall
        obtain ⟨k, hk⟩ : ∃ k, Nat.find hall = k + 1 := by
          cases hfind : Nat.find hall with
          | zero => rw [hfind] at hspec; exact absurd hx hspec
          | succ k => exact ⟨k, rfl⟩
        refine Set.mem_iUnion.mpr ⟨k + 1, ?_⟩
        rw [hgs]
        refine ⟨not_not.mp (Nat.find_min hall (by omega)), ?_⟩
        rw [← hk]
        exact hspec
  have hValD : ν.Val D := by
    have hValU : ν.Val (⋃ n, g n) := by rw [hUg]; exact hFVal 0
    obtain ⟨n, hn⟩ := (ν.val_iUnion hgdisj hgHas).mp hValU
    cases n with
    | zero => rwa [hg0] at hn
    | succ k =>
      exfalso
      have hdisj : Disjoint (g (k + 1)) (F (k + 1)) := by
        rw [hgs]; exact disjoint_sdiff_left
      exact ν.val_at_most_one (hgHas (k + 1)) (hFHas (k + 1)) hdisj hn
        (hFVal (k + 1))
  have hDne : D.Nonempty := by
    rw [Set.nonempty_iff_ne_empty]
    intro hcon
    rw [hcon] at hValD
    exact ν.not_val_empty hValD
  -- the dichotomy σ-subfield
  have hGdich : ∀ n, D ⊆ G n ∨ D ∩ G n = ∅ := fun n => by
    have hDside : D ⊆ side n := (hDsub n).trans (hFside n)
    rw [hside] at hDside
    by_cases h : ν.Val (G n)
    · rw [if_pos h] at hDside; exact Or.inl hDside
    · rw [if_neg h] at hDside
      exact Or.inr (Set.disjoint_iff_inter_eq_empty.mp
        (Set.subset_compl_iff_disjoint_right.mp hDside))
  have hdich : ∀ A : Set Ω, d'.Has A → (D ⊆ A ∨ D ∩ A = ∅) := fun A hA =>
    dichotomy_of_generateMeasurable hGdich hA
  -- package
  have hiff : ∀ A : Set Ω, d'.Has A → (ν.Val A ↔ D ⊆ A) := by
    intro A hA
    constructor
    · intro h
      rcases hdich A hA with hsub | hemp
      · exact hsub
      · exact absurd h (ν.val_at_most_one hDmeas hA
          (Set.disjoint_iff_inter_eq_empty.mpr hemp) hValD)
    · intro hsub
      exact ν.val_mono hDmeas hA hsub hValD
  refine ⟨D, hDmeas, hDne, hValD, hiff, ?_⟩
  intro ω hω A hA
  rcases hdich A hA with hsub | hemp
  · exact iff_of_true ((hiff A hA).mpr hsub) (hsub hω)
  · have hnval : ¬ ν.Val A := ν.val_at_most_one hDmeas hA
      (Set.disjoint_iff_inter_eq_empty.mpr hemp) hValD
    have hnmem : ω ∉ A := fun hωA =>
      Set.notMem_empty ω (hemp ▸ Set.mem_inter hω hωA)
    exact iff_of_false hnval hnmem

/-! ## §10. A2 + T3 composed: σ-states are Dirac on countably generated
maximal blocks -/

/-- **T3 on blocks** (the note's statement, assembled): if a maximal block of
a σ-class OML — a σ-field by A2 — is countably generated, then every global
two-valued σ-additive state restricts on it to a point evaluation: a nonempty
kernel `D ∈ M` with `s(A) = 1 ⟺ D ⊆ A` for `A ∈ M`, and agreement with
`δ_ω` on all of `M` for every `ω ∈ D`. (Depends on the Foulis–Holland axiom
through A2's σ-field packaging.) -/
theorem IsMaxBlock.dirac_realization {M : Set (Set Ω)} (hM : IsMaxBlock d M)
    (hMeets : MeetsExist d) (s : TwoValuedState d) (G : ℕ → Set Ω)
    (hgen : hM.toMeasurableSpace hMeets =
      MeasurableSpace.generateFrom (Set.range G)) :
    ∃ D ∈ M, D.Nonempty ∧ s.Val D ∧
      (∀ A ∈ M, (s.Val A ↔ D ⊆ A)) ∧
      ∀ ω ∈ D, ∀ A ∈ M, (s.Val A ↔ ω ∈ A) := by
  obtain ⟨D, hD, hDne, hDval, hiff, hpt⟩ :=
    dirac_realization_of_countablyGenerated (hM.toMeasurableSpace hMeets) G
      hgen (s.restrict (hM.toMeasurableSpace hMeets) fun A hA => hM.has hA)
  exact ⟨D, hD, hDne, hDval, fun A hA => hiff A hA,
    fun ω hω A hA => hpt ω hω A hA⟩

/-! ## §11. Receipts -/

#print axioms exists_isMaxBlock_superset
#print axioms IsMaxBlock.empty_mem
#print axioms IsMaxBlock.univ_mem
#print axioms IsMaxBlock.compl_mem
#print axioms IsMaxBlock.iUnion_mem
#print axioms isSigmaOn_carrier_iff_maxBlocks
#print axioms pattern_pair_overlap_nonempty
#print axioms pattern_pair_dirac_rescue
#print axioms Compat.isGreatest_inter
#print axioms compat_of_commuting_decomp
#print axioms compat_of_locally_resolved
#print axioms compat_union_right
#print axioms compat_inter_right
#print axioms compat_inter_left
#print axioms compat_of_singletons
#print axioms interClosed_of_singletons
#print axioms PoorPair.propagate
#print axioms sigma_superadditive_lower_bound
#print axioms IsMaxBlock.overlapMeasurableSpace
#print axioms IsMaxBlock.inter_mem
#print axioms IsMaxBlock.iUnion_mem'
#print axioms IsMaxBlock.toMeasurableSpace
#print axioms SigmaEssential.TwoValuedState.restrict
#print axioms dirac_realization_of_countablyGenerated
#print axioms IsMaxBlock.dirac_realization

end SigmaEssential.Blocks
