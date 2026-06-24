"""
Ejercicios Extra de Iterables y Listas
Jaime C Smith
05/22/2026
"""

# 5) Ask the user to enter 5 words.
#    Then show a new list with only the words that have more than 4 letters.

# Empty list to store the 5 words
words = []

# Ask the user for 5 words, one by one
for i in range(5):
    word = input(f"Enter word #{i + 1}: ")
    words.append(word)

# Create a new list with words longer than 4 letters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

# Show the resulting list
print("Original list:", words)
print("Words with more than 4 letters:", long_words)