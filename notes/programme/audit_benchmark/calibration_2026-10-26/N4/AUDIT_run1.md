## Audit: seed.md (wedge product of table algebras) (mode: full)

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)

The types are declared, but no per-type bar is stated. The seed does not say what it commits to show for Type 3, i.e. which method transfers, and from where to where. Under the framework, this alone makes the Type 3 claim not ready.

### Pure Verdict: KNOWN

**Stripped statement.** The seed makes four claims.
- (i) Muzychuk's wedge product of association schemes extends to (standard) table algebras.
- (ii) There is an iff criterion for a table algebra to decompose as a wedge product of two table algebras.
- (iii) Let A and B be commutative table algebras whose character-duals are table algebras. Then the dual of A∧B is a table algebra, and it is isomorphic to B̂∧Â.
- (iv) Applications to association schemes.

**Most damaging source.** J. Bagherian, "On the wedge product of table algebras and applications to association schemes", arXiv:1508.05604 (v1 23 Aug 2015, v2 7 Sep 2015; v3/v4 2018 withdrawn, no reason stated, no journal ref).
- Its abstract states (i)–(iv) almost word for word. The seed paragraph is in effect a paraphrase of that abstract.
- The criterion (ii) and the dual theorem (iii) are both announced there.
- Read level: **abstract** (arXiv abs page, v2). The PDF was fetched but could not be text-extracted inside the audit sandbox. Theorem numbers are therefore not verified.

**Supporting owners.**
- **J. Bagherian, arXiv:1509.06046** (2015; withdrawn 2018). Determines the irreducible representations of a wedge product of table algebras from those of the factors, and gives further iff conditions for being a wedge product. Read level: **abstract** plus the arXiv comments field.
  - The comments field says that **Blau later calls this construction the "partial wreath product of table algebras" and studies it more generally for C-algebras**.
  - So the table-algebra construction is also owned, more generally, by H. I. Blau's partial wreath products (C-algebra level).
  - Read level for Blau: **snippet** (author's withdrawal comment). Further indirect evidence is Antonou's 2014 NIU thesis (advisor Blau), whose abstract uses "partial wreath product (B, D, C)" of table algebras. Read level: **abstract**. The exact Blau paper was not located.
- **M. Muzychuk, "A wedge product of association schemes", European J. Combin. 30 (2009) 705–715.** Owns the association-scheme case, i.e. the special case behind (iv). It credits the S-ring version to Leung–Man and the external version, under the name "generalized wreath product", to Evdokimov–Ponomarenko. Read level: **snippet** (abstract as quoted in search results).
- **B. Xu, "On wreath products of C-algebras, table algebras, and association schemes", J. Algebra (2012), DOI 10.1016/j.jalgebra.2011.07.001.** Owns the wreath-product special case: the wedge product with the trivial homomorphism, per Bagherian. Read level: **snippet** (MaRDI metadata only).
- **Unverified lead.** For S-rings over abelian groups, duality reversing the order of a generalized wreath product (Evdokimov–Ponomarenko school) may already own the S-ring shadow of (iii). It was searched but not confirmed. Read level: none.

**Hostile assessment.**
- (i)–(iv) are explicitly stated in a 2015 preprint, so the claim is KNOWN.
- The construction itself is also absorbed into Blau's more general partial wreath product for C-algebras.
- Bagherian's withdrawal is a caution flag on correctness, not evidence of novelty. Withdrawn preprints still establish priority of the statement, and Blau's later work owns the construction.
- If the seed author *is* Bagherian, the seed re-submits a withdrawn result without addressing why it was withdrawn. Nothing in the seed engages Blau's generalisation.

### Applied Verdict: not evaluated (Type 7 not claimed; pure algebraic combinatorics, no computational component)

### Contribution Type Verdicts (mode=full only):

**Type 1 (New theorem): FAIL.**
- The bar is "not known". The construction, the iff criterion and the reversed-dual theorem are all stated in Bagherian arXiv:1508.05604 (abstract).
- The construction is generalised by Blau's partial wreath product of C-algebras.
- Neither the criterion's proof nor its statement adds anything visible beyond these sources.

**Type 3 (Unifying framework): FAIL.**
- The bar is method transfer. Lifting a scheme-level construction (Muzychuk 2009) to table algebras is the standard move of this literature: Xu 2012 already did it for wreath products, and Blau goes further, to C-algebras.
- The seed names no technique that becomes available in a new domain because of the framework.
- The "applications to association schemes" run back along the forgetful direction. They specialise to Muzychuk's setting, with no transfer demonstrated.
- No per-type bar was declared.

**Undeclared types.** A Type 6 framing (exposition of the wedge product for the table-algebra audience) would also fail. The material is accessible in Muzychuk 2009, Xu 2012 and Blau's work.

### Cross-reference
- Both the components and the assembly are owned.
- The seed is not "known pieces, novel assembly". The assembly itself (wedge product at table-algebra level, plus the duality theorem) is the content of an existing preprint, and it was subsequently generalised.
- No owned region is left for Type 3 to claim.
- **owned_by:**
  - Bagherian arXiv:1508.05604: region = wedge product of table algebras, iff decomposition criterion, reversed-dual theorem. Verified at abstract level.
  - Blau, partial wreath product: region = the same construction for C-algebras. Verified at snippet level via 1509.06046's comment.
  - Muzychuk EJC 2009: region = association-scheme case. Snippet level.
  - Xu J. Algebra 2012: region = wreath special case. Snippet level.

**WHY.md bearing (one line).** Gluing an algebra from a "local" factor and a quotient is a composition-not-circle construction. It bears on the question only as a lens: it says nothing about local views failing to cohere.

### Recommendation
**PARK.**
- Evaluated: Type 1 (FAIL: known, Bagherian 2015 / Blau) and Type 3 (FAIL: no method transfer, no bar declared).
- No open-question status: no precise open problem is formulated.
- If revived, the only possible residue is the following. Find out why 1508.05604 was withdrawn, and check whether the reversed-dual theorem (iii) is false or unproved as stated in Blau's C-algebra generality.
  - That requires full-text reads of 1508.05604 v2 and Blau's partial-wreath-product paper.
  - Neither was available here at full-text level.
