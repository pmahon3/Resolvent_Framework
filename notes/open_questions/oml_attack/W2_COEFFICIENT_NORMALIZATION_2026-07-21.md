# W2 — Coefficient normalization: verdict (escape (a))

*2026-07-21. Executes W2 of `SIGMA_LAYER_TARGET.md` §3, scoped to escape (a).
The trichotomy re-run is PARKED by user decision (redundant: §6 of the parked
seed already ran it, audit-certified accurate, and the audit itself called the
result hollow — T0 restates CSS∧¬GS). W2 here is the coefficient layer only:
what group, if any, acts on the fibres. No W1 re-opening; no grammar-engine run
(no clause named, per A2).*

**Headline.** For escape (a) **on the raw `P(G_i)` atlas as banked**, the
σ-fibres are **singleton-or-empty in ZFC**. There is no coefficient structure at
all — not ℤ/2, not any group, and not even an inhomogeneous set to test for
homogeneity. The section system is **set-valued with inclusion bonding**, and
its obstruction is **lim⁰ death** (every stage nonempty, limit empty). The
group-valued derived-limit machinery has nothing to act on there.

⚠ **Scope, corrected 2026-07-21:** this is a theorem about the **raw** atlas.
Under an *admissible-OML* re-derivation with **coarser** blocks, **both** the
fibre pattern **and** the no-coefficients conclusion are **open** — coarsening
can create non-principal σ-states in ZFC with no measurable (H1). Do not quote
the headline without this scope.

**Secondary finding (a correction to the parked seed).** §5 Test 1 of the
σ-nerve seed misdescribes this architecture on two counts, and its "one
non-principal state and a proper class of Diracs" fibre census is **refuted**,
not merely sharpened. See §3.

---

## 1. What was computed, and the object it was computed on

**Object.** `oml_omega1_cylinder_hub.md` §2–§4: `I = ω₁`, `H = 2^I`, `A` = the
countable-support product σ-algebra on `H`, `G_i = H∖{i}`, **`B_i = P(G_i)`**
(full powerset — checked verbatim against the source, §4 below), `j_i(E) =
E ∩ G_i`, atlas `(B_i)_{i∈H}`.

**Fibre.** Over a common `A`-trace, the fibre at block `B_i` is the set of
states on `B_i` restricting along `j_i` to that trace. Computed in both layers
(σ and fa), per the second-inclusion framing.

**Not computed / not claimed:** anything about escape (b) (deferred, and it
inherits §3.2 of the W1 verdict); any lim¹/limⁿ identification (TARGET, never a
premise — Stage-0 §2); any re-run of the T0/T1/T2 trichotomy.

---

## 2. The σ-fibre computation

### Theorem W2-1 (σ-fibres are singleton-or-empty). ⟦HAND, ZFC⟧

For every `i ∈ H` and every common trace `eval_x`:

```
fibre_σ(B_i, eval_x)  =  {δ_x}   if x ≠ i
                      =  ∅       if x = i
```

*Proof, in three steps.*

**(1) Every σ-state on `B_i = P(G_i)` is principal — in ZFC, outright.**
A σ-additive two-valued state on `P(G_i)` is a countably complete ultrafilter
on `G_i`. If a nonprincipal one existed, some cardinal `≤ |G_i| = 2^{ω₁}` would
be measurable. But a measurable cardinal is inaccessible, hence a **strong
limit**: `λ < κ ⟹ 2^λ < κ`. So `ω₁ < κ ≤ 2^{ω₁}` forces `2^{ω₁} < κ ≤ 2^{ω₁}`,
a contradiction; and `κ ≤ ω₁` is impossible since measurables are regular
limits while `ω₁` is a successor. Hence **no measurable is `≤ 2^{ω₁}`**, and
every σ-state on `B_i` is a Dirac `δ_y`.

> ⚑ **This is stronger than the hub note's own §3 argument, and stronger than
> the form in which the derivation was handed to this session.** It is not
> conditional on "no measurable exists": a measurable can *never* sit at or
> below `2^{ω₁}` in any model of ZFC, because inaccessibility makes it a strong
> limit. No large-cardinal hypothesis is needed, and none is available as an
> escape. Hub §3 proves only the weaker local statement (no σ-extension *of
> eval_i*) via Ulam on ω₁; W2-1(1) kills **every** nonprincipal σ-ultrafilter
> on `G_i` at once. The two agree; this one subsumes it.

