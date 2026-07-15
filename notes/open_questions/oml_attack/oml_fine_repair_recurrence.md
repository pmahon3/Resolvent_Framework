# Fine-repair recurrence and invariant audit

*Campaign 19, 2026-07-14. Structural classification after two fine repairs.*

## 1. What is actually monotone

For a chain obtained by adjoining events and taking complement/disjoint-union
closure, event membership is monotone.  Consequently the following failures,
once present, persist:

- a literal same-side truth atom, hence the full same-side Boolean algebra;
- a nonzero event supported inside a row activation cylinder;
- any particular higher-support or fine-fibre event;
- refinement of the carrier-point signature partition.

The point-state relation on the fixed designated events and concrete
point-state order separation are invariant because the carrier does not
change.  In contrast, gap size, number of failed pairs, minimal-upper-bound
counts, centre, maximal blocks, compatibility, pivot identity, and even the
continued leastness of a previously selected join are not monotone.  The
three observed sizes cannot by themselves define a recurrence.  **Evidence
class: hand proved and hostile audited.**

## 2. Exact third interval

Follow the symmetric 128-point first repair and the fixed four-point
`(111,110)` second repair.  Their 492-event closure has a first next interval
with 1,666,232 free carrier points.  Its coordinate-profile counts are:

| profile | points |
|---|---:|
| `0000` | 304,580 |
| `0001` | 111,360 |
| `0010` | 113,680 |
| `0011` | 42,240 |
| `0100` | 110,528 |
| `0101` | 111,360 |
| `0110` | 113,648 |
| `0111` | 116,400 |
| `1001` | 113,648 |
| `1011` | 110,528 |
| `1101` | 113,680 |
| `1111` | 304,580 |

Only four of the sixteen coordinate profiles are absent.  The interval
overlaps the first gap in 227,296 points and the second in 224,208; the first
two gaps are disjoint.  Hence the gap supports are neither nested nor
pairwise disjoint.  Activated freedom also migrates: the row-cylinder
intersection counts across the three gaps are

\[
(0,0),\quad(352,0),\quad(0,748).
\]

No decreasing-gap or monotone activated-mass argument survives.

## 3. Whole-class recurrence is refuted

The first gap is a union of two whole coordinate fibres.  The second is a
union of 105 whole activation/local-state Cartesian macrofibres.  The third
intersects 346 such macrofibres and contains **none** wholly.  Every one of
the 346 intersections is nevertheless a Cartesian factor subrectangle.
Thus the proposed recurrence whose repair atoms are whole factor classes is
refuted at depth three.

The unique smallest intersection has two points.  Its ambient class has four
points with:

\[
(q_0,q_1,r_0,r_1)=0111,qquad
(a_0,a_1)=(110,111),qquad
(2,2,1,1)\text{ local factors}.
\]

The gap retains a `2*1*1*1` subrectangle. In the local state enumeration it
fixes cell `(0,1)` to one of its two ambient states while leaving the two
states of cell `(0,0)` free. Relative to that two-state fibre, either `n1` or
`s1` selects the retained state (and `p15` or `t1` selects the excluded one),
so no unique literal is asserted. It is a one-local-literal subcylinder, not a
diagonal correlation. The 346 structural factor descriptors are distinct;
they are not asserted to be automorphism or event-signature orbits.
**Evidence class: executable verified census; local-literal interpretation
hand checked.**

The observed grammar is now

\[
\text{factor class plus finitely many local auxiliary literals},
\]

with minimum optional sizes `64,4,2` and literal widths `0,0,1`.  There is no
evidence that literal width stays bounded.  This is a sharpened construction
architecture, not an arbitrary-depth recurrence theorem.

## 4. Exact recurrence standard and next test

A genuine recurrence proof requires a normal-form descriptor determining
closure and cuts, a complete transition theorem over every repair orbit,
closure stability, exact fibre multiplicities, and either a finite transition
graph or a well-founded measure.  Matching one selected branch is
insufficient.

Row-arm symmetry identifies the secondary `011` and `101` four-point choices,
leaving `011` and the banked `110` as two orbit representatives.  The first
recurrence test is to compute the `011` child and compare its third interval
with the `110` census.  On the selected `110` branch, the smallest next
construction test is to adjoin the exact two-point local-literal subcylinder
as the third join and determine whether the fourth interval becomes a
singleton, creates an activation-supported event, reconstructs a side
boundary, or increases literal width again.

## 5. Third repair and fourth interval

Adjoin that exact two-point subrectangle to the forced lower bound of the
third cut. Complement/disjoint-union closure grows from 492 to 558 events in
rounds

\[
4,4,34,22,0.
\]

The selected event is the unique join of the third pair. Neither same-side
boundary is reconstructed, both activation cylinders remain absent, every
nonzero event has an off-cylinder point, and the activated diagonal remains
unchanged. The result is still a nonlattice.

The fourth interval now shrinks to 205,248 points. It intersects 116
activation/local-state macrofibres, every intersection is Cartesian, and 29
of them are whole. Its unique smallest class has four points at coordinate
profile `1000` and activations `(110,111)`, with ambient and selected factor
sizes both `(2,2,1,1)`. Thus the transition of repair units is

\[
\text{whole class}\to\text{proper one-literal subrectangle}
\to\text{whole class},
\]

while the gap sizes move

\[
672800\to677840\to1666232\to205248.
\]

This refutes monotone gap growth and a permanently increasing literal-width
model. It suggests a finite-state oscillation, but four points on one branch
do not prove recurrence. **Evidence class: executable verified for the one
selected three-repair chain, subject to the exact receipt scope.**

The secondary `011` orbit representative gives a separate warning: it closes
to 468 rather than 492 events, so it is not isomorphic to the `110` family,
yet its complete next-gap mask, all profile counts, the full 346-piece
Cartesian decomposition, factor histogram, and minimum one-literal
subrectangle coincide. Therefore even the complete gap subset is not a
complete Markov state; any recurrence descriptor must retain event-family or
provenance data. A hardened independent replay recomputes the global
four-point secondary minimum, both child closures, both complete gap hashes,
the complete decomposition digest, and the activation/escape controls.
**Evidence class: executable verified for these two children.**
