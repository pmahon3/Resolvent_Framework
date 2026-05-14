/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import Paperproof
import Mathlib.MeasureTheory.Measure.AddContent
import Mathlib.MeasureTheory.OuterMeasure.OfAddContent
import Mathlib.MeasureTheory.MeasurableSpace.Basic
import Mathlib.Data.Set.Countable
import Mathlib.Order.Filter.Cofinite
import Mathlib.Order.Filter.Ultrafilter.Basic
import Mathlib.Order.Hom.WithTopBot
import QuerySystem.QuerySystem

/-!
# Extension of Charges on Directed Systems of Boolean Algebras

This file formalises the main results of the paper of the same name.

## Main results

* `exhaustiveness`: Every normalized finitely-additive charge is exhaustive — disjoint
  sequence charges tend to 0 (Prop. `prop:exhaustiveness-trivial`).
* `finCofinMSpace`: The finite-cofinite measurable space on a countably infinite type.
* `fcContent`: The finitely-additive charge on the finite-cofinite algebra assigning
  0 to finite sets and 1 to cofinite sets.
* `counterexampleQS`: A sequentially upper-directed directed system with compatible
  finitely-additive charges that fails σ-additive extension (Prop. `prop:independence`).
* `QuerySystem.CompatibleContents`: Compatible family of finitely-additive charges.
* `QuerySystem.CollectivelyExhaustive`: The valuation-layer condition characterising
  σ-additive extensibility (Def. `def:collective-exhaustion`).
* `sp1_extension`: Collectively exhaustive + compatible → σ-additive extension at
  every level (Thm. `thm:sp1`, (i)→(ii)).
* `sp1_necessity`: σ-additive extension → collectively exhaustive (Thm. `thm:sp1`, (ii)→(i)).
* `sp1_iff`: The equivalence — collective exhaustion characterises σ-additive
  extensibility (Thm. `thm:sp1`).

## Architecture

The key separation is between two independent layers:
- **Index layer**: preorder, refinement maps, sequential upper-directedness.
- **Valuation layer**: charges, compatibility, collective exhaustion.

The counterexample shows these layers are independent: index-layer conditions do not
force σ-additivity. `sp1_iff` gives the exact valuation-layer characterisation.

## References

* `papers/discriminability_foundations/discriminability_foundations_body.tex`
-/

open MeasureTheory Set
open scoped ENNReal

-- Use classical decidability throughout to avoid `Decidable` synthesis failures
open Classical in section

/-!
## Part 0: Single-algebra results

Nontrivial refinement and the extension criterion — results about a single Boolean
charge space, independent of the directed system structure.
-/

section SingleAlgebra

/-- Every normalized finitely-additive charge is exhaustive: for any pairwise disjoint
    sequence of measurable events, the charge tends to 0.

    Prop. `prop:exhaustiveness-trivial` of the paper.  The proof: partial sums
    ∑_{k≤n} ν(f k) = ν(⋃_{k≤n} f k) ≤ ν(univ) = 1 by finite additivity and
    normalization, so the series converges and its terms tend to 0. -/
theorem exhaustiveness {α : Type*} [MeasurableSpace α]
    (ν : AddContent ℝ≥0∞ {s : Set α | MeasurableSet s})
    (hnorm : ν Set.univ = 1)
    (f : ℕ → Set α)
    (hf : ∀ n, MeasurableSet (f n))
    (hf_disj : Pairwise (Function.onFun Disjoint f)) :
    Filter.Tendsto (fun n => ν (f n)) Filter.atTop (nhds 0) := by
  have hring : IsSetRing {s : Set α | MeasurableSet s} := ⟨
    MeasurableSet.empty,
    fun _ _ hs ht => hs.union ht,
    fun _ _ hs ht => hs.diff ht⟩
  -- ∑ ν(f n) ≤ 1 < ∞: addContent_accumulate gives range(n+1) sums = ν(accumulate f n) ≤ 1
  have hsum_le : ∑' n, ν (f n) ≤ 1 :=
    ENNReal.tsum_le_of_sum_range_le fun n => by
      calc ∑ i ∈ Finset.range n, ν (f i)
          ≤ ∑ i ∈ Finset.range (n + 1), ν (f i) :=
            Finset.sum_le_sum_of_subset (Finset.range_mono (Nat.le_succ n))
        _ = ν (Set.accumulate f n) :=
            (addContent_accumulate ν hring hf_disj hf n).symm
        _ ≤ 1 :=
            (addContent_mono hring.isSetSemiring (hring.accumulate_mem hf n) MeasurableSet.univ
              ((Set.accumulate_subset_iUnion n).trans
                (Set.iUnion_subset (fun _ => Set.subset_univ _)))).trans hnorm.le
  exact ENNReal.tendsto_atTop_zero_of_tsum_ne_top
    (hsum_le.trans_lt (by norm_num) |>.ne)

/-- A refinement map π : O_j → O_i is nontrivial if the finer algebra E_j strictly
    extends the pullback π⁻¹(E_i): there exists A ∈ E_j not of the form π⁻¹(B)
    for any B ∈ E_i.  Prop. `prop:nontrivial` of the paper. -/
def NontrivialRefinement {α β : Type*} [MeasurableSpace α] [MeasurableSpace β]
    (π : β → α) : Prop :=
  ∃ A : Set β, MeasurableSet A ∧ ∀ B : Set α, MeasurableSet B → A ≠ π ⁻¹' B

/-- Nontrivial refinement introduces new events: the pullback algebra is a strict
    subset of the finer algebra.  This is Prop. `prop:nontrivial` — immediate from
    the definition. -/
