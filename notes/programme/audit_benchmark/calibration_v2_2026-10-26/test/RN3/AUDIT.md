## Audit: seed.md (non-extendability of one-sided quasianalytic germs) (mode: full)

Audit date per AS_OF.md: **2010-06-20**. Only sources dated on or before that day count as prior art.
The seed's own paper, in any version, is the submission and is excluded. Search run 2026-10-26.

### Declared contribution type(s): Type 1 (new theorem)
The seed declares a type but states no per-type bar. Under the framework a seed must also say what it
commits to clearing, so this is a minor readiness gap. The implied bar is the Type 1 bar: the statement
is not known, not folklore, and not a trivial consequence of standard results.

WHY.md was not in the audit directory, so how the item bears on the programme's question was not
assessed. In outline it is a local-to-global extension question: a germ that is good from one side
fails to extend to the two-sided world. It was given no weight.

### Pure Verdict: UNCLEAR (leaning NOVEL; one pre-2010 source unresolved)

**Stripped statement.** Let M be a weight sequence that gives a quasianalytic Denjoy–Carleman class.
Let E_1(M)^+ be the germs at 0 of class-M functions on [0, ε). Then E_1(M)^+ contains a germ f that
does not extend to a quasianalytic germ on (−ε, ε), unless E_1(M)^+ = O_1^+ (real-analytic germs).

**Scope ambiguity, flagged.** "Extended quasianalytically" can mean two things:
- (a) extended to a germ of the *same* class M on a two-sided neighbourhood;
- (b) extended to a germ of *some* quasianalytic Denjoy–Carleman class.

(b) is much stronger and is the version worth having. The union of all quasianalytic classes is not
quasianalytic, so no single-class argument settles it. The audit reads the claim as (b), and the
referee would need that made explicit.

**Sanity check.** The exception is coherent: an analytic germ on [0, ε) always extends analytically.
So the dichotomy has the right shape.

