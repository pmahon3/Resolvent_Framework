/-
# σ-essential conjectures — stress-testing candidate solutions

Uses the open-core scaffold to TRIAGE conjectured solutions before hand-investment.
A conjecture's claimed ingredients become hypotheses; we ask Lean whether they
entail a witness (sufficiency), whether they are jointly consistent (no `→ False`),
and whether the proof smuggles the answer (`#print axioms` receipt).

This decides NO open mathematics. It checks the *internal logic* of a proposed
construction: does the idea, as stated, even reach the goal — and what's the gap?

## How to read a conjecture below
* `Ingredient` hypotheses = what the conjecture CLAIMS (open or to-be-built).
* If a theorem CLOSES `ingredients → WitnessAt`: the ingredients suffice (the carrier
  is still to be built by hand; sufficiency ≠ existence).
* If it STALLS: the remaining goal is the precise missing lemma.
* If `costume_kills_witness` fires (an ingredient entails `IntersectionClosed`): the
  conjecture is a costume — dead, mechanically.
-/
import QuerySystem.SigmaEssentialOpenCore

open Set MeasurableSpace
namespace SigmaEssential.Conjectures
open SigmaEssential SigmaEssential.OpenCore

variable {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d)

/-! ## §1. The intrinsic-𝒦 conjecture (taxonomy `open.intrinsic_K`)

CLAIM: a carrier 𝒦 with (a) generators, (b) closed under complement + countable
disjoint union, (c) the forbidden finite intersections `(S∩S')×{0} ∉ 𝒦` — yields a
witness. The non-distributivity is supposed to live in (c): the carrier is NOT
intersection-closed.

We formalize the claimed ingredients. The decisive structural ingredient is exactly
the NEGATION of intersection-closure (that is what "(c) forbidden intersections"
means, and what `rem:segregated`/Gleason force any witness carrier to satisfy). -/

/-- The intrinsic-𝒦 ingredients, as a record of claimed hypotheses. None is proved;
each is what the conjecture must deliver. -/
structure IntrinsicK where
  /-- (c) the carrier is NOT intersection-closed for the pattern — the non-distributive
      core. (Forced on any witness by `witness_not_intersection_closed`; here it is a
      *claimed* ingredient of the construction.) -/
  notIntersectionClosed : ¬ IntersectionClosed s₀ B
  /-- (i) clause (i) is arranged: no Dirac extends. -/
  kernelEmpty : kernel s₀ B = ∅
  /-- (ii) wall A: no non-Dirac state extends. THE open core — the conjecture must
      supply this; it cannot be proved. Stated as a hypothesis, honestly open. -/
  wallA : WallA s₀ B

/-- **Sufficiency check (PROVED).** The intrinsic-𝒦 ingredients DO entail a witness.
So the conjecture is *internally sufficient*: if a carrier delivers (i)+(ii)+(¬closed),
it is a witness. This tells us the construction's TARGET is correctly specified —
the whole burden is `wallA` (clause (ii)), exactly as the taxonomy says. -/
theorem intrinsicK_suffices (h : IntrinsicK s₀ B) : WitnessAt s₀ B :=
  (witness_iff_kernel_empty_and_wallA s₀ B).mpr ⟨h.kernelEmpty, h.wallA⟩

/-- **Consistency check (PROVED).** The ingredients are NOT jointly contradictory:
the `¬IntersectionClosed` ingredient is *consistent with* (indeed forced by) being a
witness — it does not collide with (i)+(ii). Formally: from the ingredients we derive
a witness, and a witness refutes `IntersectionClosed`, matching ingredient (c). So the
construction does not self-destruct (unlike a costume). -/
theorem intrinsicK_consistent (h : IntrinsicK s₀ B) :
    ¬ IntersectionClosed s₀ B :=
  witness_not_intersection_closed s₀ B (intrinsicK_suffices s₀ B h)

/-- **The gap, stated precisely.** Stripping the freely-arrangeable (i) and the
structural (c), the entire open content of intrinsic-𝒦 is `WallA` (clause (ii)).
The conjecture reduces the construction to *exactly* the open core — no more, no less.
This is the investigative payoff: intrinsic-𝒦 is well-posed and gap = wall A. -/
theorem intrinsicK_gap_is_wallA (h : IntrinsicK s₀ B) : WallA s₀ B := h.wallA

/-! ## §1b. CANDIDATE SHAPE — atomless blocks on an uncountable carrier (2026-06-26)

