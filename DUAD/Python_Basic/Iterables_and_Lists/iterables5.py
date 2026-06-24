"""
Ejercicios de Iterables y Listas
Jaime C Smith
05/22/2026
"""

# ============================================================
# 5) Ask the user for 10 numbers, then show all numbers
#    and the highest one
# ============================================================

# Empty list where we will store the user's numbers
numbers = []

# Helper list to make the prompts more friendly
order_words = [
    "first", "second", "third", "fourth", "fifth",
    "sixth", "seventh", "eighth", "ninth", "tenth"
]

# We ask the user for 10 numbers
for i in range(10):
    prompt = f"Enter the {order_words[i]} number: "
    user_input = int(input(prompt))
    numbers.append(user_input)

# We find the highest number manually (without using max)
# We assume the first number is the initial highest
highest = numbers[0]

# We iterate through the list to find the highest number
for number in numbers:
    if number > highest:
        highest = number

# We show the full list
print("Numbers entered:", numbers)
# We show the highest number
print("The highest number was", highest)