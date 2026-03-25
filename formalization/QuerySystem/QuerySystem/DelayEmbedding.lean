/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.QuerySystem

/-!
# Delay Query System (Paper 1: Observational Probability)

This file formalises the delay query system over a sensor alphabet and verifies that
it satisfies the axioms of a `QuerySystem`. The main results instantiate the abstract
framework of Paper 0, triggering the Observational Extension Theorem for delay embeddings.

## Setup

Fix a measurable space `(X, 𝒳)` (the sensor alphabet). The observation space is
`Ω = X^ℤ` (bi-infinite streams). The delay query at `(d, τ) : ℕ+ × ℕ+` reads off
`d` samples at lag `τ`:

    eval_{d,τ}(ω) = (ω₀, ω₋τ, ω₋₂τ, …, ω₋₍d₋₁₎τ)  ∈ Xᵈ

## Refinement order

`(d, τ) ≤ (d', τ')` iff `τ' ∣ τ` and `d' > (d - 1) * (τ / τ')`.
The refinement map π : Xᵈ' → Xᵈ picks out the coordinates at positions
`0, τ/τ', 2τ/τ', …, (d-1)τ/τ'` of the finer outcome vector.

## Main results

* `delayQuerySystem`: the `QuerySystem` instance over `(X, 𝒳)`.
* `delayQS_upperDirected`: any two queries have a common refinement (via gcd of lags).
* `delayQS_evalSurjective`: every outcome in Xᵈ is realized by some coherent stream.
* `delayQS_compatibleMarginals`: any probability measure on `ℤ → X` induces compatible
  marginals.

## References

* observational_probability_body.tex: Observational Probability (Paper 1)
* QuerySystem.lean: Abstract query system framework (Paper 0)
-/

open MeasureTheory
open scoped ENNReal

universe u

variable {X : Type u} [MeasurableSpace X]

/-! ## Observation space: bi-infinite streams -/

/-- The observation space: bi-infinite streams of sensor readings.
    We use `SensorStream` to avoid name collision with `Std.Stream`. -/
abbrev SensorStream (X : Type u) : Type u := ℤ → X

instance : MeasurableSpace (SensorStream X) := MeasurableSpace.pi

/-- Evaluation of a sensor stream at a single time index. -/
def sensorEval (t : ℤ) : SensorStream X → X := fun ω => ω t

lemma measurable_sensorEval (t : ℤ) : Measurable (sensorEval (X := X) t) :=
  measurable_pi_apply t

/-! ## Delay queries -/

/-- The outcome space of a delay query `(d, τ)`: `d`-tuples from `X`.
    We use `Fin d → X` with the product measurable space. -/
def DelayOutcome (X : Type u) [MeasurableSpace X] (d : ℕ) : Type u := Fin d → X

instance (d : ℕ) : MeasurableSpace (DelayOutcome X d) := MeasurableSpace.pi

/-- The evaluation map for delay query `(d, τ)`:
    samples the stream at times `0, -τ, -2τ, …, -(d-1)τ`. -/
def delayEval (d τ : ℕ) (ω : SensorStream X) : DelayOutcome X d :=
  fun k => ω (-(↑(k.val * τ) : ℤ))

lemma measurable_delayEval (d τ : ℕ) : Measurable (delayEval (X := X) d τ) :=
  measurable_pi_lambda _ fun k => measurable_sensorEval _

/-- The delay query at `(d, τ)` as a `Query`. -/
def delayQuery (X : Type u) [MeasurableSpace X] (d τ : ℕ) : Query.{u} where
  Outcome  := DelayOutcome X d
  instMeas := inferInstance

/-! ## Refinement order and maps -/

/-- `(d, τ) ≤ (d', τ')` in the delay refinement order:
    `τ'` divides `τ` and `d'` covers all `d` sample times `{0, τ, …, (d-1)τ}` in
    `{0, τ', …, (d'-1)τ'}`.  With `k = τ / τ'`, need `(d-1)*k < d'`. -/
