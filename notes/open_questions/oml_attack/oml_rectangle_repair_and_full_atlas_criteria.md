# Rectangle repair and full-atlas criteria

*Campaign 16, 2026-07-14. Necessary repairs for grouped outputs and exact
state/MBRC gates.*

## 1. Rectangle-repair theorem

Let `L` be a concrete OML whose two-valued states determine order. Suppose it
contains the four edge Boolean algebras `Bool(q_a,r_i)`, `a,i<2`, and that the
projection of its state space to `(q0,q1,r0,r1)` contains all sixteen profiles.
Put

\[
 x=q_0'\wedge r_0',\quad y=q_1'\wedge r_1',\quad
 U=(q_1\wedge r_0)',\quad V=(q_0\wedge r_1)'.
\]

Then `x,y<=U,V`, while `U,V` are incomparable, witnessed by profiles `0011`
and `1100`. Hence `x join y` cannot equal either edge-local bound: every OML
completion contains a genuinely rectangle-supported repair event `z` with

\[
 \operatorname{supp}(x)\cup\operatorname{supp}(y)
 \subseteq\operatorname{supp}(z)
 \subseteq\operatorname{supp}(U)\cap\operatorname{supp}(V).
\]

On the sixteen coordinate profiles, only `0011,1100` are undecided, leaving
four possible repair traces. For every edge there are two profiles agreeing
on that edge, one forced into and one forced out of `z`; thus `z` belongs to
none of the edge algebras. Full off-activation freedom in the conditional
cell supplies the sixteen-profile hypothesis, so auxiliary gadgets cannot
remove the rectangle cut. They can only select one of its four traces through
their finer state fibres. **Evidence class: hand proved.**

Adjoining the literal set union in the stripped core does not by itself yield
a lattice; scratch evidence shows a repair cascade. No sufficiency or
minimality theorem is claimed.

## 2. Spatial-carrier prohibition

In a concrete sigma-complete OML of subsets, every carrier point defines a
sigma-additive two-valued state, since countable orthogonal joins are disjoint
set unions. Therefore the intended nonprincipal finitely additive puncture
witness must not be inserted into the concrete fibre carrier: doing so would
turn it into a forbidden global activated sigma-state. The infinite carrier
may contain only intended sigma points and off-cylinder escape points; the fa
witness must be abstract/nonspatial. **Evidence class: hand proved.**

## 3. Nonspatial fa compactness theorem

Let `p` be the fixed activation pattern in a proposed sigma-completion `L`.
Assume every finite set of events lies in a countable-index sub-OML admitting
a two-valued state that realizes `p`. Introduce one Boolean variable per event
and impose the finitary equations for zero, one, complement, and binary
orthogonal additivity, together with the literals of `p`. Every finite set of
equations is satisfiable in one countable sub-OML, so propositional compactness
gives a global finitely additive two-valued state realizing `p`.

Thus countable-support localization plus activated solvability supplies the
fa witness without adding a carrier point. **Evidence class: hand proved,
using propositional compactness.**

## 4. Completion-independent no-gain

If every conditional cell embeds faithfully as an OML sublogic, restriction
of any global two-valued state is a cell state. Hence an activated global state
satisfies every intended edge equality, regardless of completion-created
blocks. No-gain is automatic; the difficult MBRC direction is no-loss and
compatible selection over actual blocks. **Evidence class: hand proved.**

## 5. Defect-footprint criterion

Let `H` be the declared hub-point space and let the boundary projection send a
block state to its transported hub trace. For every actual maximal block `B`
define

\[
 D(B)=\{x:\operatorname{eval}_x\text{ has no intended L-relative sigma lift
 to }B\}.
\]

A sufficient CSS/noGS criterion is:

1. **atlas anchoring/completeness:** every compatible global section projects
   under the declared boundary map
   to one hub evaluation `eval_x`, and each component is an intended
   `L`-relative sigma lift of that same evaluation;
2. coherent lifts `v_{B,x}` exist whenever `x notin D(B)`, and satisfy
   `v_{B,x}|_{B intersection C}=v_{C,x}|_{B intersection C}` whenever both
   sides are defined;
3. every countable family `J` of actual maximal blocks leaves
   `H minus union_{B in J}D(B)` nonempty;
4. the union of `D(B)` over all actual maximal blocks is `H`;
5. for every `x`, a corresponding actual block is L-relative-normal enough to
   forbid a sigma lift of `eval_x`.

Here an intended `L`-relative sigma lift means a two-valued state on the
Boolean block which is countably additive for those countable orthogonal
joins whose join in `L` remains in the block, and which agrees with the hub
trace on the declared boundary. Without the anchoring/completeness clause,
covering `H` rules out only sections already parametrized by hub points and
does not exclude an unrelated compatible global section.

Then every countable block subsystem has a compatible section but the full
atlas has none. Event-support locality alone does not imply this criterion: a
single maximal block may contain uncountably many finite- or countably-
supported events. **Evidence class: conditional hand theorem.**


## 6. Additional infinite gates

Order separation requires an off-cylinder countable-cover exclusion theorem:
no countable orthogonal family of mixed events may cover the entire off-
activation locus, or the complement of its sigma-join becomes a nonzero
activation-supported event. The nonprincipal fa state must also extend over
all rectangle and sigma repairs. These gates are open.
