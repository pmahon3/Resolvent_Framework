## Audit: seed.md (counting solution-free sets for non-translation-invariant linear equations) (mode: full)

Audit date per AS_OF.md: **2009-05-06**. Only sources dated on or before that day are used as prior art. The seed's own text is the submission. Search hits for the seed's own arXiv preprint (arXiv:0905.0990, May 2009) were seen in search listings and **not read or used**. Hits dated after 2009-05-06 (Hancock–Treglown arXiv:1607.08399, 2016) were used **only as a bibliography pointer** to find older primary sources; no claim in this audit rests on them.

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)
The seed declares types but does not state the per-type bars it commits to clearing. That is a gap in readiness, not fatal.

### Stripped statement
Take L: a_1x_1+…+a_kx_k = b, with k ≥ 3 and Σa_i ≠ 0, so L is not translation-invariant. Let f(N,L) be the number of L-free subsets of [N] and μ_L(N) the maximum size of one.
- (C) Conjecture: f(N,L) = 2^{(1+o(1))μ_L(N)}.
- (T) Theorem: a weaker upper bound for a family of equations whose μ_L is known. It is proved by building a graph G_L on [N] of almost-constant degree, so that free sets are independent in G_L, and then bounding the number of independent sets of an almost-regular graph.

Note that μ_L(N) = Ω(N) for non-invariant L (Ruzsa 1993), so (C) is the same as f(N,L) = 2^{μ_L(N)+o(N)}.

### Pure Verdict: UNCLEAR (partly KNOWN)

**(C) is already a theorem in the homogeneous case b = 0, and the seed does not credit it.**
- Green, "A Szemerédi-type regularity lemma in abelian groups, with applications", GAFA 15 (2005) 340–376, arXiv math/0310476 (v2 dated 21 Oct 2004, before the audit date). Its **Theorem 9.3** reads: for a fixed linear form L = L_b with nonzero integer coefficients, log₂|LF(N)| = f_L(N) + o(N), where LF(N) is the set of weakly L-free subsets of [N] and f_L(N) is the largest strongly L-free size. The proof goes through Propositions 9.1 and 9.2 (granularization, a container-type family of size 2^{o(N)}).
- *Read level: primary source, §9 read via ar5iv HTML of the arXiv version (full text, read in two segments).* For a non-invariant homogeneous L, trivial solutions do not arise in positive integers, and μ_L = Ω(N). Theorem 9.3 therefore gives exactly f(N,L) = 2^{(1+o(1))μ_L(N)}.
- So for b = 0, (C) is proved in full, which is stronger than the seed's weak form (T).
- The seed's sentence "we ask how many free sets there are … conjecturing" presents an already-settled question as open, for every homogeneous member of its class.

**Known special cases of (C), all homogeneous:**
- Sum-free sets (x+y=z): Cameron–Erdős conjecture, posed in Cameron–Erdős, *Number Theory* (de Gruyter 1990). Proved by Green, *Bull. LMS* 36 (2004) 769–778, and independently by Sapozhenko, *Dokl. Akad. Nauk* 393 (2003). *Read level: bibliographic, via a secondary pointer; the results are standard.*
- (k,l)-sum-free sets:
  - Calkin–Taylor (1996), for (k,1);
  - Calkin–Thomason, *J. Number Theory* 68 (1996/98), for k ≥ 4l−1;
  - Bilu, *Combinatorica* 18 (1998);
  - Schoen, *EJC* 7 (2000) R30, and *Acta Arith.* 98 (2001).

  These give f = O(2^{μ}) for various ranges. *Read level: bibliographic; bounds via Schoen's EJC note as quoted in search snippets. The exact exponents were not verified in the primary sources.*

**The method in (T) is standard.** Counting free sets by counting independent sets in an almost-regular graph is the Alon–Granville–Cameron route:
- Alon, "Independent sets in regular graphs and sum-free subsets of finite groups", *Israel J. Math.* 73 (1991) 247–256. A d-regular n-vertex graph has at most 2^{(1/2+ε(d))n} independent sets, and the result was motivated by the counting of sum-free sets. *Read level: abstract and bibliographic.*
- Sapozhenko's container method for independent sets (1987 onward) and Lev–Łuczak–Schoen, *Israel J. Math.* 125 (2001), use the same idea for sum-free sets in groups. *Read level: from memory and bibliographic; not re-read.*
- Extending from regular to almost-regular graphs is a routine change to these proofs. It is a lemma, not a new technique.

**What survives as possibly new:**
1. The conjecture (C) for **inhomogeneous** non-invariant equations (b ≠ 0). Green's Theorem 9.3 and its removal-lemma machinery are stated only for homogeneous forms. I found no pre-2009 paper that states or proves the count for b ≠ 0.
2. The weak bound (T) for the b ≠ 0 members of the seed's family.

Both are modest. The b ≠ 0 extension of Green's granularization looks plausible but is not immediate: it needs an inhomogeneous removal lemma in [N]. Pre-2009 candidates are Kráľ–Serra–Vena (arXiv 2008) and Shapira (arXiv 0807.4901, 2008). *These were not read; they were seen in search listings only. Whether they cover b ≠ 0 in [N] is UNVERIFIED.*

**Searched:**
- "Cameron–Erdős non-invariant linear equations number of free sets";
- Green GAFA §9;
- the counting literature on (k,l)-sum-free sets;
- Alon 1991.

