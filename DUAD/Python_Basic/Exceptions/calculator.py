"""
Ejercicios de Excepciones
Jaime C Smith
05/26/2026
"""

# Command-line calculator using:
# - A list (array) of operations to build the menu.
# - Helper functions for input, formatting, and applying operations.
#
# Features:
# - Initial number entered by the user (current result).
# - Menu of operations:
#       1. Addition
#       2. Subtraction
#       3. Multiplication
#       4. Division
#       5. Clear result and start over (ask for a new initial number)
#       6. Exit calculator
# - Input validation and exception handling for:
#       - Invalid menu option.
#       - Invalid numeric input.
#       - Division by zero.
# - Display formatting:
#       - Whole numbers shown as integers (10.0 -> 10).
#       - Non-whole numbers rounded to 2 decimal places.
# - Flow:
#       - User enters an initial number.
#       - Loop: show current result, show menu, perform operation.
#       - Exit only via option 6 with "Thank you for using our calculator".


# ------------------------------------------------------------------
# Operation registry (list-based)
# ------------------------------------------------------------------

# Each element is a "record" (dictionary) describing one menu option.
# We use the list index + 1 as the menu number.
OPERATIONS = [
    {"label": "Addition",                       "type": "add"},
    {"label": "Subtraction",                    "type": "sub"},
    {"label": "Multiplication",                 "type": "mul"},
    {"label": "Division",                       "type": "div"},
    {"label": "Clear result and start over",    "type": "clear"},
    {"label": "Exit calculator",                "type": "exit"},
]

# Pre-compute the number of options to avoid magic numbers.
MENU_SIZE = len(OPERATIONS)


# ------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------

def format_number(value: float):
    """
    Format a float for display.

    - If the value is a whole number (e.g. 5.0), return it as int (5).
    - Otherwise, return the value rounded to 2 decimal places.
    """
    if value.is_integer():
        return int(value)
    return round(value, 2)


def get_number_from_user(prompt: str) -> float:
    """
    Prompt the user until a valid int or float is entered.

    Returns:
        float: the numeric value entered by the user.
    """
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid number. Please enter digits only (you may use a decimal point).")


def get_menu_option() -> int:
    """
    Display the operation menu and return the validated choice.

    The menu numbers go from 1 to MENU_SIZE, and we will later convert
    that to a 0-based index for accessing the OPERATIONS list.

    Returns:
        int: the chosen menu option (1-based index).
    """
    while True:
        print("\nPlease choose an operation:")

        # Build the menu from the OPERATIONS list using enumerate
        # enumerate(..., start=1) makes the menu start at 1 instead of 0.
        for index, info in enumerate(OPERATIONS, start=1):
            print(f"  {index}. {info['label']}")

        option_input = input(f"Enter an option (1-{MENU_SIZE}): ")

        # Validate that the input is digits only
        if not option_input.isdigit():
            print("Invalid option. Please enter digits only.")
            continue

        option = int(option_input)

        # Check that the numeric option is within the valid range
        if 1 <= option <= MENU_SIZE:
            return option

        print(f"Invalid option. Please enter a number between 1 and {MENU_SIZE}.")


def apply_operation(current_result: float, new_number: float, op_type: str) -> float:
    """
    Apply an arithmetic operation to current_result using new_number.

    Args:
        current_result: the running total.
        new_number:     the operand supplied by the user.
        op_type:        one of 'add', 'sub', 'mul', 'div'.

    Returns:
        float: the new result.

    Raises:
        ZeroDivisionError: if op_type is 'div' and new_number is 0.
        ValueError: if op_type is not a recognised arithmetic operation.
    """
    if op_type == "add":
        return current_result + new_number
    if op_type == "sub":
        return current_result - new_number
    if op_type == "mul":
        return current_result * new_number
    if op_type == "div":
        # This will raise ZeroDivisionError if new_number is 0
        return current_result / new_number

    # If we reach here, op_type is unknown; raise an error to catch logic issues.
    raise ValueError(f"Unknown operation type: '{op_type}'")


# ------------------------------------------------------------------
# Main program
# ------------------------------------------------------------------

def main() -> None:
    """
    Control loop:
      - Ask for an initial number.
      - Show current result → show menu → perform operation.
      - Option 5 clears and restarts; option 6 exits.
    """
    print("Welcome to the command-line calculator!")

    # Ask for the initial number (initial "current result")
    current_result = get_number_from_user("Enter the initial number: ")

    while True:
        # Show the current result at the start of each loop
        print(f"\nCurrent result: {format_number(current_result)}")

        # Ask for an operation (1-based index)
        option = get_menu_option()

        # Convert the 1-based menu choice to a 0-based index for the list
        op_info = OPERATIONS[option - 1]
        op_type = op_info["type"]

        # Exit option
        if op_type == "exit":
            print("\nThank you for using our calculator.")
            break

        # Clear and restart option
        if op_type == "clear":
            print("Result has been cleared.")
            current_result = get_number_from_user("Enter the new initial number: ")
            continue

        # Arithmetic operations (1–4) require a second number
        new_number = get_number_from_user("Enter the number to use in the operation: ")

        try:
            current_result = apply_operation(current_result, new_number, op_type)
            print(f"After {op_info['label'].lower()}, the new result is: {format_number(current_result)}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. The current result remains unchanged.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C
        print("\n\nCalculator interrupted. Goodbye!")
    except Exception as error:
        print("An unexpected error occurred:", error)