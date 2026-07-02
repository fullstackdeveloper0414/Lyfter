"""
Ejercicios de OOP
Jaime C Smith
07/01/2026
"""

"""
Exercise 3 – Convert Student Control System to use Student objects.

This exercise asks us to modify the existing Student Control System so
that:

- Students are stored as objects of a Student class instead of
  dictionaries.
- When importing from CSV, rows (which arrive as dictionaries) are
  converted into Student objects.
- When exporting to CSV, Student objects are converted into dictionaries.
- Code that used dictionary keys (student['name']) now uses attributes
  (student.name).

The purpose of this code is to show how to define a Student class and
update helper functions that create, import, export, and display
students using objects instead of plain dictionaries. This file is a
self‑contained example that demonstrates the main ideas; you can adapt
the same patterns inside your full Student Control System project.
"""

from typing import List, Dict
import csv
from pathlib import Path


class Student:
    """
    Student represents a student with identification and grades.

    Attributes:
        full_name (str): Student's full name.
        section (str): Student's section (for example, "10A").
        spanish (float): Grade in Spanish.
        english (float): Grade in English.
        social_studies (float): Grade in Social Studies.
        science (float): Grade in Science.
    """

    def __init__(
        self,
        full_name: str,
        section: str,
        spanish: float,
        english: float,
        social_studies: float,
        science: float,
    ) -> None:
        """
        Constructor for Student.

        Args:
            full_name (str): Student's full name.
            section (str): Section where the student belongs.
            spanish (float): Spanish grade.
            english (float): English grade.
            social_studies (float): Social Studies grade.
            science (float): Science grade.

        This constructor stores all these values as attributes so that
        other parts of the program can access them using dot notation,
        like student.full_name or student.spanish.
        """
        self.full_name = full_name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

    def to_dict(self) -> Dict[str, object]:
        """
        Convert this Student object to a dictionary.

        Returns:
            dict: A dictionary with keys matching the CSV columns.

        This method is used when exporting students to a CSV file. The
        CSV writer expects plain dictionaries, so we convert our object
        attributes back to dictionary form.
        """
        return {
            "full_name": self.full_name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social_studies": self.social_studies,
            "science": self.science,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, object]) -> "Student":
        """
        Create a Student object from a dictionary.

        Args:
            data (dict): Dictionary containing student data. It should
                have keys for full_name, section, spanish, english,
                social_studies, and science.

        Returns:
            Student: A new Student instance containing the same data.

        This class method is used when importing from CSV. The CSV
        reader returns rows as dictionaries, so we wrap those values
        into Student objects.
        """
        return cls(
            full_name=str(data.get("full_name", "")),
            section=str(data.get("section", "")),
            spanish=float(data.get("spanish", 0.0)),
            english=float(data.get("english", 0.0)),
            social_studies=float(data.get("social_studies", 0.0)),
            science=float(data.get("science", 0.0)),
        )

    def average(self) -> float:
        """
        Calculate the student's average grade across all subjects.

        Returns:
            float: The arithmetic mean of Spanish, English, Social
            Studies, and Science.

        This is a convenience method that matches what your original
        Student Control System calculates from dictionaries.
        """
        total = (
            self.spanish
            + self.english
            + self.social_studies
            + self.science
        )
        return total / 4.0


# -------- Creation functions (replacing dictionary-based version) --------


def create_student(students_list: List[Student]) -> None:
    """
    Create a new student and add it to the given list.

    This is the OOP version of the earlier function that appended a
    dictionary. Now we create a Student object instead.

    Args:
        students_list (list[Student]): The list where new students will
            be stored.

    Behavior:
        - Ask the user for name, section, and grades via input.
        - Build a Student instance with those values.
        - Append the Student object to students_list.
    """
    print("\n--- Create Student (OOP version) ---")
    full_name = input("Enter student's full name: ")
    section = input("Enter student's section (e.g., 10A, 11B): ")
    spanish = float(input("Enter Spanish grade: "))
    english = float(input("Enter English grade: "))
    social_studies = float(input("Enter Social Studies grade: "))
    science = float(input("Enter Science grade: "))

    # Create a Student object instead of a dictionary.
    student = Student(
        full_name=full_name,
        section=section,
        spanish=spanish,
        english=english,
        social_studies=social_studies,
        science=science,
    )

    students_list.append(student)
    print(f"Student '{student.full_name}' (section {student.section}) created.")


