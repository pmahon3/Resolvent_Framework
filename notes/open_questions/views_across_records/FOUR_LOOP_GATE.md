# Is it even loops, or the four-loop? (parity batch, 2026-11-13)

reviewed: false. Declared batch (horizon rule): (1) test the six-loop; (2) understand by hand why loops differ.
Set aside as bookkeeping, not part of this batch: the source for the degree-2 bound; whether the 384 five-quantity
sets on K₅(4,2,2,2,2) are all selectors; a general hand proof for K_m.
Notation: crosswalk §A″. Two values per quantity throughout unless stated. ⟦HAND⟧ = unchecked hand argument.

## What prompted it
C₄(2) has 8 questions that add up and cannot be built; C₃ and C₅ have none (`GLUING_LEMMA_CHECK.md`). The user asked
on 2026-11-13 whether odd/even parity is involved. Claude guessed a five-loop would fail; it does not.

## Hand reasoning before running ⟦HAND⟧
1. **Half-counts.** Let dᵢ = "neighbours i, i+1 disagree"; round a loop the number of disagreements is even. A
   half-count is c + ½ Σ ±dᵢ. For it to be yes/no its values must be two consecutive integers. Checking the cases:
   length 3 with no minus sign (this is "not all equal", buildable); length 4 with one minus sign (the 8 gap sets);
   **no choice of signs works at length 5 or 6**. So half-counts single out lengths 3 and 4, not even lengths.
2. **Degree.** With bits, a sum of pair functions is a polynomial of degree ≤ 2 whose quadratic terms are seen pairs.
   Remembered, unverified: a yes/no function of degree ≤ 2 depends on at most 4 bits. Our own counts agree for K₅(2)
   and K₆(2), and the members depending on exactly 4 quantities number 24 per four quantities (120 = 5×24,
   360 = 15×24), i.e. only the images of the four-bit pattern A₄.
3. **A₄'s quadratic terms form a four-loop.** With A₄ on (p,u,v,t): 1_{A₄} = 1 − p − v + vt − ut + pu + pv. The
   quadratic terms are pu, ut, tv, vp: the loop p–u–t–v–p, and neither diagonal (pt, uv).
4. **So, with bits:** every question that adds up involves at most four quantities. Those involving ≤ 3 need at most
   a triangle of seen pairs and are buildable where they add up. The only four-quantity kind, A₄, adds up exactly
   when its four-loop is seen, and (K₄, K₄⁻ results) is buildable as soon as one diagonal is also seen.
**Conjecture from this (bits).** D(G(2)) = V₀₁(G(2)) iff G has no four-loop without a diagonal (no induced C₄), and
the gap consists of 8 sets per such four-loop.
This would answer the parity question: **it is the four-loop, not even length.** A yes/no question built from pairs
cannot involve more than four bits, so it cannot run all the way round a longer loop.

## Gate `gate.four_loop` (pre-registered 2026-11-13, before running)
Predictions, all for two values per quantity:
| shape | prediction |
|---|---|
| C₆ | gap 0 |
| C₇ | gap 0 |
| C₆ plus the long chord 03 (two four-loops without diagonals) | gap 16 |
| C₆ plus the short chord 02 (a triangle and a five-loop) | gap 0 |
| K₂,₃ (two quantities each seen with three others; three four-loops without diagonals) | gap 24 |
| C₄ | its 8 gap sets are images of A₄ |
- All hold ⇒ the conjecture survives; "even loops" is refuted as the rule (C₆). Affects the withdrawn chordal guess
  (replace by "no four-loop without a diagonal", bits only).
- C₆ has a gap ⇒ the degree argument is wrong somewhere; even length is back in play.
- A gap count differs ⇒ some other kind of unbuildable question exists; describe it.
**Prior guesses (unvalidated):** C₆ gap 0: 85%. All six rows: 60%.
Not addressed by this gate: more than two values (where selectors can involve many quantities), and why A₄ cannot be
built on the bare four-loop (computed; the October "shape lemma" for triangle-free shapes would explain it).

## FIRED 2026-11-13: all six predictions hold exactly
Script `../verification/four_quantities/bits_shape_gap.py` (exact integer arithmetic; closure to a fixed point).

| shape (two values each) | \|D\| | \|V₀₁\| | gap | predicted |
|---|---|---|---|---|
| C₄ | 82 | 90 | 8 | 8, all images of A₄ ✓ (8 images of A₄ add up on C₄; none is buildable) |
| C₅ | 102 | 102 | 0 | (known) |
| **C₆** | 122 | 122 | **0** | 0 ✓ |
| C₇ | 142 | 142 | 0 | 0 ✓ |
| C₆ + long chord 03 | 164 | 180 | 16 | 16 ✓ |
| C₆ + short chord 02 | 172 | 172 | 0 | 0 ✓ |
| K₂,₃ | 144 | 168 | 24 | 24 ✓ |
| C₅ + chord 02 | 152 | 160 | 8 | (known) |
| K₄⁻ | 148 | 148 | 0 | (known) |

