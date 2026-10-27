## Audit: seed.md, "a small acyclic digraph on which the directed bunkbed inequality fails" (mode: full)

Audit date (per AS_OF.md): **2025-06-26**. Only sources that existed on or before that date count as prior art.
The seed's own work (arXiv:2506.22284, Przybyłowski, v1 dated 27 Jun 2025 / v2 Nov 2025) is the
submission itself and is NOT used as prior art. I fetched only its arXiv abstract page and metadata to
confirm identity. The PDF body could not be read, so no correctness judgement relies on it. Later citing
works (e.g. arXiv:2511.13589, Nov 2025) are also excluded.

### Declared contribution type(s): Type 1 (new theorem)
The seed declares a type but does not state the per-type bar it commits to clearing. It also leaves out
the graph, the edge-probability model, which vertical-edge convention is used, and the computed
probabilities. It is a two-sentence abstract, not an audit-ready seed.

### Pure Verdict: NOVEL (as of 2025-06-26)
**Stripped statement.** There is a finite directed acyclic graph G, with vertices u, v and an
independent bond percolation in which each edge is open with probability p. On its directed bunkbed
(two copies of G joined by vertical edges, under a stated convention), the following holds:
P(u₀ → v₁) > P(u₀ → v₀). So Leander's acyclic directed bunkbed conjecture is false.

**Prior art checked, and what each source owns:**
- Hollom, "The bunkbed conjecture is not robust to generalisation", arXiv:2406.01790 v1 (3 Jun 2024;
  Eur. J. Combin. 128 (2025) 104188). Read level: §4 and §6 read via the HTML text, fetched 2026-10-26.
  It disproves the *directed* bunkbed conjecture (Thm 1.6), but its counterexample "has many cycles",
  and its vertical edges are bidirectional. It says explicitly: "it remains open whether the conjecture
  holds for acyclic directed graphs" (§4). Question 6.3 asks whether the E6/E7 model conjectures hold for
  all acyclic digraphs, and the author says it is unclear which way the answer goes. **This makes the
  target an explicitly posed open problem as of the audit date.**
- Leander, "On the bunkbed conjecture", Stockholm Univ. report 2009. Read level: secondary only (seen
  through Hollom §4); the primary source was not read. It poses the acyclic directed conjecture, and
  suggests it may extend to all digraphs.
- Gladkov–Pak–Zimin, "The bunkbed conjecture is false", arXiv:2410.02545 (Oct 2024; PNAS, accepted
  19 Apr 2025). Read level: abstract and secondary summaries, 2026-10-26. It gives an undirected planar
  counterexample on 7222 vertices. Read as a digraph, an undirected graph has every edge in both
  directions, so it is full of directed 2-cycles. It therefore does not settle the acyclic case. They also
  note that Hollom's hypergraph gadget cannot be simulated directly by bond percolation, so no quick
  reduction is known.
- Richthammer, arXiv:2204.12931 (v1 Apr 2022, v2 25 Mar 2025). Read level: abstract. It gives positive
  results for complete bipartite and related undirected classes. Nothing on acyclic digraphs.
- Searched without finding a hit: "acyclic directed bunkbed", "directed bunkbed counterexample",
  "bunkbed oriented percolation", "Leander bunkbed acyclic". No pre-2025-06-26 acyclic counterexample was
  found.
- Gravner–Painter–Zhou (2024) is cited in the submission's metadata. I could not locate it, so it is
  unverified. **Gap:** I cannot rule out that it touches directed or acyclic cases.

**Trivial-consequence check.** Do the known counterexamples reduce to the acyclic case? (a) The GPZ
undirected graph and Hollom's directed graph both rely on cycles. (b) Orienting an undirected
counterexample acyclically changes the connection events, so it is not a reduction. (c) Hollom and
Leander both record the case as open, which is strong evidence that experts saw no 3-line derivation.
Not folklore.

### Applied Verdict: not evaluated (no Type 7 claim; pure combinatorics/probability)

### Contribution Type Verdicts (mode=full only):
**Type 1 (new theorem): PASS, conditional on verification.**
The bar is: not known, not folklore, not a trivial consequence, and the proof is non-routine. The first
three hold as of 2025-06-26 (see above). Whether the proof is non-routine cannot be judged from the
seed, because no graph or computation is given. For a counterexample the "proof" is an exact
computation. Conditions:
1. Exhibit the graph, p, and the vertical-edge convention. The seed must say which of Hollom's models it
   uses (E6, E7, or Leander's original), because "settles the acyclic question" depends on matching
   Leander's exact formulation.
2. Certify the strict inequality by exact rational/polynomial arithmetic, not floating-point Monte Carlo.
3. Check acyclicity of G *and* say whether the bunkbed itself is acyclic (vertical edges oriented one
   way or both). Bidirectional vertical edges would create 2-cycles. Whether that still counts as
   "acyclic" is exactly the question Leander's formulation fixes.

**Type 5 (impossibility / counterexample): not declared, but this is the natural fit. Would PASS.**
Bar (a), closing off an active direction, is met. After GPZ, the acyclic directed version was one of the
few remaining live forms of the conjecture, and Hollom posed it as open in Q6.3. The seed should
re-declare as Type 1 + Type 5, or as Type 5 alone.

Types 2, 3, 4, 6: not claimed, not applicable.

### Cross-reference
The novelty is clean, but the verification is unseen. The pure audit finds no owner as of the audit
date, because the problem is explicitly recorded as open by Hollom (2024). The whole contribution
rides on one explicit, checkable object, so the only real risk is correctness or a model mismatch, not
prior art. Smallness ("small digraph") is a plus for refereeing: it can be checked by hand or with exact
arithmetic.

Bearing on WHY.md (one line): a pure percolation counterexample. It touches "do local views add up?"
only as a lens: removing loops (acyclicity) does not restore the intuitive monotonicity, an echo of
"hidden idealisation". No direct bearing.

### Recommendation
**Proceed to Phase 3**, scoped to Type 1 / Type 5, subject to three things:
- (i) stating the exact model;
- (ii) an exact-arithmetic certificate of the strict inequality;
- (iii) independent verification (exact computation, Lean-checkable if small).

Also cite Leander 2009 (primary source, still to be read) and Hollom Q6.3, and re-check
Gravner–Painter–Zhou 2024.

### Referee estimate: ACCEPT-LIKELY
Venue class: research journal (short paper; e.g. Electron. J. Combin. / Combin. Probab. Comput. class), or a short-note venue
Value carried by: factor 1 (new theorem: resolves an explicitly posed open conjecture, Leander 2009 / Hollom 2024 Q6.3)
Main risk a referee would raise: whether the model, especially the orientation of the vertical edges, matches Leander's or Hollom's exact acyclic formulation, and whether the strict inequality is certified exactly.
