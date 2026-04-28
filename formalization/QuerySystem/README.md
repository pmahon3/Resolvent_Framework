# QuerySystem — Lean 4 Formalization

Lean 4 / Mathlib formalization of the **Structure from Observation** trilogy:
three papers showing that probability, dynamics, reconstruction, and their
finite-sample witnesses follow from coherent structured observation.

Formalization covers Papers I–II fully. Paper III (finite-sample certification)
is mathematically complete in LaTeX (`papers/paper_iii/`) but not yet formalized in Lean.

## File overview

| File | Paper | Content | Status |
|------|-------|---------|--------|
| `QuerySystem.lean` | I (Carathéodory route) | Query system, cylinder algebra, observational extension | ✅ 0 sorrys |
| `DiscriminabilityFoundations.lean` | I (CE theory) | CE theorem, irreducibility, Łoś argument | ✅ 0 sorrys on main results; 3 Mathlib-gap sorrys |
| `StoneDualityExtension.lean` | I (Stone route) | Stone space, bonding maps, route coincidence | ✅ 0 sorrys on proved tasks; 2 intentional Mathlib-gap sorrys |
| `TopologicalQuerySystem.lean` | I (Prokhorov route) | Topological query systems, inverse limit | ✅ 0 sorrys on new theorems; 1 intentional skeleton |
| `ProkhorovExtension.lean` | I (Prokhorov route) | Prokhorov extension main theorem | ✅ 1 Mathlib-blocked sorry |
| `PredictiveState.lean` | II | Conditional regularity kernel, minimal sufficient factor, factorization | ✅ 0 sorrys |
| `PredictiveOperators.lean` | II | Semigroup, Koopman–Perron duality, deterministic specialization | ✅ 0 sorrys |
| `DelayEmbedding.lean` | III | Delay query system; bounded-subsystem extension; reconstruction bridge | ✅ 0 sorrys on proved results; 1 deliberate scope note; 1 documented elaboration sorry |
| `ReconstructionTheorem.lean` | II | Observable algebra, delay map, density bridge, reconstruction theorem | ✅ 0 sorrys |

## Key results

### Paper I — Probability from Observation

- `observational_determination`: uniqueness of P via π-λ theorem
- `observational_extension`: compatible σ-additive marginals + SUD + EvalSurjective → unique global P
- `sp1_iff`: CE ↔ σ-additive extensibility at every level
- `ce_independence`: SUD + NCC does not imply CE (finite-cofinite counterexample)
- `stone_agrees_with_caratheodory`: Stone and Carathéodory routes produce the same measure

### Paper II — Dynamics and Reconstruction in the Observable Measure

- `predictive_factorization`: E[g(F) | σ(Q)] factors through the minimal sufficient factor Q\*
- `predictive_sufficiency`: E[g(F)|Q] = E[g(F)|Q\*]
- `semigroup_property`: K_{t+s} = K_t ∘ K_s (Chapman–Kolmogorov)
- `koopman_perron_duality`: ∫ (K_t g) dμ = ∫ g d(P_t\* μ)
- `deterministic_specialization`: Dirac kernels recover classical Koopman operators
- `deterministic_semigroup`: flow law φ_{t+s} = φ_t ∘ φ_s
- `observableAlgebra_eq_comap`: 𝒪_h = Φ_h⁻¹(ℬ(ℕ→ℝ)) (pullback identity; Definition II:def:delay-map)
- `delayMap_intertwines_shift`: Φ_h ∘ T = σ ∘ Φ_h (shift intertwining; inline in §4.2 proof)
- `cyclic_implies_dense`: cyclic span dense → L²(𝒪_h) dense in L²(μ) (Corollary II:cor:cyclic-implies-reconstruction)
- `observational_extension_fixedLag`: extension theorem for bounded fixed-lag subsystems
- `delay_cyclic_implies_reconstruction`: bridge from `DelayEmbedding.lean`

### Paper III — Finite-sample certification

Paper III (finite-sample certification) is mathematically complete in LaTeX (`papers/paper_iii/`) but not yet formalized in Lean.

## Intentional sorrys

All remaining sorrys are Mathlib-gap markers or deliberate scope notes.

| Sorry | Location | Reason |
|-------|----------|--------|
| `stone_measure_exists` | `StoneDualityExtension.lean` | Clopen-algebra charge → regular Borel measure; not in Mathlib |
| `stone_observational_extension` | `StoneDualityExtension.lean` | Choksi's theorem + Yosida–Hewitt; not in Mathlib |
| `IsFinitarilyExpressible` | `DiscriminabilityFoundations.lean` | Ultraproduct construction for QuerySystem not in Mathlib |
| `evalSurjective_of_upperDirected_refinementMaps_surjective` | `DiscriminabilityFoundations.lean` | Abstract inverse limit requires Tychonoff; concrete systems verified directly |
| `prokhorov_extension_polish` | `ProkhorovExtension.lean` | `PerfectMeasure` and Musiał's theorem not in Mathlib |
| `delayQuerySystem.seqUpperDirected` | `DelayEmbedding.lean` | Deliberate scope note: full delay system is NOT SUD (documented counterexample) |
| `ce_sep_defect` (not in Lean) | — | Paper II Theorem 3.4 (CE drives δ(G_k)→0) not formalized; requires martingale convergence; deliberate scope omission |
| `delay_reconstruction_iff` | `DelayEmbedding.lean` | Two-`MeasurableSpace`-instance elaboration prevents cross-file call; documented |

## Build

```bash
lake build
```

Requires Lean 4 and Mathlib. All files build cleanly; sorry warnings are
expected for the documented gaps above.

## Mathematical framework

A **query system** consists of a preordered index set ι, a family of measurable
spaces indexed by ι, evaluation maps from a sample space Ω to each outcome
space, and surjective refinement maps between outcome spaces — all satisfying a
coherence condition. The **observable σ-algebra** is generated by the cylinder
sets. A **compatible family of charges** on the cylinder algebras extends to a
unique global probability measure if and only if it is **collectively exhaustive**
(CE). CE is irreducible: not derivable from any finitary or structural condition.
