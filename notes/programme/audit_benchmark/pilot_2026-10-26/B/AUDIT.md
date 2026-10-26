## Audit: seed.md, "countable additivity is not first-order axiomatizable" (mode: full)

### Declared contribution type(s): Type 1 (new theorem), Type 2 (new proof via saturation)

The seed declares types. It does not state per-type bars beyond the labels, which makes it only partly ready for Phase 2.

---

### Pure Verdict: KNOWN (folklore / trivial consequence). The proof idea is BROKEN.

**1. What the statement actually says, without the new vocabulary.** The seed works in a two-sorted language: a Boolean-algebra sort 𝔉, a real sort, and a symbol μ : 𝔉 → reals. The claim is that no first-order theory T has, as its models, exactly the σ-additive (𝔉, μ).

There is an ill-posedness to fix first. If the real sort must be the standard ℝ, the *ambient* class (structures with μ valued in [0,1] ⊂ ℝ) is already non-elementary: upward Löwenheim–Skolem gives non-Archimedean real sorts. Read literally, the claim is then true for a reason that has nothing to do with σ-additivity. The only sensible reading is relative: no T separates the σ-additive members of the ambient class from the rest. That requires a pair M ≡ N with M σ-additive and N not.

**2. A short witness, so the statement is a trivial consequence.** ⟦HAND⟧, checked by me and not machine-checked.
- Let N = (FinCof(ℕ), μ) and M = (FinCof(ω₁), μ). In both, the field is the finite/cofinite sets, μ = 0 on finite sets and μ = 1 on cofinite sets. Both measures are finitely additive.
- N is not σ-additive: ℕ = ⋃ₙ{n}, but μ(ℕ) = 1 ≠ 0 = Σ μ({n}).
- M is σ-additive as a field of sets. Suppose countably many pairwise disjoint members have their union in the field. If all of them are finite, the union is countable, so it must be finite, and only finitely many members are nonempty. If one member is cofinite, the others lie inside its finite complement, so again only finitely many are nonempty. Either way additivity holds trivially.
- M ≡ N. μ is definable from the ideal Fin of finite elements and the constants 0, 1. So it suffices that (FinCof(ℕ), Fin) ≡ (FinCof(ω₁), Fin). Atoms are definable, and "exactly n atoms below x" is first-order for each n. So a countable elementary substructure of (FinCof(ω₁), Fin), obtained by downward Löwenheim–Skolem on the Boolean-algebra sort, is ≅ (FinCof(A), Fin) for some countable infinite A, hence ≅ (FinCof(ℕ), Fin). The real sort is ℝ in both structures and interacts only through the definable μ, so equivalence transfers to the two-sorted structures.

So σ-additivity is not preserved under elementary equivalence. That takes a few lines from standard facts, which puts it in the "trivial consequence of standard techniques" category: KNOWN (folklore).

**3. The literature already treats this as standard.**
- **Fagin–Halpern–Megiddo**, "A logic for reasoning about probabilities", *Inform. & Comput.* 87 (1990), as reported by **Halpern**, "Set-theoretic completeness for epistemic and conditional logic", *Ann. Math. AI* 26 (1999), arXiv:cs/9808006, §1 Introduction. Read level: full text of §1 of Halpern; FHM itself not read. Halpern's text: a complete axiomatization is given "where, semantically, probability is taken to be countably additive, but axiomatically, we require only finite additivity". It follows that "there will be nonstandard models of the theory where the probability is finitely additive but not countably additive". This is the same phenomenon at the propositional level, recorded as a remark and not presented as a theorem.
- **Keisler, "Probability quantifiers"**, in Barwise–Feferman (eds.), *Model-Theoretic Logics* (1985), pp. 509–556. Read level: snippet (bibliographic and secondary description only). Keisler–Hoover use an admissible infinitary fragment (L_AP) with probability quantifiers. That they do so *because* countable additivity escapes first-order logic is my inference, not a statement I read. Hoover (1978): unread.
- **Pourmahdian–Zoghifard**, "Probability Logic: A Model Theoretic Perspective", arXiv:1810.07413. Read level: full text (ar5iv), targeted reading of §§1–3. This is the closest owner of the separation, though for propositional probability logic and not the two-sorted language.
  - **Example 2.6:** a theory Σ is finitely satisfiable but has no σ-additive model.
  - **Example 2.7:** the same Σ is satisfiable in a finitely additive model.
  - **Thm 3.1 vs Thm 3.4:** the Löwenheim–Skolem number is ℵ₀ < λ ≤ 2^ℵ₀ for σ-additive models and ℵ₀ for finitely additive ones.
  - §1 notes 𝒫ℳ ⊊ ℱ𝒫ℳ.
  - Ex. 2.6–2.7 are a compactness argument showing that finitary axioms cannot single out the σ-additive class. That is the seed's claim in a neighbouring logic.
  - The paper contains no numbered "not axiomatizable" theorem.

The seed's "Status" line ("does not appear to have been settled by an explicit proof") is therefore misleading. The question is not open; it is too easy to be stated as a theorem. I did not find a single numbered theorem stating the exact two-sorted claim. That gap is about phrasing, not knowledge.

