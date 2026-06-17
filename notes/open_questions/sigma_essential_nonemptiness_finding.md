# σ-essential contextuality: non-emptiness routing verdict — **GAP**

*Subsession finding, 2026-06-12. Answers the one question of
`subsession_sigma_essential_via_CE.md` via the CE/Stone machinery. This is a
ROUTING verdict (which exit the investigation takes), not a construction or a
proof. Continues `reading1_prize_reduction.md`.*

> **VERDICT: GAP.** CE does **not** settle whether σ-essential contextuality can
> occur. The Boolean CE/Stone argument that killed `∏ₙMO₂` ("σ-additive ⟹
> concentration on principal points ⟹ non-contextual") **provably does not
> transfer** to the non-distributive case: it controls only the Boolean *center*
> of a concrete σ-complete OML and is *vacuous* off-center. So EMPTY is
> unestablished (the impossibility tool has no content where a witness would
> live), and no positive consistency argument was found either, so NON-EMPTY is
> unestablished. The durable payload is the **named break-point** and the
> **sharpened Exit-A target**: a witness must put its infinitary structure
> *off-center* (irreducible / non-central-infinite), which a product of finite
> blocks like `∏ₙMO₂` structurally cannot do.

---

## The pivot (sub-question 1): does contextuality localize to the center? **No — the argument does, the contextuality need not.**

The brief's load-bearing pivot was whether a concrete σ-complete OML's
contextuality must localize to its Boolean center (where CE/Stone kills it), or
whether off-center non-distributive structure can carry σ-essential contextuality
the center misses. The answer, traced through the actual CE machinery rather than
assumed, is that **the Stone argument localizes to the center, but contextuality
does not** — and that mismatch is exactly the gap.

### The two CE routes point opposite ways once you leave Boolean

- **Carathéodory / non-derivability route** (Łoś + finite-cofinite) delivers a
  *negative* result: finite consistency does not force σ-additivity. It never
  produces "σ-additive ⟹ non-contextual." **It cannot support EMPTY at all.**
- **Stone / support route** is the *only* one that could carry EMPTY. Its
  mechanism: σ-additivity + compactness ⟹ the measure concentrates on the
  **principal ultrafilters** ⟹ non-contextual. The hidden equality that makes the
  final arrow work is the triple identity

  > **principal ultrafilter = atom of the algebra = dispersion-free state**,

  which holds **only in a Boolean algebra**. This is precisely one of the
  three-point-space conflations the brief flagged (center vs. P(A) vs.
  dispersion-free states are three different objects).

### The exact non-distributive step where the Boolean argument breaks

Let `w` be a σ-additive state on a concrete σ-complete OML `L`. Two standard,
load-bearing facts (named, not re-proved here):

- **Center.** `Z(L)` is a Boolean sub-σ-algebra of `L`, and `w` restricts to
  `w|Z(L)` as a σ-additive Boolean measure. *Over the center, the Stone argument
  applies:* `w|Z(L)` concentrates on the **atoms of `Z(L)`**.
- **Concreteness.** Concrete ⟺ a *separating* (Zierler–Gudder set-representable),
  **not** necessarily *spanning*, family of dispersion-free states. Dispersion-free
  states are abundant enough to separate points; the open question is whether they
  *span* the state space. (Wright's pentagon already shows they need not — a
  finite, finitely-witnessed counterexample.)

The break is then sharp:

> **An atom of `Z(L)` is not a dispersion-free state of `L`.** A central atom can
> subtend an entire non-Boolean block; a σ-additive state concentrated on that
> atom can still be contextual *within the block*. "Concentration on principal
> points" controls the center and says **nothing** about whether `w` lies in the
> hull of `L`'s dispersion-free states.

The first implication (σ-additive ⟹ concentration on central atoms) transfers;
the second (concentration ⟹ non-contextual) does **not**. It was Boolean-specific
because only in a Boolean algebra do center-atoms exhaust the dispersion-free
states.

### The degenerate witness of the break: trivial center ⟹ the argument is *empty*

Push to the extreme. If `L` is **irreducible** (`Z(L) = {0,1}`), the Stone/center
argument says only `w(1) = 1` — **zero content**. It places no constraint
whatsoever on how `w` distributes over the non-Boolean structure. So for an
irreducible σ-complete OML the entire Boolean killing-mechanism *evaporates*. The
Boolean argument's content lives in the center; where the center is trivial, the
content is nil. That is the cleanest possible demonstration that the transfer
fails.

(**Trap, not slid past:** `L(H)` is irreducible and σ-complete but **not
concrete** — by Kochen–Specker it has *no* dispersion-free states, so its
dispersion-free hull is empty and "contextual" there is a degenerate vacuity, a
different phenomenon. `L(H)` establishes only that *irreducible σ-complete OMLs
exist*; it is **not** a witness candidate. The witness needs irreducible /
non-central-infinite **AND concrete AND σ-complete** — and the existence of that
conjunction is exactly the open Exit-A target.)

---

## Why ∏ₙMO₂ confirms GAP rather than EMPTY (sub-question 1, finished)

`∏ₙMO₂` fails to be σ-essential **not** because σ kills all OML contextuality, but
because **all of its infinitary structure is central.** Each `MO₂` factor is
finite and irreducible; the only place infinitary behaviour can live is the
Boolean center `P(ℕ)` — exactly where Stone *does* kill it (diffuse
finitely-additive states → σ-additivity forces atomicity → concentration on
singletons = principal ultrafilters → non-contextual). That is a structural
feature of a **product of finite blocks**, not an impossibility theorem. It tells
you where a witness would have to live, and sharpens the target:

> A witness must be an **irreducible (trivial-center) — or at least
> non-central-infinite — σ-complete concrete OML** with genuinely infinite
> non-Boolean structure. A product of finite blocks can never supply this: its
> infinitary content is forced into the center, into Stone's reach. `∏ₙMO₂`'s
> failure **sharpens** Exit A; it does not close it.

---

## Sub-questions 2 and 3 (briefly, consistent with GAP)

- **(2) Non-derivability transfer.** Establishing NON-EMPTY would route through
  this: does CE's non-derivability (a Boolean/first-order result) have an OML
  analogue that *positively permits* a σ-essential witness as a
  consistent-but-not-finitely-constructible existence? That is unestablished here.
  "No obstruction found" is GAP, **not** NON-EMPTY — NON-EMPTY needs a positive
  consistency/witness argument this subsession does not have.
- **(3) Wright in the limit.** A σ-orthocomplete countable paste of Wright-type
  blocks whose finite sublogics stay non-contextual but whose σ-join forces
  contextuality is the *plausible* Exit-A shape, and the break-point above shows CE
  raises **no objection** to it off-center. But "CE does not forbid it" is again
  GAP, not a permission to assert it occurs.

---

## Back-door EMPTY: closed (PP1994)

One last check that GAP is honest and not hiding a boring EMPTY. **Pták–Pulmannová
1994**: an OML is Boolean iff it carries a unital set of *subadditive* measures —
the forcing property is **subadditivity**, not σ-additivity. So **σ-additivity
alone does not collapse a non-Boolean OML to Boolean.** Were it otherwise, the
question would be empty for the trivial reason (no genuinely non-Boolean
σ-additive states to begin with). It is not. The non-Boolean σ-additive layer
genuinely exists; whether contextuality survives in it σ-essentially is the open
matter.

---

## Routing payload (the durable result — what the next subsession inherits)

1. **EMPTY is not provable with the current instrument.** Stone-over-center is the
   *wrong tool off-center* — it is vacuous exactly where a witness would live. An
   impossibility proof (Exit B) cannot reuse the ∏ₙMO₂ mechanism; it needs a
   **genuinely different finite-witnessing argument** showing every σ-additive
   contextual state on a concrete σ-complete OML is already contextual on a finite
   sub-OML. No such mechanism is in hand.
2. **Exit A's target is sharpened.** Not just "infinite concrete σ-complete OML
   with a contextual σ-additive state," but one whose **infinitary structure is
   off-center** (irreducible or non-central-infinite). Products of finite blocks
   are excluded a priori. Pasting constructions (sub-question 3) are the natural
   place to look, and CE does not obstruct them.
3. **Verdict: GAP.** CE locates and explains the ∏ₙMO₂ death but does not
   generalize it. The investigation stays at the win/kill fork; neither exit is
   foreclosed, and the off-center requirement is the new constraint on both.

## Pointers
- The question: `subsession_sigma_essential_via_CE.md` ("## The one question").
- The reduction: `reading1_prize_reduction.md` (relational ⟺ contextual; σ
  load-bearing; the ∏ₙMO₂ center/diffuse computation; the Wright 1978 bound).
- CE machinery: `programme/program_overview.md` §"Paper I" (Carathéodory +
  Stone routes, the non-derivability metatheorem).
- Center / set-representability standard facts: OML center theory; Zierler–Gudder
  concrete ⟺ separating dispersion-free states.
- Related: [[reading1_prize_reduction]], [[oml_descent_inhabitation]],
  [[oml_two_point_spaces]] (the three-point-space distinction this verdict
  depends on), [[direction2_gate_finding]].

---

## Update 2026-06-17 — the GAP/off-center routing was right; now made precise

This note's verdict (CE can't settle non-emptiness; the witness must put its
infinitary structure **off-center**, products of finite blocks excluded, pasting the
place to look) was the correct routing. The 2026-06-17 push made it precise (full
record: `[[sigma_essential_construction_attempt]]` memory):

- "Off-center / infinitary / not products of finite blocks" sharpens to the proved
  **necessary condition**: any witness needs **uncountably many infinite atomic
  blocks**, because `S_df^σ(L) = S_df ∩ ⋂_{block B} O_B` is `G_δ` (⟹ Exit B) as soon
  as there are ≤ℵ₀ atomic blocks. "Pasting" = exactly building the uncountable block
  family.
- The single live construction target is **(B)**: uncountably many atomic blocks on a
  countable ground set ℕ (|L| = 𝔠). The "one non-atomic block" shortcut is **struck**
  (Boolean ⟹ reducible + distributive ⟹ fails irreducible + non-Boolean).
- CE-reconnection confirmed at the **measure** level (not lattice): the leak is "can a
  representing μ dodge an uncountable union of fake-sets on `S_df`," a
  strictly-positive-measure question — same flavour as Strategy D's measure axis.
