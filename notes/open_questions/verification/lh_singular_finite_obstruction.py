import numpy as np
import itertools

np.random.seed(0)

# Verify in L(C^2 tensor C^2) = L(C^4). First factor = "H_0" (here finite, dim 2,
# standing in for the infinite-dim H_0); second factor = C^2 carrying the lines.
# a1 = H0 (x) Ce, a1p = H0 (x) Cf, a2 = H0 (x) C(e+f), a2p = H0 (x) C(e-f).

d0 = 2  # dim H0 (toy; the real claim lifts d0 -> infinity)
# C^2 second-factor lines as unit vectors
e  = np.array([1,0], float)
f  = np.array([0,1], float)
v_e  = e
v_f  = f
v_pl = (e+f)/np.sqrt(2)
v_mi = (e-f)/np.sqrt(2)

def subspace_basis(v2):
    # H0 (x) Cv2 : basis {h_i (x) v2} for h_i ranging over H0 basis -> a d0-dim subspace of C^(d0*2)
    cols = []
    for i in range(d0):
        h = np.zeros(d0); h[i]=1
        cols.append(np.kron(h, v2))
    return np.array(cols).T  # columns are basis vectors, shape (d0*2, d0)

A = {
 'a1' : subspace_basis(v_e),
 'a1p': subspace_basis(v_f),
 'a2' : subspace_basis(v_pl),
 'a2p': subspace_basis(v_mi),
}

def dim(B):
    return np.linalg.matrix_rank(B)

def intersection_dim(B1, B2):
    # dim(col(B1) ∩ col(B2)) = dim(B1)+dim(B2) - dim([B1 B2])
    r1, r2 = dim(B1), dim(B2)
    r12 = np.linalg.matrix_rank(np.hstack([B1,B2]))
    return r1 + r2 - r12

def is_orthogonal(B1, B2):
    return np.allclose(B1.T @ B2, 0, atol=1e-10)

print("=== (i) each subspace infinite-dim (here dim = d0 =", d0, ") ===")
for k,B in A.items():
    print(f"  {k}: dim = {dim(B)}")

print("\n=== (ii) pairwise meet (intersection) dimensions ===")
names = list(A)
for x,y in itertools.combinations(names,2):
    idim = intersection_dim(A[x],A[y])
    orth = is_orthogonal(A[x],A[y])
    tag = "ORTHOGONAL" if orth else "meet-zero, NOT orthogonal"
    print(f"  {x} ∩ {y}: dim = {idim}   [{tag}]")

print("\n=== (iii) orthoadditivity pair-sum (state-independent) ===")
print("  a1 ⟂ a1p ?", is_orthogonal(A['a1'],A['a1p']), " and a1 ∨ a1p = H ?",
      np.linalg.matrix_rank(np.hstack([A['a1'],A['a1p']]))==d0*2)
print("  a2 ⟂ a2p ?", is_orthogonal(A['a2'],A['a2p']), " and a2 ∨ a2p = H ?",
      np.linalg.matrix_rank(np.hstack([A['a2'],A['a2p']]))==d0*2)
print("  => s(a1)+s(a1p) = s(H) = 1 and s(a2)+s(a2p) = s(H) = 1")
print("  => Σ = s(a1)+s(a1p)+s(a2)+s(a2p) = 2  for EVERY state (no σ, no normality)")

print("\n\n=== RECONCILIATION: why infinite-dim H0 is load-bearing, not cosmetic ===")
print("In L(C^2) (d0=1): the four atoms are LINES (rank 1, finite-rank).")
d0_finite = 1
def sub1(v2):
    cols=[]
    for i in range(d0_finite):
        h=np.zeros(d0_finite); h[i]=1
        cols.append(np.kron(h,v2))
    return np.array(cols).T
for nm,vv in [('a1',v_e),('a1p',v_f),('a2',v_pl),('a2p',v_mi)]:
    B=sub1(vv)
    print(f"   {nm}: dim = {np.linalg.matrix_rank(B)}  (finite-rank => a SINGULAR state assigns s={0})")
print("   => in C^2, Sigma = 0 for any singular state: NO obstruction, NO singular states even exist.")
print("   => the C^2 count only bites states nonzero on finite rank = NORMAL states = Prop 3.4 territory.")
print("   => infinite-dim H0 makes the atoms infinite-dim, so orthoadditivity forces")
print("      s(a_i)+s(a_i^perp)=s(1)=1 REGARDLESS of behaviour on finite rank => reaches singular states.")
