"""
Student Control System
Jaime C Smith
06/25/2026
"""

# ============================
# main.py
# ============================
"""
Main module.

This module contains the entry point for the Student Control System.
It starts the command-line menu so the user can manage students and their grades.
"""

from menu import run_menu


def main() -> None:
    """
    Main function that starts the menu loop for the student control system.
    """
    run_menu()


if __name__ == "__main__":
    main()
