# Inhabitation of the descent-axis stage — orientation finding (2026-06-05)

**Binding question (refined three times this session):** does there exist a
*concrete, infinite, non-Boolean, σ-(ortho)complete OML with non-trivial
countable orthogonal structure and meet-zero≠orthogonal pairs*? I.e. an
inhabitant that actually **exercises the descent axis**, not merely a member
of the class.

This is the go/park hinge for the descent-axis residue (survey §5–§6). If
the refined class is inhabited by a workable example, the thesis-advisor
consult is "how to attack the ideal mechanism." If provably empty, that is a
clean citable park (the open problem is vacuous). **Result: still open, with
two independent near-misses pointing toward possible emptiness.**

## Why the obvious candidates fail (each dodges the frontier)

The refinement was forced by two false starts, each caught by
verify-by-building:

1. **MO₂ / finite concrete (Ex 2.8).** Concrete and non-Boolean, but
   *finite* — descent vacuous. The uniform set-measure is a genuine state
   yet does NOT extend to a charge: `{a₁,a₁ᶜ,a₂,a₂ᶜ}` is pairwise
   *meet-zero* (cross-pairs share a point, so not disjoint, but no nonzero
   L-member fits inside) with Σs = 2 > 1 — the same obstruction as L(H).
   Concreteness does **not** rescue extension. (`/tmp` check, archived
   reasoning.)

2. **MO_κ, κ infinite.** Concrete, infinite, non-Boolean, lattice-complete.
   But its *entire* non-Booleanness is the meet-zero/orthogonal gap (the
   **extension** axis). Max pairwise-orthogonal family of nonzero elements =
   **2** ({a, a^⊥}, since a⊥b among atoms iff a=b^⊥). So **no non-trivial
   countable orthogonal joins**: σ-additivity = finite additivity, descent
   **vacuous**. And MO_κ ⊇ MO₂ ⟹ Σ=2 obstruction ⟹ no state extends, as on
   L(H). Inhabits the class, exercises only the closed axis.

**Lesson (the refinement):** class membership ≠ relevance. The inhabitant
must carry *non-trivial countable orthogonal structure* (so σ-additivity is
live) AND *meet-zero≠orthogonal pairs* (non-Boolean in the descent-relevant
way). Orthogonal richness is exactly what forced L(H) non-concrete (KS,
Rmk 4.1) — so richness + concreteness is the genuine open frontier.

## Navara 1992 — the real near-miss (primary source read)

`navara_1992.pdf`, "Regularity and σ-additivity of states on quantum
logics," PAMS 115. Constructs L as a sublogic of ∏_{m∈M} V (M countable, V
= horizontal sum of copies of U = T×S; T={0,1} trivial, S a Greechie
*stateless* logic), via the constancy condition. Navara proves:

- L is **σ-orthocomplete** (countable orthogonal joins exist — non-trivial
  countable orthogonal structure ✓, unlike MO_κ);
- L is a **lattice** (OML, explicit: "Notice also that L is a lattice");
- **infinite, non-Boolean** ✓;
- admits states (regular ones), some **not σ-additive** — the paper's point.

This *looks* like an inhabitant. **It is not — it is non-concrete**, for a
*state-theoretic* reason, and that is exactly the frontier property.

### Non-concreteness of Navara's L (airtight version)

