## Audit: seed.md — "a ZFC atomless, non-σ-complete Boolean algebra with no strictly positive σ-additive measure" (mode: full)

Date: 2026-10-26. Scope: only the files in this directory were consulted, plus the web. WHY.md is not in scope, so its one-line note is n/a.

### Declared contribution type(s): Type 1 (new theorem), Type 5 (impossibility: closes the suspected ZFC-independence)

The seed declares its types but not the per-type bars it commits to clearing. That is a minor Phase-1 defect and it does not affect the verdict.

---

### Pure Verdict: KNOWN (folklore; a trivial consequence of textbook facts)

**1. The statement without the novel vocabulary.** There is a ZFC Boolean algebra B with:
- (i) B atomless;
- (ii) some countable subset of B has no supremum;
- (iii) no finite measure μ on B is strictly positive and σ-additive.

**2. The kill: B = P(ω)/fin.** All three properties hold in ZFC with elementary proofs. ⟦HAND⟧, each step a few lines and checkable by hand.

- **(i) Atomless.** Every infinite A ⊆ ω splits into two infinite sets, so every nonzero class splits into two nonzero classes.
- **(ii) Not σ-complete.** Let a₀, a₁, … be pairwise disjoint infinite subsets of ω, with classes Aₙ. Take any upper bound X. Remove one element of aₙ from X for each n. The result X′ is still an upper bound, but X \ X′ is infinite, so X′ is strictly smaller. Hence the countable family {Aₙ} has no supremum.
  - Source: Wikipedia, "Complete Boolean algebra", section on non-complete examples. Read level: **full text** of the relevant section; the argument is quoted there verbatim.
- **(iii) No strictly positive σ-additive measure.**
  - *Not ccc.* For x ∈ 2^ω, let A_x = {x↾n : n ∈ ω} ⊆ 2^{<ω} ≅ ω. For x ≠ y, A_x ∩ A_y is finite. This gives an almost disjoint family of size 𝔠, so its classes form an antichain of size 𝔠 in P(ω)/fin. ⟦HAND⟧ This is standard; the web page on almost disjoint sets that I fetched does not give the construction, so the step rests on the hand argument.
  - *A strictly positive finitely additive real measure forces ccc.* Suppose μ is one and {b_α} is an uncountable antichain. Then some n has uncountably many b_α with μ(b_α) > 1/n. Any finite k of them, all disjoint, give total measure > k/n, which exceeds μ(1) once k is large. This contradicts finite additivity.
    - Source: Jech, "Measures on Boolean algebras", arXiv:1705.01006, §1 after Def. 1.1: "Every measure algebra satisfies ccc, the countable chain condition, i.e. every antichain is countable." Read level: **full text** (ar5iv HTML, §1 and §4 read; quote checked).
  - *Both readings of "σ-additive" are killed.* On a non-σ-complete algebra, "σ-additive" can mean (a) additive over the countable disjoint families whose supremum exists in B, or (b) extendable to a measure on a generated σ-algebra. Both readings imply finite additivity, so the ccc argument rules out both. Even a strictly positive *finitely* additive measure is impossible.
  - *Scope.* "Measure" here means finite and real-valued. A [0, ∞]-valued "measure" that gives every nonzero element the value ∞ is degenerate and is excluded by any standard definition. For σ-finite measures the ccc argument also goes through.

**3. Where the argument comes from.** It is the routine pairing of two facts:
- "not ccc ⟹ no strictly positive measure", which is the trivial half of the Horn–Tarski 1948 / Kelley 1959 measure problem;
- a standard non-σ-complete, non-ccc algebra.

Any expert in Boolean algebras or set-theoretic topology would call the combination obvious. The non-trivial theory in this area concerns **ccc** algebras without strictly positive measures:
- Gaifman, *Pacific J. Math.* 14 (1964) 61–73. Read level: **abstract/snippet** (MSP listing and secondary sources). A ccc, indeed σ-bounded cc, algebra with no strictly positive measure.
- Argyros, "On compact spaces without strictly positive measure", *Pacific J. Math.* 105 (1983) 257–272. Read level: **abstract** (MSP page).
- Kelley's criterion: Kelley, *Pacific J. Math.* 9 (1959). Read level: **snippet**, with its statement checked via Jech arXiv:1705.01006 Thm 4.2 / Cor 4.3 (**full text**).
- Fremlin, *Measure Theory* Vol. 3, §391 (391D, 391H–J). Read level: **snippet** of the results-only extract chap39.ro.pdf.

The seed's claim does not require ccc, so the actual content of Argyros's theorem is **not used**. Argyros's space is a much heavier witness than the claim needs. The kill does not depend on checking the seed's "gap family at the base point" argument for (i)–(ii).

**4. The premise "why it seemed open" is a selection artefact.** In the seed's near-miss table every entry was complete or σ-complete. That is a fact about the table, not about the literature. Non-ccc algebras, which have no strictly positive measure for trivial reasons, are rarely tabulated as "measure-free examples" because they are uninteresting. No source I found poses or suggests a ZFC-independence question for (i)+(ii)+(iii).

