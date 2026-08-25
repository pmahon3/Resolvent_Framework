# Delay embedding: blueprint chapter + the predictive-sufficiency gaps

**Written 2026-08-25.** Survey + plan. No new math.

## Why this is worth doing

`DelayEmbedding.lean` (620 lines, 26 declarations) formalizes the delay query
system: the query at `(d,τ)` reads `d` samples at lag `τ`, with refinement
`(d,τ) ≤ (d',τ')` iff `τ' ∣ τ` and `d' > (d-1)(τ/τ')`.

Its punchline is one theorem:

```
theorem not_seqUpperDirected : ¬ (delayQuerySystem X).SequentiallyUpperDirected
```

The full delay system is upper-directed but **NOT** sequentially upper-directed.
That is exactly the hypothesis `stone_observational_extension` needs and whose
`UpperDirected` form is FALSE — refuted by Andersen–Jessen, now kernel-checked
(`thm:aj-no-extension`, 2026-08-24). So delay embedding is a **natural, concrete
system landing on the wrong side of the very hypothesis the AJ counterexample
forced.** The extension theorem applies only after passing to
`delayFixedLagBoundedSystem` (fixed lag, bounded depth), where
`seqUpperDirected` does hold.

That is the chapter's reason to exist, and it is already proved.

## Verified status (2026-08-25)

- 26 declarations, **axiom-clean** (`[propext, Classical.choice, Quot.sound]`)
  on `delayQuerySystem`, `upperDirected`, `not_seqUpperDirected`,
  `observational_extension_fixedLag`, `delay_cyclic_implies_reconstruction`.
- **No real sorries.** The one `sorry` string is inside a docstring.
- Imports `QuerySystem.QuerySystem` (in the blueprint, ch0) and
  `QuerySystem.ReconstructionTheorem` (uncovered).
- Blueprint decls it genuinely uses: `QuerySystem`, `Query`, `Omega`,
  `UpperDirected`, `SequentiallyUpperDirected`, `observational_extension`.
  These are **real Lean dependencies**, so they become **real DAG edges** — not
  the prose-only kind the AJ chapter had before this week.

## PHASE 1 — the chapter (do this now, standalone)

Add a chapter on the STRUCTURAL half only. Everything in it is proved and
axiom-clean; it must not be coupled to the disintegration project below.

Nodes:

| node | Lean |
|---|---|
| `def:delay-query` | `delayQuery`, `delayEval` |
| `def:delay-refine` | `delayLe`, `delayRefineMap` |
| `thm:delay-qs` | `delayQuerySystem` |
| `thm:delay-upper` | `delayQuerySystem.upperDirected` |
| `thm:delay-not-sud` | `delayQuerySystem.not_seqUpperDirected` ← **the point** |
| `thm:delay-surj` | `delayQuerySystem.evalSurjective` |
| `thm:delay-compat` | `delayQuerySystem.compatibleMarginals` |
| `def:delay-fixed-lag` | `delayFixedLagBoundedSystem` |
| `thm:delay-fixed-sud` | `delayFixedLagBoundedSystem.seqUpperDirected` |
| `thm:delay-extension` | `observational_extension_fixedLag` |

Expected new cross-chapter edges into ch0/ch1: `def:query-system`,
`def:upper-directed`, `def:seq-upper-directed`, `thm:observational-extension-seq`.
That would make it the **second** chapter with real incoming mathematical edges.

Build `thm:delay-not-sud` as the chapter's centre, with prose (NOT a remark node —
remarks were deliberately removed from the graph) pointing at
`thm:aj-no-extension`.

Record the six gaps below as a **prose section**, following the `sec:sequentiality`
precedent.

Coverage baseline moves 27 → 26. Regenerate deliberately in the same commit.

## PHASE 2 — the predictive-sufficiency gaps

The file's header lists six unformalized Paper-1 results:

