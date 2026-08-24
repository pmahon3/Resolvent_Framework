"""safe_rho_instrument.py — THE INSTRUMENT (Theorem 1 of the shovel plan).

Computes, for a relation rho, the exact eventual-periodicity CERTIFICATE for
Safe(rho): per-k minimal (s_k, p_k) via Boolean-power repeat-search on the
injective-tuple tensor digraph T_k (Theorem B), the union certificate
(S, P, exact prefix, residue table), where per Theorem P
(papers/reconstruction/notes/pruning_theorem_and_B.md)

    LISC_k(L)  <=>  TR_k^{(1)}(L)   (rotation by a GENERATOR; rot-1 canonical)

so Unsafe(rho) = U_{k=2}^{|A|} TR_k^{(1)} and Safe(rho) = its complement.

ANCHOR DISCIPLINE: raw-DFS LISC (the ONLY trusted LISC oracle; independent
code path, copied from pruning_lemma_hunt.py) is recomputed for every L in the
anchor window and compared PER-K (winding sets, not just the union). Any
mismatch = FAIL, no certificate is emitted for that target. Coverage is logged
explicitly — if the anchor window does not cross S + P, that is PRINTED, never
silent.
"""
import signal
import sys
from itertools import permutations, product
from math import lcm

# ---------------------------------------------------------------- raw DFS ----
# Trusted LISC oracle (pruning_lemma_hunt.py lineage): enumerate simple cycles
# of the layered ring over Z_L, collect windings k >= 2, verify
# layer-injectivity explicitly (defensive; it is implied by simplicity).

def raw_lisc_windings(rel, A, L, kmax):
    adj = {}
    for i in range(L):
        for s in range(A):
            adj[(i, s)] = [((i + 1) % L, t) for t in range(A) if (s, t) in rel]
    out = set()

    def dfs(start, cur, path, visited):
        for nx in adj[cur]:
            if nx == start and len(path) >= L:
                if len(path) % L == 0:
                    k = len(path) // L
                    if 2 <= k <= kmax and k not in out:
                        bylayer = {}
                        for (i, s) in path:
                            bylayer.setdefault(i, []).append(s)
                        if all(len(v) == len(set(v)) for v in bylayer.values()):
                            out.add(k)
            elif nx not in visited and len(path) < min(kmax, A) * L:
                visited.add(nx)
                path.append(nx)
                dfs(start, nx, path, visited)
                path.pop()
                visited.discard(nx)

    for s0 in range(A):
        start = (0, s0)
        dfs(start, start, [start], {start})
    return out

# ------------------------------------------------- Boolean-power machinery ----

def tuple_digraph(rel, A, k):
    """Injective k-tuples; arcs coordinatewise in rel, target injective.
    Returns (tuples, idx, rows-as-bitmasks)."""
    tuples = list(permutations(range(A), k))
    idx = {u: i for i, u in enumerate(tuples)}
    outn = {a: [b for b in range(A) if (a, b) in rel] for a in range(A)}
    rows = []
    for u in tuples:
        row = 0
        for v in product(*(outn[a] for a in u)):
            if len(set(v)) == k:
                row |= 1 << idx[v]
        rows.append(row)
    return tuples, idx, tuple(rows)

def bool_matmul(Arows, Brows, N):
    out = []
    for i in range(N):
        r, a = 0, Arows[i]
        while a:
            j = (a & -a).bit_length() - 1
            r |= Brows[j]
            a &= a - 1
        out.append(r)
    return tuple(out)

def tr_k_certificate(rel, A, k, cap=4096):
    """Minimal (s, p) for the power sequence of T_k's Boolean matrix, plus the
    TR_k^{(1)} predicate values for L = 1 .. s+p (enough to evaluate all L).
    Returns (s, p, pred) with pred[L] for 1 <= L <= s+p, or None past cap."""
    tuples, idx, M = tuple_digraph(rel, A, k)
    N = len(tuples)
    sig = [idx[u[1:] + u[:1]] for u in tuples]  # sigma_1 = left rotation

    def predicate(rows):
        return any((rows[i] >> sig[i]) & 1 for i in range(N))

    seen = {}
    powers = [tuple(1 << i for i in range(N))]  # M^0 = I
    seen[powers[0]] = 0
    cur = powers[0]
    for L in range(1, cap + 1):
        cur = bool_matmul(cur, M, N)
        if cur in seen:
            s, p = seen[cur], L - seen[cur]
            pred = {t: predicate(powers[t]) for t in range(1, L)}
            pred[L] = predicate(cur)
            return s, p, pred
        seen[cur] = L
        powers.append(cur)
    return None  # cap exceeded (log upstream; never silent)

