"""
Ejercicios extra de Diccionarios
Jaime C Smith
05/22/2026
"""

# Given a list of sold products where each product has:
#   - name
#   - category
#   - price
#
# Create a dictionary that accumulates the total price per category.
#
# Example:
# products = [
#     {"name": "Monitor", "category": "Electrónica", "price": 200},
#     {"name": "Teclado", "category": "Electrónica", "price": 50},
#     {"name": "Silla", "category": "Muebles", "price": 120},
#     {"name": "Mesa", "category": "Muebles", "price": 180},
#     {"name": "Mouse", "category": "Electrónica", "price": 25},
# ]
# Result:
# {
#   "Electrónica": 275,
#   "Muebles": 300
# }

# Example input list
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

# Dictionary that will store total price per category
# Key: category name (string)
# Value: total price (number)
totals_by_category = {}

# Iterate through each product in the list
for product in products:
    # Read the category and price of the current product
    category = product["category"]
    price = product["price"]

    # If this category is not yet in the dictionary, initialize it with 0
    if category not in totals_by_category:
        totals_by_category[category] = 0

    # Add the price to the running total for this category
    totals_by_category[category] += price

# Print the resulting dictionary
print("Total price per category:")
print(totals_by_category)

# Optional: print in a more readable format
print("\nDetailed totals:")
for category, total in totals_by_category.items():
    print(f"{category}: {total}")