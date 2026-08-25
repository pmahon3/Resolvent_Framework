# The four admissibility predicates: what is actually owed

**Written 2026-08-24.** Scoping. Corrects two earlier misreadings of my own.

## First: what is NOT owed

`SigmaEssentialOpenCore.lean` declares four opaque predicates —
`IsConcrete`, `IsSigmaComplete`, `IsIrreducible`, `IsNonSegregated` — and it is
tempting to read them as four formalization gaps. They are not, for two reasons.

**(1) They are load-bearing for nothing proved.** The only consumer is
`Admissible`, used only in `TargetA_sharp`, and the one theorem about it
discards the conjunct:

```
theorem targetA_sharp_gives_targetA (h : TargetA_sharp) : TargetA := by
  obtain ⟨Ω, d, s₀, B, _, hw⟩ := h      -- `_` is the Admissible data
  exact ⟨Ω, d, s₀, B, hw⟩
```

No gate is lying and no result is weakened by their being axioms. The design is
deliberate and honest: the docstring says "the hypotheses are `→` ... the machine
shows precisely what is still owed."

**(2) ⚠ Replacing them with easy definitions would make things WORSE.** Both of
these are provable of *every* `DynkinSystem`, definitionally:

```
ConcreteCarrier d := d.Has ∅ ∧ ∀ A, d.Has A → d.Has Aᶜ      -- has_empty, has_compl
SigmaCompleteCarrier d := closure under countable disjoint unions -- has_iUnion_nat
```

(Both machine-checked as trivial, 2026-08-24.) Substituting them for the axioms
would silently turn two conjuncts of `Admissible` into `True`, weakening
`TargetA_sharp` — a NAMED CONJECTURE — while making the weakening invisible to
`#print axioms`. **Strictly worse than the axiom.** Do not do it.

They are also not the paper's notions. `rem:offcenter` is explicit:
concreteness is "exactly order-determination by two-valued states
(Gudder 1969, Harding 2004)", not "family of sets closed under complement".
(Nor is it `ConcreteSigmaOrtho`, `SigmaEssentialOpenCore.lean:323` — that is
the Feldman–Wilce σ-orthostructure thread, a different notion.)

## What IS owed: `TargetA_sharp` — the paper's `prop:adm`

The real obligation is the converse the docstring names: **the Ulam witness lands
on an admissible carrier.** Six conjuncts; two are already theorems.

| conjunct | status |
|---|---|
| ¬ IntersectionClosed | PROVED — `witness_not_intersection_closed` |
| ¬ PolishRepresentable | PROVED — `witness_not_polish` (off cited Derr–Williamson D.6) |
| non-segregated | forcing lemma, see below — likely cheapest |
| essentially irreducible | needs `cor:centre`, see below |
| concrete | paper: order-determination by two-valued states |
| σ-complete | paper says "by construction"; may be genuinely free — CONFIRM the paper's meaning before assuming |

## Non-segregated — check this first

`rem:segregated` + `lem:horizontal` give it the shape of a FORCING lemma:
segregated ⟹ Φ, so `WitnessAt → ¬Segregated`. That is structurally identical to
`witness_not_polish` and `witness_not_intersection_closed`, both three-liners off
a prior fact.

Ingredients present in Lean:
- `ConcreteOMLPatterns.isSigmaOn_of_blockwisePointed` — blockwise σ globalizes
  (the gluing direction `lem:horizontal` runs on), PROVED
- `blockwisePointed_of_isSigmaOn` — the converse on countably generated blocks
- `ODBCSections` — abstract compatible-section/gluing logic
- `thm:rigidity` (`UlamWitnessCore`) — the witness's block admits no non-Dirac
  σ-additive state, which is exactly why the witness is non-segregated

Missing: a `Segregated` definition, and `lem:horizontal` itself.

## Essentially irreducible — re-checked, and cheaper than I first said

I previously reported that `cor:centre` needs `cor:stripping` and
`cor:meet-region` and that neither is in Lean. **That was wrong** — it came from
grepping PAPER LABEL names, the same bad evidence class as the stale "§3 is the
next unit" note that `slab0_not_mem` refuted. Searching by statement shape:

