"""Triangle staircase: hunt for a refutation of the forced functional (2026-10-16).

Setting (see notes/open_questions/cyclic_marginal/pointless_coherence.tex, Prop. "forced functional").
Three slots x0,x1,x2 over N; windows (0,1),(1,2),(2,0); staircase window ultrafilters p(x)p, orientation +++.
Any state extending them must equal Lambda on every finitely built question, where (anchored at base 0)
    Lambda(E) = [z in E] - sum_k [e_k in E] + sum_w [p_w in E]
with z=(0,0,0), e_k = (x_k far, others 0), p_w = (lo far, hi farther, other 0).
Lambda is additive, so it leaves {0,1} on the Dynkin closure IFF two DISJOINT buildable questions both have
Lambda = 1. This script works in the definable sub-carrier at threshold level T (atoms = order types of
(x0,x1,x2) relative to the constants 0..T) and either
  --exact : builds the whole finite Dynkin closure (feasible for T<=1) and checks every set, or
  --hunt  : grows a random pool of buildable questions and tests every new TRUE question for
            disjointness against all known TRUE questions; on success prints a construction certificate.
A refutation is a theorem (no pointless staircase state on the triangle). Passing is evidence only.

Usage:  python3 triangle_lambda_hunt.py --T 2 --hunt --seed 1 --minutes 600
        python3 triangle_lambda_hunt.py --T 1 --exact          (validation: expect 74738 sets, 0 bad)
Parallel on a many-core machine: one process per (T, seed); e.g.
        for T in 2 3 4; do for s in 1 2 3 4; do python3 triangle_lambda_hunt.py --T $T --hunt --seed $s --minutes 720 > hunt_T${T}_s${s}.log & done; done
"""
import argparse, itertools, random, sys, time

def build(T):
    NV = T + 4
    def key(x):
        big = sorted(set(v for v in x if v > T))
        return tuple(v if v <= T else T + 1 + big.index(v) for v in x)
    atoms = sorted({key(x) for x in itertools.product(range(NV), repeat=3)})
    aidx = {a: i for i, a in enumerate(atoms)}
    W = [(0, 1), (1, 2), (2, 0)]
    def ptype(a, i, j):
        u, v = a[i], a[j]
        cu = u if u <= T else 'B'; cv = v if v <= T else 'B'
        return (cu, cv, ((u > v) - (u < v)) if (u > T and v > T) else 0)
    wev = []  # (window index, mask): the single cells of each window (every window question is a
              # disjoint union of these, so they generate the same carrier)
    for wi, (i, j) in enumerate(W):
        types = sorted({ptype(a, i, j) for a in atoms}, key=str)
        for t in types:
            m = 0
            for a in atoms:
                if ptype(a, i, j) == t: m |= 1 << aidx[a]
            wev.append((wi, m))
    f1, f2 = T + 1, T + 2
    def pt(d): return key(tuple(d.get(k, 0) for k in range(3)))
    z = pt({}); e = [pt({k: f1}) for k in range(3)]; p = [pt({a: f1, b: f2}) for (a, b) in W]
    bit = lambda a: 1 << aidx[a]
    zb, eb, pb = bit(z), [bit(x) for x in e], [bit(x) for x in p]
    def Lam(m):
        return (1 if m & zb else 0) - sum(1 for b in eb if m & b) + sum(1 for b in pb if m & b)
    full = (1 << len(atoms)) - 1
    # sanity: Lambda on window events equals the window ultrafilter value
    def u_val(wi, m):
        i, j = W[wi]
        pt_far = pt({i: f1, j: f2})
        return 1 if m & bit(pt_far) else 0
    for wi, m in wev:
        assert Lam(m) == u_val(wi, m), "Lambda disagrees with window ultrafilter"
    C = []
    for (i, j) in W:
        C.append(sum(1 << aidx[a] for a in atoms if a[i] < a[j]))
    return atoms, full, wev, Lam, C

def exact(T):
    atoms, full, wev, Lam, C = build(T)
    D = {m for _, m in wev} | {0, full}
    frontier = list(D); t0 = time.time(); rnd = 0
    while frontier:
        rnd += 1; new = set(); L = list(D)
        for a in frontier:
            c = full ^ a
            if c not in D: new.add(c)
            for b in L:
                if a & b == 0 and (a | b) not in D: new.add(a | b)
        D |= new; frontier = list(new)
        print(f"[exact T={T}] round {rnd}: |D|={len(D)} new={len(new)} {time.time()-t0:.0f}s", flush=True)
    bad = [m for m in D if Lam(m) not in (0, 1)]
    print(f"[exact T={T}] atoms={len(atoms)} |D|={len(D)} bad={len(bad)}", flush=True)

def hunt(T, seed, minutes, poolcap):
    random.seed(seed)
    atoms, full, wev, Lam, C = build(T)
    print(f"[hunt T={T} seed={seed}] atoms={len(atoms)} window events={len(wev)}", flush=True)
    parent = {}            # mask -> construction ('win',wi) | ('not',m) | ('or',a,b)
    pool = []; trues = []
    def add(m, how):
        if m in parent: return None
        parent[m] = how; pool.append(m)
        v = Lam(m)
        if v not in (0, 1): return ('range', m)
        if v == 1:
            for t in trues:
                if t & m == 0: return ('disjoint', t, m)
            trues.append(m)
        return None
    for wi, m in wev:
        r = add(m, ('win', wi))
        if r: return report(r, parent, Lam)
    add(0, ('const', 0)); add(full, ('const', 1))
    t0 = time.time(); steps = 0; last = t0
    while time.time() - t0 < minutes * 60:
        steps += 1
        a = random.choice(pool)
        if random.random() < 0.3:
            r = add(full ^ a, ('not', a))
        else:
            # find a disjoint partner by sampling
            r = None
            for _ in range(40):
                b = random.choice(pool)
                if a & b == 0 and a != b:
                    r = add(a | b, ('or', a, b)); break
        if r: return report(r, parent, Lam)
        if len(pool) > poolcap:
            keep = set(m for _, m in wev) | set(trues[-poolcap // 4:])
            pool = [m for m in pool if m in keep] + random.sample(pool, poolcap // 2)
        now = time.time()
        if now - last > 60:
            print(f"[hunt T={T} seed={seed}] {now-t0:.0f}s steps={steps} pool={len(pool)} "
                  f"known={len(parent)} true={len(trues)}", flush=True)
            last = now
    print(f"[hunt T={T} seed={seed}] NO REFUTATION in {minutes} min; known={len(parent)} true={len(trues)}", flush=True)

def report(r, parent, Lam):
    print("REFUTATION FOUND:", r[0], flush=True)
    def tree(m, depth=0):
        how = parent[m]; pad = '  ' * depth
        print(f"{pad}{m:#x}  Lambda={Lam(m)}  via {how[0]}", flush=True)
        if how[0] == 'not': tree(how[1], depth + 1)
        if how[0] == 'or': tree(how[1], depth + 1); tree(how[2], depth + 1)
    for m in r[1:]: tree(m)
    sys.exit(2)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--T', type=int, default=1)
    ap.add_argument('--exact', action='store_true')
    ap.add_argument('--hunt', action='store_true')
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--minutes', type=float, default=10)
    ap.add_argument('--poolcap', type=int, default=400000)
    a = ap.parse_args()
    if a.exact: exact(a.T)
    else: hunt(a.T, a.seed, a.minutes, a.poolcap)
