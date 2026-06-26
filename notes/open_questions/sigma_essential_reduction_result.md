# The σ-essential reduction — standing result

> **⚑ FINAL STATUS (weld run, 2026-06-25): the A↔HW2 weld is RESOLVED — they are
> ORTHOGONAL, and HW2 DROPS OUT.** This note's body below still narrates the
> earlier "weld open / three walls" stage (kept for the trail); the resolution
> supersedes it. **The witness reduces to σ-point-selection (A) FULL STOP** — a
> state-realization question on a fixed σ-complete lattice, strictly above
> faithful-tribe (B); the lattice-completion problem HW2 (C) is a *type-mismatched*
> red herring, not on the route. A's carrier is already σ-complete, so C is
> trivially-yes there; A-failure is a state defect, not a completion defect.
> Clean statement: [[sigma_essential_reduction_writeup]] §3 + §5. ⟦self-checked
> adversarially, advisor-pass pending; reduction-to-A stands regardless.⟧

*Recorded 2026-06-25, CORRECTED + then RESOLVED same day. Theorem-shaped finding of
the forcing-programme work: the σ-essential contextual witness question REDUCES to
σ-point-selection failure (a state-realization wall, cardinal-sensitive). ⟦HAND —
"witness ⟺ σ-point-selection-failure" verified at sketch level.⟧ Body below records
the intermediate "is it HW2?" stage now closed by the weld run.*

---

## The result (conditional) — ⚠ CORRECTED 2026-06-25: TWO walls, not one chain

> **Claim (corrected).** The existence of a *concrete σ-essential contextual
> witness* — a concrete σ-complete non-Boolean off-center OML `L ⊆ P(Ω)` with a
> finite local 2-valued state `s₀` that extends to **no** global σ-additive
> 2-valued state on `L` — reduces to a **σ-point-selection failure**: a locally
> coherent 2-valued pattern with no globally coherent σ-additive 2-valued
> realization. The Ulam/measurable-cardinal strength (Blecher–Weaver) attaches to
> **this state-realization side.** Its existence is **not decidable in ZFC by any
> route attempted.**

**⚠ The earlier "⟺ HW Problem 2" was an OVERSTATEMENT — two distinct walls were
welded.** They are *related but not proven equivalent*:

- **σ-point-selection** (the witness side): does a coherent local 2-valued pattern
  extend to a global σ-additive 2-valued **STATE**? This is about *states*; the
  cardinal lives here (Blecher–Weaver: Ulam-measurable on the Hilbert analogue).
- **HW Problem 2** (the adjacent wall): can every omp be **EMBEDDED into a
  σ-complete omp**? (Harding–Wang arXiv:2108.09819, Problem 2, verbatim.) This is a
  *lattice-embedding* question — **plain ZFC, no cardinal in it.**

These are not obviously the same. A σ-completion `L̄` could *exist* (HW2 yes) and a
local state still fail to σ-extend (the new joins in `L̄` add constraints the state
must respect); the cardinal-sensitivity is on the state side, not the embedding
side. **Honest direction held:** HW2-failure (no σ-completion) *plausibly* forces a
state-realization gap, but the converse is unestablished. So HW2 is an **adjacent
wall, NOT confirmed as "the bottom."**

So the honest status of the "σ-essential witness" prize is neither
*constructible* nor *refutable* in ZFC, but **reducible to σ-point-selection
failure** — whose own relationship to the named open problem HW2 is itself an open
sub-question (the unproven weld).

## Why (the verified core)

A global σ-additive 2-valued state on a concrete `L ⊆ P(Ω)` is either a
point-evaluation `δ_ω` (always available) or a **non-Dirac** σ-state. A finite
local `s₀` fails to extend **iff** (i) no `δ_ω` realizes it — the
"`⋂{generators s₀↦1} = ∅`" condition, freely arrangeable by the Navara–Pták
intersection device — **and** (ii) no non-Dirac σ-state rescues it.

Condition (ii) is exactly the **σ-point-selection problem**: does a globally
coherent σ-additive 2-valued **state** thread the locally-coherent constraints?
Hence:

