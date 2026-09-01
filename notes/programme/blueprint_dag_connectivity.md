# What is missing that would make the blueprint a network

**Written 2026-08-25.** Measurement, not proposal. Answers: which nodes/results
are absent that currently keep the DAG a set of parallel chains rather than a
connected structure.

## AMENDMENT 2026-08-25 (tower): island 1 is closed

The descent-witness ladder is now in the blueprint. Blueprint declarations went
104 -> 115; the four `DescentWitness*` modules moved off the coverage baseline
(26 -> 22 uncovered).

Measured with `scratchpad/dagcheck.py` (a different parser from the one that
produced the numbers below, so compare the deltas, not the absolutes):

| | before | after |
|---|---|---|
| nodes | 98 | 110 |
| edges | 160 | 179 |
| components | 6 | 6 |
| MO2 component | **4** | **16** |

So the MO2 island is no longer a dead end — it is the 4-rung ladder
`def:mo2 -> def:l2n -> thm:star-finite -> def:navara-l2 -> thm:star-infinite`
with the consistency and closure legs hanging off it. What did **not** happen:
the component count is unchanged, and the ladder did not attach to the 28-node
ch4/ch5 body. Growing an island is not the same as connecting one. The
`\uses` edges all run *into* MO2, because that is the real dependency
direction — nothing in the σ-essential lane consumes `star_infinite`.

Two things found on the way in, both recorded because they change what the
nodes mean:

1. **The consistency model did not cover `L2.instOML`.** `DescentWitnessConsistency`
   realized the ten blockwise axioms using a bare `mOrtho` function, and its
   docstring claimed all eleven. But there was no product `OrthomodularLattice`
   instance anywhere in the library, so the eleventh axiom — that `L₂` *is* an
   OML — was unmodelled, and it is the one that gives `⊓`, `≤`, `ᗮ`, `⊥` in the
   other ten their meaning. Fixed by proving `instPiOrthomodularLattice`
   (products of OMLs are OMLs, coordinatewise) and identifying `mOrtho` with
   that structure's orthocomplement definitionally (`mOrtho_eq_ortho`).
   `axioms_consistent` now carries both as conjuncts. This is the standing
   hazard in its usual costume: everything compiled, and the gap was only
   visible by reading what the model did *not* say.

2. **`axiomcheck.sh` grew a citation-keyed allowlist** (`axiom_allowlist.txt`),
   because `star_infinite` rests on Navara's eleven cited axioms and the gate
   was absolute. The allowlist is not a weakening: an unlisted axiom still fails
   hard, an allowlist entry without a citation is a hard error, entries used by
   no node are reported as stale, and cited declarations are counted *separately*
   from closed ones so the number of things actually proved stays visible. The
   gate now reads `115 declarations: 113 closed, 2 cited, 0 uncited`.

Island 2 (the diagonal layer, 4 nodes) is untouched and still the next item.

---

## AMENDMENT 2 — 2026-08-25 (tower): island 2 is closed, and [B] is not what it looked like

### Island 2 (the diagonal layer) — closed

`AJNoExtension.cyl_iInter_empty` now routes through
`Diagonal.pi_inter_diag_eq_empty` instead of re-running the argument.
`grep 'Diagonal\.'` over the library no longer returns nothing.

The carrying map is the content: a coherent family is not a sequence, so
`ASM.toSeq ω : k ↦ (ω_k)_k` reads off the top coordinate at each level. The two
facts `pi_inter_diag_eq_empty` consumes come from different places, which is
what makes the reduction non-trivial rather than a rename — every entry lies in
its own `X k` by the subtype and needs no hypothesis at all, while constancy
needs *both* the coherence (coordinate `0` from level `i` down to level `0`) and
the base cylinders (coordinate `0` across to coordinate `i` at level `i`).

With the Lean routed, the blueprint edge `thm:aj-no-extension → thm:diag-empty`
became *true* and was added. Before the refactor it would have been a lie: the
prose described the argument the diagonal layer proves while the Lean proof did
it again by hand.

| | before | after ladder | after refactor |
|---|---|---|---|
| nodes | 98 | 110 | 110 |
| edges | 160 | 179 | 180 |
| components | 6 | 6 | **5** |
| diagonal island | 4 | 4 | **absorbed into 48** |

