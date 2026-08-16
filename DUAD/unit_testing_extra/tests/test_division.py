"""
Ejercicios Extra de Unit Testing
Jaime C Smith
08/11/2026
"""

import unittest

from division import divide

# -------------------------------------------------------------
# Section 4 – Tests for the Division Function
# -------------------------------------------------------------
# Purpose:
# Verify normal division and the required error scenarios.
#
# Expected results:
# - divide(10, 2) returns 5.0.
# - divide(10, 0) raises ValueError.
# - divide("10", 2) raises TypeError.
# -------------------------------------------------------------


class TestDivide(unittest.TestCase):
    """
    Test valid and invalid uses of the divide function.
    """

    def test_divide_returns_five_for_ten_divided_by_two(self):
        """
        Test normal division.

        Expected result:
        divide(10, 2) returns 5.0.
        """
        # Arrange
        number1 = 10
        number2 = 2

        # Act
        result = divide(number1, number2)

        # Assert
        self.assertEqual(result, 5.0)

    def test_divide_raises_value_error_for_zero_divisor(self):
        """
        Test division by zero.

        Expected result:
        divide(10, 0) raises ValueError.
        """
        # Arrange
        number1 = 10
        number2 = 0

        # Act and Assert
        with self.assertRaises(ValueError):
            divide(number1, number2)

    def test_divide_raises_type_error_for_string_parameter(self):
        """
        Test division with a string parameter.

        Expected result:
        divide("10", 2) raises TypeError.
        """
        # Arrange
        number1 = "10"
        number2 = 2

        # Act and Assert
        with self.assertRaises(TypeError):
            divide(number1, number2)


if __name__ == "__main__":
    unittest.main()