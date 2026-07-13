# Two-fibre monodromy in the centre-free seven-block OML

**Non-atomic follow-up:** [`oml_nonatomic_pullback_completion.md`](oml_nonatomic_pullback_completion.md)
constructs the `(5,11)` pullback completion; it retains one quotient edge
and has no monodromy.
The subsequent [`oml_two_edge_pullback_completion.md`](oml_two_edge_pullback_completion.md)
audit shows that both two-common-block selector orbits repeat one embedded
four-region datum and likewise do not define monodromy.

*Opened 2026-07-12. Starting commit:
`422478fbf2a377bc6552329ce7bc9fd8ef120adf` (`Construct tame distributed
OML interval inflation`). Status: Outcome C for distinct lattice-atom
interval substitutions; the broader partial-interface/nonspatial class is
open. The banked one-fibre construction is unchanged.*

## 1. Statement of record

The conjecture remains:

> Every concrete σ-complete non-Boolean essentially irreducible OML
> satisfies the finite-trace σ-lifting property `Phi`.

The one-fibre result already proves that centre-freeness plus a
face-exposed noncompact eligible local σ-state slice does not imply failure
of `Phi`. This note tests the first literal two-fibre class. It finds two
coherent fibres and a block-graph cycle, but proves that the actual overlap
relation is rectangular. No counterexample to `Phi` or
`Psi_OML` is claimed.

## 2. Certified skeleton and selector orbits

The certificate `../verification/seven_block_skeleton.json` describes the
56-event OML `L*` with maximal blocks

\[
 B,D0,D1,D2,Ca,D3,Cb.
\]

The Hasse diagram has 128 automorphisms and twelve lattice atoms in two
orbits. Events are the stable certificate IDs.

| Orbit | Selector events | Propagation supports |
|---|---|---|
| 0 | `1,4,10,40` | three blocks, always including `B` |
| 1 | `2,3,6,8,16,22,28,34` | two blocks |

More explicitly:

| Event | Mask | Support blocks |
|---:|---:|---|
| `1=q0` | `0x000f` | `B,D0,D1` |
| `2` | `0x0033` | `D2,Ca` |
| `3` | `0x00cc` | `D2,Ca` |
| `4` | `0x00f0` | `B,D0,D3` |
| `6` | `0x0505` | `D3,Cb` |
| `8` | `0x0a0a` | `D3,Cb` |
| `10` | `0x0f00` | `B,D1,D2` |
| `16,34` | `0x3300,0xcc00` | `D0,Ca` |
| `22,28` | `0x5050,0xa0a0` | `D1,Cb` |
| `40` | `0xf000` | `B,D2,D3` |

The machine-readable derivation is
`../verification/seven_block_two_fibre_cycle_audit.py`, with stable receipt
`../verification/seven_block_two_fibre_cycle_schema.json`.

## 3. The smallest jointly coherent crossed pair

Two selectors are jointly coherent when a two-valued skeleton state charges
both. On the certified concrete carrier this is witnessed by a carrier point
in both event masks. Relative to `q0`, the only distinct coherent atoms are

\[
 2,3,6,8.
\]

All four lie in orbit 1. The stable smallest pair is therefore

\[
 (q,r)=(1,2),\qquad
 \operatorname{supp}(q)=\{B,D0,D1\},\quad
 \operatorname{supp}(r)=\{D2,Ca\}.
\]

The supports are non-nested but disjoint. They lie on the five-cycle

\[
 B-Ca-D0-D1-D2-B.
\]

Thus they are crossed in the weighted block-incidence graph. They do **not**
form a fibre-compatibility cycle: no maximal block contains both selector
intervals. The pair `(1,6)` is the symmetric alternative, on
`B-Cb-D1-D0-D3-B`.

This distinction is decisive. A cycle in the block graph is not a cycle of
coordinate transport unless overlap equations carry one fibre into the
other.

## 4. Atom-support separation theorem

**Theorem (jointly coherent atom supports separate).** In `L*`, every
distinct lattice atom jointly chargeable with `q0` has propagation support
disjoint from `supp(q0)`. Consequently no jointly coherent distinct
atom-selector pair is visible in one maximal block.

*Proof.* The exhaustive Hasse automorphism and block-atom incidence
calculation gives the table above. Direct mask intersection leaves exactly
events `2,3,6,8`; their supports are respectively `D2,Ca` and `D3,Cb`, all
disjoint from `B,D0,D1`. The certificate checks both assertions. ∎

There is also an intrinsic short reason for the last implication. If two
distinct lattice atoms occur as atoms of one Boolean block, they are
orthogonal, so no two-valued state can charge both. Therefore any coherent
distinct atom pair must avoid common support blocks. The exhaustive part is
the classification of which disjoint-support pair is smallest and where it
sits in the seven-block incidence.

