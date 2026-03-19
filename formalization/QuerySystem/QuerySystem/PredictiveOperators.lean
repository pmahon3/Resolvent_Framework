/-
Copyright (c) 2025. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: [Your Name]
-/
import Mathlib.MeasureTheory.Measure.MeasureSpaceDef
import Mathlib.MeasureTheory.Measure.ProbabilityMeasure
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Probability.Kernel.Basic
import Mathlib.MeasureTheory.Measure.Dirac
import Mathlib.Probability.Kernel.Composition.Comp
import Mathlib.Probability.Kernel.Composition.IntegralCompProd
import QuerySystem.QuerySystem
import QuerySystem.PredictiveState

/-!
# Predictive Operator Theory (Paper 3)

This file formalizes the operator-theoretic content of Paper 3: the semigroup
of predictive operators, the Markov kernel representation, Koopman–Perron duality,
and the deterministic specialization.

## The derivational chain

```
predictive state Q_*  →  horizon-indexed operators K_t
                      →  semigroup K_{t+s} = K_t ∘ K_s  (Chapman–Kolmogorov)
                      →  Markov kernel representation
                      →  Koopman–Perron duality: ∫ K_t g dμ = ∫ g d(P_t^* μ)
                      →  deterministic specialization → classical Koopman operators
```

## Mathematical content

**Horizon-indexed operators.** Given a family of Markov kernels `{Π_t}` on a
state space `γ`, the predictive operator at horizon `t` is:
```
(K_t g)(q) = ∫ q', g q' ∂(Π_t q)
```

**Semigroup.** The Chapman–Kolmogorov equation `Π_{t+s} = Π_t ∘ Π_s` implies:
```
K_{t+s} g = K_t (K_s g)
```
This is the semigroup property. The structure `PredictiveSemigroupKernel` packages
the kernel family together with this equation.

**Koopman–Perron duality.** `K_t` acts on functions; the dual `P_t^*` acts on
measures of predictive states by `P_t^* μ = μ.bind Π_t`. The duality is:
```
∫ (K_t g) dμ = ∫ g d(P_t^* μ)
```

**Deterministic specialization.** When `Π_t q = δ_{φ_t(q)}` for a measurable
flow `φ_t`, the operators reduce to classical Koopman operators: `K_t g = g ∘ φ_t`.

## Main definitions

* `PredictiveKernelFamily`    : a family `{Π_t}` of Markov kernels with identity at 0
* `PredictiveSemigroupKernel` : `PredictiveKernelFamily` + Chapman–Kolmogorov
* `predictiveOpFamily K t g`  : the operator `(K_t g)(q) = ∫ g d(Π_t q)`
* `koopmanPerronDual K t μ`   : the dual `P_t^* μ = μ.bind (Π_t)`

## Main results

* `predictiveOpFamily_at_zero`     : `K_0 = id` — complete proof (P3.1)
* `predictiveOpFamily_positive`    : `g ≥ 0 → K_t g ≥ 0` — complete proof (P3.1)
* `semigroup_id`                   : `K_0 = id` — complete (P3.2)
* `semigroup_property`             : `K_{t+s} = K_t ∘ K_s` — complete (P3.3, bounded g)
* `semigroup_const_one`            : `K_t 1 = 1` — complete (P3.4)
* `semigroup_positive`             : positivity — complete (P3.4)
* `koopman_perron_duality`         : duality — complete (P3.5, bounded g)
* `deterministic_specialization`   : Koopman reduction — complete (P3.6)
* `deterministic_semigroup`        : flow law `φ_{t+s} = φ_t ∘ φ_s` — complete (P3.6)

## Open proof obligations (sorry)

All main theorems are now proved. Key resolving lemmas:
- `Kernel.integral_comp` (Bochner Fubini for kernel composition, from
  `Mathlib.Probability.Kernel.Composition.IntegralCompProd`) resolves both
  `semigroup_property` and `koopman_perron_duality`.
- `Measure.dirac_bind` + `Measure.dirac_eq_dirac_iff` + `K.comp` resolves
  `deterministic_semigroup`.
- Both `semigroup_property` and `koopman_perron_duality` require a bounded
  measurable hypothesis `hg_bdd : ∃ C, ∀ q, |g q| ≤ C` for integrability.

## Notation

