# Independent s36 period-two scope audit

Scope: the seven-loop face `C={a0,a3,a11}`, rooted one-sided/any-position
semantics, constant interface width `k<=2`.  This is an audit artifact, not a
canonical attack note.

## Width one: exhaustive result

`audit_s36_p2_k1.py` exhaustively enumerates all ordered pairs of labeled
width-one ports.  Results:

- raw ordered period-two pairs: `196^2 = 38,416`;
- both component interfaces pass the two-cell girth gate: `38,416`;
- the ordered pair passes the three-cell girth gate: `38,416`;
- operative pairs: zero for every common-zero target
  `a1,a2,a4,a10,a12,a13`.

The computation runs targets `a1,a2,a4`; the other three counts transfer by
the exact face-stabilizing reflection `a -> -a (mod 14)`.  A deterministic
sample checked the implementation-level screen signature under that
reflection and found zero mismatches.

Thus period two, width one is a rigorous bounded no-go.  Period-one pairs are
included in the enumeration (`p0=p1`), so no exact-period convention affects
the zero result.

## Width two: size and safe filtering plan

- raw ordered pairs: `16,562^2 = 274,299,844`;
- after requiring each component port to pass two-cell girth:
  `9,408^2 = 88,510,464`;
- a fixed-seed 10,000-pair sample found 9,922 passing three-cell girth, an
  estimated `~87.82M`; hence the three-cell gate alone barely reduces this
  class.

Safe gate order for a complete census:

1. Enumerate only the 9,408 individually two-cell-girth-valid ports.
2. Check ordered-pair three-cell girth (necessary, but expect little pruning).
3. Compute phasewise face-free masks first and reject unless the entire face
   is free in both phases.  This is a necessary portion of the operative
   definition and is independent of complement order determination.
4. On survivors compute face non-liveness, then the live-complement
   nonorder-witness condition in both phases.
5. Apply longer-window quotient girth and master geometry only to operative
   survivors.

For feasibility, represent each port's 29-by-29 successor relation as bit
masks and evaluate pair gates by bitset joins.  Bucket ports by their induced
transition data on the three face states before testing all pairs.  The only
proved global symmetry here is the face-stabilizer reflection, which pairs
the six targets and halves target work, not the 88.5M ordered interface pairs
for a fixed representative target.  Do **not** quotient by swapping the two
interfaces without a separate rooted-semantics proof: period rotation is not
automatically safe for a chain rooted in phase zero.

