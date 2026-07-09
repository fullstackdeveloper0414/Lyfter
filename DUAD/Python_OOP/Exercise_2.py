"""
Ejercicios de OOP
Jaime C Smith
07/01/2026
"""

"""
Exercise 2 – Bus class to manage passengers.

This exercise asks us to create a Bus class with:
- An attribute max_passengers: the maximum capacity of the bus.
- A method to add passengers one by one, accepting a Person instance
  (from the OOP lesson). It should only add a passenger when the bus
  currently has fewer passengers than its maximum; otherwise, it should
  show a message indicating that the bus is full.
- A method to remove passengers one by one (in any order).

The purpose of the code below is to model a bus as an object that holds
Person objects in a list. We enforce the maximum capacity and allow
adding and removing passengers in a simple way that matches the
exercise requirements.
"""

from typing import List, Optional


class Person:
    """
    Person represents an individual passenger.

    This is a simplified version of the Person class shown in the OOP
    lesson. It includes just a name attribute so the Bus can store
    readable passenger information.

    Attributes:
        name (str): The name of the person.
    """

    def __init__(self, name: str) -> None:
        """
        Constructor for Person.

        Args:
            name (str): Name of the person. This is stored as an
                attribute so we can later identify the passenger.
        """
        self.name = name

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of Person.

        This makes it easier to see who is inside the bus when we print
        the passenger list.
        """
        return f"Person(name='{self.name}')"


class Bus:
    """
    Bus represents a bus that can carry passengers.

    Attributes:
        max_passengers (int): Maximum number of passengers allowed.
        passengers (list[Person]): The current list of passengers.

    Methods:
        add_passenger(person: Person) -> None:
            Add a Person to the bus if there is available capacity.
            Otherwise, print a message saying the bus is full.

        remove_passenger() -> Optional[Person]:
            Remove and return a passenger from the bus. If the bus has
            no passengers, print a message and return None.
    """

    def __init__(self, max_passengers: int) -> None:
        """
        Constructor for Bus.

        Args:
            max_passengers (int): Maximum number of passengers the bus
                can carry.

        The bus starts empty, so passengers is initialized as an empty
        list. We only allow adding passengers until we reach the limit.
        """
        self.max_passengers = max_passengers
        self.passengers: List[Person] = []

    def add_passenger(self, person: Person) -> None:
        """
        Add a new passenger to the bus if capacity allows.

        Args:
            person (Person): The passenger to add to the bus.

        Behavior:
            - If current number of passengers is less than max_passengers,
              append the person to the passengers list and show a
              confirmation message.
            - Otherwise, print a message indicating the bus is full and
              do not add the person.
        """
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(
                f"Passenger '{person.name}' boarded the bus. "
                f"Total passengers: {len(self.passengers)}."
            )
        else:
            print(
                "Cannot add passenger. The bus is full "
                f"(maximum {self.max_passengers} passengers)."
            )

    def remove_passenger(self) -> Optional[Person]:
        """
        Remove a passenger from the bus and return them.

        Returns:
            Optional[Person]:
                - A Person object if someone was removed.
                - None if the bus had no passengers.

        Behavior:
            - If there is at least one passenger, remove the last one
              added (LIFO order) and print a message.
            - If there are no passengers, print a message and return None.

        The exercise states we can remove passengers in any order, so
        choosing the last passenger in the list is a simple strategy.
        """
        if not self.passengers:
            print("Cannot remove passenger. The bus is empty.")
            return None

        removed = self.passengers.pop()
        print(
            f"Passenger '{removed.name}' left the bus. "
            f"Remaining passengers: {len(self.passengers)}."
        )
        return removed


# Example usage (for manual testing):
if __name__ == "__main__":
    # Create a bus with capacity for 2 passengers
    bus = Bus(max_passengers=2)

    # Create some people
    alice = Person("Alice")
    bob = Person("Bob")
    charlie = Person("Charlie")

    # Try boarding passengers
    bus.add_passenger(alice)
    bus.add_passenger(bob)
    bus.add_passenger(charlie)  # should say the bus is full

    # Remove passengers
    bus.remove_passenger()
    bus.remove_passenger()
    bus.remove_passenger()  # should say the bus is empty