# Ejercicios de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Program that asks the user for three numbers
and prints which one is the largest.
"""

# 1. Ask the user for three numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
number_3 = float(input("Enter the third number: "))

# 2. Assume the first number is the largest
max_number = number_1

# 3. Compare with the second number
if number_2 > max_number:
    max_number = number_2

# 4. Compare with the third number
if number_3 > max_number:
    max_number = number_3

# 5. Show the result
print("The largest number is:", max_number)