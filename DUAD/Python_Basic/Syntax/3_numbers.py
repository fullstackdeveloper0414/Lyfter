# Ejercicios extra de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Program that:
- Asks the user for 3 numbers.
- If at least one of those numbers is 30, OR if the sum of the 3 numbers is 30,
  it shows "Correct".
- Otherwise, it shows "Incorrect".
"""

# 1. Ask the user for the three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# 2. Check the conditions:
#    - one of them is 30
#    - OR the sum of the three is 30
if (num1 == 30 or num2 == 30 or num3 == 30) or (num1 + num2 + num3 == 30):
    print("Correct")
else:
    print("Incorrect")