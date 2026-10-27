## Audit: seed.md — axis-parallel hyperplane transversals of convex bodies with no m+1 pairwise disjoint (mode: full)

Audit date (per AS_OF.md): **2010-04-19**. Only pre-2010-04-19 sources are used as prior art. The seed's
own text, and any version, withdrawal or commentary of it, is excluded.
Search date: 2026-10-26 (web, standard mode). WHY.md is not in the audit directory, so the why-line
below rests only on the seed.

### Declared contribution type(s): Type 1 (new theorem), Type 2 (new proof of known result)
Declared, but the seed states no per-type bar it commits to clearing. That is a Phase-1 gap.

### Pure Verdict: KNOWN (all three claimed bounds are implied by, and weaker than, published results)

**1. Stripping the vocabulary.** A hyperplane x_i = c meets a convex body K iff c lies in the
projection interval π_i(K). So each body K becomes a *separated d-interval*
I(K) = π_1(K) ∪ … ∪ π_d(K), with one interval on each of d disjoint lines, and
"cut by f axis-parallel hyperplanes" becomes "pierced by f points" (τ of the d-interval family).

The hypothesis transfers in the right direction. If I(K) and I(K′) are disjoint, the projections
are disjoint on every axis, so K ∩ K′ = ∅. Hence a matching of d-intervals gives pairwise
disjoint bodies, and ν(I(C)) ≤ m.

The question is therefore exactly the τ-versus-ν problem for separated d-intervals (2-intervals
when d = 2). Convexity is used only to make the projections intervals; connectedness would be
enough. ⟦HAND, 3-line reduction; checked⟧

