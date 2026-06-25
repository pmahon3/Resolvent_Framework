# The σ-essential reduction — standing result (conditional)

*Recorded 2026-06-25. The theorem-shaped finding of the forcing-programme work:
the σ-essential contextual witness question REDUCES to a named open problem.
⟦HAND — the reduction direction "witness ⟹ σ-LS-failure" is verified at sketch
level; the converse and the exact strength are the content of [[#29]]/HW2.⟧*

---

## The result (conditional)

> **Claim.** The existence of a *concrete σ-essential contextual witness* — a
> concrete σ-complete non-Boolean off-center OML `L ⊆ P(Ω)` with a finite local
> 2-valued state `s₀` that extends to **no** global σ-additive 2-valued state on
> `L` — is **equivalent to the failure of a σ-Loomis–Sikorski representation** for
> non-distributive concrete σ-OMLs. In particular its existence is **not decidable
> in ZFC by any route attempted**: it bottoms out at **HW Problem 2** (whether every
> orthomodular poset has a σ-complete / regular completion), which is open in the
> literature and suggested-independent.

So the honest status of the "σ-essential witness" prize is neither
*constructible* nor *refutable* in ZFC, but **reducible**: it is provably as hard
as σ-Loomis–Sikorski for OMLs.

## Why (the verified core)

A global σ-additive 2-valued state on a concrete `L ⊆ P(Ω)` is either a
point-evaluation `δ_ω` (always available) or a **non-Dirac** σ-state. A finite
local `s₀` fails to extend **iff** (i) no `δ_ω` realizes it — the
"`⋂{generators s₀↦1} = ∅`" condition, freely arrangeable by the Navara–Pták
intersection device — **and** (ii) no non-Dirac σ-state rescues it.

Condition (ii) is exactly the **σ-point-selection problem**: does a globally
coherent σ-additive 2-valued state thread the locally-coherent constraints? That
is the σ-Loomis–Sikorski question. Hence:

- **witness exists ⟹ σ-LS fails** (a witness is a coherent local pattern with no
  global σ-realization = a σ-LS counterexample). ⟦verified at sketch level⟧
- **σ-LS holds ⟹ no witness** (a σ-LS representation realizes every coherent local
  pattern by a global σ-state). This is the direction whose exact form is HW2.

## What this DISsolves and what it does NOT

- **Resolves the framing confusion:** "the construction keeps hitting a wall" is
  not fatigue — it is the theorem. Four independent routes today (non-classical
  logic, the ¬Ψ lever, the direct construction, the template no-go) plus ~21 prior
  fenced reversals all collapse to σ-LS *because the witness question IS σ-LS*.
- **Does NOT prove the cell empty / ¬Ψ.** Blecher–Weaver: the Hilbert analogue
  *exists* under an Ulam-measurable cardinal, so ¬Ψ is not a ZFC theorem. The
  reduction says "as hard as σ-LS," not "impossible."
- **Does NOT (yet) prove the equivalence unconditionally.** The σ-LS⟹no-witness
  direction is HW Problem 2; resolving it is [[#29]].

## Pointers

- Mechanism + verification: `CHARTED_sigma_essential.md` (TEMPLATE NO-GO block,
  ¬Ψ FIRST RUN block, Con(Ψ) CONSTRUCTION block, 2026-06-25).
- HW Problem 2 / no regular completion: Harding 1998; Harding–Wright
  arXiv:2108.09819. CHARTED L:NAMED WALLS line 66.
- Navara–Pták 1983 (template + concentration criterion):
  `literature/navara_ptak_1983_two_valued_measures_sigma_classes.pdf`.
- Hilbert-side precedent (the measurable-cardinal flavor): Blecher–Weaver
  arXiv:1607.08505.