**(2) Compatibility pins the Dirac.** `δ_y` restricts to `eval_x` iff for every
`E ∈ A`, `y ∈ E ∩ G_i ⟺ x ∈ E`. Coordinate cylinders `{z : z_α = b}` lie in
`A`, so `y_α = x_α` for all `α < ω₁`, i.e. **`y = x`**.

**(3) Existence iff `x ≠ i`.** `δ_x` is a state on `P(G_i)` iff `x ∈ G_i`, i.e.
`x ≠ i`. ∎

### Corollary W2-2 (no coefficients). ⟦HAND⟧

A singleton has no nontrivial group acting simply transitively; an empty fibre
has none at all. So the fibre system carries **no group-valued coefficients**,
and *a fortiori* is not a ℤ/2-system. Binary regularity fails not because the
fibres are too big (as the seed's Test 1 has it) but because they are **too
small** — cardinality 1 or 0, never 2.

> ⚠ **Why the originally proposed homogeneity test had to be corrected.** The
> planned W2 check was: "the fibre has a distinguished point (one non-principal
> state among many Diracs), hence is a torsor under no group." On the *correct*
> object that test returns a **vacuous yes** — a singleton *is* trivially a
> torsor, under the trivial group — and would have suggested T1-like structure
> where there is none. The test was aimed at a misdescribed object *and* would
> have returned a misleading answer on the real one. Recorded because the
> failure mode (testing homogeneity without first testing cardinality) is
> reusable.

### Theorem W2-3 (the system is set-valued; obstruction is lim⁰). ⟦HAND, ZFC⟧

Section space over a countable stage `J ⊆ H`:
`X(J) = {eval_x : x ∉ J} ≅ H∖J`, with bonding = **inclusion** (restriction of
a point evaluation to a smaller block family).

- **CSS:** `J` countable, `|H| = 2^{ω₁}`, so `H∖J ≠ ∅`. Every stage is
  nonempty. ✔
- **no-GS:** `lim = ⋂_J (H∖J) = ∅` — each `x` is excluded at its own stage
  `J = {x}`. ✔

So CSS∧¬GS holds in system form, with **no group structure anywhere**: the
obstruction is emptiness of the inverse limit of a **set-valued** system
(lim⁰ death), not a nonvanishing class of a group-valued one. ∎

---

## 3. Correction to the parked seed's §5 Test 1 (REFUTED, not sharpened)

Test 1 reads: *"The hub block is a coarse (not countably generated) σ-field of
countable/co-countable type; its eligible σ-lifts include one non-principal
state and a proper class of Diracs constrained by μ. Interface fibres are not
two-element."*

Two independent errors:

**(i) Wrong algebra.** `A` is the **countable-support product** σ-algebra
(hub §2), not one "of countable/co-countable type." These are different: the
cylinder `{z : z_0 = 1}` has both size and co-size `2^{ω₁}`, so it lies in the
product algebra but **not** in the countable/co-countable algebra.

**(ii) Wrong fibre census — the category slip.** Hub §2 *proves* every σ-state
of `A` is a point evaluation, and W2-1 proves every σ-state on each `B_i` is a
Dirac. **There is no non-principal state anywhere in the σ layer.** The
non-principal object is real but lives elsewhere: hub §3's **finitely additive**
BPI extension of `eval_i`, which exists exactly at the puncture — precisely
where the σ-fibre is *empty*. Test 1 imported an fa-layer object into a σ-layer
fibre census.

**Why the slip matters (not pedantry).** A distinguished point *inside a fibre*
would be a statement about the σ-fibres and would rule out torsors. An
fa-object *outside the σ-system* says nothing about the σ-fibres at all. The
true σ-finding is strictly stronger than the one Test 1 gestured at.

**What survives of Test 1.** Its *conclusions* — binary regularity fails, the
lim¹ identification does not apply, the architecture is T0 — all stand. Only
the stated *reason* was wrong (fibres too small, not too large). The ledger row
"omega-one cylinder common hub → T0" is unaffected.

