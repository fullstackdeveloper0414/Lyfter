"""
Personal Finance Manager
Business logic and data models.

Expected outcome:
- Categories and movements are represented by reusable classes.
- Finance rules remain separate from the graphical interface.
- Validation, totals, filtering, editing, deletion, and CSV export
  are handled consistently.
"""

from __future__ import annotations

import csv
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from uuid import uuid4


# ---------------------------------------------------------------------
# Section 1 – Constants
# ---------------------------------------------------------------------
# Expected outcome:
# Shared application values are defined once and reused consistently.
# ---------------------------------------------------------------------

INCOME_TYPE = "Income"
EXPENSE_TYPE = "Expense"
DATE_FORMAT = "%m/%d/%Y"

DEFAULT_CATEGORY_COLOR = "#DCEAF7"
DEFAULT_SETTINGS = {
    "last_category": "",
}


# ---------------------------------------------------------------------
# Section 2 – Data Models
# ---------------------------------------------------------------------
# Expected outcome:
# Category and Movement objects store application data in a structured,
# testable, JSON-compatible format.
# ---------------------------------------------------------------------


@dataclass
class Category:
    """Represent one financial category and its display color."""

    name: str
    color: str

    def to_dict(self) -> dict:
        """Return a JSON-compatible representation of the category."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Category":
        """Build a Category object from saved JSON data."""
        return cls(
            name=str(data["name"]),
            color=str(data.get("color", DEFAULT_CATEGORY_COLOR)),
        )


@dataclass
class Movement:
    """
    Represent one financial transaction.

    Expected outcome:
    Income amounts are positive and expense amounts are negative.
    Each movement has a persistent unique identifier.
    """

    title: str
    amount: float
    category: str
    movement_type: str
    movement_date: str
    movement_id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        """Return a JSON-compatible representation of the movement."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Movement":
        """
        Build a Movement object from saved JSON data.

        Expected outcome:
        Older JSON files without movement_id remain compatible.
        """
        return cls(
            title=str(data["title"]),
            amount=float(data["amount"]),
            category=str(data["category"]),
            movement_type=str(data["movement_type"]),
            movement_date=str(data["movement_date"]),
            movement_id=str(data.get("movement_id", uuid4())),
        )


@dataclass
class TableRowStyle:
    """
    Describe a transaction row style without using tuple-based state.

    Expected outcome:
    The interface can use named properties for row position, text color,
    background color, and category accent color.
    """

    row_index: int
    text_color: str
    background_color: str
    category_color: str

    def to_table_value(self) -> tuple[int, str, str]:
        """
        Convert to the tuple required only by FreeSimpleGUI's Table API.
        """
        return (
            self.row_index,
            self.text_color,
            self.background_color,
        )


# ---------------------------------------------------------------------
# Section 3 – Finance Manager
# ---------------------------------------------------------------------
# Expected outcome:
# The FinanceManager centralizes all finance rules and protects the
# interface from validation and storage details.
# ---------------------------------------------------------------------


