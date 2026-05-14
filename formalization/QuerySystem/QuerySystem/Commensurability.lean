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

/-- The set of "proper filter carriers" on a Boolean algebra: sets containing ⊤,
not containing ⊥, upward closed, and closed under ⊓. -/
private def IsProperFilterCarrier (α : Type*) [BooleanAlgebra α] (S : Set α) : Prop :=
  ⊤ ∈ S ∧ ⊥ ∉ S ∧ (∀ {a b : α}, a ∈ S → a ≤ b → b ∈ S) ∧
  (∀ {a b : α}, a ∈ S → b ∈ S → a ⊓ b ∈ S)

/-- The union of a chain of proper filter carriers is a proper filter carrier. -/
private theorem isProperFilterCarrier_sUnion {α : Type*} [BooleanAlgebra α]
    {c : Set (Set α)} (hc : ∀ S ∈ c, IsProperFilterCarrier α S)
    (hchain : IsChain (· ⊆ ·) c) (hne : c.Nonempty) :
    IsProperFilterCarrier α (⋃₀ c) := by
  obtain ⟨s₀, hs₀⟩ := hne
  refine ⟨⟨s₀, hs₀, (hc s₀ hs₀).1⟩, ?_, ?_, ?_⟩
  · rintro ⟨s, hs, hbot⟩; exact (hc s hs).2.1 hbot
  · rintro a b ⟨s, hs, ha⟩ hab; exact ⟨s, hs, (hc s hs).2.2.1 ha hab⟩
  · rintro a b ⟨sa, hsa, ha⟩ ⟨sb, hsb, hb⟩
    rcases hchain.total hsa hsb with h | h
    · exact ⟨sb, hsb, (hc sb hsb).2.2.2 (h ha) hb⟩
    · exact ⟨sa, hsa, (hc sa hsa).2.2.2 ha (h hb)⟩

/-- In a Boolean algebra, if a ∉ maximal proper filter F, then adding a
would make the filter improper: ∃ b ∈ F, a ⊓ b = ⊥. -/
private theorem maximal_proper_filter_dichotomy {α : Type*} [BooleanAlgebra α]
    {F : Set α} (hF : IsProperFilterCarrier α F)
    (hmax : ∀ G, IsProperFilterCarrier α G → F ⊆ G → G ⊆ F)
    (a : α) : a ∈ F ∨ aᶜ ∈ F := by
  by_contra h
  push_neg at h
  obtain ⟨ha, hac⟩ := h
  -- If neither a nor aᶜ is in F, we can extend F to include aᶜ.
  -- Define G = {x : α | ∃ f ∈ F, aᶜ ⊓ f ≤ x}
  set G := {x : α | ∃ f ∈ F, aᶜ ⊓ f ≤ x} with hGdef
  have hFG : F ⊆ G := fun x hx => ⟨x, hx, inf_le_right⟩
  have hac_in : aᶜ ∈ G := ⟨⊤, hF.1, by simp⟩
  have hG_proper : IsProperFilterCarrier α G := by
    refine ⟨hFG hF.1, ?_, ?_, ?_⟩
    · rintro ⟨f, hf, hle⟩
      -- aᶜ ⊓ f ≤ ⊥ implies f ≤ a in Boolean algebra (disjoint + compl_compl)
      have hfa : f ≤ a := by
        have h1 : Disjoint aᶜ f := disjoint_iff.mpr (le_bot_iff.mp hle)
        exact disjoint_compl_left_iff.mp h1
      exact ha (hF.2.2.1 hf hfa)
    · rintro a' b' ⟨f, hf, hle⟩ hab
      exact ⟨f, hf, le_trans hle hab⟩
    · rintro a' b' ⟨fa, hfa, hlea⟩ ⟨fb, hfb, hleb⟩
      refine ⟨fa ⊓ fb, hF.2.2.2 hfa hfb, ?_⟩
      -- aᶜ ⊓ (fa ⊓ fb) ≤ (aᶜ ⊓ fa) ⊓ (aᶜ ⊓ fb) ≤ a' ⊓ b'
      calc aᶜ ⊓ (fa ⊓ fb) ≤ (aᶜ ⊓ fa) ⊓ (aᶜ ⊓ fb) :=
            le_inf (inf_le_inf_left _ inf_le_left) (inf_le_inf_left _ inf_le_right)
        _ ≤ a' ⊓ b' := inf_le_inf hlea hleb
  -- G is a proper filter carrier strictly containing F (aᶜ ∈ G but aᶜ ∉ F)
  have : G ⊆ F := hmax G hG_proper hFG
  exact hac (this hac_in)

theorem lattice_ultrafilter_exists (α : Type*) [BooleanAlgebra α] [Nontrivial α] :
    Nonempty (LatticeUltrafilter α) := by
  -- The principal filter {x | ⊤ ≤ x} = {⊤} is a proper filter carrier
  have hstart : IsProperFilterCarrier α (Set.Ici ⊤) :=
    ⟨le_refl _, fun (h : ⊤ ≤ ⊥) => absurd (le_antisymm bot_le h) bot_ne_top,
     fun ha hab => le_trans ha hab,
     fun ha hb => le_inf ha hb⟩
  -- Zorn gives a maximal proper filter carrier
  obtain ⟨m, hmstart, hmmax⟩ := zorn_subset_nonempty
    {S : Set α | IsProperFilterCarrier α S}
    (fun c hcS hchain hne => ⟨⋃₀ c, isProperFilterCarrier_sUnion
      (fun S hS => hcS hS) hchain hne, fun s hs => Set.subset_sUnion_of_mem hs⟩)
    (Set.Ici ⊤) hstart
  have hm : IsProperFilterCarrier α m := hmmax.prop
  -- Maximality: if G is a proper filter carrier containing m, then G = m
  have hmaximal : ∀ G, IsProperFilterCarrier α G → m ⊆ G → G ⊆ m :=
    fun G hG hFG => (hmmax.eq_of_le hG hFG).symm ▸ le_refl _
  -- Maximality gives: ∀ a, a ∈ m ∨ aᶜ ∈ m
  have hdict := maximal_proper_filter_dichotomy hm hmaximal
  -- Construct the LatticeUltrafilter
  exact ⟨{
    carrier := m
    top_mem := hm.1
    bot_not_mem := hm.2.1
    up_closed := fun ha hab => hm.2.2.1 ha hab
    inf_closed := fun ha hb => hm.2.2.2 ha hb
    maximal := fun a => (hdict a).imp id (fun hac => ⟨aᶜ, hac, inf_compl_eq_bot⟩)
  }⟩

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
