"""
Ejercicios de Funciones
Jaime C Smith
05/24/2026
"""

# 1) Create two functions that print two different things,
#    and make the first one call the second.
#
#    Then experiment with scope:
#    - Try to access a variable defined inside a function from outside.
#    - Try to access a global variable from inside a function and change its value.


# Global variable for the scope experiment
global_counter = 0


def print_first_message():
    """
    Print the first message and call the second function.
    This shows how one function can call another.
    """
    print("This is the FIRST message.")
    # Call the second function
    print_second_message()


def print_second_message():
    """
    Print the second message.
    This function is called by print_first_message.
    """
    print("This is the SECOND message.")


def scope_experiments():
    """
    Demonstrate scope:
    - Try to read a local variable outside its function (will fail).
    - Modify a global variable from inside a function.
    """
    # Local variable: only exists inside this function
    local_value = 42

    # We declare that we want to use the global variable here
    global global_counter

    # Change the global variable
    global_counter_value_before = global_counter
    global_counter = global_counter + 1

    print("Inside scope_experiments:")
    print("  local_value is:", local_value)
    print("  global_counter before change:", global_counter_value_before)
    print("  global_counter after change:", global_counter)


# Call the functions to see the behavior
print_first_message()
print()  # blank line

scope_experiments()
print()

# Try to access the global variable (this works)
print("Outside any function, global_counter is:", global_counter)

# The following line would cause an error because local_value
# only exists inside scope_experiments.
# Uncomment it to see the error:
# print(local_value)  # NameError: name 'local_value' is not defined