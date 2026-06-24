"""
Ejercicios Ejercicios de Diccionarios
Jaime C Smith
05/23/2026
"""

# 2) Create a program that builds a dictionary using two lists of the
#    same size: one list for keys and the other for values.
#
# Example:
# list_a = ['first_name', 'last_name', 'role']
# list_b = ['Alek', 'Castillo', 'Software Engineer']
# Result -> {'first_name': 'Alek', 'last_name': 'Castillo', 'role': 'Software Engineer'}

# Example lists
list_a = ['first_name', 'last_name', 'role']
list_b = ['Jaime', 'Smith', 'Software Engineer']

# We assume both lists have the same length
result_dict = {}

# Iterate by index to pair each key with its corresponding value
for index in range(len(list_a)):
    key = list_a[index]
    value = list_b[index]
    result_dict[key] = value

# Print the resulting dictionary
print("Resulting dictionary:")
print(result_dict)