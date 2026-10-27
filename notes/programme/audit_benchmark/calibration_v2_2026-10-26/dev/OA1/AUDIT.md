## Audit: seed.md, "Bell's theorem fails for Clifford-algebra-valued local hidden variables" (mode: full)

Audit date (AS_OF.md): **2007-03-19**. Only sources dated on or before that day are used. Read levels: **[P]** = primary source read or fetched; **[A]** = abstract or bibliographic record seen via search; **[K]** = standard knowledge of a classical result, not re-read in this session. All lookups were done 2026-10-26.

### Declared contribution type(s): Type 1 (new theorem), Type 5 (impossibility/counterexample)
The seed declares its types but does not state the per-type bars it commits to clearing, so it only partly meets the Phase-1 requirement. It does not name Types 2, 3, 4 or 6, and none is evaluated here.

### Pure Verdict: UNCLEAR on novelty; the central claim is not established and, as stated, is false
**What the seed actually claims, with the vocabulary stripped.** There is a local deterministic model: outcome functions A(a,λ) and B(b,λ), where the hidden variable λ ranges over a Clifford algebra and the outcomes do not depend on the remote setting. The model reproduces E(a,b) = −a·b and so violates CHSH up to 2√2.

**Correctness. This is the decisive point, and a hostile referee in 2007 would raise it at once.**
- The CHSH derivation never uses the value space of λ. It needs only three things:
  1. each recorded outcome A(a,λ), B(b,λ) is a number in [−1,1] (in the EPR-Bohm experiment, ±1);
  2. locality: A does not depend on b, and B does not depend on a;
  3. the distribution of λ does not depend on (a,b).

  Under these, |A(a)B(b) + A(a)B(b′) + A(a′)B(b) − A(a′)B(b′)| ≤ 2 holds pointwise in λ. Integrating gives |S| ≤ 2. Sources: [K] Bell, *Physics* 1, 195 (1964); [K] Clauser–Horne–Shimony–Holt, *PRL* 23, 880 (1969); [K] Bell, *Speakable and Unspeakable* (1987), ch. 2 and 16. Fine (*PRL* 48, 291 (1982); *J. Math. Phys.* 23, 1306 (1982)) [K] shows the bound is equivalent to a joint distribution of the four ±1 variables. That again uses only the outcome values, not λ.
- So making λ Clifford-valued cannot break the bound if the model's outcomes are ±1 numbers. A violation would need one of two things:
  - **(i) The outcomes are not ±1 scalars.** For example, they are bivectors or other multivectors whose noncommutative product is what gets "correlated". Then the model does not describe the EPR-Bohm experiment, whose detectors record ±1 clicks, and the comparison with CHSH is a category error.
  - **(ii) Covert dependence of one wing on the other wing's setting, or of the λ-measure on the settings.** That is nonlocality or a measurement-dependence loophole, which the seed explicitly denies.

  "Clifford products are noncommutative" is not a mechanism. In CHSH the product A·B is a product of two real numbers per run, and real numbers commute.
- Without the model's explicit definitions of A, B and the λ-measure (the seed gives none), this audit cannot say *which* of (i) or (ii) occurs. That the claim *as stated* contradicts a two-line inequality is certain [HAND: the pointwise bound above, checked by inspection]. **Correctness problem: the central claim is false as stated, or else it changes what an "outcome" is.**

**Novelty.** The seed belongs to a known genre: local models claimed to evade Bell by enlarging the hidden-variable space.
- Hess–Philipp, *PNAS* 98, 14224 (2001) [K]: time-dependent hidden variables. It was rebutted by Gill–Weihs–Zeilinger–Żukowski, "No time loophole in Bell's theorem; the Hess-Philipp model is non-local", *PNAS* 99, 14632 (2002) [A] (arXiv:quant-ph/0208187, 2002, so it predates 2007-03-19).
- Pitowsky, *PRL* 48, 1299 (1982) [K]: non-measurable hidden variables.

