# W2 — Coefficient normalization: verdict (escape (a))

*2026-07-21. Executes W2 of `SIGMA_LAYER_TARGET.md` §3, scoped to escape (a).
The trichotomy re-run is PARKED by user decision (redundant: §6 of the parked
seed already ran it, audit-certified accurate, and the audit itself called the
result hollow — T0 restates CSS∧¬GS). W2 here is the coefficient layer only:
what group, if any, acts on the fibres. No W1 re-opening; no grammar-engine run
(no clause named, per A2).*

**Headline.** For escape (a) the σ-fibres are **singleton-or-empty in ZFC**.
There is no coefficient structure at all — not ℤ/2, not any group, and not even
an inhomogeneous set to test for homogeneity. The section system is
**set-valued with inclusion bonding**, and its obstruction is **lim⁰ death**
(every stage nonempty, limit empty). The group-valued derived-limit machinery
has nothing to act on for escape (a).

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
extending the filter generated by `{E ∩ G_i : x ∈ E ∈ A}`. That filter is not
an ultrafilter on `P(G_i)`: `|P(G_i)| = 2^{2^{ω₁}}` vastly exceeds `|A| =
2^{ω₁}`, so some `S ⊆ G_i` is undecided by it and both `S` and its complement
extend it. Hence many lifts. At the puncture, hub §3's trace filter
`{E∖{i} : i ∈ E ∈ A}` is proper and BPI-extendable; every such ultrafilter is
non-principal, since the countably-supported `E ∋ i` have empty intersection
(coordinates separate points).

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
- **The residue for (a) is algebraic around spent set theory.** The set-theoretic
  content is discharged by W2-1(1): no measurable `≤ 2^{ω₁}` is a ZFC theorem,
  and after it is applied nothing set-theoretically live remains at the fibre
  level. This is the fibre-level counterpart of W1's degenerate-reduction
  reading for (a).
- **The isolation's live set-theoretic half narrows toward (b)**, pending (b)'s
  §3.2 scope call (concrete Cantor `I = C` vs abstract ℵ₁). ⚠ Stated as a
  narrowing of where to look, **not** as a theorem about (b) — (b)'s own fibres
  are NOT computed here.
- **Import to scout — NOT needed.** The non-trivial branch (set-valued /
  inhomogeneous limit theory) does not fire, since the fibres are
  singleton-or-empty rather than merely non-group-valued.

---

## 6. Hostile pass (gate doc §6)

**H1 — "Is `B_i` really full `P(G_i)`? That is where this breaks."** The
flagged risk, checked first. `oml_omega1_cylinder_hub.md` §2 reads verbatim
`B_i=P(G_i)`. **Residual risk: REAL, and scoped.** The hub's own §5 records
that this raw atlas is **central**, hence *not itself an admissible OML
counterexample*, and that a σ-completion could in principle de-centralize it
with "every new countable join, maximal block, and state relation" requiring
audit (**evidence class: open** in the source). If an admissible-OML version
replaces `P(G_i)` with a *proper* sub-σ-algebra, W2-1 must be re-derived. Note
the direction of the risk: shrinking the block can only **shrink or preserve**
the σ-fibre (fewer sets to be an ultrafilter on cannot create non-principal
σ-states where the powerset had none) — but it can change *which* traces lift,
so the singleton/empty pattern is what needs rechecking, not the absence of
coefficients. **The "no coefficients" conclusion is robust to this; the exact
fibre pattern is not.**

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
| Robustness under an admissible-OML `B_i` | **open** (H1) — "no coefficients" robust, exact pattern not |
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

---

## 9. What this hands forward

- **W2 for escape (b) is the open remainder.** It should be run only after
  (or alongside) the §3.2 reading call from the W1 verdict, since `I = C` vs
  abstract ℵ₁ changes the block set. Expect a *different* answer: (b)'s
  fibres are described in the parked seed's Test 2 as continuum-sized — but per
  §8 that description is un-recomputed and must not be quoted until checked.
- **C-a is unaffected as a campaign.** W2 constrains the *route* (no limⁿ via
  natural fibres), not the target.
- **W3 (measure knot) is untouched** and its trigger is unchanged.
