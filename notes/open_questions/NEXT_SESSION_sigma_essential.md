# Next-session prompt — σ-essential descent (the countable-generation ⟹ lifting sub-theorem)

*Drop-in prompt for the next working session on the lone open problem. Written
2026-06-22 at the end of Session 10 (the DST construction attempt). Supersedes the
prior two-hull-probe prompt — that probe is RESOLVED (it was a degenerate bracket, not
a discriminator; see §8 of `sigma_duality_targets.md`). Self-contained; detail lives in
the files it points to.*

---

## Orientation (read these first, in order)

1. `sigma_duality_targets.md` **§8** — Session-10 findings: the deliverable is the
   restriction-gap, NOT non-Borel `S_df^σ`; off-hull is finitely *detected*; the
   countable-generation sub-theorem. **This is the live edge.**
2. `oml_onboarding.tex` (the survey) — now driven to the ridge, plainly stated. The
   "Exhibit a witness" item in §Directions states the restriction-gap target with the
   displayed `A_F` / `B_F` chain; `rem:ce` states the finitely-detected/globally-caused
   form. The survey is the authoritative artifact — do NOT put unproven conjectures
   into it (the sub-theorem below stays in the working notes until proved).
3. `[[sigma_essential_construction_attempt]]` memory, "THE POLE" block + Session 10 —
   standing orientation + what's closed.

## The standing guardrails (do not violate)

- **`rem:dw` is STABLE.** The σ-essential cell is EMPTY for Polish/regular-representable
  OMLs (Derr–Williamson). The residue is the non-representable case = the σ-Loomis–
  Sikorski wall. Do NOT reopen or re-adjudicate; restate its residue only.
- **Exit-B inclination is held OPEN, NOT a verdict.** ~23 reversals on record; the
  failure mode is tidying "no candidate / no proof yet" → "impossible/proved." **Run the
  red-flag rule:** any positive result, first ask *where did the smuggle enter?*
- All novel hand-work flagged `⟦HAND⟧` / `⟦HAND — unverified⟧`; user verifies.

## The fixed setting (definitions you need)

`L` a concrete σ-complete OML, realised as a σ-Dynkin system `D ⊆ P(X)`. For a finite
sub-OML `F ⊆ L`:

- `S_df` = global dispersion-free states (2-valued states on all of `L`).
- `S_df^σ` = the **σ-additive** dispersion-free states — a (possibly proper) subset of
  `S_df` (glossary, survey). The contextuality predicate is stated against `S_df^σ`
  (`w ∉ conv̄(S_df^σ)`); the σ-additivity restriction is load-bearing, not cosmetic.
- `S_df(F)` = **all** 2-valued states on the finite `F` (the full *local* hull's
  vertices). On a finite `F` every state is trivially σ-additive, so there is no
  `S_df(F)` vs `S_df^σ(F)` distinction — the σ-content lives only in which *global*
  states restrict to `F`.
- **Lifting holds** ⟺ `S_df(F) = { s|_F : s ∈ S_df^σ }` for every finite `F` — i.e. every
  local dispersion-free state is the restriction of a global **σ-additive** one. (This
  is the σ-additive lifting; it is what the restriction-gap measures. A weaker
  "lifts to some global df-state, not necessarily σ-additive" question also exists but
  is NOT the one that decides the witness.)

Standing facts (verified Session 10):
- Always `{ s|_F : s∈S_df^σ } ⊆ S_df(F)`. Lifting is the reverse inclusion.
- **Off-hull is finitely detected:** `w ∉ conv̄(S_df^σ)` ⟺ a finite-support functional
  `Σcᵢ s(aᵢ)` separates `w` (Hahn–Banach in `ℝ^L`, product topology). ⟦HAND — verified⟧
- A σ-essential contextual witness exists ⟺ the **restriction-gap**
  `{ s|_F : s∈S_df^σ } ⊊ S_df(F)` is non-empty for some finite `F`. (Lifting-failure.)

## THE DECISIVE MOVE (lead with this — a theorem to prove or refute)

> **Conjecture (Type-5 impossibility candidate).** *Every **countably generated**
> concrete σ-complete OML satisfies lifting — i.e. its restriction-gap is empty at every
> finite `F`.*

**Why it is the right next move.** It is a genuine theorem (not a re-description of the
gap), and *either* outcome advances the problem non-trivially:

