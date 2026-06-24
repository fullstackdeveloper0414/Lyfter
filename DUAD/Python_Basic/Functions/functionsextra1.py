"""
Ejercicios de Funciones
Jaime C Smith
05/25/2026
"""

# 1) Create a function that receives a text and a character,
#    and returns how many times that character appears in the text.


def count_character(text, character):
    """
    Return how many times 'character' appears in 'text'.

    Both 'text' and 'character' are treated as case-sensitive.
    If 'character' has length > 1, we still count exact matches of that string.
    """
    count = 0

    # Iterate over each position in the text
    for index in range(len(text)):
        # Compare the substring of length len(character) at this position
        if text[index : index + len(character)] == character:
            count += 1

    return count


# Example usage (matching the assignment idea)
example_text = "programacion"
char_to_search = "o"

result = count_character(example_text, char_to_search)

print(f"In the text '{example_text}', the character '{char_to_search}' appears {result} times.")