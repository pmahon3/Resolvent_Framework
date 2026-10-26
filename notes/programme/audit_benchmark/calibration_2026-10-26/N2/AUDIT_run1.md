## Audit: seed.md (generalised Cameron–Erdős for non-translation-invariant linear equations) (mode: full)

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)

The seed declares types but states no per-type bar it commits to clearing (the framework's Phase-1 requirement). It is also very short: it gives no conjecture statement, no class of equations, and no theorem statement. This is a readiness defect noted in addition to the verdicts below.

### Pure Verdict: KNOWN

**The statement with the vocabulary stripped out.** Let L be a homogeneous linear equation over Z in k ≥ 3 variables, not translation-invariant (coefficients do not sum to 0). Let f(n,L) be the number of L-free subsets of [n], and μ_L(n) the size of the largest one. The proposed generalisation of Cameron–Erdős is f(n,L) = Θ(2^{μ_L(n)}). The weak form, for a class of equations whose extremal sets are known, is f(n,L) = 2^{μ_L(n)+o(n)}. The method bounds the number of independent sets in almost-regular graphs.

**Prior art, most damaging first:**

1. **P. Hegarty, "Independent sets in almost-regular graphs and the Cameron–Erdős problem for non-invariant linear equations", arXiv:0905.0990 (v1 May 2009; v2 Sep 2010, withdrawn).** [read level: arXiv abstract and comments field. The PDF did not render as text, so I have not read the body.] Its abstract says what the seed says, almost word for word. It proposes the generalisation to arbitrary non-translation-invariant equations in ≥3 variables. It proves a weak form for a class of equations whose maximum-size solution-free sets were previously characterised, using graph-theoretic methods. The seed reads as a paraphrase of this abstract.
2. **The arXiv withdrawal comment on 0905.0990** says the author withdrew the paper because **its main result (Theorem 2.2) follows from Theorem 9.3 of B. Green, "A Szemerédi-type regularity lemma in abelian groups, with applications", GAFA 15 (2005) 340–376.** [Green: read level is snippet / secondary. I did not read the text of Thm 9.3 directly, because the PDF did not render. The attribution comes from the withdrawal comment and from item 3.] So the weak form was not even new in 2009. It is a consequence of Green's arithmetic regularity and removal machinery.
3. **R. Hancock, A. Treglown, "On solution-free sets of integers", European J. Combin. 66 (2017); arXiv:1607.08399.** [read level: abstract, plus §1.1, §1.2 and Theorem 3/9/20 statements via the ar5iv HTML, first 100k characters.] Theorem 9 credits Green with f(n,L) = 2^{μ_L(n)+o(n)} for **every** homogeneous linear equation L, which is stronger than any weak form restricted to a class. Theorem 3 (proved as Thm 20, §4) proves the **strong**, Θ-form f(n,L) = Θ(2^{μ_L(n)}) for px+qy=z when (i) q ≥ 2 and p > q(3q−2)/(2q−2), or (ii) q = 1 and p ≥ 3. §1.2 records that the Θ-form fails for translation-invariant L (Cameron–Erdős). So the strong conjecture is already partly settled.
4. **P. Hegarty, "Extremal subsets of {1,…,n} avoiding solutions to linear equations in three variables", Electron. J. Combin. 14 (2007) R74.** [read level: secondary, as cited in Hancock–Treglown §1.1.] This is the source of the "extremal solution-free sets already known in size" that the seed relies on, e.g. μ_L(n) = n − ⌊n/(p+q)⌋ for px+qy=z.
5. **R. Hancock, A. Treglown, "On solution-free sets of integers II", Acta Arith. 180 (2017); arXiv:1611.08498.** [read level: abstract.] Further exact μ_L values and counts of maximal L-free sets for px+qy=rz, via Green's container and removal lemmas.
6. **N. Alon, "Independent sets in regular graphs and sum-free subsets of finite groups", Israel J. Math. 73 (1991) 247–256.** [read level: abstract / portal snippet.] The original method that counts independent sets in (near-)regular graphs to count sum-free sets. The seed's technique is this standard route.
7. **B. Green, "The Cameron–Erdős conjecture", Bull. LMS 36 (2004); A. A. Sapozhenko (2003).** [read level: secondary, via Hancock–Treglown §1.2.] Both settle the original conjecture.

**Hostile-referee answers.** Is this a restatement? Yes, of Hegarty 2009. Is it a trivial consequence? Its main result follows from Green 2005 Thm 9.3, according to the original author's own withdrawal. Would an expert call it obvious? An expert would call it known. Green gives the o(n) form for all homogeneous equations, and Hancock–Treglown have since proved the Θ-form for large classes.

### Applied Verdict: not evaluated (no applied or Type-7 claim; the item is pure additive combinatorics)

### Contribution Type Verdicts (mode=full only):

**Type 1 (New theorem): FAIL.** Bar: not known, not folklore, not a trivial consequence. Both the conjecture and the weak theorem are in Hegarty, arXiv:0905.0990. The theorem is subsumed by Green GAFA 2005 Thm 9.3, which by Hancock–Treglown Thm 9 gives f(n,L) = 2^{μ_L(n)+o(n)} for all homogeneous L. The strong form has been proved for large classes (Hancock–Treglown 2017, Thm 3).

**Type 3 (Unifying framework): FAIL.** Bar: concrete method transfer from domain A to domain B. The transfer from graph theory to additive counting, done by bounding independent sets in near-regular graphs, has been standard since Alon 1991 and runs through Sapozhenko, Green, and the container method used by Hancock–Treglown. The seed names no technique that becomes newly applicable, and no previously unrelated results that it unifies. The extension from x+y=z to non-invariant equations is a generalisation, not a unification. It was proposed in 2009 and is now handled by Green's regularity/removal and container methods.

**Undeclared types implicitly in play.** Type 2 (new proof of a known result) would be the only fallback, if the almost-regular-graph argument gave a substantially simpler route than Green's regularity lemma. The seed gives no proof, so this cannot be assessed: UNCLEAR at best. Even then, Hegarty's withdrawn paper is that same route, so the bar would have to be cleared against both Green and Hegarty.

### Cross-reference
This is not a case of known components with a novel assembly. Both the assembly and the headline result are known, and the weak result is subsumed by a stronger, earlier theorem. The Type 3 framing adds nothing beyond the Alon/Sapozhenko/Green method lineage. The seed bears on the programme's WHY question (local views adding up to one world) only as a distant lens: counting configurations that avoid local constraints. It touches no glued-carrier or cycle × infinity seam.

### Recommendation
**Park.** Evaluated: Type 1 FAIL (Hegarty 2009 arXiv:0905.0990, withdrawn because it is subsumed by Green GAFA 2005 Thm 9.3; Θ-form partly proved by Hancock–Treglown EJC 2017 Thm 3). Type 3 FAIL (no method transfer beyond Alon 1991 / Sapozhenko / Green). It is not open-question material: the general Θ-form for all non-invariant L is open, but it is already posed (Hegarty 2009; Hancock–Treglown) and actively pursued. Before any re-entry, read Green GAFA 2005 §9 (Thm 9.3) and the Hegarty v1 PDF body at full text, to confirm the subsumption at primary-source level.