---

## 4. σ vs fa, side by side — the second inclusion, locally

Requested as the tie to the banked frontier (clause (b)) rather than to the
parked seed's frame. fa-states on `B_i` are ultrafilters on `G_i` (no
completeness). ⟦HAND⟧

| trace | σ-fibre | fa-fibre |
|---|---|---|
| `eval_x`, `x ≠ i` | `{δ_x}` — **singleton** | **large** (many ultrafilters) |
| `eval_i` (the puncture) | **∅** | **large, every member non-principal** |

*fa computation.* Compatible fa-lifts of `eval_x` are the ultrafilters
extending the filter `F_x` generated by `{E ∩ G_i : x ∈ E ∈ A}`. `F_x` is not
an ultrafilter on `P(G_i)`, by diagonalization: its minimal generators are the
punctured cylinders, of which there are `2^{ω₁}`, each of size `2^{ω₁}` (fixing
countably many coordinates leaves `2^{ω₁}` points free). Recurse along an
enumeration of the generators in order type `2^{ω₁}`; at stage `α` pick two
distinct not-yet-used points of generator `G_α` (possible, since
`|G_α| = 2^{ω₁}` exceeds the `<2^{ω₁}` points used so far), putting one into
`S` and one into its complement. Then `S` and `G_i∖S` each meet every
generator, so neither contains one, so `F_x` decides neither — and extends to
ultrafilters both ways. Hence **many** lifts.

> ⚑ **Repaired 2026-07-21 (user's verification pass).** The earlier
> justification here was a cardinality one-liner — "`|P(G_i)| = 2^{2^{ω₁}}`
> vastly exceeds `|A| = 2^{ω₁}`, so some `S` is undecided." That is **loose and
> does not do the work**: `F_x` is a *filter* on `P(G_i)`, and since every
> superset of a generator belongs to it, `|F_x|` can be as large as `|P(G_i)|`.
> Comparing cardinalities therefore exhibits no undecided set. The
> diagonalization above replaces it. **Conclusion and grade unaffected.**

At the puncture, hub §3's trace filter `{E∖{i} : i ∈ E ∈ A}` is proper and
BPI-extendable; every such ultrafilter is non-principal, since the
countably-supported `E ∋ i` have empty intersection (coordinates separate
points).

**Reading.** The **σ layer is rigid** — singleton-or-empty, zero freedom. The
**fa layer is floppy** — large everywhere, BPI-fed. The obstruction sits
exactly in the σ/fa gap at the puncture: *fa survives where σ dies*. This is
clause (b)'s second inclusion (σ-states catching non-extendable finitely
additive states) appearing at the level of a single interface fibre, which is
the sense in which W2's output feeds the live frontier rather than the parked
frame. **Grade: hand proved** (fa side uses BPI, flagged per clause (a)'s
BPI-exactness discipline).

---

## 5. Conversions (A1 discipline, both pre-registered)

The user pre-registered both branches before the computation. **The "trivial"
branch fired.**

- **Escape (a) is closed to limⁿ-reduction *via the natural state fibres*.**
  The derived-limit engine needs group-valued (or at least homogeneous)
  coefficients; (a)'s σ-fibres supply none. Any limⁿ route to (a) must first
  *manufacture* coefficients the natural fibres do not have — e.g. by a
  different fibre functor or an enriched atlas. **Named witness/proof design
  constraint:** `coefficient-free σ-fibres (escape (a))`.
- **(a)'s OBSTRUCTION is ZFC-trivial, even though its index cofinality VALUE is
  not ZFC-fixed.** Two things must be kept apart here, and conflating them
  would resurrect a retracted claim (see the ⚑ below):
  - *ZFC-trivial:* (i) the fibre coefficient layer — W2-1(1) discharges the
    set-theoretic content outright (no measurable `≤ 2^{ω₁}`, no hypothesis);
    and (ii) the **lim⁰-death mechanism** — `⋂_J (H∖J) = ∅` holds because each
    `x` drops at its own stage `{x}`, *regardless of the value of* `2^{ω₁}`.
  - *Not ZFC-fixed:* the **value** of (a)'s index cofinality, `≥ 2^{ω₁}`
    (W1) — which never enters the obstruction.

  > ⚑ **Do NOT phrase this as "(a)'s residue is spent set theory," and do not
  > cite any "degenerate-reduction reading" of W1.** W1's coordinate-reduction
  > of (a) to `[ω₁]^{≤ω}` was **RETRACTED** (W1 verdict §2.2, commit
  > `8497320`); W1's standing finding is that (a) is
  > **cardinal-arithmetic-sensitive**. An unqualified "residue is spent" would
  > contradict the W1 row in canon. The correct combined statement is the
  > two-part one above: **trivial obstruction, non-ZFC-fixed index value.**
