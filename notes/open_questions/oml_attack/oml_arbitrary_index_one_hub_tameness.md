# Arbitrary-index one-hub tameness theorem

*Campaign 15, 2026-07-14. The fixed-interface support-two architecture is
sigma-complete and Phi-tame.*

## 1. Definition and normal form

Let `I0=<a1,a2,a3,q>` be the ten-event horizontal sum of four four-element
Boolean algebras. For an arbitrary nonempty index set `J`, take copies `C_i` of the
56-event conditional cell amalgamated over `I0`. Write

\[
 Q_i=\{e_{11}^i,e_{10}^i\},\qquad
 P_i=\{e_{01}^i,e_{00}^i\}.
\]

Define

\[
 L_J=I_0\cup\bigcup_{i\in J}(C_i\setminus I_0)
 \cup\{x_i\cup y_j:i\ne j,\ x_i\in Q_i,\ y_j\in P_j\}.
\]

Equivalently, `L_J` is the union of the eleven private ternary Boolean
blocks in every cell and the sixteen-event blocks

\[
 M_{ij}=\operatorname{Bool}
 \{e_{11}^i,e_{10}^i,e_{01}^j,e_{00}^j\},\qquad(i,j)\in J^2.
\]

For `i=j`, this is the original coordinate block. For `i!=j`, its only
nonraw events are the four displayed cross pairs. Every event has private
coordinate support of size at most two.

## 2. Conservative-support theorem

If `S subset J`, `u,v in L_S`, and `w in L_J` satisfies
`w subset u intersection v`, then there is `bar(w) in L_S` with

\[
 w\subseteq\bar w\subseteq u\cap v.
\]

The exact outsider-elimination rules are:

- replace an outsider private raw event by its least allowable interface
  ceiling;
- replace `x_i union y_j` with `j` outsider by `x_i union q'`;
- replace it with `i` outsider by `q union y_j`;
- replace a repair with both indices outsider by `1`.

Complementation gives the dual upper-bound theorem. This is not a generic
cylinder-projection claim: several private events have non-interface
signature projections and least allowable ceiling `1`. The complete finite
kernel explicitly checks all 46 private forms against all 110 retained
two-cell forms, including all eight repairs, plus every one-outsider, dual,
and two-outsider case. **Evidence class:** the finite elimination table is
executable verified; the arbitrary-index conservative-support theorem is hand
proved from that table and index symmetry.
Certificate: `../verification/verify_h4_interface_hulls.py` and
`../verification/h4_interface_hull_receipt.json`.

Every binary calculation has finite support. Conservative support therefore
shows that its extrema computed in a finite subsystem remain global extrema.
The finite block-floor kernel supplies those extrema. The inclusions
`L_S -> L_T` preserve complement, meet, and join, so `L_J` is a concrete OML
for every nonempty index set `J`. **Evidence class: hand proved using the executable
outsider kernel.**

## 3. Blocks, centre, and states

A maximal compatibility clique containing a repair lies in its unique
`M_ij`; a maximal clique without repairs is an original private cell block.
Thus the displayed blocks are exhaustive. Every block is finite, and the
centre is `{0,1}`. **Evidence class: hand proved from the normal forms;
executable verified for `|J|<=3`.**

Restriction gives a bijection

\[
 \operatorname{St}_{fa}(L_J)\cong
 \{(s_i)_{i\in J}:s_i\in\operatorname{St}_{fa}(C_i),
                   \ s_i|_{I_0}=s_j|_{I_0}\}.
\]

Repair values are forced by additivity; conversely every compatible tuple is
the evaluation at its fibre-product point. Finite separating witnesses extend
by repeating a state with the same interface character, so point evaluations
separate order. **Evidence class: hand proved from the normal forms and the
finite cell census; executable verified for `|J|<=3`.**

On activation, the exact relation is

\[
 (q,r_i)_{i\in J}\in\{(0,0,\ldots),(1,1,\ldots)\}.
\]

No pair of private outputs enters one maximal block or reconstructs its joint
Boolean cylinders.

## 4. Disjoint-cylinder theorem and sigma completeness

Let `T` be the finite interface-character set and write the carrier as

\[
 X_J=\coprod_{t\in T}F_t^J
\]

with every `F_t` finite. Any pairwise-disjoint family of nonempty events of
`L_J` is finite.

Indeed, pigeonhole one component `F_t^J` on which infinitely many events are
nonempty and take minimal coordinate supports. Disjoint nonempty cylinders
cannot have disjoint supports, since independent fibre choices would give an
intersection. A pairwise-intersecting family of supports of size at most two
is either a star or is contained in one triangle. The triangle has finitely
many supports and finitely many subsets of each finite fibre square. In a
star, events on distinct leaves must have disjoint nonempty projections on
the finite centre fibre; only finitely many leaves occur, and each fixed
support again permits finitely many events.

Therefore every countable orthogonal family has only finitely many nonzero
members. `L_J` is already sigma-complete, and every finitely additive
two-valued state is sigma-additive:

\[
 \operatorname{St}_{fa}(L_J)=\operatorname{St}_{\sigma}(L_J).
\]

Consequently `Phi(L_J)` holds. **Evidence class: hand proved and hostile
reviewed.** This closes the entire arbitrary-index one-hub, finite-template,
support-at-most-two architecture as a counterexample route.

## 5. Scope: the two-dimensional gate

The theorem does not realize the puncture architecture. That requires events
`r_{i,alpha}` which, for fixed `i`, commute and generate a large Boolean
puncture block across many hub coordinates `alpha`. The one-hub family keeps
distinct private outputs incompatible and has no genuinely infinite
orthogonal family or non-sigma-liftable trace.

The next gate is therefore a bipartite row/column assembly. Its stripped
coordinate core already leaves the support-two class and develops crossed-
rectangle lattice failures; see `oml_bipartite_coordinate_core.md`.