- **witness exists ⟺ σ-point-selection fails** (a witness IS a coherent local
  pattern with no global σ-state realization). ⟦verified at sketch level — this is
  the genuine equivalence⟧
- **σ-point-selection vs HW2:** σ-point-selection is a *state*-realization
  statement (cardinal-sensitive); HW2 is a *lattice*-embedding statement (plain
  ZFC). The implication "HW2-fails ⟹ σ-point-selection-fails" is *plausible but
  unestablished*, and the converse is open. **So the reduction lands on
  σ-point-selection, and whether that equals HW2 is the unproven weld** — NOT a
  verified equivalence.

### THREE walls, not two (2026-06-25 — #29 sharpened, NOT resolved)

A sharper sub-result, distinguishing three distinct objects (keep these lexically
separate — blurring them was the recurring error):

1. **σ-point-selection** (state-realization): does a coherent local 2-valued
   pattern extend to a global σ-additive 2-valued **state**? (Cardinal-sensitive.)
2. **faithful-tribe-representability**: does `L` embed faithfully into a σ-tribe of
   *honest sets* (a σ-algebra)?
3. **HW2-embedding**: does `L` embed into *some* σ-complete **OMP** `L̄` (not
   required to be a tribe of sets, not concrete, not state-separating)?

Established:
- **σ-point-selection-failure is STRICTLY ABOVE faithful-tribe-representability**
  ⟦charted, cited: the Floor (`thm:floor`) forces faithful tribe-of-sets ⟹
  distributive ⟹ Boolean; Dvurečenskij σ-LS (J.Aust.MS 68, 2000) gives only a
  σ-*epimorphic* (lossy, non-faithful) tribe image, which does NOT separate the
  2-valued points — the "tribe-vs-points gap"; RDP needed, OMLs lack it (MO₂)⟧.
- **HW2-embedding does NOT entail faithful-tribe-representability** ⟦HAND, today⟧:
  HW2's `L̄` may be a *non-distributive abstract* σ-OMP carrying no tribe-of-sets
  structure, so it sidesteps the Floor entirely. (One non-implication — NOT mutual
  independence; HW2 ⟹ σ-point-selection and the converse both remain open.)

**∴ HW2 is a genuinely THIRD wall, off to the side of the state wall — NOT shown to
be the same as σ-point-selection.** This *narrows* the reduction's bottom from
"σ-LS / HW2" to "σ-point-selection, strictly above faithful-tribe, with HW2 a
separate open embedding question." The #29 weld (σ-point-selection ↔ HW2) is
**still open** — sharpened and precisely located, not closed.

## What this DISsolves and what it does NOT

- **Resolves the framing confusion:** "the construction keeps hitting a wall" is
  not fatigue — it is the theorem. Four independent routes today (non-classical
  logic, the ¬Ψ lever, the direct construction, the template no-go) plus ~21 prior
  fenced reversals all collapse to **σ-point-selection** *because the witness
  question IS σ-point-selection*. (Earlier these were said to collapse to "σ-LS /
  HW2" — that conflated the state-realization wall with the lattice-embedding wall;
  the convergence is on the state side.)
- **Does NOT prove the cell empty / ¬Ψ.** Blecher–Weaver: the Hilbert analogue
  *exists* under an Ulam-measurable cardinal, so ¬Ψ is not a ZFC theorem. The
  reduction says "as hard as σ-point-selection," not "impossible."
- **Does NOT prove witness ⟺ HW2.** The weld between σ-point-selection (state) and
  HW2 (embedding) is unproven. The genuine bounded next question: **is
  σ-point-selection-failure equivalent to HW2, or strictly between it and the
  witness?** ([[#29]] — a clarification question, not a HW2 assault.)

## Pointers

- Mechanism + verification: [[sigma_essential_construction_runs]] (¬Ψ first run,
  Con(Ψ) run, template no-go, selection-first kill).
- HW Problem 2 / no regular completion: Harding 1998; Harding–Wang
  arXiv:2108.09819.
- Navara–Pták 1983 (template + concentration criterion):
  `literature/navara_ptak_1983_two_valued_measures_sigma_classes.pdf`.
- Hilbert-side precedent (the measurable-cardinal flavor): Blecher–Weaver
  arXiv:1607.08505.