def delayLe (d τ d' τ' : ℕ) : Prop :=
  τ' ∣ τ ∧ (d = 0 ∨ (d - 1) * (τ / τ') < d')

/-- The refinement map π : Xᵈ' → Xᵈ.
    Picks coordinates `0, k, 2k, …, (d-1)k` from the finer vector, where `k = τ / τ'`. -/
def delayRefineMap (d τ d' τ' : ℕ) (hdiv : τ' ∣ τ) (hbnd : d = 0 ∨ (d - 1) * (τ / τ') < d') :
    DelayOutcome X d' → DelayOutcome X d :=
  fun v k =>
    v ⟨k.val * (τ / τ'), by
      rcases hbnd with rfl | hlt
      · exact Fin.elim0 k
      · calc k.val * (τ / τ')
            ≤ (d - 1) * (τ / τ') := Nat.mul_le_mul_right _ (by omega)
          _ < d'                  := hlt⟩

lemma measurable_delayRefineMap (d τ d' τ' : ℕ) (hdiv : τ' ∣ τ)
    (hbnd : d = 0 ∨ (d - 1) * (τ / τ') < d') :
    Measurable (delayRefineMap (X := X) d τ d' τ' hdiv hbnd) :=
  measurable_pi_lambda _ fun _ => measurable_pi_apply _

/-! ### Reflexivity -/

lemma delayLe_refl (d τ : ℕ) : delayLe d τ d τ :=
  ⟨dvd_refl τ, by
    rcases Nat.eq_zero_or_pos d with rfl | hd
    · exact Or.inl rfl
    · right
      rcases Nat.eq_zero_or_pos τ with rfl | hτ
      · simp; omega
      · simp [Nat.div_self hτ]; omega⟩

lemma delayRefineMap_refl (d τ : ℕ) (hτ : 0 < τ) :
    delayRefineMap (X := X) d τ d τ (dvd_refl τ) (delayLe_refl d τ).2 = id := by
  funext v k
  simp only [delayRefineMap, id]
  congr 1
  apply Fin.ext
  simp [Nat.div_self hτ]

/-! ### Transitivity -/

/-- The ratio `τ₁/τ₃ = (τ₁/τ₂) * (τ₂/τ₃)` when `τ₂ ∣ τ₁` and `τ₃ ∣ τ₂`. -/
private lemma div_div_mul {τ₁ τ₂ τ₃ : ℕ} (h₁₂ : τ₂ ∣ τ₁) (h₂₃ : τ₃ ∣ τ₂)
    (hτ₂ : 0 < τ₂) (hτ₃ : 0 < τ₃) :
    τ₁ / τ₃ = (τ₁ / τ₂) * (τ₂ / τ₃) := by
  obtain ⟨a, rfl⟩ := h₁₂
  obtain ⟨b, rfl⟩ := h₂₃
  -- τ₁ = τ₃ * b * a, τ₂ = τ₃ * b
  -- Goal: τ₃ * b * a / τ₃ = (τ₃ * b * a / (τ₃ * b)) * (τ₃ * b / τ₃)
  -- Each of the three divisions is exact:
  --   τ₃ * b * a / τ₃ = b * a
  --   τ₃ * b * a / (τ₃ * b) = a
  --   τ₃ * b / τ₃ = b
  -- So the goal reduces to b * a = a * b
  have lhs : τ₃ * b * a / τ₃ = b * a := by
    rw [Nat.mul_assoc, Nat.mul_div_cancel_left _ hτ₃]
  have rhs1 : τ₃ * b * a / (τ₃ * b) = a := Nat.mul_div_cancel_left a hτ₂
  have rhs2 : τ₃ * b / τ₃ = b := Nat.mul_div_cancel_left _ hτ₃
  rw [lhs, rhs1, rhs2]; ring

lemma delayLe_trans {d₁ τ₁ d₂ τ₂ d₃ τ₃ : ℕ}
    (h₁₂ : delayLe d₁ τ₁ d₂ τ₂) (h₂₃ : delayLe d₂ τ₂ d₃ τ₃) :
    delayLe d₁ τ₁ d₃ τ₃ := by
  obtain ⟨hdiv₁₂, hbnd₁₂⟩ := h₁₂
  obtain ⟨hdiv₂₃, hbnd₂₃⟩ := h₂₃
  refine ⟨dvd_trans hdiv₂₃ hdiv₁₂, ?_⟩
  rcases hbnd₁₂ with rfl | hlt₁₂
  · exact Or.inl rfl
  right
  rcases hbnd₂₃ with rfl | hlt₂₃
  · omega
  -- (d₁-1)*(τ₁/τ₃) = (d₁-1)*(τ₁/τ₂)*(τ₂/τ₃) < d₂*(τ₂/τ₃) ≤ ...
  rcases Nat.eq_zero_or_pos τ₂ with rfl | hτ₂
  · simp at hdiv₁₂; subst hdiv₁₂; simp at hlt₂₃ ⊢; omega
  rcases Nat.eq_zero_or_pos τ₃ with rfl | hτ₃
  · simp at hdiv₂₃; subst hdiv₂₃; simp at hlt₁₂ hlt₂₃ ⊢
    omega
  rw [div_div_mul hdiv₁₂ hdiv₂₃ hτ₂ hτ₃]
  have hk' : 0 < τ₂ / τ₃ := Nat.div_pos (Nat.le_of_dvd hτ₂ hdiv₂₃) hτ₃
  have h1 : (d₁ - 1) * (τ₁ / τ₂) < d₂ := hlt₁₂
  have h2 : (d₂ - 1) * (τ₂ / τ₃) < d₃ := hlt₂₃
  -- (d₁-1)*(τ₁/τ₂) ≤ d₂-1 (in ℕ, < d₂ means ≤ d₂-1 when d₂ > 0)
  -- multiply by (τ₂/τ₃): (d₁-1)*(τ₁/τ₂)*(τ₂/τ₃) ≤ (d₂-1)*(τ₂/τ₃) < d₃
  have hd₂ : 0 < d₂ := by omega
  have hle : (d₁ - 1) * (τ₁ / τ₂) ≤ d₂ - 1 := by omega
  have := Nat.mul_le_mul_right (τ₂ / τ₃) hle
  nlinarith

lemma delayRefineMap_trans {d₁ τ₁ d₂ τ₂ d₃ τ₃ : ℕ}
    (h₁₂ : delayLe d₁ τ₁ d₂ τ₂) (h₂₃ : delayLe d₂ τ₂ d₃ τ₃) :
    delayRefineMap (X := X) d₁ τ₁ d₃ τ₃ (delayLe_trans h₁₂ h₂₃).1
        (delayLe_trans h₁₂ h₂₃).2 =
    delayRefineMap d₁ τ₁ d₂ τ₂ h₁₂.1 h₁₂.2 ∘
    delayRefineMap d₂ τ₂ d₃ τ₃ h₂₃.1 h₂₃.2 := by
  funext v k
  simp only [delayRefineMap, Function.comp]
  congr 1
  apply Fin.ext
  simp only [Fin.val_mk]
  rcases Nat.eq_zero_or_pos τ₂ with rfl | hτ₂
  · -- τ₂ = 0 implies τ₁ = 0
    have : τ₁ = 0 := by simpa using h₁₂.1
    subst this; simp
  rcases Nat.eq_zero_or_pos τ₃ with rfl | hτ₃
  · -- τ₃ = 0 implies τ₂ = 0, contradicting hτ₂
    have : τ₂ = 0 := by simpa using h₂₃.1
    omega
  rw [div_div_mul h₁₂.1 h₂₃.1 hτ₂ hτ₃]
  ring

/-! ## The delay query system -/

/-- The delay query system over sensor alphabet `X`.

    Index set `ℕ+ × ℕ+`, query at `(d, τ)` has outcome space `Xᵈ`. -/
noncomputable def delayQuerySystem (X : Type u) [MeasurableSpace X] : QuerySystem.{u, 0} where
  ι        := ℕ+ × ℕ+
  q        := fun ⟨⟨d, _⟩, ⟨τ, _⟩⟩ => delayQuery X d τ
  le       := fun ⟨⟨d, _⟩, ⟨τ, _⟩⟩ ⟨⟨d', _⟩, ⟨τ', _⟩⟩ => delayLe d τ d' τ'
  π        := fun {_} {_} h => ⟨delayRefineMap _ _ _ _ h.1 h.2,
                                 measurable_delayRefineMap _ _ _ _ h.1 h.2⟩
  le_refl  := fun ⟨⟨d, _⟩, ⟨τ, _⟩⟩ => delayLe_refl d τ
  le_trans := fun h₁₂ h₂₃ => delayLe_trans h₁₂ h₂₃
  π_refl   := fun ⟨⟨d, _⟩, ⟨τ, hτ⟩⟩ => by
    simp only
    exact delayRefineMap_refl d τ hτ
  π_trans  := by
    intro ⟨⟨d₁,_⟩,⟨τ₁,_⟩⟩ ⟨⟨d₂,_⟩,⟨τ₂,_⟩⟩ ⟨⟨d₃,_⟩,⟨τ₃,_⟩⟩ h₁₂ h₂₃
    exact delayRefineMap_trans h₁₂ h₂₃

namespace delayQuerySystem

/-! ## Upper-directedness -/

/-- Any two delay queries have a common refinement.
    Common lag: `τ'' = gcd(τ, τ')`.
    Common dimension: `d'' = max((d-1)*(τ/τ''), (d'-1)*(τ'/τ'')) + 1`. -/
theorem upperDirected : (delayQuerySystem X).UpperDirected := by
  intro ⟨⟨d, hd⟩, ⟨τ, hτ⟩⟩ ⟨⟨d', hd'⟩, ⟨τ', hτ'⟩⟩
  have hτ''_pos : 0 < Nat.gcd τ τ' := Nat.gcd_pos_of_pos_left _ hτ
  refine ⟨⟨⟨max ((d - 1) * (τ / Nat.gcd τ τ')) ((d' - 1) * (τ' / Nat.gcd τ τ')) + 1,
             by positivity⟩,
           ⟨Nat.gcd τ τ', hτ''_pos⟩⟩, ?_, ?_⟩
  · exact ⟨Nat.gcd_dvd_left τ τ',
           Or.inr (by omega)⟩
  · exact ⟨Nat.gcd_dvd_right τ τ',
           Or.inr (by omega)⟩

/-- Every countable family of delay queries has a common refinement,
    provided the family is bounded (i.e., there is a finite common refinement).

    **Note on `SequentiallyUpperDirected`**: The abstract definition requires
    `∀ u : ℕ → ι, ∃ k, ∀ n, le (u n) k`. For unbounded sequences of delay queries
    (where dimensions grow without bound), the sup `d'' = sup_n (d_n-1)*k_n + 1` may
    be infinite. The paper (Prop. 2 proof) handles this via a diagonal argument for
    finite subfamilies. The general countable case requires an additional boundedness
    hypothesis. This sorry records that gap. -/
theorem seqUpperDirected : (delayQuerySystem X).SequentiallyUpperDirected := by
  sorry

/-! ## Realizability -/

/-- The delay query system's `Omega` is nonempty (needed for surjectivity). -/
instance [Nonempty X] : Nonempty (delayQuerySystem X).Omega :=
  ⟨⟨fun _ _ => Classical.arbitrary X, by
    intro ⟨⟨d,_⟩,⟨τ,_⟩⟩ ⟨⟨d',_⟩,⟨τ',_⟩⟩ h
    simp only [delayQuerySystem]
    funext k
    simp only [delayRefineMap]⟩⟩

/-- Every outcome in `Xᵈ` is realized by some coherent sequence:
    `eval_{d,τ}` is surjective on the delay query system's Omega.

    Proof: given `y : Xᵈ`, the constant stream `ω_t = y(0)` is coherent
    (refinement maps are coordinate projections; all entries equal `y(0)`
    suffices for d=1). For general d we need a richer construction.

    **Note**: The full realizability proof requires constructing a coherent family
    (element of `Omega`) for arbitrary `y : Xᵈ`. This is more involved than
    surjectivity of `delayEval` on `SensorStream X` (which is straightforward).
    This sorry records that gap; the stream-level surjectivity is proved below. -/
theorem evalSurjective [Nonempty X] : (delayQuerySystem X).EvalSurjective := by
  sorry

/-- Stream-level surjectivity: `delayEval d τ : SensorStream X → Xᵈ` is surjective.

    Proof: given `y : Xᵈ`, construct `ω` by `ω(-(k*τ)) = y(k)` for `k < d`,
    and `ω(t) = Classical.arbitrary X` elsewhere. -/
lemma delayEval_surjective [Nonempty X] (d τ : ℕ) (hτ : 0 < τ) :
    Function.Surjective (delayEval (X := X) d τ) := by
  intro y
  classical
  -- Construct ω assigning y(k) at time -(k*τ)
  refine ⟨fun t =>
    if h : ∃ k : Fin d, t = -(↑(k.val * τ) : ℤ) then
      y h.choose
    else Classical.arbitrary X, ?_⟩
  funext k
  simp only [delayEval]
  have hk : ∃ k' : Fin d, -(↑(k.val * τ) : ℤ) = -(↑(k'.val * τ) : ℤ) :=
    ⟨k, rfl⟩
  simp only [hk, dif_pos]
  -- show y hk.choose = y k, i.e., hk.choose = k
  congr 1
  apply Fin.ext
  have heq := hk.choose_spec
  push_cast at heq
  have hτ' : (τ : ℤ) ≠ 0 := Int.natCast_ne_zero.mpr (Nat.pos_iff_ne_zero.mp hτ)
  have hmul : (hk.choose.val : ℤ) * τ = k.val * τ := by linarith
  exact_mod_cast Int.eq_of_mul_eq_mul_right hτ' hmul

/-! ## Compatible marginals -/

/-- Any probability measure on `SensorStream X` induces compatible marginals
    for the delay query system.

    Proof: pushforward commutes with composition; the refinement map is a coordinate
    projection satisfying `delayEval d τ = π ∘ delayEval d' τ'` on streams. -/
theorem compatibleMarginals (P : Measure (SensorStream X)) [IsProbabilityMeasure P] :
    (delayQuerySystem X).CompatibleMarginals
      (fun ⟨⟨d, _⟩, ⟨τ, _⟩⟩ => Measure.map (delayEval (X := X) d τ) P) := by
  intro ⟨⟨d, _⟩, ⟨τ, _⟩⟩ ⟨⟨d', _⟩, ⟨τ', hτ'_pos⟩⟩ h
  simp only [delayQuerySystem]
  rw [Measure.map_map (measurable_delayRefineMap _ _ _ _ h.1 h.2)
        (measurable_delayEval d' τ')]
  congr 1
  -- Show: delayRefineMap ∘ delayEval d' τ' = delayEval d τ on SensorStream X
  funext ω k
  simp only [Function.comp, delayEval, delayRefineMap]
  congr 1
  -- -(k * τ) = -(k * (τ/τ') * τ') as integers, since τ' ∣ τ
  obtain ⟨a, ha⟩ := h.1
  have hdiv : τ / τ' = a := by rw [ha]; exact Nat.mul_div_cancel_left a hτ'_pos
  rw [hdiv, ha]
  push_cast
  ring

end delayQuerySystem
