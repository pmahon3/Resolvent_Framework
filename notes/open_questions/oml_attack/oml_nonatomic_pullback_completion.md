# Completion of the `(5,11)` non-atomic pullback

*Opened and completed for the explicit pullback-carrier class 2026-07-12.
Starting commit: `61d1aae743a4a7e159a3b8a37815c6c91031df43`.
Outcome B: centre-free, nonrectangular, single-edge, and `Phi`-tame under
the stated common-point extension hypothesis.  A single edge without that
hypothesis is not proved tame.*

## 1. Statement of record and scope

The conjecture is unchanged:

> Every concrete σ-complete non-Boolean essentially irreducible OML
> satisfies the σ-lifting property `Phi`.

The construction below proves neither the conjecture nor its negation.  It
does prove that the first non-atomic finite architecture survives literal
mixed completion as a centre-free one-edge pullback.  Its finite relation is
nonrectangular and nonfunctional, but the explicit infinite coordinate model
is tame by common-point replacement.  Finite computations are not used to
infer infinite σ-completeness.

## 2. Automorphisms and the 42-pair census

The atomistic 56-event skeleton has 128 automorphisms.  They are enumerated
as permutations of the twelve lattice atoms preserving the complete family
of atom supports; this gives a certified generating family (indeed the full
group) and its induced action on every event.

The 42 qualifying unordered pairs form six orbits, not one:

| Pair orbit | Representative | Orbit size | Common blocks | Meet orbit representative | Support-cycle type | Priority |
|---|---:|---:|---:|---:|---|---|
| O1 | `(5,11)` | 4 | 1 | `1=q0` | 7-cycle; supports `4+4`, overlap 1 | primary |
| O2 | `(5,51)` | 8 | 2 | `1=q0` | 5-cycle; supports `4+3`, overlap 2 | separate control |
| O3 | `(15,45)` | 4 | 2 | `5` | 4-cycle; supports `3+3`, overlap 2 | separate control |
| O4 | `(15,47)` | 16 | 1 | `7` | 4-cycle; supports `3+2`, overlap 1 | separate control |
| O5 | `(15,54)` | 2 | 1 | `14` | 5-cycle; supports `3+3`, overlap 1 | separate control |
| O6 | `(21,52)` | 8 | 1 | `18` | 3-cycle; supports `2+2`, overlap 1 | separate control |

Thus `(5,11)` represents exactly four pairs:

`{(5,11),(5,44),(11,50),(44,50)}`.

The orbit invariants in the executable receipt additionally record interval
sizes, carrier-region cardinalities, generated sub-OML size, and the full
member list.  The earlier 861-pair classification remains banked unchanged.

## 3. Intrinsic pair and seven-block placement

Put

\[
 e=q_0\vee q_1=5,\qquad f=q_0\vee q_2=11,
\]

and, inside the unique common maximal block `B`,

\[
 d=e\wedge f=q_0,\quad a=e\wedge f^\perp=q_1,\quad
 c=e^\perp\wedge f=q_2,\quad r=(e\vee f)^\perp=q_3.
\]

The intervals `[0,d]`, `[0,a]`, and `[0,c]` have two elements.  The
intervals `[0,e]` and `[0,f]` have six elements and are `MO2`, not Boolean
atom intervals.  This is why the construction must refine the four Boolean
regions rather than substitute below `e,f` as though they were atoms.

The propagation atlas is

| Datum | Blocks containing it |
|---|---|
| `d=q0` | `B,D0,D1` |
| `a=q1` | `B,D0,D3` |
| `c=q2` | `B,D1,D2` |
| `e` | `B,D0,D2,Ca` |
| `f` | `B,D1,D3,Cb` |

The substitution diagram `A superset D subset C` sits in `B`.  Its shared
pullback atoms propagate through `B,D0,D1`; `A`-private information propagates
through the `q1` side, and `C`-private information through the `q2` side.

## 4. Literal finite `4-2-4` carrier

Let the atom maps be

\[
 \rho_A,\rho_C:\{0,1,2,3\}\longrightarrow\{0,1\},\qquad
 \rho(0)=\rho(1)=0,\quad\rho(2)=\rho(3)=1.
\]

