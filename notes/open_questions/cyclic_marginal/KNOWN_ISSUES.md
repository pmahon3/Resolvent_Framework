# Known issues in the notes of this folder (fixes listed here; note text is not edited for a reversal)

reviewed: false.

## 2026-11-10: finite-kernel scope ("at compressed sizes" is now "at every finite size")
The finite triangle carrier contains every 0/1 span vector at every finite size (always closed, positive iff
compressed). Evidence and record: `../views_across_records/TRIANGLE_CONSEQUENCES_CHECK.md` C2; Lean core
`TriangleFinitary.box_iff_mem_of_finDet`; not claimed as new.
- `order_without_a_centre.tex:211`: "already reach every 0/1 facet at the compressed sizes" → holds at every finite
  size; compressedness enters only through positivity.
- `hidden_failure/SEED.md:51`: "(a) every 0/1 facet functional is realised by a carrier set at compressed sizes" →
  same change (dated seed; banner-level note only).
- `entry_audits/RESOLUTION_ovchinnikov_dnp.md:16–17, 93, 102`: old scope in a dated verdict; superseded by the dated
  answer at its "Open probe" item.
- `hidden_failure/REAUDIT_v21.md:6, 176, 230, 302` and `AUDIT_PHASE2.md:94`: old scope / owed certificate, covered by
  the 2026-11-10 banners in those files.

## 2026-11-10: triangle gate
`pointless_coherence.tex` and `order_without_a_centre.tex` do not assert the old "open" status. Possible
strengthenings (not made): on the triangle "finitely built" is every question; ideal point ⟺ globally glued family.
