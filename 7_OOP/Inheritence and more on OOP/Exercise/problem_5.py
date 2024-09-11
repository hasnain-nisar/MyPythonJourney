'''
Write a class vector representing a vector of n dimensions. Overload the + and * 
operator which calculates the sum and the dot(.) product of them.
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
    

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)


# Addition 
v3 = v1 + v2
print(f"Addition: {v3}")

# Multiplication
product = v1 * v2
print(f'Dot Product: {product}')


# Another way of doing this problem which is more easy.

# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result
    
#     def __mul__(self, other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result
    
#     def __str__(self):
#         return f"Vector({self.x}, {self.y}, {self.z})"
    
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(11, 22, 33)

# # Addition 
# v = v1 + v2 + v3
# print(f"Addition: {v}")

# # Dot Product - Pairwise
# product_v1_v2 = v1 * v2
# product_v1_v3 = v1 * v3
# product_v2_v3 = v2 * v3

# print(f'Dot Product v1 * v2: {product_v1_v2}')  # Output: 32
# print(f'Dot Product v1 * v3: {product_v1_v3}')  # Output: 154
# print(f'Dot Product v2 * v3: {product_v2_v3}')  # Output: 352
