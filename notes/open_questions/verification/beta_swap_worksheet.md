# The (β) swap — closure, hinge, and the finite→limit degeneration

**Status: LLM-ATTEMPTED DERIVATION, 2026-06-10. NOT VERIFIED.** Per CLAUDE.md
("verify LLM proofs independently") and [[feedback_verify_by_building]], every
claim here is a candidate for the user to check by hand or in Lean. Confidence
flags are mine and are fallible. Primary source: `navara_1992.pdf` (PAMS 115,
1992 — superseded resolution below).

> ## ⚑ RESOLUTION APPENDED 2026-06-10 (Path A + Path B) — hinge leans YES
>
> After writing §1–§4 below (which ended "leans NO / localized to two cruxes"),
> Paths A and B were run and **converge on hinge = YES**, completing the notes'
> own corrected reasoning. Read this box first; §3's adversarial-check caveats
> are **resolved** by Path A.
>
> **Path A (re-read Navara p.428 for the order question).** Navara defines `L`
> as a **sublogic of the product** `W = ∏ V` — a *subset* satisfying constancy,
> **not** a quotient/MacNeille completion — and proves closure by taking the
> join **"in W"** (coordinatewise) and showing it already lands in `L`. So **`L`'s
> order is the restriction of `W`'s product order (coordinatewise); no elements
> or order relations are added.** Hence (item 1) `p = ⋁ₙ b|Cₙ` is **not enlarged**
> (it is the coordinatewise join), and (item 2) `≤` is **coordinatewise, not a
> completion order** — so `p ⊀ aₙ^⊥` block-locally **does** transfer to `L`.
> Both §3 adversarial worries dissolve. *(This is THE load-bearing reading —
> user must re-verify p.428 directly. If `L` were a completion, this flips.)*
>
> **Path B (`beta_swap_finite_hinge.py`).** Modelling `L₂^(N) = MO₂^N`
> coordinatewise (faithful **iff** Path A holds), (★) **holds at every finite
> truncation N=2,3,4,5,8**: for each block `i`, `p∧aᵢ=0` ✓ and `p ⊀ aᵢ^⊥` ✓
> (because `aᵢ^⊥ = (a' on block i, 1 elsewhere)` and `b ⊀ a'` is the MO₂ gap).
> If the order is coordinatewise, **nothing changes at N=∞** ⟹ hinge YES.
>
> **Reconciliation with the "segregation/leans-NO" memory.** The notes'
> segregation argument was **already self-retracted** by the 2026-06-08 session
> ("vacuous probe… **Discard it**"), replaced by the element-vs-family (★) and
> the **same witness `p` built here**, with *transfer* flagged as the sole open
> step. Path A reads the transfer (coordinatewise ⟹ transfers); Path B confirms
> the witness. **The memory's "verdict leans FALSE" carried the *retracted*
> intuition, not the notes' final state.** This work does not contradict the
> notes — it completes them.
>
> **NET (pending user verification of Path A):** hinge **YES** ⟹ `L₂` satisfies
> (★) ⟹ concrete σ-orthocomplete non-Boolean OML exercising descent ⟹
> **"richness starves concreteness" is FALSE**, `L₂` is a second (concrete)
> witness ⟹ **flip park → ATTACK.**
>
> **What user must verify (in priority):** (i) Path A's reading of p.428
> (sublogic-of-product, coordinatewise order — the load-bearing fact); (ii) that
> `aᵢ^⊥` is coordinatewise also for union-of-block-supported elements (only
> single-block checked); (iii) Claim 1's closure (VERIFY 1).
>
> ---
>
> *(Original §1–§4 below preserved as the derivation path; §3's "leans NO /
> distrust Claim 3" is now superseded by Path A, but kept for the audit trail.)*

Primary source: `navara_1992.pdf` (PAMS 115,
1992), read directly; formulas quoted from p. 428.

---

## §0. The (β) construction, fixed precisely

Chosen per the programme's anti-smuggler orientation (genealogy_vision.md:
"watch structure appear without being snuck in"): MO₂ is the **primitive atom**;
Navara's state-engineering scaffold (T×S, stateless S) is **discarded**.

- **Block.** `U := MO₂`, atoms `a, a^⊥, b, b^⊥`, with `a∧b = 0`, `a ⊀ b^⊥`
  (i.e. `a ⊥̸ b`), and the two complementary pairs `{a,a^⊥}`, `{b,b^⊥}`.
  Bounds `0, 1`. (Contrast Navara: he had `U = T×S`. We drop the `T×` wrapper.)
