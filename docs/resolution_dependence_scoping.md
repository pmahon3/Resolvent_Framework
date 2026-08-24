# Resolution dependence: scoping memo

*2026-08-03. Phase 2 returned non-trivial, so the gated check ran. Hand proof;
no Lean or paper-of-record changes.*

## Verdict

**ANTITONICITY — PROVED, AT THE ONLY COMPARABLE SCOPE.** Fix the underlying
set `Omega`, retain the same local event-value data supported on the coarser
carrier, and compare two `DynkinSystem Omega` carriers by inclusion. A
refinement can only destroy finite or sigma coherence; a coarsening can only
create it. “Can” here is one-way permission, not strictness at every step.

The result is an elementary restriction theorem, not a new research
direction. A broader claim about arbitrary “block resolutions” is not a
well-formed invariant until the local data and the comparison of blocks are
specified.

## The concrete operations

**Resolution.** A carrier resolution is the actual event family
`Carrier d = {A | d.Has A}` of a `DynkinSystem Omega`, together with its
induced maximal compatible families `IsMaxBlock d M`. If `MeetsExist d`, each
such `M` is a maximal Boolean sigma-field, and two blocks `M,C` have the site
$M\cap C$ packaged by `IsMaxBlock.overlapMeasurableSpace`.

**Refinement.** A same-base refinement `d <= e` means

```
forall A, d.Has A -> e.Has A.
```

The corpus's concrete instances are `L_1 <= L+`, adjoining $A\cap B$ and
closing as a Dynkin system; `L_1 <= sigma(L_1)`; and the terminal inclusion
into `P(Omega)`. A compatible family in `d` remains compatible in `e`, so each
coarse maximal block extends by Zorn to at least one fine maximal block. The
extension is generally non-unique, and two coarse blocks can lie in one fine
block after a missing intersection is adjoined.

**Coarsening.** The reverse operation discards events while retaining a
Dynkin system. W2's comparison `CC(S) <= P(S)` is the unit example: the
countable/co-countable sigma-field is the coarser resolution, and removing
events removes sigma-additivity/ultrafilter obligations.

**Boundary descent.** At a fixed resolution, `CompatibleBlockStates` in
`BoundaryDescent.lean` asks block states to agree on every event in each actual
overlap. `glueBlockStates` then produces one global sigma-state. Conversely,
one global sigma-state restricts to a compatible state on every maximal block.
This lets comparisons be made through global states even though maximal
blocks themselves have no canonical refinement map.

## Falsifier first

The named falsifier was a refinement that creates coherence for unchanged
local data. It cannot occur.

Let `d <= e`. Restrict a finitely additive state on `e` by keeping its value
function on `Carrier d`. Normalization, complement additivity, and disjoint
pair additivity remain true because every old event and every old operation is
still present. The same restriction works for a sigma-additive state: every
old countable disjoint family is also a family in `e`, and its union is the
same set. Agreement with a fixed local trace is unchanged. Therefore

\[
 \operatorname{Coh}_e(s_0)\Longrightarrow
 \operatorname{Coh}_d(s_0),
 \qquad
 \operatorname{SigmaExt}_e(s_0)\Longrightarrow
 \operatorname{SigmaExt}_d(s_0).
\]

For a `BoundaryDescent` presentation, first glue a hypothetical compatible
fine family, then restrict the resulting global state, then restrict it to
the coarse maximal blocks. Thus block merging cannot furnish a falsifier.

An apparent example can arise only by changing the local pattern, forgetting
old values, or choosing unrelated maximal-block indices after recomputation.
That compares different extension problems and does not refute antitonicity.

## Strictness and the Phase B gate

Phase B is a strict refinement step. `FinitelyCoherent` on `L_1` is witnessed
by `mState`. In `L+`, the adjoined event $D_0=A\cap B$ forces `D_1,D_2` and

\[
 A=D_0\sqcup D_1,\quad B=D_0\sqcup D_2,\quad C=D_1\sqcup D_2.
\]

No finitely additive two-valued state can assign one to `A,B,C`. This is a
new constraint, not a mere change of type.

W2 supplies the sigma-side strictness mechanism in the same direction. On its
audited set of size `2^{omega_1}`, the coarse sigma-field `CC(S)` carries the
nonprincipal co-countable sigma-state, while the fine powerset asks the state
to decide all uncountable splits and admits no nonprincipal sigma-state.
Coarseness creates the state by removing obligations. W2's robustness
retraction is therefore exactly a too-coarse-base error at this scope.
Nonprincipality itself is representation-relative and is not asserted to be
antitone; W2 is evidence of strict enlargement of the coarse sigma-state
space, not a second restriction theorem.

## Canonical resolution and stabilization

For a fixed concrete base `Omega`, `P(Omega)` is the canonical terminal event
refinement. For a finite local two-valued pattern, coherence there is exactly
the nonempty-kernel test: a kernel point gives a Dirac extension, and the
Boolean baseline gives the converse. In this limited sense the terminal
resolution is the strictest test, and once coherence fails it remains false
under every further refinement.

This is not a canonical resolution of an abstract OMP or of its block atlas.
It depends on the chosen concrete representation, collapses all events into
one Boolean block, need not preserve old blocks as maximal, and is not the
regular/MacNeille completion sought in C′. No representation-invariant
canonical block resolution is present in the corpus. Nor does antitonicity
imply that a verdict becomes constant before the terminal carrier along an
arbitrary refinement chain.

## Corpus disposition

**CORPUS-INTERNAL AND CLOSED at fixed-data same-base scope.** The mechanism is
state restriction, already implicit in the carrier-indexed definitions and
in `BoundaryDescent`. There is no theorem-sized antitonicity programme to
open. A canonical admissible resolution for abstract OMPs would be adjacent
completion theory and is not pursued here.

No existing corpus theorem states a coherence conclusion without fixing its
resolution. The sigma-essential theorems name `L`/`d`; the block-gluing
theorems use `IsMaxBlock d`; reconstruction fixes the protocol; and the
spine's ladder names the carrier/protocol of each witness. No theorem needs a
new hypothesis. W2's already-retracted robustness prose was the only located
scope failure.
