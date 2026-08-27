/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.DelayEmbedding
import QuerySystem.TheoremB

/-!
# Relational delay systems: the pruning lane's objects as delay data

The delay chapter observes a **function** `T : X → X`; the pruning chapter
studies a **relation** `ρ ⊆ A × A`. `delayQueryAlgebraAtLag_eq` showed the two
chapters index by the same thing -- the delay chapter's lag is the pruning
chapter's ring length -- but a dictionary between indices is not a theorem
between chapters. This file supplies one.

## Why the relation side is the general one

Specialising pruning to a deterministic `ρ` collapses it. A functional graph is
rho-shaped -- one cycle per component -- so every closed walk is a repeated
cycle, and traversing a cycle of length `m` gives winding `m / gcd(m, L)`: the
layer-`i` states are `{i + jL mod m}`, and `C_m × C_L` is `gcd(m,L)` copies of
`C_lcm(m,L)`. For a function every strand therefore lies on ONE orbit.
Branching is what lets strands sit on different orbits, so Theorem P's content
is in the nondeterministic case, and the join has to carry the delay side up to
relations rather than push pruning down to maps.

The carrying object is the **subshift**: the bi-infinite `ρ`-trajectories inside
`SensorStream α`. A relation has no orbit map, but it does have a trajectory
space, and delay queries apply to a trajectory space exactly as they apply to a
stream.

## The time convention, again

`Subshift` is stated as `ρ (ω (t+1)) (ω t)` -- reading the stream backwards runs
the relation forwards -- which is the convention `orbitStream` already fixed and
which `delayEval`'s sampling at `0, -τ, …` forces. It is not a free choice here:
with the other orientation the theorem below would sample the trajectory in
reverse.

## What is proved

`isLISC_delay_witness`: a layer-injective simple cycle of winding `k` in the
layered ring `R_L(ρ)` yields a `ρ`-trajectory that is `k*L`-periodic and whose
**depth-`k`, lag-`L` delay query is injective**.

That is the bridge, and the injectivity is not an add-on -- `IsLISC`'s
simplicity clause says precisely that the `k` positions sharing layer `0` carry
distinct states, and those positions are exactly the `k` sample times of the
lag-`L` query. Read in the delay chapter's vocabulary: `L` is unsafe exactly
when lag-`L` sampling of some periodic trajectory fails to collapse, seeing `k ≥ 2`
distinct strands where safety would see one.

## The deterministic case is a subclass of this, not a parallel to it

The relational description is the general one, so the deterministic theory has
to appear *inside* it at `ρ = graph T`. It does, and the final section proves
it: for a `graphRel T`-trajectory `ω`, the delay data the relational picture
assigns to `ω` is literally the delay data the deterministic picture assigns to
`ω 0` (`delayEval_comp_eq_orbitStream`). `orbitStream` and everything proved
from it are the `ρ = graph T` instance, not a lookalike development.

The obstruction to this is narrower than it first appears, and the earlier
reading of it was the wrong shape. `stateStream T x` really is not a member of
`Subshift (graphRel T)` -- `Int.toNat` clamps its positive half constant, so the
trajectory condition there would demand `x = T x`. But **delay queries never
sample positive times**: `delayEval` reads at `0, -τ, …, -(d-1)τ`
(`delayEval_congr_nonpos`). Disagreement on the positive half is disagreement
about something no query in the theory can observe, so requiring agreement there
was requiring more than the theory uses.

What genuinely does not transfer is smaller and is a condition on `T`, not on
observation: being the base of a bi-infinite trajectory forces
`ω 0 ∈ range (T^[n])` for every `n` (`graphSubshift_base_mem_range`), so a
non-surjective `T` has points no relational trajectory can be based at -- while
the delay data of those points is still perfectly well defined by `orbitStream`.
The two halves of a trajectory carry the asymmetry: the non-positive half is the
forward orbit of the base point, the positive half is a coherent choice of
backward orbit, and only the second can fail to exist.
-/

namespace QuerySystem
namespace RelationalDelay

open Reconstruction.Pruning

universe u

variable {α : Type u} [MeasurableSpace α]

/-- **The subshift of a relation**: the bi-infinite `ρ`-trajectories, as a set of
sensor streams. Stated in the delay chapter's time convention -- reading the
stream backwards runs `ρ` forwards. -/
def Subshift (ρ : α → α → Prop) : Set (SensorStream α) :=
  {ω | ∀ t : ℤ, ρ (ω (t + 1)) (ω t)}

