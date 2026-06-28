"""
Student Control System
Jaime C Smith
06/25/2026
"""

# ============================
# actions.py
# ============================
"""
Actions module.

This module contains the logic for all menu actions except CSV export and import:
- Adding students and validating their data.
- Viewing all students and their averages.
- Viewing the top 3 students by average grade.
- Viewing the overall average grade across all students.
- Deleting students (optional extra requirement).
- Viewing failing students (optional extra requirement).

Each student record is stored as a dictionary with the following keys:
- full_name        -> student's full name
- section          -> class section (for example, 11B)
- spanish          -> Spanish language grade
- english          -> English language grade
- social_studies   -> Social studies grade
- science          -> Science grade

Helper functions that are meant for internal use inside this module are
prefixed with an underscore. User-facing functions such as add_student,
show_all_students, show_top_3_students, show_overall_average, delete_student,
and show_failing_students are not prefixed and form the public API.
"""

from typing import List, Dict, Optional, Tuple

from config import SUBJECTS, PASSING_GRADE
from logger import log_event

# Type alias for better readability
Student = Dict[str, object]


# ------------- Internal validation helpers (prefixed with _) ------------- #
def _is_valid_name(full_name: str) -> bool:
    """
    Validate that the student's full name is not empty and contains no digits.

    Args:
        full_name: The full name entered by the user.

    Returns:
        True if the name is valid, False otherwise.
    """
    if not full_name.strip():
        return False

    # Name should not contain digits
    for char in full_name:
        if char.isdigit():
            return False

    return True


def _is_valid_section(section: str) -> bool:
    """
    Validate that the section follows a format like '10A', '11B', etc.

    Requirements:
    - At least 2 characters.
    - All characters except the last are digits.
    - The last character is an alphabetical letter.

    Args:
        section: The section string entered by the user.

    Returns:
        True if the section is valid, False otherwise.
    """
    section = section.strip()

    if len(section) < 2:
        return False

    number_part = section[:-1]
    letter_part = section[-1]

    if not number_part.isdigit():
        return False

    if not letter_part.isalpha():
        return False

    return True


def student_exists(students: List[Student], full_name: str, section: str) -> bool:
    """
    Check if a student with the given name and section already exists.

    This function is part of the public API because it is also used
    by the menu when merging imported students.

    Args:
        students: Current list of student dictionaries.
        full_name: Full name to check.
        section: Section to check.

    Returns:
        True if a student with the same name and section exists, False otherwise.
    """
    full_name_lower = full_name.strip().lower()
    section_upper = section.strip().upper()

    for student in students:
        if (
            str(student["full_name"]).strip().lower() == full_name_lower
            and str(student["section"]).strip().upper() == section_upper
        ):
            return True

    return False


def _get_valid_full_name() -> str:
    """
    Prompt the user until a valid full name is entered.

    The name must not be empty and must not contain numbers.
    """
    while True:
        full_name = input("Enter student's full name: ").strip()
        if _is_valid_name(full_name):
            return full_name

        print(
            "Invalid input. The name must not be empty and must not contain numbers.\n"
            "Please try again."
        )


def _get_valid_section() -> str:
    """
    Prompt the user until a valid section is entered.

    The section must follow a format like 10A, 11B, 12C, etc.
    """
    while True:
        section = input("Enter student's section (e.g., 10A, 11B): ").strip().upper()
        if _is_valid_section(section):
            return section

        print(
            "Invalid input. The section must be a number followed by a letter, "
            "for example: 10A, 11B, 12C. Please try again."
        )


def _get_valid_grade(subject_name: str) -> float:
    """
    Prompt the user until a valid numeric grade between 0 and 100 is entered.

    Args:
        subject_name: Name of the subject, used in the prompt.

    Returns:
        A float grade value between 0 and 100.
    """
    while True:
        grade_str = input(f"Enter grade for {subject_name} (0-100): ").strip()
        try:
            grade = float(grade_str)
        except ValueError:
            print(
                "Invalid input. Please enter a numeric grade value between 0 and 100."
            )
            continue

        if 0 <= grade <= 100:
            return grade

        print("Invalid input. Grade out of range. Please enter a value between 0 and 100.")


