# Non-profile fibre-splitter calculus

*Campaign 20, 2026-07-15. Exact escape from coordinate-closed reconstruction.*

## 1. Fibre hulls

Let `pi : Omega -> {0,1}^4` be the full-grid coordinate-profile map. For an
arbitrary subset `e` define

\[
 \operatorname{int}_\pi(e)=\bigcup\{F:F\text{ is a }\pi\text{-fibre},F\subseteq e\},
 \qquad
 \operatorname{sat}_\pi(e)=\bigcup\{F:F\cap e\ne\varnothing\}.
\]

These are subsets of the carrier, not automatically events.

For the displayed crossed pair

\[
 x=\{q_0=0,r_1=1\},\qquad y=\{q_1=1,r_0=0\},
\]

write `M=x union y` and let `W` be the intersection of all current upper
bounds. The exact extrema certificate gives

\[
 W\setminus M=A\mathbin{\dot\cup}B,
 \quad A=\pi^{-1}(0110),\quad B=\pi^{-1}(1001).
\]

Hence every join `j` of this pair in any same-carrier concrete extension has
the unique set normal form

\[
 j=M\mathbin{\dot\cup}S_A\mathbin{\dot\cup}S_B,
 \qquad S_A\subseteq A,\quad S_B\subseteq B.
\]

Its fibre interior contains an ambiguous fibre exactly when the corresponding
`S` is full, while its fibre saturation contains that fibre exactly when the
corresponding `S` is nonempty. **Hand proved.** The displayed extrema are
separately **Executable verified** by the full-grid certificate.

## 2. Necessary splitter theorem

**Theorem 2.1.** Every same-carrier concrete OML completion preserving both
distributed same-side boundaries has some profile-measurable failed pair
whose join properly splits at least one ambiguous profile fibre.

Otherwise every such join would be profile-measurable. The
coordinate-closed completion theorem would then descend the completion to
the exhaustive `P(16)` core and force a same-side Boolean reconstruction.
Thus the minimal escape is a binary colouring `empty != S != F` of a profile
fibre, retained by an event and its complement. **Hand proved.** The finite
core covering premise is separately **Executable verified**.

The verified 256-, 492-, and 558-event nonlattice stages demonstrate that
such splitters can survive complement/disjoint-union closure without
immediate reconstruction or activation support. They do not demonstrate a
terminal OML. **Executable verified** for exactly the stated stages.

## 3. Conditional hull extraction and correction

**Lemma 3.1.** Suppose both `int_pi(j)` and `sat_pi(j)` are events and exactly
one of `A,B` is properly split by `j`. Then their nested event difference is
that entire ambiguous profile fibre.

Indeed, nested differences exist in every complement/disjoint-union-closed
family:

\[
 v\setminus u=(u\cup v^c)^c\qquad(u\subseteq v).
\]

If both ambiguous fibres are properly split, the hull difference is `A union
B`; this argument does not separate the two. **Hand proved** under the
displayed hull and one-split-fibre hypotheses.

The formerly asserted next implication was false and is retracted: a whole
four-coordinate profile fibre is not a same-side literal macro cylinder.
The latter fixes only `q0,q1` and contains four profile fibres. On the
stripped core, adjoining any one profile singleton to the 82-word edge core
closes to 204 words and produces no nontrivial same-side-measurable word.
Thus Lemma 3.1 is an extraction lemma, not a boundary-reconstruction lemma.
**Executable verified** for all sixteen singleton profiles by the existing
independent word-closure audit
`notes/open_questions/verification/core16_single_profile_noncollapse.py`,
payload
`a85c5b89b0ceb5a1d0aa09cf6ca25ad1ac0e4fe3b7a060aa3eb1466ad0305415`.
Whether further lattice cuts from an
extracted profile fibre eventually force a side boundary is **Open**.

The hull hypotheses are substantial. Fibre interiors and saturations need
not be events; the trace family on a fibre need not inherit global lattice
extrema; point-state order separation imposes no fibre invariance; and a
fibre permutation need not preserve the completed lattice. No unconditional
saturation theorem follows from concreteness or orthomodularity alone, and
even their availability may yield only a four-coordinate fibre event.

## 4. Surviving architecture and next test

The surviving escape is an overlapping family of nontrivial partitions of
ambiguous fibres such that:

- the relevant fibre interiors and saturations remain unavailable;
- complements retain every split;
- differences of globally nested repair events never isolate a whole profile
  fibre;
