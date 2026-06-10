# Descent axis — what is actually open after the state-separation kill (2026-06-10)

*Single consolidated map of the descent-axis frontier, written after the L₂
dispersion-free/homomorphism state-separation was KILLED by `/audit full`
(parked to `covered_leads/`). Supersedes the scattered status across
`verification/inhabitation_check.md`, `verification/beta_swap_worksheet.md`,
and the two retired handoffs as the descent-axis entry point.*

> **HEADLINE (updated 2026-06-10, after reading Navara p. 428 directly):** the
> state-level separation is dead, BUT the **lattice-level (★) resolved YES** —
> L_MO₂ carries genuine non-distributive **descent structure**. This is the
> first forward motion on the descent axis since 2026-05-18. It is **NOT yet a
> contribution and NOT yet a falsification of the conjecture** — both hinge on
> one open question (is L_MO₂ concrete?) that `/audit full` will decide. Two
> results in one session, on different objects: a kill (state side) and a
> structural advance (lattice side). See the canonical statement next.

## ⓘ CANONICAL STATEMENT (the single source of truth — copy verbatim, do not re-improvise)

> **(★) resolves YES** (Navara 1992 p. 428, read directly 2026-06-10): L_MO₂
> carries genuine non-distributive **descent structure** — order, orthocomplement,
> and countable orthogonal join all restrict coordinatewise from W, so the witness
> `p = ⋁ₙ b|Cₙ` against the family `aₙ = a|Cₙ` satisfies `p∧aₙ=0` and `p⊀aₙ^⊥`.
> **This much is ESTABLISHED.**
>
> Whether this *falsifies* the conjecture "richness starves concreteness," AND
> whether it is a contribution at all, both hinge on the **SAME one open
> question: is L_MO₂ concrete?** The conjecture is a statement *about concrete
> OMLs*; (★) gives non-Boolean + σ-orthocomplete, but concreteness is unproven.
> The **horizontal-sum step is the crux**: V is a horizontal sum (pasting) of
> copies of T×MO₂, and pasting is exactly where states get destroyed (the
> Greechie mechanism Navara exploits with his *stateless* block). "Sub-OMP of
> concrete is concrete" covers the product and sublogic steps but **not** the
> horizontal sum. So concreteness is NOT free.
>
> **`/audit full`** (target: *is L_MO₂ concrete?*) decides everything downstream.
> If concrete → conjecture falsified AND a candidate contribution. If not →
> L_MO₂ is another L(H)-analogue, conjecture stands, no contribution.

## The axis, in one frame

The programme's surviving question (see `programme/genealogy.md`,
`programme/program_overview.md`) split into two axes:

- **Extension axis** (non-distributivity): does a state extend to a charge on
  the full clopen Boolean algebra of the dual? — **CLOSED on L(H)** (no state
  extends, n=4 witness; Type-5 impossibility). Done.
- **Descent axis** (σ-additivity / concentration on points): does a *concrete,
  σ-orthocomplete, non-Boolean* OML genuinely **exercise descent** — i.e. host
  point-free σ-additive probability on a natively non-distributive lattice?
  This is the live frontier and the only place a standalone contribution
  could still sit. Its novel content is *non-distributivity* (point-free
  σ-additive on distributive frames is already done — localic measure theory,
  Vickers/Simpson/Coquand–Spitters). So this axis serves curiosity (b), the
  incompatibility theorist, not (a). See the (a)/(b) fork in `genealogy.md`.

## Two questions live on this axis. One is dead, one is unresolved.

### 1. STATE-LEVEL separation (df-state vs 2-valued homomorphism) — DEAD

KILLED 2026-06-10. L₂ splits dispersion-free states from 2-valued
homomorphisms; the claim was Type-4 vocabulary / Paper II §5 refinement.
Audit verdict: clears no bar. df-state ≠ homomorphism is textbook (Kalmbach
1983 Chinese lantern, Pták–Pulmannová), σ-additivity is *free* here (eval
sees one block) so L₂ is decorative packaging on a finite MO₂ fact, and the
strict-point-free object is explicitly disclaimed (L₂ is concrete). 5th death
on the decorative-σ-additivity rock. Parked:
`covered_leads/l2_dispersion_free_homomorphism_separation.md`. The Paper II
§5 line-304 fix (df-state ≠ homomorphism) STANDS as an internal correction.

### 2. LATTICE-LEVEL inhabitation (the HINGE / "richness starves concreteness") — OPEN, and it is the real residue

