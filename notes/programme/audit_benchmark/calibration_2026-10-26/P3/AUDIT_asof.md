## Audit: seed.md, bunkbed counterexample on a planar graph with 7222 vertices (mode: full)

**Audit date (AS_OF.md):** 2024-10-02. Only sources dated on or before 2024-10-02 count as prior art. The seed's own work under any title is excluded: arXiv:2410.02545 and its PNAS version, press coverage, and seminar abstracts. Search results surfaced these, and they were deliberately ignored.

### Declared contribution type(s): Type 1 (new theorem)

The seed declares the type but states no per-type bar. That is a minor Phase-1 hygiene gap, not blocking.

### Pure Verdict: NOVEL (as of 2024-10-02; correctness unverified, as the seed has no proof)

**Stripped statement.** There is a finite planar graph G with vertices u, v and a p ∈ (0,1) satisfying the following. Under independent bond percolation on G□K₂ with posts always open (Kasteleyn's formulation, equivalent by standard reductions), P(u₀ ↔ v₁) > P(u₀ ↔ v₀). This is a counterexample to the bunkbed conjecture for ordinary graphs.

**Searched.** Hypergraph, site and directed generalisations; the p↑1 limit; equivalent formulations; special classes (complete, complete bipartite, outerplanar); and "bunkbed counterexample" before October 2024.

Sources:
- **Hollom, "The bunkbed conjecture is not robust to generalisation", arXiv:2406.01790 v1, 3 Jun 2024.** Read level: arXiv HTML full text, read via a summariser, so excerpts only. Thm 1.6 disproves the generalised conjecture for site percolation, hypergraphs and digraphs. §5.1 gives the 3-uniform hypergraph H₄ on 10 vertices, which disproves Linusson's hypergraph Conjecture 4.2. The paper states that these results "do not directly say anything" about the original graph conjecture, and that the graph conjecture "is widely expected to be true". This is the most damaging prior source: it supplies the seed's starting object. It also explicitly leaves the graph case open, so it does not own the seed's statement.
- **Hutchcroft, Kent, Nizić-Nikolac, "The bunkbed conjecture holds in the p↑1 limit", Combin. Probab. Comput. 32(3):363–369, 2023.** Read level: citation and snippet. The conjecture holds near p = 1. This is consistent with a counterexample whose gap is astronomically small, as in the seed (~10⁻⁶⁵⁰⁹). It is not an obstruction.
- **Rudzinski–Smyth, "Equivalent formulations of the bunk bed conjecture", 2016.** Read level: snippet, as cited in Hollom. A counterexample at one fixed p suffices. This is a reduction, not a counterexample.
- **Linusson (outerplanar case, ~2011), de Buyer / van Hintum–Lammers (complete graphs, 2016/2019), Richthammer (complete bipartite, ~2022).** Read level: names known from the literature, not opened this audit. These are positive special cases only and do not reach planar graphs in general.

No source dated on or before 2024-10-02 gives a graph counterexample. Hollom's own framing (Jun 2024) shows the community consensus was that the conjecture is true. The hypergraph-to-graph conversion is not a trivial consequence of Hollom. A single 3-hyperedge cannot be simulated exactly by a bond-percolation gadget, so the gadget must be approximate and robust, and that is the non-routine step. That point comes from general knowledge of the problem plus the seed's own description. I did not verify it from a prior source.

**Gap.** The seed has no proof. Novelty is NOVEL conditional on correctness. Correctness, i.e. the exact computation of the gap and the gadget's error control, must be checked independently. The 10⁻⁶⁵⁰⁹ gap makes Monte Carlo useless, so only an exact or rigorous symbolic check counts.

**Date uncertainty.** Hollom 2406.01790 is clearly before the cutoff (3 Jun 2024). Search snippets give the excluded seed paper as 1 Oct 2024. That is the seed's own work and is excluded either way. For HKN-N I relied on the CPC 2023 volume, which predates the cutoff, and did not check the exact online-first date.

### Applied Verdict: not evaluated (Type 7 not claimed; the decision test is not applicable to a pure counterexample)

### Contribution Type Verdicts (mode=full):

**Type 1 (New theorem): PASS (conditional on correctness).** Bar: not known, not folklore, not a trivial consequence, proof non-routine.
- No prior graph counterexample exists.
- The 40-year-old conjecture was widely believed true (Hollom 2024).
- The construction needs a new robust gadget beyond Hollom's hypergraph.

**Type 5 (Impossibility / counterexample): not declared, but would PASS.** The seed is in substance a counterexample. Bar (a): it closes an actively pursued direction, since a proof of the bunkbed conjecture was being sought through 2023–24 (HKN-N 2023; Hollom 2024). Bar (b): it also sharpens Hollom's generalisation failure down to the original setting. Noted per the skill's instruction, which says to assess types honestly beyond the declared one.

Types 2, 3, 4 and 6 are not claimed and do not apply. Type 3 might apply to the hypergraph→graph gadget as transferable method, but the seed does not claim it or demonstrate it beyond this one use.

### Cross-reference

- Hollom (Jun 2024) owns the hypergraph, site and directed counterexamples.
- HKN-N (2023) owns the p↑1 positive result.
- The seam is the hypergraph→graph transfer. Hollom explicitly left it open, and the seed claims to cross it.
- Pure NOVEL and Type 1 PASS coincide.
- The verdict rests entirely on a correctness check that this audit cannot perform.
- Bearing on WHY.md, in one line: an "unaskable joint question" case. Local pairwise comparisons (lower vs upper copy) fail to globalise in the expected direction, and the failure is a hidden idealisation (the intuition that "same floor is closer") breaking at an extremely small scale.

### Recommendation

Proceed to Phase 3, scoped to Type 1, with Type 5 as the natural framing. Precondition: independently verify the exact gap computation and the gadget's error bounds before any claim is made. Most damaging prior source: Hollom, arXiv:2406.01790 (3 Jun 2024), Thm 1.6 / §5.1 (hypergraph H₄). It supplies the base object, but by its own statement it does not reach graphs.
