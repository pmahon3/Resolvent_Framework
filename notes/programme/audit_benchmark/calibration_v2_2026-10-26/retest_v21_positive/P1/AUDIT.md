## Audit: seed.md — "R(k) <= (4 - eps)^k via a book algorithm" (mode: full)

Audit date (per AS_OF.md): **2023-03-22**. Only sources dated on or before 2023-03-22 are used as
prior art. The seed's own work, under any title or author, is the submission and was excluded. Search
hits for it and for later work were seen and **not used**: arXiv 2303.09521 (abstract and listings),
the Annals 2026 listing, the Isabelle AFP entry, FoCM 2023 abstracts, IBS/Bristol/Oxford seminar
pages, and Gupta–Ndiaye–Norin–Wei arXiv 2407.19026 (2024).
Date uncertainty: none material. Every cited source below carries an arXiv YYMM identifier or a
journal date that is clearly before 2023-03-22.

Search mode: standard web search, plus full-text fetches through ar5iv. Searches ran on 2026-10-27,
using the 2023-03-22 cut-off.

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)
The seed does **not** state per-type bars. It lists "1, 3" but never says what it commits to
demonstrating for each, which contribution_evaluation.md §Phase 1 requires. This is a procedural gap.
It is noted here, not treated as fatal.

### Pure Verdict: NOVEL (as of 2023-03-22; conditional on correctness, which the seed cannot show)

**Stripped statement.** There is an absolute ε > 0 with R(k,k) ≤ (4−ε)^k for all large k. This is an
exponential improvement in the base of the Erdős–Szekeres bound R(k+1,k+1) ≤ C(2k,k) = Θ(4^k/√k). The
words "book algorithm" and "density-increment-like" describe the method only. The statement uses no
new vocabulary.

**Prior work, all predating 2023-03-22. Each improves only the subexponential factor; the base stays
at 4:**
| Source | Date | Bound | Read level |
|---|---|---|---|
| Erdős–Szekeres, Compositio Math. 2 (1935) | 1935 | C(2k,k) | known via secondary statements (CFS 2015 §2.1, Sah 2020 intro, Conlon 2006 intro); primary not opened |
| Thomason, J. Graph Theory (1988) | 1988 | k^{-1/2+A/√log k}·C(2k,k) | secondary (Conlon 2006 intro, CFS 2015 §2.1); primary not opened |
| Conlon, "A new upper bound for diagonal Ramsey numbers", arXiv math/0607788 (30 Jul 2006); Ann. Math. 170 (2009) 941–960 | 2006/2009 | k^{-C log k/log log k}·C(2k,k) | **full text (ar5iv HTML), intro + method sections, via fetch-model summary**, 2026-10-27 |
| Sah, "Diagonal Ramsey via effective quasirandomness", arXiv 2005.09251 (19 May 2020); Duke Math. J. 172(3), 15 Feb 2023 | 2020/2023-02-15 | e^{-c(log k)^2}·C(2k,k) | **full text (ar5iv HTML), intro + method + barrier discussion, via fetch-model summary**, 2026-10-27 |
| Conlon–Fox–Wigderson, "Ramsey numbers of books and quasirandomness", arXiv 2001.00407 (Jan 2020); Combinatorica 42 (2022) | 2020/2022 | book Ramsey numbers; no new R(k) bound | **full text, first ~100k of ~163k characters (intro and main theorems), via fetch-model summary**, 2026-10-27 |
| Conlon–Fox–Sudakov, "Recent developments in graph Ramsey theory", Surveys in Combinatorics 2015, arXiv 1501.02474 | 2015 | survey; §2.1 upper bounds | **full text, first ~100k of ~192k characters (§2.1 read), via fetch-model summary**, 2026-10-27 |

**Hostile checks.**
1. *Already known?* No pre-cut-off source gives an exponential saving. CFS 2015 §2.1 lists the
   upper-bound history (Erdős–Szekeres, Rödl, Thomason, Conlon), and every entry keeps base 4.
   CFW 2020's introduction says the bounds 2^{r/2} ≤ r(K_r) ≤ 4^r "have remained almost unchanged since
   1947". Sah 2020 says the optimality of its quasirandomness estimates "represents a natural barrier"
   and that "new ideas will be required". A hostile search for a 2021–early-2023 base improvement
   (queries: "r(k,k)", "Erdős–Szekeres improvement", "base 4", "(4−ε)^k") returned no pre-cut-off
   claim. The only hits were the submission itself and later work, which are excluded.
2. *Folklore or a trivial consequence?* No. Sah 2020 argues that the Thomason–Conlon–Sah
   quasirandomness-plus-induction framework hits a barrier at e^{-c(log k)^2}, so standard techniques
   do not yield an exponential saving.
