# Fine-fibre rectangle repair

*Campaign 18, 2026-07-14. The first repairs beyond the stripped macro no-go.*

## 1. Exact full-grid join interval

Let `x={q0=0,r1=1}` and `y={q1=1,r0=0}` be the crossed pair in the
6,186,568-point full conditional grid.  Put `M=x union y`.  The intersection
of their two current minimal upper bounds differs from `M` on exactly two
coordinate macrofibres

\[
 A=(q_0,q_1,r_0,r_1)=(0,1,1,0),\qquad
 B=(1,0,0,1).
\]

Each has 336,400 points.  Therefore every possible concrete join in an
extension has the exact form

\[
 z=M\cup S_A\cup S_B,qquad S_A\subseteq A,quad S_B\subseteq B,
\]

with 672,800 genuinely free fine bits.  The four macro-saturated corner
choices are precisely those closed by Campaign 17.  Any
distributed-preserving completion must choose a proper nonempty subset in at
least one ambiguous fibre.  **Evidence class: hand proved from the exact
extrema.**

## 2. Activation-pair classes

Neither row can have activation triple `111` on `A` or `B`, since each row
then contains one activated edge with `q` unequal to `r`.  Partition either
ambiguous fibre by the two row activation triples.  There are consequently
`7*7=49` nonempty classes.  Their cardinalities are products of the four
corresponding single-cell state counts.  The unique smallest class has both
row triples equal to `110` and cardinality

\[
 2\cdot4\cdot4\cdot2=64.
\]

The two fibres have the same histogram.  The fibre-exchange-symmetric version
of the smallest choice therefore selects 128 optional points.  **Evidence
class: hand derived and executable counted.**

The 230-event signature quotient must not be treated as an exhaustive
fine-fibre quotient.  In fact the pulled-back cell events distinguish the
compatible local-state tuples.  A new event may split any old signature
class; a negative search on saturated classes would prove only a saturated
no-go.

## 3. Two minimal activation-class repairs

Among repairs formed from whole activation-pair classes, the smallest
one-sided choice takes `S_A` to be the 64-point `(110,110)` class and
`S_B=empty`.  Complement/disjoint-union closure grows from 230 to 310 events,
with increments

\[
4,4,20,12,10,10,5,5,4,4,0.
\]

It reconstructs neither `Bool(q0,q1)` nor `Bool(r0,r1)`, but remains a
nonlattice.  The inserted event is machine-certified as the unique join of
the original crossed pair after closure. Its first next cut has one maximal lower bound, two minimal upper
bounds, and an admissible interval with 940,900 free points.

For the smallest fibre-exchange-symmetric whole-class repair, select the two
corresponding 64-point classes in
`A` and `B`.  Closure has only 256 events, with increments

\[
4,4,12,4,0.
\]

It also reconstructs neither same-side Boolean boundary and remains a
nonlattice; again the inserted repair is the original pair's unique join. Its
first next cut has one maximal lower bound, two minimal upper
bounds, and 677,840 free points.  Exact masks are represented by hashes and
cardinalities in the executable receipt.  **Evidence class: exhaustive finite
evidence plus executable verified for these two stated repairs.**

For both variants, neither row activation cylinder becomes an event, no
nonzero completed event is supported within either cylinder, and every
nonzero event has an off-cylinder point. The doubly activated point relation
remains exactly `{0000,1111}`. These are executable-verified controls; centre
and maximal blocks are not asserted because both families are nonlattices.

Thus immediate fine-fibre saturation to a macro atom is refuted, as is
one-repair sufficiency.  The result is not an exhaustive search over the
`2^672800` first-join choices and is not a full OML construction.

## 4. Next gate

The symmetric branch is the smaller and more invariant skeleton.  Partition
its 677,840-point secondary interval by the exact activation/local-state
types preserved by its stabilizer.  Adjoin the smallest admissible invariant
selection, close again, and test:

1. both same-side macro boundaries remain absent;
2. neither row activation cylinder gains a nonzero supported event;
3. every nonzero event retains an off-cylinder point;
4. the next cut is classified exactly;
5. latticehood and centre are checked only at a terminal family.

Repeated forced reconstruction across structurally distinct fine branches
would support a fibre-saturation theorem.  A terminal centre-free OML pivots
immediately to overlapping rectangles and then the uncountable assembly.
