reviewed: false. 2026-11-10. Hostile cross-field prior-art scout. Nothing here is a claim of novelty.

# Prior art for the triangle carrier D (S1 finite 0/1-span, S2 infinite normal form, S3 determination)

Object: Omega = X0 x X1 x X2, D = smallest family containing A01 u A12 u A20, closed under complement and (countable) disjoint union.
Scope of this scout: one pass; shelf bodies read where stated; web = search-result snippets and abstracts only unless noted. Weak web reading means "NOT FOUND" below is bounded, not strong.

## 0. Headline
- No source found that states S1, S2 or S3 for the triangle (pair-marginal) logic.
- The nearest *owned* material is (i) Ovchinnikov's closed/regular/positive duality (S1 is exactly "D is closed" for the finite logic D; vocabulary owned, instance not found), (ii) Sullivant/Farkas for the compressed threshold, (iii) Fishburn-Lagarias-Reeds-Shepp / Kemperman "additive sets" (same sum-of-functions shape, but axis projections, not pair projections, and no logic-closure).
- Warning on the briefed pointer: Ovchinnikov Thm 3.3 is NOT S1 (see 1.1).

## 1. Sources

### 1.1 Ovchinnikov, "Measures on finite concrete logics", PAMS 127 (1999) 1957-1966. Shelf PDF, body read (pdftotext, Section 2 defs, Section 3, remarks).
- Def 2.1: E regular iff every signed measure on E extends to P(Omega). Closed: S^oo = S via the polar Galois correspondence (p.1959). Thm 2.5: regular iff dim E^o + dim V(E) = card Omega. Thm 2.6: positive implies closed.
- Thm 3.3 (p.1960): "Delta(Lambda), Lambda = {0..n-1} x {0..m-1}, is regular for all n,m." Delta(Lambda) is the least concrete logic on a planar grid making pi1, pi2, pi1+pi2 measurable: three single-variable-window partitions (coordinate, coordinate, sum), NOT three pair-windows on a 3-fold product. Proof uses additivity of the Gudder integral (Thm 3.1, citing Zerbe/Gudder). Rem 3.6: its two-valued states are points (Navara-Ptak 1983). p.1962: Delta({0..3}^2) not positive.
- Problem 6.2 asks whether every Delta(Lambda) is regular/closed/filled; 6.3 asks whether locally positive implies positive. No product-of-three-coordinates logic, no pair marginals, no infinite case.
- Verdicts: S1 ADJACENT (the duality supplies the vocabulary: S1 for finite X is equivalent to "the finite logic D is closed", HAND translation recorded in `cyclic_marginal/entry_audits/RESOLUTION_ovchinnikov_dnp.md` 1.2, not in the paper); S2 UNRELATED (finite only); S3 ADJACENT (regular = signed measures extend, which implies determination by a spanning set for finite logics; no triangle instance).

### 1.2 Ovchinnikov-Sultanbekov, IJTP 37 (1998) 147-153. Shelf; read in full 2026-10-27 per RESOLUTION file (not re-read today).
- Survey of the same duality, Delta(n x m), Nim/symmetric logics; Thm 2.9 = regularity theorem. Nothing on product carriers. S1/S2/S3: ADJACENT/UNRELATED/ADJACENT as above.

### 1.3 Sultanbekov, arXiv math/0211311 (found via search; abstract-level only, URL fetch failed). Quotes regularity criterion dim E^o + dim V(E) = card Omega. Nothing seen on products. Not an owner as far as read.

### 1.4 De Simone-Navara-Ptak, "Extending states on finite concrete logics" (IJTP 2007) and "States on systems of sets closed under symmetric difference" (Math. Nachr. 2015). Shelf; read per RESOLUTION file.
- Finite shadows of free two-valued states (even-size subsets; 10-point Chinese lantern). Symmetric-difference closure, not disjoint union. No product/pair-window logic. S1 UNRELATED; S2 UNRELATED (σ-part is positive extension on uncountable carriers); S3 ADJACENT (extension of states, opposite direction).