NOT "L inherits S-stateless blocks" — that is false (Navara exhibits states
on L; and he warns "the lattice operations in L do not coincide with those
of W", so S-as-sublogic-of-L cannot be assumed). The correct argument runs
through the **state space**, read off Navara p. 428:

- U = T×S admits **exactly one** state ω, and it is **S-blind**: ω(t,s)
  depends only on t (S is stateless, so the only state on T×S is pulled
  back from T's unique state via projection).
- Every state of L restricts, block-wise, to this unique S-blind state.
- L contains two distinct elements differing only in an S-coordinate within
  a block — e.g. v₁|C, v₂|C with constant value (1,p) vs (1,q) for distinct
  atoms p,q of S (constancy condition permits f(m)∈U_C\{0,1}, m∈C, f
  constant on C). **Verified** (`navara_separation_check.py`).
- Hence **no** state of L separates v₁|C from v₂|C ⟹ no order-determining
  family of states, a fortiori none two-valued ⟹ **L is NOT concrete**
  (Gudder's set-representability criterion).

So Navara is the **σ-orthocomplete analogue of L(H)**: infinite,
non-Boolean, rich countable orthogonal structure, σ-(ortho)complete —
everything *except* concreteness. A near-miss missing **exactly** the
frontier property.

### Completeness notion: σ-orthocompleteness is the relevant one

Survey §5 says "σ-*complete*"; Navara proves σ-*orthocomplete* (countable
*orthogonal* joins only). This gap does **not** matter for inhabitation:
σ-additivity, `s(⋁ₙaₙ)=Σₙs(aₙ)` for orthogonal {aₙ}, touches only countable
*orthogonal* joins, so σ-orthocompleteness is the notion the *probabilistic*
question requires. (Full σ-completeness is what the Loomis–Sikorski
representation manipulates structurally, strictly stronger.) Navara
satisfies the probabilistically-relevant completeness — so **concreteness is
the only gap**, confirming Navara as a clean near-miss rather than a
member-failing-on-two-axes.

*Recommend recording in the survey: the open problem should pose
σ-**ortho**completeness (or note σ-completeness is the structural, not the
measure-theoretic, requirement).*

## Standing finding (the honest orientation deliverable)

> **Conjecture (richness starves concreteness).** A concrete (set-
> representable) σ-orthocomplete OML with infinite pairwise-orthogonal
> families is Boolean — equivalently, the refined descent-axis class is
> empty.

**The two near-misses do NOT share a mechanism — the conjecture rests on
ONE example, not two** (corrected after the first pass conflated them):
- **L(H):** the orthogonal richness *itself* causes state-poverty — KS
  coloring obstruction (dim≥3 orthogonality forbids any consistent {0,1}
  assignment). Genuine evidence for the conjecture.
- **Navara:** non-concreteness traces to the imported *finite,
  orthogonality-free* Greechie-stateless block S; the infinite orthogonal
  richness is bolted on **separately** by the M-indexed product/constancy
  machinery. State-poverty and richness have *different sources* — Navara
  is **not** evidence for the conjecture.

**So Navara is a construction template, not evidence for emptiness.** Rerun
its product/constancy machinery over a *concrete, stateful, non-Boolean*
block — **MO₂** (concrete per `concrete_meetzero_vs_orthogonal.py`).
Products and sub-OMPs of concrete logics are concrete (order-determining
states of the ambient restrict, orthogonality inherited), so the swap is
concrete *for free* — testing concreteness by enumeration is uninformative
(and a finite-M enumeration would re-run the MO₂ finite trap: no infinite
orthogonal families). **The binding check is whether σ-orthocompleteness
survives the swap** — Navara's closure step (p. 428: `fₙ(m)≤f(m) ⟹ constant
on C`) leaned on T×S's orthocomplement structure; with MO₂ blocks the
orthogonal contributors on a block collapse to a single complementary pair
{a,a^⊥}, so the constancy/global-join step needs by-hand re-derivation at
infinite M. **Not yet run.**

**Decision is pending this check — do not lean park:**
- σ-closure survives + genuinely non-Boolean (meet-zero≠orthogonal pairs
  present, not segregated Boolean-factor vs MO₂-factor) ⟹ refined class
  **inhabited**, conjecture **false**, flip to **attack**.
- σ-closure fails *because* MO₂'s states obstruct the constancy step ⟹ the
  closure device provably **needs** state-poverty — upgrades "one example"
  into "a mechanism," stronger than the current state. (Not a dead end.)

**Status:** inhabitation **OPEN**, decided by the unrun MO₂-block
σ-orthocompleteness check (by hand, infinite M). Per CLAUDE.md Phase 4,
attempting that derivation is the user's call.

## Cross-references / corrections applied this session
- Survey §4.2 **mis-citation fixed** (both .md and .tex): Pták–Pulmannová
  1994 is a *finitary* subadditive-unitality→Boolean theorem (Theorem 1,
  lattice-only; OMP version false by Müller's set-representable
  counterexample), **not** "σ-additivity collapses to Boolean." No countable
  joins anywhere in PP 1994. Now cites `PtakPulmannova1994` (was the 1991
  book).
- Primary sources read: `ptak_pulmannova_1994.pdf`, `navara_1992.pdf`.
- Verification: `navara_separation_check.py` (the load-bearing separation
  fact).
