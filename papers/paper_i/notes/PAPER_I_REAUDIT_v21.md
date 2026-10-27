# Paper I re-audit, `/audit full`, skill v2.1 (2026-10-27)

reviewed: false. Auditor: Claude (Opus), forked agent. Target: `papers/paper_i/probability_from_observation.tex`
+ `probability_from_observation_body.tex` + `references.bib` (the FIXED text, post-2026-06-25 corrections).
No other file edited; nothing committed.

**Method / disclosure.** I read the paper in full first and formed the verdict below before reading
`PAPER_I_AUDIT_VERDICT.md`. During the shelf-first grep I did see the one-line `$meta.status` of
`notes/unsorted/foundations/ce_nonderivability/ce_taxonomy.json`, which restates the prior verdict
("σ-Loomis–Sikorski realization gap, Prop B2"). Everything marked ⟦HAND⟧ is my own reasoning, checked by hand
and not by Lean.

**Read levels.**
- Paper: full read.
- Shelf: Marczewski 1953 (`summary_basis: read`, per the index; not re-read); Fremlin vol. 3 (memory); Howson 2008
  (index entry only).
- Web: Andersen–Jessen 1948 (snippet only; the scanned PDF has no text layer); M. M. Rao 1971 and Pachl 1972
  (snippet); Lacey 1974 (cited secondhand in arXiv:2105.05339, snippet); Cardona–Mejía–Uribe-Zapata
  arXiv:2503.08910 (snippet); Shafer–Vovk arXiv:1802.06071 (snippet).
- Memory only: Bochner 1955, Mallory–Sion 1971, Bhaskara Rao & Bhaskara Rao 1983, Fremlin §321K's exact scope.

---

## Audit: Paper I (mode: full)

### Declared contribution type(s)
None are declared in the paper. The prior audit evaluated Types 1, 2, 4 and 6. I evaluate Types 1–6; Type 7 does
not apply.

### What the paper actually says, with the vocabulary stripped
1. **Carathéodory route (Thm 2.x).** Suppose the index is σ-directed (every countable set has an upper bound),
   evaluation is surjective, and the marginals are compatible σ-additive measures. Then a unique P exists on
   σ(𝒞).
2. **"CE" (Prop/Thm main).** For a compatible family, CE ⟺ each ℓ_i is σ-additive ⟺ each Yosida–Hewitt pure
   part is 0. The paper itself says this is a one-line tautology.
3. **Stone route (Prop invlim, B1, B2, Thm stone-main, Cor stone-support).** Any charge gives a Baire measure μ̂
   on St(𝒞), unconditionally. Under CE plus a "realization hypothesis" (countably complete ultrafilters Σ are
   realized by points of Ω, up to null sets), μ̂(pure Ω) = 1 and μ̂ descends to P on Ω.
4. **Framing.**
   - The abstract and introduction call σ-additivity *of each charge* "the exact boundary". Intro, lines
     181–183, says "a compatible charge family extends to a unique σ-additive measure on σ(𝒞) iff CE (Thm main)".
   - The passage to P is presented as a "geometric commitment": a Loomis–Sikorski phantom-point wall that opens
     only at measurable cardinals.

### Correctness (these block, independent of novelty)

**C1. FATAL: Theorem `I:thm:stone-main` is false as stated, even with the added realization hypothesis.**
⟦HAND⟧ Counterexample:
- Let S = {0,1} and ι = (ℕ, ≤). Let Ω be the countable set of eventually-zero binary sequences, with eval_L the
  first L coordinates and ℓ_L uniform on {0,1}^L.
- Surjective Evaluation holds, Discriminability holds, and common coarsenings hold (ℕ is a chain).
- CE holds: every level is a finite algebra, so every ℓ_L is σ-additive.
- 𝒞 ≅ the clopen algebra of the Cantor set, because Ω is dense. So St(𝒞) = 2^ℕ, and μ̂ is the coin-tossing
  measure.
- For x ∉ Ω, the ultrafilter u_x contains the prefix cylinders of x. Their intersection in Ω is ∅, and ∅ ∈ 𝒞 but
  ∅ ∉ u_x. So u_x ∉ Σ, and therefore Σ = pure(Ω) exactly. The realization hypothesis holds with no exceptional
  set at all.
- The result does not depend on how Σ is read. Under the strict reading of "closed under countable
  intersection" (the meet must itself be a member, hence lie in 𝒞), even principal ultrafilters fail, since the
  meet of the prefix cylinders of ω is {ω} ∉ 𝒞. Then Σ = ∅. Either way Σ ⊆ pure(Ω), so the realization hypothesis
  holds. The strict reading also falsifies the paper's own line "each principal ultrafilter is countably complete".
