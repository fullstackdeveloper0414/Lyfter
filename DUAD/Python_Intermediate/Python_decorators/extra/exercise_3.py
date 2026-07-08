"""
Python decorators Exercises- Extra
Jaime C Smith
07/08/2026
"""

"""
Section 3 – multiply with @log_call and @validate_numbers

Requirement:
- Create a function named 'multiply' that takes two values and multiplies them.
- Combine two decorators on this function:
  1) @log_call:
       - Prints the function name, the arguments, the current date/time,
         and the return value.
  2) @validate_numbers:
       - Checks that all arguments are numeric (int or float).
       - If any argument is not numeric, it should raise an exception.

Example:
    multiply(3, 4)

Expected output format (example with a fixed datetime):
    func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Result: 12
    Result 12

In real usage, the datetime part will show the actual current date and time.
"""

from functools import wraps
from datetime import datetime


def validate_numbers(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check all positional arguments.
        for index, value in enumerate(args):
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Argument at position {index} is not numeric: {value!r}"
                )

        # Check all keyword arguments.
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Argument '{key}' is not numeric: {value!r}"
                )

        # If all arguments are numeric, call the original function.
        return func(*args, **kwargs)

    return wrapper


def log_call(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Call the original function and capture the result.
        result = func(*args, **kwargs)

        # Get the current date and time.
        current_time = datetime.now()

        # Build a string representation of positional arguments,
        # like "3, 4" for args = (3, 4).
        args_str = ", ".join(str(arg) for arg in args)

        # Print the log line in the required format.
        # Example:
        #   func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Result: 12
        print(
            f"func:{func.__name__} - args: {args_str} - "
            f"[{current_time}] - Result: {result}"
        )

        # Return the result so callers still get the actual value.
        return result

    return wrapper


@log_call          # This decorator logs the function call and result.
@validate_numbers  # This decorator ensures all arguments are numeric.
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    # Example 1: Valid numeric arguments.
    #
    # Expected output (datetime will vary):
    #   func:multiply - args: 3, 4 - [<current datetime>] - Result: 12
    #   Result 12
    result = multiply(3, 4)
    print("Result", result)

    # Example 2: Invalid argument type (non-numeric).
    #
    # Expected behavior:
    #   - @validate_numbers detects the non-numeric argument.
    #   - A TypeError is raised.
    #   - The error message explains which argument failed.
    try:
        multiply(3, "not a number")
    except TypeError as e:
        print("Error while multiplying:", e)