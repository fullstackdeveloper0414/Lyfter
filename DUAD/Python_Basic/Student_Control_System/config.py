"""
Student Control System
Jaime C Smith
06/25/2026
"""

# ============================
# config.py
# ============================
"""
Configuration module.

This module centralizes constants used across the Student Control System,
such as subject names, CSV file name, and passing grade threshold.
Keeping these values here avoids magic strings and numbers scattered in the code.
"""

# File name used for CSV export and import
CSV_FILE_NAME = "students_data.csv"

# Subject identifiers used consistently for student dictionaries and CSV headers
SUBJECTS = ["spanish", "english", "social_studies", "science"]

# Minimum passing grade for all subjects
PASSING_GRADE = 60.0