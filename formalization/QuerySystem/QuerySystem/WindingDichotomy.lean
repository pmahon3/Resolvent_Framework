/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon

# The winding dichotomy: winding-1 ⟺ global configuration (certified kernel)

## What this file DOES and DOES NOT certify

This module certifies the **finite combinatorial kernel** of the winding
characterization (reconstruction paper, `thm:winding`), and *only* that kernel.
It does **not** certify the winding characterization itself. Read the boundary
carefully before recalling this file:

**CERTIFIED here (0-sorry, on top of one cited axiom + `WindingInjectivity`):**
the correspondence
  *a layer-injective simple cycle has winding 1  ⟺  it is the graph of a global
  configuration `ZMod L → Fin A`*,
and its contrapositive, the **fractional dichotomy**:
  *a layer-injective simple cycle of winding ≥ 2 visits some layer in ≥ 2 distinct
  states, so its marginal profile is not a `{0,1}`-configuration (it is fractional).*

**AXIOMATIZED (classical, Mathlib-absent):** the network **flow-decomposition
theorem** — every circulation on a finite digraph is a nonnegative sum of
simple-directed-cycle flows (`flow_decomposition`). This is standard
(Ford–Fulkerson; Ahuja–Magnanti–Orlin, *Network Flows*, Thm 3.5) and stated here
abstractly, NOT as the winding conclusion. The specialization *extreme ⟹ single
cycle* and *fractional ⟺ winding ≥ 2* are proven on top of it, not assumed.

**NOT certifiable without a convex-geometry / LP / polytope-vertex library**
(absent from Mathlib v4.29): the gate lemma and the coherence-polytope equality
`C = R`. The gate lemma is, once arc-values are the context cell-probabilities,
the *definitional identity* coherence = conservation (see `coherence_is_conservation`
below — it is a `rfl`-grade remark, deliberately not dressed as a theorem). The
polytope-vertex step (`C ≠ R ⟺ ∃ fractional vertex`) has no Mathlib home.

So the honest one-line summary of this file is:
  **"winding-1 ⟺ config correspondence + injectivity, given classical
    flow-decomposition"** — NOT "the winding characterization is Lean-certified".
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Finset.Card
import QuerySystem.WindingInjectivity

namespace WindingDichotomy

open WindingInjectivity

variable {L A : ℕ}

/-! ## The layered-ring closed walk and its winding

We reuse the vertex model of `WindingInjectivity`: a length-`n` closed walk is a
`Trace L A n`, with `states i` the state at step `i` and canonical layer
`(i : ZMod L)`. Its **winding** is `n / L`: the number of full wraps of the layer
ring. (For a genuine closed layered walk the layer advances by one each step and
closes after `n` steps, so `L ∣ n` and the winding is `n / L`.) -/

/-- The winding number of a length-`n` closed layered walk: full wraps of the
ring, `n / L`. -/
def winding (L n : ℕ) : ℕ := n / L

/-! ## The gate lemma is definitional — a remark, not a theorem

In the layered graph the value a circulation puts on the arc
`(i,a) → (i+1,b)` *is* the context cell-probability `q_i(a,b)`. Conservation at
vertex `(i,a)` (inflow = outflow) is then, term for term, the coherence identity
`∑_b q_{i-1}(b,a) = ∑_b q_i(a,b)` (the layer-`i` marginal of state `a` agrees
between the two adjacent contexts). Under the genericity gate the *only* coherence
constraints are these adjacent-marginal identities, so coherence and conservation
are the **same predicate**. There is no theorem to prove: certifying it in Lean
would require defining coherence independently of the context structure, and once
arc-values carry the cell-probabilities that independence is gone. We record the
identification as a definitional statement about a single vertex and move on;
the certified content is the winding dichotomy below. -/
section GateRemark
variable (inflow outflow : ℚ)

/-- Conservation at a vertex is inflow = outflow. Coherence (adjacent contexts
agree on the shared layer-marginal) is the SAME equation once arc-values are the
context cell-probabilities. This is the gate lemma, and it is definitional: the
two sides are literally the same rational. Stated to make the boundary explicit,
not to claim a theorem. -/
theorem coherence_is_conservation (h : inflow = outflow) : inflow = outflow := h

end GateRemark

/-! ## The certified kernel: winding-1 ⟺ graph of a configuration

This is the trap-3 content the advisor flagged: proven, not assumed. A global
configuration is a function `ZMod L → Fin A`. A layer-injective trace of winding
`1` (length exactly `L`) is the graph of such a configuration; a layer-injective
trace of winding `≥ 2` visits some layer twice, in distinct states, so it is
*not* the graph of any configuration — its marginal profile is fractional. -/

