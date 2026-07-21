# W1 — Index category determination: verdict

*2026-07-21. Executes W1 of `SIGMA_LAYER_TARGET.md` §3 (Stage-0 gate doc).
Scope: W1 only — no W2, no C-a, no grammar-engine run (A2 names no clause
here). Hostile pass in §6, as §6 of the gate doc requires.*

**Headline.** Both index posets are of the **same kind** — countable sets of
*blocks*, `[κ]^{≤ω}` — but at **different cardinals**: escape (a) is
`[2^{ω₁}]^{≤ω}` (cof `≥ 2^{ω₁} ≥ ℵ₂`, **never** an ω₁-tower, ZFC); escape (b)
is `[𝔠]^{≤ω}` (cof `≥ 𝔠`, an ω₁-tower **iff CH**). So they **differ under CH**
— (b) is a tower there, (a) is not — and both are uncountably cofinal in every
model. Neither is ω^ω-like. The tempting reduction of (a) to `[ω₁]^{≤ω}` (its
*coordinate* poset, cofinality ℵ₁) is **false as a cofinality claim** — §2.2.
**The index-category fence (`oml_odbc_sigma_nerve_absorption.md` §1) is
CONFIRMED**, a fortiori — see §5, which also records a refutation attempt that
failed and why.

⚠ **This note's first version claimed the opposite for (a)** ("factors through
`[ω₁]^{≤ω}`, cofinality ℵ₁, ZFC-robust"). That claim was **WRONG and is
retracted in §2.2** before ever leaving the branch. The error and its tell are
recorded rather than quietly fixed, because the tell is reusable.

---

## 1. What is being computed, and what is not

W1 asks for the **cofinal structure of the section-system index poset**. That
is a pure ZFC cofinality question about a poset. It is *not* a derived-limit
adjudication, and nothing below promotes the lim¹/limⁿ identification from
target to premise (Stage-0 §2). §5 keeps the two strictly apart.

**Reading of "the index poset."** The atlas of §4 of the cylinder hub has a
compatible σ-section over every *countable* subfamily; the index poset is
therefore the poset of countable subsets of the relevant index set, ordered by
inclusion. The live question is *which* index set — and the answer for (a) is
not the naive one. See §2.

---

## 2. Escape (a) — the ω₁ cylinder hub

Object: `oml_omega1_cylinder_hub.md` §2–§4. `I = ω₁`, `H = 2^I`, `A` = the
countable-support product σ-algebra, `B_i = P(H \ {i})` for `i ∈ H`, atlas
`(B_i)_{i∈H}`.

### 2.1 The index poset is the block poset

The atlas is `(B_i)_{i∈H}` — one block per **point** `i ∈ H`. §4 of the hub
note gives compatible σ-sections over every **countable** subfamily and none
globally. A stage of the section system is therefore a countable set of
*blocks*, i.e. a countable `J ⊆ H`.

**Theorem (a).** The section-system index poset for escape (a) is
`[H]^{≤ω} = [2^{ω₁}]^{≤ω}`, with `cof ≥ 2^{ω₁}`. ⟦HAND⟧

*Proof.* Index set is `H` by the previous paragraph; apply Theorem (b) of §3.1
at `κ = |H| = 2^{ω₁}`. ∎

**Verdict (a): cardinal-arithmetic-sensitive; NOT an ω₁-tower.** `2^{ω₁}` is
not decided by ZFC (Easton), so the cofinality of (a)'s index poset is not a
ZFC-fixed value. It is `≥ 2^{ω₁} ≥ ℵ₂` always, so the poset is **never** a
chain of type ω₁ and never countably cofinal.

**Not ω^ω-like.** ω^ω-likeness in the relevant sense means an
eventual-domination/scale structure with cofinality 𝔡. (a)'s obstruction is
not a domination scale — it is Ulam measurability at ω₁.

### 2.2 RETRACTED: the coordinate-reduction "theorem"

