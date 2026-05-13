# Active Lead: Fibre Mixing Condition

## The definition

A dynamical system (X, T, μ) with observable h and delay map
Φ_L satisfies **fibre mixing** at lag L if the conditional
measures on fibres of Φ_L are non-degenerate:

  μ_z(S) · μ_z(S^c) ≥ c · p_z

for μ-a.e. z in the image of Φ_L, for some constant c > 0.

## Why it's novel

This is NOT equivalent to any standard temporal mixing condition
(α, β, ψ, weak Bernoulli, K-mixing). Those concern decorrelation
over time. Fibre mixing concerns spatial non-degeneracy of
conditional measures on fibres of a specific factor map.

Closest relative: **Furstenberg's relative mixing** for extensions
of measure-preserving systems — non-degeneracy of conditional
measures on fibres of a factor. Fibre mixing is weaker: it
requires only one event to straddle fibres, not all events.

## The open question

**Is fibre mixing derivable from standard structural conditions?**

Specifically: if (X, T, μ) is ergodic (or mixing, or K) and h
is a "generic" observable, does fibre mixing hold for sufficiently
large L?

The derivability question is precisely located (step 6):
- Step A: need an analytic bound on κ (the fibre mass balance)
- Step B: need a dynamical condition forcing ν(M_0 ∪ M_1) = 0
  (the degenerate fibres have measure zero)

Neither step is proved. The gap is concrete and well-posed.

## What fibre mixing buys

The bridge theorem (step 7): under fibre mixing,
  geometric convergence (delay map becomes injective)
  ↔ algebraic convergence (Rokhlin distance → 0)

Without fibre mixing, the hard direction fails: geometric
convergence does not imply algebraic convergence.

## The rotation witness

The irrational rotation example (step 4) computes fibre mixing
constants explicitly: c(α, L) ~ Θ(α_n) where α_n are continued
fraction coefficients. The computation is routine (three-distance
theorem / Steinhaus 1958) but identifies the fatal obstruction:
a binary observable on the circle does NOT reconstruct (δ_L does
not converge), so fibre mixing is vacuous in this regime.

This means fibre mixing is only interesting for systems where
reconstruction actually succeeds — i.e., where the observable
is rich enough. The condition is about the quality of the
observable, not just the dynamics.

## Attribution required

- Furstenberg relative mixing: cite and distinguish
- Rokhlin distance: cite for the separation defect
- Three-distance theorem: Steinhaus (1958) / Sós (1958)

## Source files

- Bridge note: papers/archive/paper_iii_withdrawn/notes/bridge_note.tex
- Steps 1-5: notes/archive/fibre_mixing_investigation/
- Steps 6-7: notes/future/dynamics_reconstruction/fibre_mixing/
- Rotation computation: notes/archive/fibre_mixing_investigation/
  step4_rotation_computation.md

## Status

Active lead. The definition is novel, the open question is
well-posed, and the relationship to Furstenberg relative mixing
is unexplored. Needs: (1) Furstenberg comparison, (2) attempt
at Step A/B, (3) assessment of publishability.
