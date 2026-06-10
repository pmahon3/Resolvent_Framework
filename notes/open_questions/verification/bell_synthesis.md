# Bell's theorem ↔ the σ-additive-OML open problem — synthesis

**Date:** 2026-06-10. **Input:** `bell_deepresearch_partial.json` (deep-research run,
102 agents, died at synthesis; 25 claims reached the verifier, 8 cleanly confirmed
before the first session reset). **Method:** synthesis only — no new searches.

---

## ⚠ Read the "8 confirmed / 17 killed" honestly

The run hit a session/token limit **twice** (7:50pm reset, then 12:50am reset). The
log shows the consequence clearly:

- **Batch 1 (before 12:50am reset):** 10 claims reached real verifiers. 8 confirmed
  with genuine adverse-or-supporting votes (`3-0`, `2-0`); 2 "killed" only because
  their verifiers crashed mid-vote (`0-0 (3 abstain)`, `1-0 (2 abstain)`).
- **Batch 2 (after 12:50am reset):** **every** verifier failed with
  "session limit" → almost all of the "17 killed" are `0-0 (3 abstain)` —
  i.e. **NOT run, not refuted.** The harness labels an un-confirmed claim "killed,"
  but abstention-by-infrastructure-failure is not adverse evidence.

So the real tally is: **8 claims positively confirmed; the rest unadjudicated.**
Crucially, the unadjudicated claims (Abramsky–Brandenburger sheaf unification, the
Fine-is-finitary claim, the "framework is entirely finitary, no σ-additivity"
claims, the Pitowsky-H3-has-no-quantum-content claim) are exactly the ones that
would, if confirmed, **most strongly support the survey's gap**. They were not
refuted; they were never tested. None of the 8 confirmed claims contradicts them.

**No claim — confirmed or abstained — asserts a σ-additive / countably-additive
result in the Bell/contextuality literature.** The closest (the un-run Pitowsky-H3
claim) says the opposite: completeness/σ-closure carries *no* essential quantum
content for Pitowsky.

---

## Grouped, ranked findings (the 8 confirmed)

All 8 sit on **angle 1 (Bell = extension/joint-distribution feasibility)** and
**angle 3 (KS = no two-valued homomorphism)**. Angles 2, 4, 5 — the σ-additivity,
sheaf, and point-free angles, i.e. the ones that could pre-empt the open problem —
produced **zero confirmed claims** (their claims all fell in the crashed batch 2).
This is itself the headline: the literature the run surfaced is entirely finitary.

### Tier 1 — confirmed `3-0` (highest confidence)

1. **Bell inequalities = facets of a finite correlation polytope.** The classical
   probability vector must lie in the convex hull of the 16 truth-value vertices in
   ℝ⁸; the facets *are* the Clauser–Horne/Bell inequalities; QM falls outside.
   *(Pitowsky, philsci 2474 / TOBUB1.)*

2. **Bell is an extension/joint-distribution obstruction**, not fundamentally a
   locality one: violation arises from assuming a single joint truth-value
   assignment over incompatible propositions. *(philsci 2474.)*

3. **Budroni–Morchio: PBAs/PPTs unify Bell-type and KS-type** classical
   representability as **one extension problem** for partial Boolean algebras.
   *(arXiv:1010.4662.)*

4. **Classical representability ⟺ extension of the partial Boolean algebra to a
   single Boolean algebra carrying a normalized measure**, with necessary-and-
   sufficient conditions **supplied by Horn & Tarski's partial measure.** This is
   the explicit *Horn–Tarski feasibility* framing — the survey's exact §5 anchor.
   *(arXiv:1010.4662.)*

5. **The Budroni–Morchio criterion is read off Pitowsky's correlation polytopes and
   recovers Fine 1982** (four-observable model exists iff two three-observable
   models agree on overlaps). Ties the abstract framing to Pitowsky 1989 + Fine 1982.
   *(arXiv:1010.4662.)*