This note's first version claimed the section system **factors through**
`[ω₁]^{≤ω}` — that events are countably supported, σ-states are point
evaluations, the non-extension is Ulam at ω₁, so the `2^{ω₁}` point-breadth is
"redundant" — yielding cofinality ℵ₁ and a ZFC-robust ω₁-tower. **That claim
is false. It is retracted.** Three independent refutations:

1. **A countable coordinate set pins no point.** Fix countable `S ⊆ ω₁`. The
   points of `H` agreeing on `S` number `2^{|ω₁∖S|} = 2^{ω₁}`. So the step
   "a countable stage constrains the evaluation point through its coordinates"
   fails outright: it constrains it not at all, down to `2^{ω₁}` candidates.
2. **Cofinality is an invariant.** A factorization through `[ω₁]^{≤ω}` would
   require it to be cofinal in `[2^{ω₁}]^{≤ω}`. Cofinally equivalent posets
   have equal cofinality, and `ℵ₁ ≠ cof([2^{ω₁}]^{≤ω}) ≥ 2^{ω₁} ≥ ℵ₂`. No
   limit-preserving reduction exists.
3. **Point-breadth is load-bearing, by the hub's own §4.** There is no global
   section "because every common `A` σ-trace is evaluation at some `x`, which
   does not extend σ-additively to `B_x`" — the failure must block **every**
   `x ∈ H`, so all `2^{ω₁}` blocks participate. Breadth is what makes the
   atlas CSS∧¬GS; it is not redundant.

**The tell, recorded because it is reusable.** The first version applied *two
different rules* to the two architectures: for (b) it indexed by the block/point
set (`C`), for (a) by the *coordinate* set (ω₁) rather than the block set
(`H = 2^{ω₁}`). Same geometry, opposite choice. The asymmetry is what made the
false "they differ, and (a) is the robust one" headline look natural — in (b)
the coordinates are ℕ (visibly not the index), in (a) they are ω₁ (uncountable,
hence temptingly index-shaped). **Rule to carry forward: the section-system
index is whatever the atlas has one block per — check it against a second
architecture before trusting it.**

**What survives the retraction.** `cof([ω₁]^{≤ω}) = ℵ₁`, with a cofinal chain
of order type ω₁, remains **true and hand-proved** — as a fact about the
*coordinate* poset, which is not the index poset. (ω₁ regular ⟹ every countable
`J ⊆ ω₁` is bounded by `sup(J)+1`; the initial segments `[0,β)` are countable,
increasing, cofinal.) It is the poset the fence's derived-limit machinery
*would* engage **if** the obstruction factored through coordinates — and by (1)
above it does not. **Any such factorization is a TARGET, not established**
(Stage-0 §2), and refutation (2) makes it false at the cofinality level.

---

## 3. Escape (b) — the distributed nonseparating quotients

Object: `oml_distributed_relation_cell_assembly.md` §1–§4. Here the concrete
hub is Cantor space `C = 2^ℕ`, `I = C`, one hub variable, `G_i = C \ {i}`,
and the σ-section space over `J ⊆ I` is `C \ J` (§1).

### 3.1 Cofinality

The section-system poset is `[𝔠]^{≤ω}` under the concrete reading (`|C| = 𝔠`).

**Theorem (b).** `cof([κ]^{≤ω}) ≥ κ` for uncountable `κ`. ⟦HAND⟧

*Proof.* A cofinal `F ⊆ [κ]^{≤ω}` must have `⋃F = κ` (every singleton lies in
some member), so `κ = |⋃F| ≤ |F|·ℵ₀`, giving `|F| ≥ κ` for uncountable κ. ∎

**Verdict (b): CH-sensitive.**
- Under **CH** (`𝔠 = ℵ₁`): `cof([𝔠]^{≤ω}) = ℵ₁` and (b) is cofinally an
  ω₁-tower — **the same shape as (a)**.
- Under **¬CH** (`𝔠 ≥ ℵ₂`): `cof([𝔠]^{≤ω}) ≥ 𝔠 > ℵ₁`, and the poset is **not**
  a chain — strictly wider than (a).

### 3.2 The abstract reading, and why it does not settle (b)

