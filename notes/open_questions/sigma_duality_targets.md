# The two targets of the missing σ-duality: what is forced, what is free

*Working note, 2026-06-22. Continues the faithfulness trichotomy now in the
survey (`oml_onboarding.tex`, after `thm:floor`) and `sigma_essential_prior_art_verdict.md`.
The user, having seen why route (c) — a σ-Loomis–Sikorski for concrete OMLs — is
the live route, asked: **what are the exact targets on either side of that
duality?** This note decomposes both sides into FORCED structure (derivable from
constraints already established) and the one UNFORCED clause. The upshot (revised
after advisor): the left side is fully determined; the right side, once the functor
is fixed to the Gudder/concrete-logic one, is **also** pinned (= Derr–Williamson's
σ-Dynkin-systems, inhabited) — so the open problem is not "what is the right-side
category" but the single clause (iii): does the σ-additive *measure* descend onto
the physical points carrying contextuality, off the Polish-realizable case.*

> **VERDICT (2026-06-22, revised after advisor).** The duality sought is
> $$\sigma\text{OML}_{\mathrm{conc}} \;\simeq\; \mathbf{?}$$
> **Left side — SETTLED:** concrete σ-complete (non-Boolean) OMLs, with
> σ-homomorphisms. Every clause forced; no freedom. (= Derr–Williamson
> Dynkin-systems, in the realized case.)
> **Right side — NARROWER THAN it first looks, and already pinned.** The naive
> first guess "measurable space" is killed by the Floor (forces Boolean). But the
> *correct* right-side object under the natural functor — a **concrete logic /
> σ-Dynkin-system of sets** (Gudder, set-complement, orthogonal joins = disjoint
> unions) — is **inhabited and known**: it is exactly Derr–Williamson's category,
> and `∏ₙMO₂` is a living example satisfying it. So conditions (i)+(ii) below are
> NOT the open frontier — they are settled (`rem:concrete`: disjoint-union-closure
> ≠ intersection-closure, so no Floor collapse).
> **The genuinely open edge is condition (iii): is the σ-additive state `w` a
> barycentre of a σ-additive measure on the DISPERSION-FREE states `S_df^σ`** —
> i.e. `w ∈ conv̄(S_df^σ)` (`lem:relational`) — off the regular-realizable case.
> That is the `rem:dw` residue **verbatim** (STABLE; this note restates it, does not
> move it). **CRITICAL (audit 2026-06-22):** the descent space is `S_df^σ`, NOT the
> principal-filter points `P(A)`. The survey is explicit — contextuality "is a
> condition on the dispersion-free states, not on `P(A)`; `P(A)` is *permitted*"
> (`rem:AB`, three-space ¶). Landing (iii) on `P(A)` is the σ-form of the (A)/(B)
> equivocation `rem:AB` warns against; `S_df^σ` is the only correct target.
> `∏ₙMO₂` shows why (iii) bites where (ii) doesn't: it satisfies (i),(ii), even has
> σ-additive states, yet its contextual states are *finitely*-additive (diffuse on
> the central `P(ℕ)`) and σ-additivity washes them out. The bite is **(iii) +
> contextuality**, not the representation.

---

## 1. The left side is forced

The algebra-side object is pinned down with no slack — each clause traces to a
constraint already in the survey:

| Component | Target | Forced by |
|---|---|---|
| carrier | σ-complete OML `L` | `⋁ₙ aₙ` must exist to *state* σ-additivity (`def:complete`) |
| + | **concrete** (order-determining 2-valued states) | non-concrete = `L(H)` = excluded pole (KS, no points; `rem:miss`(i), `rem:AB`) |
| + | **non-Boolean** | else the duality is just Loomis–Sikorski |
| morphisms | **σ-OML homs** (preserve countable orthogonal joins) | functoriality must hold *for the σ-structure*, not only finitely (`rem:finitary`) |

Write `σOML_conc` for the category. Identification with prior art: Derr–Williamson's
**Dynkin-systems** are exactly the *realized* objects of `σOML_conc` (concrete
σ-complete OMLs presented as countable-disjoint-union-closed families of Borel
sets); their **pre-Dynkin-systems** are the finitary (OMP) shadow. So the left
side is not only forced but already named in the literature. No open content here.

## 2. The right side: what the Floor forces, which functor to pick, what is left open

