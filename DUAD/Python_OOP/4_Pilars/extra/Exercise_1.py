"""
Ejercicios Extra de Los 4 Pilares de OOP
Jaime C Smith
07/04/2026
"""

"""
Section 1 – Employee (Encapsulation with private attributes and properties)

Requirements:
- Create an Employee class with:
  - Private attributes: _name, _salary.
- Use @property and @<attribute>.setter to:
  - Show (read) the name and salary.
  - Validate that the salary is never negative.
- Create a promote method that increases the salary by a given percentage.

Example:
    employee = Employee("Ana", 1000)
    employee.promote(0.1)  # +10%
    print(employee.salary)  # 1100

The purpose of this section is to demonstrate encapsulation using private
attributes and properties: access to salary is controlled through
getters/setters, and business logic like promotion is implemented in a
clear method.
"""


class Employee:
    """
    Employee represents an employee with a name and a salary.

    Attributes (private):
        _name (str): Employee name.
        _salary (float): Employee salary (must be non-negative).

    Properties:
        name (str): Read-only property for the employee's name.
        salary (float): Read/write property for the salary, with validation.

    Methods:
        promote(percentage: float) -> None:
            Increase the salary by the given percentage (for example, 0.1 = 10%).
    """

    def __init__(self, name: str, salary: float) -> None:
        """
        Constructor for Employee.

        Args:
            name (str): Employee name.
            salary (float): Initial salary. Must be non-negative.

        Behavior:
            - Stores name and salary in private attributes.
            - Validates that salary is not negative.
        """
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self._name = name
        self._salary = salary

    @property
    def name(self) -> str:
        """
        Read-only property that returns the employee's name.

        Returns:
            str: The name of the employee.
        """
        return self._name

    @property
    def salary(self) -> float:
        """
        Property that returns the employee's salary.

        Returns:
            float: The current salary.
        """
        return self._salary

    @salary.setter
    def salary(self, new_salary: float) -> None:
        """
        Setter for the salary property.

        Args:
            new_salary (float): New salary value. Must be non-negative.

        Behavior:
            - If new_salary is negative, raises ValueError.
            - Otherwise, updates the private _salary attribute.
        """
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = new_salary

    def promote(self, percentage: float) -> None:
        """
        Increase the salary by a given percentage.

        Args:
            percentage (float): Promotion percentage. For example:
                - 0.10 means a 10% increase
                - 0.05 means a 5% increase

        Behavior:
            - If percentage is negative, raises ValueError.
            - Otherwise, calculates the increase and updates the salary.
        """
        if percentage < 0:
            raise ValueError("Promotion percentage cannot be negative.")

        increase = self._salary * percentage
        new_salary = self._salary + increase
        self.salary = new_salary  # uses the property setter for validation


# Example usage (for manual testing):
if __name__ == "__main__":
    employee = Employee("Ana", 1000)
    employee.promote(0.10)  # 10% promotion
    print("Employee name:", employee.name)
    print("Employee salary after promotion:", employee.salary)  # 1100