`ASM.AJ_no_extension_unconditional` still rests on `propext, Classical.choice,
Quot.sound` only. One edge, because one duplicated argument was removed.

### [B] `ReconstructionTheorem` — the stated rationale does not hold

The claim was that it "imports QuerySystem (covered) AND is imported by
DelayEmbedding (covered)", so a node would land *between* two things already in
the graph. Both ends fail, at the node level rather than the module level:

1. **Nothing is used from `QuerySystem`.** `ReconstructionTheorem.lean` imports
   `QuerySystem.QuerySystem` and references no declaration from it. The import
   is inert; there is no edge to ch0 to be had.
2. **The covered `DelayEmbedding` nodes do not depend on it.** The ten delay
   nodes in the blueprint are all query-system side (`delayQuery`, `delayEval`,
   `delayQuerySystem`, `not_seqUpperDirected`, the fixed-lag chain). The five
   declarations that *do* consume `ReconstructionTheorem` —
   `delayObservableAlgebra`, `delayObservableAlgebra_eq_comap`,
   `delayMap_shift_intertwining`, `delay_reconstruction_iff`,
   `delay_cyclic_implies_reconstruction` — are **none of them blueprint nodes**.

`DelayEmbedding.lean` is really two mathematically disjoint halves sharing a
file: the delay query system over `SensorStream X`, and a "Reconstruction
bridge" section over `(X, h : X → ℝ, T : X → X)`. They share no declaration.
Coverage cannot see this — it asks only that a module have *some* covered
declaration, so a module can be half-blueprinted and read as done.

So adding `ReconstructionTheorem` alone yields a **new sixth island**, which is
what the table below ranks as value "none". A real bridge needs a lemma
identifying the delay query system's `delayEval` with `delayMap` — i.e.
instantiating the sensor stream as an orbit `n ↦ T^[n] x` and the outcome space
as `ℝ` via `h`. That is mathematics and a modelling decision about whether the
query system's `X` is the state space or the observation space, not annotation.
Left for the human.

---

## AMENDMENT 3 — 2026-08-25 (tower): [B] resolved by writing the bridge, not by annotating

Amendment 2 recorded that `ReconstructionTheorem` could not be attached by
annotation, and that a real bridge needed a lemma identifying the delay query
system's `delayEval` with `delayMap`. That lemma is now written, and the lane is
in.

### The bridge (in `DelayEmbedding.lean`, `ReconstructionBridge` section)

- `orbitStream h T x` — the sensor stream a state emits.
- `delayEval_orbitStream` — sampling that stream at `(d, τ)` returns exactly the
  delay-coordinate vector `(h (T^(kτ) x))_{k<d}`.
- `delayEval_orbitStream_one` — at unit lag, `Φ_h` truncated to `d` coordinates.
- `delayQueryAlgebra` — the σ-algebra the queries induce on the state space.
- `delayQueryAlgebra_eq_delayObservableAlgebra` — **it equals `𝒪_h`**.

All five rest on `[propext, Classical.choice, Quot.sound]`.

The two modelling questions Amendment 2 flagged, answered and written into the
blueprint prose so they can be disagreed with:

1. *Whose space is the query system's type parameter?* The **observation**
   space. `delayQuerySystem Y` samples streams `ℤ → Y`; at `Y = ℝ` its outcomes
   are tuples of sensor readings. The state space enters only through
   `orbitStream`. A state is never an outcome of a delay query.
2. *Which time direction?* `delayEval` samples the **past** (`0, -τ, …`) while
   reconstruction iterates `T` **forward**. They agree once reading the stream
   backwards is reading the orbit forwards — the ordinary delay-coordinate
   convention. The alternative (past = backward iterates) needs `T` invertible;
   for invertible `T` the two generate the same σ-algebra, and for
   non-invertible `T` only the convention taken here exists.

Checked before blueprinting, because a bridge to a decorative node is not a
bridge: `delayEval` is load-bearing in the query system. `evalSurjective` — the
hypothesis the fixed-lag extension theorem consumes — is proved through
`delayEval_surjective`, and coherent families are literally built as
`ω.1 (d',τ') = delayEval d' τ' s`.