/-- The periodic trajectory read off a cycle witness: position `t` of the stream
carries the cycle's state at index `(-t) mod n`. The negation is the time
convention; the modulus makes it bi-infinite and `n`-periodic. -/
def cycleStream (W : ℕ → α) (n : ℕ) : SensorStream α :=
  fun t => W ((-t) % (n : ℤ)).toNat

/-- `cycleStream` is `n`-periodic. -/
theorem cycleStream_periodic (W : ℕ → α) (n : ℕ) (t : ℤ) :
    cycleStream W n (t + n) = cycleStream W n t := by
  simp only [cycleStream]
  congr 2
  have h1 : -(t + (n : ℤ)) = -t - (n : ℤ) := by ring
  rw [h1, Int.sub_emod_right]

/-- Sampling `cycleStream` at the lag-`L` times of a depth-`k` delay query
returns the cycle's layer-`0` states, in order. -/
theorem delayEval_cycleStream (W : ℕ → α) (k L : ℕ) (hk : 0 < k) (hL : 0 < L)
    (j : Fin k) :
    delayEval k L (cycleStream W (k * L)) j = W (j.val * L) := by
  simp only [delayEval, cycleStream, neg_neg]
  congr 1
  have hltN : j.val * L < k * L := (Nat.mul_lt_mul_right hL).mpr j.isLt
  have hlt : ((j.val * L : ℕ) : ℤ) < ((k * L : ℕ) : ℤ) := by exact_mod_cast hltN
  have hnonneg : (0 : ℤ) ≤ ((j.val * L : ℕ) : ℤ) := Int.natCast_nonneg _
  rw [Int.emod_eq_of_lt hnonneg hlt]
  exact Int.toNat_natCast _

/-- `cycleStream` really is a `ρ`-trajectory. The wrap is the only interesting
step: at the one position where the index rolls over, the cycle's closing arc
`ρ (W (k*L-1)) (W 0)` is what continues the trajectory. -/
theorem cycleStream_mem_subshift {ρ : α → α → Prop} {W : ℕ → α} {k L : ℕ}
    (hn : 0 < k * L)
    (hstep : ∀ t, t + 1 < k * L → ρ (W t) (W (t + 1)))
    (hclose : ρ (W (k * L - 1)) (W 0)) :
    cycleStream W (k * L) ∈ Subshift ρ := by
  intro t
  simp only [Subshift, cycleStream, Set.mem_setOf_eq]
  set n : ℕ := k * L with hnn
  set m : ℤ := -(t + 1) with hm
  have hneg : -t = m + 1 := by rw [hm]; ring
  rw [hneg]
  have hnpos : (0 : ℤ) < (n : ℤ) := by exact_mod_cast hn
  have ha0 : 0 ≤ m % (n : ℤ) := Int.emod_nonneg _ (ne_of_gt hnpos)
  have han : m % (n : ℤ) < (n : ℤ) := Int.emod_lt_of_pos _ hnpos
  have key : (m + 1) % (n : ℤ) = (m % (n : ℤ) + 1) % (n : ℤ) := by
    conv_lhs => rw [show m = m % (n : ℤ) + (n : ℤ) * (m / (n : ℤ)) from
      (Int.emod_add_ediv m (n : ℤ)).symm]
    rw [add_right_comm, Int.add_mul_emod_self_left]
  rw [key]
  set a : ℤ := m % (n : ℤ) with hA
  rcases lt_or_eq_of_le (Int.add_one_le_iff.mpr han) with hlt | heq
  · -- interior: the index simply advances
    rw [Int.emod_eq_of_lt (by omega) hlt]
    have h1 : (a + 1).toNat = a.toNat + 1 := by omega
    rw [h1]
    exact hstep a.toNat (by omega)
  · -- wrap: the closing arc
    rw [heq, Int.emod_self]
    have h2 : a.toNat = n - 1 := by omega
    rw [h2]
    simpa using hclose

/-- **The bridge.** A layer-injective simple cycle of winding `k` in the layered
ring `R_L(ρ)` is a `ρ`-trajectory that is `k*L`-periodic and whose depth-`k`,
lag-`L` delay query is *injective*.

