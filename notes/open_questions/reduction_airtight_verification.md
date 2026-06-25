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

## REMAINING (claims 4–7) — to verify, same gap-vs-wording discriminator
- **(4)** forward: witness ⟹ (i)∧¬(ii). [near-definitional; pin "extends" vs "realizes"]
- **(5)** reverse: (i)∧¬(ii) ⟹ witness, confirming the Dirac/non-Dirac taxonomy is
  exhaustive of ALL σ-states extending `s₀`.
- **(6)** clause (ii) = σ-point-selection is a faithful restatement, not a relabel.
- **(7)** Navara–Pták engine (their Thm 1 + example) used correctly — verify vs the PDF.