**5. Searches run (standard mode).**
- Argyros 1983 strictly positive measure;
- Kelley 1959 intersection number;
- P(ω)/fin σ-completeness, ccc and almost disjoint families;
- Fremlin §391;
- Gaifman 1964;
- Koppelberg *Handbook* Vol. 1 on P(ω)/fin.

I did not see the exact Koppelberg proposition number, so none is cited. The facts used are textbook-level and folklore and are derived above in full.

**Remark: a natural strengthening is also not new.** ⟦HAND — unverified beyond this sketch; not claimed by the seed⟧ Suppose ccc is added as a requirement (iv). Let B be any ccc algebra without a strictly positive measure, such as Gaifman's, and let C be the countable atomless algebra. Take (B ⊕ C) × C, where ⊕ is the free product.
- **Atomless:** C splits every nonzero element.
- **ccc:** B is ccc and C is countable, hence σ-centred, so B ⊕ C is ccc; a finite product of ccc algebras is ccc.
- **Not σ-complete:** suprema in a product are computed coordinatewise, and C is not σ-complete.
- **No strictly positive measure:** such a measure would restrict, through B ↪ B ⊕ C ↪ the first factor, to a strictly positive measure on B.

So even the ccc version reduces to Gaifman 1964 (ZFC).

---

### Applied Verdict: not evaluated
No Type 7 claim, and there is no applied or computational content.

---

### Contribution Type Verdicts

**Type 1 (New theorem): FAIL.**
The bar is that the statement is not known, not folklore and not a trivial consequence. It fails on the third count: there is a short derivation, P(ω)/fin with (i) splitting, (ii) the column-shrinking argument and (iii) not ccc ⟹ no strictly positive finitely additive measure (Jech arXiv:1705.01006 §1). The statement is folklore-level and the "proof" is routine.

**Type 5 (Impossibility: closes the suspected independence): FAIL.**
- (a) It closes no direction anyone is actively pursuing. No literature source suspects or poses independence. The suspicion came from the seed's own near-miss table.
- (b) It does not sharpen an existing impossibility. The impossibility of a strictly positive measure on a non-ccc algebra is a direct corollary of the ccc obstruction that has been known since Horn–Tarski/Kelley, so this is "we already knew this couldn't work".
- If ccc is imposed, the result still reduces to Gaifman 1964 (Remark above), so no sharpening survives there either.

**Undeclared types.** None are implicitly claimed. Type 6 (exposition) is not a rescue: the facts are in standard references such as Koppelberg's *Handbook* and Fremlin's *Measure Theory* Vol. 3 §391.

---

### Cross-reference
Every component is known, and so is the assembly. The "assembly" is the conjunction of a textbook non-σ-complete algebra with the trivial necessary condition (ccc) for a strictly positive measure. The witness the seed chose (Argyros's space) hides this: its non-trivial content (ccc without a strictly positive measure) is not needed for the claimed statement. Types 1 and 5 fail for the same reason, a 3-line derivation from standard facts.

### Owned-region record (for the seam map)
- `owned_by`: folklore. Primary references: Jech, arXiv:1705.01006 §1 ("every measure algebra satisfies ccc"), and the standard non-σ-completeness of P(ω)/fin.
- Region: atomless + non-σ-complete + no strictly positive (finitely or σ-) additive measure, in ZFC.
- How verified: hand derivation above, plus the quoted primary text for the ccc step.
- The ccc-strengthened region is owned by Gaifman 1964 (abstract-level) together with the product trick (⟦HAND⟧).

### Recommendation
**PARK.**
- Types evaluated: 1 and 5. Both FAIL; the bar failed for each is "trivial consequence of known results".
- Open-question status: not available, because the question has a ZFC answer.
- Lesson for the near-miss table: add non-ccc algebras such as P(ω)/fin as a row ("no strictly positive measure for trivial ccc reasons"). The table's apparent pattern "measure-free ⟹ σ-complete" is an artefact of listing only ccc examples.

### Sources
- Jech, "Measures on Boolean algebras", arXiv:1705.01006 (ar5iv HTML: https://ar5iv.arxiv.org/html/1705.01006). **Full text** (§1, §4).
- Wikipedia, "Complete Boolean algebra" (https://en.wikipedia.org/wiki/Complete_Boolean_algebra). **Full text**, relevant section.
- Argyros, *Pacific J. Math.* 105 (1983) 257–272 (https://msp.org/pjm/1983/105-2/p01.xhtml). **Abstract.**
- Gaifman, *Pacific J. Math.* 14 (1964) 61–73 (https://msp.org/pjm/1964/14-1/p08.xhtml). **Abstract/snippet.**
- Kelley, *Pacific J. Math.* 9 (1959) (https://msp.org/pjm/1959/9-4/pjm-v9-n4-p14-p.pdf). **Snippet**; statement via Jech Thm 4.2.
- Fremlin, *Measure Theory* Vol. 3, Ch. 39 extract (https://www1.essex.ac.uk/maths/people/Fremlin/chap39.ro.pdf). **Snippet.**
- Wikipedia, "Almost disjoint sets". **Full text**; it does not contain the size-𝔠 construction, so the hand argument above stands on its own.
