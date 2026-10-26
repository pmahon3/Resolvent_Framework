## Audit: seed.md (axis-parallel hyperplane transversals T_d(m)) (mode: full)

### Declared contribution type(s): Type 1 (new theorem), Type 2 (new proof)
Types are declared. **Per-type bars are not stated** (the framework requires "the per-type bars I commit to clearing"). On this point the seed is not Phase-2-ready. The audit proceeds anyway.

### Pure Verdict: KNOWN

**Step 1: strip vocabulary.** A convex set K ⊂ R^d meets the hyperplane {x_i = c} iff c ∈ π_i(K), where π_i is the i-th coordinate projection. So K ↦ (π_1(K), …, π_d(K)) sends the family to a family of **separated d-intervals**: one interval on each of d disjoint copies of R. Axis-parallel hyperplanes become points on those copies. T_d(m) is therefore the bound τ ≤ f(d, ν) for separated d-intervals. This is the classical Gallai-type problem for multiple intervals.

**Step 2: the hypothesis is mis-stated in the seed, and the literal version is trivial.** The seed defines independence as "pairwise disjoint subfamily". Under that reading:
- Pairwise-disjoint projections π_1 force the sets themselves to be pairwise disjoint. So the intervals {π_1(K)} have ν ≤ m.
- Intervals satisfy τ = ν (Gallai, folklore).
- Hence m hyperplanes orthogonal to e_1 pierce everything, and T_d(m) = m exactly. For the lower bound, take m points with distinct coordinates.

That is a 3-line consequence: KNOWN / trivial. The intended, non-trivial reading is the one in the source text below. There, independence means that no two members meet a common axis-parallel hyperplane, i.e. the matching number of the separated d-interval hypergraph.

**Step 3: the intended statement is owned, with bounds that dominate the seed's.**
- **Werner & Lenz, "Polynomial Bounds on the Slicing Number", arXiv:1004.3381.** The seed's abstract is essentially this paper's abstract: T_d(m) exists, a super-exponential bound, then a polynomial bound for fixed d, then O(m²) in the plane (TOPP Problem 74). Read level: **abstract** (v3 abstract page, and the v4 withdrawal abstract and comments, read in full). The authors withdrew it (v4, 2 Aug 2010): "most of the results mentioned here were already known under the name of 'd-separated interval piercing'". Their withdrawal note gives these attributions:
  - existence of T_d(m) is due to Gyárfás–Lehel 1970;
  - Károlyi–Tardos strengthened it "to match our result", "using ideas very similar to ours … a similar recurrence";
  - Tardos (d = 2) and Kaiser (general d) proved a linear bound.
- **Gyárfás & Lehel (1970)**, a Helly-type problem for multiple intervals: existence of a bound f(d, ν). Read level: **snippet** (secondhand, via the Werner–Lenz note and arXiv:1509.03408 search snippet).
- **Károlyi & Tardos, "On point covers of multiple intervals and axis-parallel rectangles", Combinatorica 16(2) (1996) 213–222.** Improved upper bounds of τ in terms of ν for multiple intervals. Read level: **snippet** (SZTAKI/Springer abstract only).
- **Tardos, "Transversals of 2-intervals, a topological approach", Combinatorica 15 (1995) 123–134.** τ ≤ 2ν for 2-intervals. In the plane this gives T_2(m) ≤ 2m, which beats the seed's O(m²). Read level: **snippet**.
- **Kaiser, "Transversals of d-intervals", Discrete Comput. Geom. 18 (1997) 195–203.** A topological proof (Borsuk–Ulam) of τ ≤ d(d−1)ν, so T_d(m) ≤ d(d−1)·m. That bound is linear in m and beats any polynomial bound of higher degree. Read level: **snippet**, with the statement verified secondhand in the full-text introduction of the next item.
  - Sources disagree on the constant, (d²−d) versus (d²−d+1) depending on separated versus homogeneous d-intervals. This is unresolved from the primary source. It does not matter here, because either is O(d²)·m.
- **Aharoni, Holzman & Zerbib, "Edge-covers in d-interval hypergraphs", arXiv:1605.01942, Thm 1.2** (citing [Tardos 1995; Kaiser 1997]): τ(H) ≤ d(d−1)ν(H) for d ≥ 2. Read level: **full text (introduction only)**, via ar5iv.
- arXiv:2501.03207, "Helly-type theorems for separated d-intervals", definition of separated d-interval. Read level: **abstract**.
- Alon, "Piercing d-intervals" (DCG 1998), an elementary proof of the O(d²ν) bound. Read level: **unread** (the PDF did not render; cited only as a secondhand pointer).

**Step 4: would an expert say "obvious"?** The reduction to separated d-intervals is one line. Once it is made, every claimed result is weaker than, or equal to, published results from 1970–1997, and the authors of the near-verbatim source withdrew it for exactly this reason.

### Applied Verdict: not evaluated (no Type 7 claim; pure combinatorial geometry with no computational component)

### Contribution Type Verdicts (mode=full only):

**Type 1 (New theorem): FAIL.**
- Existence is Gyárfás–Lehel 1970.
- The polynomial bound for fixed d is superseded by Kaiser 1997 (linear, τ ≤ d(d−1)ν), with Károlyi–Tardos 1996 giving the matching recurrence-type result.
- The planar O(m²) is superseded by Tardos 1995 (τ ≤ 2ν).
- Under the seed's literal hypothesis (pairwise disjoint), the result is a trivial consequence of τ = ν for intervals, with T_d(m) = m.

**Type 2 (New proof of known result): FAIL.**
- (a) Technique applicable elsewhere: the seed's route is an iterated recurrence, which by its own authors' account "uses ideas very similar" to Károlyi–Tardos. No new technique.
- (b) Unexpected connection: none. The convex-sets-to-d-intervals link is a one-line projection, and it is the standard framing (TOPP 74).
- (c) Substantial simplification: no. The seed's proof yields strictly weaker bounds than the topological proofs, and Alon 1998 already supplies an elementary (non-topological) proof of the linear bound. A route that is both weaker and not simpler fails the bar: "different but not better or more revealing."

### Cross-reference
- The Type 1 and Type 2 verdicts reinforce each other. The statements are owned, and the proof route is owned and dominated.
- The only potentially distinctive element is the convex-object phrasing, and the projection map removes it.
- The seed also mis-states the independence condition. Under the stated condition the problem collapses to the trivial T_d(m) = m.
- Bearing on WHY (local views → one world): one line only. This is a piercing/transversal bound of the "local (pairwise) data controls global cover" kind. It is a Helly/Gallai-type lens, not a contribution.

### Recommendation
**Park** (move to covered leads).
- Types evaluated: 1 and 2. Both bars failed.
  - Type 1: known (Gyárfás–Lehel 1970; Károlyi–Tardos 1996; Tardos 1995; Kaiser 1997), and trivial under the literal hypothesis.
  - Type 2: no new technique, connection or simplification, and weaker bounds than the existing proofs.
- Not an open-question candidate: the linear bound is settled. Whether the constant d(d−1) is optimal is a separate, already-studied question (Matoušek's Ω(d²/log d) lower bound, snippet-level).
- Most damaging single source: **Kaiser, Discrete Comput. Geom. 18 (1997) 195–203, main theorem (τ ≤ d(d−1)ν for separated d-intervals)**. Together with the Werner–Lenz withdrawal note (arXiv:1004.3381v4), it shows the seed's abstract was retracted by its own authors as known.
