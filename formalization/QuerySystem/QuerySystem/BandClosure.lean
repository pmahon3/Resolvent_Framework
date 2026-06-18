/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import Mathlib.Data.Set.Lattice
import Mathlib.Data.Set.Prod
import Mathlib.Data.Set.Countable
import Mathlib.Data.Set.Pairwise.Basic

/-!
# Band-family closure: the Session-8 relative-complement chain (Bite 1)

A **concrete** orthomodular logic à la Kalmbach is just a sub-collection of
`Set Ω` closed under complement and (countable) disjoint union: the
orthocomplement is set-complement, the orthogonal join is disjoint union, and
blocks are derived, not primitive. So the σ-essential descent substrate lives
entirely in `Set Ω` combinatorics — **no orthomodular-lattice typeclass is ever
instantiated.** This file therefore escapes the standing "Mathlib v4.29 has no
OML/Foulis–Holland" wall: it formalizes the substrate, not abstract OML theory.

## What this certifies

The **Session-8 finding** (`sigma_essential_construction_attempt`, Session 8):
the band-family trichotomy collapses to a dichotomy because, for *every*
finite-∪-closed index family `ℐ`, a **two-relative-complement chain** forces the
forbidden finite set `(Sα ∩ Sβ) ×ˢ {j}` into the closure at the **finite
pre-σ level**, for *any* binding pair `Sα, Sβ` and *any difference size*:

* Step 1: `Sα ⊆ Sα ∪ Sβ` (both indices in `ℐ`), comparable ⟹
  `(Sα ∪ Sβ) \ Sα = Sβ \ Sα` cells are in the closure.
* Step 2: `Sβ \ Sα ⊆ Sβ`, comparable ⟹
  `Sβ \ (Sβ \ Sα) = Sα ∩ Sβ` cells are in the closure.

The workhorse is `relCompl`: relative complement of a **comparable** pair is in
any complement-and-disjoint-union-closed collection, because
`B \ A = (Bᶜ ∪ A)ᶜ` and `A ⊆ B` makes `A` and `Bᶜ` disjoint. Lean makes that
disjointness obligation **non-skippable** — it is exactly the by-hand "legality
check" that the difference size is irrelevant.

The band chain is **finitary** (binary disjoint union suffices). The **σ-step**
to "Boolean / `= P(Ω)`" needs **countable disjoint union** (`csUnion`): the
Session-8 chain manufactures the forbidden finite cells / singletons via
`relCompl`, and then `forces_boolean` *assembles* every subset as the countable
disjoint union of its singletons. Crucially the assembly is by disjoint union,
NOT intersection — the Session-7 prose "`{x}` = countable ∩" was the wrong route
(intersection is not a concrete-logic operation; it computes the Boolean
σ-algebra, not the concrete-logic σ-closure, which is the very crux).

## Main results

* `InClosure` — the closure predicate (generators, `∅`, complement, binary
  disjoint union `dunion`, **countable disjoint union `csUnion`**). The
  constructor set is *exactly* `{complement, countable disjoint union}`.
* `relCompl` — relative complement of a comparable pair stays in the closure.
* `band_chain` — abstract two-step chain: from cells for `Sα`, `Sα ∪ Sβ`, `Sβ`,
  the cell for `Sα ∩ Sβ` is in the closure.
* `band_chain_inter` — the Session-8 specialization on `Ω = ℕ × ℕ`: the
  forbidden finite cell `(Sα ∩ Sβ) ×ˢ {j}` is forced in.
* `forces_boolean` — on a **countable** `Ω`, all singletons in the closure ⟹
  *every* subset is (the full power set `P(Ω)`), via assembly by countable
  disjoint union. "Boolean" = `∀ A, InClosure G A`, not just `univ ∈ InClosure`.

**Zero sorry, zero new axioms.**
-/

namespace QuerySystem
namespace BandClosure

variable {Ω : Type*}

