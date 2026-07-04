"""
Ejercicios de Los 4 Pilares de OOP
Jaime C Smith
07/04/2026
"""

"""
Section 2 – Abstract Shape and concrete Circle, Square, Rectangle (Abstraction and Polymorphism)

Requirements:
- Create an abstract class Shape that:
  - Has abstract methods calculate_perimeter and calculate_area.
- Create Circle, Square, and Rectangle classes that inherit from Shape
  and implement these methods.
- Each concrete shape must have the attributes needed to compute
  perimeter and area (for example: radius for Circle, side for Square,
  width and height for Rectangle).

The purpose of this section is to demonstrate:
- Abstraction: Shape defines the interface (contract) for shapes.
- Polymorphism: Different shapes implement the same methods in their
  own way, but can be used interchangeably via the Shape interface.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Shape is an abstract base class for geometric shapes.

    Methods:
        calculate_perimeter() -> float:
            Abstract method that must return the shape's perimeter.
        calculate_area() -> float:
            Abstract method that must return the shape's area.

    This class cannot be instantiated directly. It defines the contract
    that all concrete shapes must follow.
    """

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the shape.

        This method must be implemented by concrete subclasses.
        """
        pass

    @abstractmethod
    def calculate_area(self) -> float:
        """
        Calculate the area of the shape.

        This method must be implemented by concrete subclasses.
        """
        pass


class Circle(Shape):
    """
    Circle represents a circle shape.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        calculate_perimeter() -> float:
            Return the circumference (2 * π * radius).
        calculate_area() -> float:
            Return the area (π * radius^2).
    """

    def __init__(self, radius: float) -> None:
        """
        Constructor for Circle.

        Args:
            radius (float): Radius of the circle. Must be non-negative.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: 2 * π * radius.
        """
        return 2 * math.pi * self.radius

    def calculate_area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: π * radius^2.
        """
        return math.pi * (self.radius ** 2)


class Square(Shape):
    """
    Square represents a square shape.

    Attributes:
        side (float): Length of one side of the square.

    Methods:
        calculate_perimeter() -> float:
            Return the perimeter (4 * side).
        calculate_area() -> float:
            Return the area (side^2).
    """

    def __init__(self, side: float) -> None:
        """
        Constructor for Square.

        Args:
            side (float): Length of a side. Must be non-negative.
        """
        if side < 0:
            raise ValueError("Side length cannot be negative.")
        self.side = side

    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the square.

        Returns:
            float: 4 * side.
        """
        return 4 * self.side

    def calculate_area(self) -> float:
        """
        Calculate the area of the square.

        Returns:
            float: side^2.
        """
        return self.side ** 2


class RectangleShape(Shape):
    """
    RectangleShape represents a rectangle shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        calculate_perimeter() -> float:
            Return the perimeter (2 * (width + height)).
        calculate_area() -> float:
            Return the area (width * height).
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Constructor for RectangleShape.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.

        Both width and height must be non-negative.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative.")
        self.width = width
        self.height = height

    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: 2 * (width + height).
        """
        return 2 * (self.width + self.height)

    def calculate_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: width * height.
        """
        return self.width * self.height


# Example usage (for manual testing):
if __name__ == "__main__":
    # Simple list of shapes, without subscripted type hints (compatible with older Python)
    shapes = [
        Circle(radius=5),
        Square(side=4),
        RectangleShape(width=3, height=6),
    ]

    for shape in shapes:
        print(
            f"{shape.__class__.__name__} -> "
            f"Perimeter: {shape.calculate_perimeter():.2f}, "
            f"Area: {shape.calculate_area():.2f}"
        )