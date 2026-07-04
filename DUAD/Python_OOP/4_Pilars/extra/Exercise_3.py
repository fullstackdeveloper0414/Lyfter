"""
Ejercicios Extra de Los 4 Pilares de OOP
Jaime C Smith
07/04/2026
"""

"""
Section 3 – Vehicle, Car, Motorcycle (Inheritance and Method Overriding)

Requirements:
- Create a base class Vehicle with attributes:
  - _brand
  - _year
- Add a method get_info() that returns a description of the vehicle.
- Then create two child classes:
  - Car
  - Motorcycle
- Each must add its own attribute (for example, doors or type) and
  override get_info() to include this additional information.

Example:
    vehicle1 = Car("Toyota", 2020, 4)
    vehicle2 = Motorcycle("Yamaha", 2022, "Sport")

    print(vehicle1.get_info())  # Toyota (2020) - 4 doors
    print(vehicle2.get_info())  # Yamaha (2022) - Type: Sport

The purpose of this section is to demonstrate inheritance and method
overriding: Car and Motorcycle reuse Vehicle's attributes but customize
get_info() to add their own details.
"""


class Vehicle:
    """
    Vehicle is a base class for different types of vehicles.

    Attributes (private):
        _brand (str): Brand of the vehicle (for example, "Toyota").
        _year (int): Manufacturing year of the vehicle.

    Methods:
        get_info() -> str:
            Return a basic description of the vehicle.
    """

    def __init__(self, brand: str, year: int) -> None:
        """
        Constructor for Vehicle.

        Args:
            brand (str): Brand name.
            year (int): Manufacturing year.
        """
        self._brand = brand
        self._year = year

    def get_info(self) -> str:
        """
        Return a basic description of the vehicle.

        Returns:
            str: String in the format "Brand (Year)".
        """
        return f"{self._brand} ({self._year})"


class Car(Vehicle):
    """
    Car represents a car vehicle.

    Attributes:
        doors (int): Number of doors the car has.

    Methods:
        get_info() -> str:
            Return a description including brand, year, and number of doors.
    """

    def __init__(self, brand: str, year: int, doors: int) -> None:
        """
        Constructor for Car.

        Args:
            brand (str): Brand name.
            year (int): Manufacturing year.
            doors (int): Number of doors.

        Behavior:
            - Calls Vehicle.__init__ for brand and year.
            - Stores doors.
        """
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self) -> str:
        """
        Return a description of the car including doors.

        Returns:
            str: For example, "Toyota (2020) - 4 doors".
        """
        base_info = super().get_info()
        return f"{base_info} - {self.doors} doors"


class Motorcycle(Vehicle):
    """
    Motorcycle represents a motorcycle vehicle.

    Attributes:
        moto_type (str): Type of motorcycle (for example, "Sport", "Cruiser").

    Methods:
        get_info() -> str:
            Return a description including brand, year, and motorcycle type.
    """

    def __init__(self, brand: str, year: int, moto_type: str) -> None:
        """
        Constructor for Motorcycle.

        Args:
            brand (str): Brand name.
            year (int): Manufacturing year.
            moto_type (str): Type of motorcycle.

        Behavior:
            - Calls Vehicle.__init__ for brand and year.
            - Stores moto_type.
        """
        super().__init__(brand, year)
        self.moto_type = moto_type

    def get_info(self) -> str:
        """
        Return a description of the motorcycle including its type.

        Returns:
            str: For example, "Yamaha (2022) - Type: Sport".
        """
        base_info = super().get_info()
        return f"{base_info} - Type: {self.moto_type}"


# Example usage (for manual testing):
if __name__ == "__main__":
    vehicle1 = Car("Toyota", 2020, 4)
    vehicle2 = Motorcycle("Yamaha", 2022, "Sport")

    print(vehicle1.get_info())  # Toyota (2020) - 4 doors
    print(vehicle2.get_info())  # Yamaha (2022) - Type: Sport