- Yet μ̂(pure Ω) = 0, because pure(Ω) is countable. No P can exist: σ(𝒞) contains every singleton, each with
  P-mass 2^{-L} → 0, and Ω is countable, so P(Ω) would be 0.

So every hypothesis of the theorem holds, but its conclusion fails. Prop `I:prop:B2`'s first claim
("CE ⟹ μ̂(Σ) = 1") fails on the same example.

**C2. The root error: σ-additivity per level is conflated with σ-additivity of the glued charge.**
- B2's proof says "CE gives μ_p = 0, so μ is σ-additive". But CE (Def `I:def:collectively-exhaustive`) and
  Thm main (i)–(iii) are statements about each B_i separately, while μ is the glued charge on 𝒞 = ⋃B_i.
- Per-level σ-additivity does not imply σ-additivity on 𝒞. C1 shows this, and so does the classical Andersen–Jessen
  1948 example of compatible σ-additive marginals with no extension (snippet-level read).
- In C1 the cover Ω ⊆ ⋃_k C_k by cylinders with Σμ(C_k) < ε breaks σ-subadditivity.
- So the abstract's "the exact boundary is σ-additivity of each charge" and the intro's "extends iff CE" are
  **false** unless ι is σ-directed. The paper's own flagship example (ℕ, ≤) is not σ-directed.
- Under σ-directedness every countable family lives at one level and the two notions coincide. But then
  Thm 2.x (Carathéodory) already covers the case, and that case is the known Bochner "sequentially maximal"
  setting (M. M. Rao 1971; Choksi; Mallory–Sion; memory/snippet).
- Kolmogorov's real content (tightness or compact classes, i.e. Marczewski 1953) is exactly what the paper's
  "what replaces tightness?" sentence sidesteps. Its hypothesis excludes Kolmogorov's own index set.

**C3. The realization hypothesis is the wrong condition: not needed, and not sufficient.** ⟦HAND⟧
- *Not sufficient:* see C1.
- *Not needed:*
  - If the glued μ is σ-additive on the field 𝒞 ⊆ 2^Ω, Hahn–Kolmogorov extends it to σ(𝒞) on Ω directly. No
    condition on ultrafilters enters (Billingsley Thm 3.1; Bogachev 1.5.6).
  - In Stone terms, take the *Baire* μ̂ the paper itself names. Every zero set Z of St(𝒞) is a countable
    intersection ⋂[E_n] of decreasing clopens.
  - Suppose Z ∩ pure(Ω) = ∅. Then ⋂E_n = ∅ in Ω, because ω ∈ ⋂E_n gives pure(ω) ∈ Z. So μ̂(Z) = lim μ(E_n) = 0.
  - By inner regularity with respect to zero sets, the Baire outer measure satisfies μ̂*(pure Ω) = 1. The trace on
    pure(Ω), pulled back through Prop B1, gives P.
  - Conversely, μ̂*(pure Ω) = 1 forces σ-additivity on 𝒞.
- The correct statement is therefore:
  > compatible charges extend to P on (Ω, σ(𝒞)) ⟺ the glued charge is σ-additive on 𝒞 ⟺ μ̂*_{Baire}(pure Ω) = 1.

  This is a folklore trace-measure fact. It has no Loomis–Sikorski residue in this Boolean field-of-sets setting.
- Test case: Ω = a measurable cardinal κ, 𝒞 = P(κ), μ = δ_u with u σ-complete and non-principal.
  - Here P = δ_u exists.
  - The Baire outer measure of pure(Ω) is 1. Every Baire set is fixed by countably many clopens, and σ-completeness
    puts a principal point in the same fibre as u.
  - Only the *Radon/Borel* extension gives pure(Ω) measure 0.
  - So the measurable-cardinal "phantom point" is not an obstruction to descent. It is an artefact of measuring
    pure(Ω) with the Borel extension.

**C4. The measurable-cardinal paragraph (lines ~648–664) is wrong on several counts.**
- It conflates countably complete ultrafilters *of the subalgebra 𝒞* with those on P(Ω).
- It says "the gap cannot bite on the observation spaces of ordinary practice … countable or standard-Borel Ω".
  C1 is a countable Ω where descent fails.
- It treats the gap as the same wall met in the orthomodular setting. That analogy is unsupported for the Boolean
  case (see C3). I make **no** claim about the OML/σ-essential `rem:dw` residue, where Hahn–Kolmogorov is not
  available. Not assessed.

**C5. Minor errors.**
- Lemma `I:lem:pi-system` and Lemma `I:thm:obs-determination` assume common *lower* bounds k ≤ i, j. But
  π_{ki}^{-1}(A) with A ⊆ O_i does not type-check (π_{ki}: O_i → O_k). Upward directedness is needed.
