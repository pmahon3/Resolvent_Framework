# QuerySystem — Lean 4 Formalization

Lean 4 / Mathlib formalization of Paper I: "When Does Observational
Coherence Determine Probability?"

## Active OML/lattice files

| File | Content | Status |
|------|---------|--------|
| `ConcreteOMLBlocks.lean` | Blocks, overlaps, compatibility, T1/P1/T3/A2 | ✅ axiom-free |
| `ConcreteOMLPatterns.lean` | Clusters, 2BR, Φ-density, B′(i) ⇒ T4 | ✅ axiom-free |
| `MarczewskiTransport.lean` | Compact transport and the ω₁ coarse bank | ✅ axiom-free |
| `InnerRegularity.lean` | Theorem-lets R and two-valued P | ✅ axiom-free |
| `PruningTheorem.lean` | Reconstruction pruning theorem, Steps 2–4 | ✅ axiom-free |

Current mathematical frontier: principal-atom reachability for T4
(`notes/open_questions/oml_attack/oml_lattice_regularity_attack.md`
§§13–26). On countably generated blocks this is equivalent to nonempty
restriction-image interior, so local openness/interpolation is not an
independent intermediate target. T4 is already a named open Lean
proposition; Maharam (8.2) is excluded as its proof engine (§12).
Section 15 records why the tempting finite-generator tree reduction
does not close the f.a.-to-σ-field completion gap.
Section 16 gives the current BC + finite-stage fibre-saturation
sufficient condition; §17 demotes it and isolates contextual cyclic
propagation as the live boundary. No new Lean phase has started.
Section 18 supplies a finite pentagon atom-killing cell and moves the
frontier to countable high-girth assembly.
Section 19 classifies direct/serial pentagon gluing and leaves a
separated-port multi-cell repeater as the current bounded search.
Section 20 supplies a composable repeater and spaced-master candidate;
§21 kills it by σ-state non-separation and moves the finite target to an
essential ternary trigger.
Section 22 finds 45 essential pentagon triggers and moves the frontier
to high-girth ternary composition.
Section 23 finds an indirect essential two-overlap relay and returns the
frontier to infinite structural/state-separation certification.
Section 24 kills that relay by a non-ω-live order witness and makes
σ-live automaton separation the mandatory pre-completion screen.
Section 25 pivots to the all-odd removable pentagon state and finds a
relay with all states live; §26 corrects this as T4 satisfaction and
exhaustively kills the entire two-port pentagon relay class.

## Paper I + companion files

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
