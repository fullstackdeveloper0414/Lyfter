"""
Ejercicios de Manejo de CSVs
Jaime C Smith
05/30/2026
"""

# Program 1:
# - Opens the CSV file generated in exercise 1 (video_games.csv).
# - Uses csv.reader() to read each line.
# - Skips the header row.
# - Prints each video game in a readable format, line by line.
#
# Example output:
#   Name: Grand Theft Auto IV
#   Genre: Action
#   Developer: Rockstar Games
#   ESRB Rating: M
#   ------------------------------


import csv

CSV_FILE_NAME = "video_games.csv"


def display_video_games_from_csv(file_path):
    """
    Read a CSV file using csv.reader() and print each video game
    in a human-readable format.

    If the file does not exist, inform the user.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)

            # Read the header row first (name, genre, developer, esrb_rating)
            try:
                headers = next(reader)
            except StopIteration:
                print("The CSV file is empty. Nothing to display.")
                return

            # Determine the index of each column (in case order changes)
            # This makes the code more robust.
            # Expected headers: name, genre, developer, esrb_rating
            try:
                name_index = headers.index("name")
                genre_index = headers.index("genre")
                developer_index = headers.index("developer")
                esrb_index = headers.index("esrb_rating")
            except ValueError:
                print("Error: CSV headers do not match expected columns.")
                print("Expected headers: name, genre, developer, esrb_rating")
                print(f"Found headers: {headers}")
                return

            # Process each data row
            print("\nVideo games in the CSV file:\n")

            for row in reader:
                # Skip empty rows if any
                if not row:
                    continue

                name = row[name_index]
                genre = row[genre_index]
                developer = row[developer_index]
                esrb_rating = row[esrb_index]

                print(f"Name: {name}")
                print(f"Genre: {genre}")
                print(f"Developer: {developer}")
                print(f"ESRB Rating: {esrb_rating}")
                print("-" * 30)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please make sure you have already created it with exercise 1.")
    except OSError as error:
        print(f"Error: Could not open the file '{file_path}'.")
        print("Details:", error)


if __name__ == "__main__":
    display_video_games_from_csv(CSV_FILE_NAME)