"""
Python decorators Exercises
Jaime C Smith
07/06/2026
"""

"""
Section 2 – Decorator that validates parameter types

Requirement:
- Create a decorator that checks if ALL parameters of the decorated
  function are numbers.
- If any parameter is not a number, it should raise an exception.

Idea:
- For each positional and keyword argument, check if it is an instance of
  int or float.
- If any value is not numeric, raise a TypeError with an explanatory message.
- Otherwise, call the original function and return its result.
"""

from functools import wraps


def ensure_numeric_parameters(func):
    """
    Decorator that ensures all parameters passed to the decorated function
    are numeric (int or float).

    Behavior:
        - Checks every value in args and kwargs.
        - If any value is not a number, raises TypeError.
        - If all are numeric, calls the original function and returns its result.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper that:
        - Validates each argument.
        - Raises TypeError if a non-numeric value is found.
        - Calls the original function if all arguments are valid.
        """
        # Check positional arguments.
        for index, value in enumerate(args):
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Parameter at position {index} is not numeric: {value!r}"
                )

        # Check keyword arguments.
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Parameter '{key}' is not numeric: {value!r}"
                )

        # If all validations pass, call the original function.
        return func(*args, **kwargs)

    return wrapper


# Example usage (for manual testing):
@ensure_numeric_parameters
def multiply_three_numbers(a, b, c):
    """
    Example function that multiplies three numbers.

    Expected behavior:
    - If a, b, and c are all numeric (int/float), it returns a * b * c.
    - If any parameter is not numeric, the decorator will raise a TypeError
      before this function is executed.

    Example:
        multiply_three_numbers(2, 3, 4)  ->  24
        multiply_three_numbers(2, "x", 4)  ->  TypeError raised by decorator.
    """
    return a * b * c


if __name__ == "__main__":
    # Case 1: All numeric – the decorator allows the call.
    result_ok = multiply_three_numbers(2, 3, 4)
    print("Result (all numeric):", result_ok)  # Expected: 24

    # Case 2: One non-numeric – the decorator raises TypeError.
    try:
        result_error = multiply_three_numbers(2, "not a number", 4)
    except TypeError as e:
        # Expected output: a TypeError message explaining which parameter failed.
        print("Error while multiplying:", e)