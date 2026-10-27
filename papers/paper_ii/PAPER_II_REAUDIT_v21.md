# Paper II re-audit, `/audit full`, skill v2.1 (2026-10-27)

reviewed: false. Auditor: Claude (forked agent, Opus). Target: `papers/paper_ii/distributivity_and_realism.tex`
+ `distributivity_and_realism_body.tex` (current working tree, about 6,000 words) + `references.bib`. The verdict below was formed from
the paper before the prior verdict (`PAPER_II_AUDIT_VERDICT.md`, 2026-06-23) was opened. The comparison is
the last section. The programme bar is unchanged. No other file was edited. Nothing was committed.

Read levels: **[R]** read (primary source or the passage itself); **[P]** passage or snippet from a secondary
source; **[A]** abstract or citation only; **[M]** memory or general knowledge, not re-checked this session;
**[H]** ⟦HAND⟧ argument by the auditor, not machine-checked.

Shelf-first was done. Grep of `SHELF_INDEX.json` and `stone_role_prior_art.md` gave these hits: McDonald–Bimbó 2023
(on shelf, read), Horn–Tarski 1948 (owns), Burešová–Pták 2024 (owns "Stone space := two-valued states"),
Abramsky–Brandenburger 2011 (owns), Kalmbach 1983, Shultz 1974, Svozil 2001, and De Simone–Navara–Pták 2007 and
Burešová–Pták–Ševic 2026 (state extension). These are **not on the shelf**: Bub–Clifton 1996, Halvorson–Clifton 1999,
Stairs 1983, Eva 2017, Döring 2008, Gunji 2026, Kochen–Specker 1967, Gudder 1970 and Pitowsky 1989. Memory
`oml_singular_extension_resolved.md` already records that the L(H) extension obstruction is "elementary, needs no
KS". Two web searches (standard mode) and one fetch (Bub, arXiv:quant-ph/9910096) were run.

---

## Audit: Paper II, "Distributivity and the Commensurability of VDR and EA" (mode: full)

### Declared contribution type(s)

- **The paper** says it is "neither a new philosophical thesis nor a new theorem but a *bridge*" (§1, line 186). That is Type 6.
- **The cover letter** (`submission_bjps/cover_letter.md`) says "expository and unifying", which is Types 6 and 3.
- **`contribution_evaluation.md`** names Paper II as its Type 4 calibration example: "Paper II (EA/PR/VDR) clears this bar."
  That line is a prior verdict built into the rubric. It was **not** used here. Type 4 is tested fresh below.
- Types evaluated: 1 (only to check the one candidate new statement), 3, 4, 5 (for PR_dual failing on L(H)) and 6.

### Pure verdict: KNOWN (components and framing). The one candidate new statement is KNOWN under another name ⟦H⟧.

**Stripped content.**
- (a) **Boolean case.** Every charge on a Boolean algebra extends to a Radon measure on its Stone space. Descent to a
  point set Ω needs σ-additivity plus a Loomis–Sikorski realization condition. Ultrafilters are 2-valued. All of this
  is textbook (Bhaskara Rao §4–5, Halmos, Choksi 1958) **[M]**.
- (b) **L(H), dim ≥ 3.** Kochen–Specker gives no dispersion-free state. Gleason gives the trace form of σ-additive states.
  Both are textbook.
- (c) **New candidate.** PR_dual fails on L(H): no state extends to a charge on the clopens of the McDonald–Bimbó dual
  space S₀(L(H)). The paper says this "has not previously been isolated" in those terms (lines 197–200).
- (d) **The filtration** S ⊇ S_σ ⊇ S_df^σ. The paper concedes it is standard (Pták–Pulmannová, Kalmbach).
  Its added content is the labels "pasting / regularity / sharpness".
- (e) **The philosophical reading.** The paper concedes it: van Fraassen 1991, Stairs 1983, Bub–Pitowsky 2010, Eva 2017.

**On (c), the auditor's reduction ⟦H⟧.** S₀(A) is a Stone space and h is meet-preserving, with h(0) = {improper filter}.
A charge μ on Clop(S₀(A)) with μ(h(a)) = s(a) therefore extends to a Radon measure. That measure satisfies:
- μ(h(0)) = 0;
- μ(h(a) ∪ h(a^⊥)) = s(a) + s(a^⊥) − μ(h(0)) = 1 for every a.

