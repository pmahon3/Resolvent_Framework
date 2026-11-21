/-
Machine-checked pieces of the running examples and of the Cauchy–Schwarz step in
`~/Work/INN-Science/identification-through-reduction/paper/core.tex` (2026-11-20).

* Example B (Landau free energy with a slaved secondary variable `y`, record `m`):
  - `F_complete_square`: a field `h` on the hidden variable shifts the quadratic coefficient `a`
    by `-2hc` and adds a constant;
  - `landau_marginal`: the `y`-integral of the Boltzmann weight equals the Boltzmann weight of the
    shifted effective potential times `√(2π/(βk))`, a constant independent of `m`. With `h = 0`
    this is the exactness of the reduction `ρ(θ) = (a,b)` (the fibre `(c,k)` is invisible in the
    record); with `h ≠ 0` it is the counterexample of §4.3: the response to a field on the hidden
    variable is proportional to the fibre coordinate `c`;
  - `landau_conditional_mean`: `E[y | m] = c m²` (as the Gaussian mean), the instance of
    Proposition 4's conditional mean.
* `response_sq_le_var_mul_info`: the Cauchy–Schwarz step behind the paper's (eq:cramerrao):
  the squared covariance of a centred statistic with a score is at most variance × information.
* Example C (two-dimensional OU process, record `x`):
  - `exampleC_scaling_invariants`: the four spectral combinations are invariant under the scaling
    direction of the fibre;
  - `exampleC_response_x`: the static response of `x` to a unit push on `x` is `δ/(αδ − κκ')`,
    which is not one of the four combinations;
  - `reversible_inverse`: if `A P = Σ/2` (reversibility) then `A⁻¹ = 2 P Σ⁻¹`, so the same
    response is a functional of the stationary covariance.

Not formalised: the general Proposition 4 (differentiation under the integral sign), the
constant-rank local forms of Propositions 2–3, and anything about the leak.
-/
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.MeasureTheory.Group.Integral
import Mathlib.Algebra.QuadraticDiscriminant
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Data.Fin.VecNotation
import Mathlib.Analysis.Calculus.ParametricIntegral
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Calculus.Deriv.Inv

open MeasureTheory Real

namespace ReductionExamples

/-! ### Example B -/

/-- Free energy of Example B with a field `h` on the hidden variable `y`. -/
noncomputable def F (a b c k h m y : ℝ) : ℝ :=
  a / 2 * m ^ 2 + b / 4 * m ^ 4 + k / 2 * (y - c * m ^ 2) ^ 2 - h * y

/-- Completing the square: the field on `y` shifts `a` by `-2hc` and adds `-h²/(2k)`. -/
theorem F_complete_square (a b c k h m y : ℝ) (hk : k ≠ 0) :
    F a b c k h m y
      = (a - 2 * h * c) / 2 * m ^ 2 + b / 4 * m ^ 4
        + k / 2 * (y - (c * m ^ 2 + h / k)) ^ 2 - h ^ 2 / (2 * k) := by
  unfold F
  field_simp
  ring

