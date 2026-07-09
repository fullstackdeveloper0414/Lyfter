"""
Ejercicios de OOP
Jaime C Smith
07/01/2026
"""

"""
Exercise 1 – Circle class with radius and area.

This exercise asks us to create a Circle class that:
- Has one attribute: radius.
- Has one method: get_area, which returns the area of the circle.

The purpose of the code below is to model a geometric circle as an
object and provide a method that computes its area using the formula
area = π * radius^2. The radius can be set when creating the object.
"""

import math


class Circle:
    """
    Circle represents a geometric circle with a given radius.

    Attributes:
        radius (float): The radius of the circle. It is expected to be
            a non-negative number (0 or greater). We do not enforce it
            strictly here, but callers should respect that rule.

    Methods:
        get_area() -> float:
            Compute and return the area of the circle using the formula
            area = π * radius^2.
    """

    def __init__(self, radius: float) -> None:
        """
        Constructor for Circle.

        Args:
            radius (float): Radius of the circle. This value is stored
                as an attribute of the object for later calculations.

        This constructor simply remembers the given radius so that
        the get_area method can compute the area later.
        """
        self.radius = radius

    def get_area(self) -> float:
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area computed as π * radius^2.

        This method uses the math.pi constant from the Python standard
        library to give a more accurate value of π.
        """
        return math.pi * (self.radius ** 2)


# Example usage (for manual testing):
circle = Circle(5.0)
print(circle.get_area())