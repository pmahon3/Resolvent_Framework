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

## The orthomodular structure is part of the obligation

Rung 3 axiomatizes eleven things, and one of them is `L2.instOML` — that `L₂`
*is* an orthomodular lattice. That axiom is what gives the other ten their
meaning: `⊓`, `≤`, `ᗮ` and `⊥` in `le_iff_blockwise`, `blockVal_inf`,
`blockVal_ortho` and `blockVal_bot` are the operations of that structure, not
bare functions. A model that supplies the ten while leaving the eleventh
unrealized does not establish consistency of the set — it establishes
consistency of a fragment whose vocabulary is undefined.

So `instPiOrthomodularLattice` below proves the missing piece: a product of
orthomodular lattices is orthomodular, coordinatewise. `M = ℕ → MO₂` is such a
product, `mOrtho` is *definitionally* that structure's orthocomplement
(`mOrtho_eq_ortho`), and the model now realizes all eleven.

## Main results
* `instPiOrthomodularLattice` — products of OMLs are OMLs, componentwise.
* `model_instOML`, `mOrtho_eq_ortho` — the axiom `L2.instOML` realized, and the
  model's `mOrtho` identified with that structure's `ᗮ`.
* `model_le_iff_blockwise`, `model_blockVal_ortho`, `model_blockVal_inf`,
  `model_blockVal_bot`, `model_blockVal_pWitness`, `model_blockVal_aWitness`
  — each remaining Rung-3 axiom, proved for the concrete model. **Zero sorry.**
* `model_star` — `(★)` holds in the concrete model directly.
* `axioms_consistent` — all eleven together, in one statement.
-/

namespace QuerySystem

/-- **A product of orthomodular lattices is orthomodular**, everything
computed coordinatewise.

Every law of the class is an equation or an implication between elements, and
the `Pi` order, lattice and bounded-order structures are all pointwise — so
each law follows from the same law in each factor, applied at each coordinate.
Built *from* `Pi.instLattice` and `Pi.instBoundedOrder` rather than restating
them, so the lattice operations on a product are the ones already in use and no
second, non-defeq copy is introduced.

This is what makes the consistency argument below cover `L2.instOML` and not
merely the ten blockwise axioms. -/
instance instPiOrthomodularLattice {ι : Type*} {α : ι → Type*}
    [∀ i, OrthomodularLattice (α i)] : OrthomodularLattice (∀ i, α i) :=
  { (inferInstance : Lattice (∀ i, α i)),
    (inferInstance : BoundedOrder (∀ i, α i)) with
    ortho := fun x i => (x i)ᗮ
    inf_ortho := fun x => funext fun i => OrthomodularLattice.inf_ortho (x i)
    sup_ortho := fun x => funext fun i => OrthomodularLattice.sup_ortho (x i)
    ortho_ortho := fun x => funext fun i => OrthomodularLattice.ortho_ortho (x i)
    ortho_le_ortho := fun h i => OrthomodularLattice.ortho_le_ortho (h i)
    orthomodular := fun h => funext fun i => OrthomodularLattice.orthomodular (h i) }

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

/-- **Axiom `L2.instOML` realized.** `M` is an orthomodular lattice, by
`instPiOrthomodularLattice` applied to the countable product of copies of
`MO₂`. Named so the consistency statement can cite it. -/
@[reducible] def model_instOML : OrthomodularLattice M := inferInstance

/-- `mOrtho` is not an ad-hoc function: it **is** the orthocomplement of the
orthomodular structure `model_instOML`, definitionally. Without this the model
would interpret `blockVal_ortho` using a symbol the axiom does not refer to. -/
theorem mOrtho_eq_ortho (x : M) : mOrtho x = xᗮ := rfl

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

/-- **Consistency.** Every Rung-3 axiom is realized by `(M, blockVal, pW, aW)`
carrying the orthomodular structure `model_instOML`, and `(★)` holds in it.
Therefore the Rung-3 axiom set is consistent and `star_infinite` is non-vacuous.

The first conjunct is the one that used to be missing: it discharges
`L2.instOML`, and `mOrtho_eq_ortho` is what makes the orthocomplement appearing
in the third conjunct the orthocomplement of *that* structure rather than an
unrelated function with a similar definition. -/
theorem axioms_consistent :
    Nonempty (OrthomodularLattice M) ∧
    (∀ x : M, mOrtho x = xᗮ) ∧
    (∀ x y : M, x ≤ y ↔ ∀ n, blockVal x n ≤ blockVal y n) ∧
    (∀ (x : M) (n : ℕ), blockVal (mOrtho x) n = (blockVal x n)ᗮ) ∧
    (∀ (x y : M) (n : ℕ), blockVal (x ⊓ y) n = blockVal x n ⊓ blockVal y n) ∧
    (∀ n : ℕ, blockVal (⊥ : M) n = ⊥) ∧
    (∀ n : ℕ, blockVal pW n = MO2.b) ∧
    (∀ n m : ℕ, blockVal (aW n) m = if m = n then MO2.a else ⊥) ∧
    (∀ n : ℕ, pW ⊓ aW n = ⊥ ∧ ¬ pW ≤ mOrtho (aW n)) :=
  ⟨⟨model_instOML⟩, mOrtho_eq_ortho,
   model_le_iff_blockwise, model_blockVal_ortho, model_blockVal_inf,
   model_blockVal_bot, model_blockVal_pWitness, model_blockVal_aWitness, model_star⟩

end ConsistencyModel
end QuerySystem
