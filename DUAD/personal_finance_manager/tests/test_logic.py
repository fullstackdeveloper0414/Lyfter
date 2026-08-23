"""
Personal Finance Manager
Unit tests for business logic and presentation helpers.

Expected outcome:
- Tests execute without opening the graphical application.
- Category, movement, filter, totals, settings, styling, and CSV behavior
  remain stable as the application evolves.

Run from the project root:
python -m unittest discover -s tests -v
"""

from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from interface import (
    DANGER_COLOR,
    EXPENSE_ROW_BACKGROUND,
    INCOME_ROW_BACKGROUND,
    SUCCESS_COLOR,
    format_currency,
    movement_row_styles,
    movement_rows,
    table_row_colors,
    transaction_count_message,
)
from logic import (
    DATE_FORMAT,
    EXPENSE_TYPE,
    INCOME_TYPE,
    Category,
    FinanceManager,
    Movement,
)


class TestFinanceManager(unittest.TestCase):
    """
    Test the FinanceManager independently from GUI windows.

    Expected outcome:
    Business rules are verified using predictable sample data.
    """

    def setUp(self) -> None:
        """Create a fresh manager with two valid categories."""
        self.manager = FinanceManager()
        self.manager.add_category("Food", "#F59E0B")
        self.manager.add_category("Work", "#10B981")

    # -----------------------------------------------------------------
    # Category Tests
    # -----------------------------------------------------------------

    def test_add_category_returns_category(self) -> None:
        """Adding a category returns the saved Category object."""
        category = self.manager.add_category("Transport", "#3B82F6")

        self.assertEqual(category.name, "Transport")
        self.assertEqual(category.color, "#3B82F6")
        self.assertIn("Transport", self.manager.get_category_names())

    def test_add_category_rejects_duplicate_name(self) -> None:
        """Duplicate category names are rejected regardless of capitalization."""
        with self.assertRaises(ValueError):
            self.manager.add_category("food", "#FFFFFF")

    def test_add_category_rejects_invalid_color(self) -> None:
        """Category colors must use hexadecimal #RRGGBB format."""
        with self.assertRaises(ValueError):
            self.manager.add_category("Travel", "orange")

    def test_update_category_renames_linked_movements(self) -> None:
        """Renaming a category updates movements that use the old name."""
        self.manager.add_movement(
            "Lunch",
            "20",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        updated_category = self.manager.update_category(
            "Food",
            "Dining",
            "#D97706",
        )

        self.assertEqual(updated_category.name, "Dining")
        self.assertEqual(updated_category.color, "#D97706")
        self.assertEqual(self.manager.movements[0].category, "Dining")

    def test_delete_category_rejects_category_in_use(self) -> None:
        """Categories linked to movements cannot be deleted."""
        self.manager.add_movement(
            "Lunch",
            "20",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        with self.assertRaises(ValueError):
            self.manager.delete_category("Food")

    def test_delete_unused_category(self) -> None:
        """Unused categories can be deleted safely."""
        self.manager.delete_category("Work")

        self.assertNotIn("Work", self.manager.get_category_names())

    def test_category_usage_count(self) -> None:
        """Usage count reports the number of linked movements."""
        self.manager.add_movement(
            "Lunch",
            "20",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        self.assertEqual(self.manager.get_category_usage_count("Food"), 1)
        self.assertEqual(self.manager.get_category_usage_count("Work"), 0)

    # -----------------------------------------------------------------
    # Movement Tests
    # -----------------------------------------------------------------

    def test_add_income_stores_positive_amount_and_id(self) -> None:
        """Income movements are positive and receive an ID."""
        movement = self.manager.add_movement(
            "Salary",
            "1500",
            "Work",
            INCOME_TYPE,
            "07/01/2025",
        )

        self.assertEqual(movement.amount, 1500.0)
        self.assertEqual(movement.movement_type, INCOME_TYPE)
        self.assertTrue(movement.movement_id)

    def test_add_expense_stores_negative_amount(self) -> None:
        """Expense movements are stored as negative values."""
        movement = self.manager.add_movement(
            "Lunch",
            "25.50",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        self.assertEqual(movement.amount, -25.50)

    def test_add_movement_accepts_currency_and_commas(self) -> None:
        """Amounts with a dollar sign and commas are accepted."""
        movement = self.manager.add_movement(
            "Bonus",
            "$1,250.75",
            "Work",
            INCOME_TYPE,
            "07/03/2025",
        )

        self.assertEqual(movement.amount, 1250.75)

    def test_add_movement_rejects_blank_title(self) -> None:
        """Blank movement titles are rejected."""
        with self.assertRaises(ValueError):
            self.manager.add_movement(
                "",
                "25",
                "Food",
                EXPENSE_TYPE,
                "07/02/2025",
            )

    def test_add_movement_rejects_unknown_category(self) -> None:
        """Movements must use an existing category."""
        with self.assertRaises(ValueError):
            self.manager.add_movement(
                "Lunch",
                "25",
                "Unknown",
                EXPENSE_TYPE,
                "07/02/2025",
            )

    def test_add_movement_rejects_zero_amount(self) -> None:
        """Zero is not a valid transaction amount."""
        with self.assertRaises(ValueError):
            self.manager.add_movement(
                "Invalid",
                "0",
                "Food",
                EXPENSE_TYPE,
                "07/02/2025",
            )

    def test_add_movement_rejects_invalid_date_format(self) -> None:
        """Invalid MM/DD/YYYY dates are rejected."""
        with self.assertRaises(ValueError):
            self.manager.add_movement(
                "Wrong Date",
                "25",
                "Food",
                EXPENSE_TYPE,
                "31/07/2025",
            )

    def test_update_movement_keeps_same_id(self) -> None:
        """Editing a movement preserves its unique movement ID."""
        movement = self.manager.add_movement(
            "Lunch",
            "20",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        updated_movement = self.manager.update_movement(
            movement.movement_id,
            "Dinner",
            "35",
            "Food",
            EXPENSE_TYPE,
            "07/03/2025",
        )

        self.assertEqual(updated_movement.movement_id, movement.movement_id)
        self.assertEqual(updated_movement.title, "Dinner")
        self.assertEqual(updated_movement.amount, -35.0)
        self.assertEqual(updated_movement.movement_date, "07/03/2025")

    def test_delete_movement_removes_only_selected_id(self) -> None:
        """Deleting a movement removes only the matching transaction."""
        first_movement = self.manager.add_movement(
            "Lunch",
            "20",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )
        second_movement = self.manager.add_movement(
            "Salary",
            "1500",
            "Work",
            INCOME_TYPE,
            "07/03/2025",
        )

        self.manager.delete_movement(first_movement.movement_id)

        self.assertEqual(len(self.manager.movements), 1)
        self.assertEqual(
            self.manager.movements[0].movement_id,
            second_movement.movement_id,
        )

    # -----------------------------------------------------------------
    # Totals and Filter Tests
    # -----------------------------------------------------------------

    def test_date_format_is_mm_dd_yyyy(self) -> None:
        """The project date constant uses MM/DD/YYYY."""
        self.assertEqual(DATE_FORMAT, "%m/%d/%Y")

    def test_calculate_totals_for_all_movements(self) -> None:
        """Totals calculate income, expenses, and balance correctly."""
        self.manager.add_movement(
            "Salary",
            "1000",
            "Work",
            INCOME_TYPE,
            "07/01/2025",
        )
        self.manager.add_movement(
            "Lunch",
            "100",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        totals = self.manager.calculate_totals()

        self.assertEqual(totals["income"], 1000.0)
        self.assertEqual(totals["expenses"], 100.0)
        self.assertEqual(totals["balance"], 900.0)

    def test_calculate_totals_for_filtered_list(self) -> None:
        """Totals can be calculated from only visible filtered movements."""
        income = self.manager.add_movement(
            "Salary",
            "1000",
            "Work",
            INCOME_TYPE,
            "07/01/2025",
        )
        self.manager.add_movement(
            "Lunch",
            "100",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        totals = self.manager.calculate_totals([income])

        self.assertEqual(totals["income"], 1000.0)
        self.assertEqual(totals["expenses"], 0.0)
        self.assertEqual(totals["balance"], 1000.0)

    def test_filter_movements_returns_matching_dates(self) -> None:
        """Filtering returns movements inside the inclusive date range."""
        self.manager.add_movement(
            "Salary",
            "1000",
            "Work",
            INCOME_TYPE,
            "07/02/2025",
        )
        self.manager.add_movement(
            "Lunch",
            "20",
            "Food",
            EXPENSE_TYPE,
            "07/03/2025",
        )
        self.manager.add_movement(
            "Clothes",
            "50",
            "Food",
            EXPENSE_TYPE,
            "07/12/2025",
        )

        filtered_movements = self.manager.filter_movements(
            "07/01/2025",
            "07/10/2025",
        )

        self.assertEqual(
            [movement.title for movement in filtered_movements],
            ["Salary", "Lunch"],
        )

    def test_filter_rejects_reversed_range(self) -> None:
        """Start dates later than end dates are rejected."""
        with self.assertRaises(ValueError):
            self.manager.filter_movements(
                "07/10/2025",
                "07/01/2025",
            )

    # -----------------------------------------------------------------
    # Interface Helper Tests
    # -----------------------------------------------------------------

    def test_format_currency(self) -> None:
        """Currency formatting includes visible positive and negative signs."""
        self.assertEqual(format_currency(1250.5), "+$1,250.50")
        self.assertEqual(format_currency(-25.5), "-$25.50")

    def test_movement_rows(self) -> None:
        """Movement rows return readable GUI values."""
        self.manager.add_movement(
            "Lunch",
            "25.50",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        self.assertEqual(
            movement_rows(self.manager.movements),
            [
                [
                    "07/02/2025",
                    "Lunch",
                    "-$25.50",
                    "Food",
                    "Expense",
                ]
            ],
        )

    def test_movement_row_styles_use_income_colors(self) -> None:
        """Income movement styles use green text and a green background."""
        self.manager.add_movement(
            "Salary",
            "1000",
            "Work",
            INCOME_TYPE,
            "07/01/2025",
        )

        styles = movement_row_styles(
            self.manager,
            self.manager.movements,
        )

        self.assertEqual(styles[0].text_color, SUCCESS_COLOR)
        self.assertEqual(styles[0].background_color, INCOME_ROW_BACKGROUND)
        self.assertEqual(styles[0].category_color, "#10B981")

    def test_movement_row_styles_use_expense_colors(self) -> None:
        """Expense movement styles use red text and a red background."""
        self.manager.add_movement(
            "Lunch",
            "25",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        styles = movement_row_styles(
            self.manager,
            self.manager.movements,
        )

        self.assertEqual(styles[0].text_color, DANGER_COLOR)
        self.assertEqual(styles[0].background_color, EXPENSE_ROW_BACKGROUND)
        self.assertEqual(styles[0].category_color, "#F59E0B")

    def test_table_row_colors_convert_at_gui_boundary(self) -> None:
        """Named row styles convert only when required by the Table widget."""
        self.manager.add_movement(
            "Lunch",
            "25",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        styles = movement_row_styles(
            self.manager,
            self.manager.movements,
        )
        colors = table_row_colors(styles)

        self.assertEqual(
            colors,
            [(0, DANGER_COLOR, EXPENSE_ROW_BACKGROUND)],
        )

    def test_transaction_count_message(self) -> None:
        """Dashboard count messages describe empty, all, and filtered states."""
        self.assertEqual(
            transaction_count_message(0, 0),
            "No movements yet. Add income or an expense to begin.",
        )
        self.assertEqual(
            transaction_count_message(3, 3),
            "Showing all 3 movement(s).",
        )
        self.assertEqual(
            transaction_count_message(2, 5),
            "Showing 2 of 5 movement(s) matching the current filter.",
        )

    # -----------------------------------------------------------------
    # Serialization and CSV Tests
    # -----------------------------------------------------------------

    def test_movement_from_old_json_creates_id(self) -> None:
        """Older movement data without an ID remains compatible."""
        old_data = {
            "title": "Lunch",
            "amount": -25,
            "category": "Food",
            "movement_type": "Expense",
            "movement_date": "07/02/2025",
        }

        movement = Movement.from_dict(old_data)

        self.assertTrue(movement.movement_id)
        self.assertEqual(movement.title, "Lunch")

    def test_category_serialization(self) -> None:
        """Category JSON conversion preserves the name and color."""
        category = Category("Food", "#F59E0B")

        self.assertEqual(
            Category.from_dict(category.to_dict()),
            category,
        )

    def test_export_to_csv(self) -> None:
        """CSV export contains movement rows and summary totals."""
        self.manager.add_movement(
            "Salary",
            "1200",
            "Work",
            INCOME_TYPE,
            "07/01/2025",
        )
        self.manager.add_movement(
            "Lunch",
            "100",
            "Food",
            EXPENSE_TYPE,
            "07/02/2025",
        )

        with tempfile.TemporaryDirectory() as temporary_directory:
            output_path = Path(temporary_directory) / "finance_report.csv"

            self.manager.export_to_csv(output_path)

            with output_path.open(
                "r",
                encoding="utf-8",
                newline="",
            ) as file:
                rows = list(csv.reader(file))

        self.assertEqual(
            rows[0],
            ["Date", "Title", "Amount (USD)", "Category", "Type"],
        )
        self.assertIn(
            ["07/01/2025", "Salary", "1200.00", "Work", "Income"],
            rows,
        )
        self.assertIn(
            ["07/02/2025", "Lunch", "-100.00", "Food", "Expense"],
            rows,
        )
        self.assertIn(["Summary"], rows)
        self.assertIn(["Total Income", "1200.00"], rows)
        self.assertIn(["Total Expenses", "100.00"], rows)
        self.assertIn(["Net Balance", "1100.00"], rows)


if __name__ == "__main__":
    unittest.main(verbosity=2)