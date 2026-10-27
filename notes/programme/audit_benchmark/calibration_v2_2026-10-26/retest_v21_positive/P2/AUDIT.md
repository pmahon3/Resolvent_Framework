## Audit: seed.md (mode: full)

Audit date (per AS_OF.md): 2023-02-09. Only sources dated on or before 2023-02-09 are used as prior
art. The seed's own work, under any name, is excluded. Searches were run on 2026-10-27. Sources that
search returned with later dates were set aside (see "Excluded sources").

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)

The seed declares types but does not state the per-type bars it commits to clearing. This is a minor
Phase-1 omission. The seed also contains **no proof**, only the statement and a one-line sketch of the
method. Correctness therefore cannot be verified from the submission as given (see Cross-reference).

### Pure Verdict: NOVEL (statement), with correctness unverifiable from the seed

**Stripped statement.** Write r₃(N) for the size of the largest subset of {1,…,N} with no nontrivial
3-AP. The claim is r₃(N) ≤ N·exp(−c(log N)^β) for some absolute β > 0. This is a quasi-polynomial
(Behrend-shape) upper bound.

**Consistency check.** Behrend (1946) gives 3-AP-free sets of density exp(−C√log N). So the claim can
hold only for β ≤ 1/2. A claim of "some β > 0" does not contradict Behrend. If true, it would match
Behrend's shape up to the value of the exponent.

**Prior art up to 2023-02-09:**
- **Bloom–Sisask, "Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions",
  arXiv:2007.03528.** v1 is dated 2020-07-07, v2 2021-09-01, so both predate the audit date. *Read
  level: abstract plus introduction (ar5iv HTML, about the first 100k characters), read 2026-10-27.*
  - Main theorem: r₃(N) ≪ N/(log N)^{1+c}. Before it, the best was N/(log N)^{1−o(1)}, with proofs by
    Sanders, Bloom, Bloom–Sisask and Schoen.
  - Method: Bateman–Katz-style analysis of the structure of the spectrum, plus "spectral boosting",
    plus Croot–Sisask almost-periodicity. The authors say their c "would certainly be very small".
  - The paper claims nothing near quasi-polynomial. This confirms the seed's account of the previous
    bound.
- **Bateman–Katz** (cap sets in F₃ⁿ, |A| ≪ 3ⁿ/n^{1+ε}). Known only from secondary sources: the
  Bloom–Sisask introduction and the 2024 survey arXiv:2408.02328, which I used for this citation only,
  not as prior art. *I did not read the original paper.*
- **Croot–Lev–Pach and Ellenberg–Gijswijt** (polynomial method, 2016–17). In F_pⁿ they give
  exponential bounds (p−δ_p)ⁿ. So the *finite-field* bound itself was already far stronger than any
  analytic bound. Per the Bloom–Sisask introduction: "Such algebraic methods have not been successfully
  adapted to the integers." *Read level: secondary source (Bloom–Sisask introduction).*
- **Peluse, "Recent progress on bounds for sets with no three terms in arithmetic progression"**
  (Bourbaki), arXiv:2206.10037 v1, dated 2022-06-20. *Read level: abstract only (the PDF could not be
  extracted), 2026-10-27.* It surveys Bloom–Sisask and the polynomial method. Nothing found indicates a
  quasi-polynomial Roth bound before the audit date.

**Searches.** Run under the names "quasi-polynomial Roth bound", "exp(−c(log N)^c) three-term
progressions", "Behrend-type upper bound", and finite-field 3-AP / cap-set density bounds. No source
dated on or before 2023-02-09 states or claims the result. Every hit for that bound was the seed's own
work or later, and was excluded.

**Verdict.**
- The integer statement is NOT known. It is not folklore, and it is not a routine consequence of
  existing techniques: it is a jump from (log N)^{−1−c} to exp(−(log N)^β) in density.
- This verdict covers the *statement*, not the proof.
- The finite-field part is not new as a *bound*, because of the polynomial method. Its claimed value
  is the *analytic technique*.

