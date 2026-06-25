> ⚑ ARCHIVED 2026-06-25 (σ-essential thread cleanup). Superseded by `sigma_essential_reduction_writeup.md` §3 (walls A/B/C); the §6/§9a detail is preserved in THIS file. Kept for the reasoning trail; not current.

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
- **CORRECTED MECHANISM (advisor 2026-06-22 — first draft's "meet-closure ⟹ Floor"
  was WRONG).** Taking `G` meet-closed is **free** and triggers nothing: MO₂ is
  itself meet-, join-, complement-closed and non-Boolean. The Floor (`thm:floor`)
  needs a *faithful set representation* (simultaneously `∧→∩`, `∨→∪`, `⊥→`complement);
  "`G` meet-closed inside `L`" is a far weaker condition with no Boolean collapse. So
  the block is NOT at meet-closure. With `G` meet-closed, the real failure is that
  **π–λ does not transfer**: `λ(G)` [complement + orthogonal-join closure = the
  agreement set] need not reach `σ(G)` [+ arbitrary joins]. It fails at the
  **disjointification identity**
  > `(a∨b) ∧ a^⊥ = b ∧ a^⊥`,
  which Boolean π–λ uses to rewrite an arbitrary join `a∨b` as an orthogonal join
  `a ⊔ (b∧a^⊥)`. That identity is **distributive and false on OMLs**. So the
  obstruction is genuinely non-distributivity, entering at **disjointification**, not
  via meet-closure→Floor.

**Unit-test probe (`∏ₙMO₂`, separation question).** ⟦HAND⟧ Do the coordinate atoms
`{a^{(n)},b^{(n)}}` separate `S_df^σ(∏ₙMO₂)`? **YES** — but *degenerately*: within a
single MO₂ block every non-orthogonal join/meet is trivial (`a∨b=1`, `a∧b=0`), so
there is nothing for π–λ to propagate to; per-coordinate data `(s(a^{(n)}),s(b^{(n)}))`
+ σ-additivity pins the state. So separation holds on `∏ₙMO₂` **precisely because it is
segregated** — the π–λ gap is *invisible* on the unit test and bites only on a
**non-segregated** OML (non-orthogonal joins taking non-trivial values) — which is
exactly where a real witness must live. The control does not catch this gap; do not
mistake its passing for a general result.

**Key consequence — PROOF-BLOCK ≠ UNIQUENESS-FAILURE (so this is NOT a second wall).**
⟦HAND⟧ On `∏ₙMO₂` the disjointification identity **already fails** (non-orthogonal
atoms `a,b` in one block: `(a∨b)∧a^⊥ = 1∧a^⊥ = a^⊥ ≠ 0 = b∧a^⊥`), **yet separation
holds** (above). So "disjointification fails" does **not** imply "separation/uniqueness
fails" — the broken identity kills only the *standard π–λ proof*, not the conclusion.
To make a genuine second wall one would need two σ-states agreeing on `λ(G)` but
differing on `σ(G)` — which requires a **non-segregated concrete σ-complete OML**, the
exact object the whole problem lacks. **So the meet-free-uniqueness edge has no
independent attack surface: it is gated by the same missing witness as the main
problem.** Honest status: π–λ transfer fails at the distributive disjointification
identity; whether separation actually fails is OPEN and entangled with the same
existence gap (`rem:dw` residue). Not a wall, not hand-closeable now.

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

