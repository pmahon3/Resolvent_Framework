# Figures

- `ce_leak_intuition.{tex,pdf}` — the Boolean "uniform over ℕ" leak, as an intuition
  companion (NOT in the survey, by design). Draws a PROVED object: a finitely-additive
  charge with μ({1..k})=0 for every k and μ(ℕ)=1, which σ-additivity cannot realize
  (it would force 1=Σ0=0), so the unit of mass sits on the ideal points βℕ∖ℕ, not on
  any real point — the CE phenomenon. It is the honest stand-in for the σ-essential
  mechanism: the OML witness would need the SAME leak OFF-CENTRE, on non-distributive
  structure where no Boolean boundary (βℕ∖ℕ) absorbs it — the open part. Kept separate
  from the survey precisely because it is the *Boolean shadow*; putting it in the OML
  survey would risk the reader taking the βℕ leak FOR the σ-essential object, which is
  exactly what the survey must keep distinct.

## The contextuality figure now lives IN the survey

The convex-hull intuition figure (MO₂ corners-fill-the-square vs the pentagon's
separating-functional projection) was integrated into `oml_onboarding.tex` as
`Figure~\ref{fig:contextuality}` in §5.1 (after Lemma `lem:relational`), so the
standalone copy was removed. The reasoning behind that figure, retained here for
reference:

### The three spaces (why the pentagon panel is a projection)
- **L** — the lattice (pentagon = 5 atoms + loop relations); an order-theoretic object,
  not a vector space; it INDEXES the others.
- **S(L) ⊆ ℝ^L** — the STATE SPACE. A state assigns a number to each element ⇒ a point
  in ℝ^L; for the pentagon, pinned by the 5 atom-values, a polytope in ℝ⁵. S_df = its
  {0,1}-valued VERTICES; closed-conv(S_df) is a sub-polytope, also in ℝ⁵ —
  high-dimensional and undrawable.
- **ℝ** — the projection target. A SEPARATING FUNCTIONAL g : ℝ^L → ℝ (weighted sum of
  atom-values; the figure uses g = Σ s(aᵢ)) sends everything to the line. Linear ⇒
  g(hull) is an interval; g(w) outside it ⟹ w outside the hull (one-way certificate).
  g is CHOSEN for this w, not canonical: by Hahn–Banach, w is contextual iff SOME g
  separates it.

### Why no honest low-dimensional panel WITH contextuality exists
- MO_n are non-contextual: independent blocks ⇒ dispersion-free states = all 2ⁿ cube
  vertices ⇒ hull = whole cube = whole state space. (MO₃'s (½,½,½) is the centroid =
  a mixture of corners; the survey's `ex:strict`, ½+½+½=3/2>1, is the EXTENSION-axis
  charge-extendibility failure — a different functional — not a contextuality witness.)
- Lesson: **non-distributivity ≠ contextuality.** MO_n are non-distributive yet
  non-contextual; contextuality needs the loop/frustration (shared atoms, odd cycle)
  that independent blocks lack — the finite shadow of why ∏ₙMO₂ is "segregated."
- Among STANDARD minimal examples there is therefore no drawable honest
  hull-with-contextuality (even loops unfrustrated; loops <5 excluded by the Greechie
  loop lemma; smallest odd loop = pentagon = 5-dim) — so the separating-functional
  projection is the appropriate tool, not a shortcut. (A statement about standard
  examples, NOT a proof that no exotic low-dim contextual concrete OML exists.)

### Why panels use a value-axis, not a 2D blob
Membership in a convex hull is "satisfies every supporting inequality." A 2D
point-in/out-of-a-region cartoon CANNOT show a point outside its own corner-hull (a
convex polygon contains its centroid) — an earlier draft did exactly that and was
wrong. Projecting onto a separating functional makes "outside the hull" = "past a
threshold value," which cannot misrepresent membership. The MO₂ panel stays 2D because
MO₂ is genuinely 2-dimensional (2 atom-values, 4 corners, hull = the whole square).
