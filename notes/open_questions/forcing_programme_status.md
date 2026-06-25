# Forcing programme — status (superseded by the reduction)

*2026-06-25. Honest post-mortem. The σ-essential work was taken on under "commit to
the forcing programme: prove Ψ independent of ZFC." This records where that landed
and what would have to be true to revive it. The actual result lives in
[[sigma_essential_reduction_result]]; this note is only the forcing-context
accounting.*

---

## One-line status

**The forcing programme never ran — its target dissolved into a reduction upstream
of any forcing.** The σ-essential question is not "independent, prove it by forcing";
it is "reducible to **σ-point-selection**, an open state-realization wall, with
measurable-cardinal strength attached but no forcing-ready sentence yet."

This is not a defeat — it is the programme correctly diagnosing that it was
**premature**. Forcing settles *independence*; you reach for it only once you hold a
well-pinned sentence whose independence is the question. On inspection the sentence
reduces, upstream, to an open mathematical problem the forcing would not resolve.

## What happened to each piece

The programme had three pieces. All resolved *before* forcing became operative:

- **Con(Ψ) — build/force a witness.** Collapsed into σ-point-selection. The
  Navara–Pták template builds its own rescuer; the "gap" *is* the realization
  question, not a thing a forcing notion adds or kills. (CHARTED: Con(Ψ)
  CONSTRUCTION + TEMPLATE NO-GO blocks.)
- **¬Ψ — refute in L / under no measurable cardinal.** The natural lever
  (no-measurable-cardinal ⟹ σ-states are Dirac ⟹ reduce to point-realization) is a
  *σ-algebra* theorem; the carrier is non-Boolean (σ-completeness is
  orthogonal-joins-only), so there is no σ-algebra to run Ulam on. Blocked at the
  missing σ-LS representation. (CHARTED: ¬Ψ FIRST RUN block.)
- **The independence claim.** Reduces to σ-point-selection, whose own relation to
  the named open embedding problem (Harding–Wang Problem 2) is itself a *third* open
  wall. (CHARTED: TEMPLATE NO-GO + reduction note.)

## Why forcing was the wrong next tool

Forcing acts on the **metatheory** (it builds models of ZFC) to decide a
**set-theoretic sentence**. The bottleneck here is not "is this sentence
independent" — it is "what *is* the sentence," and the answer is an **open object-level
math problem** (does a coherent local 2-valued pattern admit a global σ-additive
2-valued state on a non-distributive concrete σ-OML). You cannot force your way past
an unsolved mathematics question; you can only force once the question is a clean
arithmetic/combinatorial statement. It is not — yet.

(Related charted dead end: "No forcing-over-quantum-logic exists; Ozawa OML-valued
set theory is orthogonal." That was a *different* false worry — forcing CAN study a
non-distributive object, as Blecher–Weaver do classically. The real blocker is the
one above: the target sentence isn't pinned, not that the tool is contaminated.)

## What would revive it

The forcing programme becomes live again **iff** the σ-point-selection wall is first
turned into a clean independence-ready sentence — concretely, one of:

1. **A specific candidate witness OML** `L` (concrete, σ-complete, non-Boolean,
   off-center, uncountably generated) is pinned, and "L has a binding global σ-point"
   becomes a definite Σ²₁-ish statement about that fixed `L` — *then* forcing/inner-model
   theory can attack its independence. (We do not have such an `L`; by-hand
   construction is charted-dead, and the abstract existence is the reduction itself.)
2. **The σ-point-selection ↔ HW2 weld closes** (currently a third open wall): if
   σ-point-selection-failure is shown equivalent to a *known* independence-flavored
   statement, the forcing target is inherited rather than built.
3. **The Hilbert→concrete transfer is found** (Blecher–Weaver's Ulam-measurable
   mechanism relocated to a concrete σ-OML) — but Akemann–Weaver (no routing port)
   says this is direct construction, i.e. case 1.

All three route back through the same open wall. Until one is cleared, forcing has no
well-posed sentence to act on, and the honest deliverable is the reduction, not an
independence proof.

## Verdict

**Forcing programme: PARKED as premature, not failed.** Its value was diagnostic — it
forced (the irony noted) the discovery that the σ-essential question reduces to
σ-point-selection rather than awaiting a forcing verdict. The reduction
([[sigma_essential_reduction_result]]) is what the programme actually produced.
