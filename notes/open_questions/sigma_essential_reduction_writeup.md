# The σ-essential contextual witness reduces to σ-point-selection

*Standalone writeup, 2026-06-25. For understanding and record (not submission). This
consolidates the scattered ledger material into one coherent statement. The terse
working record is `CHARTED_sigma_essential.md`; the result-with-corrections is
[[sigma_essential_reduction_result]]; the forcing-context post-mortem is
[[forcing_programme_status]]. ⟦HAND throughout — verified at sketch level + advisor-
checked; not Lean-formalized, not refereed.⟧*

---

## 0. The question

Is there a **concrete σ-essential contextual witness**: a concrete σ-complete
non-Boolean off-center orthomodular lattice `L ⊆ P(Ω)` (orthocomplement =
set-complement, joins of orthogonal elements = disjoint unions) carrying a finite
sub-orthoposet `B ⊆ L` and a 2-valued state `s₀` on `B` that extends to **no** global
σ-additive 2-valued state on `L`?

Motivation: this is the lattice-theoretic form of "a contextual probability assignment
witnessed by no finite sub-system but blocked at the σ-level" — the residue of the
OML-descent programme, and (independently) the same realization gap that parks Paper I.

## 1. The result

> **Reduction.** The existence of a concrete σ-essential witness is **equivalent to a
> σ-point-selection failure**: a locally coherent 2-valued pattern on `L` with no
> globally coherent σ-additive 2-valued **state** realizing it. Consequently its
> existence is neither *constructible* nor *refutable* in ZFC by any route attempted;
> it is **reducible** to this state-realization question. (Whether it carries
> *measurable-cardinal strength* is CONJECTURED, not established — see §5/§6: the
> strength claim rode the now-struck Blecher–Weaver weld; only the *refutation* side
> has independent evidence touching "no measurable cardinal.")

The reduction is the deliverable. The witness is neither built nor refuted; it is
*located* — pinned to a precise, named open wall.

## 2. Why (the mechanism)

A global σ-additive 2-valued state on `L ⊆ P(Ω)` is either a point-evaluation `δ_ω`
(always present) or a **non-Dirac** σ-state. A finite local `s₀` fails to extend iff:

(i) **no `δ_ω` realizes it** — i.e. `⋂{generators s₀ sends to 1} = ∅`. This is freely
    arrangeable: the Navara–Pták 1983 intersection device (`B∩C∩D=∅` on a concrete
    σ-class over ℚ²) makes it so for free; and

(ii) **no non-Dirac σ-state rescues it.**

Clause (ii) *is* the **σ-point-selection problem**: does a globally coherent σ-additive
2-valued state thread the locally-coherent constraints? Hence witness ⟺ (i) ∧ ¬(ii) ⟺
σ-point-selection fails. ⟦verified at sketch level — the genuine equivalence⟧

The Navara–Pták concentration criterion (their Thm 1: a 2-valued σ-measure is additive
iff concentrated at a point) is the engine of clause (i); their explicit example shows
clause (i) *alone* is not a witness, because they construct a non-Dirac σ-state through
the gap — i.e. their example *fails* clause (ii), which is exactly why the device alone
never suffices and the whole weight falls on σ-point-selection.

## 3. Three walls, kept distinct

The reduction's "bottom" is one of three distinct objects; conflating them was the
recurring error, so they are named separately:

| | wall | character | cardinal? |
|---|---|---|---|
| **A** | **σ-point-selection** | does a coherent local 2-valued pattern extend to a global σ-additive **state**? | CONJECTURED (the Ulam link via Blecher–Weaver is the Hilbert analogue, STRUCK as a transfer — §5; only the ¬-side has independent cardinal evidence) |
| **B** | **faithful-tribe-representability** | does `L` embed faithfully into a σ-tribe of *honest sets*? | — |
| **C** | **HW Problem 2** | does `L` embed into *some* σ-complete **OMP** `L̄` (not a tribe of sets, not concrete, not state-separating)? | no (plain ZFC) |

Established relations:

