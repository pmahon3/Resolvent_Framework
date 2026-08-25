/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.DelayEmbedding
import QuerySystem.SigmaEssentialAmended
import QuerySystem.UlamWitnessMain

/-!
# C1′: the σ-essential pathology cannot occur in the data regime

`papers/reconstruction/notes/commensurability_classification_seed.md` §2.3 lists
this as a licensing result to be proved:

> **C1′ (quarantine)**: finite-alphabet delay logics are compact/clopen, so the
> σ-essential pathology provably cannot occur in the data regime — the
> reconstruction foundations are *secured*, not threatened, by the witness.

This file proves it, and the proof says the reason is not the one the note
gives.

## Finiteness is not what does the work

The σ-essential witness needs a carrier that is a **proper σ-class**: a Dynkin
system that is *not* closed under intersection. That is not an incidental
feature of the construction, it is forced — `carrier_not_interClosed` derives it
from the witness's own existence, and `val_inter` is the one step where
distributivity is spent.

A query system's outcome space carries a `MeasurableSpace`, i.e. a σ-algebra,
and a σ-algebra is intersection-closed by definition. So the quarantine holds
for **every** query outcome logic, at any alphabet, finite or not, compact or
not. Clopen-ness and finiteness are true of the data regime and irrelevant to
the conclusion; what matters is that observational outcomes are measurable sets.

That is a stronger result than C1′ as stated and a cheaper one, and the
cheapness is the content: the reconstruction lane never had to worry, because
its objects are σ-algebras and the pathology lives strictly outside them.

## The scope, stated honestly

This quarantines the **carrier**. It says no local pattern on a σ-algebra
carrier is σ-essential. It does **not** say the data regime is free of
contextuality: EA-without-PR gaps are about families of states across contexts,
a different axis, and the pruning/commensurability lane is exactly where those
live. Nothing here bears on them.

## Main results
* `interClosed_ofMeasurableSpace` — a σ-algebra's Dynkin system is Boolean.
* `no_witness_ofMeasurableSpace` — hence it carries no σ-essential witness.
* `query_no_witness` — specialised to any query's outcome logic.
* `delayQuery_no_witness` — C1′ as stated, for the delay logic at any alphabet.
* `witness_carrier_not_ofMeasurableSpace` — the separation is real: the witness
  carrier is not the Dynkin system of any σ-algebra.
-/

namespace QuerySystem
namespace Quarantine

open MeasurableSpace SigmaEssential SigmaEssential.Amended

/-- **A σ-algebra is a Boolean carrier.** `DynkinSystem.ofMeasurableSpace m` has
`Has = MeasurableSet[m]`, and σ-algebras are closed under binary intersection —
so the pivot predicate `InterClosed` holds outright. -/
theorem interClosed_ofMeasurableSpace {Ω : Type*} (m : MeasurableSpace Ω) :
    InterClosed (DynkinSystem.ofMeasurableSpace m) := by
  intro A A' hA hA'
  exact MeasurableSet.inter hA hA'

/-- **The quarantine.** No local pattern on a σ-algebra carrier is σ-essential.

Immediate from `boolean_no_witness_amended` once `InterClosed` is available, and
that is the point: the σ-essential lane's own Boolean baseline already contains
the quarantine, and all the data regime has to do to be safe is be measurable. -/
theorem no_witness_ofMeasurableSpace {Ω : Type*} (m : MeasurableSpace Ω)
    (B : Block (DynkinSystem.ofMeasurableSpace m))
    (s₀ : LocalState (DynkinSystem.ofMeasurableSpace m) B) :
    ¬ IsSigmaEssentialL s₀ :=
  boolean_no_witness_amended (interClosed_ofMeasurableSpace m) s₀

/-- **Every query's outcome logic is quarantined.** A `Query` bundles an outcome
type with a `MeasurableSpace`, so its logic is Boolean and no σ-essential
witness lives on it. No hypothesis on the query at all. -/
theorem query_no_witness (q : Query)
    (B : Block (DynkinSystem.ofMeasurableSpace q.instMeas))
    (s₀ : LocalState (DynkinSystem.ofMeasurableSpace q.instMeas) B) :
    ¬ IsSigmaEssentialL s₀ :=
  no_witness_ofMeasurableSpace q.instMeas B s₀

/-- **C1′, for the delay logic.** The delay query at depth `d` and lag `τ` over
any alphabet carries no σ-essential witness. The seed states this for a finite
alphabet; finiteness is not used, and neither is compactness. -/
theorem delayQuery_no_witness (A : Type u) [MeasurableSpace A] (d τ : ℕ)
    (B : Block (DynkinSystem.ofMeasurableSpace (delayQuery A d τ).instMeas))
    (s₀ : LocalState (DynkinSystem.ofMeasurableSpace (delayQuery A d τ).instMeas) B) :
    ¬ IsSigmaEssentialL s₀ :=
  query_no_witness (delayQuery A d τ) B s₀

/-- **The separation is real, not a hypothesis nothing violates.** The witness
carrier is a Dynkin system that is not the Dynkin system of *any* σ-algebra:
every one of those is intersection-closed, and `carrier_not_interClosed` says
this one is not.

So the two regimes are genuinely disjoint, and that — rather than finiteness or
compactness — is the whole of C1′. -/
theorem witness_carrier_not_ofMeasurableSpace
    (m : MeasurableSpace (SigmaEssential.Ulam.M₁ × Fin 4)) :
    SigmaEssential.Ulam.L₁ ≠ DynkinSystem.ofMeasurableSpace m := by
  intro h
  refine SigmaEssential.Ulam.carrier_not_interClosed ?_
  rw [h]
  exact interClosed_ofMeasurableSpace m

end Quarantine
end QuerySystem