- meet-region: `coreA_inter_coreB_eq_slab0`, `lowerBound_iff_subset_slab`,
  `greatest_lowerBound_eq_slab`, and now `slab0_not_mem` — all PROVED
- stripping / trace-class: `trace`, `trace_compl`, `trace_union`, `trace_iUnion`,
  `trace_disjoint`, `CEq`, `NRep`, `nrep_exists`, `nrep_unique` — all PROVED

So the §3 machinery `cor:centre` runs on is there. **The genuinely missing piece
is the centre itself** — no `IsCentral`/`Z(L)` exists anywhere in the Lean.
Verified definable against the real carrier (2026-08-24):

```
def IsCentral (U : UlamMatrix M) (E : Set (M × Fin 4)) : Prop :=
  (carrier U).Has E ∧ ∀ A, (carrier U).Has A → (carrier U).Has (E ∩ A)
```

`cor:centre` then has two halves. ⊇ (countable/co-countable are central) should
follow from the σ-class basics. ⊆ is the substantive half: central ⟹ the trace
quadruple has last two coordinates empty, `NRep` membership forces
`[E₁]=[E₂] ∈ {0,1}`, compatibility with A₂/A₃ propagates the constant, and
parity forces the fourth. Multi-step but every input is present.

## The fidelity gap, stated correctly

My memory records `PsiAmended` as strictly weaker than the paper's Ψ because
`IsIrreducible` is an unconnected stub. Precisely: the gap is that `PsiAmended`
does not carry essential irreducibility **as a hypothesis**. Proving `cor:centre`
for the witness fixes that. **Defining `IsIrreducible` would not** — that is
bookkeeping, not fidelity.

## Recommended order

1. **Non-segregated** — forcing-lemma shape, most machinery present.
2. **`cor:centre`** — needs the centre definition + the ⊆ argument; closes the
   real Ψ-fidelity gap.
3. **Concrete / σ-complete** — read the paper's definitions first; do NOT
   discharge with the trivial readings above.

Do not touch the four axioms until the corresponding forcing lemma is proved.
Each should be RETIRED by a theorem about the witness, not DEFINED into
existence.


---

## Update 2026-08-24: `cor:centre` part 2 — and where it actually stops

Proved and committed (all `[propext, Classical.choice, Quot.sound]`):

- `trace_inter_out` / `trace_inter_in` — generic core-intersection trace calculus
- `traces_agree_of_core` — the two "inside" coordinates of a core carry
  countably-equal traces, given the two "outside" ones are empty
- `central_t01`, `central_t02`, `central_t12` — instantiated at coreA/B/C
- `central_all_traces` — **all four traces of a central set are countably equal
  to a single ξ** (the code is constant: three coordinates agree, `κ 3 = false`,
  and even weight forces the fourth)
- `countable_of_traces_countable`, `central_countable_iff` — the reduction

### The remaining gap, stated precisely

`cor:centre` claims a central `E` is countable **or co-countable**. What is
proved is the reduction: `E` is countable iff `ξ` is.

The missing step is the paper's `[E] ∈ {0,1}` — that `ξ ≈ ∅` or `ξ ≈ M`.

⚠ **This does NOT follow from the invariant.** `def:invariant` says only that the
traces are `ξ^(κ_f)` for *some* `ξ`; it permits any `ξ` whatsoever. I initially
assumed the code analysis would deliver the dichotomy and it does not — the code
being constant gives "all traces ≈ ξ", not "ξ is trivial".

So the step needs **centrality used a second time**, beyond the code: compatibility
of `E` with sets that separate an uncountable-and-co-uncountable `ξ` (the cells
`D_{α,n}`, presumably — that is where the Ulam matrix's almost-disjointness would
bite). The paper's proof compresses this into "the analysis of `cor:stripping`",
which is why it read as mechanical.

Do not close this by weakening the statement. The honest options are: find the
cell-based separation argument, or leave `cor:centre` as the reduction plus a
named open step.
