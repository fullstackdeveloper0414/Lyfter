"""
Student Control System
Jaime C Smith
06/25/2026
"""

# ============================
# data.py
# ============================
"""
Data module.

This module contains all logic for exporting and importing student data
from CSV files. It implements the required functionality:
- Export all current students to a CSV file.
- Import students from a previously exported CSV file.
- Inform the user if no CSV file exists.

It also supports two import modes:
- Overwrite: replace current students with CSV data.
- Append: merge CSV data into current students, skipping duplicate name/section.
"""

import csv
import os
from typing import List, Dict, Optional

from config import CSV_FILE_NAME, SUBJECTS
from logger import log_event

# Type alias for better readability
Student = Dict[str, object]

# CSV headers: full name, section, and all subject names
CSV_HEADERS = ["full_name", "section"] + SUBJECTS


def export_students_to_csv(students: List[Student]) -> bool:
    """
    Export all current students to a CSV file.

    Args:
        students: Current list of student dictionaries.

    Returns:
        True if export succeeded, False otherwise.
    """
    print("\n--- Export Students to CSV ---")

    if not students:
        print("No students have been registered yet. There is nothing to export.")
        return False

    try:
        with open(CSV_FILE_NAME, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=CSV_HEADERS)
            writer.writeheader()

            for student in students:
                row = {
                    "full_name": student["full_name"],
                    "section": student["section"],
                    "spanish": student["spanish"],
                    "english": student["english"],
                    "social_studies": student["social_studies"],
                    "science": student["science"],
                }
                writer.writerow(row)

        print(f"Students were exported successfully to '{CSV_FILE_NAME}'.")
        log_event(
            "Exported {} students to CSV file '{}'", len(students), CSV_FILE_NAME
        )
        return True
    except OSError as error:
        print(f"An error occurred while exporting data to CSV: {error}")
        log_event("Error exporting students to CSV: {}", error)
        return False


def import_students_from_csv() -> Optional[List[Student]]:
    """
    Import students from a previously exported CSV file.

    Returns:
        A list of students if the file exists and is loaded successfully.
        None if the file does not exist or an error occurs.
    """
    print("\n--- Import Students from CSV ---")

    if not os.path.exists(CSV_FILE_NAME):
        print(
            "No CSV file was found. "
            "Make sure to export data before attempting to import."
        )
        log_event(
            "Import failed: CSV file '{}' does not exist.", CSV_FILE_NAME
        )
        return None

    students: List[Student] = []

    try:
        with open(CSV_FILE_NAME, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            # Validate that all required headers are present
            if reader.fieldnames is None:
                print("The CSV file is empty or has no headers.")
                log_event("Import failed: CSV file has no headers.")
                return None

            missing_headers = [h for h in CSV_HEADERS if h not in reader.fieldnames]
            if missing_headers:
                print(
                    "The CSV file does not have the expected structure. "
                    f"Missing columns: {', '.join(missing_headers)}"
                )
                log_event(
                    "Import failed: CSV missing headers {}", ", ".join(missing_headers)
                )
                return None

            for row in reader:
                try:
                    # Convert numeric fields
                    spanish = float(row["spanish"])
                    english = float(row["english"])
                    social = float(row["social_studies"])
                    science = float(row["science"])
                except (ValueError, KeyError) as parse_error:
                    print(
                        "An error occurred while reading a row. "
                        "Skipping this row due to invalid numeric values "
                        f"or missing columns: {parse_error}"
                    )
                    log_event(
                        "Skipped CSV row due to parse error: {}", parse_error
                    )
                    continue

                student: Student = {
                    "full_name": row.get("full_name", "").strip(),
                    "section": row.get("section", "").strip(),
                    "spanish": spanish,
                    "english": english,
                    "social_studies": social,
                    "science": science,
                }

                students.append(student)

        if not students:
            print(
                "CSV file was read, but no valid student records were found. "
                "Please verify the file contents."
            )
            log_event("Import finished: no valid student records found.")
            return None

        print(
            f"Students were imported successfully from '{CSV_FILE_NAME}'. "
            f"Total students loaded: {len(students)}"
        )
        log_event(
            "Imported {} students from CSV file '{}'", len(students), CSV_FILE_NAME
        )
        return students

    except OSError as error:
        print(f"An error occurred while importing data from CSV: {error}")
        log_event("Error importing students from CSV: {}", error)
        return None