In Mathlib, `η ∘ₖ κ : Kernel α γ` for `κ : Kernel α β`, `η : Kernel β γ` means
"apply κ first, then η": `(η ∘ₖ κ) a = (κ a).bind η`.
So `Π_{t+s} = Π_t ∘ₖ Π_s` means "sample via Π_s from state q, then via Π_t",
consistent with `K_{t+s} = K_t ∘ K_s` as function composition.

## References

* Paper 3: *Predictive Operator Theory for Observable Dynamical Systems*
* Mathlib: `ProbabilityTheory.Kernel.Composition`
-/

open MeasureTheory ProbabilityTheory

universe u v

variable {γ : Type v} [MeasurableSpace γ]

/-! ## Kernel family structures -/

/-- A **predictive kernel family** is a family of Markov kernels `{Π_t}_{t : ℕ}`
    on a state space `γ`, with `Π_0 = δ` (identity). -/
structure PredictiveKernelFamily (γ : Type v) [MeasurableSpace γ] where
  /-- The Markov kernel at horizon `t` -/
  Π        : ℕ → Kernel γ γ
  /-- Each kernel is a Markov (probability) kernel -/
  isMarkov : ∀ t, IsMarkovKernel (Π t)
  /-- At horizon 0, `Π_0` is the Dirac kernel: `Π_0 q = δ_q` -/
  at_zero  : ∀ q, Π 0 q = Measure.dirac q

/-- A **predictive semigroup kernel** is a `PredictiveKernelFamily` satisfying
    the Chapman–Kolmogorov (semigroup) equation:
    ```
    Π_{t+s} = Π_t ∘ₖ Π_s
    ```
    i.e. `Π_{t+s} q = (Π_s q).bind Π_t` for all `q`. -/
structure PredictiveSemigroupKernel (γ : Type v) [MeasurableSpace γ] where
  /-- The Markov kernel at horizon `t` -/
  ker      : ℕ → Kernel γ γ
  /-- Each kernel is a Markov (probability) kernel -/
  isMarkov : ∀ t, IsMarkovKernel (ker t)
  /-- At horizon 0, `ker 0 q = δ_q` -/
  at_zero  : ∀ q, ker 0 q = Measure.dirac q
  /-- Chapman–Kolmogorov: `ker(t+s) = ker t ∘ₖ ker s` -/
  comp     : ∀ t s : ℕ, ker (t + s) = (ker t).comp (ker s)

/-- Every `PredictiveSemigroupKernel` yields a `PredictiveKernelFamily`. -/
def PredictiveSemigroupKernel.toFamily (K : PredictiveSemigroupKernel γ) :
    PredictiveKernelFamily γ where
  Π        := K.ker
  isMarkov := K.isMarkov
  at_zero  := K.at_zero

/-! ## Horizon-indexed predictive operators -/

/-- The **horizon-indexed predictive operator** `K_t`.

    For a `PredictiveKernelFamily` and `g : γ → ℝ`:
    ```
    (K_t g)(q) = ∫ q', g q' ∂(Π_t q)
    ``` -/
noncomputable def predictiveOpFamily
    (K : PredictiveKernelFamily γ) (t : ℕ) (g : γ → ℝ) : γ → ℝ :=
  fun q => ∫ q', g q' ∂(K.Π t q)

/-! ## Basic properties (P3.1) -/

/-- **P3.1** At horizon 0, `K_0 g = g` (identity). -/
theorem predictiveOpFamily_at_zero
    (K : PredictiveKernelFamily γ) (g : γ → ℝ) (hg : Measurable g) :
    predictiveOpFamily K 0 g = g := by
  ext q
  simp only [predictiveOpFamily, K.at_zero q]
  exact integral_dirac' g q hg.stronglyMeasurable

/-- **P3.1** Positivity: `g ≥ 0 → K_t g ≥ 0`. -/
theorem predictiveOpFamily_positive
    (K : PredictiveKernelFamily γ) (t : ℕ) (g : γ → ℝ) (hg : ∀ q, 0 ≤ g q) :
    ∀ q, 0 ≤ predictiveOpFamily K t g q :=
  fun q => integral_nonneg hg

/-! ## Semigroup theorem (P3.2 / P3.3) -/

/-- **P3.2** Identity: `K_0 = id`. -/
theorem semigroup_id
    (K : PredictiveSemigroupKernel γ) (g : γ → ℝ) (hg : Measurable g) :
    predictiveOpFamily K.toFamily 0 g = g :=
  predictiveOpFamily_at_zero K.toFamily g hg

