## Audit: seed.md — "ZFC atomless, non-σ-complete Boolean algebra with no strictly positive σ-additive measure" (mode: full)

Run from memory only (no web). Every citation carries a confidence mark.

### Declared contribution type(s): Type 1 (new theorem), Type 5 (impossibility / closes suspected independence)

The seed declares types, but it does not state the bar it commits to clearing for each one. That is a minor readiness defect.

### Pure Verdict: KNOWN (trivial consequence of standard facts; the combination is folklore-level)

**1. The statement without its vocabulary.** There exists, in ZFC, a Boolean algebra A that is atomless and not σ-complete, and on which no σ-additive measure μ has μ(a) > 0 for every a ≠ 0.

**2. Kill A: a three-line ZFC witness, P(ω)/fin.**
- *Atomless.* Every infinite subset of ω splits into two infinite pieces. (certain)
- *Not σ-complete.* Partition ω into infinite sets A_n. The family {[A_n]} has no least upper bound in P(ω)/fin. Any upper bound [B] has B ⊇* A_n for every n. Removing one point of each B ∩ A_n gives a strictly smaller upper bound. Standard. (certain; e.g. Koppelberg, *Handbook of Boolean Algebras* vol. 1, ch. on P(ω)/fin, and Hausdorff-gap material; exact section number unsure)
- *No strictly positive measure, not even a finitely additive one.* An almost-disjoint family of size 2^ℵ₀ gives an uncountable antichain. A strictly positive finitely additive probability forces ccc: for some n, uncountably many disjoint elements would each have measure > 1/n, which is impossible. (certain. This is the elementary half of Kelley 1959, "Measures on Boolean algebras", Pacific J. Math. 9, 1165–1177: strictly positive measure ⟹ positive intersection number ⟹ σ-bounded cc ⟹ ccc; likely on exact pagination)

So (i), (ii) and (iii) hold in ZFC, and (iii) holds even in its strongest, finitely additive form. Argyros's deep theorem is not needed. Argyros's examples matter because they are **ccc**, and the seed's statement never asks for ccc.

**3. Kill B: the combination reduces to (iii) alone, even with ccc added.** Take any ZFC algebra B with no strictly positive measure, for example Gaifman's ccc example. Form A = (B ⊕ Fr(ω)) × Fr(ω), where Fr(ω) is the countable free (atomless) algebra and ⊕ is the free product.
- A is atomless, since both factors are atomless.
- A is not σ-complete, since the factor Fr(ω) is not σ-complete and σ-completeness passes to factors of a product.
- A carries no strictly positive measure: such a measure would restrict along B ↪ B ⊕ Fr(ω) to a strictly positive measure on B (after renormalising, it stays strictly positive on the first factor).
- If B is ccc, A is ccc: Fr(ω) is σ-centred, ccc × σ-centred is ccc, and finite products of ccc algebras are ccc. (certain for the first three points; likely for ccc preservation)

Even the strengthened statement "plus ccc" is therefore a trivial corollary of:
- Gaifman 1964, "Concerning measures on Boolean algebras", Pacific J. Math. 14, 61–73: a ccc Boolean algebra in ZFC with no strictly positive measure. (likely on the bibliographic details; certain that Gaifman gave such an example)
- or Argyros 1983 (compact ccc spaces without strictly positive measure, Pacific J. Math., c. vol. 105). (likely on the venue; unsure on the volume)

**4. Why the near-miss table misled.** In the literature people actually work in (von Neumann's and Maharam's problems), completeness or σ-completeness is part of the *hypothesis*. Examples:
- Maharam 1947, Ann. Math. 48 (likely);
- Talagrand 2008, Ann. Math. 168, "Maharam's problem": an exhaustive submeasure that is not equivalent to a measure, which yields a complete Maharam algebra that is not a measure algebra (certain on the result, likely on the citation);
- Balcar–Jech–Pazák 2005 (Bull. LMS), the consistency of "every ccc weakly distributive complete BA is Maharam" (likely);
- Velickovic 2005 (Adv. Math.), the same under PFA (likely).

A table drawn from that literature contains only complete or σ-complete algebras because of how its entries were selected, not because of any barrier. Dropping σ-completeness makes the problem *easier*, not harder, and no one has suggested it is independent.

**5. Claim-by-claim checks of the seed's own assertions.**
- *Zero-dimensionality of Y.* Strict positivity on Clop(Y) matches strict positivity of a Radon measure on Y only when Y is zero-dimensional. If Y is connected, Clop(Y) = {0,1}, which trivially carries a strictly positive measure. The seed must show that Argyros's Y is zero-dimensional, or else work with an algebra Argyros actually built. (certain on the logic; unsure whether Argyros's space is zero-dimensional)
- *"Pre-Gleason spaces."* I cannot confirm that this describes Argyros 1983. Treat the attribution as UNVERIFIED.
- *"Gap family at the base point" check of (i) and (ii).* Not verifiable from memory. (unsure)
- *Near-miss premise.* It may be false outright, not merely biased. Gaifman-type algebras and the clopen algebras of Argyros-type spaces are typically not σ-complete. If the table contained them, its claim that every entry was complete or σ-complete was wrong. (unsure)
None of these points affects the verdict, since the claim is witnessed independently above.

