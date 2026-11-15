# Hotel Room Booking System (PS 64)

A simple Python console application for a hotel. The user can view available rooms, book a room for a number of nights, cancel a booking, and get a bill with 12% GST. Bookings are saved in a file so they are not lost when the program closes.

**University:** Rungta International Skills University
**School:** School of Computer Science and Engineering (B.Tech CSE)
**Language:** Python 3
**Concepts used:** Dictionaries, Lists, Functions, File Handling

## Rooms and Prices

| Room | Type   | Price per night |
|------|--------|-----------------|
| 101  | Single | Rs. 2000        |
| 102  | Double | Rs. 3500        |
| 201  | Suite  | Rs. 6000        |

**Bill = (price x nights) + 12% GST**

## How to Run

1. Install Python 3 (https://www.python.org).
2. Put `hotel_booking.py` in a folder.
3. Open a terminal in that folder and run:

   ```
   python hotel_booking.py
   ```

The file `bookings.txt` is created automatically in the same folder after the first booking.

## Menu

```
1. View available rooms
2. Book a room
3. View all bookings
4. Cancel a booking
5. Exit
```

## Rules the Program Checks

- The room number must exist (101, 102 or 201).
- A room that is already booked cannot be booked again.
- Nights must be a whole number from 1 to 30.
- Guest name cannot be empty.

## How the Code Is Organised

| Part | What it does |
|------|--------------|
| `rooms` (dictionary) | Stores room number, type and price |
| `bookings` (list of dictionaries) | Stores current bookings: room, guest, nights |
| `save_bookings()` | Writes all bookings to `bookings.txt` after every change |
| `load_bookings()` | Reads `bookings.txt` when the program starts |
| `is_booked()` | Checks if a room is already booked |
| `calculate_bill()` | Calculates price, GST and total |
| `view_available_rooms()` | Shows rooms that are free |
| `book_room()` | Validates input, books the room and prints the bill |
| `cancel_booking()` | Removes a booking and frees the room |
| `main()` | Shows the menu in a loop until the user exits |

## bookings.txt Format

One booking per line:

```
Room 101 - Amit - 2 nights
```

## Test Cases

| # | Scenario | Input | Expected output |
|---|----------|-------|-----------------|
| 1 | Normal | Book, Amit, Room 101, 2 nights | Room 101 booked for Amit, Bill: 4000 + GST 480 = Rs. 4480 |
| 2 | Boundary (1 night) | Book, Neha, Room 102, 1 night | Room 102 booked for Neha, Bill: 3500 + GST 420 = Rs. 3920 |
| 3 | Invalid (already booked) | Room 101 already booked by Amit, Neha tries Room 101 | Room 101 is already booked. Please choose another room. |
| 4 | Cancel | bookings.txt has Room 101 - Amit; view rooms, then cancel 101 | 102 and 201 are available, booking for 101 is cancelled, 101 is available again |

Screenshots of all four test cases are in the `screenshots` folder and in `Project_Summary.docx`.

## Files in This Project

```
hotel_booking.py      main program
bookings.txt          saved bookings (created automatically)
README.md             this file
Project_Summary.docx  summary with test case screenshots
screenshots/          test case output images
```