**4. The proof idea is wrong, and it fails in the opposite direction.** ℵ₁-saturation does not produce a σ-additivity failure; it forces σ-additivity.
- **Loeb**, *Trans. AMS* 211 (1975), 113–122. Read level: abstract, plus the Wikipedia "Loeb space" summary as a secondary source. In a denumerably comprehensive (ℵ₁-saturated) enlargement, the internal algebra has the following property: if a member is a countable union of members, it is already a finite union of them. Hence every finitely additive (standard-part) measure on the internal algebra is automatically countably additive. This is the first step of the Loeb construction.
- The same holds abstractly in an ℵ₁-saturated ultrapower of a Boolean algebra. Suppose infinitely many aₙ are nonzero and b = sup aₙ. The type {x ≤ b, x ≠ 0, x ∧ aₙ = 0 for all n} is finitely satisfiable. A realisation x makes b − x a smaller upper bound, a contradiction. So the countable sups that exist are trivial, and σ-additivity holds vacuously.
- **Hrushovski–Pillay–Simon**, "Generically stable and smooth measures in NIP theories", arXiv:1002.4763, **Remark 6.2(i)**. Read level: full text, targeted passage. "When M is ω-saturated, any Keisler measure over M is countably additive": compactness reduces any countable cover of a definable set to a finite subcover. This is the exact first-order form of the mechanism the seed invokes, and it proves the opposite of what the seed wants.
- The ultrapower also leaves the ambient class, because its real sort is *ℝ.

So the proposed saturation route is self-refuting. The correct mechanism is downward, as in the witness above (a countable non-σ-additive model elementarily equivalent to an uncountable σ-additive one), or an ultraproduct taken before saturation is available.

---

### Applied Verdict: not evaluated (no Type 7 claim; nothing applied to test). Practitioner test: n/a.

---

### Contribution Type Verdicts (mode = full):

**Type 1 (New theorem): FAIL.**
- Bar: not known, not folklore, not a trivial consequence, with a non-routine proof.
- The relative statement follows in a few lines (FinCof(ℕ) ≡ FinCof(ω₁) with the 0/1 measure). It is the standard background that motivates FHM's finite-additivity axiomatization and Keisler–Hoover's move to L_AP.
- The literal statement (with standard ℝ fixed) is trivially true for an unrelated reason: the ambient class is non-elementary.

**Type 2 (New proof via saturation): FAIL, and stronger than "no gain".** The proposed proof is invalid.
- Saturation is exactly what makes σ-additivity hold on internal or saturated algebras (Loeb 1975; the finite-union property).
- The ultrapower also exits the class of [0,1]-valued structures.
- No technique, connection or simplification survives to be assessed.

Undeclared types: none are plausibly claimable.
- Type 5 (impossibility) would fail for the same reason as Type 1: it rephrases known non-expressibility.
- Type 6 fails because the material is well covered in Keisler 1985 and FHM 1990.

---

### Cross-reference
The components are known and there is no novel assembly. The one novel-looking ingredient, the saturation argument, is backwards: it is the Loeb mechanism, which yields σ-additivity. The pure and Type 2 verdicts reinforce each other.

---

### Recommendation
**PARK.** Retire; do not draft or submit.
- Types evaluated: 1 (FAIL: folklore / trivial consequence) and 2 (FAIL: proof invalid; saturation forces σ-additivity).
- Not an open question: the question is settled, not dormant.
- If any trace is kept, record it as covered: state the FinCof(ℕ)/FinCof(ω₁) witness and cite FHM 1990, Keisler 1985 and Loeb 1975.

Bearing on the programme's why (one line): this is a hidden idealisation. "Countable additivity" is not something first-order questions can see, so local finitary data cannot certify the σ-step. That is a known fact, and it is not a new one.

---

### Sources (read levels)
- Halpern, *Ann. Math. AI* 26 (1999), arXiv:cs/9808006, §1: full text of §1 (ar5iv). It reports FHM 1990, which I did not read myself.
- Fagin, Halpern, Megiddo, *Inform. & Comput.* 87 (1990): not read directly. LICS 1988 page https://lics.siglog.org/1988/FaginHalpernMegiddo-Alogicforreasoninga.html: abstract.
- Keisler, "Probability quantifiers", *Model-Theoretic Logics* (1985) 509–556: snippet. Hoover 1978: unread.
- Pourmahdian, Zoghifard, arXiv:1810.07413, Ex. 2.6, Ex. 2.7, Thm 3.1, Thm 3.4: full text (ar5iv, targeted).
- Hrushovski, Pillay, Simon, arXiv:1002.4763, Remark 6.2(i): full text (ar5iv, targeted).
- Loeb, *Trans. AMS* 211 (1975) 113–122, https://www.ams.org/journals/tran/1975-211-00/S0002-9947-1975-0390154-8/: abstract only, no lemma number verified. Wikipedia "Loeb space": full text, secondary.
- Witness pair FinCof(ℕ)/FinCof(ω₁): ⟦HAND⟧, auditor's own argument, not machine-checked.

**Single most damaging source.**
- Against the seed as a whole (Type 2, and the proof idea): **Hrushovski–Pillay–Simon, Remark 6.2(i)**. ω-saturation makes every Keisler measure countably additive, so the seed's saturation route is refuted by a published statement.
- Against Type 1: **Pourmahdian–Zoghifard Ex. 2.6–2.7**, a finitely satisfiable theory with finitely additive but no σ-additive models, in propositional probability logic. Add the ⟦HAND⟧ FinCof witness for the exact two-sorted form.
