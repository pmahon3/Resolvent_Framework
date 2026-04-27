# Paper IIIa Skeleton — General Observational Certification

**Status:** Programme note, post-arXiv priority.
**Date:** 2026-04-27

---

## The question

Papers I and II work at the level of the general query system. Paper III (IIIb)
certifies reconstruction from finite data but only in the dynamical/time-series
specialisation. IIIa asks the prior question:

> What can finite query responses certify about observational resolution and
> admissibility — before assuming temporal or geometric structure?

---

## Central quantity: the population separation defect

Fix a query system with observable σ-algebra σ(𝒞) on the realization space Ω.
For a finite joined query algebra 𝒢 = ℰ_{n_1} ∨ ··· ∨ ℰ_{n_k}, define:

  δ(𝒢) := sup_{A ∈ σ(𝒞)} inf_{E ∈ 𝒢} μ(A △ E)

This is the separation defect of the queried family 𝒢 relative to the full
observable structure. It measures unresolved distinguishability: how much of
σ(𝒞) is still invisible to the finite queried subfamily.

Key properties:
- **Monotonicity:** 𝒢 ⊆ 𝒢' implies δ(𝒢') ≤ δ(𝒢)
- **Vanishing:** δ(𝒢) = 0 iff σ(𝒢) = σ(𝒞) mod μ (complete resolution)
- **Target:** 𝒢 must be measured relative to σ(𝒞) explicitly — in the
  non-temporal setting, the analogue of "full Borel structure" is otherwise easy
  to blur. Use Paper I notation throughout.

Note: "lag" in IIIb is replaced here by **query refinement depth** — the join
ℰ_{n_1} ∨ ··· ∨ ℰ_{n_k} plays the structural role of "more information" without
smuggling in time. The defect is non-temporal and purely algebraic/measure-theoretic.

---

## Empirical proxy

Given N sampled joint query responses at levels (n_1,...,n_k), the empirical
analogue is the collision probability of the joint response vector:

  δ̂(𝒢, N) = probability that two independent sampled responses agree on all of 𝒢

This is estimable as a U-statistic with no geometric structure. The induced
empirical atoms of the joined finite query family are the natural discrete objects.

---

## Three regularity layers — the complete architecture

IIIa has three independent regularity conditions, each controlling a distinct
failure mode. This separation is architecturally essential.

| Layer | Condition | Controls | Failure mode if absent |
|---|---|---|---|
| Population | CE | No purely finitely additive escape | Irreducible floor in δ(𝒢_k) |
| Refinement | Honest refinement | Query family genuinely approaches σ(𝒞) | Spurious stalling from bad design |
| Sampling | IID / controlled dependence | δ̂ estimates δ | Estimation bias / non-concentration |

**Definition (honest refinement).** A sequence (𝒢_k) of finite joined query
algebras is *honest* if:
- 𝒢_k ⊆ 𝒢_{k+1} (increasing), and
- σ(⋃_k 𝒢_k) = σ(𝒞) mod μ (exhaustive).

This is phrased in Paper I language: exhaustion of the directed query system,
not an ad hoc statistical condition.

**Why this matters.** Without honest refinement, a persistent empirical floor
could be a design artifact — the experimenter kept adding queries that never
cut the unresolved atoms. With it, the CE-shadow corollary becomes robust:
given that the refinement genuinely exhausts the observable system, stalling
is a population-level admissibility failure, not a choice-of-queries failure.

**Population theorem (clean statement):**
Under CE and honest refinement, δ(𝒢_k) → 0.

**CE-shadow corollary (clean statement):**
Under honest refinement and IID sampling, if δ̂(𝒢_k, N) exhibits a persistent
floor as k → ∞ and N → ∞, that is evidence against CE.

The three layers are independent: CE can fail with honest refinement and good
sampling (population obstruction); refinement can be dishonest with CE holding
and good sampling (design obstruction); sampling can be irregular with CE and
honest refinement both holding (estimation obstruction). Each failure mode has
a name and a corresponding diagnostic.

---

## Four-layer architecture

### Layer 1 — Population separation defect
Define δ(𝒢), establish monotonicity under refinement, characterise δ = 0 as
complete resolution, and connect refinement depth to σ(𝒞).

### Layer 2 — Empirical proxy
Define the empirical collision/separation statistic from sampled joint responses.
Phrase via induced empirical atoms of 𝒢, or as a U-statistic.

### Layer 3 — Estimation theorem
Under IID sampling from the observable law of the joined query responses, show
δ̂(𝒢, N) → δ(𝒢) in probability. This is where concentration lives. Note: this
requires sampling regularity (IID or exchangeability / dependence control), NOT
CE alone.

