"""
Ejercicios extra de Excepciones
Jaime C Smith
05/26/2026
"""

# 2) This file defines a function `convert_to_int_list(list_of_strings)` that:
# - Receives a list of strings.
# - Tries to convert each element to an integer using int().
# - Uses try-except to catch ValueError when conversion fails.
# - Prints a message for each element:
#       - If it converts: "<original> converted to <int_value>"
#       - If it fails: "Could not convert element: <original>"
# - Returns a new list with the successfully converted integers.


def convert_to_int_list(list_of_strings):
    """
    Try to convert each string in 'list_of_strings' to an integer.

    For each element:
        - If conversion succeeds, add it to a result list and print:
          "<value> converted to <int_value>"
        - If conversion fails, print:
          "Could not convert element: <value>"

    Args:
        list_of_strings (list of str): list of strings to convert.

    Returns:
        list of int: list with all successfully converted integers.
    """
    converted_integers = []

    print("Result:")

    # Iterate over each string in the list
    for value in list_of_strings:
        try:
            # Try to convert the current string to an integer
            int_value = int(value)
            converted_integers.append(int_value)
            print(f'"{value}" converted to {int_value}')
        except ValueError:
            # If conversion fails, show the error message and continue
            print(f"Could not convert element: {value}")

    return converted_integers


# Example usage
if __name__ == "__main__":
    my_list = ['4', 'hello', '10', '5.2']
    result_list = convert_to_int_list(my_list)
    # result_list will be [4, 10]