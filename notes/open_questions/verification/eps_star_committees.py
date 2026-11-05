# Iteration 2: eps* for the 3x4x4 committees family (intuition_kit.tex §3): each pair law uniform 1/9 on 9 allowed pairs.
import itertools, numpy as np
from scipy.optimize import linprog
XY={0:[0,1,2],1:[0,1,3],2:[1,2,3]}          # X-Y acceptable
YZ={0:[1,2],1:[0,1,3],2:[0,2],3:[2,3]}      # Y-Z acceptable
ZX={0:[0,1],1:[0,2],2:[0,1,2],3:[1,2]}      # Z-X acceptable
sizes=(3,4,4)
P=[{(x,y):(1/9 if y in XY[x] else 0) for x in range(3) for y in range(4)},
   {(y,z):(1/9 if z in YZ[y] else 0) for y in range(4) for z in range(4)},
   {(z,x):(1/9 if x in ZX[z] else 0) for z in range(4) for x in range(3)}]
for k in range(3): assert abs(sum(P[k].values())-1)<1e-12
pairs=[(0,1),(1,2),(2,0)]
pts=list(itertools.product(range(3),range(4),range(4))); nq=len(pts)
cellsets=[list(P[k].keys()) for k in range(3)]; nt=sum(len(c) for c in cellsets); n=nq+nt+1
c=np.zeros(n); c[-1]=1; A=[];b=[]; off=nq
for k,(i,j) in enumerate(pairs):
    for m,cell in enumerate(cellsets[k]):
        row=np.zeros(n)
        for a,x in enumerate(pts):
            if (x[i],x[j])==cell: row[a]=1
        ti=off+m
        r1=row.copy(); r1[ti]=-1; A.append(r1); b.append(P[k][cell])
        r2=-row; r2[ti]=-1; A.append(r2); b.append(-P[k][cell])
    r=np.zeros(n); r[off:off+len(cellsets[k])]=.5; r[-1]=-1; A.append(r); b.append(0)
    off+=len(cellsets[k])
res=linprog(c,A_ub=A,b_ub=b,A_eq=[[1]*nq+[0]*(nt+1)],b_eq=[1],bounds=[(0,None)]*n)
print("committees 3x4x4 hidden twist: eps* =",round(res.fun,6))
# exact rational guess
from fractions import Fraction
print("as fraction (limit_denominator 200):",Fraction(res.fun).limit_denominator(200))
