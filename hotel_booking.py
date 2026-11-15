# ---------------------------------------------------------
# Hotel Room Booking System  (PS 64)
# Concepts used: Dictionaries, Lists, Functions, File Handling
# ---------------------------------------------------------

FILE_NAME = "bookings.txt"
GST_RATE = 0.12          # 12% GST

# 1. Room details are stored in a DICTIONARY
#    room number -> (room type, price per night)
rooms = {
    101: {"type": "Single", "price": 2000},
    102: {"type": "Double", "price": 3500},
    201: {"type": "Suite", "price": 6000},
}

# 2. Current bookings are stored in a LIST of dictionaries
#    Example: [{"room": 101, "guest": "Amit", "nights": 2}]
bookings = []


# ---------------------------------------------------------
# FILE HANDLING
# ---------------------------------------------------------
def save_bookings():
    """Write all bookings to bookings.txt (called after every change)."""
    file = open(FILE_NAME, "w")
    for b in bookings:
        # Line looks like:  Room 101 - Amit - 2 nights
        file.write("Room " + str(b["room"]) + " - " + b["guest"] + " - " + str(b["nights"]) + " nights\n")
    file.close()


def load_bookings():
    """Read bookings from bookings.txt when the program starts."""
    try:
        file = open(FILE_NAME, "r")
    except FileNotFoundError:
        return  # No file yet, so there are no old bookings

    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(" - ")                      # ["Room 101", "Amit", "2 nights"]
        room = int(parts[0].replace("Room ", ""))
        guest = parts[1]
        nights = int(parts[2].replace(" nights", ""))
        bookings.append({"room": room, "guest": guest, "nights": nights})
    file.close()


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------
def is_booked(room_number):
    """Return True if the room is already booked."""
    for b in bookings:
        if b["room"] == room_number:
            return True
    return False


def calculate_bill(room_number, nights):
    """Bill = price x nights + 12% GST. Returns (base, gst, total)."""
    base = rooms[room_number]["price"] * nights
    gst = base * GST_RATE
    total = base + gst
    return base, gst, total


def ask_room_number():
    """Ask for a room number and check it is a valid number. Returns None if invalid."""
    text = input("Room: ")
    if not text.isdigit():
        print("Invalid room number. Please enter digits only.")
        return None
    room_number = int(text)
    if room_number not in rooms:
        print("Room", room_number, "does not exist.")
        return None
    return room_number


# ---------------------------------------------------------
# MAIN FEATURES
# ---------------------------------------------------------
def view_available_rooms():
    print("\nAvailable rooms:")
    found = False
    for number in rooms:
        if not is_booked(number):
            print(number, rooms[number]["type"], "Rs.", rooms[number]["price"])
            found = True
    if not found:
        print("No rooms are available right now.")


def view_all_bookings():
    print("\nCurrent bookings:")
    if len(bookings) == 0:
        print("No bookings yet.")
    for b in bookings:
        print("Room", b["room"], "-", b["guest"], "-", b["nights"], "nights")


def book_room():
    guest = input("Guest: ").strip()
    if guest == "":
        print("Guest name cannot be empty.")
        return

    room_number = ask_room_number()
    if room_number is None:
        return

    # Do not allow double booking
    if is_booked(room_number):
        print("Room", room_number, "is already booked. Please choose another room.")
        return

    # Nights must be a number between 1 and 30
    nights_text = input("Nights: ")
    if not nights_text.isdigit():
        print("Invalid input. Nights must be a number.")
        return
    nights = int(nights_text)
    if nights < 1 or nights > 30:
        print("Nights must be between 1 and 30.")
        return

    # Everything is valid, so save the booking
    bookings.append({"room": room_number, "guest": guest, "nights": nights})
    save_bookings()

    base, gst, total = calculate_bill(room_number, nights)
    print("Room", room_number, "booked for", guest, "|", nights, "night(s)")
    print("Bill:", int(base), "+ GST", int(gst), "= Rs.", int(total))


def cancel_booking():
    room_number = ask_room_number()
    if room_number is None:
        return

    for b in bookings:
        if b["room"] == room_number:
            bookings.remove(b)
            save_bookings()
            print("Booking for room", room_number, "cancelled. Room", room_number, "is now available.")
            return

    print("Room", room_number, "has no booking to cancel.")


# ---------------------------------------------------------
# PROGRAM STARTS HERE
# ---------------------------------------------------------
def main():
    load_bookings()

    while True:
        print("\n===== Hotel Room Booking System =====")
        print("1. View available rooms")
        print("2. Book a room")
        print("3. View all bookings")
        print("4. Cancel a booking")
        print("5. Exit")
        choice = input("Menu option: ")

        if choice == "1":
            view_available_rooms()
        elif choice == "2":
            book_room()
        elif choice == "3":
            view_all_bookings()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1 to 5.")


main()
