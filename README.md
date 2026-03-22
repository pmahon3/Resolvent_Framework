# Observable Dynamics Program

This repository develops a program for deriving dynamical structure
directly from observable experiments.

Rather than postulating a latent state space, the framework begins
with what an observer can distinguish — a structured family of queries
— and studies the probabilistic, predictive, and operator structures
that emerge from their compatibility relations.

## Program summary

The program proceeds in six papers:

**Paper −1** establishes the foundation: what an observer is, what
their coherent discriminative commitments force, and why the
σ-algebra structure arises necessarily from primitive distinguishability.

**Paper 0** derives σ-additive probability from finitely-additive
observable laws via the Prokhorov and Musiał extension theorems.

**Paper 1** establishes a canonical probabilistic representation of
compatible observable experiments.

**Paper 2** shows how a minimal predictive state space emerges from
prediction on that representation.

**Paper 3** develops the operator theory of predictive dynamics,
showing that predictive evolution is governed by a semigroup and its
infinitesimal generator.

**Paper 4** develops the delay query system as a concrete computational
instantiation of the framework.

The architectural spine of the program is:

```
discriminability  →  observable laws  →  canonical (Ω, P)  →  predictive state Q*  →  semigroup {K_t}  →  generator A
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
│   ├── prokhorov_extension/                 ← Paper 0
│   ├── observational_foundations/           ← Paper 1
│   ├── predictive_operator_theory/          ← Paper 2
│   ├── predictive_experiments/              ← Paper 3
│   └── observational_probability/           ← Paper 4
│
├── thesis/
│   └── thesis.tex                           ← master document (all six papers)
│
├── formalization/
│   └── QuerySystem/   ← Lean 4 formalization
│
└── notes/
    ├── exploratory/
    ├── conceptual_sketches/
    └── archived_artifacts/
```

## Papers

### Paper −1 — Discriminability and the Origin of the σ-Algebra
*From Primitive Distinguishability to Measurable Structure*

Derives the σ-algebra from a Boolean algebra of observable distinctions
and a finitely-additive valuation, showing that continuity at ∅ is the
minimal coherence condition bridging finitary commitments and countable
closure.

> **discriminability → measurable structure**

### Paper 0 — Finitely Additive Observable Laws and the Prokhorov Extension
*From Observable Laws to σ-Additive Probability*

Shows that compatible finitely-additive observable laws extend to a
σ-additive probability measure on the canonical experiment space, via
Prokhorov (compact) and Musiał (standard Borel) extension theorems.

> **observable laws → σ-additive probability**

### Paper 1 — Observational Foundations of Probability
*From Observable Experiments to Canonical Probability*

Proves that compatible families of observable laws admit a canonical
probabilistic representation `(Ω, σ(Q), P)` whose evaluation marginals
recover the observable laws.

> **observables → probability**

### Paper 2 — Predictive State and Operator Factorization
*From Canonical Probability to Predictive State Dynamics*

Shows that prediction induces an equivalence on observable states,
yielding a minimal predictive query `Q*` and a Markov operator
`K_{Q*}` representing predictive dynamics.

> **probability → prediction → operators**

### Paper 3 — Observable Operator Semigroups and Koopman Duality
*From Predictive State Dynamics to Operator Semigroups*

Shows that predictive evolution on the minimal predictive state space
is governed by a semigroup of Markov operators `{K_t}` and its
infinitesimal generator `A`, satisfying the predictive Kolmogorov
equation.

> **predictive state → operator semigroup → generator**

### Paper 4 — Delay Queries and Computational Instantiation
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
