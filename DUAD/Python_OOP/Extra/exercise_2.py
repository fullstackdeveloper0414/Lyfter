"""
Ejercicios Extra de OOP
Jaime C Smith
07/01/2026
"""

"""
Exercise 2 – Animal base class with Dog and Cat subclasses.

This exercise asks us to create:
- A base class Animal with:
  - A name attribute.
  - A method speak() that returns "Makes a sound".
- A Dog class that inherits from Animal and overrides speak() to say "Guau".
- A Cat class that inherits from Animal and overrides speak() to say "Miau".

The purpose of this code is to demonstrate inheritance and method
overriding: Dog and Cat reuse the Animal constructor for the name but
provide their own implementations of speak().
"""


class Animal:
    """
    Animal is a base class representing a generic animal.

    Attributes:
        name (str): The name of the animal.

    Methods:
        speak() -> str:
            Return a generic message "Makes a sound". Subclasses
            override this to provide specific sounds.
    """

    def __init__(self, name: str) -> None:
        """
        Constructor for Animal.

        Args:
            name (str): Name of the animal. This identifies the instance.
        """
        self.name = name

    def speak(self) -> str:
        """
        Return a generic sound description for the animal.

        Returns:
            str: The text "Makes a sound".

        In subclasses like Dog and Cat, this method will be overridden
        to return more specific sounds.
        """
        return "Makes a sound"


class Dog(Animal):
    """
    Dog represents a dog and specializes the Animal class.

    It inherits the name attribute from Animal and overrides speak()
    to return "Guau".
    """

    def speak(self) -> str:
        """
        Return the sound that a dog makes.

        Returns:
            str: The text "Guau".
        """
        return "Guau"


class Cat(Animal):
    """
    Cat represents a cat and specializes the Animal class.

    It inherits the name attribute from Animal and overrides speak()
    to return "Miau".
    """

    def speak(self) -> str:
        """
        Return the sound that a cat makes.

        Returns:
            str: The text "Miau".
        """
        return "Miau"


# Example usage (for manual testing):
if __name__ == "__main__":
    dog = Dog("Firulais")
    cat = Cat("Michi")

    print(dog.name, "says:", dog.speak())  # Firulais says: Guau
    print(cat.name, "says:", cat.speak())  # Michi says: Miau