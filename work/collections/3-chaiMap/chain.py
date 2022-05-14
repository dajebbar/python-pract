from collections import ChainMap

d1 = dict(a=1, b=2)
d2 = dict(c=3, d=4, e=5)
d3 = dict(b=4, f=6, g=7, h=8)

c = ChainMap(d1, d2, d3)
print(c)

for k,v in c.items():
    print(f'{k} : {v}', end=', ')