# Subsession brief — is σ-essential contextuality non-empty? (via CE)

*Targeted subsession brief, 2026-06-11. Self-contained: a fresh agent/session
should be able to attack this from the brief alone. This is the FIRST CUT on
investigation 1 (the OML descent prize), chosen because it is cheap, routes both
exits, and leverages machinery the programme already owns (CE / Paper I).*

## The one question

> **Can "σ-essential contextuality" occur at all?** I.e. does there exist (or can
> CE-type machinery forbid) a σ-complete concrete OML `L` and a σ-additive state
> `w` on it such that:
> - **every finite sub-OML of `L` is non-contextual** (its restriction of `w` is
>   spanned by dispersion-free states / has a global hidden joint), BUT
> - **`L` as a whole is contextual under `w`** (`w` is not in the closed convex
>   hull of `L`'s dispersion-free states / has no global σ-additive joint)?
>
> YES (it can occur) → investigation-1 Exit A has a target shape (build it).
> NO (CE-type compactness forbids it) → Exit B is half-proven (impossibility),
> and the empiricist-underdetermination meta-theorem becomes a theorem.

This is a non-emptiness check on a CONCEPT, prior to construction-vs-refutation.
Do not try to build a witness or prove the full theorem; just determine which way
the CE machinery points.

## Why CE is the right lever (the Boolean precedent)

CE (collective exhaustion, Paper I) is *exactly this phenomenon in the Boolean
case*. Two routes, both relevant:

- **Carathéodory route:** finite consistency does NOT force σ-additivity; CE is an
  irreducible extra commitment "about the infinite." CE is **not derivable from
  any structural/finite condition** (proved via Łoś + finite-cofinite
  counterexample). So in the Boolean world, the gap between "all finite pieces
  cohere" and "the σ-additive whole coheres" is REAL and non-trivial.
- **Stone route (the load-bearing one here):** finite additivity on the cylinder
  algebra + compactness of the Stone space yields σ-additivity, and **CE reappears
  as a SUPPORT condition — the σ-additive measure concentrates on the PRINCIPAL
  ultrafilters** (the image of the sample space), not the free ones. Free
  ultrafilters carry the finitely-additive-only / diffuse mass.

**This is precisely the ∏ₙMO₂ result one level up.** For ∏ₙMO₂ we found:
contextual states exist only finitely-additively (diffuse states on the central
`P(ℕ)`, i.e. *free* ultrafilters); σ-additivity forces concentration on points
(principal ultrafilters) and kills contextuality. That IS the Stone/CE mechanism.
So the Boolean precedent says: **σ-additivity = concentration on principal points
= non-contextual.** If that transfers to the non-distributive case unconditionally,
σ-essential contextuality is EMPTY and Exit B wins.

## The actual question the subsession must answer

**Does the CE/Stone "σ-additive ⟹ concentration on principal points ⟹
non-contextual" implication transfer from the Boolean case to the non-distributive
(OML) case — or does non-distributivity open a gap CE cannot close?**

Three sub-questions, in order:

1. **The center.** ∏ₙMO₂'s contextuality-killing went through its Boolean *center*
   (`P(ℕ)`), where the pure CE/Stone argument applies. **Does a general concrete
   σ-complete OML's contextuality also localize to its center / to Boolean
   sub-structure** — in which case CE kills it and Exit B wins — **or can
   non-distributive (non-central) structure carry σ-essential contextuality that
   the center misses?** This is the crux. The MO₂ gap (meet-zero ≠ orthogonal)
   lives off-center; does it survive σ-additivity where the center's diffuse states
   do not?
2. **The non-derivability transfer.** CE's non-derivability (Łoś + finite-cofinite)
   is a Boolean/first-order result. Does the *analogous* non-derivability hold for
   contextuality on OMLs — "σ-essential contextuality is not forced by any finite
   condition" — which would make Exit A's witness consistent-but-not-constructible-
   from-finite-data (a CE-flavored existence)? Or does the OML setting actually
   *force* finite witnessing (every contextual σ-additive state already contextual
   on a finite sublogic), which is Exit B?
3. **Wright in the limit.** Wright's pentagon is finite-contextual. Can one take a
   σ-orthocomplete *colimit / countable paste* of Wright-type blocks whose finite
   sublogics stay non-contextual but whose σ-join forces contextuality? (This is the
   Exit-A construction shape — but the subsession only needs to judge whether CE
   *permits* it, not build it.)

## What to deliver

A routing verdict: **EMPTY** (CE-type compactness forbids σ-essential
contextuality — Exit B / impossibility, with the argument sketch), **NON-EMPTY**
(it can occur — Exit A, with the witness shape CE permits), or **GAP** (CE does not
settle it; identify exactly the non-distributive step where the Boolean argument
breaks, which becomes the next subsession). Be explicit about which, with the
center-localization question (sub-question 1) as the load-bearing pivot.

## Sources (self-contained starting set)
- CE statement + both routes + non-derivability: `programme/program_overview.md`
  §"Paper I", routes 1–2 and the CE metatheorem.
- The reduction this serves: `reading1_prize_reduction.md` (relational ⟺
  contextual; σ load-bearing; the ∏ₙMO₂ center/diffuse computation; Wright bound).
- The committed problem statement: `oml_onboarding.{md,tex}` §5 (the σ-essential
  contextual-state prize; the three point-spaces — P(A) vs dispersion-free states
  vs (A)-rays — kept distinct).
- CE Lean (if formal grounding needed): `StoneDualityExtension.lean`,
  `DiscriminabilityFoundations.lean`.
- Prior contextuality contact (note the distinction):
  `covered_leads/distributed_sensor_contextuality.md` killed *dynamics-intrinsic*
  contextuality (Kolmogorov/Fine) — a DIFFERENT claim from σ-essential
  contextuality on a static OML; do not conflate.

## Discipline
- This is a non-emptiness/routing judgment, NOT a construction or a full proof.
- The center-localization pivot (sub-question 1) is where the real content is —
  spend the budget there.
- Verify the Boolean→OML transfer claim against the actual CE argument; do not
  assume it transfers (the whole novelty would be if it DOESN'T).