/-- The record law of Example B. The `y`-integral of the Boltzmann weight is the Boltzmann
weight of the effective potential `(a-2hc)/2 m² + b/4 m⁴ - h²/(2k)` times a constant that does
not depend on `m`. -/
theorem landau_marginal (β a b c k h m : ℝ) (hβ : 0 < β) (hk : 0 < k) :
    ∫ y : ℝ, exp (-β * F a b c k h m y)
      = exp (-β * ((a - 2 * h * c) / 2 * m ^ 2 + b / 4 * m ^ 4 - h ^ 2 / (2 * k)))
        * √(2 * π / (β * k)) := by
  have h1 : (fun y : ℝ => exp (-β * F a b c k h m y))
      = fun y => exp (-β * ((a - 2 * h * c) / 2 * m ^ 2 + b / 4 * m ^ 4 - h ^ 2 / (2 * k)))
                  * exp (-(β * k / 2) * (y - (c * m ^ 2 + h / k)) ^ 2) := by
    funext y
    rw [F_complete_square a b c k h m y hk.ne', ← exp_add]
    congr 1
    ring
  rw [h1, integral_const_mul]
  congr 1
  have h2 : ∫ y : ℝ, exp (-(β * k / 2) * (y - (c * m ^ 2 + h / k)) ^ 2)
      = ∫ y : ℝ, exp (-(β * k / 2) * y ^ 2) :=
    integral_sub_right_eq_self (μ := volume) (fun y : ℝ => exp (-(β * k / 2) * y ^ 2)) (c * m ^ 2 + h / k)
  rw [h2, integral_gaussian]
  congr 1
  field_simp

/-- An odd Gaussian moment vanishes. -/
theorem integral_mul_exp_neg_mul_sq_eq_zero (b : ℝ) :
    ∫ y : ℝ, y * exp (-b * y ^ 2) = 0 := by
  have h := integral_neg_eq_self (fun y : ℝ => y * exp (-b * y ^ 2)) volume
  simp only [neg_sq, neg_mul] at h
  rw [integral_neg] at h
  have h' : ∫ y : ℝ, y * exp (-b * y ^ 2) = ∫ y : ℝ, y * exp (-(b * y ^ 2)) := by
    congr 1; funext y; ring_nf
  rw [h']
  linarith

/-- The conditional mean of the hidden variable given the record in Example B:
`∫ y e^{-b(y-s)²} = s ∫ e^{-b(y-s)²}`, i.e. `E[y | m] = s` with `s = c m²`. -/
theorem landau_conditional_mean (b s : ℝ) (hb : 0 < b) :
    ∫ y : ℝ, y * exp (-b * (y - s) ^ 2) = s * ∫ y : ℝ, exp (-b * (y - s) ^ 2) := by
  have hs1 : ∫ y : ℝ, y * exp (-b * (y - s) ^ 2)
      = ∫ y : ℝ, (y + s) * exp (-b * y ^ 2) := by
    have := integral_sub_right_eq_self (μ := volume) (fun y : ℝ => (y + s) * exp (-b * y ^ 2)) s
    simp only [sub_add_cancel] at this
    exact this
  have hs2 : ∫ y : ℝ, exp (-b * (y - s) ^ 2) = ∫ y : ℝ, exp (-b * y ^ 2) :=
    integral_sub_right_eq_self (μ := volume) (fun y : ℝ => exp (-b * y ^ 2)) s
  rw [hs1, hs2]
  have hint1 : Integrable (fun y : ℝ => y * exp (-b * y ^ 2)) := integrable_mul_exp_neg_mul_sq hb
  have hint2 : Integrable (fun y : ℝ => s * exp (-b * y ^ 2)) :=
    (integrable_exp_neg_mul_sq hb).const_mul s
  have hsplit : (fun y : ℝ => (y + s) * exp (-b * y ^ 2))
      = fun y => y * exp (-b * y ^ 2) + s * exp (-b * y ^ 2) := by
    funext y
    ring
  rw [hsplit, integral_add hint1 hint2, integral_mul_exp_neg_mul_sq_eq_zero, integral_const_mul,
    zero_add]

/-! ### The Cauchy–Schwarz step behind (eq:cramerrao) -/

/-- If `B₀` is a centred statistic and `ℓ` a score, the squared covariance `(E[B₀ ℓ])²` is at most
`E[B₀²] · E[ℓ²]`: variance times information. The derivative identity `∂_v E[B] = E[B₀ ℓ]` is the
differentiability hypothesis of the paper and is not part of this statement. -/
theorem response_sq_le_var_mul_info {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    (B₀ ℓ : Ω → ℝ)
    (h00 : Integrable (fun ω => B₀ ω * B₀ ω) μ)
    (hll : Integrable (fun ω => ℓ ω * ℓ ω) μ)
    (h0l : Integrable (fun ω => B₀ ω * ℓ ω) μ) :
    (∫ ω, B₀ ω * ℓ ω ∂μ) ^ 2 ≤ (∫ ω, B₀ ω * B₀ ω ∂μ) * (∫ ω, ℓ ω * ℓ ω ∂μ) := by
  set V := ∫ ω, B₀ ω * B₀ ω ∂μ with hV
  set I := ∫ ω, ℓ ω * ℓ ω ∂μ with hI
  set C := ∫ ω, B₀ ω * ℓ ω ∂μ with hC
  have key : ∀ t : ℝ, 0 ≤ I * (t * t) + (-2 * C) * t + V := by
    intro t
    have hnn : 0 ≤ ∫ ω, (B₀ ω - t * ℓ ω) ^ 2 ∂μ :=
      integral_nonneg (fun ω => sq_nonneg _)
    have hexp : (fun ω => (B₀ ω - t * ℓ ω) ^ 2)
        = fun ω => (B₀ ω * B₀ ω + (-2 * t) * (B₀ ω * ℓ ω)) + (t * t) * (ℓ ω * ℓ ω) := by
      funext ω
      ring
    have hsum : ∫ ω, (B₀ ω * B₀ ω + (-2 * t) * (B₀ ω * ℓ ω)) + (t * t) * (ℓ ω * ℓ ω) ∂μ
        = V + (-2 * t) * C + (t * t) * I := by
      have e1 := integral_add (μ := μ) (h00.add (h0l.const_mul (-2 * t))) (hll.const_mul (t * t))
      have e2 := integral_add (μ := μ) h00 (h0l.const_mul (-2 * t))
      simp only [Pi.add_apply] at e1 e2
      rw [e1, e2, integral_const_mul, integral_const_mul]
    rw [hexp, hsum] at hnn
    linarith [hnn]
  have hd := discrim_le_zero key
  unfold discrim at hd
  nlinarith [hd]

/-! ### Example C -/

/-- The four combinations that the record determines in Example C are invariant under the
scaling direction `(κ, κ', σ_y) ↦ (λκ, κ'/λ, σ_y/λ)` of the fibre. -/
theorem exampleC_scaling_invariants (α δ κ κ' σx σy lam : ℝ) (hl : lam ≠ 0) :
    (α + δ, α * δ - (lam * κ) * (κ' / lam), σx ^ 2, δ ^ 2 * σx ^ 2 + (lam * κ) ^ 2 * (σy / lam) ^ 2)
      = (α + δ, α * δ - κ * κ', σx ^ 2, δ ^ 2 * σx ^ 2 + κ ^ 2 * σy ^ 2) := by
  simp only [Prod.mk.injEq, true_and]
  constructor
  · field_simp
  · field_simp

/-- The drift matrix of Example C. -/
def Adrift (α δ κ κ' : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := Matrix.of ![![α, κ], ![κ', δ]]

/-- The static response of the recorded coordinate `x` to a unit push on `x` is `(A⁻¹)₁₁ = δ/(αδ − κκ')`.
It depends on `δ`, which is not a function of the four spectral combinations. -/
theorem exampleC_response_x (α δ κ κ' : ℝ) (hdet : α * δ - κ * κ' ≠ 0) :
    (Adrift α δ κ κ')⁻¹ 0 0 = δ / (α * δ - κ * κ') := by
  have hdet' : -(κ' * κ) + α * δ ≠ 0 := by
    intro h0; apply hdet; linarith
  have hinv : (Adrift α δ κ κ')⁻¹ = (α * δ - κ * κ')⁻¹ • Matrix.of ![![δ, -κ], ![-κ', α]] := by
    apply Matrix.inv_eq_right_inv
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Adrift, Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply] <;>
      (try field_simp [hdet']) <;>
      first | ring1 | (rw [← mul_inv_cancel₀ hdet']; ring1)
  rw [hinv]
  simp [Matrix.of_apply, div_eq_inv_mul]

/-- Reversibility `A P = Σ/2` makes the static response a functional of the stationary covariance:
`A⁻¹ = 2 P Σ⁻¹` (written `S` below since `Σ` is reserved). -/
theorem reversible_inverse {n : Type*} [Fintype n] [DecidableEq n]
    (A P S : Matrix n n ℝ) (hS : IsUnit S.det) (h : A * P = (1 / 2 : ℝ) • S) :
    A⁻¹ = (2 : ℝ) • (P * S⁻¹) := by
  apply Matrix.inv_eq_right_inv
  calc A * ((2 : ℝ) • (P * S⁻¹)) = (2 : ℝ) • (A * P * S⁻¹) := by
          rw [Matrix.mul_smul, Matrix.mul_assoc]
    _ = (2 : ℝ) • (((1 / 2 : ℝ) • S) * S⁻¹) := by rw [h]
    _ = S * S⁻¹ := by rw [Matrix.smul_mul, smul_smul]; norm_num
    _ = 1 := Matrix.mul_nonsing_inv S hS

/-! ### Proposition 4: the derivative of the effective potential -/

open Metric Filter in
/-- Proposition 4 in the equilibrium case, at a fixed value of the recorded coordinate. With
`U = U(x,·)` and `V = V(x,·)` as functions of the hidden coordinate `y`, the effective potential
`h ↦ -β⁻¹ log ∫ exp(-β(U - hV)) dy` has derivative `-E[V | x]` at `h = 0`, where
`E[V | x] = ∫ V e^{-βU} dy / ∫ e^{-βU} dy`. Hypotheses: `U`, `V` measurable; the Boltzmann weight
integrable; and the dominating function `β|V| e^{-βU} e^{βε|V|}` integrable for some window
`|h| < ε`. -/
theorem effective_potential_hasDerivAt (β : ℝ) (hβ : 0 < β) (U V : ℝ → ℝ)
    (hU : Measurable U) (hV : Measurable V) (ε : ℝ) (hε : 0 < ε)
    (hint : Integrable (fun y => exp (-β * U y)))
    (hbound : Integrable (fun y => β * |V y| * exp (-β * U y) * exp (β * ε * |V y|))) :
    HasDerivAt (fun h : ℝ => -β⁻¹ * log (∫ y, exp (-β * (U y - h * V y))))
      (-(∫ y, V y * exp (-β * U y)) / ∫ y, exp (-β * U y)) 0 := by
  have hmeas : ∀ h : ℝ,
      AEStronglyMeasurable (fun y => exp (-β * (U y - h * V y))) volume := fun h =>
    (Real.measurable_exp.comp (measurable_const.mul (hU.sub (measurable_const.mul hV)))).aestronglyMeasurable
  have hint0 : Integrable (fun y => exp (-β * (U y - (0:ℝ) * V y))) := by
    simpa using hint
  have hF'meas : AEStronglyMeasurable (fun y => β * V y * exp (-β * (U y - (0:ℝ) * V y))) volume :=
    ((measurable_const.mul hV).mul
      (Real.measurable_exp.comp (measurable_const.mul (hU.sub (measurable_const.mul hV))))).aestronglyMeasurable
  have h_bound : ∀ᵐ y ∂volume, ∀ h ∈ ball (0:ℝ) ε,
      ‖β * V y * exp (-β * (U y - h * V y))‖ ≤ β * |V y| * exp (-β * U y) * exp (β * ε * |V y|) := by
    refine Eventually.of_forall (fun y h hh => ?_)
    rw [mem_ball, dist_zero_right, Real.norm_eq_abs] at hh
    have e1 : exp (-β * (U y - h * V y)) = exp (-β * U y) * exp (β * (h * V y)) := by
      rw [← exp_add]; congr 1; ring
    have e2 : exp (β * (h * V y)) ≤ exp (β * ε * |V y|) := by
      apply exp_le_exp.mpr
      calc β * (h * V y) ≤ β * |h * V y| := by gcongr; exact le_abs_self _
        _ = β * (|h| * |V y|) := by rw [abs_mul]
        _ ≤ β * (ε * |V y|) := by gcongr
        _ = β * ε * |V y| := by ring
    rw [Real.norm_eq_abs, abs_mul, abs_mul, abs_of_pos hβ, abs_of_pos (exp_pos _), e1]
    calc β * |V y| * (exp (-β * U y) * exp (β * (h * V y)))
        = β * |V y| * exp (-β * U y) * exp (β * (h * V y)) := by ring
      _ ≤ β * |V y| * exp (-β * U y) * exp (β * ε * |V y|) := by gcongr
  have h_diff : ∀ᵐ y ∂volume, ∀ h ∈ ball (0:ℝ) ε,
      HasDerivAt (fun h => exp (-β * (U y - h * V y))) (β * V y * exp (-β * (U y - h * V y))) h := by
    refine Eventually.of_forall (fun y h _ => ?_)
    have h1 : HasDerivAt (fun x : ℝ => -β * (U y - x * V y)) (-β * -(V y)) h :=
      ((hasDerivAt_mul_const (V y)).const_sub (U y)).const_mul (-β)
    convert h1.exp using 1
    ring
  obtain ⟨_, hZ⟩ := hasDerivAt_integral_of_dominated_loc_of_deriv_le (μ := volume)
    (F := fun h y => exp (-β * (U y - h * V y)))
    (F' := fun h y => β * V y * exp (-β * (U y - h * V y)))
    (ball_mem_nhds (0:ℝ) hε) (Eventually.of_forall hmeas) hint0 hF'meas h_bound hbound h_diff
  have hpos : 0 < ∫ y, exp (-β * U y) := by
    rw [integral_pos_iff_support_of_nonneg (fun y => (exp_pos _).le) hint]
    have hsupp : Function.support (fun y : ℝ => exp (-β * U y)) = Set.univ := by
      ext y; simp [exp_ne_zero]
    rw [hsupp]
    exact Measure.measure_univ_pos.mpr (NeZero.ne _)
  have hZ' : HasDerivAt (fun h : ℝ => ∫ y, exp (-β * (U y - h * V y)))
      (β * ∫ y, V y * exp (-β * U y)) 0 := by
    convert hZ using 1
    simp only [zero_mul, sub_zero]
    rw [← integral_const_mul]
    congr 1
    funext y
    ring
  have hZ0 : (∫ y, exp (-β * (U y - (0:ℝ) * V y))) ≠ 0 := by
    simpa using hpos.ne'
  have hlog := (Real.hasDerivAt_log hZ0).comp (0:ℝ) hZ'
  have hfinal := hlog.const_mul (-β⁻¹)
  convert hfinal using 1
  simp only [zero_mul, sub_zero]
  field_simp

/-- Corollary of Proposition 4: when the perturbing potential depends on the recorded coordinate
alone, its conditional mean given the record is itself, so the induced shift of the reduced
coefficients does not depend on the hidden coordinates at all (and a fortiori lies in the
identified algebra). Stated as the identity `∫ c f / ∫ f = c` for the Boltzmann weight `f`. -/
theorem conditional_mean_of_recorded (f : ℝ → ℝ) (c : ℝ) (hf : ∫ y, f y ≠ 0) :
    (∫ y, c * f y) / ∫ y, f y = c := by
  rw [integral_const_mul]
  field_simp

/-! ### The local forms: glue between the constant rank theorem and identification

The constant rank theorem (cited, not formalised) gives, near a point where `Dρ` has constant
rank, a `C¹` parametrisation `γ` of the fibre by a connected open set `W` with `range (Dγ x) = ker Dρ(γ x)`.
What remains is pure calculus: a differentiable `g` is constant on the parametrised piece iff
`Dg ∘ Dγ = 0` on `W`, and `Dg ∘ Dγ = 0` iff `Dg` kills the range of `Dγ`. Both are checked here. -/

/-- `g' ∘ γ' = 0` iff `g'` vanishes on the range of `γ'`. -/
theorem comp_eq_zero_iff_range {E F G : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F] [NormedAddCommGroup G] [NormedSpace ℝ G]
    (g' : F →L[ℝ] G) (γ' : E →L[ℝ] F) :
    g'.comp γ' = 0 ↔ ∀ v ∈ LinearMap.range (γ' : E →ₗ[ℝ] F), g' v = 0 := by
  constructor
  · intro h v hv
    obtain ⟨u, rfl⟩ := LinearMap.mem_range.mp hv
    have := congrArg (fun T : E →L[ℝ] G => T u) h
    simpa using this
  · intro h
    ext u
    exact h (γ' u) (LinearMap.mem_range.mpr ⟨u, rfl⟩)

/-- On a connected open set `W` parametrising a piece of the fibre, `g ∘ γ` is constant iff
`(Dg)(γ x) ∘ (Dγ)(x) = 0` for every `x ∈ W`. -/
theorem const_on_fibre_iff_fderiv_comp_zero {E Θ G : Type*}
    [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup Θ] [NormedSpace ℝ Θ]
    [NormedAddCommGroup G] [NormedSpace ℝ G]
    (W : Set E) (hW : IsOpen W) (hWc : IsPreconnected W)
    (γ : E → Θ) (hγ : ∀ x ∈ W, DifferentiableAt ℝ γ x)
    (g : Θ → G) (hg : ∀ x ∈ W, DifferentiableAt ℝ g (γ x)) :
    (∀ x ∈ W, ∀ y ∈ W, g (γ x) = g (γ y))
      ↔ ∀ x ∈ W, (fderiv ℝ g (γ x)).comp (fderiv ℝ γ x) = 0 := by
  constructor
  · intro hconst x hx
    rw [← fderiv_comp x (hg x hx) (hγ x hx)]
    have hev : (g ∘ γ) =ᶠ[nhds x] fun _ => g (γ x) :=
      Filter.eventually_of_mem (hW.mem_nhds hx) (fun y hy => hconst y hy x hx)
    rw [hev.fderiv_eq, fderiv_const_apply]
  · intro hzero x hx y hy
    have hdiff : DifferentiableOn ℝ (g ∘ γ) W := fun z hz =>
      ((hg z hz).comp z (hγ z hz)).differentiableWithinAt
    have hzero' : W.EqOn (fderiv ℝ (g ∘ γ)) 0 := fun z hz => by
      rw [fderiv_comp z (hg z hz) (hγ z hz)]
      exact hzero z hz
    exact hW.is_const_of_fderiv_eq_zero hWc hdiff hzero' hx hy

/-! ### The sample-complexity line, made exact -/

/-- If the sampling deviation of a statistic at record length `T` is `σ/√T`, it falls below a
backward error `β` iff `T ≥ σ²/β²`. The modelling content is the hypothesis on the deviation;
the arithmetic is this. -/
theorem sample_complexity_iff (σ β T : ℝ) (hσ : 0 ≤ σ) (hβ : 0 < β) (hT : 0 < T) :
    σ / √T ≤ β ↔ σ ^ 2 / β ^ 2 ≤ T := by
  have hsT : 0 < √T := Real.sqrt_pos.mpr hT
  rw [div_le_iff₀ hsT, div_le_iff₀ (by positivity : (0:ℝ) < β ^ 2)]
  constructor
  · intro h
    have h2 : σ ^ 2 ≤ (β * √T) ^ 2 := by
      have : 0 ≤ β * √T := by positivity
      exact pow_le_pow_left₀ hσ h 2
    calc σ ^ 2 ≤ (β * √T) ^ 2 := h2
      _ = T * β ^ 2 := by rw [mul_pow, Real.sq_sqrt hT.le]; ring
  · intro h
    have h2 : σ ^ 2 ≤ (β * √T) ^ 2 := by
      calc σ ^ 2 ≤ T * β ^ 2 := h
        _ = (β * √T) ^ 2 := by rw [mul_pow, Real.sq_sqrt hT.le]; ring
    have : 0 ≤ β * √T := by positivity
    exact (pow_le_pow_iff_left₀ hσ this (by norm_num : (2:ℕ) ≠ 0)).mp h2

/-! ### The drift correction of Example A, differentiated in the fast rate -/

/-- The corrected slow drift `ẋ₀(1 + 2abx²/γ) + abσ²x/γ` of Example A has derivative
`-(2abx²ẋ₀ + abσ²x)/γ²` in `γ`. The Fisher information of a drift parameter is `T/σ²` times the
stationary mean of the square of this derivative (Girsanov; cited), which is the rate in the text. -/
theorem drift_deriv_gamma (a b σ x x0 γ : ℝ) (hγ : γ ≠ 0) :
    HasDerivAt (fun γ : ℝ => x0 * (1 + 2 * a * b * x ^ 2 / γ) + a * b * σ ^ 2 * x / γ)
      (-(2 * a * b * x ^ 2 * x0 + a * b * σ ^ 2 * x) / γ ^ 2) γ := by
  have h1 : HasDerivAt (fun γ : ℝ => x0 + (2 * a * b * x ^ 2 * x0 + a * b * σ ^ 2 * x) * γ⁻¹)
      ((2 * a * b * x ^ 2 * x0 + a * b * σ ^ 2 * x) * (-(γ ^ 2)⁻¹)) γ :=
    ((hasDerivAt_inv hγ).const_mul _).const_add x0
  convert h1 using 1
  · funext γ'
    by_cases hγ' : γ' = 0
    · subst hγ'; simp
    · field_simp; ring
  · field_simp

/-! ### Proposition 5: the averaged reduced effect at `ε = 0`

For a slow–fast system whose fast sector at frozen `x` is a gradient diffusion with potential
`U(x,·)` and a perturbation `-hV(x,·)`, the averaged slow drift is `F̄_h(x) = ∫ F(x,z) ν^h_x(dz)` with
`ν^h_x ∝ exp(-β(U - hV))`. Its derivative at `h = 0` is `β Cov_{ν_x}(F, V)`. The next two theorems
check this at a fixed `x`, with `U, V, F` functions of the fast coordinate alone. -/

open Metric Filter in
/-- Differentiation of a weighted Boltzmann integral in the tilt amplitude. -/
theorem tilt_integral_hasDerivAt (β : ℝ) (hβ : 0 < β) (U V W : ℝ → ℝ)
    (hU : Measurable U) (hV : Measurable V) (hW : Measurable W) (ε : ℝ) (hε : 0 < ε)
    (hint : Integrable (fun y => W y * exp (-β * U y)))
    (hbound : Integrable (fun y => |W y| * (β * |V y| * exp (-β * U y) * exp (β * ε * |V y|)))) :
    HasDerivAt (fun h : ℝ => ∫ y, W y * exp (-β * (U y - h * V y)))
      (∫ y, W y * (β * V y * exp (-β * U y))) 0 := by
  have hmeasE : ∀ h : ℝ, Measurable (fun y => exp (-β * (U y - h * V y))) := fun h =>
    Real.measurable_exp.comp (measurable_const.mul (hU.sub (measurable_const.mul hV)))
  have hmeas : ∀ h : ℝ, AEStronglyMeasurable (fun y => W y * exp (-β * (U y - h * V y))) volume :=
    fun h => (hW.mul (hmeasE h)).aestronglyMeasurable
  have hint0 : Integrable (fun y => W y * exp (-β * (U y - (0:ℝ) * V y))) := by simpa using hint
  have hF'meas : AEStronglyMeasurable
      (fun y => W y * (β * V y * exp (-β * (U y - (0:ℝ) * V y)))) volume :=
    (hW.mul ((measurable_const.mul hV).mul (hmeasE 0))).aestronglyMeasurable
  have h_bound : ∀ᵐ y ∂volume, ∀ h ∈ ball (0:ℝ) ε,
      ‖W y * (β * V y * exp (-β * (U y - h * V y)))‖
        ≤ |W y| * (β * |V y| * exp (-β * U y) * exp (β * ε * |V y|)) := by
    refine Eventually.of_forall (fun y h hh => ?_)
    rw [mem_ball, dist_zero_right, Real.norm_eq_abs] at hh
    have e1 : exp (-β * (U y - h * V y)) = exp (-β * U y) * exp (β * (h * V y)) := by
      rw [← exp_add]; congr 1; ring
    have e2 : exp (β * (h * V y)) ≤ exp (β * ε * |V y|) := by
      apply exp_le_exp.mpr
      calc β * (h * V y) ≤ β * |h * V y| := by gcongr; exact le_abs_self _
        _ = β * (|h| * |V y|) := by rw [abs_mul]
        _ ≤ β * (ε * |V y|) := by gcongr
        _ = β * ε * |V y| := by ring
    rw [Real.norm_eq_abs, abs_mul, abs_mul, abs_mul, abs_of_pos hβ, abs_of_pos (exp_pos _), e1]
    have hw : 0 ≤ |W y| := abs_nonneg _
    calc |W y| * (β * |V y| * (exp (-β * U y) * exp (β * (h * V y))))
        = |W y| * (β * |V y| * exp (-β * U y) * exp (β * (h * V y))) := by ring
      _ ≤ |W y| * (β * |V y| * exp (-β * U y) * exp (β * ε * |V y|)) := by gcongr
  have h_diff : ∀ᵐ y ∂volume, ∀ h ∈ ball (0:ℝ) ε,
      HasDerivAt (fun h => W y * exp (-β * (U y - h * V y)))
        (W y * (β * V y * exp (-β * (U y - h * V y)))) h := by
    refine Eventually.of_forall (fun y h _ => ?_)
    have h1 : HasDerivAt (fun x : ℝ => -β * (U y - x * V y)) (-β * -(V y)) h :=
      ((hasDerivAt_mul_const (V y)).const_sub (U y)).const_mul (-β)
    convert h1.exp.const_mul (W y) using 1
    ring
  obtain ⟨_, hZ⟩ := hasDerivAt_integral_of_dominated_loc_of_deriv_le (μ := volume)
    (F := fun h y => W y * exp (-β * (U y - h * V y)))
    (F' := fun h y => W y * (β * V y * exp (-β * (U y - h * V y))))
    (ball_mem_nhds (0:ℝ) hε) (Eventually.of_forall hmeas) hint0 hF'meas h_bound hbound h_diff
  simpa using hZ

open Metric Filter in
/-- **Proposition 5 (averaged reduced effect).** At a fixed value of the slow coordinate, with
`ν^h ∝ exp(-β(U - hV))` the tilted conditional law of the fast coordinate and `F̄_h = ∫ F dν^h` the
averaged slow drift, `d/dh F̄_h |_{h=0} = β (E[FV] - E[F] E[V]) = β Cov(F, V)` under `ν^0`. -/
theorem averaged_drift_hasDerivAt (β : ℝ) (hβ : 0 < β) (U V F : ℝ → ℝ)
    (hU : Measurable U) (hV : Measurable V) (hF : Measurable F) (ε : ℝ) (hε : 0 < ε)
    (hint : Integrable (fun y => exp (-β * U y)))
    (hintF : Integrable (fun y => F y * exp (-β * U y)))
    (hbound : Integrable (fun y => β * |V y| * exp (-β * U y) * exp (β * ε * |V y|)))
    (hboundF : Integrable (fun y => |F y| * (β * |V y| * exp (-β * U y) * exp (β * ε * |V y|)))) :
    HasDerivAt
      (fun h : ℝ => (∫ y, F y * exp (-β * (U y - h * V y))) / ∫ y, exp (-β * (U y - h * V y)))
      (β * ((∫ y, F y * V y * exp (-β * U y)) / (∫ y, exp (-β * U y))
            - ((∫ y, F y * exp (-β * U y)) / (∫ y, exp (-β * U y)))
              * ((∫ y, V y * exp (-β * U y)) / (∫ y, exp (-β * U y))))) 0 := by
  have hZ : HasDerivAt (fun h : ℝ => ∫ y, exp (-β * (U y - h * V y)))
      (∫ y, (1:ℝ) * (β * V y * exp (-β * U y))) 0 := by
    have := tilt_integral_hasDerivAt β hβ U V (fun _ => (1:ℝ)) hU hV measurable_const ε hε
      (by simpa using hint) (by simpa using hbound)
    simpa using this
  have hN : HasDerivAt (fun h : ℝ => ∫ y, F y * exp (-β * (U y - h * V y)))
      (∫ y, F y * (β * V y * exp (-β * U y))) 0 :=
    tilt_integral_hasDerivAt β hβ U V F hU hV hF ε hε hintF hboundF
  have hpos : 0 < ∫ y, exp (-β * U y) := by
    rw [integral_pos_iff_support_of_nonneg (fun y => (exp_pos _).le) hint]
    have hsupp : Function.support (fun y : ℝ => exp (-β * U y)) = Set.univ := by
      ext y; simp [exp_ne_zero]
    rw [hsupp]
    exact Measure.measure_univ_pos.mpr (NeZero.ne _)
  have hZ0 : (∫ y, exp (-β * (U y - (0:ℝ) * V y))) ≠ 0 := by simpa using hpos.ne'
  have hq := hN.div hZ hZ0
  convert hq using 1
  simp only [zero_mul, sub_zero, one_mul]
  have e1 : (∫ y, F y * (β * V y * exp (-β * U y))) = β * ∫ y, F y * V y * exp (-β * U y) := by
    rw [← integral_const_mul]; congr 1; funext y; ring
  have e2 : (∫ y, β * V y * exp (-β * U y)) = β * ∫ y, V y * exp (-β * U y) := by
    rw [← integral_const_mul]; congr 1; funext y; ring
  rw [e1, e2]
  field_simp

/-! ### The static response as symmetric part plus current -/

/-- For a linear (Ornstein–Uhlenbeck) system with drift `A`, noise covariance `Σ` and stationary
covariance `P` (Lyapunov: `A P + P Aᵀ = Σ`), write `Q = A P − P Aᵀ` for the antisymmetric part, which
is zero iff the dynamics is reversible. Then the static response matrix is `A⁻¹ = 2 P (Σ + Q)⁻¹`:
the reversible value `2 P Σ⁻¹` corrected by the symmetry-breaking current `Q`. -/
theorem response_decomposition {n : Type*} [Fintype n] [DecidableEq n]
    (A P S : Matrix n n ℝ) (hlyap : A * P + P * A.transpose = S)
    (hS : IsUnit (S + (A * P - P * A.transpose)).det) :
    A⁻¹ = (2 : ℝ) • (P * (S + (A * P - P * A.transpose))⁻¹) := by
  apply reversible_inverse A P (S + (A * P - P * A.transpose)) hS
  rw [← hlyap]
  ext i j
  simp [Matrix.add_apply, Matrix.smul_apply]
  ring

end ReductionExamples

/-- Example A at first order in `1/γ`: under the input `u` on the fast variable the corrected slow drift is
`((ε₀ - b u) x - a b x³)(1 + 2 a b x²/γ)`, and its derivative in `u` at `u = 0`, the reduced effect, is the
`ε = 0` effect `-b x` times the same leak factor that corrects the record. -/
theorem exampleA_leaky_effect (ε₀ a b γ x : ℝ) :
    HasDerivAt (fun u : ℝ => ((ε₀ - b * u) * x - a * b * x ^ 3) * (1 + 2 * a * b * x ^ 2 / γ))
      (-(b * x) * (1 + 2 * a * b * x ^ 2 / γ)) 0 := by
  have h0 : HasDerivAt (fun u : ℝ => ε₀ - b * u) (-b) 0 := by
    simpa using ((hasDerivAt_id (0:ℝ)).const_mul b).const_sub ε₀
  have h2 := ((h0.mul_const x).sub_const (a * b * x ^ 3)).mul_const (1 + 2 * a * b * x ^ 2 / γ)
  convert h2 using 1
  ring

#print axioms exampleA_leaky_effect

/-- The `γ`-derivative of the `O(1/γ)` effective drift of Example A with process noise, for any coefficient `c`
of the noise-induced linear term (`c = 3 a b σ²` in the text; the earlier lemma `drift_deriv_gamma` had `c = a b σ²`). -/
theorem drift_deriv_gamma_noise (a b c x x0 γ : ℝ) (hγ : γ ≠ 0) :
    HasDerivAt (fun γ : ℝ => x0 * (1 + 2 * a * b * x ^ 2 / γ) + c * x / γ)
      (-(2 * a * b * x ^ 2 * x0 + c * x) / γ ^ 2) γ := by
  have h1 : HasDerivAt (fun γ : ℝ => x0 + (2 * a * b * x ^ 2 * x0 + c * x) * γ⁻¹)
      ((2 * a * b * x ^ 2 * x0 + c * x) * (-(γ ^ 2)⁻¹)) γ :=
    ((hasDerivAt_inv hγ).const_mul _).const_add x0
  convert h1 using 1
  · funext γ'
    by_cases hγ' : γ' = 0
    · subst hγ'; simp
    · field_simp; ring
  · field_simp

#print axioms drift_deriv_gamma_noise

/-- The static response of the linear class split into the reversible value and a current term: with
`A P + P Aᵀ = S` and `Q = A P − P Aᵀ`, `A⁻¹ = 2 P S⁻¹ − A⁻¹ Q S⁻¹` whenever `A` and `S` are invertible. -/
theorem response_split {n : Type*} [Fintype n] [DecidableEq n]
    (A P S : Matrix n n ℝ) (hA : IsUnit A.det) (hS : IsUnit S.det)
    (hlyap : A * P + P * A.transpose = S) :
    A⁻¹ = (2 : ℝ) • (P * S⁻¹) - A⁻¹ * (A * P - P * A.transpose) * S⁻¹ := by
  have hQ : (2 : ℝ) • (A * P) - (A * P - P * A.transpose) = S := by
    rw [← hlyap, two_smul]; abel
  have h2 : A⁻¹ * (A * P) = P := by
    rw [← Matrix.mul_assoc, Matrix.nonsing_inv_mul A hA, Matrix.one_mul]
  have h3 : (2 : ℝ) • P - A⁻¹ * (A * P - P * A.transpose) = A⁻¹ * S := by
    rw [← hQ, mul_sub A⁻¹ ((2 : ℝ) • (A * P)), Matrix.mul_smul, h2]
  calc A⁻¹ = A⁻¹ * S * S⁻¹ := by rw [Matrix.mul_assoc, Matrix.mul_nonsing_inv S hS, Matrix.mul_one]
    _ = ((2 : ℝ) • P - A⁻¹ * (A * P - P * A.transpose)) * S⁻¹ := by rw [h3]
    _ = (2 : ℝ) • (P * S⁻¹) - A⁻¹ * (A * P - P * A.transpose) * S⁻¹ := by
        rw [sub_mul, Matrix.smul_mul]

/-- The local mean velocity of the linear diffusion `dX = −A X dt + B dW` (`S = B Bᵀ`, stationary covariance `P`)
is `ν_s(x) = −(A − ½ S P⁻¹) x`, and the matrix in it is the current: `A − ½ S P⁻¹ = ½ Q P⁻¹`, `Q = A P − P Aᵀ`. -/
theorem local_mean_velocity_matrix {n : Type*} [Fintype n] [DecidableEq n]
    (A P S : Matrix n n ℝ) (hP : IsUnit P.det) (hlyap : A * P + P * A.transpose = S) :
    A - (1 / 2 : ℝ) • (S * P⁻¹) = (1 / 2 : ℝ) • ((A * P - P * A.transpose) * P⁻¹) := by
  have hAPP : A * P * P⁻¹ = A := by
    rw [Matrix.mul_assoc, Matrix.mul_nonsing_inv P hP, Matrix.mul_one]
  rw [← hlyap, add_mul, sub_mul, hAPP]
  ext i j
  simp only [Matrix.sub_apply, Matrix.smul_apply, Matrix.add_apply, smul_eq_mul]
  ring

#print axioms response_split
#print axioms local_mean_velocity_matrix

/-- Integrated autocovariance of a linear diffusion `dz = −Γ z dt + B dW` with stationary covariance `P`
(`Γ P + P Γᵀ = S`): `∫₀^∞ C(t) dt = Γ⁻¹ P`, whose symmetric part is half the zero-frequency spectral density,
`Γ⁻¹ P + (Γ⁻¹ P)ᵀ = Γ⁻¹ S Γ⁻ᵀ`. Hence `τ₁ = (Γ⁻¹P)₁₁ = S₁₁(0)/2`. -/
theorem integrated_autocov_symmetric_part {n : Type*} [Fintype n] [DecidableEq n]
    (G P S : Matrix n n ℝ) (hG : IsUnit G.det) (hP : P.transpose = P)
    (hlyap : G * P + P * G.transpose = S) :
    G⁻¹ * P + (G⁻¹ * P).transpose = G⁻¹ * S * G⁻¹.transpose := by
  have hGt : IsUnit G.transpose.det := by rwa [Matrix.det_transpose]
  have h1 : G⁻¹ * (G * P) * G⁻¹.transpose = P * G⁻¹.transpose := by
    rw [← Matrix.mul_assoc, Matrix.nonsing_inv_mul G hG, Matrix.one_mul]
  have h2 : G⁻¹ * (P * G.transpose) * G⁻¹.transpose = G⁻¹ * P := by
    rw [Matrix.mul_assoc, Matrix.mul_assoc P, Matrix.transpose_nonsing_inv,
      Matrix.mul_nonsing_inv G.transpose hGt, Matrix.mul_one]
  rw [← hlyap, Matrix.mul_add, Matrix.add_mul, h1, h2, Matrix.transpose_mul, hP, add_comm]

/-- C as a fast sector: at the base point `(α,δ,κ,κ',σ₁²,σ₂²) = (1,2,1,1/2,1,1)` and its α–δ mate
`(3/2,3/2,1,3/4,1,11/4)` the zero-frequency density `S₁₁(0) = (δ²σ₁² + κ²σ₂²)/(αδ − κκ')²` coincides (`20/9`), while
its δ-derivative `[2δσ₁²(αδ−κκ') − 2α(δ²σ₁² + κ²σ₂²)]/(αδ−κκ')³` does not (`−32/27` against `−28/9`). -/
theorem exampleC_fast_sector_points :
    ((2:ℚ)^2 * 1 + 1^2 * 1) / (1 * 2 - 1 * (1/2))^2 = ((3/2:ℚ)^2 * 1 + 1^2 * (11/4)) / ((3/2) * (3/2) - 1 * (3/4))^2 ∧
    (2 * 2 * 1 * (1 * 2 - 1 * (1/2)) - 2 * 1 * ((2:ℚ)^2 * 1 + 1^2 * 1)) / (1 * 2 - 1 * (1/2))^3 ≠
    (2 * (3/2) * 1 * ((3/2) * (3/2) - 1 * (3/4)) - 2 * (3/2) * ((3/2:ℚ)^2 * 1 + 1^2 * (11/4))) / ((3/2) * (3/2) - 1 * (3/4))^3 := by
  constructor <;> norm_num

#print axioms integrated_autocov_symmetric_part
#print axioms exampleC_fast_sector_points

/-- The split without inverting the noise covariance: `2 P = A⁻¹ S + A⁻¹ Q` whenever `A P + P Aᵀ = S` and `A` is
invertible. Entry `(1,1)` with `S e₁ = σ₁² e₁` reads `2 P₁₁ = σ₁² (A⁻¹)₁₁ + (A⁻¹ Q)₁₁`, valid with no hidden noise. -/
theorem response_split_noinv {n : Type*} [Fintype n] [DecidableEq n]
    (A P S : Matrix n n ℝ) (hA : IsUnit A.det) (hlyap : A * P + P * A.transpose = S) :
    (2 : ℝ) • P = A⁻¹ * S + A⁻¹ * (A * P - P * A.transpose) := by
  have h2 : A⁻¹ * (A * P) = P := by
    rw [← Matrix.mul_assoc, Matrix.nonsing_inv_mul A hA, Matrix.one_mul]
  have h3 : (A * P + P * A.transpose) + (A * P - P * A.transpose) = (2 : ℝ) • (A * P) := by
    rw [two_smul]; abel
  rw [← hlyap, ← mul_add, h3, Matrix.mul_smul, h2]

#print axioms response_split_noinv

/-- Example A: rescaling the hidden coordinate, `ỹ = l y`, carries `(a, b)` to `(l a, b / l)` and leaves both equations,
hence every `x`-trajectory, unchanged; the input `u` on `y` is carried to `l u`. -/
theorem exampleA_hidden_rescaling (ε₀ a b γ x y u l : ℝ) (hl : l ≠ 0) :
    ε₀ * x - b * x * y = ε₀ * x - (b / l) * x * (l * y) ∧
    l * (-(γ * (y - a * x ^ 2 - u))) = -(γ * (l * y - (l * a) * x ^ 2 - l * u)) := by
  constructor
  · first | (field_simp; ring) | field_simp
  · ring

/-- Example B: `ỹ = l y` carries `(c, k)` to `(l c, k / l²)` and leaves the free energy unchanged, and the covariant
field coefficient `c √(β k)` is invariant under it. -/
theorem exampleB_hidden_rescaling (k c m y l β : ℝ) (hl : 0 < l) :
    k / 2 * (y - c * m ^ 2) ^ 2 = (k / l ^ 2) / 2 * (l * y - (l * c) * m ^ 2) ^ 2 ∧
    (l * c) * Real.sqrt (β * (k / l ^ 2)) = c * Real.sqrt (β * k) := by
  constructor
  · first | (field_simp; ring) | field_simp
  · have h1 : β * (k / l ^ 2) = (β * k) / l ^ 2 := by ring
    rw [h1, Real.sqrt_div' _ (sq_nonneg l), Real.sqrt_sq hl.le]
    first | (field_simp; ring) | field_simp

#print axioms exampleA_hidden_rescaling
#print axioms exampleB_hidden_rescaling
