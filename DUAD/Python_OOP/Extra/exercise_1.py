"""
Ejercicios Extra de OOP
Jaime C Smith
07/01/2026
"""

"""
Exercise 1 – Rectangle with width, height, area, perimeter, and validation.

This exercise asks us to create a Rectangle class that:
- Has attributes width and height.
- Has a get_area() method that returns the area.
- Has a get_perimeter() method that returns the perimeter.
- Validates that no value is negative. If width or height is negative,
  it must raise an exception with an appropriate message.

The purpose of the code below is to model a rectangle as an object,
compute its area and perimeter, and enforce that dimensions are
non‑negative by raising a ValueError when invalid input is detected.
"""


class Rectangle:
    """
    Rectangle represents a geometric rectangle with width and height.

    Attributes:
        width (float): The width of the rectangle. Must be >= 0.
        height (float): The height of the rectangle. Must be >= 0.

    Methods:
        get_area() -> float:
            Return the area (width * height).
        get_perimeter() -> float:
            Return the perimeter (2 * (width + height)).

    The class validates that width and height are not negative. If a
    negative value is provided, it raises a ValueError explaining that
    values must be positive.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Constructor for Rectangle.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.

        Behavior:
            - If width or height is negative, raise ValueError with a
              clear message.
            - Otherwise, store width and height as attributes.
        """
        if width < 0 or height < 0:
            raise ValueError(
                "There is a negative value. Width and height must be positive numbers."
            )

        self.width = width
        self.height = height

    def get_area(self) -> float:
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area computed as width * height.
        """
        return self.width * self.height

    def get_perimeter(self) -> float:
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter computed as 2 * (width + height).
        """
        return 2 * (self.width + self.height)


# Example usage (for manual testing):
if __name__ == "__main__":
    try:
        # Example 1 (valid values)
        height_input = float(input("Enter the height: "))
        width_input = float(input("Enter the width: "))
        rectangle = Rectangle(width_input, height_input)
        print("Area:", rectangle.get_area())
        print("Perimeter:", rectangle.get_perimeter())
    except ValueError as error:
        # Example 2 (negative value triggers this message)
        print(error)