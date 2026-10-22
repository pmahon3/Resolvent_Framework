"""Exact closure of the r x 3 x 3 step (2026-10-21, after review). Enumerate every possible remainder R' at coarse size
c0 x 3 x 3 (c0 <= 4 row types depending on x2; forced slice values off the agreement cells) and test EXACT membership
in genuinely buildable sets: the exact carrier when c0 <= 3, and for c0 = 4 the pullbacks of exact small carriers
(product <= 27) through coordinatewise set-partition maps. No ray enumeration, no LP."""
import itertools, sys
sys.argv = ['x', '2,2,2']
exec(open('cone_D_pullback_lp.py').read().split('def rays_of')[0])
def ok_cell(a, b): return any(all(x in (0, 1) for x in (t, t - a, t - b)) for t in (0, 1))
def forced(a, b): return [t for t in (0, 1) if all(x in (0, 1) for x in (t, t - a, t - b))][0]
def rowtypes(k1, k2):
    rows = set()
    for h1 in range(-3, 4):
        for h2 in range(-3, 4):
            r1 = tuple(h1 + k for k in k1); r2 = tuple(h2 + k for k in k2)
            if all(v in (-1, 0, 1) for v in r1 + r2) and all(b - a in (-1, 0, 1) for a, b in zip(r1, r2)) and all(ok_cell(a, b) for a, b in zip(r1, r2)):
                rows.add((r1, r2))
    return sorted(rows)
Rr = range(-2, 3); targets = {}   # coarse size c0 -> set of masks
for k1 in itertools.product(Rr, repeat=3):
    for k2 in itertools.product(Rr, repeat=3):
        if len(set(k1)) == 1 and len(set(k2)) == 1: continue
        rows = rowtypes(k1, k2)
        for c0 in range(1, min(4, len(rows)) + 1):
            for chosen in itertools.combinations(rows, c0):
                pts = list(itertools.product(range(c0), range(3), range(3)))
                m = 0
                for t, (x0, x1, x2) in enumerate(pts):
                    a, b = chosen[x0][0][x2], chosen[x0][1][x2]
                    if a == 0 and b == 0: continue          # agreement cell: belongs to the common part
                    t0 = forced(a, b); vals = (t0, t0 - a, t0 - b)
                    if vals[x1] == 1: m |= 1 << t
                targets.setdefault(c0, set()).add(m)
print({c: len(v) for c, v in targets.items()}, "distinct remainders R' by coarse size", flush=True)
def partitions(n, m):
    out = []
    for f in itertools.product(range(m), repeat=n):
        if len(set(f)) == m and [f.index(b) for b in range(m)] == sorted(f.index(b) for b in range(m)): out.append(f)
    return out
ok_all = True
for c0, T in sorted(targets.items()):
    sz = (c0, 3, 3); pts = list(itertools.product(range(c0), range(3), range(3)))
    if c0 <= 3:
        _, D = carrier(sz); good = T <= D
        print(f"c0={c0}: exact carrier |D|={len(D)}; all {len(T)} remainders in D: {good}", flush=True)
    else:
        supply = set()
        for small in [(3, 3, 3), (4, 2, 3), (4, 3, 2), (4, 2, 2), (2, 3, 3), (3, 2, 3), (3, 3, 2)]:
            ptsS, DS = carrier(small); iS = {p: t for t, p in enumerate(ptsS)}
            for fm in itertools.product(*[partitions(sz[k], small[k]) for k in range(3)]):
                img = [iS[(fm[0][p[0]], fm[1][p[1]], fm[2][p[2]])] for p in pts]
                for S in DS: supply.add(sum(1 << t for t in range(len(pts)) if (S >> img[t]) & 1))
        missing = [m for m in T if m not in supply]
        good = not missing
        print(f"c0=4: supply {len(supply)}; remainders {len(T)}; NOT in supply: {len(missing)}", flush=True)
    ok_all = ok_all and good
print("ALL remainders exactly buildable:", ok_all)
