"""Problem 3 (2026-10-21): is every set in J = closure(relata events u comparison events) pair-local, i.e. a
function of a single pair (x_i, x_j)? If yes, every carrier functional restricted to J is a pair-law probability,
hence >= 0: J is blind to every twist (for every family), explaining Problem 3."""
import itertools, sys
def run(n, rel):
    pts = list(itertools.product(range(n), repeat=3)); N = len(pts); full = (1 << N) - 1
    mask = lambda pred: sum(1 << t for t, p in enumerate(pts) if pred(p))
    def closure(gens):
        D = set(gens) | {0, full}; fr = list(D)
        while fr:
            new = set(); L = list(D)
            for a in fr:
                if full ^ a not in D: new.add(full ^ a)
                for b in L:
                    if a & b == 0 and (a | b) not in D: new.add(a | b)
            D |= new; fr = list(new)
        return D
    E = [(0, 1), (1, 2), (2, 0)]
    rv = sorted({rel(a, b) for a in range(n) for b in range(n)})
    S = {mask(lambda p, i=i, v=v: p[i] == v) for i in range(3) for v in range(n)}
    R = {mask(lambda p, e=e, r=r: rel(p[e[0]], p[e[1]]) == r) for e in E for r in rv}
    J = closure(S | R)
    def pairlocal(m):
        for (i, j) in E:
            ok = True; seen = {}
            for t, p in enumerate(pts):
                key = (p[i], p[j]); v = (m >> t) & 1
                if seen.setdefault(key, v) != v: ok = False; break
            if ok: return True
        return False
    nonlocal_sets = [m for m in J if not pairlocal(m)]
    print(f"n={n}: |J| = {len(J)}, non-pair-local sets: {len(nonlocal_sets)}", flush=True)
    if nonlocal_sets:
        m = nonlocal_sets[0]; print("   example:", [pts[t] for t in range(N) if m >> t & 1][:12])
cmp_ = lambda a, b: (a > b) - (a < b)
for n in map(int, sys.argv[1:] or ["2","3","4"]): run(n, cmp_)
