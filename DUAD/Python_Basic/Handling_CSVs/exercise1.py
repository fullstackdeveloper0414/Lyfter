"""
Ejercicios de Manejo de CSVs
Jaime C Smith
05/30/2026
"""

# Program:
# - Lets the user enter information for N video games.
# - Each video game has:
#       - name
#       - genre
#       - developer
#       - esrb_rating
# - Stores all entries in a CSV file separated by commas.
# - The first row contains the headers:
#       name,genre,developer,esrb_rating
#
# Implementation details:
# - Uses the csv module and DictWriter for structured writing.
# - Uses newline='' when opening the file to avoid extra blank lines,
#   matching best practices from the csv documentation.[web:283]
# - Adds basic error handling for file writing errors.
# - Uses helper functions (as in previous sessions) to keep code organized.


import csv

CSV_FILE_NAME = "video_games.csv"


def get_video_game_data():
    """
    Interactively ask the user for video game information
    until they decide to stop.

    Returns:
        list[dict]: list of video games, each as a dictionary with keys:
                    'name', 'genre', 'developer', 'esrb_rating'.
    """
    video_games = []

    print("Enter video game information. Leave the name empty to stop.\n")

    while True:
        # Ask for the video game name
        name = input("Name (leave empty to finish): ").strip()

        # Stop when the user enters an empty name
        if not name:
            break

        # Ask for the rest of the fields
        genre = input("Genre: ").strip()
        developer = input("Developer: ").strip()
        esrb_rating = input("ESRB rating (e.g., E, T, M): ").strip()

        # Create a dictionary representing one video game
        video_game = {
            "name": name,
            "genre": genre,
            "developer": developer,
            "esrb_rating": esrb_rating,
        }

        # Add the video game to our list
        video_games.append(video_game)
        print("Video game added.\n")

    return video_games


def save_video_games_to_csv(file_path, video_games):
    """
    Save a list of video game dictionaries to a comma-separated CSV file.

    Args:
        file_path (str): path of the CSV file to create.
        video_games (list[dict]): list of video game records.
    """
    # If there is nothing to save, inform the user and exit
    if not video_games:
        print("No video games to save. File was not created.")
        return

    # Define the order of the columns explicitly
    fieldnames = ["name", "genre", "developer", "esrb_rating"]

    try:
        # Open the file in write mode, with UTF-8 encoding and newline=''
        # to avoid blank lines between rows (recommended when using csv).[web:283][web:282]
        with open(file_path, "w", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write all video game rows
            writer.writerows(video_games)

    except OSError as error:
        # Handle file-related errors (permissions, invalid path, etc.)
        print(f"Error: Could not write to file '{file_path}'.")
        print("Details:", error)
        return

    print(f"Saved {len(video_games)} video game(s) to '{file_path}'.")


def main():
    """
    Main function:
    - Collects video game data from the user.
    - Saves the data in a comma-separated CSV file.
    """
    video_games = get_video_game_data()
    save_video_games_to_csv(CSV_FILE_NAME, video_games)


if __name__ == "__main__":
    main()