**The binding question.** Is the refined descent-axis class *inhabited by a
witness that genuinely exercises descent*?

> **Conjecture (richness starves concreteness).** A concrete σ-orthocomplete
> OML with infinite pairwise-orthogonal families is Boolean — i.e. the class
> is empty / the open problem is vacuous.

The conjecture **as literally worded is FALSE** (Navara-over-MO₂ is concrete,
σ-orthocomplete, infinite-orthogonal, non-Boolean — closure proof is
state-free, verified structurally). The live content moved to a sharper
discriminator:

> **(★)** ∃ an element `p` and an *infinite* orthogonal family `{aₙ}` with
> `p ∧ aₙ = 0` for all `n`, yet `p ⊀ aₙ^⊥`.
>
> L(H) satisfies (★) (skew vector vs basis). MO_κ fails vacuously (no infinite
> orthogonal family). Whether the **MO₂-swap (L₂)** satisfies (★) is the
> outstanding by-hand check — the **HINGE**.

**The HINGE (the single open step):**
> In L₂, is `a|C ⊀ (b|C)^⊥`? (distinct non-complementary MO₂ atoms, same block
> C). YES ⟹ the witness `p = ⋁ₙ b|Cₙ` satisfies (★) ⟹ conjecture FALSE, L₂ is
> a concrete σ-orthocomplete non-Boolean OML exercising descent — the sought
> relational-probability object. NO ⟹ L₂ segregates (non-distributivity
> trapped in finite blocks, infinite orthogonal structure Boolean), and L(H)
> stays the lone witness.

## STATUS OF THE HINGE — (★) RESOLVED YES; concreteness STILL OPEN (Navara p. 428 read directly, 2026-06-10)

**The (★)/HINGE resolves YES — L_MO₂ carries genuine non-distributive descent
structure.** Settled by reading Navara 1992 p. 428 in full (the PDF is in
`notes/literature_review/literature/navara_1992.pdf`), which resolves the exact
join-faithfulness question the Lean axioms had only *encoded*. **This does NOT
yet falsify the conjecture** — see the concreteness caveat below; the conjecture
is about *concrete* OMLs, and concreteness is the open audit question.