### 1.5 Sullivant, "Compressed polytopes and statistical disclosure limitation", Tohoku Math. J. 58 (2006); arXiv math/0412535. Shelf PDF, grepped: Thm 2.4 (compressed iff facet-width-one criterion), Cor 5.7 (decomposable models compressed), Prop 5.8 as cited by repo. Body of Thm 2.4 read by repo audit (AUDIT_PHASE2).
- Concerns integer points / vertices of marginal polytopes, not "0/1 vectors in the row space are built by complement and disjoint union". It supplies the compressedness threshold for the no-three-way model. S1: OWNS A SPECIAL CASE only of the polytope half (vertices of the marginal polytope are 0/1 iff compressed); logic-closure half not there. S2, S3 UNRELATED.
- Related, snippets only: De Loera-Onn (shelf, `deloera_onn_2002...`; "binary 2-marginals" there means binary-encoded numbers, not 0/1 tables), Ohsugi-Hibi (normality of 3-way tables), Bernstein-Sullivant (normal binary hierarchical models). None states S1.

### 1.6 Fishburn-Lagarias-Reeds-Shepp, "Sets uniquely determined by projections on axes I. Continuous case", SIAM J. Appl. Math. 50 (1990) 288-306; "II. Discrete case", Discrete Math. 91 (1991); Kemperman, Pacific J. Math. 148 (1991) (scanned, unreadable via fetch).
- Via abstracts/secondary: additive sets = sets whose indicator (suitably signed/thresholded) is a sum of bounded functions of single coordinates; bad-configuration criterion for uniqueness; in R^2 uniqueness iff additive; Kemperman found unique non-additive sets for n>=3; discrete: strong set of uniqueness iff additive (reported by Kemperman); weak-set analogue false.
- Gap: projections onto AXES (1-dim), not onto coordinate pairs; "set of uniqueness" for a signed/0-1 counting measure, not a logic closed under disjoint union. The pair-projection analogue (sum f01+f12+f20, switching components in the no-3-way model) is the same pattern in Markov-basis language. Not read in body. S1 ADJACENT (closest analogue of the 0/1-span-versus-realisability question; pair analogue not found); S2 ADJACENT (a "no bad configuration" dichotomy of the same flavour as "no infinite cyclic pattern"); S3 ADJACENT (uniqueness from marginals; their hypothesis is a set, not a state).

### 1.7 Kellerer, "Massthetische Marginalprobleme", Math. Ann. 153 (1964); Vorob'ev (1962). Shelf PDF Kellerer (body not re-read); search snippets.
- Existence of a joint with prescribed marginals depends on the structure of the index family (decomposable/acyclic); signed-measure unrestricted marginal problem treated. Uniqueness for cyclic (non-decomposable) marginals is not what these papers settle; search found no uniqueness statement for finitely additive signed measures on a triple product. S3 ADJACENT; S1/S2 UNRELATED.

### 1.8 Atserias-Kolaitis, bag consistency (2020/2021); Beeri-Fagin-Maier-Yannakakis. Shelf (A-K read per repo audits).
- Triangle = minimal cyclic schema failing local-to-global consistency; global witnesses over semirings. About existence of joints, not about the logic generated by the pair algebras. S1-S3 UNRELATED/ADJACENT (S3 only in the sense that pairwise consistent bags may admit several joints).

### 1.9 Abramsky-Barbosa, "The logic of contextuality" (CSL 2021). Shelf, grepped (free construction extending commeasurability; colimits).
- Partial Boolean algebra freely generated from a cover; triangle cover is the standard example. This is a free *partial* algebra, not the concrete sub-family of P(Omega) closed under disjoint union. S1/S2 ADJACENT (conceptually the same object type; the concrete-logic/normal-form question not addressed in the parts grepped); S3 UNRELATED.

### 1.10 Gudder SIAM Rev 1984, Navara-Ptak 1983, Dravecky-Sipos 1980, Muller-Ptak-Tkadlec 1992, Greechie/Kalmbach. Read in earlier repo passes (RESOLUTION_gudder.md; glued_carriers_taxonomy `own.dynkin_star_normal_form_search`). Neighbours only: two-window rigidity (Gudder Ex 4.2), sigma-class of x, y, x+y; no triangle-of-pair-windows. S1-S3 ADJACENT/UNRELATED.

### 1.11 Marshall-O'Farrell / Khavinson / Garkavi-Medvedev: approximation by sums of functions of fewer variables. Search found only Khavinson-Garkavi-Medvedev (Sb. Math. 187, 1996; Sib. Math. J. 1996) abstracts, no O'Farrell paper. Real-valued approximation and existence of best approximants, not 0/1-valued exact decompositions or logics. S1 ADJACENT (f01+f12+f20 representation theory exists; 0/1 case not found); others UNRELATED. Not read.

## 2. Verdicts

