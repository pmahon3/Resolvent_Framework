# Fine-repair termination and the terminal dichotomy

*Campaign 19, 2026-07-15. Correction of the putative infinite-repair frontier.*

## 1. Fixed-carrier setup

Let `Omega` be the fixed compatible-state carrier of the full conditional
`K22` grid, with `|Omega| = 6,186,568`, and let `E0` be its verified
230-event complement/disjoint-union closure. A closed family is a subfamily
of `P(Omega)` containing `0,1` and closed under complement and finite
disjoint union.

For a failed join pair `x,y` in a closed family `E`, put

\[
  I_E(x,y)=\left[x\cup y,
  \bigcap\{u\in E:x\subseteq u,\ y\subseteq u\}\right].
\]

The upper endpoint may equivalently be computed from the current minimal
upper bounds. A fine-repair step selects any `z in I_E(x,y)` and replaces
`E` by the least closed family containing `E,z`. Meet failures are treated
by complementation. This definition includes all syntactically admissible
repairs; it is not restricted to Cartesian, macro-saturated, or minimum-size
choices.

## 2. Fixed-carrier termination theorem

**Theorem 2.1.** Every strict fine-repair chain on this fixed carrier is
finite. Every maximal chain in the **unrestricted** repair tree terminates at a finite concrete OML containing
`E0`. Countable orthogonal closure adds no events at any stage.

**Proof.** If `x,y` have no join in `E`, no member of `I_E(x,y)` belongs to
`E`: such a member would be an `E`-upper bound below every `E`-upper bound,
hence the missing join. The interval is nonempty because the literal set
union `x union y` belongs to it, whether or not it is currently an event.
Thus every step strictly enlarges the event family. Since `P(Omega)` is a
finite set, a strict chain of its subfamilies is finite.

A repair-terminal node in the unrestricted tree cannot have a failed cut,
because the preceding interval supplies another repair. Hence its terminal
family is a lattice. Every
complement/disjoint-union-closed lattice of sets is orthomodular: for
`x subseteq y`, the event `y setminus x = (x union y^c)^c` exists and gives
the orthomodular identity. Finally, a disjoint family of subsets of finite
`Omega` has only finitely many nonempty members, so countable orthogonal
closure is already finite disjoint-union closure. QED.

This kills the proposed alternative of an infinite strictly widening
nonlattice process on the fixed carrier. A transfinite presentation is only
an eventually constant repetition of a finite chain. It says nothing about
repairs on a growing or infinite carrier. A node maximal only inside a
boundary-preserving or otherwise pruned subtree can still be a nonlattice.
**Hand proved.** A separate hostile review found no defect at this scope.

## 3. Completion-search completeness

**Theorem 3.1.** If `F` is any concrete OML with
`E0 subseteq F subseteq P(Omega)`, then some maximal fine-repair chain has a
terminal family `T subseteq F`. Conversely, every terminal family is a
finite concrete OML completion of `E0`.

**Proof.** At a failed cut of `E subseteq F`, choose `z=x join_F y`. It lies
above the literal union and below every current `E`-upper bound, hence in
`I_E(x,y)`. It is not already in `E`, and closing under complement and
disjoint union stays inside `F`. Theorem 2.1 makes the recursion terminate.
The converse is the terminal part of Theorem 2.1. QED.

Thus complete interval branching is logically exhaustive for same-carrier
completions even though direct enumeration is infeasible: the root alone has
`2^672800` syntactic candidates before symmetry. **Hand proved.** A separate
hostile review found no defect at this scope. This cofinality transfers only
upward-monotone properties; it does not transfer trivial centre, an exact
block atlas, or `Phi` from a terminal subfamily to every containing
completion.

## 4. Exact finite theorem of record

Define two upward-absorbing gates:

- `A`: the family contains an entire literal macro cylinder of `Bool(q0,q1)` or
  `Bool(r0,r1)`;
- `B`: the family contains a nonzero event contained in either row
  activation cylinder.

One entire literal same-side macro cylinder forces the other three by complements and
orthogonal differences, so `A` is equivalent to reconstructing one full
same-side Boolean algebra. A proper fine subset of such a cylinder does not
trigger this lemma.

> **T-FIN (terminal dichotomy; open).** Every maximal chain in the unrestricted fine-repair tree on
> the fixed full-grid carrier terminates at a concrete OML satisfying `A` or
> `B`.

If T-FIN is proved, Theorem 3.1 closes every distributed-preserving
same-carrier completion of this grid. If it is refuted, the refuting terminal
is itself a finite, concrete, sigma-complete OML preserving both distributed
boundaries and activation escape. It is then an exact finite cell for the
overlapping-rectangle and uncountable-assembly campaigns, not by itself a
counterexample to `Phi`.

T-FIN is decidable but not presently computationally tractable. The verified
chain

\[
  230\longrightarrow256\longrightarrow492\longrightarrow558
\]

refutes monotonicity of gap size and repair width, while the `468/492`
sibling pair refutes completeness of even the full next-gap descriptor. It
does not decide T-FIN.

## 5. Where sigma-closure actually re-enters

**Lemma 5.1 (sigma interpolation).** If a concrete event family on an
arbitrary carrier is closed under complement and countable disjoint union,
then it is closed under countable decreasing intersections and countable
increasing unions.

For `e_1 superseteq e_2 superseteq ...`, the differences
`e_n setminus e_{n+1}` and `e_1^c` are pairwise disjoint events, and

\[
 \bigcap_n e_n=
 \left(e_1^c\mathbin{\dot\cup}
 \mathop{\dot\bigcup}_n(e_n\setminus e_{n+1})\right)^c.
\]