## 5. Two-fibre substitution datum

Let `A` and `C` be distinct concrete Boolean σ-algebras. Replace `[0,q]` by
`A` and `[0,r]` by `C`. In the concrete carrier realization, a skeleton
valuation lying below only one selector acquires the corresponding fibre
coordinate; a valuation lying in the set-theoretic intersection of the two
selector masks acquires both coordinates. Old skeleton events are inverse
images under the carrier projection.

Mixed closure propagates `A` through exactly `B,D0,D1` and `C` through
exactly `D2,Ca`. The expected blocks are

\[
 A\oplus2^3\quad(B,D0,D1),
 \qquad C\oplus2^3\quad(D2,Ca),
 \qquad 2^4\quad(D3,Cb).
\]

No block contains both a proper `A`-event and a proper `C`-event. Their
set-theoretic intersections on the enlarged carrier do not become OML
meets; as in the finite skeleton, incompatible concrete events may overlap
as subsets while their greatest lower bound in the event family is zero.

## 6. Mixed closure, maximal blocks, and centre

**Two independent atom-interval inflation theorem (hand level).** For any
concrete Boolean σ-algebras `A,C`, the seven displayed block union is a
concrete σ-complete OML. Its maximal blocks are exactly those seven blocks,
its centre is `{0,1}`, and every overlap-generated boundary saturates its
block.

The proof is the two-coordinate version of the banked one-interval shape
argument.

1. Each selector is an atom in exactly its support blocks, so substitution
   gives the displayed Boolean σ-fields.
2. Since the supports are disjoint, every block shape mentions at most one
   fibre. In a mixed disjoint family the `A`-parts and `C`-parts therefore
   close independently, while the finite outside shape is governed by the
   certified skeleton disjoint-union table.
3. Binary extrema use the corresponding Boolean extrema inside one support.
   Across supports, proper fibre events have the same zero/top extremal
   behaviour as their skeleton selectors. The finite skeleton meet/join
   table therefore supplies unique extrema and the orthomodular law.
4. Compatibility yields precisely the five inflated and two finite blocks;
   no block can combine the two fibres.
5. Any proper `A`- or `C`-event is absent from at least one finite/crossed
   block. The common intersection of the seven exhaustive blocks is the
   lift of the skeleton centre, hence `{0,1}`.
6. The original overlap generators still generate every finite part, and
   same-support neighbours share the full new interval. Boundaries remain
   saturated.

As for the one-fibre theorem, the arbitrary-base statement is a symbolic
hand proof. The finite audits below support but do not replace the
σ-completeness argument.

## 7. Finite approximants

`../verification/seven_block_two_fibre_inflation_audit.py` seeds the
`A`-fibre in `B` and the `C`-fibre in `D2`, computes canonical complement and
disjoint-union closure, all binary extrema, orthomodularity, maximal Boolean
blocks, centre, boundaries, global two-valued states, and the induced fibre
relation. Its receipt is
`../verification/seven_block_two_fibre_inflation_schema.json`.

| `(A atoms,C atoms)` | Raw | Closed | Block sizes | Global 2-states | `|R_n|` |
|---:|---:|---:|---|---:|---:|
| `(2,2)` | 88 | 112 | `16^2,32^5` | 26 | 4 |
| `(2,3)` | 120 | 160 | `16^2,32^3,64^2` | 32 | 6 |
| `(3,2)` | 120 | 176 | `16^2,32^2,64^3` | 32 | 6 |
| `(3,3)` | 152 | 224 | `16^2,64^5` | 40 | 9 |

Every case has exactly the expected seven maximal blocks, trivial centre,
saturated boundaries, and all OML closure checks. The raw family is
complement-closed but not disjoint-union closed; one closure round supplies
exactly the predicted propagated intervals.

## 8. Actual overlap relation and factorization

On the coherent face `q=r=1`, a global finitely additive state selects an
ultrafilter `u` of `A`, an ultrafilter `v` of `C`, and a finite skeleton state
charging both selectors. Since no overlap event mentions both coordinates,
there is no equation relating `u` and `v`. Hence

\[
 R=\operatorname{Ult}(A)\times\operatorname{Ult}(C).
\]

In every finite approximant the enumerated relation is the full rectangle:
its size is `|A atoms| |C atoms|`. The global state system factors as

\[
 \operatorname{Ult}(A)\times\operatorname{Ult}(C)
 \times S_{\mathrm{fin}},
\]

with the finite skeleton coordinate restricted only by the chosen face.
Thus the candidate fails the mandatory nonfactorization gate.

## 9. Monodromy

