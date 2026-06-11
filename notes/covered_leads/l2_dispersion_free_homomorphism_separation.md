# L₂ dispersion-free / homomorphism separation

*Type 4 (vocabulary) + Type 6 (exposition) audit — 2026-06-10. Hostile
referee, primary-source-verified. **VERDICT: KILL — clears no bar.***

**Claimed type(s):** Type 4 (vocabulary) primarily — the df-state/hom
separation as a sharp axis; Type 6 (exposition) secondarily — a Paper II
§5 refinement.
**Bar (Type 4):** three-statements test — ≥3 statements unstateable
before + ≥1 non-trivial result.
**Bar (Type 6):** named audience + inaccessible literature + non-trivial
translation work.

## The candidate

> L₂ (an MO₂-block descent witness) has a separating family of σ-additive,
> dispersion-free states that are NOT 2-valued homomorphisms — a concrete
> σ-orthocomplete OML on which "dispersion-free state" and "2-valued
> homomorphism" come apart, a distinction Boolean & L(H) fuse.

Verified-by-building (correct math, not in dispute): eval states `s_{m,σ}`
are genuine σ-additive dispersion-free separating states; L₂ has no
2-valued homomorphism (diagonal sub-OML, `decide`-reducible to the MO₂
gap fact). The audit tested the *contribution*, not the correctness.

## Why it dies — 5th death on the decorative-σ-additivity rock

**KR1 (df-state ≠ homomorphism is standard) — KILLS.** In quantum logic
"two-valued state" and "dispersion-free state" are explicit synonyms for
σ:L→{0,1} additive on orthogonal pairs; a homomorphism additionally
requires multiplicativity on *all* pairs. The gap between them is the
organizing subject of the concrete-OML / hidden-variable program:
- **Pták–Pulmannová**, *Orthomodular Structures as Quantum Logics* —
  concreteness ⟺ a *full set of two-valued states* (not assumed
  multiplicative). "Representation of Concrete Logics," Rep. Math. Phys.
  73 (2014) 225.
- **Kalmbach 1983**, Ch. 1–4 — K(2²) = MO₂ = "Chinese lantern," the
  standard first example where a two-valued state fails to be a
  homomorphism.
- Svozil/Tkadlec, "Embedding Quantum Universes…" (arXiv:1402.5199);
  Domenech–Freytes, "Equational characterization for two-valued states"
  (arXiv:1307.7417) — homomorphism = classical truth-valuation / hidden
  variable, two-valued state = the weaker object; the *distinction* is
  the whole point.
"A dispersion-free state on MO₂ that is not a 2-valued homomorphism" is a
textbook example, not new vocabulary.

**KR2 (does L₂ add over finite MO₂?) — KILLS (the 4×-fatal rock).** The
seed *concedes* it: the separation is entirely an MO₂ fact (`decide`-
reducible, "NO lift needed"), and the eval states are σ-additive
**automatically and for free** ("the evaluation only sees one block…
cap-at-2 keeps within-block joins finite"). σ-additivity is satisfied
vacuously, changes nothing testable, and would hold for *any* finite-block
construction. The infinite/σ-additive/concrete L₂ packaging is
**decorative** — the exact rock that killed `descent_ladder_mechanistic_
feasibility`, `distributed_sensor_contextuality`, `relational_
reconstruction_separation`, and Paper III.

**KR3 (distinct open slot?) — KILLS.** Because σ-additivity collapses to a
finite within-block condition, L₂ does NOT occupy the open
"σ-additivity-boundary" slot the prior scout found (Cannon–Döring
finitely-additive; localic distributive). It's the finite MO₂
homomorphism-free fact with a free σ-additive label. The genuinely
distinct object — *strict point-free* / non-concrete — is **explicitly
disclaimed**: L₂ is concrete/point-ful and FAILS it. No residue. The
"two mechanisms" contrast (gap vs. KS state-poverty) reduces to "a
finite OML vs. L(H)≥3" — finite OMLs trivially have no KS obstruction.
Not novel.

## Type 4 three-statements test — FAILS

1. "A concrete σ-orthocomplete OML with separating df-states but no
   2-valued homomorphism exists." → already sayable (concrete ⟺ full set
   of two-valued states; MO₂ is concrete + homomorphism-free).
2. "Dispersion-free ≠ 2-valued homomorphism on a general OML." → already
   sayable, and already *in Paper II* attributed to MO₂. Standard since
   the 1970s.
3. "L(H) and L₂ achieve homomorphism-freeness by different mechanisms
   (poverty vs. gap)." → a contrast/analogy, not a statement enabling a
   non-trivial result; fails even the Type-3 method-transfer bar.

No non-trivial new result follows.

## Type 6 — FAILS

The exposition is the already-applied §5 correction. It is an internal
**bug-fix** (line-304 conflation, fixed 2026-06-10), not translation work
for a named underserved audience reading inaccessible literature
(Kalmbach / Pták–Pulmannová are standard graduate quantum logic). An
already-applied correction to one's own paper is not a contribution.

Types 1,2,3,5,7 all fail trivially (folklore theorem; standard one-line
MO₂ proof; analogy not transfer; closes nothing; no methodology
advantage).

## Disposition

- **The Paper II §5 line-304 fix STANDS** as an internal correctness fix —
  it was a genuine bug (df-state stated to *be* a homomorphism; false,
  L₂/MO₂ counterexample) and is already landed in
  `distributivity_and_realism_body.tex` (operative VDR = dispersion-free
  state throughout, compiles clean). That is the real, complete output.
- **No separate Type-4/Type-6 contribution.** Seed parked here as the 5th
  death on the decorative-σ-additivity rock. Lattice ★ (Lean,
  `DescentWitness*.lean`, 0 sorry) stands on its own and is unaffected.

## Single most likely kill (plainly)

σ-additivity is free here, so the claim reduces to the textbook fact "a
dispersion-free state on MO₂ need not be a 2-valued homomorphism" — which
is standard quantum logic AND already written into Paper II §5. No new
object: L₂ is decorative packaging around a finite MO₂ fact, and the one
object that would have been new (strict point-free / non-concrete) is
exactly what L₂ admittedly is not.

Source seed (moved from `open_questions/verification/`):
`l2_state_space_separation.md` content preserved below for reference.

---

(See git history `9ebe51e`, `9fd95d8`, `31e88fd`, `3148123` for the
verified-by-building record. Scripts: `verify_mo2_state.py` remains in
`open_questions/verification/` (foundational MO₂ fact); `l2_states.py` and
`diag_hom.py` were archived 2026-06-11 to
`archive/oml_descent_inhabitation_dead/` with the dead L_MO₂ lead.)
