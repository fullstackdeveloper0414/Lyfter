"""
Ejercicios extra de Manejo de Archivos
Jaime C Smith
05/27/2026
"""

# Program 1:
# - Reads a text file line by line.
# - Removes newline characters and extra spaces.
# - Joins all the text into a single line separated by spaces.
# - Writes that single line into a new output file.
#
# Example:
#   Input file:
#       Hola
#       mundo
#       esto
#       es
#       Python
#
#   Output file:
#       Hola mundo esto es Python


INPUT_FILE = "input_lines.txt"      # File that should contain the original lines
OUTPUT_FILE = "single_line.txt"     # New file with all content in one line


def join_lines_into_single_line(input_path, output_path):
    """
    Read all lines from input_path, clean them, join into one line,
    and write that line to output_path.

    If the input file does not exist, catch FileNotFoundError and
    inform the user what they need to do.
    """
    parts = []

    try:
        # Try to open and read the input file
        with open(input_path, "r", encoding="utf-8") as file:
            for line in file:
                # Strip newline and surrounding spaces
                clean_line = line.strip()

                # Ignore empty lines
                if clean_line:
                    parts.append(clean_line)

    except FileNotFoundError:
        # If the file is not found, show a helpful message and exit the function
        print(f"Error: The file '{input_path}' was not found.")
        print("Please create this file and save it in the same folder as this script.")
        print("Example: create 'input_lines.txt' in the directory where you run this program.")
        return

    # Join all non-empty lines with a single space
    single_line = " ".join(parts)

    # Write the single line into the output file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(single_line)

    print(f"Single line created in '{output_path}'.")


if __name__ == "__main__":
    join_lines_into_single_line(INPUT_FILE, OUTPUT_FILE)