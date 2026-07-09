/-
# Lemma 2: the layer-injectivity discriminant for winding cycles

This module machine-certifies the **injectivity clause** of the winding
characterization: the discriminator that a closed walk on the layered ring is a
genuine *simple* cycle iff it is *layer-injective* (visits each layer in
pairwise-distinct states).

Provenance (reconstruction / commensurability programme): this clause caught two
hand-errors — the doubled-rotation non-witness and the lockstep-reduction phase
gap — so it is the highest-value object to move to certificate grade. It is
deliberately independent of the OPEN pruning lemma and of eventual periodicity:
it is pure combinatorics on the layered-ring graph.

Model. A closed walk of length `n` on the layered ring over `ZMod L` with
alphabet `Fin A` is a function `w : Fin n → ZMod L × Fin A` together with the
adjacency that consecutive vertices advance the layer by one and respect the
relation. For Lemma 2 we only need the *vertex trace*; the relation/adjacency is
not required for the injectivity ⟺ simplicity equivalence, which is what makes
the clause clean.

The statement. For a closed walk whose layer-coordinate at step `i` is `i mod L`
(the canonical layered indexing), it is a simple cycle (all vertices distinct)
iff at each layer the multiset of visited states has no repeat — layer-injective.
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fintype.Basic
import Mathlib.Data.Finset.Card

namespace WindingInjectivity

variable {L A : ℕ}

/-- A vertex of the layered ring: a layer in `ZMod L` and a state in `Fin A`. -/
abbrev Vertex (L A : ℕ) := ZMod L × Fin A

/-- The vertex trace of a length-`n` closed walk. `states i` is the state at
step `i`; the layer at step `i` is `(i : ZMod L)` by the canonical layered
indexing. -/
structure Trace (L A n : ℕ) where
  states : Fin n → Fin A

/-- The vertex at step `i`: canonical layer `(i mod L)` paired with the state. -/
def Trace.vertex (t : Trace L A n) (i : Fin n) : Vertex L A :=
  ((i : ZMod L), t.states i)

/-- **Simple**: distinct steps give distinct vertices. -/
def Trace.Simple (t : Trace L A n) : Prop :=
  Function.Injective t.vertex

/-- **Layer-injective**: whenever two steps land on the same layer, their states
differ (unless they are the same step). Equivalently, the state map is injective
on each layer fibre. -/
def Trace.LayerInjective (t : Trace L A n) : Prop :=
  ∀ i j : Fin n, (i : ZMod L) = (j : ZMod L) → t.states i = t.states j → i = j

/-- **Lemma 2 (injectivity clause).** A layered-ring closed walk is a simple
cycle iff it is layer-injective. The two conditions are literally the same
statement unfolded through the vertex definition — which is precisely why the
informal reasoning that dropped it (doubled rotation; lockstep phase gap) was
wrong: "closes up" is not "simple", and layer-injectivity is the exact
certificate of simplicity. -/
theorem simple_iff_layerInjective (t : Trace L A n) :
    t.Simple ↔ t.LayerInjective := by
  constructor
  · intro hsimple i j hlayer hstate
    -- same layer and same state ⟹ same vertex ⟹ same step by simplicity
    apply hsimple
    simp only [Trace.vertex, Prod.mk.injEq]
    exact ⟨hlayer, hstate⟩
  · intro hli i j hij
    -- equal vertices ⟹ equal layer and equal state ⟹ equal step by injectivity
    have hlayer : (i : ZMod L) = (j : ZMod L) := congrArg Prod.fst hij
    have hstate : t.states i = t.states j := congrArg Prod.snd hij
    exact hli i j hlayer hstate

/-- Consequence: on a layered ring, checking simplicity of a closed walk reduces
to a per-layer distinctness check — the algorithmic content the winding
characterization uses. -/
theorem simple_of_layerInjective (t : Trace L A n) (h : t.LayerInjective) :
    t.Simple :=
  (simple_iff_layerInjective t).mpr h

/-- The contrapositive form that names the failure mode caught in the programme:
a closed walk that revisits a (layer, state) pair is *not* simple, no matter
that it "closes up". -/
theorem not_simple_of_collision (t : Trace L A n)
    {i j : Fin n} (hne : i ≠ j)
    (hlayer : (i : ZMod L) = (j : ZMod L)) (hstate : t.states i = t.states j) :
    ¬ t.Simple := by
  intro hsimple
  exact hne ((simple_iff_layerInjective t).mp hsimple i j hlayer hstate)

/-! ## Non-vacuity: a concrete winding-2 collision that is provably not simple

On the ring `ZMod 2` with alphabet `Fin 1`, a length-2 walk visits steps `0` and
`1`, which map to layers `0` and `1` — distinct, so this is layer-injective and
simple. To exhibit a *collision* we take length `4` on `ZMod 2`: steps `0` and
`2` both land on layer `0`; with only one available state they share it, so the
walk revisits vertex `(0,0)` and is not simple. This is the winding-2
self-intersection the programme's informal reasoning repeatedly mishandled,
here machine-refuted. -/

/-- The all-single-state trace of length 4 on `ZMod 2`: a genuine collision. -/
def collisionTrace : Trace 2 1 4 := ⟨fun _ => 0⟩

example : ¬ collisionTrace.Simple := by
  apply not_simple_of_collision collisionTrace (i := (0 : Fin 4)) (j := (2 : Fin 4))
  · decide
  · decide
  · rfl

/-- A layer-injective length-2 trace on `ZMod 2` IS simple. -/
def simpleTrace : Trace 2 1 2 := ⟨fun _ => 0⟩

example : simpleTrace.Simple := by
  apply simple_of_layerInjective
  intro i j hlayer _
  -- distinct steps on ZMod 2 of length 2 have distinct layers, so hlayer forces i = j
  fin_cases i <;> fin_cases j <;> simp_all

end WindingInjectivity

-- Trust signature: only standard axioms, no `sorry`.
#print axioms WindingInjectivity.simple_iff_layerInjective
#print axioms WindingInjectivity.simple_of_layerInjective
#print axioms WindingInjectivity.not_simple_of_collision