- **"Even loops" is refuted as the rule**: the six-loop has no gap.
- **The four-loop is the obstruction, with bits**: every gap observed is 8 sets per four-loop without a diagonal, and
  on C₄ those 8 are exactly the images of the four-bit pattern A₄.
- Loops satisfy |D| = |V₀₁| = 20·L + 2 for L = 5, 6, 7 (observed; not explained).

## Reading
- With two values, a question that adds up from pairs involves at most four quantities (remembered bound; our counts
  agree up to six quantities). The only kind that needs four is A₄. It **adds up** when the four-loop p–u–t–v is seen,
  and can be **built** once a diagonal is also seen. On a bare four-loop it adds up and cannot be built.
- So the parity the user sensed is real but sits one level down: the gap sets are half-counts of disagreements round a
  loop, and a half-count is a yes/no question only at lengths 3 and 4. Length 3 is buildable, length 4 is not.
- Conjecture (bits): **D(G(2)) = V₀₁(G(2)) iff G has no four-loop without a diagonal**, with gap = 8 × (number of such
  four-loops). Evidence: nine shapes. Status: hand reasoning by one author, resting on a remembered bound; not checked.

## Not addressed
More than two values per quantity: C₄ keeps exactly the pullbacks of its 8 (checked at two sizes), C₅ has no gap at
(2,2,2,2,3); nothing else is known, and selectors show that questions can involve many quantities once sizes reach 4.
Why A₄ cannot be built on the bare four-loop is computed, not explained (the October shape lemma for triangle-free
shapes is the candidate explanation). Prior art: not searched; "degree ≤ 2 Boolean functions" and "graphs with no
induced four-cycle" are the terms to search.

## Prior art, first pass 2026-11-13 (`BITS_AND_FOUR_LOOP_PRIOR_ART.md`; web negatives are snippet-level and weak)
- **OWNED: the bound and the classification.** A Boolean function of real degree d has at most d·2^(d−1) relevant
  variables (Nisan–Szegedy 1994; statement checked in full-text secondary sources, original body unread); tight at
  d = 2, so exactly 4 (Chiarelli–Hatami–Saks 2020, arXiv:1801.08564, read in full). Degree-2 Boolean functions are
  classified up to NPN equivalence in Filmus, "Quadratic Boolean functions on the cube" (2022, read in full): constant,
  identity, XOR, OR, all-equal, 3-sortedness, 4-sortedness; exactly one four-variable class.
- **The four-bit pattern has a name.** "A₄" is the **4-sortedness function** (Filmus), also Ξ₂ (Chiarelli–Hatami–Saks).
  The provisional name A₄ is dropped in new text.
- **OWNED: the half-count observation.** Filmus's proof shows the quadratic terms form an edge or a cycle with
  coefficients ±1/2 and that the length is at most 4; the triangle gives all-equal, the square has one minus sign.
  Only the wording in terms of disagreements round a loop is ours.
- **NOT FOUND: the statement about what can be built.** That the family generated from pair events by complement and
  disjoint union equals all degree-2 functions iff the graph has no induced four-cycle, with 8 lost per such cycle.
  Nearest neighbours read in full: Sultanbekov 1993, Ovchinnikov 1999 (shelf).
- **Beyond two values: PARTLY OWNED.** "Sum of functions of pairs" on [q]ⁿ is junta-degree ≤ 2, with an active
  literature on relevant-variable bounds (Valyuzhenich, arXiv:2609.12540, read in full; no classification, no exact
  bound). Selectors are known there as q-ary decision trees, the extremal examples. Not found: a classification for
  q ≥ 3, the merge reduction, the K₄ theorem.
- **Gluing lemma: NOT FOUND** as a statement about the generated set family; the nearest owned statement concerns
  existence of joints on decomposable schemes (Vorob'ev, Kellerer). Unread caps: Lauritzen 1996; Dawid–Lauritzen 1993.
- **A rhyme to check, not an owner (snippet level only):** Greechie's loop lemma, in which a pasting of Boolean
  algebras is an orthomodular lattice iff every loop has order at least 5, also singles out loops of length 3 and 4.
- **Vocabulary to use:** relevant variable; k-junta; real degree (never GF(2) degree, which is the Reed–Muller
  notion); junta-degree on [q]ⁿ; NPN equivalence; 4-sortedness function; q-ary decision tree for selectors.

