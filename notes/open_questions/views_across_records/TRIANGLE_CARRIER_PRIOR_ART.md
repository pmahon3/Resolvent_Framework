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


## 2026-11-12 third pass: remaining papers

reviewed: false. Third scout. Purpose: obtain and read the bodies named as caps above, and a first search for
S4 (the extension theorem: every compatible triple of window ultrafilters is the window family of exactly one
two-valued finitely additive state on D; induced by an ultrafilter on Ω iff the triple is a pushforward).
Nothing here is a claim of novelty. Hand translations are marked ⟦HAND⟧ and have no second reader.

### 6.0 Headline (leads with what changes)
- **Nothing read owns S1, S2, S3 or S4 as stated.**
- **New close neighbour for S4, to be cited before the extension theorem is stated anywhere:**
  Tylec–Kuś–Krajczok 2016, Thm 12. For every finite two-party box world (complete bipartite window graph) the
  states on the concrete logic GENERATED by the pair cylinders are exactly the compatible (non-signalling)
  families, one state per family. This is the finite, real-valued, bipartite form of "states on the generated
  logic = compatible window families". It does not cover the triangle (their normal form fails there, 6.6),
  infinite alphabets, or two-valued states that are not points.
- Abramsky–Barbosa 2021 Prop 15 owns "compatible families = states" on the glued partial Boolean algebra (the
  union of the window algebras) for every window graph, the triangle included. Extending states to the
  exclusivity closure is their open Conjecture 31. ⟦HAND⟧ D sits on the far side of that conjecture.
- The Kazan caps are closed: Ovchinnikov 1994 and Sultanbekov 1993, 1995, 1998 (the "1996, submitted" item) read in
  full. They own the closed/regular/positive vocabulary and "positive ⇒ closed"; they contain no product-of-three
  logic and no closedness theorem for a logic generated by pair windows.
- Kemperman 1990 and Kellerer §3–4 read: neighbours only, as for Kemperman 1991 and Kellerer §1–2.
- FLRS II is now on the shelf.

### 6.1 Kemperman, "On sets that are uniquely determined by a restricted set of integrals", Trans. AMS 322 (1990) 417–458
Obtained: ams.org free archive through the browser (the site's connection check passed without interaction; the
PDF was saved from the viewer). Shelved `kemperman_1990_sets_uniquely_determined_restricted_integrals.pdf` (OCR
text layer). Read: §1 and §6 in full, statements of §2–5; proofs of §3–5 skimmed.
- Setting (§1, §2): (X, λ) σ-finite measure space, F any set of real functions on X. Everything is a density
  0 ≤ φ ≤ 1 against λ; sets are identified a.e. σ-additive throughout.
- Def 1.3 (p.418): S is a *weak set of uniqueness* if no other set has the same F-moments; φ is a *uniqueness
  function* if no other ψ ∈ [0,1] has the same F-moments; S a *set of uniqueness* if 1_S is one.
- 1.6, 3.10: *special s-additive set* S = ⋃_r {f_q = 0 for q < r, f_r > 0} with f_0..f_s in the span of F(S) and
  a null common zero set; *s-additive function* allows a non-null zero set Z on which F is Z-determining.
  1.9, 3.1: *additive* = {f_0 ≥ 0} or {f_0 > 0}.
- Thm 3.17: generalized additive ⇒ uniqueness. Thm 4.16: if m = dim F < ∞, uniqueness iff
  (m−1)-additive; for nonatomic λ the function must be an indicator of a special generalized additive set.
  Thm 4.11: nonatomic, dim F < ∞, zero sets null: uniqueness iff S = {f_0 > 0}. Rem 4.26 (p.442): X finite ⇒
  uniqueness iff 0-additive (thresholded once).
- §5 richness: Thm 5.15, 5.18: strongly rich (in particular nonatomic with dim F < ∞) ⇒ every φ that is not a
  uniqueness function shares its moments with infinitely many sets.
