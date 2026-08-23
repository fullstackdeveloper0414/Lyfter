"""
Personal Finance Manager
FreeSimpleGUI presentation layer.

Expected outcome:
- A polished dashboard displays totals, filters, table data, and actions.
- Forms guide users with placeholders, inline feedback, and keyboard focus.
- Users can add, edit, delete, filter, export, and manage finance data.
- Help and About windows provide accessible in-app documentation.
- The presentation layer delegates finance rules to FinanceManager.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import FreeSimpleGUI as sg

from logic import (
    EXPENSE_TYPE,
    INCOME_TYPE,
    FinanceManager,
    Movement,
    TableRowStyle,
)
from persistence import (
    save_categories,
    save_movements,
    save_settings,
)


# ---------------------------------------------------------------------
# Section 1 – Visual Theme and Constants
# ---------------------------------------------------------------------
# Expected outcome:
# Colors, fonts, labels, and layout values remain consistent.
# ---------------------------------------------------------------------

PRIMARY_COLOR = "#173B5E"
SECONDARY_COLOR = "#2E75B6"
SUCCESS_COLOR = "#1F8A4C"
DANGER_COLOR = "#C0392B"
WARNING_COLOR = "#D97706"
NEUTRAL_COLOR = "#5F6B7A"

BACKGROUND_COLOR = "#F3F6FA"
CARD_BACKGROUND = "#FFFFFF"
TEXT_COLOR = "#1F2937"
MUTED_TEXT_COLOR = "#64748B"

INCOME_ROW_BACKGROUND = "#EAF7EF"
EXPENSE_ROW_BACKGROUND = "#FDEEEE"

FONT_FAMILY = "Segoe UI"
TABLE_HEADINGS = ["Date", "Title", "Amount (USD)", "Category", "Type"]

CATEGORY_SWATCHES = [
    {"name": "Food", "color": "#F59E0B"},
    {"name": "Transport", "color": "#3B82F6"},
    {"name": "Work", "color": "#10B981"},
    {"name": "Health", "color": "#EF4444"},
    {"name": "Entertainment", "color": "#8B5CF6"},
]


# ---------------------------------------------------------------------
# Section 2 – Formatting and Table Helpers
# ---------------------------------------------------------------------
# Expected outcome:
# GUI display transformations remain reusable and easy to test.
# ---------------------------------------------------------------------


def format_currency(amount: float) -> str:
    """Return positive or negative amounts in readable USD format."""
    if amount < 0:
        return f"-${abs(amount):,.2f}"

    return f"+${amount:,.2f}"


def movement_rows(movements: list[Movement]) -> list[list[str]]:
    """
    Convert Movement objects to table rows.

    Expected outcome:
    The dashboard table shows formatted, readable transaction values.
    """
    return [
        [
            movement.movement_date,
            movement.title,
            format_currency(movement.amount),
            movement.category,
            movement.movement_type,
        ]
        for movement in movements
    ]


def movement_row_styles(
    finance_manager: FinanceManager,
    movements: list[Movement],
) -> list[TableRowStyle]:
    """
    Build named row-style objects for visible movements.

    Expected outcome:
    Income rows are green, expense rows are red, and category colors are
    retained as named accent information rather than tuple-based state.
    """
    styles = []

    for row_index, movement in enumerate(movements):
        is_income = movement.movement_type == INCOME_TYPE

        styles.append(
            TableRowStyle(
                row_index=row_index,
                text_color=SUCCESS_COLOR if is_income else DANGER_COLOR,
                background_color=(
                    INCOME_ROW_BACKGROUND
                    if is_income
                    else EXPENSE_ROW_BACKGROUND
                ),
                category_color=finance_manager.get_category_color(
                    movement.category
                ),
            )
        )

    return styles


def table_row_colors(
    styles: list[TableRowStyle],
) -> list[tuple[int, str, str]]:
    """
    Convert named styles only at the FreeSimpleGUI Table boundary.

    Expected outcome:
    Tuple use is limited to the external GUI API requirement.
    """
    return [style.to_table_value() for style in styles]


def transaction_count_message(
    displayed_count: int,
    total_count: int,
) -> str:
    """Return a clear message describing the visible transaction count."""
    if total_count == 0:
        return "No movements yet. Add income or an expense to begin."

    if displayed_count == total_count:
        return f"Showing all {total_count} movement(s)."

    return (
        f"Showing {displayed_count} of {total_count} movement(s) "
        "matching the current filter."
    )


# ---------------------------------------------------------------------
# Section 3 – Reusable Visual Components
# ---------------------------------------------------------------------
# Expected outcome:
# Repeated dashboard elements have a unified professional appearance.
# ---------------------------------------------------------------------


def summary_card(
    title: str,
    value_key: str,
    detail_key: str,
    accent_color: str,
) -> sg.Frame:
    """Create a professional finance summary card."""
    layout = [
        [
            sg.Text(
                title,
                font=(FONT_FAMILY, 10, "bold"),
                text_color=MUTED_TEXT_COLOR,
                background_color=CARD_BACKGROUND,
            )
        ],
        [
            sg.Text(
                "$0.00",
                key=value_key,
                font=(FONT_FAMILY, 18, "bold"),
                text_color=accent_color,
                background_color=CARD_BACKGROUND,
            )
        ],
        [
            sg.Text(
                "All movements",
                key=detail_key,
                font=(FONT_FAMILY, 9),
                text_color=MUTED_TEXT_COLOR,
                background_color=CARD_BACKGROUND,
            )
        ],
    ]

    return sg.Frame(
        "",
        layout,
        background_color=CARD_BACKGROUND,
        border_width=1,
        relief="solid",
        expand_x=True,
        pad=(5, 5),
    )


def form_status_text(key: str) -> sg.Text:
    """Create a reusable two-line status message area for forms."""
    return sg.Text(
        "",
        key=key,
        size=(48, 2),
        text_color=PRIMARY_COLOR,
        background_color=BACKGROUND_COLOR,
        justification="left",
    )


# ---------------------------------------------------------------------
# Section 4 – Help and About Windows
# ---------------------------------------------------------------------
# Expected outcome:
# Users can access a clear guide and application details without leaving
# the dashboard or opening an external browser.
# ---------------------------------------------------------------------


def help_window() -> sg.Window:
    """
    Create a scrollable Help & User Guide window.

    Expected outcome:
    Users can quickly review primary features, workflows, date format,
    data storage behavior, filtering, export, and category management.
    """
    guide_text = """HELP & USER GUIDE

