from math import sqrt
class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        formula = self.coor2[1] - self.coor1[1] / sqrt((self.coor2[0] - self.coor1[0])**2 + (cordinate2[1] - cordinate1[1]**2))
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