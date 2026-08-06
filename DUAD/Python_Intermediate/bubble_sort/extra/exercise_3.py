"""
Extra Sorting Algorithm Exercises
Jaime C Smith
07/26/2026
"""

# -------------------------------------------------------------
# Section 3 – Validated Bubble Sort Wrapper
# -------------------------------------------------------------
# This file defines two functions:
#
# 1) bubble_sort(numbers)
#    - A standard bubble sort implementation.
#    - It takes a list of numbers and returns a new list with the
#      elements sorted in ascending order (smallest to largest).
#
# 2) validated_bubble_sort(values)
#    - A wrapper around bubble_sort that first validates the input:
#        * Ensures the input is a list.
#        * Ensures the list is not empty.
#        * Ensures all elements are integers or floats.
#      If the input is valid, it calls bubble_sort and returns
#      the sorted list.
#      If invalid, it returns an appropriate error message string,
#      similar to the examples in the assignment.
#
# Expected outcome:
#   - For valid numeric lists, validated_bubble_sort returns the
#     list sorted in ascending order.
#   - For invalid inputs (e.g., not a list, empty list, or containing
#     non-numeric elements), it returns an error message string
#     explaining the problem.
# -------------------------------------------------------------


def bubble_sort(numbers):
    """
    Sort a list of numbers in ascending order using the bubble sort algorithm.

    This version scans the list from left to right, comparing adjacent
    elements and swapping them if they are out of order. It repeats this
    process multiple times until the entire list is sorted.

    Args:
        numbers (list of int or float):
            The list of numeric values to sort.

    Returns:
        list:
            A new list containing the same numbers in ascending order.

    Example:
        input_list = [5, 3, 1, 4, 7, 9]
        result = bubble_sort(input_list)
        # result -> [1, 3, 4, 5, 7, 9]
    """
    # Create a copy of the original list so we do not modify it in place.
    sorted_numbers = numbers.copy()

    n = len(sorted_numbers)

    # Outer loop: perform n passes over the list.
    for i in range(n):
        # Inner loop: compare each element with its neighbor on the right.
        for j in range(0, n - 1):
            # If the current element is greater than the next one,
            # they are out of order, so we swap them.
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )

    # After all passes, the list is fully sorted.
    return sorted_numbers


def validated_bubble_sort(values):
    """
    Validate the input and then sort it using bubble_sort.

    This function checks that:
      - The input 'values' is a list.
      - The list is not empty.
      - Every element in the list is a number (int or float).

    If the input is valid, it calls bubble_sort(values) and returns
    the sorted list. If there is any validation problem, it returns
    an error message string describing the issue.

    Args:
        values (list):
            The list to validate and sort.

    Returns:
        list or str:
            - If valid: a new list containing the numeric elements of
              'values' sorted in ascending order.
            - If invalid: a string with an error message.

    Example:
        valid_input = [8, 5, 3, 1, 4, 7, 9]
        result = validated_bubble_sort(valid_input)
        # result -> [1, 3, 4, 5, 7, 8, 9]

        invalid_input = [5, "hola", 2]
        result = validated_bubble_sort(invalid_input)
        # result -> "Error: The list contains non-numeric elements"
    """
    # Check that the input is actually a list.
    if not isinstance(values, list):
        return "Error: Input must be a list"

    # Check that the list is not empty.
    if len(values) == 0:
        return "Error: The list is empty and cannot be sorted"

    # Check that every element is an int or float.
    for index, item in enumerate(values):
        if not isinstance(item, (int, float)):
            return (
                "Error: The list contains non-numeric elements "
                f"(invalid at index {index}: {repr(item)})"
            )

    # If we reach this point, the input is valid, so we can sort it.
    sorted_list = bubble_sort(values)
    return sorted_list


# -------------------------------------------------------------
# Example usage (for testing)
# -------------------------------------------------------------
if __name__ == "__main__":
    # Example 1: a valid list of numbers.
    valid_input = [8, 5, 3, 1, 4, 7, 9]
    valid_result = validated_bubble_sort(valid_input)

    # Expected outcome:
    # valid_result should be [1, 3, 4, 5, 7, 8, 9]
    print("Valid input: ", valid_input)
    print("Valid result:", valid_result)

    print("-" * 60)

    # Example 2: an invalid list (contains a string).
    invalid_input = [5, "hola", 2]
    invalid_result = validated_bubble_sort(invalid_input)

    # Expected outcome:
    # invalid_result should be an error message string like:
    # "Error: The list contains non-numeric elements ..."
    print("Invalid input:", invalid_input)
    print("Result for invalid input:", invalid_result)

    print("-" * 60)

    # Example 3: an empty list.
    empty_input = []
    empty_result = validated_bubble_sort(empty_input)

    # Expected outcome:
    # empty_result should be "Error: The list is empty and cannot be sorted"
    print("Empty input:", empty_input)
    print("Result for empty input:", empty_result)