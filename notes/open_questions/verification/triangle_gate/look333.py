import itertools, numpy as np, pickle
exec(open('altrank.py').read().split('# B count')[0].replace("n=tuple(int(a) for a in sys.argv[1:4])","n=(3,3,3)").replace("print(","(lambda *a,**k:None)("))
