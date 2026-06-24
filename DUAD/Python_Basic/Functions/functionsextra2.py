"""
Ejercicios de Funciones
Jaime C Smith
05/25/2026
"""

# 2) Create a function that receives a list of words and a number n,
#    and returns a new list containing only the words that have
#    more than n letters.


def filter_words_longer_than(words, n):
    """
    Given a list of strings 'words' and an integer 'n',
    return a new list with only the words that have length > n.
    """
    filtered = []

    # Iterate over each word in the list
    for word in words:
        if len(word) > n:
            filtered.append(word)

    return filtered


# Example usage (similar to the assignment example)
example_words = ["cielo", "sol", "maravilloso", "día"]
min_length = 4

filtered_words = filter_words_longer_than(example_words, min_length)

print("Original list:", example_words)
print(f"Words with more than {min_length} letters:", filtered_words)