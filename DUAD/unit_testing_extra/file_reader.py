"""
Ejercicios Extra de Unit Testing
Jaime C Smith
08/11/2026
"""

# -------------------------------------------------------------
# Section 5 – File Reading Function
# -------------------------------------------------------------
# Purpose:
# This function reads and returns every line in a text file.
#
# Expected results:
# - If the file exists, the function returns its lines.
# - If the file does not exist, Python raises FileNotFoundError.
# -------------------------------------------------------------


def read_lines(path):
    """
    Return all lines from the file located at path.

    Expected result:
    A text file with three lines returns a list containing those
    three lines.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    # Open the file in read mode and return all lines.
    with open(path, "r") as file:
        return file.readlines()