# Adversarial review of the campaign strategy (2026-07-18)

*Provenance: LLM-drafted (Claude, Fable 5) at the user's request, against the
controllers as of commit `c110c4d` plus the in-flight iteration-316
minimal-envelope audit. This reviews allocation and direction, not the
correctness of banked receipts; no banked evidence class is disputed. Adopted
updates are listed at the end and mirrored into the controllers.*

## What the strategy has right (kept, not at issue)

Evidence-class separation; forced-object-only adjunctions (every rebase
adjoins a canonically forced or canonically minimal object, never a chosen
one); the do-not ledger; hostile review with cross-seed replay; Lean pinning
of the abstract implication layer; bounded receipts with explicit scope
strings. The review below targets *where the effort goes*, not its rigor.

## F1 — The one-seed rebase chain is becoming a repair-depth chain

Do-not item 8 bans "another finite repair-depth chain." The fibre-level ban
was earned at Campaigns 18–19: selected repairs terminated nothing and the
gap was not a Markov state. The rebase-level chain `N -> O -> PENV` now has
the same signature one level up: strict-target rank is **Refuted**
(`fc9c0b22...`), each iteration fires one production for one session plus
~20–40 minutes of reconstruction-dominated compute, and nothing yet converts
firings into a coverage or termination theorem. On a finite carrier the
selected chain terminates set-theoretically, but the number of *novel rule
types* is the real unknown, and one-seed-per-session is the most expensive
possible way to discover them.

**U1 (adopted).** Mechanize the selected canonical chain. Build a batched
rule engine (`arr_grammar_engine`) that applies the currently certified
productions — MEM discharge, forced `N`/`O` covers, minimal-envelope `PENV`,
fixed-cut forced-top descent — in the deterministic scan order, with
checkpointed receipts, and **halts** on exactly three events: (i) an
obligation matched by no rule (the next theorem target), (ii) a gate hazard
(a gate-forcing witness), (iii) quiescence (a terminal candidate). All
components exist in the iteration-315/316 producers (family extrema,
cover-report classification, gate battery). Human iterations then happen at
rule-discovery granularity, not cut granularity. Session-interactive rule
firing stops once the engine exists.

## F2 — The finite layer cannot touch `Phi`; nothing currently pulls it

Every finite concrete OML is `Phi`-tame: all orthogonal families are finite,
so `St_fa = St_sigma` trivially. The completed two-copy object, if the
grammar terminates, is still finite. Its entire value is transport
architecture for the sigma-assembly — conservative old-copy embedding
(kernel retraction), boundary preservation, activation escape, and the repair
calculus itself. But no written statement of the sigma-layer target currently
exists to *pull* the finite work, so there is no test for whether a given
finite theorem is load-bearing or gold-plating. This is how preparatory
layers regress indefinitely.

**U2 (adopted).** Write the pull-document: the exact omega-one/Ulam
adjacent-assembly target — the object, its event family, the intended
CSS/no-GS mechanism (incompatible-activation transport per Campaigns 12–14),
the Campaign-13 normality trichotomy it must thread, the Derr–Williamson
wall it must sit outside (non-Polish-representable or coarse-riding), and
the explicit list of finite-layer theorems it consumes. Every subsequent
iteration names the target clause it serves. An iteration that serves no
clause is parked by default.

## F3 — No stopping rule is in force

Campaign 7's mandatory 60-iteration continuation was satisfied long ago; at
315+ iterations, continuation is momentum unless re-chosen. The natural
checkpoint is exactly the iteration-316 dichotomy verdict.

**U3 (adopted).** Budget: after the engine's first sustained run (or at most
five further rule-discovery iterations, whichever comes first), either a
coverage/termination theorem for the production set is concretely in reach,
or the campaign pivots to costing the *direct* least-closure computation.
The 7.17-GB figure was a blind in-RAM estimate for a naive global lift, not
a wall; a sharded, disk-backed, or Fir-hosted computation of the canonical
closure is one decisive artifact versus an unbounded iteration stream. The
Fir gate file should carry a dry shard spec for it so the decision is ready
when the outage clears.

## F4 — One code lineage under all ARR receipts

The ARR chain is a single exec-patched producer lineage roughly ten deep.
Cross-seed replay catches nondeterminism, not implementation error; the
semantic manifest verifier shares the captured grammar; receipts honestly
record "not an independent implementation," but the concentration risk has
grown with the chain's length.

