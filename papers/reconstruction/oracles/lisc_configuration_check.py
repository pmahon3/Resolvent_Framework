"""lisc_configuration_check.py — LISC as a root of unity, and where that stops.

Three checks behind `notes/unsorted/lisc_configuration_space_seed.md`. All of
them use the TRUSTED LISC oracle `raw_lisc_windings` from
`safe_rho_instrument.py`, lifted verbatim at import time rather than
re-derived — that module is POSIX-only (it installs a SIGALRM handler at
import), so the function is extracted from source instead of imported.

  C1  single-cycle soundness.  A simple cycle of length m gives
      LISC_{m/gcd(m,L)}(L), so `some cycle length m has m nmid L` implies L is
      unsafe.  Expect: 0 unsound.

  C2  configuration-space equivalence.  TR_k^(1)(L) reads as: some injective
      k-tuple reaches its own cyclic rotation in L steps, i.e. a periodic point
      of the k-point configuration dynamics whose lag-L map is a k-cycle.
      Expect: 0 mismatches, per-k.

  C3  the deterministic collapse.  A fixed point of sigma^-1 . (T^L)^k
      satisfies u_j = T^L u_{j+1}.  For a FUNCTION that forces every strand
      onto one orbit, so C1 becomes exact; for a relation it does not.
      Expect: exact on every functional rho, incomplete on many others.

Run:  python lisc_configuration_check.py
"""
import io
import itertools
import os
import random
import sys

# ---- the trusted oracle, lifted verbatim ------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = io.open(os.path.join(_HERE, "safe_rho_instrument.py"), encoding="utf-8").read()
_i = _SRC.index("def raw_lisc_windings")
_j = _SRC.index("\n# ---", _i)
_ns = {}
exec(compile(_SRC[_i:_j], "safe_rho_instrument.py:raw_lisc_windings", "exec"), _ns)
raw_lisc_windings = _ns["raw_lisc_windings"]


def simple_cycle_lengths(rel, A):
    out = set()
    for start in range(A):
        stack = [(start, [start], {start})]
        while stack:
            v, path, seen = stack.pop()
            for w in range(A):
                if (v, w) not in rel:
                    continue
                if w == start:
                    out.add(len(path))
                elif w > start and w not in seen:
                    stack.append((w, path + [w], seen | {w}))
    return out


def unsafe(rel, A, Lmax):
    return {L for L in range(1, Lmax + 1) if raw_lisc_windings(rel, A, L, A)}


def single_cycle_pred(rel, A, Lmax):
    cyc = simple_cycle_lengths(rel, A)
    return {L for L in range(1, Lmax + 1) if any(L % m != 0 for m in cyc)}


def config_windings(rel, A, L, kmax):
    """k such that some injective k-tuple reaches its own rotation in L steps."""
    out = set()
    for k in range(2, kmax + 1):
        verts = list(itertools.permutations(range(A), k))
        if not verts:
            continue
        succ = {v: [w for w in verts if all((v[j], w[j]) in rel for j in range(k))]
                for v in verts}
        reach = {v: {v} for v in verts}
        for _ in range(L):
            reach = {v: {y for x in reach[v] for y in succ[x]} for v in verts}
        for v in verts:
            if tuple(v[(j + 1) % k] for j in range(k)) in reach[v]:
                out.add(k)
                break
    return out


def all_rels(A):
    E = [(i, j) for i in range(A) for j in range(A)]
    for m in range(1 << len(E)):
        yield {E[b] for b in range(len(E)) if m >> b & 1}


def functional_rels(A):
    for f in itertools.product(range(A), repeat=A):
        yield {(i, f[i]) for i in range(A)}


def c1(A, Lmax, rels, label):
    unsound = exact = incomplete = 0
    for rel in rels:
        a, p = unsafe(rel, A, Lmax), single_cycle_pred(rel, A, Lmax)
        if not p <= a:
            unsound += 1
        elif p == a:
            exact += 1
        else:
            incomplete += 1
    print("   %-26s n=%-5d unsound=%-3d exact=%-5d incomplete=%d"
          % (label, len(rels), unsound, exact, incomplete))
    return unsound


def c2(A, Lmax, rels, label):
    bad = 0
    for rel in rels:
        for L in range(1, Lmax + 1):
            if raw_lisc_windings(rel, A, L, A) != config_windings(rel, A, L, A):
                bad += 1
    print("   %-26s n=%-5d per-(rho,L) mismatches=%d" % (label, len(rels), bad))
    return bad


if __name__ == "__main__":
    random.seed(0)
    s4 = [set(random.sample([(i, j) for i in range(4) for j in range(4)],
                            random.randint(3, 10))) for _ in range(300)]

    print("C1  single-cycle soundness: some cycle length m with m nmid L => L unsafe")
    bad1 = 0
    bad1 += c1(2, 6, list(all_rels(2)), "|A|=2 exhaustive")
    bad1 += c1(3, 8, list(all_rels(3)), "|A|=3 exhaustive")
    bad1 += c1(4, 8, s4, "|A|=4 sampled")

    print()
    print("C2  configuration-space reading vs the LISC oracle, per winding k")
    bad2 = 0
    bad2 += c2(2, 6, list(all_rels(2)), "|A|=2 exhaustive")
    bad2 += c2(3, 6, list(all_rels(3)), "|A|=3 exhaustive")
    bad2 += c2(4, 5, s4[:120], "|A|=4 sampled")

    print()
    print("C3  the collapse: deterministic rho makes the single-cycle test exact")
    for A in (2, 3, 4):
        c1(A, 8, list(functional_rels(A)), "FUNCTIONAL |A|=%d" % A)
    for A in (2, 3):
        nf = [r for r in all_rels(A)
              if any(sum(1 for j in range(A) if (i, j) in r) > 1 for i in range(A))]
        c1(A, 8, nf, "NON-FUNCTIONAL |A|=%d" % A)

    print()
    print("C1/C2 clean" if bad1 == 0 and bad2 == 0 else "FAILURE -- see above")
