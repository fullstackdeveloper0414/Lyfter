# Ejercicios extra de Sintaxis
# Jaime C Smith
# 05/21/2026

"""
Program that:
- Asks the user for a product price.
- Applies a discount:
    - 2% if the price is less than 100.
    - 10% if the price is greater than or equal to 100.
- Shows the final price after discount.
"""

# 1. Ask the user for the product price
price = float(input("Enter the product price: "))

# 2. Determine the discount percentage based on the price
if price < 100:
    discount_rate = 0.02   # 2%
else:
    discount_rate = 0.10   # 10%

# 3. Calculate discount amount and final price
discount_amount = price * discount_rate
final_price = price - discount_amount

# 4. Show the result
print()
print("Original price:", price)
print("Discount rate:", discount_rate * 100, "%")
print("Discount amount:", discount_amount)
print("Final price:", final_price)