### Result

10 nodes, covering `ReconstructionTheorem.lean` (baseline 22 → 21).

| | after refactor | after lane |
|---|---|---|
| nodes | 110 | 120 |
| edges | 180 | 196 |
| components | 5 | **5** |
| main component | 48 | **58** |

The lane **merged** rather than forming the sixth island Amendment 2 predicted —
because the bridge theorem `\uses` both `def:delay-query` (query-system side,
already in the main component) and the reconstruction nodes. Gates: 125
declarations, 123 closed, 2 cited, 0 uncited.

One thing the proof turned up that is worth keeping: **unit lag alone already
generates `𝒪_h`**. The `≥` direction only ever uses queries `(n+1, 1)`, so the
lag parameter τ adds no resolution to the observable algebra. It matters for the
refinement order, not for what the queries can ultimately resolve.

What this does **not** do: it does not transfer the extension theorem.
`thm:delay-not-sud` still puts the delay query system on the wrong side of
sequential upper-directedness. The gain is that reconstruction is now a
statement in the query system's own vocabulary.

The remaining components are the σ-essential lane (28), pruning (17), the MO₂
ladder (16), and one isolated node (`lem:cont-above`). The 58/28 split is the
one the original measurement called structural and it is unchanged.

---

## AMENDMENT 4 — 2026-08-25 (tower): the pruning split is closed; the 43/27 split is not

Amendment 2 said the 43/27 split "needs mathematics, not annotation" and
Amendment 3 said the same of pruning. **Pruning's did have its mathematics
available and it is now closed. The 43/27 one did not, and an attempt to close
it was withdrawn** — see (b), which is the useful part of this entry. Three
steps, all kernel-checked, no sorries:

### (a) Fixed lag — `delayQueryAlgebraAtLag_eq`

`delayQueryAlgebraAtLag h T τ = 𝒪_h(T^τ)`. Stroboscopic observation at lag `τ`
is not a degraded view of `T`; it is the same reconstruction question asked of
`T^τ`.

This explains why the delay and pruning chapters never met. The all-lags bridge
takes a supremum and unit lag already attains it, so `τ` is invisible to it —
but at *fixed* `τ` the algebra is strictly smaller, and the fixed-lag question
is what pruning asks. The sup destroys exactly the parameter pruning is indexed
by. Not an edge, and deliberately not blueprinted as one: a dictionary is not a
dependency.

### (b) C1′ — the quarantine — **WRITTEN, THEN REMOVED 2026-08-25**

Claimed at the time to close the 43/27 split. It did close it, and the closure
was worthless, which is not the same thing.

The content: a query's outcome space carries a σ-algebra, σ-algebras are
intersection-closed, so `boolean_no_witness` forbids a witness on one.
That much is true and mildly worth knowing — it says C1′ holds for structural
reasons rather than the finiteness/compactness ones the seed gives.

But the *edge* came from `delayQuery_no_witness`, a pure instantiation of the
general statement at a delay query, adding nothing beyond naming a delay object
inside a σ-essential theorem. Removing the module puts the count straight back
to **4 components** with the σ-essential lane re-separated at 28 — which is the
proof that nothing but the instantiation was holding it. User called it an
arbitrary bolt-on and removed it; the judgement is right, and it is the same
objection this file raised against asserting `\uses` edges from prose, in Lean
form instead of LaTeX form.

**The 43/27 split is therefore still open**, and still needs mathematics. What
would count is a theorem in which the two lanes constrain each other, not one
whose statement merely mentions both.

Worth salvaging if anyone wants it later, as a σ-essential-lane fact with no
delay content: `L₁` is not the Dynkin system of *any* σ-algebra.

### (c) Relational delay — `isLISC_delay_witness` (**closes the pruning split**)

`LISC_k(L)` yields a ρ-trajectory, periodic of period `kL`, whose depth-`k`
lag-`L` delay query is **injective**. The delay query's sample times
`0, -L, …, -(k-1)L` are exactly the cycle positions sharing layer `0`, and
`IsLISC`'s simplicity clause says those carry distinct states. **Layer-injectivity
is delay-injectivity** — the same condition in two vocabularies, which is why
the lanes kept reaching the same combinatorics from opposite sides.

