"""
Ejercicios de Los 4 Pilares de OOP
Jaime C Smith
07/04/2026
"""

"""
Section 3 – Multiple Inheritance Example

Short explanation – Uses of multiple inheritance:
- Multiple inheritance allows a class to inherit behavior from more than one parent.
- In Python, it is often used to create “mixin” classes that add focused features
  (such as logging, auditing, permissions, or serialization) to many different
  classes without forcing a deep or complex single inheritance hierarchy.
- This helps keep code modular and reusable: we can combine small, independent
  behaviors as needed in each concrete class. 

Example:
- We define two mixins, LoggingMixin and AuditingMixin.
- We then create BusinessOperation that inherits from both, so it can log messages
  and record audit events while implementing its own business logic.
"""


class LoggingMixin:
    """
    LoggingMixin provides simple logging functionality.

    Methods:
        log(message: str) -> None:
            Print a log message. In a real system, this could write to
            a log file or monitoring service.
    """

    def log(self, message: str) -> None:
        """
        Log a message.

        Args:
            message (str): The message to log.
        """
        print(f"[LOG] {message}")


class AuditingMixin:
    """
    AuditingMixin provides simple auditing functionality.

    Methods:
        audit(action: str, user: str) -> None:
            Print an audit record indicating which user performed which
            action. In a real system, this could be stored in an audit
            database.
    """

    def audit(self, action: str, user: str) -> None:
        """
        Record an audit event.

        Args:
            action (str): The action that was performed.
            user (str): The user who performed the action.
        """
        print(f"[AUDIT] User '{user}' performed action '{action}'.")


class BusinessOperation(LoggingMixin, AuditingMixin):
    """
    BusinessOperation uses multiple inheritance to combine logging and
    auditing capabilities.

    It inherits from LoggingMixin and AuditingMixin, so it can both log
    messages and record audit events, while also implementing its own
    business logic.

    Methods:
        process(user: str, data: str) -> None:
            Simulate a business operation that logs and audits.
    """

    def process(self, user: str, data: str) -> None:
        """
        Perform a business operation that uses logging and auditing.

        Args:
            user (str): The user triggering the operation.
            data (str): Data being processed.

        Behavior:
            - Log that processing started.
            - Audit that the user performed a "process" action.
            - Log that processing finished.

        This shows how multiple inheritance lets us reuse small,
        focused behaviors (mixins) across different classes.
        """
        self.log(f"Starting to process data: {data}")
        self.audit(action="process", user=user)
        self.log("Finished processing data")


# Example usage (for manual testing):
if __name__ == "__main__":
    operation = BusinessOperation()
    operation.process(user="Jaime", data="Monthly financial report")