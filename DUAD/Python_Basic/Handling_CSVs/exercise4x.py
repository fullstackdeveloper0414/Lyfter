"""
Ejercicios de Manejo de CSVs
Jaime C Smith
05/30/2026
"""

# Program 4:
# - Opens the CSV file generated in exercise 1 (video_games.csv).
# - Reads all video games using csv.DictReader.
# - Asks the user to enter a developer name (e.g., "Rockstar Games").
# - Prints all video games developed by that company in readable format.
#
# Example output:
#   Enter a developer name to filter (e.g., Ubisoft): Ubisoft
#
#   Video games developed by Ubisoft:
#   - Assassin's Creed II (ESRB Rating: M, Genre: Adventure)
#   - Rayman Legends (ESRB Rating: E, Genre: Platform)


import csv

CSV_FILE_NAME = "video_games.csv"


def filter_video_games_by_developer(file_path):
    """
    Read the video games CSV and filter by developer name.

    Steps:
    - Ask the user for a developer name (case-insensitive).
    - Print all video games developed by that company.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            video_games = list(reader)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please make sure you have already created it with exercise 1.")
        return
    except OSError as error:
        print(f"Error: Could not open the file '{file_path}'.")
        print("Details:", error)
        return

    if not video_games:
        print("The CSV file is empty. No video games to filter.")
        return

    # Ask the user for a developer name
    user_developer = input("Enter a developer name to filter (e.g., Ubisoft): ").strip()

    if not user_developer:
        print("No developer name entered. Nothing to filter.")
        return

    # Normalize for case-insensitive comparison
    user_dev_lower = user_developer.lower()

    # Filter games that match the developer name (case-insensitive)
    filtered_games = []
    for game in video_games:
        developer = game.get("developer", "")
        if developer.lower() == user_dev_lower:
            filtered_games.append(game)

    print()

    if not filtered_games:
        print(f"No video games found for developer '{user_developer}'.")
        return

    print(f"Video games developed by {user_developer}:")
    for game in filtered_games:
        name = game.get("name", "Unknown")
        esrb_rating = game.get("esrb_rating", "Unknown")
        genre = game.get("genre", "Unknown")
        print(f"- {name} (ESRB Rating: {esrb_rating}, Genre: {genre})")


if __name__ == "__main__":
    filter_video_games_by_developer(CSV_FILE_NAME)