Over each of the four old carrier points in `q0`, use the eight compatible
pairs `(u,v)` with `rho_A(u)=rho_C(v)`.  Over `q1` use four `A` copies, over
`q2` four `C` copies, and over `q3` one copy.  Retaining the old internal
four-point multiplicity gives 68 carrier points.

Lift every skeleton event by inverse image.  In `B`, adjoin the four `A`
coordinate events and four `C` coordinate events.  The resulting mixed
Boolean block has 17 atoms:

\[
 8\ (q_0\text{-pullback})+4\ (q_1\text{-private})+
 4\ (q_2\text{-private})+1\ (q_3).
\]

The raw family has 131,112 events.  It is complement closed but not closed
under mixed disjoint unions.

## 5. Full mixed completion

Canonical complement/disjoint-union closure stabilizes after adding the
forced propagation events.  It has exactly 147,592 events and is the union
of these seven Boolean blocks:

| Block | Finite quotient block | Fibre data visible | Events | Overlap role | New/original |
|---|---|---|---:|---|---|
| `B` | `B` | full `A`, full `C`, and their `D` agreement | `2^17` | unique mixed block | inflated original |
| `D0` | `D0` | full `A`; full pullback atoms on `q0` | `2^14` | `A/D` propagation | inflated original |
| `D1` | `D1` | full `C`; full pullback atoms on `q0` | `2^14` | `C/D` propagation | inflated original |
| `D2` | `D2` | `C` private restriction only | `2^7` | finite/one-sided | inflated original |
| `Ca` | `Ca` | finite quotient only | `2^4` | finite | original size |
| `D3` | `D3` | `A` private restriction only | `2^7` | finite/one-sided | inflated original |
| `Cb` | `Cb` | finite quotient only | `2^4` | finite | original size |

No eighth maximal block is forced.  The executable maximality test computes,
for each displayed block, every completed event compatible with all its
atoms; the compatibility envelope is exactly that block.  The seven blocks
cover the completion, and the finite shape quotient excludes a maximal
clique crossing their seven compatibility types.

### Lattice and orthomodularity certificate

For Boolean blocks `M,N`, many event pairs have the same set intersection.
The audit enumerates every *distinct* intersection arising from every one of
the 28 unordered block pairs.  For a subset `S` of the carrier, the union of
the largest events from each of the seven blocks contained in `S` is the
only possible greatest lower bound.  Every enumerated intersection has this
lower envelope in the completed family.  Hence all event pairs have meets;
complements give all joins.

The family is a concrete Dynkin system.  If `x subset y`, closure under
complement and disjoint union puts `y minus x` in the family, so `x,y` are
compatible.  Latticehood therefore gives
`y=x join (y meet x^perp)`: the completion is an OML.

This is an exhaustive finite certificate, not a sample of generator pairs.

## 6. Boundaries, centre, and quotient

Every completed block is generated by its intersections with the other six;
the boundary sizes equal the block sizes in the table.  The literal
intersection of all seven exhaustive blocks has two events:

\[
 Z(L_{4,2,4})=\{0,1\}.
\]

Thus the finite completion is centre-free.  The old quotient shapes and all
seven named blocks survive.  Centre-freeness is computed from the completed
atlas, not inferred from the 56-event quotient.

## 7. Completed relation graph

On the face `e=f=1`, a `B` atom must lie in `q0`.  Its endpoint labels are
exactly

\[
 R=\{(u,v):\rho_A(u)=\rho_C(v)\}
   =\operatorname{Ult}(A)\times_{\operatorname{Ult}(D)}
     \operatorname{Ult}(C).
\]

It has eight pairs.  Every left and right vertex has degree two.  Carrier
point evaluation extends every one of the eight local choices to a global
two-valued state, so no further completed block removes a pair.

Only `B` contains both full endpoint algebras.  `D0` contains full `A` but
not full `C`; `D1` contains full `C` but not full `A`.  The other four see
only private restrictions or finite quotient data.  Consequently the
completed coarse graph has one edge

\[
 A\longleftrightarrow_D C.
\]

The other overlap equations repeat restrictions already implied by this
edge.  They are redundant, not a second quotient edge.  There is no cycle
transport and no monodromy.

## 8. Controls

