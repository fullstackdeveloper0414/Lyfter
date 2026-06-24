# Ejercicios de Sintaxis - Tipos de datos y suma
# Jaime C Smith
# 05/21/2026

"""
Script to experiment with + between different Python data types.
Some operations work, others raise TypeError on purpose.
"""

print("=== string + string ===")
print('"Hello" + " World" =', "Hello" + " World")
print()

print("=== string + int (will cause TypeError) ===")
try:
    result = "Hello" + 5
    print('"Hello" + 5 =', result)
except TypeError as error:
    print("Error:", error)
print()

print("=== int + string (will cause TypeError) ===")
try:
    result = 5 + "Hello"
    print("5 + 'Hello' =", result)
except TypeError as error:
    print("Error:", error)
print()

print("=== list + list ===")
print("[1, 2] + [3, 4] =", [1, 2] + [3, 4])
print()

print("=== string + list (will cause TypeError) ===")
try:
    result = "Hello" + [1, 2, 3]
    print('"Hello" + [1, 2, 3] =', result)
except TypeError as error:
    print("Error:", error)
print()

print("=== float + int ===")
print("3.5 + 2 =", 3.5 + 2)
print()

print("=== bool + bool ===")
print("True + True  =", True + True)
print("True + False =", True + False)
print("False + False =", False + False)
print()

print("End of experiment.")