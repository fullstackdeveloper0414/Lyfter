"""
Personal Finance Manager
JSON persistence and automatic backups.

Expected outcome:
- Categories, movements, and settings are loaded safely.
- Data saves automatically after changes and at application exit.
- Timestamped backups protect data before overwriting files.
- Empty or invalid JSON files do not crash the application.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from shutil import copy2

from logic import Category, Movement


# ---------------------------------------------------------------------
# Section 1 – Storage Locations
# ---------------------------------------------------------------------
# Expected outcome:
# All application data remains in a predictable project data directory.
# ---------------------------------------------------------------------

DATA_DIRECTORY = Path(__file__).parent / "data"
BACKUP_DIRECTORY = DATA_DIRECTORY / "backups"

CATEGORIES_FILE = DATA_DIRECTORY / "categories.json"
MOVEMENTS_FILE = DATA_DIRECTORY / "movements.json"
SETTINGS_FILE = DATA_DIRECTORY / "settings.json"


# ---------------------------------------------------------------------
# Section 2 – Directory and Backup Helpers
# ---------------------------------------------------------------------


def ensure_data_directories() -> None:
    """
    Create storage folders when they do not exist.

    Expected outcome:
    The application can run on a new computer without manual setup.
    """
    DATA_DIRECTORY.mkdir(exist_ok=True)
    BACKUP_DIRECTORY.mkdir(exist_ok=True)


def create_backup(file_path: Path) -> None:
    """
    Create a timestamped backup before overwriting an existing data file.

    Expected outcome:
    Previous saved records can be recovered if needed.
    """
    ensure_data_directories()

    if not file_path.exists() or file_path.stat().st_size == 0:
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    backup_path = BACKUP_DIRECTORY / (
        f"{file_path.stem}_{timestamp}{file_path.suffix}"
    )

    copy2(file_path, backup_path)


def _load_json_list(file_path: Path) -> list:
    """
    Load a JSON list safely.

    Expected outcome:
    Missing, blank, malformed, or wrong-shaped files return an empty list.
    """
    ensure_data_directories()

    if not file_path.exists() or file_path.stat().st_size == 0:
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            loaded_data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

    return loaded_data if isinstance(loaded_data, list) else []


def _load_json_dict(file_path: Path) -> dict:
    """
    Load a JSON dictionary safely.

    Expected outcome:
    Missing, blank, malformed, or wrong-shaped files return an empty dict.
    """
    ensure_data_directories()

    if not file_path.exists() or file_path.stat().st_size == 0:
        return {}

    try:
        with file_path.open("r", encoding="utf-8") as file:
            loaded_data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}

    return loaded_data if isinstance(loaded_data, dict) else {}


def _save_json(file_path: Path, data: list | dict) -> None:
    """
    Save JSON after backing up an existing file.

    Expected outcome:
    Data is readable, formatted, and protected by an automatic backup.
    """
    ensure_data_directories()
    create_backup(file_path)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4,
        )


# ---------------------------------------------------------------------
# Section 3 – Category Persistence
# ---------------------------------------------------------------------


def load_categories() -> list[Category]:
    """
    Load categories from JSON.

    Expected outcome:
    Valid saved records become Category objects; invalid records are skipped.
    """
    categories = []

    for item in _load_json_list(CATEGORIES_FILE):
        try:
            categories.append(Category.from_dict(item))
        except (KeyError, TypeError, ValueError):
            continue

    return categories


def save_categories(categories: list[Category]) -> None:
    """
    Save all categories.

    Expected outcome:
    Category names and colors persist between application sessions.
    """
    _save_json(
        CATEGORIES_FILE,
        [category.to_dict() for category in categories],
    )


# ---------------------------------------------------------------------
# Section 4 – Movement Persistence
# ---------------------------------------------------------------------


def load_movements() -> list[Movement]:
    """
    Load movements from JSON.

    Expected outcome:
    Older movement files without movement IDs remain usable.
    """
    movements = []

    for item in _load_json_list(MOVEMENTS_FILE):
        try:
            movements.append(Movement.from_dict(item))
        except (KeyError, TypeError, ValueError):
            continue

    return movements


def save_movements(movements: list[Movement]) -> None:
    """
    Save all movements.

    Expected outcome:
    Transactions persist with their unique movement IDs.
    """
    _save_json(
        MOVEMENTS_FILE,
        [movement.to_dict() for movement in movements],
    )


# ---------------------------------------------------------------------
# Section 5 – Settings Persistence
# ---------------------------------------------------------------------


def load_settings() -> dict:
    """
    Load interface preferences.

    Expected outcome:
    Preferences such as the last selected category are restored.
    """
    return _load_json_dict(SETTINGS_FILE)


def save_settings(settings: dict) -> None:
    """
    Save interface preferences.

    Expected outcome:
    Small user preferences persist separately from finance data.
    """
    _save_json(SETTINGS_FILE, settings)