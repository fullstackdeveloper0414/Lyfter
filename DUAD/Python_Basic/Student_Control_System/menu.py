"""
Student Control System
Jaime C Smith
06/25/2026
"""

# ============================
# menu.py
# ============================
"""
Menu module.

This module contains all logic related to the menu of options:
- Displaying the main menu.
- Validating the chosen menu option.
- Dispatching actions to the appropriate functions.

It also manages:
- The in-memory list of student dictionaries.
- A simple flag indicating whether there are unsaved changes since
  the last successful export or import, so the user can be warned
  before exiting.
- A help option that explains what each menu option does.
"""

from typing import List, Dict

from actions import (
    add_student,
    show_all_students,
    show_top_3_students,
    show_overall_average,
    delete_student,
    show_failing_students,
    student_exists,
)
from data import export_students_to_csv, import_students_from_csv
from logger import log_event

# Type alias for better readability
Student = Dict[str, object]


def _print_menu() -> None:
    """
    Print the main menu options for the user.
    """
    print("\n========================================")
    print(" Student Control System - Main Menu ")
    print("========================================")
    print("1. Add students")
    print("2. View all students")
    print("3. View top 3 students by average grade")
    print("4. View overall average grade (all students)")
    print("5. Export students to CSV")
    print("6. Import students from CSV")
    print("7. Delete a student (name + section)")
    print("8. View failing students")
    print("9. Exit")
    print("H. Help (show menu descriptions)")
    print("========================================")


def _print_help() -> None:
    """
    Print a short description of what each menu option does.

    This function is called when the user selects the help command.
    """
    print("\n--- Help: Menu Options ---")
    print("1. Add students")
    print("   - Add one or more students, with full validation of")
    print("     name, section, and grades.")
    print("2. View all students")
    print("   - Show all registered students and their average grade.")
    print("3. View top 3 students by average grade")
    print("   - Show the three students with the highest average grade.")
    print("4. View overall average grade (all students)")
    print("   - Show the average of all students' average grades.")
    print("5. Export students to CSV")
    print("   - Save all current student data to a CSV file for backup.")
    print("6. Import students from CSV")
    print("   - Load student data from a previously exported CSV file.")
    print("     If there are already students in memory, you can choose")
    print("     to overwrite or append the CSV data.")
    print("7. Delete a student (name + section)")
    print("   - Remove a student after confirming, using name and section.")
    print("8. View failing students")
    print("   - Show students who have at least one failing subject.")
    print("9. Exit")
    print("   - Exit the program. You will be warned if there are")
    print("     unsaved changes.")
    print("H. Help")
    print("   - Show this help information.")
    print("----------------------------------------")


def _get_valid_menu_option() -> str:
    """
    Request a valid menu option from the user.

    Returns:
        A string representing the chosen option:
        '1'..'9' for numeric options, or 'H'/'h' for help.
    """
    while True:
        option_str = input("Choose an option (1-9 or H for help): ").strip()

        if option_str.lower() == "h":
            return "H"

        if option_str.isdigit():
            if 1 <= int(option_str) <= 9:
                return option_str

        print("Invalid input. Please enter a number between 1 and 9, or H for help.")


def _merge_imported_students(
    current_students: List[Student], imported_students: List[Student]
) -> int:
    """
    Merge (append) imported students into the current list, skipping duplicates.

    Args:
        current_students: Students already in memory.
        imported_students: Students loaded from the CSV file.

    Returns:
        The number of students successfully appended.
    """
    appended = 0

    for student in imported_students:
        full_name = str(student["full_name"])
        section = str(student["section"])
        if student_exists(current_students, full_name, section):
            # Skip duplicates
            log_event(
                "Skipped imported duplicate student: name='{}', section='{}'",
                full_name,
                section,
            )
            continue

        current_students.append(student)
        appended += 1
        log_event(
            "Appended imported student: name='{}', section='{}'",
            full_name,
            section,
        )

    return appended


def run_menu() -> None:
    """
    Run the main menu loop.

    This function keeps a list of students in memory and allows
    the user to perform different actions until they choose to exit.

    It also tracks whether there are unsaved changes and warns the user
    before exiting if data has not been exported to CSV.
    """
    students: List[Student] = []
    # True when in-memory data has changed since the last export or import
    students_changed: bool = False

    print("Welcome to the Student Control System.")
    print("Use the menu to manage students and their grades.\n")

    while True:
        _print_menu()
        option = _get_valid_menu_option()
        log_event("User selected menu option '{}'", option)

        if option == "H":
            _print_help()
            continue

        if option == "1":
            # Add students
            added_any = add_student(students)
            if added_any:
                students_changed = True

        elif option == "2":
            # View all students
            show_all_students(students)

        elif option == "3":
            # View top 3 students
            show_top_3_students(students)

        elif option == "4":
            # View overall average
            show_overall_average(students)

        elif option == "5":
            # Export to CSV
            export_success = export_students_to_csv(students)
            if export_success:
                # After a successful export, memory and CSV are in sync.
                students_changed = False
            print("Export action completed (see any errors above).")

        elif option == "6":
            # Import from CSV
            imported_students = import_students_from_csv()

            # Only proceed if the CSV import actually returned data
            if imported_students is not None:
                if not students:
                    # No students in memory yet: simply load the CSV data.
                    # After this import, memory matches the CSV exactly,
                    # so we do not consider there to be unsaved changes.
                    students = imported_students
                    students_changed = False
                    log_event(
                        "Import without existing students: in-memory list initialized "
                        "from CSV data ({} students).",
                        len(students),
                    )
                else:
                    # There are already students in memory: ask how to combine data.
                    print("\nImport mode:")
                    print("1. Overwrite current students with CSV data.")
                    print("2. Append CSV data to current students (skip duplicates).")
                    mode = input("Choose import mode (1 or 2): ").strip()

                    if mode == "1":
                        # Overwrite mode: memory now matches the CSV contents.
                        students = imported_students
                        students_changed = False
                        print("Current student list has been replaced by imported data.")
                        log_event(
                            "Import mode: overwrite. Current students replaced "
                            "by CSV data ({} students).",
                            len(students),
                        )
                    elif mode == "2":
                        # Append mode: new students are added on top of what
                        # the CSV contains, so these are unsaved changes.
                        appended_count = _merge_imported_students(
                            students, imported_students
                        )
                        if appended_count > 0:
                            students_changed = True
                        print(
                            f"Imported data appended. "
                            f"{appended_count} students were added."
                        )
                        log_event(
                            "Import mode: append. {} students appended from CSV.",
                            appended_count,
                        )
                    else:
                        print(
                            "Invalid input. Import mode must be 1 (overwrite) or 2 (append). "
                            "No changes were applied."
                        )
                        log_event(
                            "Import mode selection invalid. No changes applied to students."
                        )

        elif option == "7":
            # Delete student
            deleted = delete_student(students)
            if deleted:
                students_changed = True

        elif option == "8":
            # View failing students
            show_failing_students(students)

        elif option == "9":
            # Exit with unsaved changes warning ONLY if there are changes
            if students_changed:
                print(
                    "You have unsaved changes. Would you like to export to CSV "
                    "before exiting? (yes/no)"
                )
                answer = input("> ").strip().lower()
                if answer in ("yes", "y"):
                    export_success = export_students_to_csv(students)
                    if export_success:
                        students_changed = False

            print("Exiting the program. Goodbye!")
            log_event("Program exited by user.")
            break