- **Copies + horizontal sum.** For each `C ⊆ M` (`M` countable) a copy `U_C`;
  `V :=` horizontal sum of `{U_C : C ⊆ M}` (copies glued only at `0,1`).
- **Product + constancy.** `W := ∏_{m∈M} V`; `L ⊆ W` = all `f` with Navara's
  constancy condition (p. 428, verbatim, with `U_C` now an MO₂-copy):

  > whenever `f(m) ∈ U_C \ {0,1}` for some `m∈M`, `C⊆M`, then `m∈C` and `f`
  > is constant on `C`.

- **Notation.** `v|C` = the element of `L` attaining `v ∈ U_C` on `C`, `0` on
  `M\C`. Witness data: `aₙ := a|Cₙ`, `p := ⋁ₙ b|Cₙ`, for disjoint `Cₙ`.

---

## §1. Closure step re-derived for MO₂ blocks  [the load-bearing check]

**Goal.** Navara's Theorem-proof shows `L` is closed under countable orthogonal
joins (σ-orthocompleteness). The proof's one block-dependent step (p. 428):

> "Suppose `f(m) ∈ U_C\{0,1}` … All `fₙ(m) ≤_V f(m)`, so belong to `U_C`. All
> `fₙ` with `fₙ(m)≠0` must be constant on `C`. There is some `f_i` with
> `f_i(m)≠0`. For all `f_j` with `f_j(m)=0`, the relation `f_i ⊥ f_j` implies
> `f_j` attains values from `U_C` on `C`. Hence `f_j` is constant (=0) on `C`."

**The step that must carry for MO₂.** "`f_i ⊥ f_j` and `f_i(m)≠0` ⟹ `f_j` is
constant `=0` on `C`." Navara's reason: `f_j ≤ f_i^⊥` (orthogonality), and the
elements `≤ f_i^⊥` inside the block are limited enough to force `f_j = 0` on `C`.

**MY DERIVATION (confidence: MEDIUM-HIGH on the lattice fact, MEDIUM on whether
it suffices for the proof).**

Take `f_i(m) = x ∈ {a, a^⊥, b, b^⊥}` (a nonzero, non-1 block value; if `f_i(m)
∈ {0,1}` the constancy clause is not triggered). In MO₂, for an atom `x`, the
down-set of `x^⊥` is:
```
  ↓(x^⊥) = {0, x^⊥}            (x^⊥ is itself an atom; only 0 below it)
```
because MO₂ atoms are height-1: nothing strictly between `0` and an atom.
So `f_j(m) ≤ x^⊥` forces `f_j(m) ∈ {0, x^⊥}`.

- If `f_j(m) = 0`: that is the desired "=0 on C" at coordinate `m`. ✓
- If `f_j(m) = x^⊥` (the nonzero option): then `f_j` is nonzero-non-1 on the
  block, so by constancy `f_j` is constant `= x^⊥` on `C`. But Navara's
  conclusion is `f_j` constant **=0**. So the nonzero branch must be excluded
  by the *orthogonal-family* hypothesis, not by the block alone.