### Applied Verdict: not evaluated (not applicable)

No methodology or computational claim is made. Practitioner test: n/a.

### Contribution Type Verdicts (mode=full only):

**Type 1 (New theorem): PASS, conditional on correctness.**
- Bar: the statement must not be known, folklore or routine, and the proof must be non-routine. The
  statement clears this bar (see the Pure verdict). Clearing it would settle the *shape* of r₃(N),
  leaving open only the exponent β ≤ 1/2.
- The proof is not in the seed, so the "proof is non-routine" half of the bar can be judged only from
  the sketch. A sketch claiming a new analytic method does count as non-routine.
- Condition: an independent check of the full proof.

**Type 3 (Unifying framework): FAIL.**
- Bar: a unification of *previously unrelated* results that enables method transfer.
- Transferring methods from F_qⁿ to {1,…,N} is the established finite-field-model paradigm: Green's
  "finite field models" programme, Bourgain, Sanders, Bateman–Katz to Bloom–Sisask. The two domains
  are not previously unrelated, and the seed proposes no new unifying structure.
- The transfer the seed describes is real and concrete: new F_qⁿ techniques are adapted to ℤ. That is
  method transfer *inside a known framework*. It is part of the Type 1 proof (or would count as a
  Type 2 technique contribution), not a Type 3 framework.
- Type 2 was not declared, so it was not scored. Note: the technique would likely clear Type 2(a),
  "a technique applicable elsewhere", if the proof holds.

### Cross-reference

- The contribution is a theorem (Type 1). The "framework" (Type 3) is the standard finite-field-model
  route, so it is not a separate contribution.
- Main open risk: **correctness**. The claimed improvement is dramatic: it reaches Behrend shape where
  the prior state of the art was a log-power. The seed provides no proof to check.
- No prior owner was found. Two prior-art sources were read only at abstract or secondary level:
  Bateman–Katz original, and the Peluse survey body. The nearest prior work, Bloom–Sisask, was read
  past its abstract (introduction).

### Recommendation

Proceed to Phase 3, scoped to **Type 1 only**. A full, independent verification of the proof is
required first (Lean or line-by-line hand check, per programme rules).
- Types evaluated: 1 (pass, conditional on correctness) and 3 (fail: established finite-field-model
  transfer, not a new unification).
- Undeclared Type 2 is a plausible secondary label for the technique.

Bearing on WHY.md (one line): none directly. This is additive combinatorics, with no bearing on
local-to-global gluing beyond a loose "local Fourier structure → global density" rhyme.

### Referee estimate: ACCEPT-LIKELY (conditional on the full proof checking out)
Venue class: research journal (top general venue)
Value carried by: factor 1 (sharp improvement of a central bound: from (log N)^{−1−c} to quasi-polynomial, Behrend shape)
Main risk a referee would raise: whether a jump this large is correct. The seed itself has no proof, so the referee's decision rests entirely on verifying the full manuscript.

**Caps check.**
- Pure verdict UNCLEAR → at most BORDERLINE: not engaged (verdict is NOVEL).
- ACCEPT-LIKELY on factor 1 needs the nearest prior work read past abstract level: satisfied. The
  Bloom–Sisask introduction was read (ar5iv, 2026-10-27).
- Owner found and not credited → REJECT-LIKELY: not engaged (no owner found).
- Caveat outside the caps: the "unverifiable central claim" count-against applies to the seed text as
  submitted. The estimate assumes a referee holds a full proof. With only the seed text in hand, the
  honest estimate would be BORDERLINE (unverifiable).

### Excluded sources (post-2023-02-09 or the seed's own work)
- arXiv:2408.02328 (2024 survey). Used only as a secondary pointer to the content of Bateman–Katz,
  not as prior art.
- arXiv:2308.06600 (Aug 2023), a Cornell talk page and a Bourbaki 2023 text. All set aside as later
  than the audit date or covering the seed's own work.
- The Peluse survey v2 (2023-09) was set aside; only v1 (2022-06-20) was counted.
- Date uncertainty: none for the sources that were counted.