> **RESOLVED 2026-06-22 (user picked this fork; advisor-checked). The two
> predicates are co-extensive on every accessible object and diverge EXACTLY on the
> missing witness — so the definitional question is settled without needing the
> witness.** ⟦HAND — advisor-confirmed⟧
> Name the two σ-notions of contextual on a concrete σ-complete OML `L`:
> - **(P-weak)** `w ∉ conv̄(S_df^σ)` — the survey's current predicate (`lem:relational` σ-form).
> - **(P-strong)** `w` is NOT the barycentre of any σ-additive probability measure
>   supported **on `S_df^σ` itself** (charging no CE phantom, `rem:ce`).
> Write `A = conv̄(S_df^σ)` and `B = {barycentres of σ-measures on S_df^σ}`. Always
> `B ⊆ A`, so **¬P-strong ⟹ ¬P-weak**, i.e. **P-weak ⟹ P-strong** (P-strong holds
> for more states). The fork = is the implication strict.
> - **TRIVIAL reading (any `w`): always split, VACUOUSLY.** A phantom `φ ∈ cl(S_df^σ) ⊆ A`
>   but `φ ∉ B` (a σ-measure on `S_df^σ` has a σ-additive barycentre; `φ` is
>   finitely-additive-not-σ). So `A\B ≠ ∅` whenever phantoms exist — but these are
>   non-σ-additive `w`, not contextual *states* in the substantive sense. Don't let
>   "phantoms exist" read as inhabiting the fork. **Smuggle-trap.**
> - **SUBSTANTIVE reading (σ-additive `w`): the real question, and it equals door 1.**
>   For σ-additive `w`: **`B = A` ⟺ every σ-additive state in `conv̄(S_df^σ)` is a
>   genuine σ-mixture of σ-additive POINTS = σ-point-realization** (the tribe-vs-points
>   gap, §9 / door 1). (⟸ point-mixture gives the measure; ⟹ `B=A` makes every hull
>   state a point-measure.) A σ-additive `w` needs to charge phantoms iff it is a
>   *limit barycentre* of points that is not a genuine point-mixture — which **is** the
>   σ-LS failure.
> - **Why this is general, not a `∏ₙMO₂` accident.** Agreement holds wherever
>   point-concentration holds: Boolean (Stone), Polish-representable (D–W, `rem:dw`),
>   and **segregated objects generally** — central decomposition + σ-additivity forces
>   a σ-additive state onto the central atoms, so a σ-additive hull-state IS a
>   point-mixture. Verified on `∏ₙMO₂` (survey line 1056–1059: contextual states are
>   only finitely-additive on the central `P(ℕ)`; σ-additivity forces concentration on
>   points). **The split can occur ONLY on a non-segregated, non-Polish object — the
>   exact witness class the programme lacks.**
> - **THE ANSWER to "which predicate should the open problem use":** it does not
>   matter until the witness exists; **P-weak and P-strong are co-extensive on every
>   object the programme can access.** If/when a witness exists, state it with
>   **P-strong** (genuine σ-measure charging no phantom) — the strictly stronger,
>   cleaner target. **Guardrail: this does NOT un-park.** The divergence sits on the
>   SAME wall (door 1); it is a restatement of the residue, not a new attack surface.
>   `rem:dw` STABLE; survey unchanged.

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

## 7. Construction attempt (2026-06-22) → fence + the two-hull relocation

*Tried to construct the missing non-segregated concrete σ-complete OML witness.
Advisor-gated; two substrate ideas, both = the `∏ₙMO₂` death in new clothes. No
witness — but a new fence and the actionable relocation of where a witness lives.*

- **Fence (CE-charge-limit cannot carry it).** Making the non-distributivity/
  contextuality BE the CE limit-failure (`A_n↓`, `μ(A_n)↛0`, `⋀A_n=0`) is dead: that
  limit-failure *is* failure of continuity-from-above = *is* non-σ-additivity, so the
  carrier state is finitely-additive-not-σ — the `∏ₙMO₂` death. Dual concreteness
  fence: meets never overshoot (`h(⋀A_n)⊆⋂h(A_n)` always), so non-distributivity is
  **finite/binary** and cannot live in the countable limit, either side.
