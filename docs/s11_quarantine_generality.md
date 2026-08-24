# Generality audit for s11 singleton quarantine

*Recorded 2026-08-09. Scope: the banked T1 proof, its one state-valued
corollary, and the fixed three-cell conditional-diagonal star. The paper of
record and its dependency path were read only. No finite search, construction,
or Lean work was performed. Claim-status entries are in
[`psi_lat_attack_surface_ledger.md`](psi_lat_attack_surface_ledger.md).*

## Falsifiers fixed before the abstraction test

1. **Locality falsifier.** If the proof of T1 consumes an Ulam row, column,
   countability, atomicity, sigma-state, or three-core hypothesis, then its
   mechanism is product-Ulam-specific and the audit stops after Phase 0.
2. **Candidate-lemma falsifier.** A concrete sigma-class, a finitely additive
   two-valued state `mu`, and value-one events `a,b` whose carrier meet exists
   and which satisfy the recovered local-resolution hypothesis, but with
   `mu(a meet b)=0`.
3. **Hypothesis-deletion falsifier.** A concrete sigma-complete essentially
   irreducible OML with a finitely additive state for which all private mixed
   meets of two distinct blocks are state-null. The banked `MO_omega` carrier
   is the first test.
4. **Star shortcut/evasion discriminator.** For a designated pair of
   value-one faces in every faithful realization of the star, either prove the
   recovered local-resolution hypothesis (shortcut) or prove that the
   interface hypotheses negate it (evasion). If neither implication follows,
   the verdict is undetermined.

These are tests of mechanisms, not requests for a carrier search.

## Phase 0 — the proof actually banked

### 0.1 Exact statement

