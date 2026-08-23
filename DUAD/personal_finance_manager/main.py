"""
Personal Finance Manager
Application entry point.

Expected outcome:
- Saved categories, movements, and settings load at startup.
- A FinanceManager object receives the data.
- The graphical application begins.
"""

from interface import run_application
from logic import FinanceManager
from persistence import load_categories, load_movements, load_settings


def main() -> None:
    """
    Load application data and launch the graphical interface.

    Expected outcome:
    The application starts with previously saved categories, movements,
    and user-interface settings when available.
    """
    finance_manager = FinanceManager(
        categories=load_categories(),
        movements=load_movements(),
        settings=load_settings(),
    )

    run_application(finance_manager)


if __name__ == "__main__":
    main()