- §6 (pp.449–458) marginals: arbitrary measurable maps π_j : X → Y_j, j ∈ J; F_π = {g_j(π_j x)} (6.4); finite
  sums f = Σ g_j(π_j x) define the special generalized additive sets (6.10–6.13), which are sets of π-uniqueness.
  Thm 6.23: strongly rich relative to π ⇒ nonatomic and ∞-rich. Thm 6.26: richness passes to derived systems
  τ_j = σ_j π_j. Thm 6.31–6.32: R^n with finitely many central or parallel projections is strongly rich.
  6.33: fails for countably many projections. 6.35: for axes in R^2 uniqueness iff additive; false for n ≥ 3.
- (i) exact sums: none; all sets are thresholds of sums. (ii) closedness of a generated logic: nothing.
  (iii) infinite X is the main case, but the phenomena are transfinite additivity and richness, not a generated
  family or a countable-versus-finite closure. (iv) determination of charges: nothing finitely additive; the only
  determination fact is the moment identity for densities. (v) nothing on two-valued states.
- Verdicts: S1 ADJACENT (same gap as Kemperman 1991: thresholded, uniqueness of one set from its own moments).
  S2 ADJACENT, weakly. S3 ADJACENT (σ-additive densities on the whole space). S4 UNRELATED.
- This removes the cap "most likely place for an exact-representation or infinite-X statement": it is not there.

### 6.2 Ovchinnikov, Izv. Vyssh. Uchebn. Zaved. Mat. 1994 no. 5, 36–40 (Russian)
Obtained: mathnet.ru free full text (opened through the browser; no login). Shelved
`ovchinnikov_1994_galois_correspondence_extension_charges_sigma_class.pdf` (scan, no text layer). Read in full
from page images; five short pages, all statements and proofs understood.
- Setting: Ω finite, card Ω = n. σ-class = family containing Ω, closed under complement and disjoint union. E =
  all σ-classes on Ω. Charge = additive real function on a σ-class; V(𝓔) the space of charges; measure =
  non-negative charge. M = charges on P(Ω) with μ(Ω) = 0.
- Introduction: S^0 = {x ⊆ Ω : μ(x) = 0 for all μ ∈ S}; T^0 = {μ ∈ M : μ(x) = 0 for all x ∈ T}. Remarks 1–4: S^0 is
  a σ-class, T^0 a subspace; the two maps form a Galois correspondence; S^000 = S^0; *closed* = S^00 = S; N := closed
  σ-classes; M and N are complete lattices, anti-isomorphic. Fig. 1: Hasse diagrams of N for n ≤ 4 (card N = 1,
  1, 2, 5, 18).
- §1: σ_𝓔 = restriction V(P(Ω)) → V(𝓔); Ker = 𝓔^0. *Regular*: every charge on 𝓔 is a restriction. Prop 1: regular
  iff dim 𝓔^0 + dim V(𝓔) ≤ n iff equality.
- §2: *positive*: every regular measure on 𝓔 extends to a measure on P(Ω). **Prop 2: P ⊆ N (positive ⇒ closed).**
- §3: algebras are regular and positive; A ⊂ P ⊂ N ⊂ E and A ⊂ R ⊂ E, all strict on six points, no other
  inclusions (Examples 1–3). Last example: Ω = the m×m permutation matrices, atoms x_ij = {a_ij = 1}; states
  correspond to doubly stochastic matrices, so by Birkhoff's theorem 𝓔 ∈ R ∩ P, hence closed, for every m.
- (i) no characterisation of a logic generated by algebras on a product. (ii) closedness at all sizes: only the
  permutation-matrix family, obtained from positivity. (iii) finite only. (iv) regular = charges extend; no
  statement that restrictions to generating algebras determine a charge. (v) none.
- ⟦HAND⟧ For the triangle: by the repo's own records D is closed at every finite size and positive exactly at the
  compressed sizes. So Prop 2 gives closedness of D at compressed sizes once positivity is known (Sullivant), and
  gives nothing at 3×4×4 and beyond. The closedness of D at non-compressed sizes is not reachable by this route.
- Verdicts: S1 ADJACENT (owns the vocabulary and "positive ⇒ closed"; the triangle instance and the non-positive
  closed case are not there). S2 UNRELATED. S3 ADJACENT. S4 UNRELATED.

