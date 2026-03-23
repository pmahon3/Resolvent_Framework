# Theorem Correspondence: Papers −1, 1–3 ↔ Lean Formalization

Generated: 2026-03-14, updated 2026-03-22 (Paper −1 SP1 resolution added).

---

## Paper −1: Discriminability Foundations (`DiscriminabilityFoundations.lean`)

| Paper statement | Label | Lean name | Status | Notes |
|---|---|---|---|---|
| Finite-cofinite algebra is a SetSemiring | — | `finCofinSets_isSetSemiring` | ✓ | On infinite types |
| fcContent is finitely additive | — | `fcContent` | ✓ | 0 on finite, 1 on cofinite; `sUnion'` proved |
| Counterexample fails σ-additivity | prop:independence | `fcContent_not_sigmaSubadditive` | ✓ | Refutes C1 of tetralemma |
| {s \| MeasurableSet s} is a SetRing | — | `isSetRing_measurableSets` | ✓ | Any measurable space |
| Normalized contents have finite values | — | `NormalizedCompatibleContents.ne_top` | ✓ | Via `addContent_mono` |
| Collective exhaustion → σ-additive extension | thm:sp1 (i→ii) | `sp1_extension` | ✓ | Via `addContent_iUnion_eq_sum_of_tendsto_zero` + Carathéodory |
| σ-additive extension → collective exhaustion | thm:sp1 (ii→i) | `sp1_necessity` | ✓ | Via `tendsto_measure_iInter_atTop` |
| SP1 equivalence | thm:sp1 | `sp1_iff` | ✓ | Full iff |

### Paper −1 assessment
All SP1 theorems formalized. Zero sorrys. `DiscriminabilityFoundations.lean` complete.

One paper-side proof to tighten: Theorem 4.2 (discriminability requires incompleteness)
has an informal gap — key construction step asserted rather than proved. Not formalized
in Lean. Lean gap: `counterexampleNCC` not bundled as `NormalizedCompatibleContents`
due to `finCofinSets ℚ` vs `{s | MeasurableSet s}` type mismatch (non-blocking).

---

## Conventions

- **Status**: `✓ complete` | `◐ partial` | `✗ sorry` | `—  not formalized`
- **Lean name**: fully qualified within the relevant module
- **Notes**: assumptions added or changed in the Lean version relative to the paper

---

## Paper 1: Observational Foundations (`QuerySystem.lean`)

| Paper statement | Label | Lean name | Status | Notes |
|---|---|---|---|---|
| Measurability of evaluation maps | lem:eval-measurable | `QuerySystem.measurable_eval` | ✓ | |
| Cylinder family is a π-system | lem:cyl-pisystem | `QuerySystem.isPiSystem_CylGen` | ✓ | requires `LowerDirected` |
| Observational determination (measure version) | thm:obs-determination | `QuerySystem.observational_determination` | ✓ | |
| Observational determination (probability version) | — | `QuerySystem.observational_determination_prob` | ✓ | |
| Finite observational content (premeasure well-definedness) | thm:finite-content | `QuerySystem.preμ_wellDefined` | ✓ | requires `UpperDirected` + `EvalSurjective` |
| Finite observational content (finite additivity) | — | `QuerySystem.preμ_disjoint_union` | ✓ | requires `UpperDirected` + `EvalSurjective` |
| σ-subadditivity of premeasure | — | `QuerySystem.cylGen_addContent_isSigmaSubadditive` | ✓ | requires `SequentiallyUpperDirected`; reduces to `measure_iUnion_le` for `ν m` |
| Observational extension theorem | thm:top-extension | `QuerySystem.observational_extension` | ✓ | requires `LowerDirected`, `SequentiallyUpperDirected`, `EvalSurjective`; full `∃!` statement |

### Paper 1 assessment
All theorems fully formalized. Zero sorrys.

The observational determination chain (definitions → π-system → uniqueness) and the full
extension chain (premeasure → additive content → σ-subadditivity → Carathéodory → marginal
recovery → uniqueness) are both complete.

**Pass 4 fix**: Switched extension infrastructure from `LowerDirected` (common coarsenings) to
`UpperDirected` (common refinements), fixing `finCyl_eq_cyl_of_upperBound`. Sorry count 4→2.

**Pass 5 (Path A)**: Added `SequentiallyUpperDirected` (`∀ u : ℕ → ι, ∃ k, ∀ n, le (u n) k`)
as the analytic hypothesis for σ-subadditivity. Key proof: compress all cylinders in a sequence
to a common level m, then apply `measure_iUnion_le` for `ν m`. Completed `observational_extension`
as a full `∃!` theorem. Sorry count 2→0.

