# Hypergraph centres: prior art (step 2)

reviewed: false. 2026-11-06. Scout for `HYPERGRAPH_CENTRES.md`. Shelf grep first: no hits on Boman, factor width, H-/M-matrix, Zaslavsky, Harary, Evans, Walter, Laurent (the only prior entries are the taxonomy rows R-factor-width and R-pdcompletion).
Read levels: **PDF** = full text read here; **snip** = search snippet or abstract; **mem** = from memory, not checked. Scripts: `~/.claude/jobs/26482d7b/tmp/{cycle_gap,incomparable}.py`.

## Q1. Is F2 owned? **OWNED (one-line corollary)**
- Boman, Chen, Parekh & Toledo, *LAA* 405 (2005) [PDF]. **Lemma 5:** a real symmetric A is an M-matrix iff a_ij ≤ 0 (i≠j) and A ⪰ 0. **Thm 9:** factor width ≤ 2 iff symmetric H⁺-matrix (H-matrix = comparison matrix M(A) is an M-matrix). **Thm 16/17:** FW₂ iff ρ(|I − D⁻¹A|) ≤ 1.
  F2 follows directly. If sᵢsⱼrᵢⱼ ≤ 0 on every edge, then SRS = M(R). So R ⪰ 0 ⇒ M(R) ⪰ 0 ⇒ M(R) is an M-matrix (L5) ⇒ R ∈ H⁺ = FW₂ (T9). Signature invariance M(SAS) = M(A) is textbook (snip).
- Balance: Harary 1953. Switching to all-negative is "antibalanced" in Zaslavsky's terms (snip). The user's condition says −(R−I) is balanced, i.e. R−I is antibalanced.
- **Converse, giving the full characterisation** ⟦HAND⟧, via Wielandt's theorem (Horn–Johnson, *Matrix Analysis*, Wielandt/Perron–Frobenius section [mem]). Take A = R − I and G connected. Then λ_min(A) ≥ −ρ(|A|), **with equality iff A = −S|A|S**. Spectral form: PSD ⟺ λ_min(A) ≥ −1; FW₂ ⟺ ρ(|A|) ≤ 1.
  So **{PSD with sign pattern Σ} = {FW₂ with pattern Σ} iff every component of −Σ is balanced**, and over all sign patterns this holds **iff G is a forest**. The unweighted analogue is Stanić's criterion (index equals that of the underlying graph iff balanced; cited in Brunetti–Stanić [snip]). No paper found that states the graph-class version verbatim, but it is a corollary, not a contribution.
- Cross-field rhyme (not the same cone): **completely positive graphs**, Kogan & Berman, *Discrete Math.* 114 (1993) [snip]: every doubly nonnegative matrix with graph G is completely positive iff G has no odd cycle of length ≥ 5. The bipartite case is Berman–Grone, *Math. Proc. Camb. Phil. Soc.* (1988) [snip]. Odd cycles are again the obstruction, but triangles are allowed there and not for FW₂.
- Related: k-PSD closure (dual of FW_k) distance bounds, Blekherman–Dey–Molinaro–Sun, *Math. Program.* 2022, arXiv:2002.02988 [snip]; block FW₂, Zheng–Sootla–Papachristodoulou arXiv:1909.11076 [snip].
- **Terminology correction to parent:** sᵢsⱼrᵢⱼ ≤ 0 is *antibalanced* (Harary/Zaslavsky), not "balanced".
- **Implication.** Present F2 as Boman L5 + T9 plus Harary balance, cited. The forest/antibalance iff is ⟦HAND⟧ via Wielandt. Neither is a contribution.

## Q2. Odd cycles and the PSD–FW₂ gap: **OWNED as a computation; the 1/L² law is a corollary**
- For a nonnegative cycle C_L with L odd, the antibalanced spectrum is 2cos((2j+1)π/L) [standard]. The worst case is equal weights. PSD boundary at r = 1/(2cos(π/L)), so **sup V₂ = sec(π/L) − 1**: 1, 0.236, 0.110, 0.064 for L = 3, 5, 7, 9.
  Numerical maximisation (Nelder–Mead, 200 starts) gives 1.000, 0.2361, 0.1099, 0.0636. The note's 0.95/0.22/0.06 are random-sample maxima that undershoot the sup, most visibly at L = 7. The supremum over unequal weights is numerical, not proved ⟦HAND-numeric⟧.
- **Decay is ~π²/(2L²), not 1/L.** The note's "echoing ε* = V/L" is not supported. It is the spectral gap of a cycle carrying one frustrated edge: λ₁ of the signed Laplacian equals 2 − 2cos(π/L).
- In general (d-regular |A|) the gap ρ(|A|) + λ_min(A) = λ₁(signed Laplacian of −A). Signed-Cheeger theory then bounds it above and below by a frustration constant: Atay & Liu, *Discrete Math.* 343 (2020), arXiv:1411.3530 [snip]. Their constants vanish iff balanced and generalise Harary's frustration index.
- Not the same object: Barrett–Johnson–Loewy cycle (arccos) conditions concern *completion* (off-cycle entries free, here zero).
- **Implication.** Frustration enters quantitatively through signed-Laplacian/Cheeger bounds, which are owned. The L-decay is quadratic. Long frustrated rings are nearly invisible at n ≈ 50.

