"""
Ejercicios de Funciones
Jaime C Smith
05/25/2026
"""

# 3) Create a function that receives a string and returns
#    how many vowels it contains.
#
#    We will consider both lowercase and uppercase vowels,
#    including Spanish accents: a, e, i, o, u, á, é, í, ó, ú, ü.


def count_vowels(text):
    """
    Return the number of vowels in 'text'.

    Vowels considered: a, e, i, o, u, á, é, í, ó, ú, ü
    in both lowercase and uppercase.
    """
    # Define a set of vowels for quick membership checks
    vowels = set("aeiouáéíóúüAEIOUÁÉÍÓÚÜ")

    count = 0

    # Iterate over each character in the text
    for char in text:
        if char in vowels:
            count += 1

    return count


# Example usage
example_text = "Hola mundo"
vowel_count = count_vowels(example_text)

print(f"The text '{example_text}' contains {vowel_count} vowels.")