The space-side object's *identity* turns out to be known once the functor is fixed
(§2b–2c); the only open clause is the measure descent (§2d). First, the features
the Floor forces on any candidate:

### 2a. FORCED (by the Floor + the finitary obstruction)

1. **Not a plain measurable space.** A measurable space is a σ-tribe of honest
   sets; honest sets distribute; so by the Universal Floor (`thm:floor`) any
   ⋀,⋁→∩,∪ representation forces `L` Boolean. The non-distributivity must live
   *somewhere* on the space side — not in the sets. The two functors of §2b carry
   it differently: MB puts it in a **native ⊥-relation on points** (meet `=∩`, but
   complement is ⊥-perp); the Gudder object puts it in the **meet being
   sub-intersection** (`a∧b ⊆ A∩B`, complement is honest set-complement, only
   *disjoint* unions represent joins). Either evades the Floor; the chosen Gudder
   route (§2b) does so without a ⊥-relation, via disjoint-union-only closure.

2. **The descent space is `S_df^σ`, not `P(A)`.** A frequent slip (committed in
   this note's first draft, caught on audit): the σ-additive *measure* of clause
   (iii) must witness `w ∈ conv̄(S_df^σ)` — a measure on the **dispersion-free
   states** (`lem:relational`) — NOT a measure concentrated on the principal-filter
   points `P(A)`. The survey marks `P(A)` *permitted* and locates contextuality on
   `S_df^σ` (`rem:AB`). `P(A)` may appear as auxiliary realisation datum, but it is
   not where (iii) is decided; conflating them is the σ-form of the (A)/(B)
   equivocation.

3. **σ-generated field, not a Boolean clopen algebra.** To mirror `⋁ₙ` we need
   countable unions to *exist* on the space side, so the relevant algebra of sets
   is σ-generated (Baire/Borel-like), not merely the clopen algebra of a Stone
   space.

### 2b. The functor must be CHOSEN — two are on offer, with different Floor-exposure

Before asking what is free, fix *which* representation. Two distinct functors send
`L` to sets, and welding them is an error:

| | meet | complement | join | Floor-exposure |
|---|---|---|---|---|
| **MB dual** (`def:dual`) | `∩` | **⊥-perp** | `(∪)^{⊥⊥}` | evades via perp-complement; joins are ⊥⊥-closures (`rem:finitary`) |
| **Gudder concrete logic** (`def:omp`, `rem:concrete`) | `⊆ ∩` (not =) | **set-complement** | orthogonal = disjoint `∪` | evades via disjoint-only union; **inhabited, non-collapsing** |

The σ-target should be the **Gudder/concrete-logic object**, not MB's ⊥-stable
clopens: it is the "valuation-rich, top-row" object of `sec:twoaxes`, the one where
orthogonal-joins-as-honest-unions is *native* and provably does not force Boolean.
(MB's representable sets take `⋁ₙ` to `(⋃ₙ)^{⊥⊥}` — closure not union,
`rem:finitary` — so demanding honest unions there is an *extra* bolt-on; on the
Gudder object it is the definition.)

### 2c. What is SETTLED (not free): conditions (i)+(ii)

The representation itself is **not** the open frontier. A σ-Dynkin-system of sets —
complement-closed and **countable-disjoint-union**-closed — is a concrete
σ-complete OMP/OML and does **not** force Boolean: the Floor fires only on
**intersection**-closure (a field of sets), and Dynkin-closure is strictly weaker
(`rem:concrete`: "intersection-closure would force a field of sets, hence Boolean").
MO₃ is itself concrete; `∏ₙMO₂` is concrete, σ-complete, non-Boolean, AND on
`Ω = S_df` sends countable orthogonal joins to **honest** unions (a 2-valued
σ-additive state sends `⋁aₙ` to 1 iff exactly one `aₙ` to 1). So (i)+(ii) are
inhabited; the right side under (i)+(ii) **is exactly Derr–Williamson's category**.
Note "(i)+(ii) settled" is largely a **definitional pin** — fixing the target
category to σ-Dynkin-systems makes them hold by the chosen functor, not by a
theorem. That is legitimate, but it means the entire weight of the open problem
rests on clause (iii), once (iii) is correctly stated on `S_df^σ` (§2d).

### 2d. What is OPEN (the one free/unforced edge): condition (iii)

The bite is the **measure descent + contextuality**. Derr–Williamson (Thm D.6, via
Maharam §8.1) deliver descent *under*: `X` **Polish**, σ-blocks **inner-regular**,
`σ(D_σ)=Borel(X)`. The residue (`rem:dw`, STABLE — this note restates, does not
move it) is whether descent can hold **without a pre-given such realization** —
because *obtaining* one for an abstract object of `σOML_conc` **is itself the
missing engine**, not a free input. (Per the verdict file's sharper form, the
binding condition may be **inner-regularity + Borel-σ-generation on the natural
`S_df` weak-\* representation**, not "Polish" per se; do not harden to "Polish".)
This — not the representation — is the sole unsettled
target clause.

## 3. The target, stated honestly

The duality wanted is a contravariant equivalence
$$\sigma\text{OML}_{\mathrm{conc}} \;\simeq\; \mathbf{OMσSpace}$$
where `OMσSpace` is a category of **orthomodular σ-spaces** `(X, T)` whose points,
for the descent clause, are the **dispersion-free states `S_df^σ`** (weak-\*
compact; `lem:relational`), σ-generated — such that the
**Gudder/concrete-logic** representation `h: L → (σ\text{-Dynkin-field of } X)`:

- **(i)** is an iso of σ-OMLs onto a σ-Dynkin-field (complement- and
  countable-disjoint-union-closed) of subsets of `X`;  ← *settled, inhabited*
- **(ii)** sends countable **orthogonal** joins to honest countable unions;
  ← *settled, inhabited* (`∏ₙMO₂`; `rem:concrete`)
- **(iii)** exhibits a σ-additive state `w` on `L` as a barycentre of a σ-additive
  measure on the **dispersion-free states `S_df^σ`** (weak-\* compact, the
  `lem:relational` space): `w ∈ conv̄(S_df^σ)`. ← **the open clause** (descent space
  is `S_df^σ`, NOT `P(A)` — see §2a-2)

The correction to the first draft: (i)+(ii) do **not** leave the right side
undetermined — they pin it to Derr–Williamson's σ-Dynkin-systems, an inhabited
category. The `?` is therefore **not** "what is the right-side category" but the far
narrower: *does (iii) hold off the Polish-realizable case?* So:

- **The right-side object is known under (i)+(ii).** The open problem is not its
  *identity* but whether the **measure** descends to `P` without a pre-given Polish
  realization (`rem:dw` residue).
- **The productive form of "establish the targets"** is therefore: hold the left
  side and the (i)+(ii) right side fixed (both settled), and attack (iii)
  intrinsically — make the Maharam inner-regularity step independent of a given `X`.

## 4. Self-duality check (does the meet side add a constraint?)

By De Morgan on the orthocomplement (`rem:finitary`: `⋀ₙ aₙ=(⋁ₙ aₙ^⊥)^⊥`, and
`a↦a^⊥` an order anti-iso), the countable-meet failure is dual to the
countable-join failure. So (ii) on joins already secures meets — the right-side
spec does **not** acquire an independent "countable intersections" axiom. One
condition (orthogonal-joins-as-unions), self-dual, suffices. Good: no hidden
fourth target clause.

## 5. What this clarifies / where it leaves the attack

- The "OML ↔ measurable space" instinct is the natural first guess and is exactly
  what the Floor kills — informatively: it tells you the dual object **must carry
  ⊥ natively** (or, on the Gudder object, use disjoint-union-only closure); the
  non-distributivity has nowhere else to go.
- **The relocation (the main correction to this note):** the difficulty is NOT in
  inhabiting the right-side *category* — under (i)+(ii) it is Derr–Williamson's
  σ-Dynkin-systems, inhabited (`∏ₙMO₂`). The difficulty is entirely in **(iii):
  measure descent + surviving contextuality, off the Polish-realizable case.** So
  the duality and the σ-essential witness question are the same question, but
  located precisely at (iii) — a witness in `σOML_conc` whose contextuality is
  σ-additive *and* survives descent, i.e. `w ∉ conv̄(S_df^σ)`. `∏ₙMO₂` fails not at representation but
  exactly here: its contextual states are finitely-additive (diffuse on the central
  `P(ℕ)`), washed out by σ-additivity. Cf. `sigma_essential_nonemptiness_finding.md`.
- **Standing unit test for any (iii)-attack:** run it against `∏ₙMO₂`. That object
  satisfies (i)+(ii) and has σ-additive states, so **any argument concluding
  "(i)+(ii) ⟹ Boolean" or "(ii) ⟹ no contextual σ-state" must fail on `∏ₙMO₂`** —
  if it doesn't, the bug is a slide from ⊥-perp to set-complement, or from
  disjoint-union to intersection (the two functors of §2b conflated).
## 6. §5 sub-task, ATTEMPTED → BLOCKED at the π–λ wall (a finding, not a threshold)

*Worked 2026-06-22, after advisor. **Reframed deliverable:** NOT "force
`w ∈ conv̄(S_df^σ)` in general / close the cell" — that is foreclosed (Maharam §8
topological hypothesis is LOAD-BEARING, primary-source-adjudicated; a closure result
would contradict the STABLE `rem:dw` verdict). The target was to **pin which
regularity condition `S_df^σ` needs and which OMLs supply it for free.** Result: the
intrinsic route is **blocked** — and the block is itself the distributivity wall (π–λ
needs meet-closure; the Floor forbids it). Read the OUTCOME box, not the chain above
it, for the verdict; the metrizability chain is recorded as the attempt that exposed
where it breaks.*

