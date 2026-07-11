# Fresh-context adversarial proof-read: attack note §9 (Skeleton B cold attack)

**Date:** 2026-07-10 (session 12). **Clears:** the s11 ⟦HAND⟧-glue
proof-read debt (opened in the s11 handoff). **Target:**
`oml_lattice_regularity_attack.md` §9 (corrections 9a(i)/(ii), Lemma A1,
L0, A2, pattern-dichotomy corollary, T1, T3, P1, §9d reduction +
Conjecture B′). **Method:** two independent agents — (1) fresh-context
adversarial reviewer (no prior exposure to the thread), instructed to
refute, all ten items re-derived independently, from-scratch machine
receipts (the repo's `loop5_greechie_oracle.py` was NOT read or reused);
(2) literature scout pinning the two cited-standard OML facts to
primary-grade sources. Satisfies verify-independently via independence
of *context*, not of species (s9b directive). User retains
veto/ratification.

## VERDICT: SOUND

No finding above cosmetic. All ten items VERIFIED by independent
re-derivation; 118/118 from-scratch machine checks pass (re-run
independently by the orchestrator, all exit 0). The three flagged
highest-risk steps all cleared:

- **A2's citation step** — both facts CONFIRMED at primary-source
  grade (see Citations below), including the *infinite* pairwise-
  commuting case (Bruns–Harding Prop 2.8 is stated for arbitrary X,
  via the commutant argument, not a directed-union limit).
- **T3's σ-continuity step** — full re-derivation went through:
  ν(Fₙ)=1 by two-valued f.a. induction; F₁ = D ⊍ ⊍(Fₙ\Fₙ₊₁) with each
  difference null; σ-additivity *on Bl* (supplied by A1c) gives
  ν(D)=1 ⟹ D ≠ ∅; the {D ⊆ A or D∩A = ∅} family is a σ-subfield
  containing the generators (countable unions in Bl ARE set unions,
  by A2). Both load-bearing counterexamples checked; the ω₁
  ctble/co-ctble one fully re-derived (state σ-additive, non-Dirac;
  field genuinely not countably generated).
- **L0's converse (join-vs-⊍)** — no gap: P⊍Q ∈ L is an upper bound so
  join ⊆ P⊍Q; join ⊇ P∪Q as a set since it bounds each part; equality
  follows, then A∩B = A∧B by the set computation.

## Per-item summary (all VERIFIED)

| Item | Note |
|---|---|
| 9a(i) MO_ω ∈ 𝒞 | Every claimed property re-derived incl. essential irreducibility (quotient ≅ L); Φ via lem:horizontal re-read against the paper. Truncations MO₂..MO₆ machine-checked. |
| 9a(ii) pentagon | Built from scratch; 11 two-valued states (= Lucas L₅), order-determining; latticehood verified DIRECTLY (all 484 pairs have GLB/LUB) so the loop-lemma cite is not load-bearing; 22-element representation, trivial centre, no singletons, NOT horizontal; poor-pair count 100 confirmed by independent hand decomposition 30+60+5+5; 120 incompatible pairs, 20 with nonzero meet — note never conflates incompatible with poor. |
| A1 (a)(b)(c) | High-risk (b) step re-derived: cₙ∩b ∈ L, disjointness inherited, u\b and b\u via orthomodular difference; strictly the concrete test alone suffices. |
| L0 | Both directions; converse join step scrutinized, closed (above). |
| A2 | Chain re-derived via commutant closure + L0 converse; decreasing-intersection identity fuzz-checked (500 trials); every pentagon block and overlap verified a field of sets. |
| Corollary | Feared infinite-B gap does NOT exist — patterns are finite ⊥-closed by definition (Φ quantifies over Fin_⊥(L)); atom mechanics exhaustively machine-checked. |
| T1 | Main statement + all-singletons ⟹ Boolean σ-field sound; one vague phrase repaired (edit 2 below). |
| T3 | Flagged high-risk item; full re-derivation went through (above). Machine: 200 random finite σ-fields + all pentagon blocks. |
| P1 | Weak poorness ⟺ strong intersection-poorness on lattices confirmed (so §7c(iii) and P1 usage agree); superadditivity + decomposition re-derived. |
| §9d/§9e | Reduction follows from A1c+T3; text does NOT accidentally claim B′(i); "(= Theorem 2 modulo B′(i))" checks out under the natural reading of B′(ii). |

## Findings (all cosmetic; edits applied 2026-07-10 s12, marked ✎)

1. ✎ Pentagon "∈ 𝒞": literal essential irreducibility (quotient by the
   σ-ideal of countable sets) degenerates on finite carriers —
   parenthetical added reading irreducibility as trivial centre.
2. ✎ T1's "lies in some member of L inside A∩B closed enough to exhaust
   it" was vague AND over-hedged — replaced by the clean (stronger)
   hypothesis: every point of A∩B lies in some member of L contained in
   A∩B; no exhaustion needed.
3. ✎ Corollary's "μ(A⊍B) = 2" remark superfluous — incompatibility
   alone forces A∩B ≠ ∅ (∅ ∈ L makes disjoint pairs compatible);
   replaced.
4. ✎ P1's "some Aₙ∩B ≠ ∅" tacitly uses poorness (A∩B ≠ ∅), not just
   A∧B = 0 — made explicit.
5. ✎ B′(ii) phrases a whole-carrier property (killing every selection)
   as a coarse-block property — precision caveat added; fine as a
   slogan, must be sharpened before an attack.
6. (No edit) T3's load-bearing counterexample (a) (product-Ulam Fₙ ∉ L)
   was reported consistent-but-not-re-derived by the reviewer; it is
   the corpus's own Cor. "incompatibility; not a lattice"
   (`sigma_essential_body.tex:713`), independently established there.

## Citations pinned (scout, primary-grade; ✎ applied to A2)

- Commutant closure: Bruns–Harding 2000 ("Algebraic Aspects of
  Orthomodular Lattices", *Current Research in Operational Quantum
  Logic*), Props 2.2–2.4 — C(a) closed under ′ and under all
  *existing* joins/meets (stronger than the finite-∧ form used).
- Foulis–Holland: Kalmbach 1983 **Theorem 5, p. 25**
  (Metamath-verified page cite); originals Foulis 1962 (Portugaliae
  Math. 21) / Holland **1964** (Trans. AMS 112 — NOT 1963; the 1963
  TAMS paper is the dimension-lattice one). Nuance: F–H concludes
  distributivity of the generated sub*lattice*; Boolean sub*algebra*
  needs all-pairwise commuting = Bruns–Harding Prop 2.8.
- Pairwise commuting ⟹ Boolean subalgebra, arbitrary (incl. infinite)
  subsets: Bruns–Harding Prop 2.8; blocks Prop 3.1 (+ §3 Zorn).
  Maximal pairwise-commuting sets in an OML ARE the blocks (no
  not-a-subalgebra pathology; M = ⟨M⟩ by maximality).
- OMP contrast (pairwise ⇏ jointly compatible): Ramsay 1966 (*J. Math.
  Mech.* 15, 227–234) and independently Pool 1963 (PhD thesis), via
  Pulmannová 1981 (*Ann. IHP A* 34(4), p. 393, open access at Numdam);
  reference-work confirmation Wilce, Handbook 2009, p. 458 (in
  library: `engesser_gabbay_lehmann_2009.pdf`).
- Bonus corroboration (scout): Bruns–Harding Prop 2.4 + maximality ⟹
  blocks are closed under all joins/meets existing in L — independent
  convergence with A2's blocks-are-σ-fields.

## Machine receipts (committed)

`notes/open_questions/verification/proof_read_2026-07-10_s11/`
(written from scratch by the fresh-context reviewer; repo oracle not
read): `s11a_pentagon_independent.py` (36/36 — pentagon from scratch:
states, order-determination, σ-class, lattice+OM law, blocks/fields/
overlaps, not-horizontal, centre, 100 poor pairs, no singletons, L0,
T1, P1, St_fa = Diracs, corollary atom mechanics, T3 block mechanics),
`s11b_mo_n_truncations.py` (75/75 — MO₂..MO₆), `s11c_engine_identities.py`
(7/7 — A2/T3 identities fuzzed 500 trials + full T3 pipeline on 200
random finite σ-fields). All re-run by the orchestrator: exit 0.