Non-vacuity recorded, not assumed: `isLISC_complete_bool`.

**Components 4 → 3.** Pruning (17) merges into the main component, now 118.

### The arc

| | start of session | now |
|---|---|---|
| components | 6 | **4** |
| main component | 43 | **88** |
| blueprint declarations | 104 | **140** |
| axiom receipts | 104 closed | 138 closed, 2 cited, 0 uncited |

What remains separate: the **σ-essential lane** (28) — the 43/27 split, still
open, see (b); the **MO₂ ladder** (16); and one isolated node
(`lem:cont-above`). The ladder is the honest one — nothing in the σ-essential
lane consumes `star_infinite`, and the `\uses` edges all run *into* MO₂ because
that is the real dependency direction.

### Still open, and named

The deterministic embedding. `stateStream T x` is **not** in
`Subshift (graph T)`: `Int.toNat` clamps the positive half constant, so the
trajectory condition would demand `x = T x`. A non-invertible `T` has a
one-sided orbit only. Bi-infinite trajectories for deterministic dynamics need
`T` bijective or a one-sided stream type. The bridge does not need either — a
cycle witness is bi-infinite outright — but anything wanting to run the bridge
*backwards*, from delay data to a pruning certificate, will hit this first.

---

## The measurement

95 nodes, 127 edges, 1.34 edges/node. **Five connected components** (undirected):

| size | chapters | what it is |
|---|---|---|
| 43 | 0,1,2,3 | query systems → extension → Andersen–Jessen → delay |
| 27 | 4,5 | Boolean/orthomodular hinge → σ-essential witness |
| 17 | 6 | pruning / Theorem B |
| 4 | 2 | `def:diag-cylinders`, `lem:diag-inter`, `lem:diag-measurable`, `thm:diag-empty` |
| 4 | 4 | `def:oml`, `def:mo2`, `thm:mo2-oml`, `thm:mo2-gap` |

The two size-4 components are **orphan islands inside chapters that otherwise
connect**. Those are the sharpest signal: they are not separate subjects, they
are results whose consumers are missing.

## Island 1 — MO₂ (ch4). The missing rungs are FORMALIZED and outside.

`grep MO2` over the library: MO₂ is used by four modules, **none in the
blueprint**, forming a clean ladder:

```
OrthomodularMO2          (Rung 1)  ← IN the blueprint, as the island
  └ DescentWitnessFinite    (Rung 2)  115L,  8 decls, 0 axioms
      ├ DescentWitnessInfinite (Rung 3) 160L,  3 decls, 11 cited axioms
      └ DescentWitnessConsistency       110L, 12 decls, 0 axioms
          └ DescentWitnessClosure       113L,  5 decls, 0 axioms
```

Navara's construction (PAMS 115, 1992, p. 428) with MO₂ blocks: finite
truncation `L2N N = Fin N → MO₂`, then the infinite object `L₂`, then a
concrete model proving the Rung-3 axioms consistent, then three closure legs.
Culminates in `star_infinite` — the `(★)` property.

**This is the single highest-value addition.** It is ~500 lines of existing,
axiom-clean-except-cited Lean that would attach the MO₂ island to a real
chain, and it is the (β)-swap descent argument — the thing MO₂ exists to serve.
Adding it turns a 4-node orphan into a 4-rung ladder.

## Island 2 — the diagonal layer (ch2). Genuinely unused.

`grep 'Diagonal\.'` over the library returns **nothing**. `Diagonal.lean` is
consumed by no other module.

Note this is *not* the same as being unproved — the nodes are `\leanok` and the
axiom gate passes. The diagonal cylinders were built for the Andersen–Jessen
refutation, and when that landed (2026-08-24) `AJNoExtension` proved its own
`cyl_iInter_empty` directly rather than going through `Diagonal`.

So the fix here is a *Lean* change, not a blueprint one: either
`AJNoExtension.cyl_iInter_empty` should be refactored to consume
`Diagonal.pi_inter_diag_eq_empty`, or `Diagonal` should be recognised as
superseded. **Refactoring is the better call** — it would create a real
ch2-internal edge and remove a duplicated argument.