**Reduction of the residue to one predicate.** `S_df^σ` is weak-\* compact
**Hausdorff** (claimed; sits in `[0,1]^L`), so Maharam §8.2's Hausdorff-base
hypothesis is **free**. The only thing §8.2 needs beyond it is that the barycentric
measure be **inner-regular (Radon)**. So the entire residue collapses to:
> **Is the barycentric measure on `S_df^σ` inner-regular (Radon)?**

**The metrizability chain.** ⟦HAND — load-bearing, unverified⟧
- A compact Hausdorff `K ⊆ [0,1]^L` (product topology) is **metrizable ⟺
  second-countable ⟺ a countable `D ⊆ L` separates the points of `S_df^σ`** (the
  evaluations `s ↦ s(a)`, `a∈D`, separate states).
- **`L` countably generated (as a σ-OML) ⟹ `S_df^σ` metrizable.** If countable
  `G ⊆ L` has `σ(G)=L`: two σ-additive states agreeing on `G` agree on `σ(G)=L` (the
  agreement set is a σ-sub-structure containing `G`; monotone-class/Dynkin), so `G`
  separates `S_df^σ` ⟹ second-countable ⟹ metrizable.
- **metrizable ⟹ Radon.** On a compact *metric* space every finite Borel measure is
  inner-regular (standard). So the barycentric measure is automatically Radon, §8.2
  applies, and **descent holds**.
