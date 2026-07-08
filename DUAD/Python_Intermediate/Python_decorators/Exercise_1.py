"""
Python decorators Exercises
Jaime C Smith
07/06/2026
"""

"""
Section 1 – Decorator that prints parameters and return value

Requirement:
- Create a decorator that prints the parameters and the return value of
  the function it decorates.

Idea:
- We define a decorator that receives a function.
- Inside, we define a wrapper that:
  - Receives any positional and keyword arguments (*args, **kwargs).
  - Prints the arguments it received.
  - Calls the original function, captures the result.
  - Prints the result.
  - Returns the result to the caller.

"""

from functools import wraps  # Optional: keeps the original function name and docstring.


def log_parameters_and_return(func):
    """
    Decorator that logs (prints) the parameters and the return value
    of the decorated function.

    Args:
        func (callable): Function to decorate.

    Returns:
        callable: The wrapped function that prints parameters and return
        value before returning the result.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that:
        - Receives the same parameters as the original function.
        - Prints the parameters.
        - Calls the original function.
        - Prints the return value.
        - Returns the result.
        """
        # Print positional arguments as a tuple.
        print(f"[LOG] Positional arguments (args): {args}")

        # Print keyword arguments as a dictionary.
        print(f"[LOG] Keyword arguments (kwargs): {kwargs}")

        # Call the original decorated function and capture the result.
        result = func(*args, **kwargs)

        # Print the return value of the function.
        print(f"[LOG] Return value: {result}")

        # Return the result so the caller gets the actual function output.
        return result

    return wrapper


# Example usage (for manual testing):
@log_parameters_and_return
def add_numbers(a, b):
    """
    Example function that adds two numbers.

    Expected behavior:
    - When called, the decorator will print:
      - The positional arguments (a, b).
      - Any keyword arguments (none in this simple example).
      - The return value (a + b).
    """
    return a + b


if __name__ == "__main__":
    # When you run this, you should see:
    # [LOG] Positional arguments (args): (3, 4)
    # [LOG] Keyword arguments (kwargs): {}
    # [LOG] Return value: 7
    # And then the print below: "Final result: 7"
    final_result = add_numbers(3, 4)
    print("Final result:", final_result)