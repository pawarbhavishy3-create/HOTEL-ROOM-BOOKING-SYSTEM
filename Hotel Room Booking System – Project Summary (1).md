# Hotel Room Booking System – Project Summary

PS No. 64| B.Tech Computer Science and Engineering

Language: Python 3  Concepts Used: Dictionaries, Lists, Functions, File Handling

## Overview

The Hotel Room Booking System is a console-based Python application that automates basic hotel front-desk work. Through a simple menu, a user can view available rooms, book a room for a guest for a given number of nights, cancel an existing booking, and generate a bill. All booking data is stored in a file (`bookings.txt`), so it is kept between runs of the program.

## Room Details

| Room No. | Type | Rate (per night) |
| --- | --- | --- |
| 101 | Single | Rs. 2000 |
| 102 | Double | Rs. 3500 |
| 201 | Suite | Rs. 6000 |

## Key Features

- **View Available Rooms:** shows only the rooms that are not currently booked, with their type and rate.
- **Book a Room:** takes the guest name, room number and number of nights, then confirms the booking.
- **Cancel a Booking:** removes the booking for a given room and makes it available again.
- **Bill Generation:** Bill = (rate × nights) + 12% GST. For example, Room 101 for 2 nights gives 4000 + 480 = **Rs. 4480**.
- **File Handling:** bookings are saved to `bookings.txt` after every change and loaded when the program starts.

## Validations

- Nights must be between **1 and 30**.
- Room number must be valid (101, 102 or 201).
- **Double booking is prevented:** if a room is already booked, the program shows "Room is already booked. Please choose another room."

## Implementation Approach

- Room details are stored in a **dictionary**.
- Current bookings are stored as a **list of dictionaries** (guest, room, nights).
- Separate **functions** handle viewing rooms, booking, cancelling, billing, saving and loading.
- A menu-driven loop runs the program until the user chooses to exit.

## Test Cases Covered

1. **Normal input:** Amit books Room 101 for 2 nights, so the bill is Rs. 4480.
2. **Boundary input:** Neha books Room 102 for 1 night (the minimum), so the bill is Rs. 3920.
3. **Invalid input:** booking an already booked Room 101 shows an error message.
4. **Different valid scenario:** available rooms are listed correctly, and cancelling Room 101 makes it available again.

Test cases as given in the problem statement.

**Test Case 1: Normal input** – Amit books Room 101 for 2 nights.

&#91;image: Test Case 1 output: Room 101 booked for Amit, bill Rs. 4480\]

**Test Case 2: Boundary input** – Neha books Room 102 for 1 night.

&#91;image: Test Case 2 output: Room 102 booked for Neha, bill Rs. 3920\]

**Test Case 3: Invalid input** – Room 101 is already booked, so Neha's booking is rejected.

&#91;image: Test Case 3 output: Room 101 is already booked message\]

**Test Case 4: Different valid scenario** – available rooms are listed, then the booking for Room 101 is cancelled.

&#91;image: Test Case 4 output: available rooms and Room 101 cancelled\]

## Conclusion

The project shows how core Python concepts such as dictionaries, lists, functions and file handling can be combined into a practical, menu-driven application. It handles input validation and data persistence, and it meets all the bare minimum requirements and test cases of the problem statement.
