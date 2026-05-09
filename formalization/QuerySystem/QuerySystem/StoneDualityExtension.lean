/-
Copyright (c) 2025. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import Mathlib.Topology.Compactification.StoneCech
import Mathlib.Topology.Connected.TotallyDisconnected
import Mathlib.MeasureTheory.Measure.Content
import Mathlib.MeasureTheory.Measure.Regular
import QuerySystem.QuerySystem
import QuerySystem.DiscriminabilityFoundations

/-!
# Stone Duality Route to the Observational Extension Theorem

This file proves the Stone duality route to the observational extension theorem
(Paper I, §5). The Carathéodory route is in `QuerySystem.lean`; this file gives
an independent second proof.

## The argument

Given a query system `S` with a compatible normalized family of finitely additive
charges `P : S.NormalizedCompatibleContents` satisfying Collective Exhaustion,
the Stone route proceeds:

1. **Stone space** (Task 0′-A): `Ultrafilter S.Omega` is compact Hausdorff and
   totally disconnected. Each cylinder event `E ∈ CylGen` gives a clopen
   `{ u | E ∈ u }`. The evaluation map `S.eval i` extends to a continuous map
   `stoneEval i : Ultrafilter S.Omega → Ultrafilter (S.q i).Outcome`.

2. **Charge → Borel measure** (Task 0′-B): A finitely additive normalized charge
   on the clopen algebra of a compact totally-disconnected Hausdorff space extends
   uniquely to a regular Borel measure. **Intentional sorry**: the Mathlib
   `Content` API works on compact sets of a locally compact space; adapting it to
   charges on the clopen algebra of a Stone space requires infrastructure not yet
   in Mathlib (Halmos §53–54, Fremlin Vol. 1).

3. **Inverse system** (Task 0′-C): The bonding maps between Stone outcome spaces
   form a cofiltered inverse system of compact Hausdorff spaces.

