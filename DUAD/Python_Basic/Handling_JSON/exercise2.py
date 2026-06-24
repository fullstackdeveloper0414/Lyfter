"""
Ejercicios de Manejo de JSON
Jaime C Smith
06/03/2026
"""

import json
from pathlib import Path
from typing import TypeVar, Callable, Optional

# Constant that represents the JSON file used in the lesson.
# Change the path if your file lives in a different folder.
JSON_FILE = Path("pokemons.json")

# Generic type variable for ask_number (bound to int or float)
NumT = TypeVar("NumT", int, float)


# ------------------------------------------------------------------
# File I/O helpers
# ------------------------------------------------------------------

def load_pokemons(file_path: Path) -> list:
    """
    Load the existing list of Pokemon from a JSON file.

    - If the file does not exist, creates it with an empty list and returns [].
    - If the file has invalid JSON, resets the file to [] on disk and returns [].
    - If the file cannot be read (permissions, locked), logs the error and returns [].
    - Always returns a Python list.
    """
    if not file_path.exists():
        print(f"[INFO] File '{file_path}' was not found. Creating a new file with an empty list.\n")
        file_path.write_text("[]", encoding="utf-8")
        return []   # Early return avoids a pointless re-read of the file we just wrote

    try:
        with file_path.open("r", encoding="utf-8") as json_file:
            data = json.load(json_file)

    except json.JSONDecodeError:
        print(f"[WARNING] File '{file_path}' contains invalid JSON. Resetting to an empty list.\n")
        # Also rewrite the file so the next run starts clean
        file_path.write_text("[]", encoding="utf-8")
        return []

    except OSError as error:
        print(f"[ERROR] Could not read '{file_path}': {error}\n")
        return []

    if isinstance(data, list):
        return data

    # If the root element is not a list, wrap it for consistency.
    print("[WARNING] JSON root element is not a list. Converting it to a list.\n")
    return [data]


def save_pokemons(file_path: Path, pokemon_list: list) -> None:
    """
    Save the full list of Pokemon back into the JSON file.

    Uses an atomic write (temp file -> rename) so a crash mid-write
    never corrupts the original file.
    """
    try:
        # Write to a sibling temp file first, then rename atomically.
        # Path.replace() is atomic on Linux/macOS and near-atomic on Windows.
        tmp_path = file_path.with_suffix(".tmp")
        with tmp_path.open("w", encoding="utf-8") as json_file:
            json.dump(pokemon_list, json_file, ensure_ascii=False, indent=4)
        tmp_path.replace(file_path)   # Safe rename — either succeeds fully or not at all
        print(f"\n[SUCCESS] Pokemon list was saved to '{file_path}'.")

    except OSError as error:
        print(f"\n[ERROR] Could not save the file '{file_path}'.")
        print("Details:", error)


# ------------------------------------------------------------------
# Input helpers
# ------------------------------------------------------------------

def ask_number(
    prompt: str,
    default: NumT,
    cast: Callable[[str], NumT],
    min_value: Optional[NumT] = None,
) -> NumT:
    """
    Generic helper that prompts until a valid number of the target type is entered.

    Args:
        prompt:    Text shown to the user.
        default:   Returned on empty input or invalid input.
        cast:      Conversion function — int or float.
        min_value: Optional lower bound; values below it fall back to the default.

    Returns:
        A number of the same type as default.
    """
    text = input(prompt).strip()

    if not text:
        print(f"Using default value: {default}")
        return default

    try:
        value = cast(text)
    except ValueError:
        print(f"Invalid number. Using default value: {default}")
        return default

    if min_value is not None and value < min_value:
        print(f"Value must be at least {min_value}. Using default: {default}")
        return default

    return value


def ask_int(prompt: str, default: int, min_value: Optional[int] = None) -> int:
    """Ask the user for an integer, falling back to default on bad/empty input."""
    return ask_number(prompt, default, int, min_value)


def ask_float(prompt: str, default: float, min_value: Optional[float] = None) -> float:
    """Ask the user for a float, falling back to default on bad/empty input."""
    return ask_number(prompt, default, float, min_value)


