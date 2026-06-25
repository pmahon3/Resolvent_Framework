> ⚑ ARCHIVED 2026-06-25 (σ-essential thread cleanup). Superseded by the resolved result `sigma_essential_reduction_writeup.md` + the working ledger `CHARTED_sigma_essential.md`. Kept for the reasoning trail; not current.

# MAP — σ-essential descent (read this FIRST, 30 seconds to recover the shape)

*The one-page index. Everything detailed lives elsewhere; this is the map that was
missing. Last synced 2026-06-23 (forcing scout + deep-research sweep COMPLETE; the
cheap reconnaissance is done — the open call is now persist-vs-park). If this drifts
from the working notes, the working notes win — but fix this.*

---

## THE TARGET (the whole thing, one sentence)

> **Is there a concrete σ-complete OML carrying a σ-additive contextual state
> witnessed by no finite sub-OML?**

Equivalently (the sharp form): a concrete σ-complete OML `L` with a **restriction-gap**
`{s|_F : s ∈ S_df^σ} ⊊ S_df(F)` for some finite `F` — global σ-additive dispersion-free
states fail to restrict onto the local df-state hull. *(= σ-additive lifting failure.)*

**STATUS: OPEN, PARKED.** Not solved, not proved impossible.

---

## THE ONE THING TO DO (everything reduces to this)

> **Construct — or refute the existence of — a binding global σ-additive
> 2-valued point over a concrete σ-complete non-Boolean OML.**

This is **Door 1**. It is the only way through. The "three doors" of the prior map are
not three routes — they are the **three possible exits of this one question**:

| If Door 1 resolves as… | …the exit is | name |
|---|---|---|
| the point **exists** (construct it) | a **witness** | Exit A |
| the point exists in one model of ZFC, fails in another (forcing) | an **independence** result | Door 3 |
| the point provably **cannot** exist | an **impossibility** | Exit B |

**You do not choose an exit. You work Door 1 and find out which one it has.**
Door 2 (a candidate object) and Door 1 are the *same construction* — an object is a
witness only if it carries the point. Door 3 can't even be *stated* until the object
exists. All roads run through Door 1.

---

## HOW Door 1 must be attacked (the tool is forced)

- **By-hand / compositional construction is CLOSED.** Every elementary assembly hits a
  horn (the construction log is a graveyard; see "Settled" below). Don't re-try it.
- **The lever must be GLOBAL and NON-CONSTRUCTIVE.** The record proved this: any
  pairwise/finite-assembly spec of `A∨B` across non-orthogonal pairs collapses to a
  closed horn. So the point cannot be *built* locally — it must be *summoned* globally.
- **⟹ The only tool left is FORCING** (or an inner-model argument). The missing object
  and the independence proof are plausibly the *same* forcing construction: a forcing
  that adds/controls the σ-points over the OML is simultaneously Door 1's existence
  engine and Door 3's independence proof.
- **WHERE it can bite:** only at the **uncountable-block / `S_df^σ`-density** level. On
  ℕ the obstruction is a clean ZFC contradiction (`⋂A_k=∅`) — no independence to be had
  there. Any forcing/large-cardinal action lives on the uncountable version.

**The honest cost:** this is a months-long, set-theory-heavy programme (iterated forcing,
plausibly a measurable cardinal or its failure), with a real chance the answer is "the
object can't be set up coherently" rather than a clean theorem.

---

## THE FORCING SCOUT — COMPLETE (2026-06-23). Result below.

The scout (the cheap reconnaissance) is DONE — both the pin and the survey, plus a
4-agent deep-research hostile sweep that substituted for the blocked advisor pass.
What it returned:

