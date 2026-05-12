# Structure from Observation

When does observationally coherent data determine a genuine probability
measure?  This repository develops the mathematical answer.

## Paper I — "When Does Observational Coherence Determine Probability?"

A compatible family of finitely additive charges on a directed system of
Boolean algebras extends to a unique σ-additive probability measure if and
only if each charge is σ-additive.  No weaker condition suffices; no
first-order condition can force it.

The Stone construction produces a measure unconditionally: any compatible
charges yield a Baire probability measure on the Stone space St(C).
σ-additivity is equivalent to concentration of this measure on the
principal ultrafilters — the realized states.  The passage from coherent
charges to probability is a geometric commitment, not a derivation.

**LaTeX:** `papers/paper_i/`
**Lean:** `formalization/QuerySystem/QuerySystem/`

### Companion note — "Countable Additivity is Not First-Order Axiomatizable"

σ-additivity is not first-order axiomatizable among finitely additive
probability Boolean algebras.  Proof via ultraproduct of Dirac masses.

**Lean-verified:** `UltrafilterCharge.lean` (0 sorry)

## Lean formalization

| File | Status | Content |
|------|--------|---------|
| `QuerySystem.lean` | ✅ 0 sorry | Definitions, Carathéodory extension |
| `DiscriminabilityFoundations.lean` | ✅ 0 sorry | CE characterization, counterexample |
| `StoneDualityExtension.lean` | 1 sorry | Stone measure construction (proved); descent (Yosida-Hewitt gap) |
| `UltrafilterCharge.lean` | ✅ 0 sorry | Non-σ-additivity of ultrafilter charge |

See `formalization/QuerySystem/README.md` for details.

## Repository structure

```
Resolvent_Framework/
├── papers/
│   ├── paper_i/              ← Paper I LaTeX
│   └── archive/              ← withdrawn Papers II, III
├── formalization/
│   └── QuerySystem/          ← Lean 4 / Mathlib formalization
└── notes/
    └── programme/            ← planning docs, flight log
```

## Status

Paper I is complete and ready for submission.  The classical Boolean
setting has been fully explored: realization is unconstrained by the
algebra, and the passage from coherent charges to probability is a
geometric commitment (σ-additivity), not a derivation.

Future directions involve non-Boolean observation algebras
(orthomodular lattices), where the algebra constrains realization
and the extension problem connects to Gleason-type results.
See `notes/future/` for scoping notes.