## The three big components — why they do not touch

- **43 (ch0–3) vs 27 (ch4–5).** Structural, not an oversight. Checked
  2026-08-24: no OML module imports ch0/ch1. `ConcreteOMLBlocks →
  SigmaEssentialWitness → SigmaEssentialLocalization → Mathlib`;
  `OrthomodularMO2 → Mathlib`. The σ-essential lane genuinely does not use the
  query-system core. A bridge would have to be *written*, not annotated.
- **17 (ch6, pruning).** Its own opening says it: "a separate line of work…
  sharing no definitions and no dependencies". Reconstruction lane. Honest.

## The uncovered modules that would ADD edges, ranked

Of the 26 uncovered modules, those whose imports reach something already in the
blueprint (so adding them yields immediate edges):

| module | imports | value |
|---|---|---|
| `DescentWitness{Finite,Infinite,Consistency,Closure}` | → `OrthomodularMO2` | **highest** — de-orphans MO₂, 4 rungs |
| `SigmaEssentialOpenCore` | → `SigmaEssentialLocalization` | high — Ψ/Φ open core, `TargetA_sharp`, the admissibility work |
| `ConcreteOMLBlocks`, `MarczewskiTransport`, `ConcreteOMLPatterns` | chain from `SigmaEssentialWitness` | high — the block/pattern layer, ~1700L axiom-free |
| `SigmaEssentialBareForm` | → `SigmaEssentialLocalization` | medium |
| `ReconstructionTheorem` | → `QuerySystem` | medium — would attach to ch0 AND is what `DelayEmbedding` imports |
| `UlamWitnessReceipts` | → covered modules | low — receipts, not results |
| `BandClosure`, `Commensurability`, `FibreProductReflection`, `FiniteAtomFoldKernel`, `UltrafilterCharge`, `WindingInjectivity` | no project imports | none — would be new islands |

## What would actually make it a network

Ranked by edges-per-effort:

1. **The descent-witness ladder** (4 modules, already written). De-orphans MO₂
   and gives ch4 a real internal chain.
2. **`ReconstructionTheorem`.** It imports `QuerySystem` and is imported by
   `DelayEmbedding` — so adding it puts a node *between* two things already in
   the blueprint, converting a gap into a path. Cheapest real bridge.
3. **`SigmaEssentialOpenCore` + the block/pattern layer.** Large, axiom-clean,
   and it is where Φ/`TargetA_sharp` live — the open core the whole lane is
   about.
4. **Refactor `AJNoExtension` onto `Diagonal`.** Lean work, not blueprint;
   removes a duplicated argument and de-orphans island 2.

None of these bridges the 43/27 split — that one needs mathematics, not
annotation, and is the honest shape of the corpus.

---

## AMENDMENT 5 — 2026-08-31: the narrative audited against the measured DAG

Prompted by a request to strip internal jargon ("the pivot") from the
blueprint, which turned into the broader question of whether the document's
narrative matches what the graph actually contains. Three findings, all
measured, all now fixed in `content.tex`.

### The measurement

Every `\uses`/`\ref` in chapters 4--7 whose target resolves to a label defined
before the ch4 boundary:

| edges | from | to |
|---|---|---|
| 9 | ch7 pruning | ch3/4 delay (`def:delay-query`, `def:orbit-stream`, `thm:lag-algebra`) |
| 1 | ch4 delay (l.944) | ch7 `def:lisc` |
| **0** | **the Boolean→orthomodular and σ-essential chapters** | **anything above them** |

Component recount by chapter: **87 / 82 / 1** — matching the recorded 86/82
(the singleton is an isolated delay node). Component 1 = ch1+2+3+4+7;
component 2 = ch5+6 exactly. This confirms `program_overview.md` over ch7's
own prose: **pruning is in component 1**, attached through delay. Ch7 calling
itself "a separate line of work… sharing no definitions and no dependencies"
is true only relative to the σ-essential chapters, and reads as more isolated
than the graph says.

### Finding 1 — the one false seam (FIXED)