The injectivity is the whole point and it is not an extra hypothesis:
`IsLISC`'s simplicity clause says the positions sharing layer `0` carry distinct
states, and those positions -- `0, L, …, (k-1)L` -- are exactly the sample times
of the lag-`L` delay query. Layer-injectivity in the pruning chapter's sense
*is* delay-injectivity in this chapter's sense. -/
theorem isLISC_delay_witness {ρ : α → α → Prop} {k L : ℕ}
    (hk : 0 < k) (hL : 0 < L) (h : IsLISC ρ k L) :
    ∃ ω ∈ Subshift ρ,
      (∀ t : ℤ, ω (t + ((k * L : ℕ) : ℤ)) = ω t) ∧
      Function.Injective (delayEval k L ω) := by
  obtain ⟨W, hstep, hclose, hsimple⟩ := h
  refine ⟨cycleStream W (k * L),
    cycleStream_mem_subshift (Nat.mul_pos hk hL) hstep hclose,
    cycleStream_periodic W (k * L), ?_⟩
  intro i j hij
  rw [delayEval_cycleStream W k L hk hL i, delayEval_cycleStream W k L hk hL j] at hij
  have hi : i.val * L < k * L := (Nat.mul_lt_mul_right hL).mpr i.isLt
  have hj : j.val * L < k * L := (Nat.mul_lt_mul_right hL).mpr j.isLt
  have hmod : (i.val * L) % L = (j.val * L) % L := by
    simp [Nat.mul_mod_left]
  have heq := hsimple _ _ hi hj hmod hij
  exact Fin.ext (Nat.eq_of_mul_eq_mul_right hL heq)

/-- **`Unsafe` in the delay chapter's vocabulary.** `L` is unsafe exactly when
lag-`L` sampling of some periodic `ρ`-trajectory fails to collapse: it sees
`k ≥ 2` distinct strands where safety would see one. -/
theorem unsafe_delay_witness {ρ : α → α → Prop} {L : ℕ} (hL : 0 < L)
    (h : L ∈ Unsafe ρ) :
    ∃ (k : ℕ) (ω : SensorStream α), 2 ≤ k ∧ ω ∈ Subshift ρ ∧
      (∀ t : ℤ, ω (t + ((k * L : ℕ) : ℤ)) = ω t) ∧
      Function.Injective (delayEval k L ω) := by
  obtain ⟨-, k, hk2, hlisc⟩ := h
  obtain ⟨ω, hmem, hper, hinj⟩ :=
    isLISC_delay_witness (lt_of_lt_of_le two_pos hk2) hL hlisc
  exact ⟨k, ω, hk2, hmem, hper, hinj⟩

/-! ## The bridge is not vacuous

`isLISC_delay_witness` is an implication, and an implication whose hypothesis is
unsatisfiable proves nothing. It is satisfiable: the complete relation on `Bool`
has a layer-injective simple cycle of winding `2` at ring length `1`, so `1` is
unsafe for it and the bridge fires with `k = 2`. -/

/-- A concrete `IsLISC`: the complete relation on `Bool`, winding `2`, ring
length `1`. Every step and the closure are trivially available; simplicity is
the two-case check that `W 0 ≠ W 1`. -/
theorem isLISC_complete_bool : IsLISC (fun _ _ : Bool => True) 2 1 := by
  refine ⟨fun t => decide (t = 0), fun _ _ => trivial, trivial, ?_⟩
  intro t1 t2 h1 h2 _ hW
  interval_cases t1 <;> interval_cases t2 <;> simp_all

/-- Hence the bridge's conclusion is actually inhabited: there is a periodic
trajectory of the complete relation on `Bool` whose depth-`2`, lag-`1` delay
query is injective. -/
theorem exists_delay_witness_complete_bool :
    ∃ ω ∈ Subshift (fun _ _ : Bool => True),
      (∀ t : ℤ, ω (t + ((2 * 1 : ℕ) : ℤ)) = ω t) ∧
      Function.Injective (delayEval 2 1 ω) :=
  isLISC_delay_witness two_pos one_pos isLISC_complete_bool

/-! ## The deterministic case as a subclass, not a parallel construction

The relational description is the general one, so the deterministic theory
should appear *inside* it as the special case `ρ = graph T` rather than beside
it. This section does that, and in doing so corrects the shape of the
obstruction recorded above.

The obstruction is real but narrower than "no embedding". `stateStream T x` is
genuinely not a member of `Subshift (graphRel T)` — the clamp makes its positive
half constant. But **the delay queries never sample positive times**: `delayEval`
reads at `0, -τ, …, -(d-1)τ`. So disagreement on the positive half is
disagreement about something no query in the theory can observe, and demanding
agreement there was demanding more than the theory uses.

On the half that is observed, the two pictures coincide exactly. -/

/-- The graph of a map, as a relation. -/
def graphRel (T : α → α) : α → α → Prop := fun a b => b = T a

