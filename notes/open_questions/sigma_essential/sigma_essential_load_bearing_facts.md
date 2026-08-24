# σ-essential — load-bearing facts (settled, reusable)

*Extracted from the retired `CHARTED_sigma_essential.md` (2026-06-26), which the
[[sigma_essential_taxonomy]] JSON superseded as a navigation layer. These are the
technical results CHARTED carried that the taxonomy's one-liners did not preserve in
full. Settled + reusable; cite when re-deriving. ⟦HAND-level unless a primary source is
named.⟧*

---

## State-space facts

- **S_df COMPACT.** S_df (all 2-valued states) is closed in `{0,1}^L`, hence weak-*
  compact; a σ-additive μ on S_df ALWAYS exists. The question is whether μ is
  *supported* on the non-compact S_df^σ.
- **Off-hull is ALWAYS finitely witnessed** (Hahn–Banach in ℝ^L). The deliverable is the
  **restriction-gap** `{s|_F : s ∈ S_df^σ} ⊊ S_df(F)`, NOT a non-Borel S_df^σ (that is
  the descriptive shadow, not the content).
- **Sharp characterization:** `S_df^σ = ⋂_{chains aₙ↓0} U_chain = S_df ∩ ⋂_block O_B`.
- **Countable-block theorem:** ≤ ℵ₀ atomic blocks ⟹ μ(fakes) = 0 ⟹ no leak. A witness
  needs **uncountably many INFINITE atomic blocks.**
- **Blocks must be ATOMIC — reinforced by the bisection kill (2026-07-01):** an atomless
  *measure-algebra* block admits NO 2-valued σ-additive state (halve/iterate/measure→0),
  so a global σ-2-valued state can't restrict to it ⟹ "extends to none" goes VACUOUS, not
  contextual. Atomic blocks carry Diracs ⟹ non-vacuous state space. ⚠ REGIME: the bisection
  kill is measure-algebra-specific; a general atomless σ-BA can carry a 2-valued σ-state = a
  σ-complete ultrafilter = measurable-cardinal territory (no-LC regime only). ⟹ any "atomless
  blocks" cell is incoherent; the open frontier is atomic infinite blocks + non-Polish NATIVE
  gluing (`open.intrinsic_K`). Do NOT re-introduce atomless-blocks.

## Mechanism facts

- **Genuine dichotomy** (the three incompatibility mechanisms fail oppositely):
  share-one-atom ⟹ finite blocks; share-{0,1} ⟹ trivial joins / diagonal coupling;
  share-nothing-infinite ⟹ finite blocks. A witness needs cross-block
  **incompatible-not-orthogonal between INFINITE blocks.**
- **CARRYING vs SELECTING** (2026-06-22): the difficulty is NOT mass-carrying (states are
  plentiful, S_df compact); it is **SELECTING** one globally-coherent σ-point across
  incompatible blocks = non-compact inverse-limit / free-ultrafilter existence.
- **Predicate fork:** P-weak ⟹ P-strong; co-extensive ⟺ σ-point-realization; they agree
  on all segregated/Polish carriers; use P-strong if a witness appears.
- **All-roads-through-Door-1:** Door 2 (construction) = the same object; Door 3
  (forcing-model outcome) = its consequence, unstatable without the object. One task,
  three exits.

## Forcing-sentence well-posedness (settled 2026-06-23, deep-research sweep #4)

- **(a) Φ is a clean existential** — "every local state extends to SOME global state" is
  the canonical Horn–Tarski 1948 → marginal-problem form; De Simone–Navara–Pták
  (arXiv:math-ph/0311012) exhibit exactly a ¬Φ restriction-gap on finite concrete logics.
  Uniqueness lives only in the separate Mackey–Gleason/Bunce–Wright branch; Ψ does not
  inherit it.
- **(b) Off-center is genuinely DERIVED** — Kalmbach center-decomposition +
  product-state factorization ⟹ a contextual witness must be irreducible. The literature
  conventionally IMPOSES irreducibility; cite as derived-from-standard-pieces.
- **(c) Ψ is cleanly statable + ZFC-independent-capable BEFORE a witness exists** —
  precedent: von Neumann/Maharam (ZFC-independent via Suslin tree), Talagrand,
  real-valued measurable cardinals (Fremlin Ch.39+54). Independence proofs supply MODELS,
  not a fixed structure. Caveat: all precedent is real-valued/strictly-positive; the
  2-valued + non-Boolean concrete-OML case is the open edge.

## Blecher–Weaver (2026-06-23, CORRECTED)

Singular countably-additive **pure** ({0,1}-on-mult-domain) state on `B(ℓ²(κ))` exists
⟺ κ Ulam-measurable (arXiv:1607.08505, JFA 272 2017). The set-theoretic-σ-essential cell
IS inhabited on B(H). **CORRECTION:** the cardinal does NOT factor through the abelian
diagonal in the PURE/2-valued case — that needs Anderson's conjecture (false under CH);
B–W use Marcus–Spielman–Srivastava paving; Akemann–Weaver (PNAS 105(14) 2008, p.5313)
give a pure state on no masa. Masa-factoring holds only real-valued. B–W is a PRECEDENT,
not an INSTANCE (it fails concreteness C1 by Kochen–Specker). See
[[sigma_essential_large_cardinal_bounds]] for the masa-free-extraction sharpening.
