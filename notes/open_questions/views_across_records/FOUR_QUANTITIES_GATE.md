# Four quantities, every pair seen: does the triangle theorem survive one more quantity?

reviewed: false. 2026-11-13. Pre-registration; nothing run yet. ⟦HAND⟧ marks unchecked hand arguments.
Motivation and choice of move: chat 2026-11-13 (turn one dial at a time; the shape dial first). Lens only: four-player
rock–paper–scissors (Ranta–Lundberg–Kaitala 2005, ch. 11).

## Setup
Ω = X₀×X₁×X₂×X₃. Six observers, one per pair of coordinates (window graph K₄). D₄ = closure of the six families of
pair events under complement and (countable) disjoint union. V₀₁ = sets whose indicator is a sum of six pair functions.
Always D₄ ⊆ V₀₁. Criterion for V₀₁ ⟦HAND⟧: the eight-corner identity on every three coordinates with the fourth held
fixed (Kellerer 1964 Satz 1.1 for the family of pairs).

## The three sentences, restated for four quantities
- **S1₄ (questions).** Every carrier set is finitely built. Finite form: at every finite size, D₄ = V₀₁ (the logic is
  closed, Ovchinnikov). Infinite form: D₄ = D_fin, with some description of what is shut out.
- **S2₄ (answer patterns).** An additive function on D₄ is fixed by its values on window events; every compatible
  family of six couplings (matching one-coordinate profiles) is the window family of exactly one two-valued state.
- **S3₄ (worlds).** That state is induced by an ultrafilter on Ω iff the six couplings are pushforwards of one.

## Already on record (do not re-run)
`definitions_draft.md` §9a (2026-10-19, `verification/gap_linear_vs_constructive.py`), two values per coordinate:

| window graph | |D| | |V₀₁| | gap |
|---|---|---|---|
| triangle | 70 | 70 | 0 |
| path on 4 | 56 | 56 | 0 |
| square (4-cycle, adjacent pairs only) | 82 | 90 | **8** |
| diamond | 148 | 148 | 0 |
| K₄ | 222 | 222 | 0 |

So the finite form of S1 already **fails on the square** with two values (the 8 gap sets are half-cubes counting
disagreements round the loop), and **holds on K₄ with two values**. The triangle holds at every size (Lean core,
2026-11-10). Unknown: K₄ beyond two values; K₄ over infinite alphabets; S2₄, S3₄.

## Is the outcome forced? (lesson of 2026-11-07 and 2026-11-10)
- Not by positivity: with two values K₄ is already not compressed ⟦HAND⟧ (the pentagonal facet (b·x)(b·x−1)/2 ≥ 0,
  b = (1,1,1,−1), takes the value 3), so Ovchinnikov's "positive ⇒ closed" does not apply.
- Not by the triangle theorem: slices at a fixed x₃ are triangle carrier sets, which constrains D₄ but does not give
  D₄ = V₀₁.
- No Lean lemma covers four coordinates. Verdict: not forced, as far as checked.

## Gate `gate.four_quantities_closed` (pre-registered 2026-11-13, not run)
**Probe.** Compute |D₄| by closure and |V₀₁| by direct enumeration on 2×2×2×3, then 2×2×3×3, then 2×3×3×3 if the
previous step stayed under 1 GB and 5 minutes. One size at a time.
- **(a) Equal at every size run** ⇒ supports S1₄ in finite form. Next: try to transfer the triangle proof (slice,
  compare, merge non-K-related values) by hand. Affects: `conj.window_restriction_r` (graphs containing a triangle),
  a new conjecture "closed at every size ⟺ every long loop has a shortcut (chordal)".
- **(b) A gap at some size** ⇒ S1₄ fails in finite form. Record the gap sets and describe them (which loop do they
  count round?). The boundary of the theory then lies between the triangle and K₄. Affects the same entries, negatively.
- Either way S2₄ and S3₄ are not decided by this gate.
**Prior guess (unvalidated, for calibration only):** (a) about 65%.
