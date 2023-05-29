from math import sqrt, pi

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        formula = sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)
        return formula


    def slope(self):
        formula = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        return formula

    def __str__(self):
        return f'distance: {str(self.distance())}\nslope: {str(self.slope())}'


cordinate1 = (3,2)
cordinate2 = (8,10)

li = Line(cordinate1,cordinate2)

print(li)


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        formula = pi * self.radius**2 * self.height
        return formula

    def surface_area(self):
        formula = (2 * pi * self.radius * self.height) + (2 * pi * self.radius**2)
        return formula

    def __str__(self):
        return f'Cylinder height: {self.height}, radius: {self.radius}'


c = Cylinder(12,2.5)
print(c)
print(f"Volume of the cylinder: {c.volume()}")
print(f"Surface area of the cylinder: {c.surface_area()}")
