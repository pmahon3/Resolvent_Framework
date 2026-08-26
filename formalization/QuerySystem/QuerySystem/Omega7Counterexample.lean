/-
# Ω₇ — the seven-point Boolean counterexample (Remark 1.5), machine-checked

`Ω₇ := {±}³ \ {all-plus}`. The three coordinate events `A₁, A₂, A₃` have all
twelve pairwise intersections among `{Aᵢ, Aᵢᶜ}` (`i ≠ j`) nonempty, but
`A₁ ∩ A₂ ∩ A₃ = ∅`. The pattern `s₀ ≡ 1` on the three events (encoded as the
majority vote of three marked points, one in each pairwise intersection) is a
legitimate LOCAL state on the ⊥-closure `B` — only complement pairs constrain
it — with EMPTY kernel; and, the carrier `P(Ω₇)` being a finite Boolean algebra
whose two-valued states are all Dirac, it has NO σ-additive global two-valued
extension.

Drop the coherence clause from `IsSigmaEssential` and this would make a
**Boolean** carrier a "witness", contradicting Prop 2.1. The clause excludes it:
`s₀` is NOT finitely coherent.

Four public theorems:
* `omega7_kernel_empty` — clause (i) holds: `K(s₀) = ∅`.
* `omega7_no_sigma_extension` — no σ-additive two-valued state extends `s₀`.
* `omega7_not_coherent` — the coherence clause does its job: `s₀` fails it.
* `omega7_not_witness` — sanity, from the Boolean baseline.
-/
import QuerySystem.SigmaEssentialWitness
import QuerySystem.UlamWitnessCore
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.FinCases

open Set Function MeasurableSpace

namespace SigmaEssential.Omega7

open SigmaEssential

