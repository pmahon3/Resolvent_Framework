import itertools
A=3
pts=list(itertools.product(range(A),repeat=3))
face=[x for x in pts if 0 in x]; inner=[x for x in pts if 0 not in x]
count=0
for bits in itertools.product((0,1),repeat=len(face)):
    f=dict(zip(face,bits)); ok=True
    for (a,b,c) in inner:  # zero interaction with anchor 0: f(a,b,c)= sum of lower terms
        v=(f[(a,b,0)]+f[(a,0,c)]+f[(0,b,c)]-f[(a,0,0)]-f[(0,b,0)]-f[(0,0,c)]+f[(0,0,0)])
        if v not in (0,1): ok=False; break
        f[(a,b,c)]=v
    count+=ok
print('0/1 functions in span V at A=3:',count,' (carrier D has 15914)')
