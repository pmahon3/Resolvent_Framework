# Getting up to speed: the OML descent residue

**Purpose.** A zero-to-ready reading path for the one open question in the
OML extension thread that needs *human* mathematical work. It assumes you
are coming back cold. It does not re-derive the research note — it points
you into it (`oml_extension_problem.tex`/`.pdf` and `verification/`) and
gives you the "you are here" map the note assumes you already hold.

When you can answer the **checkpoint** questions at the end of each
section without looking, you are ready for the question in §5.

Companion files:
- `oml_extension_problem.tex` / `.pdf` — the full research note (the
  authority; this doc is a guide to it).
- `verification/` — the small computational + hand-verification scripts.
- Memory: `project_overview.md`, `oml_relational_prob_novelty.md`,
  `oml_two_point_spaces.md`.

---

## 0. The one-sentence version

> Build a σ-additive probability theory on a non-distributive
> orthomodular lattice **without descending from a sample space** — or
> prove it can't be done — by supplying the missing σ-OML representation
> that all three known routes fail to give.

Everything below is the scaffolding needed to understand why that sentence
is (a) precise, (b) genuinely open, and (c) worth the effort.

---

## 1. Prerequisites to know cold

You need four things at your fingertips. If any is shaky, fix it before §2.

### 1a. OML / OMP, and meet-zero vs. orthogonal — the gap that drives everything

- **Orthomodular lattice (OML):** a bounded lattice with an
  orthocomplement `a ↦ a^⊥` (involution, order-reversing,
  `a ∧ a^⊥ = 0`, `a ∨ a^⊥ = 1`) satisfying the orthomodular law
  `a ≤ b ⟹ b = a ∨ (a^⊥ ∧ b)`. Boolean = the distributive special case.
  Motivating non-Boolean example: `L(H)`, closed subspaces of a Hilbert
  space. Smallest: `MO₃` (three complementary pairs pasted at 0 and 1).
  *(Def. in .tex §2, Defs 2.2–2.3; Hasse diagram Fig. 1.)*
- **The gap.** Two elements are **orthogonal** (`a ⊥ b`) if `a ≤ b^⊥`;
  they are **meet-zero** if `a ∧ b = 0`. In a Boolean algebra these
  coincide. In a non-distributive OML, **orthogonal ⟹ meet-zero but NOT
  conversely**. This single gap is the whole extension obstruction —
  internalize it. `MO₂` is the smallest concrete witness
  (`{1,2} ∧ {1,3} = 0` but `{1,2} ∩ {1,3} = {1} ≠ ∅`).
  *(.tex §2, "meet-zero versus orthogonal"; `verification/concrete_meetzero_vs_orthogonal.py`.)*
- **OMP / concrete logic.** An orthomodular *poset* only requires joins
  for orthogonal pairs. "Concrete" = "set-representable" = embeds in
  `(P(X), ⊆, complement)` preserving orthogonal joins. **Trap:** concrete
  ≠ Boolean (`MO₃` is concrete); the dividing line that closes the
  meet-zero/orthogonal gap is *intersection-richness*, not concreteness.
  **Naming note:** the abstract condition `a∧b=0 ⟹ a⊥b` is Tkadlec's
  *"Boolean orthoposet"* (Math. Bohemica 119, 1994) — which does **not**
  mean Boolean *algebra*. Use "intersection-richness" as the working term.

### 1b. The state / valuation / charge ladder

Three strengthenings of additivity, strictly increasing. Keep them
distinct — collapsing them is one of the recurring errors on this thread.

1. **State:** `s(1)=1`, additive on **orthogonal** pairs.
2. **Valuation** (local convention in the note): additive on **meet-zero**
   pairs (binary, strictly stronger).
3. **Extends to a (Boolean) charge:** the **n-ary** condition
   `Σᵢ s(aᵢ) ≤ 1` for every pairwise-meet-zero family (strictly stronger
   again). *This is the extension axis.*

Sanity anchor: on `MO₃`, `s ≡ ½` is a valuation but fails (3) at
`{p,q,r}` (`³⁄₂ > 1`). *(.tex §2; `verification/mo3_extension.py`.)*

