# Coarse-block inhabitation, countable-type defect anatomy, and the essential-irreducibility fence

*Opened 2026-07-13 (campaign iteration 1). Status: ⟦HAND⟧ throughout —
elementary σ-field arguments plus one instantiation of the banked
arbitrary-base q0 inflation
([`oml_exhaustive_boundary_survivor.md`](oml_exhaustive_boundary_survivor.md) §4,
independently audited in
[`oml_arbitrary_base_inflation_review.md`](oml_arbitrary_base_inflation_review.md)).
The inhabitation theorem is conditional on that audited hand theorem and
inherits its evidence class. No Lean certificate is added here; no finite
oracle applies (every claim is about uncountable carriers). Awaits
fresh-context adversarial review.*

## 1. Question addressed

§10d of [`oml_lattice_regularity_attack.md`](oml_lattice_regularity_attack.md)
factors Theorem 2 as **B′(i) + (coarse-block question: no coarse blocks in
𝒞 ∩ OML, or B′(ii))** and promotes the coarse-block toy hunt because it
"decides whether the second factor is vacuous." The taxonomy carries this as
`oml.construct.coarse_toy` (open-probe). This note settles the vacuity
question (it is NOT vacuous), classifies the σ-defect of the tractable
coarse class, and records a new admissibility fence discovered en route.

Call a maximal block **state-coarse** if it carries a non-principal (non-
carrier-point-realized) two-valued σ-additive state. By P⁼/T3 a state-coarse
block is not countably generated; the converse fails (§5(iii) below), so
state-coarseness, not generation cardinality, is what B′(ii) is about.

## 2. Countable-type σ-fields: state classification and defect anatomy

**Definition.** Let Γ be an index set, {P_γ}_{γ∈Γ} a partition of a set D
into nonempty pieces, and let

\[
 A_Γ = \{\,\textstyle\bigcup_{γ∈S}P_γ : S ⊆ Γ,\ S\ \text{countable or
 co-countable}\,\}.
\]

Call a σ-field **of countable type over its atoms** if it is of this form
(equivalently: atomic, with every element a countable or co-countable union
of atoms). Two standing examples: Γ = ℕ with singleton pieces gives
P(ℕ) — the relay master block; Γ = ω₁ with singleton pieces gives the
countable/co-countable field on ω₁ — the Marczewski coarse bank.

**Lemma 1 (σ-state classification).** The two-valued σ-additive states on
A_Γ are exactly:

1. the **atom-principal** states u_γ (u_γ(E) = 1 iff P_γ ⊆ E), one per
   atom; each is realized by every carrier point x ∈ P_γ; and
2. if Γ is uncountable, the **co-atom-countable state** ν_∞
   (ν_∞(E) = 1 iff E is a co-countable union of atoms), which is
   non-principal.

*Proof.* Let ν be σ-additive and two-valued. If ν charges some countable
union K = ⊍_{γ∈S}P_γ (S countable): K is a countable disjoint union of
atoms, so σ-additivity charges exactly one P_γ, and atomicity makes ν = u_γ
(every element contains or misses each atom). If ν charges no countable
union, it charges every co-countable one, i.e. ν = ν_∞ (well-defined only
for Γ uncountable: otherwise "co-countable" includes ∅'s complement
trivially and the family {co-countable S} is not a proper filter).
Conversely u_γ is σ-additive (an atom lies in exactly one member of a
disjoint family covering it, since members are unions of atoms), and ν_∞
is: a countable disjoint family of countable unions has countable union,
and if the union is co-countable exactly one member is co-countable (two
co-countable index sets in Γ intersect, and disjoint elements of A_Γ have
disjoint index sets). ∎

**Lemma 2 (f.a. classification; the σ-defect).** The finitely additive
two-valued states on A_Γ are exactly: the atom-principal states, ν_∞ (Γ
uncountable), and the **free-on-countable** states — for a countably
infinite S ⊆ Γ and a free ultrafilter 𝒰 on S, the state
u_{S,𝒰}(E) = 1 iff {γ ∈ S : P_γ ⊆ E} ∈ 𝒰. The σ-defect (f.a. but not
σ-additive states) is exactly the free-on-countable class.

*Proof.* A two-valued f.a. state is an ultrafilter U of the field. Either
U contains a countable union K = ⊍_{γ∈S}P_γ: all unions over subsets of S
are in A_Γ (subsets of countable sets are countable), so U induces an
ultrafilter on S; if principal, U is atom-principal; if free, U = u_{S,𝒰}
(S infinite; finite S forces principality). Or U contains no countable
union: then it contains every co-countable one, so U = ν_∞. Each u_{S,𝒰}
fails σ-additivity at K = ⊍_{γ∈S}P_γ: every piece gets value 0, the union
value 1. Lemma 1 covers the rest. ∎

**Corollary 3 (defect anatomy at countable-type boundaries).** Let B be a
maximal block, and suppose a boundary or overlap algebra through B is of
countable type over uncountably many atoms. Then at that interface

\[
 T^{\mathrm{fa}} \setminus T^{\sigma}\ \subseteq\
 \{\text{free-on-countable traces}\},
\]