## Q3. Identifiability of the hypergraph: **PARTLY OWNED**
- **Owned at the distribution level.** Evans, "Graphs for margins of Bayesian networks", *Scand. J. Stat.* 43 (2016), arXiv:1408.1809 [PDF §§3,6]. mDAG = DAG + simplicial complex B of bidirected faces (= the user's H, closed downward).
  - **Prop 6.8:** two mDAGs with no directed edges give the same marginal model iff they are equal. The proof gives M(G) ⊆ M(G′) ⟺ B ⊆ B′.
  - **Ex 6.6:** one latent over {1,2,3} (saturated) vs three pairwise latents (constrained; Fritz 2012) is exactly "one big vs many small centres". Ordinary ADMGs cannot tell them apart (Cor 6.9).
  - **Prop 6.1:** a facet can be split when it rides an instrument-type pattern (directed edges only).
  - Evans §3.1: Gaussian margins carry inequalities that are not fully characterised (Fox et al. 2014; Drton et al. 2012 [mem]).
- **Covariance level (the repo's object).**
  - Cones are still distinct for distinct complexes ⟦HAND⟧. If S ∈ H′∖H, then on matrices supported in S×S every C_T reduces to T∩S ⊊ S, and J_S ∉ FW_{|S|−1}: dual witness X = I − a(J−I), a ∈ (1/(k−1), 1/(k−2)], has all (k−1)-minors PSD and ⟨X,J⟩ < 0.
  - **But a given R need not have a unique minimal H.** Numeric example: K₄ equicorrelation r = 0.4. V₂ = +0.20 (pairs fail), while H_a = {123, 14, 24, 34} and H_b = {124, 13, 23, 34} both give V = −0.079. Each is minimal and their meet is the pairs. So **polycentric configurations are incomparable and not identifiable**. Only the sufficient family, an up-set of cones, is identified.
- Equality-constraint owners do **not** reach this cone. Trek separation (Sullivant, Talaska & Draisma, *Ann. Stat.* 38 (2010) [mem]: rank Σ_{A,B} ≤ r iff t-separation of size ≤ r) and tetrad / pure-measurement clustering (Silva, Scheines, Glymour & Spirtes, *JMLR* 7 (2006) [mem]) need rank-limited latents. With PSD blocks of arbitrary rank, FW_H is full-dimensional on its support: **only inequalities**.
- Markham & Grosse-Wentrup, UAI 2020, arXiv:1910.08778 [snip]: minimal models = edge clique covers of the dependency graph. That uses support only, so on a triangle it always returns the single 3-clique. It is blind to the FW₂-vs-PSD inequality. CPW sparse+low-rank counts latents (rank), not reach.
- **Correction to parent:** "indistinguishable with any amount of data" (balanced supports; bipartite networks "however strong") holds for **second moments only**. By Evans Prop 6.8 the full distribution separates them (Fritz triangle).
- **Implication.** Report the *set* of minimal sufficient H (or the up-set), never "the" centre structure. Distinguishing power is inequality-only.

## Q4. Testing "R ∈ FW_H": **NOT FOUND as an established test**
- Kela et al. 2020 §XI (dual witness, sample split): sketch only (known).
- Nearest established machinery: confirmatory/bifactor/group-factor LRTs test rank-limited *parametric* submodels with fixed loading patterns, with Heywood boundary. Order-restricted inference: chi-bar-square (Silvapulle & Sen 2004; Kuriki & Takemura for the PSD cone [snip]); Drton 2009 *Ann. Stat.* on LRTs at singularities [mem]. None targets a sum-of-PSD-blocks cone with free rank.
- **Implication for step 3.** The repo's V_H + directional bootstrap (Fang–Santos/Hong–Li) is the most direct route, with Kela-type split-sample witnesses as a conservative check. An LRT on the cone would need chi-bar weights from the cone's tangent geometry, which is not available off the shelf.

## Q5. Ecology: **NOT FOUND (signed / frustration); PARTLY (polycentric Moran)**
- Walter, Sheppard, Anderson, Kastens, Bjørnstad, Liebhold & Reuman, *Ecol. Lett.* 20 (2017) 801–814 [PDF]. Synchrony networks are **unweighted**: edges are significant positive synchrony (wavelet). Modules come from modularity, random-walk or spectral methods. Their simulations include block-structured Moran drivers (mechanism A) and matrix regression on candidate drivers.
  This is regional drivers as modules, which counts as polycentric. There are no signed edges, cycles or frustration, and no test against a centre-shape null.
- No ecology paper found on signed synchrony networks or odd cycles. Compensatory dynamics (negative covariance) is treated through variance ratios, which is aggregate, not topological [mem].
- **Implication for step 4.** Positive synchrony networks reveal centres beyond pairs only through odd cycles with strong, near-equal correlations. Triangles dominate, because the bound is sec(π/L) − 1. Use weighted correlations and keep the signs. Modules alone cannot decide polycentric vs monocentric.

## Established method; residue
- **Method:** none established for testing a given hypergraph hypothesis on covariances. Components are owned: the cone (Kela Prop 1 / Boman), mDAG semantics (Evans), and boundary inference (Fang–Santos). The pipeline is the repo's composition.
- **Residue that looks unowned:**
  1. Covariance-level theory of FW_H for simplicial complexes H: the up-set of sufficient complexes, non-unique minima (the K₄ example), and which supports force |S| ≥ 3. (Q3's graph bridge is owned for forests, antibalanced patterns and chordal graphs.)
  2. Quantitative frustration → required-reach bounds beyond m = 2, e.g. FW₃ vs PSD on frustrated graphs.
  3. A calibrated test of a named H on real synchrony data.

  Each needs a hostile pass first (Gaussian mDAG margins, Fox–Drton et al.; arXiv:2405.11556; covariance-network literature beyond Kela).
