# Features Highlighted
# Basic and Advanced Function Concepts: Parameters, default values, and type annotations.
# Functional Programming: Higher-order functions, lambdas, closures, and decorators.
# Data Science-Ready: Generators and recursive solutions.
# Practical Examples:
# Dictionary of operations.
# Pass-by-reference scenarios.
# Exception handling.
# Code Readability: Includes a docstring example for professional documentation.

# functions_demo.py

# 1. Basic Function
print("1. Basic Function")
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 2. Function with Default Parameters
print("\n2. Function with Default Parameters")
def introduce(name, age=30):
    return f"My name is {name}, and I am {age} years old."

print(introduce("Bob"))
print(introduce("Charlie", 25))

# 3. Function with Arbitrary Arguments (*args)
print("\n3. Function with Arbitrary Arguments (*args)")
def sum_numbers(*args):
    return sum(args)

print("Sum:", sum_numbers(1, 2, 3, 4, 5))

# 4. Function with Arbitrary Keyword Arguments (**kwargs)
print("\n4. Function with Arbitrary Keyword Arguments (**kwargs)")
def describe_person(**kwargs):
    return ", ".join(f"{key}: {value}" for key, value in kwargs.items())

print(describe_person(name="Alice", age=30, city="New York"))

# 5. Lambda Function
print("\n5. Lambda Function")
square = lambda x: x ** 2
print("Square of 5:", square(5))

# 6. Higher-Order Function (Passing Functions as Arguments)
print("\n6. Higher-Order Function")
def apply_function(func, value):
    return func(value)

print("Double of 10:", apply_function(lambda x: x * 2, 10))

# 7. Recursive Function
print("\n7. Recursive Function")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# 8. Function with Type Annotations
print("\n8. Function with Type Annotations")
def multiply(a: int, b: int) -> int:
    return a * b

print("Multiply 3 and 4:", multiply(3, 4))

# 9. Closure (Function within a Function)
print("\n9. Closure Example")
def multiplier(factor):
    def multiply_by_factor(number):
        return number * factor
    return multiply_by_factor

double = multiplier(2)
print("Double of 6:", double(6))

# 10. Decorator
print("\n10. Decorator Example")
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

print("Add 3 and 7:", add(3, 7))

# 11. Generator Function
print("\n11. Generator Function")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("First 5 Fibonacci numbers:", list(fibonacci(5)))

# 12. Function as a Dictionary Value
print("\n12. Function as a Dictionary Value")
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else "Division by zero"
}

print("Add 5 and 3:", operations["add"](5, 3))
print("Divide 10 by 0:", operations["divide"](10, 0))

# 13. Function to Modify a List (Pass by Reference)
print("\n13. Function to Modify a List (Pass by Reference)")
def append_element(lst, element):
    lst.append(element)

my_list = [1, 2, 3]
append_element(my_list, 4)
print("Modified List:", my_list)

# 14. Function with Variable Scope
print("\n14. Function with Variable Scope")
x = 10

def modify_variable():
    global x
    x += 5

modify_variable()
print("Global x after modification:", x)

# 15. Function with a Docstring
print("\n15. Function with a Docstring")
def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b

print("Sum of 8 and 2:", add_numbers(8, 2))
print("Function docstring:", add_numbers.__doc__)

# 16. Function with Exception Handling
print("\n16. Function with Exception Handling")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print("Divide 10 by 2:", safe_divide(10, 2))
print("Divide 10 by 0:", safe_divide(10, 0))

# End of examples
print("\nAll function examples executed successfully!")