and a pattern traps at that interface (forces every eligible trace into
the defect) only if it simultaneously

- **(ν_∞-exclusion)** forces value 1 on some countable atom-union K — a
  single event suffices and is cheap; and
- **(atom-killing)** makes every atom-principal trace charging the induced
  local kernel non-extendable — which, since the relevant atoms then lie
  in the fixed countable family S(K), is precisely the **countable
  atom-killing problem** over S(K) that the relay programme
  (`oml_lattice_regularity_attack.md` §§16–26) attacks on the master block
  P(ℕ), transported one level up from points to uncountable atoms.

*Proof.* The displayed inclusion is Lemma 2 applied to the interface
algebra. If no eligible trace charges a countable atom-union, ν_∞ itself
remains eligible and is σ-additive, so no trap; given the forced K, the
remaining σ-lifts through the interface are the atom-principal states at
atoms inside K by Lemma 1, and trapping requires excluding each. ∎

**Reading.** Countable-type coarseness buys a witness hunt *nothing new*:
its defect sits over a countable atom family, where the problem
re-fine-ifies to the master-block relay problem (with atoms in place of
points; the automaton geometry is unchanged, since only the Boolean
quotient by the atom partition enters). The genuinely open coarse
territory for B′(ii) is therefore σ-fields that are **not of countable
type over atoms** — non-atomic-mod-countable structures — where the
two-valued σ-state theory is set-theoretically nontrivial. This is the
precise restatement direction `oml.coarse.bprime_ii` asks for.

## 3. The essential-irreducibility fence

Admissibility (paper Definition, `sigma_essential_body.tex` §2) requires
**essential irreducibility: the quotient of L by the σ-ideal of countable
sets has centre {0,1}**. For the banked one-interval inflation this gate
interacts sharply with the choice of fibre algebra A on D.

Recall the inflation's event normal forms
([`oml_arbitrary_base_inflation_review.md`](oml_arbitrary_base_inflation_review.md) §2):
every event of an inflated block (A00, A01, C01) is E(a,S) — one
coefficient a ∈ A repeated over the four q0-points, plus a subset S of
that block's three outside 16-point-skeleton atoms; every event of the two
crossed blocks (A10, A11) contains all or none of each fibre copy, so has
the form (T × D) ∪ (finite outside part) with T a subset of the four
q0-points. The outside skeleton is finite (12 carrier points outside the
fibre region), hence countable, hence annihilated by the ideal.

**Proposition 4 (fence).** Let L_A be the arbitrary-base q0 inflation with
fibre algebra A on D. Then in the quotient L_A/[countable]:

1. every class is [T × D] (T ⊆ q0's four points) or [4 × a] (a ∈ A), where
   4 × a abbreviates the diagonal event with coefficient a over all four
   points;
2. [4 × a] is trivial iff a is countable or co-countable in D;
3. hence L_A is essentially irreducible **iff** A contains an element with
   both sides uncountable, i.e. iff A/[countable(D)] is nontrivial.

In particular **A = ctble/coctble(ω₁) fails**: its entire coarse structure
lies inside the annihilated ideal, the quotient is the Boolean P(4), and
its centre is everything.

*Proof.* (1) Every event lies in one of the five maximal blocks (banked
classification); the two normal forms above reduce mod countable to the
displayed classes (a countable coefficient contributes a countable set,
4 × a with a co-countable is ≡ 4 × D = [T×D] with T full). (2) 4 × a is
countable iff a is countable; (4 × a)Δ(4 × D) = 4 × a^c. (3, ⟸) Suppose
a₀ ∈ A has both sides uncountable and let T be proper nonempty. The
carrier intersection (T × D) ∩ (4 × a₀) = T × a₀ has uncountable symmetric
difference with every event of L_A (inflated events are 4-diagonal;
crossed events are full-fibre; everything else differs by an uncountable
piece), so in the quotient the pair {[T × D], [4 × a₀]} has no nonzero
common lower bound while [T × a₀] ≠ 0 forbids [T×D] ∧ [4×a₀]^⊥-style
decompositions: explicitly, [4×a₀] ∧ [T×D] = 0 and [4×a₀] ∧ [T^c×D] = 0,
so [4×a₀] ≠ ([4×a₀]∧[T×D]) ∨ ([4×a₀]∧[T×D]^⊥) and the two classes are
incompatible. Thus no proper class of either family is central, and the
centre is {0,1}. (⟸ of 2 and ⟹ of 3) If every a ∈ A is countable or
co-countable, every [4 × a] ∈ {0,1} and the quotient is exactly
{[T × D] : T ⊆ 4} ≅ P(4), which is Boolean; its centre is all of it. ∎

**Fence, stated for reuse.** *A load-bearing coarse fibre must survive the
countable quotient: any inflation whose coarse structure is built entirely
from countable/co-countable distinctions is essentially reducible and
leaves Adm.* This is consistent with the OMP witness's anatomy (its centre
was exactly the countable/co-countable sets, which the state annihilates)
and explains it structurally.

## 4. Inhabitation: the coarse factor of Theorem 2 is not vacuous

