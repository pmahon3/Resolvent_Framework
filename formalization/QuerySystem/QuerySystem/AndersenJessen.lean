/-
# Andersen–Jessen, stage two: the thick tower

Goal: a decreasing sequence of THICK subsets of `[0,1]` (full outer measure)
with empty intersection. Feeding it through `QuerySystem.EscapingTower` refutes
observational extension under plain `UpperDirected`.

Graduated from `staging/` into the library 2026-08-22: sorry-free, so it now
carries the ratchet and appears in the blueprint like everything else.

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
  -- If m ≠ m' then α = (n' - n)/(m - m') is rational, contradicting hα.
  have hm : m = m' := by
    by_contra hne
    have hd : ((m - m' : ℤ) : ℝ) ≠ 0 := by
      exact_mod_cast sub_ne_zero.mpr hne
    have hsub : ((m - m' : ℤ) : ℝ) * α = ((n' - n : ℤ) : ℝ) := by
      push_cast
      linarith
    have hq : α = ((n' - n : ℤ) : ℝ) / ((m - m' : ℤ) : ℝ) := by
      rw [eq_div_iff hd, mul_comm]
      exact hsub
    exact Irrational.ne_rational hα (n' - n) (m - m') hq
  refine ⟨?_, hm⟩
  subst hm
  have hn : (n : ℝ) = (n' : ℝ) := by linarith
  exact_mod_cast hn

theorem repr_unique_left (hα : Irrational α) {n m n' m' : ℤ}
    (h : (n : ℝ) + m * α = (n' : ℝ) + m' * α) : n = n' :=
  (repr_unique α hα h).1

/-! ### Step 2: `Bₖ` is decreasing with empty intersection -/

theorem B_subset_A {k : ℕ} : B α k ⊆ A α := by
  rintro x ⟨n, m, rfl, -, -⟩
  exact ⟨n, m, rfl⟩

theorem B_antitone : Antitone (B α) := by
  intro k l hkl x hx
  obtain ⟨n, m, rfl, hn, he⟩ := hx
  exact ⟨n, m, rfl, le_trans (by exact_mod_cast hkl) hn, he⟩

theorem B_iInter_eq_empty (hα : Irrational α) : (⋂ k : ℕ, B α k) = ∅ := by
  ext x
  simp only [Set.mem_iInter, Set.mem_empty_iff_false, iff_false]
  intro h
  obtain ⟨n, m, hx, -, -⟩ := h 0
  obtain ⟨n', m', hx', hn', -⟩ := h (n.natAbs + 1)
  have hnn : n = n' := (repr_unique α hα (hx.symm.trans hx')).1
  subst hnn
  rw [Int.abs_eq_natAbs] at hn'
  omega

/-! ### Step 3: closure properties used for density

`Bₖ` is closed under negation and under multiplication by NONZERO even
integers; these are what let the standard equidistribution argument conclude
density from a single small element.

Note the nonzero hypothesis on `j`: without it `j * x = 0`, whose integer
coordinate is `0`, and `k ≤ |0|` fails for `k > 0`. The first draft of this
file omitted it and was false. -/

theorem B_neg_mem {k : ℕ} {x : ℝ} (hx : x ∈ B α k) : -x ∈ B α k := by
  obtain ⟨n, m, rfl, hn, he⟩ := hx
  refine ⟨-n, -m, by push_cast; ring, ?_, he.neg⟩
  rwa [abs_neg]

theorem B_even_smul_mem {k : ℕ} {x : ℝ} (j : ℤ) (hj : Even j) (hj0 : j ≠ 0)
    (hx : x ∈ B α k) : (j : ℝ) * x ∈ B α k := by
  obtain ⟨n, m, rfl, hn, he⟩ := hx
  refine ⟨j * n, j * m, by push_cast; ring, ?_, hj.mul_right n⟩
  calc (k : ℤ) ≤ |n| := hn
    _ ≤ |j| * |n| := le_mul_of_one_le_left (abs_nonneg n) (Int.one_le_abs hj0)
    _ = |j * n| := (abs_mul j n).symm

theorem A_mem_sub {x y : ℝ} (hx : x ∈ A α) (hy : y ∈ A α) : x - y ∈ A α := by
  obtain ⟨n, m, rfl⟩ := hx
  obtain ⟨n', m', rfl⟩ := hy
  exact ⟨n - n', m - m', by push_cast; ring⟩

theorem B_sub_mem_A {k : ℕ} {x y : ℝ} (hx : x ∈ B α k) (hy : y ∈ B α k) :
    x - y ∈ A α :=
  A_mem_sub α (B_subset_A α hx) (B_subset_A α hy)

/-! ### Step 4: parity separation

The contradiction that closes Proposition 13: a difference of two `Bₖ`
elements has even integer coordinate, so it cannot lie in the odd part. -/

/-- The odd half of `A`. -/
def C (k : ℕ) : Set ℝ := {x | ∃ n m : ℤ, x = (n : ℝ) + m * α ∧ (k : ℤ) ≤ |n| ∧ ¬ Even n}

theorem B_disjoint_C (hα : Irrational α) : Disjoint (B α 0) (C α 0) := by
  rw [Set.disjoint_left]
  rintro x ⟨n, m, hx, -, he⟩ ⟨n', m', hx', -, he'⟩
  exact he' ((repr_unique α hα (hx.symm.trans hx')).1 ▸ he)

