"""
Ejercicios de Iterables y Listas
Jaime C Smith
05/22/2026
"""

# ============================================================
# 2) Iterate a string character by character from right to left
# ============================================================

# Example string
my_string = 'Pizza con piña'

# We use range starting at the last index (len(my_string) - 1)
# and ending at -1 (because the end of range is exclusive), with step -1
for index in range(len(my_string) - 1, -1, -1):
    char = my_string[index]
    print(char)