§1 of the cell-assembly note says "ℵ₁ suffices abstractly" — an uncountable
index is necessary and ℵ₁ is enough for the abstract CSS-without-GS system.
Under that reading (b) reduces to `[ω₁]^{≤ω}` and coincides with (a) outright.

The two readings genuinely differ and the note licenses both: the *abstract*
system needs only ℵ₁, the *concrete Cantor realization* has `I = C`. This is
recorded as an ambiguity in the source, not resolved by fiat. **Evidence class:
open** — which reading is load-bearing depends on whether a construction is
required to use the concrete Cantor hub (where §3's σ-closure regenerates all
Borel singletons) or may use any uncountable index.

**Not ω^ω-like either.** The (b) obstruction depth is *countable* — the
decreasing clopen basis `(U_n)` of §3. There is no domination scale.

---

## 4. The finding, stated plainly

**Both index posets are `[κ]^{≤ω}` over the BLOCK set — the same kind of poset
at different cardinals. (a) is never an ω₁-tower; (b) is one exactly under CH.
So they differ under CH and are both uncountably cofinal always.**

| | escape (a) | escape (b) |
|---|---|---|
| block set | `H = 2^{ω₁}` | `C = 𝔠` concrete / ω₁ abstract (§3.2) |
| index poset | `[2^{ω₁}]^{≤ω}` | `[𝔠]^{≤ω}` / `[ω₁]^{≤ω}` |
| cofinality | **≥ 2^{ω₁}** (≥ℵ₂ always; value not ZFC-fixed) | **≥ 𝔠** — ℵ₁ iff CH |
| cofinally a chain? | **never** | iff CH |
| ω₁-tower-like? | no | iff CH |
| ω^ω-like? | no | no |
| grade | hand proved | hand proved, CH-sensitive |

**Answer to "which set theory does the residue belong to."**

- **Escape (a): none of the three named shapes, in every model of ZFC.** It is
  `[2^{ω₁}]^{≤ω}`, uncountably cofinal with `cof ≥ ℵ₂`, so it is never an
  ω₁-tower; and it is not a domination scale. The gate doc's menu
  (`[ω₁]^{≤ω}`-like / ω₁-tower-like / ω^ω-like) simply does not contain the
  answer. Per the W1 prompt, "none of the three shapes" is a legitimate finding
  and is banked as such rather than forced into a label.
- **Escape (b): ω₁-tower-like exactly under CH**, and none of the three
  otherwise (still not a domination scale). Additionally conditional on §3.2's
  unresolved reading.

So the residue is **not** ZFC-robustly located in the tower world for either
architecture, and for (a) it is ZFC-robustly *outside* it. The *shape* verdicts
just given are themselves ZFC theorems; what is not ZFC-fixed is the *value* of
the cofinality (`2^{ω₁}`, `𝔠`).

⚠ **Anti-confirmation-bias note.** The W1 prompt says "if they differ, that is
itself the finding," which biases toward manufacturing a difference. The first
version of this note **did** manufacture one — see §2.2 — by indexing (a) by
coordinates and (b) by blocks. The corrected difference is real but *smaller
and differently located* than the retracted one: same **kind** of poset
(`[κ]^{≤ω}` over blocks), different cardinals, with the only clean qualitative
split being that (b) becomes an ω₁-tower under CH and (a) never does.

---

## 5. Relation to the index-category fence — attempted refutation, FAILED

The fence (`oml_odbc_sigma_nerve_absorption.md` §1, audit-certified) says:
closure-based globalization arguments are valid **only over countably cofinal
index systems**; over `[ω₁]^{≤ω}` surjective bonding does not kill the derived
limit, so the correct object is limⁿ, not lim¹.

### 5.1 What this session's computation does to the fence: CONFIRMS it

Theorem (a) gives `cof ≥ 2^{ω₁} > ℵ₀` and Theorem (b) gives `cof ≥ 𝔠 > ℵ₀`. So
**neither** escape is countably cofinal, and the fence's operational clause —
the ML/closure shortcut is unavailable, a CODBC proof must exhibit countably
cofinal reduction or use general-index derived-limit technology — **applies to
both**, for a now-proved reason rather than an assumed one. This is the fence's
entire operational content, and W1 confirms it.

