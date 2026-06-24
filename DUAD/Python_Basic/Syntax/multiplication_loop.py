# Ejercicios extra de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Custom multiplication table:
- Asks the user for a number from 1 to 10.
- Shows its multiplication table from 1 to 12.
"""

# 1. Ask the user for the number
number = int(input("Ingrese un número (1-10): "))

# 2. Show the multiplication table from 1 to 12
for i in range(1, 12 + 1):  # generates 1, 2, ..., 12
    result = number * i
    print(number, "x", i, "=", result)