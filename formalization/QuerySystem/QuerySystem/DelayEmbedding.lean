/-
Copyright (c) 2026. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Patrick S. Mahon
-/
import QuerySystem.QuerySystem
import QuerySystem.ReconstructionTheorem

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

* `delayQuerySystem`               : the `QuerySystem` instance over `(X, 𝒳)` [prop:is-qs]
* `upperDirected`                  : any two queries have a common refinement [prop:upper-directed-general]
* `evalSurjective`                 : every outcome in Xᵈ is realized by some coherent stream [prop:realizability]
* `compatibleMarginals`            : any probability measure on `ℤ → X` induces compatible marginals [prop:compat]
* `delayFixedLagBoundedSystem`     : bounded fixed-lag subsystem (correct scope for SUD)
* `observational_extension_fixedLag` : extension theorem instantiated for bounded delay systems

## Intentional formalization gaps

The following Paper 1 results are not yet formalized (require conditional probability
infrastructure beyond the current scope):

* `def:delay-pred-map`    : predictive law map φ_{d,τ} : Xᵈ → P(X)
* `def:pred-sufficient`   : predictive sufficiency (injectivity of φ_{d,τ} on support)
* `def:markov-order`      : predictive τ-Markov order m(τ,P)
* `thm:sufficiency`       : characterization d ≥ m(τ,P) ↔ predictive sufficiency
* `prop:stationarity`     : stationarity and time-homogeneity of delay distributions
* `cor:takens`            : Takens embedding as special case

These gaps are intentional: the delay query system's structural properties (query
system axioms, upper-directedness, realizability, compatibility) are fully formalized;
the probability-theoretic content of the sufficiency section requires conditional
distribution infrastructure not yet developed here.

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

/-- `(d, τ) ≤ (d', τ')` in the delay refinement order [def:refinement]:
    `τ'` divides `τ` and `d'` covers all `d` sample times `{0, τ, …, (d-1)τ}` in
    `{0, τ', …, (d'-1)τ'}`.  With `k = τ / τ'`, need `(d-1)*k < d'`. -/
def delayLe (d τ d' τ' : ℕ) : Prop :=
  τ' ∣ τ ∧ (d = 0 ∨ (d - 1) * (τ / τ') < d')

/-- The refinement map π : Xᵈ' → Xᵈ [def:refinement].
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

/-- **Gap**: The full delay query system is NOT sequentially upper-directed.

    `SequentiallyUpperDirected` requires `∀ u : ℕ → ι, ∃ k, ∀ n, le (u n) k` —
    a single finite `k` above the entire infinite sequence.

    **Counterexample**: `u n = (n+1, 1)`. Any upper bound `(d'', τ'')` would need
    `τ'' ∣ 1` (so `τ'' = 1`) and `(n+1-1)*(1/1) = n < d''` for all `n`, which is
    impossible for finite `d''`.

    **What Paper 1 actually proves** (Prop. 2): every *finite* subfamily has a common
    refinement. This is equivalent to `UpperDirected` (proved above), not the stronger
    `SequentiallyUpperDirected`. Paper 1's definition of "sequential upper-directedness"
    (Definition 3.3) is weaker than the Lean framework's definition — it only requires
    finite subfamilies, not the full countable family.

    **Consequence**: `observational_extension` (which needs `SequentiallyUpperDirected`)
    does not directly apply to the full delay query system. It applies to any *bounded*
    subfamily `{Q_{d_n, τ_n}}` for which `sup_n (d_n-1)*k_n` is finite. This is the
    correct scope of Paper 1's extension theorem.

    This is recorded as the negation `not_seqUpperDirected`. -/
