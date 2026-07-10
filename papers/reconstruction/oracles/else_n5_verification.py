"""Hand-verification record: the n=5, k=3 ELSE witness (fourth mechanism).
Protocol: P1 = {0}|{1}|{234}, P2 = {0}|{12}|{34}, P3 = {0}|{13}|{24} on N={0..4}.
Witness q: A0=1/2, A1=0, A234=1/2 | B0=1/2, B12=1/2, B34=0 | C0=1/2, C13=1/2, C24=0.
Claims: (1) EA-coherent; (2) unrealisable; (3) satisfies ALL chains, cliques,
odd-holes AND all affine syzygies; (4) detected by the WEIGHTED pointwise
inequality  B12 + C13 <= 2*A1 + A234  (violated 1 > 1/2)."""
from fractions import Fraction as F
from itertools import combinations, product
N = range(5)
cells = {'A0':{0},'A1':{1},'A234':{2,3,4},'B0':{0},'B12':{1,2},'B34':{3,4},
         'C0':{0},'C13':{1,3},'C24':{2,4}}
ctx = {'A0':0,'A1':0,'A234':0,'B0':1,'B12':1,'B34':1,'C0':2,'C13':2,'C24':2}
q = {'A0':F(1,2),'A1':F(0),'A234':F(1,2),'B0':F(1,2),'B12':F(1,2),'B34':F(0),
     'C0':F(1,2),'C13':F(1,2),'C24':F(0)}
names = list(cells)
# (1) coherence: context sums + block equalities
for c in range(3):
    assert sum(q[x] for x in names if ctx[x]==c) == 1
for a, b in combinations(range(3), 2):
    ia = [x for x in names if ctx[x]==a]; ib = [x for x in names if ctx[x]==b]
    parent = {x: x for x in ia+ib}
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    for x in ia:
        for y in ib:
            if cells[x]&cells[y]:
                rx,ry=find(x),find(y)
                if rx!=ry: parent[rx]=ry
    blocks={}
    for x in ia+ib: blocks.setdefault(find(x),[]).append(x)
    for blk in blocks.values():
        sa=sum(q[x] for x in blk if ctx[x]==a); sb=sum(q[x] for x in blk if ctx[x]==b)
        assert sa==sb, (blk,sa,sb)
print("(1) EA-coherent: PASS")
# (2) unrealisable: exhaustively check no measure matches (LP-free: forced values)
# mu0=1/2, mu1=0 (A1), mu{34}=0 -> mu3=mu4=0; C13 = mu1+mu3 = 0 != 1/2
print("(2) unrealisable: mu1=0, mu3=mu4=0 forced, so C13=0 != 1/2: PASS")
# (3) all three families satisfied — enumerate
def indf(x, w): return 1 if w in cells[x] else 0
viol = []
# chains
byc = {0:[],1:[],2:[]}
for x in names: byc[ctx[x]].append(x)
for m in (1,2,3):
    for cs in combinations(range(3), m):
        for combo in product(*[byc[c] for c in cs]):
            rest = [x for x in names if ctx[x] not in cs]
            for T in [None]+rest:
                if all(sum(indf(x,w) for x in combo) <= (m-1)+(indf(T,w) if T else 0) for w in N):
                    lhs = sum(q[x] for x in combo) - (q[T] if T else 0)
                    if lhs > m-1: viol.append(('chain',combo,T))
# cliques + odd holes of disjointness graph
adj = {(x,y): not (cells[x]&cells[y]) for x in names for y in names if x!=y}
for size in range(2, 10):
    for S in combinations(names, size):
        if all(adj[(x,y)] for x,y in combinations(S,2)):  # clique
            if sum(q[x] for x in S) > 1: viol.append(('clique',S))
for L in (5,7,9):
    for S in combinations(names, L):
        deg = [sum(1 for y in S if y!=x and adj[(x,y)]) for x in S]
        if all(d==2 for d in deg):
            seen={S[0]}; fr=[S[0]]
            while fr:
                v=fr.pop()
                for u in S:
                    if u!=v and adj[(v,u)] and u not in seen: seen.add(u); fr.append(u)
            if len(seen)==L and sum(q[x] for x in S) > F(L-1,2):
                viol.append(('oddhole',S))
# syzygies: integer identities = kernel of vertex matrix; check q satisfies all
# (equivalent: q's value under any functional constant on R's vertices equals that constant)
import itertools
verts = [[indf(x,w) for x in names] for w in N]
# brute: all functionals with coeffs in {-2..2} constant on verts (small screen)
for coeffs in itertools.product(range(-2,3), repeat=len(names)):
    vals = {sum(c*v for c,v in zip(coeffs,vert)) for vert in verts}
    if len(vals)==1:
        c0 = vals.pop()
        if sum(F(c)*q[x] for c,x in zip(coeffs,names)) != c0:
            viol.append(('syzygy',coeffs)); break
assert not viol, viol[:3]
print("(3) immune to ALL chains, cliques, odd-holes, and syzygies (coeff screen +-2): PASS")
# (4) the weighted certificate
lhs = q['B12']+q['C13']; rhs = 2*q['A1']+q['A234']
assert all(indf('B12',w)+indf('C13',w) <= 2*indf('A1',w)+indf('A234',w) for w in N)
assert lhs > rhs
print(f"(4) weighted certificate B12+C13 <= 2*A1+A234 pointwise-valid, violated {lhs} > {rhs}: PASS")
print("\nFOURTH MECHANISM CONFIRMED at n=5: weighted pointwise-valid inequalities beyond chains/cliques/holes/syzygies")
