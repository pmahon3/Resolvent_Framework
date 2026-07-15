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

## 3. Conditional hull squeeze

**Lemma 3.1.** Suppose both `int_pi(j)` and `sat_pi(j)` are events and exactly
one of `A,B` is properly split by `j`. Then their nested event difference is
that entire ambiguous profile fibre. It is a literal same-side macro
cylinder, so the same-side forcing lemma reconstructs a forbidden Boolean
boundary.

Indeed, nested differences exist in every complement/disjoint-union-closed
family:

\[
 v\setminus u=(u\cup v^c)^c\qquad(u\subseteq v).
\]

If both ambiguous fibres are properly split, the hull difference is `A union
B`; this argument does not separate the two. **Hand proved** under the
displayed hull and one-split-fibre hypotheses.

The hull hypotheses are substantial. Fibre interiors and saturations need
not be events; the trace family on a fibre need not inherit global lattice
extrema; point-state order separation imposes no fibre invariance; and a
fibre permutation need not preserve the completed lattice. No unconditional
saturation theorem follows from concreteness or orthomodularity alone.

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
