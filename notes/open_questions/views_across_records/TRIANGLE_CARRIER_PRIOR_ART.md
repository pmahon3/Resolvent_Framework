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