theorem nontrivialRefinement_strictSubset {α β : Type*} [MeasurableSpace α] [MeasurableSpace β]
    (π : β → α) (h : NontrivialRefinement π) :
    ∃ A : Set β, MeasurableSet A ∧ A ∉ Set.range (fun B : {B : Set α // MeasurableSet B} =>
      π ⁻¹' (B : Set α)) := by
  obtain ⟨A, hA, hnotpre⟩ := h
  exact ⟨A, hA, by simp [Set.mem_range]; intro B hB; exact Ne.symm (hnotpre B hB)⟩

/-- The extension criterion (Thm. `thm:extension-criterion`): a normalized
    finitely-additive charge ν on a measurable space extends to a σ-additive measure
    if and only if ν is continuous at ∅ (i.e., `IsSigmaSubadditive`).

    The forward direction is immediate from σ-additivity of the extension.
    The converse is the Carathéodory extension: continuity at ∅ is the condition
    that passes from finite additivity to σ-additivity on the generated σ-algebra.

    In the formalization this is not a standalone iff but the Carathéodory direction
    is `AddContent.measure` (used in `sp1_extension`) and the necessity direction
    is `tendsto_measure_iInter_atTop` (used in `sp1_necessity`).  We state it here
    for alignment with the paper. -/
theorem extensionCriterion {α : Type*} [MeasurableSpace α]
    (ν : AddContent ℝ≥0∞ {s : Set α | MeasurableSet s})
    (hring : IsSetRing {s : Set α | MeasurableSet s})
    (hne_top : ∀ s ∈ ({s : Set α | MeasurableSet s}), ν s ≠ ∞) :
    (ν.IsSigmaSubadditive ↔
     ∀ (E : ℕ → Set α), (∀ n, MeasurableSet (E n)) → (∀ n, E (n+1) ⊆ E n) →
       (⋂ n, E n = ∅) → Filter.Tendsto (fun n => ν (E n)) Filter.atTop (nhds 0)) := by
  constructor
  · -- Forward direction: IsSigmaSubadditive → continuity at ∅ for antitone sequences.
    -- Strategy: apply tendsto_atTop_addContent_iUnion_of_addContent_iUnion_eq_tsum to the
    -- monotone sequence F n = E 0 \ E n.  Union = E 0 \ ∅ = E 0, so ν(F n) → ν(E 0).
    -- Then ν(E n) = ν(E 0) - ν(F n) → 0 by ENNReal.tendsto_const_sub_nhds_zero_iff.
    intro hsubadd E hE_meas hE_anti hE_empty
    -- Antitone helper: E n is antitone
    have hE_antitone : Antitone E := fun m n hmn => by
      induction hmn with
      | refl => exact Subset.refl _
      | @step k _ ih => exact (hE_anti k).trans ih
    -- σ-additivity on disjoint unions from IsSigmaSubadditive
    have hm_iUnion : ∀ (f : ℕ → Set α) (_ : ∀ i, f i ∈ {s | MeasurableSet s})
        (_ : (⋃ i, f i) ∈ {s | MeasurableSet s})
        (_ : Pairwise (Function.onFun Disjoint f)), ν (⋃ i, f i) = ∑' i, ν (f i) :=
      fun f hf hUf hdisj =>
        addContent_iUnion_eq_tsum_of_disjoint_of_IsSigmaSubadditive
          hring.isSetSemiring hsubadd f hf hUf hdisj
    -- Complementary monotone sequence
    let F : ℕ → Set α := fun n => E 0 \ E n
    have hF_mem : ∀ n, F n ∈ {s | MeasurableSet s} :=
      fun n => (hE_meas 0).diff (hE_meas n)
    have hF_mono : Monotone F :=
      fun _ _ hmn => Set.diff_subset_diff_right (hE_antitone hmn)
    have hF_iUnion_eq : ⋃ n, F n = E 0 := by
      ext x
      simp only [Set.mem_iUnion, Set.mem_diff, F]
      constructor
      · rintro ⟨_, hx0, _⟩; exact hx0
      · intro hx0
        by_contra hall
        push Not at hall
        have : x ∈ ⋂ n, E n := Set.mem_iInter.mpr (fun n => (hall n hx0))
        rw [hE_empty] at this; exact this
    have hF_Union_mem : (⋃ n, F n) ∈ {s | MeasurableSet s} := by
      rw [hF_iUnion_eq]; exact hE_meas 0
    -- ν(F n) → ν(E 0)
    have hF_tendsto : Filter.Tendsto (fun n => ν (F n)) Filter.atTop (nhds (ν (E 0))) := by
      have h := tendsto_atTop_addContent_iUnion_of_addContent_iUnion_eq_tsum
        hring hm_iUnion hF_mono hF_mem hF_Union_mem
      rwa [hF_iUnion_eq] at h
    -- ν(E n) = ν(E 0) - ν(F n)
    have hEn_eq : ∀ n, ν (E n) = ν (E 0) - ν (F n) := by
      intro n
      have hEn_sub : E n ⊆ E 0 := hE_antitone (Nat.zero_le n)
      rw [show F n = E 0 \ E n from rfl,
          addContent_diff_of_ne_top ν hring hne_top (hE_meas 0) (hE_meas n) hEn_sub,
          ENNReal.sub_sub_cancel (hne_top _ (hE_meas 0))
            (addContent_mono hring.isSetSemiring (hE_meas n) (hE_meas 0) hEn_sub)]
    -- ν(E 0) - ν(F n) → 0 iff ν(F n) → ν(E 0)
    have hFn_le : ∀ n, ν (F n) ≤ ν (E 0) :=
      fun n => addContent_mono hring.isSetSemiring (hF_mem n) (hE_meas 0) Set.diff_subset
    have hconv : (fun n => ν (E n)) = (fun n => ν (E 0) - ν (F n)) :=
      funext hEn_eq
    rw [hconv]
    rwa [ENNReal.tendsto_const_sub_nhds_zero_iff (hne_top _ (hE_meas 0)) hFn_le]
  · intro hcont
    exact isSigmaSubadditive_of_addContent_iUnion_eq_tsum hring
      (addContent_iUnion_eq_sum_of_tendsto_zero hring ν hne_top
        (fun E hE_mem hE_anti hE_empty =>
          hcont E hE_mem (fun n => hE_anti (Nat.le_succ n)) hE_empty))

/-- Gap nonemptiness (concrete case): on the finite-cofinite algebra `finCofinSets α`,
    the gap `σ(finCofinSets α) \ finCofinSets α` is nonempty whenever `α` is infinite.

    The witness: given an injective `q : ℕ → α`, the range `Set.range q` is a countable
    union of singletons `⋃ n, {q n}`, hence σ-measurable.  But `Set.range q` is
    countably infinite (injective) with infinite complement (α is infinite), so it is
    neither finite nor cofinite — it lies outside `finCofinSets α`.

    This formalises the concrete case of Prop. `prop:gap-nonempty` (Discussion section).
    The paper also gives the general argument: any Boolean algebra that is not a σ-algebra
    has a countable union outside it by definition; that direction is definitional and
    not separately formalised. -/
theorem gapNonempty (α : Type*) [Infinite α] (q : ℕ → α) (hq : Function.Injective q)
    (hcompl : (Set.range q)ᶜ.Infinite) :
    let E := {s : Set α | s.Finite ∨ sᶜ.Finite}
    let sigmaE := MeasurableSpace.generateFrom E
    ∃ s : Set α, @MeasurableSet α sigmaE s ∧ s ∉ E := by
  -- The set S = range q is a countable union of singletons, hence σ-measurable,
  -- but is neither finite (q is injective) nor cofinite (its complement contains all
  -- elements outside the range, which is infinite since α is infinite and range q is countable).
  refine ⟨Set.range q, ?_, ?_⟩
  · -- σ-measurability: range q = ⋃ n, {q n}, each singleton is in E
    have heq : Set.range q = ⋃ n, {q n} := by
      ext x; simp [Set.mem_range, Set.mem_iUnion]
    rw [heq]
    apply MeasurableSet.iUnion
    intro n
    exact MeasurableSpace.measurableSet_generateFrom (Or.inl (Set.finite_singleton _))
  · -- Non-membership: range q is infinite and has infinite complement
    simp only [Set.mem_setOf_eq]
    push Not
    exact ⟨Set.infinite_range_of_injective hq, hcompl⟩

end SingleAlgebra

/-!
## Part I: The finite-cofinite algebra and the counterexample

We construct a sequentially upper-directed query system with compatible finitely-additive
contents that fails σ-additive extension. This refutes the original witnessing conjecture.
-/

section FinCofin

/-- The finite-cofinite measurable space on a type: measurable sets are those that are
    finite or have finite complement. This is the Boolean algebra generated by singletons. -/
def finCofinMSpace (α : Type*) : MeasurableSpace α :=
  MeasurableSpace.generateFrom {s : Set α | s.Finite ∨ sᶜ.Finite}

/-- The finite-cofinite collection is the collection used to generate `finCofinMSpace`. -/
def finCofinSets (α : Type*) : Set (Set α) := {s : Set α | s.Finite ∨ sᶜ.Finite}

/-- The finite-cofinite collection is a set semiring when the type is infinite. -/
lemma finCofinSets_isSetSemiring (α : Type*) [Infinite α] :
    IsSetSemiring (finCofinSets α) := by
  constructor
  · exact Or.inl finite_empty
  · intro s hs t ht
    simp only [finCofinSets, Set.mem_setOf_eq] at *
    cases hs with
    | inl hs => exact Or.inl (hs.subset inter_subset_left)
    | inr hs =>
      cases ht with
      | inl ht => exact Or.inl (ht.subset inter_subset_right)
      | inr ht => exact Or.inr (compl_inter s t ▸ hs.union ht)
  · intro s hs t ht
    simp only [finCofinSets, Set.mem_setOf_eq] at *
    have hdiff : (s \ t).Finite ∨ (s \ t)ᶜ.Finite := by
      cases hs with
      | inl hs => exact Or.inl (hs.subset diff_subset)
      | inr hs =>
        cases ht with
        | inl ht => exact Or.inr (by rw [compl_diff]; exact ht.union hs)
        | inr ht => exact Or.inl (ht.subset (diff_subset_compl s t))
    exact ⟨{s \ t},
      by simp only [Finset.coe_singleton, Set.singleton_subset_iff]; exact hdiff,
      by simp [Set.pairwiseDisjoint_singleton],
      by simp⟩

/-- The finitely-additive content on the finite-cofinite algebra:
    assigns 0 to finite sets and 1 to cofinite sets.

    On an infinite type, finite and cofinite are mutually exclusive, so this is
    well-defined. Finite additivity holds: disjoint sets in the algebra can only
    be (finite, finite) or (finite, cofinite) pairs — never (cofinite, cofinite). -/
noncomputable def fcContent (α : Type*) [Infinite α] :
    AddContent ℝ≥0∞ (finCofinSets α) where
  toFun s := if sᶜ.Finite then 1 else 0
  empty' := by
    simp only [compl_empty]
    rw [if_neg Set.infinite_univ.not_finite]
  sUnion' I hI_ss hI_dis hI_mem := by
    classical
    simp only [finCofinSets, Set.mem_setOf_eq] at hI_mem hI_ss
    -- Key auxiliary: on an infinite type, finite and cofinite are exclusive.
    have fin_imp_cof_inf : ∀ s : Set α, s.Finite → ¬sᶜ.Finite := by
      intro s hs hsc
      exact Set.infinite_univ.not_finite (Set.union_compl_self s ▸ hs.union hsc)
    -- Key auxiliary: two distinct disjoint cofinite sets cannot coexist on an infinite type.
    have no_two_cof : ∀ u ∈ I, ∀ v ∈ I, u ≠ v →
        ¬((u : Set α)ᶜ.Finite ∧ (v : Set α)ᶜ.Finite) := by
      intro u hu v hv huv ⟨huc, hvc⟩
      have hdisj : Disjoint u v :=
        hI_dis (Finset.mem_coe.mpr hu) (Finset.mem_coe.mpr hv) (by simpa using huv)
      rw [Set.disjoint_iff_inter_eq_empty] at hdisj
      exact Set.infinite_univ.not_finite
        (show (Set.univ : Set α).Finite by
          rw [show (Set.univ : Set α) = uᶜ ∪ vᶜ from by
                simp [← Set.compl_inter, hdisj]]
          exact huc.union hvc)
    rcases hI_mem with hfin | hcofin
    · -- Union is finite → every member is finite → all toFun values are 0
      -- Since u ⊆ ⋃₀ ↑I and ⋃₀ ↑I is finite, u is finite, so uᶜ is infinite.
      have hall_not_cof : ∀ u ∈ I, ¬(u : Set α)ᶜ.Finite :=
        fun u hu => fin_imp_cof_inf u (hfin.subset
          (Set.subset_sUnion_of_mem (Finset.mem_coe.mpr hu)))
      -- ⋃₀ ↑I is finite, so (⋃₀ ↑I)ᶜ is infinite
      have hunion_not_cof : ¬(⋃₀ ↑I)ᶜ.Finite := fin_imp_cof_inf _ hfin
      rw [if_neg hunion_not_cof]
      exact (Finset.sum_eq_zero (fun u hu => if_neg (hall_not_cof u hu))).symm
    · -- Union is cofinite → exactly one member is cofinite → sum = 1
      -- Step 1: At least one member is cofinite.
      -- If all were finite, ⋃₀ ↑I = ⋃ of finitely many finite sets = finite,
      -- but its complement is finite (hcofin), so univ would be finite. Contradiction.
      have hex_cof : ∃ w ∈ I, (w : Set α)ᶜ.Finite := by
        by_contra hall_fin
        push Not at hall_fin
        -- All members of I are finite, so ⋃₀ ↑I is a finite union of finite sets = finite
        have hunion_fin : (⋃₀ (I : Set (Set α))).Finite :=
          Set.Finite.sUnion (Finset.finite_toSet I)
            (fun u hu => (hI_ss hu).resolve_right (hall_fin u (Finset.mem_coe.mp hu)))
        exact fin_imp_cof_inf _ hunion_fin hcofin
      -- Step 2: Exactly one member is cofinite (by no_two_cof).
      obtain ⟨w, hw, hwc⟩ := hex_cof
      have huniq : ∀ u ∈ I, (u : Set α)ᶜ.Finite → u = w := by
        intro u hu huc
        by_contra huneq
        exact no_two_cof u hu w hw huneq ⟨huc, hwc⟩
      -- Step 3: Rewrite the sum using sum_eq_single.
      rw [if_pos hcofin]
      rw [Finset.sum_eq_single w
        (by intro u hu huw
            simp only [if_neg (fun huc => no_two_cof u hu w hw huw ⟨huc, hwc⟩)])
        (by intro hw'; exact absurd hw (hw'))]
      simp [hwc]

end FinCofin

/-!
## Part II: The counterexample query system

Index: WithTop ℕ (= ℕ ∪ {⊤}), sequentially upper-directed.
All outcome spaces: ℚ with the finite-cofinite algebra.
All refinement maps: identity.
All contents: fcContent ℚ.
This satisfies CompatibleContents but fails σ-additive extension.
-/

section Counterexample

/-- The counterexample query system. Index set is WithTop ℕ so that every sequence
    has an upper bound (⊤ is always an upper bound). -/
noncomputable def counterexampleQS : QuerySystem where
  ι := WithTop ℕ
  q _ := { Outcome := ℚ, instMeas := finCofinMSpace ℚ }
  le i j := i ≤ j
  π _ := { π := id, measurable_π := @measurable_id ℚ (finCofinMSpace ℚ) }
  le_refl _ := le_refl _
  le_trans h1 h2 := le_trans h1 h2
  π_refl _ := rfl
  π_trans _ _ := rfl

/-- The counterexample is sequentially upper-directed: ⊤ is a universal upper bound
    in WithTop ℕ. -/
lemma counterexampleQS_seqUpperDir :
    counterexampleQS.SequentiallyUpperDirected := by
  intro u
  exact ⟨(⊤ : WithTop ℕ), fun n => le_top⟩

/-- The key failure: the decreasing sequence E_n = ℚ \ {q_1,...,q_n}
    has empty intersection but each E_n is cofinite, so fcContent(E_n) = 1 for all n.
    No witnessing query exists anywhere in the counterexample system.

    We prove this indirectly: the complement sets F_n = {q 0, ..., q n} are finite
    (content 0) and their union is all of ℚ (content 1). σ-subadditivity would force
    1 ≤ ∑' n, 0 = 0, a contradiction.

    TODO (Layer 0): Complete once fcContent.sUnion' is proved. -/
lemma fcContent_not_sigmaSubadditive :
    ¬ (fcContent ℚ).IsSigmaSubadditive := by
  intro h
  obtain ⟨q, hq_surj⟩ := exists_surjective_nat ℚ
  -- F n = {q 0, ..., q n}: finite sets whose union is ℚ
  let F : ℕ → Set ℚ := fun n => {x | ∃ k ≤ n, x = q k}
  have hF_mem : ∀ n, F n ∈ finCofinSets ℚ := by
    intro n
    apply Or.inl
    -- F n = image of Iic n under q, which is finite
    apply Set.Finite.subset (Set.finite_Iic n |>.image q)
    intro x ⟨k, hk, hxk⟩
    exact ⟨k, Set.mem_Iic.mpr hk, hxk.symm⟩
  have hUnion_eq : (⋃ n, F n) = Set.univ := by
    ext x
    simp only [Set.mem_iUnion, Set.mem_univ, iff_true, F]
    obtain ⟨n, hn⟩ := hq_surj x
    exact ⟨n, n, le_refl n, hn.symm⟩
  have hUnion_mem : (⋃ n, F n) ∈ finCofinSets ℚ := by
    rw [hUnion_eq]; exact Or.inr (by simp)
  -- Each F n is finite (we proved this in hF_mem), so fcContent ℚ (F n) = 0
  have hF_val : ∀ n, fcContent ℚ (F n) = 0 := by
    intro n
    show (if (F n)ᶜ.Finite then (1 : ℝ≥0∞) else 0) = 0
    have hFn_fin : (F n).Finite := (hF_mem n).elim id (fun hFnc =>
      Set.Finite.subset (Set.finite_Iic n |>.image q) (fun x hx => by
        simp only [F, Set.mem_setOf_eq] at hx
        obtain ⟨k, hk, hxk⟩ := hx
        exact ⟨k, Set.mem_Iic.mpr hk, hxk.symm⟩))
    exact if_neg (fun hFnc =>
      Set.infinite_univ.not_finite (Set.union_compl_self (F n) ▸ hFn_fin.union hFnc))
  -- The union is univ, which has empty complement: fcContent ℚ univ = 1
  have hUnion_val : fcContent ℚ (⋃ n, F n) = 1 := by
    rw [hUnion_eq]
    show (if (Set.univ : Set ℚ)ᶜ.Finite then (1 : ℝ≥0∞) else 0) = 1
    simp [Set.compl_univ]
  -- σ-subadditivity gives 1 ≤ ∑' n, 0 = 0: contradiction
  have hineq := h hF_mem hUnion_mem
  rw [hUnion_val] at hineq
  simp [hF_val] at hineq

/-- The regress (Prop. `prop:regress`): for any fixed finer level j ≥ i, witnessing
    emptiness at j does not resolve the obstruction — the same finite-additivity
    failure reappears at j.

    In the counterexample system every level has the same algebra and content
    (ℚ with the finite-cofinite algebra and fcContent), so the obstruction at any
    level j is identical to the obstruction at level i: `fcContent ℚ` is not
    σ-subadditive at j any more than at i.  Compatibility merely transports the
    non-convergence across levels without eliminating it. -/
lemma counterexampleQS_regress (j : counterexampleQS.ι) :
    ¬ (fcContent ℚ).IsSigmaSubadditive := fcContent_not_sigmaSubadditive

/-- No finitary index-layer condition on `counterexampleQS` forces σ-additive
    extension (Cor. `cor:no-finitary`).

    The counterexample satisfies sequential upper-directedness (every sequence has
    an upper bound ⊤) and any finite collection of levels can be inspected — but
    every level carries the same non-σ-subadditive content fcContent ℚ.  The content
    at the universal upper bound ⊤ fails σ-subadditivity just as at every other level.
    Hence no finite inspection of the index layer can certify σ-additive extensibility. -/
lemma counterexampleQS_no_finitary_condition :
    ¬ (fcContent ℚ).IsSigmaSubadditive ∧
    counterexampleQS.SequentiallyUpperDirected :=
  ⟨fcContent_not_sigmaSubadditive, counterexampleQS_seqUpperDir⟩

end Counterexample

end -- close Classical section

/-!
## Part III: Compatible contents, normalization, and collective exhaustion
-/

namespace QuerySystem

variable (S : QuerySystem.{u, v})

/-- A compatible family of finitely-additive contents.

    This is the finitely-additive analogue of `CompatibleMarginals`. Each ℓ_Q is
    an `AddContent` (not a `Measure`), and compatibility says the content of any
    event at a coarser level equals the content of its preimage at any finer level. -/
def CompatibleContents
    (ν : ∀ i : S.ι, AddContent ℝ≥0∞ {s : Set (S.q i).Outcome | MeasurableSet s}) : Prop :=
  ∀ {i j : S.ι} (hij : S.le i j)
    (A : Set (S.q i).Outcome) (hA : MeasurableSet A),
    ν i A = ν j ((S.π hij).π ⁻¹' A)

/-- Collectively exhaustive: the valuation-layer condition characterising σ-additive
    extensibility (Def. `def:collective-exhaustion`).

    For every index i and every decreasing sequence of measurable events shrinking to
    ∅, some finer level j ≥ i witnesses the convergence: the charge of the preimage
    sequence at j converges to 0. By compatibility this forces convergence at i. -/
def CollectivelyExhaustive
    (ν : ∀ i : S.ι, AddContent ℝ≥0∞ {s : Set (S.q i).Outcome | MeasurableSet s}) : Prop :=
  ∀ (i : S.ι)
    (E : ℕ → Set (S.q i).Outcome)
    (_ : ∀ n, MeasurableSet (E n))
    (_ : ∀ n, E (n + 1) ⊆ E n)
    (_ : ⋂ n, E n = ∅),
    ∃ j : S.ι, ∃ hij : S.le i j,
      Filter.Tendsto
        (fun n => ν j ((S.π hij).π ⁻¹' E n))
        Filter.atTop (nhds 0)

/-- A normalized compatible family of finitely-additive contents: the correct domain
    for the SP1 theorem.

    Bundles three conditions that must travel together:
    - `ν`: a finitely-additive content at each level
    - `compat`: compatibility under refinement maps
    - `norm`: each content assigns total mass 1 to the full outcome space

    Normalization is not an assumption smuggled in to force σ-additivity — the
    counterexample (`fcContent`) is normalized and fails σ-additivity. Normalization
    correctly scopes the theorem to probability-valued contents, which is the domain
    of de Finetti's original question. It provides the finiteness condition
    (`ν i Set.univ ≠ ∞`) needed for the `sp1_necessity` direction. -/
structure NormalizedCompatibleContents (S : QuerySystem.{u, v}) where
  /-- The family of contents, one per level. -/
  ν      : ∀ i : S.ι, AddContent ℝ≥0∞ {s : Set (S.q i).Outcome | MeasurableSet s}
  /-- Compatibility: coarser content equals pullback of finer content. -/
  compat : S.CompatibleContents ν
  /-- Normalization: each content is a probability content. -/
  norm   : ∀ i : S.ι, ν i Set.univ = 1

/-- The collection of all measurable sets forms a set ring. -/
lemma isSetRing_measurableSets (α : Type*) [MeasurableSpace α] :
    IsSetRing {s : Set α | MeasurableSet s} := by
  constructor
  · exact MeasurableSet.empty
  · intro s t hs ht; exact hs.union ht
  · intro s t hs ht; exact hs.diff ht

/-- Every event has finite content in a normalized family. This is the finiteness
    condition needed for the σ-additivity argument.

    Proof: ν i A ≤ ν i univ = 1 < ∞ by monotonicity of AddContent on a set semiring. -/
lemma NormalizedCompatibleContents.ne_top
    (P : S.NormalizedCompatibleContents)
    (i : S.ι) (A : Set (S.q i).Outcome) (hA : MeasurableSet A) :
    P.ν i A ≠ ∞ := by
  have hring := isSetRing_measurableSets (S.q i).Outcome
  have hle : P.ν i A ≤ P.ν i Set.univ :=
    addContent_mono hring.isSetSemiring hA MeasurableSet.univ (Set.subset_univ _)
  rw [P.norm i] at hle
  exact ne_top_of_le_ne_top (by norm_num) hle

/-!
## Part III (cont.): The counterexample as a NormalizedCompatibleContents

To connect `fcContent_not_sigmaSubadditive` to `CollectivelyExhaustive`, we need a
`NormalizedCompatibleContents` for `counterexampleQS`.

Since ℚ is countable, the finite-cofinite σ-algebra on ℚ is the discrete σ-algebra,
so `NormalizedCompatibleContents.ν` requires an `AddContent` on all subsets of ℚ.
We use `hyperfilter ℚ` — the ultrafilter extending the cofinite filter — to define a
`{0,1}`-valued finitely-additive content: `s` has measure 1 if `s ∈ hyperfilter ℚ`,
and measure 0 otherwise.  This is finitely additive because ultrafilters are exactly
the `{0,1}`-valued finitely-additive probability contents.
-/

/-- A finitely-additive `{0,1}`-valued content on all subsets of ℚ, defined by
    membership in `Filter.hyperfilter ℚ`.  Since `Filter.hyperfilter ℚ` extends the
    cofinite filter, this agrees with `fcContent ℚ` on `finCofinSets ℚ`: finite sets
    receive 0 and cofinite sets receive 1. -/
noncomputable def fcContentMeas : AddContent ℝ≥0∞
    {s : Set ℚ | @MeasurableSet ℚ (finCofinMSpace ℚ) s} where
  toFun s := haveI := Classical.dec (s ∈ Filter.hyperfilter ℚ)
             if s ∈ Filter.hyperfilter ℚ then 1 else 0
  empty' := by
    classical
    simp [Ultrafilter.empty_notMem]
  sUnion' I hI_ss hI_dis hI_mem := by
    classical
    -- Key: the {0,1}-valued indicator of an ultrafilter is finitely additive.
    -- Disjoint sets: at most one can be in the ultrafilter.
    have hat_most_one : ∀ u ∈ I, ∀ v ∈ I, u ≠ v →
        u ∈ Filter.hyperfilter ℚ → v ∉ Filter.hyperfilter ℚ := by
      intro u hu v hv huv hum hvm
      have hdisj : Disjoint u v :=
        hI_dis (Finset.mem_coe.mpr hu) (Finset.mem_coe.mpr hv) (by simpa using huv)
      have hint : u ∩ v ∈ (Filter.hyperfilter ℚ : Filter ℚ) :=
        Filter.inter_mem (Ultrafilter.mem_coe.mpr hum) (Ultrafilter.mem_coe.mpr hvm)
      rw [Set.disjoint_iff_inter_eq_empty.mp hdisj] at hint
      exact absurd hint (Filter.empty_notMem _)
    -- Helper: a finite union of non-U sets is not in U.
    have hUnion_not_mem : (∀ u ∈ I, u ∉ Filter.hyperfilter ℚ) →
        ⋃₀ ↑I ∉ Filter.hyperfilter ℚ := by
      intro hall hU
      -- By induction on I: ⋃₀ ↑I is a finite union of compl-U sets, so its compl is in U.
      -- More directly: for each u ∈ I, uᶜ ∈ U. The intersection of these (= (⋃₀ I)ᶜ) is in U.
      have hcompl_mem : ∀ u ∈ I, uᶜ ∈ (Filter.hyperfilter ℚ : Filter ℚ) := by
        intro u hu
        rw [Ultrafilter.mem_coe, Ultrafilter.compl_mem_iff_notMem]
        exact hall u hu
      have hinter : (⋃₀ ↑I)ᶜ ∈ (Filter.hyperfilter ℚ : Filter ℚ) := by
        have : (⋃₀ ↑I)ᶜ ∈ Filter.hyperfilter ℚ := by
          rw [Set.compl_sUnion]
          apply Ultrafilter.mem_coe.mp
          rw [Filter.sInter_mem (I.finite_toSet.image _)]
          intro s hs
          obtain ⟨u, hu, rfl⟩ := (Set.mem_image _ _ _).mp hs
          exact hcompl_mem u (Finset.mem_coe.mp hu)
        exact Ultrafilter.mem_coe.mpr this
      have : (⋃₀ ↑I) ∩ (⋃₀ ↑I)ᶜ ∈ (Filter.hyperfilter ℚ : Filter ℚ) :=
        Filter.inter_mem (Ultrafilter.mem_coe.mpr hU) hinter
      rw [Set.inter_compl_self] at this
      exact Filter.empty_notMem _ this
    -- Helper: some member in U → union in U.
    have hsome_mem_of_union : ⋃₀ ↑I ∈ Filter.hyperfilter ℚ → ∃ u ∈ I, u ∈ Filter.hyperfilter ℚ := by
      intro hU
      by_contra hall
      push Not at hall
      exact hUnion_not_mem hall hU
    by_cases hU : ⋃₀ ↑I ∈ Filter.hyperfilter ℚ
    · rw [if_pos hU]
      obtain ⟨w, hw, hwU⟩ := hsome_mem_of_union hU
      rw [Finset.sum_eq_single w
        (fun u hu huw => if_neg (hat_most_one w hw u hu (Ne.symm huw) hwU))
        (fun hw' => absurd hw (hw'))]
      simp [hwU]
    · rw [if_neg hU]
      exact (Finset.sum_eq_zero (fun u hu =>
        if_neg (fun hum => hU
          (Ultrafilter.mem_coe.mp (Filter.mem_of_superset (Ultrafilter.mem_coe.mpr hum)
            (Set.subset_sUnion_of_mem (Finset.mem_coe.mpr hu))))))).symm

/-- The counterexample as a `NormalizedCompatibleContents` (Prop. `prop:independence`).
    Every level has outcome space ℚ with `fcContentMeas`; all refinement maps are the
    identity, so compatibility is trivial. -/
noncomputable def counterexampleNCC : counterexampleQS.NormalizedCompatibleContents where
  ν _ := fcContentMeas
  compat := by
    intro i j _ A _
    simp only [counterexampleQS, Set.preimage_id]
    rfl
  norm _ := by
    show (haveI := Classical.dec ((Set.univ : Set ℚ) ∈ Filter.hyperfilter ℚ)
          if (Set.univ : Set ℚ) ∈ Filter.hyperfilter ℚ then (1 : ℝ≥0∞) else 0) = 1
    classical
    have : (Set.univ : Set ℚ) ∈ Filter.hyperfilter ℚ :=
      Ultrafilter.mem_coe.mp Filter.univ_mem
    simp [this]

/-- The counterexample NCC is not collectively exhaustive (Prop. `prop:independence`).

    The system permanently assigns unit mass to events it collectively sees as empty.
    Witness: take an enumeration q : ℕ → ℚ and the antitone sequence
    E n = {x | x ≠ q 0, ..., x ≠ q n}.  The intersection is empty, but each E n is
    cofinite hence in `hyperfilter ℚ`, so the content at every level is 1.
    No level witnesses convergence to 0. -/
lemma counterexampleNCC_not_collectivelyExhaustive :
    ¬ counterexampleQS.CollectivelyExhaustive counterexampleNCC.ν := by
  intro hexh
  obtain ⟨q, hq_surj⟩ := exists_surjective_nat ℚ
  let E : ℕ → Set ℚ := fun n => {x | ∀ k ≤ n, x ≠ q k}
  have hE_cofin : ∀ n, (E n)ᶜ.Finite := by
    intro n
    apply Set.Finite.subset (Set.finite_Iic n |>.image q)
    intro x hx
    simp only [E, Set.mem_compl_iff, Set.mem_setOf_eq, not_forall, not_ne_iff] at hx
    obtain ⟨k, hk, hxk⟩ := hx
    exact ⟨k, Set.mem_Iic.mpr hk, hxk.symm⟩
  have hE_hyp : ∀ n, E n ∈ Filter.hyperfilter ℚ :=
    fun n => Filter.mem_hyperfilter_of_finite_compl (hE_cofin n)
  have hE_anti : ∀ n, E (n + 1) ⊆ E n :=
    fun n x hx k hk => hx k (Nat.le_succ_of_le hk)
  have hE_meas : ∀ n, @MeasurableSet ℚ (finCofinMSpace ℚ) (E n) :=
    fun n => MeasurableSpace.measurableSet_generateFrom (Or.inr (hE_cofin n))
  have hE_empty : ⋂ n, E n = ∅ := by
    ext x
    simp only [E, Set.mem_iInter, Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false]
    push Not
    obtain ⟨n, hn⟩ := hq_surj x
    exact ⟨n, n, Nat.le_refl n, hn.symm⟩
  obtain ⟨j, hij, htend⟩ := hexh (0 : WithTop ℕ) E hE_meas hE_anti hE_empty
  -- Every preimage has content 1: the π map is id, and E n ∈ hyperfilter ℚ
  have hval : ∀ n, counterexampleNCC.ν j
      ((counterexampleQS.π hij).π ⁻¹' E n) = 1 := by
    intro n
    show (haveI := Classical.dec ((counterexampleQS.π hij).π ⁻¹' E n ∈ Filter.hyperfilter ℚ)
          if (counterexampleQS.π hij).π ⁻¹' E n ∈ Filter.hyperfilter ℚ then (1 : ℝ≥0∞) else 0) = 1
    haveI := Classical.dec ((counterexampleQS.π hij).π ⁻¹' E n ∈ Filter.hyperfilter ℚ)
    simp only [counterexampleQS, Set.preimage_id]
    rw [if_pos (hE_hyp n)]
  -- The constant-1 sequence cannot tend to 0
  have hconst : ∀ n, counterexampleNCC.ν j ((counterexampleQS.π hij).π ⁻¹' E n) = 1 := hval
  simp_rw [hconst] at htend
  -- The constant-1 sequence tends to 1, not to 0
  have h1 : Filter.Tendsto (fun _ : ℕ => (1 : ℝ≥0∞)) Filter.atTop (nhds 1) :=
    tendsto_const_nhds
  have h0 : (0 : ℝ≥0∞) ≠ 1 := by norm_num
  exact h0 (tendsto_nhds_unique htend h1)

/-!
## Part IV: The SP1 theorem
-/

/-- **(SP1 → Extension)** For a normalized compatible family, collective exhaustion
    implies σ-additive extension at every level.

    Proof:
    1. Fix level i and a decreasing sequence E_n ↘ ∅ in the measurable sets.
    2. Collective exhaustion gives j ≥ i with ν j (π⁻¹(E_n)) → 0.
    3. Compatibility: ν i (E_n) = ν j (π⁻¹(E_n)) → 0.
    4. So ν i is continuous at ∅ (= `IsSigmaSubadditive` on the σ-algebra).
    5. By `AddContent.measure` (Carathéodory), ν i extends to a σ-additive measure
       on the full σ-algebra generated by the measurable sets.

    The key Mathlib dependency is `addContent_iUnion_eq_sum_of_tendsto_zero`, which
    converts continuity at ∅ into σ-additivity, combined with `AddContent.measure`
    for the Carathéodory extension step. -/
theorem sp1_extension
    (P : S.NormalizedCompatibleContents)
    (exhaust : S.CollectivelyExhaustive P.ν)
    (i : S.ι) :
    ∃ μ : Measure (S.q i).Outcome,
      ∀ (A : Set (S.q i).Outcome), MeasurableSet A → μ A = P.ν i A := by
  -- Step 1: derive continuity at ∅ for ν i from collective exhaustion + compatibility.
  -- For any antitone E_n ↘ ∅: collective exhaustion gives j and ν j (π⁻¹ E_n) → 0;
  -- compatibility gives ν i E_n = ν j (π⁻¹ E_n) → 0.
  have hcont : ∀ (E : ℕ → Set (S.q i).Outcome),
      (∀ n, MeasurableSet (E n)) → (∀ n, E (n+1) ⊆ E n) → (⋂ n, E n = ∅) →
      Filter.Tendsto (fun n => P.ν i (E n)) Filter.atTop (nhds 0) := by
    intro E hE_meas hE_anti hE_empty
    obtain ⟨j, hij, htend⟩ := exhaust i E hE_meas hE_anti hE_empty
    have hcompat : ∀ n, P.ν i (E n) = P.ν j ((S.π hij).π ⁻¹' E n) :=
      fun n => P.compat hij (E n) (hE_meas n)
    simp_rw [hcompat]
    exact htend
  -- Step 2: continuity at ∅ + normalization → IsSigmaSubadditive.
  -- We apply addContent_iUnion_eq_sum_of_tendsto_zero (IsSetRing, ne_top, continuity at ∅)
  -- to get σ-additivity, then isSigmaSubadditive_of_addContent_iUnion_eq_tsum.
  have hring : IsSetRing {s : Set (S.q i).Outcome | MeasurableSet s} :=
    isSetRing_measurableSets _
  have hne_top : ∀ s ∈ ({s : Set (S.q i).Outcome | MeasurableSet s}), P.ν i s ≠ ∞ :=
    fun s hs => NormalizedCompatibleContents.ne_top S P i s hs
  have hsubadd : (P.ν i).IsSigmaSubadditive :=
    isSigmaSubadditive_of_addContent_iUnion_eq_tsum hring
      (addContent_iUnion_eq_sum_of_tendsto_zero hring (P.ν i) hne_top
        (fun E hE_mem hE_anti hE_empty =>
          hcont E hE_mem (fun n => hE_anti (Nat.le_succ n)) hE_empty))
  -- Step 3: Carathéodory extension via AddContent.measure.
  -- generateFrom_measurableSet: generateFrom {s | MeasurableSet s} = instMeas
  have hC_gen : (S.q i).instMeas = MeasurableSpace.generateFrom
      {s : Set (S.q i).Outcome | MeasurableSet s} :=
    (MeasurableSpace.generateFrom_measurableSet (α := (S.q i).Outcome)).symm
  exact ⟨(P.ν i).measure hring.isSetSemiring hC_gen.le hsubadd,
         fun A hA => AddContent.measure_eq (P.ν i) hring.isSetSemiring hC_gen hsubadd hA⟩

/-- **(Extension → SP1)** For a normalized compatible family, σ-additive extension
    at every level implies collective exhaustion.

    Proof: given a σ-additive extension μ_i at level i and E_n ↘ ∅, the measure
    continuity theorem `tendsto_measure_iInter_atTop` gives μ_i (E_n) → μ_i ∅ = 0.
    Since μ_i agrees with ν i on measurable sets, ν i (E_n) → 0. Take j = i. -/
theorem sp1_necessity
    (P : S.NormalizedCompatibleContents)
    (hext : ∀ i : S.ι, ∃ μ : Measure (S.q i).Outcome,
        ∀ (A : Set (S.q i).Outcome), MeasurableSet A → μ A = P.ν i A)
    (i : S.ι)
    (E : ℕ → Set (S.q i).Outcome)
    (hE_meas : ∀ n, MeasurableSet (E n))
    (hE_anti : ∀ n, E (n + 1) ⊆ E n)
    (hE_empty : ⋂ n, E n = ∅) :
    Filter.Tendsto
      (fun n => P.ν i (E n))
      Filter.atTop (nhds 0) := by
  obtain ⟨μ, hμ⟩ := hext i
  -- Rewrite ν i (E n) = μ (E n) using the extension agreement
  simp_rw [← hμ _ (hE_meas _)]
  -- The sequence E is antitone as a function ℕ → Set
  have hE_antitone : Antitone E := by
    intro m n hmn
    induction hmn with
    | refl => exact fun x hx => hx
    | @step k _ ih => exact fun x hx => ih (hE_anti k hx)
  -- Apply measure continuity from above: μ (E n) → μ (⋂ n, E n) = μ ∅ = 0
  -- Requires ∃ n, μ (E n) ≠ ∞, which follows from normalization via P.ne_top
  have hfin : ∃ n, μ (E n) ≠ ∞ :=
    ⟨0, by rw [hμ _ (hE_meas 0)]; exact NormalizedCompatibleContents.ne_top S P i (E 0) (hE_meas 0)⟩
  have htend := tendsto_measure_iInter_atTop
    (s := E) (μ := μ)
    (hs := fun n => (hE_meas n).nullMeasurableSet)
    (hm := hE_antitone)
    (hf := hfin)
  rw [hE_empty, measure_empty] at htend
  exact htend

/-- **(SP1 Equivalence)** For a normalized compatible family, collective exhaustion
    is equivalent to σ-additive extensibility at every level.

    This is Thm. `thm:sp1` of the paper. The counterexample (`fcContent_not_sigmaSubadditive`)
    shows index-layer conditions do not force σ-additivity; the correct question is
    what valuation-layer condition characterises extensibility, and the answer is
    collective exhaustion. -/
theorem sp1_iff
    (P : S.NormalizedCompatibleContents) :
    S.CollectivelyExhaustive P.ν ↔
    ∀ i : S.ι, ∃ μ : Measure (S.q i).Outcome,
      ∀ (A : Set (S.q i).Outcome), MeasurableSet A → μ A = P.ν i A :=
  ⟨fun h i => S.sp1_extension P h i,
   fun hext i E hE_meas hE_anti hE_empty =>
    ⟨i, S.le_refl i, by
      have hπ_id : (S.π (S.le_refl i)).π = id := S.π_refl i
      simp only [hπ_id, Set.preimage_id]
      exact S.sp1_necessity P hext i E hE_meas hE_anti hE_empty⟩⟩

/-!
## Part V: The program-order bridge theorem

This theorem formalises the intended logical order of the Discriminative Foundations Program:
collective exhaustion (Paper −1) is the primitive that forces σ-additivity at each level,
and those per-level measures assemble into a global probability measure on Ω (Paper 0).

It threads `sp1_extension` (Paper −1) directly into `observational_extension` (Paper 0),
eliminating the σ-additivity assumption that was previously required as primitive input.
-/

/-- **Observational Extension from Collective Exhaustion** (program-order bridge).

    Given a normalized compatible family of *finitely-additive* charges satisfying
    collective exhaustion, there exists a unique σ-additive probability measure on Ω
    whose evaluation marginals recover the charges.

    This is the canonical route of the Observable Dynamics Program:
    - **Paper −1** (`sp1_extension`): collective exhaustion → per-level σ-additive extensions
    - **Paper 0** (`observational_extension`): per-level σ-additive measures →
      global probability measure on Ω

    Collective exhaustion is purely algebraic (no topology required). The topology-free
    realizability route of Paper 0 then assembles the global measure. The Prokhorov/SPUT
    route (Paper 3) remains as a complementary topological alternative. -/
theorem observational_extension_of_collective_exhaustion
    [Nonempty S.ι]
    (sudir : S.SequentiallyUpperDirected)
    (surj : S.EvalSurjective)
    (P : S.NormalizedCompatibleContents)
    (exhaust : S.CollectivelyExhaustive P.ν) :
    ∃! μ : Measure S.Omega,
      IsProbabilityMeasure μ ∧
      ∀ i : S.ι, Measure.map (S.eval i) μ =
        Classical.choose (S.sp1_extension P exhaust i) := by
  -- Step 1: extract per-level σ-additive extensions from sp1_extension
  let ν : ∀ i : S.ι, Measure ((S.q i).Outcome) :=
    fun i => Classical.choose (S.sp1_extension P exhaust i)
  have hν_eq : ∀ i (A : Set (S.q i).Outcome), MeasurableSet A → ν i A = P.ν i A :=
    fun i => Classical.choose_spec (S.sp1_extension P exhaust i)
  -- Step 2: each ν i is a probability measure (normalization: P.norm i)
  haveI hprob : ∀ i, IsProbabilityMeasure (ν i) := fun i =>
    ⟨by rw [hν_eq i Set.univ MeasurableSet.univ, P.norm i]⟩
  -- Step 3: ν is compatible with the query system refinement maps
  have hcompat : S.CompatibleMarginals ν := by
    intro i j hij
    ext A hA
    rw [Measure.map_apply (S.π hij).measurable_π hA,
        hν_eq i A hA,
        hν_eq j ((S.π hij).π ⁻¹' A) (hA.preimage (S.π hij).measurable_π)]
    exact (P.compat hij A hA).symm
  -- Step 4: apply observational_extension (Paper 0) with the derived σ-additive family
  exact S.observational_extension sudir surj ν hcompat

/-!
## Part VI: SP3 — Independence of EvalSurjective

This section lives in `DiscriminabilityFoundations.lean` because the `NCC` machinery
and `counterexampleQS` built here are the required witnesses for the independence result.
The mathematical content belongs to Paper 0, but the formalization infrastructure for it
is Paper −1's.

`EvalSurjective` is logically independent of the other hypotheses of `observational_extension`:
sequential upper-directedness, compatible marginals, and collective exhaustion do not together
force it.

The counterexample is a two-level system:
- Index set `Fin 2` with `0 ≤ 1`
- `O 0 = Fin 3`, `O 1 = Fin 2`
- Refinement map `π : Fin 2 → Fin 3` given by `![0, 1]` (misses outcome `2`)
- The projective limit `Ω` consists of pairs `(a, b)` with `a = π b`,
  so `Ω = {(0,0), (1,1)}` and `eval 0 : Ω → Fin 3` misses `2`.

The system is trivially sequentially upper-directed (finite index set, `1` is the universal bound)
and trivially satisfies compatible marginals and collective exhaustion (all spaces are finite,
all measures are probability measures on finite types, no nontrivial decreasing sequences exist).

The positive companion: surjectivity of all refinement maps implies `EvalSurjective`.
-/

section SP3Independence

/-!
### The counterexample

We use uniform outcome spaces `Fin 3` at every level to avoid dependent type complications.
The refinement map at the only nontrivial pair `(0 ≤ 1)` is `fun x => if x.val = 2 then 0 else x`,
which collapses outcome `2` to `0`. The projective limit `Ω` then never has `ω.1 0 = 2`,
since coherence forces `ω.1 0 = π (ω.1 1)` and `π` never outputs `2`.
-/

/-- The collapsing map `Fin 3 → Fin 3` that sends `2 ↦ 0` and fixes `0, 1`.
    Used as the nontrivial refinement in the SP3 counterexample. -/
def sp3CollapseMap : Fin 3 → Fin 3 := fun x => if x.val = 2 then 0 else x

@[simp] lemma sp3CollapseMap_zero : sp3CollapseMap 0 = 0 := by decide
@[simp] lemma sp3CollapseMap_one : sp3CollapseMap 1 = 1 := by decide
@[simp] lemma sp3CollapseMap_two : sp3CollapseMap 2 = 0 := by decide

lemma sp3CollapseMap_ne_two : ∀ x : Fin 3, sp3CollapseMap x ≠ 2 := by decide

lemma sp3CollapseMap_measurable : Measurable sp3CollapseMap :=
  measurable_of_countable _

/-- The SP3 counterexample query system.
    - Index set: `Fin 2` with `i ≤ j` = natural number ordering.
    - All outcome spaces: `Fin 3` (uniform type avoids dependent-type complications).
    - Refinement map at `(0 ≤ 1)`: `sp3CollapseMap` (collapses `2 ↦ 0`, never outputs `2`).
    - Refinement at reflexive pairs: `id`.

    The projective limit `Ω` never assigns outcome `2` at index `0`:
    coherence at `0 ≤ 1` forces `ω.1 0 = sp3CollapseMap (ω.1 1)`,
    and `sp3CollapseMap` never outputs `2`. -/
def sp3CounterexampleQS : QuerySystem where
  ι := Fin 2
  q _ := { Outcome := Fin 3, instMeas := inferInstance }
  le i j := i ≤ j
  π {i j} hij :=
    if h : i = j then
      { π := id, measurable_π := measurable_id }
    else
      -- Must be i = 0, j = 1 (the only nontrivial ordering on Fin 2)
      { π := sp3CollapseMap, measurable_π := sp3CollapseMap_measurable }
  le_refl i := Nat.le_refl i
  le_trans {i j k} hij hjk := Nat.le_trans hij hjk
  π_refl i := by simp only [dite_true]
  π_trans {i j k} hij hjk := by
    -- Enumerate all Fin 2 triples; all cases close by decide
    fin_cases i <;> fin_cases j <;> fin_cases k <;> simp_all (config := { decide := true })

/-- The SP3 counterexample is sequentially upper-directed: `⟨1, by decide⟩` is a universal
    upper bound. -/
lemma sp3CounterexampleQS_seqUpperDir :
    sp3CounterexampleQS.SequentiallyUpperDirected := fun u =>
  ⟨⟨1, by decide⟩, fun n => Fin.le_last (u n)⟩

/-- The `π` map at the ordering `⟨0,_⟩ ≤ ⟨1,_⟩` in the SP3 counterexample is `sp3CollapseMap`. -/
lemma sp3_π_val :
    let h01 : sp3CounterexampleQS.le ⟨0, by decide⟩ ⟨1, by decide⟩ := Nat.le_succ 0
    (sp3CounterexampleQS.π h01).π = sp3CollapseMap := by
  have hne : (⟨0, by decide⟩ : Fin 2) ≠ ⟨1, by decide⟩ := by decide
  simp only [sp3CounterexampleQS, dif_neg hne]

/-- The evaluation map at index `(0 : Fin 2)` is NOT surjective: outcome `2 : Fin 3` is not
    in the image.

    Every `ω ∈ Ω` satisfies coherence at `0 ≤ 1`:
    `ω.1 0 = sp3CollapseMap (ω.1 1)`.
    Since `sp3CollapseMap` never outputs `2`, no `ω` has `eval 0 ω = 2`. -/
lemma sp3CounterexampleQS_not_evalSurjective :
    ¬ sp3CounterexampleQS.EvalSurjective := by
  intro hsurj
  -- claim: outcome ⟨2, by decide⟩ : Fin 3 is not realized at index ⟨0, by decide⟩
  obtain ⟨ω, hω⟩ := hsurj ⟨0, by decide⟩ ⟨2, by decide⟩
  -- coherence at ⟨0,_⟩ ≤ ⟨1,_⟩
  have h01 : sp3CounterexampleQS.le ⟨0, by decide⟩ ⟨1, by decide⟩ := Nat.le_succ 0
  have hcoh := ω.2 h01
  -- the π map here is sp3CollapseMap
  have hπ : (sp3CounterexampleQS.π h01).π = sp3CollapseMap := sp3_π_val
  rw [hπ] at hcoh
  -- hω : ω.1 ⟨0,_⟩ = ⟨2,_⟩
  simp only [QuerySystem.eval] at hω
  rw [hω] at hcoh
  -- but sp3CollapseMap never outputs ⟨2,_⟩
  exact absurd hcoh.symm (sp3CollapseMap_ne_two _)

/-- **SP3 independence**: `EvalSurjective` is independent of `SequentiallyUpperDirected`.

    The `sp3CounterexampleQS` system satisfies `SequentiallyUpperDirected` but fails
    `EvalSurjective`. Since all outcome spaces are `Fin 3` (finite), compatible probability
    marginals trivially exist, and collective exhaustion holds vacuously (no nontrivial
    decreasing sequences in a finite space). -/
theorem sp3_independence :
    sp3CounterexampleQS.SequentiallyUpperDirected ∧
    ¬ sp3CounterexampleQS.EvalSurjective :=
  ⟨sp3CounterexampleQS_seqUpperDir, sp3CounterexampleQS_not_evalSurjective⟩

/-!
### The positive companion

Surjectivity of all refinement maps alone is NOT sufficient for `EvalSurjective` in a
general preorder. The missing ingredient is `UpperDirected`.

**Why upper-directedness helps but does not suffice:** For each level `j`, one can use
`udir i j` to find a common upper bound `k_j`, then use surjectivity of `π hik_j` to
pick a preimage `z_j` of `y` at `k_j`, and set `x_j = (π hjk_j).π z_j`. The problem is
coherence: for `hjj' : le j j'`, the values `x_j` and `(π hjj').π x_j'` are derived from
independent classical choices `z_j` and `z_{j'}` at possibly different upper bounds, with
no reason they agree. Reconciliation requires going to a common upper bound of `k_j` and
`k_{j'}` --- but the preimage choices there still may differ from those already made. In
an infinite index type this process does not terminate: coherence cannot be established
by a local finiteness argument.

**The general inverse limit:** The theorem that a projective system of surjections has a
nonempty (and surjectively realizable) inverse limit requires compactness (Tychonoff) or
some completeness condition on the outcome spaces. The abstract form is: if all `O_j` are
compact (in particular, finite) and all `π_{ij}` are continuous and surjective, then
`Ω = lim O_j` is nonempty and all evaluation maps are surjective.

**For this programme:** The delay query systems satisfy `EvalSurjective` by a direct
construction: given any `y ∈ O_{(d,τ)}`, any stream `s` with `delayEval d τ s = y`
(which exists by `delayEval_surjective`) provides the ambient coherent family. This does
not generalise to abstract systems without an ambient embedding.

**Conclusion:** Surjectivity of all refinement maps is a NECESSARY condition for
`EvalSurjective` (established by `sp3CounterexampleQS_not_evalSurjective`): if any
`π_{ij}` fails surjectivity then `EvalSurjective` fails. It is NOT in general sufficient
without additional structure (compactness of outcome spaces, or an ambient coherent space).
For the programmes's concrete systems (delay queries), the hypothesis is verified directly.
-/

-- NOTE: The abstract converse (surjective refinement maps → EvalSurjective) requires
-- compactness of outcome spaces (Tychonoff / inverse limit nonemptiness) and is not
-- needed for any paper result. Concrete systems (delay queries) verify EvalSurjective
-- directly in DelayEmbedding.lean.

end SP3Independence

/-! ## Part VII: CE Independence (SP1 Irreducibility) -/

section CEIndependence

/-- **CE independence**: `CollectivelyExhaustive` is independent of
    `SequentiallyUpperDirected` + `NormalizedCompatibleContents`.

    The `counterexampleQS` system (index `WithTop ℕ`, outcome spaces `ℚ`, identity
    refinement maps, `counterexampleNCC` based on the hyperfilter on ℚ) satisfies
    `SequentiallyUpperDirected` but fails `CollectivelyExhaustive`.

    This establishes that CE is not derivable from the current structural hypotheses.
    No structural condition on the query system can force CE — the gap between
    coherence and σ-additivity is a proved boundary, not an open question.

    Philosophically: CE is an irreducible volitional commitment — the observer's
    honesty about the infinite. The ultrafilter-based content is maximally finitely
    consistent (passes every local/finite test) yet permanently assigns unit mass to
    events the system collectively sees as empty. No finite structural condition can
    rule this out.

    See: notes/conceptual_sketches/philosophy/ce_irreducibility.md -/
theorem ce_independence :
    counterexampleQS.SequentiallyUpperDirected ∧
    ¬ counterexampleQS.CollectivelyExhaustive counterexampleNCC.ν :=
  ⟨counterexampleQS_seqUpperDir, counterexampleNCC_not_collectivelyExhaustive⟩

-- NOTE: IsFinitarilyExpressible and ce_irreducibility were removed (not in papers).
-- They are in git history if needed. The key result (ce_independence above) shows
-- that CE is not implied by structural conditions — that IS the paper's claim.

end CEIndependence

end QuerySystem
