/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import Mathlib.Order.Lattice
import Mathlib.Order.BoundedOrder.Basic
import Mathlib.Tactic.DeriveFintype

/-!
# MO₂ as a verified finite orthomodular lattice (Rung 1)

First rung of the (β)-swap formalization. We define a minimal
`OrthomodularLattice` class (Mathlib has none) and give `MO₂` — the horizontal
sum of two 4-element Boolean blocks, i.e. `0, 1` with two complementary pairs of
incomparable atoms `a, aᗮ, b, bᗮ` — as an explicit, fully verified instance.

The payload is **the gap** (`MO2.gap`): the meet-zero ≠ orthogonal phenomenon
that drives the whole descent question,
`a ⊓ b = ⊥  ∧  ¬ a ≤ bᗮ`,
proved by `decide` on the finite structure.

Everything finite here is decidable; the lattice, bounded-order, and
orthomodular laws are all discharged by `decide`, so this rung is **zero sorry**
and de-risks the OML definition before the product/witness rungs depend on it.

## Main definitions
* `OrthomodularLattice` — bounded lattice + orthocomplement with the three
  orthocomplementation laws and the orthomodular law.
* `MO2` — the six-element lattice, with all instances.

## Main results
* `MO2.gap` — `a ⊓ b = ⊥ ∧ ¬ a ≤ bᗮ` (meet-zero but not orthogonal).
* `MO2.instOrthomodularLattice` — `MO2` is an orthomodular lattice (no sorry).
-/

namespace QuerySystem

-- ===========================================================================
-- §1. The OrthomodularLattice class
-- ===========================================================================

/-- A (bounded) orthomodular lattice: a bounded lattice with an
orthocomplement `ᗮ` satisfying

* complement: `a ⊓ aᗮ = ⊥` and `a ⊔ aᗮ = ⊤`;
* involution: `aᗮᗮ = a`;
* order-reversing: `a ≤ b → bᗮ ≤ aᗮ`;
* orthomodular law: `a ≤ b → a ⊔ (aᗮ ⊓ b) = b`.

Mathlib has no orthomodular lattice class, so we define a minimal one here. -/
class OrthomodularLattice (α : Type*) extends Lattice α, BoundedOrder α where
  /-- orthocomplement -/
  ortho : α → α
  /-- `a ⊓ aᗮ = ⊥` -/
  inf_ortho : ∀ a : α, ortho a ⊓ a = ⊥
  /-- `a ⊔ aᗮ = ⊤` -/
  sup_ortho : ∀ a : α, ortho a ⊔ a = ⊤
  /-- `aᗮᗮ = a` -/
  ortho_ortho : ∀ a : α, ortho (ortho a) = a
  /-- `a ≤ b → bᗮ ≤ aᗮ` -/
  ortho_le_ortho : ∀ {a b : α}, a ≤ b → ortho b ≤ ortho a
  /-- orthomodular law: `a ≤ b → a ⊔ (aᗮ ⊓ b) = b` -/
  orthomodular : ∀ {a b : α}, a ≤ b → a ⊔ (ortho a ⊓ b) = b

@[inherit_doc] postfix:max "ᗮ" => OrthomodularLattice.ortho

-- ===========================================================================
-- §2. MO₂ as an explicit six-element type
-- ===========================================================================

/-- The six elements of `MO₂`: bottom, top, and two complementary pairs of
incomparable atoms `a, aᗮ` and `b, bᗮ`. Geometrically: two orthogonal pairs of
lines through the origin (the `+` and `×` overlaid), with `a` and `b` at 45° —
meet-zero but not orthogonal. -/
inductive MO2 where
  | bot | a | a' | b | b' | top
  deriving DecidableEq, Fintype, Repr

namespace MO2

/-- Boolean order test on `MO₂`: `⊥` below everything, `⊤` above everything, the
four atoms pairwise incomparable. Boolean-valued so decidability is automatic. -/
def leB : MO2 → MO2 → Bool
  | .bot, _ => true
  | _, .top => true
  | x, y => x == y

/-- The order on `MO₂`, induced from the Boolean test `leB`. -/
instance : LE MO2 := ⟨fun x y => leB x y = true⟩

instance decidableLE : DecidableLE MO2 :=
  fun x y => inferInstanceAs (Decidable (leB x y = true))

