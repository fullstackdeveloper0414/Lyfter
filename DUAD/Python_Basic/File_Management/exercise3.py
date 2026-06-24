"""
Ejercicios extra de Manejo de Archivos
Jaime C Smith
05/27/2026
"""

# Program 3:
# - Reads a text file line by line.
# - Converts each line to uppercase.
# - Writes the uppercase lines into a new file.
# - If the input file does not exist, shows a clear message and stops.


ORIGINAL_FILE = "original.txt"      # Original text file
UPPERCASE_FILE = "uppercase.txt"    # New file with uppercase content


def copy_file_to_uppercase(input_path, output_path):
    """
    Read each line from input_path, convert it to uppercase,
    and write it to output_path.

    If the input file does not exist, catch FileNotFoundError and
    inform the user what they need to do.
    """
    try:
        # Try to open the input file
        with open(input_path, "r", encoding="utf-8") as input_file:
            # Open the output file only after we confirm input exists
            with open(output_path, "w", encoding="utf-8") as output_file:
                for line in input_file:
                    # Convert the entire line to uppercase
                    upper_line = line.upper()
                    output_file.write(upper_line)

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
        print("Please create this file and save it in the same folder as this script.")
        print("Example: create 'original.txt' in the directory where you run this program.")
        return

    print(f"Uppercase copy created in '{output_path}'.")


if __name__ == "__main__":
    copy_file_to_uppercase(ORIGINAL_FILE, UPPERCASE_FILE)