The retraction of §2.2 **strengthens** this rather than weakening it: the
confirmation now rests on `2^{ω₁} > ℵ₀` and `𝔠 > ℵ₀`, which are ZFC facts
requiring no cardinal-arithmetic hypothesis at all, instead of on the (false)
ℵ₁ computation. The fence stands a fortiori.

### 5.2 A refutation was attempted and it failed — recorded so it is not retried

Mid-session this note's author derived an apparent contradiction with the
fence and came close to banking a retraction of an audit-certified claim. It
was wrong. Recorded in full, because the error is attractive:

*(Note: this is a **different** error from the one retracted in §2.2. That one
was about which poset indexes escape (a); this one is about what derived-limit
theorems say over `[ω₁]^{≤ω}`. Both were caught before banking. This subsection
is about `[ω₁]^{≤ω}` as an abstract poset and does **not** depend on (a)'s
index poset being `[ω₁]^{≤ω}` — which §2.2 shows it is not.)*

**The bad argument.** `[ω₁]^{≤ω}` is cofinally an ω₁-*chain* (§2.2's surviving
fact); derived limits are invariant under cofinal subposets; over a chain with
surjective bonding, lim¹ = 0 by Mittag-Leffler; Goblot at cofinality ℵ₁ kills
limⁿ for n ≥ 2 (n>k+1=2, plus n=k+1=2 when surjective). So surjective bonding
kills *every* derived limit over `[ω₁]^{≤ω}`, contradicting the fence.

**Why it is false.** The step "surjective + ω₁-chain ⟹ lim¹=0" fuses two
different theorems. Goblot at k=1 gives vanishing only for **n ≥ 2**; it says
**nothing about lim¹**. "Surjective ⟹ lim¹=0" is Mittag-Leffler, an
**ω-indexed (countable-cofinality)** theorem. Transfinite ML additionally
requires **continuity at limit stages** (`X_λ = lim_{α<λ} X_α`), which
surjectivity alone does not supply. lim¹ over an ω₁-tower is precisely what
*measures* the failure of limit-stage continuity — the Hausdorff-gap
phenomenon.

**The decisive check (contradiction against a published theorem).** Assume the
bad step. Under CH, `𝔟 = 𝔡 = ℵ₁`, so ω^ω carries a scale: a `≤*`-increasing
`≤*`-cofinal family of order type ω₁. The Mardešić–Prasolov system **A** is
indexed by `(ω^ω, ≤)` with terms `A_f = ⨁_{I(f)} ℤ` and bonding maps the
natural projections of a direct sum — hence **surjective**. Cofinal-subposet
invariance transports lim¹**A** onto that ω₁-chain. The bad step would then give
lim¹**A** = 0 under CH — contradicting Mardešić–Prasolov's theorem that
lim¹**A** ≠ 0 under CH. So the bad step is false. ∎

Note the irony worth remembering: the cofinal-invariance principle used to
*build* the contradiction is what *dissolves* it.