### 6.3 Sultanbekov: IJTP 32 (1993) 2177–2186; IJTP 34 (1995) 1735–1739; IJTP 37 (1998) 199–202
Obtained: link.springer.com, ordinary fetch from the institutional network (no login). Shelved as
`sultanbekov_1993_set_logics_and_their_representations.pdf`,
`sultanbekov_1995_operation_partitions_best_extension_signed_measures.pdf`,
`sultanbekov_1998_finite_concrete_logics_with_pc.pdf`. All three read in full.
"Sultanbekov 1996 (Solving problems on finite concrete logics with the help of PC, submitted)" in the
Ovchinnikov–Sultanbekov 1998 bibliography is the 1998 paper.
- 1993. Set logic = orthomodular poset with a full set of two-valued finitely additive states; representation =
  isomorphic concrete logic; minimal, separating, A-regular, regular representations. Thm 1.5 (credited to
  Ovchinnikov): a representation of a finite set logic is regular iff dim 𝓔^0 + dim V(𝓔) = number of atoms of the
  generated algebra. §2: n-gon Greechie logics E_n, L_n (Thm 2.2–2.4): automorphisms, extreme states, Fibonacci
  counts of two-valued states, which E_n are absolutely regular, minimal regular representations.
  No products, no marginals. S1–S4 UNRELATED, except S3 ADJACENT through regularity.
- 1995. Thm 1.1: two-valued states of a logic = its partitions E_0 ∪ E_1. Thm 1.3: for concrete logics (E, X),
  (F, Y) and a two-valued state p on F, {Z ⊆ X×Y : every x-section is in F, and the set of x whose section has
  p-value 1 is in E} is a concrete logic on X×Y containing all rectangles A×B. Problem 3.3: when is the
  intersection of these logics the least concrete logic containing all rectangles? Problems 3.4–3.5: product of
  signed measures on it. This is the only place in the Kazan papers read where a concrete logic is put on a
  product; it is a two-factor product of two logics, and the generated logic is posed as a problem, not
  described. S1 ADJACENT (a "least logic on a product" question, different generators); S2, S3 UNRELATED;
  S4 ADJACENT, weakly (two-valued states used to build product logics; no extension theorem).
- 1998. Routines GENER (logic generated by given sets), BIPOLAR (𝓔^00), MINRE. Result: the grid logic D_n =
  Δ({0..n−1}^2) generated by the fibres of x, y, x+y is closed for 1 ≤ n ≤ 10, by computation (Table I). States
  that Ovchinnikov 1992 proved the Gudder–Marchand logics S(L, s) closed for all L ≥ 2, s ≥ 3. So in this school
  closedness at all sizes is a theorem for S(L, s) and for the permutation-matrix logic (6.2), and a computed
  fact up to n = 10 for Δ. S1 ADJACENT (same question, other logics); S2–S4 UNRELATED.

### 6.4 Fishburn–Lagarias–Reeds–Shepp II, Discrete Math. 91 (1991) 149–159
Shelved `fishburn_lagarias_reeds_shepp_1991_projections_axes_II_discrete.pdf` (ScienceDirect open archive; no bot
check appeared this time; saved from the viewer). Not re-read; extract and verdicts as in 5.3.

### 6.5 Kellerer 1964, §3–§4 (pp.180–198), read from page images
- §3, finite factors, bounded problem (R): given r̲ ≤ r̄ on M and marginal functions r_T, find r with r̲ ≤ r ≤ r̄,
  r^T = r_T. Satz 3.1: the solvable data form a finitely generated convex cone. Satz 3.2 (p.181): solvable iff
  Σ_T Σ s_T r_T ≤ Σ_x [(Σ s_T)^+ r̄ − (Σ s_T)^− r̲] for all functions s_T. p.182: the solution is in general not
  unique; example m_i = 2, 𝔗 = all proper subsets, r = ϑ(−1)^{Σ x_i}. Satz 3.3 (p.183): the solutions form a
  polytope whose extreme points are the r with d″_𝔗({r = r̲} ∪ {r = r̄}) = 0, where d″(A) is the dimension of the
  zero-marginal functions vanishing on A. p.183–184: integer data need not have an integer solution when |𝔗| > 2
  (three axes, m_i = 3; "the coefficient matrix is in general not unimodular"). Satz 3.4: a minimal inequality
  system, indexed by s ∈ M′ with ‖s‖ = 1 and d′({s = 0}) = 1. Satz 3.5: two marginals. Satz 3.6–3.7: integer s_T
  bounded by (d−1)! suffice; infinite bounds allowed. Satz 3.8: existence of a bounded signed measure between two
  bounds with prescribed values on finitely many sets.