- **Relocation (where the witness lives).** The carrier is **not a limit gadget** —
  it is the **two-hull geometry**: a witness is `w ∈ conv̄(S_df) \ conv̄(S_df^σ)` with
  `w` **genuinely σ-additive**, i.e. `conv̄(S_df^σ)` a *strictly smaller closed hull*
  than `conv̄(S_df)` (a separation of the two df-state sets), **off-center**. Both
  hulls compact (§6). This is §6's CE-leak, now identified as the search target.
  > **HEDGE (do not state as established — survey-blocked):** the survey *defines*
  > contextual as `w ∉ conv̄(S_df^σ)` only. The extra membership `w ∈ conv̄(S_df)` is a
  > *separate* claim — it holds (via Hahn–Banach) **iff every finite df-state lifts to a
  > global df-state**, a KS/extension condition strictly stronger than concreteness
  > (order-determining global df-states). So `w ∈ conv̄(S_df) \ conv̄(S_df^σ)` is a
  > search *heuristic*, conditional on lifting; absent lifting, a witness need only sit
  > outside `conv̄(S_df^σ)` and could lie outside `conv̄(S_df)` entirely. **Decisive
  > probe:** does `S_df(F) = {s|_F : s ∈ S_df}` for finite `F`? (Finite, yes/no;
  > determines whether the two-hull framing even holds.)
- **Gate for any candidate `w` escaping `conv̄(S_df^σ)`:** *does the escape come from
  charge-non-σ-additivity?* YES ⟹ `∏ₙMO₂` death, reject. A live witness needs `w`
  σ-additive with the escape carried by `S_df^σ ⊊ S_df` as closed hulls. Whether that
  gap is inhabited for an irreducible off-center concrete σ-complete OML is the open
  problem (= HW Problem 2, untooled). **No carrier on the table; Exit-B inclination
  held open (NOT a verdict); `rem:dw` unmoved.**

## 8. DST construction attempt (2026-06-22, Session 10) → the deliverable is the restriction-gap, not non-Borelness

*Took the §7 probe and the S9-flagged DST route to ground. Three corrections to §7,
one verified fact, one new sub-theorem. No witness; reduces to σ-lifting-failure.*

- **Correction to §7's hedge: "iff" → "⟹".** Lifting (`S_df(F)={s|_F:s∈S_df}` ∀
  finite `F`) is **sufficient**, not strictly necessary, for `w∈conv̄(S_df)` (`w|_F`
  can land in the smaller restricted-hull even where lifting fails). State it
  "lifting ⟹ two-hull framing valid".
- **The probe is a degenerate bracket, not a discriminator.** `∏ₙMO₂` lifts *because*
  segregated (only ever confirms "holds"); Wright's pentagon is a loop where lifting
  fails AND is already excluded (finitely witnessed). They bracket the fork without
  touching the non-segregated regime — there lifting is *as hard as the main problem*.
  Smuggle-trap flagged+avoided: "lifting fails ⟹ finitely witnessed ⟹ not σ-essential"
  is FALSE (local hull `S_df(F)` strictly bigger than restricted-global hull; the
  "lifting fails"/KS branch is NOT closed by the loop-kills).
- **VERIFIED (load-bearing): off-hull is ALWAYS finitely witnessed.**
  `w∉conv̄(S_df^σ)` ⟺ a *finite* combination `Σcᵢ s(aᵢ)` separates `w`
  (Hahn–Banach in `ℝ^L`, product topology; continuous functionals = finite-support).
- **DELIVERABLE RE-IDENTIFIED.** Off-hull + σ-essential FORCE the strict
  **restriction-gap** `{s|_F:s∈S_df^σ} ⊊ S_df(F)` — global σ-additive df-states fail to
  restrict onto the local df-state hull. `w` exists EXACTLY when this gap does.
  Non-Borelness of `S_df^σ` is only its descriptive SHADOW — neither target nor
  sufficient. **The gap IS σ-lifting-failure = route-(iii) σ-LS wall = `rem:dw`
  residue.** Aim at the gap, not at a complicated state space.