**Definition.** Let A* be the σ-field of countable type over a partition
of D = ω₁ into ℵ₁ pairwise disjoint uncountable pieces {P_γ}_{γ<ω₁}
(e.g. the classes of the map ω₁ → ω₁ collapsing to the ω-th predecessor;
any such partition works). A* is nondegenerate and concrete.

**Theorem 5 (inhabitation; conditional on the banked arbitrary-base
inflation).** L* := the q0 inflation with fibre A* satisfies:

1. L* is a concrete σ-complete OML with exactly the five named maximal
   blocks and trivial centre (the banked audited theorem, instantiated);
2. L* is **essentially irreducible** (Proposition 4(3): each piece P_γ has
   both sides uncountable in D);
3. the three inflated blocks are **state-coarse**: not countably generated
   (any countable generating family's countable sides touch only countably
   many pieces, leaving two pieces inseparable), and each carries the
   non-principal σ-additive state ν_∞ of Lemma 1;
4. ν_∞ extends to a **global** non-principal σ-additive two-valued state
   (combine the fibre-ν_∞ ultrafilter of A* with the q0-charging skeleton
   state and its banked finite extension across A10, A11; σ-additivity is
   blockwise: the two crossed blocks are finite, and on each inflated
   block the state is atom-free exactly as in Lemma 1);
5. L* is Φ-tame (the banked tameness proof works verbatim for A*: a finite
   trace charging q0 orients finitely many A*-events; their intersection
   is charged by the trace's fibre ultrafilter, hence nonempty; any carrier
   point there gives the σ-replacement).

Hence **𝒞 ∩ OML contains members with state-coarse blocks carrying global
non-principal σ-states: the coarse factor of Theorem 2 (B′(ii)) cannot be
discharged by proving coarse blocks away.** The §10d vacuity exit is
closed, negatively.

*Proof.* (1) is the audited theorem with A = A*. (2) by Proposition 4.
(3) inseparability: a countable family {E_n} ⊆ A* has index sets S_n
(countable or co-countable); the union of the countable ones among
{S_n, S_n^c} is a countable set S̄ ⊆ Γ; any two pieces with indices
outside S̄ belong to exactly the same E_n, so no σ-field generated by
{E_n} separates them, while A* does. ν_∞ ∈ St_σ(A*) by Lemma 1 with
Γ = ω₁ uncountable. (4) the banked state-extension argument
(`oml_exhaustive_boundary_survivor.md` §4, final gates) preserves
σ-additivity when the fibre ultrafilter is σ-additive; ν_∞ is. (5) is the
banked Φ-tameness argument, which uses only concreteness of A*. ∎

**Scope.** Theorem 5 does not weaken the conjecture and produces no
witness (L* is tame); it fixes the logical geography: B′(ii) is a real,
inhabited factor. Combined with §2, its tractable countable-type
sub-locus reduces to the relay engine; the residual open coarse locus is
non-countable-type.

## 5. Consequences and corrections banked

1. **`oml.construct.coarse_toy` is settled: inhabited** (by L*, Theorem
   5), conditionally on the banked inflation. The toy's original spec
   (coarse block, incompatible overlap, non-principal blockwise σ-state)
   is met: incompatibilities between diagonal fibre events and crossed
   q0-splitting events are exactly the [4×a₀]/[T×D] pairs of
   Proposition 4.
2. **A = ctble/coctble(ω₁) is the wrong coarse fibre for admissible
   constructions** (Proposition 4) — a fence for all future inflation
   design: check A/[countable] ≠ {0,1} FIRST.
3. **B′(ii) restatement direction:** split the coarse locus into
   countable-type (defect = free-on-countable; reduces to countable
   atom-killing = the relay problem, Corollary 3) and
   non-countable-type (open; the two-valued σ-state theory on
   non-atomic-mod-countable set σ-fields is the genuinely new ground).
   Next lemma-sized task there: exhibit a concrete σ-field of sets, not of
   countable type over atoms, carrying a non-principal two-valued σ-state
   whose defect class is NOT free-on-countable — or prove that every
   state-coarse σ-field of sets has countable-type defect anatomy over
   some atom partition.
4. **State-coarse ≠ not-countably-generated**: the countable-coordinate
   σ-field on 2^I (I uncountable) is not countably generated, yet every
   two-valued σ-state on it is Dirac (every event depends on countably
   many coordinates; the Dirac-realization argument applies through the
   countable sub-σ-field each event inhabits, determining ν = δ_x for the
   coordinate-consistent point x). B′(ii) should be indexed by
   state-coarseness.

## 6. Evidence ledger

| Claim | Class |
|---|---|
| Lemmas 1–2, Corollary 3 | hand proved (elementary, self-contained) |
| Proposition 4 (fence, iff) | hand proved over the banked normal forms |
| Theorem 5 (inhabitation) | hand proved, **conditional** on the audited arbitrary-base inflation theorem |
| §5(4) countable-coordinate remark | hand proved (elementary) |
| Relay-reduction reading (§2) | strategic reading, not a theorem beyond Corollary 3's statement |

No executable receipts: every claim is about uncountable structure with no
finite instantiation. Adversarial review owed at the next review
checkpoint.
