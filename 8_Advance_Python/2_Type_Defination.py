'''
type hints or type definatiaon allowsyou to specify the expected type of varialbles, function parameters or return values.
'''

# Type hint for variables.
name: str = 'Hasnain'
age: int = 25
score: float = 85.5
is_student: bool = True

# Type hints for functions parameters and return values.

def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2
result = add_numbers(10, 20)
print(result) # Output: 30

def greet(name: str, age: int) -> str:
    return f"Hello {name}. You are {age} years old."
print(greet("Hasnain", 23)) # Output: Hello Hasnain. You are 23 years old.

# Optional Types

from typing import Optional

def get_full_name(first_name: str, last_name: Optional[str] = None) -> str:
    if last_name:
        return f"{first_name} {last_name}"
    return first_name

print(get_full_name("Hasnain"))           # Output: Hasnain
print(get_full_name("Hasnain", "Nisar"))  # Output: Hasnain Nisar

# Union Type hint is used when a variable or parameter can be of multiple types.
from typing import Union

def get_item_price(price: Union[int, float]) -> float:
    return float(price)

print(get_item_price(100))    # Output: 100.0
print(get_item_price(100.5))  # Output: 100.5

# List, Dict, and Other Container Types

from typing import List, Dict

# List of integers.
numbers: List[int] = [1, 2, 3, 4, 5]

# Dictionary of strings and integers.
student_scores: Dict[str, int] = {
    "Hasnain": 85, 
    "John": 11
    }