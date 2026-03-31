/-
Copyright (c) 2025. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: [Your Name]
-/
import Mathlib.MeasureTheory.MeasurableSpace.Basic
import Mathlib.MeasureTheory.Measure.MeasureSpaceDef
import Mathlib.MeasureTheory.Measure.Map
import Mathlib.MeasureTheory.Measure.Typeclasses.Finite
import Mathlib.MeasureTheory.Measure.ProbabilityMeasure
import Mathlib.MeasureTheory.SetSemiring
import Mathlib.MeasureTheory.Measure.AddContent
import Mathlib.MeasureTheory.OuterMeasure.OfAddContent
import Mathlib.Data.ENNReal.Basic

/-!
# Query Systems and Observational Determination

This file formalizes query systems: preordered families of measurable spaces with
compatible refinement maps. The main results are:

1. **Observational Determination Theorem**: Two (probability) measures on the projective
   limit are equal iff they have equal marginals on all queries.

2. **Observational Extension** (infrastructure only): Premeasure well-definedness for
   the extension theorem. Full extension (Carathéodory + marginal recovery) is deferred
   to the next pass.

## Main Definitions

* `Query`: A measurable space representing possible outcomes of a single query
* `Refine q₁ q₂`: A measurable map between query outcomes representing refinement
* `QuerySystem`: A preordered family of queries with coherent refinement maps
* `QuerySystem.Omega`: The projective limit (coherent families of outcomes)
* `QuerySystem.Cyl i A`: Cylinder set based on query `i` and event `A`
* `QuerySystem.LowerDirected`: Any two queries have a common coarsening
* `QuerySystem.UpperDirected`: Any two queries have a common refinement
* `QuerySystem.SequentiallyUpperDirected`: Every sequence of queries has a common refinement
* `QuerySystem.CompatibleMarginals`: Marginal measures commute with refinement maps
* `QuerySystem.FinCyl s A`: Finite intersection of single-query cylinders
* `QuerySystem.preμ`: Premeasure value on a finite cylinder, via a chosen upper bound

## Main Results (Stage 1)

* `measurable_eval`: Evaluation maps are measurable
* `isPiSystem_CylGen`: Cylinder family is a π-system (under upper-directedness)
* `observational_determination`: Uniqueness via π-λ theorem
* `observational_determination_prob`: Probability measure version

## Extension Infrastructure (Stage 1 helpers)

* `lowerBound_finset`: Finite index sets admit a common lower bound
* `upperBound_finset`: Finite index sets admit a common upper bound
* `finCyl_eq_cyl_of_upperBound`: Finite cylinder = single cylinder at common upper bound
* `compat_apply_preimage`: Compatibility implies measure equality on preimages
* `measurableSet_constraintAt`: Measurability of the upper-bound constraint set
* `pullback_constraint_eq`: Equality of pullback constraint sets under π_trans
* `preμ_eq`: `preμ` equals `ν k` on the constraint set for any chosen upper bound `k`
* `preμ_wellDefined`: `preμ` is independent of the upper bound chosen
* `preμ_respects_finCyl_eq`: Equal sets imply equal `preμ` values (needs `EvalSurjective`)
* `preμ_disjoint_union`: Finite additivity of `preμ` (needs `EvalSurjective`)

## Implementation Notes

**Refinement convention** (fine-to-coarse / projective):
`le i j` means "j is finer than i" (j is MORE informative than i).
The map `π hij : Refine (q j) (q i)`, `(π hij).π : Outcome_j → Outcome_i` goes fine → coarse.
The coherence condition on Ω: `x i = (π hij).π (x j)` — coarser outcome determined by finer one.

This matches the standard projective system convention and Paper 1 (note.tex).

**Lower-directedness** (`LowerDirected`): `∀ i j, ∃ k, le k i ∧ le k j`.
k is LESS informative (coarser) than both i and j — a common coarsening.
Used for: `lowerBound_finset` (common lower bound for finite families).

**Upper-directedness** (`UpperDirected`): `∀ i j, ∃ k, le i k ∧ le j k`.
k is MORE informative (finer) than both i and j — a common refinement.
Used for the extension: `finCyl_eq_cyl_of_upperBound` with `(π hik).π : Outcome_k → Outcome_i`.

**Sequential upper-directedness** (`SequentiallyUpperDirected`): `∀ u : ℕ → ι, ∃ k, ∀ n, le (u n) k`.
Every sequence of indices has a common refinement. Implies `UpperDirected`.
The analytic hypothesis needed for σ-subadditivity of the cylinder premeasure.

## References

* note.tex: Observational Foundations of Probability
* Classical Kolmogorov extension theorem
-/

open MeasureTheory
open scoped ENNReal

universe u v

/-- A query is a measurable space representing the possible outcomes
    of asking a single question or making a single observation. -/
structure Query where
  Outcome : Type u
  instMeas : MeasurableSpace Outcome

attribute [instance] Query.instMeas

/-- A refinement between queries is a measurable function showing how
    outcomes of one query determine outcomes of another. -/
structure Refine (q₁ q₂ : Query.{u}) where
  π : q₁.Outcome → q₂.Outcome
  measurable_π : Measurable π

/-!
## QuerySystem: A preorder of queries with refinement maps

### Refinement convention (fine-to-coarse / projective)
- `le i j` means "j is at least as informative as i" (j refines i)
- `π hij : Outcome_j → Outcome_i` goes fine → coarse
- Coherence on Ω: `x i = (π hij).π (x j)` (the coarser outcome is determined by the finer one)

This is the standard projective-system convention, matching Paper 1 exactly.

### Lower-directedness
- `LowerDirected`: `∀ i j, ∃ k, le k i ∧ le k j`
- k is LESS informative than both i and j (common coarsening)
- Used for `lowerBound_finset` (common lower bound for finite families)

### Upper-directedness for the π-system and extension infrastructure
- `UpperDirected`: `∀ i j, ∃ k, le i k ∧ le j k`
- k is MORE informative than both i and j (common refinement)
- Used to prove CylGen is a π-system and set semiring (via `cyl_refine` pulling coarser cylinders to finer)
- Used for `finCyl_eq_cyl_of_upperBound`: finite cylinder = single cylinder at a common refinement,
  with well-typed projection maps `(π hik).π : Outcome_k → Outcome_i`

### Sequential upper-directedness for σ-subadditivity
- `SequentiallyUpperDirected`: `∀ u : ℕ → ι, ∃ k, ∀ n, le (u n) k`
- Every sequence of indices has a common refinement k
- Implies `UpperDirected` (taking constant sequences)
- The analytic hypothesis for σ-subadditivity: compresses countable cylinder families to one level
-/

structure QuerySystem where
  ι : Type v
  q : ι → Query.{u}
  le : ι → ι → Prop
  π : ∀ {i j : ι}, le i j → Refine (q j) (q i)

  le_refl : ∀ i, le i i
  le_trans : ∀ {i j k}, le i j → le j k → le i k

  π_refl :
    ∀ i, (π (le_refl i)).π = id

  π_trans :
    ∀ {i j k} (hij : le i j) (hjk : le j k),
      (π (le_trans hij hjk)).π =
      (π hij).π ∘ (π hjk).π

namespace QuerySystem

variable (S : QuerySystem.{u, v})

/-! ## Stage 1: Core definitions -/

/-- The projective limit: coherent families of query outcomes.

    An element `ω : Omega` assigns to each query `i` an outcome `ω.1 i`,
    subject to coherence: `x i = (π hij).π (x j)` whenever `le i j`.

    This matches Paper 1: the coarser outcome is determined by the finer one via
    the refinement map `π hij : Outcome_j → Outcome_i`.

    Analogous to the trajectory space `S^T` in classical stochastic process theory,
    generalized to arbitrary refinement systems. -/
def Omega :=
  { x : ∀ i : S.ι, (S.q i).Outcome //
      ∀ {i j} (hij : S.le i j),
        x i = (S.π hij).π (x j) }

/-- Evaluation at query `i`: extracts the outcome for query `i` from a coherent family.

    Analogous to coordinate projection `ω ↦ ω(t)` in the classical construction. -/
def eval (i : S.ι) : S.Omega → (S.q i).Outcome :=
  fun ω => ω.1 i

/-- Cylinder set: realizations where query `i` yields an outcome in `A`.

    These events generate the observable σ-field. -/
def Cyl (i : S.ι) (A : Set ((S.q i).Outcome)) : Set S.Omega :=
  { ω | S.eval i ω ∈ A }

/-- The observable σ-field generated by cylinder events.

    Equivalently, the smallest σ-algebra making all `eval i` measurable. -/
def sigmaQ : MeasurableSpace S.Omega :=
  MeasurableSpace.generateFrom
    { E : Set S.Omega | ∃ i A, MeasurableSet A ∧ E = S.Cyl i A }

/-- Canonical measurable structure on Ω from the observable σ-field. -/
instance : MeasurableSpace S.Omega := S.sigmaQ

/-- Evaluation maps are measurable with respect to the observable σ-field.

    **Proof:** Preimages of measurable sets under `eval i` are exactly cylinders `Cyl i A`,
    which are measurable by definition of `sigmaQ = generateFrom (cylinders)`. -/
theorem measurable_eval (i : S.ι) : Measurable (S.eval i) := by
  intro A hA
  have : MeasurableSet (S.Cyl i A) :=
    MeasurableSpace.measurableSet_generateFrom ⟨i, A, hA, rfl⟩
  simpa [QuerySystem.Cyl, QuerySystem.eval, Set.preimage] using this

/-- Compatible marginals: the family `ν` commutes with refinement maps.

    `map (π hij) (ν j) = ν i` whenever `le i j`.
    The pushforward of the finer measure along the coarsening map recovers the coarser measure.
    Matches Paper 1: `(π^j_i)_# ν_j = ν_i`.
    Analogous to Kolmogorov consistency for finite-dimensional distributions. -/
def CompatibleMarginals (ν : ∀ i : S.ι, Measure ((S.q i).Outcome)) : Prop :=
  ∀ {i j} (hij : S.le i j), Measure.map (S.π hij).π (ν j) = ν i

/-- Cylinder sets commute with refinement: `Cyl i A = Cyl j (π⁻¹ A)`.

    If `le i j` (j is finer than i), then observing the coarser query `i` yielding
    an outcome in `A ⊆ Outcome_i` is the same as observing the finer query `j`
    yielding an outcome whose image under `π hij : Outcome_j → Outcome_i` lies in `A`.

    Matches Paper 1: `Cyl(i, A) = Cyl(j, (π^j_i)⁻¹ A)`. -/