Transport along the displayed five-cycle is intrinsic only where an overlap
carries a fibre event. Along the `q` portion it preserves `u`; along the `r`
portion it preserves `v`; the intervening overlaps carry only finite
skeleton data. There is no map `Ult(A) -> Ult(C)` or converse. On the product
coordinate the only honest composite is

\[
 h(u,v)=(u,v).
\]

Therefore `Fix_fa(h)` and `Fix_sigma(h)` are just the corresponding full
product loci. Monodromy is trivial. Calling the five-cycle itself a
nontrivial monodromy would confuse incidence with an overlap-induced state
map.

## 10. Finite compatibility and complete σ-selection

Let a finite coherent pattern be realized by a global finitely additive
two-valued state.

If it charges a selector, only finitely many events in that fibre occur in
the pattern. Orient them by the selected ultrafilter; their Boolean
conjunction is a nonempty concrete event. Choose a carrier point in it and
replace the ultrafilter by point evaluation. Do this independently for `A`
and `C`. If a selector is killed, all events below it are killed and no
repair is needed. Retain the finite skeleton state.

The two point replacements agree automatically on every overlap because no
overlap compares the coordinates. They produce a compatible global
σ-additive state with the same finite trace. The Lean theorem
`BoundaryDescent.independent_finite_traces_dirac` certifies the simultaneous
two-block finite-trace step; `glueBlockStates` certifies compatible gluing.

Consequently every finite compatibility fragment has a σ-solution, but so
does the complete system. On `q=r=1`, choose any carrier points of `A` and
`C` together with any skeleton carrier valuation in the concrete
intersection of the selector masks. There is no escaping net with empty
inverse limit.

## 11. Reusable factorization theorem

**Independent-coordinate tameness.** Consider a finite-skeleton inflation
whose complete overlap equations split into finitely many Boolean fibre
coordinates and a finite skeleton state, with no equation mentioning two
distinct fibre coordinates. Then every coherent finite face σ-lifts.

*Proof.* A finitely additive witness fixes the finite skeleton state and one
ultrafilter in each charged fibre. A finite face names finitely many events
in each of finitely many coordinates. Apply finite-trace point replacement
coordinatewise, retain the skeleton state, and glue. ∎

This closes rectangular multi-fibre and tree-like classes in which deleting
finite skeleton variables disconnects all coarse coordinates. The statement
does not apply to a genuine correspondence `R` or to a cycle whose overlaps
identify proper subalgebras across coordinates.

## 12. Spatial transport control

The exact safe statement is:

**Spatial fixed-point tameness.** If the eligible σ-state locus is preserved
by every cycle transport and, inside each relevant finite clopen face, the
eventwise fixed-point equations have the finite-intersection property in a
compact eligible σ-state locus, then a σ-fixed point exists.

This is the compact local-selection theorem applied to the graph of the
transport equations. It covers finite-order coordinate permutations on a
compact point-realization quotient, homeomorphisms of compact carriers when
that quotient exhausts the eligible σ-state locus, and any explicitly
compact invariant σ-state class. A stronger conclusion from the word
“spatial” alone is not justified: noncompact point loci can lose their limit
in the Stone extension.

The simplest proposed `P(N)` shift does not even pass the finitely additive
fixed-state gate. Translation swaps the even and odd events, so a fixed
ultrafilter would have to charge an event and its complement equally. More
generally an actual permutation with no fixed points admits a finite proper
colouring of its orbit graph; if the colour classes belong to the fibre
algebra, invariance of an ultrafilter forces two disjoint colours into it.
Thus no invariant-ultrafilter claim is used here.

| Fibre algebra | Transport | Finitely additive fixed states | σ-fixed states | Verdict |
|---|---|---|---|---|
| finite `P(n)` | coordinate permutation | supported on fixed atoms | same | tame control |
| `P(N)` | successor shift | none (parity) | none | fails coherence gate |
| `P(N)` | fixed-point-free permutation with measurable finite colouring | none | none | fails coherence gate |
| countable-coordinate field | finite-order coordinate permutation | constant carrier points are fixed | point fixed states exist | no finite-face separation established |
| compact eligible σ-locus | continuous invariant transport plus eventwise FIP | irrelevant | fixed point by compactness | tame theorem |

Partial embeddings, quotient relations, finite-to-one noninvertible maps, and
nonfunctional correspondences remain outside this control result.

## 13. No-go theorem and residual class

**Two-fibre atom-substitution no-go.** Every two-fibre inflation of `L*`
obtained by replacing two distinct jointly chargeable lattice atoms by
independent Boolean intervals has disjoint propagation supports. Its raw
overlap relation is rectangular, its monodromy is trivial, and—whenever the
displayed shape completion is used—it satisfies `Phi` by independent point
replacement.

