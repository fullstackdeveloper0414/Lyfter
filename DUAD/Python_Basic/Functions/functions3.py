"""
Ejercicios de Funciones
Jaime C Smith
05/25/2026
"""

# 2) Create a function that returns the sum of all the numbers in a list.
#    The function has one parameter (the list) and returns a number
#    (the sum of all its elements).
#    Example: [4, 6, 2, 29] -> 41


def sum_of_list(numbers):
    """
    Return the sum of all elements in the list 'numbers'.
    We use a manual loop to keep it simple and explicit.
    """
    total = 0

    for number in numbers:
        total += number

    return total


# Example usage
example_list = [4, 6, 2, 29]
result = sum_of_list(example_list)
print("List:", example_list)
print("Sum of list:", result)