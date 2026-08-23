/-
# RETRODICTION COPY -- proofs blanked, generated from AndersenJessen.lean

Goal: a decreasing sequence of THICK subsets of `[0,1]` (full outer measure)
with empty intersection. Feeding it through `QuerySystem.EscapingTower` refutes
observational extension under plain `UpperDirected`.

Staging file: NOT under the lake globs, so `sorry`s here do not touch CI.
Lemmas land in the library only once closed.

Route (Border, *Kolmogorov Extension Problem*, §6–8, after Halmos pp. 68–70):
  A = ℤ + αℤ, α irrational        -- countable dense subgroup
  Bₖ = {n+mα ∈ A : |n| ≥ k, n even}   -- dense, decreasing, ⋂ₖ Bₖ = ∅
  V  = transversal of ℝ ⧸ A       -- Quotient.out'
  Mₖ = V + Bₖ                     -- λ*(E ∩ Mₖ) = λ(E), by Steinhaus
  Xₖ = Mₖ ∩ [0,1]                 -- thick, and Xₖ ↓ ∅
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.RingTheory.Int.Basic
import Mathlib.NumberTheory.Real.Irrational
import Mathlib.Topology.Algebra.Order.Archimedean
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar
import Mathlib.GroupTheory.QuotientGroup.Basic

open Pointwise

namespace AndersenJessen

variable (α : ℝ)

/-- `A = ℤ + αℤ`, a countable dense subgroup of `ℝ` when `α` is irrational. -/
def A : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α}

/-- `Bₖ`: the elements of `A` whose integer coordinate is even with `|n| ≥ k`.
Decreasing in `k`, with empty intersection -- this is what eventually forces
`Xₖ ↓ ∅`. -/
def B (k : ℕ) : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α ∧ (k : ℤ) ≤ |n| ∧ Even n}

/-! ### Step 1: the representation is unique (distinctness) -/

