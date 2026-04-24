# Observable Dynamics Program

This repository develops a four-paper mathematical programme showing that
probability, dynamics, reconstruction, and their finite-sample signatures
are not assumptions but consequences of coherent structured observation.

## The argument

```
Structured observations
    → [Paper I]   → probability measure P on (Ω, σ(CylGen))
    → [Paper II]  → dynamics: Koopman operator U_T, semigroup K_t
    → [Paper III] → reconstruction: state space X ≅ St(observable algebra)
    → [Paper IV]  → finite-sample: δ̂ stopping rule, rates, honest bridge
```

The Stone space constructed in Paper I as a technical device for measure
extension reappears in Paper III as the object being reconstructed.
Paper IV asks what this reconstruction looks like from finite data,
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

### Paper II — Dynamics from Probability

Given a probability measure, the temporal structure of prediction is uniquely
determined. The predictive kernel, minimal predictive state map Q\*, and
semigroup {K_t} are derived from temporal coherence, not assumed.
Koopman–Perron duality connects operator-on-functions and measure-on-states.

**LaTeX:** `papers/paper_ii/` (4 pages, editorially polished 2026-04-24)
**Lean:** `PredictiveState.lean` ✅, `PredictiveOperators.lean` ✅ (0 sorrys)

### Paper III — Reconstruction from Observation

Under a cyclic vector condition on the Koopman operator, the delay map
Φ_h : X → ℝ^ℕ is a measure-theoretic embedding and the Stone space of the
observable algebra is isomorphic to the state space. Generalises Takens's
theorem: measurability replaces smoothness, algebraic density replaces the
dimension count.

**LaTeX:** `papers/paper_iii/` (5 pages, editorially polished 2026-04-24)
**Lean:** `ReconstructionTheorem.lean` ✅ (2 Mathlib-gap sorrys),
`DelayEmbedding.lean` ✅

### Paper IV — Finite-Sample Reconstruction: Rates, Witnesses, and the Honest Bridge

Given finite data from the system, can one certify reconstruction from data
alone, and at what rate? Three theorems answer this:

- **Algebra Theorem**: the σ-algebra approximation error δ̂(L,n) concentrates
  around the true δ(L), and the elbow stopping rule L̂* achieves the
  minimax-optimal rate n^{-s/(2s+d)} for Hölder(s) targets without any oracle
  inputs (mixing rate, lag, or smoothness index).
- **Dynamics Theorem**: under uniform separation (US), the delay map is
  bi-Lipschitz and estimated delay vectors certify point separation at rate
  n^{-β/(2β+d)}.
- **Conjunction Theorem**: for deterministic T, algebra separation and metric
  separation are the same event (not merely correlated — identical). Under
  reconstruction and (US), both witnesses certify this from data, and the
  theorem names the failure modes when either condition is removed.

The key insight: for deterministic T the predictive kernel Π_h^(L)(x,·) is a
Dirac delta, making TV separation binary; σ(Φ_h^(L)) = 𝒪_h^(L) is the honest
bridge connecting the two witnesses.

The central obstruction is **large monochromatic fibres** — fibres of the delay
map where the conditional measure is near-degenerate. Lemma 5.10 (Positive-fraction
balance) proves, without any dynamical hypothesis, that a positive ν_L-fraction of
ε-large fibres are η-balanced. The fibre mixing condition is the upgrade to
ν_L-a.e. balance; whether ergodicity supplies it is the main open question.

**LaTeX:** `papers/paper_iv/` (16 pages, editorially polished 2026-04-24; bridge note in `notes/bridge_note.tex`)
**Lean:** Not started

## Repository structure

```
Resolvent_Framework/
├── README.md
├── papers/
│   ├── paper_i/           ← Paper I LaTeX (arXiv-ready, 12 pages)
│   ├── paper_ii/          ← Paper II LaTeX (polished, 4 pages)
│   ├── paper_iii/         ← Paper III LaTeX (polished, 5 pages)
│   └── paper_iv/          ← Paper IV LaTeX (polished, 16 pages)
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
│   ├── archive/                     ← superseded notes and scaffolding
│   │   ├── fibre_mixing_investigation/  ← steps 1–5 (investigative history)
│   │   └── ultralimit_investigation/    ← resolved rungs and LaTeX drafts
│   ├── conceptual/
│   │   └── philosophy/              ← active philosophical notes
│   ├── future/                      ← post-arXiv research directions
│   │   └── fibre_mixing_investigation/ ← steps 6–7 + irreducibility (active)
│   └── programme/                   ← programme documents, task lists, logs
│       ├── program_overview.md      ← canonical task list and status
│       ├── arxiv_prep.md            ← arXiv submission checklist (all four papers)
│       └── lean_flight_log.md       ← running Lean error/fix log
└── archive/               ← superseded drafts and notes
```

## Lean formalization status

See `formalization/QuerySystem/README.md` for the full sorry inventory.
All main theorems in Papers I and II carry zero sorrys. All remaining sorrys
are documented Mathlib-gap markers, not proof-search failures.

## Current status

See `notes/programme/program_overview.md` for the canonical task list and priorities.

- **Paper I**: arXiv-ready (12 pages, MSC classifications, keywords, citations complete).
- **Paper II**: editorially polished (4 pages, 2026-04-24).
- **Paper III**: editorially polished (5 pages, 2026-04-24); 2 Mathlib-gap sorrys in `ReconstructionTheorem.lean`.
- **Paper IV**: editorially polished (16 pages, 2026-04-24); Lemma 5.10 (Positive-fraction balance) added; Lean formalization not started.
- **Bridge note**: `papers/paper_iv/notes/bridge_note.tex` — 4-page companion proving the conditional variance identity and entropy characterisation δ(L)→0 ⟺ H₂(ν_L)→∞; cited as `mahon_bridge` in Paper IV.
- **Next action**: arXiv submission of Paper I and companion note (checklist in `notes/programme/arxiv_prep.md`); Papers II–IV follow after endorsement.