- §4, general factors. Satz 4.1: one marginal. Satz 4.2–4.3 (pp.192–194): bounded signed ν̲ ≤ ν̄ on the product
  σ-field: a bounded signed ν with ν̲ ≤ ν ≤ ν̄ and marginals ν_T exists iff Σ_T ∫ g_T dν_T ≤ ∫ (Σ g_T)^+ dν̄ −
  ∫ (Σ g_T)^− dν̲ for all bounded measurable g_T (Hahn–Banach on M′). Satz 4.4: two marginals, sets suffice.
  p.196: counterexample for σ-finite bounds. Satz 4.5: σ-finite upper bound with normal marginals.
- Answers to the briefed questions. Uniqueness: none; only the non-uniqueness example (p.182) and the
  extreme-point criterion (Satz 3.3), which is trivially satisfied by every indicator when r̲ = 0, r̄ = 1 ⟦HAND⟧.
  Family of sets whose indicators are sums: nothing in §3–4. Infinite products beyond Satz 1.1: existence under
  bounds only (Satz 4.2–4.5), σ-additive signed measures on the product σ-field.
- Verdicts unchanged from 5.4: S1 OWNS A SPECIAL CASE (the corner criterion and the dimension, Satz 1.1, 1.4);
  S2 ADJACENT; S3 ADJACENT; S4 UNRELATED. p.183–184 is an early statement of the non-unimodularity behind the
  compressed threshold (credit alongside Sullivant).

### 6.6 S4: the extension theorem. First search
Shelf first. Already recorded in `cyclic_marginal/glued_carriers_taxonomy.json`: two-window gluing of ultrafilters
is OWNED (`thm.amalgamation`: β preserves weak pullbacks; Guy / Bhaskara Rao compatibility theorem); the
non-amalgamable triangle families are folklore (G1 audit); Goldberg 2022 and Hindman–Strauss §11, §18 read, pairs
only (`own.hindman_strauss_tensor`, `own.ultrafilter_products`); model-theoretic 3-amalgamation
(`own.type_amalgamation`); van den Berg–Heunen 2012 Prop 8 (compatible families of local ultrafilters as the
spectrum of a partial Boolean algebra). None of these has a state on a set logic built from a non-glued family.
Read today:
- **Tylec–Kuś–Krajczok, "Non-signalling theories and generalized probability", IJTP 55 (2016) 3832–3842,
  arXiv:1512.02457.** arXiv; shelved; pp.1–5 read in full. Setting: finite; two parties with N and M inputs,
  finite outcome sets U_a, V_b; Γ = ∏U_a × ∏V_b. "Let L be a sublogic of Boolean algebra 2^Γ generated by A",
  A = the pair cylinders [aα, bβ] = {x_a = α, y_b = β} (p.3). Observation 10: every element of L is a finite
  disjoint union of sets from A. Lemma 11: normal form of the elements above a cylinder. **Thm 12 (p.4): every
  non-signalling state P defines a state ρ_P on L, additive over cylinder decompositions, and every state on L
  defines a non-signalling state.** Prop 13, 15, Thm 16: compatibility of one-party propositions.
  Gap to S4: window graph complete bipartite, not the triangle; finite alphabets; real-valued states; no
  ultrafilters. ⟦HAND⟧ Observation 10 is false for the triangle: in {0,1}^3 the sets {00∗}, {∗10}, {1∗1} are
  disjoint cylinders and the complement of their union is {011, 100}, an atom of D that is not a cylinder. So the
  bipartite proof does not transfer as written. Verdict S4: ADJACENT, close (owns the finite bipartite analogue).
  S1 ADJACENT (a normal form for a generated pair-cylinder logic, bipartite case). S2, S3 UNRELATED.
