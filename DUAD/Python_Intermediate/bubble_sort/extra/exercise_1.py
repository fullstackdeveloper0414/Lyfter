"""
Extra Sorting Algorithm Exercises
Jaime C Smith
07/26/2026
"""

# -------------------------------------------------------------
# Section 1 – Bubble sort logic for data structure exercises
# -------------------------------------------------------------
# This function implements a generic bubble sort that can be used
# conceptually for the earlier data structure exercises
# (Queue, Stack, LinkedList, etc.).
#
# In those exercises, each structure manages its own nodes and
# swap logic. Here we express the same "bubble" idea in a plain
# Python list, where swapping elements is a direct index swap.
#
# What the code does:
# - Takes a list of numbers as input.
# - Repeatedly walks through the list, comparing each pair of
#   adjacent elements.
# - If an element is greater than the one after it, it swaps them.
# - After enough passes, the list is sorted in ascending order.
#
# Expected outcome:
# - The function returns a new list with the same elements
#   in ascending order (smallest to largest).
#   Example:
#       Input:  [5, 3, 4, 1, 2]
#       Output: [1, 2, 3, 4, 5]
# -------------------------------------------------------------


def bubble_sort(numbers):
    """
    Sort a list of numeric values in ascending order using
    the classic bubble sort algorithm.

    Args:
        numbers (list of int or float):
            List of numeric values to be sorted.

    Returns:
        list:
            A new list containing the same values, but sorted.
    """
    # Create a shallow copy so that the original list is not
    # modified by this function.
    sorted_numbers = numbers.copy()

    # Get the length of the list once so we can reuse it.
    n = len(sorted_numbers)

    # Outer loop:
    # We need up to n passes for worst-case sorting.
    for i in range(n):
        # Inner loop:
        # Iterate from the beginning up to the second-to-last element.
        # At each step, compare element j with element j+1.
        for j in range(0, n - 1):
            # If the element at j is greater than the one at j + 1,
            # they are out of ascending order, so we swap them.
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )

    # After all passes, the list is fully sorted.
    return sorted_numbers


# Example usage for Section 1 (testing)
if __name__ == "__main__":
    # Unsorted list to demonstrate the algorithm.
    data = [5, 3, 4, 1, 2]

    # Apply bubble sort.
    result = bubble_sort(data)

    # Expected output:
    # result should be [1, 2, 3, 4, 5]
    print("Original list:", data)
    print("Sorted list:  ", result)