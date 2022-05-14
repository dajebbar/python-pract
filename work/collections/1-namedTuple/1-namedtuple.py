from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, -2)
p1, p2 = p
# print(p1 + p2)

# print(p)

d = p._asdict()
print(d)