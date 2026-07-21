# W1 — Index category determination: verdict

*2026-07-21. Executes W1 of `SIGMA_LAYER_TARGET.md` §3 (Stage-0 gate doc).
Scope: W1 only — no W2, no C-a, no grammar-engine run (A2 names no clause
here). Hostile pass in §6, as §6 of the gate doc requires.*

**Headline.** The two escape architectures have index posets of **different
shape, and the difference is exactly a CH-sensitivity**: escape (a) is
ZFC-robustly an ω₁-tower; escape (b) is `[𝔠]^{≤ω}`, which coincides with (a)
under CH and is strictly wider under ¬CH. Neither is ω^ω-like in the
eventual-domination sense. **The index-category fence
(`oml_odbc_sigma_nerve_absorption.md` §1) is CONFIRMED, not contradicted** —
see §5, which records a refutation attempt that failed and why.

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

### 2.1 The coordinate-reduction theorem (the load-bearing step)

**Naive reading (rejected).** The atlas is indexed by points `i ∈ H`, so the
section-system poset is `[H]^{≤ω} = [2^{ω₁}]^{≤ω}` — of cardinality `2^{ω₁}`,
none of the three named shapes.

**Theorem (a).** The section system factors through `[ω₁]^{≤ω}`; that is,
`[ω₁]^{≤ω}` is cofinal for the obstruction, and the point-breadth `2^{ω₁}` is
redundant. ⟦HAND⟧

*Proof.* Three facts from the hub note, combined.

1. **Every event is countably supported** (§2): each `E ∈ A` depends on only
   countably many of the ω₁ coordinates. So the σ-algebra `A` — the thing all
   the `B_i` share, and hence the thing a compatible section is a section
   *of* — is already organized by countable *coordinate* sets, not by points.
2. **Every σ-state of `A` is evaluation at a point** (§2), and a point is
   pinned by its ω₁ coordinates. A countable stage of the section system sees
   a countable set of coordinates and can only constrain the evaluation point
   through those.
3. **The non-extension is Ulam on ω₁** (§3): the obstruction to extending
   evaluation at `i` is the `D_α` partition indexed by `α < ω₁`, refuted by
   Ulam's ZFC theorem that ω₁ carries no nonprincipal countably complete
   ultrafilter. The failure is therefore *located at the coordinate ordinal*,
   not at the point index.

Hence the obstruction datum is a function of the countable coordinate set, and
countable coordinate sets are cofinally ordered by `[ω₁]^{≤ω}`. ∎

This is the step to attack; it is attacked in §6.

### 2.2 Cofinality

**Theorem (a′).** `cof([ω₁]^{≤ω}) = ℵ₁`, and the cofinal family may be taken
to be a **chain of order type ω₁**. ⟦HAND, standard ZFC⟧

*Proof.* ω₁ is regular, so every countable `J ⊆ ω₁` is bounded:
`J ⊆ [0,β)` for `β = sup(J)+1 < ω₁`. The initial segments `{[0,β) : β < ω₁}`
are countable sets (for `β ≥ ω`), are increasing under `⊆`, have order type
ω₁, and are cofinal by the previous sentence. ∎

**Verdict (a): ω₁-tower-like, ZFC-robust.** Cofinality ℵ₁ outright — no
cardinal arithmetic hypothesis is used.

