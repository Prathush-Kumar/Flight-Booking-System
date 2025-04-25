# Flight-Booking-System       
  

# Overview

This project is a simple flight booking system that allows users to search for available flights, book flights, view all available flights, manage bookings (including cancellation and rescheduling), and display all bookings. The system also supports managing seats for flights, where each flight has a limited number of available seats.

Features

Search Flights: Users can search for available flights to a specified destination.

Book a Flight: Passengers can book a seat on an available flight, and the system will confirm or deny the booking based on seat availability.

Display All Flights: The system will list all flights, showing their flight number, destination, available seats, and price.

Display All Bookings: Users can view all their current bookings, along with their status.

Cancel a Booking: Users can cancel an existing booking, which will free up the seat on the flight.

Reschedule a Booking: Users can reschedule their booking to a different flight if a seat is available on the new flight.

Exit: The system will exit the program when the user selects this option.

Classes

1. Flight
   
Represents a flight with the following attributes:

flight_number: The flight number.

destination: The destination of the flight.

available_seats: The number of seats still available for booking.

price: The price of a ticket for the flight.

Methods:

check_availability(): Checks if the flight has available seats.

reserve_seat(): Reserves a seat on the flight if available.

cancel_seat(): Cancels a reservation, freeing up a seat.

2. Passenger
   
Represents a passenger with the following attributes:

name: The name of the passenger.

passport_number: The passport number of the passenger.

3. Booking
   
Represents a booking made by a passenger on a flight. The attributes are:

passenger: The passenger who made the booking.

flight: The flight on which the booking was made.

booking_status: The status of the booking (Confirmed, Failed, Cancelled, or Rescheduled).

Methods:

cancel(): Cancels the booking and frees the seat.

reschedule(new_flight): Reschedules the booking to a new flight if possible.

4. FlightBookingSystem
   
The core of the booking system. It manages the flights and bookings, and handles the operations like adding flights, searching for available flights, making bookings, and displaying 

flights/bookings.


Methods:

add_flight(flight): Adds a flight to the system.

search_flights(destination): Searches for available flights to a specified destination.

make_booking(passenger, flight): Makes a booking for a passenger on a chosen flight.

display_flights(): Displays all available flights.

display_bookings(): Displays all bookings.

Topics Used in the Code

Topic and Concepts

1. Object-Oriented Programming (OOP):

Classes and Objects: The system uses multiple classes like Flight, Passenger, Booking, and FlightBookingSystem to structure the project around real-world entities.

Attributes and Methods: Each class contains attributes (variables) and methods (functions) to model the behavior of the objects, such as booking a flight or checking seat availability.

Encapsulation: Each class encapsulates its data and provides methods to interact with that data, ensuring that the internal state is controlled and modified in specific ways.

Object Interaction: Objects of different classes interact with each other. For example, a Booking object interacts with a Flight and a Passenger object.

2. Conditionals (if-else statements):
   
Used throughout the program to make decisions, like checking if there are available seats on a flight (check_availability()) or confirming whether a booking is successful.

3. Loops (for, while loops):
   
For Loops: Used to iterate over lists of flights and bookings to display them or perform actions like cancelling or rescheduling bookings.

While Loop: The main loop that keeps the program running until the user chooses to exit.

4. Exception Handling (Implicitly via user input validation):

While there’s no explicit try-except block in the code, it assumes user input is valid. However, it's always good practice to handle possible exceptions (e.g., invalid menu choices or flight numbers).

5. String Formatting:
   
Used extensively to present flight and booking information in a user-friendly way. The __str__ method in each class ensures that objects are printed in a readable format.

6. Input/Output:
   
The program accepts user input via the console (using input()) and displays output via print() statements to interact with the user.

Conclusion

This simple flight booking system allows users to manage their flight bookings efficiently by providing key functionalities like flight searching, booking, rescheduling, and cancellation. It demonstrates core programming concepts like object-oriented design, conditionals, loops, and list management in Python.




