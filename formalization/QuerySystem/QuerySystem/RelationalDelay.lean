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

Specialising pruning to a deterministic `ρ` trivialises it: a functional graph
has out-degree one, so its cycles are vertex-disjoint and `IsLISC ρ k L`
collapses to "some cycle has length exactly `k*L`". Theorem P's content is in
the nondeterministic case. So the join has to carry the delay side up to
relations, not push pruning down to maps.

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

## What is not proved, and why not

The deterministic embedding is **absent on purpose**. `stateStream T x` --
`t ↦ T^[(-t).toNat] x` -- is *not* a member of `Subshift (graph T)`: `Int.toNat`
clamps the positive half to the constant `x`, so the trajectory condition there
would demand `x = T x`. A non-invertible `T` genuinely has only a one-sided
orbit, and pretending otherwise is the kind of statement that typechecks and
says nothing. Bi-infinite trajectories for deterministic dynamics need `T`
bijective, or a one-sided stream type; neither is assumed here, and the bridge
below does not need either, because a LISC witness supplies a genuinely
bi-infinite periodic trajectory outright.
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

end RelationalDelay
end QuerySystem
