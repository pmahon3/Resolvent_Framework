# Rigorously verify: sigma=(s(a)=1,s(b)=1) is a genuine STATE on MO2
# (additive on orthogonal pairs, s(1)=1, s(0)=0), 2-valued, but NOT a homomorphism.
BOT,A,Ap,B,Bp,TOP='bot','a','ap','b','bp','top'
elts=[BOT,A,Ap,B,Bp,TOP]
ortho={BOT:TOP,TOP:BOT,A:Ap,Ap:A,B:Bp,Bp:B}
def leq(x,y):
    if x==BOT or y==TOP: return True
    if x==TOP: return y==TOP
    if y==BOT: return x==BOT
    return x==y
def meet(x,y):
    if x==BOT or y==BOT: return BOT
    if x==TOP: return y
    if y==TOP: return x
    return x if x==y else BOT
def join(x,y):
    if x==TOP or y==TOP: return TOP
    if x==BOT: return y
    if y==BOT: return x
    return x if x==y else TOP
# orthogonal: x <= y^perp
def orthog(x,y): return leq(x, ortho[y])

s={BOT:0,TOP:1,A:1,Ap:0,B:1,Bp:0}  # sigma=(1,1)

# (1) s(1)=1, s(0)=0
assert s[TOP]==1 and s[BOT]==0
# (2) additive on ALL orthogonal pairs: x _|_ y => s(x join y)=s(x)+s(y)
ok_add=True
for x in elts:
    for y in elts:
        if orthog(x,y):
            if s[join(x,y)]!=s[x]+s[y]:
                ok_add=False; print(f"  ADDITIVITY FAIL: {x} _|_ {y}: s(join)={s[join(x,y)]} vs {s[x]}+{s[y]}")
print(f"(1) normalized s(0)=0,s(1)=1: OK")
print(f"(2) additive on every orthogonal pair: {ok_add}  => genuine STATE")
# (3) 2-valued
print(f"(3) two-valued (s(a) in 0,1 all a): {all(v in (0,1) for v in s.values())}")
# (4) NOT a homomorphism: find a pair where s(x&y)!=s(x)&s(y) or s(xvy)!=s(x)vs(y)
hom=True
for x in elts:
    for y in elts:
        if s[meet(x,y)]!=min(s[x],s[y]) or s[join(x,y)]!=max(s[x],s[y]):
            hom=False
print(f"(4) is a homomorphism (mult on ALL pairs): {hom}")
print(f"    witness: meet(a,b)={meet(A,B)} s=0 but min(s(a),s(b))=min(1,1)=1")
print()
print("CONCLUSION: dispersion-free STATE that is NOT a 2-valued homomorphism.")
print("So 'dispersion-free => homomorphism' is FALSE on MO2. Converse (hom=>df) holds always.")
