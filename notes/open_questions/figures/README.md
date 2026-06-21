# Figures

- `convex_hull_intuition.{tex,pdf}` — intuition-builder for contextuality as
  "state outside the closed convex hull of dispersion-free states." Three panels:
  - **(1) MO₂** — faithful 2D picture: state space is the square [0,1]²,
    the 4 dispersion-free states are its corners, their hull IS the whole square,
    so every state is a mixture of corners ⇒ no contextual state.
  - **(2) pentagon** — the honest picture via the SEPARATING FUNCTIONAL
    f(s)=Σ s(aᵢ): every dispersion-free corner has f ≤ 2 (odd-cycle constraint),
    so the corner-hull maps into [0,2]; the state w ≡ ½ has f = 5/2, on the far
    side of the f=2 (KCBS) face ⇒ outside the hull ⇒ contextual.
  - **(3) σ-essential** — same device with two thresholds: the σ-additive corners
    reach only g ≤ m_σ; the extra non-σ-additive "fake" corners push the full hull
    to g ≤ m_full > m_σ; the witness w lies in the gap (m_σ, m_full] — outside
    conv(S_df^σ), inside conv(S_df) — the leak no finite face sees.

  DESIGN NOTE (why panels 2–3 use a value-axis, not a blob): membership in a convex
  hull is "satisfies every supporting inequality." A 2D "point inside/outside a
  region" cartoon CANNOT show a centroid lying outside its own corner-hull (a convex
  polygon always contains its centroid) — an earlier draft did exactly that and was
  wrong. Projecting onto the separating functional (the Hahn–Banach content) makes
  "outside the hull" = "on the far side of a threshold," which cannot misrepresent
  membership. The 1D value-axes are faithful; only the specific threshold numbers
  (2, m_σ, m_full) are illustrative.
