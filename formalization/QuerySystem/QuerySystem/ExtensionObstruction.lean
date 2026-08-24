/-
# The obstruction to observational extension

Why a projective family of σ-additive marginals can fail to admit a limit
measure, stated for query systems.

## What this file is for

`stone_observational_extension` originally assumed only `UpperDirected`, and
`ce_iff_levelwise_continuity` shows collective exhaustion is exactly per-level
σ-additivity. Those hypotheses amount to Kolmogorov extension with no
regularity or compactness assumption of any kind, which is false: Sparre
Andersen and Jessen (1948) construct a counterexample. The hypothesis is now
`SequentiallyUpperDirected` and the theorem is proved.

This file formalizes the *mechanism* of that failure, which is the half specific
to this framework. An `EscapingTower` is a decreasing sequence of cylinder
events, each carrying the whole charge, with empty intersection; every finite
stage has all the mass and the limit has none. `not_exists_extension_of_escapingTower`
shows no query system carrying one admits an extension — regardless of its
directedness, surjectivity, or collective exhaustion.

## What is NOT here, and what it would take

The Andersen--Jessen system itself, which supplies such a tower. That needs a
decreasing sequence of *thick* subsets of `[0,1]` (full outer measure) with
empty intersection: `Xₖ = (V + Bₖ) ∩ [0,1]` where `V` is a transversal of
`ℝ ⧸ (ℤ + αℤ)` and `Bₖ = {n + mα : |n| ≥ k, n even}`. Thickness comes from the
measure-theoretic Steinhaus theorem, which Mathlib has as
`div_mem_nhds_one_of_haar_pos`; the transversal is `Quotient.out'` on the
quotient group. Mathlib has no thick sets and no Vitali-style transversal, so
this remains a real construction project. Until it is done, the claim that the
original statement was false rests on a hand check against the source, not on
the kernel.

Blueprint: `rmk:kolmogorov-refuted`, `rmk:extension-repaired`.
-/
import QuerySystem.DiscriminabilityFoundations

open MeasureTheory Filter Topology
open scoped ENNReal

namespace QuerySystem

variable (S : QuerySystem)

/-- An **escaping tower**: a decreasing sequence of cylinder events, each of
full charge, whose intersection is empty. This is the exact mechanism by which
a projective family of σ-additive marginals can fail to admit a limit measure.
Every finite stage carries all the mass; the limit carries none.

In the Andersen--Jessen system these are the diagonal cylinders
`Dₙ = {(x,…,x) × ∏_{k>n} Xₖ : x ∈ Xₙ}` over a decreasing sequence of thick
sets: `P(Dₙ) = λₙ(Xₙ) = 1` for every `n`, while `⋂ₙ Dₙ = ∅` because
`Xₖ ↓ ∅`. -/
structure EscapingTower (P : S.NormalizedCompatibleContents) where
  /-- the level of the `n`-th cylinder -/
  idx   : ℕ → S.ι
  /-- the base event at that level -/
  base  : ∀ n, Set ((S.q (idx n)).Outcome)
  meas  : ∀ n, MeasurableSet (base n)
  /-- each stage carries all the charge -/
  full  : ∀ n, P.ν (idx n) (base n) = 1
  anti  : Antitone fun n => S.Cyl (idx n) (base n)
  /-- yet nothing survives -/
  empty : ⋂ n, S.Cyl (idx n) (base n) = ∅

/-- **The obstruction.** No query system carrying an escaping tower admits an
extension of its charges to a probability measure on `Omega` — whatever its
directedness, surjectivity, or collective-exhaustion properties.

Note what this does *not* need: no hypothesis on `S` at all. The tower alone is
fatal. That is why strengthening `UpperDirected` was the only available repair
for `stone_observational_extension`: one cannot patch the conclusion or the
valuation layer around a tower, one can only assume an index layer rich enough
that no tower exists. -/
theorem not_exists_extension_of_escapingTower
    (P : S.NormalizedCompatibleContents) (T : S.EscapingTower P) :
    ¬ ∃ μ : Measure S.Omega, IsProbabilityMeasure μ ∧
        ∀ (i : S.ι) (A : Set ((S.q i).Outcome)), MeasurableSet A →
          μ (S.Cyl i A) = P.ν i A := by
  rintro ⟨μ, hprob, hcyl⟩
  set C : ℕ → Set S.Omega := fun n => S.Cyl (T.idx n) (T.base n) with hC
  have hone : ∀ n, μ (C n) = 1 := fun n => by
    rw [hC, hcyl (T.idx n) (T.base n) (T.meas n), T.full n]
  have hmeas : ∀ n, NullMeasurableSet (C n) μ := fun n =>
    (S.measurableSet_cyl (T.idx n) (T.base n) (T.meas n)).nullMeasurableSet
  have hlim : Tendsto (μ ∘ C) atTop (𝓝 (μ (⋂ n, C n))) :=
    tendsto_measure_iInter_atTop hmeas T.anti ⟨0, by rw [hone 0]; exact ENNReal.one_ne_top⟩
  -- the intersection is empty, so the limit is 0 -- while every term is 1
  rw [T.empty, measure_empty] at hlim
  have hconst : (fun n => μ (C n)) = fun _ : ℕ => (1 : ℝ≥0∞) := funext hone
  rw [show (μ ∘ C) = fun n => μ (C n) from rfl, hconst] at hlim
  exact zero_ne_one (tendsto_nhds_unique hlim tendsto_const_nhds)

