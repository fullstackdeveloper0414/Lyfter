"""
Unit Testing Exercises
Jaime C Smith
08/07/2026
"""

# -------------------------------------------------------------
# Section 1 – Bubble Sort Function
# -------------------------------------------------------------
# This function sorts a list of numeric values in ascending order.
#
# Expected outcome:
# - [5, 2, 4, 1] becomes [1, 2, 4, 5].
# - An empty list returns an empty list.
# - A non-list parameter raises a TypeError.
# -------------------------------------------------------------


def bubble_sort(numbers):
    """
    Sort a list in ascending order using the bubble sort algorithm.

    Args:
        numbers (list): A list of comparable values to sort.

    Returns:
        list: A new sorted list.

    Raises:
        TypeError: If numbers is not a list.
    """
    # Validate that the received value is a list.
    if not isinstance(numbers, list):
        raise TypeError("bubble_sort expects a list.")

    # Create a copy so the original list is not modified.
    sorted_numbers = numbers.copy()

    # Repeat passes through the list.
    for _ in range(len(sorted_numbers)):
        # Compare neighboring values.
        for index in range(len(sorted_numbers) - 1):
            # Swap values that are out of ascending order.
            if sorted_numbers[index] > sorted_numbers[index + 1]:
                sorted_numbers[index], sorted_numbers[index + 1] = (
                    sorted_numbers[index + 1],
                    sorted_numbers[index],
                )

    # Return the sorted copy.
    return sorted_numbers