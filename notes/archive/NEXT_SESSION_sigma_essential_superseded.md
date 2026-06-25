> ⚑ ARCHIVED 2026-06-25 (σ-essential thread cleanup). Superseded by `forcing_programme_status.md` (the persist-vs-park call is resolved: forcing parked). Kept for the reasoning trail; not current.

# Next-session prompt — σ-essential descent (PARKED; what would un-park it)

*Drop-in prompt for the next working session on the lone open problem. Updated
2026-06-23 (end of Session 13). Since the 2026-06-22 rewrite, the **forcing scout has
run and COMPLETED** (S12 pinned the sentence; S13 ran a deep-research hostile sweep that
priced the forcing route and settled the (a)/(b)/(c) well-posedness flags). Net change:
the forcing route is now **fully priced** — it bottoms out at the same σ-LS wall, with a
named cardinal target (Ulam-measurable). The open call is **persist-vs-park**, and the
leading option on the evidence is **confirm the park**. This prompt records that and names
what would still re-open productive work. Self-contained; detail in the files it points to.*

> **Lost? Read `MAP_sigma_essential.md` first** — one page, the target sentence, the
> three doors, "you are here." Recover the shape in 30 seconds, then come back here.

---

## Status in one paragraph

The lone open problem — **is there a concrete σ-complete OML carrying a σ-additive
contextual state witnessed by no finite sub-OML?** — is **OPEN but PARKED**. Not solved,
not proved impossible. Three independent attack doors (separation §6, cardinality-control,
existence/lifting) have all bottomed out, and Sessions 10–11 showed *why*: the problem
reduces to a **restriction-gap = σ-additive lifting failure**, whose two governing
surfaces (separation and existence) are **duals**, and **both lack any off-the-shelf
engine for the non-Boolean σ case**. The new abstract input that Session 11 went looking
for (a Loomis–Sikorski-type lever) does not exist for non-Boolean σ-OMLs — confirmed by
hostile prior-art. So further *hand*-progress needs a genuinely new object or new abstract
input. **Do NOT re-attack the conjecture or re-walk the doors; read this and decide
whether new input has arrived.**

## Orientation (read these first, in order)

1. `sigma_duality_targets.md` **§9 + §9a** — Session-11 prior-art + existence-route
   result + the two-dual-walls finding + the forward pointer. **This is the live record
   of the park.** §8 = Session-10 (restriction-gap re-identification).
2. `[[sigma_essential_construction_attempt]]` memory — "THE POLE" block (standing
   orientation) + Sessions 9/10/11. Sessions 8b/8c (Lean) and the generator-hunt toolkit
   are now collapsed to spines (band family dead); don't expect verbatim there.
3. `oml_onboarding.tex` (the survey) — authoritative artifact. The "Exhibit a witness"
   item states the restriction-gap target (`A_F`/`B_F` chain); `rem:dw` states the
   Polish-representable settlement; `rem:ce` the finitely-detected form. **Do NOT put the
   parked conjecture or any unproven claim into the survey.**

## The standing guardrails (do not violate)

- **`rem:dw` is STABLE.** σ-essential cell EMPTY for Polish/regular-representable OMLs
  (Derr–Williamson). The residue is the non-representable case = the σ-Loomis–Sikorski
  wall. Do NOT reopen; restate its residue only.
- **The park is "unresolved-open," NOT "impossible."** Lifting (σ-points over each finite
  `F`) is strictly *weaker* than full σ-LS point-realization; the absence of an LS engine
  does NOT entail lifting fails. "No engine" ≠ "lifting fails." Lifting may be TRUE. Do
  NOT promote "couldn't prove" → "proved impossible."
- **Exit-B inclination is held OPEN, NOT a verdict.** ~23 reversals on record. Red-flag
  rule: any positive result, first ask *where did the smuggle enter?* (inner-regularity /
  a π-system / the P(A)↔S_df^σ switch / a finitary obstruction masquerading as σ-essential).
- All novel hand-work flagged `⟦HAND⟧` / `⟦HAND — unverified⟧`; user verifies.

## What is settled / closed (do NOT re-walk)

- **The deliverable IS the restriction-gap** `{s|_F : s∈S_df^σ} ⊊ S_df(F)` = σ-additive
  lifting failure. Non-Borelness of `S_df^σ` is only its descriptive shadow. Off-hull is
  ALWAYS finitely detected (Hahn–Banach in ℝ^L). (§8.)
