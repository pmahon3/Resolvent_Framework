## Audit: seed.md — "R(k) ≤ (4 − ε)^k via a book algorithm" (mode: full)

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)
The types are declared, but the seed does not say what bar it commits to clearing. For Type 3 it also names no domains being unified.

### Pure Verdict: KNOWN
**What the statement actually says, with the vocabulary stripped:** there is an absolute ε > 0 such that R(k) ≤ (4 − ε)^k for all large k. The proof uses an iterative "book algorithm" that builds large monochromatic books, and its analysis bounds the number of bad steps (density-boost and big-blue steps).

This is exactly the main theorem of:

- **Campos, Griffiths, Morris, Sahasrabudhe, "An exponential improvement for diagonal Ramsey", arXiv:2303.09521 (2023; v2 Aug 2025); Annals of Mathematics (article page annals.math.princeton.edu/articles/22181).** Read level: abstract in full, plus the arXiv HTML v2 for roughly the first 100k of 186k characters (§1–§7; §8 onwards not read).
  - **Theorem 1.1:** "There exists ε>0 such that R(k) ⩽ (4−ε)^k for all sufficiently large k." Two proofs are given, one with ε = 2^(−10) and one with ε = 2^(−7).
  - **§3, "The Book Algorithm":** its steps are degree regularisation, big blue step (finds a blue book), central vertex, red step and density-boost step. This matches the seed's "book algorithm … finds large monochromatic books".
  - **Bounds on the bad steps:** Lemma 4.3 (|𝓑| ⩽ ℓ^{3/4} big blue steps), Lemma 7.5 (immoderate density-boost steps), and §8 Zigzag Lemma (total density-boost steps). This matches the seed's "careful analysis … bounds the number of 'bad' steps".
  - **Prior work cited there:** Erdős–Szekeres 1935 (4^k), Thomason 1988, Conlon, and Sah (4^{k−c(log k)^2}).

The seed matches CGMS in statement, in method name and in proof architecture. It is a restatement of a published theorem, not an independent result.

**Further owners of the same region:**
- **Gupta, Ndiaye, Norin, Wei, "Optimizing the CGMS upper bound on Ramsey numbers", arXiv:2407.19026 (2024).** Read level: search snippets / abstract-level only. It gives R(k) ≤ 3.8^{k+o(k)}, which is strictly stronger than the seed's claim. It replaces the book algorithm with a simpler inductive statement and extends to the off-diagonal and multicolour cases.
- **Formal verification already exists:**
  - Mehta, Lean formalisation of CGMS. Read level: snippet only (Cambridge talk listing).
  - Paulson, Isabelle/HOL, AFP entry "Diagonal_Ramsey" (2025) and an ITP 2025 paper. Read level: snippet only.

  So the seed cannot claim novelty of the formalisation either.

**Factual error in the seed:** "The Erdős–Szekeres bound … has stood as the exponential rate since then" stopped being true in March 2023.

### Applied Verdict: not evaluated (N/A)
The seed claims no Type 7 / methodology contribution, and there is no computational component. The practitioner test does not apply.

### Contribution Type Verdicts (mode=full only):

**Type 1 (new theorem): FAIL.** The statement is known: it is CGMS Theorem 1.1 (arXiv:2303.09521, Annals), and Gupta–Ndiaye–Norin–Wei 2024 has since improved it to 3.8^k. The method (the §3 book algorithm with bad-step counting) is also CGMS's. Nothing in the seed exceeds the published result.

**Type 3 (unifying framework): FAIL.**
- The seed names no two previously unrelated domains.
- It demonstrates no method transfer.
- A "density-increment-like procedure" is an analogy to density-increment arguments (Roth/Szemerédi type), not a transfer. The seed does not show any technique from a domain A becoming applicable in a domain B.
- The only transfers this method has actually achieved are to off-diagonal and multicolour Ramsey bounds. Those are owned by Gupta–Ndiaye–Norin–Wei 2024 (snippet level) and by later CGMS-school work.

**Types 2, 4, 5 and 6 were not claimed, so they were not evaluated.** Checked briefly anyway:
- **Type 2:** fails, because the seed describes the same proof, not a different one. The simplification that does exist (an inductive replacement for the algorithm) belongs to Gupta–Ndiaye–Norin–Wei.

### Cross-reference
- **Pure audit vs Type 1:** both give KNOWN. The theorem, the constant regime and the proof architecture all coincide with CGMS 2023.
- **Type 3:** has no content to assess beyond an analogy.
- **Applied:** there is no applied angle to rescue the seed.
- **Overall:** no component is novel, and the assembly is not novel either. The seed reproduces a landmark 2023 result whose bound has already been improved twice and which has been formalised in both Lean and Isabelle.
- **Bearing on WHY.md** (WHY.md is not in this directory, so this is judged from the summary in the task context): none. The seed is extremal combinatorics with no local-to-global gluing question.

### Recommendation
**PARK (KNOWN).**
- **Types evaluated:** 1 and 3. Type 1 fails as a known theorem (CGMS 2023, Thm 1.1, §3 Book Algorithm). Type 3 fails because there is no method transfer, only the density-increment analogy.
- **Not an open question:** the claimed statement is resolved, and a stronger bound is published.
- **Housekeeping:** correct the seed's historical claim before archiving it in covered_leads.

**Sources:**
- https://arxiv.org/abs/2303.09521
- https://arxiv.org/html/2303.09521v2
- https://annals.math.princeton.edu/articles/22181
- https://arxiv.org/html/2407.19026v1
- https://isa-afp.org/entries/Diagonal_Ramsey.html
- https://talks.cam.ac.uk/talk/index/210400/
