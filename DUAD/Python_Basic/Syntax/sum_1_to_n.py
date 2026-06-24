# Ejercicios extra de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Program that:
- Asks the user for a number n.
- Calculates the sum of all integers from 1 up to n (inclusive).
- Shows the result of the sum.

Examples:
n = 5  ->  1 + 2 + 3 + 4 + 5 = 15
n = 3  ->  1 + 2 + 3 = 6
n = 12 ->  1 + 2 + ... + 12 = 78
"""

# 1. Ask the user for the number
n = int(input("Enter a positive integer: "))

# 2. Initialize the accumulator for the sum
total_sum = 0

# 3. Use a loop to add all numbers from 1 to n
for i in range(1, n + 1):  # range(1, n + 1) generates 1, 2, ..., n
    total_sum += i         # same as: total_sum = total_sum + i

# 4. Show the result
print("The sum from 1 to", n, "is:", total_sum)