/-
# Marczewski compact classes: the corrected transport criterion and the ω₁ bank

Formalizes the compact-class layer of the OML attack (attack note §11e +
§9d's coarse-block anatomy; ratification kit gaps 4.3 and 4.4(a), and the
ω₁ half of gap 2.3(b)).

## PROVED (all axiom-free — classical base only)
* `CountablyCompactClass` — Marczewski 1953 §2, sequence form (purely
  set-theoretic, no topology).
* **The corrected compact-transport criterion** (kit gap 4.4(a), the ✎s16
  wording fix with forward-pointing consequences):
  `IsMaxBlock.isSigmaOn_of_compact_class` (in-block form) and
  `compact_transport` (OML form): ONE countably compact class
  Marczewski-approximating every maximal block IN-BLOCK — with the value-1
  inner witness `D ∈ Bl`, `μ(D) = 1`, `D ⊆ K ⊆ E` — makes a two-valued
  finitely additive state σ-additive (per-block M 1953 4(i) + A1c).
  The hypothesis is APPROXIMATION, not mere filter refinement — the two are
  inequivalent (singleton-class counterexample, note §11e).
* **The ω₁ scoping bank** (kit gaps 2.3(b) + 4.3): on any uncountable `Ω`,
  the countable/co-countable σ-field `cocountableMeasurableSpace` carries
  the co-countable state `cocountableState`, which is
  - two-valued and σ-additive (`TwoValuedState` instance, proved),
  - NOT a Dirac restriction (`cocountableState_not_dirac`),
  - hence the σ-field is NOT countably generated
    (`cocountable_not_countably_generated` — a corollary of T3, which
    would otherwise point it),
  - yet Marczewski-COMPACT: the co-countable class with `∅` adjoined is
    countably compact (`cocountableClass_countablyCompact`) and
    approximates the field w.r.t. the state
    (`cocountableClass_approximates`).
  So the coarse killer state is a compact measure in Marczewski's sense —
  it kills the TOPOLOGICAL inner-regularity leg and cross-block
  intersection-stability, not abstract compactness (note §11e, scoping
  bank). Both T3 hypotheses are certified load-bearing: σ-continuity holds
  here (the state IS σ-additive), countable generation fails, Dirac
  realization fails.

## NOT formalized (recorded)
* Kit gap 2.3(a) (product-Ulam pattern intersections escape `L`) needs a
  non-membership invariant over the generated carrier of
  `UlamWitnessCore` — a separate construction; demoted to corroboration by
  the T3 machine-check, left to the oracle scripts.
* Marczewski 5(iii)/(iv) transfer theorems and M–RN §1 products: cited
  source-reading (kit gap 4.4(b)/(c)), nothing load-bearing to encode.

## Receipts
`#print axioms` at file end; everything `[propext, Classical.choice,
Quot.sound]`.
-/
import QuerySystem.ConcreteOMLBlocks

open Set Function MeasurableSpace

namespace SigmaEssential.Blocks

variable {Ω : Type*} {d : DynkinSystem Ω} {A B : Set Ω} {M : Set (Set Ω)}

/-! ## §1. Finite-stage helpers (d-level and block-level) -/

/-- Finite sups of a pairwise-disjoint family lie in the σ-class (finite
disjoint unions — no latticehood). -/
theorem has_finsetSup_of_disjoint {f : ℕ → Set Ω}
    (hdisj : Pairwise (Disjoint on f)) (hf : ∀ n, d.Has (f n))
    (s : Finset ℕ) : d.Has (s.sup f) := by
  classical
  induction s using Finset.cons_induction with
  | empty => simpa [Finset.sup_empty, Set.bot_eq_empty] using d.has_empty
  | cons a s ha ih =>
    rw [Finset.sup_cons]
    exact d.has_union (hf a) ih
      (Finset.disjoint_sup_right.mpr fun i hi => hdisj fun h => ha (h ▸ hi))

