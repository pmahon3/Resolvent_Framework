## Audit: seed.md, quasipolynomial density bound for 3-APs in {1..N} (mode: full)

Audit date (per AS_OF.md): 2023-02-09. Only sources dated on or before this date are used. The seed's own work, under any title, is not treated as prior art. Read levels: **[A]** = abstract/listing checked online on 2026-10-26; **[K]** = from my background knowledge of the literature, not re-checked online in this audit. All dates given are publication or arXiv dates and are all well before 2023-02-09.

### Declared contribution type(s): Type 1 (new theorem), Type 3 (unifying framework)

The types are declared. The seed does not state the per-type bars it commits to clearing, so the declaration is only partial.

### Pure Verdict: NOVEL (as of 2023-02-09; correctness not verifiable from the seed)

**Stripped statement.** There is an absolute β > 0 such that r₃(N) ≤ N·exp(−c(log N)^β). Here r₃(N) is the size of the largest subset of [N] with no nontrivial 3-term AP. This is a quasipolynomial upper bound for Roth's theorem.

**Prior art checked (all predate 2023-02-09):**
- Roth 1953: r₃(N) ≪ N/log log N. [K]
- Heath-Brown 1987 and Szemerédi 1990 gave N/(log N)^c. Bourgain 1999 and 2008 gave (log log N)^{O(1)}/(log N)^{1/2} and then 2/3. Sanders 2011 (Annals) gave (log log N)^6/log N. Sanders 2012 gave (log log N)^4/log N. Bloom 2016 gave (log log N)^4/log N by a different route. Bloom–Sisask 2019 (arXiv:1810.12791) gave the logarithmic bound by almost-periodicity. [K; 1810.12791 listing seen, A]
- **Bloom–Sisask, arXiv:2007.03528 (submitted 7 Jul 2020, v2 1 Sep 2021):** N/(log N)^{1+c}. This is the "previous best" the seed cites. It uses Bateman–Katz-type spectral structure plus almost-periodicity. [A]
- **Schoen–Sisask, arXiv:1408.2568 (11 Aug 2014), Forum Math. Sigma 2016:** for x+y+z = 3w (four variables), N/exp(c(log N)^{1/7}). This is the closest neighbour: a Behrend-shaped bound already exists for a four-variable equation. [A] Related: Schoen–Shkredov 2014 proved a similar bound for six-variable equations. [K]
- Behrend 1946: r₃(N) ≥ N·exp(−C√(log N)). So any valid β satisfies β ≤ 1/2, and the claim is consistent with known lower bounds as long as β < 1/2. [K]
- Finite-field model: Meshulam 1995. Bateman–Katz 2012 (JAMS) gave a cap-set bound of order 3^n/n^{1+ε}. Croot–Lev–Pach and Ellenberg–Gijswijt 2016/2017 (Annals) gave power savings by the polynomial method. The analytic, density-increment methods in F_q^n had not reached exp(−n^{c}) density bounds by analytic means. [K]
- Green's "Finite field models in additive combinatorics" (2005) describes the finite-field-first heuristic. [K]

**Kill attempts.**
1. Restatement or trivial consequence? No. Schoen–Sisask needs four variables, which give an extra convolution factor for "free" L^p/almost-periodicity gains. Three variables were the known barrier, and every three-variable bound up to 2/2023 was log-type.
2. Folklore? No. Experts regarded the quasipolynomial shape for 3-APs as far out of reach. Bloom–Sisask's 1+c was celebrated as "breaking the logarithmic barrier".
3. Implied by the polynomial method? No. Ellenberg–Gijswijt does not transfer to ℤ: there is a Behrend-type lower bound in ℤ and no power saving is possible.

No source dated on or before 2023-02-09 states this bound for 3-APs. The search was limited to standard mode, and the bound would be a landmark if it were in print. **NOVEL.**

**Correctness.** The seed is a three-sentence abstract with no proof, so correctness cannot be checked. It is not falsified by Behrend as long as β < 1/2, and it does not say that it is. A referee would need the full argument. The highest risk lies in the claimed passage from the finite-field argument to ℤ through Bohr sets, since that is where earlier transfers lost the most.

### Applied Verdict: not evaluated (pure mathematics; Type 7 not claimed; applied test not applicable)

### Contribution Type Verdicts (mode=full):

**Type 1 (new theorem): PASS (conditional on correctness).** The statement is not known, not folklore and not a trivial consequence. It improves the record from a power of log to a quasipolynomial, matching Behrend's shape up to the constant β. The proof cannot be routine, because the obvious routes were tried and stopped at log-type bounds.

**Type 3 (unifying framework): FAIL.** The bar is a framework under which previously unrelated results become instances of one phenomenon, with a technique transferring from domain A to domain B through that framework. The seed describes developing techniques in F_q^n and then adapting them to [N]. That is the standard finite-field-model workflow (Green 2005; Bourgain, Sanders, Bloom–Sisask all work this way). It is not a new unification, and the two domains were not previously unrelated. The transfer is method development within one field, and it is part of the Type 1 proof, not a separate framework contribution. Type 2 is not claimed and would not apply, since the result is not known.

### Cross-reference

All of the value sits in Type 1. The Type 3 claim relabels the proof strategy as a framework and adds nothing to the case. The new analytic tools may well become reusable machinery, which would be the substance behind a Type 3 claim. That is speculative on 2023-02-09, and the seed shows no concrete transfer beyond its own theorem.

**Bearing on the why** (one line): this is a local-to-global density question, where a local density condition forces a global configuration. It is a lens only and has no direct bearing on the programme's gluing question.

### Recommendation

**Proceed to Phase 3, scoped to Type 1 only.** Drop the Type 3 claim. The first task is a full verification of the proof, especially the integer transfer, before anything else.

### Referee estimate: ACCEPT-LIKELY
Venue class: research journal (top tier: Annals / Acta / JAMS / FOCS-level, if correct)
Value carried by: factor 1 (sharp improvement of a central bound: log-power to quasipolynomial, matching Behrend's shape)
Main risk a referee would raise: correctness of the new analytic machinery and of its transfer from F_q^n to [N] via Bohr sets; the abstract gives no proof to check, and a too-good-to-be-true jump calls for line-by-line verification.

### Sources
- [Bloom–Sisask, arXiv:2007.03528](https://arxiv.org/abs/2007.03528v1): 7 Jul 2020, v2 1 Sep 2021. Abstract/listing read [A], 2026-10-26.
- [Bloom–Sisask, arXiv:1810.12791](https://ar5iv.arxiv.org/html/1810.12791): Oct 2018. Title/listing only [A].
- [Schoen–Sisask, arXiv:1408.2568](https://arxiv.org/abs/1408.2568v1): 11 Aug 2014; Forum Math. Sigma 2016. Abstract read [A], 2026-10-26.
- Roth 1953; Behrend 1946; Heath-Brown 1987; Szemerédi 1990; Bourgain 1999/2008; Sanders 2011/2012; Bloom 2016; Meshulam 1995; Bateman–Katz 2012; Ellenberg–Gijswijt 2017; Green 2005. All [K], all predate 2023-02-09.
- Undatable sources: none. Every source used has an explicit date before 2023-02-09.
