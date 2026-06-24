"""
Ejercicios de Manejo de CSVs
Jaime C Smith
05/30/2026
"""

# Program 2:
# - Reuses the same videogame structure (name, genre, developer, ESRB rating).
# - Saves the videogames to a file where values are separated by tabs
#   instead of commas.
#
# We still use the csv module and DictWriter, but we configure the writer
# with delimiter="\t", as suggested by the csv documentation.[file:277]
#
# Conceptual example of final file:
#   nombre   genero   desarrollador   clasificacion
#   Grand Theft Auto IV   Accion   Rockstar Games   M
#   The Elder Scrolls IV: Oblivion   RPG   Bethesda   M
#   Tony Hawk's Pro Skater 2   Deportes   Activision   T

import csv

TSV_FILE_NAME = "videojuegos_tabs.txt"


def get_videogame_data():
    """
    Interactively ask the user for videogame information
    until they decide to stop.

    This is intentionally the same logic as in Program 1 to keep
    each script self-contained for the exercises.
    """
    videogames = []

    print("Enter videogame information. Leave the name empty to stop.\n")

    while True:
        name = input("Name (leave empty to finish): ").strip()

        if not name:
            break

        genre = input("Genre: ").strip()
        developer = input("Developer: ").strip()
        esrb = input("ESRB rating (e.g., E, T, M): ").strip()

        videogame = {
            "nombre": name,
            "genero": genre,
            "desarrollador": developer,
            "clasificacion": esrb,
        }

        videogames.append(videogame)
        print("Videogame added.\n")

    return videogames


def save_videogames_to_tsv(file_path, videogames):
    """
    Save a list of videogame dictionaries to a tab-separated file.

    Args:
        file_path (str): path of the output file.
        videogames (list[dict]): list of videogame records.
    """
    if not videogames:
        print("No videogames to save. File was not created.")
        return

    fieldnames = ["nombre", "genero", "desarrollador", "clasificacion"]

    # Open the file in write mode, UTF-8 encoding, newline=''
    with open(file_path, "w", encoding="utf-8", newline="") as tsv_file:
        # Create a DictWriter with a tab delimiter instead of a comma.
        # This uses the same csv API but produces tab-separated values.[file:277]
        writer = csv.DictWriter(tsv_file, fieldnames=fieldnames, delimiter="\t")

        # Write header row
        writer.writeheader()

        # Write all videogame rows
        writer.writerows(videogames)

    print(f"Saved {len(videogames)} videogame(s) to '{file_path}' with tab separation.")


def main():
    """
    Main function for Program 2:
    - Collects videogame data from the user.
    - Saves the data in a tab-separated file using the csv module.
    """
    videogames = get_videogame_data()
    save_videogames_to_tsv(TSV_FILE_NAME, videogames)


if __name__ == "__main__":
    main()