/-- The seven-point space: `Bool³` minus the all-`true` point. -/
def Ω₇ : Type := {v : Fin 3 → Bool // v ≠ fun _ => true}

instance : DecidableEq Ω₇ :=
  inferInstanceAs (DecidableEq {v : Fin 3 → Bool // v ≠ fun _ => true})

instance : Countable Ω₇ :=
  inferInstanceAs (Countable {v : Fin 3 → Bool // v ≠ fun _ => true})

/-- The full powerset as a Dynkin system (a Boolean σ-algebra). -/
def powerDynkin : DynkinSystem Ω₇ where
  Has := fun _ => True
  has_empty := trivial
  has_compl := fun _ => trivial
  has_iUnion_nat := fun _ _ => trivial

/-- The powerset carrier is intersection-closed (Boolean). -/
theorem powerDynkin_interClosed : InterClosed powerDynkin := fun _ _ => trivial

/-- Coordinate events: `A i = {v | vᵢ = +}`. -/
def A (i : Fin 3) : Set Ω₇ := {v | v.1 i = true}

/-- The block: the ⊥-closure of the three coordinate events. -/
noncomputable def blk : Block powerDynkin where
  sets := {A 0, A 1, A 2, (A 0)ᶜ, (A 1)ᶜ, (A 2)ᶜ}
  mem_has := fun _ _ => trivial
  compl_closed := by
    classical
    intro S hS
    simp only [Finset.mem_insert, Finset.mem_singleton] at hS ⊢
    rcases hS with rfl | rfl | rfl | rfl | rfl | rfl <;> simp

/-- The three marked points, one in each pairwise intersection `Aᵢ ∩ Aⱼ`:
`w₀ = (+,+,−)`, `w₁ = (+,−,+)`, `w₂ = (−,+,+)`. -/
def w₀ : Ω₇ := ⟨![true, true, false], by decide⟩
def w₁ : Ω₇ := ⟨![true, false, true], by decide⟩
def w₂ : Ω₇ := ⟨![false, true, true], by decide⟩

/-- The pattern: majority vote of the three marked points. Majority-of-3 is
self-dual, so complement-additivity holds for EVERY set — `s₀` is a legitimate
local state with no case analysis on `B`. -/
noncomputable def s₀ : LocalState powerDynkin blk where
  Val S := (w₀ ∈ S ∧ w₁ ∈ S) ∨ (w₀ ∈ S ∧ w₂ ∈ S) ∨ (w₁ ∈ S ∧ w₂ ∈ S)
  decVal := Classical.decPred _
  val_compl := by
    intro S _
    by_cases h0 : w₀ ∈ S <;> by_cases h1 : w₁ ∈ S <;> by_cases h2 : w₂ ∈ S <;>
      simp [Set.mem_compl_iff, h0, h1, h2]

/-! ### The three events are in the block and `s₀`-true -/

theorem A0_mem_blk : A 0 ∈ blk.sets := by simp [blk]
theorem A1_mem_blk : A 1 ∈ blk.sets := by simp [blk]
theorem A2_mem_blk : A 2 ∈ blk.sets := by simp [blk]

-- Each `A i` contains exactly the two marked points with `i`-th coordinate `+`.
theorem w₀_mem_A0 : w₀ ∈ A 0 := rfl
theorem w₁_mem_A0 : w₁ ∈ A 0 := rfl
theorem w₀_mem_A1 : w₀ ∈ A 1 := rfl
theorem w₂_mem_A1 : w₂ ∈ A 1 := rfl
theorem w₁_mem_A2 : w₁ ∈ A 2 := rfl
theorem w₂_mem_A2 : w₂ ∈ A 2 := rfl

theorem s₀_val_A0 : s₀.Val (A 0) := Or.inl ⟨w₀_mem_A0, w₁_mem_A0⟩
theorem s₀_val_A1 : s₀.Val (A 1) := Or.inr (Or.inl ⟨w₀_mem_A1, w₂_mem_A1⟩)
theorem s₀_val_A2 : s₀.Val (A 2) := Or.inr (Or.inr ⟨w₁_mem_A2, w₂_mem_A2⟩)

/-! ### Public theorem 1: clause (i) holds — empty kernel -/

/-- Clause (i) holds on a BOOLEAN carrier: the pattern has empty kernel.
Any kernel point lies in `A 0 ∩ A 1 ∩ A 2 = ∅` (it would be the all-`+`
point, which is not in `Ω₇`). -/
theorem omega7_kernel_empty : kernel s₀ = ∅ := by
  rw [eq_empty_iff_forall_notMem]
  intro x hx
  rw [kernel, mem_sInter] at hx
  have h0 : x ∈ A 0 := hx (A 0) ⟨A0_mem_blk, s₀_val_A0⟩
  have h1 : x ∈ A 1 := hx (A 1) ⟨A1_mem_blk, s₀_val_A1⟩
  have h2 : x ∈ A 2 := hx (A 2) ⟨A2_mem_blk, s₀_val_A2⟩
  apply x.2
  funext i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2

/-! ### Every σ-additive two-valued state on `P(Ω₇)` is Dirac -/

/-- On the (countable, here finite) full powerset every σ-additive two-valued
state is a point evaluation: disjointify a countable enumeration of `univ`
into singletons, σ-additivity picks the true singleton `{ω}`, and
monotonicity + complementation pin `Val S ↔ ω ∈ S` for every `S`. -/
theorem exists_dirac_point (s : TwoValuedState powerDynkin) :
    ∃ ω : Ω₇, ∀ S : Set Ω₇, s.Val S ↔ ω ∈ S := by
  obtain ⟨g, hdisj, hunion, hshape⟩ :=
    Ulam.countable_disjointified (countable_univ (α := Ω₇)) ⟨w₀, mem_univ w₀⟩
  have hHas : ∀ n, powerDynkin.Has (g n) := fun _ => trivial
  have huniv : s.Val (⋃ n, g n) := by rw [hunion]; exact s.val_univ
  obtain ⟨n, hn⟩ := (s.val_iUnion hdisj hHas).mp huniv
  rcases hshape n with h | ⟨ω, h⟩
  · rw [h] at hn
    exact absurd hn s.not_val_empty
  · rw [h] at hn
    refine ⟨ω, fun S => ⟨?_, ?_⟩⟩
    · intro hS
      by_contra hωS
      have hsub : {ω} ⊆ Sᶜ := singleton_subset_iff.mpr hωS
      have hcompl : s.Val Sᶜ := s.val_mono trivial trivial hsub hn
      exact (s.val_compl trivial).mp hcompl hS
    · intro hωS
      exact s.val_mono trivial trivial (singleton_subset_iff.mpr hωS) hn

/-! ### Public theorems 2–4 -/

/-- The literal-definition "witness" half: NO σ-additive two-valued state on
the (Boolean!) carrier extends the pattern. Without the coherence clause
this refutes the old Prop 2.1. -/
theorem omega7_no_sigma_extension :
    ¬ ∃ s : TwoValuedState powerDynkin, ExtendsS s s₀ := by
  rintro ⟨s, hs⟩
  obtain ⟨ω, hω⟩ := exists_dirac_point s
  have hd : ExtendsS (dirac ω) s₀ := fun S hS => (hω S).symm.trans (hs S hS)
  have hker : ω ∈ kernel s₀ := (dirac_iff s₀ ω).mp hd
  rw [omega7_kernel_empty] at hker
  exact notMem_empty ω hker

/-- The coherence clause does its job: the pattern is NOT finitely coherent. If
it were, the Boolean baseline (Prop 1.6) would produce a Dirac extension,
i.e. a kernel point — but the kernel is empty. -/
theorem omega7_not_coherent : ¬ FinitelyCoherent s₀ := by
  intro hcoh
  obtain ⟨ω, hω⟩ := boolean_baseline powerDynkin_interClosed s₀ hcoh
  have hker : ω ∈ kernel s₀ := (dirac_iff s₀ ω).mp hω
  rw [omega7_kernel_empty] at hker
  exact notMem_empty ω hker

/-- Sanity (from the Boolean baseline): the pattern is not a witness. -/
theorem omega7_not_witness : ¬ IsSigmaEssential s₀ :=
  boolean_no_witness powerDynkin_interClosed s₀

end SigmaEssential.Omega7