DASHBOARD OVERVIEW
• Total Income shows all visible income movements.
• Total Expenses shows all visible expense movements.
• Net Balance equals income minus expenses.
• When a date filter is active, the table and summary cards show totals
  only for the currently visible movements.
• Income rows appear green. Expense rows appear red.

ADDING INCOME AND EXPENSES
1. Select Add Income for money received, or Add Expense for money spent.
2. Enter a title, positive amount, category, and date.
3. Use the date format MM/DD/YYYY, for example 08/18/2026.
4. The application automatically stores expenses as negative values.
5. Select Today to fill the Date field with the current date.
6. Select Save & Add Another to record several movements without reopening
   the form.

MANAGING CATEGORIES
• Select Manage Categories before creating income or expense movements.
• Add a category name and choose a color using the color chooser or the
  suggested color buttons.
• Select an existing category to rename it or update its color.
• A category cannot be deleted while one or more movements use it.
• Category colors are saved with category data for future use.

EDITING OR DELETING MOVEMENTS
1. Select one movement in the Finance Movements table.
2. Select Edit Selected to revise the title, amount, category, type, or date.
3. Select Delete Selected to remove a movement permanently.
4. A confirmation message appears before a movement is deleted.

FILTERING MOVEMENTS
• Enter an optional Start Date and/or End Date.
• Select Apply Filter to display only movements within that range.
• Select Clear to return to the full movement list.
• Start Date cannot be later than End Date.

EXPORTING TO CSV
• Select Export CSV to export the movements currently displayed.
• If a filter is active, the CSV includes only the filtered movements.
• The CSV includes movement details, total income, total expenses,
  and net balance.

DATA AND BACKUPS
• Categories, movements, and preferences are saved automatically.
• Data is stored locally in the project's data folder as JSON files.
• A backup is created automatically before saved data is overwritten.
• Backups are stored in data/backups.