**Where it actually closes (and where I'm least sure).** The family `{fₙ}` is
**pairwise orthogonal**. If two members `f_i, f_j` were both `≠0` on the same
block `C` (values `x` and `x^⊥`), they'd be a *within-block* orthogonal pair —
allowed (`x ⊥ x^⊥`), size 2. A *third* member `f_k ≠ 0` on `C` would need
`f_k(m) ≤ x^⊥ ∧ (x^⊥)^⊥ = x^⊥ ∧ x = 0` → forced `0`. So:

> **CLAIM 1 (closure survives, MEDIUM confidence).** On any block `C`, at most
> **two** family members are nonzero (a complementary pair `x, x^⊥`); all others
> are `0` on `C`. Countable orthogonal joins are thus computed coordinatewise
> with at most-2 support per block, stay constant on each `C`, and land in `L`.
> **σ-orthocompleteness survives the MO₂ swap.**

**This MATCHES the notes' assertion** ("only elements `≤ a^⊥` are `{0,a^⊥}`")
but now with the gap named: the notes' phrasing hid that the nonzero branch
`f_j = x^⊥` is killed by the *orthogonal-family cap*, not by the block's
down-set alone. The block down-set gives `{0, x^⊥}`; the family caps support at
2; together → joins close. **I believe this carries, but the "cap at 2 per
block" step is the one to check against Navara's intent — he proves `=0`
outright, I get `=0` only after invoking pairwise-orthogonality of the whole
family. Verify this is what his proof actually uses.**

⚠ **VERIFY 1:** Is "at most 2 nonzero family members per block, rest 0"
sufficient for his coordinatewise-join-lands-in-L conclusion? I think yes
(constancy holds for each, join is constant on `C`), but confirm the join of a
2-element within-block orthogonal pair plus disjoint-support tails is itself
constancy-legal.

---

## §2. Finite truncation `L₂^(N)` — statefulness lives here  [your limit intuition]

Restrict `M` to `N` blocks `C₁,…,C_N` (or take the sub-OML generated by the
first `N` block-coordinates). Call it `L₂^(N)`.

**MY CLAIM (confidence: HIGH).** `L₂^(N)` is:
- **finite** (finite product of finite MO₂-copies under constancy),
- **non-Boolean** (each block carries the live `a∧b=0`, `a⊥̸b` gap),
- **concrete + stateful** — MO₂ is concrete (order-determining 2-valued states,
  `concrete_meetzero_vs_orthogonal.py`); finite products and sub-OMPs of
  concrete logics are concrete (states restrict). So `L₂^(N)` has a genuine,
  separating state space — **proper probability tables exist at every finite
  stage.**

This is exactly the "statefulness" you expect: it is *present and healthy* at
every finite truncation. The directed family `{L₂^(N)}_N` with the inclusion
maps `L₂^(N) ↪ L₂^(N+1)` has `L₂ = ⋃_N L₂^(N)` closed under the σ-join (the
colimit, completed). **The question is what survives the colimit + closure.**

⚠ **VERIFY 2:** that `L₂` is (the σ-orthocompletion of) the directed colimit of
the `L₂^(N)` — i.e. that finite truncations are cofinal and the closure only
adds the infinite orthogonal joins. Plausible from the constancy structure;
not rigorously checked.

---

## §3. The hinge + the degeneration map  [verdict]

Now the (★) test on `p = ⋁ₙ b|Cₙ` vs `aₙ = a|Cₙ`, computed in `L₂` (not `W`).

**Fact (1): `p ∧ aₙ = 0`. (confidence: HIGH.)** Coordinatewise: on `Cₙ`,
`b ∧ a = 0` (MO₂); off `Cₙ`, disjoint support → `0`. Meets are coordinatewise
and not deformed by closure (closure adds joins). ✓ Robust.

**Fact (2): is `p ⊥ aₙ`?  i.e. `p ≤ aₙ^⊥` in `L₂`?  ← THE HINGE.**

Orthocomplement of `aₙ = a|Cₙ` in `L`. **MY DERIVATION (confidence: MEDIUM —
this is the crux, treat skeptically).**

`aₙ` is `a` on `Cₙ`, `0` elsewhere. Its orthocomplement in `L` must be the
`L`-element that is the block-orthocomplement on `Cₙ` and `1` off `Cₙ`:
```
  aₙ^⊥ = (a|Cₙ)^⊥ = a^⊥|Cₙ  ∨  1|(M\Cₙ)
```
— i.e. `a^⊥` on `Cₙ`, `1` everywhere else. **Confidence this formula is right:
MEDIUM-HIGH** — it's the standard orthocomplement of a "supported on `Cₙ`"
element, and (key point from reading the source) the orthocomplement is taken
**inside the horizontal-sum copy `U_{Cₙ}`**, where for the *atom* `a` we have
`a^⊥` = the MO₂ orthocomplement, an atom. Constancy is preserved: `a^⊥|Cₙ` is
constant `=a^⊥` on `Cₙ`. So `aₙ^⊥ ∈ L`. ✓

Now test `p ≤ aₙ^⊥` coordinatewise:
- **Off `Cₙ`:** `aₙ^⊥ = 1`, and `p ≤ 1`. ✓ no constraint.
- **On `Cₙ`:** `aₙ^⊥ = a^⊥`, and `p = b` there. So the hinge reduces to:
  ```
  ┌────────────────────────────────────────────────┐
  │  (†)   In MO₂ (the block), is  b ≤ a^⊥ ?        │
  └────────────────────────────────────────────────┘
  ```

**And in MO₂, `b ≤ a^⊥` is FALSE** — that is the defining meet-zero≠orthogonal
property of the block (`a ⊥̸ b` means precisely `b ⊀ a^⊥`). So:

> **CLAIM 3 (hinge resolves YES — ★ HOLDS — conjecture FALSE).
> CONFIDENCE: LOW-to-MEDIUM. This contradicts the notes' "leans NO." See the
> adversarial check below before believing it.**
>
> `p ⊀ aₙ^⊥` for every `n`, so (★) holds in `L₂`: `p` is a genuine element,
> `{aₙ}` an infinite orthogonal family, `p∧aₙ=0` yet `p⊀aₙ^⊥`. `L₂` would be a
> concrete, σ-orthocomplete, non-Boolean OML exercising descent — the sought
> point-free relational-probability object.

### ⚠⚠ ADVERSARIAL CHECK ON CLAIM 3 — why I do NOT trust it

The derivation above is "too easy," and the notes' verdict leans the *other*
way. Three places it can be wrong, in priority order:

1. **The orthocomplement formula may be deformed by closure (HIGH suspicion).**
   I assumed `aₙ^⊥ = a^⊥|Cₙ ∨ 1|(M\Cₙ)`. But Navara *warns* "the lattice
   operations in `L` do not coincide with those of `W`." If the **join**
   `a^⊥|Cₙ ∨ 1|(M\Cₙ)` is enlarged in `L`'s completion, or if `p`'s own closed
   form is larger than `b`-on-`⋃Cₙ`, the on-block comparison changes. I did NOT
   re-derive `p` as a *closed* join (§ flagged this earlier and I then skipped
   it — that is a gap).

2. **`p ≤ aₙ^⊥` is an ORDER relation in `L`, and `≤` in a completion can hold
   for elements that look incomparable coordinatewise (MEDIUM suspicion).** The
   completion can add order relations. "Coordinatewise `b ⊀ a^⊥` on `Cₙ`" may
   not survive as "`p ⊀ aₙ^⊥` in `L`" if `L`'s order is the completion order.
   This is exactly the segregation mechanism: the Boolean-ization across blocks
   could force `p` below `aₙ^⊥` *globally* even though it fails *locally*.

3. **The segregation argument (notes, 2026-06-08) is not addressed above.**
   The notes argue: infinite orthogonal families in `L` are disjoint-support
   ⟹ Boolean ⟹ non-distributivity trapped in finite blocks. My Claim 3 asserts
   `p` (one element) escapes that trap by being tested *against* the family
   rather than *in* it. **Which is right is the whole open question.** My
   derivation tacitly assumes the coordinatewise order IS the `L` order; the
   segregation view says the closure changes it. I cannot currently settle
   which, and I lean toward distrusting Claim 3 precisely because I skipped the
   closed-join derivation of `p` (item 1).

### The degeneration picture (holds under EITHER verdict)

Regardless of the hinge: finite truncations `L₂^(N)` are quantum + stateful
(§2). The map `L₂^(N) → L₂` (N→∞, completed) is where state-tables and the
quantum gap either stay married (Claim 3 / yes) or divorce (segregation / no).
This degeneration — *how the proper probability tables of the finite stages
relate to the limit* — is the object your "statefulness reappears in a limit"
intuition names, and it is worth characterizing **either way**:
- **yes:** the gap survives to the limit; `p` is the witness; tables persist.
- **no:** the limit Boolean-izes; tables survive on the skeleton + finite
  stages; the gap dies in the passage — an explicit picture of σ-additivity
  destroying non-distributivity (the descent obstruction, made visible).

---

## §4. What to verify, in priority order

1. **[crux] Re-derive `p` as a CLOSED join in `L`** (not the naive `b`-on-`⋃Cₙ`).
   Does the σ-orthocompletion enlarge it? This is the gap that makes me distrust
   Claim 3. — Item 1 of the adversarial check.
2. **[crux] Is `≤` in `L` the coordinatewise order or the completion order?**
   If completion order, does it force `p ≤ aₙ^⊥` globally (segregation)? —
   Item 2.
3. **[closure] Confirm Claim 1** ("≤2 nonzero family members per block")
   matches Navara's intended closure argument. — VERIFY 1.
4. **[colimit] Confirm `L₂` = σ-orthocompletion of the directed colimit of
   `L₂^(N)`.** — VERIFY 2.
5. **Then, and only then:** the hinge verdict + the degeneration map.

**Honest bottom line:** I derived a *candidate YES* (Claim 3), but my own
adversarial check finds the derivation incomplete at exactly the point
(closed-join of `p`, completion-order) where the notes' "leans NO" would bite.
So this worksheet does **not** overturn the leaning verdict — it **localizes
the open question to two concrete sub-derivations** (items 1–2), which is the
real deliverable. The hinge is now: *does `L`'s completion enlarge `p` or add
the order relation `p ≤ aₙ^⊥`?*
