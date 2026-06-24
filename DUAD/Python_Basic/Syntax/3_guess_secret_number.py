# Ejercicios de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Program that:
- Generates a random secret number from 1 to 10.
- Asks the user to guess the number.
- Does not end until the user guesses correctly.
"""

import random  # Needed to generate a random number

# 1. Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

print("I have chosen a secret number between 1 and 10. Try to guess it!")

# 2. Loop until the user guesses the correct number
while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct! You guessed the secret number.")
        break  # Exit the loop and end the program
    else:
        print("Wrong guess, try again.")