def ask_yes_no(prompt: str, default: bool = False) -> bool:
    """
    Ask the user a yes/no question, looping until a valid answer is given.

    - Accepts 'y', 'yes', 'n', 'no' (case-insensitive).
    - Empty input returns the default value without looping.
    """
    while True:
        text = input(prompt).strip().lower()

        if not text:
            return default
        if text in ("y", "yes"):
            return True
        if text in ("n", "no"):
            return False

        # Loop instead of silently defaulting — user likely just mistyped
        print("Please enter 'y' for yes or 'n' for no.")


# ------------------------------------------------------------------
# Pokemon data collection
# ------------------------------------------------------------------

def ask_new_pokemon_data() -> dict:
    """
    Guide the user through entering data for a new Pokemon.

    Returns a dictionary matching the JSON structure:
    {
        "name":      str,
        "type":      str,
        "level":     int,
        "weight_kg": float,
        "is_shiny":  bool,
        "held_item": str or None,
        "skills":    list of str,
        "stats": {
            "hp":      int,
            "attack":  int,
            "defense": int
        }
    }
    """
    print("=== Add a New Pokemon ===")
    print("Please answer the questions below. Press Enter to use the default value.\n")

    # Basic information
    name = input("1) Pokemon name (e.g. Pikachu, Bulbasaur): ").strip()
    if not name:
        name = "Unknown Pokemon"
        print("No name entered. Using 'Unknown Pokemon'.")

    poke_type = input("2) Main type (e.g. Electric, Fire, Water): ").strip()
    if not poke_type:
        poke_type = "Normal"
        print("No type entered. Using 'Normal'.")

    # min_value prevents negative or zero levels/weights
    level  = ask_int(  "3) Level (whole number, e.g. 5, 10, 25) [default 1]: ",  default=1,   min_value=1)
    weight = ask_float("4) Weight in kg (e.g. 6.0, 8.5) [default 1.0]: ",        default=1.0, min_value=0.1)

    # Shiny and held item
    is_shiny = ask_yes_no("5) Is this Pokemon shiny? (y/n) [default n]: ", default=False)

    held_item_text = input(
        "6) Held item (e.g. Charcoal, Leftovers). "
        "Press Enter if it holds nothing: "
    ).strip()
    held_item = held_item_text if held_item_text else None

    # Skills as a comma-separated list
    print("\n7) Skills / moves")
    skills_input = input(
        "   Enter skills separated by commas (e.g. Tackle, Growl, Ember).\n"
        "   Press Enter to leave empty: "
    ).strip()

    if skills_input:
        skills = [s.strip() for s in skills_input.split(",") if s.strip()]
    else:
        skills = []

    # Basic stats — min_value=0 prevents negative stats
    print("\n8) Basic stats (press Enter to use the default shown in brackets):")
    hp      = ask_int("   - HP (default 10): ",     default=10, min_value=0)
    attack  = ask_int("   - Attack (default 5): ",  default=5,  min_value=0)
    defense = ask_int("   - Defense (default 5): ", default=5,  min_value=0)

    return {
        "name":      name,
        "type":      poke_type,
        "level":     level,
        "weight_kg": weight,
        "is_shiny":  is_shiny,
        "held_item": held_item,
        "skills":    skills,
        "stats": {
            "hp":      hp,
            "attack":  attack,
            "defense": defense,
        },
    }


# ------------------------------------------------------------------
# Main program
# ------------------------------------------------------------------

def add_new_pokemon_to_json() -> None:
    """
    Orchestrate the full flow:
      1. Load existing Pokemon from the JSON file.
      2. Collect data for a new Pokemon.
      3. Append and save.
    """
    print("======================================")
    print("  JSON Pokemon Manager - Add a Pokemon")
    print("======================================\n")

    print(f"Loading Pokemon from '{JSON_FILE}'...\n")
    pokemon_list = load_pokemons(JSON_FILE)
    print(f"Currently there are {len(pokemon_list)} Pokemon in the file.\n")

    new_pokemon = ask_new_pokemon_data()
    pokemon_list.append(new_pokemon)
    save_pokemons(JSON_FILE, pokemon_list)

    print("\nNew Pokemon added successfully!")
    print("Here is the Pokemon you just created:\n")
    print(json.dumps(new_pokemon, ensure_ascii=False, indent=4))
    print("\nThank you for using the JSON Pokemon Manager.")


if __name__ == "__main__":
    try:
        add_new_pokemon_to_json()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")