### Layer 4 — CE-shadow corollary (the philosophically original result)
If refinement deepens but δ̂(𝒢_k, N) fails to decrease past a persistent floor,
this is evidence against CE / against complete observational admissibility.

Formally: CE is what guarantees the population floor can be discharged by query
refinement. A persistent floor — both at the population level (δ(𝒢_k) → c > 0)
and empirically (δ̂ stalling) — is a signature of CE-failure.

This is **one-directional**: persistent floor → evidence against CE. The converse
(δ → 0 → CE) is not claimed; see logical status note below.

This turns CE from an abstract foundational boundary (Paper I) into something
with a finite empirical shadow — the core conceptual payoff of IIIa.

---

## The two-role separation for CE (important)

CE should NOT carry the whole burden. Separate two distinct roles:

**CE as population regularity:**
CE ensures that query refinement can in principle drive δ(𝒢) → 0 rather than
leaving an irreducible floor from purely finitely additive escape. CE is a
condition on the population target, not on the estimator.

**Sampling regularity as concentration regularity:**
Concentration of δ̂ around δ requires ordinary probabilistic assumptions on the
sampled query responses (IID or controlled dependence). This is independent of CE.

This separation makes IIIa both truer and architecturally cleaner.

---

## What IIIa would and would not claim

**Would claim:**
- Consistency: δ̂(𝒢, N) → δ(𝒢) as N → ∞
- Monotonicity under refinement (population and empirical)
- Detection: persistent empirical floor under refinement → evidence against CE
- An abstract elbow criterion (stop refining when defect stops decreasing)

**Would not claim:**
- Minimax rates (need geometry)
- Sharp elbow theorems (need mixing)
- Optimal lag selection (no lag in the abstract setting)

---

## What replaces mixing

Mixing in IIIb controls how fast δ(L) → 0 under lag growth, enabling rate
theorems. In IIIa, the rate of δ(𝒢) → 0 under refinement depends on the
discriminability geometry of the query system — how fast the induced equivalence
classes shrink. This is a property of the query system, not the data. IIIa
therefore gives consistency results, not rate results. That is the right tradeoff.

---

## Relation to existing papers

- **Paper I:** CE is the exact admissibility condition. IIIa makes CE empirically
  detectable — gives CE an observational shadow.
- **Paper II:** The kernel Q*(ω) = Π_Q(Q(ω),·) is the general object; IIIa
  certifies properties of it at the level of its full generality, before temporal
  specialisation.
- **Paper IIIb (current Paper III):** IIIa is the general layer; IIIb is the
  dynamical specialisation with rates. IIIb's elbow rule is the mixing-sharpened
  version of IIIa's abstract elbow criterion.

---

## Logical status of the CE-shadow theorem (settled 2026-04-27)

The CE-shadow theorem is **one-directional**. The correct logical picture:

**Forward (CE → population regularity):**
CE rules out purely finitely additive escape, so query refinement exhausting the
system can drive δ(𝒢_k) → 0. CE is the population regularity that makes
resolution-completeness achievable.

**Backward (δ → 0 ↛ CE) — likely false in general:**
δ(𝒢_k) is defined inside σ(𝒞). CE is about whether mass has escaped to the
Stone boundary — non-principal ultrafilters that lie outside the realized
measurable horizon. A charge family could separate all points of σ(𝒞) (so
δ → 0) while still failing CE by placing mass on non-principal ultrafilters
that do not manifest as a deficit in the defect functional.

Slogan: δ sees resolution inside σ(𝒞); CE also controls escape to the
non-principal boundary. Those are related but not the same test.

**CE-shadow corollary (what is robust):**
A persistent empirical floor under refinement is evidence against CE — because
CE is what guarantees the floor can be discharged by adding more distinctions.
δ̂ stalling is a genuine finite-sample signature of CE-failure.

**The backward direction might be recoverable under:**
- A support/completeness assumption: all mass-bearing components visible inside σ(𝒞)
- A stronger realizability assumption: the observable σ-algebra is support-determining
- A tightness hypothesis at the target level (but this risks assuming CE back in)

These are stronger than the natural IIIa level. Leave as open technical question,
not a claim.

**Paper framing:** the empirical defect gives a finite observational shadow of CE,
not a complete characterisation. That is already enough to justify IIIa —
CE acquires an observable signature (persistent refinement floors) that it
does not have in the abstract Paper I treatment.

---

## Priority

Post-arXiv. Do not attempt before Papers I–III are submitted.
The right moment is after the dynamical paper is out and the general programme
is publicly visible.