**Why the worksheet's lean-NO was wrong — the support slip.** The earlier
by-hand worry was that `p = ⋁ₙ b|Cₙ` and `aₙ = a|Cₙ` live on disjoint blocks and
so are forced orthogonal. That is a misread of the witness's own support. `b|Cₙ`
(Navara's `v|C` notation, p. 428) attains value `b` **on** `Cₙ`. So at any
coordinate `m ∈ Cₙ`: `p(m) = b` and `aₙ(m) = a` — **same block, both nonzero.**
"Mutually disjoint" governs the family members among themselves (`aₙ ⊥ aₘ`,
n≠m), NOT `p` versus `aₙ`. They overlap on `Cₙ`, exactly where the MO₂ gap bites.

**(★) verified coordinatewise:**
- `p ∧ aₙ`: on `Cₙ`, `b ∧ a = 0` (MO₂); off `Cₙ`, `aₙ = 0`. So `p ∧ aₙ = 0`. ✓
- `p ≤ aₙ^⊥`? `aₙ^⊥` is `a^⊥` on `Cₙ`, `1` elsewhere. On `Cₙ`, `p = b`; need
  `b ≤ a^⊥`. MO₂ gap: `b ⊀ a^⊥`. So `p ⊀ aₙ^⊥`. ✓

So (★) holds in W, and the HINGE test `a|C ⊀ (b|C)^⊥` is the *right* test and is
satisfied — inside block `Cₙ`, where `p` and `aₙ` overlap.

**Transfer W → L is confirmed by p. 428, not left open.** All three operations
(★) touches restrict coordinatewise from W:
- L is built as a **sublogic of W** ⟹ order on L = restriction of W's order.
  There is no abstract "completion order" adding relations — the worksheet's
  item-2 worry was misframed.
- "L is closed under the formation of **orthocomplements in W**" (p. 428) ⟹
  `aₙ^⊥` is coordinatewise.
- The closure proof says verbatim "let `f` be its **join in W**" and proves it
  stays in L ⟹ countable *orthogonal* joins are the coordinatewise W-join. So
  the Lean's `navaraJoin` axiom **is faithful** — the precise risk flagged this
  session comes back confirmed, not broken. (Navara's "operations do not
  coincide with W" warning is about general meets/joins of non-orthogonal
  elements; it does NOT touch countable *orthogonal* joins, which the proof
  computes in W.)

Order, orthocomplement, and orthogonal-join all restrict from W ⟹ (★)-in-W
transfers to (★)-in-L. **HINGE = YES.**

**On statelessness, and why concreteness is NOT yet established (the crux).**
Navara's *original* block is a finite Greechie logic admitting NO states —
statelessness is load-bearing for *his* result, because it is what makes his L
the *non-concrete*, L(H)-analogue object. The MO₂-swap replaces the stateless
block with concrete/stateful MO₂ — the *correct* move, since we WANT
concreteness. The closure proof is state-free (verified), so L_MO₂ is a genuine
σ-orthocomplete non-Boolean OML. **But that does not make L_MO₂ concrete.**
Concreteness = an order-determining (separating) family of 2-valued states, and
the construction has a step that can *destroy* states: **V is a horizontal sum
(pasting) of copies of T×MO₂, and pasting is exactly the Greechie mechanism that
kills states.** "Sub-OMP of a concrete logic is concrete" covers the *product*
(`∏`) and *sublogic* (constancy-cut) steps — but **NOT the horizontal sum.** So
concreteness of L_MO₂ is **the open question**, not a free corollary of the swap.

**So the descent axis has a structural advance, NOT yet an inhabitant.** L_MO₂
satisfies (★) (non-Boolean + σ-orthocomplete descent structure — ESTABLISHED),
which is genuine forward motion and reverses the session's earlier "leans NO /
segregates" (that was a support-slip, now a primary-source resolution). But
"inhabits the *concrete* descent class" — the thing that would falsify the
conjecture and constitute a contribution — requires concreteness, which is
unproven. That is what the audit decides. (See the canonical statement at the
top of this file; this section is its long form.)

## THE NEXT MOVE — `/audit full` pointed at ONE question: is L_MO₂ concrete?

With (★) = YES, L_MO₂ has established non-distributive descent structure, but
the conjecture-falsification and the contribution both collapse to **one
unproven precondition: concreteness of L_MO₂.** So the audit is narrowly
pointed, not full-spectrum-diffuse. **DISCIPLINE: do not fold anything into
Paper II, do not call it a win, until `/audit full` resolves concreteness**
(opus Agent per [[feedback_audit_invocation]]). The asymmetry to guard against:
the state-separation got a skeptical referee and died; this lattice result must
get the same referee — it should not ride a green Lean checkmark, the more so
because the Lean *axiomatized* the construction (axiom-faithfulness is now
hand-verified against p. 428, but the *concreteness* and *contribution*
questions are untouched by Lean).

**Audit target + kill-risks, in priority order:**
1. **[PRIMARY — decides everything] Is L_MO₂ concrete?** Concreteness = an
   order-determining (separating, ideally 2-valued) family of states. The
   construction's risky step is the **horizontal sum**: V is a pasting of copies
   of T×MO₂, and pasting is the Greechie state-destroying mechanism. "Sub-OMP of
   concrete is concrete" covers the product (`∏`) and constancy-cut (sublogic)
   steps but **NOT** the horizontal sum. The audit must establish whether the
   horizontal sum of concrete T×MO₂ blocks keeps an order-determining state
   family, and whether the restriction to L still separates. YES → conjecture
   falsified AND a candidate contribution. NO → L_MO₂ is another L(H)-analogue,
   conjecture stands, no contribution.
2. **[SECONDARY — only if concrete] Novelty vs. localic / Navara.** Same family
   as the arc's prior 5 deaths: *"localic measure theory already does point-free
   σ-additive probability — is the non-distributive instance genuinely new, or a
   decorative variation on Navara with the block swapped?"* The contribution must
   do something localic/distributive point-free measure theory provably *cannot*
   (host σ-additive probability on a natively non-distributive event lattice).
3. **[TERTIARY] Already named/published?** Pták–Pulmannová, Gudder, Navara,
   Cannon–Döring — has someone already exhibited a concrete σ-orthocomplete
   non-Boolean OML with (★), or settled the conjecture?

If concreteness clears (and novelty survives): a genuine descent-axis
contribution and the first live standalone lead since 2026-05-18 — route per the
audit (Paper II §5/§6, or a short standalone). If concreteness fails: park to
`covered_leads/`. Note (★) = YES means it does NOT *segregate* — a kill here is a
concreteness/novelty kill, not the old segregation one; the *degeneration*
picture (below) is then the salvage.

## The degeneration picture (holds under EITHER HINGE verdict)

Worth recording independent of the HINGE: finite truncations `L₂^(N)` are
quantum + stateful; the map `L₂^(N) → L₂` (N→∞, σ-orthocompleted) is where the
finite-stage probability tables and the MO₂ gap either stay married (HINGE YES:
gap survives to the limit, `p` is the witness) or divorce (HINGE NO: the limit
Boolean-izes, gap dies in the passage — an explicit picture of σ-additivity
destroying non-distributivity, the descent obstruction made visible). The NO
branch is not a dead end: it would upgrade "one example (L(H))" into "a
mechanism" — the σ-orthocompletion device provably *needs* state-poverty.

## ROUTING / next move (the user's call, no rush)

(★) = YES is forward motion (structure established), but the descent axis does
NOT yet have a confirmed contribution or a falsified conjecture — both wait on
concreteness. The next move is the audit gate, narrowly pointed.

1. **THE NEXT MOVE — `/audit full` pointed at "is L_MO₂ concrete?"** (opus Agent,
   per [[feedback_audit_invocation]]). PRIMARY target = concreteness (the
   horizontal-sum crux); SECONDARY = novelty vs localic/Navara; TERTIARY =
   already-published. (See the audit-target section above.) Decide-after-audit;
   do NOT pre-place into a paper.
2. **If concreteness clears (and novelty survives):** then — and only then — a
   genuine descent-axis contribution, the first live standalone lead since
   2026-05-18; serves curiosity (b) (incompatibility theorist). Route per audit
   verdict — Paper II §5/§6 refinement or a short standalone note. A Lean
   companion proving concreteness would be new content (the current suite only
   axiomatizes Navara's construction).
3. **If concreteness fails:** park to `covered_leads/`. Would be the arc's 6th
   death, but for a *different* reason than the prior 5 — not decorative-σ ((★)
   makes the descent structure genuinely live), but concreteness-fails (the
   horizontal sum starves states, i.e. "richness starves concreteness" turns out
   TRUE after all, with L_MO₂ as one more L(H)-analogue).
4. **The (a)/(b) fork still stands underneath** (`genealogy.md`): even if this
   clears, it is a (b) result. If the user is really an (a) — anti-smuggler —
   then CE/Paper I already delivered, and **Strategy D** (ZFC-independence of a
   measure-free Boolean algebra, `papers/paper_i/notes/ultralimit_investigation/`)
   is the more faithful continuation. The descent win, if real, does not by
   itself settle which curiosity is driving.
5. **Empirical-reconnection arc:** dead 5×, same decorative-σ rock. Not a route.

## SOURCES / ARTIFACTS
- `verification/inhabitation_check.md` — full HINGE derivation history (the
  (★) discriminator, the two near-misses L(H)/Navara, the segregation analysis).
- `verification/beta_swap_worksheet.md` — the by-hand (★) attempt; leans NO,
  localizes the gap to closed-join + completion-order (items 1–2 §4).
- `formalization/QuerySystem/QuerySystem/DescentWitness{Finite,Infinite,Consistency,Closure}.lean`
  — 0 sorry. Proves (★) from `Sub` + `navaraJoin` axioms (gap → `MO2.gap`). The
  axioms encode the HINGE answer; **their p. 428 faithfulness is now hand-verified
  (2026-06-10): `navaraJoin` IS the coordinatewise W-join (closure proof computes
  the join in W), `Sub` IS the restricted order.** Lean axioms confirmed faithful.
- **Primary, READ DIRECTLY 2026-06-10: Navara 1992 (PAMS 115), p. 428** —
  `notes/literature_review/literature/navara_1992.pdf`. Construction: block =
  finite Greechie *stateless* logic S; U=T×S (one S-blind state); L = sublogic of
  W=∏V cut by constancy; closure proof computes orthogonal joins IN W
  (coordinatewise); "operations don't coincide with W" is about non-orthogonal
  meets/joins, not orthogonal joins. MO₂-swap replaces stateless S with concrete
  MO₂ — the closure proof is state-free so it survives; statelessness was
  load-bearing only for Navara's non-concreteness, which the swap deliberately
  drops. Also: Pták–Pulmannová 1994; Kalmbach 1983.
- Memory: [[oml_descent_inhabitation]], [[l2_dispersion_free_homomorphism_separation]]
  (killed), [[oml_relational_prob_novelty]] (occupied-terrain prior),
  [[oml_two_point_spaces]].
