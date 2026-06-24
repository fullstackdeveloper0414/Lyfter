"""
Ejercicios extra de Excepciones
Jaime C Smith
05/26/2026
"""

# 1) This program:
# - Asks the user for their name.
# - If the name is numeric (only digits), it raises ValueError("Name cannot be a number").
# - Then asks for the user's age.
# - If the age is not a valid integer, it catches the ValueError and shows "Invalid number".
# - If everything is valid, it prints: "Hello <name>, your age is <age>".


try:
    # Ask the user for their name
    name = input("Enter your name: ")

    # If the name consists only of digits, raise a ValueError
    if name.isdigit():
        # Raise an error with the required message
        raise ValueError("Name cannot be a number")

    # Ask the user for their age
    age_input = input("Enter your age: ")

    # Try to convert the age to an integer.
    # If this fails, a ValueError will be raised.
    age = int(age_input)

    # If we reach this point, both name and age are valid.
    print(f"Hello {name}, your age is {age}")

except ValueError as error:
    # This block will run in two cases:
    # - The name was numeric (we raised ValueError manually).
    # - The age could not be converted to int.
    message = str(error)

    # Distinguish between the two error types:
    if message == "Name cannot be a number":
        # Name was invalid (numeric)
        print(message)
    else:
        # Age conversion failed
        print("Invalid number")