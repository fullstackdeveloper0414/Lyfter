"""
Ejercicios extra de Excepciones
Jaime C Smith
05/26/2026
"""

# 3) This file defines a function `sum_values(list_of_values)` that:
# - Receives a list of mixed elements (strings, ints, floats).
# - Tries to convert each element to float.
# - If conversion succeeds:
#       - Adds the number to a running total.
#       - Prints: "<number> added successfully"
# - If conversion fails:
#       - Prints: "Invalid element: <original_value>"
# - At the end, prints: "Total sum: <total>"
# - Returns the total sum as a float.


def sum_values(list_of_values):
    """
    Sum all elements in 'list_of_values' that can be converted to float.

    For each element:
        - Try to convert it to float.
        - If successful, add to total and print:
          "<number> added successfully"
        - If it fails, print:
          "Invalid element: <value>"

    Args:
        list_of_values (list): list of values (strings, ints, floats).

    Returns:
        float: the total sum of all valid numeric values.
    """
    total = 0.0

    # Iterate over each element in the list
    for value in list_of_values:
        try:
            # Try to convert the current element to float
            number = float(value)
            total += number
            print(f"{number} added successfully")
        except ValueError:
            # If conversion fails, show invalid element message
            print(f"Invalid element: {value}")

    # After processing all elements, show the total sum
    print(f"Total sum: {total}")

    return total


# Example usage
if __name__ == "__main__":
    my_list = ['10', 'apple', '5.5', '3', 'n/a']
    total_sum = sum_values(my_list)
    # total_sum will be 18.5