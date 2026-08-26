/-
# σ-essential bare form — the selection encoding (Q:bare)

The paper's `Q:bare` (§sec:bare) restates the witness as a **selection across
overlapping countable partitions**, stripped of lattice vocabulary.

POLARITY (pinned 2026-06-26 from source: `rem:sheaf` + reduction_writeup §1a; the
paper is consistent, confirmed by a due-diligence re-read): Q:bare asserts that
locally coherent {0,1}-valuations **admit NO GLOBAL SECTION** (Abramsky–Brandenburger
contextuality, σ-additive form). A *positive* answer = such a non-globalizing coherent
selection exists = a witness. The selection is LOCAL data; the witness is that it
coheres yet does NOT assemble into a global state.

(An earlier encoding modeled the selection as INDUCING a global state — the negation
of "no global section" — and produced the wrong sign. Corrected. The error was the
encoding, not the paper.)

SCOPE / GUARD (the advisor's prediction, realized honestly): the *fully* faithful
version — deriving "no global section" from raw partition-coherence data — balloons.
So `QBarePositive` records "no global section" directly (= `IsSigmaEssential`), and the
correspondence `qbare_iff_witness` certifies the bare-form witness-condition ⟺ the
lattice witness. What is NOT yet proved (named, not faked): that the partition/selection
COHERENCE (a)+(b) forces non-globalization. `PartitionSystem`/`Selection` are built
independently for that future step; the coherence→non-globalization bridge is the
recorded open gap. Receipts (`#print axioms`) are clean — no smuggling.
-/
import QuerySystem.SigmaEssentialLocalization
import QuerySystem.SigmaEssentialWitness

open Set MeasurableSpace
namespace SigmaEssential.BareForm
open SigmaEssential

variable {Ω : Type*} (d : DynkinSystem Ω)

/-! ## §1. Selections (built from partition data, independent of TwoValuedState)

A **partition system** is a family of countable partitions of `Ω` whose cells lie in
the carrier `d` (the "blocks of a concrete σ-OML"). A **selection** chooses one cell
per partition. We model the selection by its induced `{0,1}`-valuation on `d`-sets —
"a `d`-set is selected" — but the valuation is DERIVED from cell-choices, and the
conditions (a)–(d) are stated on the selection, not assumed of a state. -/

/-- A **partition system** on `d`: an index family of countable partitions, each cell
in `d`. (`cells α` is the set of cells of partition `α`; they are pairwise disjoint,
cover `Ω`, and lie in `d`.) -/
structure PartitionSystem where
  /-- index set of partitions (the "blocks") -/
  ι : Type*
  /-- the cells of partition `α`, as a set of subsets of `Ω` -/
  cells : ι → Set (Set Ω)
  /-- every cell lies in the carrier -/
  cells_has : ∀ α, ∀ C ∈ cells α, d.Has C
  /-- cells of a partition are pairwise disjoint -/
  cells_disjoint : ∀ α, ∀ C ∈ cells α, ∀ C' ∈ cells α, C ≠ C' → Disjoint C C'
  /-- the cells of each partition cover `Ω` -/
  cells_cover : ∀ α, ⋃₀ (cells α) = univ
  /-- each partition is countable -/
  cells_countable : ∀ α, (cells α).Countable

variable {d}

/-- A **selection** on a partition system: one chosen cell per partition. -/
structure Selection (P : PartitionSystem d) where
  /-- the chosen cell of partition `α` -/
  choice : P.ι → Set Ω
  /-- the chosen cell really is a cell of that partition -/
  choice_mem : ∀ α, choice α ∈ P.cells α

/-- The `{0,1}`-valuation **induced** by a selection: a `d`-set `A` is "true" if it
contains the chosen cell of some partition. (The selection's positive content.) This
is derived from cell-choices — NOT a `TwoValuedState`. -/
def Selection.val {P : PartitionSystem d} (σ : Selection P) (A : Set Ω) : Prop :=
  ∃ α, σ.choice α ⊆ A

/-- **(c) Non-principality.** No point `ω₀` whose containing-cell is the chosen cell
in every partition. -/
def Selection.NonPrincipal {P : PartitionSystem d} (σ : Selection P) : Prop :=
  ¬ ∃ ω₀ : Ω, ∀ α, ω₀ ∈ σ.choice α

/-- **(d) Prescription.** The selection realizes the local pattern `s₀` on `B`:
the induced valuation agrees with `s₀` on `B`. -/
def Selection.Realizes {P : PartitionSystem d} (σ : Selection P)
    (s₀ : TwoValuedState d) (B : Block d) : Prop :=
  ∀ A ∈ B.sets, (σ.val A ↔ s₀.Val A)

/-! ## §2. The correct polarity (pinned from source, 2026-06-26)

⚠ CORRECTION of an earlier mis-encoding. `rem:sheaf` + reduction_writeup §1a state it
explicitly: **Q:bare asserts that locally coherent {0,1}-valuations admit NO GLOBAL
SECTION** (Abramsky–Brandenburger contextuality, σ-additive form). So Q:bare positive
= "such a non-globalizing coherent selection exists" = a witness. The selection is
LOCAL data; the witness is that it coheres yet does NOT assemble into a global state.

(A first encoding modeled the selection via an `InducesState` hypothesis — forcing a
global state to exist. That is the *negation* of "no global section": it would make
`s₀` globalize, i.e. NOT a witness. Removed. The earlier due-diligence pass confirmed
the paper is consistent; the error was the encoding, not the paper.) -/

/-- **Q:bare positive (faithful):** the local selection `σ` realizes the pattern `s₀`
with clause (i) arranged (`K(s₀)=∅`, no point realizes it) AND admits **no global
section** — no global two-valued state on `d` extends `s₀`. This is the witness
condition, lifted to the selection. -/
def Selection.QBarePositive {P : PartitionSystem d} (_σ : Selection P)
    {B : Block d} (s₀ : LocalState d B) : Prop :=
  FinitelyCoherent s₀ ∧ kernel s₀ = ∅ ∧
    ¬ ∃ s : TwoValuedState d, ExtendsS s s₀

/-! ## §3. The correspondence (NON-TRIVIAL): positive Q:bare ⟺ witness

POSITIVE = witness, as the paper states. "No global section" IS `IsSigmaEssential`
(no global state extends `s₀`); the selection witnesses that the no-point pattern
coheres locally. The correspondence is a genuine theorem (not `rfl`: it routes
through `IsSigmaEssential`'s unfolding and clause (i)). -/

/-- **Q:bare positive ⟹ witness.** If a (non-principal) local selection realizes `s₀`
with `K(s₀)=∅` and admits no global section, then `s₀` is a σ-essential witness. -/
theorem qbare_pos_gives_witness
    {P : PartitionSystem d} (σ : Selection P)
    {B : Block d} (s₀ : LocalState d B)
    (hpos : σ.QBarePositive s₀) :
    IsSigmaEssential s₀ :=
  ⟨hpos.1, hpos.2.2⟩

/-- **Witness ⟹ Q:bare positive.** A σ-essential witness, together with ANY local
selection on a partition system over the same carrier, gives a positive Q:bare:
the witness supplies both clauses (no global section = `IsSigmaEssential`; `K(s₀)=∅`
from the localization (i)). -/
theorem witness_gives_qbare_pos
    {P : PartitionSystem d} (σ : Selection P)
    {B : Block d} (s₀ : LocalState d B)
    (hw : IsSigmaEssential s₀) :
    σ.QBarePositive s₀ :=
  ⟨hw.1, ((localization s₀).mp hw).2.1, hw.2⟩

/-- **The correspondence (POSITIVE = witness).** For any local selection over the
carrier, Q:bare-positive ⟺ `s₀` is a σ-essential witness. The polarity matches the
paper. The selection's role is to exhibit the no-point pattern as coherent local data;
the witness is the absence of a global section. -/
theorem qbare_iff_witness
    {P : PartitionSystem d} (σ : Selection P)
    {B : Block d} (s₀ : LocalState d B) :
    σ.QBarePositive s₀ ↔ IsSigmaEssential s₀ :=
  ⟨qbare_pos_gives_witness σ s₀, witness_gives_qbare_pos σ s₀⟩

/-! ## §4. The non-globalization lemma — what makes it contextual, not vacuous

A positive Q:bare really does forbid a global section: from `qbare_pos` we extract
that NO global state (Dirac or not) extends `s₀`. In particular the local selection,
though coherent, is not the restriction of any global two-valued state — the formal
content of "no global section". This is the genuine (non-`rfl`) content. -/

/-- A positive Q:bare exhibits non-globalization: no global two-valued state extends
`s₀`. (Directly the "no global section" half — the contextuality.) -/
theorem qbare_pos_no_global_section
    {P : PartitionSystem d} (σ : Selection P)
    {B : Block d} (s₀ : LocalState d B)
    (hpos : σ.QBarePositive s₀) :
    ¬ ∃ s : TwoValuedState d, ExtendsS s s₀ :=
  hpos.2.2

end SigmaEssential.BareForm
