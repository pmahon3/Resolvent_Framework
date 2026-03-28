# QuerySystem — Lean 4 Formalization

Lean 4 / Mathlib formalization of the **Discriminative Foundations for Probability and Dynamics** program.

The program derives probabilistic and dynamical structure from the primitive notion of
discriminability — what an observer can distinguish — rather than assuming a probability
space as input. This directory contains the formal proofs for Papers −1 through 3.

## File overview

| File | Paper | Status |
|------|-------|--------|
| `DiscriminabilityFoundations.lean` | Paper −1 | Zero sorrys on all main theorems |
| `QuerySystem.lean` | Paper 0 | Zero sorrys |
| `DelayEmbedding.lean` | Paper 1 (delay subsystems) | Zero sorrys on fixed-lag subsystem |
| `PredictiveState.lean` | Paper 1 | Zero sorrys |
| `PredictiveOperators.lean` | Paper 2 | Zero sorrys |
| `TopologicalQuerySystem.lean` | SP3 companion | Zero sorrys on new theorems |
| `ProkhorovExtension.lean` | Paper 3 | One Mathlib-blocked sorry |

## Key results

### Paper −1 — Discriminability and the Origin of the σ-Algebra

- `sp1_iff`: a family of finitely-additive contents extends to σ-additive measures at every
  level if and only if it is **collectively exhaustive** (CE).
- `observational_extension_of_collective_exhaustion`: CE → unique global P on Ω.
- `ce_independence`: SUD + NCC does not imply CE (zero sorrys).
- `ce_irreducibility`: no finitarily expressible condition implies CE
  (one infrastructure sorry — ultraproduct construction not in Mathlib).

### Paper 0 — Observational Foundations of Probability

- `observational_extension`: σ-additive compatible marginals + SequentiallyUpperDirected
  + EvalSurjective → unique global P on Ω.
- `observational_determination`: uniqueness via π-system + monotone class.

### Paper 1 — Predictive State

- `predictive_factorization`: conditional law of F factors through Q*.
- `predictive_sufficiency`: Q is predictively sufficient iff F ⊥ Q' | Q for all Q'.

### Paper 2 — Predictive Operators

- `semigroup_property`: K_{t+s} = K_t ∘ K_s (discrete time).
- `koopman_perron_duality`: ∫ (K_t g) dμ = ∫ g d(P_t* μ).

### Paper 3 — Prokhorov Extension (SP2)

- `prokhorov_extension`: finitely-additive compatible family + SPUT → σ-additive global P.
- One sorry: `prokhorov_extension_polish` (Corollary for standard Borel spaces),
  blocked on `PerfectMeasure` and Musiał's theorem being absent from Mathlib 4.

## Intentional sorrys

All remaining sorrys are infrastructure-blocked, not proof-search failures:

| Sorry | Reason |
|-------|--------|
| `IsFinitarilyExpressible` | Ultraproduct construction for QuerySystem not in Mathlib |
| `ce_irreducibility` | Depends on `IsFinitarilyExpressible` |
| `prokhorov_extension_polish` | `PerfectMeasure` and Musiał's theorem not in Mathlib |
| `evalSurjective_of_upperDirected_refinementMaps_surjective` | Abstract inverse limit requires Tychonoff; concrete systems verified directly |
| `delayQuerySystem.seqUpperDirected` | Full delay system is genuinely NOT SUD (documented counterexample) |

## Build

```bash
lake build
```

## Mathematical framework

A **query system** `(ι, Q)` consists of a preordered index set `ι` and a family of
measurable spaces `Q i` (queries) with refinement maps `π : Q j → Q i` for `i ≤ j`.
The **realization space** `Ω ⊆ ∏ i, Q i` is the projective limit — the set of coherent
families of outcomes. Probability structure is assembled from compatible marginals on
the query outcomes, without assuming a latent state space.
