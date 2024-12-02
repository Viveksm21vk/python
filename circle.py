class Circle:
    def __init__(self,radius):
        self.radius = radius
    def __sub__(self,other):
        return self.radius - other.radius
    def __str__(self):
        print("self.radius")
c1 = Circle(100)
c2 = Circle(20)
c3 = c1 - c2
print(type(c3))
print(c1)
print(c2)