**Worth stating: two of the three named shapes coincide here.** `[ω₁]^{≤ω}` *is*
cofinally an ω₁-tower. The trichotomy of the gate doc ("`[ω₁]^{≤ω}`-like,
ω₁-tower-like, or ω^ω-like") is not a partition at its first two entries; a
session need not choose between them for (a). Reporting the coincidence is the
honest answer rather than forcing one label.

**Not ω^ω-like.** ω^ω-likeness in the relevant sense means an
eventual-domination/scale structure with cofinality 𝔡. The (a) obstruction is
not a domination scale — it is Ulam measurability at ω₁, which is a ZFC
theorem with no dependence on cardinal characteristics.

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

**The two architectures differ, and the difference is a set-theoretic
sensitivity rather than a difference of kind.**

| | escape (a) | escape (b) |
|---|---|---|
| index set | ω₁ (after coordinate reduction, §2.1) | 𝔠 concrete / ω₁ abstract (§3.2) |
| poset | `[ω₁]^{≤ω}` | `[𝔠]^{≤ω}` / `[ω₁]^{≤ω}` |
| cofinality | **ℵ₁, ZFC** | **≥ 𝔠 — ℵ₁ iff CH** |
| cofinally a chain? | yes, ω₁-tower | iff CH |
| ω^ω-like? | no | no |
| grade | hand proved | hand proved, CH-sensitive |

They **coincide under CH** and **diverge under ¬CH**. Per the gate doc's
§3 warning, this is the substantive content of the "which set theory does the
residue belong to" question: **(a)'s residue is ZFC-robust; (b)'s residue is
axiom-sensitive unless the abstract ℵ₁ reading is the operative one.**

⚠ **Anti-confirmation-bias note.** The W1 prompt says "if they differ, that is
itself the finding," which biases toward manufacturing a difference. The
difference reported here is *not* manufactured: it is a cardinal-arithmetic
fact about `[𝔠]^{≤ω}` vs `[ω₁]^{≤ω}`, and under CH the claimed difference
**vanishes**. "They coincide under CH" is reported with equal weight.

---

## 5. Relation to the index-category fence — attempted refutation, FAILED

The fence (`oml_odbc_sigma_nerve_absorption.md` §1, audit-certified) says:
closure-based globalization arguments are valid **only over countably cofinal
index systems**; over `[ω₁]^{≤ω}` surjective bonding does not kill the derived
limit, so the correct object is limⁿ, not lim¹.

### 5.1 What this session's computation does to the fence: CONFIRMS it

Theorem (a′) gives `cof = ℵ₁ > ℵ₀`. So escape (a) is **not countably cofinal**,
and the fence's operational clause — the ML/closure shortcut is unavailable,
a CODBC proof must exhibit countably cofinal reduction or use general-index
derived-limit technology — **applies exactly**, and applies for a now-proved
reason rather than an assumed one. This is the fence's entire operational
content, and W1 confirms it.

### 5.2 A refutation was attempted and it failed — recorded so it is not retried

Mid-session this note's author derived an apparent contradiction with the
fence and came close to banking a retraction of an audit-certified claim. It
was wrong. Recorded in full, because the error is attractive:

**The bad argument.** `[ω₁]^{≤ω}` is cofinally an ω₁-*chain* (Theorem a′);
derived limits are invariant under cofinal subposets; over a chain with
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

**H1 — "Theorem (a) is a definitional dodge; you chose the index set that gave
you the answer you wanted."** The strongest objection. Answer: the choice is
forced by *where the obstruction lives*, not by convenience. §3 of the hub note
derives the non-extension from the `D_α` partition indexed by `α < ω₁` and
Ulam's theorem on ω₁; no step of that argument mentions a point of `H` except
as the thing being separated. A section system whose failure is certified at
ω₁ cannot have its obstruction carried by `[2^{ω₁}]^{≤ω}` in any way that
matters. **Residual risk: REAL but bounded.** What is proved is that the
obstruction *factors through* `[ω₁]^{≤ω}`; what is *not* proved is that no
finer information is carried by the point index. If a later construction makes
the point-index breadth load-bearing (e.g. by distinguishing atlas members
beyond their coordinate support), Theorem (a) must be re-derived. Stated as a
scope condition, not hidden.

**H2 — "cof([𝔠]^{≤ω}) ≥ 𝔠 is trivial."** Granted, and labelled as such — it is
one line. Its *content* is not the inequality but the CH-sensitivity it exposes
in (b), which is what makes the (a)/(b) comparison a real finding.

**H3 — "The (a)/(b) difference is an artifact of reading (b) concretely."**
Partly conceded — §3.2 records exactly this and marks the reading question
**open** rather than picking the one that produces a difference. Under the
abstract ℵ₁ reading the architectures coincide. This is why §4 reports the
coincidence with equal weight.

**H4 — "This is near-tautological, like the §2 restatement the fence warns
about."** Distinguish. The fence's §2 warns that "CODBC failure manifests at
uncountable cofinality" is a restatement of CSS∧¬GS. That is not what is
claimed here. Theorem (a′) computes cofinality *exactly* (ℵ₁, with a chain
witness), and Theorem (a) identifies *which set* it is the cofinality of —
neither follows from CSS∧¬GS, which gives only "uncountable."

**H5 — "You confirmed a fence you had just tried to refute; is the
confirmation motivated reasoning in reverse?"** The confirmation rests on
`cof = ℵ₁ > ℵ₀` (Theorem a′) alone, which was proved before the refutation was
attempted and is independent of it. The failed refutation is recorded in full
in §5.2 precisely so a reader can check that the retraction was dropped for a
stated mathematical reason — a contradiction with a published theorem — and
not by deference.

**Not asserted anywhere in this note:** that lim¹ or limⁿ *is* the obstruction
for either architecture; that (b)'s concrete reading is the operative one; that
Theorem (a) survives a construction making point-breadth load-bearing.

---

## 7. Evidence classes and receipts

| Result | Grade |
|---|---|
| Theorem (a) — coordinate reduction to `[ω₁]^{≤ω}` | **hand proved** ⟦HAND⟧, scope condition in H1 |
| Theorem (a′) — `cof([ω₁]^{≤ω}) = ℵ₁`, chain witness | **hand proved**, standard ZFC |
| Theorem (b) — `cof([κ]^{≤ω}) ≥ κ` | **hand proved**, one line |
| (b) CH-sensitivity | **hand proved** (from Theorem (b) + `𝔠=ℵ₁ ⟺ CH`) |
| Which (b) reading is operative | **open** (§3.2) |
| Fence confirmed operationally | **hand proved** (from a′: not countably cofinal) |
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

- **W2** inherits a settled index shape for (a) (ω₁-tower, ZFC) and a
  *conditional* one for (b). W2's typing run should be read separately in the
  CH and ¬CH cases for (b), or should first settle §3.2's reading question.
- **C-a vs C-b ordering.** No reordering is recommended. The gate doc §4 permits
  promoting C-b if W1 makes it cheaper; W1 makes it **not cheaper** — (b)'s
  index structure is the axiom-sensitive one, and (a)'s is ZFC-robust, so (a)
  remains the target whose closure is unconditional. One line, as §4 asks.
- **A fence-clarification pass** (§5.3) is the one new small item: confirm that
  "limⁿ not lim¹" means the general technology, not literally lim² over ω₁.
