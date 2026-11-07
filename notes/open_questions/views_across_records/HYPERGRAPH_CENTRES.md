# The shape of the centre: hypergraph hypotheses for common causes (step 1, framework)

reviewed: false. 2026-11-06. Step 1 of 4 (framework → prior art → method → data), each conditioned on the previous.
Checks: `verification/hypergraph_cones.py` (cvxpy/Clarabel).

**Terms (added 2026-11-06; reviewed: false).** Centre = common cause (a latent common ancestor). Sign convention: a cycle is **not antibalanced** when its correlation signs do not multiply to (−1)^{length}. Older text here calls this "frustrated"; it is frustration of −R. A signed-graph reader calls product −1 "frustrated" (Toulouse 1977; Zaslavsky; Harary 1953 says "unbalanced"), which reads the other way on triangles. The size m of a centre is its **cause arity** (factor width m; formerly "reach"). See `../../programme/TERMINOLOGY_CROSSWALK.md`.

## Objects
- **Sites** 1..k. A **hypothesis** is a hypergraph H on the sites; each hyperedge S is a possible centre (a latent cause touching exactly S).
- **Feasible cone** FW_H = {D + Σ_{S∈H} C_S : D ≥ 0 diagonal, C_S ⪰ 0 supported on S}. "H suffices for R" ⟺ R ∈ FW_H.
  Kela et al. 2020 Prop. 1 gives the necessity: if the latent structure is H, then R ∈ FW_H (any responses; per-site transforms allowed).
- Special cases: H = all m-sets gives FW_m (the cause-arity test; formerly "reach test"); H = pairs gives FW₂ (the pairwise ceiling).
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
- **F2 (OWNED: Boman, Chen, Parekh & Toledo 2005, Lemma 5 + Thm 9; read in step 2):** if there are signs sᵢ with sᵢsⱼrᵢⱼ ≤ 0 on all edges
  (equivalently: around every cycle of G, ∏ sign(rᵢⱼ) = (−1)^{length}; G(R) is **antibalanced** in Harary/Zaslavsky terms. Earlier drafts said "balanced"; corrected 2026-11-06), then R ∈ FW₂ ⟺ R ⪰ 0. Pairwise centres always suffice.
  Proof: SRS (S = diag(s)) is a symmetric Z-matrix; PSD ⇒ M-matrix ⇒ SDD ⇒ FW₂; and FW₂ is invariant under signature similarity.
  **All-positive correlations:** antibalanced ⟺ G bipartite (no odd cycles). [2026-11-06 terminology pass: this line and the 3-cycle line below said "balanced", left over from before the correction above; the 4-cycle line said "unbalanced", which was correct in Harary's convention and was renamed only for consistency.]
  Checks (40 random near-boundary PSD R each, positive entries unless noted): max V₂ =
  - 3-cycle +0.95, 5-cycle +0.22, 7-cycle +0.06 (odd: can need a bigger centre);
  - 4-cycle −0.001, 6-cycle −0.001 (even: never);
  - 3-cycle with one negative edge (antibalanced) −0.001;
  - 4-cycle with one negative edge (not antibalanced) +0.34.
- **Reading (Q3, partial):** **a centre larger than a pair can be revealed only by a cycle that is not antibalanced**, a loop whose correlation signs do not
  multiply to (−1)^{length} ("frustrated" in older text, see Terms). This is the same frustration condition as the parity twist on cycles (the programme's cyclic-marginal object; cf.
  Kharoof–Ipek–Okay winding), now governing whether coordination needs a centre. **Corrected 2026-11-06:** the maximal excess on a positive odd
  L-cycle is exactly **sec(π/L) − 1 ≈ π²/(2L²)** (1, 0.236, 0.110, 0.064 for L = 3, 5, 7, 9; verified at the PSD boundary to 10⁻⁴). The sample maxima
  0.95/0.22/0.06 undershoot it. The decay is ~1/L², **not** the 1/L of ε* = V/L; that "echo" remark is withdrawn.
- **Q1 example:** the triangle {AB, BC, CA} vs {ABC}: FW₂ ⊊ PSD (equal r: r ≤ ½ vs r ≤ 1), so they are distinguishable. On antibalanced supports
  FW₂ = PSD, so "pairwise" and "one big centre" are indistinguishable **from second moments (correlations) alone**, with any amount of data.
  **Corrected 2026-11-06:** at the level of full distributions they *are* distinguishable (Evans 2016, Prop. 6.8: distinct latent-only hypergraphs give
  distinct models; Ex. 6.6 is the triangle). The limit is a property of covariance-based tests, not of the structures.
- **Q2 answered (step 2, verified): the minimal sufficient hypergraph is NOT unique.** K₄ with equal r = 0.4: pairs fail (V₂ = +0.20), but
  {012, 03, 13, 23} and {013, 02, 12, 23} both suffice (V = −0.079 each) and are incomparable. The sufficient hypergraphs form an up-set with
  several minimal elements. Polycentric structure is not identifiable from correlations in general.

## Consequences for the method (to be confirmed in step 2)
1. The polycentric/monocentric question can only be decided on **not-antibalanced** substructures of the dependency graph.
2. Positively correlated synchrony networks (typical in ecology) can reveal centres beyond pairs, **from correlations**, only through **odd cycles**.
   Sparse bipartite networks (e.g. a chain, or an even ring of sites with truly uncorrelated non-neighbours) cannot, however strong the synchrony.
   Higher-order statistics could (Evans).
3. Chordal dependency graphs bound the needed cause arity by the clique number.
