"""
Ejercicios Ejercicios de Diccionarios
Jaime C Smith
05/23/2026
"""

# 1) Create a dictionary that stores information about a hotel:
#    - name
#    - number_of_stars
#    - rooms
#    The value of the key 'rooms' must be a list, and each room must
#    have:
#       - number
#       - floor
#       - price_per_night

# Hotel dictionary with a list of rooms
hotel = {
    "name": "Ocean View Hotel",
    "number_of_stars": 5,
    "rooms": [
        {
            "number": 101,
            "floor": 1,
            "price_per_night": 120.0
        },
        {
            "number": 205,
            "floor": 2,
            "price_per_night": 150.0
        },
        {
            "number": 310,
            "floor": 3,
            "price_per_night": 180.0
        }
    ]
}

# Print the hotel dictionary to verify its structure
print("Hotel information:")
print(hotel)

# Example: print each room in a more readable way
print("\nRooms:")
for room in hotel["rooms"]:
    print(
        f"Room {room['number']} on floor {room['floor']} "
        f"costs {room['price_per_night']} per night"
    )