- **Countably-generated checkpoint: PERMITS, not FORCES.** Countable generation permits
  non-point-like σ-states (π–λ wall blocks LS collapse) but does not force the gap —
  `∏ₙMO₂` is countably generated, non-π-system generators, yet lifting holds. π–λ
  failure NECESSARY not SUFFICIENT.
- **NEW SUB-THEOREM CANDIDATE (flagged, NOT claimed — Type-5):** *every countably
  generated concrete σ-complete OML satisfies lifting?* If true ⟹ witness must be
  **uncountably generated** (narrows search). Does NOT follow from π–λ; a theorem to
  prove. **Cleanest next move.**
- **Negative-space finding.** The 5 primitive binding modes each land on a closed horn;
  the residual region = "non-orthogonal joins, non-trivial value" = the open problem in
  local terms, NOT a mechanism. Every *compositional* (pairwise) join-specification
  collapses to a horn ⟹ **the lever, if any, must be GLOBAL/non-compositional** — why
  finite-assembly construction always fails.
- **Tripwire (not triggered):** extra set-theoretic axioms (meas. cardinal / V=L / ¬MA)
  would confirm `rem:dw`'s ZFC-independence rhyme. Not seen.

## 9. Prior-art on the countably-generated cut (2026-06-22, Session 11) → OPEN, no off-the-shelf theorem reaches it; the tribe-vs-points gap is confirmed structural

*Hostile cross-field prior-art scout (per the standing rule — Strategy D died here) on
the §8 sub-theorem candidate: "every **countably generated** concrete σ-complete OML is
point-realizable / satisfies σ-additive lifting." Sweep complete across Pták–Pulmannová,
Hamhalter, Navara, Gudder, de Lucia, Kalmbach/Greechie, effect-algebra/MV/D-poset LS,
Derr–Williamson. **Verdict: OPEN — the exact conjunction (countably generated ∧ concrete
∧ σ-complete ⟹ point-realizable with separating σ-additive 2-valued states) is stated
nowhere, proved or refuted.** This is the **countably-generated cut**, explicitly DISTINCT
from `rem:dw`'s **Polish-representable** cut — a different, weaker slice of the same σ-LS
wall. Does NOT reopen `rem:dw`.*

- **The tribe-vs-points gap is REAL and structural (main deliverable).** Every
  Loomis–Sikorski theorem that exists for non-Boolean structures (effect-algebra:
  Barbieri–Weber/Dvurečenskij; MV: Mundici/Dvurečenskij; D-poset) gives a
  **σ-epimorphic image of a function-tribe**, NOT a point set with separating σ-additive
  2-valued states. Two obstructions for our purpose: (1) they require the **Riesz
  Decomposition Property (RDP)**, which non-Boolean OMLs generically **FAIL**; (2) even
  when applicable, a function-tribe quotient can carry **zero** 2-valued states. Boolean
  is the ONLY case where tribe-quotient = point set with separating 2-valued states
  (Booleanness forces a determining set of Dirac states). **Consequence: the proof route
  CANNOT ride on existing LS machinery — off-the-shelf σ-LS gives the easy thing
  (tribe), not the hard thing (separating σ-additive 2-valued points).** This vindicates
  the long-standing worry "representable as a σ-tribe ≠ point-realizable."
- **NEW ABSTRACT INPUT on the point side (the hard side): Burešová–Pták, arXiv:2401.13798
  (2024)**, "On the Set-Representable Orthomodular Posets that are Point-Distinguishing."
  *(Author corrected 2026-06-22 from "Anguelov" — verified against the arXiv abstract;
  authors are Dominika Burešová & Pavel Pták.)*
  Post-dates the programme's reading. Separates "set-representable" from
  "point-distinguishing"; their Stone-type construction over ALL 2-valued states makes
  every 2-valued state a **Dirac state** — but only after **possibly enlarging the point
  set significantly (a CARDINALITY COST)**. **It is SILENT on σ-completeness and countable
  generation.** That cardinality blow-up is *exactly* the mechanism a countable-generation
  hypothesis would have to control. THE LIVE FORK: does countable generation **bound** the
  blow-up (⟹ lifting/point-realizable holds, TRUE side) or genuinely **force uncountable
  points even for countably-generated `L`** (⟹ refutation seed)? This is the natural
  battleground; the experts on point-distinguishing OMPs have not run the σ analysis.
