from math import pi


class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return round(pi * self.radius**2 * self.height, 2)
    
    def surface_area(self):
        return round(2 * pi * self.radius * self.height + 2 * pi * self.radius**2, 2)


c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())