`[REPO — VERIFIED]` Section 9c, T1, of
[`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md)
is formalized as `compat_of_locally_resolved` and
`compat_of_singletons` in
[`ConcreteOMLBlocks.lean`](../formalization/QuerySystem/QuerySystem/ConcreteOMLBlocks.lean).
The adversarial receipt
[`PROOF_READ_2026-07-11_attack_s11.md`](../notes/open_questions/oml_attack/PROOF_READ_2026-07-11_attack_s11.md)
was checked as corroboration; the statement and argument below come from the
actual theorem text and proof, not the receipt's summary.
In the formal statement, let `d` be a concrete sigma-class on a set `Omega`,
let `X,S` be members of `d`, and assume `MeetsExist d`: every pair of carrier
events has a greatest carrier lower bound. If

\[
  \forall\omega\in X\cap S\;\exists E\in d,
  \qquad \omega\in E\subseteq X\cap S,
  \tag{LR}
\]

then `X cap S` belongs to `d`; equivalently `X` and `S` are concretely
compatible. More precisely, their carrier meet is the literal set
intersection:

\[
  X\mathbin\wedge S=X\cap S.
\]

The named singleton corollary replaces `(LR)` by
`{omega} in d` for every `omega in X cap S`. Its global corollary says that a
concrete sigma-class OM lattice containing every singleton is intersection
closed, hence a Boolean sigma-field.

### 0.2 Inherited hypotheses versus used hypotheses

`[REPO — VERIFIED BY PROOF INSPECTION]` The proof chooses the greatest lower
bound `m` of this one pair. Every resolving `E` in `(LR)` is a carrier lower
bound, so maximality of `m` puts every point of `X cap S` in `m`. Since every
lower bound is set-theoretically contained in `X cap S`, equality follows.

| Hypothesis appearing in the banked setting | What this proof uses |
|---|---|
| concrete sigma-class / Dynkin-system structure | only the carrier membership predicate and literal subset order; complement and countable disjoint-union closure are unused |
| `MeetsExist d` for all pairs | only the greatest lower bound of the one pair `X,S` |
| orthomodularity | unused |
| sigma-completeness | unused |
| maximal blocks or their sigma-fields | unused |
| a finitely or sigma-additive state | unused |
| countable generation, atomicity, Ulam rows/columns, or the three cores | unused |
| `(LR)` | load-bearing: its lower bounds cover the whole literal intersection |

Thus the locality falsifier does not fire. The result is substantially more
general than the product-Ulam construction, but its extra generality is a
pairwise order statement, not yet a state constraint.

### 0.3 What “T1” does

`[REPO — VERIFIED; SCOPE CORRECTION]` T1 is not used to make the meet a
singleton and not used to prove it nonempty or non-null. Singleton events are
merely a sufficient family of carrier lower bounds, one through every point.
They squeeze an existing carrier meet up to the literal set intersection.
The sharpened proof needs local resolution `(LR)`, not global singleton
availability and not a topological separation theorem.

`[REPO — VERIFIED]` In the product-Ulam carrier, every singleton below
`A_1 cap A_2` is present, while
[`cor:incompat`](../papers/sigma_essential/sigma_essential_body.tex) proves
that `A_1,A_2` are incompatible and have no meet. T1 says exactly that this
fine resolved overlap cannot coexist with a lattice meet. The Ulam matrix is
used separately for sigma-state rigidity; it does not occur in T1.

### 0.4 Arity

`[REPO — VERIFIED]` T1 concerns one meet of one pair of events. It contains no
two-block gluing theorem and no loop or three-block step. Incompatibility
appears only after contraposition:

> if `X,S` are incompatible in a concrete sigma-class OM lattice, some point of
> `X cap S` lies in no carrier event contained in that intersection.

The Phase-0 stop condition therefore does not fire: the proof is not
product-Ulam-specific, although its product-Ulam application is tied to that
carrier's fine singleton structure.

## Phase 1 — the abstraction that survives

### 1.1 Candidate lemma

**Locally resolved value-one meet lemma.** `[HAND — PROVED FROM BANKED T1]`
Let `L` be a concrete sigma-class, let `mu` be a finitely additive two-valued
state on `L`, and let `a,b in L` have a carrier meet and satisfy

\[
  \mu(a)=\mu(b)=1.
\]

Assume that `a cap b` satisfies `(LR)`. Then

\[
  a\wedge b=a\cap b\in L,
  \qquad \mu(a\wedge b)=1.
  \tag{*}
\]

*Proof.* T1 gives `a meet b=a cap b` and compatibility. Restricting `mu` to
the Boolean algebra generated by the compatible pair gives an ultrafilter,
so it is closed under intersection. Equivalently, if
`mu(a cap b)=0`, finite additivity on
`a=(a cap b) disjoint_union (a setminus b)` gives `mu(a setminus b)=1`;
the disjoint value-one pair `a setminus b,b` would then have a union of value
two, impossible. Hence `mu(a cap b)=1`. QED.

No sigma-completeness, countable-type, atomicity, block, or Ulam hypothesis is
used. This is the weakest non-tautological form recovered from the proof:
global latticehood is reduced to existence of this pair's meet, and global
singleton availability is reduced to `(LR)` on this one intersection. In
particular, if `B_1,B_2` are chosen distinct blocks and they contain private
value-one events `a,b` satisfying `(LR)`, their mixed meet is nonempty and
non-state-null. This is the honest general live-constraint corollary of s11.

The candidate-lemma falsifier would be a tuple satisfying all displayed
hypotheses but violating `(*)`; the proof excludes it. The important boundary
is instead whether `(LR)` follows from the ambient assumptions.

### 1.2 Why latticehood alone does not supply `(LR)`

`[REFUTED — BANKED EXPLICIT COUNTEREXAMPLE]` The hypothesis-deletion
falsifier fires. In section 9a of
[`oml_lattice_regularity_attack.md`](../notes/open_questions/oml_attack/oml_lattice_regularity_attack.md),
take `Omega=2^N`,

\[
  A_i=\{x:x_i=0\},\qquad
  L=\{0,1,A_i,A_i^\perp:i\in\mathbb N\}=MO_\omega.
\]

For `i != j`, every private nontrivial element of the block
`{0,1,A_i,A_i^perp}` has lattice meet `0` with every private nontrivial
element of the `j`-block, although their literal set intersections are
nonempty. Choose, for example, the Dirac state at the all-zero sequence;
then `mu(A_i)=mu(A_j)=1` but `mu(A_i meet A_j)=0`. No nonempty carrier event
lies inside `A_i cap A_j`, so `(LR)` fails exactly where T1 says it must.

The same banked example is infinite, concrete, sigma-complete, non-Boolean,
and has trivial centre; since it has no nonempty countable carrier events,
its quotient by the countable ideal is unchanged and it is essentially
irreducible. It is excluded from `Adm` by its segregated/Polish-tame state
behaviour, not by latticehood, sigma-completeness, or essential
irreducibility. Therefore no lemma saying merely “latticehood forces a live
cross-block meet” is available from s11.

### 1a. Relation to `Adm`

`[REPO DEFINITION AUDIT + HAND CONSEQUENCES]` The paper defines `Adm` in the
Discussion of
[`sigma_essential_body.tex`](../papers/sigma_essential/sigma_essential_body.tex)
as concrete, sigma-complete, non-Boolean, essentially irreducible,
non-segregated, and non-Polish-representable. `Psi_lat` adds latticehood.

| Paper condition | Relation to the candidate lemma |
|---|---|
| concreteness | supplies the literal set representation used by `(LR)` |
| latticehood | supplies the pair meet, but not resolving lower bounds |
| sigma-completeness | stronger than anything used and does not imply `(LR)` (`MO_omega`) |
| non-Boolean | conflicts with the **global** all-singletons form of T1, because that form makes a lattice Boolean; it does not conflict with local `(LR)` on a compatible pair |
| essential irreducibility | does not imply live mixed meets or `(LR)` (`MO_omega`) |
| non-segregation | is a blockwise sigma-state rescue condition (`rem:segregated`), not a mixed-meet or point-resolution condition; no repo implication to `(LR)` is known |
| non-Polish-representability | unused; no repo implication to `(LR)` is known |

Thus the candidate's decisive premise is neither an `Adm` axiom nor a
consequence banked for `Adm intersect lattices`. At global singleton scope it
is actually too fine for a non-Boolean admissible lattice.

### 1b. Relation to the six-part flat habitat

`[REPO DEFINITION AUDIT]` Section 4 of
[`psi_lat_attack_surface.md`](psi_lat_attack_surface.md) requires the flat
habitat to combine: (i) an infinite concrete sigma-complete OML, (ii) an
infinite coarse boundary, (iii) strict or state-null mixed meets, (iv) a
non-countable-type state defect or other non-T4 rigidity, (v) survival of the
countable quotient, and (vi) a common-`mu` GSD obstruction plus the remaining
`Adm` conditions.

- The candidate bears on (iii) only if a designated value-one intersection
  is locally resolved. It then gives state value one, contradicting flatness.
- Conditions (i), (ii), (iv), (v), and (vi) do not supply `(LR)` in any
  cited repo theorem.
- Being outside the countable-type-over-atoms class is not the negation of
  `(LR)`: T1 contains no countability or atomicity hypothesis. Likewise, a
  nonseparating quotient need not say whether carrier lower bounds cover one
  particular mixed set intersection.
- Conversely, any successfully realized **strict** mixed meet—or any
  state-null meet of two designated value-one inputs—automatically fails
  `(LR)`. That is a necessary feature of the desired realization, not a proof
  that the realization exists.

Accordingly the habitat avoids the known *source* of `(LR)`—a faithful fine
singleton-resolving shared boundary—but its six conditions do not formally
negate `(LR)` at the designated mixed cuts. Calling this a proved evasion
would slide from “nonseparating” to “locally unresolved.”

## Phase 2 — the three-cell conditional-diagonal star

`[REPO — TARGET SPECIFICATION, NOT A CONSTRUCTION]` Section 8 of
[`oml_distributed_relation_cell_assembly.md`](../notes/open_questions/oml_attack/oml_distributed_relation_cell_assembly.md)
names a three-cell conditional-diagonal star with distinct proper
nonseparating quotient supports. The attack memo further requires interfaces
outside the countable-type-over-atoms class and nontrivial after quotienting
by countable sets, using sections 2--3 of
[`oml_coarse_inhabitation_and_defect.md`](../notes/open_questions/oml_attack/oml_coarse_inhabitation_and_defect.md).
The proposed flat-realisation lemma, rather than an existing carrier, is what
would supply the faithful concrete sigma-complete OML, the global finitely
additive state, and strict state-null mixed meets.

For s11 to shortcut that calculation, one still needs the following exact
statement for at least one pair `a,b` among the prescribed value-one faces:

\[
  (LR_*)\qquad
  \forall\omega\in a\cap b\;\exists E\in L,
  \quad \omega\in E\subseteq a\cap b.
\]

`[SCOPE CHECK — NOT IMPLIED]` Distinct quotient supports do not provide
`(LR_*)`; “nonseparating” is not synonymous with “no local lower-bound
cover”; non-countable-type and quotient survival concern state-defect and
essential-irreducibility gates, not this pointwise carrier condition. No
banked completion theorem decides which new mixed cuts the infinite star
creates. The finite `k=1,2,3` stars in section 9 are explicitly controls with
compatible-event, point-state semantics and are not the live incompatible
construction; their receipts cannot settle `(LR_*)` for the proposed coarse
interfaces.

**Phase-2 verdict: UNDETERMINED.** `[GRADED: EXACT MISSING HYPOTHESIS
LOCATED]` If every faithful realization forces `(LR_*)`, the candidate lemma
gives `mu(a meet b)=1`, the flat-realisation lemma is false, and the result is
a shortcut. If a faithful realization preserves strict/state-null mixed
meets, then T1 certifies that those intersections contain unresolved points
and the result is evasion. Present interface fences prove neither branch.
What settles the verdict is precisely the mixed-cut portion of the planned
hand calculation, not a finite census or a new construction front.

## Phase 3 — half-page memo

**Is s11 local or general?** **GENERAL AS A CONDITIONAL PAIRWISE LEMMA;
LOCAL AS A PRODUCT-ULAM KILL MECHANISM.** `[REPO — VERIFIED + HAND COROLLARY]`
The meet squeeze uses no Ulam, sigma, atomic, block, or state hypothesis. With
a finitely additive state and two value-one events it forces a value-one meet.
But it requires their literal intersection to be covered pointwise by carrier
lower bounds. Latticehood and `Adm` do not provide that condition; `MO_omega`
shows that even a concrete sigma-complete essentially irreducible OML can have
all private off-block meets equal to zero.

**Candidate lemma and `Adm`.** The locally resolved value-one meet lemma is
the full honest abstraction: pair meet + `(LR)` + finite-additive value one on
both inputs imply `mu(a meet b)=1`. Concreteness and latticehood provide only
the ambient language and the meet. Sigma-completeness, essential
irreducibility, non-segregation, and the other `Adm` gates do not imply
`(LR)`; global singleton resolution would instead Booleanize a lattice.

**Star verdict.** **UNDETERMINED.** The star is specified to avoid a faithful
shared separating boundary, but that is not yet a proof that every designated
mixed intersection fails local resolution. Proving or refuting `(LR_*)` is
one part of the already-planned mixed-cut audit.

**Pen-and-paper target.** It does not substantively change: run the three-cell
star calculation, checking `(LR_*)` at the first designated mixed cut; no
s11-based shortcut or proved evasion is currently banked.
