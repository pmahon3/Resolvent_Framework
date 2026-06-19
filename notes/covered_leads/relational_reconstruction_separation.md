# Relational Reconstruction: Separating Predictive from Geometric Content

*Seed — 2026-06-05. From a handoff conversation on the delay-embedding
origin of the programme.*

**Claimed type(s):** Type 6 (exposition/translation) primarily; Type 4
(vocabulary) secondarily. **Bar:**
- *Type 6* — the predictive/geometric separation must let one **state a
  question classical (Takens) reconstruction cannot pose**, for a named
  audience (dynamical-systems / time-series reconstruction), and the
  reframing must be non-trivial work, not relabelling.
- *Type 4* — "faithfulness of the canonical factor" as the reconstruction
  primitive must pass the three-statements test: ≥3 new statements
  expressible in it that are awkward or unstateable in embedding language,
  plus ≥1 non-trivial result. (CE-as-engine + the skew-product limit are
  candidates; this needs to be checked, not assumed.)

**Not claimed:** Type 1/2 (new theorem/proof). The delivering mechanics are
classical — Koopman 1931, Krieger generating partitions, Rokhlin
disintegration. The novelty audit already records "reconstruction theorem =
Krieger in delay-map language." Do **not** let "relational reasoning is
powerful" re-badge Koopman/Krieger as new. The one genuine theorem-locus is
**Part I / CE** (coherence ⟹ unique σ-additive observable measure, not
first-order derivable), which sits *upstream* of reconstruction.

## The question

Classical reconstruction (Takens) makes "recover the hidden state from a
scalar time series" well-posed by **assuming the target**: a manifold of
dimension `d`, with its topology, neighbour relations, smoothness. That
assumption is the abductive smuggling the relational standpoint objects to —
you posit the space you are reconstructing into, then reason backward.

Proposal: drop the target. Reason only from the **internal relational
structure of the series** — its morphisms (the shift acting on the observable
σ-algebra, the entailment/order relations among observed events) — and ask
what σ-additive *probabilistic* content that determines, without positing a
space. Does the relational view deliver something the classical case could
not, where the reconstructed space had to be assumed?

## The answer (two halves; the deliverable is the line between them)

**It cannot deliver the reconstructed space — and that is a theorem, not a
hedge.** The skew-product witness (`X = A^ℤ × B^ℤ`, `T = σ×σ`, observe
`h(a,b) = a_0`; the `b`-fibre is invisible) gives collision `→ 0` while
`δ_L = 1/4` for all `L`: the observable algebra does **not** fix the
realization (see knowledge map, *geometric ≠ algebraic reconstruction*,
2026-05-14, and the corrected bridge note). So "reason from morphisms of the
series, recover the state space without assuming it" is **provably
impossible**. Any claim that the relational view returns the geometry
contradicts the skew-product.

**What it genuinely delivers — unavailable classically.** Takens makes the
problem well-posed by *assuming* genericity (a generic observable embeds).
The relational view drops that and replaces it with a **testable property of
the series**:

> Is the canonical factor faithful — does the delay algebra generate the full
> σ-algebra mod μ? (Reconstruction theorem = Krieger's generating-partition
> theorem in delay-map language.)

Embedding quality moves from **assumed premise** to **checkable conclusion**.
When it fails, the obstruction is *named* (an invisible fibre the
observations never resolve) rather than assumed away. **Assumption →
checkable criterion** is the well-posedness gain.

Two bonuses:
- **Defined where "assume a manifold" is meaningless** — stochastic,
  fractal, symbolic systems (the Cantor examples). Classical Takens cannot
  state the problem there; the faithfulness criterion can.
- **Separates two questions the classical framing fuses:**

| | Relational view |
|---|---|
| **Predictive / probabilistic** content (conditional laws, σ-additive observable measure, Koopman–Perron prediction) | **Fully delivered** from morphisms of the series alone; the target manifold was *surplus*. |
| **Geometric** state-space (dimension, neighbour relations, embedded manifold) | **Provably underdetermined** (skew-product). The relational view cannot and should not try to deliver it. |

**The deliverable is this separation itself** — that probabilistic
reconstruction needs no assumed space, geometric reconstruction needs one and
cannot get it from relations. Classical framing cannot pose the separation
because it imports the geometry before the question is asked.

## What this is NOT (closed off this session)