- Tylec–Kuś, "Non-signaling boxes and quantum logics", arXiv:1305.3449v3 (2015; journal reference not checked). arXiv; shelved;
  §1–4.2 read. The (2,2) case by exhaustive computation: 82 propositions; Thm 14: orthomodular poset, states =
  non-signalling boxes, 16 two-valued states, set-representable; §4.2: isomorphic to the concrete logic of pair
  cylinders on {0,1}^4. The PR box is a state on a concrete logic that is not a mixture of points. Same verdicts.
- Abramsky–Barbosa 2021 (shelf; Def 13–Prop 15, the start of §4.1 and Conjectures 30–31 read today; rest grepped). Prop 15: for any graphical
  measurement scenario, states on the partial Boolean algebra A_X (the union of the context algebras, glued
  along inclusions) correspond one-to-one to empirical models. Thm 25 and Conjecture 31: a state that extends to
  the exclusivity extension A[⊥] satisfies the probabilistic exclusivity principle; the converse is conjectured,
  extending a state on a partial Boolean algebra to a state on its free extension is stated as open. ⟦HAND⟧ D contains
  disjoint unions across windows, so it lies beyond A_X; the Specker triangle model (perfect anticorrelation on
  each pair, two outcomes) is a compatible family that violates exclusivity (three pairwise disjoint cylinders of
  weight 1/2), so not every probabilistic compatible family extends to D; S4 says the two-valued ones always do.
  Verdict S4: ADJACENT, close (owns the correspondence on the glued algebra; the extension step is their open
  problem in general).
- Burešová–Pták–Ševic 2026 (shelf, arXiv:2609.10770; body read today, 7 pp.). Thm 2.5: if two-valued states
  order-determine L, then L is set-representable and any "well conditioned" pair of states on two Boolean
  subalgebras extends to a state on L. Proof: extend to all subsets by Theory of Charges Thm 3.6.1, restrict.
  Two subalgebras; existence only; the extension is taken through the Boolean algebra of all subsets, which is
  exactly what a non-glued triangle family does not allow. Verdict S4: ADJACENT.
- Pták, CMUC 28 (1987) 157–163 (dml.cz; shelved `ptak_1987_hidden_variables_concrete_logics_extensions.pdf`).
  Thm 4: a two-valued measure on a Boolean sublogic extends to a two-valued measure on any concrete logic
  containing it. One window; existence only. Prop 2: free two-valued measure on the even-cardinality logic on 4
  points. Verdict S4: ADJACENT.
- Kemperman 1990, Kellerer §3–4, Ovchinnikov 1994, Sultanbekov 1993/1998: nothing on S4. Sultanbekov 1995
  Thm 1.1/1.3: weakly adjacent.
Web (5 standard queries; snippet level, weak negatives): ultrafilters on a triple product with prescribed
two-dimensional projections; two-valued states on a concrete logic generated by Boolean algebras; finitely
additive 0–1 measures with given marginals; Tylec–Kuś follow-ups; Foulis–Randall tensor products and
influence-free states. No source found with a three-window ultrafilter family defining a state on a set logic.
Seen in snippets only, NOT opened (unvalidated): Wilce, "Influence-free states on compound quantum systems"
(quant-ph/0507108) and the Kläy–Randall–Foulis line (states on the Foulis–Randall tensor product of test spaces
= non-signalling states; the test-space ancestor of Tylec–Kuś–Krajczok Thm 12); Cardona–Mejía–Uribe-Zapata
arXiv:2503.08910 (abstract mentions a criterion for three compatible finitely additive measures; only Thm 3.12
was read in an earlier pass).

