'''
 Write a class 'Complex' to represent complex numbers, along with overloaded 
operators '+' and '*' which adds and multiplies them.
'''

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    # Overloading the '+' operator for complex number addition
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)
    
    # Overloading the '*' operator for complex number multiplication
    def __mul__(self, other):
        real_part = (self.r * other.r) - (self.i * other.i)
        img_part = (self.r * other.i) + (self.i * other.r)
        return Complex(real_part, img_part) 
    
    # Method to display the complex number
    def __str__(self):
        return f"{self.r} + {self.i}i"
    

# Example usage:
c1 = Complex(2, 3)  # 2 + 3i
c2 = Complex(1, 4)  # 1 + 4i

# Add two complex numbers
c3 = c1 + c2  # (2 + 3i) + (1 + 4i)
print(f"Addition: {c3}")  # Output: 3 + 7i

# Multiply two complex numbers
c4 = c1 * c2  # (2 + 3i) * (1 + 4i)
print(f"Multiplication: {c4}")  # Output: -10 + 11i