/-- **Delay queries only see non-positive times.** Two streams agreeing there
are indistinguishable to every delay query. -/
theorem delayEval_congr_nonpos {ω₁ ω₂ : SensorStream α} (d τ : ℕ)
    (hEq : ∀ t : ℤ, t ≤ 0 → ω₁ t = ω₂ t) :
    delayEval d τ ω₁ = delayEval d τ ω₂ := by
  funext k
  exact hEq _ (neg_nonpos.mpr (Int.natCast_nonneg _))

/-- A `graphRel T`-trajectory reads the forward orbit of its base point at
non-positive times. This is the sense in which such a trajectory *is* an orbit. -/
theorem graphSubshift_neg {T : α → α} {ω : SensorStream α}
    (hω : ω ∈ Subshift (graphRel T)) (n : ℕ) :
    ω (-(n : ℤ)) = T^[n] (ω 0) := by
  induction n with
  | zero => simp
  | succ m ih =>
      have h := hω (-(m + 1 : ℤ))
      simp only [graphRel] at h
      have hstep : (-(m + 1 : ℤ)) + 1 = -(m : ℤ) := by ring
      rw [hstep] at h
      rw [show (-((m : ℤ) + 1)) = (-(m + 1 : ℕ) : ℤ) by push_cast; ring] at h
      rw [h, ih, Function.iterate_succ_apply']

/-- The delay data of a deterministic trajectory is the orbit's delay data. -/
theorem delayEval_graphSubshift {T : α → α} {ω : SensorStream α}
    (hω : ω ∈ Subshift (graphRel T)) (d τ : ℕ) :
    delayEval d τ ω = fun k : Fin d => T^[k.val * τ] (ω 0) := by
  funext k
  simpa using graphSubshift_neg hω (k.val * τ)

/-- **Deterministic is a subclass.** For an observable `h`, the delay data the
*relational* picture assigns to a `graphRel T`-trajectory is literally the delay
data the *deterministic* picture assigns to its base point.

So `orbitStream` and everything proved from it — `delayEval_orbitStream`,
`delayQueryAlgebraAtLag_eq`, the reconstruction bridge — are the `ρ = graph T`
instance of the relational description, not a separate development that happens
to look similar. -/
theorem delayEval_comp_eq_orbitStream {T : α → α} {ω : SensorStream α}
    (hω : ω ∈ Subshift (graphRel T)) (h : α → ℝ) (d τ : ℕ) :
    delayEval d τ (fun t => h (ω t)) = delayEval d τ (orbitStream h T (ω 0)) := by
  funext k
  rw [delayEval_orbitStream]
  simpa using congrArg h (graphSubshift_neg hω (k.val * τ))

/-- Positive times of a trajectory are *preimages*: `ω 0 = T^[n] (ω n)`. The
two halves of a `graphRel T`-trajectory play different roles -- the non-positive
half is the forward orbit of the base point, the positive half is a coherent
choice of backward orbit. -/
theorem graphSubshift_pos {T : α → α} {ω : SensorStream α}
    (hω : ω ∈ Subshift (graphRel T)) (n : ℕ) :
    T^[n] (ω (n : ℤ)) = ω 0 := by
  induction n with
  | zero => simp
  | succ m ih =>
      have h := hω (m : ℤ)
      simp only [graphRel] at h
      rw [show ((m : ℤ) + 1) = ((m + 1 : ℕ) : ℤ) by push_cast; ring] at h
      rw [Function.iterate_succ_apply, ← h, ih]

/-- The one thing that genuinely does not transfer: not every point is the base
of a bi-infinite trajectory. Being one forces `ω 0 ∈ range (T^[n])` for every
`n`, i.e. a full backward orbit.

This is a condition on `T` -- surjectivity onto the part of the space one cares
about -- not on delay observation, and it is the honest residue of the
"one-sided orbit" issue. A non-surjective `T` has points no relational
trajectory can be based at, while the delay data of those points is still
perfectly well defined by `orbitStream`. So the deterministic picture is the
`ρ = graph T` case of the relational one *on delay data*, which is what the
theory observes, and is strictly larger in base points. -/
theorem graphSubshift_base_mem_range {T : α → α} {ω : SensorStream α}
    (hω : ω ∈ Subshift (graphRel T)) (n : ℕ) :
    ω 0 ∈ Set.range (T^[n]) :=
  ⟨ω (n : ℤ), graphSubshift_pos hω n⟩

end RelationalDelay
end QuerySystem