/-- **P3.3** Semigroup property: `K_{t+s} = K_t ∘ K_s`.

    For bounded measurable `g : γ → ℝ` (needed for integrability over Markov kernels):
    ```
    (K_{t+s} g)(q)
      = ∫ q', g q' ∂(ker(t+s) q)
      = ∫ q', g q' ∂((ker t ∘ₖ ker s) q)     [Chapman–Kolmogorov: K.comp t s]
      = ∫ q'' (∫ q', g q' ∂(ker t q'')) ∂(ker s q)  [Kernel.integral_comp]
      = (K_t (K_s g))(q)
    ```
    The Bochner Fubini `Kernel.integral_comp` is in
    `Mathlib.Probability.Kernel.Composition.IntegralCompProd`. -/
theorem semigroup_property
    (K : PredictiveSemigroupKernel γ) (t s : ℕ) (g : γ → ℝ) (hg : Measurable g)
    (hg_bdd : ∃ C, ∀ q, |g q| ≤ C) :
    predictiveOpFamily K.toFamily (t + s) g =
    predictiveOpFamily K.toFamily t (predictiveOpFamily K.toFamily s g) := by
  obtain ⟨C, hC⟩ := hg_bdd
  ext q
  simp only [predictiveOpFamily, PredictiveSemigroupKernel.toFamily]
  -- Step 1: rewrite ker(t+s) using Chapman–Kolmogorov
  rw [K.comp t s]
  -- Step 2: apply Kernel.integral_comp: ∫ g d((ker t ∘ₖ ker s) q) = ∫ q'', ∫ g d(ker t q'') d(ker s q)
  -- Need: Integrable g ((ker t ∘ₖ ker s) q)  (bounded + Markov ⇒ finite measure)
  haveI hmt : IsMarkovKernel (K.ker t) := K.isMarkov t
  haveI hms : IsMarkovKernel (K.ker s) := K.isMarkov s
  have hg_int : Integrable g ((K.ker t ∘ₖ K.ker s) q) := by
    apply Integrable.mono' (integrable_const C)
    · exact hg.aestronglyMeasurable
    · exact Filter.Eventually.of_forall (fun q' => hC q')
  rw [Kernel.integral_comp hg_int]

/-! ## Markov properties (P3.4) -/

/-- **P3.4** Constant preservation: `K_t 1 = 1`. -/
theorem semigroup_const_one (K : PredictiveSemigroupKernel γ) (t : ℕ) :
    predictiveOpFamily K.toFamily t (fun _ => (1 : ℝ)) = fun _ => 1 := by
  ext q
  simp only [predictiveOpFamily, PredictiveSemigroupKernel.toFamily]
  haveI : IsProbabilityMeasure (K.ker t q) := (K.isMarkov t).isProbabilityMeasure q
  simp [integral_const, MeasureTheory.measure_univ]

/-- **P3.4** Positivity: `g ≥ 0 → K_t g ≥ 0`. -/
theorem semigroup_positive
    (K : PredictiveSemigroupKernel γ) (t : ℕ) (g : γ → ℝ) (hg : ∀ q, 0 ≤ g q) :
    ∀ q, 0 ≤ predictiveOpFamily K.toFamily t g q :=
  predictiveOpFamily_positive K.toFamily t g hg

/-! ## Koopman–Perron duality (P3.5) -/

/-- The **Koopman–Perron dual** operator `P_t^*` pushes distributions forward:
    ```
    P_t^* μ = μ.bind (ker t)
    ``` -/
noncomputable def koopmanPerronDual
    (K : PredictiveSemigroupKernel γ) (t : ℕ) (μ : Measure γ) : Measure γ :=
  μ.bind (K.ker t)

/-- **P3.5** Koopman–Perron duality: `∫ (K_t g) dμ = ∫ g d(P_t^* μ)`.

    `K_t` acts on observable functions; `P_t^*` acts on distributions of states.
    They are adjoint with respect to integration.

    **Proof:** Use `μ.bind (ker t) = (ker t ∘ₖ Kernel.const Unit μ) ()` and
    `Kernel.integral_comp` (Bochner Fubini for kernel compositions):
    ```
    ∫ g d(μ.bind (ker t))
      = ∫ g d((ker t ∘ₖ Kernel.const Unit μ) ())
      = ∫ x, ∫ g d(ker t x) d(Kernel.const Unit μ ())   [Kernel.integral_comp]
      = ∫ q, ∫ g d(ker t q) dμ                           [const_apply]
      = ∫ q, (K_t g)(q) dμ
    ``` -/