- overlapping crossed joins glue consistently without reconstructing a
  same-side Boolean algebra;
- the completed family becomes a lattice without an activation-supported
  event.

The next falsifiable computation is the splitter-incidence graph of the
558-event branch: for each crossed-cut orbit representative, record the
ambiguous fibres it splits, whether either hull is already an event, and
whether two repair hulls are globally nested or orthogonal so that a
difference isolates a whole fibre. A positive isolation closes that branch;
a negative census supplies the first explicit compatible splitter graph.

## 5. Exact symmetry quotient

Let `G` be the group of carrier permutations preserving the 230-event base
family and the two gate families setwise. `G` acts on the unrestricted repair
tree, commutes with closure and admissible intervals, and preserves T-FIN.
Quotienting complete event families by `G` therefore gives a finite rooted
DAG whose terminal orbits decide T-FIN. The complete invariant is the
canonical coloured incidence/operation structure of the entire event
family, not its next gap.

Because the base events separate carrier points, `G` is equivalently the
automorphism group of the realized 230-coordinate point-signature code with
complement, disjoint-union, and gate colours. Named grid/cell symmetries give
only a subgroup until equality is executable-certified. The group-action and
quotient claims are **Hand proved**. Computational tractability is **Open**.

## 6. Stage-558 hull checkpoint

The discriminating census stops before a fourth repair. In the exact
558-event family there are 90 profile-measurable events and 127 unordered
join-failing pairs among those 90 events. This is not a census of every
lattice failure, meet failure, or symmetry orbit.

All three selected joins remain least at the final stage. The first has
neither fibre hull as an event. The second has its fibre interior but not its
saturation. The third has its interior, saturation, and hull difference as
events, while the whole join properly splits twelve profile fibres. Much of
that twelve-fibre pattern is inherited through its forced lower bound; the
two-point repair increment must be recorded separately.

Thus availability of both hulls does not by itself cause immediate
reconstruction: their difference may be a union of many whole profile fibres
rather than one literal macro cylinder. This does not refute Lemma 3.1,
whose one-split-fibre hypothesis fails, and it proves nothing about terminal
OMLs. It changes the next invariant from individual hull availability to
incidence among several hull gaps: nested or compatible differences must
progressively isolate one fibre.

**Executable verified:**
`notes/open_questions/verification/full_grid_stage558_splitter_incidence.py`
on the single certified 558-event branch; payload
`6b12e4a9ea7bafd4abc67e08dbc9a53ec6cd01487056f548d17e8f65a8aa39f5`.
The computation reuses the banked
carrier construction and is not an independent implementation.

**Hand proved:** the finite-family criterion used by the census: a pair has
a join exactly when the set intersection of all its current upper bounds is
itself an event.

**Open:** whether overlapping hull gaps in any terminal necessarily isolate
a same-side macro fibre or activation subset.

An independent implementation sharpens this checkpoint. Across all 558
events it finds seventeen distinct split-fibre signatures with 81
nonlaminar pairs. Exactly nine distinct nonempty hull gaps are themselves
events; one is the whole carrier. Among their 36 unordered pairs, exactly
eight are nested, every resulting event difference contains four whole
profile fibres, and no pair has one-fibre symmetric difference. No whole
profile fibre is an event, and no nonzero event is contained in a single
profile fibre. Thus laminar refinement and one-fibre hull isolation are both
refuted as stage invariants. **Executable verified** on this one nonlattice
stage by the partially independent audit
`notes/open_questions/verification/full_grid_stage558_hull_gap_isolation_audit.py`,
payload
`eeb79b8531ab80e44d8a8a091f8d2683d319b0526d944c4840af1acf3e644d62`.
The audit independently implements closure, order tables, failure and hull
censuses, but shares the defining carrier constructor and the three selected
repair descriptions.

The companion audit
`notes/open_questions/verification/full_grid_stage558_meet_witness_audit.py`
(payload
`4cd553be1d4cd5187c4afb36fc340a9bd573b147651bd5507897611a1446a55d`)
exposes a more informative provenance object. The sole
nonzero same-side literal-pair lattice meet at this stage is

\[
 q_0^\perp\wedge_L q_1,
\]