/-- Meet (greatest lower bound): equal arguments give that argument; `⊥` with
anything gives `⊥`; `⊤` is the identity; two distinct atoms meet at `⊥`. -/
def inf : MO2 → MO2 → MO2
  | .bot, _ => .bot
  | _, .bot => .bot
  | .top, y => y
  | x, .top => x
  | x, y => if x = y then x else .bot

/-- Join (least upper bound): the order-dual of `inf`. Distinct atoms join at
`⊤`. -/
def sup : MO2 → MO2 → MO2
  | .top, _ => .top
  | _, .top => .top
  | .bot, y => y
  | x, .bot => x
  | x, y => if x = y then x else .top

/-- Orthocomplement: swaps `⊥ ↔ ⊤`, `a ↔ aᗮ`, `b ↔ bᗮ`. -/
def compl : MO2 → MO2
  | .bot => .top
  | .top => .bot
  | .a => .a'
  | .a' => .a
  | .b => .b'
  | .b' => .b

instance : Max MO2 := ⟨sup⟩
instance : Min MO2 := ⟨inf⟩
instance : Bot MO2 := ⟨.bot⟩
instance : Top MO2 := ⟨.top⟩

/-- `MO₂` is a lattice. Every law is a finite case-check: after splitting all
arguments, each goal reduces by `rfl`/`decide`. -/
instance instLattice : Lattice MO2 where
  sup := sup
  inf := inf
  le_refl := by intro x; cases x <;> rfl
  le_trans := by intro x y z; cases x <;> cases y <;> cases z <;> decide
  le_antisymm := by intro x y; cases x <;> cases y <;> decide
  le_sup_left := by intro x y; cases x <;> cases y <;> decide
  le_sup_right := by intro x y; cases x <;> cases y <;> decide
  sup_le := by intro x y z; cases x <;> cases y <;> cases z <;> decide
  inf_le_left := by intro x y; cases x <;> cases y <;> decide
  inf_le_right := by intro x y; cases x <;> cases y <;> decide
  le_inf := by intro x y z; cases x <;> cases y <;> cases z <;> decide

/-- `MO₂` is bounded. -/
instance instBoundedOrder : BoundedOrder MO2 where
  le_top := by intro x; cases x <;> rfl
  bot_le := by intro x; cases x <;> rfl

/-- `MO₂` is an orthomodular lattice: all four orthocomplementation/orthomodular
laws hold by finite case-check. **Zero sorry.** -/
instance instOrthomodularLattice : OrthomodularLattice MO2 where
  ortho := compl
  inf_ortho := by intro x; cases x <;> rfl
  sup_ortho := by intro x; cases x <;> rfl
  ortho_ortho := by intro x; cases x <;> rfl
  ortho_le_ortho := by intro x y h; cases x <;> cases y <;> first | rfl | (revert h; decide)
  orthomodular := by intro x y h; cases x <;> cases y <;> first | rfl | (revert h; decide)

-- ===========================================================================
-- §3. The gap: meet-zero ≠ orthogonal
-- ===========================================================================

/-- **The gap.** In `MO₂`, the atoms `a` and `b` have meet `⊥` (no shared
content) yet `a` is *not* orthogonal to `b` (`¬ a ≤ bᗮ`, i.e. `¬ a ≤ b'`). This
is the defining non-distributive phenomenon that the entire descent question
turns on, here proved by `decide`. -/
theorem gap : (a ⊓ b = ⊥) ∧ ¬ (a ≤ bᗮ) := by
  refine ⟨rfl, ?_⟩; intro h; exact absurd h (by decide)

/-- For later rungs: `a` and `b` are genuinely incomparable, and the gap is
symmetric (`b ⊓ a = ⊥ ∧ ¬ b ≤ aᗮ`). -/
theorem gap_symm : (b ⊓ a = ⊥) ∧ ¬ (b ≤ aᗮ) := by
  refine ⟨rfl, ?_⟩; intro h; exact absurd h (by decide)

/-- `a` and `aᗮ` *are* orthogonal — the contrast that makes "gap" meaningful. -/
theorem a_ortho_a' : a ≤ (a')ᗮ := rfl

end MO2

end QuerySystem