| gap | status after today's check |
|---|---|
| `def:delay-pred-map` φ_{d,τ} : Xᵈ → P(X) | **now supported** — see below |
| `def:pred-sufficient` | supported |
| `def:markov-order` | supported |
| `thm:sufficiency` d ≥ m(τ,P) ↔ sufficiency | supported |
| `prop:stationarity` | supported |
| `cor:takens` | ⛔ **OUT OF SCOPE — see below** |

### The unlock

The 2025 note says these "require conditional probability infrastructure beyond
the current scope". **Mathlib now has it**: `MeasureTheory.Measure.condKernel`
and `Measure.disintegrate` (`ρ.fst ⊗ₘ ρCond = ρ`) in
`Probability/Kernel/Disintegration/StandardBorel.lean`. Verified present.

### ⚠ BLOCKING decision before any code

`Measure.condKernel` requires `[StandardBorelSpace Ω] [Nonempty Ω]`.
`DelayEmbedding` is stated for bare `[MeasurableSpace X]`. **So φ_{d,τ} cannot
be defined at the file's current generality.** Two options, and this is a
statement-fidelity call, not an implementation detail:

- (a) `X` gains `[StandardBorelSpace X]`, and every existing structural theorem
  either inherits it or gets split. Costs generality in the part that currently
  has none.
- (b) The predictive section is stated for a restricted subclass and says so
  in the blueprint.

**(b) is recommended** — the structural results are genuinely general and
should not be narrowed to buy the probabilistic ones. Decide before writing.

This is the same shape as two errors already made this session (`Thick` vs
`ThickFor`; the trivial `IsConcrete` reading). Resolve it in the plan.

*Side note, no action:* `StandardBorelSpace` is the same neighbourhood as
`PolishRepresentable`, a cited axiom in the σ-essential lane where
Derr–Williamson kills witnesses on Polish carriers. Different lane, no edge —
but worth being conscious of rather than surprised by.

### ⛔ Takens is out of scope

`cor:takens` needs generic-embedding / differential-topology machinery.
**Mathlib has nothing on Takens** (checked: no hits). Listing it beside the
other five makes the plan look tractable when one item is a research project.
Drop it from the deliverable; keep it as prose.

## PHASE 3 — the archived modules: DO NOT ASSUME THEY WORK

`archive/PredictiveState.lean` (639L, 14 decls) and
`archive/PredictiveOperators.lean` (332L, 16 decls) import exactly the kernel /
disintegration machinery Phase 2 needs, so they look like a head start.

**They are not.** Commit `ce55bb4` says it outright: *"archive two that never
compiled."* Confirmed today:

- 28 errors. Applying the two obvious Mathlib renames (`Measurable.prodMk`,
  `comap_le_iff_le_map`) takes it to 23 — so renames are a small minority.
- Several errors are `set Q_* := ...`. **`Q_*` is not a valid Lean identifier**
  — `*` cannot appear in a name. That code never parsed, in any Mathlib version.
- `Measure.condExp` does not exist as a field (3 errors).
- `PredictiveOperators`' single error is a missing `.olean` from
  `PredictiveState`, so its 16 declarations are **unverified, not clean**.

Treat these as a **design sketch to read, not a codebase to repair.** The
mathematical intent (predictive kernel, minimal predictive state map,
factorization) is worth mining; the proofs are not.

Destination when rewritten: `staging/`, not the library — CI compiles staging
without sorry-gating, and the ratchet is at 0 with a hard CI gate.

## Recommended order

1. **Phase 1 now.** Self-contained, all proved, gives the real ch0/ch1 edges.
2. **Decide the StandardBorel question** (a) vs (b).
3. Phase 2 `def:delay-pred-map` + `def:pred-sufficient` first — they are
   definitions, and getting the statements right is the whole risk.
4. `thm:sufficiency` last; it is the real theorem.
5. Takens: never, unless Mathlib grows the machinery.


---

## Update 2026-08-25: restrict chosen; φ built; a correction to Phase 2's order