an event of 336,404 points equal to the entire 336,400-point `0101` profile
fibre disjoint-unioned with the four-point second repair selector. It is not
the literal set intersection of the two coordinates. It has four activated
row-0 points and many off-activation points, so neither reconstruction nor
gate `B` follows. This refutes the stage-level implication “nonzero
same-side literal meet implies its literal macro cylinder is an event.”
**Executable verified** on the exact 558-event stage. Persistence of this
exact equality in a terminal extension is **Open**, but its event core is
irreversible: in every extension, any new meet of the same two coordinates
must contain the old meet because the old event remains a lower bound.
**Hand proved.**

The next T-FIN object is therefore a *fattened-fibre meet*: a lattice meet
consisting of a whole profile fibre plus a finite repair escape. The
discriminating interval is above this meet and below the literal set
intersection (dually below the corresponding same-side join): classify
whether every terminal repair fills the four-fibre same-side cylinder or
stabilizes at a larger fattened-fibre meet. Killing or shrinking the meet is
impossible.

For this witness the literal same-side intersection has 1,355,680 points,
so the irreversible enlargement gap has 1,019,276 points. It consists of the
remaining 341,436 points of profile `0100` after removing the four-point
selector, together with the whole `0110` and `0111` fibres of 336,400 and
341,440 points. Every meet in a terminal extension lies set-theoretically in

\[
 e_*\ \subseteq\ q_0^\perp\wedge_{L_{\rm terminal}}q_1
 \ \subseteq\ \{q_0=0,q_1=1\}.
\]

This is a genuine provenance-sensitive monotone interval, but its raw
`2^1019276` subset space is another computational stop signal. Any next
computation must quotient candidate enlargements by a stated trace/provenance
rule rather than enumerate them.

**Theorem 6.1 (fattened-meet bifurcation).** In every same-carrier terminal
OML extending the 558-event family, either this meet equals the full
four-fibre cylinder `{q0=0,q1=1}`, in which case one same-side literal macro
atom is an event and the same-side forcing lemma reconstructs
`Bool(q0,q1)`; or the terminal contains a proper fattened-fibre meet `m`
satisfying

\[
 e_*\subseteq m\subsetneq\{q_0=0,q_1=1\}.
\]

**Hand proved.** This is an exact terminal bifurcation, but its second branch
is realizability architecture rather than a counterexample: latticehood,
the other same-side meets, centre, and later assembly gates remain **Open**.

## 7. Exact macrofibre interval normal form

The enlargement gap in Theorem 6.1 has a useful but sharply limited finite
coordinate description. Relative to the activation/local-state macrofibres
used by the full-grid producer, it is the disjoint union of exactly 160 whole
macrofibres and contains no partial macrofibre. Their four-coordinate profile
counts are

\[
 55\text{ in }0100,\qquad 49\text{ in }0110,\qquad
 56\text{ in }0111.
\]

The gap has 1,019,276 points and the smallest constituent macrofibre has four
points. **Executable verified** by
`notes/open_questions/verification/full_grid_stage558_fattened_meet_gap.py`
on the single exact stage-558 interval, payload
`680414ee42c5494ebccbdba213d92f71d39d344c5567ad8f6533ce875952552b`.
The verifier reconstructs the 558-event stage and recomputes the factor
decomposition, but it reuses the banked carrier/stage and factor-projection
modules and is therefore not an independent implementation.

**Lemma 7.1 (stage-558 macro-saturated candidates).** Let
`M_1,...,M_160` be those disjoint macrofibres. Every candidate enlargement
of `e_*` inside its literal cylinder which is saturated for this particular
macrofibre partition has the unique form

\[
 e_*\ \mathbin{\dot\cup}\!\bigcup_{i\in S}M_i,
 \qquad S\subseteq\{1,\ldots,160\}.
\]

Conversely every such expression is a set lying in the literal interval.
**Hand proved** from disjointness and exhaustion of the verified partition.
Eventhood, admissibility as a lattice meet, and preservation of the two gates
are not asserted.

This supplies an exact 160-bit grammar for one *macrofibre-saturated
interval*, not a repair grammar for future stages. Whether every terminal
meet is saturated for this partition is **Open**. Later non-profile repairs
may cut a macrofibre, and neither complement/disjoint-union closure nor the
current provenance calculus has been proved to exclude that possibility.
Accordingly arbitrary branching over `2^160` subsets is also suspended: a
next computation is discriminating only if it classifies partial splitters
or quotients the 160 bits by a proved gate-preserving provenance action.
