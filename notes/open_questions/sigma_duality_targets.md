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
- Next concrete sub-task (if pursued): test whether the **Maharam inner-regularity
  step (D.6) can be made intrinsic** — whether `w ∈ conv̄(S_df^σ)` can be forced
  from the abstract σ-OML structure rather than read off a pre-given Polish/regular
  realization of `S_df^σ`. Per the verdict file's sharper form, the binding
  condition is inner-regularity + Borel-σ-generation on the natural `S_df^σ` weak-\*
  representation, not "Polish" per se. That is the live edge of the `rem:dw`
  residue, and the only unforced target clause.

---

*Status: working scaffold, not survey-ready. Decide incorporation after the §5
sub-task is attempted. Does NOT reopen the `rem:dw` verdict (STABLE); only
restates its residue as a right-side specification gap.*