This is Outcome C for the smallest literal substitution class. It does not
say that every conceivable two-fibre completion of the skeleton is tame.
A successful construction must leave the atom-interval class. The smallest
residual relation class is:

> inflate non-atomic selector intervals or proper shared subalgebras so that
> a completed maximal block contains events from both coordinates and
> induces a genuine partial-isomorphism/correspondence, while no common
> fibre enters every block.

Such a construction must recompute mixed closure and maximal blocks from
scratch. Abstractly declaring a relation on ultrafilters is not enough.

## 14. Required status table

| Claim | Scope | Status | Consequence |
|---|---|---|---|
| Selector pair is jointly coherent | `(q0,2)` | proved/executable | face accessible |
| Supports form a genuine cycle | block incidence | proved: five-cycle; refuted as fibre-transport cycle | incidence alone insufficient |
| Two-fibre inflation closes as an OML | independent atom intervals | proved at hand level; finite exhaustive | admissible tame class |
| σ-completeness holds | arbitrary concrete `A,C` shape theorem | proved at hand level | infinite validity in stated class |
| Centre remains trivial | completed candidate | proved from exhaustive block family | irreducible |
| Fibre relation is nonrectangular | candidate | refuted | factorization |
| Monodromy is nontrivial | candidate | refuted | identity product |
| Finitely additive fixed state exists | face `q=r=1` | proved | coherence |
| Every finite compatibility fragment has σ-solution | candidate | proved; finite-trace step formalized | FIP |
| No global σ-fixed solution exists | candidate | refuted | no GSD obstruction |
| Spatial twists are always tame | unrestricted spatial class | open; compact/FIP subclass proved | residual noncompact spatial class |
| Independent multi-fibre coordinates are tame | finite-skeleton rectangular class | proved; two-coordinate trace formalized | classification |
| `Psi_OML` threatened or preserved | full candidate | preserved | no counterexample |

## 15. Strategic outcome and next handoff

**Outcome C — two-fibre no-go theorem for atom selectors.** The smallest
jointly coherent crossed pair is `(q0,2)`. Its supports occupy a genuine
five-cycle in the block graph, and the two-fibre completion remains a
centre-free seven-block concrete σ-complete OML. Nevertheless actual
overlaps impose no cross-coordinate equation. The relation is the full
product, monodromy is identity, and simultaneous point replacement proves
`Phi`.

The single best next task is to classify non-atomic skeleton selector events
and proper subalgebra embeddings by the maximal blocks in which their
interval data can appear, then test the smallest jointly coherent pair for
a completion-created block that sees both fibres. The target relation should
first be a partial Boolean isomorphism; graph-of-an-isomorphism is retained
only as a control because it reduces to one coordinate.

**2026-07-12 residual-pair update.** The finite classification is now
complete in `oml_nonatomic_pair_classification.md`. Of 861 unordered
non-atomic pairs, 42 pass the stated coherence, support, common-block,
cycle, and noncentral-shared-fibre gates. The stable smallest pair is
`(5,11)=(q0∨q1,q0∨q2)`, with common block `B` and shared meet `q0`. Proper
shared-subalgebra substitutions target the genuinely partial relation
`Ult(A) ×_{Ult(D)} Ult(C)`. Completed coarse substitution remains open and
must be audited from scratch.

## 16. Validation receipt

Passed on 2026-07-12:

```sh
python3 notes/open_questions/verification/seven_block_skeleton_data.py \
  --output notes/open_questions/verification/seven_block_skeleton.json
python3 notes/open_questions/verification/three_block_interface_audit.py
python3 notes/open_questions/verification/three_block_completion_audit.py
python3 notes/open_questions/verification/distributed_trap_audit.py
python3 notes/open_questions/verification/census_2026-07-12_s38/classify_near_misses.py
python3 notes/open_questions/verification/census_2026-07-12_s38/sasaki_root_audit.py
python3 notes/open_questions/verification/seven_block_interval_inflation_audit.py \
  --max-fibre-atoms 4 \
  --output notes/open_questions/verification/seven_block_interval_inflation_schema.json
python3 notes/open_questions/verification/seven_block_two_fibre_cycle_audit.py \
  --output notes/open_questions/verification/seven_block_two_fibre_cycle_schema.json
python3 notes/open_questions/verification/seven_block_two_fibre_inflation_audit.py \
  --max-fibre-atoms 3 \
  --output notes/open_questions/verification/seven_block_two_fibre_inflation_schema.json
cd formalization/QuerySystem && lake build
```

The new Lean theorem has no `sorry` or `sorryAx`; its `#print axioms`
receipt reports only `propext`, `Classical.choice`, and `Quot.sound`, matching
the existing finite-trace theorem.
