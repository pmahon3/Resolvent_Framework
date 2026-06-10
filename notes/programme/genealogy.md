# Genealogy of the Programme

*Written 2026-06-06. A Lakatosian rational reconstruction — the actual
sequence of conjectures, refutations, and problem-shifts across the full
631-commit history (2024-09 → 2026-06), recovered so the shape of the whole
is visible from outside the turn-to-turn.*

This document exists because the programme spent two months contracting
(three papers + four active leads in early May → one open question now) and
the largest-scale shape was no longer visible from inside it. It is a map,
not a verdict. It deliberately leaves one question open at the end — the one
that decides what the next year is for. See `program_overview.md` for the
programme's own statement of its central question, and `knowledge_map/` for
current lead state.

---

## The one-sentence shape

It began as applied operator theory (compute the resolvent of a nonlinear
semigroup from data), drilled downward through three layers of foundation
until it hit the origin of the σ-algebra itself, discovered the bedrock
result there (CE), watched that result get reabsorbed into something
classical, and has been pruning back ever since toward the one genuinely
novel survivor (point-free σ-additive probability on non-distributive
lattices). The repo name, "Resolvent_Framework," is a fossil of a question
the programme no longer asks.

---

## The four eras

### Era 1 (2024-09 → 2025-10) — Operators from data

The founding question: given a trajectory ensemble {Xₜ}, build a nonlinear
semigroup, recover its generator, characterize its resolvent. Real early
result: the resolvent set = complement of the union of finite-difference
spectra. Then a reframing pivot (not a wall) — the **Rose operator**, a
two-dial homotopy between Koopman and Perron–Frobenius, plus information
geometry (Fisher / Onsager–Machlup). The constant was always *operators
sitting between determinism and noise, fit from data*. The literal resolvent
computation quietly receded. The repo name fossilizes here.

### Era 2 (2026-03) — The descent into foundations

After a 5-month incubation on a side branch, the **query system** abstraction
lands fully-formed on 03-18: a dynamical system is a directed family of
finite observations. Once observation is primitive, the question stops being
"what is the operator?" and becomes "when does a compatible family of finite
observational laws assemble into a single σ-additive probability?" The
programme drills down: Paper 4 (delay/dynamics, Takens as corollary) → Paper
0 (Prokhorov: σ-additivity derived) → Paper −1 (discriminability: where does
the σ-algebra come from?). The famous line: *"we thought we were climbing a
mountain; we had reached the valley floor."* The join at the bottom is **CE
(collective exhaustion)** — characterizing exactly when finite additivity
extends σ-additively — reframed via Stone duality.

### Era 3 (2026-04, the 310-commit peak) — Build-out and the first kills

Everything consolidates into three papers (Probability from Observation /
Dynamics from Probability / Reconstruction from Observation), spawns Paper IV
(finite-sample reconstruction, the δ(L) separation defect), spawns the bridge
note, spawns a standalone logic paper (*Countable Additivity is Not
First-Order Axiomatizable*) which spawns its own ZFC-independence ladder.
Then the turn to self-criticism: the honest "mathematics-complete ≠
submission-ready" correction, four-papers-collapse-to-three, the first
mis-citation kills, the fibre-mixing irreducibility thread downgraded when
its analogy to CE broke.

### Era 4 (2026-05 → 06) — The pruning