---

## Paper 2: Predictive Experiments (`PredictiveState.lean`)

| Paper statement | Label | Lean name | Status | Notes |
|---|---|---|---|---|
| Predictive kernel existence | def:predictive-kernel | `predictiveKernel` (def) | ✓ | via `Measure.condKernel` (Rokhlin disintegration); requires `StandardBorelSpace β` |
| Predictive law map | — | `predictiveLawMap` (def) | ✓ | `α → ProbabilityMeasure β` |
| Measurability of predictive law map | — | `measurable_predictiveLawMap` | ✓ | via `Kernel.measurable.subtype_mk` |
| Predictive compatibility (tower) | prop:pred-compat | `predictive_compatibility` | ✓ | statement is a.e. under P.map Q₁ (condKernel is only a.e.-unique); proved via Kernel.comap + eq_condKernel_of_measure_eq_compProd |
| Minimal predictive query | thm:minimal-predictive-query | `minimalPredictiveQuery` (def) | ✓ | `Q_* = φ_Q ∘ Q : Ω → ProbabilityMeasure β` |
| Measurability of minimal predictive query | — | `measurable_minimalPredictiveQuery` | ✓ | composition of measurable maps |
| Predictive equivalence | — | `predictive_equivalence` | ✓ | `Q_*(ω) = Q_*(ω') ↔ Π_Q(Qω) = Π_Q(Qω')` |
| Predictive factorization theorem | thm:predictive-factorization | `predictive_factorization` | ✓ | `E[g(F)\|σ(Q)] =ᵐ (predictiveOp g) ∘ Q_*`; requires `hg_bdd` (bounded g) |
| Predictive sufficiency | — | `predictive_sufficiency` | ✓ | `E[g(F)\|σ(Q)] =ᵐ E[g(F)\|σ(Q_*)]` |
| Canonical predictive operator | cor:canonical-operator | `predictiveOp` (def) + properties | ✓ | `(K_{Q_*} g)(q_*) = ∫ g dq_*` |
| Predictive operator positivity | — | `predictiveOp_positive` | ✓ | |
| Constant preservation | — | `predictiveOp_const_one` | ✓ | |
| Linearity | — | `predictiveOp_add`, `predictiveOp_smul` | ✓ | |
| Contraction | — | `predictiveOp_le_norm` | ✓ | |
| Measurability of predictive operator | — | `measurable_predictiveOp_aux` (private) | ✓ | `Measurable (μ ↦ ∫ g dμ)` via Jordan + Giry σ-algebra |

### Paper 2 assessment
All theorems formalized. Zero sorrys. `predictive_compatibility` is proved via `Kernel.comap`
+ `eq_condKernel_of_measure_eq_compProd`; its statement was corrected from pointwise to a.e.
(since `condKernel` is only a.e.-unique). The formalization uses `StandardBorelSpace β` for
disintegration and adds explicit boundedness hypotheses to factorization and sufficiency.

**Key design choice captured in Lean**: `Q_* : Ω → ProbabilityMeasure β` avoids quotient
constructions; state space = image of `φ_Q` inside the standard Borel space `ProbabilityMeasure β`.

---

## Paper 3: Predictive Operator Theory (`PredictiveOperators.lean`)

| Paper statement | Label | Lean name | Status | Notes |
|---|---|---|---|---|
| Predictive operator family | def:predictive-operator | `PredictiveKernelFamily` (structure) + `predictiveOpFamily` | ✓ | |
| Positivity of K_t | prop:positivity | `predictiveOpFamily_positive` | ✓ | |
| Identity at horizon 0 | — | `predictiveOpFamily_at_zero`, `semigroup_id` | ✓ | uses `integral_dirac'` |
| Semigroup property K_{t+s} = K_t ∘ K_s | thm:semigroup | `semigroup_property` | ✓ | requires `hg_bdd`; via `Kernel.integral_comp` (Bochner Fubini) |
| Constant preservation | — | `semigroup_const_one` | ✓ | |
| Positivity (semigroup form) | — | `semigroup_positive` | ✓ | |
| Koopman–Perron duality | prop:duality | `koopman_perron_duality` | ✓ | requires `hg_bdd`; via `Kernel.integral_comp` + `Measure.comp_eq_comp_const_apply` |
| Deterministic specialization (K_t g = g ∘ φ_t) | prop:deterministic | `deterministic_specialization` | ✓ | |
| Deterministic semigroup law (φ_{t+s} = φ_t ∘ φ_s) | — | `deterministic_semigroup` | ✓ | via `dirac_bind` + `dirac_eq_dirac_iff`; requires `[SeparatesPoints γ]` |