- S1 (finite, D = all 0/1 vectors in the span): PARTLY OWNED / vocabulary owned. Owned: equivalence with "D closed" (Ovchinnikov duality, HAND translation), positive implies closed (O99 Thm 2.6), compressed threshold for the polytope half (Sullivant, Farkas). Not found: a statement that D itself equals the 0/1 span (the closedness instance) for the pair-window triangle. Nearest read past abstract: Ovchinnikov 1999 body (Thm 2.5, 2.6, 3.3). Note Thm 3.3 concerns Delta, a different logic.
- S2 (infinite normal form, no-infinite-cyclic-order dichotomy, E* not in D): NOT FOUND. Searched: shelf index, all taxonomies' owned_regions via grep of names, Ovchinnikov/OS98/DNP/Gudder/Navara-Ptak bodies (repo reads), web on concrete logics, Dynkin generated by coordinate sigma-algebras, additive sets, sums of functions of fewer variables. Nearest read past abstract: DNP 2015 (σ-part, opposite direction), Gudder 1984 Ex 4.2 (two windows), O99 (finite).
- S3 (determination by pair marginals, finitely additive, infinite): NOT FOUND for the infinite case; finite case follows from S1 by linearity and is PARTLY OWNED through the same sources. Nearest: Kellerer/Vorob'ev (existence, not uniqueness), FLRS-Kemperman (axes only, abstract level).

