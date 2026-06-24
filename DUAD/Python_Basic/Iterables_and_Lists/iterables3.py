"""
Ejercicios de Iterables y Listas
Jaime C Smith
05/22/2026
"""

# ============================================================
# 3) Swap the first and last element of a list
#    (works for lists of any size >= 2)
# ============================================================

my_list = [4, 3, 6, 1, 7]

# We check that the list has at least 2 elements
if len(my_list) >= 2:
    # Store the first element in a temporary variable
    temp = my_list[0]
    # The first element takes the value of the last element
    my_list[0] = my_list[-1]      # index -1 is the last element
    # The last element takes the original value of the first element
    my_list[-1] = temp

print(my_list)  # Example output: [7, 3, 6, 1, 4]

