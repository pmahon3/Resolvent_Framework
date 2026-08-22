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

end QuerySystem