## 3. Unread caps
- Ptak-Pulmannova, Orthomodular Structures as Quantum Logics (1991): hardcopy, user checking; contents not guessed.
- Ovchinnikov 1994a (Izv. VUZ Mat. 1994 no. 5, 36-40, the duality source); Sultanbekov 1992/1993/1996 (set logics, PC computation); Ovchinnikov 1985 thesis. Russian/not located.
- FLRS I and II and Kemperman PJM 1991 bodies (core.ac.uk 403; PJM scan unreadable). Needed to rule out a pair-projection generalisation.
- Bhaskara Rao-Bhaskara Rao, Theory of Charges (1983) body (charge Vorob'ev-type results); Dvurecenskij-Neubrunn-Pulmannova 1992 (on shelf, not grepped); Hammer-type/Marshall-O'Farrell full text; Kellerer 1964 body re-read for signed uniqueness.
- Russian-literature search for Ovchinnikov-school products of partitions was not done.

## 4. Searched scope
Shelf: SHELF_INDEX.json names (Ovchinnikov, Navara, Ptak, De Simone, Gudder, Dravecky, Sipos, Sullivant, Kellerer, Dynkin, concrete logic); repo files RESOLUTION_ovchinnikov_dnp.md, CONVEX_GLUING_T1_PRIOR_ART.md, glued_carriers_taxonomy.json (`own.dynkin_star_normal_form_search`); PDFs read today: O99 (Section 2-3), Sullivant (grep), De Loera-Onn (grep), Abramsky-Barbosa (grep). Not re-opened today: stone_role_prior_art.md, SEAM_B_PRIOR_ART.md, AUDIT_PHASE2.md, REAUDIT_v21.md, G1/G5 audits (relied on RESOLUTION and taxonomy summaries).
Web (about 10 queries, standard mode): FLRS additive sets; no-three-way interaction / 0-1 tables / switching components; concrete logic generated by Boolean algebras / Dynkin of coordinate sigma-algebras; indicator = f(x,y)+g(y,z)+h(z,x); Marshall-O'Farrell/Khavinson; Sullivant compressed polytopes; Ovchinnikov-Sultanbekov follow-ups; finitely additive uniqueness from cyclic marginals; eight-corner identity. Not queried: Hemmecke Markov bases specifically, discrete tomography proper (Gardner-Gritzmann), number-on-forehead cylinder intersections, Kochen-Specker/van den Berg-Heunen, Latin-square/(3,2) marginal literature beyond a slide hit. Search tool is snippet-level, so weak negatives.

## 2026-11-10 second pass: bodies read

reviewed: false. Second scout, same day. Purpose: read the bodies of the caps named in section 3. Nothing here is a claim of novelty. Hand translations between their notions and ours are marked ⟦HAND⟧ and are unverified by a second reader.

### 5.0 Headline (leads with the change)
- **Change to S1.** The "equivalently the eight-corner identity" clause of S1 is OWNED: Kellerer 1964, Satz 1.1 (p.174), for bounded measurable functions on any finite product of measurable spaces (finite or infinite factors) and any family of coordinate subsets. Section 1.7 above said "S1/S2 UNRELATED" for Kellerer on the basis of snippets; that was wrong for S1. Kellerer also owns the dimension of the pair-sum space (Satz 1.4) and the orthogonal splitting into pair-sums and zero-marginal functions (Satz 1.2).
- No source read states that the family generated from the pair cylinders by complement and disjoint union equals the 0/1-valued pair-sums (the closure half of S1), nor S2, nor S3 as stated.
- FLRS I/II and Kemperman are confirmed neighbours, not owners. Kemperman 1991 already works with ARBITRARY families of maps (pair projections included), so the "pair-projection generalisation" exists in print; but its notions (thresholded sums, uniqueness of a set from its own marginals) are different from membership in D.

### 5.1 Kemperman, "Sets of uniqueness and systems of inequalities having a unique solution", Pacific J. Math. 148 (1991) 275-301
Obtained: open access, msp.org (text layer good). Shelved `kemperman_1991_sets_of_uniqueness_inequalities_unique_solution.pdf`. Read: sections 1, 2, 3.1-3.17, 4.11-4.51 in full; construction 3.17-3.32 and proofs 4.1-4.10, 4.21-4.26 skimmed.
- Setting (section 2, p.278-279): X any measurable space with a sigma-finite reference measure lambda; {pi_j : X -> Y_j, j in J} an arbitrary finite or infinite family of measurable maps. "Classical case" (Ex 2.6) = R^n with the n axis projections; Ex 2.7 = {1..a}^n with axis projections. Pair projections are an instance of the general setting but are never singled out.
- Def 2.4 (p.279): S is a *weak set of uniqueness* if no other measurable T has the same marginals; a *(strong) set of uniqueness* if no density 0 <= psi <= 1 other than 1_S has the same marginals as 1_S d lambda. *Uniqueness function*: phi in M_0 with M_0(phi) = {phi}.
- Def 2.8 (p.281): F(S) = functions f(x) = sum_j f_j(pi_j x) with an integrability condition. (2.1), p.278: if two measures have the same marginals then they give the same integral to every g = sum_j g_j(pi_j x).
- Def 2.11 (p.281): S is *additive* if S = {x : f(x) >= 0} for some f in F(S). Lemma 2.14 (p.282): additive => strong set of uniqueness. Property (A) (2.16): every set of uniqueness is additive; holds for R^2 with two axes (Lorentz; FLRS I; Kuba-Volcic), fails for R^n, n >= 3 (Thm 3.23), holds whenever X is finite (2.17(iv)).
- Def 3.1 (p.283): *(stepwise) additive of degree <= m*: lexicographic thresholding by f^(1),...,f^(m) in F(S); Thm 3.11 (p.285): such sets are sets of uniqueness; Lemma 3.8: for finite X degree m collapses to degree 1; Rem 3.15 (p.286): extends to countable ordinals; asks which systems have Property (B) (every set of uniqueness is additive of some countable ordinal degree).
- Section 4, X finite, arbitrary maps: Thm 4.15/4.27 (p.293, 297): x0 is the only solution of Ax = Ax0, alpha <= x <= beta iff some row combination f has the sign pattern (4.17) and the submatrix on the strictly interior coordinates has full rank. Thm 4.42 (p.299): the same for functions phi on X determined by their marginals. Thm 4.50 (p.300): for finite X, S is a set of uniqueness iff additive iff S = {f >= 0} with f a finite sum of f_j(pi_j x) iff the same with f nowhere zero. Rem 4.51: weak uniqueness is strictly weaker (FLRS II example, 66 points in {1..5}^3).
- (i) coordinate planes/pairs: covered only as an unnamed instance of "arbitrary maps". (ii) closure under complement and disjoint union: nothing. (iii) infinite sets: infinite X is where additive and uniqueness separate; transfinite degrees; no finite-type/compactness dichotomy of the S2 kind. (iv) finitely additive measures: nothing (all measures are densities against lambda).
- Relation to D ⟦HAND⟧: take pi_j = the three pair projections, X finite. If 1_E is exactly a pair-sum then E = {1_E - 1/2 >= 0} is additive and so is its complement; so D-sets are sets of uniqueness. The converse fails: in {0,1}^3 a single point is additive (already with axis functions, f = x0+x1+x2-5/2) but its indicator is not a pair-sum (it is not orthogonal to the parity vector). So "additive" (thresholded sum) strictly GENERALISES "indicator equals a pair-sum", and "set of uniqueness" is strictly WEAKER than membership in D. The two questions also quantify differently: a set of uniqueness is recovered from its own marginals; a D-set is one whose measure is fixed by the pair marginals of every (signed) measure.
- Verdicts: S1 ADJACENT (general-marginal framework and the linear fact (2.1); no closure statement, no exact-sum sets). S2 ADJACENT, weakly (infinite X and transfinite additivity; nothing about generated families or an order-pattern obstruction). S3 ADJACENT ((2.1) is the integral-determination fact for measures on the whole space; nothing finitely additive, nothing on a sub-family of sets).

### 5.2 Fishburn-Lagarias-Reeds-Shepp, "Sets uniquely determined by projections on axes I. Continuous case", SIAM J. Appl. Math. 50 (1990) 288-306
Obtained: Penn institutional repository (core.ac.uk was behind a bot check). Shelved `fishburn_lagarias_reeds_shepp_1990_projections_axes_I_continuous.pdf`. Read: sections 1-2 and the statements of section 3; proofs of Thm 3.2/3.3 and the Appendix skimmed.
- Setting: sets of finite measure in R^n, hyperplane-integral projections onto the n coordinate AXES only (1.1). p.289 argues n axis directions is the minimum.
- Additive (1.2, p.290): x in S iff sum_i f_i(x_i) >= 0 with bounded measurable f_i. Thm 1.1: additive => set of uniqueness. *k-bad configuration* (p.291): distinct z^1..z^k in Int(S) and distinct w^1..w^k in Int(S^c) with the same number of z's and w's in every hyperplane x_i = c; *weakly k-bad*: repetitions allowed. Thm 1.2: a set of uniqueness has no bad configuration. Thm 2.1: for open sets, bad and weakly bad coincide. Thm 2.2 (n=2): set of uniqueness iff additive (Lorentz 1949). Thm 2.3: open sets in R^2: unique among open sets iff no k-bad configuration, iff (boundary null) no 2-bad configuration.
- Thm 3.1: if measures mu on S and nu on S^c have the same axis marginals then S is not additive. Thm 3.2/3.3: S0 = {x in [0,1]^3 : x3 >= max(x1,x2)} is a monotone limit of additive sets, is not additive and is not a set of uniqueness; so neither property is closed under monotone limits for n >= 3.
- Infinite phenomena: Remark (1) p.297: Lemma 2.4 fails in infinite area ("infinite checkerboard staircase", Fig. 2.2). Lemma 2.5 (p.297, Appendix): two disjoint bounded open sets in R^3 with identical axis projections and no finite bad configuration; every bad configuration "contains infinitely many points" (end of the Appendix).
- (i) pairs/planes: nothing. (ii) closure of a family: nothing (only: not closed under monotone limits). (iii) see Lemma 2.5: an obstruction that is only infinite, in the opposite direction to S2 (there a non-unique set has no finite witness; in S2 a pair-sum set outside D has an infinite pattern as witness). (iv) nothing.
- Verdicts: S1 ADJACENT (axes; thresholded). S2 ADJACENT (same flavour: finite versus infinite configurations, an order-defined set S0 as the counterexample; different object and different statement). S3 UNRELATED.

### 5.3 Fishburn-Lagarias-Reeds-Shepp, "... II. Discrete case", Discrete Math. 91 (1991) 149-159
Obtained: NOT shelved. Elsevier open archive showed the scanned PDF in the browser viewer; direct download blocked by a bot check, no text layer for page-text extraction. Read level: body read in browser from page images (all 11 pages viewed; statements read; long case proof of Thm 5 skimmed), PDF not shelved. To shelve: the user can download it from the ScienceDirect open-archive page.
- Setting: finite S in N^n = {1..N}^n, coordinate projection COUNTS P_i(j) = |{x in S : x_i = j}| (axes only). *Set of uniqueness* here = the only SUBSET with these projections (Kemperman's "weak" notion).
- (1) additive: x in S iff sum_i f_i(x_i) >= 0, f_i : N -> R. (2) k-bad configuration: k distinct z's in S, k distinct w's outside, |{h : z^h_i = j}| = |{h : w^h_i = j}| for all (i,j); bad rectangle = 2-bad, n=2. (3) weakly k-bad: repetitions (multiplicities) allowed.
- Thm 1 (p.151): set of uniqueness iff no k-bad configuration for all k >= 2. Thm 2 (p.152): additive iff no weakly k-bad configuration for all k >= 2 (linear separation theorem). Thm 3 (p.153): n=2: uniqueness, additive, no bad, no weakly bad, no bad rectangle are equivalent. Thm 4 (p.154): a 14-point S_1 in 3^3 with a 3-bad but no 2-bad configuration. Thm 5 (p.155): S_2 in 5^3, a set of uniqueness that is not additive.
- p.151: for N=2 this is threshold-function theory (Chow 1961, Lapidot 1972, Winder 1971 "Chow parameters"; Gabelman's example). Open problems (p.158): bound on k; counting.
- (i)-(iv): nothing on pairs/planes, on generated families, on infinite sets, or on finitely additive measures.
- Verdicts: S1 ADJACENT (the bad-configuration calculus is the axis analogue of zero-pair-marginal signed tables; no pair version, no closure). S2 UNRELATED. S3 UNRELATED.

### 5.4 Kellerer, "Masstheoretische Marginalprobleme", Math. Ann. 153 (1964) 168-198 (shelf; scan without usable text layer)
Read from page images: pp.168-180 (Einleitung, section 0, section 1, section 2, start of section 3). Sections 3-4 (the bounded/positive problem) not read.
- Setting: product of measurable spaces (M_i, K_i), i in I finite; T a family of subsets of I; "allgemeines Mass" = signed measure; marginals nu^T.
- Section 1 Definition (p.174): M'_T(K) = { sum_{T in T} g_T : g_T bounded measurable, depending on x_T only }; M''_T(mu) = { g : all T-marginal integrals of g against the product measure vanish }.
- **Satz 1.1 (p.174):** M'_T(K) is exactly the set of bounded measurable g with sum_{S subset T} (-1)^{|S|} g(x on the intersection of S, y on the rest) = 0 for all x, y in M. ⟦HAND⟧ instance for I = {0,1,2}, T = the three pairs: g(x0,x1,x2) + g(x0,y1,y2) + g(y0,x1,y2) + g(y0,y1,x2) = g(x0,x1,y2) + g(y0,x1,x2) + g(x0,y1,x2) + g(y0,y1,y2), which for g = 1_E is the eight-corner identity of S1. It holds for arbitrary (also infinite) factors.
- Satz 1.2 (p.175): M' and M'' are closed, orthogonal with respect to the product measure, and together span all bounded measurable functions. Satz 1.4 (p.177), finite sets of sizes m_i: dim M' = sum over nonempty S subset T of (-1)^{|S|-1} m_{intersection of S}; ⟦HAND⟧ for the three pairs this is m0 m1 + m1 m2 + m2 m0 - m0 - m1 - m2 + 1, with complement prod (m_i - 1) (stated on p.177 for T = {I - {i}}).
- Satz 2.1 (p.177-178): bounded signed nu_T are compatible iff sum_T int g_T d nu_T = 0 whenever sum_T g_T = 0; so the integral of any g in M' is well defined by the marginals. Satz 2.2 (p.178): compatible bounded signed marginals always have a bounded signed joint (inclusion-exclusion formula). p.179: "ein allgemeines Mass ... durch die Marginalmasse nu^T, T != I, im allgemeinen nicht eindeutig bestimmt ist".
- Answer to the briefed question: in the pages read there is NO uniqueness theorem for a measure with given cyclic 2-dimensional marginals; only existence (signed case), the explicit non-uniqueness remark on p.179, and the dimension count that measures the non-uniqueness. Sections 3-4 treat existence under bounds and were not read.
- (ii) closure of a family of sets: nothing. (iii) Satz 1.1 covers infinite factors, for functions; nothing on generated families. (iv) sigma-additive signed measures on the product sigma-field only.
- Verdicts: S1 OWNS A SPECIAL CASE: the equivalence "indicator is a pair-sum iff eight-corner identity" (Satz 1.1) and the dimension of the span (Satz 1.4). Not the statement that the generated family D equals the 0/1 pair-sums. S2 ADJACENT (the pair-sum sets in the infinite case are characterised by Satz 1.1; D, the normal form and E* are not there). S3 ADJACENT (Satz 2.1 gives determination of integrals of pair-sums by the marginals for signed measures on the whole product; nothing for finitely additive functions defined only on D).

### 5.5 Generalisations beyond axis projections (target 4)
- Kemperman 1991 (5.1) is the general-marginal version, body read.
- Aharoni-Herman-Kuba, "Binary vectors partially determined by linear equation systems", Discrete Math. 171 (1997) 1-16. Open archive, viewer only; abstract and pp.1-2 read in browser, body NOT read, not shelved. General "projection matrix" P; a position j is *invariant* if all solutions of Px = Pa in a domain agree at j; *integral invariance* (binary solutions) versus *fractional invariance* (solutions in [0,1]^J); Farkas-type criterion; the two coincide for totally unimodular P; applied to row/column sums of binary pictures. About coordinates of one vector, not about which sets have marginal-determined measure. S1-S3 ADJACENT at most (abstract level).
- Vallejo, arXiv:1408.6219 (shelved `vallejo_2014_kronecker_stability_discrete_tomography.pdf`; sections 1 and 3 read): the Torres-Chazaro-Vallejo line treats 3-dimensional binary matrices with given 1-marginals (plane sums, i.e. axis projections); Thm 3.4: matrix of uniqueness iff minimal and pi-unique. No 2-marginal uniqueness theory. S1-S3 UNRELATED.
- Two web queries for uniqueness of 0/1 three-way tables from two-way margins / line sums returned no characterisation (snippet level; weak negative). Gardner-Gritzmann (TAMS 1997) and Gardner-Gritzmann-Prangenberg not opened.

### 5.6 Not obtained
- Kemperman, "On sets that are uniquely determined by a restricted set of integrals", Trans. AMS 322 (1990) 417-458: ams.org bot check on direct download; not pursued in the browser. Free at AMS; the user can download.
- Gutmann-Kemperman-Reeds-Shepp, "Existence of probability measures with given marginals" (Ann. Probab. 1991): cited by FLRS I and Kemperman for the reduction from bounded densities to 0/1 densities; not sought.
- Sultanbekov IJTP 32 (1993) and 1996; Ovchinnikov 1994 (Izv. VUZ Mat. 1994 no.5, 36-40; mathnet record ivm4218, English title per the AMS reference list "Galois correspondence associated with the extension of charges on the sigma-class of subsets of a finite set"): library proxy asked for a login (stopped); the mathnet full-text URL did not return a PDF. Needs user login / manual download.
### 5.7 Sultanbekov, arXiv:math/0211311 (the item of 1.3)
Obtained from arXiv, shelved `sultanbekov_2002_33_homogeneous_greechie_omps.pdf`; sections 1-2 start read, rest grepped. (3,3)-homogeneous Greechie logics and their state spaces; quotes the regularity criterion. No products, no marginals. S1-S3 UNRELATED.

### 5.8 Revised verdicts
- **S1: PARTLY OWNED (more than in the first pass).** Owned: pair-sum iff eight-corner identity, and the dimension of the span (Kellerer 1964 Satz 1.1, 1.4, read); the closed/regular/positive duality vocabulary (Ovchinnikov 1999, read); compressed threshold (Sullivant). NOT FOUND, with nearest neighbours read past abstract (Kellerer section 1, Kemperman 1991, FLRS I and II, Ovchinnikov 1999): that the family generated from the three pair algebras by complement and disjoint union is exactly the set of 0/1-valued pair-sums.
- **S2: NOT FOUND**, nearest neighbours read past abstract: FLRS I Lemma 2.5 and Thm 3.2 (infinite-only configurations; order-defined counterexample, axis setting), Kemperman Rem 3.15 (transfinite additivity), Kellerer Satz 1.1 (pair-sum functions on infinite products). None concerns the generated family, countable versus finite closure, the normal form, or E*.
- **S3: NOT FOUND as stated.** The integral-determination fact for measures on the whole product is OWNED (Kellerer Satz 2.1; Kemperman (2.1)); Kellerer p.179 states non-uniqueness of the joint. ⟦HAND⟧ remark: for the FINITE closure S3 is immediate (two finitely additive functions agree on a family closed under complement and disjoint union), so the content of S3 for the countable closure is S2's "countable closure = finite closure".
- Caps that keep these at NOT FOUND rather than stronger: Kemperman TAMS 1990 (restricted sets of integrals: the most likely place for an "exact representation" or infinite-X statement), Aharoni-Herman-Kuba body, Sultanbekov 1993/1996, Ovchinnikov 1994, Ptak-Pulmannova 1991, Kellerer sections 3-4, Gardner-Gritzmann.

### 5.9 Vocabulary owned by the neighbours (for new text)
- *marginal problem*, *T-marginals*, *compatible (vertraeglich) marginals* (Kellerer). The pair-sum space is Kellerer's M'_T; its orthogonal complement M''_T is the space of functions with vanishing marginals (statistics: moves of the no-three-way-interaction model; tomography: switching components / bad configurations).
- The eight-corner identity should be cited as Kellerer's alternating-sum criterion (Satz 1.1), not presented as ours.
- *additive set* is TAKEN and means a thresholded sum {sum f_j(pi_j x) >= 0} (FLRS, Kemperman). Do not use it for D-sets, whose indicator EQUALS a sum. *(strong) set of uniqueness*, *weak set of uniqueness*, *uniqueness function*, *(weakly) k-bad configuration*, *bad rectangle*, *stepwise additive of degree m* are theirs. For two-point factors: *threshold function*, *Chow parameters*. AHK: *projection matrix*, *integral / fractional invariance* of a position.

### 5.10 How it was searched (second pass)
Direct downloads: msp.org (ok), Penn repository (ok), arXiv (ok), core.ac.uk / ams.org / ScienceDirect PDF (bot checks; not bypassed), mathnet (no PDF returned). Browser: ScienceDirect open-archive viewer for FLRS II and AHK (read from page images); library proxy asked for login (stopped). Web: 6 standard queries (FLRS PDFs; additive sets with two-dimensional marginals; Vallejo/Torres-Chazaro; binary three-way tables from two-way margins; AHK; Ovchinnikov 1994). Shelf index updated: four new entries, Kellerer entry extended.

## 2026-11-12 hardcopy read: Pták–Pulmannová, *Orthomodular Structures as Quantum Logics* (1991) (user)

Primary source, read by the user from the hardcopy; statements relayed in chat, no second reader. Lookup sheet:
`../kits/ptak_pulmannova_lookup_sheet.pdf` (v2).

**Scope covered.** §2.2 in full (2.2.1–2.2.6); §2.7 in full (2.7.1–2.7.2); Chapter 1 and Chapter 2 at section-title
level (1.1 basic examples; 1.2 compatible pairs, sublogics, product logics, morphisms; 1.3 intrinsic properties,
compatible subsets; 2.1 basic properties of states; 2.3 states on the product of logics; 2.4 exotic logics; 2.5
Jauch–Piron states; 2.6 logics with given state space and given centre). Not read: bodies of §1.1–1.3, §2.1,
§2.3–2.6; later chapters; the index.

**What is there.**
- Thm 2.2.1 (Gudder): a logic is concrete iff it has a rich set of two-valued states; in the representation each
  two-valued state becomes a point of the representing set.
- Prop 2.2.3: sublogics of concrete logics are concrete; products and {0,1}-pastings of concrete logics are concrete.
- Lemma 2.2.4, Thm 2.2.5: Loomis–Sikorski for Boolean σ-algebras and for logics (every logic is a morphic image of a
  concrete one, with centres and compatible subsets lifting).
- Lemma 2.2.6: a Boolean-power construction for logics with finite blocks (prescribed centre).
- Prop 2.7.1, 2.7.2: a state on exp I (I of admissible cardinality) or on L(H) extends to any unital logic containing
  it as a sublogic; a state on a Boolean σ-algebra inside L(H), dim H ≥ 3, extends to L(H).

**Verdicts for the sheet's items, within the scope covered.**
| Item | Verdict |
|---|---|
| 1 normal form for a logic generated by several (σ-)algebras of sets | NOT THERE at title level in Ch. 1–2; bodies of §1.1–1.3 unread |
| 1′ a state on a concrete logic is determined by its restrictions to generating blocks | NOT THERE (§2.2, §2.7) |
| 2 two-valued state on a concrete logic given by no point of the underlying set | NOT THERE as an example or theorem; only Gudder's representation, where states become points |
| 3 countable underlying set, two-valued state with no σ-additive extension | NOT THERE (§2.2, §2.7) |

**Why the book does not reach the triangle statements.** Its results answer "which logics have good state spaces"
and "build a logic with a given one"; it does not take a particular logic of sets and compute its states. Its
extension results go upward from one Boolean piece and give existence only. States there are σ-additive; on a
countable set σ-additive two-valued states are points, so the finitely additive phenomenon is outside its setting.
"Pointless" is relative to the chosen underlying set (Gudder): consistent with our records.

**Effect on the verdicts above.** Pták–Pulmannová 1991 is no longer an unread cap for S2 and S3 within §2.2 and
§2.7. Remaining caps: Kemperman, Trans. AMS 1990; Sultanbekov 1993/96; Ovchinnikov 1994; Kellerer §3–4; the unread
bodies listed above. Overall: S1 partly owned (Kellerer criterion; Ovchinnikov vocabulary; Sullivant threshold);
S2, S3 and the extension theorem NOT FOUND. Nothing is claimed.

