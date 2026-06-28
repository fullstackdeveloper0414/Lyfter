Student Control System — Submission Notes
Student: Jaime C Smith
Date: June 25, 2026 
Course: Python Programming — Instituto de Estudios Generales de Lyfter 


This is my implementation of the Student Control System. This project has been fully developed in English to meet your requirements, ensuring clean code, descriptive naming conventions, and a strict separation of concerns across dynamic modules. 

The system architecture has been divided cleanly into the requested modules: 
•	main.py: The lightweight, dedicated entry point of the application. 
•	menu.py: Controls the command-line interface, navigation inputs, and user assistance (Help) text. 
•	actions.py: Houses all administrative and operational logic, including student record creations, grade validations, rankings, and structural deletions. 
•	data.py: Manages safe file I/O operations, ensuring data persistence via structured CSV exports and imports. 

Highlights of Additional Work & Enhancements Included
To demonstrate a comprehensive understanding of software design, I went beyond the core baseline project requirements to deliver an enterprise-grade solution by fully implementing all optional milestones and introducing advanced architectural improvements: 

1. Full Extra Credit Feature Implementation
•	Student Deletion (Option 7): Implemented a secure delete student workflow that prompts for a student's full name and section, verifies their existence in memory, displays their profile, and requires an explicit confirmation step before removing any data. 
•	Failing Students Report (Option 8): Created an advanced filtering utility (show_failing_students) that scans all active records and flags any student with at least one individual subject grade below $60.0$ (PASSING_GRADE), listing their section and their specific failing marks cleanly. 
•	Advanced Target Input Validation: Developed independent helper functions (_is_valid_name, _is_valid_section, and student_exists) to guarantee that names cannot contain numbers or be left empty, sections strictly follow alphanumeric configurations (e.g., 10A, 11B), and matching duplicate entries for the same student name and section are barred from entering the application. 

2. Advanced Software Architecture & Design Principles
•	Centralized Configuration Engine (config.py): I isolated application constants—such as the target CSV file name, the global passing grade threshold, and the core subjects’ array—into a single configuration file. This completely removes hardcoded "magic strings," allowing the entire system to scale dynamically if new academic subjects are added or the grading scale shifts in the future. 
•	Persistent System Auditing (logger.py): Designed a background logging utility (log_event) that tracks system events, successful exports, data-merges, skipped corrupt rows, and errors with precise ISO timestamps to a local students_system.log file without interrupting the user-facing CLI experience. 
•	UX Safety Layer (Unsaved Changes Warning): The menu actively monitors state changes through a students_changed Boolean flag. If a user tries to exit the application while holding unexported data in volatile memory, the system safely intercepts the command, warns them, and offers an immediate opportunity to save their work to disk. 
•	Smart CSV Data Sync Options: When importing records from an existing CSV file while current records live in memory, the application intelligently presents a sub-menu allowing the user to either entirely overwrite current memory or smoothly append the incoming file data while automatically filtering out overlapping duplicates. 

Thank you for your valuable guidance throughout this program. I look forward to your constructive feedback on this architecture!

Best regards,
Jaime C Smith
