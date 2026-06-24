"""
Ejercicios extra de Manejo de Archivos
Jaime C Smith
05/27/2026
"""

# Program 2:
# - Opens a text file.
# - Counts how many words it contains in total.
# - Words are separated by spaces and/or newlines (default string split).
# - If the file does not exist, it shows a clear message explaining
#   that the file must be created in the same folder as the script.


FILE_TO_COUNT = "text_to_count.txt"  # File whose words we want to count


def count_words_in_file(path):
    """
    Count the total number of words in the file located at 'path'.

    Steps:
    - Try to open the file in read mode with UTF-8 encoding.
    - If the file does not exist, catch FileNotFoundError and inform the user.
    - If the file exists, read all its content.
    - Use str.split() to split on any whitespace (spaces, newlines, tabs).
    - Return the length of the resulting list as the word count.

    Returns:
        int | None: total number of words, or None if the file was not found.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        print("Please create this file and save it in the same folder as this script.")
        print("Example: create 'text_to_count.txt' in the directory where you run this program.")
        return None

    # Split on any whitespace; this returns a list of words
    words = content.split()
    return len(words)


if __name__ == "__main__":
    total_words = count_words_in_file(FILE_TO_COUNT)

    # Only print the result if we actually got a number (file existed)
    if total_words is not None:
        print(f"This file contains {total_words} words.")