**6. Ambiguity in "σ-additive".** On a non-σ-complete algebra, "σ-additive" means either (a) additive over those countable disjoint families whose supremum exists, or (b) induced by a countably additive Baire/Borel measure on the Stone space. Under (b), every finitely additive measure qualifies, by the Carathéodory/Stone extension, since compactness makes countable additivity automatic on clopen sets (certain). Either way, Kill A kills the finitely additive form, so it kills both readings.
*Measure convention.* Kill A assumes finite measures. If [0,∞] values are allowed, the measure that is 0 on 0 and ∞ elsewhere is strictly positive and σ-additive on every algebra, so the claim only has content for finite measures. The semi-finite case dies too: P(ω)/fin is homogeneous, so below any element of finite positive measure sits a copy of P(ω)/fin with an uncountable antichain, and the pigeonhole argument applies there.

**Searched (from memory) under:** strictly positive measure; Kelley intersection number; Gaifman's example; Horn–Tarski problem (σ-finite cc versus measures; Todorcevic 2004 and Thümmel on Horn–Tarski, likely); Maharam / von Neumann problem; Argyros; measure-free ccc algebras; P(ω)/fin; free products and ccc; Fremlin, *Measure Theory* vol. 3, ch. 39 ("Measurable algebras", §391 on the existence of strictly positive additive functionals, likely); Koppelberg's Handbook vol. 1.

### Applied Verdict: FAIL
- Decision test: no practitioner's action changes. This is a pure existence statement in Boolean algebra.
- Practitioner test: there is no method, no computational comparison and no regime boundary, so the kill condition "no computational evidence feasible" is met.

### Contribution Type Verdicts (mode=full only):

**Type 1 (new theorem): FAIL.**
- Bar: the statement must not be known, folklore, or a trivial consequence.
- The statement is a three-line consequence of standard facts. P(ω)/fin witnesses it directly in ZFC, and any measure-free algebra (Gaifman 1964) becomes a witness after a product/free-product adjustment.
- The proof is routine. The only non-trivial ingredient, Argyros's theorem, is both cited and unnecessary.

**Type 5 (impossibility / closes suspected independence): FAIL.**
- Bar: it must (a) close a direction people are actively pursuing, or (b) non-trivially sharpen an existing impossibility.
- (a) fails: the "suspected independence" came from a biased sample (§4), and no one in the literature suspected or pursued it.
- (b) fails: the result *weakens* the known impossibilities (Gaifman's and Argyros's examples are ccc; this one need not be) instead of sharpening them.
- This is the "we already knew this couldn't work" park condition.

No undeclared types are claimed. Type 6 would also fail: the material is well covered in Fremlin vol. 3 ch. 39 and Koppelberg's Handbook.

### Cross-reference
Both claimed types fail for the same reason. The combination (i)+(ii)+(iii) has no content beyond (iii), and (iii) without ccc holds for every non-ccc algebra. The seed's own witness (Argyros) is stronger than its claim, which tells you the claim is pitched below the known frontier. The "independence" suspicion was a sampling artefact of a table drawn from Maharam-problem literature, where completeness is assumed.

The neighbouring questions are already owned:
- ccc + complete + no strictly positive measure, in ZFC, is not a live question. The Dedekind completion of Gaifman's 1964 algebra witnesses it. The algebra is dense in its completion, so ccc carries over, and a strictly positive measure on the completion would restrict to one on the algebra. (certain on the argument)
- The weakly distributive (Maharam) strengthening is owned by Talagrand 2008.
- The consistency and Horn–Tarski variants are owned by Balcar–Jech–Pazák, Velickovic and Todorcevic.

Bearing on WHY.md: the item says nothing about the question of when local views add up to one world. It only re-confirms that "no global strictly positive state" is cheap once antichains are uncountable. The interesting cases are the ccc ones, where every local constraint looks fine.

### Recommendation
**Park.**
- Evaluated: Type 1 (FAIL: trivial consequence, P(ω)/fin in three lines) and Type 5 (FAIL: no live direction; weakens rather than sharpens Gaifman 1964 and Argyros 1983).
- Not an open question: the stated problem is solved in ZFC by elementary means.
- If anything is retained, record the owned region as `owned_by`: Kelley 1959 (the elementary non-ccc obstruction) + Gaifman 1964 (a ccc example; its completion covers the complete case), with Talagrand 2008 for the weakly distributive (Maharam) frontier. Note the verification: from memory, unchecked against primary sources in this run.

**Single most damaging prior source.** Gaifman 1964, Pacific J. Math. 14. It gives a ZFC ccc algebra with no strictly positive measure, and §3's product adjustment then yields the seed's claim even with ccc added. Argyros is redundant for this claim. (For the claim exactly as stated, the elementary P(ω)/fin argument of §2 suffices; it is textbook material, not tied to one paper.)
