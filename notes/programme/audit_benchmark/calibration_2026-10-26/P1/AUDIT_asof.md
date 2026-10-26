## Audit: seed.md, "R(k) <= (4 - eps)^k via a book algorithm" (mode: full; audit date 2023-03-22)

Audit date set by AS_OF.md: **2023-03-22**. I treat the seed as the submission. I set aside every source dated after 2023-03-22, as well as the seed's own preprint and its published version (CGMS, arXiv 2303.09521 and later). Searches were run on 2026-10-26 in standard mode. Every item cited below is dated on or before 2023-03-22.

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)

The seed declares its types. It does not state the per-type bars it commits to clearing, which contribution_evaluation.md §"Phase 1 requirement" asks for. This is a minor readiness gap.

### Pure Verdict: NOVEL (as a statement, as of 2023-03-22). Correctness: not assessable from the seed.

**Stripped statement.** There is an absolute eps > 0 such that R(k,k) <= (4 - eps)^k for all large k. No new vocabulary needs stripping. "Book" is standard: B_n^(k) is n copies of K_{k+1} sharing a common K_k.

**Prior art: what was known on 2023-03-22.**
- Erdős–Szekeres, Compositio Math. 2 (1935). R(k+1,l+1) <= C(k+l,k), which gives R(k) <= 4^k. This is the base-4 bound the seed claims to beat. Read level: known classical statement, cited via the Conlon abstract below.
- Thomason, J. London Math. Soc. (1988). R(k+1,k+1) <= k^{-1/2 + o(1)} C(2k,k). This is a polynomial-factor improvement and leaves the base at 4. Read level: snippet (as cited in the Conlon abstract/Caltech record, fetched 2026-10-26).
- Conlon, "A new upper bound for diagonal Ramsey numbers", Annals of Math. 170 (2009) 941–960; arXiv math/0607788, 30 Jul 2006. R(k+1,k+1) <= k^{-C log k / log log k} C(2k,k), a super-polynomial factor but still sub-exponential, so the base stays 4. Read level: abstract.
- Sah, "Diagonal Ramsey via effective quasirandomness", arXiv 2005.09251 (May 2020); Duke Math. J. 172(3), published 15 Feb 2023. R(k+1,k+1) <= exp(-c (log k)^2) C(2k,k). This was the state of the art on the audit date and is the **most damaging prior source**: main theorem (Thm 1.1), base 4. Read level: abstract/snippet.
- Book-Ramsey line, the direct source of the seed's "books" ingredient:
  - Erdős–Faudree–Rousseau–Schelp (1978) posed the book-Ramsey question. Read level: snippet via Conlon 2019.
  - Thomason's book conjecture. Read level: snippet via Conlon 2019.
  - Conlon, "The Ramsey number of books", Advances in Combinatorics 2019:3 (arXiv 1808.03157, Aug 2018). Main theorem: r(B_n^(k)) = 2^k n + o_k(n). Read level: abstract.
  - Conlon–Fox–Wigderson, "Ramsey numbers of books and quasirandomness", Combinatorica 42(3) (2022) 309–363 (arXiv 2001.00407, Jan 2020). Regularity-free proof, and extremal colourings are quasirandom. Read level: abstract.

**Hostile assessment.**
- **Restatement?** No. Every bound before 2023-03-22 (Thomason, Conlon, Sah) improves R(k) only by a sub-exponential factor 4^k / k^{f(k)}. None reaches base 4 - eps.
- **Trivial consequence?** No. Removing the exponential base 4 was a well-known open problem attributed to Erdős, and the Thomason–Conlon–Sah quasirandomness-induction method was known to bottom out sub-exponentially.
- **Folklore?** No known folklore claim of an exponential improvement.
- **Owned ingredients.** "Finding large monochromatic books" is an owned region: Conlon 2019 and Conlon–Fox–Wigderson 2022 for fixed k. The seed's step from books with fixed k to an iterative algorithm that controls "bad" steps for the diagonal problem is not stated anywhere I found.

**Gap.** The seed gives only a one-paragraph sketch. No referee could verify the eps-gain from it, and Type 1's bar requires a non-routine *proof*. So the statement is novel; the correctness of the proof is UNVERIFIED pending the full manuscript.

**Could not tell whether a source predates 2023-03-22.** None. All cited sources carry clear dates before the audit date. The search engine returned later items (CGMS itself, Gupta–Ndiaye–Norin–Wei, a 2026 preprint, an AFP formalization); I excluded them.

### Applied Verdict: not evaluated / not applicable
Type 7 was not claimed and there is no computational or practitioner component. The practitioner test does not apply to a pure extremal bound.

### Contribution Type Verdicts (mode=full only):

**Type 1 (new theorem): PASS (conditional on proof verification).**
Bar: not known, not folklore, not a trivial consequence, proof non-routine. As of 2023-03-22 the statement is unknown: the best bound was Sah 2020/2023, still base 4. It is the first exponential improvement since 1935 and a major result if correct. The condition is that the full proof must be checked. The seed's sketch alone does not establish it.

**Type 3 (unifying framework): FAIL.**
Bar: the framework must enable *method transfer*, with a technique from domain A demonstrably applicable in domain B. The seed describes a single technique (the "book algorithm", a density-increment-like procedure) applied to a single problem. It names no second domain, no unified family of previously unrelated results, and no transfer it carries out. "Density-increment-like" is an analogy to Roth/Szemerédi-type arguments. By the framework's own rule, "these look alike" without "and therefore this technique applies here" does not clear the bar. Possible future transfers (off-diagonal R(k,l), multicolour Ramsey) are not demonstrated in the seed. The book algorithm may well become a transferable *method*, but that would be a Type 2/Type 7-style methodological gain shown later. It is not a unification the seed exhibits.

**Undeclared types the seed gestures at:** none beyond those declared.

### Cross-reference
This is a strong Type 1 claim with a weak Type 3 claim attached. The theorem stands alone, and the "framework" language adds nothing the bar recognises. Following "one contribution per paper", the seed should scope itself to Type 1 and drop Type 3. The owned region is books with fixed k and quasirandom extremal colourings (Conlon 2019; Conlon–Fox–Wigderson 2022). The unowned joint is the iterative book algorithm with bad-step control that yields base 4 - eps.

Bearing on WHY.md: none directly. This is classical extremal combinatorics. The one loose echo is the question of when local colour structure forces global order, a lens and not a link.

### Recommendation
**Proceed to Phase 3, scoped to Type 1 only.** Drop the Type 3 claim.

Before drafting, the full proof needs independent verification, with the analysis of bad steps and the explicit eps as the critical points. A hostile line-by-line check of the book-algorithm analysis is owed. Cite Erdős–Szekeres 1935, Thomason 1988, Conlon 2009, Sah 2020/2023, Conlon 2019 and Conlon–Fox–Wigderson 2022.

Sources (all searched 2026-10-26):
- Conlon 2009: https://annals.math.princeton.edu/2009/170-2/p15 ; https://arxiv.org/abs/math/0607788 ; https://resolver.caltech.edu/CaltechAUTHORS:20190812-162957624
- Sah: https://arxiv.org/abs/2005.09251v1 ; https://projecteuclid.org/journals/duke-mathematical-journal/volume-172/issue-3/Diagonal-Ramsey-via-effective-quasirandomness/10.1215/00127094-2022-0048.full
- Conlon 2019: https://arxiv.org/abs/1808.03157
- Conlon–Fox–Wigderson: https://arxiv.org/abs/2001.00407 ; https://research-explorer.ista.ac.at/record/22174
