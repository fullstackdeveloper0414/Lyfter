"""
Ejercicios de Funciones
Jaime C Smith
05/25/2026
"""

# 3) Create a function that reverses a string and returns it.
#    Example: "Hola mundo" -> "odnum aloH"


def reverse_string(text):
    """
    Return a new string which is the reverse of 'text'.
    We build the reversed string manually using a loop.
    """
    reversed_text = ""

    # Iterate over the string from the last index to the first
    for index in range(len(text) - 1, -1, -1):
        reversed_text += text[index]

    return reversed_text


# Example usage
original = "Hola mundo"
reversed_value = reverse_string(original)
print("Original:", original)
print("Reversed:", reversed_value)