First specified candidate for intrinsic-𝒦 (disciplined "attack #1"). Motivation: the
band family died via `BandClosure.forces_boolean`, which requires BOTH `[Countable Ω]`
AND "every singleton ∈ closure" — σ-additivity over the countable disjoint union of
singletons then determines the state by points. A candidate dodges this iff it negates
BOTH hypotheses.

**Definite closure rule:** blocks = copies of a fixed **atomless** Boolean σ-algebra
(e.g. a measure algebra), glued along incompatible (non-orthogonal, non-trivial)
overlaps; carrier `Ω` uncountable; the cells are atomless, so **no singletons lie in
`L`**. Distinguishing claims (what makes it not-the-band):
- `uncountableCarrier`: `Ω` is uncountable (negates `forces_boolean`'s `[Countable Ω]`)
- `noSingletons`: no singleton `{ω}` is in `d` (negates the singleton hypothesis)

These are the ONLY new content vs the band; they target exactly the two hooks of the
certified band death. This section records the candidate + the provable fact that it
avoids the band mechanism. It does NOT discharge wall A (the open core). -/

/-- The atomless-block candidate's distinguishing properties (what differentiates it
from the dead band family). Claimed of the carrier, not yet constructed. -/
structure AtomlessBlockCandidate {Ω : Type*} (d : DynkinSystem Ω) : Prop where
  /-- the carrier is uncountable (negates `forces_boolean`'s `[Countable Ω]`) -/
  uncountableCarrier : ¬ Countable Ω
  /-- no singleton lies in the carrier (negates the singleton hypothesis of the band
      death; the blocks are atomless) -/
  noSingletons : ∀ ω : Ω, ¬ d.Has {ω}

/-- **Triage fact (PROVED).** The atomless-block candidate avoids the band-death
mechanism by construction: it has neither hook (`[Countable Ω]`, singletons-in-`L`)
that `BandClosure.forces_boolean` needs. So the band dichotomy does NOT kill it — the
first candidate to clear that gate with a *specific structural reason*, not a hope. -/
theorem atomlessBlock_evades_band_death {Ω : Type*} {d : DynkinSystem Ω}
    (h : AtomlessBlockCandidate d) :
    (¬ Countable Ω) ∧ (∀ ω : Ω, ¬ d.Has {ω}) :=
  ⟨h.uncountableCarrier, h.noSingletons⟩

/-! The candidate clears band-death triage. It does NOT clear wall A (open core).

**⚠ ADVERSARIAL CHECK (2026-06-26) — the DW boundary kills the TRACTABLE instantiation
and sharpens the escape.** If the blocks are measure algebras of Polish spaces (e.g.
Borel[0,1] mod null), the block IS Polish-representable (Ω Polish, σ-class = Borel,
inner-regular = Derr–Williamson D.6 hypotheses). A *countable* gluing of Polish-
representable blocks stays Polish-representable (countable ops preserve standard-Borel)
⟹ **DW D.6 kills it (no σ-essential witness).** So atomlessness alone does NOT escape:
the escape is FORCED to be an **uncountable** gluing producing a **non-Polish-
representable** carrier. (This was a listed profile requirement; the check shows it is
*forced by DW*, not optional.)

The brutal core surfaced from the construction side: the candidate is **buildable
exactly where it is DW-dead** (Polish blocks, countable gluing) and **alive only where
it is non-Polish-representable** = non-standard-Borel = resists explicit construction.
Same wall, reached constructively. NEXT (if pursued): a non-Polish gluing — but that is
the unbuildable regime; honest status is "candidate sharpened + bounded, no buildable
instantiation". -/

/-! ## §1c. The POLARITY check — "builds a state ⟹ rescuer, not witness" (2026-06-26)

The harness's costume-detector (§3) checks the *disjointification* axis but has a
BLIND SPOT: it does not catch the **polarity** failure mode — a candidate that
"constructs a witness" by exhibiting a global STATE. A witness is the NON-existence of
an extension (`IsSigmaEssential = ¬∃ s, Extends s s₀ B`); any constructed global state
extending `s₀` is therefore a *rescuer* that REFUTES the witness. This fired three
times this session (Navara–Pták's `m`; the bare-form mis-encoding; the `U↾L`
large-cardinal channel). It is a clean impossibility — record it as the polarity gate. -/

/-- **Polarity gate (PROVED).** If a candidate produces ANY global state `s` extending
`s₀` on `B`, then `s₀` is NOT σ-essential. So "build a state to witness it" is
self-defeating: a state is an extension, and a witness forbids all extensions.
Use as the polarity check — a construction that yields a global state has produced a
rescuer, not a witness. -/
theorem builds_state_implies_not_witness
    {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d)
    (s : TwoValuedState d) (hext : Extends s s₀ B) :
    ¬ IsSigmaEssential s₀ B :=
  fun hess => hess ⟨s, hext⟩

/-- **Corollary — the large-cardinal-ultrafilter trap, abstractly.** Reading a state
off any global object (e.g. `U↾L` for an ultrafilter `U`) gives an extension, hence
no witness. The lemma is `builds_state_implies_not_witness` applied to that state;
stated separately to name the trap: a large-cardinal ultrafilter is inherently
GLOBAL, so "U supplies the witness's state" always rescues. "Direct construction from
U" must instead mean **U builds the CARRIER** (Ω uncountable/non-Polish), with
non-extendability emerging structurally from `L`, `U` never read as a state. -/
theorem ultrafilter_as_state_is_rescuer
    {Ω : Type*} {d : DynkinSystem Ω} (s₀ : TwoValuedState d) (B : Block d)
    (uState : TwoValuedState d) (huext : Extends uState s₀ B) :
    ¬ IsSigmaEssential s₀ B :=
  builds_state_implies_not_witness s₀ B uState huext

/-! ## §2. Detector validation — re-run COVERED (killed) items, expect death

A trustworthy detector must re-kill what is already dead. We replay two covered
carriers whose recorded death is "∪/∩-closure ⟹ Boolean" and confirm the formal
detector fires. -/

/-- **`band_family` re-killed (taxonomy `carrier.band_family`, DEAD).** Its recorded
death: "∪-closed ⟹ Boolean". The ∪-closed regime's defining property entails the
intersection-closure the detector tests, so the detector fires: no witness. We model
the band-family's fatal hypothesis as `IntersectionClosed` (its ∪-closed-⟹-Boolean
horn) and confirm death. -/
theorem band_family_dead (hBand : IntersectionClosed s₀ B) : ¬ WitnessAt s₀ B :=
  costume_kills_witness s₀ B hBand