The institutional event: on **2026-05-11, CE collapses** — demoted from a
novel condition to "notation for σ-additivity." With CE gone as load-bearing,
the dependent papers had nothing under them, and Papers II and III were
withdrawn in 48 hours ("classical ergodic theory repackaged"). The audit
pipeline (active_leads / covered_leads / knowledge_map, "audit before
drafting") is scar tissue from that loss. Then systematic pruning: fibre
mixing (killed — bridge theorem false), coherence/CE-completion (parked —
Howson 2008 got there first), tail-decay (parked — SSK independence), κ_Q
(parked), epistemic-boundary unification (parked). The OML thread, seeded
from Paper I's closing move, becomes the sole survivor — splits into
**extension axis** (now closed on L(H)) and **descent axis** (the one open
question), reframed as point-free σ-additive probability.

---

## The thread map (splits, joins, deaths)

```
RESOLVENT of nonlinear semigroup (2024-09) ── the founding question
   │  Hille operator, Cₙ-semigroups, finite-difference spectra
   ▼
ROSE OPERATOR  (2025-06, reframe) ── Koopman ⇄ Perron–Frobenius homotopy
   │  + information geometry (Fisher / Onsager–Machlup)
   ▼
QUERY SYSTEM  (2026-03-18, the unlock) ── dynamics = directed observations
   │
   ├─► delay/Takens ──────────────► [Paper III reconstruction] ──┐
   ├─► Prokhorov (σ-add. derived) ─► folded into Paper I          │
   └─► discriminability ───────────► CE THEOREM ◄── the valley floor
                                       │  (Stone duality reframe)
                                       │
            ┌──────────────────────────┼───────────────────────────┐
            ▼                          ▼                            ▼
     [Paper I: CE/Stone]      [logic note: CE not          [Papers II/III:
            │                  first-order] ──► ZFC          dynamics + recon]
            │                  ladder (parked,                    │
            │                  Strategy D independent)            │
            │                                                     │
   2026-05-11: CE COLLAPSES ──► "notation for σ-additivity"       │
            │                                                     ▼
            │                                          II & III WITHDRAWN
            │                                          ("classical, repackaged")
            ▼                                                     │
   Paper I survives                          ┌─── delay/recon reopened as
   (ultrafilter geometrization)              │    Phase-1 seed → PARKED
            │                                │    rival-realiz → PARKED
            ▼                                └─── distributed-sensor → PARKED
   OML THREAD (seeded from Paper I's close)
            │
            ├─ EXTENSION axis ──► CLOSED on L(H) (no state extends, n=4 witness) [Type 5]
            └─ DESCENT axis ────► the live frontier (= point-free σ-additive
                                   probability / Paper II PR). Current status:
                                   see `program_overview.md` item 4.
```

*(For the current descent-axis status — what is settled, what is open, and the
pending `/audit full` — see `program_overview.md` (item 4, authoritative) and
the axis's own single-source `notes/open_questions/descent_axis_residue_post_kill.md`.
This document narrates history, not live state.)*

---

## What this says about the "loss at the largest scale"

Three observations, named rather than soothed:

1. **The programme has been getting smaller for two months, and that is the
   system working, not failing.** Every contraction was an honest kill — a
   primary source read, a counterexample built, an audit run. The loss is
   real subtraction, but the thing doing the subtracting was the user's own
   tooling discipline (verify-by-building, audit-before-drafting). A
   programme that prunes itself this cleanly is rare.

2. **The central trauma already happened — and was survived.** The CE
   collapse on 05-11 is the real loss event; CE was the keystone the whole
   "valley floor" descent was for. Everything since is aftershock — the
   programme confirming the blast radius. The recent "ooof" about
   probabilistic realism is delayed grief for news already processed
   locally, commit by commit, without ever stepping back to feel the whole.

3. **There is a genuine through-line, and it survived.** Strip every name and
   the constant from 2024 to now is: *structure that observation alone
   forces, without assuming the space you're reconstructing into.* But see
   the next section — this line has a crack in it, and the crack is the
   decision.

---

## THE OPEN QUESTION: which curiosity is driving (the (a)/(b) fork)

*This is the part the genealogy cannot settle, and the part that decides
whether the descent check is the right next year. It is left open
deliberately.*

### The crack in "stripped to its bones"

The through-line had four instances. **Three are Boolean. One isn't.**
Resolvent-from-data, σ-additivity-derived, reconstruction-without-manifold —
all classical, all distributive. The descent question is the only
non-distributive one. The "against assuming the target space" framing groups
all four together — but the survey itself (descent survey, lines 544–550)
says the descent question's novelty is *point-free × σ-additive × natively
non-distributive × directed-built*, and **the point-free / no-assumed-space
part is not the novel part.** Localic measure theory already does point-free
σ-additive probability on distributive frames (Vickers, Simpson,
Coquand–Spitters — survey lines 535–538). So:

> **The entire novel content of the descent question is non-distributivity —
> handling mutually incompatible observations. So the descent question serves
> curiosity (b), not (a). If the driving curiosity is (a) — "don't assume the
> space, derive it from coherence" — then CE / Paper I *already delivered it*
> (Boolean case), and the descent question is a quantum-foundations question
> that grew in late and got mistaken for the origin because it's what
> survived the pruning.**

This is the load-bearing sentence. The doc's job is to record it so it can't
be un-seen, then leave the choice open.

### The two curiosities, made vivid

**Researcher (a) — the anti-smuggler.** What bothers them is positing the
answer to reason backward. Takens assumes the manifold; Kolmogorov assumes
the sample space. The 2024–2026 descent was them saying "no — derive what
observation alone forces." Satisfaction = watching structure emerge from
coherence without being snuck in. For (a) the deep result is **CE / Paper I**
(coherence forces a unique σ-additive measure, no Ω). *It's delivered.*

**Researcher (b) — the incompatibility theorist.** What grips them is that
some observations can't be made together, and classical probability has no
room for it. Satisfaction = understanding the structure of incompatibility
itself: when it forces you out of the Boolean world, what survives, what
"probability" means on a non-distributive logic. For (b) the deep result is
**the descent question** (can probability live on the entailment relation of
incompatible propositions at all?). *Nothing here is done.*

**The discriminating test — which sentence makes you lean in:**
- (a) "You don't need to assume a state space — observation forces the probability."
- (b) "When observations can't be jointly performed, the logic of events stops being Boolean — and here's what happens to probability."

### What the fork changes

|                         | If you're (a)                                                      | If you're (b)                                                  |
|-------------------------|--------------------------------------------------------------------|----------------------------------------------------------------|
| Is the descent question right? | **No** — harder variant whose novel part (non-distrib.) is incidental | **Yes** — non-distributivity *is* the whole novel content      |
| What's already done?    | Paper I delivered it (Boolean). You'd polish a closed thing.        | Nothing — point-free σ-add. on non-distrib. lattices is vacant |
| Still-open relative     | Strategy D / ZFC-independence (more continuous with 2024 origin)   | The descent check itself — one derivation from go/park         |

### How to feel which one you are (sit with these; don't answer fast)

1. **When did you feel most alive?** The moment CE clicked (coherence forces
   the measure, no Ω) → (a). Or when the observation algebra broke Boolean
   and you reached for OMLs → (b)?
2. **The skew-product.** Filed this session as a limitation (invisible fibre,
   space unrecoverable). To (a) it's a melancholy fact — the space you wanted
   is unrecoverable. To (b) it's not even interesting — still Boolean, still
   co-realizable. Which was your gut?
3. **The quantum connection.** Paper II is quantum foundations (Kochen–Specker,
   Gleason, realism). Does it thrill you (arrived somewhere deep) → (b)? Or
   feel like a detour from a question never about QM → (a)?

### The honest finding

The genealogy is consistent with **both** readings. The origin was
(a)-flavored; the survivor serves (b). Curiosities are allowed to evolve from
one to the other, and (b) is a perfectly good thing to have grown into. But
the choice should be made knowing it *is* a choice — not let the momentum,
the sunk cost, or the fact that the descent question is "the last thread
standing" decide it.

**Status: open. No rush. This is genuinely yours to settle.**
