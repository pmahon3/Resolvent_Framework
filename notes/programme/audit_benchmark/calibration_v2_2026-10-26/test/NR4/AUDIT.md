## Audit: seed.md, a composite (wedge-type) product of table algebras (mode: full)

**Audit date (per AS_OF.md): 2015-08-22.** Only sources dated on or before this date count as prior art. Any paper that is the seed's own work (the arXiv preprints 1508.05604 and 1509.06046 by J. Bagherian, which turned up in searches) was set aside as the submission itself and is not used as prior art. Search access dates: 2026-10-26.

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)

The seed declares types but states no per-type bar it commits to clearing. That is a Phase-1 defect and is noted, not fatal.

### Stripped statement

The seed's "one scheme placed on top of another, the relations of the second refining one class of the first" is Muzychuk's **wedge product** of association schemes. It generalises the wreath product and is itself the scheme form of the Leung–Man wedge product of Schur rings, called the "generalized wreath product" by Evdokimov–Ponomarenko. The seed claims three things:
- (D) the definition of a wedge product of table algebras;
- (T1) a necessary and sufficient condition for a table algebra to be a wedge product of two smaller ones;
- (T2) if two commutative table algebras have table-algebra duals, then the dual of their wedge product is a table algebra, isomorphic to the wedge product of the duals in reverse order;
- plus corollaries for schemes.

### Pure Verdict: UNCLEAR (leaning NOVEL-but-incremental)

Owned regions found (all dated before 2015-08-22):
- **Wedge product for association schemes.** M. Muzychuk, "A wedge product of association schemes", *European J. Combin.* 30(3) (2009) 705–715. *Read level: abstract and metadata via secondary records; full text not read.* It owns the construction at scheme level. I could not confirm whether it contains a recognition (decomposition) criterion. No necessary-and-sufficient statement surfaced in its abstract.
- **Schur-ring origin.** K.H. Leung and S.H. Man (wedge product of Schur rings over cyclic groups, 1990s), and Evdokimov–Ponomarenko ("generalized wreath product"). *Read level: cited via secondary sources only.* These own the group-ring case.
- **Wreath product of table algebras, and the reversed-dual statement in the wreath case.** B. Xu, "On wreath products of C-algebras, table algebras, and association schemes", *J. Algebra* 344 (2011) 268–283, DOI 10.1016/j.jalgebra.2011.07.001. *Read level: metadata only (Crossref, MaRDI); abstract and paywall not accessible.* Secondary search snippets attribute to an earlier reference the theorem that the dual of a wreath product of table algebras with table-algebra duals is the reverse-order wreath product of the duals. Xu 2011 is the most likely owner, but I did not verify that from the primary source. If it is, then T2 is owned in the special case where the wedge product is a wreath product (trivial homomorphism).
- **Wreath product definition for table algebras.** H.I. Blau, "Table algebras", *European J. Combin.* 30(6) (2009) 1426–1455 (Def. 1.2, per citing literature). *Read level: citation only.*
- **Supercharacter-theory wedge products.** A.O.F. Hendrickson, constructions of supercharacter theories corresponding to Schur-ring products (around 2012). *Read level: cited via secondary sources only; I could not confirm the exact date or title.* This owns a group-based case.
- **Duals of commutative table algebras.** The question of when the dual of a commutative table algebra (in general only a C-algebra) is a table algebra is a standing question from Bannai–Ito, *Algebraic Combinatorics I* (1984). *Read level: secondary report.*

What I searched: "wedge product" / "generalized wreath product" / "wreath product" × table algebra / C-algebra / association scheme / Schur ring; the dual of a wreath or wedge product; recognition criteria. I found **no pre-2015-08-22 source** that defines the wedge product at the level of table algebras, that gives T1 for table algebras, or that states T2 for the wedge product in general.

What makes it UNCLEAR rather than NOVEL:
1. Three primary sources were not read in full (Muzychuk 2009, Xu 2011, Blau 2009). A recognition criterion at scheme level in Muzychuk 2009, or a characterisation in Xu 2011, would reduce T1 to a routine transcription.
2. The hostile reading is that D, T1 and T2 transcribe the scheme-level wedge product (Muzychuk) and the table-algebra wreath dual (Xu) into the axiomatic setting. An expert in table algebras may call that the expected generalisation.

The statements themselves appear not to be in print.

**Correctness.** The seed contains no proofs, so nothing could be verified. The hypotheses are under-specified: the wedge product needs closed subsets (with normality and a homomorphism or compatibility condition), and the seed states none of them. A referee would need the exact hypotheses of T1 and T2. I found no evidence that any claim is false.

### Applied Verdict: not evaluated (no methodology claimed; pure algebraic combinatorics)

### Contribution Type Verdicts (mode=full):

**Type 1 (New theorem): UNCLEAR.**
- The bar has two parts: the statement is not known or folklore, and the proof is non-routine.
- The first part is provisionally met. T1 and the general-wedge case of T2 were not found before the audit date.
- The second part cannot be assessed: there are no proofs, and the closest owners (Muzychuk 2009, Xu 2011) were not read in full.
- If Xu 2011 contains a characterisation of wreath products of table algebras, T1 may be a direct extension of it.
- Resolution needs a primary read of Xu 2011 §§ on duals and recognition, and of Muzychuk 2009 for any recognition criterion.

**Type 3 (Unifying framework): FAIL.**
- The bar is method transfer between previously unrelated domains.
- Association schemes (through their Bose–Mesner algebras) are already standard table algebras, and table algebras were built to abstract them.
- Lifting a scheme construction to table algebras, then specialising back to "consequences for association schemes", is a generalisation within one field. It does not move a technique from domain A to an unrelated domain B.
- Schur rings and supercharacter theories already sit inside this hierarchy, and their wedge products were already related (Evdokimov–Ponomarenko, Muzychuk, Hendrickson).
- No concrete method transfer is exhibited.

### Cross-reference

The ingredients are owned: the construction at scheme level (Muzychuk 2009) and, very probably, the reversed-dual theorem in the wreath case (Xu 2011). The possible contribution is a correct generalisation to table algebras with two theorems (T1, T2) not found in earlier literature. That is a Type 1 question only. Type 3 is a mis-declared type: generalisation is not unification.

### Recommendation

**Needs deeper audit**, scoped to Type 1 only. Before Phase 3, read Xu 2011 and Muzychuk 2009 in full, and pin down the exact hypotheses of T1 and T2.
- If T1 or T2 reduces to a transcription of those papers, **park** (Type 1 fails as a routine consequence; Type 3 already failed).
- Type 3 is evaluated and FAILS: no method transfer.

**Bearing on the programme's why** (one line): an algebraic gluing of a fine local structure into one class of a coarse one is a lens on "local views adding to one world". There is no bridge here beyond analogy.

### Referee estimate: ACCEPT-LIKELY
Venue class: research journal (specialist algebraic-combinatorics or algebra journal, mid-tier)
Value carried by: factor 1 (new theorems: the recognition criterion and the dual of the wedge product, generalising Muzychuk 2009 and Xu 2011)
Main risk a referee would raise: incremental. This is a routine lift of Muzychuk's scheme-level wedge product and of Xu's wreath-product duality to table algebras, and the reversed-dual statement is already known in the wreath case.

**Dates of sources.** All cited works are dated 1984–2012, before 2015-08-22. Two points were uncertain:
- the exact date and title of Hendrickson's work (around 2012, believed to predate the audit date);
- whether Xu 2011 is the uncited "earlier source" behind the reversed-dual wreath theorem (attribution inferred from snippets of later papers, which were not used as evidence of content).
