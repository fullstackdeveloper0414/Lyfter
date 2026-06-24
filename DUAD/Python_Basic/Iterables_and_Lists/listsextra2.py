"""
Ejercicios Extra de Iterables y Listas
Jaime C Smith
05/22/2026
"""

# 2) Check if all elements in a list are positive
#    Restriction: Do not use functions like all()

# We will loop until the user enters a valid list of integers
while True:
    # Ask the user for a list of numbers as a single line
    print("Enter numbers separated by spaces (for example: 3 6 0 -2 4)")
    numbers_input = input("Numbers: ")

    # Split the string into a list of strings
    numbers_str_list = numbers_input.split()

    # Try to convert each element to an integer
    numbers = []
    try:
        for item in numbers_str_list:
            # int() will fail if the string is not a valid integer
            number = int(item)
            numbers.append(number)
        # If we reach here, all conversions worked, so we break the loop
        break
    except ValueError:
        # If conversion fails, show a clear message and ask again
        print("Invalid input. Please enter only whole numbers separated by spaces (no commas).")
        print()  # blank line for readability

# At this point, we have a valid list of integers in 'numbers'

# Assume all are positive at the beginning
all_positive = True

# Check each number
for num in numbers:
    # If we find a number that is zero or negative, set the flag to False
    if num <= 0:
        all_positive = False
        # We can stop checking once we find a non-positive number
        break

# Show the appropriate message
if all_positive:
    print("All numbers are positive")
else:
    print("There is at least one negative number or zero")