Ch5 opened "Everything above is the distributive case… This chapter isolates
the single predicate separating that regime from the orthomodular one." Two
claims, and they do not fail together:

* *intersection-closure separates Boolean from orthomodular* — expository,
  true, needs no edge. `def:interclosed` feeds six nodes across ch6
  (`thm:boolean-baseline`, `lem:boolean-no-witness`, `thm:phi-finite`,
  `thm:one-block-iff-boolean`, `cor:carrier-not-orderiso`). **Earned.**
* *"Everything above is the distributive case"* — asserts inheritance from
  ch1--4. **Zero edges underneath it.** Unearned.

What made this a defect rather than a convention: **the blueprint already
narrates seams honestly everywhere else.** Ch7 declares its independence, ch6
declares its open question. Ch5 was the sole outlier. Replaced by an explicit
statement of independence in ch7's idiom, plus what the chapter actually does,
with `\ref`s to the three results that do it. Prose `\ref` adds no `\uses`
edge: the count stayed 389.

### Finding 2 — Φ was absent from the front, and overloaded (FIXED)

The blueprint opened on "preordered families of measurable spaces with
compatible refinement maps." Φ — the question the σ-essential line exists to
reach — appeared first at `rmk:phi-open`, line 2148 of 2757. A reader could
not learn from the document what question it was for.

Compounding it: `\Phi` names two unrelated things. `\Phi_h` is the delay map
in ch4; unsubscripted `\Phi` is the frontier conjecture in ch6. Same glyph, no
disambiguation. Same defect class as "pivot" — a symbol carrying private
meaning — and the more expensive of the two.

Fixed by an unnumbered front-matter chapter stating: the two lines and that
they are independent, `psi_ZFC` as the theorem and Φ as the open question with
forward refs, an explicit notation warning on Φ, and the status conventions
(206 closed / 7 cited, and that conditional claims carry their hypotheses
explicitly rather than by citation).

### Finding 3 — "the pivot" removed

Eight occurrences (4 in `content.tex`, 4 in `ConcreteMO2.lean` docstrings)
replaced by the predicate's own name, intersection-closure. No new coinage; no
`\label`/`\uses`/`\lean` touched. Neighbouring coinages left standing and
flagged instead: `PoorPair` (a Lean identifier, so renaming costs a refactor)
and "rung"/"descent ladder" (a live metaphor doing navigational work).

### Found on the way in: a red gate, and five stale oleans

**`checkdecls.sh` was failing on `main`,** and not from any edit here. A bare
`import QuerySystem` errored: `environment already contains
'SigmaEssential.TwoValuedState.toFinAdd' from QuerySystem.SigmaEssentialWitness`.

Cause: `.lake/build/lib/lean/QuerySystem/SigmaEssentialAmended.olean`, dated
**2026-07-06**, whose source was renamed to `SigmaEssentialWitness.lean` in
`fc17d58`. The stale olean was never swept and `lakefile.toml`'s `QuerySystem.+`
glob picks up orphan oleans. Four more orphans alongside it: `AxCheck`,
`CapTest`, `EncodingDefectCheck`, `SelectorUpperCore` — none referenced by any
source file or blueprint node. Note `EncodingDefectCheck`: the index records its
certificates as **vacuous**, so a stale olean of it in the build tree is the
standing hazard sitting in the artifact layer rather than the source.

Swept and rebuilt; all five gates now green (0 sorries · 213 decls · structure
OK · coverage OK · 206 closed / 7 cited / 0 uncited).

**This is the docstring of `QuerySystem.lean` coming true a second time.** It
already records that two modules defining the same name is "not merely untidy:
importing both is a hard error… which is how this was found." The same failure
recurred through the *build directory* rather than through sources, where no
gate looks. A `lake clean`-and-rebuild, or an orphan-olean check, would catch
the class.

### Not attempted

The bridge (task A). The bar in amendment 4(b) — *a theorem in which the two
lanes constrain each other, not one whose statement merely mentions both* —
is unmet and nothing here bears on it. Everything above is prose brought into
line with measured structure, which is subtraction, not new mathematics. The
two-component shape is unchanged and is still the honest shape of the corpus.