Consequently, if countably many events decrease exactly to a nonempty subset
of an activation cylinder, sigma-closure creates a `B` event. Equivalently,
a distributed-preserving infinite assembly must prevent a countable disjoint
event cover of the entire off-cylinder locus. Unbounded local-literal width
alone does not imply such isolation. **Hand proved.**

On an infinite carrier this interpolation lemma supplies no termination
theorem. Least closure under countable orthogonal unions may require
transfinite iteration (in general through stages below `omega_1`), and
sigma-closing a union of live stages may itself create a forbidden macro
cylinder. No Zorn or finite-carrier termination argument is imported here.

## 6. Scope correction and next action

The fixed-carrier theorem does not rule out representations on a larger
carrier. Restriction of larger-carrier points gives a map to `Omega`, but
the saturated shadows of a lattice need not form a lattice, and a
larger-carrier activation-supported event need not be saturated. Therefore a
same-carrier proof of T-FIN would close only this representation class.

The best next finite action is to compute the exact automorphism group of
the 230-event full family and use it to seek a structural T-FIN invariant.
The cheapest discriminating computation is a splitter-incidence audit across
structurally distinct crossed cuts, simultaneously monitoring all earlier
selected joins for loss of leastness. A fourth selected-depth repair is not
justified unless it tests a stated provenance invariant. Do not search for an
infinite or periodic repair chain on this carrier.

## 7. Strategic decision checkpoint

The campaign has reached **stop signal E: computational exhaustion**.
This is a theorem-extraction boundary, not a claim that T-FIN is true.

| Monitoring question | Answer | Evidence |
|---|---|---|
| New structural pattern? | Yes: a same-side lattice meet is a whole profile fibre plus a four-point repair escape, while hull signatures are strongly nonlaminar. | **Executable verified** on the selected 230→256→492→558 chain. |
| Genuinely new or relabelled? | The 468/492 sibling closures are genuinely nonisomorphic, yet have the identical complete next gap. | **Executable verified** for the two siblings. |
| Finite grammar rule? | One exact interval has a 160-bit normal form for macrofibre-saturated candidates. No transition theorem shows later interpolants remain saturated. | Decomposition **Executable verified**; conditional normal form **Hand proved**; terminal grammar **Open**. |
| Candidate well-founded invariant? | Existing same-side meet cores can only grow in extensions; the 336,404-point fattened core is irreversible. Whether this growth forces the full cylinder is unknown. | Core monotonicity **Hand proved**; forcing conclusion **Open**. |
| Collapse unavoidable? | Only for coordinate-closed completions. One-split-fibre hull extraction does not force a side boundary; nonlaminar hulls and a fattened same-side meet survive at stage 558. | Coordinate theorem **Hand proved**; singleton-profile noncollapse and stage control **Executable verified**; unconditional T-FIN **Open**. |
| Evidence of infinite coherent grammar? | No: an infinite strict chain on this carrier is impossible. | **Hand proved**. |
| Would arbitrary branching discriminate live hypotheses? | No: the root has `2^672800` candidates, the fattened interval has `2^1019276` unrestricted subsets, and the available descriptor is non-Markov. | Counts **Executable verified**; strategic conclusion **Hand proved** from search scope. |

### Gate table

| Gate | Current status | Evidence | Remaining obligation |
|---|---|---|---|
| Repair grammar | Necessary residue signature; bare-square collapse refuted; PJH is a sufficient hull grammar | Identities/PJH **Hand proved**; controls **Executable verified** | Prove certificate-local PJH or classify its first nonevent hull |
| Latticehood | 558-event selected stage is a nonlattice; unrestricted terminals exist abstractly | Stage **Executable verified**; termination **Hand proved** | Exhibit and audit a gate-avoiding terminal or prove all terminals hit A/B |
| Orthomodularity | Automatic for every complement/disjoint-union-closed terminal lattice | **Hand proved** | Applies only after latticehood |
| Same-side boundary preservation | Preserved through three selected repairs | **Executable verified**, one chain only | Prove preservation at a terminal or prove reconstruction unavoidable |
| Activation-event avoidance | Preserved through three selected repairs | **Executable verified**, one chain only | Prove preservation at a terminal or prove gate B unavoidable |
| Trivial centre | Not meaningful as a monotone nonterminal invariant | **Hand proved** | Compute only for a terminal candidate |
| State order separation | Point states separate the fixed concrete set family at every stage | **Hand proved** for concreteness; finite checks **Executable verified** | Classify all states only if a terminal candidate survives |
| `Phi` tameness or obstruction | Undecided; every finite terminal is itself `Phi`-tame | **Hand proved** (finite additivity equals sigma-additivity on finite OMLs) | Use a surviving terminal only as an assembly cell; it cannot itself refute `Phi` |
| Infinite-limit viability | Impossible on the fixed carrier; larger-carrier assembly remains open | Fixed carrier **Hand proved**; larger carrier **Open** | Prove coherent embeddings and sigma gates only after a scalable terminal architecture exists |
| Universal normalization | None from arbitrary `Phi` failure to this rectangle architecture | **Open** | Required before local collapse could prove the full conjecture |

### Selected route: inconclusive theorem extraction

The narrowest unresolved question is T-FIN, now sharpened to the
fattened-fibre interval: can a terminal extension keep a nonzero same-side
meet equal to a whole profile fibre plus finite repair escape without
assembling the four-fibre same-side macro cylinder? The meet core cannot
shrink in an extension. That interval is now certified as 160 whole
macrofibres, but this partitions only its macrofibre-saturated subclass. The
smallest discriminating question is whether a forced next repair cuts one of
those pieces. This directly tests the proposed grammar, whereas enumerating
either the `2^160` saturated class or another arbitrary minimum-depth repair
would not distinguish T-FIN from the surviving partial-splitter architecture.
