## Audit: seed.md, "a directed bunkbed counterexample on an acyclic digraph" (mode: full)

**Audit date (as-of): 2025-06-26.** Only sources dated on or before this date count as prior art. The
seed's own work (it appears as arXiv:2506.22284, Przybyłowski, "The acyclic directed bunkbed conjecture is
false", submitted 27 Jun 2025) is the submission. I did not use it as prior art or open its text. Its
search-snippet metadata only confirmed which work this is. Later sources (arXiv:2509.18788, Sep 2025;
arXiv:2511.13589, Nov 2025) turned up in searches and were ignored.

### Declared contribution type(s): Type 1 (new theorem)
The seed declares the type but states **no per-type bar**, which the framework requires ("the per-type
bars I commit to clearing"). The seed is also only a two-sentence abstract. It does not give the graph,
does not say which directed percolation model is meant (see the gap below), and contains no proof or
computation. So the claim cannot be checked for correctness here. It can only be checked for novelty.

### Pure Verdict: NOVEL (as of 2025-06-26), conditional on the claim being correct and on the model being specified

**Stripped statement.** There is a finite acyclic digraph D, and a directed bunkbed model (layers D×{0,1}
with vertical edges, independent bond percolation), with vertices u, v such that
P(u₀ → v₁) > P(u₀ → v₀). This refutes the acyclic-digraph form of the bunkbed conjecture.

**Prior art searched (each source dated):**

1. **Hollom, "The bunkbed conjecture is not robust to generalisation", arXiv:2406.01790 v1, 3 Jun 2024**
   (later Eur. J. Combin. 2025). *Read level: HTML full text via a fetch summary, with quoted passages.*
   This is the closest prior art and the most damaging source.
   - Thm 1.6: the generalised bunkbed conjecture is false for digraphs. The models are E6^{T,F} (digraph D6) and
     E7 (directed multigraph D7), §5.2.
   - The vertical edges are bidirectional, so the counterexamples contain 2-cycles. The paper says "the example we construct has many cycles."
   - §4: Leander conjectured the bunkbed conjecture for acyclic digraphs. The extension to all digraphs is
     disproved, but **"it remains open whether the conjecture holds for acyclic directed graphs."**
   - **Question 6.3:** "Do BBC(E6^{T,F}, D) and BBC(E7, D) hold for all acyclic digraphs D?" The author
     calls the answer "unclear". The acyclic case is "far more amenable to inductive techniques", but
     induction "seems far from trivial."
   - Conj 6.2 asks for a *simple* digraph counterexample for the fully directed model E8. Conj 6.4 asks
     about the acyclic transitive tournament T_n under E7.
   → As of 2025-06-26, the acyclic case is an **explicitly posed open question** in the most recent
   specialist paper. Hollom's result does not cover the seed's claim. It sharpens the target instead.
2. **Gladkov–Pak–Zimin, "The bunkbed conjecture is false", arXiv:2410.02545 v1, 3 Oct 2024**
   (PNAS 2025, accepted Apr 2025). *Read level: HTML full text via a fetch summary.* The setting is undirected
   only. The word "directed" does not appear, and §8 covers only undirected variants. The reduction
   replaces hyperedges with undirected gadgets. An undirected counterexample does not give an acyclic
   digraph, since each undirected edge becomes a 2-cycle. Not covering. I could not extract text from the
   PNAS PDF. There may be a directed remark in the PNAS version that I did not see.
3. **Leander, "On the bunkbed conjecture", Stockholm Univ. report 2009:7 (supervisor Linusson), 2009.**
   *Read level: secondary (as cited by Hollom 2024, and in search snippets). The PDF text was not extractable.*
   This is the source of the acyclic-digraph conjecture that the seed refutes. It is the conjecture, not a refutation.
4. Searches: "directed bunkbed acyclic counterexample", "Hollom question 6.3", "transitive tournament
   bunkbed directed", Pak blog and coverage, MathOverflow. *Read level: snippets, Oct 2024–Jun 2025.*
   No source dated on or before 2025-06-26 gives an acyclic directed counterexample, or proves the
   acyclic case.

**Is it trivial or folklore?** No. Hollom (2024), the expert who built the cyclic directed
counterexamples, says the acyclic case is open and unclear. An expert would therefore not call it "obvious".
Removing the 2-cycles from D6/D7 is not an obvious modification, because the bidirectional vertical edges
carry the construction. No three-line derivation from known results was found.

**Gaps that keep this conditional:**
- (a) **Which model?** "Directed bunkbed inequality" is ambiguous. Hollom distinguishes E6^{T,F}, E7 and E8:
  whether the vertical edges are directed, and whether horizontal copies are coupled. The vertical edges
  must also be one-way for the whole bunkbed to be acyclic. The novelty claim must name the model, and
  should say whether the graph is simple (Conj 6.2 asks for that) and whether it settles Q6.3 for
  E6, E7 or both.
- (b) **Correctness.** The seed gives no graph or computation. The inequality must be checked exactly, by
  exact rational computation of the two connection probabilities at a stated p. The GPZ gap was about
  10^-6500, so numerical evaluation is not enough.
- (c) I could not confirm whether Hollom's EJC published version (2025) added remarks on the acyclic case
  after v1. The arXiv listing shows only v1 (3 Jun 2024).

### Applied Verdict: not evaluated (no Type 7 claim; pure combinatorics/probability)

### Contribution Type Verdicts (mode=full):

**Type 1 (new theorem): PASS, conditionally.** Bar: not known, not folklore, not a trivial consequence;
non-routine proof. No source on or before 2025-06-26 contains it. The closest source (Hollom 2024, §4 and
Q6.3) states it is open. This passes on condition that (a) the model is fixed to E6 and/or E7 (or E8) with
one-way vertical edges, and (b) the inequality is exactly verified. Without (b) the claim is unverified,
not known.

**Type 5 (impossibility / counterexample), not declared but the natural fit: PASS, conditionally.** The seed
is a counterexample, so it should declare Type 5 alongside or instead of Type 1. Bar (a), "closes off a
direction people are actively pursuing", is met. It refutes Leander's 2009 conjecture and answers
Hollom's Question 6.3 negatively. Hollom had flagged the acyclic case as the inductively tractable route,
"far more amenable to inductive techniques", so the counterexample closes that proof strategy.
Bar (b), sharpening an existing impossibility, also plausibly holds: it strengthens Hollom's digraph
counterexample from cyclic to acyclic.

**Types 2, 3, 4, 6: FAIL / not applicable.** None is claimed. There is no new proof of a known result, no
framework enabling method transfer, no new vocabulary passing the three-statements test, and no exposition.
Not claimed, and the bars are not met.

### Cross-reference
This is a single, sharp counterexample to an explicitly open, recently re-posed question (Hollom, Q6.3,
June 2024). Novelty holds as of the audit date. The risk is in correctness and model specification, not in
prior art. The contribution is best classed as Type 5, with the Type 1 statement as its content.

WHY.md lens, one line: the bunkbed inequality asks whether local proximity (same layer) always beats
crossing. An acyclic failure shows that removing all loops, so that the graph has no circle, still does not
restore the "local is closer" order. This is a rhyme only, with no bridge to the programme's carriers.

### Recommendation
**Proceed to Phase 3, scoped to Type 5 (+ Type 1 content), after three fixes:**
1. Declare Type 5 and state the bar: "refutes Leander 2009 / answers Hollom 2024 Q6.3 for model ___".
2. Name the model (E6^{T,F} / E7 / E8, vertical edge orientation) and say whether the digraph is simple.
3. Supply the graph and an exact rational verification of P(u₀→v₁) > P(u₀→v₀).

Cite Hollom 2024 (Thm 1.6, §4, Q6.3, Conj 6.2/6.4), Leander 2009, and Gladkov–Pak–Zimin 2024 as context.

**Undated/unclear points:** the content of the PNAS version of GPZ (accepted Apr 2025; text not extractable)
and of Hollom's EJC 2025 version, with respect to directed acyclic remarks. Neither could be read.
