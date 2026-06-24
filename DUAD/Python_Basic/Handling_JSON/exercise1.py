"""
Ejercicios extra de Manejo de JSON
Jaime C Smith
06/03/2026
"""

import json
from pathlib import Path

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


def find_pokemon_by_type():
    """
    Ask the user for a Pokemon type and display all Pokemon
    that match that type (case-insensitive).
    """
    pokemons = load_pokemons(JSON_FILE)
    if not pokemons:
        return

    # Ask the user for a type to search
    print("=== Search Pokemon by Type ===")
    user_type = input("Enter the type of Pokemon to search (e.g., Water, Fire, Electric): ").strip()

    if not user_type:
        print("No type entered. Nothing to search.")
        return

    user_type_lower = user_type.lower()

    # Filter the list of Pokemon by the given type (case-insensitive)
    matching_pokemons = [
        p for p in pokemons
        if str(p.get("type", "")).lower() == user_type_lower
    ]

    print()
    if not matching_pokemons:
        print(f"No Pokemon found with type '{user_type}'.")
        return

    print(f"The Pokemon of type '{user_type}' are:")
    for pokemon in matching_pokemons:
        name = pokemon.get("name", "Unknown")
        print(f"- {name}")


if __name__ == "__main__":
    find_pokemon_by_type()