QUICK TIPS
• Amounts must be greater than zero when entered.
• Categories must exist before adding income or expenses.
• Use clear titles such as Grocery Store, Monthly Salary, or Gas Station.
• Select a row in the table before using Edit Selected or Delete Selected.
"""

    layout = [
        [
            sg.Text(
                "Help & User Guide",
                font=(FONT_FAMILY, 17, "bold"),
                text_color=PRIMARY_COLOR,
            )
        ],
        [
            sg.Text(
                "A quick reference for managing your personal finances.",
                font=(FONT_FAMILY, 10),
                text_color=MUTED_TEXT_COLOR,
            )
        ],
        [
            sg.Multiline(
                guide_text,
                size=(82, 30),
                disabled=True,
                autoscroll=False,
                reroute_cprint=False,
                font=(FONT_FAMILY, 10),
                text_color=TEXT_COLOR,
                background_color=CARD_BACKGROUND,
                border_width=1,
                expand_x=True,
                expand_y=True,
            )
        ],
        [
            sg.Push(),
            sg.Button(
                "Close",
                key="-CLOSE-HELP-",
                button_color=("white", NEUTRAL_COLOR),
                size=(10, 1),
            ),
        ],
    ]

    return sg.Window(
        "Help & User Guide",
        layout,
        modal=False,
        finalize=True,
        resizable=True,
        size=(720, 650),
        background_color=BACKGROUND_COLOR,
    )


def about_window() -> sg.Window:
    """
    Create an About window.

    Expected outcome:
    The user can view the application name, technology, local storage
    message, author, and release date.
    """
    about_text = (
        "Personal Finance Manager\n\n"
        "Built with Python and FreeSimpleGUI\n"
        "Data is stored locally in JSON files\n\n"
        "Jaime C Smith\n"
        "08/18/2026"
    )

    layout = [
        [
            sg.Text(
                "About",
                font=(FONT_FAMILY, 17, "bold"),
                text_color=PRIMARY_COLOR,
                justification="center",
                expand_x=True,
            )
        ],
        [
            sg.Text(
                about_text,
                font=(FONT_FAMILY, 11),
                text_color=TEXT_COLOR,
                justification="center",
                expand_x=True,
                pad=(20, 20),
            )
        ],
        [
            sg.Push(),
            sg.Button(
                "Close",
                key="-CLOSE-ABOUT-",
                button_color=("white", NEUTRAL_COLOR),
                size=(10, 1),
            ),
            sg.Push(),
        ],
    ]

    return sg.Window(
        "About Personal Finance Manager",
        layout,
        modal=True,
        finalize=True,
        size=(420, 280),
        background_color=BACKGROUND_COLOR,
    )


def show_help_window() -> None:
    """
    Display the Help & User Guide window.

    Expected outcome:
    The guide remains available while the user continues using the dashboard.
    """
    window = help_window()

    while True:
        event, _ = window.read()

        if event in (sg.WIN_CLOSED, "-CLOSE-HELP-"):
            break

    window.close()


def show_about_window() -> None:
    """
    Display the About window.

    Expected outcome:
    The user can close the concise About window safely.
    """
    window = about_window()

    while True:
        event, _ = window.read()

        if event in (sg.WIN_CLOSED, "-CLOSE-ABOUT-"):
            break

    window.close()


# ---------------------------------------------------------------------
# Section 5 – Main Dashboard Window
# ---------------------------------------------------------------------
# Expected outcome:
# The user sees a modern financial overview with fast access to actions.
# ---------------------------------------------------------------------


def create_main_window() -> sg.Window:
    """Create the main Personal Finance Manager dashboard."""
    today_label = date.today().strftime("%B %d, %Y")

    header_layout = [
        [
            sg.Text(
                "Personal Finance Manager",
                font=(FONT_FAMILY, 22, "bold"),
                text_color="white",
                background_color=PRIMARY_COLOR,
                expand_x=True,
            ),
            sg.Text(
                today_label,
                font=(FONT_FAMILY, 10),
                text_color="#DCEAF7",
                background_color=PRIMARY_COLOR,
                justification="right",
                pad=(0, 5),
            ),
            sg.Button(
                "Help",
                key="-HELP-",
                button_color=("white", SECONDARY_COLOR),
                size=(7, 1),
                tooltip="Open the Help & User Guide.",
                pad=(10, 5),
            ),
            sg.Button(
                "About",
                key="-ABOUT-",
                button_color=("white", NEUTRAL_COLOR),
                size=(7, 1),
                tooltip="View application information.",
                pad=(5, 5),
            ),
        ],
        [
            sg.Text(
                "Track your income, expenses, categories, and balance.",
                font=(FONT_FAMILY, 10),
                text_color="#DCEAF7",
                background_color=PRIMARY_COLOR,
                expand_x=True,
                pad=(0, 0),
            )
        ],
    ]

    filter_layout = [
        [
            sg.Text("Start Date", size=(10, 1)),
            sg.Input(
                key="-START-DATE-",
                size=(12, 1),
                tooltip="Use MM/DD/YYYY. Leave blank for no start date.",
            ),
            sg.Text("End Date", size=(9, 1)),
            sg.Input(
                key="-END-DATE-",
                size=(12, 1),
                tooltip="Use MM/DD/YYYY. Leave blank for no end date.",
            ),
            sg.Button(
                "Apply Filter",
                key="-APPLY-FILTER-",
                button_color=("white", SECONDARY_COLOR),
                size=(12, 1),
            ),
            sg.Button(
                "Clear",
                key="-CLEAR-FILTER-",
                button_color=("white", NEUTRAL_COLOR),
                size=(8, 1),
            ),
        ]
    ]

    action_layout = [
        [
            sg.Button(
                "Add Income",
                key="-ADD-INCOME-",
                button_color=("white", SUCCESS_COLOR),
                size=(15, 1),
                tooltip="Record money received.",
            ),
            sg.Button(
                "Add Expense",
                key="-ADD-EXPENSE-",
                button_color=("white", DANGER_COLOR),
                size=(15, 1),
                tooltip="Record money spent.",
            ),
            sg.Button(
                "Manage Categories",
                key="-MANAGE-CATEGORIES-",
                button_color=("white", WARNING_COLOR),
                size=(18, 1),
                tooltip="Add, rename, recolor, or delete categories.",
            ),
            sg.Button(
                "Edit Selected",
                key="-EDIT-MOVEMENT-",
                button_color=("white", SECONDARY_COLOR),
                size=(14, 1),
                tooltip="Edit the selected movement.",
            ),
            sg.Button(
                "Delete Selected",
                key="-DELETE-MOVEMENT-",
                button_color=("white", NEUTRAL_COLOR),
                size=(15, 1),
                tooltip="Delete the selected movement.",
            ),
            sg.Button(
                "Export CSV",
                key="-EXPORT-CSV-",
                button_color=("white", PRIMARY_COLOR),
                size=(12, 1),
            ),
            sg.Button(
                "Exit",
                key="-EXIT-",
                button_color=("white", NEUTRAL_COLOR),
                size=(8, 1),
            ),
        ]
    ]

    table_layout = [
        [
            sg.Text(
                "No movements yet. Add income or an expense to begin.",
                key="-MOVEMENT-COUNT-",
                font=(FONT_FAMILY, 10),
                text_color=MUTED_TEXT_COLOR,
                background_color=BACKGROUND_COLOR,
                expand_x=True,
            )
        ],
        [
            sg.Table(
                values=[],
                headings=TABLE_HEADINGS,
                key="-MOVEMENTS-TABLE-",
                auto_size_columns=False,
                col_widths=[12, 28, 16, 18, 12],
                justification="left",
                num_rows=15,
                expand_x=True,
                expand_y=True,
                enable_events=True,
                select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                header_background_color=PRIMARY_COLOR,
                header_text_color="white",
                selected_row_colors=("white", SECONDARY_COLOR),
                row_colors=[],
            )
        ],
        [
            sg.Text(
                "Select a movement to edit or delete it.",
                key="-SELECTION-HINT-",
                font=(FONT_FAMILY, 9, "italic"),
                text_color=MUTED_TEXT_COLOR,
                background_color=BACKGROUND_COLOR,
            )
        ],
    ]

    layout = [
        [
            sg.Frame(
                "",
                header_layout,
                background_color=PRIMARY_COLOR,
                border_width=0,
                expand_x=True,
                pad=(0, 0),
            )
        ],
        [
            sg.Frame(
                "Date Range",
                filter_layout,
                background_color=BACKGROUND_COLOR,
                title_color=PRIMARY_COLOR,
                expand_x=True,
                pad=(10, 8),
            )
        ],
        [
            summary_card(
                "TOTAL INCOME",
                "-INCOME-",
                "-INCOME-DETAIL-",
                SUCCESS_COLOR,
            ),
            summary_card(
                "TOTAL EXPENSES",
                "-EXPENSES-",
                "-EXPENSES-DETAIL-",
                DANGER_COLOR,
            ),
            summary_card(
                "NET BALANCE",
                "-BALANCE-",
                "-BALANCE-DETAIL-",
                PRIMARY_COLOR,
            ),
        ],
        [
            sg.Frame(
                "Finance Movements",
                table_layout,
                background_color=BACKGROUND_COLOR,
                title_color=PRIMARY_COLOR,
                expand_x=True,
                expand_y=True,
                pad=(10, 5),
            )
        ],
        [
            sg.Frame(
                "Actions",
                action_layout,
                background_color=BACKGROUND_COLOR,
                title_color=PRIMARY_COLOR,
                expand_x=True,
                pad=(10, 5),
            )
        ],
        [
            sg.Text(
                "Ready.",
                key="-STATUS-",
                size=(110, 1),
                font=(FONT_FAMILY, 10),
                text_color=PRIMARY_COLOR,
                background_color="#DCEAF7",
                pad=(10, 8),
            )
        ],
    ]

    return sg.Window(
        "Personal Finance Manager",
        layout,
        resizable=True,
        finalize=True,
        size=(1080, 720),
        background_color=BACKGROUND_COLOR,
    )


# ---------------------------------------------------------------------
# Section 6 – Movement Form Windows
# ---------------------------------------------------------------------
# Expected outcome:
# Add/edit forms provide clear guidance and efficient repeated entry.
# ---------------------------------------------------------------------


def movement_form_window(
    category_names: list[str],
    movement_type: str,
    movement: Movement | None = None,
    default_category: str = "",
) -> sg.Window:
    """
    Create an Add or Edit Income/Expense dialog.

    Expected outcome:
    The form supports save, save-and-add-another, inline feedback,
    placeholders, and an optional prefilled movement.
    """
    is_editing = movement is not None
    action_color = (
        SUCCESS_COLOR
        if movement_type == INCOME_TYPE
        else DANGER_COLOR
    )

    default_date = (
        movement.movement_date
        if movement is not None
        else date.today().strftime("%m/%d/%Y")
    )

    selected_category = (
        movement.category
        if movement is not None
        else default_category
    )

    title_text = "Edit Movement" if is_editing else f"Add {movement_type}"
    save_text = "Save Changes" if is_editing else f"Save {movement_type}"

    layout = [
        [
            sg.Text(
                title_text,
                font=(FONT_FAMILY, 16, "bold"),
                text_color=action_color,
            )
        ],
        [
            sg.Text(
                "Enter the required information below.",
                font=(FONT_FAMILY, 9),
                text_color=MUTED_TEXT_COLOR,
            )
        ],
        [
            sg.Text("Title *", size=(14, 1)),
            sg.Input(
                movement.title if movement else "",
                key="-TITLE-",
                size=(30, 1),
                tooltip="Example: Grocery Store, Monthly Salary.",
            ),
        ],
        [
            sg.Text("Amount (USD) *", size=(14, 1)),
            sg.Input(
                f"{abs(movement.amount):.2f}" if movement else "",
                key="-AMOUNT-",
                size=(30, 1),
                tooltip="Enter a positive amount, such as 125.75.",
            ),
        ],
        [
            sg.Text("Category *", size=(14, 1)),
            sg.Combo(
                category_names,
                default_value=selected_category,
                key="-CATEGORY-",
                readonly=True,
                size=(28, 1),
                tooltip="Choose a saved category.",
            ),
        ],
        [
            sg.Text("Date *", size=(14, 1)),
            sg.Input(
                default_date,
                key="-DATE-",
                size=(18, 1),
                tooltip="Use MM/DD/YYYY. Future dates are not allowed.",
            ),
            sg.Button(
                "Today",
                key="-TODAY-",
                button_color=("white", SECONDARY_COLOR),
                size=(8, 1),
                tooltip="Fill the date with today's date.",
            ),
        ],
        [
            sg.Text(
                "* Required fields | Date format: MM/DD/YYYY",
                font=(FONT_FAMILY, 9, "italic"),
                text_color=MUTED_TEXT_COLOR,
            )
        ],
        [form_status_text("-FORM-STATUS-")],
        [
            sg.Button(
                save_text,
                key="-SAVE-",
                button_color=("white", action_color),
                size=(16, 1),
            ),
            sg.Button(
                "Save & Add Another",
                key="-SAVE-AND-NEW-",
                visible=not is_editing,
                button_color=("white", SECONDARY_COLOR),
                size=(18, 1),
            ),
            sg.Button(
                "Cancel",
                key="-CANCEL-",
                button_color=("white", NEUTRAL_COLOR),
                size=(10, 1),
            ),
        ],
    ]

    return sg.Window(
        title_text,
        layout,
        modal=True,
        finalize=True,
        background_color=BACKGROUND_COLOR,
    )


# ---------------------------------------------------------------------
# Section 7 – Category Management Window
# ---------------------------------------------------------------------
# Expected outcome:
# The user can create, select, edit, recolor, and safely delete categories.
# ---------------------------------------------------------------------


def category_management_window(
    finance_manager: FinanceManager,
) -> sg.Window:
    """Create the category management dialog."""
    recent_categories = finance_manager.get_recent_categories()

    recent_text = (
        "Recently added: "
        + ", ".join(category.name for category in recent_categories)
        if recent_categories
        else "No categories created yet."
    )

    swatch_buttons = [
        sg.Button(
            swatch["name"],
            key=f"-SWATCH-{swatch['color']}-",
            button_color=("white", swatch["color"]),
            size=(12, 1),
            tooltip=f"Use {swatch['color']} as the category color.",
        )
        for swatch in CATEGORY_SWATCHES
    ]

    layout = [
        [
            sg.Text(
                "Manage Categories",
                font=(FONT_FAMILY, 16, "bold"),
                text_color=PRIMARY_COLOR,
            )
        ],
        [
            sg.Text(
                "Create a category or select one below to edit it.",
                font=(FONT_FAMILY, 9),
                text_color=MUTED_TEXT_COLOR,
            )
        ],
        [
            sg.Listbox(
                values=finance_manager.get_category_names(),
                key="-CATEGORY-LIST-",
                size=(28, 8),
                enable_events=True,
            ),
            sg.Column(
                [
                    [
                        sg.Text("Category Name", size=(14, 1)),
                        sg.Input(
                            key="-CATEGORY-NAME-",
                            size=(28, 1),
                        ),
                    ],
                    [
                        sg.Text("Color", size=(14, 1)),
                        sg.Input(
                            "#FFFFFF",
                            key="-CATEGORY-COLOR-",
                            size=(12, 1),
                        ),
                        sg.ColorChooserButton(
                            "Choose Color",
                            target="-CATEGORY-COLOR-",
                            button_color=("white", WARNING_COLOR),
                        ),
                        sg.Text(
                            "     ",
                            key="-COLOR-PREVIEW-",
                            background_color="#FFFFFF",
                            relief="solid",
                            border_width=1,
                        ),
                    ],
                    [
                        sg.Text(
                            "Suggested colors",
                            font=(FONT_FAMILY, 9, "bold"),
                            text_color=MUTED_TEXT_COLOR,
                        )
                    ],
                    swatch_buttons,
                    [
                        sg.Text(
                            "Category usage: 0 movement(s)",
                            key="-CATEGORY-USAGE-",
                            text_color=MUTED_TEXT_COLOR,
                        )
                    ],
                ],
                background_color=BACKGROUND_COLOR,
                pad=(15, 0),
            ),
        ],
        [
            sg.Text(
                recent_text,
                key="-RECENT-CATEGORIES-",
                size=(68, 1),
                text_color=MUTED_TEXT_COLOR,
                background_color=BACKGROUND_COLOR,
            )
        ],
        [form_status_text("-CATEGORY-STATUS-")],
        [
            sg.Button(
                "Add Category",
                key="-ADD-CATEGORY-",
                button_color=("white", SUCCESS_COLOR),
                size=(15, 1),
            ),
            sg.Button(
                "Save Changes",
                key="-SAVE-CATEGORY-",
                button_color=("white", SECONDARY_COLOR),
                size=(15, 1),
            ),
            sg.Button(
                "Delete Category",
                key="-DELETE-CATEGORY-",
                button_color=("white", DANGER_COLOR),
                size=(16, 1),
            ),
            sg.Button(
                "Close",
                key="-CLOSE-CATEGORIES-",
                button_color=("white", NEUTRAL_COLOR),
                size=(10, 1),
            ),
        ],
    ]

    return sg.Window(
        "Manage Categories",
        layout,
        modal=True,
        finalize=True,
        background_color=BACKGROUND_COLOR,
    )


def refresh_category_window(
    window: sg.Window,
    finance_manager: FinanceManager,
) -> None:
    """
    Refresh category lists and recent-category information.

    Expected outcome:
    The category window immediately reflects every successful change.
    """
    recent_categories = finance_manager.get_recent_categories()

    recent_text = (
        "Recently added: "
        + ", ".join(category.name for category in recent_categories)
        if recent_categories
        else "No categories created yet."
    )

    window["-CATEGORY-LIST-"].update(
        values=finance_manager.get_category_names()
    )
    window["-RECENT-CATEGORIES-"].update(recent_text)


# ---------------------------------------------------------------------
# Section 8 – Dashboard Updates
# ---------------------------------------------------------------------
# Expected outcome:
# The dashboard table, totals, styles, count, and messages stay synchronized.
# ---------------------------------------------------------------------


def update_status(window: sg.Window, message: str) -> None:
    """Update the dashboard status bar."""
    window["-STATUS-"].update(message)


def update_dashboard(
    window: sg.Window,
    finance_manager: FinanceManager,
    displayed_movements: list[Movement] | None = None,
    filter_label: str = "All movements",
) -> None:
    """
    Refresh dashboard data based on currently displayed movements.

    Expected outcome:
    Table rows and summary cards always represent the same data.
    """
    visible_movements = (
        displayed_movements
        if displayed_movements is not None
        else finance_manager.movements
    )

    totals = finance_manager.calculate_totals(visible_movements)
    styles = movement_row_styles(finance_manager, visible_movements)

    window["-MOVEMENTS-TABLE-"].update(
        values=movement_rows(visible_movements),
        row_colors=table_row_colors(styles),
    )

    balance_color = (
        SUCCESS_COLOR
        if totals["balance"] >= 0
        else DANGER_COLOR
    )

    window["-INCOME-"].update(f"${totals['income']:,.2f}")
    window["-EXPENSES-"].update(f"${totals['expenses']:,.2f}")
    window["-BALANCE-"].update(
        f"${totals['balance']:,.2f}",
        text_color=balance_color,
    )

    window["-INCOME-DETAIL-"].update(filter_label)
    window["-EXPENSES-DETAIL-"].update(filter_label)
    window["-BALANCE-DETAIL-"].update(filter_label)

    window["-MOVEMENT-COUNT-"].update(
        transaction_count_message(
            len(visible_movements),
            len(finance_manager.movements),
        )
    )

    selection_message = (
        "Select a movement to edit or delete it."
        if visible_movements
        else "Your new income and expense records will appear here."
    )

    window["-SELECTION-HINT-"].update(selection_message)


# ---------------------------------------------------------------------
# Section 9 – Form Event Handlers
# ---------------------------------------------------------------------
# Expected outcome:
# Each form validates input, saves successful actions, and gives useful feedback.
# ---------------------------------------------------------------------


def handle_movement_form(
    finance_manager: FinanceManager,
    movement_type: str,
    movement: Movement | None = None,
) -> bool:
    """
    Open and process an add/edit movement form.

    Expected outcome:
    Users can save once, save repeatedly, edit a selected movement,
    or cancel without affecting saved data.
    """
    if not finance_manager.categories:
        sg.popup_error(
            "No categories are available.\n"
            "Use Manage Categories to add a category first."
        )
        return False

    window = movement_form_window(
        category_names=finance_manager.get_category_names(),
        movement_type=movement_type,
        movement=movement,
        default_category=finance_manager.settings.get("last_category", ""),
    )

    window["-TITLE-"].set_focus()
    changed = False

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "-CANCEL-"):
            window.close()
            return changed

        if event == "-TODAY-":
            window["-DATE-"].update(
                date.today().strftime("%m/%d/%Y")
            )
            window["-FORM-STATUS-"].update(
                "Today's date has been selected."
            )

        if event in ("-SAVE-", "-SAVE-AND-NEW-"):
            try:
                if movement is None:
                    saved_movement = finance_manager.add_movement(
                        title=values["-TITLE-"],
                        amount_text=values["-AMOUNT-"],
                        category=values["-CATEGORY-"],
                        movement_type=movement_type,
                        movement_date=values["-DATE-"],
                    )
                    success_message = (
                        f"{movement_type} saved: "
                        f"{format_currency(saved_movement.amount)}."
                    )
                else:
                    saved_movement = finance_manager.update_movement(
                        movement_id=movement.movement_id,
                        title=values["-TITLE-"],
                        amount_text=values["-AMOUNT-"],
                        category=values["-CATEGORY-"],
                        movement_type=movement_type,
                        movement_date=values["-DATE-"],
                    )
                    success_message = (
                        f'"{saved_movement.title}" was updated successfully.'
                    )

                save_movements(finance_manager.movements)
                save_settings(finance_manager.get_settings())
                changed = True

                window["-FORM-STATUS-"].update(success_message)

                if event == "-SAVE-AND-NEW-" and movement is None:
                    window["-TITLE-"].update("")
                    window["-AMOUNT-"].update("")
                    window["-DATE-"].update(
                        date.today().strftime("%m/%d/%Y")
                    )
                    window["-CATEGORY-"].update(
                        finance_manager.settings.get("last_category", "")
                    )
                    window["-TITLE-"].set_focus()
                    continue

                window.close()
                return changed

            except ValueError as error:
                window["-FORM-STATUS-"].update(
                    f"Please correct the form: {error}"
                )


def handle_category_management(
    finance_manager: FinanceManager,
) -> bool:
    """
    Open and process the category management window.

    Expected outcome:
    Categories can be added, edited, recolored, and safely deleted.
    """
    window = category_management_window(finance_manager)
    selected_category_name = ""
    changed = False

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "-CLOSE-CATEGORIES-"):
            window.close()
            return changed

        if event == "-CATEGORY-LIST-" and values["-CATEGORY-LIST-"]:
            selected_category_name = values["-CATEGORY-LIST-"][0]
            selected_category = next(
                category
                for category in finance_manager.categories
                if category.name == selected_category_name
            )

            window["-CATEGORY-NAME-"].update(selected_category.name)
            window["-CATEGORY-COLOR-"].update(selected_category.color)
            window["-COLOR-PREVIEW-"].update(
                background_color=selected_category.color
            )
            window["-CATEGORY-USAGE-"].update(
                f"Category usage: "
                f"{finance_manager.get_category_usage_count(selected_category.name)} "
                "movement(s)"
            )
            window["-CATEGORY-STATUS-"].update(
                f'"{selected_category.name}" selected.'
            )

        if event.startswith("-SWATCH-"):
            selected_color = event.replace("-SWATCH-", "").rstrip("-")
            window["-CATEGORY-COLOR-"].update(selected_color)
            window["-COLOR-PREVIEW-"].update(
                background_color=selected_color
            )

        if event == "-CATEGORY-COLOR-":
            entered_color = values["-CATEGORY-COLOR-"].strip().upper()
            if len(entered_color) == 7 and entered_color.startswith("#"):
                window["-COLOR-PREVIEW-"].update(
                    background_color=entered_color
                )

        if event == "-ADD-CATEGORY-":
            try:
                category = finance_manager.add_category(
                    values["-CATEGORY-NAME-"],
                    values["-CATEGORY-COLOR-"],
                )
                save_categories(finance_manager.categories)
                changed = True

                refresh_category_window(window, finance_manager)
                window["-CATEGORY-NAME-"].update("")
                window["-CATEGORY-COLOR-"].update("#FFFFFF")
                window["-COLOR-PREVIEW-"].update(
                    background_color="#FFFFFF"
                )
                window["-CATEGORY-USAGE-"].update(
                    "Category usage: 0 movement(s)"
                )
                window["-CATEGORY-STATUS-"].update(
                    f'"{category.name}" was added successfully.'
                )
                selected_category_name = ""

            except ValueError as error:
                window["-CATEGORY-STATUS-"].update(str(error))

        if event == "-SAVE-CATEGORY-":
            if not selected_category_name:
                window["-CATEGORY-STATUS-"].update(
                    "Select a category from the list before saving changes."
                )
                continue

            try:
                category = finance_manager.update_category(
                    current_name=selected_category_name,
                    new_name=values["-CATEGORY-NAME-"],
                    new_color=values["-CATEGORY-COLOR-"],
                )
                save_categories(finance_manager.categories)
                save_movements(finance_manager.movements)
                save_settings(finance_manager.get_settings())
                changed = True

                refresh_category_window(window, finance_manager)
                window["-CATEGORY-LIST-"].update(
                    set_to_index=finance_manager.get_category_names().index(
                        category.name
                    )
                )
                window["-CATEGORY-STATUS-"].update(
                    f'"{category.name}" was updated successfully.'
                )
                selected_category_name = category.name

            except ValueError as error:
                window["-CATEGORY-STATUS-"].update(str(error))

        if event == "-DELETE-CATEGORY-":
            if not selected_category_name:
                window["-CATEGORY-STATUS-"].update(
                    "Select a category from the list before deleting it."
                )
                continue

            confirmation = sg.popup_yes_no(
                f'Delete category "{selected_category_name}"?\n\n'
                "Categories connected to movements cannot be deleted.",
                title="Confirm Category Deletion",
            )

            if confirmation != "Yes":
                continue

            try:
                finance_manager.delete_category(selected_category_name)
                save_categories(finance_manager.categories)
                save_settings(finance_manager.get_settings())
                changed = True

                refresh_category_window(window, finance_manager)
                window["-CATEGORY-NAME-"].update("")
                window["-CATEGORY-COLOR-"].update("#FFFFFF")
                window["-COLOR-PREVIEW-"].update(
                    background_color="#FFFFFF"
                )
                window["-CATEGORY-USAGE-"].update(
                    "Category usage: 0 movement(s)"
                )
                window["-CATEGORY-STATUS-"].update(
                    f'"{selected_category_name}" was deleted.'
                )
                selected_category_name = ""

            except ValueError as error:
                window["-CATEGORY-STATUS-"].update(str(error))


# ---------------------------------------------------------------------
# Section 10 – CSV Export
# ---------------------------------------------------------------------
# Expected outcome:
# Users can export either all movements or the currently filtered list.
# ---------------------------------------------------------------------


def export_movements(
    finance_manager: FinanceManager,
    displayed_movements: list[Movement],
) -> bool:
    """Ask for a file location and export visible movements to CSV."""
    output_path = sg.popup_get_file(
        "Choose a CSV Export Location",
        save_as=True,
        default_extension=".csv",
        file_types=(("CSV Files", "*.csv"),),
        default_path=str(Path.cwd() / "finance_report.csv"),
        no_window=True,
    )

    if not output_path:
        return False

    finance_manager.export_to_csv(output_path, displayed_movements)
    sg.popup_ok(
        "CSV exported successfully.\n"
        f"Exported {len(displayed_movements)} movement(s)."
    )
    return True


# ---------------------------------------------------------------------
# Section 11 – Main Event Loop
# ---------------------------------------------------------------------
# Expected outcome:
# The application stays synchronized until the user exits.
# ---------------------------------------------------------------------


def run_application(finance_manager: FinanceManager) -> None:
    """Start the full Personal Finance Manager user interface."""
    sg.theme("LightBlue3")

    window = create_main_window()
    visible_movements = list(finance_manager.movements)
    active_filter_label = "All movements"

    update_dashboard(
        window,
        finance_manager,
        visible_movements,
        active_filter_label,
    )
    update_status(
        window,
        "Ready. Add income, add an expense, or manage categories.",
    )

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "-EXIT-"):
            break

        if event == "-HELP-":
            show_help_window()
            update_status(window, "Help & User Guide opened.")

        elif event == "-ABOUT-":
            show_about_window()
            update_status(window, "About information displayed.")

        elif event == "-ADD-INCOME-":
            if handle_movement_form(finance_manager, INCOME_TYPE):
                visible_movements = list(finance_manager.movements)
                active_filter_label = "All movements"
                update_dashboard(
                    window,
                    finance_manager,
                    visible_movements,
                    active_filter_label,
                )
                update_status(window, "Income saved successfully.")

        elif event == "-ADD-EXPENSE-":
            if handle_movement_form(finance_manager, EXPENSE_TYPE):
                visible_movements = list(finance_manager.movements)
                active_filter_label = "All movements"
                update_dashboard(
                    window,
                    finance_manager,
                    visible_movements,
                    active_filter_label,
                )
                update_status(window, "Expense saved successfully.")

        elif event == "-MANAGE-CATEGORIES-":
            if handle_category_management(finance_manager):
                save_categories(finance_manager.categories)
                save_movements(finance_manager.movements)
                save_settings(finance_manager.get_settings())
                update_dashboard(
                    window,
                    finance_manager,
                    visible_movements,
                    active_filter_label,
                )
                update_status(window, "Category changes saved successfully.")

        elif event == "-EDIT-MOVEMENT-":
            selected_rows = values["-MOVEMENTS-TABLE-"]

            if not selected_rows:
                update_status(
                    window,
                    "Select a movement in the table before editing it.",
                )
                continue

            selected_movement = visible_movements[selected_rows[0]]

            if handle_movement_form(
                finance_manager,
                selected_movement.movement_type,
                selected_movement,
            ):
                visible_movements = list(finance_manager.movements)
                active_filter_label = "All movements"
                update_dashboard(
                    window,
                    finance_manager,
                    visible_movements,
                    active_filter_label,
                )
                update_status(window, "Movement updated successfully.")

        elif event == "-DELETE-MOVEMENT-":
            selected_rows = values["-MOVEMENTS-TABLE-"]

            if not selected_rows:
                update_status(
                    window,
                    "Select a movement in the table before deleting it.",
                )
                continue

            selected_movement = visible_movements[selected_rows[0]]

            confirmation = sg.popup_yes_no(
                f"Delete this movement?\n\n"
                f"Date: {selected_movement.movement_date}\n"
                f"Title: {selected_movement.title}\n"
                f"Amount: {format_currency(selected_movement.amount)}",
                title="Confirm Movement Deletion",
            )

            if confirmation == "Yes":
                finance_manager.delete_movement(
                    selected_movement.movement_id
                )
                save_movements(finance_manager.movements)

                visible_movements = list(finance_manager.movements)
                active_filter_label = "All movements"
                update_dashboard(
                    window,
                    finance_manager,
                    visible_movements,
                    active_filter_label,
                )
                update_status(window, "Movement deleted successfully.")

        elif event == "-APPLY-FILTER-":
            try:
                visible_movements = finance_manager.filter_movements(
                    values["-START-DATE-"],
                    values["-END-DATE-"],
                )

                start_label = values["-START-DATE-"] or "Beginning"
                end_label = values["-END-DATE-"] or "Today"
                active_filter_label = f"{start_label} – {end_label}"

                update_dashboard(
                    window,
                    finance_manager,
                    visible_movements,
                    active_filter_label,
                )
                update_status(
                    window,
                    f"Filter applied: {len(visible_movements)} movement(s) shown.",
                )

            except ValueError as error:
                update_status(window, f"Filter could not be applied: {error}")

        elif event == "-CLEAR-FILTER-":
            window["-START-DATE-"].update("")
            window["-END-DATE-"].update("")
            visible_movements = list(finance_manager.movements)
            active_filter_label = "All movements"

            update_dashboard(
                window,
                finance_manager,
                visible_movements,
                active_filter_label,
            )
            update_status(window, "Filters cleared. All movements are shown.")

        elif event == "-EXPORT-CSV-":
            if export_movements(finance_manager, visible_movements):
                update_status(
                    window,
                    "CSV export completed successfully.",
                )
            else:
                update_status(window, "CSV export canceled.")

    save_categories(finance_manager.categories)
    save_movements(finance_manager.movements)
    save_settings(finance_manager.get_settings())
    window.close()