/-- If `α` is irrational, `n + mα` determines `n` and `m`. Everything about
`Bₖ ↓ ∅` rests on this: it is what gives each element of `A` a well-defined
integer coordinate. -/
theorem repr_unique (hα : Irrational α) {n m n' m' : ℤ}
    (h : (n : ℝ) + m * α = (n' : ℝ) + m' * α) : n = n' ∧ m = m' := by
  sorry

theorem repr_unique_left (hα : Irrational α) {n m n' m' : ℤ}
    (h : (n : ℝ) + m * α = (n' : ℝ) + m' * α) : n = n' :=
  (repr_unique α hα h).1

/-! ### Step 2: `Bₖ` is decreasing with empty intersection -/

theorem B_subset_A {k : ℕ} : B α k ⊆ A α := by
  unfold B A ; aesop (add simp [abs])

theorem B_antitone : Antitone (B α) := by
  intro s t h ; rw [B, B] ; rintro x ⟨n, m, x_def, ht, hn⟩ ; exact ⟨n, m, x_def, by linarith, hn⟩

theorem B_iInter_eq_empty (hα : Irrational α) : (⋂ k : ℕ, B α k) = ∅ := by
  sorry

theorem B_neg_mem {k : ℕ} {x : ℝ} (hx : x ∈ B α k) : -x ∈ B α k := by
  cases hx ; rcases ‹_› with ⟨m, rfl, _, h2⟩ ; simp only [B, Set.mem_Ioc, neg_add, neg_neg] ; refine ⟨-_, -m, ?_, ?_, h2.neg⟩ <;> simp_all

theorem B_even_smul_mem {k : ℕ} {x : ℝ} (j : ℤ) (hj : Even j) (hj0 : j ≠ 0)
    (hx : x ∈ B α k) : (j : ℝ) * x ∈ B α k := by
  sorry

theorem A_mem_sub {x y : ℝ} (hx : x ∈ A α) (hy : y ∈ A α) : x - y ∈ A α := by
  simp [A, hx, hy] ; obtain ⟨n, hn⟩ := hx ; obtain ⟨m, hm⟩ := hn ; rcases hy with ⟨n', m', hm'⟩ ; refine' ⟨n - n', m - m', _⟩ <;> simp [hm, hm', sub_eq_add_neg] <;> ring

theorem B_sub_mem_A {k : ℕ} {x y : ℝ} (hx : x ∈ B α k) (hy : y ∈ B α k) :
    x - y ∈ A α :=
  A_mem_sub α (B_subset_A α hx) (B_subset_A α hy)

/-! ### Step 4: parity separation

The contradiction that closes Proposition 13: a difference of two `Bₖ`
elements has even integer coordinate, so it cannot lie in the odd part. -/

/-- The odd half of `A`. -/
def C (k : ℕ) : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α ∧ (k : ℤ) ≤ |n| ∧ ¬ Even n}

theorem B_disjoint_C (hα : Irrational α) : Disjoint (B α 0) (C α 0) := by
  sorry

/-- `2ℤ + αℤ`, as an additive subgroup of `ℝ`. -/
def Aeven : AddSubgroup ℝ where
  carrier := {x | ∃ n m : ℤ, x = 2 * (n : ℝ) + m * α}
  zero_mem' := ⟨0, 0, by norm_num⟩
  add_mem' := by
    rintro _ _ ⟨n, m, rfl⟩ ⟨n', m', rfl⟩
    exact ⟨n + n', m + m', by push_cast; ring⟩
  neg_mem' := by
    rintro _ ⟨n, m, rfl⟩
    exact ⟨-n, -m, by push_cast; ring⟩

theorem Aeven_dense (hα : Irrational α) : Dense (Aeven α : Set ℝ) := by
  sorry

theorem C_zero_eq : C α 0 = (fun y => 1 + y) '' (Aeven α : Set ℝ) := by
  apply Set.ext ; simp [C, Aeven, Set.mem_image, Set.mem_setOf, add_comm, add_left_comm] ; intro t ; aesop (add simp [Odd]) ; exacts [⟨w, w_1, by ring⟩, ⟨w, w_1, by linarith⟩]

theorem C_zero_dense (hα : Irrational α) : Dense (C α 0) := by
  sorry

/-- `A = ℤ + αℤ`, as an additive subgroup. -/
def Afull : AddSubgroup ℝ where
  carrier := A α
  zero_mem' := ⟨0, 0, by norm_num⟩
  add_mem' := by
    rintro _ _ ⟨n, m, rfl⟩ ⟨n', m', rfl⟩
    exact ⟨n + n', m + m', by push_cast; ring⟩
  neg_mem' := by
    rintro _ ⟨n, m, rfl⟩
    exact ⟨-n, -m, by push_cast; ring⟩

lemma mem_Afull {x : ℝ} : x ∈ Afull α ↔ ∃ n m : ℤ, x = (n : ℝ) + m * α := Iff.rfl

/-- A transversal of `ℝ ⧸ A`. -/
noncomputable def V : Set ℝ := Set.range (fun q : ℝ ⧸ Afull α => q.out)

/-- The only property of the transversal that Proposition 13 uses. -/
theorem V_unique {v v' : ℝ} (hv : v ∈ V α) (hv' : v' ∈ V α)
    (h : v - v' ∈ Afull α) : v = v' := by
  sorry

/-- `Mₖ = V + Bₖ`. -/
def M (k : ℕ) : Set ℝ := {x | ∃ v ∈ V α, ∃ b ∈ B α k, x = v + b}

lemma B_sub_mem_B_zero {k : ℕ} {b b' : ℝ} (hb : b ∈ B α k) (hb' : b' ∈ B α k) :
    b - b' ∈ B α 0 := by
  sorry

/-- Every real is a transversal representative plus an element of `A`. -/
theorem V_covers (x : ℝ) : ∃ v ∈ V α, x - v ∈ Afull α := by
  sorry

/-- **Proposition 13, core (general form).** If `S ⊆ A` has all its differences
even, then `V + S` contains no measurable set of positive measure.

The parity hypothesis is the whole content. Steinhaus makes `F - F` a
neighbourhood of `0`; `C₀` is dense so meets it; the transversal forces any
element of `A` in `(V+S) - (V+S)` to be a difference of two `S` elements, hence
even by hypothesis -- contradicting the oddness of the witness.

Both `V + Bₖ` and `V + C₀` satisfy the hypothesis: even minus even is even, and
odd minus odd is even. -/
theorem V_add_measurable_subset_null (hα : Irrational α) (S : Set ℝ)
    (hSdiff : ∀ a ∈ S, ∀ b ∈ S, a - b ∈ B α 0)
    {F : Set ℝ} (hF : MeasurableSet F)
    (hFS : F ⊆ {x | ∃ v ∈ V α, ∃ s ∈ S, x = v + s}) :
    MeasureTheory.volume F = 0 := by
  sorry

/-- `V + Bₖ` contains no measurable set of positive measure. -/
theorem M_measurable_subset_null (hα : Irrational α) (k : ℕ)
    {F : Set ℝ} (hF : MeasurableSet F) (hFM : F ⊆ M α k) :
    MeasureTheory.volume F = 0 :=
  V_add_measurable_subset_null α hα (B α k)
    (fun a ha b hb => B_sub_mem_B_zero α ha hb) hF hFM

/-- Odd minus odd is even. -/
theorem C_sub_mem_B_zero {c c' : ℝ} (hc : c ∈ C α 0) (hc' : c' ∈ C α 0) :
    c - c' ∈ B α 0 := by
  sorry

/-- `V + C₀` likewise contains no measurable set of positive measure. -/
theorem VC_measurable_subset_null (hα : Irrational α)
    {F : Set ℝ} (hF : MeasurableSet F)
    (hFM : F ⊆ {x | ∃ v ∈ V α, ∃ c ∈ C α 0, x = v + c}) :
    MeasureTheory.volume F = 0 :=
  V_add_measurable_subset_null α hα (C α 0)
    (fun a ha b hb => C_sub_mem_B_zero α ha hb) hF hFM

/-! ### Step 7: `M₀` is thick

At `k = 0` the transversal decomposition splits `ℝ` exactly: every real is
`v + a` with `a ∈ A`, and `a` is even or odd, so `M₀ᶜ = V + C₀`. Both halves
satisfy the parity hypothesis of `V_add_measurable_subset_null`, so neither
contains a positive-measure measurable set -- which is thickness for each. -/

theorem C_subset_A {k : ℕ} : C α k ⊆ A α := by
  intro x hx ; dsimp [C, A] at hx ; unfold A ; aesop

theorem M_zero_compl (hα : Irrational α) :
    (M α 0)ᶜ = {x | ∃ v ∈ V α, ∃ c ∈ C α 0, x = v + c} := by
  sorry

/-- **`M₀` is thick**: every measurable set disjoint from it is null. This is
what makes the trace measure of Proposition 14 well defined. -/
theorem M_zero_thick (hα : Irrational α) {E : Set ℝ} (hE : MeasurableSet E)
    (hdisj : E ∩ M α 0 = ∅) : MeasureTheory.volume E = 0 := by
  sorry

theorem Afull_dense (hα : Irrational α) : Dense (Afull α : Set ℝ) := by
  sorry

/-- **The replacement for Proposition 13.** For finite `F ⊆ A`, the set `V + F`
contains no measurable set of positive measure.

`F - F` is finite and `A` is dense, so some element of `A` sits in any
neighbourhood of `0` while avoiding `F - F`; the transversal then forces it to
lie in `F - F` after all. -/
theorem V_add_finite_measurable_null (hα : Irrational α) (F : Set ℝ)
    (hFfin : F.Finite) (hFA : F ⊆ (Afull α : Set ℝ))
    {G : Set ℝ} (hG : MeasurableSet G)
    (hGV : G ⊆ {x | ∃ v ∈ V α, ∃ a ∈ F, x = v + a}) :
    MeasureTheory.volume G = 0 := by
  sorry

/-- `V + S` and `V + (A ∖ S)` partition `ℝ`, for any `S ⊆ A`. -/
theorem V_add_compl {S : Set ℝ} (hSA : S ⊆ (Afull α : Set ℝ)) :
    {x | ∃ v ∈ V α, ∃ a ∈ S, x = v + a}ᶜ
      = {x | ∃ v ∈ V α, ∃ a ∈ (Afull α : Set ℝ) \ S, x = v + a} := by
  sorry

theorem Afull_countable : (Afull α : Set ℝ).Countable := by
  sorry

theorem exists_enumA : ∃ e : ℕ → ℝ, (Afull α : Set ℝ) = Set.range e :=
  (Afull_countable α).exists_eq_range ⟨0, (Afull α).zero_mem⟩

/-- An enumeration of `A`. -/
noncomputable def enumA : ℕ → ℝ := (exists_enumA α).choose

theorem enumA_range : (Afull α : Set ℝ) = Set.range (enumA α) := (exists_enumA α).choose_spec

/-- `A` minus its first `k` enumerated elements. -/
def tail (k : ℕ) : Set ℝ := (Afull α : Set ℝ) \ (enumA α '' Set.Iio k)

theorem tail_antitone : Antitone (tail α) := by
  intro a b hab ; dsimp [tail] ; intro x hx ; simp only [Set.mem_diff, Set.mem_image, Set.mem_Iio] at hx ⊢ ; exact ⟨hx.1, fun ⟨c, hc, h⟩ ↦ hx.2 ⟨c, (lt_of_lt_of_le hc hab), h⟩⟩

theorem tail_iInter : (⋂ k, tail α k) = ∅ := by
  sorry

/-- **The thick tower.** `Xₖ = V + (A minus its first k elements)`. -/
def X (k : ℕ) : Set ℝ := {x | ∃ v ∈ V α, ∃ a ∈ tail α k, x = v + a}

theorem X_antitone : Antitone (X α) := by
  sorry

theorem X_iInter : (⋂ k, X α k) = ∅ := by
  sorry

/-- **Every `Xₖ` is thick** -- the complement is `V +` a FINITE subset of `A`.
This is what parity could not deliver past `k = 0`. -/
theorem X_thick (hα : Irrational α) (k : ℕ) {E : Set ℝ} (hE : MeasurableSet E)
    (hdisj : E ∩ X α k = ∅) : MeasureTheory.volume E = 0 := by
  sorry
