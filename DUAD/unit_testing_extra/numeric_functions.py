"""
Ejercicios Extra de Unit Testing
Jaime C Smith
08/11/2026
"""

# -------------------------------------------------------------
# Section 1 – Numeric Functions
# -------------------------------------------------------------
# Purpose:
# This module contains three functions that operate with numbers:
# - add_numbers: adds two numbers.
# - calculate_average: calculates the average of a list of numbers.
# - celsius_to_fahrenheit: converts Celsius to Fahrenheit.
#
# Expected results:
# - add_numbers(4, 6) returns 10.
# - calculate_average([2, 4, 6]) returns 4.
# - celsius_to_fahrenheit(0) returns 32.
# -------------------------------------------------------------


def add_numbers(number1, number2):
    """
    Return the sum of two numeric values.

    Expected result:
    add_numbers(4, 6) returns 10.
    """
    return number1 + number2


def calculate_average(numbers):
    """
    Return the average value of a non-empty list of numbers.

    Expected result:
    calculate_average([2, 4, 6]) returns 4.

    Raises:
        ValueError: If the list is empty.
    """
    # An average cannot be calculated with an empty list.
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")

    # Divide the total by the amount of values.
    return sum(numbers) / len(numbers)


def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Expected result:
    celsius_to_fahrenheit(0) returns 32.
    """
    return (celsius * 9 / 5) + 32