So μ gives full measure to each closed set C_a = (h(a) ∪ h(a^⊥)) \ h(0). By τ-additivity, the support of μ lies inside
H = ⋂_a C_a. This step deals with the uncountable intersection: every closed full-measure set contains the support.

A point x of H is a proper filter that contains exactly one of a, a^⊥ for each a. Its indicator therefore preserves
meets and orthocomplements, so it is a 2-valued OML homomorphism. Hence:

> **s extends to a charge on S₀(A) ⟺ s = ∫ δ_x dμ(x), a (Radon) mixture of 2-valued homomorphisms.**
> (⇐: integrate Dirac measures.)

So **PR_dual is exactly the classical non-contextual hidden-variable condition.** That condition asks whether the state
is a mixture of dispersion-free valuations that are homomorphisms. It is the Kochen–Specker 1967 / Gudder 1970 /
Pitowsky 1989 question. In the finite case it is membership in the correlation polytope, which the paper's own footnote
(lines 539–554) half-says. Read levels for this owner: KS **[M]**; Gudder **[P]**, from a 1972 Aplikace Matematiky
snippet that states "the hidden variables question = is s a mixture of dispersion-free states"; Pitowsky **[M]**. Read-level anchors on the shelf: Svozil 2001, pp. 6–7 (the correlation polytope is the convex hull of two-valued states) **[R, passage]**; Abramsky–Brandenburger 2011, Thm 8.1 (a factorizable HV realization exists iff a global section exists; this is the empirical-model form) **[R]**;
Burešová–Pták 2024 Thm 3.1, which owns "points := two-valued states" **[R via shelf note]**.

Consequences:
- **L(H), dim ≥ 3.** There are no homomorphisms (KS), so no state extends at all. That is the paper's open item 1
  ("every state"). It follows in one line from KS, so neither the sketched footnote nor the MO₂ device is needed.
- **L(ℂ²), and MO_n with n ≥ 2.** There are no homomorphisms either, so PR_dual fails in dimension 2 too. The paper treats
  dim ≥ 3 as the dividing line.
- **General OMLs.** Open item 1 asks whether every state on a general OML extends, and calls this open. The answer is
  **no** already on the 6-element MO₂: s(a) + s(a^⊥) + s(b) + s(b^⊥) = 2 > 1 over four pairwise meet-zero elements.
  MO₂ is the paper's own example (line 382). The natural general question has the answer above: exactly the mixtures
  of homomorphisms.

**Verdict on (c).** Under the RN1 rule, (c) is an **existing notion (non-contextual hidden-variable representability) under
a new name** ("PR_dual, a measure on S₀(A)"). The McDonald–Bimbó dual adds no content to it. This is ⟦H⟧, not
Lean-checked. The argument is short and uses only standard facts (Radon extension on a Stone space, τ-additivity,
meet-preservation of h, which the shelf McDonald–Bimbó entry confirms). The auditor's confidence is high, and the
verdict is therefore KNOWN rather than UNCLEAR. If the user rejects the ⟦H⟧ step, downgrade the verdict to UNCLEAR.
The referee estimate below is REJECT-LIKELY either way, because of the correctness items.

### Correctness findings (independent of novelty)

