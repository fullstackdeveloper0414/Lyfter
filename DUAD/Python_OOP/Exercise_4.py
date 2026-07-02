"""
Ejercicios de OOP
Jaime C Smith
07/01/2026
"""

"""
Exercise 4 – Human composed of body-part classes.

This exercise asks us to:
- Create classes: Head, Torso, Arm, Hand, Leg, Feet.
- Create a Human class and connect all these classes logically through
  attributes.

The idea is to model a human body using composition: each Human has a
Torso, and the Torso holds references to the Head, Arms, Legs, Hands,
and Feet. Each part is its own class so we can later add specialized
attributes or methods if needed.
"""


class Head:
    """
    Head represents the head of a human.

    For now, it is a minimal class. In a more advanced version, we
    could add attributes like hair_color or eye_color, and methods like
    speak() or think().
    """

    def __init__(self) -> None:
        """
        Constructor for Head.

        Currently it does not initialize any attributes, but this is
        where we would set them up in the future.
        """
        pass


class Hand:
    """
    Hand represents a human hand.

    This class could later include attributes like finger_count and
    methods such as grab() or wave().
    """

    def __init__(self) -> None:
        """
        Constructor for Hand.

        The hand is created without specific attributes for now.
        """
        pass


class Arm:
    """
    Arm represents an arm that is connected to a hand.

    Attributes:
        hand (Hand): The hand attached to this arm.
    """

    def __init__(self, hand: Hand) -> None:
        """
        Constructor for Arm.

        Args:
            hand (Hand): The hand to attach to this arm.

        This models the idea that an arm includes a hand at the end.
        """
        self.hand = hand


class Feet:
    """
    Feet represents a pair of feet.

    In a more complex design, we could have separate classes for each
    foot, but here we model both feet together for simplicity.
    """

    def __init__(self) -> None:
        """
        Constructor for Feet.

        Currently this class does not define specific attributes, but
        it gives us a place to add them later (for example, shoe_size).
        """
        pass


class Leg:
    """
    Leg represents a leg that is connected to feet.

    Attributes:
        feet (Feet): The feet attached to this leg.
    """

    def __init__(self, feet: Feet) -> None:
        """
        Constructor for Leg.

        Args:
            feet (Feet): The feet to attach to this leg.

        This represents a leg ending in feet.
        """
        self.feet = feet


class Torso:
    """
    Torso represents the central part of the body, connecting head,
    arms, and legs.

    Attributes:
        head (Head): The head that belongs to this torso.
        right_arm (Arm): The right arm attached to the torso.
        left_arm (Arm): The left arm attached to the torso.
        right_leg (Leg): The right leg attached to the torso.
        left_leg (Leg): The left leg attached to the torso.
    """

    def __init__(
        self,
        head: Head,
        right_arm: Arm,
        left_arm: Arm,
        right_leg: Leg,
        left_leg: Leg,
    ) -> None:
        """
        Constructor for Torso.

        Args:
            head (Head): Head instance.
            right_arm (Arm): Right arm instance.
            left_arm (Arm): Left arm instance.
            right_leg (Leg): Right leg instance.
            left_leg (Leg): Left leg instance.

        This torso object ties all the main body parts together, making
        it possible to represent a full human body by linking them.
        """
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Human:
    """
    Human represents a complete human body composed of body parts.

    Attributes:
        torso (Torso): The torso that connects the head, arms, and legs.
    """

    def __init__(self) -> None:
        """
        Constructor for Human.

        This constructor builds all the body parts and connects them
        together:

        - Creates a Head.
        - Creates two Hands (right and left).
        - Creates two Arms, each connected to one Hand.
        - Creates two Feet objects.
        - Creates two Legs, each connected to one Feet object.
        - Creates a Torso that holds the Head, both Arms, and both Legs.

        All of these parts are stored inside the Human instance through
        the torso attribute.
        """
        # Create head
        head = Head()

        # Create hands and arms
        right_hand = Hand()
        left_hand = Hand()
        right_arm = Arm(right_hand)
        left_arm = Arm(left_hand)

        # Create feet and legs
        right_feet = Feet()
        left_feet = Feet()
        right_leg = Leg(right_feet)
        left_leg = Leg(left_feet)

        # Connect everything through the torso
        self.torso = Torso(head, right_arm, left_arm, right_leg, left_leg)


# Example usage (for manual testing):
if __name__ == "__main__":
    person = Human()
    print("Human created with:")
    print("Head:", person.torso.head)
    print("Right arm:", person.torso.right_arm)
    print("Right hand:", person.torso.right_arm.hand)
    print("Right leg:", person.torso.right_leg)
    print("Right feet:", person.torso.right_leg.feet)