The receipt constructs balanced finite quotient maps for endpoint atom
counts in `{2,3,4}` and common atom counts one and two.  The `4-2-4` control
has eight pairs.  With a one-atom common algebra the relation is rectangular.
If one endpoint restriction is bijective, the relation is functional in the
corresponding direction.  With `A=C=D`, equality reduces the two labels to
one coordinate; if that same algebra is propagated through every maximal
block it is a central common factor, as in the banked common-base theorem.

These controls distinguish nonfunctionality, nonrectangularity, coordinate
collapse, and central propagation.

## 9. Single-pullback tameness: exact theorem

The graph shape alone is not sufficient.  Write `St_sigma(A) -> St_sigma(D)`
and `St_sigma(C) -> St_sigma(D)` for restriction.

**Single-edge extension theorem.**  Let `p` be a finite coherent two-valued
pattern with a finitely additive witness `(u,v)` agreeing on `D`.  Suppose
there is a σ-additive state `w` on `D` and σ-additive endpoint states
`u_sigma,v_sigma` such that:

1. `u_sigma|D=w=v_sigma|D`;
2. `u_sigma` preserves every `A` requirement of `p`; and
3. `v_sigma` preserves every `C` requirement of `p`.

Then the single-edge compatibility system has a σ-additive replacement
preserving `p`.  If the remaining atlas equations factor through these
endpoint restrictions and finite skeleton data, compatible block-state
gluing gives a global σ-state.

The proof is exactly the displayed choice followed by compatible gluing.
The content is the endpoint extension hypothesis; it must not be omitted.
Separate extendibility to `A` and `C` is insufficient unless the two
extensions can be chosen over one `w`.

### Point version

For carrier maps `X_A -> X_D <- X_C`, a sufficient hypothesis is the
finite common-point extension property:

> every pair of finite oriented endpoint traces with a common realizable
> `D` trace has realizers `x_A,x_C` with the same base point.

Then evaluation at `(x_A,x_C)` supplies the replacement.  Agreement of
Stone ultrafilter restrictions does not by itself imply that such carrier
points exist; state-space, carrier-point, and σ-state pullbacks remain
distinct notions.

An abstract one-edge network can already fail without this hypothesis.  In
the Cantor trace cube `{0,1}^N`, let the left eligible restriction image be
the eventually-zero sequences and the right image the eventually-one
sequences.  They are disjoint and dense.  For every finite coordinate set
one can choose a left and right sequence agreeing there, but no pair agrees
on every coordinate.  Thus `single pullback => tame` is false as a relation-
graph theorem without an extension/compactness/properness hypothesis.  This
trace-space example is not claimed to be a concrete σ-complete OML.

## 10. Infinite coordinate model

Take disjoint index sets `I_D,I_A,I_C`.  Let `D` be the
countable-coordinate σ-field on `2^{I_D}`, and let `A,C` be the analogous
fields on `2^{I_D union I_A}` and `2^{I_D union I_C}`.  Use the literal
carrier pullback, canonically `2^{I_D union I_A union I_C}`.

The seven finite block shapes above extend parametrically:

- `B` is the direct sum of the joint pullback σ-field on `q0`, an `A`
  private region, a `C` private region, and the finite complement;
- `D0,D1` carry the shared pullback part and the appropriate endpoint;
- `D2,D3` carry the indicated one-sided private restriction; and
- `Ca,Cb` remain finite.

Blockwise complements and countable disjoint unions preserve these seven
shapes.  Cross-block extrema use the same finite quotient shape as the
finite certificate, with Boolean extrema inside the visible σ-fields.
Hence their union is a concrete σ-complete OML with these seven maximal
blocks and trivial centre.  This is the arbitrary-base shape theorem; the
finite event count is not its proof.

For countable-coordinate fields, finite endpoint conjunctions have
projections depending on only countably many shared coordinates and hence
belong to `D`.  If a common `D` ultrafilter charges both projections, their
intersection is nonempty; choose one base point and compatible points in
the two fibres.  Therefore the finite common-point extension property holds,
and every coherent finite face is repaired by a point state.

The face `e=f=1` exposes the joint countable-coordinate σ-state slice.  As
in the banked one-fibre model, point/σ-ultrafilter states are dense and the
eligible locus is nonclosed and noncompact in the full Stone space.  The
slice is genuinely nonrectangular at the endpoint-restriction level, but
the common-point argument repairs every finite face.  No global selection
failure occurs.