**Trivial-consequence test (does it follow from Carleman's theorem?).** The natural three-line attempt
breaks:
- Carleman's theorem says the Borel map E_1(M) → F_1(M) is not onto when the class is quasianalytic
  and strictly larger than O_1. This is stated, e.g., as Thm 3 in Thilliez, *An introduction to
  quasianalytic local rings*, arXiv:math/0509273 (2005; read level: full HTML, ar5iv, read for that
  theorem and the "Borel-type extension" discussion).
- The half-line Borel map is also injective, because quasianalyticity holds on [0, ε). Carleman's
  argument also shows it is not onto.
- To conclude non-extendability, one needs a series realised by a *one-sided* class-M germ that is
  realised by *no* two-sided quasianalytic germ of *any* class. Nothing in Carleman's theorem supplies
  that separation, especially uniformly over all quasianalytic classes.
- So the claim is not a trivial consequence. It needs a construction. The seed says it gives one
  ("explicit construction"), but the proof is not in the seed and was not checked.

**Searches (standard mode).** Exact and weaker phrasings were searched: "quasianalytic germs half-line
not extendable", "Denjoy–Carleman [0,∞) extension neighbourhood", "Borel map half-line quasianalytic",
Langenbruch extension of ultradifferentiable functions, and Rolin–Speissegger–Wilkie extension. Every
hit that states the result explicitly is the seed itself (arXiv:1006.4171, June 2010) or dates after
2010-06-20, so all of them were excluded.

**Pre-2010 sources checked:**
- Carleman, *Les fonctions quasi analytiques* (1926). Non-surjectivity of the Borel map, known via
  Thilliez 2005 Thm 3. Read level: secondary statement only. It does not give the claim (see above).
- Thilliez, arXiv:math/0509273 (2005). Read level: full HTML.
  - Covers germs at 0 in R^n, Carleman's theorem, the Borel-type extension question (Petzsche) and
    noetherianity (Problem 1).
  - Does **not** state or pose the half-line extension question.
- Rolin–Speissegger–Wilkie, "Quasianalytic Denjoy–Carleman classes and o-minimality", JAMS 16 (2003)
  751–777. Read level: abstract only.
  - It is the context in which one-sided and restricted quasianalytic functions matter, through
    o-minimal expansions on boxes.
  - The abstract says nothing about extension.
- **Langenbruch, M., Manuscripta Math. 83 (1994) 123–143** (Zbl 0836.46027), on extension of
  ultradifferentiable functions. Read level: **bibliographic record only**. zbMATH returned 403 and
  Springer requires login.
  - **How it was found (disclosed).** The pointer came from a search-engine summary that relayed a
    footnote in a later version of the seed's own PDF, plus post-2010 papers (Nowak arXiv:1310.1303,
    Rainer's survey arXiv:2107.01061). Those carriers are inadmissible, and none of them was read in
    primary form.
  - The 1994 paper itself predates the audit date, so it is admissible prior art for what it actually
    proves.
  - From secondary descriptions (unverified), it seems to treat compact convex K ⊂ int L and the
    absence of extension *operators*, mainly in the non-quasianalytic setting.
  - The absence of a continuous linear extension operator does not imply that an individual germ fails
    to extend. Whether it does depends on whether Langenbruch proves (i) the quasianalytic case,
    (ii) failure for an individual function, and (iii) failure into *any* quasianalytic class.
  - **This is the gap that keeps the verdict UNCLEAR.**

Folklore check: no pre-2010 source found states this as folklore. Experts in quasianalytic geometry
and o-minimality (Bierstone–Milman, Rolin–Speissegger–Wilkie, Nowak) would recognise the question as
natural. Nothing found suggests they considered it settled.

### Applied Verdict: not evaluated (no applied or methodology claim; Type 7 not declared)

### Contribution Type Verdicts (mode=full only):
**Type 1 (new theorem): UNCLEAR, conditional PASS.**
- Bar applied: not known, not folklore, not a trivial consequence, and a non-routine proof.
- Not trivial: the Carleman derivation breaks, see above.
- No pre-2010 statement was found.
- It becomes PASS if Langenbruch 1994, read in primary form, does not already prove that an individual
  one-sided quasianalytic germ fails to extend, and if the proof checks.
- It becomes FAIL (KNOWN) if Langenbruch 1994 contains reading (b), or reading (a) with an
  individual-function statement.

Types 2–6: **not claimed, not evaluated.**
- An unclaimed but plausible Type 5 framing: the result closes off quasianalytic extension as a tool
  for reducing one-sided to two-sided o-minimal or quasianalytic geometry.
- It is not used for the verdict.

### Cross-reference
- The only claimed type is a theorem.
- The components (Carleman non-surjectivity, Denjoy–Carleman quasianalyticity on half-lines) are
  classical, and the assembly is not a short consequence of them.
- The novelty question turns on one unread primary source (Langenbruch 1994).
- The seed's proof is not available in the seed, so correctness is unverified. This is a limitation,
  not a correctness failure. No internal inconsistency was found.

### Recommendation
**Needs deeper audit, then proceed to Phase 3 if it clears.**
1. Read Langenbruch, Manuscripta Math. 83 (1994), in primary form, against the three questions in the
   Langenbruch entry above.
2. Fix the scope to reading (b) explicitly.
3. Check the construction by hand.

Not parked: no bar has been shown to fail.

### Referee estimate: ACCEPT-LIKELY
Venue class: research journal (short-note scale, e.g. a Proceedings-type or Comptes-rendus-type venue)
Value carried by: factor 1 (new theorem: one-sided quasianalytic germs need not extend, with sharp
analytic exception)
Main risk a referee would raise: overlap with Langenbruch's 1994 extension results for
ultradifferentiable classes, which would need to be credited and distinguished. The second risk is
ambiguity over the target class of the extension (same M, or any quasianalytic class).

**Sources and read levels (all checked 2026-10-26):**
- Thilliez, arXiv:math/0509273 (2005): full HTML (ar5iv).
- Rolin–Speissegger–Wilkie, JAMS 2003: abstract.
- Langenbruch, Manuscripta Math. 1994: bibliographic record only.
- Carleman 1926: secondary statement.
- Excluded as post-dated or the seed itself: arXiv:1006.4171, 1310.1303, 1405.2840, 1212.4265,
  1303.4424 and 2107.01061.
- Undatable: I could not establish the date of the univ-lille.fr PDF version of the seed or of its
  footnote. It is treated as the seed and excluded.