### Not yet formalized in Paper 3
| Paper statement | Label | Status |
|---|---|---|
| Predictive generator (infinitesimal generator) | def:generator, thm:generator-existence | — |
| Predictive Kolmogorov equation | thm:kolmogorov | — |
| Generator in deterministic/stochastic settings | prop:koopman-generator, prop:markov-generator | — |
| Spectral structure (eigenfunctions) | def:eigenfunction | — |

### Paper 3 assessment
The discrete-time operator-theoretic core is fully formalized (zero sorrys).
Continuous-time generator theory and spectral structure are not yet formalized.
Both `semigroup_property` and `koopman_perron_duality` required adding
`hg_bdd : ∃ C, ∀ q, |g q| ≤ C` relative to the paper statements.

---

## Summary table

| File | Theorems complete | Sorrys | Not yet formalized |
|---|---|---|---|
| `DiscriminabilityFoundations.lean` | 8 | **0** | Theorem 4.2 (incompleteness); counterexampleNCC (type gap) |
| `QuerySystem.lean` | ~16 | **0** | — |
| `PredictiveState.lean` | 15 | **0** | — |
| `PredictiveOperators.lean` | 10 | **0** | generator, spectral theory |
| `ProkhorovExtension.lean` | ~10 | **1** | `prokhorov_extension_polish` (Mathlib-blocked) |

---

## Assumptions added in the Lean development

The following hypotheses appear in the Lean statements but are not always explicit in the papers:

| Assumption | Where added | Mathematical role |
|---|---|---|
| `[StandardBorelSpace β]` | Paper 2, all predictive kernel results | Required for Rokhlin disintegration (`condKernel`) |
| `UpperDirected` | Paper 1, premeasure extension | Required for `finCyl_eq_cyl_of_upperBound` (common refinement for compression); derived from `SequentiallyUpperDirected` in `observational_extension` |
| `SequentiallyUpperDirected` | Paper 1, σ-subadditivity | `∀ u : ℕ → ι, ∃ k, ∀ n, le (u n) k`: every sequence has a common refinement; implies `UpperDirected`; the analytic hypothesis for the extension theorem |
| `EvalSurjective` | Paper 1, premeasure well-def + additivity | `∀ i, Surjective (eval i)`: realizability condition not in note.tex |
| `[Nonempty β]` | Paper 2, all predictive kernel results | Required for `condKernel` existence |
| `hg_bdd : ∃ C, ∀ b, \|g b\| ≤ C` | `predictive_factorization`, `predictive_sufficiency`, `semigroup_property`, `koopman_perron_duality` | Required for integrability over Markov/probability kernels |
| `[SeparatesPoints γ]` | `deterministic_semigroup` | Required for injectivity of `Measure.dirac` |
| `[IsFiniteMeasure μ]` | `koopman_perron_duality` | Needed for the dual measure to be well-behaved |

---

## Key Mathlib dependencies

| Mathlib lemma | Used in | Role |
|---|---|---|
| `Measure.condKernel` | `predictiveKernel` | Regular conditional distribution via Rokhlin disintegration |
| `Kernel.measurable` | `measurable_predictiveLawMap` | Kernel measurability as `α → Measure β` |
| `ae_eq_condExp_of_forall_setIntegral_eq` | `predictive_factorization`, `predictive_sufficiency` | Uniqueness of conditional expectation |
| `Measure.setIntegral_condKernel` | `predictive_factorization` | Disintegration set-integral identity |
| `StronglyMeasurable.integral_kernel` | `predictive_factorization` | Measurability of kernel integrals |
| `measurable_lintegral` | `measurable_predictiveOp_aux` | Giry σ-algebra measurability |
| `integral_eq_lintegral_pos_part_sub_lintegral_neg_part` | `measurable_predictiveOp_aux` | Jordan decomposition for Bochner integral |
| `Kernel.integral_comp` | `semigroup_property`, `koopman_perron_duality` | Bochner Fubini for kernel composition |
| `Kernel.comp_apply` | `semigroup_property`, `deterministic_semigroup` | `(η ∘ₖ κ) a = (κ a).bind η` |
| `Measure.comp_eq_comp_const_apply` | `koopman_perron_duality` | `μ.bind κ = (κ ∘ₖ const Unit μ) ()` |
| `Measure.dirac_bind` | `deterministic_semigroup` | `(dirac a).bind f = f a` |
| `Measure.dirac_eq_dirac_iff` | `deterministic_semigroup` | Dirac injectivity under `SeparatesPoints` |