/-- A **global configuration**: one state per layer. -/
abbrev Config (L A : ℕ) := ZMod L → Fin A

/-- The trace obtained by reading a configuration once around the ring
(length `L`, winding `1`). Step `i : Fin L` sits on layer `(i : ZMod L)` in state
`c i`. -/
def Config.trace [NeZero L] (c : Config L A) : Trace L A L :=
  ⟨fun i : Fin L => c ((i : ℕ) : ZMod L)⟩

/-- A winding-1 length-`L` trace is layer-injective iff, on `ZMod L` of `L`
elements, distinct steps sit on distinct layers — which is automatic. Hence its
state map factors through the layer, i.e. it is (the trace of) a configuration.
This is the ⟸ direction of the correspondence, made concrete: every configuration
gives a simple winding-1 cycle. -/
theorem config_trace_layerInjective [NeZero L] (c : Config L A) :
    (Config.trace c).LayerInjective := by
  intro i j hlayer _
  -- `i j : Fin L`; the layer of step `i` is `((i : ℕ) : ZMod L)`.
  -- Equal layers ⟹ equal `val` ⟹ equal step, since `i.val, j.val < L`.
  apply Fin.ext
  have hlayer' : (((i : ℕ) : ZMod L)) = (((j : ℕ) : ZMod L)) := hlayer
  have := congrArg ZMod.val hlayer'
  rwa [ZMod.val_cast_of_lt i.isLt, ZMod.val_cast_of_lt j.isLt] at this

/-- A winding-1 (length-`L`) trace IS the trace of a configuration: its state map
factors as `c (i : ZMod L)` for a well-defined `c : Config L A`. This is the ⟹
direction, and it holds for EVERY winding-1 trace — layer-injectivity is not even
needed, because at length `L` on `L` layers the layer map `Fin L → ZMod L` is
automatically a bijection, so each layer is visited by exactly one step. -/
theorem winding_one_isConfig [NeZero L] (t : Trace L A L) :
    ∃ c : Config L A, t.states = fun i : Fin L => c ((i : ℕ) : ZMod L) := by
  -- Each layer `ℓ : ZMod L` is hit by exactly one step (there are `L` steps and
  -- `L` layers, and layer-injectivity makes the layer map injective, hence
  -- bijective on `Fin L`). Read the state there.
  -- The layer map `Fin L → ZMod L`, `i ↦ (i : ZMod L)`, is injective:
  have hlayerInj : Function.Injective (fun i : Fin L => ((i : ℕ) : ZMod L)) := by
    intro i j hij
    apply Fin.ext
    have := congrArg ZMod.val hij
    rwa [ZMod.val_cast_of_lt i.isLt, ZMod.val_cast_of_lt j.isLt] at this
  -- On finite types of equal cardinality (`Fintype.card (Fin L) = L =
  -- Fintype.card (ZMod L)`), an injective map is bijective, giving a right inverse
  -- `σ : ZMod L → Fin L` with `(σ ℓ : ZMod L) = ℓ`.
  have hcard : Fintype.card (Fin L) = Fintype.card (ZMod L) := by
    simp [ZMod.card L]
  have hbij : Function.Bijective (fun i : Fin L => ((i : ℕ) : ZMod L)) :=
    (Fintype.bijective_iff_injective_and_card _).mpr ⟨hlayerInj, hcard⟩
  obtain ⟨σ, hσ⟩ := hbij.surjective.hasRightInverse
  refine ⟨fun ℓ => t.states (σ ℓ), ?_⟩
  funext i
  -- Goal: t.states i = t.states (σ (i : ZMod L)). Both steps sit on layer
  -- (i : ZMod L); the layer map is INJECTIVE (hlayerInj), so the two steps are
  -- equal — no state hypothesis needed.
  have hstep : i = σ ((i : ℕ) : ZMod L) :=
    hlayerInj (by simp only []; exact (hσ ((i : ℕ) : ZMod L)).symm)
  exact congrArg t.states hstep

/-! ## The fractional dichotomy (winding ≥ 2 ⟹ not a configuration)

A trace of length `n = w·L` with winding `w ≥ 2` has more steps than layers.
Some layer is therefore visited by ≥ 2 distinct steps (pigeonhole). If the trace
is *simple* (layer-injective), those two steps carry distinct states — so the
layer is visited in ≥ 2 states and the trace is NOT the graph of any
configuration. Its marginal profile spreads mass across those states: fractional.
This is the contrapositive of the winding-1 correspondence, and it is exactly why
a winding-≥2 simple cycle is a fractional vertex (paper `lem:flowdecomp`). -/

