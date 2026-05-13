# Structure from Observation

What can be determined from observations alone, and what requires
additional commitment?  This repository develops the mathematical answer
across three papers.

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
**Status:** Complete, ready for submission.

### Companion note — "Countable Additivity is Not First-Order Axiomatizable"

**Lean-verified:** `UltrafilterCharge.lean` (0 sorry)

## Paper II — "Distributivity and the Commensurability of Value-Definite Realism and Empirical Adequacy"

Distributivity of the observation algebra is the exact condition (for
dim ≥ 3) under which value-definite realism and empirical adequacy are
commensurable.  The state space admits a filtration S ⊇ S_σ ⊇ S_df
whose three transitions (pasting, regularity, sharpness) are of different
mathematical character.  Distributivity collapses the filtration.

Any collection of Boolean contexts produces an OML via categorical
gluing (Gunji et al. 2026); the commensurability theorem applies to
the colimit.

**LaTeX:** `papers/paper_ii/`
**Lean:** `formalization/QuerySystem/QuerySystem/Commensurability.lean` (0 sorry)
**Status:** First draft, 9 pages.  Target: Synthese.

## Paper III — WITHDRAWN (novelty audit, 2026-05-12)

Attempted: noise thresholds for embedding diagnostics + residual
criterion.  Novelty audit revealed all claims have clear precedent
(Rhodes-Morari 1997, Billings-Voon 1986, Casdagli 1991, Kantz-Schreiber
textbook).  Archived to `papers/archive/paper_iii_canned/`.

## Lean formalization

| File | Status | Content |
|------|--------|---------|
| `QuerySystem.lean` | ✅ 0 sorry | Definitions, Carathéodory extension |
| `DiscriminabilityFoundations.lean` | ✅ 0 sorry | CE characterization, counterexample |
| `StoneDualityExtension.lean` | 1 sorry | Stone measure (proved); descent (Yosida-Hewitt gap) |
| `UltrafilterCharge.lean` | ✅ 0 sorry | Non-σ-additivity of ultrafilter charge |
| `Commensurability.lean` | ✅ 0 sorry | Paper II: VDR for Boolean algebras via Zorn |

## Repository structure

```
Resolvent_Framework/
├── papers/
│   ├── paper_i/              ← Paper I LaTeX
│   ├── paper_ii/             ← Paper II LaTeX
│   ├── paper_iii/            ← Paper III LaTeX + code
│   └── archive/              ← withdrawn earlier Papers II, III
├── formalization/
│   └── QuerySystem/          ← Lean 4 / Mathlib formalization
└── notes/
    ├── programme/            ← planning docs, flight log
    └── future/               ← scoping notes for future directions
```

## The programme

Papers I and II share a single thread: *what you can know depends on
what you're willing to assume, and the boundary between the unconditional
and the committed is algebraic.*

- Paper I: the unconditional object (Stone measure) always exists;
  descent to a probability on Ω requires σ-additivity
- Paper II: empirical adequacy is always available; value-definite
  realism requires distributivity