- **A is strictly above B.** ⟦charted, cited⟧ The Floor (`thm:floor`): a faithful
  tribe-of-sets representation forces distributivity ⟹ Boolean. Dvurečenskij σ-LS
  (J. Austral. Math. Soc. 68, 2000): every `L` admits only a σ-*epimorphic* (lossy,
  non-faithful) tribe image, which does **not** separate the 2-valued points — the
  "tribe-vs-points gap." RDP is needed and OMLs lack it (MO₂ is the standard witness).
- **C does not entail B.** ⟦HAND, 2026-06-25⟧ HW2's `L̄` may be a non-distributive
  *abstract* σ-OMP with no tribe-of-sets structure, so it sidesteps the Floor entirely.
  (One non-implication only — **not** mutual independence.)
- **A and C are ORTHOGONAL — a TYPE MISMATCH** ⟦HAND, self-checked, advisor-pass
  pending (advisor was down at recording)⟧. **The weld run (2026-06-25) resolves the
  A↔C relation: neither cross-implication holds, for a structural reason.**
  - *C-fails ⟹ A-fails: VACUOUS.* A's carrier is **already σ-complete** (C2 is a
    standing hypothesis; the witness is "concrete σ-**complete**"). C (does an OMP
    embed into *some* σ-complete OMP?) is **trivially YES** on A's carriers — they
    are their own σ-completion. So C-failure can only occur for *non*-σ-complete
    OMPs, which A's carrier class **excludes**. The two walls do not range over the
    same lattices.
  - *A-fails ⟹ C-fails: also fails.* A-failure is a **state** defect on an
    already-σ-complete `L`; it exhibits no OMP *lacking* a σ-completion. (`L` has one
    — itself.)
  - *Adversarial self-check (advisor down):* could A-failure secretly encode a
    completion failure of the **finite** sub-OMP `⟨B⟩`? No — `⟨B⟩` is finite, hence
    trivially σ-complete and σ-embeds into `L`; the defect is in the **state**, not
    the lattice. No hidden completion question inside A.
- **∴ HW Problem 2 (C) DROPS OUT of the picture.** It is not "the bottom," not
  "above," not "below" A — it is about a *different* phenomenon (lattice completion
  of non-σ-complete OMPs) than A (state realization on σ-complete OMLs). The earlier
  "the witness reduces to HW2 / σ-LS" framing welded two genuinely orthogonal walls.

So the bottom is **A (σ-point-selection) — full stop**, strictly above B, with C
removed as a red herring. A is a **state-realization** question on a fixed
σ-complete lattice; the reduction does NOT route through any lattice-completion
problem.

## 4. What it is and is not

- **Is:** a reduction of the σ-essential witness question to σ-point-selection (wall
  A), with A's location relative to B and C pinned. The honest, recorded form of "the
  wall is load-bearing."
- **Is not a proof the cell is empty (¬Ψ).** Blecher–Weaver: the *Hilbert* analogue —
  a singular σ-additive pure state on B(ℓ²(κ))'s projection lattice — **exists ⟺ κ is
  Ulam-measurable.** So ¬Ψ is not a ZFC theorem; the witness exists under a large
  cardinal in the Hilbert sector. The concrete sector is the open transfer.
- **Is not an independence proof.** That would need wall A turned into a clean
  independence-ready sentence (see [[forcing_programme_status]]); it is currently an
  open math problem, not an undecided sentence.

## 5. A bottleneck, not a convergence — ⚠ CORRECTED 2026-06-25 (hostile audit)

**An earlier draft of this section claimed "seven independent routes converge on
wall A" and treated that as a unification. A hostile audit BROKE that claim. The
honest finding is a BOTTLENECK, not a convergence — and a bottleneck is nearly
tautological once the core is named.** The corrected count:

- **Genuine independent reductions to wall A: ≈ 1.** The §2 equivalence (witness ⟺
  σ-point-selection) is the one real reduction.
- **Routes 4 (¬Ψ-lever), 5 (Con(Ψ) construction), 6 (template no-go) are ONE
  argument, three angles** — refute / build / bound the *same* clause-(ii) object.
  The ledger says so verbatim: "#28 and #29 are ONE theorem"; "one task, three
  exits." Not three confirmations; one fact viewed three ways.
