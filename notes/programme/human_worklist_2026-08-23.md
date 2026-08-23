# Human worklist — 2026-08-23

Four items needing your judgment rather than compute. Written so you can act
without re-reading the session. The compute items (Prop 14, the diagonal layer)
are running unattended and block none of these.

Current Lean state: library `sorry`-free, CI green (build + ratchet + 50
blueprint declarations + staging compile), everything pushed.

---

## H1 — Confirm the Andersen–Jessen hypothesis match  *(~1 hour, blocking)*

**Why first.** It is the only load-bearing claim in the session that is not
kernel-checked, and H2–H4 all lean on it.

### The claim

`stone_observational_extension` originally read:

    UpperDirected + EvalSurjective + NormalizedCompatibleContents +
    CollectivelyExhaustive  ==>  exists unique probability measure mu on Omega
                                 with mu (Cyl i A) = nu i A

I claim this was **false**, and that correcting `UpperDirected` to
`SequentiallyUpperDirected` is what makes it provable. It is now proved that
way, axiom-free.

The falsity claim has two steps:

1. `ce_iff_levelwise_continuity` (PROVED, in the kernel) — collective exhaustion
   is *exactly* per-level sigma-additivity. The "exists j >= i" in the
   definition is cosmetic, because `CompatibleContents` gives
   `nu i A = nu j (pi inverse A)`, so the quantity tested at `j` equals the one
   at `i`. **Take this as settled.**

2. Andersen–Jessen supplies a system meeting every hypothesis with no extension.
   **This step is verified only by hand, by me, against one source.**

### What to check

The classical statement — consistent sigma-additive marginals alone do not imply
a limit measure — is confirmed by Dudley, *Real Analysis and Probability* (2002),
p. 256 and section 12.1 problem 2, p. 448. See
`formalization/QuerySystem/notes/andersen_jessen_brief.md`. No concern there.

The gap: our theorem carries a hypothesis the classical statement never
mentions, **`EvalSurjective`** — every `eval i : Omega -> Outcome i` is
surjective. It is the only hypothesis that could have rescued the original
theorem, so it is the one worth a second pair of eyes.

My reasoning, to check or refute:

| hypothesis | in Andersen–Jessen |
|---|---|
| index set | N under <= |
| `UpperDirected` | yes — chain, max |
| NOT `SequentiallyUpperDirected` | yes — (0,1,2,...) has no upper bound. This is the gap |
| variance: `pi : Outcome n -> Outcome m` for `m <= n` | X_0 x ... x X_n, projections — correct |
| `Omega` = coherent families | the product of the X_k |
| **`EvalSurjective`** | **projections onto initial segments; surjective because each X_k is nonempty (thick implies outer measure 1)** |
| compatible, normalized | Kolmogorov consistency; P_n(X) = 1 |
| `CollectivelyExhaustive` | each P_n is a genuine measure, so CE holds by `ce_iff_levelwise_continuity` |
| conclusion | fails — diagonal cylinders D_n have P(D_n) = 1 and empty intersection |

**Concretely: is `eval n` from the product onto X_0 x ... x X_n surjective?**
Given (a_0,...,a_n) with a_k in X_k, extend by choosing any point of X_k for
k > n. That needs each X_k nonempty, which holds since a thick subset of [0,1]
has outer measure 1. I believe this is right; it is also exactly the kind of
step I have gotten wrong repeatedly this session.

### Consequences

- **Confirmed** — H2/H3 proceed as written; the paper cites Dudley and does not
  need the formalization.
- **`EvalSurjective` fails in A–J** — the original theorem may not be refuted
  after all and the framing of H2/H3 changes. Tell me and stop.

---

## H2 — Decide what the paper says about collective exhaustion  *(authorial)*

`ce_iff_levelwise_continuity` is proved: **CE = per-level sigma-additivity.**

The prose around the definition calls CE "the valuation-layer condition
characterising sigma-additive extensibility", and `sp1_iff`'s docstring says
"the correct question is what valuation-layer condition characterises
extensibility, and the answer is collective exhaustion."

That is **true for per-level extensibility** — which is what `sp1_iff` proves —
and **false for global extensibility**, the reading the surrounding text
invites. Per-level sigma-additivity is famously insufficient for a projective
limit.

Options, which I should not pick for you:

- **(a)** Keep CE, restate the theorem with sequential upper-directedness, say
  plainly that CE is per-level. Smallest change; matches what is proved.
- **(b)** Reframe CE's role: not the characterisation, but one of two necessary
  conditions. Bigger rewrite, truer to the structure.
- **(c)** Present the three-position picture below and let CE sit inside it.

---

## H3 — Write the prose  *(the actual deliverable)*

### H3a — the CE section, per your H2 decision.

### H3b — "you must pay at both layers"

This is the clarify-the-choice contribution. It is a **two-leg** result. I have
previously called it three independent facts, which oversold it:

- **Valuation layer alone insufficient.** Andersen–Jessen: every nu_i
  sigma-additive, upper-directed, surjective evaluations, no limit measure.
  *Backing: citation (Dudley) plus the H1 hand-check. NOT kernel-checked.*
- **Index layer alone insufficient.** `counterexampleQS`: sequentially
  upper-directed, yet the content is not sigma-subadditive and does not extend.
  *Backing: `counterexampleQS_no_finitary_condition` and `ce_independence` —
  the SAME witness viewed two ways, not two independent results.*

So both a valuation-layer and an index-layer condition are required, with a
counterexample on each side.

### The three positions

| position | theorem | status |
|---|---|---|
| completed countable queries legitimate | `observational_extension`, `stone_observational_extension` | proved, axiom-free |
| only finite observers; contents not measures | `stone_measure_exists` | proved — no CE, no directedness beyond upper |
| neither | — | false |

The middle row is the one nobody was looking at, and may be the more interesting
theorem given your instincts: on that reading free ultrafilters carrying
positive mass are not a pathology but the trace of observers who never complete
their observations.

Worth making explicit: sequential upper-directedness is **not a new article of
faith**. Making each query a sigma-algebra already assumes completed countable
operations — a countable union is exactly as unphysical as a countable join.
Admitting them inside a query but not between queries is hard to motivate. The
honest cost is that it excludes finite-dimensional marginal families, which is
precisely where the counterexample lives.

---

## H4 — Optional: the gap in Border's Proposition 13

Border asserts thickness of both M_k and its complement for every k, proves the
second, and disposes of the first with "a similar argument interchanging the
roles of B_k and C_k".

At k = 0 that works: A = B_0 union C_0 and the complement of M_0 is exactly
V + C_0. For k > 0 both B_k and C_k omit everything with |n| < k, so V + B_k and
V + C_k do not cover R, the complement of M_k is strictly larger than V + C_k,
and the parity contradiction does not reach it.

This does not threaten the classical result, and our formalization sidesteps it:
`AndersenJessen.lean` builds the tower from **finiteness** rather than parity
(`V_add_finite_measurable_null`), giving thickness at every k. Your call whether
it is worth mentioning to anyone — it is one line of one expository document and
I may be misreading a compressed step.

---

## Pointers

- `formalization/QuerySystem/notes/andersen_jessen_brief.md` — citation check
- `formalization/QuerySystem/QuerySystem/AndersenJessen.lean` — the thick tower
- `formalization/QuerySystem/QuerySystem/ExtensionObstruction.lean` — EscapingTower
- `formalization/QuerySystem/blueprint/web/index.html` — rendered blueprint
- `formalization/tools/prover/README.md` — what the prover loop does and does not do