theorem cyl_refine {i j : S.ι} (hij : S.le i j) (A : Set ((S.q i).Outcome)) :
    S.Cyl i A = S.Cyl j ((S.π hij).π ⁻¹' A) := by
  ext ω
  have h := ω.2 hij
  constructor <;> intro hx <;> simpa [Cyl, eval, Set.preimage, h] using hx

/-- Lower-directedness: any two queries have a common coarsening (meet-like condition).

    `∀ i j, ∃ k, le k i ∧ le k j`

    k is less informative than both i and j — a common coarsening.
    Key hypothesis for the π-system proof: allows finite cylinder intersections to be
    rewritten as cylinders at a common coarsening via `cyl_refine`. -/
def LowerDirected : Prop :=
  ∀ i j : S.ι, ∃ k : S.ι, S.le k i ∧ S.le k j

/-- Deprecated alias for `LowerDirected`. -/
@[deprecated LowerDirected (since := "2026-03-04")]
def Directed : Prop := S.LowerDirected

/-- Upper-directedness: any two queries have a common refinement (join-like condition).

    `∀ i j, ∃ k, le i k ∧ le j k`

    k is more informative than both i and j — a common refinement.
    Key hypothesis for the extension infrastructure: allows finite cylinder intersections
    to be compressed to a single cylinder at a common refinement level k, where the
    projection maps `π hik : Outcome_k → Outcome_i` are well-typed. -/
def UpperDirected : Prop :=
  ∀ i j : S.ι, ∃ k : S.ι, S.le i k ∧ S.le j k

/-- Sequential upper-directedness: every sequence of indices has a common upper bound.

    `∀ u : ℕ → ι, ∃ k, ∀ n, le (u n) k`

    k is finer than every element of the sequence — a common refinement for countable families.
    This is stronger than `UpperDirected` (which gives refinements for pairs) and is the
    analytic hypothesis needed for σ-subadditivity of the cylinder premeasure.

    Mathematical role: with this hypothesis, any sequence of cylinders `Cyl (u n) (A n)` can
    be compressed to a single level k, reducing σ-subadditivity to σ-additivity of `ν k`. -/
def SequentiallyUpperDirected : Prop :=
  ∀ u : ℕ → S.ι, ∃ k : S.ι, ∀ n : ℕ, S.le (u n) k

/-- The generating family of cylinder events used in `sigmaQ`. -/
def CylGen : Set (Set S.Omega) :=
  { E : Set S.Omega | ∃ i A, MeasurableSet A ∧ E = S.Cyl i A }

/-- Cylinders are measurable in the observable σ-field. -/
lemma measurableSet_cyl (i : S.ι) (A : Set ((S.q i).Outcome)) (hA : MeasurableSet A) :
    MeasurableSet (S.Cyl i A) :=
  MeasurableSpace.measurableSet_generateFrom ⟨i, A, hA, rfl⟩

/-- Pushforward of `P` along `eval i`, evaluated at `A`, equals `P` of the cylinder `Cyl i A`. -/
lemma map_apply_eval_eq_cyl
    (P : Measure S.Omega) (i : S.ι) (A : Set ((S.q i).Outcome)) (hA : MeasurableSet A) :
    (Measure.map (S.eval i) P) A = P (S.Cyl i A) := by
  simpa [QuerySystem.Cyl, QuerySystem.eval, Set.preimage]
    using Measure.map_apply (S.measurable_eval i) hA

/-- **Projection compatibility**: evaluation commutes with refinement maps.

    `eval i = (π hij).π ∘ eval j` whenever `le i j`.

    Matches Paper 1, Lemma 3.1: `eval_i = π^j_i ∘ eval_j`.
    The coarser evaluation is the composition of the finer evaluation with the coarsening map. -/
theorem eval_comp_refine {i j : S.ι} (hij : S.le i j) :
    S.eval i = (S.π hij).π ∘ S.eval j := by
  funext ω
  exact ω.2 hij

/-- The cylinder family forms a π-system when the preorder is upper-directed.

    **Proof sketch:** Given `Cyl i A` and `Cyl j B`, upper-directedness gives `k` with
    `i ≤ k` and `j ≤ k` (k is a common refinement). Use `cyl_refine` to lift both:
    `Cyl i A = Cyl k ((π hik)⁻¹ A)` and `Cyl j B = Cyl k ((π hjk)⁻¹ B)`.
    The intersection is then `Cyl k ((π hik)⁻¹ A ∩ (π hjk)⁻¹ B)`, which is measurable
    by preimage stability.

    Matches Paper 1, Lemma 3.2. -/
theorem isPiSystem_CylGen (udir : S.UpperDirected) : IsPiSystem (S.CylGen) := by
  classical
  intro s hs t ht _
  rcases hs with ⟨i, A, hA, rfl⟩
  rcases ht with ⟨j, B, hB, rfl⟩
  -- Use upper-directedness: find k finer than both i and j.
  -- With le i k and le j k, (π hik).π : O_k → O_i and (π hjk).π : O_k → O_j.
  rcases udir i j with ⟨k, hik, hjk⟩
  have eq : S.Cyl i A ∩ S.Cyl j B =
      S.Cyl k ((S.π hik).π ⁻¹' A ∩ (S.π hjk).π ⁻¹' B) := by
    calc S.Cyl i A ∩ S.Cyl j B
        = S.Cyl k ((S.π hik).π ⁻¹' A) ∩ S.Cyl k ((S.π hjk).π ⁻¹' B) := by
          rw [S.cyl_refine hik A, S.cyl_refine hjk B]
      _ = S.Cyl k ((S.π hik).π ⁻¹' A ∩ (S.π hjk).π ⁻¹' B) := by
          ext ω; simp [QuerySystem.Cyl, Set.mem_inter_iff]
  rw [eq]
  exact ⟨k, (S.π hik).π ⁻¹' A ∩ (S.π hjk).π ⁻¹' B,
    (hA.preimage (S.π hik).measurable_π).inter (hB.preimage (S.π hjk).measurable_π), rfl⟩

/-! ## Stage 1: Determination theorems -/

/-- **Observational Determination Theorem**: Finite measures on Ω are determined by marginals.

    If `P` and `P'` have equal pushforwards along every `eval i`, then `P = P'`.

    **Proof strategy:**
    1. Equal pushforwards ⟹ agreement on all cylinders (by `map_apply_eval_eq_cyl`)
    2. Cylinders form a π-system (by `isPiSystem_CylGen` + upper-directedness)
    3. Apply `ext_of_generate_finite` (the π-λ theorem for finite measures) -/
theorem observational_determination
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (P P' : Measure S.Omega)
    [IsFiniteMeasure P]
    (h : ∀ i, Measure.map (S.eval i) P = Measure.map (S.eval i) P') :
    P = P' := by
  classical
  have hagree : ∀ s ∈ S.CylGen, P s = P' s := by
    intro s hs
    rcases hs with ⟨i, A, hA, rfl⟩
    have hi := congrArg (fun μ : Measure ((S.q i).Outcome) => μ A) (h i)
    simpa [S.map_apply_eval_eq_cyl P i A hA, S.map_apply_eval_eq_cyl P' i A hA] using hi
  have huniv : P Set.univ = P' Set.univ := by
    obtain ⟨i⟩ := ‹Nonempty S.ι›
    have hi := congrArg (fun μ : Measure ((S.q i).Outcome) => μ Set.univ) (h i)
    have cyl_univ : S.Cyl i Set.univ = Set.univ := by
      ext ω; simp [QuerySystem.Cyl, QuerySystem.eval]
    rw [← cyl_univ]
    simpa [S.map_apply_eval_eq_cyl P i Set.univ MeasurableSet.univ,
           S.map_apply_eval_eq_cyl P' i Set.univ MeasurableSet.univ] using hi
  refine ext_of_generate_finite S.CylGen ?_ (S.isPiSystem_CylGen udir) ?_ huniv
  · rfl
  · exact hagree

/-- Probability-measure version of observational determination.

    Two probability measures with equal marginals on all queries are equal. -/
theorem observational_determination_prob
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (P P' : ProbabilityMeasure S.Omega)
    (h : ∀ i, Measure.map (S.eval i) P.toMeasure = Measure.map (S.eval i) P'.toMeasure) :
    P = P' := by
  apply ProbabilityMeasure.toMeasure_injective
  exact S.observational_determination udir P.toMeasure P'.toMeasure h

/-!
## Extension infrastructure (Stage 1)

This section provides the helper lemmas needed for the observational extension theorem.
The full extension (Carathéodory + marginal recovery + uniqueness packaging) is deferred.

### Architecture:
1. ✓ `FinCyl`: finite intersections of single-query cylinders
2. ✓ `lowerBound_finset`: any finite index set has a common lower bound
3. ✓ `upperBound_finset`: any finite index set has a common upper bound
4. ✓ `finCyl_eq_cyl_of_upperBound`: compression to a single cylinder at a common refinement
5. ✓ `compat_apply_preimage`: compatibility ⟹ measure equality on preimages
6. ✓ `measurableSet_constraintAt`: measurability of the constraint set at an upper bound
7. ✓ `pullback_constraint_eq`: the two pullback constraint sets coincide (uses `π_trans`)
8. ✓ `preμ_eq`: exposes `preμ` in terms of any explicit upper bound
9. ✓ `preμ_wellDefined`: `preμ` is independent of the upper bound chosen
10. ✓ `preμAt_single`: `preμAt` on a singleton index set equals `ν i (A i)`
11. ✓ `isSetSemiring_CylGen`: `CylGen` is a set semiring (under `UpperDirected`)
12. ✓ `preμ_respects_finCyl_eq`: equal sets imply equal masses (needs `EvalSurjective`)
13. ✓ `preμ_disjoint_union`: finite additivity (needs `EvalSurjective`)
14. ✓ `cylGen_addContent`: `preμ` packaged as an `AddContent ℝ≥0∞ S.CylGen`
15. ✓ `sequentiallyUpperDirected_implies_upperDirected`: `SequentiallyUpperDirected → UpperDirected`
16. ✓ `cylGen_seq_compress`: compress a sequence of cylinders to one level (via `SequentiallyUpperDirected`)
17. ✓ `cylGen_addContent_isSigmaSubadditive`: σ-subadditivity (via `SequentiallyUpperDirected`)
18. ✓ `observational_extension`: full extension theorem
-/

/-- A finite cylinder: realizations satisfying `eval i ω ∈ A i` for all `i ∈ s`. -/
def FinCyl (s : Finset S.ι) (A : ∀ i, Set ((S.q i).Outcome)) : Set S.Omega :=
  { ω | ∀ i, i ∈ s → S.eval i ω ∈ A i }

/-- Finite cylinders are measurable (finite intersection of measurable cylinders). -/
lemma measurableSet_finCyl
    (s : Finset S.ι)
    (A : ∀ i, Set ((S.q i).Outcome))
    (hA : ∀ i ∈ s, MeasurableSet (A i)) :
    MeasurableSet (S.FinCyl s A) := by
  classical
  induction s using Finset.cons_induction with
  | empty =>
    have : S.FinCyl ∅ A = Set.univ := by ext ω; simp [FinCyl]
    rw [this]; exact MeasurableSet.univ
  | cons i s hi ih =>
    have eq : S.FinCyl (Finset.cons i s hi) A = S.Cyl i (A i) ∩ S.FinCyl s A := by
      ext ω
      simp only [FinCyl, Cyl, eval, Finset.mem_cons, Set.mem_inter_iff, Set.mem_setOf_eq]
      constructor
      · intro h; exact ⟨h i (Or.inl rfl), fun j hj => h j (Or.inr hj)⟩
      · intro ⟨hi_mem, hs_mem⟩ j hj
        cases hj with
        | inl h => subst h; exact hi_mem
        | inr h => exact hs_mem j h
    rw [eq]
    exact (S.measurableSet_cyl i (A i) (hA i (Finset.mem_cons_self i s))).inter
      (ih (fun j hj => hA j (Finset.mem_cons_of_mem hj)))

/-- Lower-directedness implies any finite set of indices admits a common lower bound.

    **Proof:** Induction on `s`. Empty case uses `Nonempty`. Inductive step uses
    lower-directedness to find a lower bound `k` below both the current lower bound
    `k'` of the tail and the new index `i`. -/
lemma lowerBound_finset [Nonempty S.ι] (dir : S.LowerDirected) (s : Finset S.ι) :
    ∃ k, ∀ i ∈ s, S.le k i := by
  induction s using Finset.cons_induction with
  | empty =>
    obtain ⟨k⟩ := ‹Nonempty S.ι›
    exact ⟨k, fun i hi => absurd hi (Finset.notMem_empty i)⟩
  | cons i s hi ih =>
    rcases ih with ⟨k', hk'⟩
    rcases dir k' i with ⟨k, hkk', hki⟩
    exact ⟨k, fun j hj => by
      simp only [Finset.mem_cons] at hj
      cases hj with
      | inl heq => subst heq; exact hki
      | inr hmem => exact S.le_trans hkk' (hk' j hmem)⟩

/-- Upper-directedness implies any finite set of indices admits a common upper bound.

    **Proof:** Induction on `s`. Empty case uses `Nonempty`. Inductive step uses
    upper-directedness to find an upper bound `k` above both the current upper bound
    `k'` of the tail and the new index `i`. -/
lemma upperBound_finset [Nonempty S.ι] (udir : S.UpperDirected) (s : Finset S.ι) :
    ∃ k, ∀ i ∈ s, S.le i k := by
  induction s using Finset.cons_induction with
  | empty =>
    obtain ⟨k⟩ := ‹Nonempty S.ι›
    exact ⟨k, fun i hi => absurd hi (Finset.notMem_empty i)⟩
  | cons i s hi ih =>
    rcases ih with ⟨k', hk'⟩
    rcases udir k' i with ⟨k, hk'k, hik⟩
    exact ⟨k, fun j hj => by
      simp only [Finset.mem_cons] at hj
      cases hj with
      | inl heq => subst heq; exact hik
      | inr hmem => exact S.le_trans (hk' j hmem) hk'k⟩

/-- Compression: A finite cylinder equals a single cylinder at any common upper bound.

    With the projective convention (`le i k` means k is finer than i,
    `π hik : Refine (q k) (q i)`, `(π hik).π : Outcome_k → Outcome_i`),
    the coherence condition gives `ω.1 i = (π hik).π (ω.1 k)`.

    Therefore `ω ∈ FinCyl s A` iff `∀ i ∈ s, ω.1 i ∈ A i`
                                   iff `∀ i ∈ s, (π hik).π (ω.1 k) ∈ A i`
                                   iff `ω.1 k ∈ {o_k | ∀ i ∈ s, (π hik).π o_k ∈ A i}`
                                   iff `ω ∈ Cyl k (constraint set)`. -/
lemma finCyl_eq_cyl_of_upperBound
    {s : Finset S.ι} {A : ∀ i, Set ((S.q i).Outcome)} {k : S.ι}
    (hk : ∀ i ∈ s, S.le i k) :
    S.FinCyl s A =
    S.Cyl k {o | ∀ (i : S.ι) (hi : i ∈ s), (S.π (hk i hi)).π o ∈ A i} := by
  ext ω
  simp only [FinCyl, Cyl, eval, Set.mem_setOf_eq]
  constructor
  · intro hω i hi
    -- Coherence: ω.1 i = (π hik).π (ω.1 k), so ω.1 i ∈ A i iff (π hik).π (ω.1 k) ∈ A i.
    rw [← ω.2 (hk i hi)]
    exact hω i hi
  · intro hω i hi
    -- From hω: (π hik).π (ω.1 k) ∈ A i. By coherence ω.1 i = (π hik).π (ω.1 k).
    rw [ω.2 (hk i hi)]
    exact hω i hi

/-- Compatibility implies measure equality on preimages.

    `ν k E = ν i ((π hki)⁻¹ E)` when `le k i` (i is finer) and `map (π hki) (ν i) = ν k`.

    With the new convention: `π hki : Outcome_i → Outcome_k`, `map (π hki) (ν i) = ν k`,
    so for measurable `E ⊆ Outcome_k`: `ν k E = ν i ((π hki)⁻¹ E)`. -/
lemma compat_apply_preimage
    {ν : ∀ i, Measure ((S.q i).Outcome)}
    (compat : S.CompatibleMarginals ν)
    {k i : S.ι} (hki : S.le k i)
    (E : Set ((S.q k).Outcome)) (hE : MeasurableSet E) :
    ν k E = ν i ((S.π hki).π ⁻¹' E) := by
  have h := compat hki
  rw [← h, Measure.map_apply (S.π hki).measurable_π hE]

/-- **Measurability of the constraint set at an upper bound.**

    For any upper bound `k_ub` for a finite index set `t ⊆ s` (meaning `∀ i ∈ t, le i k_ub`),
    the set `{o : Outcome_{k_ub} | ∀ i ∈ t, (π hk_ub i hi).π o ∈ A i}` is measurable.

    Here `(π hk_ub i hi).π : Outcome_{k_ub} → Outcome_i` (k_ub finer → coarser i), so
    the set is a finite intersection of measurable preimages, hence measurable.

    **Proof:** Induction on `t`. Empty case: set is `univ`. Inductive step:
    decompose into `(π (hk_ub i ·))⁻¹ (A i) ∩ (constraint for tail)`. -/
lemma measurableSet_constraintAt
    {s : Finset S.ι}
    (A : ∀ i, Set ((S.q i).Outcome))
    (hA : ∀ i ∈ s, MeasurableSet (A i)) :
    ∀ (t : Finset S.ι) (ht_sub : t ⊆ s) (k_ub : S.ι) (hk_ub : ∀ i ∈ t, S.le i k_ub),
    MeasurableSet
      {o : (S.q k_ub).Outcome | ∀ (i : S.ι) (hi : i ∈ t), (S.π (hk_ub i hi)).π o ∈ A i} := by
  intro t ht_sub
  classical
  induction t using Finset.cons_induction with
  | empty =>
    intro k_ub _
    convert MeasurableSet.univ using 1
    ext o; simp [Finset.notMem_empty]
  | cons i t' hi_notin ih =>
    intro k_ub hk_ub
    have eq :
        {o : (S.q k_ub).Outcome | ∀ (j : S.ι) (hj : j ∈ Finset.cons i t' hi_notin),
            (S.π (hk_ub j hj)).π o ∈ A j} =
        (S.π (hk_ub i (Finset.mem_cons_self i t'))).π ⁻¹' (A i) ∩
        {o : (S.q k_ub).Outcome | ∀ (j : S.ι) (hj : j ∈ t'),
            (S.π (hk_ub j (Finset.mem_cons_of_mem hj))).π o ∈ A j} := by
      ext o
      simp only [Set.mem_setOf_eq, Set.mem_inter_iff, Set.mem_preimage, Finset.mem_cons]
      constructor
      · intro h
        exact ⟨h i (Or.inl rfl), fun j hj => h j (Or.inr hj)⟩
      · intro ⟨hi_mem, ht_mem⟩ j hj
        cases hj with
        | inl heq => subst heq; exact hi_mem
        | inr hmem => exact ht_mem j hmem
    rw [eq]
    apply MeasurableSet.inter
    · exact (hA i (ht_sub (Finset.mem_cons_self i t'))).preimage
        (S.π (hk_ub i (Finset.mem_cons_self i t'))).measurable_π
    · exact ih (fun j hj => ht_sub (Finset.mem_cons_of_mem hj))
        k_ub (fun j hj => hk_ub j (Finset.mem_cons_of_mem hj))

/-- **Equality of pullback constraint sets under two upper bounds.**

    Given upper bounds `k` and `k'` for `s` (`∀ i ∈ s, le i k` and `le i k'`) and a
    common upper bound `m` of both (`le k m` and `le k' m`, so m is finer than both),
    the preimages of the respective constraint sets under `π hkm` and `π hk'm` coincide.

    Here `(π hkm).π : Outcome_m → Outcome_k` and `(π hik).π : Outcome_k → Outcome_i`.
    The preimage set at m: `{o_m | ∀ i ∈ s, (π hik).π ((π hkm).π o_m) ∈ A i}`.
    By `π_trans`, `(π hik).π ∘ (π hkm).π = (π (le_trans hik hkm)).π`.
    Both sides reduce to `{o_m | ∀ i ∈ s, (π (le_trans hik hkm)).π o_m ∈ A i}`, which
    is the same for k and k' by proof irrelevance of `le_trans hik hkm = le_trans hik' hk'm`. -/
lemma pullback_constraint_eq
    {s : Finset S.ι}
    (A : ∀ i, Set ((S.q i).Outcome))
    {k k' m : S.ι}
    (hk  : ∀ i ∈ s, S.le i k)
    (hk' : ∀ i ∈ s, S.le i k')
    (hkm  : S.le k  m)
    (hk'm : S.le k' m) :
    (S.π hkm).π ⁻¹'
      {o : (S.q k).Outcome  | ∀ (i : S.ι) (hi : i ∈ s), (S.π (hk  i hi)).π o ∈ A i} =
    (S.π hk'm).π ⁻¹'
      {o : (S.q k').Outcome | ∀ (i : S.ι) (hi : i ∈ s), (S.π (hk' i hi)).π o ∈ A i} := by
  ext o
  simp only [Set.mem_preimage, Set.mem_setOf_eq]
  -- Both sides reduce to: ∀ i ∈ s, (π (le_trans hik hkm)).π o ∈ A i
  -- by π_trans: (π hik).π ∘ (π hkm).π = (π (le_trans hik hkm)).π
  constructor <;> intro h i hi
  · have from_h := h i hi
    have eq1 : (S.π (S.le_trans (hk  i hi) hkm )).π = (S.π (hk  i hi)).π ∘ (S.π hkm ).π :=
      S.π_trans (hk i hi) hkm
    have eq2 : (S.π (S.le_trans (hk' i hi) hk'm)).π = (S.π (hk' i hi)).π ∘ (S.π hk'm).π :=
      S.π_trans (hk' i hi) hk'm
    have hproof : S.le_trans (hk i hi) hkm = S.le_trans (hk' i hi) hk'm :=
      Subsingleton.elim _ _
    have key : (S.π (hk i hi)).π ((S.π hkm).π o) = (S.π (hk' i hi)).π ((S.π hk'm).π o) := by
      have lhs_eq : (S.π (hk  i hi)).π ((S.π hkm ).π o) = (S.π (S.le_trans (hk  i hi) hkm )).π o :=
        (congrFun eq1 o).symm
      have rhs_eq : (S.π (hk' i hi)).π ((S.π hk'm).π o) = (S.π (S.le_trans (hk' i hi) hk'm)).π o :=
        (congrFun eq2 o).symm
      rw [lhs_eq, rhs_eq, hproof]
    rw [← key]; exact from_h
  · have from_h := h i hi
    have eq1 : (S.π (S.le_trans (hk  i hi) hkm )).π = (S.π (hk  i hi)).π ∘ (S.π hkm ).π :=
      S.π_trans (hk i hi) hkm
    have eq2 : (S.π (S.le_trans (hk' i hi) hk'm)).π = (S.π (hk' i hi)).π ∘ (S.π hk'm).π :=
      S.π_trans (hk' i hi) hk'm
    have hproof : S.le_trans (hk i hi) hkm = S.le_trans (hk' i hi) hk'm :=
      Subsingleton.elim _ _
    have key : (S.π (hk i hi)).π ((S.π hkm).π o) = (S.π (hk' i hi)).π ((S.π hk'm).π o) := by
      have lhs_eq : (S.π (hk  i hi)).π ((S.π hkm ).π o) = (S.π (S.le_trans (hk  i hi) hkm )).π o :=
        (congrFun eq1 o).symm
      have rhs_eq : (S.π (hk' i hi)).π ((S.π hk'm).π o) = (S.π (S.le_trans (hk' i hi) hk'm)).π o :=
        (congrFun eq2 o).symm
      rw [lhs_eq, rhs_eq, hproof]
    rw [key]; exact from_h

/-- Premeasure value on `(s, A)` using a specific upper bound `k`.

    `k` is finer than all `i ∈ s` (`∀ i ∈ s, le i k`), so `(π hik).π : Outcome_k → Outcome_i`.
    The constraint set `{o_k | ∀ i ∈ s, (π hik).π o_k ∈ A_i}` is well-typed, and
    `preμAt ν hk A = ν k (constraint set)`. -/
noncomputable def preμAt
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    {s : Finset S.ι} {k : S.ι}
    (hk : ∀ i ∈ s, S.le i k)
    (A : ∀ i : S.ι, Set ((S.q i).Outcome)) : ENNReal :=
  ν k {o | ∀ (i : S.ι) (hi : i ∈ s), (S.π (hk i hi)).π o ∈ A i}

/-- Premeasure on finite cylinders (definition using classical choice of upper bound). -/
noncomputable def preμ
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (s : Finset S.ι)
    (A : ∀ i : S.ι, Set ((S.q i).Outcome)) : ENNReal :=
  let ⟨k, hk⟩ := Classical.indefiniteDescription _ (S.upperBound_finset udir s)
  S.preμAt ν hk A

/-- **Premeasure Well-Definedness**: `preμ` is independent of the upper bound chosen.

    Given any two upper bounds `k` and `k'` for `s` (`∀ i ∈ s, le i k` and `le i k'`),
    the constraint-set measures agree: `ν k (constraint at k) = ν k' (constraint at k')`.

    **Proof strategy:**
    1. Use `UpperDirected` to find a common upper bound `m` of k and k' (`le k m`, `le k' m`).
    2. Push each measure forward to m using `compat_apply_preimage`.
    3. Show the pullback constraint sets are equal via `pullback_constraint_eq`. -/
lemma preμ_wellDefined
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (ν : ∀ i, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν)
    (s : Finset S.ι)
    (A : ∀ i, Set ((S.q i).Outcome))
    (hA : ∀ i ∈ s, MeasurableSet (A i)) :
    ∀ {k k' : S.ι} (hk : ∀ i ∈ s, S.le i k) (hk' : ∀ i ∈ s, S.le i k'),
    S.preμAt ν hk A = S.preμAt ν hk' A := by
  intro k k' hk hk'
  rcases udir k k' with ⟨m, hkm, hk'm⟩
  -- The constraint sets at k and k'
  let Ek  : Set (S.q k ).Outcome := {o | ∀ (i : S.ι) (hi : i ∈ s), (S.π (hk  i hi)).π o ∈ A i}
  let Ek' : Set (S.q k').Outcome := {o | ∀ (i : S.ι) (hi : i ∈ s), (S.π (hk' i hi)).π o ∈ A i}
  -- Measurability of constraint sets
  have hEk  : MeasurableSet Ek  := S.measurableSet_constraintAt A hA s (fun _ h => h) k  hk
  have hEk' : MeasurableSet Ek' := S.measurableSet_constraintAt A hA s (fun _ h => h) k' hk'
  -- Push both measures forward to m via compatibility
  -- compat_apply_preimage: ν k Ek = ν m ((π hkm)⁻¹ Ek) since map (π hkm) (ν m) = ν k
  have step1 : ν k Ek = ν m ((S.π hkm).π ⁻¹' Ek) :=
    S.compat_apply_preimage compat hkm Ek hEk
  have step2 : ν k' Ek' = ν m ((S.π hk'm).π ⁻¹' Ek') :=
    S.compat_apply_preimage compat hk'm Ek' hEk'
  -- The two preimages at m are equal
  have preimages_eq : (S.π hkm).π ⁻¹' Ek = (S.π hk'm).π ⁻¹' Ek' :=
    S.pullback_constraint_eq A hk hk' hkm hk'm
  -- Combine
  simp only [preμAt]
  calc ν k Ek = ν m ((S.π hkm).π ⁻¹' Ek)   := step1
    _         = ν m ((S.π hk'm).π ⁻¹' Ek')  := by rw [preimages_eq]
    _         = ν k' Ek'                     := step2.symm

/-- `preμ` equals `preμAt` for any explicitly given upper bound.

    This lemma lets the next extension pass work with `preμ` via an explicit upper bound,
    without going through `Classical.indefiniteDescription` directly.
    Key use: marginal recovery `(eval i)_# P = ν i` reduces to `preμAt ν (hk i ·) A = ν i A`. -/
lemma preμ_eq
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν)
    (s : Finset S.ι)
    (A : ∀ i : S.ι, Set ((S.q i).Outcome))
    (hA : ∀ i ∈ s, MeasurableSet (A i))
    {k : S.ι} (hk : ∀ i ∈ s, S.le i k) :
    S.preμ udir ν s A = S.preμAt ν hk A := by
  -- preμ = preμAt ν hk₀ where hk₀ is the classically chosen upper bound.
  -- preμ_wellDefined says preμAt ν hk₀ = preμAt ν hk for any two upper bounds.
  show S.preμAt ν (Classical.indefiniteDescription _ (S.upperBound_finset udir s)).2 A =
       S.preμAt ν hk A
  exact S.preμ_wellDefined udir ν compat s A hA _ hk

/-!
## Extension infrastructure (Stage 2): measurable finite cylinders and additive content

Strategy: define mass on finite-cylinder *presentations* `(s, A, hA)` via `preμ`, prove
invariance under equal-set presentations, prove finite additivity at the finite-cylinder
level by compressing to a common lower bound, then package as `AddContent`.

This avoids the bad route of choosing representatives from `CylGen` membership proofs,
which requires `Cyl k E₁ = Cyl k E₂ → E₁ = E₂` (generally false without surjectivity of `eval`).

**Note on `EvalSurjective`:**  The well-definedness and additivity results below carry a
`EvalSurjective` hypothesis:

  `EvalSurjective : Prop := ∀ i, Function.Surjective (S.eval i)`

This is a **realizability / amalgamation condition** on the projective limit: every local
outcome at query level `i` extends to a globally coherent realization in `Omega`.  It is
mathematically equivalent to saying that the system has no "phantom" outcomes that cannot
be observed globally.

This hypothesis is **not** present in the current note.tex and constitutes an alignment gap
between the Lean formalization and the manuscript.  The resulting theorem
(`observational_extension_of_evalSurjective`) is stronger than the note states.  Future
work should either (a) prove `EvalSurjective` from a weaker richness assumption or
(b) weaken the statement to avoid it.
-/

/-- **Realizability / amalgamation condition on the projective limit.**

    Every local outcome at query level `i` extends to a coherent global realization in `Omega`.
    Equivalently, the evaluation maps `eval i : Omega → Outcome_i` are all surjective.

    This is a strengthening beyond the current note.tex hypotheses.  It is needed for the
    well-definedness and additivity of `preμ` (to conclude `E₁ = E₂` from
    `eval i ⁻¹' E₁ = eval i ⁻¹' E₂`).  See the note in the Stage 2 section header. -/
def EvalSurjective : Prop := ∀ i : S.ι, Function.Surjective (S.eval i)

/-- **`preμAt` on a singleton index equals `ν i (A i)`.**

    When `s = {i}` and `k = i`, `hk : le i i = le_refl i`, so
    `(π (le_refl i)).π = id` by `π_refl`. The constraint set
    `{o | (π (le_refl i)).π o ∈ A i} = {o | o ∈ A i} = A i`.

    Key bridge to marginal recovery: `(eval i)_# P = ν i` will follow from this. -/
lemma preμAt_single_eq_marginal
    (ν : ∀ j : S.ι, Measure ((S.q j).Outcome))
    (i : S.ι)
    (A : ∀ j : S.ι, Set ((S.q j).Outcome)) :
    S.preμAt ν (s := {i}) (k := i)
        (fun j hj => Finset.mem_singleton.mp hj ▸ S.le_refl j) A = ν i (A i) := by
  simp only [preμAt]
  congr 1
  ext o
  simp only [Finset.mem_singleton, Set.mem_setOf_eq]
  constructor
  · intro h
    have h' := h i rfl
    have hid := congrFun (S.π_refl i) o
    simp only [id] at hid
    rwa [hid] at h'
  · intro ho j hj
    have hid := congrFun (S.π_refl i) o
    simp only [id] at hid
    subst hj
    rw [hid]
    exact ho

/-! ### Measurable finite cylinders -/

/-- A measurable finite cylinder: a finite index set `s`, component sets `A i`, and
    measurability of each `A i` for `i ∈ s`.

    This packages the triple `(s, A, hA)` that appears throughout the extension
    infrastructure, avoiding repeated bundling and unbundling. -/
structure MeasFinCyl where
  s   : Finset S.ι
  A   : ∀ i : S.ι, Set ((S.q i).Outcome)
  hA  : ∀ i ∈ s, MeasurableSet (A i)

/-- The subset of `Omega` defined by a measurable finite cylinder. -/
def MeasFinCyl.set (C : S.MeasFinCyl) : Set S.Omega :=
  S.FinCyl C.s C.A

/-- The `preμ` mass of a measurable finite cylinder. -/
noncomputable def MeasFinCyl.mass
    (C : S.MeasFinCyl)
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome)) : ℝ≥0∞ :=
  S.preμ udir ν C.s C.A

/-- **Premeasure respects equal finite-cylinder sets.**

    If two measurable finite-cylinder presentations define the same subset of `Omega`,
    their `preμ` values agree.

    **Proof strategy:** Compress both to a common upper bound `m`. By
    `finCyl_eq_cyl_of_upperBound`, both become `Cyl m Ec` and `Cyl m Ed`. Since
    `Cyl m E = eval m ⁻¹' E` by definition, equality of cylinder sets in `Omega`
    means `eval m ⁻¹' Ec = eval m ⁻¹' Ed`. With `surj m : Surjective (eval m)`, this
    implies `Ec = Ed`, and hence `ν m Ec = ν m Ed`. -/
lemma preμ_respects_finCyl_eq
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν)
    (surj : S.EvalSurjective)
    (C D : S.MeasFinCyl)
    (hEq : C.set = D.set) :
    S.preμ udir ν C.s C.A = S.preμ udir ν D.s D.A := by
  classical
  -- Get a common upper bound m for C.s ∪ D.s
  rcases S.upperBound_finset udir (C.s ∪ D.s) with ⟨m, hm⟩
  have hms : ∀ i ∈ C.s, S.le i m := fun i hi => hm i (Finset.mem_union_left _ hi)
  have hmt : ∀ i ∈ D.s, S.le i m := fun i hi => hm i (Finset.mem_union_right _ hi)
  -- Rewrite each preμ as preμAt at m
  rw [S.preμ_eq udir ν compat C.s C.A C.hA hms,
      S.preμ_eq udir ν compat D.s D.A D.hA hmt]
  simp only [preμAt]
  -- The constraint sets at m
  set Ec : Set (S.q m).Outcome :=
    {o | ∀ (i : S.ι) (hi : i ∈ C.s), (S.π (hms i hi)).π o ∈ C.A i} with hEc_def
  set Ed : Set (S.q m).Outcome :=
    {o | ∀ (i : S.ι) (hi : i ∈ D.s), (S.π (hmt i hi)).π o ∈ D.A i} with hEd_def
  -- C.set = Cyl m Ec, D.set = Cyl m Ed (by finCyl_eq_cyl_of_upperBound)
  have hCc : C.set = S.Cyl m Ec := S.finCyl_eq_cyl_of_upperBound hms
  have hDd : D.set = S.Cyl m Ed := S.finCyl_eq_cyl_of_upperBound hmt
  -- So Cyl m Ec = Cyl m Ed from hEq
  have hCylEq : S.Cyl m Ec = S.Cyl m Ed := by rw [← hCc, ← hDd]; exact hEq
  -- Cyl m E = eval m ⁻¹' E by definition, so preimage equality holds
  have hPreEq : S.eval m ⁻¹' Ec = S.eval m ⁻¹' Ed := by
    have hEc_rfl : S.eval m ⁻¹' Ec = S.Cyl m Ec := rfl
    have hEd_rfl : S.eval m ⁻¹' Ed = S.Cyl m Ed := rfl
    rw [hEc_rfl, hEd_rfl, hCylEq]
  -- Surjectivity of eval m gives Ec = Ed
  have hEcEd : Ec = Ed := Set.preimage_injective.mpr (surj m) hPreEq
  -- Therefore ν m Ec = ν m Ed
  rw [hEcEd]

/-- **`CylGen` is a set semiring under `UpperDirected`.**

    - `empty_mem`: `∅ = Cyl i ∅` for any `i`.
    - `inter_mem`: two cylinders intersect to a cylinder (the π-system property, plus
      empty-case handling).
    - `diff_eq_sUnion'`: `Cyl i A \ Cyl j B = Cyl k ((π hik)⁻¹ A ∩ ((π hjk)⁻¹ B)ᶜ)`,
      witnessed by a singleton finset, where k is finer than both i and j. -/
lemma isSetSemiring_CylGen [Nonempty S.ι] (udir : S.UpperDirected) :
    IsSetSemiring S.CylGen := by
  refine ⟨?_, ?_, ?_⟩
  · -- empty_mem
    obtain ⟨i⟩ := ‹Nonempty S.ι›
    exact ⟨i, ∅, MeasurableSet.empty, by ext ω; simp [Cyl, eval]⟩
  · -- inter_mem: closed under intersection (delegate to isPiSystem_CylGen; handle ∅ case)
    intro s hs t ht
    by_cases hne : s ∩ t = ∅
    · obtain ⟨i⟩ := ‹Nonempty S.ι›
      rw [hne]; exact ⟨i, ∅, MeasurableSet.empty, by ext ω; simp [Cyl, eval]⟩
    · exact S.isPiSystem_CylGen udir s hs t ht (Set.nonempty_iff_ne_empty.mpr hne)
  · -- diff_eq_sUnion': Cyl i A \ Cyl j B = Cyl k ((π hik)⁻¹ A ∩ ((π hjk)⁻¹ B)ᶜ)
    -- where k is finer than both i and j (upper-directedness)
    intro s hs t ht
    rcases hs with ⟨i, A, hA, rfl⟩
    rcases ht with ⟨j, B, hB, rfl⟩
    rcases udir i j with ⟨k, hik, hjk⟩
    let E := (S.π hik).π ⁻¹' A ∩ ((S.π hjk).π ⁻¹' B)ᶜ
    have hE : MeasurableSet E :=
      (hA.preimage (S.π hik).measurable_π).inter
        (hB.preimage (S.π hjk).measurable_π).compl
    have hdiff : S.Cyl i A \ S.Cyl j B = S.Cyl k E := by
      rw [S.cyl_refine hik A, S.cyl_refine hjk B]
      ext ω; simp [Cyl, eval, E, Set.mem_diff, Set.mem_compl_iff]
    exact ⟨{S.Cyl k E},
      fun x hx => by simp only [Finset.coe_singleton, Set.mem_singleton_iff] at hx
                     exact hx ▸ ⟨k, E, hE, rfl⟩,
      by simp [Set.PairwiseDisjoint, Set.pairwise_singleton],
      by simp [hdiff]⟩

/-- **Finite additivity for `preμ` on disjoint finite-cylinder presentations.**

    If two measurable finite cylinders `C` and `D` have disjoint sets, and their
    union is presented by a third measurable finite cylinder `U`, then
    `U.mass = C.mass + D.mass`.

    **Proof strategy:** Compress all three to a common upper bound `m`. Each becomes
    a measurable subset of `Outcome_m` via `finCyl_eq_cyl_of_upperBound`. Disjointness
    and union equality at the `Omega` level pull back (via `surj m`) to disjointness
    and union equality in `Outcome_m`. Then `ν m` additivity gives the result. -/
lemma preμ_disjoint_union
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν)
    (surj : S.EvalSurjective)
    (C D U : S.MeasFinCyl)
    (hDisj : Disjoint C.set D.set)
    (hUnion : U.set = C.set ∪ D.set) :
    S.preμ udir ν U.s U.A = S.preμ udir ν C.s C.A + S.preμ udir ν D.s D.A := by
  classical
  -- Get a common upper bound m for all three index sets
  rcases S.upperBound_finset udir (C.s ∪ D.s ∪ U.s) with ⟨m, hm⟩
  have hmC : ∀ i ∈ C.s, S.le i m := fun i hi => hm i (by simp [hi])
  have hmD : ∀ i ∈ D.s, S.le i m := fun i hi => hm i (by simp [hi])
  have hmU : ∀ i ∈ U.s, S.le i m := fun i hi => hm i (by simp [hi])
  -- Rewrite each preμ as preμAt at m
  rw [S.preμ_eq udir ν compat C.s C.A C.hA hmC,
      S.preμ_eq udir ν compat D.s D.A D.hA hmD,
      S.preμ_eq udir ν compat U.s U.A U.hA hmU]
  simp only [preμAt]
  -- The constraint sets at m
  set Ec : Set (S.q m).Outcome :=
    {o | ∀ (i : S.ι) (hi : i ∈ C.s), (S.π (hmC i hi)).π o ∈ C.A i} with hEc_def
  set Ed : Set (S.q m).Outcome :=
    {o | ∀ (i : S.ι) (hi : i ∈ D.s), (S.π (hmD i hi)).π o ∈ D.A i} with hEd_def
  set Eu : Set (S.q m).Outcome :=
    {o | ∀ (i : S.ι) (hi : i ∈ U.s), (S.π (hmU i hi)).π o ∈ U.A i} with hEu_def
  -- Cylinder compressions
  have hCc : C.set = S.Cyl m Ec := S.finCyl_eq_cyl_of_upperBound hmC
  have hDd : D.set = S.Cyl m Ed := S.finCyl_eq_cyl_of_upperBound hmD
  have hUu : U.set = S.Cyl m Eu := S.finCyl_eq_cyl_of_upperBound hmU
  -- Measurability of constraint sets
  have hEc : MeasurableSet Ec := S.measurableSet_constraintAt C.A C.hA C.s (fun _ h => h) m hmC
  have hEd : MeasurableSet Ed := S.measurableSet_constraintAt D.A D.hA D.s (fun _ h => h) m hmD
  -- Surjectivity: Cyl m E = eval m ⁻¹' E, so equality of cylinders → equality of preimages
  -- → (by surjectivity) equality of sets in Outcome_m
  have inj_eval : Function.Injective (S.eval m ⁻¹' ·) :=
    Set.preimage_injective.mpr (surj m)
  -- Disjointness: Ec ∩ Ed = ∅
  have hDisjEcEd : Disjoint Ec Ed := by
    rw [Set.disjoint_iff_inter_eq_empty]
    apply inj_eval
    simp only [Set.preimage_inter, Set.preimage_empty]
    -- eval m ⁻¹' (Ec ∩ Ed) = eval m ⁻¹' Ec ∩ eval m ⁻¹' Ed
    -- = C.set ∩ D.set = ∅
    have : S.eval m ⁻¹' Ec = C.set := hCc.symm
    have : S.eval m ⁻¹' Ed = D.set := hDd.symm
    rw [‹S.eval m ⁻¹' Ec = C.set›, ‹S.eval m ⁻¹' Ed = D.set›]
    exact Set.disjoint_iff_inter_eq_empty.mp hDisj
  -- Union: Eu = Ec ∪ Ed
  have hUnionEcEd : Eu = Ec ∪ Ed := by
    apply inj_eval
    simp only [Set.preimage_union]
    -- eval m ⁻¹' Ex = Cyl m Ex = X.set by definition
    change S.Cyl m Eu = S.Cyl m Ec ∪ S.Cyl m Ed
    rw [← hCc, ← hDd, ← hUu]
    exact hUnion
  -- ν m additivity
  rw [hUnionEcEd, measure_union hDisjEcEd hEd]

/-!
## Extension infrastructure (Stage 3): AddContent and Carathéodory construction

With `preμ_respects_finCyl_eq` and `preμ_disjoint_union` established, we can:

1. Define `cylGen_addContent`: an `AddContent` on `CylGen` using `preμ` as the mass function,
   choosing a presentation for each element of `CylGen` and using well-definedness.

2. Apply `AddContent.measure` (Carathéodory) to obtain a `Measure S.Omega` from the content.

3. Package everything into `observational_extension_of_evalSurjective`, which asserts the
   existence and uniqueness of a measure `P` on `Omega` with the correct marginals.

**Alignment note:** This theorem carries the `EvalSurjective` hypothesis which is not present
in note.tex.  It is an intermediate formal milestone; the gap should be closed in future work.
-/

/-- Helper: the mass of a `CylGen` element, defined by choosing a presentation.

    For `E = Cyl i A ∈ CylGen`, the mass is `preμAt ν (k := i) (hk := le_refl i) A_ext`
    where `A_ext j = if j = i then A else ∅`.  `preμ_respects_finCyl_eq` ensures this is
    independent of the presentation. -/
noncomputable def cylGenMass
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν)
    (E : Set S.Omega) (hE : E ∈ S.CylGen) : ℝ≥0∞ :=
  -- Choose a presentation from hE using Classical choice
  haveI : DecidableEq S.ι := Classical.decEq S.ι
  let i := hE.choose
  let A := hE.choose_spec.choose
  -- Package as a singleton MeasFinCyl and compute its mass
  S.preμ udir ν {i} (fun j => if h : j = i then h ▸ A else ∅)

/-- `cylGenMass` is well-defined: independent of the presentation chosen. -/
lemma cylGenMass_wellDef
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν)
    (E : Set S.Omega) (h₁ h₂ : E ∈ S.CylGen) :
    S.cylGenMass udir surj ν compat E h₁ = S.cylGenMass udir surj ν compat E h₂ := by
  -- cylGenMass uses Classical.choose which is proof-irrelevant (h₁ and h₂ yield the same choice)
  simp only [cylGenMass]

/-- Helper: the singleton FinCyl `{j}` with component `B` at `j` (and `∅` elsewhere)
    equals the cylinder `Cyl j B`. -/
private lemma finCyl_singleton_eq_cyl
    [DecidableEq S.ι]
    (j : S.ι) (B : Set ((S.q j).Outcome)) :
    S.FinCyl {j} (fun k => if h : k = j then h ▸ B else ∅) = S.Cyl j B := by
  have hk : ∀ k ∈ ({j} : Finset S.ι), S.le k j :=
    fun k hk => Finset.mem_singleton.mp hk ▸ S.le_refl j
  rw [S.finCyl_eq_cyl_of_upperBound hk]
  congr 1
  ext o
  simp only [Set.mem_setOf_eq, Finset.mem_singleton]
  have hπ_refl : (S.π (S.le_refl j)).π o = o := by
    have := congrFun (S.π_refl j) o; simp only [id] at this; exact this
  constructor
  · intro h; have h' := h j rfl; simp [dif_pos rfl, hπ_refl] at h'; exact h'
  · intro ho k hk
    have hkj : k = j := hk
    subst hkj
    simp [dif_pos rfl, hπ_refl, ho]

/-- **`cylGenMass` on an explicit cylinder equals the marginal.**

    For any measurable `A ⊆ (S.q i).Outcome`, `cylGenMass ... (Cyl i A) h = ν i A`.

    This is the key bridge between the `Classical.choose` definition and concrete
    marginal values.  It is the single lemma that unblocks all downstream sorrys. -/
lemma cylGenMass_eq_marginal
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν)
    (i : S.ι) (A : Set ((S.q i).Outcome)) (hA : MeasurableSet A) :
    S.cylGenMass udir surj ν compat (S.Cyl i A) ⟨i, A, hA, rfl⟩ = ν i A := by
  haveI : DecidableEq S.ι := Classical.decEq S.ι
  -- Route through preμ_respects_finCyl_eq to avoid reducing Classical.choose.
  -- cylGenMass uses the chosen presentation (i', A') from Classical.choose.
  -- We compare it to the explicit presentation (i, A) via equal set = Cyl i A.
  let hE : S.Cyl i A ∈ S.CylGen := ⟨i, A, hA, rfl⟩
  let i' : S.ι := hE.choose
  let A' : Set ((S.q i').Outcome) := hE.choose_spec.choose
  let hA'spec := hE.choose_spec.choose_spec
  -- Build the "chosen" MeasFinCyl: this is literally what cylGenMass computes
  let Achosen : ∀ j : S.ι, Set ((S.q j).Outcome) :=
    fun j => if h : j = i' then h ▸ A' else ∅
  let Cchosen : S.MeasFinCyl := ⟨{i'}, Achosen,
    fun j hj => by
      simp only [Finset.mem_singleton] at hj; subst hj
      simp only [Achosen, dif_pos rfl]; exact hA'spec.1⟩
  -- Build the explicit MeasFinCyl at (i, A)
  let Aexpl : ∀ j : S.ι, Set ((S.q j).Outcome) :=
    fun j => if h : j = i then h ▸ A else ∅
  let Cexpl : S.MeasFinCyl := ⟨{i}, Aexpl,
    fun j hj => by
      simp only [Finset.mem_singleton] at hj; subst hj
      simp only [Aexpl, dif_pos rfl]; exact hA⟩
  -- cylGenMass (...) = preμ of Cchosen, by definitional unfolding
  have hcylGen_eq : S.cylGenMass udir surj ν compat (S.Cyl i A) hE =
      S.preμ udir ν Cchosen.s Cchosen.A := rfl
  -- Cchosen.set = Cyl i A  (finCyl_singleton_eq_cyl + hA'spec.2)
  have hCchosen_set : Cchosen.set = S.Cyl i A := by
    show S.FinCyl {i'} Achosen = S.Cyl i A
    rw [S.finCyl_singleton_eq_cyl i' A']
    exact hA'spec.2.symm
  -- Cexpl.set = Cyl i A  (finCyl_singleton_eq_cyl)
  have hCexpl_set : Cexpl.set = S.Cyl i A :=
    S.finCyl_singleton_eq_cyl i A
  -- preμ(Cchosen) = preμ(Cexpl) since both sets equal Cyl i A
  have hpreμ_eq : S.preμ udir ν Cchosen.s Cchosen.A = S.preμ udir ν Cexpl.s Cexpl.A :=
    S.preμ_respects_finCyl_eq udir ν compat surj Cchosen Cexpl
      (hCchosen_set.trans hCexpl_set.symm)
  -- preμ(Cexpl) = ν i A via preμ_eq + preμAt_single_eq_marginal
  have hpreμ_expl : S.preμ udir ν Cexpl.s Cexpl.A = ν i A := by
    rw [S.preμ_eq udir ν compat {i} Aexpl
      (fun j hj => by
        simp only [Finset.mem_singleton] at hj; subst hj
        simp only [Aexpl, dif_pos rfl]; exact hA)
      (fun j hj => Finset.mem_singleton.mp hj ▸ S.le_refl j)]
    rw [S.preμAt_single_eq_marginal ν i Aexpl]
    simp only [Aexpl, dif_pos rfl]
  rw [hcylGen_eq, hpreμ_eq, hpreμ_expl]

/-- **`AddContent` on `CylGen` from the premeasure `preμ`.**

    For each `E ∈ CylGen`, use `cylGenMass` (which is presentation-independent via
    `preμ_respects_finCyl_eq`) as the mass.  Additivity follows from `preμ_disjoint_union`. -/
noncomputable def cylGen_addContent
    [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν) :
    AddContent ℝ≥0∞ S.CylGen where
  toFun E :=
    haveI : Decidable (E ∈ S.CylGen) := Classical.propDecidable _
    if h : E ∈ S.CylGen then S.cylGenMass udir surj ν compat E h else 0
  empty' := by
    -- ∅ ∈ CylGen (it equals Cyl i ∅ for any i), so dif_pos fires
    haveI : Decidable (∅ ∈ S.CylGen) := Classical.propDecidable _
    obtain ⟨i⟩ := ‹Nonempty S.ι›
    have hempty_mem : (∅ : Set S.Omega) ∈ S.CylGen :=
      ⟨i, ∅, MeasurableSet.empty, by ext ω; simp [Cyl, eval]⟩
    simp only [hempty_mem, dite_true]
    rw [S.cylGenMass_wellDef udir surj ν compat _ _ ⟨i, ∅, MeasurableSet.empty,
          by ext ω; simp [Cyl, eval]⟩]
    rw [S.cylGenMass_eq_marginal udir surj ν compat i ∅ MeasurableSet.empty]
    exact measure_empty
  sUnion' := by
    intro I hI_ss hI_dis hI_mem
    induction I using Finset.induction_on with
    | empty => simp
    | insert hnotmem ih =>
        rename_i t I'
        rw [Finset.coe_insert, Set.sUnion_insert]
        have ht_mem : t ∈ S.CylGen := hI_ss (Finset.mem_coe.mpr (Finset.mem_insert_self t I'))
        have hI'_ss : ↑I' ⊆ S.CylGen := fun x hx =>
          hI_ss (Finset.mem_coe.mpr (Finset.mem_insert_of_mem (Finset.mem_coe.mp hx)))
        have hI'_dis : PairwiseDisjoint (↑I' : Set (Set S.Omega)) id :=
          hI_dis.subset (by simp [Finset.coe_insert, Set.subset_insert])
        have hI'_mem : ⋃₀ ↑I' ∈ S.CylGen := by
          by_cases hne : I' = ∅
          · simp [hne]; obtain ⟨i⟩ := ‹Nonempty S.ι›
            exact ⟨i, ∅, MeasurableSet.empty, by ext ω; simp [Cyl, eval]⟩
          · have hfull_mem : ⋃₀ ↑(insert t I') ∈ S.CylGen := by
              rw [Finset.coe_insert]; exact hI_mem
            have hfull_eq : ⋃₀ ↑(insert t I') = t ∪ ⋃₀ ↑I' := by
              simp [Finset.coe_insert, Set.sUnion_insert]
            have hdisj_t : Disjoint t (⋃₀ ↑I') := by
              rw [Set.disjoint_sUnion_right]
              intro s hs
              exact hI_dis (Finset.mem_coe.mpr (Finset.mem_insert_self t I'))
                (Finset.mem_coe.mpr (Finset.mem_insert_of_mem (Finset.mem_coe.mp hs)))
                (fun heq => hnotmem (heq ▸ Finset.mem_coe.mp hs))
            have hunion_eq : ⋃₀ ↑I' = (t ∪ ⋃₀ ↑I') \ t := by
              rw [Set.union_diff_cancel_left (Set.disjoint_left.mp hdisj_t.symm)]
            rw [hunion_eq, ← hfull_eq]
            exact (S.isSetSemiring_CylGen udir).diff_mem hfull_mem ht_mem |>.choose_spec.1
              (Finset.mem_coe.mpr (Finset.mem_insert_self _ _))
        have hdisj_t_union : Disjoint t (⋃₀ ↑I') := by
          rw [Set.disjoint_sUnion_right]
          intro s hs
          exact hI_dis (Finset.mem_coe.mpr (Finset.mem_insert_self t I'))
            (Finset.mem_coe.mpr (Finset.mem_insert_of_mem (Finset.mem_coe.mp hs)))
            (fun heq => hnotmem (heq ▸ Finset.mem_coe.mp hs))
        have ih' := ih hI'_ss hI'_dis hI'_mem
        haveI : Decidable (t ∈ S.CylGen) := Classical.propDecidable _
        haveI : Decidable (⋃₀ ↑I' ∈ S.CylGen) := Classical.propDecidable _
        haveI : Decidable ((t ∪ ⋃₀ ↑I') ∈ S.CylGen) := Classical.propDecidable _
        have hval_t : (if h : t ∈ S.CylGen then S.cylGenMass udir surj ν compat t h else 0) =
            S.cylGenMass udir surj ν compat t ht_mem := dif_pos ht_mem
        have hval_union : (if h : ⋃₀ ↑I' ∈ S.CylGen then S.cylGenMass udir surj ν compat _ h else 0) =
            S.cylGenMass udir surj ν compat _ hI'_mem := dif_pos hI'_mem
        have hval_full : (if h : (t ∪ ⋃₀ ↑I') ∈ S.CylGen then S.cylGenMass udir surj ν compat _ h else 0) =
            S.cylGenMass udir surj ν compat _ hI_mem := dif_pos hI_mem
        rcases ht_mem with ⟨it, At, hAt, rfl⟩
        rcases hI'_mem with ⟨iu, Au, hAu, rfl⟩
        rcases hI_mem with ⟨iU, AU, hAU, hUeq⟩
        let Ct : S.MeasFinCyl := ⟨{it}, fun j => if h : j = it then h ▸ At else ∅,
          fun j hj => by simp [Finset.mem_singleton] at hj; subst hj; simpa using hAt⟩
        let Cu : S.MeasFinCyl := ⟨{iu}, fun j => if h : j = iu then h ▸ Au else ∅,
          fun j hj => by simp [Finset.mem_singleton] at hj; subst hj; simpa using hAu⟩
        let CU : S.MeasFinCyl := ⟨{iU}, fun j => if h : j = iU then h ▸ AU else ∅,
          fun j hj => by simp [Finset.mem_singleton] at hj; subst hj; simpa using hAU⟩
        have hCt_set : Ct.set = S.Cyl it At := S.finCyl_singleton_eq_cyl it At
        have hCu_set : Cu.set = S.Cyl iu Au := S.finCyl_singleton_eq_cyl iu Au
        have hCU_set : CU.set = S.Cyl iU AU := S.finCyl_singleton_eq_cyl iU AU
        have hmt : S.cylGenMass udir surj ν compat (S.Cyl it At) ⟨it, At, hAt, rfl⟩ =
            ν it At := S.cylGenMass_eq_marginal udir surj ν compat it At hAt
        have hmu : S.cylGenMass udir surj ν compat (S.Cyl iu Au) ⟨iu, Au, hAu, rfl⟩ =
            ν iu Au := S.cylGenMass_eq_marginal udir surj ν compat iu Au hAu
        have hmU : S.cylGenMass udir surj ν compat (S.Cyl iU AU) ⟨iU, AU, hAU, rfl⟩ =
            ν iU AU := S.cylGenMass_eq_marginal udir surj ν compat iU AU hAU
        have hUnionCD : CU.set = Ct.set ∪ Cu.set := by
          rw [hCt_set, hCu_set, hCU_set, ← hUeq]
        have hDisjCD : Disjoint Ct.set Cu.set := by
          rw [hCt_set, hCu_set]; exact hdisj_t_union
        have hpreμ := S.preμ_disjoint_union udir ν compat surj Ct Cu CU hDisjCD hUnionCD
        simp only [Finset.sum_insert hnotmem]
        rw [hval_full, hval_t]
        rw [← ih']
        conv_lhs => rw [S.cylGenMass_wellDef udir surj ν compat _ ⟨iU, AU, hAU, rfl⟩ ⟨iU, AU, hAU, rfl⟩]
        rw [hmU]
        rw [S.cylGenMass_wellDef udir surj ν compat _ ⟨it, At, hAt, rfl⟩ ⟨it, At, hAt, rfl⟩]
        rw [hmt]
        rw [hval_union, S.cylGenMass_wellDef udir surj ν compat _ ⟨iu, Au, hAu, rfl⟩ ⟨iu, Au, hAu, rfl⟩]
        rw [hmu]
        have hpCt : S.preμ udir ν Ct.s Ct.A = ν it At := by
          rw [S.preμ_eq udir ν compat {it} Ct.A
            (fun j hj => by simp [Finset.mem_singleton] at hj; subst hj; simpa using hAt)
            (fun j hj => Finset.mem_singleton.mp hj ▸ S.le_refl j)]
          rw [S.preμAt_single_eq_marginal ν it Ct.A]
          simp [Ct, dif_pos rfl]
        have hpCu : S.preμ udir ν Cu.s Cu.A = ν iu Au := by
          rw [S.preμ_eq udir ν compat {iu} Cu.A
            (fun j hj => by simp [Finset.mem_singleton] at hj; subst hj; simpa using hAu)
            (fun j hj => Finset.mem_singleton.mp hj ▸ S.le_refl j)]
          rw [S.preμAt_single_eq_marginal ν iu Cu.A]
          simp [Cu, dif_pos rfl]
        have hpCU : S.preμ udir ν CU.s CU.A = ν iU AU := by
          rw [S.preμ_eq udir ν compat {iU} CU.A
            (fun j hj => by simp [Finset.mem_singleton] at hj; subst hj; simpa using hAU)
            (fun j hj => Finset.mem_singleton.mp hj ▸ S.le_refl j)]
          rw [S.preμAt_single_eq_marginal ν iU CU.A]
          simp [CU, dif_pos rfl]
        linarith [hpreμ.symm.trans (by rw [hpCt, hpCu])]

/-- `SequentiallyUpperDirected` implies `UpperDirected`.

    **Proof:** For any pair `i j`, apply `SequentiallyUpperDirected` to the sequence
    `n ↦ if n = 0 then i else j` to obtain a common upper bound `k`. -/
lemma sequentiallyUpperDirected_implies_upperDirected
    (sudir : S.SequentiallyUpperDirected) : S.UpperDirected := by
  intro i j
  rcases sudir (fun n => if n = 0 then i else j) with ⟨k, hk⟩
  have h0 : S.le i k := by have := hk 0; simpa using this
  have h1 : S.le j k := by have := hk 1; simpa using this
  exact ⟨k, h0, h1⟩

/-- **Sequential cylinder compression.**

    Given a sequence of cylinders `f n = Cyl (u n) (A n) ∈ CylGen` and a cylinder
    `g = Cyl k B ∈ CylGen`, if `m` is a common upper bound for the sequence `n ↦ u n`
    and for `k` (i.e., `∀ n, le (u n) m` and `le k m`), then:

    - Each `f n = Cyl m (Eₙ)` where `Eₙ = (π h_n_m).π ⁻¹' A n`
    - `g = Cyl m E` where `E = (π h_k_m).π ⁻¹' B`

    and the sets `Eₙ, E` are all at level `m`, allowing comparison via `ν m`. -/
lemma cyl_refine_to_upper_bound
    {u : ℕ → S.ι} {A : ∀ n, Set ((S.q (u n)).Outcome)} {k : S.ι}
    {B : Set ((S.q k).Outcome)} {m : S.ι}
    (hum : ∀ n, S.le (u n) m)
    (hkm : S.le k m) :
    (∀ n, S.Cyl (u n) (A n) = S.Cyl m ((S.π (hum n)).π ⁻¹' A n)) ∧
    (S.Cyl k B = S.Cyl m ((S.π hkm).π ⁻¹' B)) := by
  exact ⟨fun n => S.cyl_refine (hum n) (A n), S.cyl_refine hkm B⟩

/-- **σ-subadditivity of `cylGen_addContent`** (under `SequentiallyUpperDirected`).

    **Proof strategy:** Given a sequence `f n ∈ CylGen` with `⋃ n, f n ∈ CylGen`:
    1. Write `f n = Cyl (u n) (A n)` and `⋃ n, f n = Cyl k B`.
    2. Use `SequentiallyUpperDirected` on `n ↦ (if n = 0 then k else u (n-1))` to find a
       common upper bound `m` of k and all `u n`.
    3. Compress all cylinders to level m via `cyl_refine`: `f n = Cyl m Eₙ`, `⋃ f n = Cyl m E`.
    4. By surjectivity of `eval m`: from the set equality in `Omega` deduce `E = ⋃ n, Eₙ` in `Outcome_m`.
    5. The content value on each is: `content (f n) = ν m Eₙ` and `content (⋃ f n) = ν m E`.
    6. `ν m E = ν m (⋃ n, Eₙ) ≤ ∑' n, ν m Eₙ` by σ-subadditivity of the measure `ν m`. -/
lemma cylGen_addContent_isSigmaSubadditive
    [Nonempty S.ι]
    (sudir : S.SequentiallyUpperDirected)
    (surj : S.EvalSurjective)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν) :
    (S.cylGen_addContent (S.sequentiallyUpperDirected_implies_upperDirected sudir) surj ν compat).IsSigmaSubadditive := by
  -- Unfold IsSigmaSubadditive
  let udir := S.sequentiallyUpperDirected_implies_upperDirected sudir
  intro f hf hfU
  -- Step 1: Extract cylinder presentations
  -- For each n, write f n = Cyl (u n) (A n) with A n measurable
  choose u A hAmeas hfEq using fun n => hf n
  -- Write ⋃ f = Cyl k B with B measurable
  -- Save hfU membership before destructuring for use in content computation
  have hmem_U : (⋃ n, f n) ∈ S.CylGen := hfU
  obtain ⟨k, B, hBmeas, hfUEq⟩ := hfU
  -- Step 2: Common upper bound m for all u n and k
  -- Apply SequentiallyUpperDirected to the sequence: n ↦ if n = 0 then k else u (n-1)
  rcases sudir (fun n => Nat.casesOn n k u) with ⟨m, hm⟩
  have hkm : S.le k m := hm 0
  have hum : ∀ n, S.le (u n) m := fun n => hm (n + 1)
  -- Step 3: Compress all cylinders to level m
  -- f n = Cyl (u n) (A n) = Cyl m (Eₙ) where Eₙ = (π h_um_n)⁻¹(A n)
  -- ⋃ f = Cyl k B = Cyl m E where E = (π h_km)⁻¹(B)
  let E : Set (S.q m).Outcome := (S.π hkm).π ⁻¹' B
  let En : ℕ → Set (S.q m).Outcome := fun n => (S.π (hum n)).π ⁻¹' A n
  have hfn_eq : ∀ n, f n = S.Cyl m (En n) := by
    intro n
    rw [hfEq n]
    exact S.cyl_refine (hum n) (A n)
  have hfU_eq : ⋃ n, f n = S.Cyl m E := by
    rw [hfUEq]
    exact S.cyl_refine hkm B
  -- Step 4: Deduce E = ⋃ n, Eₙ in Outcome_m via surjectivity
  have hE_eq_iUnion : E = ⋃ n, En n := by
    apply Set.preimage_injective.mpr (surj m)
    -- eval m ⁻¹' E = Cyl m E = ⋃ n, f n = ⋃ n, Cyl m (En n) = ⋃ n, eval m ⁻¹' (En n)
    -- Note: Cyl m X = eval m ⁻¹' X by definition, so preimage and Cyl are definitionally equal
    have hL : S.eval m ⁻¹' E = ⋃ n, f n := by
      change S.Cyl m E = ⋃ n, f n
      rw [← hfU_eq]
    have hR : ∀ n, S.eval m ⁻¹' En n = f n := by
      intro n
      change S.Cyl m (En n) = f n
      rw [← hfn_eq n]
    rw [Set.preimage_iUnion]
    simp only [hR, hL]
  -- Step 5: Content values via cylGenMass at level m
  -- content (⋃ f) = ν m E
  -- content (f n) = ν m (En n)
  have hmem_n : ∀ n, f n ∈ S.CylGen := hf
  -- content (⋃ f) = ν m E
  have hcontent_U : S.cylGen_addContent udir surj ν compat (⋃ n, f n) = ν m E := by
    -- Rewrite ⋃ n, f n = S.Cyl k B using hfUEq, then apply cylGenMass_eq_marginal
    have hkB_mem : S.Cyl k B ∈ S.CylGen := ⟨k, B, hBmeas, rfl⟩
    have heq_sets : (⋃ n, f n) = S.Cyl k B := hfUEq
    have hkB_eq : S.cylGen_addContent udir surj ν compat (S.Cyl k B) = ν k B := by
      show (S.cylGen_addContent udir surj ν compat).toFun (S.Cyl k B) = ν k B
      simp only [cylGen_addContent, hkB_mem, dite_true]
      rw [S.cylGenMass_wellDef udir surj ν compat _ _ hkB_mem]
      exact S.cylGenMass_eq_marginal udir surj ν compat k B hBmeas
    calc S.cylGen_addContent udir surj ν compat (⋃ n, f n)
        = S.cylGen_addContent udir surj ν compat (S.Cyl k B) := by rw [heq_sets]
      _ = ν k B := hkB_eq
      _ = ν m E := S.compat_apply_preimage compat hkm B hBmeas
  -- content (f n) = ν m (En n)
  have hcontent_n : ∀ n, S.cylGen_addContent udir surj ν compat (f n) = ν m (En n) := by
    intro n
    -- Rewrite f n = S.Cyl (u n) (A n) using hfEq n, then apply cylGenMass_eq_marginal
    have hun_mem : S.Cyl (u n) (A n) ∈ S.CylGen := ⟨u n, A n, hAmeas n, rfl⟩
    have heq_sets : f n = S.Cyl (u n) (A n) := hfEq n
    have hun_eq : S.cylGen_addContent udir surj ν compat (S.Cyl (u n) (A n)) = ν (u n) (A n) := by
      show (S.cylGen_addContent udir surj ν compat).toFun (S.Cyl (u n) (A n)) = ν (u n) (A n)
      simp only [cylGen_addContent, hun_mem, dite_true]
      rw [S.cylGenMass_wellDef udir surj ν compat _ _ hun_mem]
      exact S.cylGenMass_eq_marginal udir surj ν compat (u n) (A n) (hAmeas n)
    calc S.cylGen_addContent udir surj ν compat (f n)
        = S.cylGen_addContent udir surj ν compat (S.Cyl (u n) (A n)) := by rw [heq_sets]
      _ = ν (u n) (A n) := hun_eq
      _ = ν m (En n) := S.compat_apply_preimage compat (hum n) (A n) (hAmeas n)
  -- Step 6: σ-subadditivity of ν m
  rw [hcontent_U, hE_eq_iUnion]
  have hEn_meas : ∀ n, MeasurableSet (En n) := by
    intro n
    exact (hAmeas n).preimage (S.π (hum n)).measurable_π
  calc ν m (⋃ n, En n)
      ≤ ∑' n, ν m (En n) := measure_iUnion_le (μ := ν m) En
    _ = ∑' n, S.cylGen_addContent udir surj ν compat (f n) := by
        congr 1; ext n; rw [hcontent_n n]

/-- **Observational Extension Theorem.**

    Under compatible marginals, sequential upper-directedness (`SequentiallyUpperDirected`),
    and realizability (`EvalSurjective`), there exists a unique probability measure `P`
    on `Omega` whose pushforwards recover the given compatible marginal family.

    **Hypotheses vs. note.tex:**
    - `sudir : SequentiallyUpperDirected` — the analytic hypothesis: every sequence of
      queries has a common refinement. Implies `UpperDirected`. In the classical setting this
      is implied by compactness of factor spaces or Polish topology; here it is stated explicitly.
    - `compat : CompatibleMarginals` — present in note.tex
    - `surj : EvalSurjective` — realizability condition; not in note.tex (alignment gap)

    **Proof structure:**
    1. `udir` from `sequentiallyUpperDirected_implies_upperDirected sudir`
    2. `cylGen_addContent` — `AddContent ℝ≥0∞ S.CylGen`
    3. `isSetSemiring_CylGen` — semiring structure on `CylGen`
    4. `cylGen_addContent_isSigmaSubadditive` — σ-subadditivity via `SequentiallyUpperDirected`
    5. `AddContent.measure` — Carathéodory measure `P`
    6. `AddContent.measure_eq` — `P (Cyl i A) = ν i A` on generator sets
    7. Marginal recovery: `map (eval i) P = ν i` via `measure_eq` + `map_apply_eval_eq_cyl`
    8. `IsProbabilityMeasure`: `P univ = 1` via `measure_eq` on `Cyl i univ = univ`
    9. Uniqueness: `observational_determination` -/
theorem observational_extension
    [Nonempty S.ι]
    (sudir : S.SequentiallyUpperDirected)
    (surj : S.EvalSurjective)
    (ν : ∀ i : S.ι, Measure ((S.q i).Outcome))
    (compat : S.CompatibleMarginals ν)
    [∀ i, IsProbabilityMeasure (ν i)] :
    ∃! P : Measure S.Omega,
      IsProbabilityMeasure P ∧
      ∀ i : S.ι, Measure.map (S.eval i) P = ν i := by
  -- Step 1: Derive UpperDirected from SequentiallyUpperDirected
  let udir := S.sequentiallyUpperDirected_implies_upperDirected sudir
  -- Step 2: Build the additive content
  let content := S.cylGen_addContent udir surj ν compat
  -- Step 3: Set semiring structure
  have hSR : IsSetSemiring S.CylGen := S.isSetSemiring_CylGen udir
  -- Step 4: σ-subadditivity via SequentiallyUpperDirected
  have hsubadd : content.IsSigmaSubadditive :=
    S.cylGen_addContent_isSigmaSubadditive sudir surj ν compat
  -- Step 5: Carathéodory extension
  -- sigmaQ = generateFrom CylGen by definition
  have hgen : S.sigmaQ = MeasurableSpace.generateFrom S.CylGen := rfl
  let P := content.measure hSR hgen.le hsubadd
  -- Step 6: P agrees with content on CylGen sets
  have hmeas_eq : ∀ {s : Set S.Omega}, s ∈ S.CylGen → P s = content s :=
    fun hs => content.measure_eq hSR hgen hsubadd hs
  -- Step 7: Marginal recovery
  have hmarginals : ∀ i : S.ι, Measure.map (S.eval i) P = ν i := by
    intro i
    ext A hA
    rw [Measure.map_apply (S.measurable_eval i) hA]
    -- P (eval i ⁻¹' A) = P (Cyl i A) = content (Cyl i A) = ν i A
    have hcyl_mem : S.Cyl i A ∈ S.CylGen := ⟨i, A, hA, rfl⟩
    rw [show S.eval i ⁻¹' A = S.Cyl i A from rfl, hmeas_eq hcyl_mem]
    -- content (Cyl i A) = cylGenMass ... = ν i A
    show (S.cylGen_addContent udir surj ν compat).toFun (S.Cyl i A) = ν i A
    simp only [cylGen_addContent, hcyl_mem, dite_true]
    rw [S.cylGenMass_wellDef udir surj ν compat _ _ ⟨i, A, hA, rfl⟩]
    exact S.cylGenMass_eq_marginal udir surj ν compat i A hA
  -- Step 8: IsProbabilityMeasure — P univ = 1
  have hprob : IsProbabilityMeasure P := by
    constructor
    obtain ⟨i⟩ := ‹Nonempty S.ι›
    -- univ = Cyl i univ
    have huniv_eq : (Set.univ : Set S.Omega) = S.Cyl i Set.univ := by
      ext ω; simp [QuerySystem.Cyl, QuerySystem.eval]
    rw [huniv_eq]
    have hcyl_univ : S.Cyl i Set.univ ∈ S.CylGen :=
      ⟨i, Set.univ, MeasurableSet.univ, rfl⟩
    rw [hmeas_eq hcyl_univ]
    -- content (Cyl i univ) = ν i univ = 1
    show (S.cylGen_addContent udir surj ν compat).toFun (S.Cyl i Set.univ) = 1
    simp only [cylGen_addContent, hcyl_univ, dite_true]
    rw [S.cylGenMass_wellDef udir surj ν compat _ _ ⟨i, Set.univ, MeasurableSet.univ, rfl⟩]
    rw [S.cylGenMass_eq_marginal udir surj ν compat i Set.univ MeasurableSet.univ]
    exact IsProbabilityMeasure.measure_univ
  -- Step 9: Uniqueness via observational_determination
  refine ⟨P, ⟨hprob, hmarginals⟩, fun P' ⟨hP'prob, hP'marg⟩ => ?_⟩
  exact S.observational_determination udir P' P
    (fun i => by rw [hP'marg i, hmarginals i])

end QuerySystem