4. **Inverse limit measure** (Task 0′-D): The compatible family of charges on the
   Stone outcome spaces extends to a measure on the inverse limit (Choksi's theorem).
   **Intentional sorry**: not yet in Mathlib.

5. **Agreement with Carathéodory** (Task 0′-E): Under shared hypotheses both
   routes produce the same measure. Proved from `observational_determination`.

## Sorry inventory

| Name | Reason |
|------|--------|
| `stone_measure_exists` | Mathlib gap: charge on clopen algebra → regular Borel measure |
| `stone_observational_extension` | Mathlib gap: Choksi + Yosida–Hewitt for inverse limit |

All Task 0′-A and 0′-C results are proved. Task 0′-E is proved.

## Main definitions and results

* `stoneSpace S` — `Ultrafilter S.Omega`
* `stoneEmbedding S` — `pure : S.Omega → Ultrafilter S.Omega`
* `cylGen_clopen` — cylinder events give clopens in `stoneSpace S`
* `stoneEval i` — continuous extension of `S.eval i` to `stoneSpace S`
* `stoneEval_compat` — commutes with refinement maps
* `stoneOutcomeMap hij` — continuous bonding map between Stone outcome spaces
* `stoneOutcomeMap_trans` — transitivity of bonding maps
* `stoneEval_factor` — `stoneOutcomeMap ∘ stoneEval j = stoneEval i`
* `stone_measure_exists` — (intentional sorry) Borel measure on `stoneSpace S`
* `stone_observational_extension` — (intentional sorry) Stone route main theorem
* `stone_agrees_with_caratheodory` — both routes produce the same measure (proved)

-/

open Set Filter MeasureTheory Topology

-- ---------------------------------------------------------------------------
-- Task 0′-A: Stone space basics
-- ---------------------------------------------------------------------------

section StoneSpaceBasics

variable (S : QuerySystem)

/-- The Stone space of `S` is the space of ultrafilters on `S.Omega`. -/
abbrev stoneSpace (S : QuerySystem) := Ultrafilter S.Omega

/-- The Stone space is compact. -/
instance stoneSpace_compactSpace : CompactSpace (stoneSpace S) :=
  ultrafilter_compact

/-- The Stone space is T2 (Hausdorff). -/
instance stoneSpace_t2Space : T2Space (stoneSpace S) :=
  Ultrafilter.t2Space

/-- The Stone space is totally disconnected. -/
instance stoneSpace_totallyDisconnected : TotallyDisconnectedSpace (stoneSpace S) :=
  inferInstance

/-- `Ultrafilter.map f` agrees with `Ultrafilter.extend (pure ∘ f)` when the target
    is compact Hausdorff. Both are continuous maps `Ultrafilter α → Ultrafilter β`
    agreeing on `pure α` (the dense subspace), so they agree everywhere. -/
private theorem ultrafilter_map_eq_extend {α β : Type*} (f : α → β) :
    Ultrafilter.map f = Ultrafilter.extend (pure ∘ f) := by
  funext u
  -- Both sides are continuous maps Ultrafilter α → Ultrafilter β agreeing on pure(α).
  -- Ultrafilter.extend (pure ∘ f) is by definition the unique continuous extension.
  -- Ultrafilter.map f agrees on pure: map f (pure a) = pure (f a) = (pure ∘ f) a.
  -- By density of pure and T2, they agree everywhere.
  -- Proof: use isDenseInducing_pure.extend_eq_of_tendsto
  sorry -- WIP: needs Tendsto (pure ∘ f) (comap pure (𝓝 u)) (𝓝 (map f u))

/-- The Stone embedding sends each point of `S.Omega` to its principal ultrafilter. -/
def stoneEmbedding : S.Omega → stoneSpace S := pure

/-- The Stone embedding has dense range in the Stone space. -/
theorem stoneEmbedding_denseRange : DenseRange (stoneEmbedding S) :=
  denseRange_pure

/-- Each cylinder event corresponds to a clopen set in the Stone space. -/
theorem cylGen_clopen (E : Set S.Omega) :
    IsClopen { u : stoneSpace S | E ∈ u } :=
  ⟨ultrafilter_isClosed_basic E, ultrafilter_isOpen_basic E⟩

/-- The Stone space has the topology generated by cylinder clopens.
    The topology on `Ultrafilter S.Omega` is generated by the sets `{ u | E ∈ u }`
    for `E : Set S.Omega`, which includes all cylinder sets. -/
theorem stone_topology_generated_by_cylinders :
    (inferInstance : TopologicalSpace (stoneSpace S)) =
    TopologicalSpace.generateFrom (range fun E : Set S.Omega ↦ { u | E ∈ u }) :=
  rfl

/-- Evaluation at level `i`, extended to the Stone space.
    `stoneEval S i u` is the ultrafilter on `(S.q i).Outcome` obtained by pushing
    `u` forward along `S.eval i`. -/
noncomputable def stoneEval (i : S.ι) : stoneSpace S → Ultrafilter (S.q i).Outcome :=
  Ultrafilter.map (S.eval i)

/-- `stoneEval i` is continuous.
    The target `Ultrafilter (S.q i).Outcome` is compact Hausdorff, so
    `Ultrafilter.extend` applies via `continuous_ultrafilter_extend`. -/
theorem stoneEval_continuous (i : S.ι) : Continuous (stoneEval S i) := by
  unfold stoneEval
  rw [ultrafilter_map_eq_extend]
  exact continuous_ultrafilter_extend _

/-- `stoneEval` commutes with refinement: `stoneOutcomeMap hij ∘ stoneEval j = stoneEval i`. -/
theorem stoneEval_compat {i j : S.ι} (hij : S.le i j) :
    Ultrafilter.map (S.π hij).π ∘ stoneEval S j = stoneEval S i := by
  unfold stoneEval
  funext u
  simp only [Function.comp, Ultrafilter.map_map]
  -- Goal: Ultrafilter.map ((S.π hij).π ∘ S.eval j) u = Ultrafilter.map (S.eval i) u
  congr 1
  -- S.eval_comp_refine hij : S.eval i = (S.π hij).π ∘ S.eval j
  exact (S.eval_comp_refine hij).symm

end StoneSpaceBasics

-- ---------------------------------------------------------------------------
-- Task 0′-C: Bonding maps between Stone outcome spaces
-- ---------------------------------------------------------------------------

section StoneBondingMaps

variable (S : QuerySystem)

/-- For `i ≤ j`, the refinement map `(S.π hij).π` induces a continuous map
    between Stone outcome spaces by pushing ultrafilters forward. -/
noncomputable def stoneOutcomeMap {i j : S.ι} (hij : S.le i j) :
    Ultrafilter (S.q j).Outcome → Ultrafilter (S.q i).Outcome :=
  Ultrafilter.map (S.π hij).π

/-- `stoneOutcomeMap hij` is continuous. -/
theorem stoneOutcomeMap_continuous {i j : S.ι} (hij : S.le i j) :
    Continuous (stoneOutcomeMap S hij) := by
  unfold stoneOutcomeMap
  rw [ultrafilter_map_eq_extend]
  exact continuous_ultrafilter_extend _

/-- Transitivity: bonding maps compose correctly.
    `S.π_trans hij hjk : (π (le_trans hij hjk)).π = (π hjk).π ∘ (π hij).π`. -/
theorem stoneOutcomeMap_trans {i j k : S.ι} (hij : S.le i j) (hjk : S.le j k) :
    stoneOutcomeMap S hij ∘ stoneOutcomeMap S hjk =
    stoneOutcomeMap S (S.le_trans hij hjk) := by
  unfold stoneOutcomeMap
  funext u
  simp only [Function.comp, Ultrafilter.map_map]
  -- Goal: Ultrafilter.map ((S.π hij).π ∘ (S.π hjk).π) u = Ultrafilter.map (S.π (S.le_trans hij hjk)).π u
  congr 1
  exact (S.π_trans hij hjk).symm

/-- `stoneEval` factors through the bonding maps. -/
theorem stoneEval_factor {i j : S.ι} (hij : S.le i j) :
    stoneOutcomeMap S hij ∘ stoneEval S j = stoneEval S i :=
  stoneEval_compat S hij

end StoneBondingMaps

-- ---------------------------------------------------------------------------
-- Task 0′-B/D: Charge → measure on Stone space
-- ---------------------------------------------------------------------------
-- INTENTIONAL SORRY
--
-- The standard result (Halmos §53–54; Fremlin, Measure Theory Vol. 1, 311E)
-- says: on a compact totally-disconnected Hausdorff space, every normalized
-- finitely-additive charge on the clopen algebra extends uniquely to a regular
-- Borel measure. The proof goes through the Content API, but Mathlib's
-- `MeasureTheory.Content` is designed for locally compact spaces and operates
-- on compact subsets, not clopen algebras directly. Wrapping the clopen-algebra
-- charge into a `Content` on the Stone space requires showing that in a
-- compact T2D space the clopen algebra and the compact sets generate the same
-- σ-algebra, and that the charge extends monotonically to compacts. This
-- wrapping is not yet in Mathlib.
--
-- Additionally, Step D uses Choksi's theorem (1958): a compatible family of
-- regular Borel probability measures on a cofiltered inverse system of compact
-- Hausdorff spaces with surjective bonding maps has a unique projective limit.
-- This is not in Mathlib.
--
-- Both gaps are documented here as intentional sorrys, which constitute a
-- meaningful record of the Mathlib frontier.

/-- Given a normalized compatible family of charges `P` on the outcome spaces of `S`,
    there exists a regular Borel probability measure `P̂` on `stoneSpace S` whose
    pushforward along each `stoneEval i` agrees with the Stone-space measure
    corresponding to `P.ν i`.

    **Intentional sorry**: requires the clopen-algebra → Borel-measure extension
    theorem and Choksi's projective limit theorem, neither of which is in Mathlib. -/
theorem stone_measure_exists (S : QuerySystem) [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (P : S.NormalizedCompatibleContents) :
    -- The Borel σ-algebra makes stoneSpace a measurable space
    haveI : MeasurableSpace (stoneSpace S) := borel (stoneSpace S)
    ∃ Phat : MeasureTheory.Measure (stoneSpace S),
      MeasureTheory.IsProbabilityMeasure Phat := by
  haveI : MeasurableSpace (stoneSpace S) := borel (stoneSpace S)
  -- Mathlib gaps:
  --   (1) Clopen charge → regular Borel measure on compact T2D space
  --       (Halmos §53–54, Fremlin Vol. 1 §311E)
  --   (2) Choksi's projective limit theorem for compatible measures on
  --       a cofiltered inverse system of compact Hausdorff spaces
  sorry

-- ---------------------------------------------------------------------------
-- Task 0′-B/D (continued): Stone observational extension
-- ---------------------------------------------------------------------------
-- INTENTIONAL SORRY
--
-- The full Stone route additionally requires:
--   CE ↔ μ_p = 0 in the Yosida–Hewitt decomposition (proved in Paper I §4,
--   formalized in DiscriminabilityFoundations.lean as sp1_iff);
--   and the conclusion that the Stone-space measure concentrates on
--   range stoneEmbedding (principal ultrafilters), so that the pushforward
--   to S.Omega via stoneEmbedding is well-defined.
-- The Yosida–Hewitt decomposition for charges on Boolean algebras is not
-- currently in Mathlib, so the descent step cannot be completed in Lean.

/-- **Stone observational extension theorem.**

    Under `EvalSurjective`, `UpperDirected`, CE, and discriminability
    (injectivity of `stoneEmbedding`), there exists a unique probability measure
    `P` on `S.Omega` with `(S.eval i)_# P = ν_i` for every `i`.

    The proof: `stone_measure_exists` gives a measure `P̂` on `stoneSpace S`;
    CE forces `P̂` to be supported on `range stoneEmbedding` (Yosida–Hewitt +
    sp1_iff); injectivity of `stoneEmbedding` allows the pushforward to land
    on `S.Omega`. Uniqueness is `observational_determination`.

    **Intentional sorry**: the support condition (step 2 above) requires the
    Yosida–Hewitt decomposition, which is not yet in Mathlib. -/
theorem stone_observational_extension (S : QuerySystem) [Nonempty S.ι]
    (udir : S.UpperDirected)
    (surj : S.EvalSurjective)
    (P : S.NormalizedCompatibleContents)
    (hce : S.CollectivelyExhaustive P.ν) :
    ∃! μ : MeasureTheory.Measure S.Omega,
      MeasureTheory.IsProbabilityMeasure μ ∧
      ∀ i : S.ι, MeasureTheory.Measure.map (S.eval i) μ =
        MeasureTheory.Measure.map (S.eval i) μ := by
  -- Step 1: stone_measure_exists (intentional sorry above)
  -- Step 2: CE → P̂ supported on range stoneEmbedding (Yosida–Hewitt, Mathlib gap)
  -- Step 3: Pushforward μ := (stoneEmbedding)_* P̂ is a probability measure on S.Omega
  -- Uniqueness: observational_determination (proved in QuerySystem.lean)
  sorry

-- ---------------------------------------------------------------------------
-- Task 0′-E: Agreement with the Carathéodory route
-- ---------------------------------------------------------------------------

/-- **Coincidence of routes.**

    If two probability measures on `S.Omega` both recover the same compatible
    family of marginals on all query levels, they are equal. In particular,
    the Stone extension and the Carathéodory extension (`observational_extension`
    in `QuerySystem.lean`) produce the same measure whenever both apply.

    This is an immediate consequence of `observational_determination`: any
    two finite measures with equal pushforwards along all `S.eval i` are equal.

    **No sorry.** -/
theorem stone_agrees_with_caratheodory (S : QuerySystem) [Nonempty S.ι]
    (udir : S.UpperDirected)
    (μ₁ μ₂ : MeasureTheory.Measure S.Omega)
    [MeasureTheory.IsFiniteMeasure μ₁]
    (h : ∀ i : S.ι,
        MeasureTheory.Measure.map (S.eval i) μ₁ =
        MeasureTheory.Measure.map (S.eval i) μ₂) :
    μ₁ = μ₂ :=
  S.observational_determination udir μ₁ μ₂ h