# -------- Import / export helpers using Student objects --------


def import_students_from_csv(file_path: Path) -> List[Student]:
    """
    Import students from a CSV file and convert them into Student objects.

    Args:
        file_path (Path): Path to the CSV file that contains student data.

    Returns:
        list[Student]: A list of Student objects constructed from the
            CSV data.

    Behavior:
        - Open the CSV file.
        - Read rows using csv.DictReader (each row is a dictionary).
        - For each row, create a Student object using Student.from_dict.
        - Return the list of Student objects.
    """
    students: List[Student] = []

    if not file_path.is_file():
        print(f"CSV file '{file_path}' does not exist. No students imported.")
        return students

    with file_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            student = Student.from_dict(row)
            students.append(student)

    print(f"Imported {len(students)} students from '{file_path}'.")
    return students


def export_students_to_csv(students: List[Student], file_path: Path) -> None:
    """
    Export a list of Student objects to a CSV file.

    Args:
        students (list[Student]): List of Student objects.
        file_path (Path): Path of the CSV file to write.

    Behavior:
        - Convert each Student into a dictionary using to_dict().
        - Use csv.DictWriter to write all rows to the CSV file.
        - If there are no students, it still writes headers but no rows.
    """
    # Convert Student objects to dictionaries first.
    rows: List[Dict[str, object]] = [student.to_dict() for student in students]

    fieldnames = ["full_name", "section", "spanish", "english", "social_studies", "science"]

    with file_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"Exported {len(students)} students to '{file_path}'.")


# -------- Display / utility functions using Student attributes --------


def show_all_students(students: List[Student]) -> None:
    """
    Display all students using their object attributes.

    Args:
        students (list[Student]): List of Student objects.

    Behavior:
        - If the list is empty, show a message.
        - Otherwise, print each student's name, section, grades, and
          average, accessing attributes via dot notation
          (student.full_name, student.spanish, etc.).
    """
    print("\n--- All Students (OOP version) ---")

    if not students:
        print("No students have been registered yet.")
        return

    for index, student in enumerate(students, start=1):
        avg = student.average()
        print("----------------------------------------")
        print(f"Student #{index}")
        print(f"Name   : {student.full_name}")
        print(f"Section: {student.section}")
        print(f"Spanish: {student.spanish}")
        print(f"English: {student.english}")
        print(f"Social : {student.social_studies}")
        print(f"Science: {student.science}")
        print(f"Average: {avg:.2f}")
    print("----------------------------------------")


def show_overall_average(students: List[Student]) -> None:
    """
    Display the overall average of all students' average grades.

    Args:
        students (list[Student]): List of Student objects.

    Behavior:
        - If there are no students, show a message.
        - Otherwise, compute each student's average and then compute
          the overall mean across all students, printing the result.
    """
    print("\n--- Overall Average Grade (OOP version) ---")

    if not students:
        print("No students have been registered yet.")
        return

    total = 0.0
    for student in students:
        total += student.average()

    overall = total / len(students)
    print(f"The overall average grade of all students is: {overall:.2f}")


# -------- Small demo menu to test the OOP approach --------


def main() -> None:
    """
    Simple demonstration menu for the OOP-based student system.

    This is not the full Student Control System, but a minimal menu to
    show how Student objects are created, displayed, imported, and
    exported.

    Options:
        1. Create a new student (object).
        2. Show all students.
        3. Show overall average.
        4. Import students from CSV (students_data.csv).
        5. Export students to CSV (students_data_export.csv).
        0. Exit.
    """
    students: List[Student] = []
    csv_import_path = Path("students_data.csv")
    csv_export_path = Path("students_data_export.csv")

    while True:
        print("\n--- OOP Student System Demo ---")
        print("1. Create student")
        print("2. Show all students")
        print("3. Show overall average")
        print("4. Import students from CSV")
        print("5. Export students to CSV")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_student(students)
        elif choice == "2":
            show_all_students(students)
        elif choice == "3":
            show_overall_average(students)
        elif choice == "4":
            imported = import_students_from_csv(csv_import_path)
            students.extend(imported)
        elif choice == "5":
            export_students_to_csv(students, csv_export_path)
        elif choice == "0":
            print("Exiting OOP Student System demo.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()