**Verdict:** KNOWN for b = 0, through Green 2005 Theorem 9.3. UNCLEAR for b ≠ 0, which is the only live region. That region's status depends on whether an inhomogeneous removal or granularization argument existed before 2009, and that was not established.

### Correctness flag
The seed says the graph's "independent sets are **exactly** the free sets". For k ≥ 3 the solution set is a k-uniform hypergraph constraint. A graph on [N] can only capture the degenerate solutions with variables collapsed to two values. Free sets are then independent sets, but the converse fails in general: an independent set can contain a solution with three or more distinct values.
- The upper-bound argument needs only "free ⟹ independent", so (T) is probably unaffected.
- The "exactly" claim is false as stated, unless the family is so restricted that it holds. The seed gives no such restriction.

The write-up must restate it as containment.

### Applied Verdict: not evaluated (no Type 7 claimed; pure combinatorics)

### Contribution Type Verdicts (mode=full)

**Type 1 (new theorem): UNCLEAR, leaning FAIL**
- Bar applied: not known, not folklore, not a routine consequence.
- For homogeneous members of the family, (T) is strictly weaker than Green 2005 Theorem 9.3. That part FAILS as known.
- For inhomogeneous members, (T) may be new. But it is a weak bound, obtained by applying the Alon/Sapozhenko independent-set count, a standard technique, to an explicit graph. The non-routine content is at most building the graph and the almost-regular lemma.
- Passing needs a statement of which family members have b ≠ 0, and confirmation that no pre-2009 inhomogeneous removal or container result already gives (C) there.

**Type 3 (unifying framework): FAIL**
- Bar applied: method transfer from domain A to domain B, demonstrated.
- The transfer "counting independent sets in near-regular graphs → counting solution-free sets" already exists. Alon 1991 was written for sum-free sets, and Lev–Łuczak–Schoen and Sapozhenko use graph containers for the same purpose. The seed applies this transfer to more equations; it does not create it.
- "Extends to general equations the known counting question for sum-free sets" also overstates, because Green 2005 §9 already made that extension for every homogeneous equation.

**Undeclared but relevant:** the seed's real asset may be an **open question** (framework outcome 3): the count for inhomogeneous non-invariant equations.
- (a) It is precisely stated.
- (b) The obstruction is partly identified: Green's granularization needs a removal lemma that handles b ≠ 0 in [N].
- (c) Its consequences are named, though thinly: Cameron–Erdős-type counting for all non-invariant equations.

### Cross-reference
The pure verdict and the Type 3 verdict share one cause. The headline framing (a new Cameron–Erdős-type conjecture for general equations, reached through a graph bridge) is owned by Green 2005 for the homogeneous half, and by Alon 1991 and Sapozhenko for the method. The live part is the inhomogeneous case. Even there, the seed's theorem is a weak bound by a standard method, so neither Type 1 nor Type 3 clears the bar now.

### Recommendation
**Park as a contribution and move to open-question status, with the scope narrowed to b ≠ 0.**
- Evaluated: Type 1, which is UNCLEAR and fails on the b = 0 part, and Type 3, which FAILS because the transfer is prior art.
- Before any re-entry:
  1. credit Green 2005 Theorem 9.3, and restrict (C) to b ≠ 0;
  2. check the 2008 removal-lemma preprints (Kráľ–Serra–Vena, Shapira) for an inhomogeneous [N] version that would settle (C) with Green's §9 argument;
  3. fix the "exactly" claim.

**Bearing on the WHY:** this is a seam where a local constraint (no solution among a few elements) meets a global count. It bears only as a lens on loop versus composition, with no practical bridge.

### Referee estimate: BORDERLINE
Venue class: research journal (combinatorics or number theory, mid-tier)

Value carried by: factor 1 (a new, if weak, bound for the inhomogeneous members) together with factor 3 (a natural new conjecture that others can attack, posed for b ≠ 0).

Main risk a referee would raise: Green (GAFA 2005, Thm 9.3) already proves the conjectured count 2^{μ+o(N)} for every homogeneous equation. That is not credited, so the novelty and "extension" claims must shrink to the inhomogeneous case. The graph-counting method is Alon 1991 / Sapozhenko, and the "independent sets are exactly the free sets" claim is false as stated for k ≥ 3.

### Sources (read level; date)
- Green, GAFA 15 (2005); arXiv math/0310476 v2, 21 Oct 2004. Primary: §1 and §9 read via ar5iv. Before the audit date.
- Alon, Israel J. Math. 73 (1991). Abstract and bibliographic. Before the audit date.
- Green, Bull. LMS 36 (2004); Sapozhenko, Dokl. 393 (2003); Cameron–Erdős (1990); Ruzsa, Acta Arith. 65 (1993); Calkin–Thomason (1996/98); Bilu, Combinatorica 18 (1998); Schoen, EJC 7 (2000) and Acta Arith. 98 (2001); Łuczak–Schoen, PAMS 129 (2001). Bibliographic, from a secondary bibliography. All before the audit date.
- Kráľ–Serra–Vena (arXiv 2008) and Shapira (arXiv 0807.4901, July 2008). Titles only; contents unverified. Their dates precede the audit date, as far as could be told.
- Hancock–Treglown, arXiv:1607.08399 (2016). After the audit date; used only as a citation pointer, not as prior art.
- arXiv:0905.0990. The submission itself; ignored.