6. **KS contradiction = non-existence of a homomorphism (projection PBA)→{0,1}**
   (a two-valued/multiplicative measure); any KS obstruction forces a Bell
   violation for every quantum state. Confirms the survey's reading of KS as the
   failure of two-valued states, and links KS→Bell. *(arXiv:1010.4662.)*

7. **Membership in a correlation polytope is NP-complete** (facets probably not in
   NP). The feasibility face of Bell is a **finite, computationally hard** problem —
   finitary, not infinitary. *(Pitowsky, BF01594946.)*

### Tier 2 — confirmed `2-0`

8. **Fine's five-way equivalence**: deterministic HV model ⟺ factorizable stochastic
   model ⟺ one joint distribution for all observables ⟺ compatible joint
   distributions for all commuting+noncommuting pairs/triples ⟺ Bell inequalities
   hold. **Bell is a joint-distribution-existence (extension) question.**
   *(Fine 1982, scispace.)*

### Un-adjudicated but gap-supporting (abstained only because verifiers crashed)

- Fine's equivalence is **finitary** (finite observables/pairs/triples, no countable
  additivity). *(scispace.)*
- The PBA/PPT framework is **explicitly finitary**: finite Boolean algebras, finite
  additivity only — **no σ-additivity, no infinite orthogonal families.**
  *(arXiv:1010.4662.)*
- The marginal-problem / polyhedral-projection literature is **entirely finitary**,
  no engagement with countable additivity, OMLs, or point-free measure.
  *(arXiv:1805.03313.)*
- Abramsky–Brandenburger unify Bell + KS as **"no global section of a presheaf"** of
  Boolean-context data. *(arXiv:1102.0264.)* — the sheaf framing exists, but **its
  base is the poset of finite Boolean contexts; no σ-additivity claim was found.**
- **Pitowsky treats H3 (completeness / σ-closure) as carrying NO essential quantum
  content** — the quantum/classical split comes solely from irreducibility
  (non-distributivity), and probability is read off *finite* segments of L.
  *(philsci 2474.)* — if confirmed, this is the single most relevant claim:
  it says the σ-closure layer was *deliberately set aside* as inessential, i.e.
  **the descent axis was never engaged, not that it was settled.**

---

## (a) Is the {σ-additive × point-free × natively non-distributive} gap real?

**Yes — confirmed, and the evidence is one-sided in its favor.**

- Every confirmed result places Bell/KS on the **finite extension axis**: convex
  polytopes (finite-dim), Horn–Tarski partial measures (finite additivity), partial
  Boolean algebras (finite), NP-complete feasibility (finite). This is exactly the
  axis the survey marks **settled** (§5, Horn–Tarski/Pitowsky).
- **Not a single claim** — confirmed or abstained — exhibits a σ-additive /
  countably-additive treatment, an infinite orthogonal family, or a point-free
  measure on an OML, in the Bell/KS literature. The angles that *could* have
  pre-empted it (2, 4, 5) returned zero confirmed claims and, where the underlying
  source spoke at all, spoke *finitarily* (Pitowsky H3 = no quantum content).
- The sheaf/topos unification (Abramsky–Brandenburger; Bohrification) is real but
  builds over a poset of **Boolean** contexts — distributive local data — which is
  the frame/Heyting setting, **not** a natively non-distributive (OML) σ-additive
  measure. Distinct structure; does not occupy the slot.

This corroborates the survey's two-axis claim **exactly**: Bell is the *finitary
shadow of the extension axis*, fully absorbed under Pitowsky/Horn–Tarski; **it does
not reach the σ-additive descent axis** (Q1 structural / Q2 descent-relevance). The
hinge (†) is untouched by anything Bell-theoretic.

## (b) Any result that PRE-EMPTS the open problem?

**No.** Nothing surfaced poses σ-additive point-free probability on a natively
non-distributive OML.

