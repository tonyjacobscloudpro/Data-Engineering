# Features Highlighted:
# Basic Counter Loops: Demonstrates increment and iteration logic.
# Conditionals (break/continue): Breaks out of loops or skips iterations.
# Iterating Structures: Loops through lists, dictionaries, and zipped structures.
# User Inputs: Includes commented examples for interactive loops.
# Advanced Constructs: Demonstrates usage of all(), any(), and nested loops.
# You can expand on these examples with more scenarios tailored to specific use cases. Let me know if you want additional examples!

# loop_conditions.py

# 1. Basic while loop with a counter
print("1. Basic while loop with a counter")
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# 2. Infinite loop with a break condition
print("\n2. Infinite loop with a break condition")
n = 0
while True:
    print(f"n: {n}")
    n += 1
    if n >= 5:
        break

# 3. For loop with a range
print("\n3. For loop with a range")
for i in range(5):
    print(f"i: {i}")

# 4. Loop with continue statement
print("\n4. Loop with continue statement")
for i in range(5):
    if i == 2:
        continue
    print(f"i: {i}")

# 5. Loop over a list
print("\n5. Loop over a list")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"Fruit: {fruit}")

# 6. Loop over a dictionary
print("\n6. Loop over a dictionary")
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")

# 7. Nested loops
print("\n7. Nested loops")
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# 8. Using else with a loop
print("\n8. Using else with a loop")
for i in range(5):
    print(f"i: {i}")
else:
    print("Loop completed without interruption.")

# 9. Using a flag variable in a loop
print("\n9. Using a flag variable in a loop")
found = False
for num in range(10):
    if num == 7:
        found = True
        break
if found:
    print("Number 7 found in the range!")

# 10. Loop with enumeration
print("\n10. Loop with enumeration")
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")

# 11. Loop with zip
print("\n11. Loop with zip")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# 12. While loop with a user input condition (commented to avoid blocking execution)
# print("\n12. While loop with a user input condition")
# while True:
#     user_input = input("Enter 'exit' to quit: ")
#     if user_input.lower() == 'exit':
#         break

# 13. For loop with a range in reverse
print("\n13. For loop with a range in reverse")
for i in range(5, 0, -1):
    print(f"i: {i}")

# 14. While loop to find a number divisible by both 3 and 5
print("\n14. While loop to find a number divisible by both 3 and 5")
n = 1
while n <= 100:
    if n % 3 == 0 and n % 5 == 0:
        print(f"Found: {n}")
        break
    n += 1

# 15. Using all() or any() in a loop condition
print("\n15. Using all() or any() in a loop condition")
numbers = [1, 2, 3, 4, 5]
if all(num > 0 for num in numbers):
    print("All numbers are positive.")
if any(num > 3 for num in numbers):
    print("There is at least one number greater than 3.")

# End of examples
print("\nAll loop condition examples executed successfully!")
