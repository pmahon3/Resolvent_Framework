# Proper boundary surviving exhaustive maximal completion

*Completed 2026-07-13. Outcome A for the bounded search: among all 127
nonempty subfamilies of the seven labelled maximal blocks of the certified
56-event OML, four centre-free finite OMLs retain a proper full maximal-block
boundary and a proper-closure transverse triangle. The smallest have 44
events. This is exhaustive finite evidence for that fixed block-subfamily
class, not a classification of arbitrary completions, an infinite theorem,
or a Lean certificate. Human review approved banking this restricted finite
counterexample/result on 2026-07-13.*

**Epistemic correction.** The positive statement is executable finite
evidence: the 56-event control contains a locally noncentral proper joint
closure. Separately, that construction refutes only the proposed local
obstruction that every proper transverse joint closure must become central.
Whether an infinite inflation preserves the required structural gates and
produces a noncompact eligible sigma-state slice remains open; no such
inflation is claimed to exist here.

## 1. The 44-event survivor

Use the labelled blocks from
[`oml_three_block_noncentral_transverse_candidate.md`](oml_three_block_noncentral_transverse_candidate.md)
and retain

\[
             A00,\quad A01,\quad C01,\quad A10,\quad A11.
\]

Their union has 44 events on the same 16-point carrier. Exhaustive
compatibility-clique enumeration shows that these are exactly its five
maximal Boolean blocks, all of size 16. The union is closed under complement
and disjoint binary union, has unique meet and join for every ordered pair,
satisfies the orthomodular law for every comparable pair, and has centre
`{0,1}`. Finiteness therefore gives a concrete sigma-complete OML.

The full overlap-generated boundary sizes are

| block | `A00` | `A01` | `C01` | `A10` | `A11` |
|---|---:|---:|---:|---:|---:|
| boundary size | 16 | 16 | 8 | 16 | 16 |

Thus `C01` retains a proper eight-element boundary even after every maximal
block of this completion has been classified and included. The triangle
`A01,C01,A10` has three distinct four-element pairwise interfaces and
eight-element proper incident joint closure at every vertex. Since the
ambient centre is trivial, all its nontrivial interface events are
noncentral.

## 2. State and regularity gates

The exhaustive block-ultrafilter census finds 12 global two-valued states.
They are exactly the 12 distinct point-evaluation signatures. They
order-separate the 44-event carrier, and their restrictions give all 12
locally coherent two-valued block-ultrafilter triples on the transverse
triangle. Hence the finite completion loses no triangle state.

The candidate remains Phi-tame and has no sigma-essential state: on a finite
carrier, finite and countable additivity coincide. It passes the finite
proper-boundary gate but does not address the required noncompact local
sigma-state slice. The next step is therefore an infinite inflation of the
44-event incidence pattern, with maximal blocks, latticehood,
sigma-completeness, centre, global state extension, order separation, and
noncompactness re-audited rather than inherited from the finite control.
Section 4 performs that audit for the literal one-interval substitution.

## 3. Exhaustive scope

The census checks all `2^7-1=127` nonempty labelled block subfamilies. Of
these, 100 fail concrete-logic closure and 27 are OMLs. Exactly four satisfy
all of: trivial centre, exact named maximal-block classification, a proper
full boundary, and a proper-closure transverse triangle. All four have 44
events. This minimality is only inside the fixed seven-block subfamily
universe; no claim is made about all finite OMLs or all transverse
completions.

## 4. Infinite one-interval inflation audit

Let `q_0={(0,r,s):r,s in {0,1}}` and let `A` be a concrete Boolean
sigma-algebra. Replace `[0,q_0]` by `A` and lift the other skeleton events by
inverse image. Exactly `A00,A01,C01` contain `q_0` as an atom, so mixed
closure propagates the same `A` interval through precisely those three
blocks. The proposed completion is their union with the unchanged 16-event
blocks `A10,A11`.

The required stop gates pass at hand-proof level.

1. **Maximal blocks.** Outside `[0,q_0]`, the finite compatibility table is
   the table of the certified 44-event survivor. A proper fibre event has
   the same zero/top extremal behaviour against a crossed skeleton event as
   `q_0`. Compatibility therefore replaces the `q_0` atom in exactly the
   three named blocks and creates no new compatibility clique. The maximal
   blocks are exactly `A00,A01,C01,A10,A11`.
