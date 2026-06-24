# Ejercicios de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Program that asks the user for their first name, last name and age,
then shows whether they are a baby, child, preteen, teenager,
young adult, adult, or senior adult.
"""

# 1. Ask the user for their data
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

# Convert age to int so we can compare numerically
age = int(input("Please enter your age: "))

# 2. Determine the age category
if age < 0:
    age_category = "an invalid age"
elif age <= 2:
    age_category = "a baby"
elif age <= 9:
    age_category = "a child"
elif age <= 12:
    age_category = "a preteen"
elif age <= 17:
    age_category = "a teenager"
elif age <= 25:
    age_category = "a young adult"
elif age <= 64:
    age_category = "an adult"
else:
    age_category = "a senior adult"

# 3. Show the result
print()
print("User summary:")
print("-------------")
print("Full name:", first_name, last_name)
print("Age:", age, "years old")
print("You are", age_category + ".")