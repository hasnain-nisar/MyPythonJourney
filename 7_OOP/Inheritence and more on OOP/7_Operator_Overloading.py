class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)
print(n + m)

# Another Example

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the plus operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    

# Create two point object.
p1 = Point(2, 3)
p2 = Point(4, 5)

# Using the overload + operator.
p3 = p1 + p2

print(p3)