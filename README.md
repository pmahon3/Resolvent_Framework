# Structure from Observation

This repository develops a mathematical programme showing that probability,
dynamics, reconstruction, and their finite-sample signatures are not
assumptions but consequences of coherent structured observation.

## The argument

```
Structured observations
    → [Paper I]     → probability measure P on (Ω, σ(CylGen))
    → [Paper II]  → dynamics: Koopman operator U_T, semigroup K_t
                     + reconstruction: state space X ≅ St(observable algebra)
    → [Paper III] → finite-sample: δ̂ stopping rule, rates, honest bridge
```

The Stone space constructed in Paper I as a technical device for measure
extension reappears in Paper II as the object being reconstructed.
Paper III asks what this reconstruction looks like from finite data,
and answers with three theorems: one for the algebra side, one for the
dynamics side, and one for their conjunction.

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

**LaTeX:** `papers/paper_i/` (12 pages, arXiv-ready)
**Lean:** `QuerySystem.lean` ✅, `DiscriminabilityFoundations.lean` ✅,
`StoneDualityExtension.lean` ✅, `TopologicalQuerySystem.lean` ✅,
`ProkhorovExtension.lean` ✅

### Paper II — Dynamics and Reconstruction in the Observable Measure

Starting from the probability measure of Paper I, shows that dynamics and
reconstruction are already present in the measure — not derived by further
work, but read off.

- **Conditional regularity**: the Rokhlin disintegration forces a Markov
  kernel Π_Q(q,·) = P(F ∈ · | Q = q) from any two observations Q, F.
  This is not a modelling choice. Composing with Q gives the minimal
  sufficient factor Q*, the coarsest reduction carrying full conditional
  information about F. Temporal prediction is the special case; the object
  is neutral on time.
- **Dynamics**: indexing over time, temporal coherence of the conditional
  regularity forces Chapman–Kolmogorov — derived, not assumed. This yields
  a Markov semigroup {K_t} and Koopman–Perron duality. Dirac kernels recover
  the classical Koopman picture.
- **Reconstruction**: specialising Q* to a measure-preserving system yields
  the delay map Φ_h. The reconstruction question is internal: is the factor
  faithful? The answer is a three-way equivalence (O_h = B mod μ ↔ A_h
  L²-dense ↔ Φ_h embedding) via the density bridge lemma. When
  reconstruction holds, the Stone space of Paper I is identified with X.

**LaTeX:** `papers/paper_ii/` (9 pages)
**Lean:** `PredictiveState.lean` ✅, `PredictiveOperators.lean` ✅ (0 sorrys),
`DelayEmbedding.lean` ✅, `ReconstructionTheorem.lean` ✅ (0 sorrys)

### Paper III — Certifying Reconstruction from Finite Data

Given finite data from the system, what can be certified about the structures
Paper II establishes? Two threads converge: the general query certification
framework (Paper I's level of abstraction) meets the dynamical reconstruction
(Paper II), and the meeting point is stronger than either alone — honest
refinement, a design condition in the general setting, is automatic in the
dynamical setting, freeing the rate theorems to exploit mixing and geometry.

- **General level** (§2): the separation defect δ(G) and its U-statistic
  empirical proxy certify CE-failure from data, with no temporal or
  geometric assumptions. A persistent empirical floor is evidence against CE.
- **Algebra Theorem**: the elbow stopping rule L̂* achieves the minimax-optimal
  rate n^{-s/(2s+d)} for Hölder(s) targets without oracle inputs.
- **Dynamics Theorem**: under uniform separation, empirical delay vectors
  certify point separation at rate n^{-β/(2β+d)}.
- **Conjunction Theorem**: for deterministic T, algebra separation and metric
  separation are the same event — identical, not merely correlated. The
  conditional regularity kernel specialises to a Dirac delta; σ(Φ_h^(L)) =
  𝒪_h^(L) is the bridge connecting both witnesses.

**LaTeX:** `papers/paper_iii/` (18 pages)
**Lean:** Not started

## Repository structure

```
Resolvent_Framework/
├── README.md
├── papers/
│   ├── paper_i/           ← Paper I LaTeX (arXiv-ready, 12 pages)
│   ├── paper_ii/          ← Paper II LaTeX (polished, 9 pages)
│   ├── paper_iii/         ← Paper III LaTeX (polished, 18 pages)
│   └── archive/           ← original separate Paper II and III sources
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
│   ├── README.md                    ← note map and naming conventions
│   ├── archive/                     ← superseded notes and scaffolding
│   ├── conceptual/
│   │   └── foundations/             ← conceptual scaffolds not yet theorem programmes
│   ├── future/
│   │   ├── foundations/             ← CE, coherence/completion, zeta
│   │   ├── dynamics_reconstruction/ ← fibre mixing and Lyapunov directions
│   │   └── finite_sample/           ← observational resolution and interaction
│   ├── literature/
│   │   ├── foundations/
│   │   ├── finite_sample/
│   │   └── programme_reception/
│   └── programme/                   ← programme documents, task lists, logs
│       ├── program_overview.md      ← canonical task list and status
│       ├── arxiv_prep.md            ← arXiv submission checklist
│       └── lean_flight_log.md       ← running Lean error/fix log
└── archive/               ← superseded drafts and notes
```

## Lean formalization status

See `formalization/QuerySystem/README.md` for the full sorry inventory.
All main theorems in Papers I and II carry zero sorrys. All remaining sorrys
are documented Mathlib-gap markers, not proof-search failures.

## Current status

See `notes/programme/program_overview.md` for the canonical task list and priorities.

- **Paper I**: arXiv-ready (12 pages). Narrative: interrogative register, CE as logically unavoidable admissibility condition. Abstract updated 2026-04-27 with trilogy arc.
- **Paper II**: 9 pages. Disclosure register: structures read off from the measure, not constructed. Title updated to "Dynamics and Reconstruction in the Observable Measure" (2026-04-27). Terminology: "conditional regularity kernel", "minimal sufficient factor".
- **Paper III**: 18 pages. Opens by picking up Paper II's disclosure register; §2→§3 transition frames the general-to-dynamical move as convergence and strengthening, not specialisation. Abstract updated 2026-04-27 with story arc.
- **Combined monograph**: `papers/combined/combined.tex` — all three papers as Parts I–III; abstract updated to match new register.
- **Next action**: arXiv submission of Paper I and companion note (checklist in `notes/programme/arxiv_prep.md`); Papers II and III follow after endorsement.
