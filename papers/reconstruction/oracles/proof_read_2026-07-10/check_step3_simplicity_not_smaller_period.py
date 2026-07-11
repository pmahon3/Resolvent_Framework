"""Step 3 claims the assembled W (length kL) is simple, hence 'a simple cycle
of winding k'. A simple cycle by definition (line 32: 'all of whose vertices
distinct') already forces length = true minimal period of the closed walk --
if all kL vertices are distinct, the walk cannot repeat with any smaller
period naturally (a walk of true period m|kL would revisit vertices unless
m=kL). So 'winding k' claim is fine BY the simplicity already proved in Step 3
(no separate primitivity gap) -- but let's confirm no assembly could produce
a closed walk with a repeated vertex that the proof's argument overlooks, by
directly re-deriving Step 3's assembled walk for TR examples and checking
simplicity by brute force (not trusting the proof's own injectivity argument)."""
from itertools import permutations, product

def build_and_check_assembly(rel, A, k, L):
    """Find a TR_k^(1)(L) witness (tau_0 ... tau_L) if any, assemble W per
    Step 3, and check simplicity directly + that it's a closed walk of length kL
    consistent with the ring adjacency."""
    tuples = list(permutations(range(A), k))
    outn = {a:[b for b in range(A) if (a,b) in rel] for a in range(A)}
    def succs(u):
        return [v for v in product(*(outn[a] for a in u)) if len(set(v))==k]
    def sigma1(u):
        return u[1:] + u[:1]
    # BFS to find a walk tau_0..tau_L with tau_L = sigma1(tau_0)
    # track paths (small state spaces)
    for start in tuples:
        frontier = {start: [start]}
        for step in range(L):
            nxt = {}
            for u, path in frontier.items():
                for v in succs(u):
                    if v not in nxt:
                        nxt[v] = path + [v]
            frontier = nxt
            if not frontier:
                break
        target = sigma1(start)
        if target in frontier:
            taus = frontier[target]  # tau_0 .. tau_L
            # Assemble W: position t = jL+i -> vertex (i, taus[i][j])
            W = []
            for j in range(k):
                for i in range(L):
                    W.append((i, taus[i][j]))
            # check closed walk: consecutive arcs in R_L(rel), and wraps to W[0]
            ring_ok = True
            for t in range(len(W)):
                (i1,s1) = W[t]
                (i2,s2) = W[(t+1)%len(W)]
                if i2 != (i1+1)%L or (s1,s2) not in rel:
                    ring_ok = False
            simple = (len(set(W)) == len(W))
            length_ok = (len(W) == k*L)
            print(f"  A={A} k={k} L={L}: found witness. |W|={len(W)}=kL:{length_ok} "
                  f"ring-consistent:{ring_ok} simple:{simple}")
            return
    print(f"  A={A} k={k} L={L}: no TR^(1) witness found")

# Stress on several graphs incl. ones with extra structure that might tempt
# a bad assembly (repeated states across strands could in principle collide
# if injectivity failed -- test on denser graphs)
TARGETS = [
    ({(0,1),(1,2),(2,3),(3,0)}, 4, 2, 2),   # C4dir, k=2,L=2
    ({(0,1),(1,2),(2,3),(3,0)}, 4, 4, 4),   # C4dir, k=4,L=4
    (set(product(range(4),repeat=2)), 4, 3, 3),  # full4, k=3,L=3 (dense, many collisions possible)
    (set(product(range(5),repeat=2)), 5, 4, 2),  # full5, k=4,L=2
    ({(0,1),(1,0),(1,2),(2,0),(0,3),(3,1)}, 4, 3, 5),  # adv2, k=3,L=5
]
for rel,A,k,L in TARGETS:
    build_and_check_assembly(rel, A, k, L)
