# §2 Reduction — airtight verification log

*2026-06-25. Task 1 of the next-push: take the §2 reduction (witness ⟺
σ-point-selection) from ⟦self-checked⟧ to ⟦verified⟧, claim by claim. Discriminator
carried throughout (advisor): separate **genuine math gap** from **loose exposition**;
do NOT record a wording cleanup as a phantom mathematical correction.*

**Quantifier pinned (load-bearing for the whole reduction):** `B` is a **⊥-closed
finite sub-orthoposet** of `L` (NOT a generating set `F`). Settled in
`forcing_scout_sentence` (intrinsic-inherited local hull). Several claims below ride
on this; if ever loosened to a non-⊥-closed `F`, they must be revisited.

---

## Definitions (Claim 1 — VERIFIED ✓)
- **Concrete σ-OML** `L ⊆ P(Ω)`: contains ∅, Ω; closed under complement
  `A^⊥ = Ω∖A`; closed under countable **orthogonal** (pairwise-disjoint) unions.
  Order = ⊆. (= Gudder concrete logic = Navara–Pták σ-class, Def 1.)
- **σ-additive 2-valued state** `s: L→{0,1}`: `s(Ω)=1`; for pairwise-disjoint
  `{A_n}⊆L`, `s(⋃A_n)=Σ s(A_n)` (= Navara–Pták Def 3, 2-valued case; for 2-valued
  `s`, at most one disjoint piece is sent to 1).
- **`δ_ω`** (ω∈Ω): `δ_ω(A)=1 ⟺ ω∈A`. **Is a σ-state:** `δ_ω(Ω)=1` ✓; for disjoint
  `{A_n}`, `ω∈⋃A_n` iff `ω∈` exactly one `A_n` ⟹ `δ_ω(⋃A_n)=Σδ_ω(A_n)` ✓. So **every
  point gives a σ-state.** ✓

## The Dirac/non-Dirac dichotomy (Claim 2 — VERIFIED ✓, trivial)
Every global σ-state is either `=δ_ω` for some ω (Dirac) or not (non-Dirac).
Exhaustive by definition. The *content* lives in claims 3 and 5.

## Clause (i): no Dirac extends `s₀` (Claim 3 — VERIFIED ✓; ONE WORDING FIX)
A Dirac `δ_ω` extends `s₀` (i.e. `δ_ω|_B = s₀`) iff for every `A∈B`,
`s₀(A)=1 ⟺ ω∈A`. So `ω ∈ K(s₀) := ⋂{A∈B: s₀(A)=1} ∩ ⋂{A^⊥: A∈B, s₀(A)=0}`.

**⊥-closure SUBSUMES the false side** (advisor-confirmed): `B` ⊥-closed ⟹ for false
`A`, `A^⊥∈B` and `s₀(A^⊥)=1−s₀(A)=1`, so `A^⊥` is an s₀-true element of `B`. Hence
`{A^⊥: false} ⊆ {true elements}` and
**`K(s₀) = ⋂{s₀-true elements of B}`** — the false-complement constraints are already
in the true-intersection.
- Sufficiency check: `ω∈⋂{true}` ⟹ true `A`: `ω∈A`, `δ_ω(A)=1=s₀(A)` ✓; false `A`:
  `A^⊥` true so `ω∈A^⊥`, `ω∉A`, `δ_ω(A)=0=s₀(A)` ✓. Both directions clean.

**∴ Clause (i): "no Dirac extends `s₀`" ⟺ `⋂{s₀-true elements of B} = ∅`.**