/-- **The concrete-logic closure predicate.** Given a generating collection
`G : Set (Set Ω)`, `InClosure G` is the smallest family of subsets of `Ω`
containing every generator and `∅`, and closed under set-complement and
**binary disjoint union** (the disjointness side-condition is what makes the
union an *orthogonal* join in the concrete logic).

The orthogonal join is **countable disjoint union** (`csUnion`), matching
σ-completeness; binary `dunion` is the finite special case. The constructor set
is *exactly* `{complement, countable disjoint union}` — intersection / arbitrary
(non-disjoint) union are deliberately absent, because each would collapse the
concrete logic toward Boolean and destroy the only thing the closure
discriminates. -/
inductive InClosure (G : Set (Set Ω)) : Set Ω → Prop
  | gen {A : Set Ω} (h : A ∈ G) : InClosure G A
  | empty : InClosure G (∅ : Set Ω)
  | compl {A : Set Ω} (h : InClosure G A) : InClosure G Aᶜ
  | dunion {A B : Set Ω} (hA : InClosure G A) (hB : InClosure G B)
      (hdisj : Disjoint A B) : InClosure G (A ∪ B)
  | csUnion {S : Set (Set Ω)} (hS : S.Countable) (hmem : ∀ A ∈ S, InClosure G A)
      (hdisj : S.PairwiseDisjoint id) : InClosure G (⋃₀ S)

namespace InClosure

variable {G : Set (Set Ω)}

/-- The full space `univ = ∅ᶜ` is in the closure. -/
theorem univ : InClosure G (Set.univ : Set Ω) := by
  simpa using (InClosure.empty (G := G)).compl

/-- **The workhorse (`relCompl`).** For a **comparable** pair `A ⊆ B` both in the
closure, the relative complement `B \ A` is in the closure.

Proof: `B \ A = (Bᶜ ∪ A)ᶜ`. The union `Bᶜ ∪ A` is a *disjoint* union precisely
because `A ⊆ B` ⟹ `A ∩ Bᶜ = ∅` — this disjointness obligation (discharged by
`hsub`) is the formal content of the by-hand "legality check": the difference
size of `B \ A` never enters. -/
theorem relCompl {A B : Set Ω} (hA : InClosure G A) (hB : InClosure G B)
    (hsub : A ⊆ B) : InClosure G (B \ A) := by
  have hdisj : Disjoint Bᶜ A := by
    rw [Set.disjoint_left]
    intro x hxBc hxA
    exact hxBc (hsub hxA)
  have hrw : B \ A = (Bᶜ ∪ A)ᶜ := by
    rw [Set.compl_union, compl_compl, Set.diff_eq, Set.inter_comm]
  rw [hrw]
  exact (hB.compl.dunion hA hdisj).compl

-- ===========================================================================
-- §  Forcing Boolean: all singletons ⟹ closure is the full power set
-- ===========================================================================

/-- The singletons of a set are pairwise disjoint: `(singleton '' A).PairwiseDisjoint id`.
Distinct singletons `{x}, {y}` (so `x ≠ y`) are disjoint. -/
theorem pairwiseDisjoint_singleton_image (A : Set Ω) :
    (Set.singleton '' A).PairwiseDisjoint id := by
  rintro _ ⟨x, _, rfl⟩ _ ⟨y, _, rfl⟩ hne
  refine Set.disjoint_singleton.2 (fun h => hne ?_)
  rw [h]

/-- **The "forces Boolean" step (Session 7, repaired).** On a **countable** `Ω`,
if every singleton is in the closure, then *every* subset is — i.e. the closure
is the full power set `P(Ω)`, so the concrete logic is Boolean.

The mechanism is **assembly by countable disjoint union**, NOT intersection:
each `A : Set Ω` is the countable disjoint union of its own singletons,
`A = ⋃₀ (singleton '' A)`, and `singleton '' A` is countable (image of the
countable `A`) and pairwise disjoint. This is why the constructor set stays
`{complement, countable disjoint union}` — the Session-7 prose "`{x}` = countable
∩" was the wrong route (intersection is not a concrete-logic operation; it would
silently compute the Boolean σ-algebra rather than the concrete-logic σ-closure).

