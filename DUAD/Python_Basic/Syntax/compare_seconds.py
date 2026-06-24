# Ejercicios extra de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Program that:
- Asks the user for a time in seconds.
- Checks if it is less than, greater than, or equal to 10 minutes.
- 10 minutes = 600 seconds.
- If it is less, shows how many seconds are missing to reach 10 minutes.
- If it is greater, shows "Mayor".
- If it is exactly equal, shows "Igual".
"""

# 1. Ask the user for a time in seconds
seconds = int(input("Enter a time in seconds: "))

# 2. Define 10 minutes in seconds
TEN_MINUTES = 600

# 3. Compare and show the appropriate result
if seconds < TEN_MINUTES:
    # Calculate how many seconds are missing to reach 10 minutes
    missing_seconds = TEN_MINUTES - seconds
    print(missing_seconds)
elif seconds > TEN_MINUTES:
    print("Mayor")
else:  # seconds == TEN_MINUTES
    print("Igual")