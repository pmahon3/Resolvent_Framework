"""r x 3 x 3 reduction (2026-10-21). Slice along x1 (3 values): slices T0,T1,T2 over (x0,x2) differ by additive patterns
d01 = h1(x0)+k1(x2), d02 = h2(x0)+k2(x2) with d01, d02, d12 = d02-d01 in {-1,0,1}, and each cell admitting 0/1 slice values.
A 'row type' is the pair (row of d01, row of d02) at one x0 value. Exhaustive over normalised k1, k2 (spread <= 2):
maximum number of row types (a) overall, (b) when some row depends on x2."""
import itertools
def ok_cell(a, b): return any(all(x in (0, 1) for x in (t, t - a, t - b)) for t in (0, 1))
def rowtypes(k1, k2):
    rows = set()
    for h1 in range(-3, 4):
        for h2 in range(-3, 4):
            r1 = tuple(h1 + k for k in k1); r2 = tuple(h2 + k for k in k2)
            if all(v in (-1, 0, 1) for v in r1 + r2) and all(b - a in (-1, 0, 1) for a, b in zip(r1, r2)) and all(ok_cell(a, b) for a, b in zip(r1, r2)):
                rows.add((r1, r2))
    return rows
R = range(-2, 3)
allmax = max(len(rowtypes(k1, k2)) for k1 in itertools.product(R, repeat=3) for k2 in itertools.product(R, repeat=3))
depmax = max(len(rowtypes(k1, k2)) for k1 in itertools.product(R, repeat=3) for k2 in itertools.product(R, repeat=3) if not (len(set(k1)) == 1 and len(set(k2)) == 1))
print("max row types overall:", allmax, "| when rows depend on x2:", depmax)
