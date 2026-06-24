"""
Ejercicios de Funciones
Jaime C Smith
05/25/2026
"""

# 4) Create a function that prints the number of uppercase
#    and the number of lowercase letters in a string.
#    Example:
#    "I love Nación Sushi" ->
#    "There's 3 upper cases and 13 lower cases"


def count_upper_and_lower(text):
    """
    Count how many uppercase and lowercase letters are in 'text'.
    Then print a message with both counts.
    """
    upper_count = 0
    lower_count = 0

    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            upper_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lower_count += 1
        # If it's not a letter (spaces, punctuation, etc.), we ignore it

    # Print the result following the example phrase
    print(f"There's {upper_count} upper cases and {lower_count} lower cases")


# Example usage
phrase = "I love Nación Sushi"
print("Text:", phrase)
count_upper_and_lower(phrase)