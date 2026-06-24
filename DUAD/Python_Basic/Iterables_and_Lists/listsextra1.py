"""
Ejercicios Extra de Iterables y Listas
Jaime C Smith
05/22/2026
"""

# 1) Count how many times a specific number appears in a list

# Ask the user for a list of numbers as a single line (e.g., "4 2 7 2 8 2 1")
numbers_input = input("Enter numbers separated by spaces: ")

# Split the string into a list of strings
numbers_str_list = numbers_input.split()

# Convert each element to an integer
numbers = []
for item in numbers_str_list:
    numbers.append(int(item))

# Ask the user for the number to search
target = int(input("Enter the number to search for: "))

# Count how many times the target appears (manual count, not using list.count)
count = 0
for num in numbers:
    if num == target:
        count += 1

# Show the result
print(f"The number {target} appears {count} times")