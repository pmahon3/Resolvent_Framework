/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import Mathlib.Data.Set.Image

/-!
# One-step reflection on a fibre product

The theorem isolates the set-theoretic core of the one-step adjacent-assembly
reflection argument.  An `X`-cylinder and a `Y`-cylinder are disjoint on the
fibre product.  If their union is independent of the `Y` coordinate, then
membership in the `Y` event is constant on every fibre, so that event descends
to the common boundary.

No lattice, orthomodular, finiteness, or sigma-completeness claim is made.
-/

namespace QuerySystem
namespace FibreProductReflection

universe u v w

/-- A surjective coordinate map gives a faithful cylinder embedding. -/
theorem preimage_injective_of_surjective
    {X : Type u} {D : Type w} (f : X → D) (hf : Function.Surjective f) :
    Function.Injective (fun T : Set D => f ⁻¹' T) := by
  intro S T h
  ext d
  obtain ⟨x, rfl⟩ := hf d
  exact Set.ext_iff.mp h x

/-- If a disjoint union of an `X`-cylinder and a `Y`-cylinder is
`X`-cylindrical on `X ×_D Y`, then membership in the `Y` event is constant
on fibres of `g`.

`hCyl` is the membership form of `X`-cylindricity: changing only the
`Y` coordinate inside one fibre does not change membership in the union.
Surjectivity of `f` supplies an `X` point over each relevant `Y` fibre. -/
theorem membership_constant_on_fibres
    {X : Type u} {Y : Type v} {D : Type w}
    (f : X → D) (g : Y → D) (A : Set X) (B : Set Y)
    (hf : Function.Surjective f)
    (hDisjoint :
      ∀ x y, f x = g y → ¬ (x ∈ A ∧ y ∈ B))
    (hCyl :
      ∀ x y₁ y₂,
        f x = g y₁ →
        f x = g y₂ →
        (x ∈ A ∨ y₁ ∈ B ↔ x ∈ A ∨ y₂ ∈ B)) :
    ∀ y₁ y₂, g y₁ = g y₂ → (y₁ ∈ B ↔ y₂ ∈ B) := by
  intro y₁ y₂ hEq
  obtain ⟨x, hx⟩ := hf (g y₁)
  have hx₁ : f x = g y₁ := hx
  have hx₂ : f x = g y₂ := hx.trans hEq
  constructor
  · intro hy₁
    have hu : x ∈ A ∨ y₂ ∈ B :=
      (hCyl x y₁ y₂ hx₁ hx₂).mp (Or.inr hy₁)
    cases hu with
    | inl hxA => exact (hDisjoint x y₁ hx₁ ⟨hxA, hy₁⟩).elim
    | inr hy₂ => exact hy₂
  · intro hy₂
    have hu : x ∈ A ∨ y₁ ∈ B :=
      (hCyl x y₂ y₁ hx₂ hx₁).mp (Or.inr hy₂)
    cases hu with
    | inl hxA => exact (hDisjoint x y₂ hx₂ ⟨hxA, hy₂⟩).elim
    | inr hy₁ => exact hy₁

/-- Under the same hypotheses, the `Y` event is the inverse image of a set
on the common boundary.  The boundary set can be taken to be `g '' B`. -/
theorem exists_boundary_trace
    {X : Type u} {Y : Type v} {D : Type w}
    (f : X → D) (g : Y → D) (A : Set X) (B : Set Y)
    (hf : Function.Surjective f)
    (hDisjoint :
      ∀ x y, f x = g y → ¬ (x ∈ A ∧ y ∈ B))
    (hCyl :
      ∀ x y₁ y₂,
        f x = g y₁ →
        f x = g y₂ →
        (x ∈ A ∨ y₁ ∈ B ↔ x ∈ A ∨ y₂ ∈ B)) :
    ∃ T : Set D, B = g ⁻¹' T := by
  refine ⟨g '' B, Set.ext ?_⟩
  intro y
  constructor
  · intro hy
    exact ⟨y, hy, rfl⟩
  · rintro ⟨y', hy', hgy'⟩
    exact (membership_constant_on_fibres f g A B hf hDisjoint hCyl
      y' y hgy').mp hy'

#print axioms membership_constant_on_fibres
#print axioms exists_boundary_trace
#print axioms preimage_injective_of_surjective

end FibreProductReflection
end QuerySystem
