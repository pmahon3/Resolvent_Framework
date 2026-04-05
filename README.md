# Observable Dynamics Program

This repository develops a three-paper mathematical programme showing that
probability, dynamics, and reconstruction are not assumptions but consequences
of coherent structured observation.

## The argument

```
Structured observations
    → [Paper I]   → probability measure P on (Ω, σ(CylGen))
    → [Paper II]  → dynamics: Koopman operator U_T, semigroup K_t
    → [Paper III] → reconstruction: state space X ≅ St(observable algebra)
```

The Stone space constructed in Paper I as a technical device reappears at
the end of Paper III as the object being reconstructed. The programme begins
and ends with the same compact space, seen from different angles.

## Papers

### Paper I — Probability from Observation

A coherent family of observations determines a unique probability measure on
the observable σ-algebra. Proved by two independent routes:

- **Carathéodory route**: σ-additive compatible marginals extend uniquely via
  Carathéodory on the realization space.
- **Stone route**: finite additivity alone, combined with compactness of the
  Stone space, derives σ-additivity. CE appears as a support condition.

The irreducibility of Collective Exhaustion (CE) — the necessary and sufficient
condition — is established via a finite-cofinite counterexample and Łoś's theorem.

**LaTeX:** `papers/paper_i/` (13 pages) | **Lean:** `QuerySystem.lean`,
`DiscriminabilityFoundations.lean`, `StoneDualityExtension.lean`

### Paper II — Dynamics from Probability

Given a probability measure, the temporal structure of prediction is uniquely
determined. The predictive kernel, minimal predictive state map Q*, and
semigroup {K_t} are derived, not assumed. Koopman–Perron duality connects
operator-on-functions and measure-on-states into a single picture.

**LaTeX:** `papers/paper_ii/` (8 pages) | **Lean:** `PredictiveState.lean`,
`PredictiveOperators.lean`

### Paper III — Reconstruction from Observation (in progress)

Under a cyclic vector condition on the Koopman operator, the Stone space of
the observable algebra is measure-theoretically isomorphic to the state space.
This generalises Takens's theorem: measurability replaces smoothness, and the
cyclic vector condition replaces the dimension count.

**LaTeX:** not started | **Lean:** `DelayEmbedding.lean` (delay query system
structure proved; cyclic vector theorem open)

## Repository structure

```
Resolvent_Framework/
├── README.md
├── papers/
│   ├── paper_i/           ← Paper I LaTeX (paper_i.tex, paper_i_body.tex, references.bib)
│   └── paper_ii/          ← Paper II LaTeX
├── formalization/
│   └── QuerySystem/       ← Lean 4 / Mathlib formalization
│       └── QuerySystem/
│           ├── QuerySystem.lean
│           ├── DiscriminabilityFoundations.lean
│           ├── StoneDualityExtension.lean
│           ├── PredictiveState.lean
│           ├── PredictiveOperators.lean
│           ├── DelayEmbedding.lean
│           ├── TopologicalQuerySystem.lean
│           └── ProkhorovExtension.lean
├── notes/
│   ├── program_overview.md          ← canonical task list and status table
│   ├── stone_duality_lean_flight_plan.md
│   └── conceptual_sketches/
│       └── philosophy/
└── archive/               ← superseded drafts and notes
```

## Lean formalization status

See `formalization/QuerySystem/README.md` for the full sorry inventory.
All main theorems in Papers I and II carry zero sorrys. Remaining sorrys
are intentional Mathlib-gap markers, not proof-search failures.

## Current status

See `notes/program_overview.md` for the canonical task list and priorities.

- **Papers I and II**: revised drafts complete.
- **Paper III**: cyclic vector theorem under development.
