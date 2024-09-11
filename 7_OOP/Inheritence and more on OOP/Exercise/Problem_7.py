'''
Override the __len__() method on vector of problem 5 to display the dimension of the 
vector. 
'''

class Vector:
    def __init__(self, *components):
        self.components = list(components)

    # Method to Overload the '+' operator for vector addition.
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        result = [a + b for a,b in zip(self.components, other.components)] 
        return Vector(*result)
    
    # Overloading the '*' operator for dot product
    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        result = sum(a * b for a,b in zip(self.components, other.components)) 
        return result
    
    # Method to display the vector as a string.
    def __str__(self):
        return f"Vector{tuple(self.components)}"
    
    # Method to return the dimension of the vector.
    def __len__(self):
        return len(self.components)
    

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)


# Addition 
v3 = v1 + v2
print(f"Addition: {v3}")

# Multiplication
product = v1 * v2
print(f'Dot Product: {product}')

# Dimension of the vector
print(f"Dimension of v1: {len(v1)}")  # Output: Dimension of v1: 3
print(f"Dimension of v2: {len(v2)}")  # Output: Dimension of v2: 3
