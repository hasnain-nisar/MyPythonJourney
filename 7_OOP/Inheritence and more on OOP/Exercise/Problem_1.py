# Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method to display 2D vector.
    def display(self):
        print(f'2D vector: ({self.x}, {self.y})')


# Crete a 3D vector class inheriting from Vector2D
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        # Call the constructor of Vector2D to initialize x and y
        super().__init__(x, y)
        self.z = z # z component

    # Method to display thr 3D vector.
    def display(self):
        print(f"3D vector: ({self.x}, {self.y}, {self.z})")

#Create a 2D vector
v2d = Vector2D(1, 2)
v2d.display()

# Create a 3D vector
v3d = Vector3D(4, 5, 6)
v3d.display()