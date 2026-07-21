# W1 session prompt — index category determination

*Drafted 2026-07-20 (end of E5) for the next session. Paste §"The prompt"
below into a fresh session, or open this file and say "run W1". Everything
above and below the prompt is context for the user, not for the session.*

**Model recommendation:** Opus, high reasoning, fresh context. This is a
mathematical determination, not a bookkeeping run.

**Why this is a good first mathematical step.** W1 is the sharpest of the
three workstreams because its deliverable is a *fact about objects that
already exist in the corpus* — the C11 and C12 architectures are written down
with hand proofs — rather than a new construction. It is also gating: W2's
typing run and the choice between campaigns C-a and C-b both depend on the
answer, and §2 of the Stage-0 doc records that conflating the two candidate
worlds is an error already made once and corrected.

---

## The prompt

> Read `notes/open_questions/oml_attack/SIGMA_LAYER_TARGET.md` first — it is
> the Stage-0 gate document and §6 lists standing gates that bind this
> session. Then execute **W1 (index category determination)**, §3 of that
> document. Do W1 only: do not start W2, do not open campaign C-a, and do not
> run the grammar engine (it is hard-gated by AMENDMENT A2 in
> `CAMPAIGN_CHAIN.md` and this session names no clause for it).
>
> **The task.** Determine the cofinal structure of the section-system index
> poset for the two escape architectures. Is it `[ω₁]^{≤ω}`-like,
> ω₁-tower-like, or ω^ω-like? The point of the question is that it decides
> *which set theory the residue belongs to* — ZFC-robust tower phenomena
> versus axiom-sensitive ω^ω phenomena are different worlds, and §3 of the
> Stage-0 doc records that an earlier chat-level conflation of them is on
> record and corrected. Do not repeat it.
>
> **The two architectures, both already written down with hand proofs — read
> these before theorizing:**
> - **Escape (a), the uncountably-generated separating boundary.** The live
>   object is C12's ω₁ cylinder hub: `oml_omega1_cylinder_hub.md` §2–§4, with
>   `I = ω₁`, `H = 2^I`, `A` the countable-support product σ-algebra,
>   `B_i = P(H \ {i})`. §4 is the exact Boolean CSS-without-GS atlas —
>   compatible σ-section over every **countable** `J ⊆ H`, no global section.
>   That is the section system whose index poset you are asked to identify.
>   Note §5: the construction is *central*, hence not itself an admissible OML
>   counterexample — you are determining the index structure of the
>   architecture, not promoting the object.
> - **Escape (b), the distributed nonseparating quotients.** C11's
>   puncture-meet theorem, `oml_distributed_relation_cell_assembly.md` §3,
>   scoped to kill only the countably-generated *separating* shared boundary;
>   §4's incidence-hypergraph paste is the distributed architecture.
>
> **The input you should not reconstruct blind.**
> `oml_odbc_sigma_nerve_absorption.md` §1 (cherry-picked into canon
> 2026-07-20, commit `cdda1ce`) is the surviving keeper of the parked σ-nerve
> seed and is *directly about this question*: it fences closure-based
> globalization to **countably cofinal** index systems, and states that over
> `[ω₁]^{≤ω}`-shaped posets — where `𝒥_{≤ω}(I)` lives for uncountable atlases
> — surjective bonding does **not** kill the derived limit, so the correct
> obstruction object is limⁿ, not lim¹. It is audit-certified. Its §2 also
> records that CODBC failure manifests at uncountable cofinality with every
> countable stage alive — and flags that this is a restatement of CSS∧¬GS,
> *near-tautological*, not a discovery. Do not re-derive either as new.
>
> **Deliverable.** A precise statement of the index structure with a proof,
> for each architecture separately (they may differ — if they do, that is
> itself the finding). Bank it as a dated note in
> `notes/open_questions/oml_attack/` with an explicit **verdict grade** and
> evidence class in the corpus's existing vocabulary (hand proved / executable
> / Lean certified / open), and a ledger row on `CAMPAIGN_CHAIN.md` using the
> additive-plus-supersede convention. **Hostile-pass the result before banking
> it** — §6 requires this for any W1/W2 verdict.
>
> **Discipline for this session.**
> - The lim¹/derived-limit identification is a **TARGET, never a premise**
>   (Stage-0 §2). If your answer makes the derived-limit machinery apply, that
>   is a result to be proved, not an assumption to reason from.
> - Distinguish sharply what you *prove* about the index poset from what you
>   *conjecture* about which set theory the residue then belongs to. The
>   second does not follow automatically from the first; say so where it
>   doesn't.
> - "The two architectures have different index structure" and "the structure
>   is none of the three named shapes" are both legitimate findings. Bank
>   either honestly rather than forcing one of the three labels.
> - Flag every hand-constructed step ⟦HAND⟧, and ⟦HAND — unverified⟧ where you
>   have not checked it. Never push; the user pushes.
>
> If W1's answer makes campaign C-b cheaper than C-a, say so explicitly with
> one line of justification — the Stage-0 doc §4 permits that reordering and
> asks for it to be recorded.

---

## Pointers the session will want

| What | Where |
|---|---|
| Gate document (read first; §6 = standing gates) | `SIGMA_LAYER_TARGET.md` |
| Escape (a) architecture — ω₁ cylinder hub, CSS/no-GS atlas | `oml_omega1_cylinder_hub.md` §2–§5 |
| Escape (b) architecture — puncture meet + hypergraph paste | `oml_distributed_relation_cell_assembly.md` §3–§4 |
| **Index-category fence (direct W1 input, audit-certified)** | `oml_odbc_sigma_nerve_absorption.md` §1–§2 |
| Parked σ-nerve parent (context for the fence) | `notes/covered_leads/sigma_nerve_torsor_parked/` |
| Authoritative ledger + A2 gate | `CAMPAIGN_CHAIN.md` |
| Compact state index | `CURRENT_STATE.md` |
| Jargon-free exposition (read-mostly) | `notes/exposition/problem_state.tex` |
