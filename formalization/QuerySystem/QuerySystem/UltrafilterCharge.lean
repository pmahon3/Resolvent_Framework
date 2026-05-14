/-
Copyright (c) 2025 Patrick S. Mahon. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Order.Filter.Ultrafilter.Basic
import Mathlib.MeasureTheory.Measure.Dirac
import Mathlib.Topology.Instances.ENNReal.Lemmas

/-!
# The ultrafilter charge on P(ℕ)

This file formalizes the measure-theoretic core of the companion note
"Countable Additivity is Not First-Order Axiomatizable":

* `ultrafilterCharge U A` is `1` if `A ∈ U`, else `0`.
* It is finitely additive (`ultrafilterCharge_union_of_disjoint`).
* When `U` is nonprincipal, it is **not** σ-additive
  (`ultrafilterCharge_not_sigma_additive`): the sets `Set.Ici k` decrease
  to `∅` yet all have charge `1`.
* It equals the pointwise ultralimit of Dirac evaluations
  (`ultrafilterCharge_eq_one_iff_dirac`).

Together these show that the class of σ-additive probability structures is
not closed under ultraproducts (hence not first-order axiomatizable, by
Łoś's theorem — the model-theoretic wrapper is standard and not formalized here).
-/

noncomputable section

open scoped ENNReal
open MeasureTheory Set Filter

attribute [local instance] Classical.propDecidable

/-- The `{0,1}`-valued charge on `Set ℕ` induced by an ultrafilter `U`:
    `ultrafilterCharge U A = 1` iff `A ∈ U`. -/
def ultrafilterCharge (U : Ultrafilter ℕ) (A : Set ℕ) : ℝ≥0∞ :=
  if A ∈ U then 1 else 0

@[simp]
theorem ultrafilterCharge_mem {U : Ultrafilter ℕ} {A : Set ℕ} (h : A ∈ U) :
    ultrafilterCharge U A = 1 :=
  show (if A ∈ U then 1 else 0) = 1 from if_pos h

@[simp]
theorem ultrafilterCharge_notMem {U : Ultrafilter ℕ} {A : Set ℕ} (h : A ∉ U) :
    ultrafilterCharge U A = 0 :=
  show (if A ∈ U then 1 else 0) = 0 from if_neg h

theorem ultrafilterCharge_empty (U : Ultrafilter ℕ) :
    ultrafilterCharge U ∅ = 0 :=
  ultrafilterCharge_notMem (fun h => U.neBot.ne (empty_mem_iff_bot.mp h))

theorem ultrafilterCharge_univ (U : Ultrafilter ℕ) :
    ultrafilterCharge U Set.univ = 1 :=
  ultrafilterCharge_mem univ_mem

-- Helper to avoid repeating the ∅ ∈ U → False pattern
private theorem empty_not_mem_ultrafilter (U : Ultrafilter ℕ) : ∅ ∉ U :=
  fun h => U.neBot.ne (empty_mem_iff_bot.mp h)

/-- The ultrafilter charge is finitely additive on disjoint sets. -/
theorem ultrafilterCharge_union_of_disjoint (U : Ultrafilter ℕ) {A B : Set ℕ}
    (hd : Disjoint A B) :
    ultrafilterCharge U (A ∪ B) = ultrafilterCharge U A + ultrafilterCharge U B := by
  rcases U.mem_or_compl_mem A with hA | hAc
  · -- A ∈ U, so B ∉ U (since A ∩ B = ∅ and U is a filter)
    have hB : B ∉ U := fun hB =>
      empty_not_mem_ultrafilter U (hd.inter_eq ▸ Filter.inter_mem hA hB)
    have hAB : A ∪ B ∈ U := Filter.mem_of_superset hA Set.subset_union_left
    rw [ultrafilterCharge_mem hAB, ultrafilterCharge_mem hA, ultrafilterCharge_notMem hB]
    norm_num
  · -- Aᶜ ∈ U, so A ∉ U
    have hA : A ∉ U := U.compl_mem_iff_notMem.mp hAc
    rcases U.mem_or_compl_mem B with hB | hBc
    · have hAB : A ∪ B ∈ U := Filter.mem_of_superset hB Set.subset_union_right
      rw [ultrafilterCharge_mem hAB, ultrafilterCharge_notMem hA, ultrafilterCharge_mem hB]
      norm_num
    · have hB : B ∉ U := U.compl_mem_iff_notMem.mp hBc
      have hAB : A ∪ B ∉ U := by
        intro h
        have hc : (A ∪ B)ᶜ ∈ U.toFilter := Set.compl_union A B ▸ Filter.inter_mem hAc hBc
        exact empty_not_mem_ultrafilter U (Set.inter_compl_self (A ∪ B) ▸ Filter.inter_mem h hc)
      rw [ultrafilterCharge_notMem hAB, ultrafilterCharge_notMem hA, ultrafilterCharge_notMem hB]
      norm_num

-- ---------- Non-σ-additivity for nonprincipal ultrafilters ----------

/-- Key lemma: `Set.Ici k` is cofinite in `ℕ`, hence belongs to the hyperfilter. -/
theorem Ici_mem_hyperfilter (k : ℕ) : Set.Ici k ∈ hyperfilter ℕ := by
  apply mem_hyperfilter_of_finite_compl
  simp only [Set.compl_Ici]
  exact (finite_lt_nat k).subset (fun n hn => hn)

/-- Singletons are not in a nonprincipal ultrafilter. -/
theorem singleton_notMem_hyperfilter (n : ℕ) : {n} ∉ hyperfilter ℕ :=
  notMem_hyperfilter_of_finite (Set.finite_singleton n)

/-- The intersection `⋂ k, Set.Ici k` is empty in `ℕ`. -/
theorem iInter_Ici_eq_empty : (⋂ k : ℕ, Set.Ici k) = (∅ : Set ℕ) := by
  ext n
  simp only [Set.mem_iInter, Set.mem_Ici, Set.mem_empty_iff_false, iff_false, not_forall, not_le]
  exact ⟨n + 1, by omega⟩

/-- The ultrafilter charge of the hyperfilter is not σ-additive:
    `Set.Ici k` decreases to `∅`, yet `ultrafilterCharge (hyperfilter ℕ) (Set.Ici k) = 1`
    for all `k`. -/
theorem ultrafilterCharge_not_sigma_additive :
    ¬ (∀ (f : ℕ → Set ℕ), (∀ k, f k ⊇ f (k + 1)) → (⋂ k, f k) = ∅ →
      Filter.Tendsto (fun k => ultrafilterCharge (hyperfilter ℕ) (f k)) Filter.atTop
        (nhds 0)) := by
  intro h
  -- Instantiate with f k = Set.Ici k
  have hdec : ∀ k, Set.Ici k ⊇ Set.Ici (k + 1) :=
    fun k => Set.Ici_subset_Ici.mpr (Nat.le_succ k)
  have htend := h (fun k => Set.Ici k) hdec iInter_Ici_eq_empty
  -- But ultrafilterCharge (hyperfilter ℕ) (Set.Ici k) = 1 for all k
  have hconst : (fun k => ultrafilterCharge (hyperfilter ℕ) (Set.Ici k)) = fun _ => 1 := by
    ext k; exact ultrafilterCharge_mem (Ici_mem_hyperfilter k)
  rw [hconst] at htend
  -- Constant sequence 1 cannot tend to 0 in ℝ≥0∞ (which is T1)
  exact one_ne_zero (tendsto_const_nhds_iff.mp htend)

-- ---------- Connection to Dirac evaluations ----------

/-- Key identity: `{n | δ_n(A) = 1} = A` in `ℕ`. -/
theorem setOf_dirac_eq_one (A : Set ℕ) : {n : ℕ | Measure.dirac n A = 1} = A := by
  ext n
  simp only [Set.mem_setOf_eq, Measure.dirac_apply n A, Set.indicator, Pi.one_apply]
  constructor
  · intro h; by_contra hn; simp [hn] at h
  · intro h; simp [h]

/-- The ultrafilter charge equals the pointwise ultralimit of Dirac evaluations.
    More precisely: `ultrafilterCharge U A = 1 ↔ {n | δ_n(A) = 1} ∈ U`. -/
theorem ultrafilterCharge_eq_one_iff_dirac (U : Ultrafilter ℕ) (A : Set ℕ) :
    ultrafilterCharge U A = 1 ↔ {n : ℕ | Measure.dirac n A = 1} ∈ U := by
  rw [setOf_dirac_eq_one]
  exact ⟨fun h => by by_contra hA; simp [hA] at h,
         fun hA => ultrafilterCharge_mem hA⟩

end
