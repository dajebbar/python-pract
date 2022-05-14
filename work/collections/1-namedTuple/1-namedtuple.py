from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, -2)
p1, p2 = p
# print(p1 + p2)

# print(p)

d = p._asdict()
# print(d)

# print(p._replace(x = 4))
# print(p)

Color = namedtuple('Color', ['blue', 'yellow'])
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
pix = Pixel(11, 22, 128, 168)
print(pix)