**FIX for the writeup (wording, NOT math):** §2 says "⋂{generators s₀ sends to 1}".
The word **"generators"** invites a non-⊥-closed reading (a generating set `F`), on
which the false constraints are NOT subsumed and the two-family `K` WOULD be needed.
Correct to: "`B` a ⊥-closed finite sub-orthoposet; clause (i) = `⋂{s₀-true elements
of B} = ∅`," + one line noting the false constraints are subsumed by ⊥-closure. Do
NOT add the two-family `K` as a math correction — it is redundant under ⊥-closure.

---

## Claim 4 — forward: witness ⟹ (i)∧(ii) — VERIFIED ✓ (wording: "extends")
Witness = no global σ-state `s` has `s|_B=s₀`. σ-states partition Dirac+non-Dirac
(Claim 2, exhaustive). So "no σ-state extends s₀" = "no Dirac extends" (i) ∧ "no
non-Dirac extends" (ii). Definitional via the partition. **Standardize "extends"
(`s|_B=s₀`) throughout; drop the loose synonym "realizes."** Wording, not math. ✓

## Claim 5 — reverse: (i)∧(ii) ⟹ witness — VERIFIED ✓
(i)∧(ii) = no σ-state of either type extends s₀; the types are exhaustive of ALL
global σ-states (Claim 2); ⟹ no global σ-state extends s₀ = witness. ✓
**So witness ⟺ (i)∧(ii)** — the polarity is **(i)∧(ii)**, both NEGATIVE clauses
("no Dirac…" ∧ "no non-Dirac…"). ⚠ The writeup §2 formula "(i)∧¬(ii)" has a SIGN
SLIP — (ii) is already "no non-Dirac rescues", so it must be (i)∧(ii), not (i)∧¬(ii).
FIX in the writeup.

## Claim 6 — "= σ-point-selection" — ⚠ NOT a reduction; it's a LOCALIZATION (FIXED)
**The genuine gap of the whole pass (advisor-confirmed). The headline overstated.**
- §1 defined σ-point-selection failure as "no σ-additive 2-valued **STATE** realizes
  it." But Diracs ARE states (Claim 1) ⟹ that = "no σ-state extends s₀" = the witness
  VERBATIM ⟹ "witness ⟺ σ-point-selection" is a **TAUTOLOGY** (renaming), not a
  reduction.
- §2 said clause (ii) (non-Dirac only) "IS σ-point-selection" — under THAT reading
  "witness ⟺ σ-point-selection" is **FALSE** (witness needs (i) too).
- Validation scouts: σ-point-selection is written down NOWHERE = it is just our name
  for clause (ii), NOT a separate harder named problem to reduce TO.
**RESOLUTION (keeps real content, downgrades the claim honestly):** the contribution
is **LOCALIZATION**, not equivalence-to-a-harder-problem. witness ⟺ (i)∧(ii); clause
(i) is **concrete + freely arrangeable** (N–P device: ⋂{s₀-true}=∅ for free); ∴ all
difficulty + any cardinal-sensitivity **localizes to the non-Dirac realization core
(ii).** That is genuinely contentful; the boundary map (Polish→no-gap, HW2 orthogonal,
faithful-tribe below, no-routing-port) hangs off (ii). **Headline = "the σ-essential
witness question LOCALIZES TO the non-Dirac realization core," NOT "reduces to
σ-point-selection."**
- FIXES: (a) define σ-point-selection := clause (ii) and rewrite §1 to match (drop the
  "any state" phrasing that collapses to the witness); (b) restate central claim as
  localization "essentially clause (ii), modulo the arrangeable (i)" — keep the
  "modulo" as the content; (c) fix the (i)∧(ii) vs (i)∧¬(ii) polarity slip (Claim 5).

## Claim 7 — Navara–Pták engine — VERIFIED ✓ (vs the PDF; ONE wording tightening)
Checked against `navara_ptak_1983_…pdf`:
- **7a (concentration = Dirac):** N–P Thm 1 condition (2): "m restricted to A_{f,g} is
  *concentrated*" := "∃ x∈Q s.t. for any A, m(A)=1 iff x∈A" = **exactly δ_x = our
  Dirac.** So clause (i)'s "Dirac-realizable" IS N–P "concentrated." ✓
- **7b (example = non-Dirac rescuer):** their Example (Q=ℚ²; m(A)=1 iff A⊇ one of
  B,C,D; B∩C∩D=∅) gives a genuine 2-valued **measure (σ-state) that is NOT
  concentrated** — a non-Dirac σ-state realizing the local pattern {B,C,D true} that
  NO Dirac realizes. = exactly "(i) holds, (ii) fails." ✓ This is why the device alone
  is not a witness — N–P BUILD the rescuer.
- **⚠ WORDING TIGHTENING:** the writeup cites "their Thm 1: a 2-valued σ-measure is
  additive iff concentrated." That is N–P's OWN result (about *integration*-additivity,
  their problem). Our reduction does NOT use the additivity-iff — it uses only
  (concentration = Dirac) + (the example). Cite N–P for the **concentration-concept +
  example**, not for an additivity-equivalence the reduction doesn't depend on. (Avoids
  importing a dependency we don't need.)

---

## VERDICT — airtight pass COMPLETE (7/7)
**The §2 mechanism is mathematically SOUND but the §2/§1 FRAMING overstated.** No math
gap in the equivalence `witness ⟺ (i)∧(ii)` (claims 4,5 ✓). The genuine finding
(Claim 6): it is a **LOCALIZATION** (difficulty localizes to the non-Dirac core (ii),
since (i) is freely arrangeable), NOT a reduction to a separate harder named problem.
Fixes to apply to `sigma_essential_reduction_writeup.md`:
1. **§2 wording:** "generators" → "σ-true elements of the ⊥-closed sub-orthoposet B";
   add the false-constraints-subsumed line (Claim 3).
2. **§2 polarity:** the formula "(i)∧¬(ii)" → "(i)∧(ii)" (both negative clauses) (Claim 5).
3. **§2 "extends" standardized**, drop "realizes" (Claim 4).
4. **§1 + headline:** define σ-point-selection := clause (ii); restate the central claim
   as **LOCALIZATION** ("essentially clause (ii), modulo the freely-arrangeable (i)"),
   NOT "reduces to σ-point-selection." Drop §1's "any state" phrasing (collapses to the
   witness) (Claim 6).
5. **§2 N–P citation:** cite for concentration-concept + example, not the additivity-iff
   (Claim 7).
⟦All claims HAND-verified; Claim 6 is the load-bearing correction, advisor-confirmed.⟧
