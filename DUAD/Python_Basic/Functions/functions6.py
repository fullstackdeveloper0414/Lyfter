"""
Ejercicios de Funciones
Jaime C Smith
05/25/2026
"""

# 5) Create a function that accepts a string with words separated by a hyphen
#    and returns a string with the words sorted alphabetically, joined by hyphen.
#
#    Steps:
#    - Convert the string to a list (split by '-').
#    - Sort the list.
#    - Convert the list back to a string with '-'.
#
#    Example:
#    "python-variable-funcion-computadora-monitor"
#    -> "computadora-funcion-monitor-python-variable"


def sort_hyphen_separated_words(text):
    """
    Take a hyphen-separated string 'text', sort the words alphabetically,
    and return a new hyphen-separated string.
    """
    # Split the string into a list of words
    words = text.split("-")

    # Sort the list in place (alphabetical order)
    words.sort()

    # Join the list back into a string with hyphens
    sorted_text = "-".join(words)

    return sorted_text


# Example usage
original = "python-variable-funcion-computadora-monitor"
sorted_result = sort_hyphen_separated_words(original)
print("Original:", original)
print("Sorted:", sorted_result)