### 1c. McDonald–Bimbó duality — the dual space `S₀(A)` and its points `P(A)`

The relational realist move: instead of starting from a space of outcomes,
build the dual from the lattice itself.
- `S₀(A)` = the space of **filters** on `A` (compact, Stone-like).
- `P(A) ⊆ S₀(A)` = the **principal filters** — the "physical points," the
  realization datum. *Canonical*, unlike the Boolean case where the pure
  points are a non-canonical choice.
- `h(a) = {filters containing a}` is an OML iso onto the ⊥-stable clopens.
  Set `μ(h(a)) = s(a)`.
- **The duality is FINITARY.** `h(⋁ₙ aₙ) = (⋃ₙ h(aₙ))^⊥⊥` holds for
  *finite* joins, fails for countable ones. This finitariness is the wall
  the whole open question runs into. *(.tex §2; primary-source check in
  `verification/mb_primeness_check.md`.)*
- Why MB and not the rival Cannon–Döring OML duality? MB carries `P(A)` as
  explicit structure; both are purely structural (no measure), but MB's
  filter points are exactly the realization datum the programme needs.

### 1d. Loomis–Sikorski — the Boolean engine the OML case is missing

This is the keystone. In the Boolean world, the descent argument
("σ-additive ⟺ the measure concentrates on the physical points") runs on a
**Loomis–Sikorski** representation: a σ-complete Boolean algebra is a
σ-tribe of sets mod a σ-ideal. **There is no OML analogue** — and supplying
one (or proving none exists) *is the open question*. Hold this as: "the
Boolean proof has an engine; the OML proof needs one and doesn't have it."

> **Checkpoint 1.** (i) Give the `MO₂` witness for meet-zero ≠ orthogonal.
> (ii) Why does `s ≡ ½` on `MO₃` clear the valuation bar but fail
> extension? (iii) What is `P(A)`, and why is it canonical here but not in
> the Boolean case? (iv) What does Loomis–Sikorski do in the Boolean
> descent proof, and what's the OML status of it?

---

## 2. The narrowing: from "the extension problem" to "the one residue"

The headline question — *when does a state on an OML `A` extend to a
σ-additive measure on `S₀(A)`?* (.tex Question 2.6) — splits into **two
independent axes** that the Boolean case fuses. Most of the problem is
already settled; one residue is live.

```
  state s on OML A
        │
        ├── EXTENSION axis: does μ extend to a finitely additive
        │   charge on the FULL Boolean clopen algebra of S₀(A)?
        │   → governed by the meet-zero/orthogonal gap (§1a)
        │   → SETTLED: classical Horn–Tarski/Pitowsky feasibility;
        │     finite case = decidable LP; can fail for every state.
        │
        └── DESCENT axis: once extended, does the measure concentrate
            on the physical points P(A)?
            → governed by σ-additivity (needs the missing engine, §1d)
            → OPEN. This is the residue.
```

Two sharp results pin down the extension axis so you don't re-fight it:

- **Finite case:** a decidable linear program. `MO₃` shows it can fail for
  *every* state. Not a frontier. *(.tex §2, §5 "Extension axis".)*
- **Infinite `L(H)`, normal states — KILLED.** The clustering argument
  inside a single 2-plane: `k` distinct lines force `k·s(e) ≤ 1` for all
  `k`, so any state with `s(e) > 0` on some finite-dim `e` fails to
  extend. That's *every normal (Gleason) state*. σ-completeness
  irrelevant; the argument is finitary. *(.tex §2.1, Prop 2.7;
  `verification/lh_infinite_extension.py`.)*

So on the extension axis the *only* survivors are the **singular states**
of `L(H)` (`s(e)=0` on every finite-dim `e`) — see §4. The descent axis
is where the real open problem lives — see §3.

> **Checkpoint 2.** Draw the two-axis diagram from memory. Why is the
> extension axis "settled but partly degenerate"? Which states on `L(H)`
> survive the clustering kill, and why does the kill not touch them?

---

## 3. The open question, stated crisply

