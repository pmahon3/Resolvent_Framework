# Five and six quantities, every pair seen: K₅, K₆

reviewed: false. 2026-11-13. Pre-registration first; results appended below. ⟦HAND⟧ = unchecked hand argument.
Notation: `notes/programme/TERMINOLOGY_CROSSWALK.md` §A″. Context: `FOUR_QUANTITIES_GATE.md` (K₄ closed at every
finite size, hand, two readers). An independent check of the gluing lemma is running separately and will compute
K₅(2) and "two K₄'s sharing a triangle" at two values by closure; this file does not repeat that.

## Forcedness check and what is expected
- **Slices.** For K_m, two slices at one quantity differ by a sum of m−1 one-quantity functions with values in
  {−1,0,1}. The T1 argument gives the same dichotomy: simple, or K-type on exactly two quantities ⟦HAND⟧. So "reducible"
  and the merge move make sense for every m, and a reducible set on K_m(n) is in D once the merged grid is settled.
- **Two values.** A sum of pair functions on bits is a real polynomial of degree ≤ 2, so V₀₁(K_m(2)) is the set of
  Boolean functions of degree ≤ 2. From memory, unverified: such a function depends on at most 4 of its variables
  (the degree-d bound of Nisan–Szegedy is d·2^(d−1)). If so, every member of V₀₁(K_m(2)) lives on four quantities and is
  in D by the K₄ theorem, for every m.

## Gate `gate.five_quantities` (pre-registered 2026-11-13, not yet run)
1. **Bits, m = 5 and 6.** Enumerate V₀₁(K₅(2)) and V₀₁(K₆(2)) exactly; for each member count the quantities it
   depends on. Prediction: never more than 4. A member depending on 5 or 6 would be a new irreducible object and
   would refute the remembered bound as used here.
2. **Irreducible sets on K₅ beyond bits.** Enumerate V₀₁(K₅(n)) by slices for n with entries in {2,3}, up to K₅(3) if
   each step stays under 1.5 GB, and count irreducible members. Prediction (by analogy with K₄, no proof): none
   unless every quantity has two values.
- (a) both predictions hold ⇒ every set tested reduces, by verified merges, to a set on bits that depends on ≤ 4
  quantities; with the K₄ theorem this gives D = V₀₁ at the sizes run. Next: try the hand proof "irreducible ⇒ two
  values everywhere" for general m.
- (b) a prediction fails ⇒ the failing set is the object to study; nothing is concluded about D.
**Prior guesses (unvalidated):** part 1 holds 85%; part 2 holds 65%.

## FIRED 2026-11-13: outcome (a), both predictions hold
Script `../verification/four_quantities/km_slices.py` (slice enumeration for any number of quantities). Validated
first: K₃(3) = 15,914, K₄(2) = 222, K₄(3) = 67,742.

| scenario | \|V₀₁\| | irreducible | members depending on exactly k quantities (k: count) |
|---|---|---|---|
| K₅(2) | 552 | 0 | 0: 2, 1: 10, 2: 100, 3: 320, 4: 120 |
| K₆(2) | 1,164 | 0 | 0: 2, 1: 12, 2: 150, 3: 640, 4: 360 |
| K₅(2,2,2,2,3) | 2,220 | 0 | …, 4: 504 |
| K₅(2,2,2,3,3) | 9,136 | 0 | …, 4: 1,752 |
| K₅(2,2,3,3,3) | 32,668 | 0 | …, 4: 5,400 |
| K₅(2,3,3,3,3) | 86,104 | 0 | …, 4: 14,904 |
| K₅(3) | 184,652 | 0 | 0: 2, 1: 30, 2: 4,980, 3: 144,000, 4: 35,640 |
| K₆(2,2,2,2,2,3) | 4,188 | 0 | …, 4: 1,320 |
| K₅(4,2,2,2,2) | 13,908 | 0 | …, 4: 4,536, **5: 384** |

- **Part 1 (bits).** No member of V₀₁(K₅(2)) or V₀₁(K₆(2)) depends on more than 4 quantities. Consistent with the
  remembered bound for Boolean functions of degree ≤ 2 (still unverified against a source).
- **More than predicted.** With sizes 2 and 3 the same holds: at every K₅ and K₆ size run with no quantity above three
  values, every member depends on at most 4 quantities. So each lives on some four of the quantities, and is in D by
  the K₄ theorem (hand, two readers) plus "forgetting observers". **D = V₀₁ at those sizes**, at that evidence level.
- **Part 2.** No irreducible member at any size run.
- **A hand prediction confirmed.** With a four-valued quantity a selector can read four different other quantities.
  K₅(4,2,2,2,2) has exactly 384 members depending on all five quantities; none is irreducible. (That they are all
  selectors was not checked.)
- Largest run 4 s; peak 1.4–1.6 GB (the first batch touched 1.6 GB, over the 1.5 GB rule; later runs were separated).
- Merge certificates were **not** verified mechanically here (they were for K₄); only reducibility was tested.

**Beat 2 (explain) — partly.** Bits: degree ≤ 2 Boolean functions (needs the source). Sizes up to 3: no hand
argument yet for "at most four quantities". **Beat 3 (relocate).** The smallest unexplained things: (i) why at most
four quantities when no size exceeds 3; (ii) a hand proof of "irreducible ⇒ two values everywhere" for K_m, m ≥ 5
(the K₄ argument's two-case split now has a pair-sum set T on m−2 quantities in place of a subset of one quantity);
(iii) members depending on five or more quantities at sizes ≥ 4: are they all selectors?