## 11. Eventwise satisfiability and full selection

Order finite compatibility requirements by inclusion.  Given a finite
fragment and a global finitely additive witness, conjoin its oriented events
inside each endpoint.  Project the endpoint conjunctions to the shared
countable-coordinate field, choose a point in the charged intersection, and
then choose endpoint fibre points.  Retain the finite skeleton choice and
evaluate all seven blocks at the resulting compatible coordinates.

This constructs a σ-solution for every finite fragment.  The same argument
uses all events named by the finite face at once and produces a complete
compatible σ-state, so there is no escaping net with empty inverse limit.
In particular `C_p intersect St_sigma(L)` is nonempty for every coherent
finite face `p` in this model.

## 12. Executable and formal receipts

Run:

```sh
python3 notes/open_questions/verification/seven_block_nonatomic_pullback_audit.py \
  --verify-dynkin-closure \
  --output notes/open_questions/verification/seven_block_nonatomic_pullback_schema.json
python3 notes/open_questions/verification/verify_seven_block_nonatomic_pullback_schema.py
cd formalization/QuerySystem && lake build
```

The producer certifies the automorphism orbits, controls, carrier and event
counts, all distinct block-pair intersections, latticehood, orthomodularity,
block envelopes, boundaries, centre, and relation graph.  The verifier
independently recomputes the orbit action and checks the stable completion
counts and invariants.

No new Lean theorem is added.  `BoundaryDescent.finite_trace_dirac` already
certifies finite point replacement within one concrete block;
`independent_finite_traces_dirac` certifies the rectangular two-endpoint
step; and `glueBlockStates` certifies gluing once compatibility is supplied.
The new load-bearing step is the common-point extension property, which is
a hypothesis in the general theorem and an elementary projection argument
for the explicit coordinate model.  Formalizing only the conditional
choice-and-glue statement would restate its hypothesis and would not certify
the infinite seven-shape construction.  No `sorry` or new axiom is introduced.

## 13. Status table

| Claim | Scope | Status | Consequence |
|---|---|---|---|
| 42 qualifying pairs split into known automorphism orbits | finite skeleton | complete: six | census scope fixed |
| `(5,11)` represents its full orbit | chosen pair | proved; orbit size four | valid reduction only within O1 |
| `A-D-C` substitution is well-defined | literal pullback carrier | proved | concrete candidate |
| Mixed closure stabilizes | finite `4-2-4` control | proved: 147,592 events | admissible finite completion |
| Completed family is an OML | finite control | proved/exhaustive | lattice validity |
| σ-completeness holds | explicit arbitrary-base seven-shape class | proved at hand level | infinite candidate valid |
| All maximal blocks are classified | finite and shape class | complete: seven | centre calculation valid |
| Centre is trivial | completed candidate | proved | centre-free |
| Completed relation graph has one edge | completed candidate | proved | single pullback |
| Relation is nonrectangular and nonfunctional | `4-2-4` face | proved | genuine coupling |
| Finite face exposes noncompact slice | countable-coordinate model | proved at hand level | topology survives |
| Single-pullback tameness holds | common σ-extension/common-point class | proved | conditional hierarchy |
| Completion creates second quotient edge | candidate | no | no monodromy |
| Every finite compatibility fragment has σ-solution | coordinate candidate | proved constructively | FIP |
| No complete σ-selection exists | coordinate candidate | refuted | `Phi` preserved |
| Seven-block skeleton remains viable | completed analysis | yes, but tame here | seek multi-edge data |

## 14. Strategic outcome and next handoff

This is **Outcome B — nonrectangular but tame pullback inflation**.  The
`(5,11)` pullback survives full completion, remains centre-free, and creates
no second quotient edge.  Its explicit noncompact coordinate realization
satisfies `Phi`.  It therefore preserves, rather than threatens,
`Psi_OML`.

The single best next task is to leave the one-edge class: test a representative
from a different pair orbit whose completion can place the same two endpoint
coordinates in two common blocks with inequivalent shared quotients.  The
target datum must exhibit two restriction maps before any noncompact fibre
is introduced; redundant copies of the present `D` edge do not count.
