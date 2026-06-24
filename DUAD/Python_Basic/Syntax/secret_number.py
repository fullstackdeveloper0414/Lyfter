# Ejercicios extra de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Program that:
- Has a secret number between 1 and 10.
- Asks the user to guess the number.
- Repeats (does not end) until the user guesses the secret number correctly.
"""

# 1. Define the secret number (between 1 and 10)
secret_number = 7  # you can change this value if you want

# 2. Start a loop that continues until the user guesses correctly
while True:
    # Ask the user for a guess
    guess = int(input("Guess the secret number (between 1 and 10): "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Correct! You guessed the secret number.")
        break  # exit the loop when the guess is correct
    else:
        print("Incorrect, try again.")