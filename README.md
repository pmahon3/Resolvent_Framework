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

The Stone space constructed in Paper I as a technical device for measure
extension reappears in Paper III as the object being reconstructed.
The programme begins and ends with the same compact space.

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

**LaTeX:** `papers/paper_i/` (13 pages, arXiv-ready)
**Lean:** `QuerySystem.lean` ✅, `DiscriminabilityFoundations.lean` ✅,
`StoneDualityExtension.lean` ✅, `TopologicalQuerySystem.lean` ✅,
`ProkhorovExtension.lean` ✅

### Paper II — Dynamics from Probability

Given a probability measure, the temporal structure of prediction is uniquely
determined. The predictive kernel, minimal predictive state map Q\*, and
semigroup {K_t} are derived from temporal coherence, not assumed.
Koopman–Perron duality connects operator-on-functions and measure-on-states.

**LaTeX:** `papers/paper_ii/` (8 pages, arXiv-ready)
**Lean:** `PredictiveState.lean` ✅, `PredictiveOperators.lean` ✅ (0 sorrys)

### Paper III — Reconstruction from Observation

Under a cyclic vector condition on the Koopman operator, the delay map
Φ_h : X → ℝ^ℕ is a measure-theoretic embedding and the Stone space of the
observable algebra is isomorphic to the state space. Generalises Takens's
theorem: measurability replaces smoothness, algebraic density replaces the
dimension count.

**LaTeX:** `papers/paper_iii/` (6 pages, revised)
**Lean:** `ReconstructionTheorem.lean` ✅ (2 Mathlib-gap sorrys),
`DelayEmbedding.lean` ✅

## Repository structure

```
Resolvent_Framework/
├── README.md
├── papers/
│   ├── paper_i/           ← Paper I LaTeX (arXiv-ready)
│   ├── paper_ii/          ← Paper II LaTeX (arXiv-ready)
│   └── paper_iii/         ← Paper III LaTeX (revised)
├── formalization/
│   └── QuerySystem/       ← Lean 4 / Mathlib formalization
│       └── QuerySystem/
│           ├── QuerySystem.lean
│           ├── DiscriminabilityFoundations.lean
│           ├── StoneDualityExtension.lean
│           ├── PredictiveState.lean
│           ├── PredictiveOperators.lean
│           ├── DelayEmbedding.lean
│           ├── ReconstructionTheorem.lean
│           ├── TopologicalQuerySystem.lean
│           └── ProkhorovExtension.lean
├── notes/
│   ├── program_overview.md          ← canonical task list and status
│   ├── arxiv_prep.md                ← arXiv submission checklist
│   ├── lean_flight_log.md           ← running Lean error/fix log
│   ├── reconstruction_lean_flight_plan.md
│   └── conceptual_sketches/
└── archive/               ← superseded drafts and notes
```

## Lean formalization status

See `formalization/QuerySystem/README.md` for the full sorry inventory.
All main theorems in Papers I and II carry zero sorrys. All remaining sorrys
are documented Mathlib-gap markers, not proof-search failures.

## Current status

See `notes/program_overview.md` for the canonical task list and priorities.

- **Papers I and II**: arXiv-ready (MSC classifications, keywords, citations complete).
- **Paper III**: first draft revised; 2 Mathlib-gap sorrys in `ReconstructionTheorem.lean`.
- **Next action**: arXiv submission of Papers I and II.
