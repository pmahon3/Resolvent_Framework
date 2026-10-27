## Audit: seed.md, a new proof of the ASM enumeration via square ice / six-vertex DWBC (mode: full)

Audit date per AS_OF.md: **1995-12-31**. Only sources dated on or before that day count as prior art. The submission's own text and any later version of it are excluded. Web searches were run 2026-10-26, and later sources were used only to identify and date earlier work. Read levels: **A** = abstract or listing page; **S** = secondary report of the content, with the primary source not read; **R** = recalled from background knowledge and not re-read in this audit.

### Declared contribution type(s): Type 2 (new proof), Type 3 (unifying framework)
The seed declares its types but does not state the per-type bars it commits to clearing, as framework Phase 1 asks. This is a minor procedural gap.

### Pure Verdict: KNOWN (the theorem), with the proof route not found in prior art
Stripped of vocabulary, the statement is: #ASM(n) = ∏_{k=0}^{n-1} (3k+1)!/(n+k)!. The claim is a re-proof.

Prior art as of 1995-12-31:
- **Mills, Robbins, Rumsey (1983)**, J. Combin. Theory A 34, "Alternating sign matrices and descending plane partitions". This is the source of the conjecture. [R]
- **Zeilberger**, "Proof of the alternating sign matrix conjecture", arXiv:math/9407211, submitted 1994-07-02. The Electronic Journal of Combinatorics page gives a publication date of 1995-07-25 (cited as EJC 3(2) 1996, R13). This is the combinatorial (constant-term / generating-function) proof that the seed acknowledges. [A, arXiv listing + EJC page]. **The theorem is KNOWN.**
- **Robbins & Rumsey (1986)**, "Determinants and alternating sign matrices", Adv. Math. 62. Later literature credits it as the first description of the ASM ↔ square ice bijection. [S, via Colomo–Pronko arXiv:2509.14006. That source is post-date and was used only for attribution; the 1986 paper was not read.]
- **Elkies, Kuperberg, Larsen, Propp (1992)**, J. Algebraic Combin. 1, 111–132 and 219–234 (arXiv:math/9201305, 1991/92). It gives the ASM / domino / square-ice correspondence, and Part II discusses Lieb's square ice. [A]
- **Lieb (1967)**, Phys. Rev. Lett. 18, the residual entropy of square ice, with periodic boundary and not DWBC. [R]
- **Korepin (1982)**, Comm. Math. Phys. 86, 391. It introduced the six-vertex model with domain-wall boundary conditions and gave recursions that determine Z_n. [S]
- **Izergin (1987)**, Dokl. Akad. Nauk SSSR 297, 331. It gives the determinant formula solving Korepin's recursions. [S. The original was not read, and its content was confirmed through secondary sources only.]

The ingredients are all owned. The encoding is Robbins–Rumsey and EKLP. The determinant is Izergin–Korepin. The Yang–Baxter equation is Baxter's (1982 book, [R]). I searched for an evaluation of the Izergin–Korepin determinant at the "combinatorial point" (q a cube root of unity, which gives weight 1 per configuration) that yields the ASM count, and found none dated on or before 1995-12-31. The **assembly**, meaning this route to this enumeration, is not found in prior art. The theorem itself is not new.

**Gap a hostile referee would press:** the seed says "a determinant evaluation … determines the enumeration" but does not say *how*. The Izergin–Korepin determinant becomes 0/0 in the homogeneous limit, and evaluating it at the combinatorial point is the entire technical content. Correctness cannot be checked from the seed.

### Applied Verdict: not evaluated (Type 7 not claimed; pure-mathematics item)

### Contribution Type Verdicts (mode=full only):

