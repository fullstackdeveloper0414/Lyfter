"""
Ejercicios extra de Diccionarios
Jaime C Smith
05/22/2026
"""

# Given a list of sales where each sale has:
#   - date
#   - customer_email
#   - items (a list of items)
# and each item has:
#   - name
#   - upc
#   - unit_price
#
# Create a dictionary that stores the total sales amount for each UPC.

# Example input data
sales = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Iron',
                'upc': 'ITEM-324',
                'unit_price': 32.45,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 12.54,
            },
        ],
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 5.42,
            },
        ],
    },
    {
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 3.42,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 17.54,
            },
        ],
    },
]

# Dictionary that will store total sales per UPC
# Key: upc (string)
# Value: total sales amount (float)
sales_totals_by_upc = {}

# Iterate over each sale in the list
for sale in sales:
    # Get the list of items for this sale
    items = sale['items']

    # Iterate over each item in the sale
    for item in items:
        upc = item['upc']
        unit_price = item['unit_price']

        # If this UPC is not yet in the dictionary, initialize it with 0
        if upc not in sales_totals_by_upc:
            sales_totals_by_upc[upc] = 0.0

        # Add the unit_price to the running total for this UPC
        sales_totals_by_upc[upc] += unit_price

# Print the resulting dictionary
print("Total sales per UPC:")
print(sales_totals_by_upc)

# To verify against the example result, we should see:
# {
#   'ITEM-453': 131.52,
#   'ITEM-324': 32.45,
#   'ITEM-432': 30.08,
#   'ITEM-23': 8.84,
# }