theorem koopman_perron_duality
    (K : PredictiveSemigroupKernel γ) (t : ℕ) (g : γ → ℝ) (hg : Measurable g)
    (hg_bdd : ∃ C, ∀ q, |g q| ≤ C)
    (μ : Measure γ) [IsFiniteMeasure μ] :
    ∫ q, predictiveOpFamily K.toFamily t g q ∂μ =
    ∫ q', g q' ∂koopmanPerronDual K t μ := by
  obtain ⟨C, hC⟩ := hg_bdd
  simp only [predictiveOpFamily, PredictiveSemigroupKernel.toFamily, koopmanPerronDual]
  -- Rewrite RHS using kernel composition: μ.bind (ker t) = (ker t ∘ₖ Kernel.const Unit μ) ()
  haveI hmt : IsMarkovKernel (K.ker t) := K.isMarkov t
  rw [Measure.comp_eq_comp_const_apply (κ := K.ker t) (μ := μ)]
  -- Apply Kernel.integral_comp:
  -- ∫ g d((ker t ∘ₖ Kernel.const Unit Unit μ) ()) = ∫ x, ∫ g d(ker t x) d(Kernel.const Unit μ ())
  have hg_int : Integrable g ((K.ker t ∘ₖ Kernel.const Unit μ) ()) := by
    apply Integrable.mono' (integrable_const C)
    · exact hg.aestronglyMeasurable
    · exact Filter.Eventually.of_forall (fun q' => hC q')
  rw [Kernel.integral_comp hg_int]
  -- Simplify: Kernel.const Unit μ () = μ
  simp [Kernel.const_apply]

/-! ## Deterministic specialization (P3.6) -/

/-- **P3.6** Deterministic specialization.

    If `ker t q = δ_{φ_t(q)}` for a measurable flow `φ_t : γ → γ`, then:
    ```
    K_t g = g ∘ φ_t
    ```
    recovering the classical Koopman operator. -/
theorem deterministic_specialization
    (K : PredictiveSemigroupKernel γ) (t : ℕ) (φ : γ → γ) (hφ : Measurable φ)
    (g : γ → ℝ) (hg : Measurable g)
    (h_det : ∀ q, K.ker t q = Measure.dirac (φ q)) :
    predictiveOpFamily K.toFamily t g = g ∘ φ := by
  ext q
  simp only [predictiveOpFamily, PredictiveSemigroupKernel.toFamily, Function.comp, h_det q]
  exact integral_dirac' g (φ q) hg.stronglyMeasurable

/-- **P3.6 Corollary** The flow semigroup law `φ_{t+s} = φ_t ∘ φ_s`.

    When all kernels are Dirac, Chapman–Kolmogorov recovers the classical flow law.

    **Proof:**
    ```
    dirac (φ (t+s) q)
      = ker(t+s) q                    [h_det (t+s) q]
      = (ker t ∘ₖ ker s) q            [K.comp t s]
      = (ker s q).bind (ker t)         [Kernel.comp_apply]
      = (dirac (φ s q)).bind (ker t)   [h_det s q]
      = ker t (φ s q)                  [Measure.dirac_bind]
      = dirac (φ t (φ s q))            [h_det t (φ s q)]
    ```
    Conclude by `Measure.dirac_eq_dirac_iff` under `[SeparatesPoints γ]`. -/
theorem deterministic_semigroup
    (K : PredictiveSemigroupKernel γ) (φ : ℕ → γ → γ)
    (hφ : ∀ t, Measurable (φ t))
    (h_det : ∀ t q, K.ker t q = Measure.dirac (φ t q))
    [SeparatesPoints γ] (t s : ℕ) (q : γ) :
    φ (t + s) q = φ t (φ s q) := by
  -- The Dirac measures on both sides are equal; extract the points by injectivity
  rw [← Measure.dirac_eq_dirac_iff]
  -- LHS: dirac (φ (t+s) q) = ker(t+s) q
  rw [← h_det (t + s) q]
  -- Apply Chapman–Kolmogorov and unfold the kernel composition
  rw [K.comp t s, Kernel.comp_apply, h_det s q]
  -- (dirac (φ s q)).bind (ker t) = ker t (φ s q)
  rw [Measure.dirac_bind (K.ker t).measurable]
  -- ker t (φ s q) = dirac (φ t (φ s q))
  exact h_det t (φ s q)
