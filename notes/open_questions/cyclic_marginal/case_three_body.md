# Case study 3: the three-body problem (2026-10-19)

reviewed: false. This is a CASE, not a generalisation (memory: feedback_reflective_equilibrium). It
is a companion to cases 1 (three species) and 2 (delay windows). No computation was run.
- **cited:** checked at abstract or lecture-note level.
- **memory:** from memory, not yet checked.
- **hand:** my reading, unverified.

## Background facts

- **Chazy (1922)** classified the final motions of the three-body problem: hyperbolic, parabolic,
  bounded and oscillatory. In oscillatory motion a body swings out ever further but keeps
  returning. Chazy had no examples of it. **cited**
- **Existence of oscillatory motions.** Sitnikov (1960s) proved it in a symmetric restricted model,
  and Moser gave a new proof. Alekseev extended it to the full, unrestricted problem. Llibre–Simó
  (1980) and Guardia–Martín–Seara treated the planar restricted problem. **cited**
- **Rarity is open.** The conjecture that oscillatory motions have Lebesgue measure zero
  (Kolmogorov, stated by Alekseev) is a long-standing open question. Gorodetski–Kaloshin show that
  they often have *maximal Hausdorff dimension*. That is compatible with measure zero. **cited**
- **Typical fate (full problem, negative energy).** One body escapes and a binary remains.
  Stable bounded motions also exist: hierarchical triples (KAM) and the figure-eight orbit
  (Chenciner–Montgomery, 2000). **memory**

## 3a. External pair stations

- **Queries.** Each body gets b_k = "is body k in the currently closest pair?". Station (i, j)
  watches (b_i, b_j). That is a triangle of separate-variable windows, the shape that twisted in
  case 1.
- **Case 1's mechanism needs two things:**
  - (i) separated observers ✓;
  - (ii) long-run frequencies that never settle, with each station averaging over its own epoch.
- **Reading.** ⟦hand⟧ Escapes settle ("which pair is closest" freezes), and so do quasi-periodic
  bounded motions. Non-settling statistics would come from oscillatory motions, and perhaps from
  bounded chaotic ones; that second possibility is unchecked.
- **Prediction.** Pairwise stations can describe no world only along non-settling motions.
  **Whether that happens with positive probability is tied to the open Kolmogorov question.**

## 3b. The isolated relational universe

- **Setting.** Three bodies and nothing else. With no outside observer, the meaningful quantities
  are relational: the mutual distances r₁₂, r₂₃, r₃₁, i.e. the shape of the triangle they form.
  Barbour et al. use the N-body problem as a toy cosmology in exactly this way ("shape dynamics";
  Barbour, Koslowski and Mercati, PRL 2014, gravitational arrow of time). **memory**
- **Perspectives.** Each body knows its own relations: body 1 sees (r₁₂, r₁₃), body 2 sees
  (r₁₂, r₂₃), body 3 sees (r₁₃, r₂₃). Neighbouring perspectives share one relation. **The bodies'
  own viewpoints form the triangle of queries.** This is the most natural form of the triangle met
  so far. ⟦hand⟧
- **The catch.** In Newtonian mechanics the three perspectives share one history and one absolute
  time. Averaged together they always describe a world. For them to come apart as case 1's
  stations did, each body would need its own clock or epoch. That points toward proper time
  (relativity) or relational notions of time (Barbour). **Open pointer, speculation.**

## Open: different results beyond Newtonian physics ⟦speculation, not a result⟧

Case 3's "no pointlessness" verdict rests on Newtonian absolute time: one shared history, one
shared way of averaging. Other physics may change it.
- **Relativity.** There is no absolute simultaneity, and each body has its own proper time.
  Spacelike-separated observers have no privileged common epoch over which to average. That is a
  natural, physical source of the "observers who cannot combine their averaging" that case 1
  needed. Open question: can the long-run relational statistics of a relativistic few-body system,
  each averaged along a body's own proper time, agree on overlaps yet admit no joint description?
- **Relational time (Barbour, shape dynamics).** Time is read off from change within the system.
  Different "clocks" built from different relations could play the role of the separate epochs.
- **Quantum mechanics.** Here joint questions are unaskable *in principle*, not just in practice.
  Specker's three boxes are the triangle, and Kochen–Specker contextuality is this phenomenon in
  the lab. The theory's triangle is literal there, but that is the owned finite,
  ordinary-probability side (Abramsky–Brandenburger; Kharoof–Ipek–Okay).

Status: pointers only. They need their own cases before any claim. They do suggest that "a world
exists" in case 3 may be a property of Newtonian time, not of three bodies.

## Equilibrium after three cases

| Case | Separated views? | Non-settling statistics? | Asynchrony? | Pointless? |
|---|---|---|---|---|
| 1. Three species, field stations | yes | yes (heteroclinic) | yes (own epochs) | **yes** (P(none) = −0.2) |
| 2. One observable, delay windows | no (same variable) | yes | yes | no |
| 3a. Three bodies, pair stations | yes | only along oscillatory motions (rarity open) | yes | only there |
| 3b. Three-body universe, own perspectives | yes | as 3a | not in Newtonian time | no (Newtonian) |

- **Pattern so far** (descriptive, NOT a generalisation): pointlessness appears only when three
  things hold together:
  1. views of separate variables;
  2. long-run statistics that never settle;
  3. observers that cannot combine their averaging.

  The triangle of views exposes it in finite settings.
- **Pushback on "world = model".** Long-run worlds exist as ideal limits but come as a loop chosen
  by the observer (case 1). Shared absolute time forces a single world (3b). So *time* may be what
  decides whether perspectives can fail to have a model, more than the dynamics.
- **Do not generalise yet.** Natural next cases:
  - a fast-mixing system, for case 2's scope;
  - real competition data;
  - the relational-time question in 3b.