| # | Location | Finding | Severity | Read level |
|---|---|---|---|---|
| C1 | Thm `thm:bub-clifton` (lines 576–588), statement (i) | "D(ρ,R) is a Boolean algebra" is **false as stated**. Bub (quant-ph/9910096, p.≈7) says the determinate sublattice "need not be a Boolean algebra". D includes all rays orthogonal to the span of ψ's projections onto R-eigenspaces. The theorem's content is that ρ restricted to D is a mixture of 2-valued *homomorphisms* on a possibly **non-Boolean** D. Lines 590–593 and §4 ("Bell's beables … maximal Boolean subalgebra") inherit the error. | **High.** A phil-physics referee who knows Bub 1997 catches this on page 5. | [R] Bub 1999 passage, lines 312–315 and 382 of the extracted text |
| C2 | Thm 3.2(b), 5th bullet | "VDR holds locally within each Boolean context (Bub–Clifton)". Every Boolean block has ultrafilters, so this is trivial, and it is not what Bub–Clifton proves. | Medium | [H] |
| C3 | Footnote at line 940; §4 "If not, the colimit is orthomodular and VDR may be blocked" | "Non-distributivity of the colimit is **equivalent** to non-existence of a joint distribution" is **false**. The paper's own Example (contexts (A,B), (A,C)) is non-distributive. Its context graph is a tree, so every compatible pair of marginals glues (Vorob'ev 1962; conditional independence given A). Non-distributivity is a property of the algebra. Contextuality is a property of a state or empirical model. This category error also undercuts the thesis that "distributivity is the commensurability condition": distributivity is refuted as the dividing line. Acyclicity of the context hypergraph is a *sufficient* condition (Vorob'ev) for a *different* predicate, gluing of states. It is not necessary, and it does not characterise VDR availability: loopy OMLs can have plenty of two-valued states. | **High.** It is the central slogan. | [R] Vorob'ev is in the programme taxonomies; [H] the example |
| C4 | Descent footnote (line 537) vs Discussion item 1 (lines 964–970) vs abstract and Thm 3.2(b) | Whether singular states extend is called "open" in one place and "settled" in another. The theorem and abstract say "normal" only. | Medium (internal contradiction) | [R] |
| C5 | Line 380 | "Dispersion-free = 2-valued homomorphism … on L(H)". This is false for dim H = 2: L(ℂ²) = MO_𝔠 has dispersion-free states, and by the paper's own MO₂ argument they are not homomorphisms. For dim ≥ 3 it holds only vacuously. | Low–medium | [H] |
| C6 | Ladder, lines 621–631 | "VDR_σ ⇒ PR_dual". This is false for dispersion-free states, which the paper calls "the operative notion". On MO₂ (finite, so σ-additivity is automatic) a dispersion-free state exists and no state extends. It holds for 2-valued homomorphisms (Dirac measures). The hedge "in the dual-realising scope" is undefined. | **High.** The ladder is the organising picture. | [H] |
| C7 | Thm 3.2(b), PR_lat bullet | Gleason does no work for *existence* of a σ-additive state, since vector states give one trivially. Gleason's content is the trace form, which the paper never uses. | Low (presentation), but a referee will notice | [M] |
| C8 | Thm 3.2 heading "non-distributive (OML with A ≅ L(H))" | The heading promises the non-distributive case, but the proof covers L(H) only. The general-OML clause is missing. | Medium | [R] |
| C9 | §2 opening ("Gunji et al. show that gluing Boolean algebras … produces an OML … The OML is *forced*") | Pastings of Boolean algebras need not be OMLs. Greechie's loop lemma (Kalmbach Ch. 4, on shelf): loops of order 3 break the orthomodular lattice property. "Forced" is too strong unless Gunji et al. carry hypotheses that the paper does not state. Gunji 2026 is unread. | Medium | [M]; Gunji [A] |
| C10 | Boolean part, lines 245–247 | μ̂(pure(Ω)) = 1 presupposes that pure(Ω) is measurable. The paper needs "outer measure 1" or a measurability hypothesis. | Low | [M] |
| C11 | Discussion, lines 876–881 | "For non-Boolean observations (dim ≥ 3) VDR is algebraically impossible; constructive empiricism is the generic position". This conflates hidden-variable value-definiteness with scientific realism. Bohmian mechanics is realist and contextual. Everettian and structural realism do not need a global dispersion-free state. This is the main **philosophical** objection a BJPS referee would raise. | **High** for BJPS | [M] |

### Applied verdict: not applicable (no methodology claimed). §4's "diagnostic" is conceded to CbD (Dzhafarov–Kujala), correctly.

### Contribution type verdicts

**Type 1 (new theorem): FAIL.** No new theorem is claimed. The one candidate, (c), reduces to the classical
hidden-variable condition ⟦H⟧, and on L(H) it is a one-line corollary of KS.

**Type 3 (unifying framework): FAIL.** No method transfers. The paper places EA, PR_lat, PR_dual and VDR on one axis,
but no technique from Stone/McDonald–Bimbó duality solves a problem in the realism debate, or the reverse. The axis
itself is refuted: by C3, distributivity does not govern gluing, and trees are sufficient for gluing whatever the algebra.
By C6, the ladder does not hold for the paper's own "operative notion".

**Type 4 (vocabulary), three-statements test, applied fresh: FAIL.** Candidate statements stateable "only" in EA/PR/VDR:
1. "PR_lat holds and PR_dual fails on L(H)". In standard vocabulary this reads: "L(H) has σ-additive states, but none is a
   mixture of 2-valued homomorphisms", which is KS. It is stateable in standard terms.
2. "The three transitions pasting / regularity / sharpness are of different character". This relabels
   states ⊇ σ-states ⊇ dispersion-free states, which the paper concedes are standard. No theorem distinguishes them
   beyond the table.
3. "Bell's beables = D(ρ,R)". This is Bub–Clifton restated (conceded at line 921), and stated wrongly (C1).

The test needs three statements that are new in the vocabulary, plus one non-trivial result. There is no non-trivial
result that standard vocabulary could not state. The calibration line in `contribution_evaluation.md` should be
revisited (user's call; this audit does not edit it).

**Type 5 (impossibility): FAIL.** The PR_dual failure on L(H) is KS in other words ⟦H⟧. The MO₂ argument is folklore, as
memory already recorded.

**Type 6 (exposition / translation): FAIL at present, CONDITIONAL in principle.**
- (a) **Audience:** named, philosophers of physics.
- (b) **Inaccessible literature:** McDonald–Bimbó 2023 is a 2023 arXiv/journal paper in algebraic logic, so it is plausibly
  unread by that audience. But the content carried across it is the hidden-variable / KS condition. That condition is
  thoroughly accessible to the audience: Bub 1997, Redhead 1987, Pitowsky 1989, the Döring/Isham line, and Eva 2017 in
  BJPS itself.
- (c) **Non-trivial translation work:** the translation adds a second dual-space wrapper around a known condition, and
  in the process introduces errors C1, C3, C6 and C11.

Translating McDonald–Bimbó for philosophers would clear the bar only if the dual space did something the
hidden-variable formulation cannot. The reduction ⟦H⟧ suggests it does not.

### Cross-reference

All components are known. The assembly's one new-looking statement is a known notion under a new name. The organising
axis (distributivity) is refuted by the paper's own example: a non-distributive tree pasting always glues. No type clears. The math that is correct is correct because it is classical. The parts that go beyond the
classics (C1, C3, C6, the ladder) are where the errors are.

### Recommendation (programme)

**Park as a programme contribution.** Types 1, 3, 4, 5 and 6 were evaluated. Type 6 fails on (b) and (c), and Type 4 fails
the non-trivial-result leg. The paper is not dead as writing, but it is not "the survivor" in its present form.

There is one salvage route. It is a *different* paper and needs a new seed plus `/audit full`. Rebuild the paper around the
correct dividing line: tree versus loop contexts (Vorob'ev / Beeri et al. / Abramsky–Brandenburger), and states versus
algebras. Treat PR_dual honestly as non-contextual hidden-variable representability. This is close to what the
programme's current theory (glued carriers) already does better.

**Bearing on WHY.md (one line).** The paper sets distributivity as the line between "one world" and "no world". Its own two-context example refutes that: trees always glue, so a loop is *necessary* for failure (WHY.md question 1), though not sufficient. The paper is a pre-loop framing.

---

### Referee estimate: REJECT-LIKELY

Venue class: none
- Post-rewrite target (not a current estimate): after fixing C1, C3, C6 and C11 and reframing PR_dual as HV representability, an expository/short-note piece in Foundations of Physics or SHPMP. BJPS would also need a philosophical argument the paper does not contain.
- **Value carried by:** none as it stands. Factor 4 (exposition making McDonald–Bimbó usable) is the only candidate. It is
  undercut by "a known object under a new name" (PR_dual = non-contextual HV model), which triggers the RN1 rule, and by
  wrong central claims (C3, C6, C1).
Main risk a referee would raise: PR_dual is Kochen–Specker hidden-variable representability renamed, and the distributivity thesis is refuted by the paper's own example (plus the Bub–Clifton misstatement).

**Caps applied.**
- The pure verdict is KNOWN with an owner found. The paper does cite KS/Pitowsky as the *type* of the obstruction (lines 523–526 and 545–547). What it leaves uncredited is the *identification*: it presents PR_dual as a new grade "not previously isolated" when PR_dual is HV representability. That is the RN1 "known object under a new name" case, so the third cap applies: REJECT-LIKELY unless a clearly
  substantial residual remains. **No such residual was found.**
- If the ⟦H⟧ reduction is rejected, the pure verdict becomes UNCLEAR. The cap is then BORDERLINE at most, and C1, C3, C6 and C11
  (wrong central claims) still push to REJECT-LIKELY.
- ACCEPT-LIKELY is unavailable either way: the nearest prior work was not read beyond snippet level.

**Unread neighbours, named per the cap rule.**
- Kochen–Specker 1967 §§0–1 (the hidden-variable / embedding criterion) [M].
- Gudder 1970, "On hidden-variable theories" (J. Math. Phys.) [P].
- Pitowsky 1989 (*Quantum Probability – Quantum Logic*) [M].
- Bub 1997 (*Interpreting the Quantum World*, Ch. 4–5) [M]; Bub–Clifton 1996 [P via Bub 1999 (R)].
- Halvorson–Clifton 1999 [A].
- Eva 2017 (BJPS, "Topos Theoretic Quantum Realism") [A]. **This is the closest same-venue neighbour**: same question, same
  journal. Its abstract-level framing (topos "realism" via dual-space measures) suggests the referee will be from that circle.
- Döring 2008; Cannon–Döring 2018 [A].
- Stairs 1983 [A].
- Gunji 2026 [A]. Needed to check C9.
- Wright 1990 (mixtures of two-valued states on orthologics; the shelf note flags its scope as doubtful) [A].

### Top changes a referee would require

1. **Fix the false central claims.**
   - Bub–Clifton statement (C1): D need not be Boolean.
   - "Non-distributive ⟺ no joint distribution" (C3), refuted by the paper's own (A,B),(A,C) example. Replace the
     distributivity axis with the context-shape / state-level criterion (Vorob'ev, Abramsky–Brandenburger).
   - The ladder arrow VDR_σ ⇒ PR_dual for dispersion-free states (C6).
2. **Identify PR_dual honestly.**
   - Prove, rather than sketch in footnotes, that extension to S₀(A) ⟺ mixture of 2-valued homomorphisms. Credit
     KS / Gudder / Pitowsky.
   - Then the L(H) failure is KS in one line. Open item 1 is answered by MO₂.
   - The "not previously isolated" claim (lines 197–200, also in the cover letter) must go.
3. **Engage the realism literature properly** (C11). Contextual and realist programmes (Bohm, modal, Everett, structural
   realism) and Eva 2017 show that "VDR impossible ⇒ constructive empiricism generic" does not follow. The paper also
   needs to argue for, not stipulate, why a dual-space measure formalises van Fraassen's empirical adequacy, which is a
   semantic-view notion (embedding of appearances into empirical substructures), not a measure.

### `submission_bjps/` readiness: NOT READY

- It is a **June 24 snapshot that is stale against the current body**. A diff shows it still carries the unqualified "VDR
  implies PR implies EA" and "Distributivity collapses the filtration". The current version retracted both. The
  paper-local-notation remark is also missing.
- The anonymisation is mostly done: `\author{}`, with the author's name only in a LaTeX comment. Remove that comment
  before upload, because the source may be sent. The body cites "manuscript~\cite{mahon2026}", a self-citation that can
  de-anonymise the author under triple-anonymous review. Check the `.bbl` entry.
- The cover letter repeats the "isolating the σ-additive passage to the dual space in McDonald–Bimbó terms" claim, which
  this audit finds to be a renaming. It also lists ChatGPT and Claude use: fine, and BJPS requires it.
- **Do not submit** in either version until the three changes above are made.

---

## Comparison with prior audit (`PAPER_II_AUDIT_VERDICT.md`, 2026-06-23), read after the above was formed

| Point | Prior (2026-06-23) | This re-audit | Why the difference |
|---|---|---|---|
| Correctness | "Central math SOUND"; the ladder was "FINE", including "VDR⟹PR_dual (Dirac) right" | Not sound in the parts that go beyond the classics: C1, C3, C6, C11 | **C6 is a regression introduced after the prior audit.** The paper later made the *dispersion-free state* the "operative notion" (the MO₂ remark), but it kept the arrow VDR_σ ⇒ PR_dual. That arrow holds only for homomorphisms (Dirac), which is what the prior audit checked. C1 (Bub–Clifton "Boolean") and C3 ("non-distributive ⟺ no joint distribution") were not examined in the prior audit. C3's footnote may postdate it. |
| PR_dual impossibility | "Crown jewel", sound; novelty LOW (KS/Pitowsky in MB dress) | KNOWN: PR_dual ⟺ mixture of 2-valued homomorphisms, the classical HV condition ⟦H⟧. On L(H) it is one line from KS, for *every* state and for dim 2 too | Same direction as the prior verdict, but stronger. The prior audit owned the *instance*. This audit identifies the *notion*, which removes the "PR_lat/PR_dual split" as the claimed packaging novelty. |
| Döring 2008 | Blocking: cite and differentiate | Now cited and differentiated (lines 556–569). The differentiation ("σ-additivity as the precise marker of the descent axis") is moot, because the extension step that fails is not governed by σ-additivity: the paper's own footnote says so (line 549) | The prior audit's fix was applied; the claim it protected does not survive. |
| Inherited biconditional | Blocking: hedge to Paper I | Fixed (Loomis–Sikorski realization hedge throughout) | Resolved. |
| p_i^⊥ notation | Blocking | Fixed (e ⊖ p, line 528) | Resolved, but C4 (singular states "open" vs "settled") is new. |
| Type 4 | WEAK; "drop the Type-4 lean" | FAIL | Agrees in substance. **`contribution_evaluation.md` still names Paper II as the Type 4 calibration example that "clears this bar"**, which conflicts with both audits. The user should edit it (this audit did not). |
| Type 6 | **CLEARS** ("rest the contribution HERE") | **FAIL** at present | The prior audit judged Type 6 on community-distance (MB ↔ van Fraassen). This audit asks what the bridge carries. It carries the HV/KS condition, which is accessible to the audience (Bub 1997, Pitowsky, Eva 2017 in BJPS). The translation also introduces the errors. |
| Overall | REVISE; "the survivor"; submit = user's call | PARK as a programme contribution. Referee estimate REJECT-LIKELY. Not submission-ready | **The prior verdict changes.** "The survivor" no longer holds in the current form. |

**What would reverse this re-audit:**
- (i) the ⟦H⟧ reduction (extension ⟺ mixture of homomorphisms) is shown wrong; or
- (ii) a philosophy-of-physics argument is supplied that the dual-space formulation does work the HV formulation
  cannot (for example, the P(A) "distinguished points" structure yields a statement about *descent* that is not
  about homomorphisms).

Either would move the pure verdict to UNCLEAR, cap the estimate at BORDERLINE, and reopen Type 6 as CONDITIONAL.
C1, C3, C6 and C11 must be fixed regardless.

Sources (web, this session): [Bub, "Quantum mechanics as a principle theory", arXiv:quant-ph/9910096](https://arxiv.org/pdf/quant-ph/9910096) (read passage);
[Aplikace Matematiky 17 (1972), hidden-variables-as-mixtures framing](https://www.dml.cz/bitstream/handle/10338.dmlcz/103392/AplMat_17-1972-1_6.pdf) (snippet);
[Halvorson–Clifton, philsci-archive 65](https://philsci-archive.pitt.edu/65) (abstract).

## Places that assert the old verdict (user to update; this audit edited none)

- `CLAUDE.md`, "Other papers": "Paper II is the survivor (Type-6)".
- MEMORY.md, the Paper II entry ("AUDITED + REVISED (the SURVIVOR) … Type 6 CLEARS").
- `notes/programme/contribution_evaluation.md`, Type 4 calibration line: "Paper II (EA/PR/VDR) clears this bar".
- The Paper II rows in `notes/taxonomies_index.json` and `papers/paper_ii/paper_ii_taxonomy.json`.
- `papers/paper_ii/submission_bjps/cover_letter.md`, the "isolating the σ-additive passage" claim.