- **The refutation side is STRUCTURALLY STARVED — but this is WEAKER evidence than it
  looks (wrong axis).** Known state-poor OMLs (Greechie's state-free constructions;
  Navara's no-group-valued-measure OML; Navara–Pták) are **combinatorial loop/pasting
  constructions, finite or finitely generated, and NOT σ-complete.** σ-completeness is a
  real filter that rules out exactly the constructions that kill states. ⚠⚠ **CAVEAT
  (advisor 2026-06-22): those are STATE-POVERTY constructions, but lifting-failure is
  RESTRICTION-NON-SURJECTIVITY — a local 2-valued state on `F` that no global σ-additive
  state restricts onto.** These are DIFFERENT failure modes: an `L` can be state-*rich*
  (`S_df^σ` separating) yet have the restriction map miss a local pattern. So the
  starvation point addresses the wrong axis — it is necessary-not-sufficient evidence and
  must NOT accrue weight toward TRUE. ⚠ Doubly an **absence-of-counterexample universal**
  — Exit-B shape.
- **Bounds on the open cut.** Lower bound (free): function-tribe representation (too weak,
  no points). Upper bound (settled positively): Derr–Williamson Polish-representable case
  (`rem:dw`) — strictly STRONGER hypothesis than countable generation; nobody has bridged
  Polish-representable ⟸ countably-generated.
- **Citations to pull:** Burešová–Pták arXiv:2401.13798 (Thm 2.5, 3.1); Dvurečenskij
  effect-algebra LS (survey arXiv:1204.6486 for the RDP hypothesis); Pták–Pulmannová
  *Concrete Quantum Logics* + the 1994 CMUC 35:205–208 subadditive-measures⟹Boolean
  prior-art (already held); Derr–Williamson arXiv:2302.03522 (upper bound).
- **PROOF-DIRECTION DISCIPLINE (carry into the attack).** Attack **existence** (does a
  2-valued state `s_0` on finite `F` extend to a global σ-additive 2-valued state on
  countably-generated `L`?). Do NOT attack the prompt's "is the extension *determined*
  once generator-values are fixed?" (prompt lines 102–105) — that is *uniqueness* = §6,
  already gated by the missing witness, and "determined ⟹ lifting" is an INVALID
  inference (determinacy ≠ existence). Re-walking it re-runs §6 under a new name.

### 9a. Existence route worked → PARKED (the two-dual-walls convergence)

*Worked + advisor-checked 2026-06-22, Session 11, after the Burešová–Pták read.
Outcome: **unresolved-open, PARKED** — not impossible, not walled-shut. A convergence
finding.*

- **The finitary per-step CANNOT block (so don't compute it).** In the back-and-forth
  (extend a 2-valued σ-additive `s` from `Lₙ=⟨g₁…gₙ⟩` to `Lₙ₊₁`), assigning `s(gₙ₊₁)` at
  a **finitary** step is **always free** (the MO₂ phenomenon: state `(0,0)` has
  `s(a)=s(b)=0` yet `s(a∨b)=1`, value unconstrained). A finitary obstruction would be
  finite-character = Wright = unit-test-3 excluded = **not σ-essential**. So a finitary
  disjointification contradiction can only ever confirm "finite works" — it cannot find
  the witness and cannot park the problem. ⟦HAND — advisor-confirmed⟧
- **The ONLY blocking relations are the countable-join / σ-additivity ones.** When
  `gₙ₊₁ = ∨ₖhₖ`, σ-additivity FORCES `s(gₙ₊₁)=1 ⟺ some s(hₖ)=1`. That σ-limit is the
  one place a value isn't free and a contradiction can arise. The conjecture, stated
  correctly, IS **σ-point-richness for the countably-generated cut**: "every
  countably-generated concrete σ-complete OML has *enough σ-additive* 2-valued states to
  lift every finite local df-state."
- **Borel(2^ℕ) sanity check (shape confirmed).** Countably generated, σ-complete,
  point-realizable, lifting HOLDS — *despite* carrying free-ultrafilter (finitely-additive-
  not-σ) states = the `rem:ce` phantoms — because it ALSO has enough `δ_x`. So CE phantoms
  existing does NOT break lifting; lifting needs enough *σ-additive* states regardless.
  Open: do non-Boolean countably-generated concrete σ-OMLs keep that richness?
- **THE FINDING — both DUAL surfaces lack a tool for the non-Boolean σ case (NOT "one
  wall").** Existence and separation/uniqueness are **duals**, genuinely distinct
  surfaces:
  - **Separation route (§6):** blocked at the **disjointification** identity
    `(a∨b)∧a⊥=b∧a⊥` (a uniqueness surface).
  - **Existence route (here):** needs **σ-LS point-existence** (a σ-homomorphism
    `L→{0,1}` with prescribed values on `F`) — the **dual** surface.
  - **Cardinality-control route:** DISSOLVED (wrong axis — Burešová–Pták blow-up is
    indexed by the count of ALL [incl. non-σ] states, which countable generation does not
    bound; Borel(2^ℕ) has 2^ℵ₀ states yet lifts).

  Three doors, two genuinely-dual walls, **both** without an off-the-shelf engine for the
  non-Boolean σ case (scout: LS gives tribe-not-points, RDP fails; BP: wrong tool). That
  **double-absence** is the finding — more honest and more informative than collapsing
  them to "one wall."
- **GUARDRAIL — "no engine" ≠ "lifting fails."** Lifting (σ-points over each finite `F`)
  is strictly **weaker** than full σ-LS point-realization (separating all of `L`). Absence
  of an LS engine does NOT entail lifting fails. **Lifting may well be TRUE.** Status:
  **unresolved-open, PARKED** — do NOT promote "couldn't prove" → "impossible/walled."
- **FORWARD POINTER (the shape of the new input a future session waits on).** The new
  object the problem needs must supply σ-points **non-constructively** — no LS engine will
  deliver them for non-Boolean σ-OMLs. That is the shape of the "new abstract input"
  required to move either way. Until such input arrives, the existence route adds no
  nameable lever beyond what §6 already exhausted on the dual side.
- **Survey unchanged** (guardrail): the conjecture and this convergence stay in working
  notes, NOT `oml_onboarding`. `rem:dw` STABLE/untouched (Polish-representable cut; this is
  the countably-generated cut).

---

*Status: working scaffold, not survey-ready. §5 sub-task ATTEMPTED (§6) → intrinsic
route BLOCKED at the π–λ/meet-closure wall (the distributivity obstruction again).
Second worry (compactness of `S_df^σ`) RESOLVED: `lem:relational` stands on the
compact `S_df`; the σ-realization direction has a closure gap = the CE leak (`rem:ce`)
— a refinement, not a crack. Meet-free-uniqueness edge also resolved-to-GATED: π–λ
transfer fails at the distributive disjointification identity `(a∨b)∧a^⊥=b∧a^⊥`, but
proof-block ≠ uniqueness-failure (∏ₙMO₂ breaks the identity yet separates), so it has
no independent attack surface — gated by the same missing non-segregated witness as
the main problem. **Both hand-edges now bottom out at the same `rem:dw` residue;
further hand-progress needs a new object or new abstract input.** A finding, not a
threshold result. Does NOT reopen the `rem:dw` verdict (STABLE); only
restates its residue as a right-side specification gap.*