- **The isolation's live set-theoretic half narrows toward (b)** — resting on
  the ground that **(a)'s obstruction mechanism is ZFC-trivial** (fibres rigid,
  death by empty intersection), which is independent of the retracted
  reduction. Pending (b)'s §3.2 scope call (concrete Cantor `I = C` vs abstract
  ℵ₁). ⚠ Stated as a narrowing of where to look, **not** as a theorem about
  (b) — (b)'s own fibres are NOT computed here.
- **Import to scout — NOT needed.** The non-trivial branch (set-valued /
  inhomogeneous limit theory) does not fire, since the fibres are
  singleton-or-empty rather than merely non-group-valued.

---

## 6. Hostile pass (gate doc §6)

**H1 — "Is `B_i` really full `P(G_i)`? That is where this breaks."** The
flagged risk, checked first. `oml_omega1_cylinder_hub.md` §2 reads verbatim
`B_i=P(G_i)`, so the computation above is correct **for the raw atlas**. The
hub's own §5 records that this raw atlas is **central**, hence *not itself an
admissible OML counterexample*, and that a σ-completion could de-centralize it
with "every new countable join, maximal block, and state relation" requiring
audit (**evidence class: open** in the source).

> ⚑ **CORRECTED 2026-07-21 (user's verification pass). An earlier version of
> this item claimed the risk was one-directional — "shrinking the block can
> only shrink or preserve the σ-fibre, since fewer sets cannot create
> non-principal σ-states where the powerset had none" — and concluded that the
> no-coefficients result was robust and only the fibre *pattern* was at risk.
> That claim is FALSE and is retracted.**
>
> **Counterexample (ZFC, no measurable anywhere).** For any uncountable `S`,
> the countable/co-countable σ-algebra `CC(S)` carries the **co-countable
> state**: `μ(E) = 1` if `E` is co-countable, `0` if countable. It is
> σ-additive (of pairwise disjoint sets at most one can be co-countable, since
> two disjoint co-countable sets would make `S` a countable union) and
> **non-principal** (`μ({s}) = 0` for every `s`). No large cardinal is used.
>
> **Why this does not contradict W2-1.** A σ-state on a sub-algebra is an
> ultrafilter **on that algebra**, *not* the restriction of one on `P(G_i)`.
> Coarsening removes obligations: split `S` into two uncountable halves — on
> `P(S)` a state must decide them, but `CC(S)` does not contain them, so the
> state is never asked. **Fewer sets = fewer obligations, and coarseness is
> exactly how non-principality gets cheap.**

**Corrected residual risk: BOTH the fibre pattern AND the no-coefficients
conclusion are OPEN under admissible re-derivation.** Only the computation on
the raw `P(G_i)` atlas is safe. The admissible version must contain `j_i(A)`,
which constrains how coarse its blocks can be; whether a *proper* sub-σ-algebra
containing all the traces can still harbour a non-principal σ-state is
**genuinely unresolved**.

**⚑ Full circle worth recording.** The configuration §3 Test 1 described — *one
non-principal state among Diracs* — is refuted as a description of **this**
atlas, but is precisely what a **coarse admissible block could legitimately
produce**. If the de-centralized version coarsens the blocks, the seed's
picture could resurrect at the admissible level, inhomogeneous fibre and all —
at which point **the originally proposed homogeneity test becomes the right
tool after all**, one architecture later than intended. Test 1 was not so much
wrong-in-kind as filed against the wrong object.

**H2 — "W2-1(1) is just Ulam, already in the hub note."** No — it is strictly
stronger and by a different route. Hub §3 rules out a σ-extension *of eval_i*
by pushing forward to ω₁ and citing Ulam. W2-1(1) rules out **every**
nonprincipal countably complete ultrafilter on `G_i`, via the measurable/strong-
limit bound. Ulam is the sharper statement about the coordinate index; the
measurable bound is what covers the whole powerset. W2 needs the latter,
because the fibre is a set of states on `P(G_i)`, not on the coordinate algebra.

**H3 — "Refuting an audit-certified seed's Test 1 — is this W1's mistake
again?"** Different situation, and checked against it. In W1 the session tried
to refute an audit-*certified* claim (the index-category fence) and was wrong.
Here (i) Test 1 is explicitly flagged in its own source as ⟦HAND, from the
banked architecture description; a fibre-cardinality census is the named finite
check⟧ and in the seed's §7 as "fibre census not yet computed" — it is
*self-labelled as un-computed*; (ii) the refutation is by direct contradiction
with hub §2's own theorem ("every σ-state of `A` is evaluation at a point"),
not by an imported principle; (iii) Test 1's *conclusions* are unaffected. This
is a recomputation of an explicitly-owed census, not an overturning of a
certified result.

**H4 — "lim⁰ death is a restatement of no-GS."** **Conceded, and stated as
such.** "The limit is empty" *is* no-GS. The non-trivial content of W2-3 is not
that the limit is empty but that the system is **set-valued with inclusion
bonding** — i.e. that there is no group-valued system here whose lim¹ could be
the obstruction. That is a statement about the *applicability of the machinery*,
not about the obstruction.

**H5 — "Does this prove limⁿ is not the obstruction for (a)?"** **No, and it is
not claimed.** W2 proves a fact about the *natural state fibres*: they carry no
coefficients. Whether some other functor on this architecture yields a
group-valued system with a meaningful derived limit is **not** decided here.
Promoting this to "limⁿ is/isn't the obstruction" would make the derived-limit
identification a premise, which Stage-0 §2 forbids. §5's conversion is phrased
as a constraint on routes, not a theorem about limⁿ.

**H6 — "The σ/fa table uses BPI; is the choice principle tracked?"** Yes. The
σ side is choice-free ZFC. The fa side uses BPI (Boolean ultrafilter lemma),
flagged inline in §4 and consistent with clause (a)'s BPI-exactness discipline.
The *contrast* between the layers is therefore partly a contrast in choice
strength, which is worth noting and is not hidden.

**H7 — "Is this consistent with W1's *corrected* finding, or does it lean on
the retracted one?"** Added after H1–H6 missed it: the first draft of §5
conversion (2) said "(a)'s residue is algebraic around spent set theory … the
fibre-level counterpart of **W1's degenerate-reduction reading**." **That was a
defect and is fixed.** W1 has no degenerate-reduction reading — the
coordinate-reduction of (a) to `[ω₁]^{≤ω}` was retracted (W1 §2.2, commit
`8497320`), and W1's standing finding is that (a) is
cardinal-arithmetic-sensitive. The stale phrase would have resurrected in canon
exactly the claim the previous session killed. Corrected statement: **(a)'s
*obstruction* is ZFC-trivial (fibre coefficients + the empty-intersection death
mechanism), while its *index cofinality value* is not ZFC-fixed** — no conflict,
because the index value never enters the obstruction. **Lesson: a hostile pass
that checks a note only against its own sources will not catch a contradiction
with a sibling verdict; cross-check the sibling's *current* state, not your
memory of it.**

---

## 7. Evidence classes

| Result | Grade |
|---|---|
| W2-1 — σ-fibres singleton-or-empty | **hand proved**, ZFC, choice-free ⟦HAND⟧ |
| W2-1(1) — no measurable `≤ 2^{ω₁}`; all σ-UFs on `G_i` principal | **hand proved**, ZFC outright (strong-limit argument) |
| W2-2 — no group-valued coefficients | **hand proved** (corollary) |
| W2-3 — set-valued system, lim⁰ death | **hand proved** (CSS/no-GS half is restatement — H4) |
| §3 — Test 1 fibre census refuted (2 errors) | **hand proved** (contradicts hub §2's own theorem) |
| §4 — fa-fibres large; σ/fa contrast | **hand proved**, uses BPI |
| Robustness under an admissible-OML `B_i` | **OPEN — both the pattern AND "no coefficients"** (H1, corrected). Coarsening can create non-principal σ-states in ZFC (`CC(S)`); only the raw `P(G_i)` computation is safe |
| (b) concrete Borel reading ⟹ Diracs (no measurable bound) | **hand proved** ⟦HAND⟧ (§9.1) — but *which* reading is operative is the user's call |
| Escape (b)'s fibres | **NOT COMPUTED** — deferred |
| lim¹/limⁿ identification for (a) | **TARGET, not established** (Stage-0 §2) |

---

## 8. Process rule (user-directed, general)

**Parked-seed numerics are quotable only after re-derivation — exactly like
external citations.** This is the second seed-era hand-argued description to
need recomputation before use (first: the index-category conflation corrected
in W1; now: Test 1's fibre census). A parked seed's *certified* claims remain
citable; its ⟦HAND⟧/un-computed censuses do not, and both of these were
self-labelled as such in their own sources. Applies wherever W2 output is
reused.

**Corollary (user, 2026-07-21): conversational summaries are part of the same
contamination surface.** The H7 defect entered via phrasings — "degenerate-
reduction reading," "residue is spent set theory" — that originated in *session
and user summaries* of W1 and carried the flavour of the retracted
coordinate-reduction even after its retraction had been endorsed by both
parties. Retracted claims propagate through prose about the work, not only
through the notes. **The sibling-cross-check (H7) must be run against the
sibling verdict's current text, never against anyone's recollection or summary
of it — including the user's.**

---

## 9. What this hands forward

### 9.1 The two open items are ONE mechanism (user's observation, 2026-07-21)

**H1's admissible-version risk and W1 §3.2's scope call for escape (b) are the
same question seen twice:** *coarse blocks admit ZFC non-principal σ-states;
fine ones do not.* The unifying principle is H1's counterexample — coarseness
removes obligations, and that is what makes non-principality cheap.

Applied to (b), the fork is sharp:

- **Concrete Borel reading (`I = C`, `B_i = Borel(R_i)`): fibres are Diracs**,
  by an argument *easier* than W2-1 and needing **no measurable bound at all**.
  On a countably generated separating σ-algebra with generators `(a_n)`, put
  `b_n = a_n` or its complement according to `μ`; σ-additivity gives
  `μ(⋂_n b_n) = 1`, so the intersection is nonempty, while separation allows at
  most one point in it. Hence `μ = eval_y`, principal. ⟦HAND — verified this
  session⟧ *(Same mechanism as hub §1's countably-generated extension theorem —
  reused, not new.)*
- **Abstract reading (any uncountable index, coarse blocks permitted): rich
  fibres are LIVE**, exactly as H1's `CC(S)` counterexample shows.

**Consequence for sequencing.** §9's prediction splits along precisely the §3.2
fork, so **running W2-for-(b) jointly with the scope call adjudicates both open
items in one move.** That is the recommended next step, and it is cheaper than
treating them separately.

⚠ The scope call itself — which reading is operative — is a **definition
decision and belongs to the user**, not to a session. W2 supplies the
consequence of each branch, not the choice.

### 9.2 Remaining hand-offs

- **W2 for escape (b) is the open remainder**, gated as in §9.1. Under the
  concrete reading expect **coefficient-free also**; under the abstract reading
  expect the opposite. Neither is a result until recomputed.

  > ⚑ **Self-catch, per §8.** An earlier draft of this line predicted a
  > *different* answer for (b) on the strength of the parked seed's Test 2
  > ("eligible fibres are continuum-sized"). That is exactly an un-recomputed
  > parked-seed numeric, which §8 forbids quoting. The prediction was re-derived
  > from W2-1's own argument instead, and is now superseded by §9.1's sharper
  > two-branch statement.
- **C-a is unaffected as a campaign.** W2 constrains the *route* (no limⁿ via
  natural fibres), not the target.
- **W3 (measure knot) is untouched** and its trigger is unchanged.
