"""
Ejercicios de Los 4 Pilares de OOP
Jaime C Smith
07/04/2026
"""

"""
Section 1 – BankAccount and SavingsAccount (Inheritance and Encapsulation)

Requirements:
- Create a BankAccount class that:
  - Has a balance attribute.
  - Has a method to deposit money.
  - Has a method to withdraw money.
- Create a SavingsAccount class that inherits from BankAccount:
  - Has a min_balance attribute that can be set at creation.
  - Raises an error if a withdrawal would make the balance go below
    min_balance. Withdrawals are allowed only if the remaining balance
    stays at or above min_balance.

The purpose of this section is to demonstrate:
- Encapsulation: only methods should change the balance.
- Inheritance: SavingsAccount reuses BankAccount behavior and extends it
  with minimum-balance rules.
"""


class BankAccount:
    """
    BankAccount represents a generic bank account with a balance.

    Attributes:
        balance (float): Current amount of money in the account.

    Methods:
        deposit(amount: float) -> None:
            Increase the balance by a given amount.
        withdraw(amount: float) -> None:
            Decrease the balance by a given amount, if sufficient funds exist.
    """

    def __init__(self, initial_balance: float = 0.0) -> None:
        """
        Constructor for BankAccount.

        Args:
            initial_balance (float): Starting balance. Defaults to 0.0.

        The balance is stored and later modified only through deposit()
        and withdraw() methods to keep access controlled.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit. Must be positive.

        Behavior:
            - If amount is positive, add it to the balance.
            - If amount is zero or negative, raise a ValueError.

        This method encapsulates the logic of increasing the balance.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw. Must be positive.

        Behavior:
            - If amount is positive and less than or equal to balance,
              subtract it from the balance.
            - If amount is zero or negative, raise a ValueError.
            - If amount is greater than balance, raise a ValueError
              because there are not enough funds.

        This method encapsulates the logic of decreasing the balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount


class SavingsAccount(BankAccount):
    """
    SavingsAccount represents a savings account with a minimum balance.

    It inherits the balance and the basic deposit/withdraw methods from
    BankAccount, but adds rules to prevent the balance from going below
    a specified min_balance.

    Attributes:
        min_balance (float): Minimum allowed balance.
    """

    def __init__(self, initial_balance: float = 0.0, min_balance: float = 0.0) -> None:
        """
        Constructor for SavingsAccount.

        Args:
            initial_balance (float): Starting balance.
            min_balance (float): Minimum balance that must be preserved.

        Behavior:
            - Calls the BankAccount constructor to set initial_balance.
            - Stores min_balance.
            - Validates that initial_balance is not below min_balance.
        """
        if initial_balance < min_balance:
            raise ValueError(
                "Initial balance cannot be below the minimum balance."
            )
        super().__init__(initial_balance)
        self.min_balance = min_balance

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the savings account, enforcing min_balance.

        Args:
            amount (float): Amount to withdraw.

        Behavior:
            - Uses the same basic checks as BankAccount (amount > 0).
            - Before withdrawing, calculates the remaining balance:
              remaining = balance - amount.
            - If remaining would be below min_balance, raises a ValueError
              that explains the numbers involved (current balance,
              requested amount, resulting balance, and minimum balance).
            - Otherwise, calls the parent withdraw method to subtract
              the amount from the balance.

        This method uses inheritance and overriding to add extra rules on
        top of the generic BankAccount behavior.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        remaining_balance = self.balance - amount
        if remaining_balance < self.min_balance:
            raise ValueError(
                (
                    "Withdrawal denied: balance cannot go below the minimum balance.\n"
                    f"Current balance: {self.balance}\n"
                    f"Requested withdrawal: {amount}\n"
                    f"Resulting balance: {remaining_balance}\n"
                    f"Minimum allowed balance: {self.min_balance}"
                )
            )

        # Perform the normal withdrawal from the parent class.
        super().withdraw(amount)


# Example usage (for manual testing):
if __name__ == "__main__":
    # BankAccount example
    account = BankAccount(initial_balance=1000)
    account.deposit(500)      # balance -> 1500
    account.withdraw(300)     # balance -> 1200
    print("BankAccount balance:", account.balance)

    # SavingsAccount example
    savings = SavingsAccount(initial_balance=1000, min_balance=200)
    savings.withdraw(700)     # leaves 300, still above min_balance
    print("SavingsAccount balance:", savings.balance)

    try:
        # This withdrawal would leave 150, which is below min_balance (200)
        savings.withdraw(150)
    except ValueError as e:
        print("SavingsAccount error:")
        print(e)