2. **Sigma-completeness.** In a countable disjoint family, only finitely many
   members have nonzero support outside `q_0`, because the outside skeleton
   is finite. The remaining portions form a disjoint family in the common
   copy of `A`. Take their union in `A` and combine it with the finite
   outside union in the block supplied by the certified finite shape table.
   Binary extrema and the orthomodular law reduce in the same way to the
   finite survivor outside `q_0` and Boolean operations inside it.

### Independent arbitrary-base proof audit

The two assertions above do not rely on atomicity of `A`.  Here is the
finite-reduction argument that makes their arbitrary-base scope explicit.
Every event in an inflated block has a unique normal form consisting of one
coefficient `a in A` on `q_0` and a subset of the three unchanged outside
atoms.  Events in `A10,A11` retain one of finitely many crossed skeleton
forms.  Complement, inclusion, disjointness, and the compatibility equation
for two such events depend only on their two `A` coefficients and their
finite skeleton forms.  The Boolean algebra generated by two coefficients
has at most four atoms.  Its faithful identification with `P(k)`, `k<=4`,
reduces every binary relation to one of the checked finite controls.

It follows first that the union is a concrete logic and an OML: all binary
extrema and the orthomodular equation reduce to those controls.  Centralizer
calculations for the five displayed blocks are not, by themselves, a global
classification of compatibility cliques.  The following separate
finite-pattern argument supplies that missing step.

### Global compatibility-graph audit

There are 44 constant skeleton forms and 16 nonconstant forms
`E(a,S)`, where `S` is the outside-`q0` part and `a in A` is the sole fibre
coefficient.  For two nonconstant forms, the Boolean algebra generated by
their coefficients has the four regions

`a meet b`, `a meet b^c`, `a^c meet b`, `a^c meet b^c`.

The two events are compatible exactly when their two zero/one skeleton
specializations are compatible on every nonzero region.  This follows by
applying the unique normal forms to the compatibility equation.  The
four-region receipt also checks all 47,070 form-instance pairs against the
certified `P(4)` block cover.

Now let `F` be a finite pairwise-compatible family.  Its coefficients
generate a finite Boolean algebra whose atoms are labelled by truth vectors
of the coefficients in `F`.  On every occurring truth vector, `F`
specializes to a compatible family in the 44-event skeleton.  Suppose no
one named block contained `F`.  An inclusion-minimal such subfamily has at
most five members: for each of the five block labels, retain one event that
excludes it.  Repeated forms cannot occur in a minimal obstruction because
they have the same named-block signature.  Exhaustive enumeration of the
60 forms, all minimal families of sizes two through five, and all feasible
truth vectors finds no obstruction.  Thus every finite compatible family is
contained in one named block.

For an arbitrary compatible family, its eventwise named-block signatures
are subsets of the fixed five-element label set.  Their finite intersections
are nonempty by the preceding paragraph.  Their total intersection is then
nonempty: otherwise one event excluding each label would already give a
finite obstruction.  Hence every compatible family is contained in one of
`A00,A01,C01,A10,A11`.  A maximal compatible family therefore equals one of
these five blocks.  This proves the global classification for every
nondegenerate concrete Boolean sigma-algebra `A`; no sixth maximal
compatible family exists.

This is a hand proof backed by an exact finite-pattern receipt, not a Lean
certificate.  The executable part verifies the finite form census and
truth-vector consistency.  The normal-form specialization and passage from
finite to arbitrary families are the hand-proof boundary.

For sigma-completeness, take a countable disjoint family.  Only finitely many
members can use a crossed form from the two finite blocks.  Among the rest,
only finitely many can have nonempty support outside `q_0`, since those
supports are disjoint subsets of a fixed finite set of outside atoms.  The
tail is therefore a disjoint family in the common copy of `A`; take its
sigma-union there.  Repeated binary closure combines the finite head, and
one final binary union combines it with the tail union.  Thus the concrete
union is closed under countable disjoint unions.  In an OML, disjointizing a
countable family by successive finite joins turns this into countable join
completeness.  This independently proves sigma-completeness in the stated
arbitrary-base scope.

The finite receipt through four fibre atoms has the exact role used here:
it checks all two-coefficient Boolean relation types.  It is still bounded
executable evidence, not by itself the arbitrary-base theorem.