**2. What was already in print on or before 2010-04-19.**
- **Gyárfás–Lehel**, "A Helly-type problem in trees", in *Combinatorial Theory and its
  Applications* (Erdős, Rényi, Sós eds.), North-Holland 1970, 571–584. Also Gyárfás–Lehel,
  "Covering and coloring problems for relatives of intervals", *Discrete Math.* 55 (1985)
  167–180. These give the existence of τ ≤ f(d, ν) for d-intervals, which is the seed's first
  claim (that the bound depends only on d and m).
  [read level: citation only, via Alon 1998's reference list and secondary summaries. The
  original's exact constant was not seen. Dates 1970/1985 are clearly before the audit date.]
- **G. Tardos**, "Transversals of 2-intervals, a topological approach", *Combinatorica* 15
  (1995) 123–134. Proves τ ≤ 2ν for 2-intervals, and the bound is tight. Separated 2-intervals
  are a special case, so in the plane the seed's question already has the linear bound
  **2m**, which beats the seed's O(m²).
  [read level: statement via secondary sources (Wikipedia "d-interval hypergraph", accessed
  2026-10-26, citing the 1995 paper) and Alon 1998's reference list. Primary text not read.]
- **T. Kaiser**, "Transversals of d-intervals", *Discrete Comput. Geom.* 18 (1997) 195–203,
  doi:10.1007/PL00009315. Proves τ ≤ d(d−1)ν for d ≥ 2. That gives **d(d−1)m**, linear in m,
  which beats the seed's "polynomial in m for fixed d".
  [read level: statement via secondary sources (Wikipedia, accessed 2026-10-26; Alon 1998's
  description "τ ≤ O(d²ν)"). Primary text not read. One residual I could not settle: whether
  Kaiser's d(d−1) is stated for the separated or the general (one-line) model. Either way the
  separated case is covered, since separated d-intervals embed into one line.]
- **N. Alon**, "Piercing d-intervals", *Discrete Comput. Geom.* 19 (1998) 333–334.
  Proves τ ≤ 2d²ν with a short proof that avoids topology.
  [read level: abstract/metadata only. The PDF fetched 2026-10-26 was unreadable binary, and its
  reference list was recovered through search snippets.]
- **J. Matoušek**, *Using the Borsuk–Ulam Theorem*, Springer 2003, which presents the Tardos and
  Kaiser approach. [read level: recalled, not re-read for this audit.]

**3. Assessment.** Every claimed bound (existence, polynomial in m, O(m²) in the plane) is a
strictly weaker form of a result published 12–40 years before the submission date.

The planar claim to "lower the best exponential bound" is contradicted by the literature: since
1995 the best bound has been linear (2m), not exponential. The remark that "most of the results
here were already known as d-separated interval piercing" appears only in later versions or the
withdrawal of the submission, so it is not used here. It agrees with this verdict.

Searches run: "convex sets no k+1 pairwise disjoint pierced by axis-parallel hyperplanes";
Gyárfás–Lehel hyperplanes perpendicular to coordinate axes; Kaiser transversals of d-intervals;
Gyárfás–Lehel Helly-type problem in trees. The only hit on the statement itself was the
submission (arXiv 1004.3381, D. Werner), which is excluded as self.

### Applied Verdict: not evaluated (no Type 7 claim; the result is pure combinatorial geometry)

### Contribution Type Verdicts (mode=full only):

**Type 1 (new theorem): FAIL.**
- Bar: the statement is not known, not folklore, and not a trivial consequence of known results.
- Every claimed statement follows from Gyárfás–Lehel (existence), Tardos 1995 (plane, 2m), or
  Kaiser 1997 / Alon 1998 (O(d²)·m), through the 3-line projection reduction.
- The claimed bounds are weaker than these, not sharper.

**Type 2 (new proof of known result): FAIL** (judged on the seed as submitted; see the caveat).
- Bar: (a) a technique usable elsewhere, (b) an unexpected cross-field connection, or
  (c) a substantial simplification.
- The seed proves *weaker* bounds than the known ones, so it is not a new proof of the known
  results.
- (c) is pre-empted. Alon 1998 already gives a one-page, non-topological proof of the stronger
  linear bound O(d²ν).
- (a) and (b) are not shown. The seed names no technique and no connection.
- Caveat: the seed is an abstract with no proof content, so the proof itself cannot be judged.
  A method that is genuinely different from both topological (Tardos/Kaiser) and LP (Alon)
  routes might be worth a note, but nothing in the seed shows one.

### Cross-reference
- The pure and type verdicts agree. The central object is a known object (separated d-interval
  piercing) under a geometric costume, and the claimed results sit below the known bounds.
- No component is novel, and no assembly is offered.
- Correctness: the statements are *true*, since they follow from the known bounds. The
  novelty and "improvement" positioning is false.
- Bearing on the programme's why ("local views → one world"): this is a lens only. Projections
  onto axes are local views, and the d-interval reduction shows that piercing depends only on
  those views. It is a clean instance of "the questions you can ask suffice", already owned by
  Tardos/Kaiser.

### Recommendation
**Park.**
- Types evaluated: 1 (FAIL, known and weaker: Gyárfás–Lehel 1970/85, Tardos 1995, Kaiser 1997,
  Alon 1998) and 2 (FAIL, no proof shown; simplification already pre-empted by Alon 1998).
- Possible owned_by entry: "axis-parallel hyperplane cover of convex bodies with ν ≤ m" is owned
  by separated d-interval piercing (Tardos 1995; Kaiser 1997), verified by the projection
  reduction above.

### Referee estimate: REJECT-LIKELY
Venue class: none
Value carried by: none
Main risk a referee would raise: the problem reduces in three lines to separated d-interval
piercing, where Tardos (1995) and Kaiser (1997) already give linear bounds (2m in the plane,
d(d−1)m in general). The claimed O(m²) and polynomial bounds are weaker, and the claim to improve
"the best exponential bound" is contradicted by the literature.

Undated-source note: every cited prior-art source predates 2010-04-19 by publication year. The
secondary sources used to confirm statements (Wikipedia, 2026 search snippets) are post-date and
were used only to identify what the pre-2010 papers state, not as prior art.