- Thm stone-main omits upward directedness, so 𝒞 need not even be an algebra.
- Σ ("closed under countable intersection") is ill-defined when 𝒞 is not σ-complete.
- "μ̂(pure Ω) = 1" presupposes measurability; the correct notion is outer measure.
- B2 cites Fremlin §321K/§314M (null ideal = meagre ideal). That holds for the canonical measure on the Stone
  space of a *measure algebra*, which is strictly positive. It does not hold for the Stone measure of an arbitrary
  charge: δ_ω on Cantor space charges a meagre singleton. So the citation does not support the step.
- Lemma `I:lem:surj-inj`(i) re-proves something Def `I:def:obs-structure` already assumes.
- The wrapper file closes `\end{document}` before the body's own `\maketitle`/abstract block. That is harmless
  only because the body is `\input`.

### Pure Verdict: KNOWN (every correct piece is owned; the one piece not owned is false)

| Piece | Status | Owner (read level) |
|---|---|---|
| A charge gives a σ-additive Radon/Baire measure on its Stone space | KNOWN, textbook | Lacey 1974 (snippet); Bhaskara Rao² 1983 (memory); Cardona et al. 2503.08910 (snippet) |
| Carathéodory extension for a σ-directed index | KNOWN | Bochner sequential maximality; M. M. Rao 1971; Choksi 1958; Mallory–Sion 1971 (snippet/memory) |
| CE ⟺ per-level σ-additivity ⟺ Yosida–Hewitt pure part = 0 | Tautology, KNOWN | Halmos 1950; Yosida–Hewitt 1952 (memory) |
| Per-level σ-additive compatible marginals need not extend | KNOWN | Andersen–Jessen 1948 (snippet); Shafer–Vovk 1802.06071 (snippet) |
| Extension ⟺ glued σ-additivity ⟺ Baire outer measure of pure(Ω) = 1 | Folklore (Hahn–Kolmogorov + trace measure) | Billingsley; Bogachev; Fremlin vol. 2 trace measures (memory) |
| σ-additivity is not first-order axiomatizable | Folklore | Łoś; Hoover 1978; FHM 1990 (memory; the companion note was killed on this) |
| Stone-route descent under CE + realization | **FALSE** (C1) | — |

### Applied Verdict: not evaluated
There is no methodology claim.

### Contribution Type Verdicts
- **Type 1 (new theorem): FAIL.** The correct statements are owned or folklore. The only unowned theorem
  (stone-main / B2 under the realization hypothesis) is false.
- **Type 2 (new proof): FAIL.** The Stone route to Carathéodory adds no technique. Where it departs from the
  textbook route, it is wrong.
- **Type 3 (unifying framework): FAIL.** "Directed system of event algebras" is the standard projective-limit
  set-up. No method transfers.
- **Type 4 (vocabulary CE): FAIL.** CE collapses to continuity at ∅ by the paper's own remark, so the
  three-statements test fails. The terms "observational structure" and "query system" rename projective systems.
- **Type 5 (impossibility): FAIL.** "No first-order condition forces σ-additivity" is folklore (Łoś, Hoover, FHM).
  "No condition strictly between coherence and σ-additivity" is a tautology inside the paper's own definitions.
- **Type 6 (exposition): FAIL as written.**
  - (a) Audience: philosophy of probability, implied but never named.
  - (b) The material is accessible: Billingsley §2–3, Bogachev §7.7, Bhaskara Rao², Shafer–Vovk 2018,
    Howson 2008.
  - (c) The one non-trivial conceptual move, the "geometric commitment" diagnosis, is wrong (C3).
  - Exposition that misdiagnoses where the obstruction lives cannot clear (c).

### Cross-reference
Every component is known, and the assembly is incorrect. The paper's distinctive thesis is that the passage to
probability is a choice of realization space, governed by phantom σ-complete ultrafilters. It sits exactly where
the error is. The true dependence on Ω is real but elementary: whether the *glued* cylinder charge is σ-additive
depends on which countable intersections are empty in Ω (C1 versus the full Cantor space). That is
textbook-visible in Kolmogorov/Andersen–Jessen, not a large-cardinal phenomenon.

### Recommendation
**Keep it parked.** The park decision does not change, but its *reason* must be corrected (see the comparison
section). Do not repair it toward a theorem paper: the correct version is Hahn–Kolmogorov plus a trace measure.

**Bearing on WHY.md (one line).** The correct form of the result is exactly the probabilistic loop question.
Local views that are each σ-additive (correct as far as they go) can fail to glue into one world, with no
contradiction at any level. Here the culprit is an idealisation (WHY question 3: which countable intersections are
empty in Ω), not a loop. It does not make the paper more novel.

---

