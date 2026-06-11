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

## UPDATE 2026-06-08 — the MO₂ swap resolves, but as a SEGREGATED fake; conjecture needs an irreducibility clause

Triggered by the question "is there a finite-cofinite analogue on OMLs?"
(session 2026-06-08). The chain: finite-cofinite charge → its OML analogue
is **Boolean (decorative)** because σ-additivity only ever sees countable
*orthogonal* families, and a pairwise-orthogonal family generates a Boolean
subalgebra (Kalmbach) — so σ-additivity failure is intrinsically
within-block/Boolean (the L(H)/MASA/singular-state realization is the
finite-cofinite charge verbatim). The ultraproduct/Łoś toolkit re-enters not
on the charge (job A, decorative) but as a **diagnostic** on the inhabitation
conjecture. Running that diagnostic on the proposed MO₂ swap settles the
"unrun check" above — in the **segregation** direction, not the attack one.

### The MO₂-block σ-orthocompleteness check — RUN (structurally), survives

Navara's closure-under-countable-orthogonal-joins proof (p. 428) is **state-
free**: orthocomplement-stays-in-block (horizontal sum) + the constancy
condition + coordinatewise join. State-poverty enters **only** the final
non-concreteness paragraph (`{v|C}` admits one state). The one step that
could break under the swap — "`f_j(m)=0`, `f_i ⊥ f_j ⇒ f_j` constant `(=0)`
on C" — carries verbatim: in MO₂ the only elements `≤ a^⊥` are `{0, a^⊥}`,
so the nonzero case is still killed by constancy. **σ-orthocompleteness
survives the MO₂ swap.** Concreteness is free (products/sub-OMPs of concrete
logics are concrete).

The standing note (line 123–128) flagged the block-collapse to `{a,a^⊥}` as a
**possible threat to closure**. That was backwards: it is not a threat to
closure — it is a **forced segregation** (see next).

### But it survives VACUOUSLY — the swap is a segregated reducible fake

MO₂ is **finite** ⟹ no infinite orthogonal family fits inside one block ⟹
every infinite orthogonal join must come from **disjoint supports across M**,
and disjoint-support orthogonality is **Boolean**. Consequence:

- the infinite-orthogonal structure (where σ-additivity lives) is entirely
  Boolean — a `2^M`-style support skeleton;
- the non-distributivity (`a|C` vs `b|C`: meet-zero ≠ orthogonal pairs) is
  **confined to finite blocks that never enter an infinite orthogonal join**.

This is **exactly** the "segregated Boolean-factor vs MO₂-factor"
configuration the decision criterion (line 131–133) was written to **exclude**
as a non-genuine inhabitant. It is the **MO_κ disease one level up**: MO_κ
failed by having *no* infinite orthogonal families; the swap fails by having
infinite-but-*Boolean* ones. So the swap does **not** fire the attack branch.

### The discriminator (CORRECTED 2026-06-08) — element-vs-family, not within-family

