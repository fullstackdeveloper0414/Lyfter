"""
Ejercicios extra de Manejo de JSON
Jaime C Smith
06/03/2026
"""

import json
from pathlib import Path
from collections import defaultdict

JSON_FILE = Path("pokemons.json")


def load_pokemons(file_path: Path):
    """
    Load the Pokemon list from a JSON file.

    Returns an empty list if the file is missing or invalid.
    """
    if not file_path.exists():
        print(f"[ERROR] File '{file_path}' was not found.")
        print("Make sure you already created it in exercise 1.")
        return []

    try:
        with file_path.open("r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except json.JSONDecodeError as error:
        print(f"[ERROR] The file '{file_path}' does not contain valid JSON.")
        print("Details:", error)
        return []

    if not isinstance(data, list):
        print("[ERROR] The JSON root element is not a list. Expected a list of Pokemon.")
        return []

    return data


def show_average_level_by_type():
    """
    Group Pokemon by their type and calculate the average level for each type.

    Steps:
    - Read the JSON file.
    - Group levels by type ('Fire', 'Water', etc.).
    - Compute and display the average level for every type found.
    """
    pokemons = load_pokemons(JSON_FILE)
    if not pokemons:
        return

    # Dictionary: type -> list of levels
    levels_by_type = defaultdict(list)

    for pokemon in pokemons:
        poke_type = pokemon.get("type")
        level = pokemon.get("level")

        # Only consider entries that have both type and level
        if poke_type is None or level is None:
            continue

        # Ensure that level is numeric before adding
        try:
            numeric_level = float(level)
        except (TypeError, ValueError):
            continue

        levels_by_type[poke_type].append(numeric_level)

    if not levels_by_type:
        print("No valid type/level data found in the JSON file.")
        return

    print("=== Average Level by Type ===\n")
    for poke_type, levels in sorted(levels_by_type.items()):
        if not levels:
            continue
        avg_level = sum(levels) / len(levels)
        print(f"Type: {poke_type} → Average level: {avg_level:.1f}")


if __name__ == "__main__":
    show_average_level_by_type()