The nearest contact — and it is the opposite of a pre-emption — is the
(un-adjudicated) **Pitowsky H3 claim**: the σ-closure axiom was explicitly judged to
carry no essential quantum content, so it was bracketed off and the analysis lives on
finite segments. That is the descent axis being **declined as uninteresting**, not
**resolved**. The open problem asks the question Pitowsky set aside.

**Caveat on coverage — now closed.** The deep-research run died before exhausting
angles 2/4/5. A targeted single-scout pass (sonnet, 2026-06-10) swept exactly the
un-swept corner — the topos/point-free σ-additivity literature. Result below.

### Angle 4/5 scout sweep (2026-06-10) — the residual corner

The scout checked the four literatures that could host the slot. **Verdict:
UNOCCUPIED.** The three conditions exist pairwise but never all three together. The
decisive distinction throughout: *non-distributive structure mentioned* ≠
*σ-additivity carried on the non-distributive structure itself, point-free.*

1. **Bohrification (Heunen–Landsman–Spitters, arXiv:0909.3468 / 0905.2275).**
   σ-additivity is carried by the **internal distributive locale** Σ_A (a frame), not
   the projection OML. States ↔ probability integrals/valuations on the internal
   *commutative* algebra. The programme **escapes non-distributivity by moving to a
   distributive base** — does NOT occupy the slot.
2. **Localic valuations (Coquand–Spitters arXiv:0808.1522; Vickers; "Measure theory
   via Locales" arXiv:2510.08826).** Base is **always a frame/locale** —
   distributivity is definitional (modular law, Scott-continuity). No non-distributive
   base anywhere.
3. **σ-additive states on OMLs (Navara–Rogalewicz; Dvurečenskij–Pulmannová,
   *New Trends in Quantum Structures* 2000; arXiv:1501.00597; spectral-presheaf
   arXiv:0809.4847).** σ-additivity IS native to the OML here — but the framing is
   **point-based** throughout (Gleason, spectral/Hilbert representations, or a concrete
   Ω). Never representation-free.
4. **Loomis–Sikorski for σ-complete non-Boolean structures (Dvurečenskij σ-MV 2000;
   Buhagiar–Chetcuti–Dvurečenskij effect-tribes 2006; EMV arXiv:1707.00270).** All
   generalisations represent the algebra as a **quotient of functions on a classical
   point-set Ω** — point-based. **No Loomis–Sikorski / σ-Stone theorem for σ-complete
   OMLs exists** (MV/effect-algebra proofs do not carry to OMLs; Cannon's OML spectral
   presheaf is a logical duality, not σ-additivity-carrying).

Pairwise occupancy: {σ-add × OML} point-based; {σ-add × point-free} distributive-base;
{point-free × non-distributive} logical-duality-only (σ-additivity absent or carried
distributively). **No source poses the triple.** This is direct, independent
corroboration of the survey's Q1 (σ-Stone duality / Loomis–Sikorski for σ-complete
OMLs: none known, none ruled out) being genuinely open — and of the gap being real,
not an artifact of the truncated deep-research run. **No pre-emption found.**

---

## Bottom line for the survey

The §5 framing survives intact and is positively corroborated: **Bell = finitary
extension axis (Pitowsky/Horn–Tarski/Fine/Budroni–Morchio), settled; the σ-additive
descent axis (Q1/Q2, hinge †) is untouched and unoccupied.** Verdict on the open
problem is unchanged.

> *(Note 2026-06-10: this conclusion — Bell does not touch the descent axis —
> remains correct. Separately, the hinge (†)/(★) itself was later resolved YES
> from Navara p. 428 (descent structure established); the open descent question
> moved to concreteness of L_MO₂. That resolution is internal to the descent
> work and does not change anything Bell-theoretic here. See
> `../descent_axis_residue_post_kill.md`.)* No citation in the survey needs revision; optionally,
**Budroni–Morchio (arXiv:1010.4662)** is a clean citation to add for the
"Bell+KS = one extension problem" point, since it states the Horn–Tarski framing
more explicitly than Pitowsky alone.
