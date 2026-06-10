# Descent axis — what is actually open after the state-separation kill (2026-06-10)

*Single consolidated map of the descent-axis frontier, written after the L₂
dispersion-free/homomorphism state-separation was KILLED by `/audit full`
(parked to `covered_leads/`). Supersedes the scattered status across
`verification/inhabitation_check.md`, `verification/beta_swap_worksheet.md`,
and the two retired handoffs as the descent-axis entry point.*

> **HEADLINE (updated 2026-06-10, after reading Navara p. 428 directly):** the
> state-level separation is dead, BUT the **lattice-level HINGE resolved YES** —
> `L_MO₂` is a concrete σ-orthocomplete non-Boolean OML that genuinely exercises
> descent ((★) holds; "richness starves concreteness" is FALSE as worded). This
> is a **live candidate contribution — the first since 2026-05-18 — pending
> `/audit full`.** Two opposite results in one session: a kill (state side) and
> an inhabitation (lattice side). They are NOT the same object.

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

## STATUS OF THE HINGE — RESOLVED YES (Navara p. 428 read directly, 2026-06-10)

**The HINGE resolves YES. The "richness starves concreteness" conjecture is
FALSE as worded.** Settled by reading Navara 1992 p. 428 in full (the PDF is in
`notes/literature_review/literature/navara_1992.pdf`), which resolves the exact
join-faithfulness question the Lean axioms had only *encoded*.

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

**On statelessness (the one thing that looked like a violation, but isn't).**
Navara's *original* block is a finite Greechie logic admitting NO states — and
statelessness is load-bearing for his result, because it is what makes his L the
*non-concrete*, L(H)-analogue object. The MO₂-swap deliberately replaces the
stateless block with concrete/stateful MO₂. That is the *correct* move, because
we WANT concreteness — statelessness was load-bearing only for the property
we are trying to avoid. The closure proof is state-free (verified), so
`L_MO₂` is a genuine concrete σ-orthocomplete OML.

**So the descent axis is INHABITED:** `L_MO₂` is a concrete, σ-orthocomplete,
non-Boolean OML satisfying (★) — it genuinely exercises descent. This reverses
the session's earlier "unsure"; it is not another oscillation but a primary-
source resolution (the p. 428 read is new evidence and points one way).

## THE CANDIDATE IS NOW ACTIVE — and needs `/audit full` BEFORE it is called a win

With the HINGE = YES, the result —
> *`L_MO₂` is a concrete, σ-orthocomplete, non-Boolean OML hosting point-free
> non-distributive σ-additive probability (descent genuinely exercised, (★)
> satisfied)*
— is a **candidate contribution, and a bigger one than the state separation
just killed today.** It has NOT had a hostile audit. **DISCIPLINE: do not fold
it into Paper II, do not call it a win, until it clears `/audit full`** (opus
Agent per [[feedback_audit_invocation]]). The asymmetry to guard against: the
state-separation got a skeptical referee and died; this lattice result must get
the same referee — it should not ride a green Lean checkmark to acceptance, the
more so because the Lean *axiomatized* the construction (faithfulness now
hand-verified against p. 428, but the *contribution* question is untouched by
Lean).

**What the audit must verify hardest (the load-bearing kill-risks):**
1. **Concreteness of `L_MO₂` — the single load-bearing claim.** The whole result
   is "*concrete* σ-orthocomplete non-Boolean exercising descent." The
   concreteness rests on "products and sub-OMPs of concrete logics are concrete"
   (MO₂ concrete per `concrete_meetzero_vs_orthogonal.py`). The audit must check
   that `W = ∏(horizontal sum of T×MO₂)` is genuinely concrete AND that the
   restriction to L still has an order-determining (separating, ideally
   2-valued) family of states. If concreteness fails, `L_MO₂` is just another
   L(H)-analogue and the result collapses.
2. **Novelty vs. localic / Navara.** Likely-kill, same family as the arc's prior
   5 deaths: *"localic measure theory already does point-free σ-additive
   probability — is the non-distributive instance genuinely new content, or a
   decorative variation on Navara's construction with the block swapped?"* The
   contribution must be a witness that does something localic/distributive
   point-free measure theory provably *cannot* (host σ-additive probability on a
   natively non-distributive event lattice). The conjecture being false-as-worded
   is NOT yet the contribution.
3. **Is "concrete σ-orthocomplete non-Boolean OML exercising (★)" already
   named/published?** Pták–Pulmannová, Gudder, Navara himself, Cannon–Döring —
   has someone already exhibited exactly this object or proved the class
   nonempty? (The conjecture may be folklore-false.)

If it clears: this is a genuine descent-axis contribution and the first live
standalone lead since 2026-05-18 — route per the audit (Paper II §5/§6, or a
short standalone). If it dies on concreteness or novelty: park to
`covered_leads/`, and the *segregation/degeneration* picture (below) becomes the
salvage — but note the HINGE being YES means it does NOT segregate, so a kill
here would be a novelty/concreteness kill, not a segregation one.

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

The HINGE is now settled YES, so the descent axis has, for the first time since
2026-05-18, a **live candidate**. The next move is no longer a derivation — it is
the audit gate.

1. **THE NEXT MOVE — `/audit full` on the `L_MO₂` descent-witness result**
   (opus Agent, per [[feedback_audit_invocation]]). Target = "*`L_MO₂` is a
   concrete σ-orthocomplete non-Boolean OML exercising descent ((★)), hosting
   point-free non-distributive σ-additive probability*." Kill-risks 1–3 above;
   the load-bearing one is **concreteness of `L_MO₂`**. Decide-after-audit; do
   NOT pre-place into a paper.
2. **If it clears:** first standalone lead in ~3 weeks; serves curiosity (b)
   (incompatibility theorist). Route per audit verdict — Paper II §5/§6
   refinement or a short standalone note. Consider a Lean companion making the
   concreteness explicit (the current suite axiomatizes Navara; a concreteness
   proof would be new content).
3. **If it dies (concreteness or novelty):** park to `covered_leads/`. Would be
   the arc's 6th death, but for a *different* reason than the prior 5 (not
   decorative-σ — the HINGE makes σ-additivity genuinely live here; the kill
   would be concreteness-fails or localic-already-does-it).
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