# ------------- Public actions ------------- #
def add_student(students: List[Student]) -> bool:
    """
    Add one or more students to the current list.

    This function:
    - Asks how many students will be added.
    - For each student, asks for:
      - Full name (validated).
      - Section (validated).
      - Four subject grades (validated from 0 to 100).
    - Prevents duplicate students (same name and section).
    - Returns True if at least one student was added, False otherwise.

    Args:
        students: Current list of student dictionaries.

    Returns:
        True if any student was added, False otherwise.
    """
    print("\n--- Add Students ---")

    while True:
        count_str = input("How many students do you want to add? ").strip()
        if not count_str.isdigit():
            print("Invalid input. Please enter a valid positive number.")
            continue

        count = int(count_str)
        if count <= 0:
            print("Invalid input. Please enter a number greater than zero.")
            continue

        break

    added_any = False

    for i in range(1, count + 1):
        print(f"\nAdding student {i} of {count}")
        full_name = _get_valid_full_name()
        section = _get_valid_section()

        # Check for duplicates
        if student_exists(students, full_name, section):
            print(
                "Invalid input. A student with this name and section already exists.\n"
                "This student will not be added. Please use a different "
                "combination of name and section."
            )
            log_event(
                "Duplicate student prevented: name='{}', section='{}'",
                full_name,
                section,
            )
            continue

        # Get grades
        spanish = _get_valid_grade("Spanish")
        english = _get_valid_grade("English")
        social_studies = _get_valid_grade("Social Studies")
        science = _get_valid_grade("Science")

        # Create and append student record (dictionary)
        student: Student = {
            "full_name": full_name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "social_studies": social_studies,
            "science": science,
        }
        students.append(student)
        added_any = True
        print(f"Student '{full_name}' (section {section}) added successfully.")
        log_event("Added student: name='{}', section='{}'", full_name, section)

    return added_any


def show_all_students(students: List[Student]) -> None:
    """
    Print the information of all students, including their average grade.

    Args:
        students: Current list of student dictionaries.
    """
    print("\n--- All Students ---")

    if not students:
        print("No students have been registered yet.")
        return

    for index, student in enumerate(students, start=1):
        average = calculate_student_average(student)
        print("----------------------------------------")
        print(f"Student #{index}")
        print(f"Name   : {student['full_name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish: {student['spanish']}")
        print(f"English: {student['english']}")
        print(f"Social : {student['social_studies']}")
        print(f"Science: {student['science']}")
        print(f"Average: {average:.2f}")
    print("----------------------------------------")
    print("Tip: Use option 5 to export these students to CSV for backup.")


def calculate_student_average(student: Student) -> float:
    """
    Calculate the average grade for a single student.

    The average is computed from the four subject grades:
    Spanish, English, Social Studies, and Science.

    Args:
        student: Dictionary with student data.

    Returns:
        The average of the four subject grades.
    """
    total = (
        float(student["spanish"])
        + float(student["english"])
        + float(student["social_studies"])
        + float(student["science"])
    )
    return total / 4.0


def show_top_3_students(students: List[Student]) -> None:
    """
    Show the top 3 students with the highest average grade.

    If there are fewer than 3 students, show as many as available.

    Args:
        students: Current list of student dictionaries.
    """
    print("\n--- Top 3 Students by Average Grade ---")

    if not students:
        print("No students have been registered yet.")
        return

    # Create a list of (student, average) tuples
    students_with_avg: List[Tuple[Student, float]] = [
        (student, calculate_student_average(student)) for student in students
    ]

    # Sort by average grade in descending order
    students_with_avg.sort(key=lambda item: item[1], reverse=True)

    top_count = min(3, len(students_with_avg))
    for position in range(top_count):
        student, avg = students_with_avg[position]
        print("----------------------------------------")
        print(f"Rank #{position + 1}")
        print(f"Name   : {student['full_name']}")
        print(f"Section: {student['section']}")
        print(f"Average: {avg:.2f}")
    print("----------------------------------------")
    print("Tip: Use option 5 to export these results to CSV for backup.")


