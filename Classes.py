

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coordS = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __str__(self, ):
        return "(" + str(self.x) + ',' + str(self.y) + ')'


p1 = Point(3,4)
p2 = Point(7,9)
p3 = Point(2,1)
p4 = Point(5,2)
p5 = p1 + p2
p6 = p4 - p3
p7 = p2*p3

print(p5, p6, p7)

