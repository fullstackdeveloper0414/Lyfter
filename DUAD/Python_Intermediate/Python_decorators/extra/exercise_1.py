"""
Python decorators Exercises- Extra
Jaime C Smith
07/08/2026
"""

"""
Section 1 – @repeat_twice decorator

Requirement:
- Create a function that prints "Hola, [name]" (Spanish for "Hello, [name]")
  two times.
- Create a decorator @repeat_twice that makes the decorated function run
  twice in a row with the same arguments.

Expected behavior:
    @repeat_twice
    def say_hello(name):
        print(f"Hola, {name}")

    say_hello("Jeanca")

Expected output:
    Hola, Jeanca
    Hola, Jeanca
"""

from functools import wraps


def repeat_twice(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # First call to the original function.
        result = func(*args, **kwargs)

        # Second call to the original function with the same arguments.
        result = func(*args, **kwargs)

        # Return the result of the second call.
        return result

    return wrapper


@repeat_twice
def say_hello(name: str) -> None:

    print(f"Hola, {name}")


if __name__ == "__main__":
    # Example usage for manual testing.
    #
    # Expected output when this script is run directly:
    #   Hola, Jeanca
    #   Hola, Jeanca
    say_hello("Jeanca")