"""
Unit Testing Exercises
Jaime C Smith
08/07/2026
"""

# -------------------------------------------------------------
# Section 3 – Functions Exercises 3 Through 7
# -------------------------------------------------------------
# These functions are based on the attached Functions exercises:
#
# Exercise 3: Return the sum of all numbers in a list.
# Exercise 4: Reverse a string and return it.
# Exercise 5: Return the number of uppercase and lowercase letters.
# Exercise 6: Alphabetically sort hyphen-separated words.
# Exercise 7: Return the prime numbers from a list.
# -------------------------------------------------------------


def sum_list_numbers(numbers):
    """
    Return the sum of all numbers in a list.

    Expected outcome:
    [4, 6, 2, 29] returns 41.
    """
    total = 0

    # Add every value in the list to the total.
    for number in numbers:
        total += number

    return total


def reverse_string(text):
    """
    Return a reversed version of a string.

    Expected outcome:
    "Hello world" returns "dlrow olleH".
    """
    # Reverse the string using slicing.
    return text[::-1]


def count_uppercase_and_lowercase(text):
    """
    Return the number of uppercase and lowercase letters in a string.

    Expected outcome:
    "I love Nación Sushi" returns (3, 13).

    Returns:
        tuple: (uppercase_count, lowercase_count)
    """
    uppercase_count = 0
    lowercase_count = 0

    # Check every character in the text.
    for character in text:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


def sort_hyphen_separated_words(text):
    """
    Alphabetically sort words separated by hyphens.

    Expected outcome:
    "python-variable-function-computer-monitor" becomes
    "computer-function-monitor-python-variable".
    """
    # Split the text into separate words.
    words = text.split("-")

    # Sort the words alphabetically.
    words.sort()

    # Join the sorted words with hyphens.
    return "-".join(words)


def is_prime(number):
    """
    Return True if a number is prime; otherwise, return False.

    A prime number is greater than 1 and is only divisible by
    1 and itself.
    """
    # Numbers less than 2 are not prime.
    if number < 2:
        return False

    # Check possible divisors from 2 through number - 1.
    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def get_prime_numbers(numbers):
    """
    Return a list containing only the prime numbers from a list.

    Expected outcome:
    [1, 4, 6, 7, 13, 9, 67] returns [7, 13, 67].
    """
    prime_numbers = []

    # Add a number only when it is prime.
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers