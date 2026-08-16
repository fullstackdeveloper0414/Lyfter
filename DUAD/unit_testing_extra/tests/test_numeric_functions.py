"""
Ejercicios Extra de Unit Testing
Jaime C Smith
08/11/2026
"""

import unittest

from numeric_functions import (
    add_numbers,
    calculate_average,
    celsius_to_fahrenheit,
)

# -------------------------------------------------------------
# Section 2 – Tests for Numeric Functions
# -------------------------------------------------------------
# Purpose:
# This test class verifies three numeric functions:
# - add_numbers
# - calculate_average
# - celsius_to_fahrenheit
#
# Required test cases:
# - Positive numbers.
# - Negative numbers.
# - Zero values.
# -------------------------------------------------------------


class TestNumericFunctions(unittest.TestCase):
    """
    Test numeric functions using positive, negative, and zero values.
    """

    def test_numeric_functions_with_positive_numbers(self):
        """
        Test the three functions with positive values.

        Expected results:
        - add_numbers(10, 5) returns 15.
        - calculate_average([4, 6, 8]) returns 6.
        - celsius_to_fahrenheit(25) returns 77.
        """
        # Arrange
        number1 = 10
        number2 = 5
        average_list = [4, 6, 8]
        celsius = 25

        # Act
        addition_result = add_numbers(number1, number2)
        average_result = calculate_average(average_list)
        conversion_result = celsius_to_fahrenheit(celsius)

        # Assert
        self.assertEqual(addition_result, 15)
        self.assertEqual(average_result, 6)
        self.assertEqual(conversion_result, 77)

    def test_numeric_functions_with_negative_numbers(self):
        """
        Test the three functions with negative values.

        Expected results:
        - add_numbers(-10, -5) returns -15.
        - calculate_average([-2, -4, -6]) returns -4.
        - celsius_to_fahrenheit(-40) returns -40.
        """
        # Arrange
        number1 = -10
        number2 = -5
        average_list = [-2, -4, -6]
        celsius = -40

        # Act
        addition_result = add_numbers(number1, number2)
        average_result = calculate_average(average_list)
        conversion_result = celsius_to_fahrenheit(celsius)

        # Assert
        self.assertEqual(addition_result, -15)
        self.assertEqual(average_result, -4)
        self.assertEqual(conversion_result, -40)

    def test_numeric_functions_with_zero_values(self):
        """
        Test the three functions with zero values.

        Expected results:
        - add_numbers(0, 0) returns 0.
        - calculate_average([0, 0, 0]) returns 0.
        - celsius_to_fahrenheit(0) returns 32.
        """
        # Arrange
        number1 = 0
        number2 = 0
        average_list = [0, 0, 0]
        celsius = 0

        # Act
        addition_result = add_numbers(number1, number2)
        average_result = calculate_average(average_list)
        conversion_result = celsius_to_fahrenheit(celsius)

        # Assert
        self.assertEqual(addition_result, 0)
        self.assertEqual(average_result, 0)
        self.assertEqual(conversion_result, 32)


if __name__ == "__main__":
    unittest.main()