# Distributed-Sensor Contextuality: When Embedding Contexts Refuse to Glue

*Seed — 2026-06-06. Carved off from the parked reconstruction seed
(`notes/covered_leads/relational_reconstruction_separation.md`), which
named this branch as a live escape hatch but explicitly did not pursue it.*

**Claimed type(s):** Type 1 (new theorem) *if* a genuinely non-co-realizable
multi-sensor construction can be built; Type 3 (unifying framework) as the
fallback if the construction is classical but the *transfer* (Paper II
forcing → reconstruction) is the contribution. **Bar:**
- *Type 1* — exhibit a concrete family of time-series observers (sensors)
  whose context lattice is **provably non-distributive** (contains MO₂ or a
  pentagon as a sub-orthoposet), where the obstruction is **not removable by
  a common joining**. Must survive the [[oml_singular_extension_resolved]]-style
  stress test: is the non-distributivity load-bearing or imported? Is it
  visible in a finite concrete sublogic, or does it need an L(H)-type
  non-concreteness?
- *Type 3* — if the sensors are individually classical but the *family*
  forces an OML via Paper II §7, the transfer must be **demonstrated, not
  analogized**: a reconstruction/prediction statement provable via the OML
  dual (McDonald–Bimbó, Gleason descent) that is **false or unstateable** on
  any single classical joining of the sensors.

**Not claimed (yet):** Type 6/4. The parked reconstruction seed already
failed those bars for the single-series case; this seed must clear a
*structural* bar (OML genuinely forced), not an expository one.

## What distinguishes this from already-covered ground

This branch must clear **two** prior closures, or it is dead on arrival:

1. **Single-series delay nesting is closed.** `𝒪_1 ⊆ 𝒪_2 ⊆ ⋯` are nested
   sub-σ-algebras of one measure algebra → directed → Boolean colimit →
   contextuality decorative. *This seed must NOT be a single series.* The
   contexts must come from observers that **cannot share one measure
   algebra**.

2. **Rival realizations of one series co-realize (closed 2026-06-06).** The
   skew-product witnesses *underdetermination*, not contextuality: rival
   hidden-fibre realizations M₁, M₂ both have the observable factor 𝒪 as a
   common factor, so the **relatively independent joining over 𝒪**
   (Furstenberg) is a single classical p.m.p. system having both as factors.
   Any finite family of rival realizations of one series co-realizes on one
   classical space → Boolean. A mixture of Boolean algebras is Boolean.
   *This seed must NOT be rival realizations of one series.*

**The standing obstruction this seed must defeat (Kolmogorov).** Any finite
family of classical real-valued observables on a common probability space
**jointly distributes** — there is always a joint law, hence a Boolean
algebra they all sit inside. So "two sensors watching the same scene" is
Boolean *as long as a joint distribution exists*. The construction only
produces an OML if the sensors are **non-co-realizable**: there is provably
**no** probability space carrying all of them simultaneously. That is the
whole technical content. Candidate mechanisms:
- **No common dynamical clock / no joint stationary law** — sensors on
  different, non-synchronizable time bases, where no shift-invariant joint
  measure exists (the joining over a common factor *fails to exist* because
  there is no common factor).
- **Operationally exclusive measurement settings** — sensor configurations
  that physically cannot be co-deployed (a genuine measurement-incompatibility,
  not mere unobserved-fibre ignorance), so no joint experiment realizes both.
- **Rival dynamical hypotheses promoted to settings** — but ONLY if they are
  non-co-realizable as joint experiments; if they admit a joining over a
  common factor, this collapses to closure (2) above.

## The question

Paper II §3 already names "distributed systems" as a source of incompatible
observations, and §7 proves: distributivity ⟺ VDR/EA commensurability;
non-distributive (OML) ⟹ VDR blocked, PR/EA survive via Gleason. **But Paper
II never builds a distributed-sensor example.** The question:

> Is there a concrete distributed time-series measurement setup whose context
> lattice is genuinely non-distributive (no common joining), so that the
> Paper II forcing fires for a *reconstruction* problem — and does the OML
> dual then deliver a predictive/reconstruction statement that no single
> classical joining of the sensors can?

If yes: the embedding/reconstruction question acquires a genuine
contextuality, the OML machinery is load-bearing (not decorative), and the
parked single-series result is recontextualized as the *Boolean corner* of a
properly contextual problem.

## Why this is worth a seed (not just a note)

- It is the **only** version of "contextuality + embedding" that survived
  the two closures. The reconstruction seed named it and walked away; nobody
  has checked whether it is inhabited.
- It connects directly to the **live OML work** — if a distributed-sensor
  OML is concrete and stateful, it is a candidate **inhabitant** for the
  descent axis ([[oml_descent_inhabitation]]): a concrete OML with states
  where σ-additive descent can be tested, arising from a *dynamical* source
  rather than Navara's imported finite block. This could feed the one unrun
  check from the other direction.
- Paper II's "distributed systems" motivation (§3) is currently a **promissory
  note**. Either this seed cashes it (a real example) or it confirms the note
  cannot be cashed for time series (also informative — sharpens Paper II's
  scope).

## Open / next (Phase 4 — user's call, then Phase 2 gate)

