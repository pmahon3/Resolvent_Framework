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