/-- A two-valued f.a. state vanishing on each member of a pairwise-disjoint
family vanishes on every finite sup. -/
theorem _root_.SigmaEssential.FinAddState.not_val_finsetSup
    (μ : FinAddState d) {f : ℕ → Set Ω}
    (hdisj : Pairwise (Disjoint on f)) (hf : ∀ n, d.Has (f n))
    (s : Finset ℕ) (h : ∀ i ∈ s, ¬ μ.Val (f i)) : ¬ μ.Val (s.sup f) := by
  classical
  induction s using Finset.cons_induction with
  | empty =>
    simpa [Finset.sup_empty, Set.bot_eq_empty] using μ.not_val_empty
  | cons a s ha ih =>
    rw [Finset.sup_cons]
    have hdisj' : Disjoint (f a) (s.sup f) :=
      Finset.disjoint_sup_right.mpr fun i hi => hdisj fun h => ha (h ▸ hi)
    intro hval
    rcases (μ.val_union (hf a) (has_finsetSup_of_disjoint hdisj hf s)
        hdisj').mp hval with h1 | h1
    · exact h a (Finset.mem_cons_self a s) h1
    · exact ih (fun i hi => h i (Finset.mem_cons_of_mem hi)) h1

/-- **In-block multiplicativity**: on a maximal block of a σ-class OML,
two-valued f.a. states multiply (the block is ∩-closed by A2, so the
Boolean `val_inter` derivation runs inside it). -/
theorem IsMaxBlock.val_inter (hM : IsMaxBlock d M) (hMeets : MeetsExist d)
    (μ : FinAddState d) (hA : A ∈ M) (hB : B ∈ M)
    (h1 : μ.Val A) (h2 : μ.Val B) : μ.Val (A ∩ B) := by
  have hII : d.Has (A ∩ B) := hM.has (hM.inter_mem hMeets hA hB)
  have hID : d.Has (A ∩ Bᶜ) := by
    rw [← Set.diff_eq]
    exact hM.has (hM.diff_mem hMeets hA hB)
  have hBc_false : ¬ μ.Val Bᶜ := fun h => (μ.val_compl (hM.has hB)).mp h h2
  have hID_false : ¬ μ.Val (A ∩ Bᶜ) := fun hbad =>
    hBc_false (μ.val_mono hID (d.has_compl (hM.has hB))
      Set.inter_subset_right hbad)
  have hsplit : A = (A ∩ B) ∪ (A ∩ Bᶜ) := by
    rw [← Set.inter_union_distrib_left, Set.union_compl_self, Set.inter_univ]
  have hdisj : Disjoint (A ∩ B) (A ∩ Bᶜ) :=
    Disjoint.mono Set.inter_subset_right Set.inter_subset_right
      disjoint_compl_right
  have := hsplit ▸ h1
  rcases (μ.val_union hII hID hdisj).mp this with h | h
  · exact h
  · exact absurd h hID_false

/-- In-block multiplicativity over finite families: the inf of finitely
many value-1 block members is value-1 (hence nonempty). -/
theorem IsMaxBlock.val_finsetInf (hM : IsMaxBlock d M) (hMeets : MeetsExist d)
    (μ : FinAddState d) {ι : Type*} {D : ι → Set Ω} {s : Finset ι}
    (hD : ∀ i ∈ s, D i ∈ M) (hval : ∀ i ∈ s, μ.Val (D i)) :
    (s.inf D ∈ M) ∧ μ.Val (s.inf D) := by
  classical
  induction s using Finset.cons_induction with
  | empty =>
    refine ⟨?_, ?_⟩ <;> simp only [Finset.inf_empty, Set.top_eq_univ]
    · exact hM.univ_mem
    · exact μ.val_univ
  | cons a s ha ih =>
    rw [Finset.inf_cons]
    have ih' := ih (fun i hi => hD i (Finset.mem_cons_of_mem hi))
      (fun i hi => hval i (Finset.mem_cons_of_mem hi))
    exact ⟨hM.inter_mem hMeets (hD a (Finset.mem_cons_self a s)) ih'.1,
      hM.val_inter hMeets μ (hD a (Finset.mem_cons_self a s)) ih'.1
        (hval a (Finset.mem_cons_self a s)) ih'.2⟩

/-! ## §2. Countably compact classes and the transport criterion -/

/-- **Marczewski countably compact class** (M 1953 §2, sequence form —
purely set-theoretic, his stated aim being "eliminating non-essential
topological concepts"): every sequence in the class whose finite
intersections are nonempty has nonempty total intersection. -/
def CountablyCompactClass (𝒦 : Set (Set Ω)) : Prop :=
  ∀ K : ℕ → Set Ω, (∀ n, K n ∈ 𝒦) →
    (∀ s : Finset ℕ, (s.inf K).Nonempty) → (⋂ n, K n).Nonempty

/-- **Marczewski approximation, two-valued in-block form** (M 1953 §3,
specialized as in note §11e / kit gap 4.4(a)): every value-1 member of the
family carries a value-1 INNER witness `D` in the family sandwiched below a
class member, `D ⊆ K ⊆ E`. (For value-0 members the general `η`-form is
vacuous once `∅ ∈ 𝒦`; two-valuedness reduces it to this.) -/
def ApproximatesOn (𝒦 : Set (Set Ω)) (μ : FinAddState d)
    (F : Set (Set Ω)) : Prop :=
  ∀ E ∈ F, μ.Val E → ∃ D ∈ F, ∃ K ∈ 𝒦, μ.Val D ∧ D ⊆ K ∧ K ⊆ E

/-- **The compact-transport criterion, in-block form** (M 1953 4(i),
two-valued, run inside one maximal block): a countably compact class
Marczewski-approximating the block w.r.t. `μ` forces the σ-condition on the
block. Proof = the corrected FIP argument of kit gap 4.4(a): tails are
value-1, their inner witnesses have value-1 (hence nonempty) finite
intersections, so the sandwich compacts have the FIP; countable compactness
then meets the empty tail intersection. -/
theorem IsMaxBlock.isSigmaOn_of_compact_class (hM : IsMaxBlock d M)
    (hMeets : MeetsExist d) (μ : FinAddState d) {𝒦 : Set (Set Ω)}
    (hcc : CountablyCompactClass 𝒦) (happrox : ApproximatesOn 𝒦 μ M) :
    IsSigmaOn μ M := by
  classical
  intro f hdisj hf
  have hu : (⋃ n, f n) ∈ M := hM.iUnion_mem hdisj hf
  constructor
  · -- value on the union forces a value-1 member, by the FIP argument
    intro hval
    by_contra hnone
    push Not at hnone
    -- the tails Fₙ = u \ (f₀ ∪ … ∪ f_{n-1}) are value-1 members of the block
    have hhasSup : ∀ n : ℕ, d.Has ((Finset.range n).sup f) := fun n =>
      has_finsetSup_of_disjoint hdisj (fun i => hM.has (hf i)) (Finset.range n)
    have hFmem : ∀ n : ℕ, (⋃ i, f i) \ (Finset.range n).sup f ∈ M := fun n =>
      hM.diff_mem hMeets hu (hM.finsetSup_mem hMeets fun i _ => hf i)
    have hsupsub : ∀ n, (Finset.range n).sup f ⊆ ⋃ i, f i := fun n =>
      Finset.sup_le fun i _ => Set.subset_iUnion f i
    have hFval : ∀ n, μ.Val ((⋃ i, f i) \ (Finset.range n).sup f) := by
      intro n
      have hsplit :
          (Finset.range n).sup f ∪ ((⋃ i, f i) \ (Finset.range n).sup f) =
            ⋃ i, f i := Set.union_diff_cancel (hsupsub n)
      have hval' : μ.Val ((Finset.range n).sup f ∪
          ((⋃ i, f i) \ (Finset.range n).sup f)) := by
        rw [hsplit]; exact hval
      rcases (μ.val_union (hhasSup n) (hM.has (hFmem n))
          disjoint_sdiff_right).mp hval' with h | h
      · exact absurd h (μ.not_val_finsetSup hdisj (fun i => hM.has (hf i))
          (Finset.range n) fun i _ => hnone i)
      · exact h
    -- the in-block sandwiches Dₙ ⊆ Kₙ ⊆ Fₙ
    choose D hDmem K hKmem hDval hDK hKF using fun n =>
      happrox _ (hFmem n) (hFval n)
    -- the Kₙ have the FIP: their inner witnesses have value-1 finite infs
    have hFIP : ∀ s : Finset ℕ, (s.inf K).Nonempty := by
      intro s
      have h1 := hM.val_finsetInf hMeets μ (D := D) (s := s)
        (fun i _ => hDmem i) (fun i _ => hDval i)
      have hne : (s.inf D).Nonempty := by
        rw [Set.nonempty_iff_ne_empty]
        intro hcon
        exact μ.not_val_empty (hcon ▸ h1.2)
      exact hne.mono (Finset.inf_mono_fun fun i _ => hDK i)
    -- countable compactness meets the empty tail intersection
    obtain ⟨x, hx⟩ := hcc K hKmem hFIP
    have hxF : ∀ n, x ∈ (⋃ i, f i) \ (Finset.range n).sup f := fun n =>
      hKF n (Set.mem_iInter.mp hx n)
    obtain ⟨k, hk⟩ := Set.mem_iUnion.mp (hxF 0).1
    exact (hxF (k + 1)).2
      (Finset.le_sup (f := f) (Finset.mem_range.mpr (Nat.lt_succ_self k)) hk)
  · rintro ⟨n, hn⟩
    exact μ.val_mono (hM.has (hf n)) (hM.has hu) (Set.subset_iUnion f n) hn

/-- **The compact-transport criterion, OML form** (note §11e, corrected
✎s16 statement): ONE countably compact class Marczewski-approximating
every maximal block in-block makes a two-valued f.a. state σ-additive
(per-block 4(i) + the A1c blockwise reduction). This is the intrinsic
engine for the coarse factor; B′(i) does not need it (§11c). -/
theorem compact_transport (hMeets : MeetsExist d)
    (μ : FinAddState d) {𝒦 : Set (Set Ω)}
    (hcc : CountablyCompactClass 𝒦)
    (happrox : ∀ M, IsMaxBlock d M → ApproximatesOn 𝒦 μ M) :
    IsSigmaOn μ (Carrier d) :=
  (isSigmaOn_carrier_iff_maxBlocks μ).mpr fun M hM =>
    hM.isSigmaOn_of_compact_class hMeets μ hcc (happrox M hM)

/-! ## §3. The ω₁ scoping bank: the coarse killer state, certified

Everything below lives on an arbitrary UNCOUNTABLE `Ω` (the note's ω₁ —
nothing uses more than uncountability). -/

section Cocountable

variable (Ω : Type*) [Uncountable Ω]

/-- The countable/co-countable σ-field. -/
@[reducible]
def cocountableMeasurableSpace : MeasurableSpace Ω where
  MeasurableSet' A := A.Countable ∨ Aᶜ.Countable
  measurableSet_empty := Or.inl Set.countable_empty
  measurableSet_compl A hA := by
    rcases hA with h | h
    · exact Or.inr (by rwa [compl_compl])
    · exact Or.inl h
  measurableSet_iUnion f hf := by
    classical
    by_cases h : ∀ i, (f i).Countable
    · exact Or.inl (Set.countable_iUnion h)
    · push Not at h
      obtain ⟨i, hi⟩ := h
      rcases hf i with hc | hc
      · exact absurd hc hi
      · exact Or.inr (hc.mono (Set.compl_subset_compl.mpr
          (Set.subset_iUnion f i)))

/-- Its σ-class packaging. -/
def cocountableDynkin : DynkinSystem Ω :=
  DynkinSystem.ofMeasurableSpace (cocountableMeasurableSpace Ω)

variable {Ω}

theorem cocountable_not_both {A : Set Ω} (hA : A.Countable)
    (hAc : Aᶜ.Countable) : False := by
  have huniv : (Set.univ : Set Ω).Countable := by
    rw [← Set.union_compl_self A]
    exact hA.union hAc
  exact not_countable (Set.countable_univ_iff.mp huniv)

variable (Ω)

/-- **The co-countable state**: value 1 exactly on co-countable sets. It is
two-valued and σ-ADDITIVE — the coarse killer of the corpus (the
countable/co-countable pattern of the witness's centre). -/
noncomputable def cocountableState : TwoValuedState (cocountableDynkin Ω) where
  Val A := Aᶜ.Countable
  decVal := Classical.decPred _
  val_univ := by simp
  not_val_empty := by
    simp only [Set.compl_empty]
    intro h
    exact not_countable (Set.countable_univ_iff.mp h)
  val_compl {A} hA := by
    rw [compl_compl]
    constructor
    · intro h hc
      exact cocountable_not_both h hc
    · intro h
      rcases hA with hc | hc
      · exact hc
      · exact absurd hc h
  val_iUnion {f} hdisj hf := by
    constructor
    · intro h
      by_contra hnone
      push Not at hnone
      have hall : ∀ i, (f i).Countable := fun i => by
        rcases hf i with hc | hc
        · exact hc
        · exact absurd hc (hnone i)
      exact cocountable_not_both (Set.countable_iUnion hall) h
    · rintro ⟨i, hi⟩
      exact hi.mono (Set.compl_subset_compl.mpr (Set.subset_iUnion f i))

/-- The co-countable state is **not a Dirac restriction**: it disagrees
with every point evaluation on the co-countable set `{ω}ᶜ`. -/
theorem cocountableState_not_dirac :
    ∀ ω : Ω, ∃ A, (cocountableDynkin Ω).Has A ∧
      (cocountableState Ω).Val A ∧ ω ∉ A := fun ω =>
  ⟨{ω}ᶜ, Or.inr (by rw [compl_compl]; exact Set.countable_singleton ω),
    by simp [cocountableState],
    fun h => h rfl⟩

/-- Hence `IsDirac` fails outright. -/
theorem cocountableState_not_isDirac :
    ¬ (cocountableState Ω).IsDirac := by
  rintro ⟨ω, h⟩
  obtain ⟨A, _, hval, hω⟩ := cocountableState_not_dirac Ω ω
  have hval' : (dirac (d := cocountableDynkin Ω) ω).Val A := h ▸ hval
  exact hω hval'

/-- **The countable/co-countable σ-field is NOT countably generated**
(kit gap 2.3(b), second half) — a corollary of T3: countable generation
would point the co-countable state, but it is non-Dirac. So T3's
countable-generation hypothesis is load-bearing. -/
theorem cocountable_not_countably_generated :
    ¬ ∃ G : ℕ → Set Ω, cocountableMeasurableSpace Ω =
      MeasurableSpace.generateFrom (Set.range G) := by
  rintro ⟨G, hgen⟩
  obtain ⟨D, _, hDne, _, _, hpt⟩ :=
    dirac_realization_of_countablyGenerated (cocountableMeasurableSpace Ω) G
      hgen (cocountableState Ω)
  obtain ⟨ω, hω⟩ := hDne
  obtain ⟨A, hA, hval, hnω⟩ := cocountableState_not_dirac Ω ω
  exact hnω ((hpt ω hω A hA).mp hval)

/-- The co-countable class, with `∅` adjoined (the ✎s16 fix: approximation
quantifies over null sets too). -/
def cocountableClass : Set (Set Ω) := insert ∅ {K : Set Ω | Kᶜ.Countable}

/-- **The co-countable class is countably compact** (kit gap 4.3(a)): a
countable intersection of co-countables is co-countable, hence nonempty on
uncountable `Ω`; a sequence containing `∅` fails the FIP vacuously. -/
theorem cocountableClass_countablyCompact :
    CountablyCompactClass (cocountableClass Ω) := by
  intro K hK hFIP
  have hcc : ∀ n, (K n)ᶜ.Countable := by
    intro n
    rcases hK n with h | h
    · exfalso
      obtain ⟨x, hx⟩ := hFIP {n}
      rw [Finset.inf_singleton, h] at hx
      exact hx
    · exact h
  have hint : (⋂ n, K n)ᶜ.Countable := by
    rw [Set.compl_iInter]
    exact Set.countable_iUnion hcc
  rw [Set.nonempty_iff_ne_empty]
  intro hcon
  rw [hcon, Set.compl_empty] at hint
  exact not_countable (Set.countable_univ_iff.mp hint)

/-- **The co-countable class Marczewski-approximates the field w.r.t. the
co-countable state** (kit gap 4.3(b)): the sandwich for a value-1 (i.e.
co-countable) `E` is `E ⊆ E ⊆ E`. So the coarse killer is a COMPACT
measure in Marczewski's sense — Marczewski compactness ≠ topological
(8.1)-regularity, which it kills (note §10). -/
theorem cocountableClass_approximates :
    ApproximatesOn (d := cocountableDynkin Ω) (cocountableClass Ω)
      ((cocountableState Ω).toFinAdd) (Carrier (cocountableDynkin Ω)) := by
  intro E hE hval
  exact ⟨E, hE, E, Or.inr hval, hval, subset_rfl, subset_rfl⟩

end Cocountable

/-! ## §4. Receipts -/

#print axioms has_finsetSup_of_disjoint
#print axioms SigmaEssential.FinAddState.not_val_finsetSup
#print axioms IsMaxBlock.val_inter
#print axioms IsMaxBlock.val_finsetInf
#print axioms IsMaxBlock.isSigmaOn_of_compact_class
#print axioms compact_transport
#print axioms cocountableState
#print axioms cocountableState_not_isDirac
#print axioms cocountable_not_countably_generated
#print axioms cocountableClass_countablyCompact
#print axioms cocountableClass_approximates

end SigmaEssential.Blocks