class FinanceManager:
    """Manage categories, movements, settings, totals, filters, and CSV."""

    def __init__(
        self,
        categories: list[Category] | None = None,
        movements: list[Movement] | None = None,
        settings: dict | None = None,
    ) -> None:
        """Initialize finance data with saved values or safe defaults."""
        self.categories = categories if categories is not None else []
        self.movements = movements if movements is not None else []
        self.settings = {**DEFAULT_SETTINGS, **(settings or {})}

    # -----------------------------------------------------------------
    # Section 3.1 – Category Operations
    # -----------------------------------------------------------------

    def add_category(self, name: str, color: str) -> Category:
        """
        Validate and add a category.

        Expected outcome:
        A new category is added only when its name and color are valid.
        """
        cleaned_name = name.strip()
        cleaned_color = color.strip().upper()

        self._validate_category_name(cleaned_name)
        self._validate_color(cleaned_color)

        if self._find_category(cleaned_name) is not None:
            raise ValueError(f'The category "{cleaned_name}" already exists.')

        category = Category(name=cleaned_name, color=cleaned_color)
        self.categories.append(category)
        return category

    def update_category(
        self,
        current_name: str,
        new_name: str,
        new_color: str,
    ) -> Category:
        """
        Rename a category and/or update its color.

        Expected outcome:
        All movements using the old category name are updated safely.
        """
        category = self._find_category(current_name)

        if category is None:
            raise ValueError("The selected category no longer exists.")

        cleaned_name = new_name.strip()
        cleaned_color = new_color.strip().upper()

        self._validate_category_name(cleaned_name)
        self._validate_color(cleaned_color)

        existing_category = self._find_category(cleaned_name)
        if existing_category is not None and existing_category is not category:
            raise ValueError(f'The category "{cleaned_name}" already exists.')

        old_name = category.name
        category.name = cleaned_name
        category.color = cleaned_color

        for movement in self.movements:
            if movement.category == old_name:
                movement.category = cleaned_name

        if self.settings.get("last_category") == old_name:
            self.settings["last_category"] = cleaned_name

        return category

    def delete_category(self, name: str) -> None:
        """
        Delete an unused category.

        Expected outcome:
        Categories attached to movements cannot be deleted accidentally.
        """
        category = self._find_category(name)

        if category is None:
            raise ValueError("The selected category no longer exists.")

        usage_count = self.get_category_usage_count(category.name)
        if usage_count > 0:
            raise ValueError(
                f'"{category.name}" cannot be deleted because it is used by '
                f"{usage_count} movement(s)."
            )

        self.categories.remove(category)

        if self.settings.get("last_category") == category.name:
            self.settings["last_category"] = ""

    def get_category_names(self) -> list[str]:
        """Return category names in alphabetical order."""
        return sorted(category.name for category in self.categories)

    def get_category_color(self, category_name: str) -> str:
        """
        Return a category color.

        Expected outcome:
        The interface always receives a safe fallback color.
        """
        category = self._find_category(category_name)
        return category.color if category is not None else DEFAULT_CATEGORY_COLOR

    def get_category_usage_count(self, category_name: str) -> int:
        """Return the number of movements linked to a category."""
        return sum(
            movement.category == category_name
            for movement in self.movements
        )

    def get_recent_categories(self, limit: int = 5) -> list[Category]:
        """
        Return recently created categories.

        Expected outcome:
        The category form can display recent additions to the user.
        """
        return list(reversed(self.categories[-limit:]))

    def _find_category(self, category_name: str) -> Category | None:
        """Find a category without exposing search logic to the interface."""
        normalized_name = category_name.strip().lower()

        for category in self.categories:
            if category.name.lower() == normalized_name:
                return category

        return None

    @staticmethod
    def _validate_category_name(name: str) -> None:
        """Validate a category name."""
        if not name:
            raise ValueError("Category name is required.")

        if len(name) > 30:
            raise ValueError("Category name must be 30 characters or fewer.")

    @staticmethod
    def _validate_color(color: str) -> None:
        """Validate a #RRGGBB hexadecimal color."""
        valid_characters = "0123456789ABCDEF"

        if (
            len(color) != 7
            or not color.startswith("#")
            or any(character not in valid_characters for character in color[1:])
        ):
            raise ValueError(
                "Category color must use #RRGGBB format, such as #FFA500."
            )

    # -----------------------------------------------------------------
    # Section 3.2 – Movement Operations
    # -----------------------------------------------------------------

    def add_movement(
        self,
        title: str,
        amount_text: str,
        category: str,
        movement_type: str,
        movement_date: str,
    ) -> Movement:
        """
        Validate and add an income or expense movement.

        Expected outcome:
        A valid movement is stored using a positive income amount or
        a negative expense amount.
        """
        validated_data = self._validate_movement_data(
            title=title,
            amount_text=amount_text,
            category=category,
            movement_type=movement_type,
            movement_date=movement_date,
        )

        movement = Movement(**validated_data)
        self.movements.append(movement)
        self.settings["last_category"] = movement.category

        return movement

    def update_movement(
        self,
        movement_id: str,
        title: str,
        amount_text: str,
        category: str,
        movement_type: str,
        movement_date: str,
    ) -> Movement:
        """
        Update an existing movement.

        Expected outcome:
        The same movement ID remains intact while its values are changed.
        """
        movement = self.get_movement_by_id(movement_id)

        if movement is None:
            raise ValueError("The selected movement no longer exists.")

        validated_data = self._validate_movement_data(
            title=title,
            amount_text=amount_text,
            category=category,
            movement_type=movement_type,
            movement_date=movement_date,
        )

        movement.title = validated_data["title"]
        movement.amount = validated_data["amount"]
        movement.category = validated_data["category"]
        movement.movement_type = validated_data["movement_type"]
        movement.movement_date = validated_data["movement_date"]

        self.settings["last_category"] = movement.category

        return movement

    def delete_movement(self, movement_id: str) -> Movement:
        """
        Delete a movement by its unique ID.

        Expected outcome:
        Only the selected movement is removed.
        """
        movement = self.get_movement_by_id(movement_id)

        if movement is None:
            raise ValueError("The selected movement no longer exists.")

        self.movements.remove(movement)
        return movement

    def get_movement_by_id(self, movement_id: str) -> Movement | None:
        """Return the movement matching a unique ID."""
        for movement in self.movements:
            if movement.movement_id == movement_id:
                return movement

        return None

    def _validate_movement_data(
        self,
        title: str,
        amount_text: str,
        category: str,
        movement_type: str,
        movement_date: str,
    ) -> dict:
        """
        Validate movement input and return standardized movement values.

        Expected outcome:
        Add and edit actions follow identical validation rules.
        """
        cleaned_title = title.strip()
        cleaned_category = category.strip()
        parsed_date = self._parse_date(movement_date.strip())
        amount = self._parse_amount(amount_text)

        if not cleaned_title:
            raise ValueError("Movement title is required.")

        if len(cleaned_title) > 50:
            raise ValueError("Movement title must be 50 characters or fewer.")

        if movement_type not in (INCOME_TYPE, EXPENSE_TYPE):
            raise ValueError("Movement type must be Income or Expense.")

        if self._find_category(cleaned_category) is None:
            raise ValueError("Choose a valid category before saving.")

        if parsed_date.date() > datetime.today().date():
            raise ValueError("Future dates are not allowed.")

        signed_amount = (
            abs(amount)
            if movement_type == INCOME_TYPE
            else -abs(amount)
        )

        return {
            "title": cleaned_title,
            "amount": signed_amount,
            "category": cleaned_category,
            "movement_type": movement_type,
            "movement_date": parsed_date.strftime(DATE_FORMAT),
        }

    @staticmethod
    def _parse_amount(amount_text: str) -> float:
        """Convert validated currency text into a positive number."""
        cleaned_amount = (
            amount_text.strip()
            .replace("$", "")
            .replace(",", "")
        )

        if not cleaned_amount:
            raise ValueError("Amount is required.")

        try:
            amount = float(cleaned_amount)
        except ValueError as error:
            raise ValueError(
                "Amount must be a valid number, such as 25.50."
            ) from error

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        return amount

    @staticmethod
    def _parse_date(date_text: str) -> datetime:
        """Validate and parse a date in MM/DD/YYYY format."""
        if not date_text:
            raise ValueError("Date is required.")

        try:
            return datetime.strptime(date_text, DATE_FORMAT)
        except ValueError as error:
            raise ValueError(
                "Date must use MM/DD/YYYY format, for example 08/16/2026."
            ) from error

    # -----------------------------------------------------------------
    # Section 3.3 – Totals and Filtering
    # -----------------------------------------------------------------

    def calculate_totals(
        self,
        movements: list[Movement] | None = None,
    ) -> dict[str, float]:
        """
        Calculate totals for all movements or a supplied filtered list.

        Expected outcome:
        Dashboard cards always match the visible movement table.
        """
        selected_movements = (
            movements
            if movements is not None
            else self.movements
        )

        total_income = sum(
            movement.amount
            for movement in selected_movements
            if movement.movement_type == INCOME_TYPE
        )

        total_expenses = abs(
            sum(
                movement.amount
                for movement in selected_movements
                if movement.movement_type == EXPENSE_TYPE
            )
        )

        return {
            "income": total_income,
            "expenses": total_expenses,
            "balance": total_income - total_expenses,
        }

    def filter_movements(
        self,
        start_date_text: str,
        end_date_text: str,
    ) -> list[Movement]:
        """
        Return movements within an optional inclusive date range.

        Expected outcome:
        Users can filter by start date, end date, both dates, or neither.
        """
        start_date = (
            self._parse_date(start_date_text.strip()).date()
            if start_date_text.strip()
            else None
        )

        end_date = (
            self._parse_date(end_date_text.strip()).date()
            if end_date_text.strip()
            else None
        )

        if start_date and end_date and start_date > end_date:
            raise ValueError("Start Date cannot be later than End Date.")

        filtered_movements = []

        for movement in self.movements:
            movement_date = self._parse_date(
                movement.movement_date
            ).date()

            if start_date and movement_date < start_date:
                continue

            if end_date and movement_date > end_date:
                continue

            filtered_movements.append(movement)

        return filtered_movements

    # -----------------------------------------------------------------
    # Section 3.4 – Preferences and Export
    # -----------------------------------------------------------------

    def get_settings(self) -> dict:
        """Return a copy of user settings for safe persistence."""
        return dict(self.settings)

    def export_to_csv(
        self,
        output_path: str | Path,
        movements: list[Movement] | None = None,
    ) -> None:
        """
        Export movements and totals to CSV.

        Expected outcome:
        The export contains the selected transaction rows and totals.
        """
        selected_movements = (
            movements
            if movements is not None
            else self.movements
        )

        totals = self.calculate_totals(selected_movements)
        path = Path(output_path)

        with path.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(
                [
                    "Date",
                    "Title",
                    "Amount (USD)",
                    "Category",
                    "Type",
                ]
            )

            for movement in selected_movements:
                writer.writerow(
                    [
                        movement.movement_date,
                        movement.title,
                        f"{movement.amount:.2f}",
                        movement.category,
                        movement.movement_type,
                    ]
                )

            writer.writerow([])
            writer.writerow(["Summary"])
            writer.writerow(["Total Income", f"{totals['income']:.2f}"])
            writer.writerow(["Total Expenses", f"{totals['expenses']:.2f}"])
            writer.writerow(["Net Balance", f"{totals['balance']:.2f}"])