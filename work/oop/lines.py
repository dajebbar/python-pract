from math import sqrt


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self, other_point):
        other_point = Line(other_point.x, other_point.y)
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

    def distance_2(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def slope(self, other_point):
        other_point = Line(other_point.x, other_point.y)
        return (other_point.y - self.y) / (other_point.x - self.x)

    def slope_2(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)

    def __add__(self, other_point):
        other_point = Line(other_point.x, other_point.y)
        self.x += other_point.x
        self.y += other_point.y

        return self.x, self.y

    def __str__(self):
        return f"Point[{self.x, self.y}]"


# coor1 = Line(3, 2)
# coor2 = Line(8, 10)
coor1 = (3, 2)
coor2 = (8, 10)
coor = Line(coor1, coor2)

print(coor.distance_2())
print(coor.slope_2())

# print(coor1.distance(coor2))
# print(coor1)