### 6.7 Revised verdicts
- **S1: PARTLY OWNED (unchanged).** Owned: corner criterion and dimension (Kellerer Satz 1.1, 1.4); closed /
  regular / positive vocabulary and positive ⇒ closed (Ovchinnikov 1994 Prop 2, read; 1999 Thm 2.6); compressed
  threshold (Sullivant; non-unimodularity already in Kellerer p.183–184). NOT FOUND, nearest neighbours read past
  abstract (Ovchinnikov 1994, 1999; Sultanbekov 1993, 1995, 1998; Kemperman 1990, 1991; FLRS I, II; Kellerer
  §1–4; Tylec–Kuś–Krajczok): that the logic generated by the three pair algebras is closed at every finite size,
  i.e. equals the 0/1-valued pair-sums.
- **S2: NOT FOUND**, nearest neighbours read past abstract: as in 5.8, plus Kemperman 1990 §6 (infinite X,
  σ-additive, thresholds) and Tylec–Kuś–Krajczok Observation 10 (finite bipartite normal form).
- **S3: NOT FOUND as stated** (unchanged). Owned around it: determination of integrals of pair-sums by marginals
  for measures on the whole product (Kellerer Satz 2.1; Kemperman); regularity (Ovchinnikov).
- **S4: NOT FOUND as stated**, nearest neighbours read past abstract: Tylec–Kuś–Krajczok 2016 Thm 12 (finite
  bipartite analogue, OWNED there), Abramsky–Barbosa 2021 Prop 15 and Conjecture 31, Burešová–Pták–Ševic 2026
  Thm 2.5, Pták 1987 Thm 4, Goldberg 2022 and Hindman–Strauss (pairs of ultrafilters). Owned sub-parts: gluing two
  windows (`thm.amalgamation`); existence of non-amalgamable compatible triples (folklore); the clause "induced by
  an ultrafilter on Ω iff the triple is a pushforward" is immediate from the definitions ⟦HAND⟧. The search was
  one pass at snippet level outside the bodies listed; the negative is bounded by the caps below.

### 6.8 What remains unread
- For S1: Ovchinnikov 1992, "Measures on the logics of Gudder and Marchand", Konstr. Teor. Funktsiĭ i Funk. Anal.
  (Kazan) 8, 95–98 (the all-sizes closedness proof for S(L, s), known only through Sultanbekov 1998); Sultanbekov
  1992 (same volume, 57–68); Ovchinnikov 1985 thesis. Kazan serial, not found online.
- For S1–S3: Aharoni–Herman–Kuba 1997 body; Gardner–Gritzmann 1997; Gutmann–Kemperman–Reeds–Shepp 1991; Kellerer
  1961 (Math. Ann. 144, integer solutions for two marginals); Bhaskara Rao–Bhaskara Rao, Theory of Charges Ch. 3
  (hardcopy, pinned); Dvurečenskij–Neubrunn–Pulmannová 1992; Pták–Pulmannová §1.1–1.3, §2.1, §2.3–2.6 bodies.
- For S4: Foulis–Randall 1981 and Kläy–Randall–Foulis 1987 (tensor products of test spaces, states with given
  marginals); Wilce quant-ph/0507108; Acín–Fritz–Leverrier–Sainz (hypergraph scenarios, consistent exclusivity);
  Tylec–Kuś later tensor-product papers (arXiv:1604.01949 and a 2017 sequel); Cardona–Mejía–Uribe-Zapata
  three-measure criterion; Staton–Uijlen (effect algebras and empirical models); Blass 1970 thesis and Puritz
  (non-tensor two-dimensional ultrafilters); Navara–Rogalewicz on pastings; Abramsky et al. 2016 "Possibilities
  determine the combinatorial structure" (shelf, not re-opened).
- Housekeeping noticed, not changed: `SHELF_INDEX.json` `$meta.count` and `basis_counts` are stale; the
  Burešová–Pták–Ševic entry still says `summary_basis: abstract` although the body is now read.

### 6.9 How it was obtained (third pass)
Ordinary fetches: link.springer.com (three Sultanbekov papers), arXiv (two), dml.cz (one), the mathnet.ru PDF link
once the browser had opened it. Browser (new tabs only, closed afterwards): ams.org (automatic connection check,
no interaction), mathnet.ru, ScienceDirect open archive. No login page, no CAPTCHA interaction, no credentials.
Nine PDFs shelved, nine index entries appended; the Kellerer entry's `text_layer` corrected to false.