- **If TRUE** ⟹ a witness must be **uncountably generated**. This is a real impossibility
  result (closes the countable case) and narrows the search decisively — every
  construction attempt to date (band families, ∏ₙMO₂, Navara, loops) is countably
  generated, so the theorem would explain *en bloc* why they all failed and redirect
  effort to uncountable carriers.
- **If FALSE** ⟹ the refuting object is a **countably generated witness** (or a clean
  obstruction-free path to one) — i.e. Exit-A, the prize. A counterexample here IS the
  witness.

**Crucial gate (the smuggle-trap to avoid).** This does NOT follow from the π–λ
observation. `∏ₙMO₂` is countably generated with non-π-system generators (π–λ
propagation blocked) **yet lifting HOLDS there** (it is segregated ⟹ coordinatewise
extension ⟹ gap empty). So π–λ-failure is **necessary but not sufficient** for the gap.
The conjecture is consistent with `∏ₙMO₂` whether it is true or false; the unit-test
object decides nothing here. A real argument is required.

## How to attack it (both directions)

**Proof direction (lifting holds).** The target arrow is: *a 2-valued σ-additive state
on a finite `F` extends to a global 2-valued σ-additive state on a countably generated
`L`.* The natural machine:
- Enumerate generators `g₁, g₂, …`. Build the global state by a back-and-forth /
  one-generator-at-a-time extension, maintaining 2-valued σ-additive coherence on the
  sub-OML generated so far.
- The **obstruction to watch**: at each step the agreement/extension set is a **λ-system**
  (complement- and countable-disjoint-union-closed), and propagating a partial 2-valued
  state to the generated σ-OML is a π–λ argument that *needs a π-system* (meet-closed
  generating set) — which an OML can't supply without triggering the Floor. **This is the
  same π–λ wall as §6.** The question is whether *countability of the generator list* +
  *σ-additivity* (continuity from above) is enough to push the extension through the
  countably many steps **despite** the missing π-system — or whether a generator can
  appear at which no coherent 2-valued value exists. That is the crux; it is NOT yet
  settled either way.
- Concrete sub-question: does `σ-additivity` force the extension to be *determined* (not
  merely *constrained*) once values on the generators are fixed? If determined ⟹ lifting
  via a limiting/monotone-class argument. If only constrained ⟹ a branch where two global
  states agree on generators but differ on `L` = exactly the refutation seed.

**Refutation direction (lifting fails).** Seek a countably generated concrete σ-complete
`L` and a finite `F` with a 2-valued state `s_0` on `F` that extends to NO global
σ-additive 2-valued state. By the standing facts this `s_0` (suitably mixed) yields the
σ-essential witness `w`. **Gate:** the failure must be a genuine df-state-set separation
(`{s|_F} ⊊ S_df(F)`), NOT charge-non-σ-additivity (= the ∏ₙMO₂ death). Check any
candidate against the three unit tests:
1. Does it segregate? (run on `∏ₙMO₂` structure — must NOT.)
2. Does it reintroduce intersection-closure? (Floor fires → Boolean — must NOT.)
3. Is it finite-character? (Wright 1978 → finitely witnessed → not σ-essential — must NOT.)

A counterexample surviving all three is the prize; if every candidate fails a test, that
is evidence (not proof) toward the TRUE side.

## What's CLOSED (do not re-walk)

Faithful σ-tribe (Floor); all binding modes (coordinatewise→segregated, atom-share→
loop/band, subtractive→Navara/band); the entire band family (Session-8 dichotomy);
loops/Greechie/KS-configs (finite-character ⟹ fail σ-essential); the two-hull probe
(degenerate bracket, §8); the intrinsic π–λ route as a *standalone* attack (it gates the
sub-theorem above but is not itself a separate open thread). The carrier, if it exists,
must be **non-loop, non-central, non-band, non-segregated**, with contextuality of
**non-finite character** — and, per the conjecture, plausibly **uncountably generated**.

## If the session ends without resolving it

Record honestly: a *partial* proof (e.g. "lifting holds under additional hypothesis H")
is progress; a *failed* counterexample that died on a unit test is progress (log which
test). Do NOT promote "couldn't refute" to "proved," nor "couldn't prove" to
"refuted/impossible." Both are the ~23-reversal failure mode. The conjecture stays in the
working notes (`sigma_duality_targets.md`) — NOT the survey — until genuinely proved.
