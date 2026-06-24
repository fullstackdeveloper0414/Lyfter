"""
Ejercicios de Manejo de CSVs
Jaime C Smith
06/01/2026
"""

# Program A:
# - Opens the CSV file generated in exercise 1 (video_games.csv).
# - Reads the file using csv.DictReader.
# - Asks the user for an ESRB rating (for example: "T").
# - Displays all video games that have that rating in a readable format.

import csv

CSV_FILE_NAME = "video_games.csv"


def filter_video_games_by_esrb(file_path):
    """
    Read the CSV file of video games and filter by ESRB rating.

    Steps:
    - Open the CSV file with DictReader for easy column access.
    - Ask the user for an ESRB rating (case-insensitive).
    - Print all video games that match this rating.
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

    # Ask the user for an ESRB rating
    user_rating = input("Enter an ESRB rating to filter (e.g., E, T, M): ").strip()
    if not user_rating:
        print("No rating entered. Nothing to filter.")
        return

    # Normalize rating for case-insensitive comparison
    user_rating_upper = user_rating.upper()

    # Filter games that match the given ESRB rating
    filtered_games = [
        game for game in video_games
        if game.get("esrb_rating", "").upper() == user_rating_upper
    ]

    print()

    if not filtered_games:
        print(f"No video games found with ESRB rating '{user_rating_upper}'.")
        return

    print(f"Video games with ESRB rating '{user_rating_upper}':")
    for game in filtered_games:
        name = game.get("name", "Unknown")
        genre = game.get("genre", "Unknown")
        developer = game.get("developer", "Unknown")
        print(f"- {name} (Genre: {genre}, Developer: {developer})")


if __name__ == "__main__":
    filter_video_games_by_esrb(CSV_FILE_NAME)