/-! ### Step 5: density

Proposition 13 needs a dense set of ODD elements meeting any neighbourhood of
`0`. The source proves `Bₖ` and `Cₖ` dense for every `k` by an equidistribution
argument. That is more than the proof uses: the contradiction it reaches is
`B₀ ∩ C₀ = ∅`, a parity fact, so density is only ever needed at `k = 0`.

And `C₀` is a coset of a subgroup. `Aeven = 2ℤ + αℤ` is an additive subgroup of
`ℝ`, dense because it is not cyclic (a generator would make `α` rational), and
`C₀ = 1 + Aeven`. So the whole equidistribution argument collapses into
`AddSubgroup.dense_or_cyclic` plus a translation. -/

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
  rcases AddSubgroup.dense_or_cyclic (Aeven α) with h | ⟨a, ha⟩
  · exact h
  exfalso
  have h2 : (2 : ℝ) ∈ Aeven α := ⟨1, 0, by norm_num⟩
  have hA : α ∈ Aeven α := ⟨0, 1, by norm_num⟩
  rw [ha, AddSubgroup.mem_closure_singleton] at h2 hA
  obtain ⟨p, hp⟩ := h2
  obtain ⟨q, hq⟩ := hA
  rw [zsmul_eq_mul] at hp hq
  have hp0 : (p : ℝ) ≠ 0 := by
    intro h0
    rw [h0, zero_mul] at hp
    norm_num at hp
  have : α = ((2 * q : ℤ) : ℝ) / ((p : ℤ) : ℝ) := by
    rw [eq_div_iff (by exact_mod_cast hp0)]
    push_cast
    calc α * (p : ℝ) = ((q : ℝ) * a) * p := by rw [hq]
      _ = (q : ℝ) * ((p : ℝ) * a) := by ring
      _ = (q : ℝ) * 2 := by rw [hp]
      _ = 2 * q := by ring
  exact Irrational.ne_rational hα (2 * q) p this

theorem C_zero_eq : C α 0 = (fun y => 1 + y) '' (Aeven α : Set ℝ) := by
  ext x
  constructor
  · rintro ⟨n, m, rfl, -, hodd⟩
    obtain ⟨j, hj⟩ := Int.not_even_iff_odd.mp hodd
    exact ⟨2 * (j : ℝ) + m * α, ⟨j, m, rfl⟩, by rw [hj]; push_cast; ring⟩
  · rintro ⟨y, ⟨n, m, rfl⟩, rfl⟩
    refine ⟨2 * n + 1, m, by push_cast; ring, by positivity, ?_⟩
    simp [Int.odd_iff]

theorem C_zero_dense (hα : Irrational α) : Dense (C α 0) := by
  rw [C_zero_eq, dense_iff_closure_eq]
  have hcont : Continuous (fun y : ℝ => 1 + y) := continuous_const.add continuous_id
  have h := hcont.range_subset_closure_image_dense (Aeven_dense α hα)
  refine Set.eq_univ_of_univ_subset fun x _ => h ⟨x - 1, by ring⟩

/-! ### Step 6: the transversal and Proposition 13

`V` picks one representative from each coset of `A = ℤ + αℤ` in `ℝ`, via
`Quotient.out'`. The only property used is that two representatives congruent
mod `A` are equal.

