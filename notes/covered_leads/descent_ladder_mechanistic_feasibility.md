# Descent Ladder for Mechanistic-Feasibility Inference

*Type 6 (exposition/translation) audit — 2026-06-08. Hostile referee,
web-search-verified.*

**Claimed type(s):** Type 6 (exposition/translation) primarily; Type 4
(vocabulary) secondarily.
**Bar (Type 6):** named audience + genuinely inaccessible literature +
non-trivial translation work (not afternoon's relabeling).
**Bar (Type 4):** three-statements test — ≥3 statements unstateable
without the ladder + ≥1 non-trivial result.

## The candidate

A "descent ladder" claimed to unify four otherwise-disjoint literatures
answering "can data determine the feasibility of a mechanistic
hypothesis?":

- **R1** (do local charges cohere into a global law?): marginal /
  compatibility problem — Kolmogorov extension, Kellerer (1984),
  Vorob'ev (1962).
- **R2** (is the global law in the shadow of the mechanism class,
  Obs⁻¹(ℓ) ≠ ∅?): partial / set identification — Manski, Tamer,
  Molchanov–Molinari random sets, Molinari (Handbook of Econometrics
  Vol 7A, 2019).
- **R3** (does a mechanism reproduce the conditional structure?):
  conditional-moment / specification testing — Bierens (1990),
  Markov-order tests, GMM over-ID / Hansen J.
- **R4** (deterministic special case xₜ₊₁=F(xₜ)): Takens reconstruction
  + statistical theory — Takens (1981), Sauer–Yorke–Casdagli (1991),
  Botvinick-Greenhouse (JSP 2025), Rhodes–Morari (1997).
- Negative rung: Shah–Peters (2020) — no model-free CI/feasibility test
  is both valid and consistent against all alternatives.

The Stone-space / σ-additivity / "collective exhaustion" layer is the
R1→R2 transition (finitely-additive measure on a Stone space →
σ-additive realised probability on Ω).

## Verdict: FAIL (Type 6 and Type 4)

Primary kill: **bar 2 (inaccessible literature)** — every rung is either
handbook material for its field or already published in the target
audience's own venue. Reinforced by **bar 1 (no concrete audience)**,
**bar 3 (relabeling, no method transfer)**, the three-statements test,
and the σ-additivity layer being **decorative** for feasibility.

### The claim is inflated: three of the four rungs are ONE field

R1, R2, R3 are all econometrics/statistics, and the rung-to-rung
bridges are already published *in a single handbook chapter*:

- **R1↔R2 is published.** Molinari (Handbook of Econometrics Vol 7A,
  2019; arXiv:2004.11751) builds the identified set on **Artstein's
  theorem** (1983): a selection of the random set Obs exists iff
  P(y∈K) ≤ P(Obs∩K≠∅) for all compact K. "Selectionability =
  observational equivalence" *is* a marginal-compatibility statement;
  the chapter explicitly discusses the classical marginal problem and
  Kolmogorov extension. The "identified set = Obs⁻¹(ℓ)" identification
  the seed offers is the opening move of that chapter.
- **R2↔R3 is textbook.** The Hansen J / over-identification statistic
  "can be viewed as a model specification test" (standard GMM
  pedagogy, Hayashi; Hansen 1982). Set identification and over-ID
  specification testing are adjacent tools in the same field.

So the honest claim is not "four disjoint literatures." It is
"econometric feasibility inference (R1–R3, one handbook) ∪ Takens
reconstruction (R4)." Only the **R2/R3 ↔ R4** link is genuinely
cross-field.

### "No one has stacked these four" — narrowly TRUE for R2↔R4, but the
### gap fails the bar anyway

Aggressive search found **no** single treatment unifying econometric
set-identification with deterministic Takens reconstruction. That one
cross-field pairing is unstacked. **But a literature gap is not a Type 6
pass.** The gap fails every prong of the bar:

- **Bar 1 (audience) — no concrete population reads both.** The two
  candidate audiences each fail: (a) **econometricians** — R1–R3 are
  their own handbook (Molinari Vol 7A), R4 is not their problem; (b)
  **dynamicists** — R4 is their own venue, and the econometric rungs
  are foreign but *they don't need them*: the feasibility question on
  the dynamics side is already answered natively by **observability /
  functional observability** (arXiv:2301.04108, already in the
  knowledge map) and by the measure-theoretic delay-embedding
  identifiability result ("invariant measure in delay coordinates
  identifies dynamics up to topological conjugacy," Botvinick-Greenhouse
  JSP 2025). The gap is unstacked because **nobody needs it stacked**,
  not because stacking is hard.
- **Bar 2 (inaccessible literature) — nothing is inaccessible.** R1–R3
  is a handbook chapter; R4 is *already published in the audience's own
  venue* (Botvinick-Greenhouse, J. Stat. Phys. 2025) — the identical
  ground on which this programme already parked the
  `relational_reconstruction_separation` Type 6 seed (2026-06-06). Same
  R4 citation, same kill.
- **Bar 3 (non-trivial translation) — relabeling.** See (b) below.

### (b) Organizational only — NO method transfers between rungs

The ladder transfers no technique. The random-set / Artstein capacity-
functional machinery (R2) does nothing for the Takens side; the
delay-embedding genericity / observability theory (R4) does nothing for
set identification. There is no cross-rung method a practitioner would
newly perform because of the ladder. It is organizational, and the
organization just chains bridges that are individually standard
(Artstein for R1↔R2, Hansen J for R2↔R3). Organizational-only with no
non-obvious transfer ⇒ bar 3 fails.

### (c) The Stone / σ-additivity layer is DECORATIVE for feasibility

By the programme's **own Paper I companion note** (CE non-derivability:
`notes/unsorted/foundations/ce_nonderivability/index.md`, Part I),
σ-additivity is **not first-order axiomatizable** — invisible to any
finite test. The R1→R2 obstruction ("concentration on principal
ultrafilters" vs σ-additive collective exhaustion) therefore *cannot*
change any finite-data feasibility procedure. A working
econometrician's set-identification analysis is never altered by knowing
the obstruction lives at βℕ∖ℕ. Load-bearing for Paper I's foundational
point; decorative for the feasibility question.

### Three-statements test (Type 4) — every statement reduces

Each statement the ladder enables is an existing statement in one of the
four literatures:

1. "Local charges cohere into a global law" = Artstein /
   selectionability holds (Molinari Vol 7A).
2. "The global law is in the shadow of the mechanism class,
   Obs⁻¹(ℓ) ≠ ∅" = the identified set is nonempty (Molinari).
3. "A mechanism reproduces the conditional structure" = the
   over-identifying / conditional-moment restriction holds (Hansen J;
   Bierens 1990).
4. (Dynamics) "The mechanism is recoverable from the series" =
   functional observability / faithful generating partition
   (arXiv:2301.04108; Krieger; Botvinick-Greenhouse 2025).

No statement is unstateable without the ladder, and no non-trivial
result is provable in ladder vocabulary that isn't already a result in
one of the four fields. Three-statements test **fails**.

## Minimal honest survivor — and why even it fails

The one identification not pre-stacked is **"Obs⁻¹(ℓ) is the
reconstruction-feasibility set"** (the econometric identified set =
the dynamics feasibility set). It fails because it is trivial-once-
stated to anyone who knows both objects, and the population who knows
*both* Molinari's random-set partial identification *and* Takens
reconstruction *for a feasibility question* is not concretely nameable.
Obvious-once-stated + empty audience ⇒ bars 1 and 3 fail. Nothing
survives as a Type 6 contribution.