3. *Method anticipated?* **Partly.** CFW 2020 explicitly proposes the route through books. A coloring
   with no monochromatic K_r has no monochromatic book B_n^{(k)} with n = r(K_r, K_{r−k}), so
   r(K_r) ≤ r(B_n^{(k)}). CFW write that "one might hope for an exponential improvement on r(K_r)" if
   book Ramsey numbers match the random bound with strong error control. They do not carry this out:
   they prove only a slowly decaying error term, and their proofs are regularity- or counting-based,
   not algorithmic. Conlon 2006 also used book-type and quasirandom counting ideas. The *strategy*
   "find large monochromatic books to beat 4^k" therefore has a pre-cut-off owner. The *theorem* does
   not, and neither does an algorithmic book-finding procedure that controls the number of bad steps.
4. Textbook check: Graham–Rothschild–Spencer, *Ramsey Theory* (2nd ed., 1990), states the
   Erdős–Szekeres bound. This was not opened in this audit; it is cited from background knowledge, so
   its read level is **not read**.

Verdict NOVEL: the nearest prior works (Sah 2020, Conlon 2006, CFW 2020) were read beyond abstract
level, and none contains the statement. **Correctness cannot be assessed.** The seed contains no proof,
only a three-sentence sketch, so "a careful analysis bounds the number of bad steps" is unverified.

### Applied Verdict: FAIL / not applicable
This is a pure existence bound with no computational or practitioner claim. The decision test
(does it change what a practitioner does?) has nothing to act on. The "algorithm" is a proof device,
not a method offered for use. No Type 7 claim was made.

### Contribution Type Verdicts (mode=full):

**Type 1 (New theorem): PASS (conditional on the proof checking out).**
Bar: not known, not folklore, not a trivial consequence, non-routine proof. The statement is absent
from all pre-cut-off literature found. The standard framework is documented to stall short of an
exponential saving (Sah 2020), so the proof cannot be routine. The condition is that the proof, which
the seed lacks, must be verified.

**Type 3 (Unifying framework): FAIL.**
Bar: a demonstrated method transfer from domain A to domain B. The seed's only gesture is the word
"density-increment-like". That is an analogy to density-increment arguments (Roth/Szemerédi type), and
the seed shows no technique carried across, no previously unrelated results unified, and no new
application of the framework outside this one bound. "These look alike" without "therefore this
technique applies here" is the park condition stated in the bar. A future write-up might show that the
book algorithm transfers, for example to off-diagonal or multicolour Ramsey bounds. The seed does not
show this, and it is not counted here.

No undeclared types are implicitly claimed. Type 2 does not apply because the result is new, not a
re-proof.

### Cross-reference
This is a novel theorem, not a framework contribution. The method's high-level strategy (books →
exponential improvement) was publicly proposed in CFW 2020, so the novelty lies in the result and in
executing that strategy (the algorithm plus the bad-step count), not in the idea of using books.
Type 1 carries the seed on its own; Type 3 adds nothing and should be dropped from the claim.
WHY.md is not present in the audit directory, so the one-line "bearing on the why" note is omitted.

### Recommendation
**Proceed to Phase 3, scoped to Type 1 only.** Drop the Type 3 claim. Before drafting:
(a) state the per-type bar explicitly;
(b) credit Conlon–Fox–Wigderson 2020 for the books route to an exponential improvement, and credit
Thomason 1988, Conlon 2009 and Sah 2020 (Duke 2023) for the subexponential savings;
(c) the full proof must be independently verified. The seed is a sketch, and the central claim stands
or falls on the bad-step analysis.

### Referee estimate: ACCEPT-LIKELY (conditional on the proof being correct)
Venue class: research journal (top general venue; the result settles a base that stood since 1935)
Value carried by: factor 1 (a sharp improvement of a famous bound: the first exponential saving over
Erdős–Szekeres)
Main risk a referee would raise: correctness of the book algorithm's bad-step count and the
density-increment analysis, which cannot be checked from the seed. A secondary risk is missing credit
to CFW 2020 for the books strategy.

**Caps check.**
- Cap 1 (pure verdict UNCLEAR → at most BORDERLINE): not engaged, because the verdict is NOVEL.
- Cap 2 (ACCEPT-LIKELY needs the nearest prior read beyond abstract): satisfied. Sah 2020 and
  Conlon 2006 were read through the intro and method sections. CFW 2020 and CFS 2015 were read in part
  (the first ~100k characters each).
- Cap 3 (owner in print, uncredited → REJECT-LIKELY): not engaged. No owner of the theorem was found.
  The CFW strategy-level anticipation is a crediting issue, not an owner of the main result.
- Entry-level theory-item cap (v2.1): not applicable. The target is a seed, not a taxonomy entry.
