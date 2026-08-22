/-
# Andersen–Jessen, stage two: the thick tower

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

end AndersenJessen
