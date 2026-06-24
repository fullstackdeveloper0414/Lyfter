"""
Ejercicios Extra de Iterables y Listas
Jaime C Smith
05/22/2026
"""

# 3) Show the smallest value in a list without using min()
#    Use a variable to compare values one by one

# Ask the user for a list of numbers as a single line
numbers_input = input("Enter numbers separated by spaces: ")

# Split and convert to integers
numbers_str_list = numbers_input.split()

numbers = []
for item in numbers_str_list:
    numbers.append(int(item))

# Assume the first element is the smallest
smallest = numbers[0]

# Compare each element with the current smallest
for num in numbers:
    if num < smallest:
        smallest = num

# Show the result
print(f"The smallest value is {smallest}")