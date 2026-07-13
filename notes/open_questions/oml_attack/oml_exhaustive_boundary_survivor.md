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

## Reproduction

```sh
python3 notes/open_questions/verification/exhaustive_boundary_properness_audit.py \
  --output notes/open_questions/verification/exhaustive_boundary_properness_schema.json
python3 notes/open_questions/verification/verify_exhaustive_boundary_properness.py
python3 notes/open_questions/verification/exhaustive_boundary_inflation_audit.py \
  --max-fibre-atoms 4 \
  --output notes/open_questions/verification/exhaustive_boundary_inflation_schema.json
```