**Earlier draft of this note used a vacuous probe** ("exhibit an orthogonal
family containing a meet-zero≠orthogonal pair"). That is impossible in
*every* OML — an orthogonal family generates a Boolean subalgebra (Kalmbach),
where meet-zero *is* orthogonality — so it holds in L(H) too and discriminates
nothing. The "by definition" exclusion was the tell. **Discard it.**

The interleaving that actually separates the segregated swap from the genuine
witness is **element-versus-family**:

> **(★)** ∃ an element `p` and an *infinite* orthogonal family `{aₙ}` with
> `p ∧ aₙ = 0` for all `n`, yet `p ⊀ aₙ^⊥` (`p` not orthogonal to any `aₙ`).

- **L(H): (★) holds.** Basis `{eₙ}`, skew vector `f = Σ cₙ eₙ`, all `cₙ ≠ 0`:
  ray `P_f` meets each `P_{eₙ}` at `0` but is orthogonal to none.
- **MO_κ: fails vacuously** (no infinite orthogonal family) — correctly excluded.
- **MO₂-swap: (★) is NOT blocked by constancy — explicit candidate witness
  exists (2026-06-08, worked from Navara p.428).** Elements of L are
  `⋁_{C∈ℱ} v_C|C`, ℱ mutually disjoint (p.428); infinite orthogonal family ⟹
  infinitely many disjoint `Cₙ` (MO₂ caps within-block orthogonal families
  at 2). MO₂ atoms `a,a^⊥,b,b^⊥`, `a∧b=0`, `a⊀b^⊥`. Set `aₙ:=a|Cₙ`,
  `p:=⋁ₙ b|Cₙ`. Constancy is **per-coordinate**, `Cₙ` disjoint ⟹ `p` violates
  nothing; `p∈L` as a countable disjoint-support (orthogonal) join — supplied
  by σ-orthocompleteness itself. In W: `p∧aₙ=0`, `p⊀aₙ^⊥`. **(★) holds in W.**

  **SOLE OPEN STEP — does it transfer to L?** Navara: "lattice operations in L
  do not coincide with those of W" (p.428). Orthogonality is via the
  orthocomplement. Reduces to one check:

  > **(HINGE)** In L, is `a|C ⊀ (b|C)^⊥`? (distinct non-complementary MO₂
  > atoms, same C, non-orthogonal in L inheriting from MO₂)

  - HINGE holds ⟹ `p` witnesses (★) ⟹ swap is concrete σ-orthocomplete
    non-Boolean satisfying interleaving ⟹ **conjecture FALSE**, swap IS the
    relational-probability object.
  - L's orthocomplement forces `a|C ⊥ b|C` ⟹ swap **segregates**, L(H) stays
    the only known witness.

  **Lean update:** prior framing ("open by an element in MO₂-position in ∞
  blocks") is RESOLVED — constancy *permits* it. The live hinge is the
  orthocomplement check (HINGE), not the support count. **(HINGE) not yet run**
  (Phase 4 = user's call). The verdict now leans FALSE-conjecture (witness
  exists in W, only an L-orthocomplement subtlety stands between it and (★)).

**Do NOT use the word "irreducible"** for the sharpened hypothesis. As a
technical term it means trivial center, and Navara's horizontal-sum
construction is center-irreducible — so "irreducible" would *not* exclude the
swap. (★) sidesteps the center question entirely; use (★), not a one-word
hypothesis.

### Net: the conjecture SHARPENS — neither attack nor park

1. **The class as stated IS inhabited.** σ-orthocompleteness survives the
   swap (closure proof state-free, see above), so the MO₂ swap is concrete,
   σ-orthocomplete, infinite-orthogonal, and non-Boolean — all four stated
   hypotheses. The "richness starves concreteness" conjecture as literally
   worded (no concrete member exists) is therefore **false**; what the swap
   may still be is a *segregated* member, not a strong-descent witness.
2. **The sharpened question is the (★) interleaving condition** (above), NOT
   an "irreducibility" clause (that word is wrong — Navara's horizontal sums
   are center-irreducible). Restated:

   > Does a concrete σ-orthocomplete non-Boolean OML satisfy (★) — an element
   > meet-zero-but-not-orthogonal to an *infinite* orthogonal family? L(H)
   > does; MO_κ does not; whether the MO₂-swap does is the **outstanding
   > by-hand check**.

3. **A candidate (★)-witness for the MO₂-swap EXISTS in W** (`p = ⋁ₙ b|Cₙ`,
   see the discriminator section). It satisfies (★) coordinatewise in W and
   lies in L by σ-orthocompleteness. The only gap is whether MO₂-orthogonality
   transfers to L's orthocomplement — the **(HINGE)** check. So the verdict now
   **leans conjecture-FALSE**: the witness is built; only an L-orthocomplement
   subtlety stands between it and (★). This reverses the earlier provisional
   lean ("likely segregates").

**Status: OPEN, reduced to the single check (HINGE)** — is `a|C ⊀ (b|C)^⊥` in
L? One yes/no decides everything: YES ⟹ conjecture false, swap is the
relational-probability object; NO ⟹ swap segregates, L(H) stays the lone
witness. Not a park; orthogonal to the four parked empirical-reconnection
seeds.

> **⊳ SUPERSEDED 2026-06-10 — see the resolution box below and the canonical
> statement in `../../covered_leads/descent_axis_residue_post_kill.md` (now
> PARKED). The HINGE resolved YES, but the deciding question turned out to be
> CONCRETENESS, not the HINGE — and concreteness resolved YES with the lead
> dying anyway on triviality + prior-art (Pták–Pulmannová 1994).**

*(Caveat on the "sharpen" outcome per `feedback_research_workflow` lifecycle:
the standing MO₂-swap-survival check DID flip — σ-orthocompleteness survives,
inhabitation-as-stated confirmed — and the (★) clause excludes the old
segregated instance, so this clears the sharpen guardrail. But the (★) check
itself is unrun; the segregation verdict is provisional, not settled.)*

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

---

## RESOLUTION 2026-06-10 — (★)/HINGE = YES, but CONCRETENESS is the real deciding question

Read Navara 1992 p. 428 **in full and directly** (not just the closure
paragraph). Two corrections to everything above:

**1. The HINGE resolves YES — and the prior "leans NO / segregates" was a
support-slip.** The worry that `p = ⋁ₙ b|Cₙ` and `aₙ = a|Cₙ` sit on disjoint
blocks (forcing orthogonality) misread the witness: `b|Cₙ` attains value `b`
*on* `Cₙ`, so at `m∈Cₙ`, `p(m)=b` and `aₙ(m)=a` — **same block.** "Mutually
disjoint" governs `aₙ ⊥ aₘ`, not `p` vs `aₙ`. The within-block MO₂ gap gives
`p∧aₙ=0`, `p⊀aₙ^⊥`. (★) holds in W. **Transfer W→L is confirmed by p. 428**
(not open as line 264 claimed): L is a *sublogic of W* (order = restriction),
closed under orthocomplements *in W*, and the closure proof computes orthogonal
joins *in W* (coordinatewise). So order/orthocomplement/orthogonal-join all
restrict from W ⟹ (★) transfers. The Lean `Sub`/`navaraJoin` axioms are faithful.

**2. But (★) = YES does NOT settle the conjecture — CONCRETENESS does, and it is
OPEN.** The conjecture "richness starves concreteness" is about *concrete* OMLs.
(★) gives non-Boolean + σ-orthocomplete descent structure, but **not**
concreteness. Navara's block is Greechie STATELESS *precisely* to make his L
non-concrete; the MO₂-swap drops statelessness to *try* for concreteness — but
the **horizontal-sum step** (V = pasting of T×MO₂ copies; pasting is the Greechie
state-destroying mechanism) is exactly where it can fail. "Sub-OMP of concrete is
concrete" covers the product (`∏`) + sublogic (constancy-cut) steps, NOT the
horizontal sum. So concreteness is the open question.

**Net (RESOLVED 2026-06-10):** the deciding question moved from the HINGE (YES)
to **concreteness of L_MO₂**, and `/audit full` settled it: L_MO₂ **IS** concrete
(conjecture FALSE as worded), but the lead is **DEAD** anyway — the witness is
trivial (plain ∏ₙ MO₂ has the whole bundle) and the Boolean-forcing boundary was
already characterized (Pták–Pulmannová 1994: *subadditivity*, not σ-additivity).
Also corrected: V is a Kalmbach horizontal sum (glued at {0,1}), NOT Greechie
atom-sharing, so statelessness — not the horizontal sum — was the only obstruction
to concreteness. Parked. Canonical statement (parked):
`../../covered_leads/descent_axis_residue_post_kill.md`.
