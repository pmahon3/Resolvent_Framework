# The shape of the centre: hypergraph hypotheses for common causes (step 1, framework)

reviewed: false. 2026-11-06. Step 1 of 4 (framework → prior art → method → data), each conditioned on the previous.
Checks: `verification/hypergraph_cones.py` (cvxpy/Clarabel).

## Objects
- **Sites** 1..k. A **hypothesis** is a hypergraph H on the sites; each hyperedge S is a possible centre (a latent cause touching exactly S).
- **Feasible cone** FW_H = {D + Σ_{S∈H} C_S : D ≥ 0 diagonal, C_S ⪰ 0 supported on S}. "H suffices for R" ⟺ R ∈ FW_H.
  Kela et al. 2020 Prop. 1 gives the necessity: if the latent structure is H, then R ∈ FW_H (any responses; per-site transforms allowed).
- Special cases: H = all m-sets gives FW_m (the reach test); H = pairs gives FW₂ (the pairwise ceiling).
- **Test statistic** V_H(R) = min{t : R + tI ∈ FW_H}. It is sublinear (FW_H is a closed convex cone containing the PSD diagonal), so the
  domination + bootstrap proof (`REACH_TEST_VALIDITY.md`, `REACH_TEST_SPEARMAN.md`) transfers **verbatim** to any H.
- **Dependency graph** G(R) = support of R (pairs with r_ij ≠ 0). The observable 2-section.

## Three questions
- **Q1 distinguishability:** when is FW_H ≠ FW_H′ (on correlation matrices with a given support)? Equal cones mean no data can separate the structures.
- **Q2 order:** cones are ordered by inclusion. Is the minimal sufficient hypergraph for R unique, or are there incomparable ones
  (polycentric vs monocentric non-identifiable)?
- **Q3 graph bridge:** which properties of G(R) force or forbid centres larger than pairs?

## Facts (step 1 output)
- **F1 (owned: Agler, Helton, McCullough & Rodman 1988; cf. Grone, Johnson, Sá & Wolkowicz 1984):** if G(R) is **chordal**, every PSD R with that
  support lies in FW_{cliques(G)}: the maximal cliques of G always suffice. Check: two triangles sharing an edge, 40 random R, max V = −0.001 (boundary).
- **F2 (⟦HAND⟧, likely owned via signature similarity / M-matrix theory; Harary balance):** if there are signs sᵢ with sᵢsⱼrᵢⱼ ≤ 0 on all edges
  (equivalently: around every cycle of G, ∏ sign(rᵢⱼ) = (−1)^{length}; call G(R) **balanced**), then R ∈ FW₂ ⟺ R ⪰ 0. Pairwise centres always suffice.
  Proof: SRS (S = diag(s)) is a symmetric Z-matrix; PSD ⇒ M-matrix ⇒ SDD ⇒ FW₂; and FW₂ is invariant under signature similarity.
  **All-positive correlations:** balanced ⟺ G bipartite (no odd cycles).
  Checks (40 random near-boundary PSD R each, positive entries unless noted): max V₂ =
  - 3-cycle +0.95, 5-cycle +0.22, 7-cycle +0.06 (odd: can need a bigger centre);
  - 4-cycle −0.001, 6-cycle −0.001 (even: never);
  - 3-cycle with one negative edge (balanced) −0.001;
  - 4-cycle with one negative edge (unbalanced) +0.34.
- **Reading (Q3, partial):** **a centre larger than a pair can be revealed only by a frustrated cycle**, a loop whose correlation signs do not
  multiply to (−1)^{length}. This is the same frustration condition as the parity twist on cycles (the programme's cyclic-marginal object; cf.
  Kharoof–Ipek–Okay winding), now governing whether coordination needs a centre. The numerics suggest the excess decays with the length of
  the frustrated cycle (0.95, 0.22, 0.06 for L = 3, 5, 7), echoing ε* = V/L. This is an observation, not a theorem.
- **Q1 example:** the triangle {AB, BC, CA} vs {ABC}: FW₂ ⊊ PSD (equal r: r ≤ ½ vs r ≤ 1), so they are distinguishable. On balanced supports FW₂ = PSD,
  so "pairwise" and "one big centre" are **indistinguishable** there, with any amount of data.

## Consequences for the method (to be confirmed in step 2)
1. The polycentric/monocentric question can only be decided on **frustrated** substructures of the dependency graph.
2. Positively correlated synchrony networks (typical in ecology) can reveal centres beyond pairs only through **odd cycles**. Bipartite
   synchrony networks (e.g. a chain, or an even ring of sites) cannot, however strong the synchrony.
3. Chordal dependency graphs bound the needed reach by the clique number.