/-- Contrapositive, in the form the repaired theorem uses: a query system whose
charges *do* extend carries no escaping tower. -/
theorem no_escapingTower_of_extension
    (P : S.NormalizedCompatibleContents)
    (h : ∃ μ : Measure S.Omega, IsProbabilityMeasure μ ∧
        ∀ (i : S.ι) (A : Set ((S.q i).Outcome)), MeasurableSet A →
          μ (S.Cyl i A) = P.ν i A) :
    IsEmpty (S.EscapingTower P) :=
  ⟨fun T => S.not_exists_extension_of_escapingTower P T h⟩

/-! ## The obstruction is not vacuous

A structure nobody can instantiate would make `not_exists_extension_of_escapingTower`
empty content. The finite–cofinite counterexample already in this development
carries a tower, which settles that. -/

open Classical in
/-- An enumeration of `ℚ`. -/
noncomputable def cexEnum : ℕ → ℚ := (exists_surjective_nat ℚ).choose

lemma cexEnum_surj : Function.Surjective cexEnum := (exists_surjective_nat ℚ).choose_spec

/-- `Eₙ = ℚ ∖ {q₀,…,qₙ}`: cofinite, decreasing, empty intersection. -/
def cexE (n : ℕ) : Set ℚ := {x | ∀ k ≤ n, x ≠ cexEnum k}

lemma cexE_cofinite (n : ℕ) : (cexE n)ᶜ.Finite := by
  apply Set.Finite.subset (Set.finite_Iic n |>.image cexEnum)
  intro x hx
  simp only [cexE, Set.mem_compl_iff, Set.mem_setOf_eq, not_forall, not_ne_iff] at hx
  obtain ⟨k, hk, hxk⟩ := hx
  exact ⟨k, Set.mem_Iic.mpr hk, hxk.symm⟩

lemma cexE_antitone : Antitone cexE := by
  intro m n hmn x hx k hk
  exact hx k (_root_.le_trans hk hmn)

lemma cexE_iInter : ⋂ n, cexE n = ∅ := by
  ext x
  simp only [cexE, Set.mem_iInter, Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false]
  push Not
  obtain ⟨n, hn⟩ := cexEnum_surj x
  exact ⟨n, n, Nat.le_refl n, hn.symm⟩

/-- **`EscapingTower` is inhabited.** The finite–cofinite counterexample carries
one: every `Eₙ` is cofinite, hence in the hyperfilter, hence of content 1, while
the `Eₙ` shrink to nothing.

This matters as a guard. `not_exists_extension_of_escapingTower` would be empty
content if no query system could carry a tower; it does not, and this is the
witness. -/
noncomputable def counterexampleTower :
    counterexampleQS.EscapingTower counterexampleNCC where
  idx _ := (0 : WithTop ℕ)
  base n := cexE n
  meas n := MeasurableSpace.measurableSet_generateFrom (Or.inr (cexE_cofinite n))
  full n := by
    show (haveI := Classical.dec (cexE n ∈ Filter.hyperfilter ℚ)
          if cexE n ∈ Filter.hyperfilter ℚ then (1 : ℝ≥0∞) else 0) = 1
    haveI := Classical.dec (cexE n ∈ Filter.hyperfilter ℚ)
    rw [if_pos (Filter.mem_hyperfilter_of_finite_compl (cexE_cofinite n))]
  anti := by
    intro m n hmn ω hω
    exact cexE_antitone hmn hω
  empty := by
    ext ω
    simp only [Set.mem_iInter, Set.mem_empty_iff_false, iff_false]
    intro h
    have : counterexampleQS.eval (0 : WithTop ℕ) ω ∈ ⋂ n, cexE n := Set.mem_iInter.mpr h
    rw [cexE_iInter] at this
    exact this

/-- Consequence: the finite–cofinite system admits no extension. Recovered from
the abstract obstruction rather than re-argued. -/
theorem counterexample_no_extension :
    ¬ ∃ μ : Measure counterexampleQS.Omega, IsProbabilityMeasure μ ∧
        ∀ (i : counterexampleQS.ι) (A : Set ((counterexampleQS.q i).Outcome)),
          MeasurableSet A → μ (counterexampleQS.Cyl i A) = counterexampleNCC.ν i A :=
  counterexampleQS.not_exists_extension_of_escapingTower counterexampleNCC counterexampleTower

end QuerySystem