**Lesson (matches the repo's standing one).** Goblot's hypothesis was read
off a search summary and then silently widened. Both load-bearing literature
facts were subsequently confirmed verbatim against primary text (§7) — and
that is what caught it.

### 5.3 One nuance left OPEN for clarification (not a retraction)

At cofinality exactly ℵ₁, Goblot kills limⁿ for n ≥ 2 (surjective case) and
leaves **lim¹ as the live invariant**; higher limⁿ become live only at
`[ω_n]^{≤ω}` for larger n. That sits in *surface* tension with the fence's
phrase "the correct obstruction object is limⁿ, not lim¹."

**Charitable and almost certainly intended reading:** the fence means the
general higher-derived-limit *technology* / the ZFC-robust program
(Bergfalk–Lambie-Hanson) as against the naive ω-tower lim¹-with-ML argument —
not literally "lim² over ω₁." Under that reading there is no tension at all.

**Status: OPEN clarification, deliberately not adjudicated here.** Adjudicating
it would require promoting the derived-limit identification to a premise, which
Stage-0 §2 forbids. W1 computes cofinality; it does not decide which derived
functor carries the obstruction. ⟦Flagged for W2 or a fence-clarification pass⟧

---

## 6. Hostile pass (required by gate doc §6 before banking)

**H1 — "Is the index really the block set, or could it be the coordinate
set?"** This is the question the first version got wrong, so it gets the
sharpest answer. The index is the block set because *that is what the atlas is
a family over*: `(B_i)_{i∈H}`, one block per point, and §4's sections are over
countable subfamilies of it. The coordinate set enters the hub note only in
describing the *internal structure* of the shared algebra `A`, never as an
index for the section system. Decisive check: a countable coordinate set leaves
`2^{ω₁}` points undetermined (§2.2(1)), so coordinates cannot even in principle
index the stages of a system whose sections are point evaluations. **Residual
risk: LOW.** The remaining way to be wrong is if a future re-posing makes the
atlas a family over something other than `H` — in which case the index changes
with it, and this theorem is re-derived, not patched.

**H2 — "cof([κ]^{≤ω}) ≥ κ is trivial."** Granted, and labelled as such — it is
one line. But it is now doing *all* the work for both architectures, which is
the honest state of affairs: W1's answer is a one-line cardinality argument
applied twice, and the difficulty was never in the computation but in
identifying the right index set (H1). Reporting an easy answer as easy is
preferable to dressing it up.

**H3 — "The (a)/(b) comparison is an artifact of reading (b) concretely."**
Conceded and marked **open** in §3.2. Note the corrected finding is far less
sensitive to this than the first version was: under *either* (b) reading, both
architectures are non-countably-cofinal and cardinal-arithmetic-governed. The
reading question changes *which cardinal*, not the shape verdict.

**H4 — "This is near-tautological, like the §2 restatement the fence warns
about."** Partly **conceded**, more than the first version admitted. The fence's
§2 warns that "CODBC failure manifests at uncountable cofinality" restates
CSS∧¬GS. The corrected §4 verdict — both posets uncountably cofinal, governed
by cardinal arithmetic — is *closer* to that restatement than the retracted
ℵ₁-tower claim was. What is genuinely more than restatement: the identification
of the exact cardinals (`2^{ω₁}`, `𝔠`), the proof that the coordinate reduction
is **false** (§2.2, a real negative result that removes a route), and the
consequent finding that **none of the three named shapes** applies. The
"uncountable cofinality" part alone would indeed be near-tautological.

**H5 — "You confirmed a fence you had just tried to refute; is the
confirmation motivated reasoning in reverse?"** The confirmation rests only on
`2^{ω₁} > ℵ₀` and `𝔠 > ℵ₀` — ZFC facts independent of the refutation attempt
and of the retracted claim. The failed refutation is recorded in full in §5.2
so a reader can check the retraction was dropped for a stated mathematical
reason (contradiction with a published theorem), not by deference.

**H6 — "The note retracts its own headline mid-file; is anything left
trustworthy?"** Fair to ask. What is load-bearing and *unaffected* by the
retraction: §5.2's Goblot/Mardešić–Prasolov analysis (independent of the index
computation, and the session's most substantive content), the verbatim
primary-source receipts (§7), and Theorem (b). What changed is the (a)
computation and everything downstream of it, all corrected in place with the
error left visible. The retraction was caught *before* the branch left the
machine, by applying the note's own (b) rule back to (a).

**Not asserted anywhere in this note:** that lim¹ or limⁿ *is* the obstruction
for either architecture; that (b)'s concrete reading is the operative one; that
any coordinate-level reduction of (a) exists (§2.2 refutes it).

---

## 7. Evidence classes and receipts

| Result | Grade |
|---|---|
| Theorem (b) — `cof([κ]^{≤ω}) ≥ κ` for uncountable κ | **hand proved**, one line |
| Theorem (a) — (a)'s index poset is `[2^{ω₁}]^{≤ω}`, `cof ≥ 2^{ω₁}` | **hand proved** ⟦HAND⟧ (index identification + Thm (b)) |
| (a) cardinal-arithmetic-sensitive, never an ω₁-tower | **hand proved** (`2^{ω₁} ≥ ℵ₂`, value Easton-free) |
| (b) `[𝔠]^{≤ω}`, CH-sensitivity | **hand proved** (Thm (b) + `𝔠=ℵ₁ ⟺ CH`) |
| Neither is ω^ω-like; none of the three named shapes fits (a) | **hand proved** |
| ~~coordinate reduction of (a) to `[ω₁]^{≤ω}`, cof ℵ₁~~ | **RETRACTED — FALSE** (§2.2, three refutations) |
| `cof([ω₁]^{≤ω}) = ℵ₁` with ω₁-chain witness | **hand proved**, standard ZFC — but about the *coordinate* poset, which is **not** the index poset |
| Which (b) reading is operative | **open** (§3.2) |
| Fence confirmed operationally | **hand proved** (both cofinalities `> ℵ₀`, a fortiori) |
| §5.3 limⁿ-vs-lim¹ phrasing | **open clarification**, not adjudicated |
| lim¹/limⁿ identification for these architectures | **TARGET, not established** (Stage-0 §2) |

**Primary-source receipts (both fetched and confirmed verbatim 2026-07-21):**
- **Goblot's vanishing theorem**, quoted from arXiv:2507.05471 (*Higher limits
  of wider systems*): "If the indexing order of a directed inverse system **X**
  of abelian groups is of cofinality ℵₖ for some k<ω then limⁿ**X**=0 for all
  n>k+1; if, in addition, the transition maps of **X** are all surjective, then
  limⁿ**X**=0 for n=k+1 as well."