### Referee estimate: REJECT-LIKELY
- **Venue class:** none, as it stands.
  - Research journals (Fund. Math., J. Theoret. Probab., Ann. Pure Appl. Logic) would reject it as both known and
    incorrect.
  - Expository venues (Amer. Math. Monthly, Expositiones Math.) reject wrong diagnostics too.
- **Value carried by:** none.
  - Factor 2 fails because the new route is wrong where it is new.
  - Factor 4 fails because the exposition misplaces the obstruction and duplicates accessible treatments.
- **Main risk a referee would raise.** "Thm stone-main is false. Take Ω = the eventually-zero sequences in 2^ℕ with
  fair-coin marginals. Every hypothesis, including realization, holds, yet no measure exists. The obstruction is
  per-level versus glued σ-additivity (Andersen–Jessen), not Loomis–Sikorski."
- **Caps applied.**
  - The pure verdict is KNOWN, not UNCLEAR, so the UNCLEAR cap does not bind.
  - No factor-1/2 ACCEPT is sought, so the read-level cap does not bind.
  - The central claim is wrong, which alone forces REJECT-LIKELY.
- **Unread neighbours, to be named:** Andersen–Jessen 1948 (body; scan only); M. M. Rao 1971 and Pachl 1972;
  Bochner 1955; Mallory–Sion 1971; Lacey 1974; the body of Bhaskara Rao² 1983; Fremlin §321K's exact scope.

**Repositioning that could make it publishable.** At best BORDERLINE, at a philosophy-of-probability or
expository venue (e.g. *Erkenntnis*/*Synthese*/*BJPS* note, or a Monthly-style note). It would need to be
rewritten as a correct short note:
1. coherence and per-level σ-additivity do not glue (C1, plus Andersen–Jessen);
2. the exact criterion is σ-additivity of the glued charge ⟺ Baire outer measure 1 on the realized points;
3. the Ω-dependence, read through van Fraassen as "empirically adequate on St(𝒞) versus committed on Ω".

Item 3 is the only plausible residual. Howson 2008 and Shafer–Vovk 2018 cover most of the rest, so a referee would
ask what is added beyond them. This would be a new paper, not the fixed Paper I.

---

## Comparison with prior audit (2026-06-23/25)

**This is a reversal of the prior diagnosis, so it comes first: the prior audit got the park right but the reason
wrong.**

- **Agreement.**
  - Park.
  - Novelty is owned: Stone-measure facts, Choksi/Mallory–Sion, and CE as a tautology.
  - Types 1/2/4 FAIL; Type 6 thin.
  - "The vise", in the sense that no regime is both correct and novel, still holds. The correct regime is
    Hahn–Kolmogorov plus a trace measure, which is folklore.
- **Disagreement 1: the fatal error is not the σ-Loomis–Sikorski realization gap.**
  - The prior audit's fix added the realization hypothesis. The theorem is still false with it (C1).
  - The hypothesis is also unnecessary once the correct (glued) σ-additivity is assumed (C3).
  - The true error is C2: per-level CE is conflated with σ-additivity of the glued charge on 𝒞.
- **Disagreement 2: the "circularity" finding of 2026-06-25.** That pass called the Ω-meet argument circular
  ("⋂C_k = ∅ if unrealized … presupposes B2"). ⟦HAND⟧ It is not circular:
  - If ω ∈ ⋂C_k, then pure(ω) ∈ ⋂[C_k] = {u}, so u is realized.
  - The meet in Ω is what σ-additivity on a field of sets *means*.
  - Its example δ_u with u unrealized has δ_u **not** σ-additive on 𝒞 whenever u is a G_δ point. When u is not
    G_δ (the measurable-cardinal case), P = δ_u exists on Ω anyway.
- **Disagreement 3: the Fremlin §321K/§314M re-attribution.** It cites a statement about measure-algebra Stone
  spaces, which does not apply to the Stone measure of an arbitrary charge (C5). Replacing the rao1983 miscitation
  with Fremlin did not fix the step; it moved the miscitation.
- **New findings the prior audit did not record:** C1, the explicit counterexample to the fixed theorem; the
  per-level/glued conflation; the intro's false iff; the common-coarsening direction error; the countable-Ω refutation
  of the "ordinary practice" claim.

**Downstream records the user should review (not edited, per instructions).**
1. The `ce_taxonomy.json` `$meta.status` line and its walls entry ("σ-complete ultrafilters need not be realized
   as points — the standing wall that sinks Paper I's Prop B2"). For Paper I (the Boolean field-of-sets case) the
   wall attribution looks wrong.
2. The CLAUDE.md/MEMORY line "fatal B2 (σ-LS realization gap)".
3. Any place asserting that "the same realization gap recurs" with Paper I as an instance.

The OML/σ-essential `rem:dw` residue itself is **not** touched by this audit.
