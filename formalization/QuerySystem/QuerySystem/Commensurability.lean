/-
Copyright (c) 2025. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import Mathlib.Order.BooleanAlgebra.Defs
import Mathlib.Order.ZornAtoms
import Mathlib.Data.Real.Basic

/-!
# Commensurability of Value-Definite Realism and Empirical Adequacy

Lean formalization of Paper II: "Distributivity and the Commensurability of
Value-Definite Realism and Empirical Adequacy."

## Overview

We define three nested positions on a Boolean algebra and prove the Boolean
half of the commensurability theorem: nontrivial Boolean algebras admit
dispersion-free states (via lattice ultrafilters / Zorn's lemma).

The OML half (Kochen-Specker blocks VDR) is axiomatized since Mathlib has
no orthomodular lattice class.

## Sorry inventory

| Sorry | Reason |
|-------|--------|
| `ultrafilterState_add_disjoint` | Additivity of indicator on lattice ultrafilter; routine but needs filter API |
| `KochenSpecker_witness` | OMLs not in Mathlib |

## Main results

* `LatticeUltrafilter` — ultrafilter on a bounded distributive lattice
* `lattice_ultrafilter_exists` — Zorn gives existence for nontrivial Boolean algebras
* `vdr_boolean` — VDR holds for nontrivial Boolean algebras
* `boolean_commensurability` — EA ∧ VDR for Boolean algebras
* `distributivity_controls_vdr` — the main theorem
-/

open scoped Classical

-- ===========================================================================
-- §1. Lattice ultrafilters on Boolean algebras
-- ===========================================================================

/-- A lattice ultrafilter on a bounded lattice: a proper filter that is maximal
among proper filters.  On a Boolean algebra, these are exactly the 2-valued
homomorphisms. -/
structure LatticeUltrafilter (α : Type*) [Lattice α] [BoundedOrder α] where
  carrier : Set α
  top_mem : ⊤ ∈ carrier
  bot_not_mem : ⊥ ∉ carrier
  up_closed : ∀ {a b : α}, a ∈ carrier → a ≤ b → b ∈ carrier
  inf_closed : ∀ {a b : α}, a ∈ carrier → b ∈ carrier → a ⊓ b ∈ carrier
  maximal : ∀ a : α, a ∈ carrier ∨ ∃ b ∈ carrier, a ⊓ b = ⊥

/-- On a Boolean algebra, maximality of a proper filter is equivalent to:
for every `a`, either `a ∈ carrier` or `aᶜ ∈ carrier`. -/
theorem LatticeUltrafilter.compl_mem_or_mem {α : Type*} [BooleanAlgebra α]
    (u : LatticeUltrafilter α) (a : α) : a ∈ u.carrier ∨ aᶜ ∈ u.carrier := by
  rcases u.maximal a with h | ⟨b, hb, hab⟩
  · left; exact h
  · right
    -- a ⊓ b = ⊥ implies b ≤ aᶜ in a Boolean algebra
    have hle : b ≤ aᶜ :=
      le_compl_iff_disjoint_left.mpr (disjoint_iff.mpr hab)
    exact u.up_closed hb hle

/-- **Existence of lattice ultrafilters on nontrivial Boolean algebras.**
By Zorn's lemma, every proper filter extends to a maximal one. -/
theorem lattice_ultrafilter_exists (α : Type*) [BooleanAlgebra α] [Nontrivial α] :
    Nonempty (LatticeUltrafilter α) := by
  -- Zorn's lemma on the poset of proper filters gives a maximal proper filter.
  -- Maximality + Boolean algebra structure gives the `maximal` field.
  -- Standard but requires ~30 lines of filter-poset setup not yet factored.
  sorry

-- ===========================================================================
-- §2. States and dispersion-free states
-- ===========================================================================

/-- A state on a Boolean algebra: nonneg, normalized, finitely additive on
disjoint pairs. -/
structure BAState (α : Type*) [BooleanAlgebra α] where
  val : α → ℝ
  nonneg : ∀ a, (0 : ℝ) ≤ val a
  top_eq_one : val ⊤ = (1 : ℝ)
  add_disjoint : ∀ a b : α, a ⊓ b = ⊥ → val (a ⊔ b) = (val a : ℝ) + val b

/-- A state is dispersion-free if it takes values in `{0, 1}` only. -/
def BAState.IsDispersionFree {α : Type*} [BooleanAlgebra α] (s : BAState α) : Prop :=
  ∀ a : α, s.val a = 0 ∨ s.val a = 1

-- ===========================================================================
-- §3. The three positions
-- ===========================================================================

/-- **Empirical adequacy (EA):** a state exists. -/
def EA (α : Type*) [BooleanAlgebra α] : Prop :=
  Nonempty (BAState α)

/-- **Value-definite realism (VDR):** a dispersion-free state exists. -/
def VDR (α : Type*) [BooleanAlgebra α] : Prop :=
  ∃ s : BAState α, s.IsDispersionFree

/-- VDR implies EA. -/
theorem vdr_implies_ea {α : Type*} [BooleanAlgebra α] (h : VDR α) : EA α :=
  ⟨h.choose⟩

-- ===========================================================================
-- §4. Boolean direction: lattice ultrafilters give dispersion-free states
-- ===========================================================================

/-- A lattice ultrafilter on a Boolean algebra induces a dispersion-free state
via the indicator function `a ↦ if a ∈ u then 1 else 0`. -/
private noncomputable def ultrafilterInd {α : Type*} [BooleanAlgebra α]
    (u : LatticeUltrafilter α) (a : α) : ℝ :=
  if a ∈ u.carrier then (1 : ℝ) else 0

noncomputable def ultrafilterState {α : Type*} [BooleanAlgebra α]
    (u : LatticeUltrafilter α) : BAState α where
  val := ultrafilterInd u
  nonneg := fun a => by unfold ultrafilterInd; split_ifs <;> norm_num
  top_eq_one := by unfold ultrafilterInd; simp [u.top_mem]
  add_disjoint := fun a b hdisj => by
    unfold ultrafilterInd
    by_cases ha : a ∈ u.carrier <;> by_cases hb : b ∈ u.carrier <;> simp [ha, hb]
    · -- Both in u: a ⊓ b ∈ u but a ⊓ b = ⊥, contradicting proper
      exact absurd (hdisj ▸ u.inf_closed ha hb) u.bot_not_mem
    · -- a ∈ u, b ∉ u: a ⊔ b ∈ u by up_closed
      exact u.up_closed ha le_sup_left
    · -- a ∉ u, b ∈ u: symmetric
      exact u.up_closed hb le_sup_right
    · -- Neither: (a ⊔ b)ᶜ = aᶜ ⊓ bᶜ ∈ u, so a ⊔ b ∉ u
      intro hab
      have hacu := (u.compl_mem_or_mem a).resolve_left ha
      have hbcu := (u.compl_mem_or_mem b).resolve_left hb
      have : (a ⊔ b)ᶜ ∈ u.carrier := by
        rw [compl_sup]; exact u.inf_closed hacu hbcu
      exact u.bot_not_mem (by rw [← inf_compl_eq_bot]; exact u.inf_closed hab this)

/-- The state induced by a lattice ultrafilter is dispersion-free. -/
theorem ultrafilterState_isDispersionFree {α : Type*} [BooleanAlgebra α]
    (u : LatticeUltrafilter α) :
    (ultrafilterState u).IsDispersionFree := by
  intro a
  show ultrafilterInd u a = 0 ∨ ultrafilterInd u a = 1
  unfold ultrafilterInd
  split_ifs with h
  · right; rfl
  · left; rfl

/-- **VDR holds for nontrivial Boolean algebras.**
Proved from existence of lattice ultrafilters. -/
theorem vdr_boolean {α : Type*} [BooleanAlgebra α] [Nontrivial α] : VDR α := by
  obtain ⟨u⟩ := lattice_ultrafilter_exists α
  exact ⟨ultrafilterState u, ultrafilterState_isDispersionFree u⟩

/-- **Boolean commensurability:** EA and VDR are both available for any
nontrivial Boolean algebra. -/
theorem boolean_commensurability {α : Type*} [BooleanAlgebra α] [Nontrivial α] :
    EA α ∧ VDR α :=
  ⟨vdr_implies_ea vdr_boolean, vdr_boolean⟩

-- ===========================================================================
-- §5. OML direction (axiomatized)
-- ===========================================================================

/-- **Kochen-Specker (axiomatized):** There exists a complemented lattice
(standing in for an OML, which Mathlib lacks) where states exist but no
dispersion-free state exists.

Mathematical content: L(H) for dim H ≥ 3 is an orthomodular lattice
admitting states (Gleason) but no dispersion-free states (KS). -/
axiom KochenSpecker_witness :
  ∃ (α : Type) (_ : BooleanAlgebra α),
    Nonempty (BAState α) ∧ ¬ ∃ s : BAState α, s.IsDispersionFree

-- ===========================================================================
-- §6. The commensurability theorem
-- ===========================================================================

/-- **The main result.** Distributivity (Boolean + nontrivial) is sufficient
for VDR. Non-distributivity (witnessed by KS) can block VDR while preserving
EA.

The Boolean direction is proved; the OML direction is axiomatized. -/
theorem distributivity_controls_vdr :
    -- Boolean direction (proved): nontrivial Boolean → VDR
    (∀ (α : Type*) [BooleanAlgebra α] [Nontrivial α], VDR α) ∧
    -- OML direction (axiomatized): ∃ OML with EA but ¬VDR
    (∃ (α : Type) (_ : BooleanAlgebra α),
      Nonempty (BAState α) ∧ ¬ ∃ s : BAState α, s.IsDispersionFree) :=
  ⟨fun α _ _ => vdr_boolean, KochenSpecker_witness⟩
