"""
Ejercicios extra de Manejo de JSON
Jaime C Smith
06/03/2026
"""

import json
from pathlib import Path

# JSON file that contains the list of Pokemon with stats including "speed"
JSON_FILE = Path("pokemons.json")


def load_pokemons(file_path: Path):
    """
    Load the Pokemon list from a JSON file.

    Returns an empty list if:
    - The file does not exist.
    - The JSON is invalid.
    - The root element is not a list.

    This keeps the rest of the program safe from crashes.
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


def show_pokemon_stats():
    """
    For each Pokemon in the JSON file, display its main statistics.

    Expected 'stats' structure:
    {
        "hp": number,
        "attack": number,
        "defense": number,
        "speed": number
    }

    If some fields are missing, the program uses 'N/A' for that value.
    """
    pokemons = load_pokemons(JSON_FILE)
    if not pokemons:
        return

    print("=== Pokemon Stats ===\n")
    for pokemon in pokemons:
        # Basic info
        name = pokemon.get("name", "Unknown")

        # Stats dictionary (may be missing or incomplete)
        stats = pokemon.get("stats", {})

        attack = stats.get("attack", "N/A")
        defense = stats.get("defense", "N/A")
        speed = stats.get("speed", "N/A")

        print(f"Name   : {name}")
        print(f"Attack : {attack}")
        print(f"Defense: {defense}")
        print(f"Speed  : {speed}")
        print("-" * 30)


if __name__ == "__main__":
    show_pokemon_stats()