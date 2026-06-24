"""
Ejercicios Ejercicios de Diccionarios
Jaime C Smith
05/23/2026
"""

# 3) Create a program that uses a list to remove keys from a dictionary.
#
# Example:
# list_of_keys = ['access_level', 'age']
# employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
# Result -> {'name': 'John', 'email': 'john@ecorp.com'}

# Example list of keys to remove
list_of_keys = ['access_level', 'age']

# Example dictionary
employee = {
    'name': 'Jaime',
    'email': 'jsmith@smithfreelancing.com',
    'access_level': 5,
    'age': 28
}

# Remove each key in list_of_keys from the dictionary if it exists
for key in list_of_keys:
    # We can use pop with a default value to avoid errors if the key is missing
    employee.pop(key, None)

# Print the resulting dictionary
print("Dictionary after removing keys:")
print(employee)