`Mₖ = V + Bₖ`. Proposition 13's core is that `Mₖ` contains no measurable set of
positive measure: if it did, Steinhaus would put a neighbourhood of `0` inside
`Mₖ - Mₖ`, `C₀` is dense so meets it, and any element of `A` in `Mₖ - Mₖ` forces
the two representatives to coincide and is therefore EVEN -- contradicting the
oddness of the `C₀` witness. -/

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
  obtain ⟨q, rfl⟩ := hv
  obtain ⟨q', rfl⟩ := hv'
  have hq : (QuotientAddGroup.mk (s := Afull α) q.out)
      = QuotientAddGroup.mk q'.out := by
    rw [QuotientAddGroup.eq]
    simpa [neg_add_eq_sub, neg_sub] using (Afull α).neg_mem h
  have : q = q' := by
    rw [← Quotient.out_eq q, ← Quotient.out_eq q']
    exact hq
  rw [this]

/-- `Mₖ = V + Bₖ`. -/
def M (k : ℕ) : Set ℝ := {x | ∃ v ∈ V α, ∃ b ∈ B α k, x = v + b}

lemma B_sub_mem_B_zero {k : ℕ} {b b' : ℝ} (hb : b ∈ B α k) (hb' : b' ∈ B α k) :
    b - b' ∈ B α 0 := by
  obtain ⟨n, m, rfl, -, he⟩ := hb
  obtain ⟨n', m', rfl, -, he'⟩ := hb'
  exact ⟨n - n', m - m', by push_cast; ring, by simp, he.sub he'⟩

/-- Every real is a transversal representative plus an element of `A`. -/
theorem V_covers (x : ℝ) : ∃ v ∈ V α, x - v ∈ Afull α := by
  refine ⟨(QuotientAddGroup.mk (s := Afull α) x).out, ⟨_, rfl⟩, ?_⟩
  have h : (QuotientAddGroup.mk (s := Afull α))
      ((QuotientAddGroup.mk (s := Afull α) x).out) = QuotientAddGroup.mk x :=
    Quotient.out_eq _
  rw [QuotientAddGroup.eq] at h
  simpa [neg_add_eq_sub] using h

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
  by_contra hpos
  have hp : 0 < MeasureTheory.volume F := pos_iff_ne_zero.mpr hpos
  have hnhds : F - F ∈ nhds (0 : ℝ) :=
    MeasureTheory.Measure.sub_mem_nhds_zero_of_addHaar_pos MeasureTheory.volume F hF hp
  obtain ⟨U, hUsub, hUopen, hU0⟩ := mem_nhds_iff.mp hnhds
  obtain ⟨x, hxC, hxU⟩ := (C_zero_dense α hα).exists_mem_open hUopen ⟨0, hU0⟩
  obtain ⟨f, hf, f', hf', rfl⟩ : ∃ f ∈ F, ∃ f' ∈ F, x = f - f' := by
    obtain ⟨f, hf, f', hf', hx⟩ := hUsub hxU
    exact ⟨f, hf, f', hf', hx.symm⟩
  obtain ⟨v, hv, b, hb, rfl⟩ := hFS hf
  obtain ⟨v', hv', b', hb', rfl⟩ := hFS hf'
  obtain ⟨n, m, hxn, -, hodd⟩ := hxC
  have hxA : (v + b) - (v' + b') ∈ Afull α := ⟨n, m, hxn⟩
  have hbb : b - b' ∈ Afull α := by
    obtain ⟨p, q, hpq, -, -⟩ := hSdiff b hb b' hb'
    exact ⟨p, q, hpq⟩
  have hvv : v - v' ∈ Afull α := by
    have hrw : v - v' = ((v + b) - (v' + b')) - (b - b') := by ring
    rw [hrw]
    exact (Afull α).sub_mem hxA hbb
  have hveq : v = v' := V_unique α hv hv' hvv
  subst hveq
  have hxB : (v + b) - (v + b') ∈ B α 0 := by
    have hrw : (v + b) - (v + b') = b - b' := by ring
    rw [hrw]
    exact hSdiff b hb b' hb'
  exact (Set.disjoint_left.mp (B_disjoint_C α hα)) hxB ⟨n, m, hxn, by simp, hodd⟩

/-- `V + Bₖ` contains no measurable set of positive measure. -/
theorem M_measurable_subset_null (hα : Irrational α) (k : ℕ)
    {F : Set ℝ} (hF : MeasurableSet F) (hFM : F ⊆ M α k) :
    MeasureTheory.volume F = 0 :=
  V_add_measurable_subset_null α hα (B α k)
    (fun a ha b hb => B_sub_mem_B_zero α ha hb) hF hFM

/-- Odd minus odd is even. -/
theorem C_sub_mem_B_zero {c c' : ℝ} (hc : c ∈ C α 0) (hc' : c' ∈ C α 0) :
    c - c' ∈ B α 0 := by
  obtain ⟨n, m, rfl, -, ho⟩ := hc
  obtain ⟨n', m', rfl, -, ho'⟩ := hc'
  refine ⟨n - n', m - m', by push_cast; ring, by simp, ?_⟩
  rw [Int.not_even_iff_odd] at ho ho'
  exact ho.sub_odd ho'

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
  rintro x ⟨n, m, rfl, -, -⟩
  exact ⟨n, m, rfl⟩

theorem M_zero_compl (hα : Irrational α) :
    (M α 0)ᶜ = {x | ∃ v ∈ V α, ∃ c ∈ C α 0, x = v + c} := by
  ext x
  simp only [Set.mem_compl_iff, Set.mem_setOf_eq, M]
  constructor
  · intro hx
    obtain ⟨v, hv, n, m, hnm⟩ := V_covers α x
    by_cases he : Even n
    · exact absurd ⟨v, hv, x - v, ⟨n, m, hnm, by simp, he⟩, by ring⟩ hx
    · exact ⟨v, hv, x - v, ⟨n, m, hnm, by simp, he⟩, by ring⟩
  · rintro ⟨v, hv, c, hc, rfl⟩ ⟨v', hv', b, hb, heq⟩
    have hcA : c ∈ Afull α := C_subset_A α hc
    have hbA : b ∈ Afull α := B_subset_A α hb
    have hvv : v - v' ∈ Afull α := by
      have hrw : v - v' = b - c := by linarith [heq]
      rw [hrw]
      exact (Afull α).sub_mem hbA hcA
    have hveq : v = v' := V_unique α hv hv' hvv
    subst hveq
    have : c = b := by linarith [heq]
    subst this
    exact (Set.disjoint_left.mp (B_disjoint_C α hα)) hb hc

/-- **`M₀` is thick**: every measurable set disjoint from it is null. This is
what makes the trace measure of Proposition 14 well defined. -/
theorem M_zero_thick (hα : Irrational α) {E : Set ℝ} (hE : MeasurableSet E)
    (hdisj : E ∩ M α 0 = ∅) : MeasureTheory.volume E = 0 := by
  refine VC_measurable_subset_null α hα hE ?_
  rw [← M_zero_compl α hα]
  intro y hy hyM
  have hmem : y ∈ E ∩ M α 0 := ⟨hy, hyM⟩
  rw [hdisj] at hmem
  exact hmem

/-! ### Step 8: finiteness beats parity

The parity argument caps out at `k = 0`: a set with all-even differences lies in
a coset of `Aeven`, and `A / Aeven` has only two classes, so it can never split
`A` into more than two pieces. For `k > 0` the complement `A ∖ Bₖ` contains all
odd elements, and odd − odd already exhausts the evens, so no dense witness is
disjoint from its difference set.

Replace parity by FINITENESS. If `F ⊆ A` is finite then `F - F` is finite, while
`A` is dense; so a witness in `A` avoiding `F - F` always exists. That gives
thickness at every level, and it needs no `Bₖ`, no `Cₖ`, and no coset density. -/

theorem Afull_dense (hα : Irrational α) : Dense (Afull α : Set ℝ) := by
  refine (Aeven_dense α hα).mono ?_
  rintro x ⟨n, m, rfl⟩
  exact ⟨2 * n, m, by push_cast; ring⟩

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
  by_contra hpos
  have hp : 0 < MeasureTheory.volume G := pos_iff_ne_zero.mpr hpos
  have hnhds : G - G ∈ nhds (0 : ℝ) :=
    MeasureTheory.Measure.sub_mem_nhds_zero_of_addHaar_pos MeasureTheory.volume G hG hp
  obtain ⟨U, hUsub, hUopen, hU0⟩ := mem_nhds_iff.mp hnhds
  -- `U ∖ (F - F)` is open and nonempty: `U` contains an interval, which is
  -- infinite, and `F - F` is finite.
  have hdiff_fin : (F - F).Finite := hFfin.sub hFfin
  have hUopen' : IsOpen (U \ (F - F)) := hUopen.sdiff hdiff_fin.isClosed
  have hUne : (U \ (F - F)).Nonempty := by
    obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp hUopen 0 hU0
    have hsub : Set.Ioo (-ε) ε ⊆ U := fun y hy => hball (by
      simp only [Metric.mem_ball, Real.dist_eq, sub_zero, abs_lt]
      exact ⟨hy.1, hy.2⟩)
    have hinf : (Set.Ioo (-ε) ε).Infinite := Set.Ioo_infinite (by linarith)
    obtain ⟨y, hy, hyF⟩ := (hinf.diff hdiff_fin).nonempty
    exact ⟨y, hsub hy, hyF⟩
  -- a witness in A avoiding F - F
  obtain ⟨x, hxA, hxU⟩ := (Afull_dense α hα).exists_mem_open hUopen' hUne
  obtain ⟨g, hg, g', hg', rfl⟩ : ∃ g ∈ G, ∃ g' ∈ G, x = g - g' := by
    obtain ⟨g, hg, g', hg', hx⟩ := hUsub hxU.1
    exact ⟨g, hg, g', hg', hx.symm⟩
  obtain ⟨v, hv, a, ha, rfl⟩ := hGV hg
  obtain ⟨v', hv', a', ha', rfl⟩ := hGV hg'
  have hvv : v - v' ∈ Afull α := by
    have hrw : v - v' = ((v + a) - (v' + a')) - (a - a') := by ring
    rw [hrw]
    exact (Afull α).sub_mem hxA ((Afull α).sub_mem (hFA ha) (hFA ha'))
  have hveq : v = v' := V_unique α hv hv' hvv
  subst hveq
  refine hxU.2 ?_
  have hrw : (v + a) - (v + a') = a - a' := by ring
  rw [hrw]
  exact ⟨a, ha, a', ha', rfl⟩

/-! ### Step 9: the thick tower -/

/-- `V + S` and `V + (A ∖ S)` partition `ℝ`, for any `S ⊆ A`. -/
theorem V_add_compl {S : Set ℝ} (hSA : S ⊆ (Afull α : Set ℝ)) :
    {x | ∃ v ∈ V α, ∃ a ∈ S, x = v + a}ᶜ
      = {x | ∃ v ∈ V α, ∃ a ∈ (Afull α : Set ℝ) \ S, x = v + a} := by
  ext x
  simp only [Set.mem_compl_iff, Set.mem_setOf_eq]
  constructor
  · intro hx
    obtain ⟨v, hv, ha⟩ := V_covers α x
    exact ⟨v, hv, x - v, ⟨ha, fun hmem => hx ⟨v, hv, x - v, hmem, by ring⟩⟩, by ring⟩
  · rintro ⟨v, hv, a, ⟨haA, haS⟩, rfl⟩ ⟨v', hv', a', ha', heq⟩
    have hvv : v - v' ∈ Afull α := by
      have hrw : v - v' = a' - a := by linarith [heq]
      rw [hrw]
      exact (Afull α).sub_mem (hSA ha') haA
    have hveq : v = v' := V_unique α hv hv' hvv
    subst hveq
    have : a = a' := by linarith [heq]
    subst this
    exact haS ha'

theorem Afull_countable : (Afull α : Set ℝ).Countable := by
  have him : (Afull α : Set ℝ) = (fun p : ℤ × ℤ => (p.1 : ℝ) + p.2 * α) '' Set.univ := by
    ext x
    constructor
    · rintro ⟨n, m, rfl⟩; exact ⟨(n, m), trivial, rfl⟩
    · rintro ⟨⟨n, m⟩, -, rfl⟩; exact ⟨n, m, rfl⟩
  rw [him]
  exact Set.countable_univ.image _

theorem exists_enumA : ∃ e : ℕ → ℝ, (Afull α : Set ℝ) = Set.range e :=
  (Afull_countable α).exists_eq_range ⟨0, (Afull α).zero_mem⟩

/-- An enumeration of `A`. -/
noncomputable def enumA : ℕ → ℝ := (exists_enumA α).choose

theorem enumA_range : (Afull α : Set ℝ) = Set.range (enumA α) := (exists_enumA α).choose_spec

/-- `A` minus its first `k` enumerated elements. -/
def tail (k : ℕ) : Set ℝ := (Afull α : Set ℝ) \ (enumA α '' Set.Iio k)

theorem tail_antitone : Antitone (tail α) := by
  intro j k hjk x hx
  exact ⟨hx.1, fun hmem => hx.2 (by
    obtain ⟨i, hi, rfl⟩ := hmem
    exact ⟨i, lt_of_lt_of_le hi hjk, rfl⟩)⟩

theorem tail_iInter : (⋂ k, tail α k) = ∅ := by
  ext x
  simp only [Set.mem_iInter, Set.mem_empty_iff_false, iff_false]
  intro h
  obtain ⟨hxA, -⟩ := h 0
  rw [enumA_range α] at hxA
  obtain ⟨j, rfl⟩ := hxA
  exact (h (j + 1)).2 ⟨j, Nat.lt_succ_self j, rfl⟩

/-- **The thick tower.** `Xₖ = V + (A minus its first k elements)`. -/
def X (k : ℕ) : Set ℝ := {x | ∃ v ∈ V α, ∃ a ∈ tail α k, x = v + a}

theorem X_antitone : Antitone (X α) := by
  intro j k hjk x hx
  obtain ⟨v, hv, a, ha, rfl⟩ := hx
  exact ⟨v, hv, a, tail_antitone α hjk ha, rfl⟩

theorem X_iInter : (⋂ k, X α k) = ∅ := by
  ext x
  simp only [Set.mem_iInter, Set.mem_empty_iff_false, iff_false]
  intro h
  obtain ⟨v, hv, hxv⟩ := V_covers α x
  have hall : ∀ k, x - v ∈ tail α k := by
    intro k
    obtain ⟨v', hv', a, ha, heq⟩ := h k
    have hvv : v - v' ∈ Afull α := by
      have hrw : v - v' = a - (x - v) + (x - v) - a + (v - v') := by ring
      have h2 : v' - v ∈ Afull α := by
        have : v' - v = (x - v) - a := by linarith [heq]
        rw [this]
        exact (Afull α).sub_mem hxv ha.1
      simpa using (Afull α).neg_mem h2
    have hveq : v = v' := V_unique α hv hv' hvv
    subst hveq
    have : a = x - v := by linarith [heq]
    rwa [← this]
  have : x - v ∈ ⋂ k, tail α k := Set.mem_iInter.mpr hall
  rw [tail_iInter α] at this
  exact this

/-- **Every `Xₖ` is thick** -- the complement is `V +` a FINITE subset of `A`.
This is what parity could not deliver past `k = 0`. -/
theorem X_thick (hα : Irrational α) (k : ℕ) {E : Set ℝ} (hE : MeasurableSet E)
    (hdisj : E ∩ X α k = ∅) : MeasureTheory.volume E = 0 := by
  have hsub : E ⊆ (X α k)ᶜ := by
    intro y hy hyX
    have hmem : y ∈ E ∩ X α k := ⟨hy, hyX⟩
    rw [hdisj] at hmem
    exact hmem
  have hcompl : ({x | ∃ v ∈ V α, ∃ a ∈ tail α k, x = v + a} : Set ℝ)ᶜ
      = {x | ∃ v ∈ V α, ∃ a ∈ (Afull α : Set ℝ) \ tail α k, x = v + a} :=
    V_add_compl α (fun z hz => hz.1)
  rw [show X α k = {x | ∃ v ∈ V α, ∃ a ∈ tail α k, x = v + a} from rfl, hcompl] at hsub
  have hfin : ((Afull α : Set ℝ) \ tail α k).Finite := by
    refine ((Set.finite_Iio k).image (enumA α)).subset ?_
    rintro z ⟨hzA, hzt⟩
    by_contra hz
    exact hzt ⟨hzA, hz⟩
  exact V_add_finite_measurable_null α hα _ hfin (fun z hz => hz.1) hE hsub

end AndersenJessen
