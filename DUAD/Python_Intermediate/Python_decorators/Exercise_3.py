"""
Python decorators Exercises
Jaime C Smith
07/06/2026
"""

"""
Section 3 – User class with age property and age-check decorator

Requirements:
- Create a User class that:
  - Has a date_of_birth attribute.
  - Has an age property.
- Then create a decorator for functions that accept a User as a parameter.
  - The decorator must check if the User is of legal age (adult).
  - If the User is not an adult, it must raise an exception.

Design decisions:
- We will assume "legal age" means 18 years or older.
- date_of_birth will be stored as a datetime.date object.
- The age property will calculate the age based on today's date.
- The decorator will search the wrapper's arguments for a User instance:
  - It will look in positional arguments (args).
  - It will also look in keyword arguments (kwargs).
- If it finds a User and user.age < 18, it will raise a ValueError.
- If no User is found, it will raise a ValueError to avoid silently skipping
  the check.

"""

from datetime import date
from functools import wraps


class User:
    """
    User represents a person with a date of birth and a computed age.

    Attributes:
        date_of_birth (date): The user's date of birth.

    Properties:
        age (int): The user's current age in years, computed from
                   date_of_birth and today's date.
    """

    def __init__(self, date_of_birth: date) -> None:
        """
        Constructor for User.

        Args:
            date_of_birth (date): The user's date of birth.

        Behavior:
            - Stores the date of birth.
            - Does not compute age immediately; age is computed on demand
              via the age property.
        """
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        """
        Compute and return the user's age in years.

        Calculation:
        - Start with the difference in years between today's year and
          birth year.
        - Adjust by subtracting 1 if today's date is before the user's
          birthday in the current year.

        Returns:
            int: Age in full years.

        Example:
            If date_of_birth = 2000-07-06 and today is 2026-07-06,
            age will be 26.
        """
        today = date.today()
        years = today.year - self.date_of_birth.year

        # If today's month/day is before the birth month/day, subtract 1 year.
        has_had_birthday_this_year = (
            (today.month, today.day) >= (self.date_of_birth.month, self.date_of_birth.day)
        )

        if not has_had_birthday_this_year:
            years -= 1

        return years


def require_adult_user(func):
    """
    Decorator for functions that accept a User as a parameter.

    Behavior:
        - Searches for a User instance in *args and **kwargs.
        - If a User is found and user.age < 18:
            - Raises ValueError indicating the user is not an adult.
        - If no User instance is found:
            - Raises ValueError, because the decorator is meant to be used
              with functions that receive a User.
        - If the User is 18 or older:
            - Calls the original function and returns its result.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper that ensures the given User is an adult before
        executing the function's logic.
        """
        # Try to locate a User instance in positional arguments.
        adult_user = None
        for value in args:
            if isinstance(value, User):
                adult_user = value
                break

        # If not found in args, try keyword arguments.
        if adult_user is None:
            for value in kwargs.values():
                if isinstance(value, User):
                    adult_user = value
                    break

        # If no User was found in any argument, raise an error.
        if adult_user is None:
            raise ValueError(
                "No User instance found in function arguments. "
                "This decorator must be used on functions that accept a User."
            )

        # Check if the user is an adult (18 or older).
        if adult_user.age < 18:
            raise ValueError(
                f"User is not an adult. Age: {adult_user.age}. "
                "This operation is restricted to adult users."
            )

        # If the user is an adult, proceed with the original function call.
        return func(*args, **kwargs)

    return wrapper


# Example usage (for manual testing):
@require_adult_user
def access_restricted_content(user: User):
    """
    Example function that represents accessing restricted content.

    Expected behavior:
    - If user.age >= 18, the decorator allows the function to run and
      this function prints a success message.
    - If user.age < 18, the decorator raises a ValueError before
      this function executes.

    The function assumes that:
    - 'user' is an instance of User.
    - The decorator has already enforced the age check.
    """
    print("Access granted: showing restricted content.")


if __name__ == "__main__":
    # Example 1: Adult user (should pass).
    # Suppose someone born in 1990 is definitely over 18 today.
    adult = User(date(1990, 7, 6))
    print("Adult age:", adult.age)
    access_restricted_content(adult)
    # Expected:
    # Adult age: (a value >= 18)
    # "Access granted: showing restricted content."

    # Example 2: Underage user (should fail).
    # Suppose someone born in 2010 is under 18 today.
    minor = User(date(2010, 7, 6))
    print("Minor age:", minor.age)
    try:
        access_restricted_content(minor)
    except ValueError as e:
        # Expected:
        # A ValueError explaining that the user is not an adult and
        # the operation is restricted.
        print("Error while accessing content:", e)