The delay-dimension-as-context / OML framing **fails** for a single series.
Delay algebras are nested, `O_1 ⊆ O_2 ⊆ ⋯`, all sub-σ-algebras of one
measure algebra, so the family is directed/compatible → Boolean colimit →
contextuality decorative (Paper II forcing: only *incompatible* contexts
force an OML). The L=1-vs-L=2 Cantor panel is **refinement, not
incompatibility** (`O_1 ⊆ O_2`), with common refinement `O_∞ = ⋁_L O_L`
available from the data. Contextuality could only enter where contexts cannot
share one measure algebra — multiple non-co-realizable observers/sensors, or
incompatible dynamical hypotheses as rival realizations — which is **not** the
single-series case. So the genuine ill-posedness here is the geometric ≠
algebraic underdetermination, *not* a contextuality.

## Open / next (Phase 4 — user's call)

1. **Three-statements test for Type 4.** Find ≥3 statements about
   reconstruction natural in faithful-factor language and awkward/unstateable
   in embedding language, + ≥1 non-trivial result. Candidates: faithfulness
   as a checkable criterion; the skew-product as the canonical failure;
   stochastic/symbolic reconstruction stated without a manifold.
2. **Audit against the novelty record.** The mechanics are classical; the
   contribution must be the *separation + criterion*, expositorily
   non-trivial. Run `/audit full` to test whether Type 6/4 bars actually
   clear or whether this collapses into already-known ergodic theory
   (the audit's standing worry — "Krieger in delay-map language").
3. **CE as the upstream engine.** The predictive half rests on the Part I /
   CE measure existing at all. Make that dependency explicit; it is where any
   genuine theorem-content lives.

## Phase 2 audit verdict — PARK (2026-06-06)

`/audit full` (opus, web search). **Pure: KNOWN. Type 6: FAIL. Type 4: FAIL.**

The predictive/geometric separation *is* the **factor-vs-conjugacy
distinction** of ergodic theory (Walters, Glasner, Einsiedler–Ward,
Petersen all carry it). The specific delay-embedding translation this seed
offers is not merely "known to ergodic theorists" — it is **already
published in the target audience's own venues**, which kills the Type 6
"inaccessible literature" bar directly:

- *Fibre-indistinguishability* (non-injective observable → invisible fibre →
  distinct states, distinct futures): Botvinick-Greenhouse, *J. Stat. Phys.*
  2025 (arXiv 2409.08768) — the measure-theoretic Takens recast as a
  pushforward, fibres = non-injectivity. Already cited in our knowledge map
  as `BotvinickGreenhouse2025`.
- *Observability as a checkable property controlling faithfulness*:
  "Functional observability and subspace reconstruction in nonlinear
  systems," arXiv 2301.04108 — the seed's exact move.
- *Stochastic/manifold-free reconstruction without clean genericity*: the
  probabilistic-Takens line (a.e.-orbit, self-intersections up to negligible
  probability).

**Type 4 three-statements test, run on the seed's own three candidates,
all fail:** (1) "faithfulness as checkable criterion" = "the partition
generates mod μ" (Krieger; δ(𝒪)→0 is the Rokhlin metric, named since 1967);
(2) "skew-product as canonical failure" = a standard non-generating factor
(project off an independent fibre); (3) "manifold-free stochastic
reconstruction" backfires — manifold-freeness is the *default* setting of
the abstract p.m.p./Cantor machinery (Jewett–Krieger), not a capability the
vocabulary unlocks.

This matches the seed's own pre-registered kill condition: it collapsed into
"Krieger in delay-map language," and the audience already has it.

**The one load-bearing observation that survives** — the predictive half
depends entirely on the CE / Part I measure existing at all — belongs to the
CE / Part I locus (`notes/programme/programme_reception/`), where the genuine
theorem-content already lives; it is recorded here, not inserted into those
finished reception documents. This seed parks as a known restatement. Filed:
`notes/covered_leads/`.

## Cross-references
- Geometric ≠ algebraic reconstruction; skew-product counterexample:
  `notes/knowledge_map/knowledge_map_body.tex` (§ reconstruction,
  2026-05-14).
- Paper II forcing (compatible→Boolean, incompatible→OML; the discriminator
  used to close the contextuality branch): `papers/paper_ii/`,
  `notes/open_questions/oml_onboarding.tex` §1.
- "Stone/Takens = rhyme not structure" (`0ff3387`) — the standing warning
  against framing-analogies in this corner.
- CE / Part I novelty locus: `notes/programme/programme_reception/`.
