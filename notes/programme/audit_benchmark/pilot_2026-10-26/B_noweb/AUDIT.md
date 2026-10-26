## Audit: seed.md, "countable additivity is not first-order axiomatizable" (mode: full)

Conditions: no web access, so every citation below is from memory. Confidence is marked [certain / likely / unsure]. Theorem and section numbers marked "likely" or "unsure" must be checked against the primary source before anyone relies on them.

### Declared contribution type(s): Type 1 (new theorem), Type 2 (new proof via saturation)

The seed declares types but does not state its per-type bars. It also makes an undeclared Type 5 claim (an impossibility: "no first-order theory has exactly the σ-additive models"), so Type 5 is evaluated below too.

---

### Step 0: what is the actual statement? (The seed is mis-posed as written)

The seed offers two languages, and the answer depends on which one is used.

- **(L1) Two-sorted, with the real field as a first-order second sort.** Here the models are not structures with μ : 𝔉 → [0,1] for the *standard* [0,1]. Every elementary extension of the real sort is a non-Archimedean real closed field. So the class "μ takes standard real values" is not elementary already, before σ-additivity comes in. That makes the claim true for a trivial reason that has nothing to do with countable additivity. The claim can also be ill-posed, because "Σ μ(Aₙ)" has no meaning in *ℝ, where bounded countable sets need not have suprema. Either way the seed's question is not well formed in L1.
- **(L2) One sort for the field (or Boolean algebra) of sets, plus unary predicates P_r(x) :⟺ μ(x) ≥ r for rational r**, with μ(x) := sup{r : P_r(x)}. This is Keisler's "fixed language for probability structures". In L2 the values are standard, finite additivity is axiomatizable by first-order schemes, and the question makes sense. Read in L2, the real statement is:

  > The class of (𝔉, μ) with μ σ-additive is not closed under elementary equivalence in L2.

  This must be read in one of two ways: (a) **set-theoretic**, meaning a countable disjoint union that is a member of 𝔉 gets measure Σμ; or (b) **algebraic**, meaning a countable disjoint family whose Boolean-algebra supremum exists gets measure Σμ. The seed does not say which. The witness below works for both.

### Step 1: the three-line proof (folklore level) ⟦HAND⟧

Let FC(X) be the finite–cofinite field on an infinite set X, with μ(a) = 0 for finite a and μ(a) = 1 for cofinite a. This μ is finitely additive and two-valued.

1. **FC(ω) is not σ-additive.** ω = ⋃ₙ {n}, and both ω and every {n} are members. The sum of the measures is 0, but μ(ω) = 1. In the algebra, sup{{n}} = ω, so this works in reading (b) too.
2. **FC(ω₁) is σ-additive, vacuously.** Take a countable disjoint family of members. If every member is finite, the union is countably infinite or finite. A countably infinite union is neither finite nor cofinite in ω₁, so it is not a member, and a family of nonempty members with no supremum (reading b) also escapes the condition. If one member is cofinite, the others lie in its finite complement, so only finitely many are nonempty. Either way the condition reduces to finite additivity.
3. **FC(ω) ≼ FC(ω₁) in L2.** P_r for r > 0 picks out the unique non-principal ultrafilter (the cofinite sets), and P_0 is everything. A back-and-forth argument on finite subalgebras shows that the type of a finite partition is determined by the sizes of its finite blocks plus one infinite block. That type is the same in both structures, and every extension step (split a finite block, or split the infinite block into finite + infinite or infinite + infinite) can be matched on the other side. ⟦HAND; standard back-and-forth for atomic Boolean algebras with a distinguished ultrafilter. Compare Tarski's theorem that the theory of infinite atomic Boolean algebras is complete [certain, as a classical fact; source e.g. Chang–Keisler, *Model Theory*, 3rd ed., §5.5 exercises, unsure of the exact number].⟧

So σ-additivity is not preserved under elementary substructure or equivalence, and the class is not elementary. **This is a trivial consequence of standard techniques.**

---

### Pure Verdict: KNOWN (folklore and trivial consequence), and the seed's proof is WRONG

**(i) The proof idea is broken, and backwards.** The seed passes to an ℵ₁-saturated elementary extension (an ultrapower) and expects "a countable disjoint family whose measures do not sum correctly". In fact ℵ₁-saturation gives the opposite. In an ℵ₁-saturated structure, if internal (definable-with-parameters) sets A, A₁, A₂, … satisfy A = ⋃ₙ Aₙ with the Aₙ disjoint, then A = A₁ ∪ … ∪ A_N for some finite N. This is countable saturation applied to the type {x ∈ A, x ∉ A₁, …, x ∉ Aₙ : n}. So the standard part of the internal measure is σ-additive on the internal algebra, *vacuously*. This is exactly the key lemma behind the Loeb measure.
- **Loeb, P. A., "Conversion from nonstandard to standard measure spaces and applications in probability theory", Trans. AMS 211 (1975), 113–122** [certain for the paper and its main construction; likely that the vacuous-σ-additivity lemma is stated there essentially as above, as the step that lets Carathéodory extension apply].
- The same fact appears in textbook form in, for example, Albeverio–Fenstad–Høegh-Krohn–Lindstrøm, *Nonstandard Methods in Stochastic Analysis and Mathematical Physics* (1986), Ch. 3 [likely], and Goldblatt, *Lectures on the Hyperreals* (GTM 188, 1998), Ch. 16 on Loeb measure [likely].

In reading (b), an ℵ₁-saturated Boolean algebra has no supremum for an infinite countable disjoint family of nonzero elements. So σ-additivity again holds vacuously in the saturated extension [⟦HAND⟧, same saturation argument]. The ultrapower route therefore cannot produce a counterexample. Saturation moves the structure *into* the σ-additive class. A counterexample must go the other way: a non-σ-additive model that is elementarily equivalent to a σ-additive one, as in Step 1, where the σ-additive model is the larger one.