1. **Build the smallest non-co-realizable pair** ([[feedback_verify_by_building]]).
   Two sensors, smallest setup, where you can *prove* no joint probability
   space exists. Likeliest engine: no common stationary joint law / no
   joining over a common factor (because there is no common factor). If you
   cannot build even a 2-sensor non-co-realizable example, the branch is
   empty — park it honestly, and Paper II §3's "distributed systems" claim
   gets a scope caveat.
2. **Check the lattice is genuinely non-distributive.** A finite sub-orthoposet
   = MO₂ or pentagon, with the non-distributivity load-bearing (not imported,
   not an artifact of coarsening). Cross-check against the extension-axis
   lesson: is the obstruction elementary/concrete, or does it need an
   L(H)-style non-concreteness ([[oml_singular_extension_resolved]])?
3. **Demonstrate the transfer (Type 3 fallback).** A reconstruction/prediction
   statement provable via the OML dual that is false/unstateable on every
   single classical joining. Without this, even a genuine OML is "an OML
   exists here," not a contribution.
4. **Then `/audit full`** (Phase 2). The audit's job: does a *new theorem*
   (genuine non-co-realizable construction) or *genuine transfer* clear, or
   does it collapse into (a) "contextuality exists, known since Kochen–Specker,"
   (b) Paper II's already-stated §3 motivation re-dressed, or (c) a
   no-joint-law fact already standard in stochastic-process theory?

## Phase 2 audit verdict — PARK (2026-06-06)

`/audit full` + inhabitation survey (opus, web search). **Pure: KNOWN.
Type 1: FAIL. Type 3: FAIL.** A double-kill: inhabitation and emptiness
close it from opposite sides, meeting at the seed's own load-bearing/imported
test.

**Emptiness kills Type 1.** The seed's "standing obstruction" (Kolmogorov:
classical observables on a common space always jointly distribute) is not a
hurdle the construction defeats — it is a **theorem (Fine 1982, PRL 48, 291)**
guaranteeing the construction is *empty* for genuinely classical time-series
sensors. "All observables on a classical state space are compatible"
(arXiv:2106.03588). To get an OML you must **impose** incompatibility
operationally — at which point the OML is **imported** (the same mechanism as
Navara's finite block, [[oml_descent_inhabitation]]), not load-bearing. The
one slot that would have been new — non-co-measurability *intrinsic to the
dynamics* of a single classical system — is exactly what Kolmogorov/Fine rule
out. No search under any name surfaced it.

**Inhabitation kills Type 3.** Every level the seed claims is already built:
- *"Non-co-realizable family → no global joint" IS the definition of
  contextuality*, not an obstruction: Abramsky–Brandenburger (NJP 13, 113036,
  2011; arXiv:1102.0264) — local sections that don't glue to a global section.
- *The Kolmogorov obstruction is Fine's theorem* (joint distribution ⟺
  factorizability). *The "stochastically unrelated cross-context variables"*
  is Dzhafarov–Kujala Contextuality-by-Default (arXiv:1511.03516) — and there
  the non-co-measurability is **imposed**, never derived from one process.
- *The Boolean-contexts→OML transfer engine is PUBLISHED* (2026):
  "Contextuality as a Left Adjoint" (arXiv:2603.22353) proves gluing Boolean
  algebras by identifying only {0,1} via pushout generates orthomodular
  (generically non-distributive) lattices, as a left adjoint, with
  *"failure to remain Boolean ⟺ absence of global sections in
  Abramsky–Brandenburger."* This **is** Paper II §7's
  distributivity⟺commensurability as a general theorem — the seed's claimed
  transfer, already built.
- *The title and one engine are taken*: "Contextuality in distributed
  systems" (arXiv:2210.09476) — the "no common clock" engine, again from
  *imposed* no-global-clock structure, not intrinsic dynamics.
- *Foulis–Randall test-space empirical logic* (1970s) already gives the
  OML of distributed operational tests.

This matched the seed's pre-registered kill (lines 14–17: load-bearing or
imported?). The descent-axis cross-payoff does **not** rescue it — any OML
built here is the imported-block kind, so it gives no new evidence on
"richness starves concreteness."

**Cashable fallback (do this).** Paper II §3's "distributed systems"
motivation is a promissory note that **cannot be cashed as an intrinsic
time-series example**. Add a one-line scope caveat to §3: distributed-systems
contextuality requires *operationally imposed* incompatible contexts (CbD /
no-global-clock structure), not incompatibility intrinsic to a single
dynamical system, which Kolmogorov precludes. This sharpens §3 honestly — the
seed itself (lines 96–98) flagged this as the informative-failure outcome.

Filed: `notes/covered_leads/`.

## Cross-references
- Parent (parked) seed, escape hatch named: `notes/covered_leads/relational_reconstruction_separation.md` ("What this is NOT," contexts that cannot share one measure algebra).
- Closure of the rival-realizations sibling (joining over common factor): same file, Phase-2 audit verdict (2026-06-06).
- Paper II forcing (compatible→Boolean, incompatible→OML; §3 names distributed systems; §7 distributivity⟺commensurability): `papers/paper_ii/outline.md`, `papers/paper_ii/distributivity_and_realism_body.tex`.
- Descent-axis inhabitant connection: [[oml_descent_inhabitation]], `notes/open_questions/verification/inhabitation_check.md`.
- Method discipline (build the smallest concrete example, don't analogize): [[feedback_verify_by_building]]; the "Stone/Takens = rhyme" burn (`0ff3387`) is the standing warning against framing-analogies in this exact corner.