These are hand proofs, not consequences of the bounded receipt and not Lean
certificates. The receipt checks the independent finite approximants
`A=P(n)` for `n=2,3,4`:

| fibre atoms | events | maximal block sizes | boundary sizes in `A00,A01,C01,A10,A11` |
|---:|---:|---|---|
| 2 | 76 | `16^2,32^3` | `32,32,16,16,16` |
| 3 | 140 | `16^2,64^3` | `64,64,32,16,16` |
| 4 | 268 | `16^2,128^3` | `128,128,64,16,16` |

Every approximant has exactly the five named maximal blocks, trivial centre,
and `C01` as its unique proper-boundary block. This is finite executable
evidence only.

The remaining gates also pass. The intersection of the five exhaustive
maximal blocks is `{0,1}`, so the centre is trivial. Point evaluations
order-separate the concrete carrier. A coherent two-valued state on the
inflated transverse triangle consists of a coherent finite skeleton state
and, when it charges `q_0`, one common ultrafilter of `A`; the finite
extension theorem extends the skeleton component to `A10,A11`. The same
argument preserves sigma-additivity when the local ultrafilter is
sigma-additive.

For the countable-coordinate sigma-field on `2^I`, `I` uncountable, the face
`q_0=1` exposes the same noncompact eligible local sigma-state slice as the
seven-block one-interval model. Nevertheless this inflation is Phi-tame.
Given a finite trace charging `q_0`, replace its common ultrafilter of `A` by
a point state in the finite oriented intersection and retain the extended
finite skeleton state. If the trace does not charge `q_0`, the fibre is
invisible.

This is **Outcome B: an infinite centre-free sigma-complete inflation with a
surviving proper boundary and noncompact local slice, but no sigma-essential
state**. It does not resolve the standing conjecture. The next construction
must introduce two inequivalent coarse coordinates or a genuine cycle twist
while retaining the five-block classification and proper boundary.

The independent run-0016 executor audit records the proof dependencies and
evidence boundary in
[`oml_arbitrary_base_inflation_review.md`](oml_arbitrary_base_inflation_review.md).
It found no structural failure, but it does not satisfy the required human
authorization gate; the arbitrary-base hand theorem remains pending that
review rather than accepted in the ledger.

## 5. Smallest cycle-twist test

The smallest possible twist uses the two-atom algebra `P(2)` on the triangle
of inflated blocks `A00,A01,C01`.  Its automorphism group is `Z/2`; label
each of the three pairwise identifications by identity or atom-swap.  A
faithful three-block paste must satisfy the cocycle equation on the common
`P(2)` interval, so the product of the three edge labels must be identity.

There are eight labelled cases.  The four with odd swap parity have swap
holonomy.  Transitivity of equality around the triangle then identifies
every event `a` with its swap.  The embedded interval collapses to the fixed
subalgebra `{0,1}`, so these cases are not faithful inflations and fail
before maximal-block classification.  The four even-parity cases satisfy
the cocycle equation, but vertex relabellings remove all edge labels; they
are isomorphic to the untwisted inflation.  Thus the smallest abstract edge
twist produces no genuine cycle monodromy.  This does not classify twists
using larger interfaces, proper subalgebras, correspondences, or carrier
identifications that change the mixed concrete relations.

The bounded enumeration is recorded by
`../verification/five_block_smallest_twist_audit.py` and its JSON receipt.

## Reproduction

```sh
python3 notes/open_questions/verification/exhaustive_boundary_properness_audit.py \
  --output notes/open_questions/verification/exhaustive_boundary_properness_schema.json
python3 notes/open_questions/verification/verify_exhaustive_boundary_properness.py
python3 notes/open_questions/verification/exhaustive_boundary_inflation_audit.py \
  --max-fibre-atoms 4 \
  --output notes/open_questions/verification/exhaustive_boundary_inflation_schema.json
python3 notes/open_questions/verification/five_block_smallest_twist_audit.py \
  --output notes/open_questions/verification/five_block_smallest_twist_schema.json
python3 notes/open_questions/verification/verify_five_block_smallest_twist_schema.py
python3 notes/open_questions/verification/five_block_global_compatibility_audit.py \
  --output notes/open_questions/verification/five_block_global_compatibility_schema.json
python3 notes/open_questions/verification/verify_five_block_global_compatibility.py
```
