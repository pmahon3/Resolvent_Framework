# QuerySystem — Lean 4 Formalization

Lean 4 / Mathlib formalization of the **Observable Dynamics Program**:
three papers showing that probability, dynamics, and reconstruction follow
from coherent structured observation.

## File overview

| File | Paper | Content | Status |
|------|-------|---------|--------|
| `QuerySystem.lean` | Paper I (Carathéodory route) | Query system, cylinder algebra, observational extension | ✅ 0 sorrys |
| `DiscriminabilityFoundations.lean` | Paper I (CE theory) | CE theorem, irreducibility, Łoś argument | ✅ 0 sorrys on main results; 3 Mathlib-gap sorrys |
| `StoneDualityExtension.lean` | Paper I (Stone route) | Stone space, bonding maps, route coincidence | ✅ 0 sorrys on proved tasks; 2 intentional Mathlib-gap sorrys |
| `TopologicalQuerySystem.lean` | Paper I (Prokhorov route) | Topological query systems, inverse limit | ✅ 0 sorrys on new theorems |
| `ProkhorovExtension.lean` | Paper I (Prokhorov route) | Prokhorov extension main theorem | ✅ 1 Mathlib-blocked sorry |
| `PredictiveState.lean` | Paper II | Predictive kernel, minimal predictive state map, factorization | ✅ 0 sorrys |
| `PredictiveOperators.lean` | Paper II | Semigroup, Koopman–Perron duality, deterministic specialization | ✅ 0 sorrys |
| `DelayEmbedding.lean` | Paper III | Delay query system structure, bounded-subsystem extension | ✅ 0 sorrys on proved results; 1 deliberate scope note |

## Key results

### Paper I — Probability from Observation

- `observational_determination`: uniqueness of P via π-λ theorem
- `observational_extension`: compatible σ-additive marginals + SUD + EvalSurjective → unique global P
- `sp1_iff`: CE ↔ σ-additive extensibility at every level
- `ce_independence`: SUD + NCC does not imply CE (finite-cofinite counterexample)
- `stone_agrees_with_caratheodory`: Stone and Carathéodory routes produce the same measure

### Paper II — Dynamics from Probability

- `predictive_factorization`: E[g(F) | σ(Q)] factors through the minimal predictive state map Q*
- `predictive_sufficiency`: corollary — E[g(F)|Q] = E[g(F)|Q*]
- `semigroup_property`: K_{t+s} = K_t ∘ K_s (Chapman–Kolmogorov)
- `koopman_perron_duality`: ∫ (K_t g) dμ = ∫ g d(P_t* μ)
- `deterministic_specialization`: Dirac kernels recover classical Koopman operators
- `deterministic_semigroup`: flow law φ_{t+s} = φ_t ∘ φ_s

### Paper III — Reconstruction from Observation (in progress)

- `delayQuerySystem.upperDirected`: any two delay queries have a common refinement
- `delayQuerySystem.evalSurjective`: every outcome is realized by a coherent stream
- `delayQuerySystem.compatibleMarginals`: any measure on sensor streams induces compatible marginals
- `observational_extension_fixedLag`: extension theorem for bounded fixed-lag subsystems
- Cyclic vector theorem: **not yet formalized** (open mathematics)

## Intentional sorrys

All remaining sorrys are Mathlib-gap markers or deliberate scope notes:

| Sorry | Location | Reason |
|-------|----------|--------|
| `stone_measure_exists` | `StoneDualityExtension.lean` | Clopen-algebra charge → regular Borel measure (Halmos §53–54; not in Mathlib) |
| `stone_observational_extension` | `StoneDualityExtension.lean` | Choksi's theorem + Yosida–Hewitt (not in Mathlib) |
| `stoneEval_continuous`, `stoneOutcomeMap_continuous` | `StoneDualityExtension.lean` | Technical: `Ultrafilter.map f = Ultrafilter.extend (pure ∘ f)`; not load-bearing |
| `IsFinitarilyExpressible` | `DiscriminabilityFoundations.lean` | Ultraproduct construction for QuerySystem not in Mathlib |
| `evalSurjective_of_upperDirected_refinementMaps_surjective` | `DiscriminabilityFoundations.lean` | Abstract inverse limit requires Tychonoff; concrete systems verified directly |
| `prokhorov_extension_polish` | `ProkhorovExtension.lean` | `PerfectMeasure` and Musiał's theorem not in Mathlib |
| `delayQuerySystem.seqUpperDirected` | `DelayEmbedding.lean` | Deliberate scope note: full delay system is NOT SUD (documented counterexample); extension is correctly scoped to bounded subsystems |

## Build

```bash
lake build
```

## Mathematical framework

A **query system** consists of a preordered index set ι, a family of measurable
spaces (outcome spaces) indexed by ι, evaluation maps from a sample space Ω to
each outcome space, and surjective refinement maps between outcome spaces —
all satisfying a coherence condition. The **observable σ-algebra** is generated
by the cylinder sets. A **compatible family of charges** on the cylinder algebras
extends to a unique global probability measure if and only if it is **collectively
exhaustive** (CE).