/-- **`selection_first` re-killed (taxonomy `costume.selection_first`, 6th costume).**
Recorded death: "coherence conditions ARE closure conditions (BandClosure.lean); the
selection dies the same collapse." Its closure condition entails intersection-closure,
so the detector fires. Same mechanism, different dress — exactly "6th costume". -/
theorem selection_first_dead (hClosure : IntersectionClosed s₀ B) : ¬ WitnessAt s₀ B :=
  costume_kills_witness s₀ B hClosure

/-- **`embedding_transport` re-killed (taxonomy `costume.embedding_transport`, #8,
FORBIDDEN).** Recorded: transporting `U` onto orthogonal-only closure "bottoms out at
the same identity". The transport's success would require the carrier to be
intersection-closed (so `U`'s κ-completeness, stated via intersections, applies) —
which the detector kills. Confirms #8 is a costume without ever building it. -/
theorem embedding_transport_dead (hTransport : IntersectionClosed s₀ B) :
    ¬ WitnessAt s₀ B :=
  costume_kills_witness s₀ B hTransport

/-! ## §3. The contrast that makes the detector meaningful

intrinsic-𝒦 (§1) supplies `¬ IntersectionClosed` — the detector does NOT fire, the
conjecture survives triage. The three covered items (§2) supply `IntersectionClosed`
— the detector DOES fire, they die. Same theorem (`costume_kills_witness`); the
discriminator is whether the conjecture's ingredients include intersection-closure.
That is the formal content of "is this a costume?". -/

/-- The detector's discriminating principle, stated once: a conjecture is a costume
**iff** its ingredients force intersection-closure. Survivors (like intrinsic-𝒦) must
supply `¬ IntersectionClosed`; that is necessary (witnesses fail closure) but NOT
sufficient (clause (ii) still open). -/
theorem costume_discriminator :
    (IntersectionClosed s₀ B → ¬ WitnessAt s₀ B) ∧
    (WitnessAt s₀ B → ¬ IntersectionClosed s₀ B) :=
  ⟨costume_kills_witness s₀ B, witness_not_intersection_closed s₀ B⟩

end SigmaEssential.Conjectures