- *Converse is weaker:* metrizable ⟹ countably many coordinates *separate* `S_df^σ`,
  which is separation, not generation — so "metrizable ⟹ `L` countably generated"
  need **not** hold. The clean direction is the one above (generated ⟹ metrizable ⟹
  Radon ⟹ descent).

**OUTCOME: the intrinsic route is BLOCKED at the generation⟹separation step — and
the block is the π–λ / meet-closure obstruction, i.e. the SAME distributivity wall.**
⟦HAND⟧ The metrizability chain's load-bearing arrow "`L` countably generated ⟹ `G`
separates `S_df^σ`" **fails as stated.** Diagnosis (advisor-confirmed):

- The agreement set `E={a : s(a)=t(a)}` is a **λ-system** (Dynkin): contains `1`,
  complement-closed, closed under countable *orthogonal* joins. Boolean
  uniqueness-from-generators is the **π–λ theorem**, which requires `G` to be a
  **π-system: meet-closed.**
- In an OML you **cannot propagate agreement to meets** — `s(a∧b)` is not determined
  by `s(a),s(b)` (the same non-determination as non-orthogonal joins) — and
  meet-closure of generators is exactly the **Floor / `rem:concrete`** trigger toward
  Boolean. So the uniqueness step breaks on the *same* distributivity obstruction as
  the rest of the problem. That is the finding: descent resists going intrinsic
  because the measure-uniqueness machinery is π–λ, π-systems are meet-closed, and
  meet-closure is what the Floor forbids.