def show_overall_average(students: List[Student]) -> None:
    """
    Show the average of all students' average grades.

    Args:
        students: Current list of student dictionaries.
    """
    print("\n--- Overall Average Grade ---")

    if not students:
        print("No students have been registered yet.")
        return

    total_average = 0.0
    for student in students:
        total_average += calculate_student_average(student)

    overall = total_average / len(students)
    print(f"The overall average grade of all students is: {overall:.2f}")
    print("Tip: Use option 5 to export current student data to CSV for backup.")


# ------------- Extra: delete student ------------- #
def _find_student_index(
    students: List[Student], full_name: str, section: str
) -> Optional[int]:
    """
    Find the index of a student by name and section.

    Args:
        students: Current list of student dictionaries.
        full_name: Full name to locate.
        section: Section to locate.

    Returns:
        Index of the student if found, otherwise None.
    """
    full_name_lower = full_name.strip().lower()
    section_upper = section.strip().upper()

    for index, student in enumerate(students):
        if (
            str(student["full_name"]).strip().lower() == full_name_lower
            and str(student["section"]).strip().upper() == section_upper
        ):
            return index

    return None


def delete_student(students: List[Student]) -> bool:
    """
    Delete a student using their name and section.

    This function:
    - Asks for full name and section.
    - Validates that the student exists.
    - Asks for confirmation before deleting.
    - Returns True if a student was deleted, False otherwise.

    Args:
        students: Current list of student dictionaries (modified in place).

    Returns:
        True if a student record was deleted, False otherwise.
    """
    print("\n--- Delete Student ---")

    if not students:
        print("No students have been registered yet.")
        return False

    full_name = _get_valid_full_name()
    section = _get_valid_section()

    index = _find_student_index(students, full_name, section)
    if index is None:
        print("Invalid input. The specified student was not found.")
        return False

    # Show student information before deletion
    student = students[index]
    print("Student found:")
    print(f"Name   : {student['full_name']}")
    print(f"Section: {student['section']}")

    confirmation = input(
        "Are you sure you want to delete this student? (yes/no): "
    ).strip().lower()

    if confirmation not in ("yes", "y"):
        print("Deletion canceled. Student was not removed.")
        return False

    # Remove student
    removed_student = students.pop(index)
    print(
        f"Student '{removed_student['full_name']}' "
        f"(section {removed_student['section']}) was deleted successfully."
    )
    log_event(
        "Deleted student: name='{}', section='{}'",
        removed_student["full_name"],
        removed_student["section"],
    )
    return True


# ------------- Extra: failing students ------------- #
def _get_failing_subjects(student: Student) -> List[Tuple[str, float]]:
    """
    Get a list of subjects where the student has a failing grade.

    A failing grade is defined as any grade strictly less than PASSING_GRADE.

    Args:
        student: Dictionary with student data.

    Returns:
        List of (subject_name, grade) tuples for failed subjects.
    """
    failing: List[Tuple[str, float]] = []

    for subject in SUBJECTS:
        grade = float(student[subject])
        if grade < PASSING_GRADE:
            failing.append((subject, grade))

    return failing


def show_failing_students(students: List[Student]) -> None:
    """
    Show all students who have at least one failing subject.

    For each failing student, print:
    - Full name
    - Section
    - Each failing subject and its grade

    Args:
        students: Current list of student dictionaries.
    """
    print("\n--- Failing Students ---")

    if not students:
        print("No students have been registered yet.")
        return

    any_failing = False

    for student in students:
        failing_subjects = _get_failing_subjects(student)
        if failing_subjects:
            any_failing = True
            print("----------------------------------------")
            print(f"Name   : {student['full_name']}")
            print(f"Section: {student['section']}")
            print("Failing subjects:")
            for subject_name, grade in failing_subjects:
                # Make subject name more readable
                pretty_name = subject_name.replace("_", " ").title()
                print(f"  - {pretty_name}: {grade}")

    if not any_failing:
        print("There are no failing students at this moment.")
    else:
        print("----------------------------------------")
        print("Tip: Use option 5 to export current student data to CSV for backup.")