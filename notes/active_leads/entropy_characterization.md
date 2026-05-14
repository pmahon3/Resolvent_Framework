# Active Lead: Entropy Characterization of Reconstruction

## The result

From the bridge note (Corollary 4.2):

  δ(L) → 0  iff  H₂(ν_L) → ∞

where:
- δ(L) = sup_S inf_{E ∈ O_L} μ(S △ E) is the Rokhlin distance
  between the delay observable σ-algebra and the full σ-algebra
- H₂(ν_L) = -log ∫ ν_L(z)² dz is the Rényi-2 entropy of the
  fibre measure ν_L (the push-forward of μ under the delay map)

## Why it might be novel

The delay embedding literature (Takens, Sauer-Yorke-Casdagli,
Robinson) uses geometric/topological genericity arguments.
Information-theoretic criteria for reconstruction quality are
not standard in that literature.

This specific bridge — Rokhlin distance vanishes iff collision
entropy diverges — connects measure-theoretic reconstruction
(ergodic theory) to information-theoretic quantities (Rényi
entropy). The equivalence is not in Ornstein theory, which uses
d̄-distance and entropy rate, not Rokhlin distance and Rényi-2.

## What needs checking

1. Is this implicit in information-theoretic ergodic theory?
   Check: Shields "Ergodic Theory of Discrete Sample Paths",
   Gray "Entropy and Information Theory", Pinsker.

2. Is the Rokhlin distance → Rényi-2 entropy connection known
   outside the reconstruction context? It might be a standard
   functional analysis fact (the two quantities are related via
   conditional variance).

3. Is this substantial enough for a standalone note/paper, or
   is it a one-line consequence of known identities?

## Attribution required

- Rokhlin distance: cite Rokhlin (1967) and name it
- Rényi-2 entropy: cite Rényi (1961)
- The conditional variance identity connecting them: verify
  whether this is standard

## Source files

- Bridge note: papers/archive/paper_iii_withdrawn/notes/bridge_note.tex
- Fibre mixing step 7: notes/future/dynamics_reconstruction/
  fibre_mixing/step_07_bridge_theorem.md

## Status

Active lead. Needs: (1) verification that the equivalence is
genuinely novel, (2) proper attribution, (3) assessment of
whether it's a paper, a note, or a remark.
