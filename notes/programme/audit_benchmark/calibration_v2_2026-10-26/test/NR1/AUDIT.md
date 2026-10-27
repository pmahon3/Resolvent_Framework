## Audit: seed.md (Butson-type matrices: n ∈ ℕq₁+…+ℕq_s) (mode: full)

Audit date (per AS_OF.md): **2007-07-26**. Only sources dated on or before that day count as prior art.

### Declared contribution type(s): Type 1 (new theorem)
The seed names the type but gives no per-type bar statement. Under the framework it is not fully ready for Phase 2. The audit still proceeds.

WHY.md is not in the audit directory. Bearing on the why, one line: none direct. This is a pure finite-combinatorics and number-theory question.

### Pure Verdict: KNOWN (trivial consequence of Lam–Leung, which covers every s)

**Stripped statement.** Let H be n×n with entries that are l-th roots of unity, and with HH* = nI (a Butson Hadamard matrix BH(n,l)). Let p₁,…,p_s be the distinct primes dividing l. Claim: n ∈ ℕp₁+…+ℕp_s. The seed proves this for s = 2 and s = 3 and conjectures it for all s.

**Reading of the seed's notation.** The seed writes "s distinct prime powers q_j^{e_j}" and then states the condition with the bases q_j, which are primes. That is the only reading under which the statement is true. If q_j were read as prime powers, the statement is false: BH(2,4) exists (the real 2×2 Hadamard matrix), but 2 ∉ 4ℕ.

**Two-line derivation from known results.**
1. For rows i ≠ j, the (i,j) entry of HH* = nI gives Σ_k h_ik·conj(h_jk) = 0. Each term is an l-th root of unity, so this is a vanishing sum of exactly n l-th roots of unity.
2. Lam–Leung's theorem: the weight set W(l) of vanishing sums of l-th roots of unity equals ℕp₁+…+ℕp_s. Hence n ∈ ℕp₁+…+ℕp_s, **for every s**.

So the s = 2 and s = 3 results are special cases, and the "conjecture for every s" was already a theorem before 2007-07-26. Lam–Leung is not credited in the seed. The s = 1 "standard divisibility fact" is the prime-power case of the same theorem.

**Sources (read level, date):**
- T. Y. Lam, K. H. Leung, *On vanishing sums of m-th roots of unity in finite fields*, arXiv:math/9605216, submitted **2 May 1996**. Read level: abstract (arxiv.org/abs) plus introduction (via ar5iv). Its Thm 1.1 states: for m = p₁^{a₁}⋯p_r^{a_r}, W(m) = ℕp₁+⋯+ℕp_r, called "the principal result in [LL]". Caveat: ar5iv renders the current arXiv version, and I could not confirm whether a later version exists. The 1996 abstract itself says the characteristic-0 weight set was already determined in "an earlier work".
- [LL] = T. Y. Lam, K. H. Leung, *On vanishing sums for roots of unity*, **MSRI preprint 1995-082 (1995)**. Read level: listing page only (title, authors, year). Text not read. The abstract page was unreachable (connection refused).
- Same authors and title, *J. Algebra* 224 (**2000**) 91–109. Read level: bibliographic detail **recalled, not verified online**. Searches did not reach the ScienceDirect or MathSciNet page.
- Unverified older lead for s = 2: N. G. de Bruijn (1953), on cyclic-group factorization and vanishing sums with two prime divisors (and related work of Rédei and Schoenberg). Not checked. It is not needed for the verdict.

**Excluded as the seed's own work, or as post-dating 2007-07-26:**
- arXiv:0707.4175, *On Hadamard matrices at roots of unity*. Search snippet: Thm 7.2 gives the condition for at most three prime factors. The arXiv number (July 2007) and the content match the seed, so it is treated as the submission itself and ignored.
- Every other hit is post-dated and was not used as prior art: Winterhof–Yayla–Ziegler (arXiv:1407.6548, 2014), Kumar–Kumar (arXiv:1503.07281, 2015), Sivek (2010), arXiv:0901.2331, 1707.02287, 1903.09824, the Schmidt BH note (undated, almost certainly later), ALCO 2020, and Czifra–Matolcsi–Szőllősi (arXiv:2511.11230). Some of these quote the Lam–Leung theorem. I used them only to locate the result, and the verdict rests on the 1996 preprint.

**Correctness problem.** The claim fails for n = 1: H = (1) satisfies HH* = 1·I for every l, but 1 ∉ ℕp₁+…+ℕp_s. The statement needs n ≥ 2, which is the case where an off-diagonal row pair exists. This is minor, but the statement as written is false.

### Applied Verdict: not evaluated
The seed proposes no method or algorithm. Type 7 was not claimed.

### Contribution Type Verdicts (mode=full only):
Type 1 (new theorem): **FAIL.** The bar is "not known, not folklore, not a trivial consequence". The statement for all s is a two-line consequence of Lam–Leung (1995 preprint, 1996 arXiv, J. Algebra 2000). The s = 2 and s = 3 cases and the conjecture are all covered.

No other types are claimed. A Type 2 (new proof) reading of the s = 2 and s = 3 arguments also fails on what is visible. These are partial re-proofs of a theorem already proved in full generality. The seed's text shows no technique, connection or simplification beyond the Lam–Leung route. The closing "remarks on other obstructions" are too thin to carry Type 6.

### Cross-reference
The theorem is known: it is a trivial corollary of a known number-theoretic classification, with no credit given in the seed. No surviving type carries the seed.

### Recommendation
**Park** (to covered_leads). Type evaluated: 1. Bar failed: known (trivial consequence of Lam–Leung). This is not an open question, because the conjecture is already a theorem. If the work is pursued, the honest repositioning is: cite Lam–Leung, state the BH condition as an immediate corollary, and look for obstructions beyond it.

### Referee estimate: REJECT-LIKELY
Venue class: none
Value carried by: none (a partial re-proof of a fully proved theorem cannot carry factor 2; the remarks on other obstructions are too thin for factor 4)
Main risk a referee would raise: "This is a two-line corollary of Lam–Leung (J. Algebra 2000; MSRI preprint 1995), which settles the conjectured general case; it is uncredited."