**Type 2 (New proof of known result): PASS, conditional on the determinant evaluation being correct.**
- (b) *Unexpected connection between fields:* yes. The connection is not the bijection itself, which is owned by Robbins–Rumsey and EKLP. It is that the *integrability machinery* of statistical mechanics (Yang–Baxter, the Izergin–Korepin determinant) gives exact enumeration. Before this, the bijection was used combinatorially. Nothing found before 1995-12-31 uses the solvable-model toolkit to count ASMs.
- (c) *Substantial simplification:* yes, if the claim of shortness holds. Zeilberger's proof is long, and per his own page it needed more than two years and more than eighty checkers. A short proof is a clear gain.
- (a) *Technique applicable elsewhere:* plausible, and the seed itself points to symmetry classes. Robbins' symmetry-class conjectures were circulating, but I **could not establish a dated pre-1996 source for them**, so I cannot check this part against the record.

**Type 3 (Unifying framework): PASS (narrow), on the method-transfer criterion. The unification itself is owned.**
- The object-level identification (ASM = DWBC square-ice configuration) is prior art (Robbins–Rumsey 1986; EKLP 1992), so it cannot be claimed.
- The bar asks for *method transfer, demonstrated concretely*, and the seed does this. A technique from domain A, the integrable six-vertex model, settles a problem in domain B, ASM enumeration. That is transfer, not analogy, and the symmetry-class remark suggests the transfer repeats.
- Caveat: much of the Type 3 credit overlaps with Type 2(b). If Type 3 is read as a *new* framework, it fails, because the framework is Robbins–Rumsey/EKLP + Korepin–Izergin. Credit the transfer, not the framework. The symmetry-class part must be **delivered** (at least one class enumerated) for Type 3 to stand independently of Type 2.

### Cross-reference
Every component is known: the theorem, the bijection, the determinant and Yang–Baxter. The **assembly** is new: integrable-model methods yield the enumeration. Type 2 carries the item, and Type 3 survives only as "demonstrated method transfer," not as a new framework. Everything hinges on the unspecified homogeneous-limit evaluation at the combinatorial point.

### Recommendation
**Proceed to Phase 3, scoped to Type 2**, with Type 3 secondary and contingent on a worked symmetry class. Before drafting:
1. write out the determinant evaluation in full and verify it independently;
2. credit Robbins–Rumsey (1986) and EKLP (1992) for the bijection, Korepin (1982) and Izergin (1987) for the determinant, and Zeilberger (1994/95) for the first proof;
3. pin down a dated source for the symmetry-class conjectures.

**Bearing on WHY.md (one line):** this item is a case of composition. A locally checked rule (the ice rule at each vertex) together with a global boundary condition yields a global count via a local relation (Yang–Baxter). It is a lens on local-to-global, with no claim beyond that.

### Referee estimate: ACCEPT-LIKELY
Venue class: research journal (or a short-note / letters-style research venue; a short, high-impact re-proof fits either)
Value carried by: factor 2 (a markedly shorter, different-technique proof of a known enumeration, using a different model), with factor 3 as a secondary contribution if the symmetry classes are delivered
Main risk a referee would raise: whether the Izergin–Korepin determinant's evaluation at the combinatorial point (the homogeneous limit) is actually carried out correctly. The seed asserts this step and does not show it, together with full crediting of the Robbins–Rumsey/EKLP bijection.

### Sources (searched 2026-10-26)
- arXiv:math/9407211 (Zeilberger), listing, dated 1994-07-02 [A]: https://arxiv.org/abs/math/9407211
- EJC v3i2r13 page, publication date 1995-07-25 [A]: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v3i2r13
- EKLP Parts I/II, JACO 1 (1992) [A]: https://emis.univie.ac.at/journals/JACO/Volume1_2/x9m7n00g384067u3.html ; https://emis.univie.ac.at/journals/JACO/Volume1_3/r261p9652890q1j7.html ; arXiv:math/9201305
- Korepin 1982 / Izergin 1987, via secondary sources [S]: https://m.mathnet.ru/eng/znsl7319 ; https://ar5iv.labs.arxiv.org/html/2304.01824 (post-date, used for attribution only)
- Robbins–Rumsey 1986 attribution, via secondary source [S]: https://arxiv.org/pdf/2509.14006 (post-date, used for attribution only)
- Excluded as the submission's own work: arXiv:math/9712207.
- Undated or uncertain: whether a written record of Robbins' symmetry-class conjectures predates 1995-12-31 was not established.
