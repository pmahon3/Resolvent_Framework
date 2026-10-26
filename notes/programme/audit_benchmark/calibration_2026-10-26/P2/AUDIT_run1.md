## Audit: seed.md (mode: full)

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)
The seed declares types but does not state the specific per-type bars it commits to clearing (the framework's Phase 1 requirement). This is noted. It does not change the verdict.

### Pure Verdict: KNOWN

**Stripped statement.** There exists β > 0 such that every A ⊆ {1,…,N} with |A| ≥ 2^{−O((log N)^β)}·N contains a non-trivial 3-term AP (equivalently, r₃(N) ≤ N·exp(−c(log N)^β)). The comparison point is the earlier bound N/(log N)^{1+c}. The method develops finite-field (F_q^n) analytic techniques first and then transfers them to Z/NZ and [N].

**Owner.** Z. Kelley and R. Meka, "Strong Bounds for 3-Progressions", arXiv:2302.05537 (Feb 2023; FOCS 2023). The main theorem in the abstract is the seed's statement almost word for word: the same density 2^{−O((log N)^β)}, the same comparison to (log N)^{1+c}, and the same methodology sentence ("first develop new analytic techniques for … the finite-field setting, then adapt variants … to the integers"). Read level: **abstract** (arXiv abstract page, fetched). The seed is a near-verbatim restatement of that abstract.

**Previous best, as the seed cites it.** The bound N/(log N)^{1+c} is due to T. Bloom and O. Sisask, "Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions" (arXiv:2007.03528, 2020). Read level: **snippet / background knowledge**; not fetched in this audit.

**Later work that subsumes the seed's statement:**
- T. Bloom and O. Sisask, "The Kelley–Meka bounds for sets free of three-term arithmetic progressions", arXiv:2302.07211 (2023). This is an exposition and simplification of Kelley–Meka with an explicit exponent (β = 1/11 in their version; Kelley–Meka's own exponent is usually cited as 1/12). Read level: **snippet** (search result).
- T. Bloom and O. Sisask, "An improvement to the Kelley–Meka bounds on three-term arithmetic progressions", arXiv:2309.02353 (2023). Gives β = 1/9, and says a more elaborate version gives 5/41 (remarks after the proof of Lemma 6). Read level: **snippet** (search result).
- Raghavan, arXiv:2603.27045 (Mar 2026). Gives exp(−c(log N)^{1/6}(log log N)^{−1})·N. Read level: **snippet** (search result).

**Hostile checks.**
- Is the statement known? Yes. It is explicitly stated, peer-reviewed, and widely followed up.
- Has it been strengthened? Yes, three times since (β from 1/12 to 1/9 to 5/41 to roughly 1/6).
- Does the seed contain anything that goes beyond Kelley–Meka? No: no new exponent, no new setting, no new mechanism.

Textbook check by theorem number: not needed, because a primary-source owner matches the statement exactly.

### Applied Verdict: not evaluated
No Type 7 claim, and the item has no applied component.

### Contribution Type Verdicts (mode=full only):

**Type 1 (New theorem): FAIL.** The statement is the main theorem of Kelley–Meka 2023 (arXiv:2302.05537, abstract) and has since been strengthened (Bloom–Sisask 2309.02353, β = 1/9; Raghavan 2603.27045, about 1/6). Bar: "not known." It is known, so park.

**Type 3 (Unifying framework): FAIL.** The only candidate for unification is the finite-field-to-integers transfer. That transfer is (a) the method of Kelley–Meka itself: their abstract states it, and the integer case is adapted from F_q^n. It is also (b) a long-standing paradigm in additive combinatorics: the finite-field model as testing ground (Green, "Finite field models in additive combinatorics", 2005, read level **background knowledge, not fetched**; Meshulam 1995 vs Roth 1953; Bourgain/Sanders). The bar asks for a method transfer that the framework *newly* enables. The seed demonstrates no transfer beyond what the owner already did, and gives no framework beyond the standard model-setting heuristic.

**Undeclared types considered:**
- Type 2 (new proof): not applicable. No alternative proof is offered.
- Type 6 (exposition): would fail. Bloom–Sisask 2302.07211 is already an expository simplification.

### Cross-reference
Type 1 and Type 3 fail for the same reason: both the theorem and the finite-field-to-integers transfer belong to Kelley–Meka 2023. The seed restates the owner's abstract and adds no new component, assembly or framing. Nothing survives to be scoped to Phase 3.

### Bearing on WHY.md
None directly. This is a density/Ramsey-type result in additive combinatorics. It has no bearing on local-to-global coherence of queries beyond a loose "local structure forces global pattern" rhyme, which is an analogy and not a lens.

### Recommendation
**Park.** Types evaluated: 1 (FAIL: known, Kelley–Meka 2023 main theorem) and 3 (FAIL: the transfer is the owner's method and standard paradigm). The same exposition is already accessible (Bloom–Sisask 2302.07211), so open-question status is unavailable. Record owned_by: Kelley–Meka arXiv:2302.05537, region = "3-AP-free density in [N] at quasi-polynomial scale exp(−(log N)^β)", verified at abstract level.

Sources:
- [Kelley–Meka, arXiv:2302.05537](https://arxiv.org/abs/2302.05537) (abstract)
- [Bloom–Sisask, arXiv:2302.07211](https://arxiv.org/pdf/2302.07211) (snippet)
- [Bloom–Sisask, arXiv:2309.02353](https://arxiv.org/pdf/2309.02353) (snippet)
- [Raghavan, arXiv:2603.27045](https://arxiv.org/pdf/2603.27045) (snippet)
