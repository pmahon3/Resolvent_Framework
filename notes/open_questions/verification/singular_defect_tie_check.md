# Are the singular residue and the descent defect the same object?

Tests the conjectured "tie": that the extension-axis singular case and the
descent-axis defect D are two faces of one object (L(H)'s infinite sector),
sharing the carrier ↑p. **Verdict: the strong tie is REFUTED; a weaker
"same sector, disjoint carriers" survives (strongly suggested).**

**Sources.** McDonald–Bimbó 2023 (filter/P(A)/h defs, Def 3.4);
[[mb_primeness_check]], [[meagre_vs_measure_check]],
[[lh_singular_dichotomy]]. Computations checked in L(ℂ³) concretely.

## The claim tested (T)

A singular state on L(H), insofar as it corresponds to mass on the MB dual,
must place that mass on the defect points ↑p that block descent — so
"singular state extends + concentrates" and "a measure carries mass on D"
are the same phenomenon, with ↑p the shared carrier.

## The decisive computation (proved)

An atom of mass m at a filter ↑p induces, via s(a) = μ̂(h(a)),
  s(a) ⊇ m·[a ∈ ↑p] = m·[p ≤ a].
Evaluate at a = p: **s(p) = m > 0**. But a **singular** state has s(p) = 0
for every rank-one (line) p — lines are compact and singular states
annihilate K(H) ([[lh_singular_dichotomy]] step 4). So a singular charge
carries **no atom at any line-↑p**. These are exactly the defect carriers
the repo proved (the isolated-point result holds for p an atom/line). Hence
the singular state and the proven defect carriers are **disjoint**: defect
witnesses ↑p (lines) sit on the NORMAL / finite-rank-detected side; the
singular state is DEFINED by annihilating all finite rank. (Checked in
L(ℂ³): p = span(e₁+e₂), a = span(e₁), b = span(e₂).)

## Two corrections this forced (both now propagated)

1. **δ_{↑p} is not a state.** [p ≤ ·] is two-valued and fails
   orthoadditivity (p = span(e₁+e₂): s(a∨b)=1 ≠ 0+0=s(a)+s(b), a⊥b) —
   forbidden by Kochen–Specker on L(H), dim ≥ 3. So the Boolean
   "point-mass ↔ pure state" dictionary BREAKS in the OML case. (A finding
   in its own right: no Dirac-at-realised-point picture survives.)
2. **"Infinite support" mis-names the defect condition.** ↑p ∈ D iff
   p ≤ ⋁aₙ (always) and p ≰ aₙ ∀n, i.e. v not parallel to any eₙ —
   ANY non-basis-aligned line, finite-support e₁+e₂ included; and
   basis-DEPENDENT. Corrected in mb_primeness_check, meagre_vs_measure,
   two_grades_of_pr, and survey Rem 2.11.

## What survives (strongly suggested, not proved)

Singular mass, if it exists, cannot sit on line-↑p; it must live on the
**infinite-dimensional / non-principal** filters — the "tail" /
points-at-infinity of S₀ — OR be purely diffuse (no atoms). For
infinite-dim p, [p ≤ e] = 0 for every finite-rank e, so such ↑p contribute
nothing to s on finite rank, consistent with singularity; these ↑p also lie
in D. But the isolated-point/non-meagre result was proved only for ATOMS
(lines), so whether infinite-dim ↑p are isolated/atoms of a charge is NOT
established.

**Corrected tie:** same broad "infinite region" of S₀, but **opposite
specific carriers** — singular mass on the infinite-dim/non-principal tail;
proven defect witnesses on rank-one ↑p. So the singular case (extension)
and the descent defect are NOT the same problem; resolving one does not
resolve the other. The "same object / shared ↑p" conjecture is wrong.

## Consequence for the impossibility instinct

The two residues being disjoint (not one funnel) weakens the "everything
reduces to a single obstruction" picture: a singular-case resolution would
not automatically settle descent. The impossibility direction, if pursued,
must treat them separately.

## Open / not determinable

- Whether a singular state extends at all: OPEN (unchanged).
- Whether infinite-dim ↑p are isolated points / can be charge atoms: not
  determinable from MB (no measure/category content in the source; the
  isolation result is the programme's, proved only for atoms).
- Where exactly singular mass sits (infinite-dim ↑p vs diffuse vs
  non-principal): strongly suggested "tail", not pinned down.
