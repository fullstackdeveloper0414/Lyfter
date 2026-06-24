"""
Ejercicios extra de Manejo de Archivos
Jaime C Smith
05/27/2026
"""

# Program 4 (updated with error handling and filename in message):
# - Asks the user to enter a line of text.
# - Opens an existing file in append mode ('a').
# - Adds the new line at the end of the file without erasing existing content.
# - If the file does not exist, it is created automatically.
# - If there is a problem opening/writing the file, it shows an error message.
# - After success, it tells the user which file was appended.


LOG_FILE = "log_file.txt"  # File where we append new lines


def append_user_line_to_file(path):
    """
    Ask the user for a line of text and append it to the file at 'path'.

    If the file does not exist, it will be created automatically
    because we use append mode ('a').
    If there is an OSError (e.g., permission issue), we inform the user.
    """
    # Ask the user for a line of text
    user_line = input("Enter the line to append to the file: ")

    try:
        # Open the file in append mode; create it if it does not exist
        with open(path, "a", encoding="utf-8") as file:
            # Always add a newline before the new text to ensure separation.
            file.write("\n" + user_line)

    except OSError as error:
        # OSError covers common file I/O problems (permissions, etc.)
        print(f"Error: Could not open or write to '{path}'.")
        print("Details:", error)
        print("Please make sure you have permission to write in this folder.")
        return

    # Success message including the filename
    print(f"The text was appended to the file '{path}' without deleting previous content.")


if __name__ == "__main__":
    append_user_line_to_file(LOG_FILE)