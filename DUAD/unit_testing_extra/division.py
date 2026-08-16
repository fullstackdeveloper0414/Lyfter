"""
Ejercicios Extra de Unit Testing
Jaime C Smith
08/11/2026
"""

# -------------------------------------------------------------
# Section 3 – Division Function
# -------------------------------------------------------------
# Purpose:
# This function divides the first number by the second number.
#
# Expected results:
# - divide(10, 2) returns 5.0.
# - divide(10, 0) raises ValueError.
# - divide("10", 2) raises TypeError.
# -------------------------------------------------------------


def divide(number1, number2):
    """
    Divide number1 by number2.

    Expected result:
    divide(10, 2) returns 5.0.

    Raises:
        ValueError: If number2 is zero.
        TypeError: If the parameters cannot be divided.
    """
    # Prevent division by zero.
    if number2 == 0:
        raise ValueError("Cannot divide by zero.")

    # Python raises TypeError if the values cannot be divided.
    return number1 / number2