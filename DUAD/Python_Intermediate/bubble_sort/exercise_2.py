"""
Sorting Algorithm Exercises
Jaime C Smith
07/26/2026
"""
# -------------------------------------------------------------
# Section 2 – Modified Bubble Sort (Right-to-Left)
# -------------------------------------------------------------
# This section defines a bubble sort that runs from right to left.
# Instead of pushing the largest elements to the end first, this
# implementation pulls the smallest elements toward the beginning
# of the list in each pass.
#
# Concept (based on the attached explanation):
#   - We still compare neighboring elements and swap them when
#     they are out of order.
#   - In this variation, we iterate from the right side toward
#     the left side, so smaller numbers "bubble" to the front.
#
# Expected outcome:
#   - The function returns a new list sorted in ascending order,
#     but the movement is conceptually from right to left.
#   - Example:
#       Input:  [8, 5, 3, 1, 4, 7, 9]
#       Output: [1, 3, 4, 5, 7, 8, 9]
# -------------------------------------------------------------

def bubble_sort_right_to_left(numbers):
    """
    Sort a list of numbers in ascending order using a modified
    bubble sort that scans from right to left.

    Args:
        numbers (list of int or float):
            The list of numeric values to sort.

    Returns:
        list:
            A new list containing the same numbers in ascending order.
    """
    # Copy the input list to avoid changing the original.
    sorted_numbers = numbers.copy()

    n = len(sorted_numbers)

    # Outer loop: repeat passes across the list.
    for i in range(n):
        # Inner loop: go from the right side (index n - 1) down to 1.
        # We compare each element with its neighbor to the left.
        for j in range(n - 1, 0, -1):
            # If the element on the left is greater than the one on
            # the right, they are out of order for ascending order.
            # We swap them so the smaller element moves left.
            if sorted_numbers[j - 1] > sorted_numbers[j]:
                # Swap elements at positions j-1 and j.
                sorted_numbers[j - 1], sorted_numbers[j] = (
                    sorted_numbers[j],
                    sorted_numbers[j - 1],
                )


    return sorted_numbers

# -------------------------------------------------------------
# Example usage for Section 2 (testing)
# -------------------------------------------------------------
if __name__ == "__main__":
    # Original unsorted list of numbers.
    original_list_for_right_to_left = [8, 5, 3, 1, 4, 7, 9]

    # Apply the modified bubble sort (right-to-left).
    result_right_to_left = bubble_sort_right_to_left(
        original_list_for_right_to_left
    )

    # Expected outcome:
    #   result_right_to_left should be [1, 3, 4, 5, 7, 8, 9]
    #   and smaller numbers will have moved to the front first
    #   during the right-to-left passes.
    print("Original list (right-to-left test):", original_list_for_right_to_left)
    print("Sorted (right-to-left):", result_right_to_left)
