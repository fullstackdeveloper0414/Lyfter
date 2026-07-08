"""
Python decorators Exercises- Extra
Jaime C Smith
07/08/2026
"""

"""
Section 2 – @requires_login decorator

Requirement:
- Create a decorator @requires_login that:
  - Checks if the global variable 'user_logged_in' is True.
  - If 'user_logged_in' is False, it must raise an exception with the
    message "User not authenticated".
  - If 'user_logged_in' is True, the decorated function should run normally.

Example scenario:
    user_logged_in = False

    @requires_login
    def view_profile():
        print("Showing user profile")

    view_profile()

Expected behavior:
    - With user_logged_in = False, calling view_profile() raises an exception.
    - With user_logged_in = True, calling view_profile() prints the message.
"""

from functools import wraps

# Global variable indicating whether the current user is logged in.
user_logged_in = False


def requires_login(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
  
        global user_logged_in

        # If the user is not logged in, raise an exception.
        if not user_logged_in:
            # Exception message is now in English: "User not authenticated".
            raise Exception("User not authenticated")

        # If the user is logged in, call the original function.
        return func(*args, **kwargs)

    return wrapper


@requires_login
def view_profile() -> None:

    print("Showing user profile")


if __name__ == "__main__":
    # Test case 1: user_logged_in is False.
    #
    # Expected behavior:
    #   - Calling view_profile() raises an exception.
    #   - The exception message printed is: "User not authenticated".
    user_logged_in = False
    try:
        view_profile()
    except Exception as e:
        print("Error:", e)

    # Test case 2: user_logged_in is True.
    #
    # Expected behavior:
    #   - Calling view_profile() prints:
    #       "Showing user profile"
    user_logged_in = True
    view_profile()