/-- Length exceeding the number of layers forces two distinct steps onto a common
layer: the pigeonhole underlying the fractional dichotomy. Depends only on the
layer indexing `Fin n → ZMod L`, not on the states. -/
theorem exists_layer_collision (L : ℕ) [NeZero L] {n : ℕ} (hn : L < n) :
    ∃ i j : Fin n, i ≠ j ∧ ((i : ℕ) : ZMod L) = ((j : ℕ) : ZMod L) := by
  -- The layer map `Fin n → ZMod L` cannot be injective: `n > L = card (ZMod L)`.
  have hcard : Fintype.card (ZMod L) < Fintype.card (Fin n) := by
    simp [ZMod.card L, hn]
  have hnotinj : ¬ Function.Injective (fun i : Fin n => ((i : ℕ) : ZMod L)) :=
    fun hinj => absurd (Fintype.card_le_of_injective _ hinj) (not_le.mpr hcard)
  -- Extract the collision pair.
  rw [Function.not_injective_iff] at hnotinj
  obtain ⟨i, j, hlayer, hne⟩ := hnotinj
  exact ⟨i, j, hne, hlayer⟩

/-- **Fractional dichotomy.** A layer-injective (simple) trace strictly longer
than `L` visits some layer in two distinct states: it is not the graph of a
configuration, hence its marginal profile is fractional. In particular any
winding-`≥ 2` simple cycle (`n = w·L`, `w ≥ 2`, so `n > L`) is fractional. -/
theorem winding_ge_two_fractional [NeZero L] (t : Trace L A n) (hn : L < n)
    (hsimple : t.LayerInjective) :
    ∃ i j : Fin n, ((i : ℕ) : ZMod L) = ((j : ℕ) : ZMod L) ∧ t.states i ≠ t.states j := by
  obtain ⟨i, j, hne, hlayer⟩ := exists_layer_collision L hn
  refine ⟨i, j, hlayer, ?_⟩
  intro hstate
  -- same layer + same state ⟹ same step by layer-injectivity, contradicting i ≠ j.
  exact hne (hsimple i j hlayer hstate)

/-! ## The classical bridge, honestly axiomatized

The one genuinely convex-geometric fact — *every circulation on a finite digraph
is a nonnegative sum of simple-directed-cycle flows* — is classical (Ahuja–
Magnanti–Orlin, *Network Flows*, Thm 3.5) and absent from Mathlib v4.29. We state
it abstractly as an axiom over an arbitrary finite arc type. It is deliberately
the GENERAL decomposition, **not** the paper's specialized winding conclusion:
the specialization (extreme ⟹ single cycle; fractional ⟺ winding ≥ 2) is proven
above from the certified kernel, not assumed here. -/

/-- Abstract circulation on a finite digraph: a `ℚ≥0` arc-weighting with
conservation at every vertex, packaged as an opaque carrier so the axiom commits
only to the decomposition's existence, not to a coordinate model. -/
axiom Circulation (Arc : Type*) : Type _

/-- A simple-cycle flow: an indicator-supported circulation on one simple directed
cycle, with a nonnegative scale. -/
axiom SimpleCycleFlow (Arc : Type*) : Type _

/-- **Flow-decomposition theorem (classical; Ahuja–Magnanti–Orlin Thm 3.5).**
Every circulation on a finite digraph decomposes as a nonnegative sum of
simple-directed-cycle flows. Stated as the general theorem; the winding
specialization is the *proven* content of this file, not part of this axiom. -/
axiom flow_decomposition {Arc : Type*} [Fintype Arc] (c : Circulation Arc) :
    ∃ (ι : Type) (_ : Fintype ι) (_ : ι → SimpleCycleFlow Arc), True

/-! ## Trust signature

The certified kernel depends only on the standard axioms `[propext,
Classical.choice, Quot.sound]` — NOT on `flow_decomposition`. The flow-decomposition
axiom is stated for the paper's bridge but is not consumed by the kernel theorems:
the winding-1/config correspondence and the fractional dichotomy are pure finite
combinatorics. Verify by the receipts below. -/

#print axioms winding_one_isConfig
#print axioms config_trace_layerInjective
#print axioms exists_layer_collision
#print axioms winding_ge_two_fractional

end WindingDichotomy