- **The countable-generation ⟹ lifting conjecture is PARKED.** Prior-art OPEN (no
  off-the-shelf theorem; the **tribe-vs-points gap** is structural — non-Boolean LS gives
  a function-tribe, not separating σ-additive 2-valued points, and needs RDP which OMLs
  fail). The **cardinality-control axis is DISSOLVED** (Burešová–Pták arXiv:2401.13798:
  blow-up indexed by count of ALL states; Borel(2^ℕ) is countably-gen with 2^ℵ₀ states yet
  lifts). The **finitary per-step is always free** (MO₂ (0,0)); only σ-limit relations
  `gₙ₊₁=∨ₖhₖ` can block. (§9, §9a.)
- **Both dual surfaces are walled-of-tools:** separation (§6) → disjointification
  `(a∨b)∧a⊥=b∧a⊥`; existence → σ-LS point-existence. The double-absence is the finding.
- **All carrier-construction routes dead:** faithful σ-tribe (Floor); all five binding
  modes; the entire band family (S8 dichotomy, Lean-certified); loops/Greechie/KS-configs
  (finite-character ⟹ fail σ-essential); finite-assembly generally (the lever must be
  GLOBAL/non-compositional, S11 negative-space). The carrier, if it exists, is
  **non-loop, non-central, non-band, non-segregated, non-finite-character**, plausibly
  **uncountably generated**, and its σ-points must arise **non-constructively**.

## THE ONLY THING WORTH DOING NEXT (gate the session on it)

**Has new input arrived?** Productive hand-work needs ONE of:

1. **A non-constructive σ-point existence principle for non-Boolean σ-OMLs.** The forward
   pointer (§9a): no LS engine delivers σ-points for non-Boolean σ-OMLs, so a witness's
   σ-additive 2-valued states (or the proof that enough exist) must come from a
   *non-constructive* source — a fixed-point / compactness / Baire-category / forcing-style
   argument, NOT a representation theorem. If you can NAME such a principle and it bears on
   either (a) "enough σ-additive 2-valued states to lift every finite df-state" [⟹ lifting
   TRUE, witness must be uncountably generated] or (b) a σ-OML where they provably fail to
   lift [⟹ the witness], that is the call to make. Take it to the advisor framed as: "I can
   name lever X that supplies/denies σ-points without an LS engine — does it touch lifting?"

2. **A genuinely new candidate object** that is non-segregated, off-center, σ-complete,
   concrete, non-Boolean — the object the whole programme lacks. Before spending effort,
   run it against the three unit tests (§9a refutation gate): (i) must NOT segregate
   (∏ₙMO₂); (ii) must NOT reintroduce intersection-closure (Floor → Boolean); (iii) must
   NOT be finite-character (Wright → finitely witnessed → not σ-essential). A candidate
   surviving all three is the prize; one failing a test is logged and dropped.

3. **The set-theoretic tripwire fires.** If any construction starts needing extra axioms
   (measurable cardinal / V=L / ¬MA), that is the `rem:dw` "rhymes with ZFC-independence"
   prediction coming true — record it as an independence-flavoured finding, a real result.
   **⟦S13 UPDATE (CORRECTED after Phase-2 audit): the tripwire is partially visible from
   prior art, but NOT via a "Boolean-factoring port" — that was retracted.⟧**
   Blecher–Weaver (arXiv:1607.08505, *JFA* 272 2017) prove that on `B(ℓ²(κ))`'s projection
   OML, a singular σ-additive 2-valued (pure) state exists ⟺ κ is **Ulam-measurable** — a
   genuine large-cardinal tripwire on a non-distributive σ-complete OML. ⚠⚠ The earlier
   gloss here — *"the cardinal bites only through the abelian diagonal masa (the
   'distributive routing port'); no instance bites WITHOUT factoring through a Boolean
   sub-object"* — is **RETRACTED, FALSE for the pure/2-valued case.** Masa-factoring holds
   only for B–W's *real-valued* dichotomy; the **pure** case does NOT factor (B–W use
   Marcus–Spielman–Srivastava paving because Anderson's conjecture is false under CH), and
   **Akemann–Weaver (PNAS 105(14) 2008, p.5313) give a pure state on B(H) multiplicative on
   NO masa** — a direct counterexample. There is **no "routing port" meta-principle**; the
   pure/2-valued non-commutative case is itself genuinely OPEN. So the honest reading: the
   B(H) tripwire is real but does NOT reduce to the abstract-OML target, and the residue is
   the **σ-LS / RDP wall** (no σ-Loomis–Sikorski for non-distributive OMLs), not a port to
   build. The Ulam-measurable target + the B–W/Dzhenzher anchor remain the toolkit IF you
   pursue this, with Akemann–Weaver as the cautionary counterexample. Detail:
   `sigma_essential_prior_art_verdict.md` 2026-06-23 CORRECTION; `CHARTED` ⚠⚠ + FENCE;
   parked seed `notes/covered_leads/boolean_factoring_sigma_essential_PARKED.md`.

