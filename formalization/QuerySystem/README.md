# QuerySystem — Lean 4 Formalization

Lean 4 / Mathlib formalization of Paper I: "When Does Observational
Coherence Determine Probability?"

## Active files (Paper I + companion note)

| File | Content | Status |
|------|---------|--------|
| `QuerySystem.lean` | Query system, cylinder algebra, Carathéodory extension | ✅ 0 sorrys |
| `DiscriminabilityFoundations.lean` | CE characterization, counterexample, independence | ✅ 0 sorrys |
| `StoneDualityExtension.lean` | Stone space, stone_measure_exists, route coincidence | 1 Mathlib-gap sorry |
| `UltrafilterCharge.lean` | Non-σ-additivity of ultrafilter charges | ✅ 0 sorrys |

## Retained files (classical results, not load-bearing)

Papers II and III were withdrawn after novelty audit (2026-05-11).
These Lean files remain as correct proofs of classical results:

| File | Content | Status |
|------|---------|--------|
| `PredictiveState.lean` | Rokhlin disintegration, sufficiency | ✅ 0 sorrys |
| `PredictiveOperators.lean` | Markov semigroup, Koopman-Perron | ✅ 0 sorrys |
| `ReconstructionTheorem.lean` | Density bridge, generating partitions | ✅ 0 sorrys |
| `DelayEmbedding.lean` | Delay query systems | ✅ 0 sorrys |

## Key results

- `observational_determination`: uniqueness of P via π-λ theorem
- `observational_extension`: compatible σ-additive marginals → unique global P
- `sp1_iff`: CE ↔ σ-additive extensibility at every level
- `ce_independence`: SUD + NCC does not imply CE (finite-cofinite counterexample)
- `stone_measure_exists`: Stone-space probability measure from finitely-additive charges (0 sorry)
- `stone_agrees_with_caratheodory`: both routes produce the same measure

## Intentional sorry

| Sorry | Location | Reason |
|-------|----------|--------|
| `stone_observational_extension` | `StoneDualityExtension.lean` | Yosida–Hewitt decomposition not in Mathlib |

## Build

```bash
lake build
```

Requires Lean 4 and Mathlib.