**Unit-test probe (`∏ₙMO₂`, separation question).** ⟦HAND⟧ Do the coordinate atoms
`{a^{(n)},b^{(n)}}` separate `S_df^σ(∏ₙMO₂)`? **YES** — but *degenerately*: within a
single MO₂ block every non-orthogonal join/meet is trivial (`a∨b=1`, `a∧b=0`), so
there is nothing for π–λ to propagate to; per-coordinate data `(s(a^{(n)}),s(b^{(n)}))`
+ σ-additivity pins the state. So separation holds on `∏ₙMO₂` **precisely because it is
segregated** — the π–λ gap is *invisible* on the unit test and bites only on a
**non-segregated** OML (non-orthogonal joins taking non-trivial values) — which is
exactly where a real witness must live. The control does not catch this gap; do not
mistake its passing for a general result.

**Second crack — RESOLVED (advisor-checked 2026-06-22): real but mislocated, and it
is a CE *connection*, not a threat.** ⟦HAND⟧ The first draft overstated it. Three
facts settle it:
1. **`S_df` (ALL 2-valued states) IS weak-\* compact** — closed in `[0,1]^L`
   (`s(1)=1`, orthoadditivity, and 2-valuedness `⋂_a{s:s(a)∈{0,1}}` are each closed
   conditions) ∩ Tychonoff. So **`lem:relational`, stated for `S_df`, STANDS** — it
   was never in danger. *(Owned check: orthoadditivity is the only state condition in
   this setup, so the closedness argument is complete.)*
2. **`S_df^σ` is NOT weak-\* closed** (the δ_{x_n}→free-ultrafilter argument; = CE,
   `rem:ce`), hence not compact. True — but see (3).
3. **`conv̄(S_df^σ)` is compact regardless** (closed convex hull inside the compact
   `S_df`), so the **contextuality predicate `w ∉ conv̄(S_df^σ)` needs NO compactness
   assumption.** The crack does not touch the predicate.

So the crack lives in exactly one place: the *realization direction* of the σ-analog
of `lem:relational`. `w ∈ conv̄(S_df^σ)` gives a barycentre of a measure on
`cl(S_df^σ)`, which may charge `cl(S_df^σ)\S_df^σ` = the finitely-additive
dispersion-free states = **the CE phantoms (`rem:ce`)**. Hence "genuine σ-additive
hidden-variable mixture" (measure on `S_df^σ`) is potentially **strictly stronger**
than `w ∈ conv̄(S_df^σ)`. This is a one-directional **closure gap = the CE leak**: a
refinement connecting the scaffold to `rem:ce`, NOT a transfer failure. Sub-question
**CLOSED** (refined to a CE connection, not a death).

> **Flagged forward-looking sub-question (do NOT act unprompted — touches the
> survey's `lem:relational`/`rem:ce` definitions):** if "measure genuinely on
> `S_df^σ`" is strictly stronger than `w∈conv̄(S_df^σ)`, the survey's contextuality
> predicate may be the *weaker* of two inequivalent σ-notions. A witness for the
> stronger one (a σ-additive measure charging no CE phantom) would be a cleaner
> object — and possibly the *right* target. Whether the two notions actually differ
> on some `L`, and which the open problem should use, is an open definitional
> question for the user's call, not a settled refinement.

**Honest status of §6.** Intrinsic route **attempted and blocked at ONE wall** (the
π–λ/meet-closure step = the distributivity obstruction again); the second worry
resolved to a CE-leak refinement (above), not a crack. A real finding — *why* the
residue resists intrinsic resolution — NOT a completed threshold result and NOT a
closure. Does **not** swing `rem:dw`. The "countably generated ⟹ descent" claim is
**withdrawn** pending a meet-free uniqueness argument (none known). Remaining live
edge: that meet-free uniqueness argument.

**Red-flag rule (standing).** If any later argument forces `w ∈ conv̄(S_df^σ)` for
*general* `L`, STOP — it has smuggled inner-regularity/Radon (or a π-system), the
analog of the `P(A)`/`S_df^σ` switch caught on audit. First question on any positive
result: *where did meet-closure / inner-regularity enter?*

---

*Status: working scaffold, not survey-ready. §5 sub-task ATTEMPTED (§6) → intrinsic
route BLOCKED at the π–λ/meet-closure wall (the distributivity obstruction again).
Second worry (compactness of `S_df^σ`) RESOLVED: `lem:relational` stands on the
compact `S_df`; the σ-realization direction has a closure gap = the CE leak (`rem:ce`)
— a refinement, not a crack. A finding, not a threshold result. Sole remaining live
edge: a meet-free uniqueness argument (none known). Does NOT reopen the `rem:dw`
verdict (STABLE); only
restates its residue as a right-side specification gap.*
