"""
Ejercicios Extra de Los 4 Pilares de OOP
Jaime C Smith
07/04/2026
"""

"""
Section 2 – Abstract User, AdminUser, RegularUser (Abstraction and Polymorphism)

Requirements:
- Create an abstract class User with abstract methods:
  - get_role()
  - has_permission(permission)
- Then create two classes that inherit from User:
  - AdminUser
  - RegularUser
- Each must implement the methods.
  - AdminUser always has permissions.
  - RegularUser has limited permissions (for example, only "read").

Example:
    user1 = AdminUser("Carlos")
    user2 = RegularUser("Andrea")

    print(user1.has_permission("delete"))  # True
    print(user2.has_permission("delete"))  # False

The purpose of this section is to show:
- Abstraction: User defines a contract for roles and permissions.
- Polymorphism: Different user types implement has_permission() in their
  own way but can be used through the common User interface.
"""

from abc import ABC, abstractmethod
# If you want type hints that work on older Python, you can also do:
# from typing import List


class User(ABC):
    """
    User is an abstract base class representing a generic system user.

    Attributes:
        name (str): The name of the user.

    Abstract methods:
        get_role() -> str:
            Return the role of the user (for example, "admin" or "regular").
        has_permission(permission: str) -> bool:
            Return True if the user has the given permission; False otherwise.
    """

    def __init__(self, name: str) -> None:
        """
        Constructor for User.

        Args:
            name (str): Name of the user.
        """
        self.name = name

    @abstractmethod
    def get_role(self) -> str:
        """
        Return the role of the user.

        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def has_permission(self, permission: str) -> bool:
        """
        Check whether the user has a given permission.

        Must be implemented by subclasses.

        Args:
            permission (str): The permission identifier (for example, "read", "delete").
        """
        pass


class AdminUser(User):
    """
    AdminUser represents an administrator user.

    Behavior:
        - Role is "admin".
        - Admin users are considered to have all permissions (always True).
    """

    def get_role(self) -> str:
        """
        Return the role of the user.

        Returns:
            str: "admin".
        """
        return "admin"

    def has_permission(self, permission: str) -> bool:
        """
        Admin users always have permission.

        Args:
            permission (str): Permission identifier (ignored for admins).

        Returns:
            bool: Always True.
        """
        return True


class RegularUser(User):
    """
    RegularUser represents a normal, non-admin user.

    Behavior:
        - Role is "regular".
        - Regular users have limited permissions (for example, "read" only).
    """

    def __init__(self, name: str, allowed_permissions=None) -> None:
        """
        Constructor for RegularUser.

        Args:
            name (str): Name of the user.
            allowed_permissions (list | None): Optional list of
                permissions this user has. Defaults to ["read"] if not provided.

        Note:
            We avoid using list[str] in the type hint to stay compatible
            with older Python/Thonny versions that do not support this syntax.
        """
        super().__init__(name)
        # By default, a regular user can only "read"
        self.allowed_permissions = allowed_permissions or ["read"]

    def get_role(self) -> str:
        """
        Return the role of the user.

        Returns:
            str: "regular".
        """
        return "regular"

    def has_permission(self, permission: str) -> bool:
        """
        Check whether the user has the given permission.

        Args:
            permission (str): Permission identifier.

        Returns:
            bool: True if permission is in allowed_permissions; False otherwise.
        """
        return permission in self.allowed_permissions


# Example usage (for manual testing):
if __name__ == "__main__":
    user1 = AdminUser("Carlos")
    user2 = RegularUser("Andrea")  # default allowed_permissions = ["read"]

    print(f"{user1.name} ({user1.get_role()}) delete permission:", user1.has_permission("delete"))  # True
    print(f"{user2.name} ({user2.get_role()}) delete permission:", user2.has_permission("delete"))  # False
    print(f"{user2.name} ({user2.get_role()}) read permission:", user2.has_permission("read"))      # True