def tr_value(certk, L):
    s, p, pred = certk
    if L <= s + p:
        return pred[L]
    return pred[s + 1 + ((L - s - 1) % p)]

# ----------------------------------------------------------------- targets ----
TARGETS = {
    "NAND/golden": ({(0, 0), (0, 1), (1, 0)}, 12),
    "full2":       ({(0, 0), (0, 1), (1, 0), (1, 1)}, 12),
    "rho13":       ({(0, 0), (0, 1), (1, 2), (2, 0)}, 15),
    "rho5":        ({(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)}, 12),
    "tournament3": ({(0, 1), (1, 2), (2, 0)}, 12),
    "full3":       (set(product(range(3), repeat=2)), 8),
    "mixed":       ({(0, 1), (1, 2), (1, 3), (2, 0), (3, 0)}, 10),
    "C4tgt":       ({(0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (3, 2), (3, 0), (0, 3)}, 9),
    "C4dir":       ({(0, 1), (1, 2), (2, 3), (3, 0)}, 10),
    "adv1":        ({(0, 1), (1, 0), (1, 2), (2, 1), (2, 3), (3, 0)}, 10),
    "adv2":        ({(0, 1), (1, 0), (1, 2), (2, 0), (0, 3), (3, 1)}, 17),
    "adv3":        ({(0, 1), (1, 0), (0, 2), (2, 1), (1, 3), (3, 0)}, 17),
    "adv4":        ({(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)}, 21),
    "adv5":        ({(0, 1), (1, 2), (2, 0), (2, 3), (3, 1)}, 10),
    "rho20(2c+3c, not SC)": ({(0, 1), (1, 0), (2, 3), (3, 4), (4, 2)}, 8),
}

class TO(Exception):
    pass

def _handler(sig, frm):
    raise TO()

signal.signal(signal.SIGALRM, _handler)
PER_L_WALL = 60  # seconds per raw-DFS anchor point

def run_target(name, rel, Lanchor):
    A = 1 + max(max(a, b) for (a, b) in rel)
    certs = {}
    for k in range(2, A + 1):
        c = tr_k_certificate(rel, A, k)
        if c is None:
            print(f"[{name}] k={k}: power-repeat CAP EXCEEDED — no certificate")
            return False
        certs[k] = c
    S = max(c[0] for c in certs.values())
    P = lcm(*(c[1] for c in certs.values()))

    def unsafe(L):
        return any(tr_value(certs[k], L) for k in certs)

    # ---- anchor: per-k winding sets vs raw DFS, every L in window ----
    fails, covered = [], []
    for L in range(1, Lanchor + 1):
        signal.alarm(PER_L_WALL)
        try:
            raw = raw_lisc_windings(rel, A, L, A)
            signal.alarm(0)
        except TO:
            print(f"[{name}] raw-DFS wall at L={L} — anchor window truncated "
                  f"to L<={L-1} (EXPLICIT, not silent)")
            Lanchor = L - 1
            break
        covered.append(L)
        pred = {k for k in certs if tr_value(certs[k], L)}
        if pred != raw:
            fails.append((L, sorted(pred), sorted(raw)))
    if fails:
        print(f"[{name}] *** ANCHOR FAIL *** (L, predicted, raw): {fails}")
        return False

    crosses = Lanchor >= S + P
    prefix_safe = [L for L in range(1, S + 1) if not unsafe(L)]
    residues_safe = sorted(r for r in range(P) if not unsafe(S + 1 + r))
    perk = ", ".join(f"k={k}:(s={c[0]},p={c[1]})" for k, c in certs.items())
    print(f"[{name}] A={A}  {perk}")
    print(f"    CERTIFICATE: S={S} P={P}; Safe prefix(1..{S})={prefix_safe}; "
          f"Safe residues of L-{S + 1} mod {P} on L>{S}: {residues_safe}")
    print(f"    ANCHOR: per-k EXACT match vs raw DFS on L=1..{Lanchor} "
          f"({len(covered)} pts){' — window CROSSES S+P' if crosses else f' — window does NOT cross S+P={S + P} (partial anchor, logged)'}")
    return True

if __name__ == "__main__":
    ok = True
    for name, (rel, La) in TARGETS.items():
        ok &= run_target(name, frozenset(rel), La)
        print()
    print("=== ALL TARGETS ANCHORED, certificates emitted ===" if ok
          else "=== AT LEAST ONE FAILURE — see above; NO trust ===")
    sys.exit(0 if ok else 1)
