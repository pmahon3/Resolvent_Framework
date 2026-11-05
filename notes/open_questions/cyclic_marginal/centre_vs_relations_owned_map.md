# Centre vs relations: owned-territory map

reviewed: false. 2026-11-05.

Question: when local views cohere, is the coherence held by one common source (centre) or only by local sources/interactions (relations)? Hostile cross-field scout. Read levels: R = full text/section read, A = abstract/summary page only, M = from memory, unread, S = search snippet.
Not re-derived: interior-consistent pairwise margins always admit a pairwise max-ent (MRF) joint; Moran vs dispersal owns the ecology version.

## 1. Owned-region table

| Region | Owner(s) | Read | Already recorded? |
|---|---|---|---|
| Correlation scenarios: sources as hyperedges, observers without inputs; Bell scenarios embed | Fritz 2012 NJP 14 103001 (arXiv:1206.5115), extending Branciard–Rosset–Gisin–Pironio 2010/2012 (bilocal) | A (abstract; triangle content not confirmed) | No (Fritz–Chaves 2013 recorded; Fritz 2012 not) |
| Classical compatibility with latent DAG: inflation, complete asymptotically | Wolfe–Spekkens–Fritz 2019 (arXiv:1609.00672); Navascués–Wolfe 2020 (arXiv:1707.06476): n-th order test within O(n^-1/2) of compatible, zero-error only in the limit | A | WSF yes (shelf, "population level"); Navascués–Wolfe no |
| Finite cardinality of local sources; classical triangle set closed, connected, semialgebraic | Rosset–Gisin–Wolfe 2018 QIC 18 (arXiv:1709.00707) | S | No |
| Quantum triangle: distribution not trilocal, no Bell violation | Renou et al. PRL 123 140401 (arXiv:1905.04902) | R (statements, via ar5iv; proofs not checked) | No |
| Triangle with no-signalling/independence: Finner inequality, limits on correlations | Gisin et al. (arXiv:1906.06495, S); Renou et al. arXiv:1901.08287; Finner 1992 (M) | A/S | No |
| Entropic/information tests for common ancestors | Steudel–Ay, Entropy 17 (2015), arXiv:1010.5720 | R (theorem 10 and caveats) | No |
| Entropy-vector approach to causal structures | Chaves et al. 2014; Weilenmann–Colbeck (arXiv:1605.02078, S) | S | Fritz–Chaves yes |
| Marginal problem, local vs global consistency on cyclic schema | Vorob'ev 1962; Kellerer 1964; BFMY 1983; Abramsky–Brandenburger 2011; Fritz–Chaves 2013 | shelf | YES (merging_seam_prior_art.md) |
| No-three-way-interaction polytope, existence threshold | Sullivant 2006; Ohsugi–Hibi; De Loera–Onn | shelf | YES |
| Pairwise MRF / Hammersley–Clifford; marginal vs local polytope | Besag 1974, Clifford 1990, Wainwright–Jordan 2008, Amari 2001 (hierarchy of interactions) | M | Hammersley–Clifford only as "builds a joint" in ecology sweep |
| Common-cause principle, quantitative | Reichenbach 1956; Hofer-Szabó–Rédei–Szabó 2013 book | M | No |
| Measures of "how much centre": Gács–Körner (common part = shared function), Wyner (min. common randomness for conditional independence), exact common information | Gács–Körner 1973; Wyner 1975; Kumar–Li–El Gamal 2014 | S (Yu–Tan monograph, Now 2024 is the survey) | No |
| Latent class / factor models: identifiability, tetrads | Kruskal 1977; Allman–Matias–Rhodes 2009; Drton–Sturmfels–Sullivant 2007 | M | No |
| Instrument/Bell/IV inequalities, Pearl | Pearl 1995; Wood–Spekkens 2015 | shelf-ish (S) | YES (ecology_contextuality_prior_art_DEEP.md) |
| Categorical probability, infinite products, de Finetti, standard Borel | Fritz–Rischel 2020 (arXiv:1912.02769); Fritz–Gonda–Perrone 2021 (arXiv:2105.02639); d-separation in Markov categories (Fritz–Klingler, M) | S | No |
| Cycles and feedback in causal models | Bongers–Forré–Peters–Mooij 2021; Forré–Mooij 2018; Barrett–Lorenz–Oreshkov 2021 (quantum) | M | No |
| Leaderless distributed computing: symmetric graph coverings block election | Angluin 1980 STOC 82-93 (lifting lemma, coverings; open problem in Sec. 4); Yamashita–Kameda 1996; Boldi–Vigna fibrations; Chalopin–Métivier 2007 | S (statement of lemma not read) | No |
| Sheaf consensus/harmonic sections | Hansen–Ghrist 2019 (arXiv:1808.01513); Robinson; Ghrist–Cooperband 2025 | S | Ghrist–Cooperband yes (shelf); Hansen–Ghrist no. No causal/latent-source use found |
| Ecology: Moran effect vs dispersal; partitioning | Moran 1953; Liebhold–Koenig–Bjørnstad 2004; Vasseur–Fox 2009; Sheppard et al. 2016 (wavelet) | M (unread) | YES (views_across_records_taxonomy.json, unread flag) |

## 2. Sharpest separations (needs a centre vs local sources suffice)

(S1) Steudel–Ay Thm 10 (R). X_1..X_n discrete, I_c = sum_i H(X_i)/c - H(X_1..X_n), 1<=c<=n-1. If I_c>0, every Bayesian net containing the X_i has a node that is an ancestor of more than c of them, and H(A_{c+1}) >= c/(n-c) I_c. Observed nodes may be their own ancestors. Scope: classical, acyclic, finite, sufficient not necessary. Corollaries: X_1=X_2=X_3 nonconstant forces a common ancestor of all three (c=2); three binary uniform variables with H(X1X2X3) < 1.5 log 2 force one. Caveat in the paper: pure 3-way interaction (parity-like) can be produced with only pairwise common ancestors, so high-order dependence does not force a centre. Does not say what the ancestor is, nor handle observed-to-observed edges as "no centre".