"Boolean" here = `∀ A, InClosure G A` (the full power set), NOT merely
`univ ∈ InClosure` (which only gives the 2-element algebra `{∅, univ}`). -/
theorem forces_boolean [Countable Ω] (hsingleton : ∀ x : Ω, InClosure G {x})
    (A : Set Ω) : InClosure G A := by
  have hassemble : A = ⋃₀ (Set.singleton '' A) := by
    ext x
    simp only [Set.mem_sUnion, Set.mem_image, Set.mem_singleton_iff]
    constructor
    · intro hx; exact ⟨{x}, ⟨x, hx, rfl⟩, rfl⟩
    · rintro ⟨_, ⟨y, hy, rfl⟩, rfl⟩; exact hy
  rw [hassemble]
  refine InClosure.csUnion (((A.to_countable).image _)) ?_
    (pairwiseDisjoint_singleton_image A)
  rintro _ ⟨x, _, rfl⟩
  exact hsingleton x

end InClosure

-- ===========================================================================
-- §  The abstract band chain
-- ===========================================================================

open InClosure

/-- **The abstract two-step chain (Session 8).** Work with three "cells"
`cα ⊆ cαβ`, `cβ ⊆ cαβ` standing for `Sα ×ˢ {j}`, `(Sα ∪ Sβ) ×ˢ {j}`,
`Sβ ×ˢ {j}` (so `cα ∪ cβ = cαβ`). The hypothesis `hαβ : cα ∪ cβ = cαβ` packages
"the index family is finite-∪-closed, so `Sα ∪ Sβ ∈ ℐ`."

From the three generator cells in the closure, the meet cell `cα ∩ cβ` is forced
in by two `relCompl` applications — Step 1 extracts `cβ \ cα`, Step 2 extracts
`cβ \ (cβ \ cα) = cα ∩ cβ`. -/
theorem band_chain {G : Set (Set Ω)} {cα cβ cαβ : Set Ω}
    (hα : InClosure G cα) (hβ : InClosure G cβ) (hαβ : InClosure G cαβ)
    (hsubα : cα ⊆ cαβ) (hunion : cα ∪ cβ = cαβ) :
    InClosure G (cα ∩ cβ) := by
  -- Step 1: cβ \ cα = cαβ \ cα  (using cα ∪ cβ = cαβ), in the closure.
  have step1 : InClosure G (cαβ \ cα) := relCompl hα hαβ hsubα
  have hsub1 : cαβ \ cα ⊆ cβ := by
    rw [← hunion]; intro x hx
    rcases hx.1 with h | h
    · exact absurd h hx.2
    · exact h
  -- Step 2: cβ \ (cαβ \ cα) = cα ∩ cβ, in the closure.
  have step2 : InClosure G (cβ \ (cαβ \ cα)) := relCompl step1 hβ hsub1
  have hrw : cβ \ (cαβ \ cα) = cα ∩ cβ := by
    rw [← hunion]
    ext x
    simp only [Set.mem_diff, Set.mem_union, Set.mem_inter_iff]
    constructor
    · rintro ⟨hxβ, hxnot⟩
      have hxα : x ∈ cα := by
        by_contra hxα
        exact hxnot ⟨Or.inr hxβ, hxα⟩
      exact ⟨hxα, hxβ⟩
    · rintro ⟨hxα, hxβ⟩
      exact ⟨hxβ, fun h => h.2 hxα⟩
  rwa [hrw] at step2

-- ===========================================================================
-- §  The Session-8 specialization on  Ω = ℕ × ℕ
-- ===========================================================================

/-- A **band cell** `S ×ˢ {j}` on `Ω = ℕ × ℕ`: the action cell for row-index set
`S` in column `j`. -/
def cell (S : Set ℕ) (j : ℕ) : Set (ℕ × ℕ) := S ×ˢ {j}

@[simp] theorem mem_cell {S : Set ℕ} {j : ℕ} {p : ℕ × ℕ} :
    p ∈ cell S j ↔ p.1 ∈ S ∧ p.2 = j := by
  simp [cell, Set.mem_prod]