> **Does a σ-complete, concrete, non-Boolean, infinite OML admit a
> Loomis–Sikorski-type representation (a σ-tribe of sets mod a σ-ideal),
> or a countable-join-preserving σ-Stone duality — or can one prove none
> exists?**

A positive answer is the engine for *relational probability without
realizations*: σ-additive probability built from the entailment relation
of a non-distributive OML, **not** descended from any sample space — the
non-Boolean analogue of localic (pointless) measure theory. A negative
answer (an impossibility theorem) closes the whole cluster, including both
residues, at once. The outcome is **binary and large**. *(.tex §3
"finitary-to-σ bridge"; §5 "Descent axis"; "What is at stake".)*

**Why this is the live stake, not just a loose end.** The motivating idea
("probability from relations, point-free") might *look* already delivered
by `L(H)` + Gleason. It is not — and seeing why is the conceptual crux:

> **The (A)/(B) point-space equivocation — do not let this creep back.**
> "Point-free" slides between two point-spaces. **(A)** the Hilbert rays
> `L(H)` and the Gleason density `ρ` are *built from*; **(B)** the MB dual
> filters `P(A)`. The programme defines *realization* = concentration on
> **(B)**. Gleason removes **(B)** but **requires (A)** — and is a
> *representation* theorem (the most point-ful result available, reducing
> every lattice state to the point datum `ρ`). So `L(H)`/Gleason witnesses
> the PR_lattice / PR_dual **separation**, NOT point-freeness, and is not
> the existence proof. Because it isn't, the σ-OML representation (§3) is
> the *only* candidate engine. **Never write "Gleason already builds
> relational probability."** *(Memory: `oml_two_point_spaces.md`; .tex
> "What is at stake".)*

> **Checkpoint 3.** State the open question in one sentence without
> looking. Explain why Gleason on `L(H)` does *not* already answer it
> (the (A)/(B) distinction). What would a positive vs. negative answer
> each deliver?

---

## 4. What is already ruled out (don't redo this)

Coming back cold, the danger is re-walking dead ground. The following are
closed; cite them, don't re-derive them.

- **Three named routes to a σ-OML engine — all blocked.** *(.tex §3.)*
  1. **RDP / effect-algebra:** Loomis–Sikorski holds for σ-MV and
     monotone σ-effect-algebras *with* RDP, but lattice-EA has RDP iff
     it is MV, and OML ∩ MV = Boolean. So **OML + RDP ⟺ Boolean** — the
     machinery has no non-Boolean OML to act on.
  2. **MacNeille completion:** the MacNeille completion of an OML need not
     be orthomodular (Harding 1991) — can't complete to absorb joins.
  3. **σ-Stone duality:** none exists. MB is finitary; Freytes gives only
     an equational theory, no set/tribe representation.
- **Normal states on `L(H)` don't extend.** Clustering argument (§2);
  hand-verified dichotomy in `verification/lh_singular_dichotomy.md`.
- **Both standing negatives stress-tested against primary sources (MISS,
  2026-06-04).** (i) No impossibility theorem for the *concrete* class —
  the load-bearing word is "concrete": the one positive occupant
  `P(H)`+Gleason is *non-concrete* (Kochen–Specker → no separating
  two-valued states). (ii) No σ-Loomis–Sikorski: both OML dualities take
  infinite joins as a *closure* not a union (Cannon–Döring `cls(⋃Sᵢ)`,
  MB `(⋃h(aₙ))^⊥⊥`). *Overclaim guard:* Gudder concrete logics ARE
  set-representable non-Boolean — but point-ful posets, not a σ-LS theorem.