**U4 (adopted).** One representation-independent spot-verifier: a fresh
constraint-model point-membership sampler for the two-copy carrier (built
from the written spec, not from `recover()`), checking a handful of
load-bearing constants — carrier count, `|U| = 51,941,861,211`, the
`16,210,089,024`-point overlap, the `21,137,851,696`-point residual, one
forced-meet equality. Bounded hours, genuinely independent, closes the most
plausible systemic-bug scenario.

## F5 — The corridor is nearly closed and the grammar should aim at it

Campaign 13 proved the omega-one completion corridor is a needle: full
state-normality kills sigma-states, partial normality charges ambient join
defects, lost hub normality destroys point classification; face-local MBRC
is the surviving opening, reached via activation transport. The PENV-level
work is three levels below that mechanism. This is not an argument to stop —
it is the argument for U2: the finite grammar must be shaped toward the
surviving corridor (which finite theorems does face-local MBRC transport
actually need?), not toward generic latticehood of one union.

## F6 — Bookkeeping

`CAMPAIGN_LOG.md` iteration blocks are non-monotone (287–289 filed after
314); append-only integrity says do not reorder, but future tooling should
not assume monotone numbering. The Fir gate remains OUTAGE; F3's shard spec
belongs in `FIR_COMPUTE_GATE.md` when drafted.

## Adopted updates

| # | Update | Landed in |
|---|---|---|
| U1 | Batched rule engine replaces one-seed sessions; halts on novel obligation, gate hazard, or quiescence | `NEXT_CAMPAIGN_HANDOFF.md` item 7 (first action) and item 8 |
| U2 | Sigma-layer pull-document with named target clauses; clauseless iterations park by default | `NEXT_CAMPAIGN_HANDOFF.md` item 7; `notes/programme/frontier_map.md`; `notes/programme/program_overview.md` |
| U3 | Explicit budget and closure-costing pivot; dry Fir shard spec when drafted | `NEXT_CAMPAIGN_HANDOFF.md` item 7; `FIR_COMPUTE_GATE.md` (spec deferred) |
| U4 | Independent point-sampler spot-verifier for load-bearing ARR constants | `NEXT_CAMPAIGN_HANDOFF.md` item 7 |
| U5 | Non-monotone log numbering flagged; no reordering | this note only |

The review changes no evidence class, retracts no banked result, and does
not touch the sharpen guardrail: the question stays open, the architecture
stays live, and the update is to *how* the next hundred hours are spent.

## Pre-engine repo review (2026-07-18, same day)

Mechanical sweep before the engine work starts. **Clean:** working tree
clean at `3a6cef5`; every repo path referenced in the 62
oml_attack/programme documents resolves; both taxonomy JSONs' file
pointers resolve; no uncommitted Lean changes; all verification receipts
tracked.

**Machine reality for U3 costing:** this workstation has 16 GB RAM, 10
cores, and only ~10 GB free disk. The naive 7.17-GB in-RAM lift plausibly
fits in RAM; free *disk* is the binding constraint for checkpointed
shards, and closure growth beyond the entry cost is uncosted. So: not
shown prohibitive, not shown feasible — U3's costing is a real
deliverable, and disk should be cleared (or Fir restored) before any
closure run.

**Open decision items (user-owed; no action taken):**
1. `explore/c-sigma-nerve` worktree + branch (7 commits: parked σ-nerve
   seed, absorption note, `prediction_entry_DRAFT.md` awaiting manual
   banking) — merge/inspect, then `git worktree remove`.
2. `fir-backend-poc` worktree + branch — fully contained in this branch
   (0 commits ahead); removable if nothing external uses that checkout.
3. Stale exploration branches `explore/a-strategy-d`,
   `explore/b-pointfree-descent` (both topics killed/parked 2026-06) —
   archive or delete.
4. `main` is 461 commits behind this branch and 4 unpushed ahead of
   origin/main — merge/push policy is a checkpoint decision; nothing
   pushed this session.
5. `notes/unsorted/` Tier-3 backlog (8 pre-programme items) — unchanged,
   known.
6. Standing ratification queue: s11–s33 hand+census blocks (s33 only
   with its liveness caveat), C17/s34 receipts, FIDELITY_REVIEW, abstract
   length, statistics verdict, ILL hunt.
