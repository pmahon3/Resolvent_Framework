# Observable Dynamics Program

This repository develops a program for deriving dynamical structure
directly from observable experiments.

Rather than postulating a latent state space, the framework begins
with a system of admissible observational queries and studies the
probabilistic, predictive, and operator structures that emerge from
their compatibility relations.

## Program summary

**Paper 1** establishes a canonical probabilistic representation of
compatible observable experiments.

**Paper 2** shows how a minimal predictive state space emerges from
prediction on that representation.

**Paper 3** develops the operator theory of predictive dynamics,
showing that predictive evolution is governed by a semigroup and its
infinitesimal generator.

A **Lean formalization** verifies the structural components of the
observational framework.

The architectural spine of the program is:

```
observable queries  →  canonical experiment (Ω, P)  →  predictive state Q*  →  semigroup {K_t}  →  generator A
```

Conceptually:

```
observations  →  probability  →  predictive state  →  operator dynamics
```

## Repository structure

```
Resolvent_Framework/
│
├── README.md
│
├── program/
│   └── observable_dynamics_program.tex      ← research program overview
│
├── papers/
│   ├── observational_foundations/           ← Paper 1
│   ├── predictive_experiments/              ← Paper 2
│   └── predictive_operator_theory/          ← Paper 3
│
├── formalization/
│   └── QuerySystem/   ← Lean formalization, project config, and working notes
│
└── notes/
    ├── exploratory/
    ├── conceptual_sketches/
    └── archived_artifacts/
```

## Papers

### Paper 1 — Observational Foundations of Probability
*From Observable Experiments to Canonical Probability*

Proves that compatible families of observable laws admit a canonical
probabilistic representation `(Ω, σ(Q), P)` whose evaluation marginals
recover the observable laws.

> **observables → probability**

### Paper 2 — Predictive Experiments and Observable Operators
*From Canonical Probability to Predictive State Dynamics*

Shows that prediction induces an equivalence on observable states,
yielding a minimal predictive query `Q*` and a Markov operator
`K_{Q*}` representing predictive dynamics.

> **probability → prediction → operators**

### Paper 3 — Predictive Operator Theory
*From Predictive State Dynamics to Operator Semigroups*

Shows that predictive evolution on the minimal predictive state space
is governed by a semigroup of Markov operators `{K_t}` and its
infinitesimal generator `A`, satisfying the predictive Kolmogorov
equation.

> **predictive state → operator semigroup → generator**

## Lean formalization

The `formalization/QuerySystem` directory contains the core Lean
development for query systems, refinement maps, and the projective
construction of the canonical experiment, along with project
configuration and working notes.