- **Prior art map (scout, PARTIALLY OCCUPIED).** Every existing
  construction gives up exactly one needed property: Döring 2009
  (finitely additive), Bohrification/HLS (σ-additive but via a
  *distributive* internal locale, per-Boolean-context), localic valuations
  (distributive by definition), Gleason (not point-free). The unoccupied
  conjunction — point-free × σ-additive × natively non-distributive ×
  directed-system-built — is exactly the residue. *(.tex §4; memory
  `oml_relational_prob_novelty.md`.)* The
  directed-context⟹non-distributivity *idea* is NOT new (it's the shape of
  Bohrification and Gunji et al.'s colimit generation); novelty lives
  entirely in the σ-additive-point-free-native combination.

> **Checkpoint 4.** Name the three blocked routes and the one-line reason
> each dies. Why is "concrete" the load-bearing qualifier in the
> no-impossibility claim? What single property does each prior-art
> construction give up?

---

## 5. Your first move

The work is **purely non-computational mathematics** from here — every
`.py` is finitary because the finitary part is the whole computable
boundary; the residue has no LP to run. Two branches, sharing one wall:

- **(a) The deep unlock — the σ-OML duality (descent axis).** Build the
  Loomis–Sikorski-type representation / countable-join-preserving σ-Stone
  duality for a concrete non-Boolean infinite σ-OML, or prove none exists.
  High ceiling, **no current foothold**.
- **(b) The tractable special case — the singular sliver.** Does a
  *singular* orthoadditive state on `L(H)` extend to a charge on
  `S₀(L(H))`? A concrete operator-algebra question (Calkin, Bunce–Wright,
  Takesaki) about one lattice. **Conditionally** self-contained.

**Do (b) first — it is informative either way.** If a singular state fails
to extend, then *no* state on `L(H)` extends, closing the PR_dual
"does-descent-do-independent-work" question negatively. If one *does*
extend, it is the first concrete object that extends but may not
concentrate — handing branch (a) its motivating example. *(.tex §5.)*

> **THE HINGE THAT GATES (b) — settle this first of all.**
> Is the singular-extension obstruction reached with a **finite** or a
> **countable** meet-zero family? This is **OPEN** — and it decides
> whether (b) is genuinely the easier branch.
> - The normal-state kill is finitary (lines in a 2-plane) and so dodges
>   the σ-wall. For singular states the relevant families are
>   *infinite-dimensional* subspaces with trivial intersection, so that
>   *line*-clustering route is **vacuous** (`s(e)=0` on all finite-dim `e`).
> - **But "the line route is vacuous" is NOT "the obstruction is
>   countable."** A *finite* family of infinite-dimensional pairwise-
>   meet-zero subspaces with `Σ s(aᵢ) > 1` is **unanalyzed**. If such a
>   finite obstruction exists, (b) is a self-contained operator-algebra
>   problem you can settle ahead of (a). If only a countable family
>   obstructs, (b) is entangled with the same finitary-to-σ bridge as (a)
>   and the tractability advantage evaporates.
> - *(Honesty note: a 2026-06-04 claim that this was "settled = infinitary,
>   both branches gate on the σ-wall" was an over-read of
>   `lh_singular_dichotomy.md` — that file calls the extension question
>   OPEN. No new mathematics settled it. It is still open. This is exactly
>   the kind of blocked-routes-≠-impossible slip the thread guards against
>   for residue #2; don't repeat it.)*

**Concretely, the very first thing to try:** take a *finite* family of
infinite-dimensional, pairwise-trivially-intersecting subspaces of `H`
and ask whether orthoadditivity of a singular state forces `Σ s > 1`
(finite obstruction) or whether singular states evade every finite bound
(pushing the obstruction to countable). That single computation/argument
decides the branch. *(Setup: `verification/lh_singular_dichotomy.md`
lines 95–108 give the singular-state constructions and the open statement.)*

> **Checkpoint 5.** State the finite-vs-countable hinge and what each
> outcome implies for branch (b). Why is (b) informative whether or not
> the singular state extends? What is the first concrete object to write
> down?

---

## Methodological reminders (the thread's hard-won rules)

- **Verify by building + reading the source**, not by grep or
  recollection. The session that produced this thread caught its central
  error (the (A)/(B) equivocation) and corrected a literature guess (HLS
  is σ-additive, not finite) only by reading primary sources in full.
- **Weaken "settled/strict/resolves" to "open/separation/conditional"**
  unless *both* directions are checked. The infinitary over-read above is
  the canonical cautionary case.
- **Blocked routes ≠ impossible.** Keep saying it.
- **Audit before drafting.** No LaTeX for unaudited claims.
