"""
Student Control System
Jaime C Smith
06/25/2026
"""

# ============================
# logger.py
# ============================
"""
Logger module.

This module centralizes basic logging utilities so that all modules can
record important events and errors to a single log file. Logging is used
for debugging and monitoring, while all user interaction remains on the
command line via input and print.
"""

import datetime
from typing import Any

LOG_FILE_NAME = "students_system.log"


def log_event(message: str, *args: Any) -> None:
    """
    Append a timestamped log message to the log file.

    Args:
        message: Log message format string.
        *args: Optional values to format into the message.

    This helper is used to record important events and errors without
    changing the user-facing behavior of the program.
    """
    timestamp = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
    formatted = message.format(*args)
    line = f"[{timestamp}] {formatted}\n"

    try:
        with open(LOG_FILE_NAME, mode="a", encoding="utf-8") as log_file:
            log_file.write(line)
    except OSError:
        # Logging failures are ignored so they never crash the program.
        pass