- **Route 3 (Blecher–Weaver) does NOT reduce to wall A.** It is the *Hilbert* sector
  (pure states on `B(ℓ²(κ))`, non-concrete by KS); Akemann–Weaver's "no routing
  port" means the concrete 2-valued question does not factor through it. Listing it
  as a route to A is a THIRD HW2-style weld (cf. §3) — caught here, struck.
- **Routes 1 (catuṣkoṭi) and 2 (structural-reduction) are failed dissolutions**, not
  reductions ("4 obstacles dissolved on inspection"); route 2 has no ledger record.
- **Route 7 (weld run) is a map *subtraction*** (HW2 removed as orthogonal), not a
  reduction TO A.

**So the structural finding is:** σ-point-selection (wall A) is a **load-bearing
bottleneck** — every *complete* attack on the σ-essential witness question must
engage clause (ii) of §2 — NOT a Type-3 unification of separate areas (the
"convergence" buys no method-transfer; it says distinct directions stall on the same
missing fact). The §2 reduction stands; the seven-route gloss was inflation.

**What remains true and load-bearing:** the §2 equivalence (witness ⟺
σ-point-selection); wall A strictly above B (§3, cited); HW2 (C) orthogonal (§3, the
weld run). σ-point-selection for non-distributive concrete σ-OMLs is the genuine,
located, open object — reached by one reduction, not seven.

## 6. Primary sources

- Navara & Pták, *Two-valued measures on σ-classes*, Čas. Pěst. Mat. 108 (1983)
  225–229. (Template + concentration criterion; in the library.)
- Blecher & Weaver, *Quantum measurable cardinals*, arXiv:1607.08505 (JFA 272, 2017).
  (Hilbert-side Ulam-measurable dichotomy.)
- Dvurečenskij, σ-Loomis–Sikorski for RDP structures, J. Austral. Math. Soc. 68 (2000).
- Harding & Wang, *On some problems concerning… completions*, arXiv:2108.09819,
  Problem 2 (the embedding wall C; in the library).
- Derr & Williamson, arXiv:2302.03522, Thm D.6 (Polish-representable ⟹ no gap; the
  upper bound — any witness must be non-Polish).
- Akemann & Weaver, PNAS 105(14) (2008) (pure state on no masa — no routing port).

## 6. THE SWING — the boldest *true* target (2026-06-25)

After correcting §5, the honest fence:

> **CONJECTURE.** The existence of a concrete σ-essential witness is **independent of
> ZFC** — a new ZFC-independence phenomenon in quantum logic (concrete σ-OMLs).

**Strength is CONJECTURED, not assumed.** Discipline check (so the just-struck
Blecher–Weaver weld does not walk back in through the framing):
- **¬-side has independent evidence.** "No measurable cardinal ⟹ every σ-additive
  2-valued state on a concrete σ-OML is Dirac" is a direct structural fact about the
  *concrete* object — it does NOT route through B(H). So the *refutation* direction
  genuinely touches "no measurable cardinal." This is real, in-field evidence the
  object is independence-flavored.
- **Con-side strength is NOT independently established.** "Measurable cardinal
  *suffices* to build the witness" was entirely inherited from the B–W Hilbert
  analogy — which §5 STRUCK (no routing port). So the consistency direction, and its
  exact strength, is the open construction to be EARNED, not imported. Do not state
  "measurable-cardinal strength" as a premise.

**Two halves of the swing:** (Con) build a concrete σ-essential witness under *some*
large-cardinal hypothesis — genuinely new, in-field construction; (¬) prove no
witness in L — the ¬Ψ lever exists but stalled at the σ-class-vs-σ-algebra gap.

**STOP-CONDITION (pre-committed, before swinging):** if the construction's first
concrete step does NOT survive the σ-class-vs-σ-algebra gap that already stalled the
¬Ψ run, that is the signal the move is genuinely out-of-field — the honest output is
then **"independence-conjecture-with-evidence, recorded for a set-theorist,"** NOT an
nth run. This is where hubris and discipline coexist concretely: swing hard, with a
defined miss.
