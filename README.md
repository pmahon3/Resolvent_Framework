# Observable Dynamics Program

This repository develops a program for deriving dynamical structure
directly from observable experiments.

Rather than postulating a latent state space, the framework begins
with what an observer can distinguish — a structured family of queries
— and studies the probabilistic, predictive, and operator structures
that emerge from their compatibility relations.

## Program summary

The program proceeds in five papers:

**Paper −1** establishes the foundation: what an observer is, what
their coherent discriminative commitments force, and why the
σ-algebra structure arises necessarily from primitive distinguishability.

**Paper 0** assembles the per-level σ-additive extensions from Paper −1
into a unique global probability measure on the canonical realization
space, via a realizability condition on the projective limit.

**Paper 1** shows how a minimal predictive state space emerges from
prediction on that probability space, and develops the operator theory
of predictive dynamics.

**Paper 2** establishes the semigroup structure of predictive evolution
and its Koopman-Perron duality.

**Paper 3** develops the delay query system as a concrete computational
instantiation of the framework, connecting to DMD and Koopman spectral
methods.

The architectural spine of the program is:

```
discriminability  →  canonical (Ω, P)  →  predictive state Q*  →  semigroup {K_t}  →  computation
```

Conceptually:

```
distinctions  →  probability  →  predictive state  →  operator dynamics  →  computation
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
│   ├── discriminability_foundations/        ← Paper −1
│   ├── observational_foundations/           ← Paper 0
│   ├── predictive_operator_theory/          ← Paper 1
│   ├── predictive_experiments/              ← Paper 2
│   └── observational_probability/           ← Paper 3
│
├── thesis/
│   └── thesis.tex                           ← master document (all five papers)
│
├── formalization/
│   └── QuerySystem/   ← Lean 4 formalization
│
└── notes/
    ├── prokhorov_extension/                 ← topological extension (companion, not trunk)
    ├── exploratory/
    ├── conceptual_sketches/
    └── archived_artifacts/
```

## Papers

### Paper −1 — Discriminability and the Origin of the σ-Algebra
*From Primitive Distinguishability to Measurable Structure*

Establishes that index-layer coherence conditions (sequential upper-directedness,
compatibility) cannot force σ-additivity, and proves the SP1 theorem: a family of
finitely-additive contents extends to σ-additive measures at every level if and
only if it is collectively exhaustive — the exact valuation-layer characterisation
of systems modelling coherent worlds.

> **discriminability → coherence → measurable structure**

### Paper 0 — Observational Foundations of Probability
*From Collective Exhaustion to Canonical Probability*

Assembles the per-level σ-additive extensions (from Paper −1 via
collective exhaustion) into a unique global probability measure on the
canonical realization space `(Ω, σ(Q), P)`, using a realizability
condition on the projective limit. No topology required.

> **collective exhaustion + realizability → canonical probability**

### Paper 1 — Predictive State and Operator Factorization
*From Canonical Probability to Predictive State Dynamics*

Shows that prediction induces an equivalence on observable states,
yielding a minimal predictive query `Q*` and a Markov operator
`K_{Q*}` representing predictive dynamics.

> **probability → prediction → operators**

### Paper 2 — Observable Operator Semigroups and Koopman Duality
*From Predictive State Dynamics to Operator Semigroups*

Shows that predictive evolution on the minimal predictive state space
is governed by a semigroup of Markov operators `{K_t}` and its
infinitesimal generator `A`, satisfying the predictive Kolmogorov
equation.

> **predictive state → operator semigroup → generator**

### Paper 3 — Delay Queries and Computational Instantiation
*From Abstract Framework to Concrete Computation*

Develops the delay query system as a concrete computational realization
of the abstract framework, connecting to DMD and Koopman spectral methods.

> **operator dynamics → computation**

## Lean formalization

The `formalization/QuerySystem` directory contains the core Lean 4
development for query systems, refinement maps, and the projective
construction of the canonical experiment.

## Thesis

`thesis/thesis.tex` assembles all six papers into a single document,
with interstitial chapters explaining the transitions between papers.
Title: *On the Formalities of Discriminability and Probability with Application to Dynamical Systems*.
