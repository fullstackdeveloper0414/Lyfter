"""
Sorting Algorithm Exercises
Jaime C Smith
07/26/2026
"""
# -------------------------------------------------------------
# Section 1 – Standard Bubble Sort (Left-to-Right)
# -------------------------------------------------------------
# This section defines a classic bubble sort implementation.
# It scans the list from left to right, comparing each pair of
# adjacent elements and swapping them if they are out of order.
# Expected outcome:
#   - The function returns a new list with the elements sorted
#     in ascending order (smallest to largest).
#   - Example:
#       Input:  [5, 3, 1, 4, 7, 9]
#       Output: [1, 3, 4, 5, 7, 9]
# -------------------------------------------------------------

def bubble_sort_left_to_right(numbers):
    """
    Sort a list of numbers in ascending order using bubble sort,
    scanning from left to right.

    Args:
        numbers (list of int or float):
            The list of numeric values to sort.

    Returns:
        list:
            A new list containing the same numbers in ascending order.
    """
    # Make a copy so we do not modify the original list passed in.
    sorted_numbers = numbers.copy()

    # The outer loop runs as many times as there are elements.
    # Each pass moves the largest remaining element toward the end.
    n = len(sorted_numbers)
    for i in range(n):
        # Inner loop goes from the start (index 0) up to n - 2,
        # comparing each element with its neighbor to the right.
        for j in range(0, n - 1):
            # If the current element is greater than the next one,
            # they are out of order, so we swap them.
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                # Swap the elements at positions j and j + 1.
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )

    # After all passes, the list is fully sorted in ascending order.
    return sorted_numbers


# -------------------------------------------------------------
# Example usage for Section 1 (testing)
# -------------------------------------------------------------
if __name__ == "__main__":
    # Original unsorted list of numbers.
    original_list = [8, 5, 3, 1, 4, 7, 9]

    # Apply the standard bubble sort (left-to-right).
    result_left_to_right = bubble_sort_left_to_right(original_list)

    # Expected outcome:
    #   result_left_to_right should be [1, 3, 4, 5, 7, 8, 9]
    print("Original list:", original_list)
    print("Sorted (left-to-right):", result_left_to_right)