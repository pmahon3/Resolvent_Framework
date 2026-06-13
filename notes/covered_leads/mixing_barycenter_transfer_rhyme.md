# Covered: "Mixing" as a method-transfer between OML descent and Strategy D — RHYME, not transfer

## Status (2026-06-12)

**KILLED as a lead; LOGGED as a recognition.** Probed whether a "mixing"
intuition names a genuine Type-3 method-transfer (one lemma, two
specializations) between the two live open problems:

- **OML descent** — contextual state = `w ∉ conv(S_df)` (barycenter failure).
- **Strategy D** — is `Clop(Yₙ)` σ-complete (countable sup in the algebra)?

Verdict: **rhyme, not transfer.** Blocks promotion under the sharpen
guardrail (no check flipped; no fork-free lemma + concrete witness).

## The discriminator (the single-lemma test)

A Type-3 transfer requires one lemma whose two instances ARE the two kills.
Attempt to state it:

> (L) A finitely-additive barycenter `w` of an extreme boundary `∂C` admits a
> countably-additive representing measure on `∂C` iff [intrinsic completeness].

The statement **forks**, and worse than on distributivity — it forks on
**object type**:

- **OML side** genuinely has this form: `C` = σ-states on `L`, live cell is a
  real barycenter failure `w ∉ conv(S_df)`.
- **Strategy D side does NOT**: the live entry point is **lattice**
  σ-completeness (countable sup exists in `Clop(Y)`), settled in the **Stone
  space** by the interior-overshoot closure argument — no convex set, no
  barycenter, no state anywhere in it.

To force SD into form (L) you need the bridge "lattice-σ-completeness ⟺
state-space completion" = **Loomis–Sikorski / faithful set representation**.
The OML problemset's own `rem:nofaithful` proves **no non-Boolean OML has one**
(KS / no faithful σ-tribe). So the functor identifying the two sides
*provably does not exist* off the Boolean line.

## Mechanism-survival check (both directions vacuous across the line)

- **Interior-overshoot** lives in clopen-union closures in a Stone space; its
  OML image needs the Stone space of `L`, which does not exist as a set
  representation. **Dies crossing to OML.**
- **The orthogonal/meet-zero gap** (`def:gap`) drives all OML contextuality; in
  a Boolean algebra `a⊥b ⟺ a∧b=0`, so the gap is **empty**. **Vacuous on SD.**

Each mechanism is native to one side, degenerate on the other — the signature
of a rhyme.

## Why it can't be otherwise (programme-internal)

Paper II's central theorem: **distributivity is the exact dividing line.** SD is
wholly Boolean; OML descent's engine is non-distributivity. A genuine
method-transfer across that line would contradict the programme's strongest
result.

**The Krein–Milman log is the proof, not just a prior:** P(ℕ) is
Krein–Milman-*trivial* (overview, ultralimit item). So all barycenter
non-triviality on the OML side comes *from* non-distributivity — exactly what
SD lacks. The rhyme is non-trivial precisely where it stops being shared.

## What is actually shared

Only "σ-additivity fails where finite-additivity holds" — the **CE shape** —
which is already [[ce_nonderivability_general]] (Paper I companion note, Łoś +
finite-cofinite). Promoting "mixing/barycenter" would relabel an existing
result. Hence: recognition, logged; not a lead.

## Distinct from the other two "mixings"

- **Fibre / dynamical mixing** — separately dead (bridge theorem false,
  disintegration p_z vs p_z² error); see `fibre_mixing.md`. Tried *as* a
  bridging condition and failed; do not re-enter.
- **Convex/state mixture inside OML descent** — live and central, but it IS the
  existing phrasing of the descent target (Fine's theorem), not a new lever.
