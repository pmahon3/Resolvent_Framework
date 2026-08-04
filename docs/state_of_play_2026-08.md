# State of play — August 2026

*Consolidated 2026-08-03. Verdicts below supersede the exploratory framing in
the week's individual audit notes. The sigma-essential paper and its
dependency path remain unchanged.*

## Methodological guardrail — three instances of one error

**REPEATED ERROR: SILENTLY WIDENING `regular`.** Three claims failed for the
same reason.

1. The Amemiya--Araki example was treated as a counterexample to
   completability. It is a counterexample only to **MacNeille/regular
   completability**; the underlying OML embeds in a complete OML after Hilbert
   completion.
2. Existence of some ambient algebra reconciling two legs was asserted to be
   equivalent to existence of a pasting diagram with regular site legs. The
   Stone-ultrafilter amalgam proves the first; an order argument rules out the
   second.
3. The clopen inclusion was claimed to be non-sigma-regular exactly when the
   Boolean algebra is infinite. The finite--cofinite algebra on an uncountable
   set refutes this: regularity tests only joins that **already exist**. A
   countable family of singletons there has no least clopen upper bound, so it
   supplies no regularity test.

Every future claim in this area must say which of **arbitrary embedding**,
**sigma-regular embedding**, and **regular embedding** it uses. Existence of an
ambient join, preservation of an existing countable join, and preservation of
all existing joins and meets are three different assertions.

## Closed

### Completion and site-regularity thread

**DETOUR — CLOSED.** Acyclicity is not necessary for orthomodular completion.
The Loop Lemma as stated by Greechie (1971) and Kalmbach (1983) allows
arbitrary Boolean blocks, not only finite ones. The five-cycle paste of
infinite finite--cofinite blocks is an OML, and pasting their powerset
completions over the same four-element sites gives a complete OML. The
proposed acyclicity obstruction is therefore **REFUTED**.

Campaign 11's puncture-meet disagreement has two distinct verdicts.

- For ordinary Boolean embeddings it is an **ARTIFACT — FALSIFIER FIRED**.
  The two puncture legs have a strong amalgam in a complete powerset Boolean
  algebra, and the common decreasing family has one ambient meet without
  identifying the nonzero singleton with zero.
- For regular or sigma-homomorphic embeddings it is **IMPOSSIBLE**. The site
  meet is forced to be zero while one leg's meet is the nonzero singleton, so
  no common realization can preserve both existing countable meets.

The asserted equivalence between “some reconciling ambient exists” and “a
regular pasting diagram exists” is **REFUTED**.

### Two local checks

**BLOCKWISE SIGMA-ADDITIVITY — VERIFIED, IN STRONGER FORM.** For a concrete
`DynkinSystem`, every countable orthogonal family is a pairwise-compatible
family and extends by Zorn to an `IsMaxBlock`. Its set union lies both in the
carrier and in that maximal block. It is the join in both orders: any upper
bound in either family contains every member and hence contains their union.
Thus the block join and carrier join agree. The same argument proves for an
arbitrary probability state that it is sigma-additive iff every maximal-block
restriction is sigma-additive; the existing theorem
`isSigmaOn_carrier_iff_maxBlocks` is the exact two-valued formal instance. This
part does not need `MeetsExist`; that hypothesis is needed to identify the
`IsMaxBlock` families as genuine maximal Boolean sigma-fields. Consequently
the first filtration gap can be nonempty, but it has **no local--global
coherence content** on these carriers: every sigma-additivity failure already
occurs inside one block.

**DISPERSION-FREE PULLBACK — VERIFIED; NO NEW MORPHISM DEFECT.** If a state
$s$ takes values in $\{0,1\}$, then $s\circ\phi$ takes values in
$\{0,1\}$ along every OMP embedding $\phi$. A non-sigma-regular embedding may
still destroy the sigma-additivity of the pullback, but that is exactly the
first gap again.
There is no additional morphism condition whose failure accounts for the
passage from sigma-additive states to dispersion-free states. The filtration
therefore contains one lift defect and one algebraic non-defect; it is not one
coherence notion repeated twice.

### `FinitelyCoherent` gate and resolution

**PHASE 2 GATE — NON-TRIVIAL; PASSED.** `FinitelyCoherent` is carrier-relative,
but the Phase B loss is not merely a failure to transport a definition. Adding
$D_0=A\cap B$ forces carrier events $D_1=A\setminus D_0$ and
$D_2=B\setminus D_0$ and the disjoint decompositions

\[
 A=D_0\sqcup D_1,\qquad B=D_0\sqcup D_2,\qquad C=D_1\sqcup D_2.
\]

Finite additivity makes `mu(A)=mu(B)=mu(C)=1` impossible. This is a new,
explicit constraint on every extension of the old local data.

**ANTITONICITY — PROVED FOR FIXED-DATA SAME-BASE REFINEMENTS.** If
`Carrier d` is contained in `Carrier e` on the same `Omega`, and the same
local event-value trace is retained, every finitely additive or sigma-additive
state on `e` restricts to one on `d`. Hence refinement cannot create
coherence; coarsening can create it. The pre-registered falsifier is impossible
at this scope. Apparent reversals obtained by changing the local pattern or
re-indexing recomputed maximal blocks compare different predicates.