**If none of the three has arrived, the honest move is: confirm the park stands, do NOT
manufacture a fourth door, and stop.** ⟦S13: the forcing scout has now run and priced the
forcing route — it does not get around the wall (it must first supply σ-points for a
non-representable concrete σ-OML = the same σ-LS wall; the "routing port" phrasing for this
is RETRACTED, see the corrected item-3 above). The (a)/(b)/(c) flags are settled: the forcing sentence
is well-posed, so Door 3 *can* be cleanly stated; what's missing is not formulation but the
port. The persist-vs-park decision is therefore decidable NOW (human's call;
`thesis-advisor` agent is the right checkpoint). Leading option on the evidence: confirm the
park (three independent passes — S11 dual-walls, S12 forcing-wall, S13 deep-research-wall —
each strengthened `rem:dw`).⟧ The three-doors-→-two-dual-walls convergence is the current
finding; thrashing for a fourth route is the ~23-reversal failure mode. A *partial* result
(e.g. "lifting holds under hypothesis H") is progress; a *failed* candidate that died on a
unit test is progress (log which test). "Couldn't prove" ≠ "impossible"; "couldn't refute"
≠ "proved."

## The fixed setting (definitions you need)

`L` a concrete σ-complete OML, realised as a σ-Dynkin system `D ⊆ P(X)`. For finite
sub-OML `F ⊆ L`:
- `S_df` = global dispersion-free states (2-valued on all of `L`); weak-* compact.
- `S_df^σ` = the **σ-additive** dispersion-free states — a (possibly proper) subset of
  `S_df`; NOT weak-* closed (the CE phantoms, `rem:ce`). Contextuality predicate is
  `w ∉ conv̄(S_df^σ)` (the σ-restriction is load-bearing).
- `S_df(F)` = ALL 2-valued states on finite `F`. On finite `F` every state is σ-additive,
  so the σ-content lives only in which *global* states restrict to `F`.
- **Lifting holds** ⟺ `S_df(F) = { s|_F : s ∈ S_df^σ }` for every finite `F` — every local
  df-state is the restriction of a global **σ-additive** one. Always `⊆`; lifting is `⊇`.
- A σ-essential witness exists ⟺ the **restriction-gap** `{s|_F:s∈S_df^σ} ⊊ S_df(F)` is
  non-empty for some finite `F`.

## Flagged forward-looking sub-question — RESOLVED 2026-06-22 (no longer a live edge)

The predicate fork ("σ-additive measure genuinely on `S_df^σ`" [P-strong] vs
`w ∈ conv̄(S_df^σ)` [P-weak]) is **settled** (user picked it, advisor-checked;
`sigma_duality_targets.md` §6 RESOLVED block). Result: **P-weak ⟹ P-strong always; on
σ-additive `w` the two are CO-EXTENSIVE ⟺ σ-point-realization (door 1)** — so they agree
on Boolean, Polish-representable (`rem:dw`), and all **segregated** objects (central
decomposition + σ-additivity ⟹ point-concentration; verified on `∏ₙMO₂`). They diverge
**only on the missing non-segregated/non-Polish witness**, where P-strong is the cleaner
target. **Net for the open problem: the predicate choice doesn't matter until a witness
exists; if one does, state it with P-strong.** This is a restatement of door 1, NOT a new
door — does not un-park. (The trivial reading — any `w` — splits vacuously via phantoms;
that is a smuggle-trap, not inhabitation.)
