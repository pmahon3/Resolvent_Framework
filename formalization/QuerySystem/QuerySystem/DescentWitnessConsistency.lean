/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.DescentWitnessFinite

/-!
# Consistency of the Rung-3 axioms (a concrete model)

`DescentWitnessInfinite.lean` axiomatizes Navara's infinite construction and
proves `(★)` on top. Axioms are only meaningful if they are **consistent** —
otherwise `(★)` would be vacuously (and worthlessly) true.

This file discharges that obligation by exhibiting an explicit **model** of every
Rung-3 axiom: take `L₂ := (ℕ → MO₂)` with all operations coordinatewise (the
honest infinite analogue of the Rung-2 finite truncation), the witness
`p := fun _ => b`, and family `aₙ := fun m => if m = n then a else ⊥`. We prove
that, in this model, every statement that Rung 3 took as an axiom is in fact a
**theorem**. Since a model exists, the axiom set is consistent, and the
`star_infinite` result is non-vacuous.

(This is a meta-check: it does not import the axioms, it re-proves their
*statements* concretely. `M` below plays the role of the axiomatized `L2`.)

## Main results
* `model_le_iff_blockwise`, `model_blockVal_ortho`, `model_blockVal_inf`,
  `model_blockVal_bot`, `model_blockVal_pWitness`, `model_blockVal_aWitness`
  — each Rung-3 axiom, proved for the concrete model. **Zero sorry.**
* `model_star` — `(★)` holds in the concrete model directly.
-/

namespace QuerySystem
namespace ConsistencyModel

open MO2

/-- The model carrier: countably many `MO₂` blocks, coordinatewise. -/
abbrev M := ℕ → MO2

/-- Block evaluation in the model is just function application. -/
def blockVal (x : M) (n : ℕ) : MO2 := x n

/-- Coordinatewise orthocomplement on the model carrier `M = ℕ → MO₂`. This is
the honest infinite analogue of the Rung-2 `piOrtho` (which is defined only for
`Fin N → MO₂`); it is kept self-contained to the model type `M`. -/
def mOrtho (x : M) : M := fun n => (x n)ᗮ

/-- Witness `p`: `b` on every block. -/
def pW : M := fun _ => MO2.b

/-- Family `aₙ`: `a` on block `n`, `⊥` elsewhere. -/
def aW (n : ℕ) : M := fun m => if m = n then MO2.a else ⊥

-- Each Rung-3 axiom, now a theorem in the model:

/-- Axiom `le_iff_blockwise` holds: the `Pi` order *is* the blockwise order. -/
theorem model_le_iff_blockwise (x y : M) :
    x ≤ y ↔ ∀ n, blockVal x n ≤ blockVal y n := Pi.le_def

/-- Axiom `blockVal_ortho` holds: orthocomplement is coordinatewise (definition
of `mOrtho` for the model carrier `M`). -/
theorem model_blockVal_ortho (x : M) (n : ℕ) :
    blockVal (mOrtho x) n = (blockVal x n)ᗮ := rfl

/-- Axiom `blockVal_inf` holds: meet is coordinatewise (`Pi.inf_apply`). -/
theorem model_blockVal_inf (x y : M) (n : ℕ) :
    blockVal (x ⊓ y) n = blockVal x n ⊓ blockVal y n := Pi.inf_apply x y n

/-- Axiom `blockVal_bot` holds. -/
theorem model_blockVal_bot (n : ℕ) : blockVal (⊥ : M) n = ⊥ := rfl

/-- Axiom `blockVal_pWitness` holds. -/
theorem model_blockVal_pWitness (n : ℕ) : blockVal pW n = MO2.b := rfl

/-- Axiom `blockVal_aWitness` holds. -/
theorem model_blockVal_aWitness (n m : ℕ) :
    blockVal (aW n) m = if m = n then MO2.a else ⊥ := rfl

/-- And `(★)` itself holds directly in the model — independent confirmation that
the axiomatic `star_infinite` is non-vacuous. -/
theorem model_star (n : ℕ) :
    pW ⊓ aW n = ⊥ ∧ ¬ pW ≤ mOrtho (aW n) := by
  constructor
  · funext m
    rw [Pi.inf_apply]
    by_cases h : m = n
    · subst h; simp only [pW, aW, if_true]; exact (MO2.gap_symm).1
    · simp only [aW, if_neg h]; simp [pW]
  · intro hle
    have hn := hle n
    simp only [mOrtho, pW, aW, if_true] at hn
    exact (MO2.gap_symm).2 hn

/-- **Consistency.** Every Rung-3 axiom is realized by `(M, blockVal, pW, aW)`,
and `(★)` holds in it. Therefore the Rung-3 axiom set is consistent and
`star_infinite` is non-vacuous. -/
theorem axioms_consistent :
    (∀ x y : M, x ≤ y ↔ ∀ n, blockVal x n ≤ blockVal y n) ∧
    (∀ (x : M) (n : ℕ), blockVal (mOrtho x) n = (blockVal x n)ᗮ) ∧
    (∀ (x y : M) (n : ℕ), blockVal (x ⊓ y) n = blockVal x n ⊓ blockVal y n) ∧
    (∀ n : ℕ, blockVal (⊥ : M) n = ⊥) ∧
    (∀ n : ℕ, blockVal pW n = MO2.b) ∧
    (∀ n m : ℕ, blockVal (aW n) m = if m = n then MO2.a else ⊥) ∧
    (∀ n : ℕ, pW ⊓ aW n = ⊥ ∧ ¬ pW ≤ mOrtho (aW n)) :=
  ⟨model_le_iff_blockwise, model_blockVal_ortho, model_blockVal_inf,
   model_blockVal_bot, model_blockVal_pWitness, model_blockVal_aWitness, model_star⟩

end ConsistencyModel
end QuerySystem
