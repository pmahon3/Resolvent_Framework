# Figures

- `convex_hull_intuition.{tex,pdf}` — intuition-builder for contextuality as
  "state outside the closed convex hull of dispersion-free states." Three panels +
  a footer spelling out the spaces.
  - **(1) MO₂** — faithful 2D picture: state space is the square [0,1]²,
    the 4 dispersion-free states are its corners, their hull IS the whole square,
    so every state is a mixture of corners ⇒ no contextual state.
  - **(2) pentagon** — the lattice (Greechie 5-loop of atoms a₁…a₅, edge = shared
    block) drawn up top, then projected by f(s)=Σ s(aᵢ) onto a value axis: every
    dispersion-free corner has f ≤ 2 (odd-loop: no two adjacent atoms both 1), so the
    corner-hull's image is [0,2]; the state w ≡ ½ has f = 5/2, past the f=2 (KCBS)
    face ⇒ outside the hull ⇒ contextual.
  - **(3) σ-essential** — two stacked reaches of the same value-axis device: the
    σ-additive corners reach only g ≤ m_σ; the extra non-σ-additive "fake" corners
    push the full hull to g ≤ m_full > m_σ; the witness w lies in the gap
    (m_σ, m_full] — outside conv(S_df^σ), inside conv(S_df) — the leak no finite face
    sees.

## The three spaces (footer of the figure)

- **L** — the lattice itself (pentagon = 5 atoms + loop relations). An order-theoretic
  object, NOT a vector space; it has no linear dimension. It is the *index set* for the
  spaces below.
- **S(L) ⊆ ℝ^L** — the STATE SPACE. A state assigns a number to each lattice element, so
  it is a point in ℝ^L. For the pentagon, the state axioms pin a state down by its 5
  atom-values, giving a polytope S(L) ⊆ [0,1]⁵ ⊆ ℝ⁵. The dispersion-free states S_df are
  its {0,1}-valued VERTICES; closed-conv(S_df) is a sub-polytope, ALSO in ℝ⁵ —
  high-dimensional and undrawable. Contextuality (w ∉ closed-conv(S_df)) is a genuine ℝ⁵
  statement.
- **ℝ** — the projection target / value axis drawn in panels 2–3.

## What the projection is (and is not)

- A SEPARATING FUNCTIONAL is a linear map g : ℝ^L → ℝ, i.e. a weighted sum of
  atom-values; panel 2 uses g = f = Σ s(aᵢ). Because g is linear, g(closed-conv(S_df))
  is an INTERVAL [min, max], and the image of the hull equals the hull of the image.
- ONE-WAY CERTIFICATE: g(w) outside that interval ⟹ w outside the hull (sound). The
  converse fails — a contextual w may have g(w) inside the interval while poking out in
  another direction.
- NOT CANONICAL: g is *chosen* to separate THIS w (here, the KCBS functional separates
  the ½-state). By the separating-hyperplane theorem (Hahn–Banach), w is contextual IFF
  SOME linear g sends it strictly past the hull's image. One g detects the states
  violating *that* inequality, not all contextual states. The figure shows "a separating
  functional for this witness," not "the projection of the hull."

## Why panels 2–3 use a value-axis, not a 2D blob

Membership in a convex hull is "satisfies every supporting inequality." A 2D
"point inside/outside a region" cartoon CANNOT show a point outside its own corner-hull
(a convex polygon always contains its centroid) — an earlier draft did exactly that and
was geometrically wrong. Projecting onto a separating functional makes "outside the
hull" = "past a threshold value," which cannot misrepresent membership. The value-axes
and the [0,2] interval are faithful; only the specific numbers (2, m_σ, m_full) are
illustrative. Panel 1 stays 2D because MO₂ is genuinely 2-dimensional (2 atom-values,
4 corners, hull = the whole square) — there the picture is honest.