(S2) Triangle network is the "relations only" case (Fritz 2012; WSF 2019). Classical set: closed, connected, semialgebraic, finite source cardinality (Rosset et al., S), non-convex (Renou, R). Finner inequality P(000) <= sqrt(P_A(0)P_B(0)P_C(0)) holds for classical, quantum and boxworld triangles (Renou et al., R). Test: inflation hierarchy is asymptotically complete (Navascués–Wolfe, A), so classical compatibility is semi-decidable from outside.

(S3) Quantum relations-only exceeds classical relations-only: Renou et al. Thm 1 (qubit sources, 4 outputs per party, not trilocal for u^2 in (0.785,1)); Thm 2 (qutrit, 9 outputs); Thm 3 (odd N-cycles; even cycles not covered). Scope: finite, proof is a logical contradiction on marginals, not a Bell inequality. Trilocal at u^2=0.785 explicitly constructed; conjecture below that.

(S4) Wyner vs Gács–Körner: a shared deterministic part exists iff maximal correlation = 1; Wyner common information positive iff maximal correlation > 0 (S). This is the two-variable "how much centre" quantity; the triangle generalisation of Wyner is the fully owned quantitative notion.

(S5) HAND, unverified, scope finite alphabets. Perfect correlation X=Y=Z (nonconstant) needs a centre (S1, c=2). Yet it is a limit of pairwise MRF joints (couplings to infinity), while the triangle set is closed (Rosset et al.). So the closure of {pairwise MRFs} is not inside the triangle-compatible set. Interior vs boundary is exactly where "relations as interactions" and "relations as sources" part ways. Conversely, whether every triangle-compatible law with full support is a pairwise MRF is false-looking (3-way interaction can appear), unchecked.

(S6) Loops: for tree-shaped schemas pairwise consistency gives a joint (running intersection, BFMY/Vorob'ev, recorded). For sources, no loop dependence of the S1 type is stated; Angluin-type results key on graph covers, structurally the same device as inflation (an inflation is a covering of the source graph). The Angluin/inflation analogy is mine, M-level, not found in the literature.

## 3. Candidate seams (up to 3)

A. Three notions of "no centre" compared: (i) relations-only sources (triangle), (ii) pairwise-interaction MRF (no 3-way term), (iii) pairwise-consistent views with a joint (Vorob'ev). Existing theories own each; no paper found comparing (i) and (ii) on the same alphabet (search snippets said no direct comparison; Steudel–Ay's pure-3-way remark touches only the DAG case). Target statement: the exact containment/non-containment picture on binary triangle, boundary included (S5). Nearest killer: Fritz 2012 full text, Amari 2001 plus Steudel–Ay (unread beyond Thm 10), Wolfe et al. Section on binary triangle (conjecture: binary triangle classical = quantum, snippet-level).

B. Finitely additive / pointless version: sources as finitely additive states on a carrier with no Ω; is "needs a centre" decidable in the glued-carrier language. Owners of parts: Rosset et al. (finite cardinality reduction, countably additive regime), Fritz–Rischel/Gonda–Perrone (standard Borel Markov categories, hence countably additive and point-based), Navascués–Wolfe (finite). Nothing found for finite additivity or Ω-free carriers. Nearest killer: a Markov-category treatment of "no common ancestor" that works in measure-free (e.g. Boolean/commutative-algebra) settings; Fritz's work on Markov categories without sampling; also Stone-dual probability on Boolean algebras (Gaifman 1964 is recorded).

C. Time order versus snapshot: a ring of units (loop graph) with a stationary process; centre = common driver, relations = coupling. Snapshots cannot decide (in-session), lags can (common driver synchronises at zero lag; dispersal propagates). Owners: Moran/Bjørnstad/Vasseur–Fox, Granger/transfer entropy, CCM false positives (Sugihara 2012, M), LPCMCI (Gerhardus–Runge 2020, M), cyclic SCMs (Bongers et al.). Gap: an exact characterisation of laws of stationary processes on a loop that need a common driver, parallel to Steudel–Ay. Nearest killer: Hugueny 2006 / Hugueny–Cazelles on extended Moran theorem, and Bongers et al. for cyclic structure.

## 4. Unread sources that could close a seam

- Fritz 2012 full text (1206.5115): triangle section, hypergraph structure, open problems (A).
- Wolfe–Spekkens–Fritz 2019 sections on triangle and binary case; shelf copy exists, check the triangle examples (A).
- Steudel–Ay full text: pure 3-way example, whether the net uses observed edges (A).
- Amari 2001, "Information geometry on hierarchy of probability distributions", and Wainwright–Jordan 2008 for MRF closure (A).
- Navascués–Wolfe 2020 full text for scope (finite cardinality assumed?) (B).
- Angluin 1980 / Chalopin–Métivier 2007 for the lifting lemma statement, to test the inflation-as-covering analogy (A, S6).
- Hofer-Szabó–Rédei–Szabó 2013, for the common-cause principle in the non-commutative and non-Boolean setting (A, B).
- Fritz–Klingler on d-separation in Markov categories, and anything on finitely additive Markov categories (B).
- Hugueny 2006 and Sheppard et al. 2016 (C), already flagged unread in views_across_records_taxonomy.json.
- Rosset–Gisin–Wolfe full text: does the cardinality bound need countable additivity (B).