## The recurrence pattern (the real lesson of this park)

This is the **fourth** time the "reconnect the foundational programme to
empirical science via dynamics/reconstruction" arc has died, and three of
the four died on or near the *same rock* — reconstruction feasibility is
already answered in the audience's own venue:

1. **Paper III** — withdrawn 2026-05-13 (rediscovery: Billings–Voon 1986,
   Rhodes–Morari 1997, Lepski 1991).
2. **distributed_sensor_contextuality** — parked 2026-06-06 (the
   construction *is* the definition of contextuality; Boolean→OML transfer
   published).
3. **relational_reconstruction_separation** — parked 2026-06-06
   (Botvinick-Greenhouse JSP 2025; Krieger in delay-map language).
4. **this seed** — parked 2026-06-08 (same R4 venue, same kill).

The seed was *presented* as "the most natural way the programme reconnects
to empirical science." That is precisely the diagnosis: the reconnection is
natural *because* the descent ladder is general enough to host any inverse
problem, and that generality is what makes it occupied at every rung. The
recurrence is a signal, not a coincidence to extend — the empirical-science
bridge is canned ground.

**What it never touched:** the then-live frontier — OML *descent
inhabitation* (does σ-orthocompleteness survive Navara's product/constancy
machinery over concrete stateful MO₂ blocks?), since itself closed/parked
2026-06-10 — has nothing
non-distributive in it. Mechanistic feasibility lives entirely in the
Boolean/realised half of the programme, where everything is classical and
occupied. The frontier is on the non-distributive descent axis; this seed
sat orthogonal to it.

## Cross-references

- Analogous prior parked Type 6, same R4 venue:
  `notes/covered_leads/relational_reconstruction_separation.md`
  (Botvinick-Greenhouse JSP 2025 in audience's own venue; "Krieger in
  delay-map language").
- Other deaths in the same empirical-reconnection arc:
  `notes/covered_leads/distributed_sensor_contextuality.md`;
  `papers/archive/paper_iii_withdrawn/` (and `paper_iii_canned/`).
- σ-additivity invisible to finite tests (the (c) kill):
  `notes/unsorted/foundations/ce_nonderivability/index.md` Part I;
  `papers/archive/countable_additivity_retired/countable_additivity_not_first_order.tex`.
- Shah–Peters impossibility, already engaged:
  `notes/covered_leads/residual_structure_inference.md`.
- Manski / partial-identification already engaged:
  `notes/unsorted/disintegration_diagnostic.md` (Phase 2 audit table).

## Key references found in audit

- Molinari, "Microeconometrics with Partial Identification," Handbook of
  Econometrics Vol 7A (2019); arXiv:2004.11751.
- Molchanov & Molinari, *Random Sets in Econometrics*, Cambridge (2018).
- Artstein (1983) — capacity-functional / selectionability theorem.
- Hansen (1982) — GMM, over-ID = specification test.
- Botvinick-Greenhouse et al., "Measure-Theoretic Time-Delay Embedding,"
  J. Stat. Phys. 192:171 (2025); arXiv:2409.08768.
- "Functional observability and subspace reconstruction in nonlinear
  systems," arXiv:2301.04108.
- Shah & Peters, "The hardness of conditional independence testing,"
  Ann. Statist. (2020).
