"""
Ejercicios Extra de Iterables y Listas
Jaime C Smith
05/22/2026
"""

# 4) Given a list of numbers, calculate the average of the values,
#    then create a new list with only the values greater than the average

# Ask the user for a list of numbers as a single line
numbers_input = input("Enter numbers separated by spaces: ")

# Split and convert to integers
numbers_str_list = numbers_input.split()

numbers = []
for item in numbers_str_list:
    numbers.append(int(item))

# Calculate the sum of the numbers
total_sum = 0
for num in numbers:
    total_sum += num

# Calculate the average (avoid division by zero just in case)
if len(numbers) > 0:
    average = total_sum / len(numbers)
else:
    average = 0

# Create a new list with values greater than the average
greater_than_average = []

for num in numbers:
    if num > average:
        greater_than_average.append(num)

# Show the average and the new list
print("Average:", average)
print("New list with values greater than the average:", greater_than_average)