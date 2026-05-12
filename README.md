# Structure from Observation

When does observationally coherent data determine a genuine probability
measure?  And when does the observation algebra permit value-definite
realism?  This repository develops the mathematical answers.

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

## Paper II — "Distributivity and the Commensurability of Value-Definite Realism and Empirical Adequacy"

Distributivity of the observation algebra is the exact condition (for
dim ≥ 3) under which value-definite realism and empirical adequacy are
commensurable.  Three nested positions — empirical adequacy (EA),
probabilistic realism (PR), value-definite realism (VDR) — are all
available for Boolean algebras.  For orthomodular lattices, VDR is
blocked by the Kochen–Specker theorem while PR remains available via
Gleason.

The state space admits a filtration S ⊇ S_σ ⊇ S_df whose three
transitions (pasting, regularity, sharpness) are of different
mathematical character.  Distributivity collapses the filtration.
Any collection of Boolean contexts produces an OML via categorical
gluing; the commensurability theorem applies to the colimit.

**LaTeX:** `papers/paper_ii/`

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
│   ├── paper_ii/             ← Paper II LaTeX
│   └── archive/              ← withdrawn earlier Papers II, III
├── formalization/
│   └── QuerySystem/          ← Lean 4 / Mathlib formalization
└── notes/
    ├── programme/            ← planning docs, flight log
    └── future/               ← scoping notes for future directions
```

## Status

Paper I is complete and ready for submission.  Paper II (first draft,
8 pages) extends the framework to orthomodular observation algebras
via the McDonald–Bimbó duality and the Gunji et al. colimit
construction.  Target venue: Synthese.
