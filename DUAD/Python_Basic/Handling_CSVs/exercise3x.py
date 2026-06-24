"""
Ejercicios de Manejo de CSVs
Jaime C Smith
06/01/2026
"""

# Program B:
# - Opens the CSV file generated in exercise 1 (video_games.csv).
# - Reads all video games using csv.DictReader.
# - Counts how many video games there are for each genre.
# - Displays the result in an ordered, readable format, similar to:
#
#   Genres found:
#   Action: 5
#   Adventure: 3
#   Sports: 4

import csv
from collections import Counter

CSV_FILE_NAME = "video_games.csv"


def count_video_games_by_genre(file_path):
    """
    Read the video games CSV and count how many games belong to each genre.

    Uses collections.Counter to simplify counting and sorts genres
    alphabetically before printing.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            genres = []

            for game in reader:
                # Get the genre, strip spaces, and skip empty values
                genre = game.get("genre", "").strip()
                if genre:
                    genres.append(genre)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please make sure you have already created it with exercise 1.")
        return
    except OSError as error:
        print(f"Error: Could not open the file '{file_path}'.")
        print("Details:", error)
        return

    if not genres:
        print("No genres found in the CSV file.")
        return

    # Count occurrences of each genre
    genre_counts = Counter(genres)

    # Display the results in a clean, ordered way
    print("Genres found:")
    for genre in sorted(genre_counts.keys()):
        print(f"{genre}: {genre_counts[genre]}")


if __name__ == "__main__":
    count_video_games_by_genre(CSV_FILE_NAME)