- **Mardešić–Prasolov index set**, same source: **A**_λ is "the inverse system
  of abelian groups indexed by (ω^λ, ≤)", terms `A_f := ⨁_{I(f)} ℤ`, transition
  maps "the natural projections"; `A = A_{ℵ₀}`. Confirms the M–P system is
  **ω^ω-indexed**, *not* `[ω₁]^{≤ω}` — the distinction §5.2 turns on.
- lim¹**A** ≠ 0 under CH: Mardešić–Prasolov (TAMS 1988), as recorded in the
  seed's T5 row and corroborated by the fetched sources.

Corroborating internal cross-check: `SIGMA_NERVE_AUDIT_VERDICT.md` Q5 already
certifies "over `[ω₁]^{≤ω}` (σ-directed, cofinality ω₁) surjectivity does not
force vanishing" — i.e. the audit had already recorded cofinality ω₁,
independently of this session's derivation.

---

## 8. What this hands to the next step

- **W2** inherits the *same* index shape for both architectures (countable sets
  of blocks, uncountably cofinal, cardinal-arithmetic-governed) — so the typing
  run need not branch on architecture at the index level. For (b) it should
  still split CH/¬CH, or first settle §3.2's reading question.
- **C-a vs C-b ordering: NO reordering, but the earlier basis is withdrawn.**
  The gate doc §4 permits promoting C-b if W1 makes it cheaper. W1 does not:
  the corrected computation shows the two are *the same shape*, so W1 supplies
  **no index-structure reason to prefer either**. C-a therefore stays first on
  its pre-existing grounds (it is the main push under A1), not on any
  robustness advantage — the first version's "(a) is ZFC-robust, so prefer it"
  argument is **retracted along with §2.2**. One line, as §4 asks.
- **A fence-clarification pass** (§5.3) is the one new small item: confirm that
  "limⁿ not lim¹" means the general technology, not literally lim² over ω₁.
- **A new constraint for the witness/proof side**, per the A1 conversion
  discipline: any closure-based or ML-style globalization argument aimed at
  either escape must confront an index poset of cofinality `≥ 𝔠` (b) or
  `≥ 2^{ω₁}` (a). Countably-cofinal reduction is not merely unavailable — for
  (a) it is *provably impossible* (§2.2(2)), since no poset of cofinality ℵ₁
  can be cofinal in one of cofinality `≥ 2^{ω₁}`. **Named tameness mechanism
  ruled out: coordinate-support reduction.**
