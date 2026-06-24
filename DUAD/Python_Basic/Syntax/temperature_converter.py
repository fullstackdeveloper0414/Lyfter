# Ejercicios extra de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Temperature unit converter:
- Asks the user to enter a temperature in Celsius.
- Converts it to Fahrenheit and Kelvin.
- Shows all three values.
"""

# 1. Ask the user for the temperature in Celsius
celsius = float(input("Ingrese temperatura en Celsius: "))

# 2. Convert Celsius to Fahrenheit and Kelvin
# Formula: F = C * 1.8 + 32
fahrenheit = celsius * 1.8 + 32  # [web:166][web:168]

# Formula: K = C + 273.15
kelvin = celsius + 273.15        # [web:165]

# 3. Show the results
print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)