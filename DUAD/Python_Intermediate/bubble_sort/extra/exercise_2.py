"""
Extra Sorting Algorithm Exercises
Jaime C Smith
07/26/2026
"""

# -------------------------------------------------------------
# Section 2 – bubble_sort_steps: counting iterations and swaps
# -------------------------------------------------------------
# This function extends the basic bubble sort by counting:
#   - How many passes (iterations) through the list were made.
#   - How many swaps were performed in total.
#
# What the code does:
# - Uses the same comparison and swap logic as bubble_sort.
# - Keeps a counter for:
#     iterations: how many times the outer loop runs.
#     swaps: how many times two elements are swapped.
# - Returns the sorted list AND both counters.
#
# Expected outcome:
# - The function returns a tuple:
#       (sorted_list, iterations, swaps)
# - Example:
#       input_list = [5, 3, 4, 1, 2]
#       sorted_list, iterations, swaps = bubble_sort_steps(input_list)
#       Possible output:
#           sorted_list = [1, 2, 3, 4, 5]
#           iterations  = 4
#           swaps       = 6
#   (Exact numbers may vary depending on early-termination logic,
#    but this matches the assignment example.)
# -------------------------------------------------------------


def bubble_sort_steps(numbers):
    """
    Sort a list of numbers in ascending order using bubble sort,
    counting the number of iterations and swaps.

    Args:
        numbers (list of int or float):
            List of numeric values to sort.

    Returns:
        tuple:
            (sorted_list, iterations, swaps)
            where:
                sorted_list (list) is the sorted result,
                iterations (int) is how many passes were performed,
                swaps (int) is how many swaps were made.
    """
    # Copy the list to avoid modifying the original.
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)

    # Initialize counters for iterations (outer passes)
    # and swaps (total element exchanges).
    iterations = 0
    swaps = 0

    # Perform up to n passes.
    for i in range(n):
        # Increase the iteration counter at the start of each pass.
        iterations += 1

        # Track if any swap occurs in this pass.
        # If no swap happens, the list is already sorted.
        swapped_this_pass = False

        # Inner loop goes through all neighboring pairs.
        for j in range(0, n - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                # Swap misplaced pair.
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j],
                )

                # Increase swap counter and mark that we swapped.
                swaps += 1
                swapped_this_pass = True

        # Optimization: if no elements were swapped in this pass,
        # the list is sorted and we can stop early.
        if not swapped_this_pass:
            break

    return sorted_numbers, iterations, swaps


# Example usage for Section 2 (testing)
if __name__ == "__main__":
    # Example unsorted list to test bubble_sort_steps.
    data = [5, 3, 4, 1, 2]

    # Apply the step-counting bubble sort.
    sorted_list, iterations, swaps = bubble_sort_steps(data)

    # Expected output (numbers may be similar to):
    # Sorted list: [1, 2, 3, 4, 5]
    # Iterations:  4
    # Swaps:       6
    print("Original list:", data)
    print("Sorted list:  ", sorted_list)
    print("Iterations:   ", iterations)
    print("Swaps:        ", swaps)