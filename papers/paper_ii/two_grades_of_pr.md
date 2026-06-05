# Two grades of probabilistic realism (PR_lattice / PR_dual)

Companion record for Paper II (`distributivity_and_realism`). This note
holds the PR-realism *overlay* on the OML extension/descent split and the
one **unresolved Paper II decision**. The underlying mathematics — the two
axes, the finitary wall, the L(H) clustering result, the "does descent do
independent work" question — lives in the standalone survey
`notes/open_questions/oml_onboarding.{tex,md}` and is not restated here;
this note only adds what is specific to the EA/PR/VDR vocabulary.

## The two grades

Re-expressed in Paper II's EA/PR/VDR vocabulary, *probabilistic realism*
(PR) splits into two grades that the Boolean case fuses and
non-distributivity separates. Same extension/descent split, named in the
realism language — not a separate construction.

- **PR_lattice(s):** a σ-additive measure on the *lattice* A agreeing with
  s. For L(H), dim ≥ 3, Gleason supplies this for every σ-additive state.
- **PR_dual(s):** a σ-additive Borel measure μ̂ on the *dual* S₀(A) with
  μ̂(h(a)) = s(a) concentrating on the physical points, μ̂(P(A)) = 1.
  Extension followed by descent.

A Born-rule realist reads off PR_lattice, a relational realist reads off
PR_dual, a constructive empiricist reads EA — the framework marks the
distinctions and serves all three (van Fraassen's stance). The
Whitehead/process reading "descent to P(A) = concrescence" is an optional
lens on why a relational realist privileges PR_dual, not an axiom.

## What is established: a witnessed one-directional separation

L(H) normal states *separate* the grades: they clear PR_lattice (Gleason)
and fail PR_dual (no charge on S₀(L(H)) exists at all — survey §3,
Prop. 3.2 — so a fortiori none concentrating). This is the cleanest
statement of that result in the realism vocabulary, and it lets one assert
*both* grades at once — Gleason clears PR_lattice for L(H), PR_dual fails —
suppressing neither.

## The nesting PR_dual ⟹ PR_lattice is NOT free (the unique content)

The reverse inclusion does not hold for free, and this is the one piece of
mathematics specific to the realism framing (the survey does not treat it).
Restricting a dual measure μ̂ to the ⊥-stable clopens recovers s only as a
*finitely* orthoadditive state, whereas PR_lattice needs σ-additivity on
the lattice, s(⋁ₙaₙ) = Σₙ s(aₙ). The gap is μ̂(D) for

    D = h(⋁ₙ aₙ) \ ⋃ₙ h(aₙ),

and concentration on P(A) does **not** force μ̂(D) = 0: D contains
*principal* filters — e.g. ↑p with aₙ = span(eₙ) and p = span(v) for any
line not aligned with a basis vector (already v = e₁+e₂), so p ≤ ⋁ₙ aₙ = H
yet p ≰ aₙ for all n. (Confirmed against the
McDonald–Bimbó primary source: filters carry no σ-prime condition, and
P(A) consists of principal — not prime — filters; see
`notes/open_questions/verification/mb_primeness_check.md`.) So
PR_dual ⟹ PR_lattice requires an extra σ-continuity hypothesis (μ̂ null on
countable-join defects) that the finitary duality does not supply — the
same finitary wall that blocks the descent residue. Hence: a witnessed
one-directional **separation**, not a proven nesting.

In the Boolean case the two grades coincide (Stone gives μ̂
unconditionally; descent ⟺ σ-additivity), which is why Paper II could write
a single "PR".

## Does descent do independent work? (status of the third grade)

Every known PR_dual failure is an *extension* failure. In finite dimension
descent is vacuous (the only non-principal point is the improper filter,
already null by s(0) = 0; verified
`notes/open_questions/verification/pr_dual_inhabitation.py`, where PR_dual
on MO₂ collapses to the extension LP). Descent can be strictly weaker than
extension only in infinite dimension, where free non-principal filters can
carry mass — exactly where the duality is no longer rigorously *statable*
(MB finitary, no σ-Loomis–Sikorski).

So the open question (survey §5, §6) reads, in this vocabulary: *is there a
σ-OML regime in which descent is both statable and strictly weaker than
extension — a state that extends to a charge on S₀(A) but fails to
concentrate on P(A)?* The only candidate is the singular-state sliver, which
runs into the same statability wall. **Until such a witness exists,
PR_lattice/PR_dual is honest bookkeeping — a separation, not a new
theorem** (it would clear the new-vocabulary bar only with an
extends-but-does-not-concentrate witness).

**Sharper form of the statability wall (2026-06-04, from
[[meagre_vs_measure_check]]).** The reason descent is not statable is now
diagnosed precisely: in the Boolean case a realised point being
*countably-meet-closed* coincides with being *off the countable-join
defect* (Rao–Rao bridges them, so "σ-additive = vanishes on meagre sets").
In a non-distributive OML these split — a principal filter ↑p is always
meet-closed but need not be join-prime, so it sits inside the join-defect
D = h(⋁aₙ)∖⋃h(aₙ), and is topologically *isolated* in S₀(L(H)) (so D is
non-meagre, the reverse of the Boolean nowhere-dense case). Both the
category route (clopens mod meagre) and the measure route choke on this
same D; the category route is moreover just the MacNeille completion
(Harding-blocked). The precise remaining open sub-question:

> Is there an ideal I ⊆ CO(S₀(A)) with CO(S₀(A))/I a σ-complete OML
> isomorphic to the σ-completion of A? Any defect-killing I must kill
> D ⊇ {↑p}, but ↑p ∈ P(A) is the realisation datum — so a defect-killing
> ideal appears to destroy realisation. Strongly suggested impossible,
> NOT proved; making "destroys realisation ⟹ no representation" precise is
> the live sub-problem.

## Paper II decision — RESOLVED (fold in, 2026-06-05)

**Decision: fold the two-grade vocabulary into Paper II.** Confirmed
2026-06-05. The body now carries PR_lat/PR_dual end to end — abstract
(ll. 20–26), intro framing (§ "splits into two grades"), the
Commensurability theorem part (b) (the four-item EA / PR_lat / PR_dual /
VDR breakdown with the witnessed-separation `(∗)` arrow), and the
open-problems list (item 1, "negative for *every* state," singular case
folded in). The L(H) PR-claim correction was applied earlier (commit
514fc98); the two-grade fold-in is the chosen refinement over the bare
single-flip, and it is consistent throughout the body. No further
architecture decision is pending on Paper II.

## Cross-references

- Survey / problem statement: `notes/open_questions/oml_onboarding.{tex,md}`
- Archived predecessor (full audit trail): `notes/archive/oml_extension_problem_superseded.md`
- Paper II body: `papers/paper_ii/distributivity_and_realism_body.tex`
- Verification: `notes/open_questions/verification/mb_primeness_check.md`,
  `pr_dual_inhabitation.py`
- Memory: `oml_two_point_spaces.md` (the (A)/(B) point-space equivocation,
  also handled in the survey's Remark 5.1)
