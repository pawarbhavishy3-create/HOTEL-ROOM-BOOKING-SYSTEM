import os
 
BOOKINGS_FILE = "bookings.txt"
GST_RATE = 0.12
 

ROOMS = {
    101: {"type": "Single", "rate": 2000},
    102: {"type": "Double", "rate": 3500},
    201: {"type": "Suite", "rate": 6000},
}
 

bookings = []
 
 
def load_bookings():
    
    bookings.clear()
    if not os.path.exists(BOOKINGS_FILE):
        return
    with open(BOOKINGS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            try:
                parts = [p.strip() for p in line.split(" - ")]
                room = int(parts[0].replace("Room", "").strip())
                guest = parts[1]
                nights = int(parts[2].split()[0])
                if room in ROOMS and not is_booked(room):
                    bookings.append({"room": room, "guest": guest, "nights": nights})
            except (ValueError, IndexError):
                continue  
 
 
def save_bookings():
    
    with open(BOOKINGS_FILE, "w") as f:
        for b in bookings:
            f.write(f"Room {b['room']} - {b['guest']} - {b['nights']} nights\n")
 
 
def is_booked(room):
    return any(b["room"] == room for b in bookings)
 
 
def view_available():
    print("Available rooms:")
    found = False
    for room, info in ROOMS.items():
        if not is_booked(room):
            print(f"{room} {info['type']} Rs. {info['rate']}")
            found = True
    if not found:
        print("No rooms available.")
 
 
def view_bookings():
    if not bookings:
        print("No current bookings.")
        return
    print("Current bookings:")
    for b in bookings:
        print(f"Room {b['room']} - {b['guest']} - {b['nights']} nights")
 
 
def generate_bill(room, nights):
    """Bill = rate x nights + 12% GST."""
    base = ROOMS[room]["rate"] * nights
    gst = round(base * GST_RATE)
    return base, gst, base + gst
 
 
def book_room():
    guest = input("Guest: ").strip()
    if not guest:
        print("Guest name cannot be empty.")
        return
 
    try:
        room = int(input("Room: ").strip())
    except ValueError:
        print("Invalid room number.")
        return
    if room not in ROOMS:
        print("Room does not exist.")
        return
    if is_booked(room):
        print(f"Room {room} is already booked. Please choose another room.")
        return
 
    try:
        nights = int(input("Nights: ").strip())
    except ValueError:
        print("Nights must be a number.")
        return
    if nights < 1 or nights > 30:
        print("Nights must be between 1 and 30.")
        return
 
    bookings.append({"room": room, "guest": guest, "nights": nights})
    save_bookings()
 
    base, gst, total = generate_bill(room, nights)
    print(f"Room {room} booked for {guest} | {nights} night{'s' if nights > 1 else ''}")
    print(f"Bill: {base} + GST {gst} = Rs. {total}")
 
 
def cancel_booking():
    try:
        room = int(input("Room: ").strip())
    except ValueError:
        print("Invalid room number.")
        return
    for b in bookings:
        if b["room"] == room:
            bookings.remove(b)
            save_bookings()
            print(f"Booking for room {room} cancelled. Room {room} is now available.")
            return
    print(f"No booking found for room {room}.")
 
 
def main():
    load_bookings()
    while True:
        print("\n=== Hotel Room Booking System ===")
        print("1. View available rooms")
        print("2. Book a room")
        print("3. View bookings")
        print("4. Cancel a booking")
        print("5. Exit")
        choice = input("Menu option: ").strip()
 
        if choice == "1":
            view_available()
        elif choice == "2":
            book_room()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("bye")
            break
        else:
            print("Invalid option. Please choose 1-5.")
 
 
if __name__ == "__main__":
    main()
 