The specific use of Clifford/geometric algebra for EPR correlations also has precedent. Doran, Lasenby, Gull, Somaroo and Challinor, "Spacetime Algebra and Electron Physics", *Adv. Imaging Electron Phys.* 95, 271 (1996) [A], and Somaroo–Lasenby–Doran, *J. Math. Phys.* 40 (1999) [A], treat two-particle spin and entanglement in the multiparticle spacetime algebra. That is a reformulation of quantum mechanics, not a local hidden-variable model, and it does not claim a Bell violation from locality. So the seed's precise model may be new as a construction. But a model that does not actually satisfy Bell's hypotheses is not a counterexample to Bell, so "new model" does not amount to a "new theorem". Novelty: UNCLEAR. Correctness: FAILS.

Date caveat: every source cited above is dated 1964–2002. None was ambiguous with respect to 2007-03-19.

### Applied Verdict: not evaluated (Type 7 not claimed)
Practitioner test, briefly: an experimentalist records ±1 coincidences. A model whose "outcomes" are multivectors makes no prediction for those records that differs from QM, and offers no local mechanism for them.

### Contribution Type Verdicts (mode=full only):
**Type 1 (new theorem): FAIL.** The bar requires a true statement with proof. The claim "Bell's theorem fails for Clifford-valued λ" contradicts the CHSH derivation, which does not depend on λ's value space. Either the outcomes are not the experiment's ±1 outcomes, or locality or measurement independence is violated covertly. Neither is a theorem refuting Bell.

**Type 5 (impossibility/counterexample): FAIL.** The seed claims to be a counterexample to an impossibility theorem.
- **Bar (a):** it would close off an active direction, here Bell-based no-go reasoning. But a valid counterexample must satisfy the theorem's hypotheses: ±1 local outcome functions and setting-independent λ. As described, the model either fails a hypothesis or misidentifies the outcome. It therefore closes off nothing.
- **Bar (b):** it does not sharpen any existing impossibility. It sits in the Hess–Philipp and Pitowsky genre, which is already answered by Gill et al. (2002) and by Fine's joint-distribution theorem.

### Cross-reference
The novelty question is moot because correctness fails first. The Clifford-algebra construction might be a new piece of formalism, but the seed's value rests entirely on its being a local counterexample to Bell, and that claim does not survive the hypotheses check. No type's bar is cleared.

### Recommendation
**Park.**
- Types evaluated: 1 and 5. Both FAIL on correctness: the claimed violation is incompatible with the hypotheses of CHSH.
- If revived, the seed must first state the outcome functions explicitly as maps to {±1} and show A independent of b and the λ-measure independent of (a,b). It should expect the construction to fail at that step.
- One line on WHY.md's question (do local views add up to one world?): Bell/CHSH is the canonical case where local views do *not* add up. A "local model" that escapes it by changing what counts as an answer is a hidden idealisation, not composition.

### Referee estimate: REJECT-LIKELY
Venue class: none (a research journal such as PRL/PRA/Found. Phys. would reject it on correctness)
Value carried by: none
Main risk a referee would raise: the CHSH bound holds pointwise for any ±1-valued local outcome functions whatever λ's value space, so the model either does not output ±1 results or is covertly nonlocal or setting-dependent; the central claim is wrong.

Sources (lookup 2026-10-26):
- [Gill–Weihs–Zeilinger–Żukowski, PNAS 2002 / quant-ph/0208187](https://arxiv.org/abs/quant-ph/0208187) [A]
- [Utrecht record of the same paper](https://research-portal.uu.nl/en/publications/no-time-loophole-in-bells-theorem-the-hess-philipp-model-is-non-l/) [A]
- [Doran et al., Spacetime Algebra and Electron Physics (1996), quant-ph/0509178](https://arxiv.org/abs/quant-ph/0509178) [A]; note that the arXiv posting date (2005) differs from the publication date (1996). Both predate the audit date.
- [Somaroo–Lasenby–Doran, multiparticle STA, J. Math. Phys. 1999](https://geometry.mrao.cam.ac.uk/?p=180) [A]
