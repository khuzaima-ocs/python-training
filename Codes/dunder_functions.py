from math import sqrt

class Vector:
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Vector.count += 1

    def __del__(self):
        print("Vector destructed..!")
        Vector.count -= 1
    
    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __len__(self):
        return int(sqrt(pow(self.x, 2) + pow(self.y, 2)))
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y) 

    def __call__(self):
        print(f"{Vector.count} vectors created!")   

    def __lt__(self, other):
        v1 = len(self)
        v2 = len(other)
        return v1 < v2
    
v1 = Vector(10,20)
v2 = Vector(20, 30)

print(f'Length of vector {v1} is {len(v1)}')
v3 = v1 + v2
v4 = v1 - v2

print(f"{v1} + {v2} = {v3}")
print(f"{v1} - {v2} = {v4}")

print(f"{v1} < {v2} = {v1 < v2}")

v4()
del v4
v1()
