"""
Ejercicios de Iterables y Listas
Jaime C Smith
05/22/2026
"""
# ============================================================
# 4) Remove all odd numbers from a list
# ============================================================

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# We create a new list containing only even numbers
even_numbers = []

for number in my_list:
    # A number is even if the remainder when divided by 2 is 0
    if number % 2 == 0:
        even_numbers.append(number)

# We replace the original list with the list of even numbers
my_list = even_numbers

print(my_list)  # Example output: [2, 4, 6, 8]


