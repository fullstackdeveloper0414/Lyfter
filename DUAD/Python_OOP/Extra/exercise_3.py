"""
Ejercicios Extra de OOP
Jaime C Smith
07/01/2026
"""

"""
Exercise 3 – Product and Inventory classes.

This exercise asks us to:
- Create a Product class with:
  - name
  - price
  - quantity
- Create an Inventory class that:
  - Stores products in a list.
  - Has methods to:
    - Add a product.
    - Show all products.
    - Calculate the total value of the inventory.

The purpose of this code is to represent individual products as objects
and manage a collection of them inside an Inventory object, including
computing the total value based on price * quantity for each product.
"""


class Product:
    """
    Product represents an item with a name, price, and quantity.

    Attributes:
        name (str): Name of the product (for example, "Mouse").
        price (float): Unit price of the product.
        quantity (int): Number of units in stock.

    Methods:
        get_total_value() -> float:
            Return the total value for this product (price * quantity).
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Constructor for Product.

        Args:
            name (str): Product name.
            price (float): Unit price of the product.
            quantity (int): Quantity in inventory.

        The constructor stores these values so that we can later
        calculate total value and show product information.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self) -> float:
        """
        Calculate the total value of this product in inventory.

        Returns:
            float: The value computed as price * quantity.
        """
        return self.price * self.quantity

    def __repr__(self) -> str:
        """
        Return a readable representation of the product for debugging.

        Example:
            Product(name='Mouse', price=5000, quantity=3)
        """
        return (
            f"Product(name='{self.name}', "
            f"price={self.price}, quantity={self.quantity})"
        )


class Inventory:
    """
    Inventory represents a collection of products.

    Attributes:
        products (list[Product]): List of Product objects stored.

    Methods:
        add_product(product: Product) -> None:
            Add a Product to the inventory.
        show_products() -> None:
            Print all products with their details.
        calculate_total_value() -> float:
            Return the total value of all products in inventory.
    """

    def __init__(self) -> None:
        """
        Constructor for Inventory.

        Initializes an empty list to store Product objects.
        """
        self.products = []

    def add_product(self, product: Product) -> None:
        """
        Add a product to the inventory.

        Args:
            product (Product): The product to add.

        The product is appended to the internal products list.
        """
        self.products.append(product)

    def show_products(self) -> None:
        """
        Display all products in the inventory.

        Behavior:
            - If there are no products, print a message.
            - Otherwise, print each product's name, price, quantity, and
              total value.
        """
        if not self.products:
            print("Inventory is empty.")
            return

        print("\n--- Inventory Products ---")
        for product in self.products:
            total_value = product.get_total_value()
            print(
                f"Name: {product.name}, "
                f"Price: {product.price}, "
                f"Quantity: {product.quantity}, "
                f"Total value: {total_value}"
            )

    def calculate_total_value(self) -> float:
        """
        Calculate the total value of all products in the inventory.

        Returns:
            float: Sum of price * quantity for all products.
        """
        total = 0.0
        for product in self.products:
            total += product.get_total_value()
        return total


# Example usage (for manual testing):
if __name__ == "__main__":
    inventory = Inventory()

    product1 = Product("Mouse", 5000, 3)
    product2 = Product("Teclado", 8000, 2)

    inventory.add_product(product1)
    inventory.add_product(product2)

    inventory.show_products()

    total_inventory_value = inventory.calculate_total_value()
    print("Total inventory value:", total_inventory_value)  # 34000