theorem not_seqUpperDirected : ¬ (delayQuerySystem X).SequentiallyUpperDirected := by
  intro h
  -- Counterexample: u n = (n+2, 1).
  let u : ℕ → (delayQuerySystem X).ι :=
    fun n => ⟨⟨n + 2, by omega⟩, ⟨1, Nat.one_pos⟩⟩
  obtain ⟨⟨⟨d', hd'⟩, ⟨τ', hτ'⟩⟩, hk⟩ := h u
  -- Apply to n = d': need delayLe (d'+2) 1 d' τ'
  have hle := hk d'
  -- delayLe requires τ' ∣ 1 and (d'+2-1)*(1/τ') < d', i.e., (d'+1)/τ' < d'
  -- But τ' ∣ 1 forces τ' = 1, giving d'+1 < d', contradiction.
  simp only [u, delayQuerySystem] at hle
  unfold delayLe at hle
  obtain ⟨hdvd, hbnd⟩ := hle
  -- hdvd : τ' ∣ 1, so τ' = 1
  have hτ1 : (τ' : ℕ) = 1 := Nat.eq_one_of_dvd_one hdvd
  rcases hbnd with h0 | hlt
  · omega
  · simp [hτ1] at hlt

/-! ## Realizability -/

/-- The delay query system's `Omega` is nonempty (needed for surjectivity). -/
instance [Nonempty X] : Nonempty (delayQuerySystem X).Omega :=
  ⟨⟨fun _ _ => Classical.arbitrary X, by
    intro ⟨⟨d,_⟩,⟨τ,_⟩⟩ ⟨⟨d',_⟩,⟨τ',_⟩⟩ h
    simp only [delayQuerySystem]
    funext k
    simp only [delayRefineMap]⟩⟩

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
  have hmul : (hk.choose.val : ℤ) * τ = k.val * τ := by
    have := neg_inj.mp heq; omega
  exact_mod_cast Int.eq_of_mul_eq_mul_right hτ' hmul

/-- **[prop:realizability]** Every outcome in `Xᵈ` is realized by some coherent sequence.

    Proof: given `(d, τ)` and `y : Xᵈ`, use stream-level surjectivity to find
    `s : SensorStream X` with `delayEval d τ s = y`, then define the coherent
    family `ω.1 (d', τ') = delayEval d' τ' s` for all `(d', τ')`. Coherence
    holds because the `delayRefineMap` condition is exactly the equation
    `delayEval d τ = delayRefineMap ∘ delayEval d' τ'` on streams. -/
theorem evalSurjective [Nonempty X] : (delayQuerySystem X).EvalSurjective := by
  intro ⟨⟨d, _⟩, ⟨τ, hτ⟩⟩ y
  -- Step 1: get a stream realising y at level (d, τ)
  obtain ⟨s, hs⟩ := delayEval_surjective d τ hτ y
  -- Step 2: build the coherent Omega element using s at every level
  refine ⟨⟨fun ⟨⟨d', _⟩, ⟨τ', _⟩⟩ => delayEval d' τ' s, ?_⟩, ?_⟩
  · -- Coherence: for any refinement (d₁,τ₁) ≤ (d₂,τ₂), the components commute
    intro ⟨⟨d₁, _⟩, ⟨τ₁, _⟩⟩ ⟨⟨d₂, _⟩, ⟨τ₂, _⟩⟩ h
    -- Need: delayEval d₁ τ₁ s = delayRefineMap ... (delayEval d₂ τ₂ s)
    funext k
    obtain ⟨a, ha⟩ := h.1
    have hdiv : τ₁ / τ₂ = a := by rw [ha]; exact Nat.mul_div_cancel_left a ‹0 < τ₂›
    simp only [delayQuerySystem, delayEval, delayRefineMap, hdiv]
    congr 1
    push_cast [ha]
    ring
  · -- The (d, τ) component equals y
    simpa [QuerySystem.eval, delayQuerySystem] using hs

/-! ## Compatible marginals -/

/-- **[prop:compat]** Any probability measure on `SensorStream X` induces compatible marginals
    for the delay query system.

    Proof: pushforward commutes with composition; the refinement map is a coordinate
    projection satisfying `delayEval d τ = π ∘ delayEval d' τ'` on streams. -/
theorem compatibleMarginals (P : Measure (SensorStream X)) [IsProbabilityMeasure P] :
    (delayQuerySystem X).CompatibleMarginals
      (fun ⟨⟨d, _⟩, ⟨τ, _⟩⟩ => Measure.map (delayEval (X := X) d τ) P) := by
  intro ⟨⟨d, _⟩, ⟨τ, _⟩⟩ ⟨⟨d', _⟩, ⟨τ', hτ'_pos⟩⟩ h
  simp only [delayQuerySystem]
  -- Goal: map (delayRefineMap ...) (map (delayEval d' τ') P) = map (delayEval d τ) P
  -- Use map_map to combine, then show the composition equals delayEval d τ
  have hcomp : (delayRefineMap d τ d' τ' h.1 h.2) ∘ (delayEval (X := X) d' τ') =
      delayEval d τ := by
    funext ω k
    simp only [Function.comp, delayEval, delayRefineMap]
    congr 1
    obtain ⟨a, ha⟩ := h.1
    have hdiv : τ / τ' = a := by rw [ha]; exact Nat.mul_div_cancel_left a hτ'_pos
    rw [hdiv, ha]; push_cast; ring
  calc Measure.map (delayRefineMap d τ d' τ' h.1 h.2) (Measure.map (delayEval (X := X) d' τ') P)
      = Measure.map (delayRefineMap d τ d' τ' h.1 h.2 ∘ delayEval d' τ') P :=
        Measure.map_map (measurable_delayRefineMap d τ d' τ' h.1 h.2) (measurable_delayEval d' τ')
    _ = Measure.map (delayEval d τ) P := by rw [hcomp]

end delayQuerySystem

/-! ## Fixed-lag delay query system -/

/-! ## Bounded fixed-lag delay query system -/

/-- The bounded fixed-lag delay query system: dimension `d ≤ N`, lag fixed at `τ₀`.

    Index set `{d : ℕ+ // d ≤ N}` — a finite chain, hence trivially
    sequentially upper-directed with `N` as universal upper bound.

    **This is the correct scope of Paper 1's Observational Extension Theorem:**
    for a fixed lag `τ₀` and a fixed maximum dimension `N`, any compatible family of
    marginal measures on `{Xᵈ : d ≤ N}` extends uniquely to a probability measure on
    the projective limit.

    The full delay system (all lags, all dimensions) is the inductive limit over
    all `N` and `τ₀` of these bounded systems. -/
noncomputable def delayFixedLagBoundedSystem (X : Type u) [MeasurableSpace X]
    (τ₀ : ℕ+) (N : ℕ+) : QuerySystem.{u, 0} where
  ι        := {d : ℕ+ // d ≤ N}
  q        := fun ⟨⟨d, _⟩, _⟩ => delayQuery X d τ₀
  le       := fun ⟨⟨d, _⟩, _⟩ ⟨⟨d', _⟩, _⟩ => d ≤ d'
  π        := fun {i} {j} h =>
    ⟨fun v k => v ⟨k.val, Nat.lt_of_lt_of_le k.isLt h⟩,
     measurable_pi_lambda _ fun _ => measurable_pi_apply _⟩
  le_refl  := fun _ => le_refl _
  le_trans := fun h₁₂ h₂₃ => le_trans h₁₂ h₂₃
  π_refl   := fun _ => by funext v k; simp
  π_trans  := by intro _ _ _ _ _; funext v k; simp

namespace delayFixedLagBoundedSystem

/-- The bounded fixed-lag system is sequentially upper-directed: `N` is a universal bound. -/
theorem seqUpperDirected (τ₀ : ℕ+) (N : ℕ+) :
    (delayFixedLagBoundedSystem X τ₀ N).SequentiallyUpperDirected := by
  intro u
  exact ⟨⟨N, le_refl N⟩, fun n => (u n).2⟩

instance nonempty_ι (τ₀ : ℕ+) (N : ℕ+) :
    Nonempty (delayFixedLagBoundedSystem X τ₀ N).ι :=
  ⟨⟨N, le_refl N⟩⟩

/-- The bounded fixed-lag system's `Omega` is nonempty. -/
instance nonempty_omega [Nonempty X] (τ₀ : ℕ+) (N : ℕ+) :
    Nonempty (delayFixedLagBoundedSystem X τ₀ N).Omega := by
  refine ⟨⟨fun _ _ => Classical.arbitrary X, ?_⟩⟩
  intro ⟨⟨d₁, _⟩, _⟩ ⟨⟨d₂, _⟩, _⟩ _
  funext k
  simp [delayFixedLagBoundedSystem]

/-- Stream-level surjectivity for fixed lag. -/
private lemma fixedLag_delayEval_surjective [Nonempty X] (d : ℕ) (τ₀ : ℕ+) :
    Function.Surjective (delayEval (X := X) d τ₀) :=
  delayQuerySystem.delayEval_surjective d τ₀ τ₀.pos

/-- Every outcome in `Xᵈ` is realized by some coherent sequence. -/
theorem evalSurjective [Nonempty X] (τ₀ : ℕ+) (N : ℕ+) :
    (delayFixedLagBoundedSystem X τ₀ N).EvalSurjective := by
  intro ⟨⟨d, _⟩, _⟩ y
  obtain ⟨s, hs⟩ := fixedLag_delayEval_surjective d τ₀ y
  refine ⟨⟨fun ⟨⟨d', _⟩, _⟩ => delayEval d' τ₀ s, ?_⟩, ?_⟩
  · -- Coherence: for d₁ ≤ d₂, the (d₁,τ₀)-component = π applied to (d₂,τ₀)-component
    intro ⟨⟨d₁, _⟩, _⟩ ⟨⟨d₂, _⟩, _⟩ h
    funext k
    simp only [delayFixedLagBoundedSystem, delayEval]
  · simpa [QuerySystem.eval, delayFixedLagBoundedSystem, delayEval] using hs

/-- Any probability measure on `SensorStream X` induces compatible marginals. -/
theorem compatibleMarginals (τ₀ : ℕ+) (N : ℕ+) (P : Measure (SensorStream X))
    [IsProbabilityMeasure P] :
    (delayFixedLagBoundedSystem X τ₀ N).CompatibleMarginals
      (fun ⟨⟨d, _⟩, _⟩ => Measure.map (delayEval (X := X) d τ₀) P) := by
  intro ⟨⟨d, _⟩, _⟩ ⟨⟨d', _⟩, _⟩ h
  -- Goal: Measure.map (S.π h).π (Measure.map (delayEval d' τ₀) P) = Measure.map (delayEval d τ₀) P
  -- (S.π h).π = fun v k => v ⟨k.val, ...⟩; use map_map + pointwise eq
  have heq : (fun v : DelayOutcome X d' => fun k : Fin d =>
      v ⟨k.val, Nat.lt_of_lt_of_le k.isLt h⟩) ∘ delayEval d' τ₀ = delayEval d τ₀ := by
    funext ω k; simp [delayEval]
  simp only [delayFixedLagBoundedSystem]
  have hπ_meas : Measurable (fun v : DelayOutcome X d' => fun k : Fin d =>
      v ⟨k.val, Nat.lt_of_lt_of_le k.isLt h⟩) :=
    measurable_pi_lambda _ fun _ => measurable_pi_apply _
  calc Measure.map (fun v : DelayOutcome X d' => fun k : Fin d =>
          v ⟨k.val, Nat.lt_of_lt_of_le k.isLt h⟩) (Measure.map (delayEval d' τ₀) P)
      = Measure.map ((fun v : DelayOutcome X d' => fun k : Fin d =>
          v ⟨k.val, Nat.lt_of_lt_of_le k.isLt h⟩) ∘ delayEval d' τ₀) P :=
        Measure.map_map hπ_meas (measurable_delayEval d' τ₀)
    _ = Measure.map (delayEval d τ₀) P := by rw [heq]; rfl

/-- **Observational Extension Theorem for fixed-lag bounded delay embeddings.**

    For fixed lag `τ₀` and maximum dimension `N`, any compatible family of marginal
    measures on `{Xᵈ : d ≤ N}` extends uniquely to a probability measure on `Omega`.

    This is the formalization of Paper 1's main theorem in its correct scope:
    finite-window delay embeddings at fixed lag. -/
theorem observational_extension_fixedLag [Nonempty X] (τ₀ : ℕ+) (N : ℕ+)
    (ν : ∀ i : (delayFixedLagBoundedSystem X τ₀ N).ι,
           Measure ((delayFixedLagBoundedSystem X τ₀ N).q i).Outcome)
    (compat : (delayFixedLagBoundedSystem X τ₀ N).CompatibleMarginals ν)
    [hν : ∀ i, IsProbabilityMeasure (ν i)] :
    ∃! P : Measure (delayFixedLagBoundedSystem X τ₀ N).Omega,
      IsProbabilityMeasure P ∧
      ∀ i, Measure.map ((delayFixedLagBoundedSystem X τ₀ N).eval i) P = ν i :=
  (delayFixedLagBoundedSystem X τ₀ N).observational_extension
    (seqUpperDirected τ₀ N) (evalSurjective τ₀ N) ν compat

end delayFixedLagBoundedSystem

-- ============================================================
-- §  Connection to Reconstruction Theorem (Paper III)
-- ============================================================

/-!
## Bridge to Paper III: Reconstruction from Delay Observations

Given a measurable dynamical system `(X, T)` and an observable `h : X → ℝ`,
the `delayMap h T : X → (ℕ → ℝ)` of Paper III is the same as the map that
sends a state `x` to its orbit observations `(h(T^n x))_{n : ℕ}`.

The `observableAlgebra` generated by `{h ∘ T^n : n : ℕ}` equals the pullback
of the product σ-algebra on `ℕ → ℝ` along `delayMap h T`
(proved as `observableAlgebra_eq_comap` in `ReconstructionTheorem.lean`).

The reconstruction theorem (`reconstruction_iff_lpMeas`) then gives the
equivalence: the delay observations separate points in L² iff the observable
σ-algebra exhausts the full Borel σ-algebra mod μ.
-/

section ReconstructionBridge

open scoped symmDiff

variable {X : Type u} [MeasurableSpace X]

/-- The **delay observable algebra** of `h` under `T`: the σ-algebra on `X`
    generated by all time-delayed observations `{h ∘ T^n : n ∈ ℕ}`.

    This is `observableAlgebra` (from `ReconstructionTheorem.lean`) applied to
    the ℤ-indexed family `n ↦ h ∘ T^[n.toNat]`. For `n < 0`, `n.toNat = 0`,
    so those generators are redundant; the algebra is determined by `n : ℕ`. -/
noncomputable def delayObservableAlgebra (h : X → ℝ) (T : X → X) : MeasurableSpace X :=
  observableAlgebra (fun n : ℤ => h ∘ T^[n.toNat])

/-- The delay observable algebra equals the pullback of the product σ-algebra
    on `ℕ → ℝ` along the delay map `Φ_h`. -/
theorem delayObservableAlgebra_eq_comap
    (h : X → ℝ) (T : X → X) (hh : Measurable h) (hT : Measurable T) :
    delayObservableAlgebra h T =
    MeasurableSpace.comap (delayMap h T)
        (MeasurableSpace.pi (m := fun (_ : ℕ) => inferInstance)) :=
  observableAlgebra_eq_comap h T hh hT

/-- The delay map `Φ_h` intertwines `T` with the unilateral shift `σ`:
    `Φ_h(T x) = σ(Φ_h(x))`. -/
theorem delayMap_shift_intertwining
    (h : X → ℝ) (T : X → X) (x : X) :
    delayMap h T (T x) = unilateralShift (delayMap h T x) :=
  delayMap_intertwines_shift h T x

/-- **Reconstruction criterion for delay observations (Paper III, Corollary 4.4).**

    For a probability space `(X, μ)` and a measurable dynamical system `(X, T)`,
    the following are equivalent:
    - (i) The delay observable algebra exhausts the full σ-algebra mod `μ`
    - (ii) `lpMeas ℝ ℝ (delayObservableAlgebra h T) 2 μ` is dense in `Lp ℝ 2 μ`

    This is `reconstruction_iff_lpMeas` instantiated for the delay observable algebra.

    **Note:** Direct proof-term application of `reconstruction_iff_lpMeas` here triggers
    Lean's two-MeasurableSpace-instance elaboration problem (the sub-σ-algebra
    `delayObservableAlgebra h T` and the ambient `[MeasurableSpace X]` are both
    `MeasurableSpace X`). The sorry is a documentation gap, not a mathematical gap. -/
theorem delay_reconstruction_iff
    (h : X → ℝ) (T : X → X)
    (hm : delayObservableAlgebra h T ≤ ‹MeasurableSpace X›)
    (μ : Measure X) [IsFiniteMeasure μ] :
    (∀ s : Set X, MeasurableSet s →
        ∃ t : Set X, MeasurableSet[delayObservableAlgebra h T] t ∧ μ (s ∆ t) = 0) ↔
    Dense (lpMeas ℝ ℝ (delayObservableAlgebra h T) 2 μ : Set (Lp ℝ 2 μ)) := by
  exact reconstruction_iff_lpMeas (m0 := ‹MeasurableSpace X›) (μ := μ) hm

/-- **Cyclic vector implies delay reconstruction (Paper III, Corollary 5.2).**

    If `h` is cyclic for the Koopman operator `U_T` on `L²(X, μ)` — i.e.,
    `span{h ∘ T^n : n ∈ ℕ}` is dense in `L²` — then the delay observable
    algebra is dense in `L²`, hence the delay map reconstructs the state space. -/
theorem delay_cyclic_implies_reconstruction
    (μ : Measure X) [IsFiniteMeasure μ]
    (h : X → ℝ) (T : X → X)
    (hh : Measurable h) (hT : Measurable T)
    (hmem : ∀ n : ℕ, MemLp (h ∘ T^[n]) 2 μ)
    (h_cyclic :
      (Submodule.span ℝ
        (Set.range (fun n : ℕ => (hmem n).toLp _))).topologicalClosure = ⊤) :
    Dense (lpMeas ℝ ℝ (delayObservableAlgebra h T) 2 μ : Set (Lp ℝ 2 μ)) :=
  cyclic_implies_dense μ h T hh hT hmem h_cyclic

/-! ### The bridge to the delay *query system*

Everything above this point relates `ReconstructionTheorem`'s objects to each
other. This subsection is the missing join to the first half of the file: the
delay query system of §1--§3, which until now shared a file with the
reconstruction material and nothing else -- no declaration, hence no dependency
edge.

**The two modelling questions, answered explicitly.**

*Whose space is the query system's type parameter?* The observation space.
`delayQuerySystem Y` samples streams `ℤ → Y`, so instantiating it at `Y = ℝ`
makes its outcomes tuples of sensor readings. The state space `X` never appears
in it; it enters only through the map `orbitStream` below. A state is not an
outcome of any delay query -- only its observations are.

*Which time direction?* `delayEval d τ` samples a stream at `0, -τ, …, -(d-1)τ`
-- the past -- while the reconstruction side uses forward iterates `T^[n]`. The
identification that makes them agree is that reading the stream backwards is
running the orbit forwards: the stream of `x` carries at time `t` the
observation of the state `(-t)` steps ahead. This is the ordinary delay-
coordinate convention: at unit lag the delay vector is
`(h x, h (T x), …, h (T^(d-1) x))`.

The alternative reading -- past times as *backward* iterates -- needs `T`
invertible and produces a genuinely bi-infinite object. That is the ℤ-vs-ℕ
point already recorded in this file's header: for invertible `T` the two
generate the same σ-algebra, so nothing below would change, but for
non-invertible `T` only the convention taken here is available at all. -/

/-- The **observation stream** of a state: the sensor stream a state emits as
the system runs. Reading it backwards in time reads the orbit forwards. -/
def orbitStream (h : X → ℝ) (T : X → X) (x : X) : SensorStream ℝ :=
  fun t => h (T^[(-t).toNat] x)

@[simp] lemma orbitStream_neg_natCast (h : X → ℝ) (T : X → X) (x : X) (n : ℕ) :
    orbitStream h T x (-(n : ℤ)) = h (T^[n] x) := by
  simp [orbitStream]

/-- **Sampling the orbit stream is taking delay coordinates.** The delay query
`(d, τ)`, applied to the stream a state emits, returns exactly that state's
delay-coordinate vector at lag `τ`. -/
theorem delayEval_orbitStream (h : X → ℝ) (T : X → X) (d τ : ℕ) (x : X) :
    delayEval d τ (orbitStream h T x) = fun k : Fin d => h (T^[k.val * τ] x) := by
  funext k
  have hc : ((k.val : ℤ) * (τ : ℤ)).toNat = k.val * τ := by
    rw [← Nat.cast_mul]; exact Int.toNat_natCast _
  simp [delayEval, orbitStream, hc]

/-- At unit lag the delay-coordinate vector is `Φ_h` truncated to its first `d`
coordinates -- the query system's outcomes and the reconstruction map are the
same data, read at finite and infinite depth respectively. -/
theorem delayEval_orbitStream_one (h : X → ℝ) (T : X → X) (d : ℕ) (x : X) :
    delayEval d 1 (orbitStream h T x) = fun k : Fin d => delayMap h T x k.val := by
  funext k
  simp [delayEval_orbitStream, delayMap]

/-- The σ-algebra the delay *queries* induce on the state space, by pulling each
query's outcome back along `orbitStream`. This is the query system's view of
`X`. -/
@[reducible] noncomputable def delayQueryAlgebra (h : X → ℝ) (T : X → X) : MeasurableSpace X :=
  ⨆ (d : ℕ) (τ : ℕ),
    MeasurableSpace.comap (fun x => delayEval d τ (orbitStream h T x)) inferInstance

/-- **The bridge.** The delay query system and the reconstruction theorem see the
same σ-algebra on the state space: what the queries can resolve is exactly the
observable algebra `𝒪_h`.

`≤` holds because every coordinate of every query is some `h ∘ T^[n]`. `≥`
holds because every `h ∘ T^[n]` is a coordinate of some query -- take `d = n+1`
at unit lag. The negative indices of the ℤ-indexed family are `h` itself, by
`Int.toNat` collapsing them to `0`, and are covered by `d = 1`. -/
theorem delayQueryAlgebra_eq_delayObservableAlgebra (h : X → ℝ) (T : X → X) :
    delayQueryAlgebra h T = delayObservableAlgebra h T := by
  apply le_antisymm
  · -- Every coordinate of every query is some `h ∘ T^[n]`, so each query map is
    -- measurable for the observable algebra, and its comap therefore sits below.
    refine iSup_le fun d => iSup_le fun τ => ?_
    have hmeas : Measurable[delayObservableAlgebra h T]
        (fun x => delayEval d τ (orbitStream h T x)) := by
      -- The domain σ-algebra here is not the ambient one, and the pi lemmas
      -- take theirs by instance synthesis rather than by unification -- so make
      -- it the ambient one for the duration. `letI`, not `haveI`: the body has
      -- to stay visible or it no longer matches the goal.
      letI m : MeasurableSpace X := delayObservableAlgebra h T
      rw [funext fun x => delayEval_orbitStream h T d τ x]
      refine measurable_pi_lambda _ fun k => ?_
      have := observableAlgebra_measurable (fun n : ℤ => h ∘ T^[n.toNat])
        ((k.val * τ : ℕ) : ℤ)
      simpa [m, delayObservableAlgebra, Function.comp] using this
    exact hmeas.comap_le
  · -- Conversely every generator `h ∘ T^[n]` is a coordinate of the query
    -- `(n+1, 1)`; the negative indices of the ℤ-indexed family collapse to `h`
    -- itself under `Int.toNat` and are covered by `d = 1`.
    refine observableAlgebra_le fun n => ?_
    set m : ℕ := n.toNat with hm
    have hcomap :
        MeasurableSpace.comap (fun x => delayEval (m + 1) 1 (orbitStream h T x))
            inferInstance ≤ delayQueryAlgebra h T :=
      le_iSup_of_le (m + 1) (le_iSup_of_le 1 le_rfl)
    refine Measurable.mono ?_ hcomap le_rfl
    have hco : Measurable[MeasurableSpace.comap
        (fun x => delayEval (m + 1) 1 (orbitStream h T x)) inferInstance]
        (fun x => delayEval (m + 1) 1 (orbitStream h T x)) :=
      Measurable.of_comap_le le_rfl
    have := (measurable_pi_apply (⟨m, Nat.lt_succ_self m⟩ : Fin (m + 1))).comp hco
    simpa [delayEval_orbitStream, Function.comp] using this

/-! #### Fixed lag: where the pruning lane's index lives

`delayQueryAlgebra` ranges over every lag, and the proof above shows unit lag
alone already achieves the supremum -- so `τ` is invisible to it. That is a fact
about the *supremum*, and it is exactly what has kept this chapter and the
pruning chapter apart: the reconstruction question takes the sup and washes the
lag out, while the pruning question is asked at a fixed lag, which the sup
destroys.

Fixing `τ` puts it back. `delayEval d τ` samples at `0, -τ, …, -(d-1)τ` --
stroboscopic sampling -- and the pruning chapter's layered ring `R_L` has vertex
set `ℤ_L × A`, its layer index being position mod `L`. Same structure: the
delay chapter's lag is the pruning chapter's ring length. The identity below is
what makes that a theorem rather than a resemblance. -/

/-- **Lag-`τ` data is the unit-lag data of the `τ`-th power map.** -/
theorem delayEval_orbitStream_iterate (h : X → ℝ) (T : X → X) (d τ : ℕ) (x : X) :
    delayEval d τ (orbitStream h T x) = fun k : Fin d => delayMap h (T^[τ]) x k.val := by
  rw [delayEval_orbitStream]
  funext k
  simp [delayMap, ← Function.iterate_mul, Nat.mul_comm]

/-- The σ-algebra the delay queries induce **at one fixed lag** `τ`, rather than
across all of them. -/
@[reducible] noncomputable def delayQueryAlgebraAtLag
    (h : X → ℝ) (T : X → X) (τ : ℕ) : MeasurableSpace X :=
  ⨆ d : ℕ, MeasurableSpace.comap (fun x => delayEval d τ (orbitStream h T x)) inferInstance

/-- **Fixed lag resolves exactly the observable algebra of the power map.**

`delayQueryAlgebraAtLag h T τ = 𝒪_h(T^τ)`. So stroboscopic observation at lag
`τ` is not a weaker way of looking at `T`; it is the *same* reconstruction
question asked of `T^τ`. In general `𝒪_h(T^τ) < 𝒪_h(T)` strictly -- the
intermediate times are genuinely lost -- which is why the fixed-lag question has
content that `delayQueryAlgebraEqDelayObservableAlgebra` cannot see.

This is the lemma that gives the pruning lane a definitional anchor here:
`Safe(ρ)` is a statement about which lags reconstruct, and this says what
"reconstructs at lag `τ`" means on the measure-theoretic side. -/
theorem delayQueryAlgebraAtLag_eq (h : X → ℝ) (T : X → X) (τ : ℕ) :
    delayQueryAlgebraAtLag h T τ = delayObservableAlgebra h (T^[τ]) := by
  apply le_antisymm
  · refine iSup_le fun d => ?_
    have hmeas : Measurable[delayObservableAlgebra h (T^[τ])]
        (fun x => delayEval d τ (orbitStream h T x)) := by
      letI m : MeasurableSpace X := delayObservableAlgebra h (T^[τ])
      rw [funext fun x => delayEval_orbitStream_iterate h T d τ x]
      refine measurable_pi_lambda _ fun k => ?_
      have := observableAlgebra_measurable
        (fun n : ℤ => h ∘ (T^[τ])^[n.toNat]) ((k.val : ℕ) : ℤ)
      simpa [m, delayObservableAlgebra, delayMap, Function.comp] using this
    exact hmeas.comap_le
  · refine observableAlgebra_le fun n => ?_
    set m : ℕ := n.toNat with hm
    have hcomap :
        MeasurableSpace.comap (fun x => delayEval (m + 1) τ (orbitStream h T x))
            inferInstance ≤ delayQueryAlgebraAtLag h T τ :=
      le_iSup_of_le (m + 1) le_rfl
    refine Measurable.mono ?_ hcomap le_rfl
    have hco : Measurable[MeasurableSpace.comap
        (fun x => delayEval (m + 1) τ (orbitStream h T x)) inferInstance]
        (fun x => delayEval (m + 1) τ (orbitStream h T x)) :=
      Measurable.of_comap_le le_rfl
    have := (measurable_pi_apply (⟨m, Nat.lt_succ_self m⟩ : Fin (m + 1))).comp hco
    simpa [delayEval_orbitStream_iterate, delayMap, Function.comp] using this

/-- Unit lag is the case where no information is lost: `T^1 = T`. Together with
`delayQueryAlgebraAtLag_eq` this is the sharp form of the remark that the
supremum over lags is already attained at `τ = 1`. -/
theorem delayQueryAlgebraAtLag_one (h : X → ℝ) (T : X → X) :
    delayQueryAlgebraAtLag h T 1 = delayObservableAlgebra h T := by
  simpa using delayQueryAlgebraAtLag_eq h T 1

end ReconstructionBridge