This is the whole mechanism. There is no general resolution theory to open.
The induced maximal-block atlases are not canonically functorial under carrier
inclusion: a coarse block can have several fine maximal extensions, and
previously distinct blocks can merge after missing intersections are added.
The restriction theorem remains valid because `glueBlockStates` in
`BoundaryDescent.lean` turns an overlap-compatible family into a global state
before restriction.

## Established

### Pullback defect

**LEMMA R — VERIFIED FOLKLORE, IN EQUALITY FORM.** For an orthogonal family
`(x_n)` in `P`, an OMP embedding `phi:P -> Q`, and a sigma-additive ambient
state `s`, put

\[
 x=\bigvee_n\phi(x_n),\qquad
 y=\phi\!\left(\bigvee_nx_n\right),\qquad
 g=(x\vee y')'.
\]

Whenever the image join exists, $x\le y$, the OMP orthomodular law gives
$y=x\vee g$ with $x\perp g$, and

\[
 s\!\left(\phi\!\left(\bigvee_nx_n\right)\right)
   =\sum_n s(\phi(x_n))+s(g).
\]

Thus the pullback defect at this family is exactly `s(g)`. Preservation of
countable orthogonal joins makes `g=0`; full sigma-regularity is sufficient but
stronger than needed. The packaging is **FOLKLORE — NOT NOVEL**.

### Boolean converse

**VERIFIED FOR EVERY FINITELY ADDITIVE BOOLEAN STATE.** By Fremlin 416Q, every
finitely additive state on a Boolean algebra is the pullback of a
sigma-additive Radon/Baire measure on its Stone space. Fremlin 313C identifies
an existing countable join with the closure of the union of the corresponding
clopens. The exact defect is the measure of the topological gap between that
union and its closure. This is a converse at Boolean scope only; it is not an
OMP dilation theorem.

### Concrete OML carriers

**VERIFIED.** Under `MeetsExist`, the corpus's `IsMaxBlock` objects are genuine
maximal Boolean blocks: concrete compatibility is lattice compatibility, and
each block is closed under complement, intersection, and arbitrary countable
union. Each block and each `overlapMeasurableSpace` is therefore a sigma-field.

Every `DynkinSystem` already has joins of countable orthogonal families, given
by set union. With `MeetsExist` it is an OML, and Holland's theorem upgrades
countable orthocompleteness to countable completeness. Hence each such carrier
is automatically a sigma-complete OML. Harding--Wang Problem 2 has no
independent content for these carriers, whether read OMP-to-OMP or, under
`MeetsExist`, OML-to-OML. The Ulam carrier's remaining issue is lattice
envelopment, not missing countable orthogonal joins.

### Quarantine mechanism

**MECHANISM IDENTIFIED; OMP-SCOPE INFERENCE REFUTED.** Parts (ii)--(iii) of
quarantine use the Boolean compactness/premeasure engine on clopen Boolean
algebras: a countable disjoint clopen cover of a clopen set is effectively
finite, and Horn--Tarski first extends a subalgebra charge to that clopen
algebra. They do not act on arbitrary OMP states. The gap between quarantine
and D is one named ingredient: extension of the OMP state to a Boolean charge
or other premeasure domain.

## Parked adjacent questions

### C′ — regular sites and MacNeille completion

**OPEN — ADJACENT — NOT OURS — PARKED.** C′ asks whether an OML pasting
whose sites are regular in every incident block has an orthomodular MacNeille
completion. The comparison class is Pulmannová--Riečanová's atomic
block-finite theorem and the Bruns--Greechie--Harding--Roddy result for
varieties generated by a finite OML. The week supplied neither a proof nor a
counterexample. Do not weaken the hypothesis or reopen the completion thread
without a new mechanism.

### D — sigma-additive state dilation

**PARTIALLY ANSWERED; GENERAL CASE OPEN — ADJACENT — PARKED.** Navara--Pták--
Rogalewicz (1988), Theorem 2.2, gives a state-specific finitely additive rigid
enlargement, but not a sigma-complete carrier with a sigma-additive state.
Boolean, finite, several operator-algebraic, and individual spatial regimes
are positive. The arbitrary OMP case remains adjacent to the open
Harding--Wang completion problem. It is not a dependency of the
sigma-essential paper, and the present evidence does not justify a
months-scale commitment.

## Corpus audit

**NO UNSCOPED COHERENCE THEOREM FOUND.** The sigma-essential statements fix the
carrier `L`/`d`; `FinitelyCoherent` contains that carrier in its type. The
`BoundaryDescent` theorems quantify over `IsMaxBlock d` for a fixed `d`. The
reconstruction results fix their protocol and window family, and the spine's
two-gap ladder names its two concrete witnesses. No existing theorem needs a
resolution hypothesis added. Only informal robustness prose had widened its
scope; W2 already retracted that prose.