**(ii) The statement is folklore in probability logic, and its standard *use* is the converse.**
- **Keisler, H. J., "Probability quantifiers", Ch. XIV of Barwise–Feferman (eds.), *Model-Theoretic Logics*, Springer 1985** [certain the chapter exists; likely on content]. It discusses L_AP and the gap between finitely additive ("weak") and σ-additive ("graded") probability models. It uses Loeb or saturation methods to show that consistent theories have σ-additive models, that is, finitary first-order means cannot force σ-additivity to *fail*. The seed's question is the setting this chapter works in.
- **Hoover, D. N., "Probability logic", Annals of Mathematical Logic 14 (1978), 287–313** [likely]. Completeness of L_AP, again via the weak-to-σ-additive passage.
- **Fagin, Halpern & Megiddo, "A logic for reasoning about probabilities", Information and Computation 87 (1990), 78–128** [certain on the paper; likely on the remark]. They note explicitly that their language cannot tell finitely additive from countably additive measures, and that completeness holds with finite additivity alone. This is the informal statement of exactly the seed's claim. The seed's phrase "does not appear to have been settled … in the literature on probability logics" is contradicted here.
- **Scott & Krauss, "Assigning probabilities to logical formulas", in Hintikka–Suppes (eds.), *Aspects of Inductive Logic*, 1966** [likely]. They move to L_{ω₁ω} *because* σ-additivity is not expressible finitarily. This is the field's standing motivation, not an open question.
- **Gaifman, H., "Concerning measures in first order calculi", Israel J. Math. 2 (1964), 1–18** [certain on the paper; likely on content]. It treats measures on Lindenbaum algebras, where only finite additivity is meaningful in general.
- **Model theory for metric structures:** Ben Yaacov, Berenstein, Henson & Usvyatsov, "Model theory for metric structures" (2008), §16, probability algebras [likely on the section number]. In continuous logic, models are metrically complete, so measure algebras are σ-complete and σ-additivity comes for free. The question the seed asks disappears in the logic built for measures. This is the cross-field reason the community does not treat the seed's question as open.

**(iii) Hostile check: would an expert say "obvious"?** Yes. A model theorist would give either the Step-1 counterexample or the observation "σ-additivity quantifies over countable families, which first-order logic cannot see". Then they would point out that the seed's saturation proof proves the converse.

**Verdict: KNOWN.** It is folklore (Keisler 1985; FHM 1990), and the statement is a trivial consequence of a three-line elementary-equivalence argument. The proof as sketched is invalid.

### Applied Verdict: not evaluated
No Type 7 is claimed and no computational or practitioner component exists.

### Contribution Type Verdicts (mode=full):

**Type 1 (new theorem): FAIL.** The bar is "not known, not folklore, not a trivial consequence". All three fail: the statement is folklore (FHM 1990 states it informally; Keisler 1985 works in exactly this gap), and the proof is the three lines in Step 1. In the two-sorted reading (L1) it is not even well posed, or it is true for a reason unrelated to σ-additivity.

**Type 2 (new proof via saturation): FAIL, and worse than "no gain": the proof is incorrect.** The bar is (a) a technique transferable elsewhere, (b) an unexpected connection, or (c) a substantial simplification. None applies, because the argument does not work. ℵ₁-saturation makes σ-additivity hold vacuously (Loeb 1975), so the proposed route proves the opposite of what it needs. A correct proof needs a σ-additive model that is elementarily equivalent to a non-σ-additive one, with the σ-additive model on the *large* side. That is the standard approach, not a new one.

**Type 5 (impossibility; undeclared but implicit): FAIL.** (a) It closes off no active direction: probability logic gave up first-order expressibility of σ-additivity decades ago (Scott–Krauss 1966) and moved to L_AP, L_{ω₁ω} or continuous logic. (b) It does not sharpen an existing impossibility. "We already knew this couldn't work."

Type 6 (exposition) is not claimed. It would also fail: the material is accessible in Keisler 1985 and in the Loeb-measure chapters of standard nonstandard-analysis texts.

### Cross-reference
The components are known and the proof component is wrong. There is no assembly to rescue. The one useful by-product is a *correction*: saturation pushes toward σ-additivity, not away from it. That is textbook content (Loeb), not a contribution. Note also that the three-line counterexample makes FHM-style remarks a sufficient reference for the claim itself.

### Recommendation
**PARK. Do not draft, and do not formalize.** The statement is known or folklore and needs no Lean, under "Don't formalize known results". It does not qualify as an open question either: it is not open, and it is mis-posed in L1.
- Evaluated: Types 1, 2 and 5 (implicit). Failed: Type 1 (folklore and trivial), Type 2 (proof invalid; even a corrected proof is standard), Type 5 (no active direction, no sharpening).
- **Lesson to record:** the seed's "status" line was written without checking the probability-logic canon. FHM 1990 or Keisler 1985 are enough to cite for the claim if it is ever needed as a lemma.
- **Single most damaging source: Loeb (1975).** It shows the proposed saturation mechanism yields σ-additivity, which invalidates the Type 2 claim outright and removes the only non-trivial part of the seed. For the statement itself, the owners are Keisler (1985) and Fagin–Halpern–Megiddo (1990).

**Bearing on WHY (one line):** this is the "hidden idealisation" question. σ-additivity is an idealisation that finitary queries cannot detect: no finite pattern of answers shows whether countably many local measurements add up. That is the programme's theme, but it is already fully owned here.