theorem cell_union (S T : Set ℕ) (j : ℕ) :
    cell S j ∪ cell T j = cell (S ∪ T) j := by
  ext p; simp only [mem_cell, Set.mem_union]; tauto

theorem cell_inter (S T : Set ℕ) (j : ℕ) :
    cell S j ∩ cell T j = cell (S ∩ T) j := by
  ext p; simp only [mem_cell, Set.mem_inter_iff]; tauto

theorem cell_subset_union_left (S T : Set ℕ) (j : ℕ) :
    cell S j ⊆ cell (S ∪ T) j := by
  rw [← cell_union]; exact Set.subset_union_left

theorem cell_subset_union_right (S T : Set ℕ) (j : ℕ) :
    cell T j ⊆ cell (S ∪ T) j := by
  rw [← cell_union]; exact Set.subset_union_right

/-- **The Session-8 finding, formalized.** On `Ω = ℕ × ℕ`, if the three band
cells `cell Sα j`, `cell (Sα ∪ Sβ) j`, `cell Sβ j` are all in the closure — the
middle one present exactly because the index family `ℐ` is finite-∪-closed, so
`Sα ∪ Sβ ∈ ℐ` — then the **forbidden finite cell** `cell (Sα ∩ Sβ) j` is forced
in by the two-relative-complement chain.

This is the substrate-level engine of the trichotomy → dichotomy collapse:
regime (c) is Boolean (not merely "not σ-complete"), because the meet cell enters
`L̄` at the finite pre-σ level, for *any* difference size. -/
theorem band_chain_inter {G : Set (Set (ℕ × ℕ))} {Sα Sβ : Set ℕ} {j : ℕ}
    (hα : InClosure G (cell Sα j))
    (hαβ : InClosure G (cell (Sα ∪ Sβ) j))
    (hβ : InClosure G (cell Sβ j)) :
    InClosure G (cell (Sα ∩ Sβ) j) := by
  have h := band_chain hα hβ hαβ
    (cell_subset_union_left Sα Sβ j) (cell_union Sα Sβ j)
  rwa [cell_inter] at h

/-- A singleton cell: the action cell for the single-row set `{i}` in column `j`
is the singleton `{(i, j)}`. This is the bridge from `band_chain_inter` (which
forces a *meet cell* `cell (Sα ∩ Sβ) j`) to `forces_boolean` (which consumes
*singletons*): when the AD intersection localizes to a single row, the forced
meet cell IS a singleton. -/
theorem cell_singleton (i j : ℕ) : cell {i} j = {(i, j)} := by
  ext p
  simp only [mem_cell, Set.mem_singleton_iff, Prod.ext_iff]

/-- **The two mechanisms composed — the Session-8 dichotomy, Boolean half,
formalized end to end.** On the band substrate `Ω = ℕ × ℕ`, suppose the
`relCompl` chain forces in every singleton cell `cell {i} j` (this is the output
of `band_chain_inter` whenever the binding AD intersection `Sα ∩ Sβ` localizes to
a single row at column `j`). Then the closure is the **full power set** `P(ℕ×ℕ)`,
i.e. the concrete logic is Boolean.

`relCompl` *manufactures* the forbidden finite cells down to singletons;
`forces_boolean` *assembles* every subset from them by countable disjoint union.
This certifies the `∪-closed ⟹ Boolean` half of the dichotomy — a **known
negative** (it kills the band route, the Sessions 6–7 frontier), and so serves as
the integration test of `csUnion`, not as progress on the open question. -/
theorem band_forces_boolean {G : Set (Set (ℕ × ℕ))}
    (hsingleton : ∀ i j : ℕ, InClosure G (cell {i} j)) (A : Set (ℕ × ℕ)) :
    InClosure G A := by
  refine InClosure.forces_boolean (fun p => ?_) A
  have := hsingleton p.1 p.2
  rwa [cell_singleton, Prod.mk.eta] at this

end BandClosure
end QuerySystem
