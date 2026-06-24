"""
Ejercicios de Manejo de Archivos
Jaime C Smith
05/27/2026
"""

# This program:
# - Reads song names from an input text file, one song name per line.
# - Sorts the song names alphabetically.
# - Writes the sorted song names into an output text file, one per line.
#
# You can change INPUT_FILE and OUTPUT_FILE to match your filenames.


INPUT_FILE = "songs_input.txt"   # File that contains the original song names
OUTPUT_FILE = "songs_sorted.txt" # File where we will save the sorted names


def read_song_names(path):
    """
    Read song names from a text file, one per line.

    Steps:
    - Open the file in read mode with UTF-8 encoding.
    - Use readlines() to get a list of lines.
    - Strip newline characters and surrounding spaces from each line.
    - Ignore empty lines.

    Returns:
        list[str]: list of song names.
    """
    song_names = []

    # Use 'with' to ensure the file closes automatically
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            # Remove newline and extra spaces from both ends
            clean_line = line.strip()

            # Only add non-empty lines
            if clean_line:
                song_names.append(clean_line)

    return song_names


def write_song_names(path, song_names):
    """
    Write song names to a text file, one per line.

    Steps:
    - Open the file in write mode with UTF-8 encoding.
    - Iterate over the list and write each song name followed by a newline.
    """
    with open(path, "w", encoding="utf-8") as file:
        for name in song_names:
            file.write(name + "\n")


def main():
    """
    Main function that:
    - Reads song names from INPUT_FILE.
    - Sorts them alphabetically.
    - Writes them into OUTPUT_FILE.
    - Prints a small confirmation message.
    """
    # Read the original song names
    songs = read_song_names(INPUT_FILE)

    # Sort the list of songs alphabetically (A–Z)
    songs.sort()

    # Write the sorted list into the output file
    write_song_names(OUTPUT_FILE, songs)

    print(f"Sorted {len(songs)} song(s) from '{INPUT_FILE}' and saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()