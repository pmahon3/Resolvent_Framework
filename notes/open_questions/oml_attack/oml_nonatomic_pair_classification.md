# Non-atomic pair classification in the seven-block skeleton

**Completion follow-up:** [`oml_nonatomic_pullback_completion.md`](oml_nonatomic_pullback_completion.md)
classifies six pair orbits and completes the `(5,11)` pullback as a
centre-free, single-edge, nonrectangular but tame inflation.
The two-common-block audit
[`oml_two_edge_pullback_completion.md`](oml_two_edge_pullback_completion.md)
closes O2/O3 as duplicate-datum candidates.

*Opened and exhaustively audited 2026-07-12. Scope: finite selector and
block-incidence classification only. No coarse completed OML is asserted.*

## Result

The 56-event skeleton has 42 nonzero, nontop, non-atomic events and hence
861 unordered non-atomic pairs. The executable audit
`../verification/seven_block_nonatomic_pair_audit.py` tests every pair.
Exactly 42 satisfy all of the following finite conditions:

1. a carrier point, hence a global point state of the concrete skeleton,
   charges both events;
2. their maximal-block supports overlap but neither contains the other;
3. a common Boolean block contains nonzero regions
   `e meet f`, `e meet f^perp`, and `e^perp meet f`;
4. the union of their propagated supports lies on a simple cycle of
   nontrivial block overlaps; and
5. their shared meet is neither central nor present in every maximal block.

The stable receipt is
`../verification/seven_block_nonatomic_pair_schema.json`. It contains all
861 pair records, not only the survivors, so every rejection and every
positive test can be recomputed.

## Smallest stable candidate

Using the stable event IDs in `seven_block_skeleton.json` and lexicographic
pair order, the first survivor is

\[
 (e,f)=(5,11),\qquad e=q_0\vee q_1,\quad f=q_0\vee q_2.
\]

The finite data are

\[
 \begin{aligned}
 \operatorname{supp}(e)&=\{B,Ca,D0,D2\},\\
 \operatorname{supp}(f)&=\{B,Cb,D1,D3\},\\
 \operatorname{supp}(e)\cap\operatorname{supp}(f)&=\{B\},\\
 e\wedge f&=q_0,\quad e\wedge f^\perp=q_1,\quad
 e^\perp\wedge f=q_2.
 \end{aligned}
\]

Thus `B` sees proper information from both selectors, while the shared
piece `q0` propagates only through `B,D0,D1` and is not central. The receipt
exhibits the seven-block cycle

\[
 B-Ca-D0-D1-Cb-D3-D2-B,
\]

which contains the full propagated support. Unlike the atom pair `(1,2)`,
this cycle already has a block (`B`) in which both coarse coordinates can
be compared.

## First genuinely partial relation

The finite datum determines the correct relation to test before a coarse
substitution. Let proper Boolean embeddings of a shared algebra `D` into
the proposed interval algebras `A` and `C` represent the information carried
by the common region below `q0`. Compatibility in `B` is then

\[
 R=A^*\times_{D^*}C^*
  =\{(u,v)\in\operatorname{Ult}(A)\times\operatorname{Ult}(C):
       u|_D=v|_D\}.
\]

This is not a declaration of an abstract relation: it is exactly the Stone
dual of agreement on the proper shared overlap subalgebra. It is
nonrectangular whenever `D` has at least two ultrafilters and both
restriction maps are onto. It is nonfunctional in either direction when
both maps have a fibre of size greater than one, so neither coordinate is a
redundant copy of the other.

A smallest transparent control takes `D` with two atoms and splits each
`D`-atom into two atoms independently in both `A` and `C`. Then

\[
 |\operatorname{Ult}(A)|=|\operatorname{Ult}(C)|=4,\qquad |R|=8<16,
\]

and every ultrafilter on either side has two compatible partners. This is
the first target relation for a completion audit. No coarse substitution
should be treated as admissible until complement/disjoint-union closure,
binary extrema, orthomodularity, maximal blocks, centre, and boundaries are
recomputed from scratch.

## Scope and formal receipt

This classification proves that the seven-block skeleton has **not** yet
been exhausted: non-atomic pairs satisfying the finite gate do exist. It
does not prove that the proposed fibre product survives completed OML
closure or produces nontrivial monodromy.

The previously established scope remains unchanged. Independent
lattice-atom interval coordinates are `Phi`-tame by the hand-level
rectangular factorization theorem. Lean's
`independent_finite_traces_dirac` certifies independent two-trace point
replacement, and `glueBlockStates` certifies gluing after compatibility is
given; Lean does not currently certify the rectangular overlap
decomposition or the full multi-fibre tameness theorem.

## Reproduction

```sh
python3 notes/open_questions/verification/seven_block_skeleton_data.py \
  --output notes/open_questions/verification/seven_block_skeleton.json
python3 notes/open_questions/verification/seven_block_nonatomic_pair_audit.py \
  --output notes/open_questions/verification/seven_block_nonatomic_pair_schema.json
python3 notes/open_questions/verification/verify_seven_block_nonatomic_pair_schema.py
```