**Decision: restrict** (option (b)). The predictive layer lives in a separate
module carrying `[StandardBorelSpace X] [Nonempty X]`; `DelayEmbedding.lean`
keeps its bare `[MeasurableSpace X]` and every structural result keeps its
generality. `staging/DelayPredictive.lean`.

**`def:delay-pred-map` DONE**, axiom-free:

- `predLaw P d τ = condDistrib (fun ω => ω 1) (delayEval d τ) P`
- `predLaw_ae_eq_condExp` — the defining property, φ computes the conditional
  expectation of an indicator of the next sample given the window.

Route note: `Measure.condKernel` on a hand-built joint law stalls on the
`IsCondKernel` instance. `condDistrib` (in `Probability/Kernel/CondDistrib.lean`,
which the first survey missed) is the purpose-built tool and works immediately.

### ⚠ Correction: `def:pred-sufficient` is NOT next

The plan above put `def:pred-sufficient` beside `def:delay-pred-map` as an easy
pair. That was based on `DelayEmbedding.lean`'s header gloss, "injectivity of
`φ_{d,τ}` on the support". **The source says something materially different**
(`archive/superseded_drafts/predictive_experiments`, Def. at l.515):

> $Q$ is predictively sufficient if for every admissible query $Q'$ there is a
> measurable $\psi : O_Q \to O_{Q'}$ with $\Pi_{Q'} = \Pi_Q \circ \psi$

— a **factorization condition quantified over all other queries**, with
characterization $F \perp Q' \mid Q$. Injectivity of φ is neither that
definition nor obviously equivalent to it.

Formalizing the gloss would yield a clean-compiling theorem about the wrong
statement — the `IsConcrete` failure mode again. **The definition has to be
settled against the source before `def:pred-sufficient`, `def:markov-order` and
`thm:sufficiency` are attempted**, and that is a reading task, not a Lean task.

Revised order: (1) settle the sufficiency definition against the source;
(2) `def:pred-sufficient`; (3) `def:markov-order`; (4) `thm:sufficiency`.


---

## Update 2026-08-25 (2): decision 3's prerequisite — THREE definitions, no current source

Before formalizing predictive sufficiency I checked whether the source draft is
current. It is not, and the situation is worse than "superseded".

**No paper in `papers/` defines predictive sufficiency.** The only two
definitions in the repo are both archived, and **they do not agree**:

1. `archive/superseded_drafts/predictive_experiments` (l.515) — a FACTORIZATION
   condition: `Q` is predictively sufficient if for every admissible `Q'` there
   is measurable `ψ : O_Q → O_{Q'}` with `Π_{Q'} = Π_Q ∘ ψ`. Characterized by
   `F ⊥ Q' | Q`.
2. `papers/archive/paper_ii_dynamics_from_probability` (`cor:sufficiency`) — a
   CONDITIONAL EXPECTATION identity: `E[g(F) | σ(Q)] = E[g(F) | σ(Q_*)]` a.e.,
   a corollary of predictive factorization through the minimal predictive state
   map `Q_*`.
3. `DelayEmbedding.lean`'s header gloss — "injectivity of `φ_{d,τ}` on the
   support".

(2) is a consequence of factorization through `Q_*`; (1) quantifies over other
queries; (3) is neither. They may be related, but they are not the same
statement, and nothing in the current corpus adjudicates.

### Consequence for the plan

Option (a) — "formalize the factorization definition" — presumes a settled
definition to be faithful TO. There isn't one. Formalizing any of the three now
would be picking a winner by accident.

**Revised recommendation: (d), park it**, until a current paper states the
definition. `def:delay-pred-map` (`predLaw`, `predLaw_ae_eq_condExp`) stands on
its own — it is the conditional law of the next sample given the window, which
is well defined regardless of how sufficiency is eventually stated, and every
version above is phrased in terms of exactly that object.

The remaining items (`def:markov-order`, `thm:sufficiency`) depend on the
sufficiency definition and are parked with it. `prop:stationarity` does not and
could be done independently if wanted.
