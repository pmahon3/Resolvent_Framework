## Audit: seed.md, a survey of expander graphs (mode: full)

**Audit date (per AS_OF.md): 2006-01-01.** Only works dated on or before 2006-01-01 are counted as prior art. Any version, preprint or later coverage of the seed's own text is ignored. Searches were run on 2026-10-26. Post-2006 hits (e.g. Lubotzky's 2012 Bull. AMS survey, arXiv:1105.2389) were discarded.

**Date ambiguity flagged:** Linial and Wigderson's Hebrew University course notes on expanders (c. 2003) may be an early form of the seed's own text. If so, they are excluded as "the submission itself". I could not tell from the search results alone, so they are not used as prior art.

### Declared contribution type(s): Type 6 (exposition/translation). The seed does not state its per-type bar explicitly (see Recommendation).

### Pure Verdict: KNOWN (not claimed; no new theorem stated)
The seed is a survey. It claims no new statement. Its components are standard by 2006:
- **Definitions** (combinatorial, spectral, random-walk) and their equivalences: Cheeger-type inequalities for graphs (Alon–Milman 1985, Dodziuk 1984, Alon 1986 "Eigenvalues and expanders", *Combinatorica* 6). Textbook form in Chung, *Spectral Graph Theory* (CBMS 92, AMS 1997). [read level: known from memory / standard citation; not re-read 2026-10-26]
- **Explicit constructions:** Margulis 1973; Gabber–Galil 1981; Lubotzky–Phillips–Sarnak 1988; Margulis 1988; Reingold–Vadhan–Wigderson zig-zag (FOCS 2000; Annals 2002). [citation-level, from memory]
- **Pure-math side:** Lubotzky, *Discrete Groups, Expanding Graphs and Invariant Measures* (Birkhäuser, 1994). Davidoff–Sarnak–Valette, *Elementary Number Theory, Group Theory and Ramanujan Graphs* (LMS Student Texts 55, CUP, 2003; date verified by web search 2026-10-26, catalogue level). Sarnak, "What is… an expander?", *Notices AMS* 51(7), 762–763, 2004 (bibliographic record verified 2026-10-26, citation level).
- **Recent CS results a 2006 survey would synthesise:** Capalbo–Reingold–Vadhan–Wigderson lossless conductors (STOC 2002); Bilu–Linial lifts (FOCS 2004); Reingold, undirected connectivity in log-space (STOC 2005); Friedman's proof of Alon's second-eigenvalue conjecture (preprint 2003/2004). These are scattered across conference papers. [citation level, from memory]

### Applied Verdict: not evaluated (no method or algorithm is claimed). Practitioner test: N/A.

### Contribution Type Verdicts (mode=full only):
**Type 6 (Exposition/translation): UNCLEAR, leaning PASS if the CS synthesis is delivered.**
- **(a) Audience:** "readers with a general mathematical background" (not specialists). This names an audience, but broadly. A sharper target would be mathematicians outside combinatorics and TCS who want both sides.
- **(b) Inaccessible literature:**
  - *Pure-math half: already accessible.* Lubotzky 1994 and Davidoff–Sarnak–Valette 2003 (written for undergraduates) cover the constructions from number theory and group theory. Chung 1997 and Alon 1986 cover the spectral and combinatorial equivalences. On this half, a survey would fail the programme's "well-explained in [textbook]" clause.
  - *TCS half: met.* As of 2006 there is no single accessible exposition of the post-2000 combinatorial programme, which runs from zig-zag through lossless expanders and lifts to Reingold 2005. Lubotzky 1994 predates it. Davidoff–Sarnak–Valette is purely arithmetic.
- **(c) Non-trivial conceptual work:** this cannot be verified from the seed's abstract. Two things would clear it:
  - organising the three definitions so that the equivalences carry the applications;
  - presenting the zig-zag/entropy-wave viewpoint alongside the algebraic constructions.

  Listing definitions, constructions and applications alone would not.
- **Bar applied:** the programme's park-if-accessible clause. Half of the scope fails it, and half clears it conditionally.

### Cross-reference
- All components are known. The contribution can only be the assembly, i.e. a unified CS-plus-pure-math exposition.
- No Type 1 claim, so there is no conflict there.
- The Type 6 verdict depends on whether the text weights the recent combinatorial and TCS material. That material is the part not already accessible. The textbook-covered arithmetic constructions are not.

### Recommendation
**Redirect to expository venue** (Bull. AMS / survey track). Scope it to the TCS synthesis and the bridge between the definitions.
- Evaluated: Pure (KNOWN, not claimed), Type 6 (UNCLEAR).
- Owed: the seed should state its Type 6 bar explicitly:
  - which post-2000 results it makes accessible;
  - how it differs from Lubotzky 1994, Davidoff–Sarnak–Valette 2003, Chung 1997 and Sarnak 2004.
- **Correctness:** no problem is detectable, because no central claim is stated beyond scope.

**Bearing on the why (one line):** expansion is a strong case of local sparse relations giving global connectivity with no centre. It serves only as a lens; nothing here bears directly on gluing local views into one world.

### Referee estimate: ACCEPT-LIKELY
Venue class: expository (Bulletin AMS / survey)
Value carried by: factor 4 (a survey that pulls together scattered recent work: zig-zag, lossless expanders, lifts, SL=L, alongside classical spectral and arithmetic theory, for a neighbouring audience)
Main risk a referee would raise: overlap with existing accessible expositions (Lubotzky 1994; Davidoff–Sarnak–Valette 2003; Chung 1997; Alon 1986; Sarnak 2004 Notices) unless the recent TCS synthesis and the unified treatment of definitions are substantial.

Sources (searched 2026-10-26):
- [Davidoff–Sarnak–Valette (Wikipedia)](https://en.wikipedia.org/wiki/Elementary_Number_Theory,_Group_Theory_and_Ramanujan_Graphs)
- [ECU catalogue record](https://lib.ecu.edu/catalog-preview/catalog/902887)
- [Sarnak 2004 BibTeX record](https://www.bibsonomy.org/bibtex/980f6a29e2c2222de64a0dc19c993577)
- [Sarnak 2004 PDF](https://www.ams.org/notices/200407/what-is.pdf) (link from a seminar list; not fetched)
- [Lubotzky 2012 (arXiv:1105.2389)](https://arxiv.org/pdf/1105.2389) (post-2006, discarded)