- **The sentence is PINNED and WELL-POSED.** `Ψ` = "∃ admissible `L` (concrete ∧
  σ-complete ∧ non-Boolean ∧ off-center) with `¬Φ(L)`," `Φ(L)` = every finite local
  df-state extends to a global σ-additive 2-valued state. Flags (a)/(b)/(c) all CLEARED
  (deep-research sweep #4): (a) `Φ` is a clean existential (Horn–Tarski lineage); (b)
  off-center is genuinely *derived* (Kalmbach center-decomposition), so the restriction
  is lossless; (c) `Ψ` is ZFC-independent-*statable before* a witness exists (von
  Neumann/Maharam precedent) — flag (c)'s pessimistic "the wall blocks *formulating*
  Door 3" is **REFUTED**. Door 3 can be cleanly stated.
- **"Q stated nowhere" PARTIALLY REFUTED.** Blecher–Weaver (arXiv:1607.08505, *JFA* 272
  2017) state+solve exactly this existence question on ONE non-distributive σ-complete
  OML — the projection lattice of `B(ℓ²(κ))`: a singular ctbly-additive pure ({0,1})
  state exists ⟺ κ Ulam-measurable (not ZFC-provable; active 2026 line, Dzhenzher
  2604.25854 / 2605.24923). **You must engage this directly** as the prior-art anchor.
- **The wall holds for the park — but for the σ-LS/RDP reason, NOT a "Boolean-factoring"
  one.** ⚠⚠ **CORRECTION 2026-06-23 (Phase-2 audit, B–W proof read verbatim):** the first
  write-up here claimed "B–W STRENGTHENS the wall — the cardinal bites only through the
  abelian diagonal; no phenomenon bites without a Boolean sub-object." That is **FALSE**.
  Masa-factoring holds only for B–W's *real-valued* dichotomy; the **pure / 2-valued**
  case (the σ-essential object) does NOT factor — B–W use Marcus–Spielman–Srivastava
  paving because Anderson's conjecture is false (CH), and **Akemann–Weaver (PNAS 105(14)
  2008) give a pure state multiplicative on NO masa** = a direct counterexample. The
  "Boolean-factoring / distributive-routing-port" thesis is RETRACTED (also failed
  Phase-2 audit as a Type-5 seed: definitional tautology + inverted evidence). What
  genuinely walls the park is the **σ-LS / RDP gap**: σ-Loomis–Sikorski is solved only
  for RDP structures (MV/effect algebras); OMLs lack RDP (MO₂), so no σ-LS for
  non-distributive OMLs. The DST + ZFC-independence framing of the residue has no prior
  art. `rem:dw` UNAFFECTED (it's the DW Polish cut, not a B(H) claim). Full retraction:
  `sigma_essential_prior_art_verdict.md` 2026-06-23 CORRECTION; `CHARTED` ⚠⚠ + FENCE;
  parked seed `notes/covered_leads/boolean_factoring_sigma_essential_PARKED.md`.
- **The frontier (set-theoretic dress, corrected):** the genuinely open analogue is
  whether **σ-additive 2-valued state existence on an abstract concrete σ-complete OML
  (not Hilbert/Polish-realizable) is ZFC-independent** — the B(H) case (B–W) shows the
  *Hilbert-realized* version is large-cardinal-sensitive, but it sidesteps σ-LS by
  supplying `H`; the target lacks `H`. That gap = `rem:dw` residue = the unclaimed cell.

**The price of a forcing programme: it must first supply σ-points for a non-Hilbert,
non-Polish concrete σ-OML — which is the σ-LS / tribe-vs-points wall (no σ-LS for
non-distributive OMLs).** Forcing does not get *around* Door 1; it bottoms out at the
same place. (The cardinal target is Ulam-measurable on the Boolean side, but — per the
correction above — there is no established "routing port" carrying it to the
non-distributive side; that routing was the retracted thesis.)

---

## THE ACTUAL NEXT ACTION — the persist-vs-park call (yours; now fully priced)

Problem-selection is the human's call; the reconnaissance is complete, so this is
decidable now. The three options:

- **(a) Commit to the forcing programme.** Step 1 is building the distributive-routing
  port = attacking the σ-LS/tribe-vs-points gap with an Ulam-measurable target. Large,
  real, months-long, and bottoms out at the known wall — but the target is now NAMED.
- **(b) Confirm the park.** The method has named the residue three times now (S11
  dual-walls, S12 forcing-wall, S13 deep-research wall) and each pass strengthened
  `rem:dw` rather than cracking it. Honest stop. *(Leading option on the evidence.)*
- **(c) Something genuinely new** — a new object or abstract input. None has arrived;
  the only thing that un-parks.

**No rush; thesis-advisor territory.** If you want a structured persist-vs-pivot pass,
run the `thesis-advisor` agent on this — it's exactly the checkpoint it's for.

---

## THE STANDING GUARDRAILS (violating these = the failure mode)

- **`rem:dw` is STABLE.** σ-essential cell EMPTY for Polish/regular-representable OMLs
  (Derr–Williamson). Residue = non-representable case = σ-LS wall. Restate, never reopen.
- **"Couldn't build it" ≠ "needs choice" ≠ "independent of ZFC."** Three different
  claims, increasing strength. We have the first (proved), suspect the second
  (conjecture), have NOT shown the third (= Door 3, the open work). Don't slide up the
  chain without doing the math. (Nor couldn't-refute → proved.)
- **CARRYING vs SELECTING** *(the discriminator from the 2026-06-22 Door-1 thread)*: the
  difficulty is NOT that blocks can't hold the mass (states are plentiful — `S_df`
  compact, `∏ₙMO₂` state-rich; "horizontal-sum-destroys-states" is a KILLED premise). It
  is that **selecting one globally-coherent σ-additive point** across all incompatible
  block-pairs at once is the non-compact inverse-limit / free-ultrafilter existence step.
  Door 1 is a *selecting* problem, not a *carrying* one.
- **Exit-B inclination held OPEN, not a verdict.** ~23 reversals on record.
- **Red-flag rule:** on ANY positive result, first ask *where did the smuggle enter?* —
  inner-regularity / a π-system / the `P(A)↔S_df^σ` switch / a finitary obstruction
  masquerading as σ-essential.
- All novel hand-work flagged `⟦HAND⟧`; user verifies. Survey gets NO unproven claim.

---

## SETTLED — do NOT re-walk (this is most of the ~23 reversals, now closed)

- **Deliverable = the restriction-gap** (above). Non-Borelness of `S_df^σ` is only its
  descriptive shadow. Off-hull is ALWAYS finitely detected (Hahn–Banach in ℝ^L).
- **Duality determined at (i)+(ii)** = Derr–Williamson σ-Dynkin-systems, inhabited by
  `∏ₙMO₂`. All weight on (iii) = the measure descent = Door 1.
- **Predicate fork RESOLVED** (P-weak ⟹ P-strong; co-extensive ⟺ σ-point-realization =
  Door 1; agree on all segregated/Polish objects; diverge only on the missing witness;
  use P-strong if a witness ever appears). A restatement of Door 1, not a new door.
- **Countable-generation ⟹ lifting: PARKED** (prior-art OPEN; tribe-vs-points structural;
  cardinality-control axis DISSOLVED by Burešová–Pták). Witness, if any, uncountably gen.
- **Order-determination does NOT help** (Paper-I Stone-descent transfer): `δ_x` are
  order-determining for free yet lifting can fail. The OML lacks the Stone-DUALITY leg
  = Door 1.
- **All carrier constructions dead:** faithful σ-tribe (Floor); 5 binding modes; band
  family (S8 dichotomy, Lean-certified); loops/Greechie/KS (finite-character). This is
  why the lever must be global/non-compositional → forcing.
- **Strategy D KILLED** (prior-art, Gaifman 1964). Separate from the descent arc.

---

## THE DOORWAY MAP (which file answers which question)

| If you're asking… | Go to |
|---|---|
| "What's the shape / what do I do?" | **this file** |
| "What's the live record of the park + forward pointer?" | `sigma_duality_targets.md` §9, §9a |
| "What are the two sides of the duality?" | `sigma_duality_targets.md` §1–5 |
| "What's the predicate fork resolution?" | `sigma_duality_targets.md` §6 RESOLVED block |
| "Has new input arrived / what would un-park?" | `NEXT_SESSION_sigma_essential.md` |
| "Why is each construction route dead?" | `sigma_essential_construction_attempt.md` |
| "Is it open / prior-art?" | `sigma_essential_prior_art_verdict.md` |
| "What did the forcing scout + deep-research sweep find?" | `CHARTED_sigma_essential.md` (FORCING SCOUT + DEEP-RESEARCH blocks); `forcing_scout_sentence.md` |
| "The authoritative math write-up" | `oml_onboarding.{tex,pdf}` (survey) |
| "Work it by hand" | `problemset_oml_descent.{tex,pdf}` |
