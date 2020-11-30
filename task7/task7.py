#import user defined module
import mod
print(mod.l1)
mod.l1=[i+1 for i in mod.l1]
print(mod.l1)

#pandas package
import pandas as p
d=['h','e','l','l','o']
s=p.Series(d)
print(s)

#random module
import random as r
x=list(range(1,101))
print(r.choice(x))

#sys package & python path
import sys
for p in sys.path:
    print(p)