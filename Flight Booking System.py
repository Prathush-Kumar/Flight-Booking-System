class Flight:
    def __init__(self, flight_number, destination, available_seats, price):      
        self.flight_number = flight_number
        self.destination = destination
        self.available_seats = available_seats          
        self.price = price   

    def check_availability(self):
        return self.available_seats > 0   

    def reserve_seat(self):
        if self.check_availability():
            self.available_seats -= 1 
            return True
        return False

    def cancel_seat(self):
        self.available_seats += 1

    def __str__(self):
        return f"Flight {self.flight_number} to {self.destination} with {self.available_seats} available seats at ${self.price}."


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def __str__(self):
        return f"Passenger {self.name} ({self.passport_number})"


class Booking:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight
        self.booking_status = "Confirmed" if flight.reserve_seat() else "Failed"

    def cancel(self):
        if self.booking_status == "Confirmed":
            self.flight.cancel_seat()
            self.booking_status = "Cancelled"
            print(f"Booking cancelled for {self.passenger.name} on flight {self.flight.flight_number}.")
        else:
            print("No booking to cancel.")

    def reschedule(self, new_flight):
        if self.booking_status == "Confirmed":
            self.flight.cancel_seat()
            self.flight = new_flight
            if new_flight.reserve_seat():
                self.booking_status = "Rescheduled"
                print(f"Booking rescheduled for {self.passenger.name} to flight {new_flight.flight_number}.")
            else:
                self.booking_status = "Failed"
                print("Rescheduling failed. No available seats.")
        else:
            print("No booking to reschedule.")

    def __str__(self):
        return f"Booking for {self.passenger.name} on flight {self.flight.flight_number}, Status: {self.booking_status}"


class FlightBookingSystem:
    def __init__(self):
        self.flights = []
        self.bookings = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, destination):
        available_flights = [flight for flight in self.flights if flight.destination == destination and flight.check_availability()]
        return available_flights

    def make_booking(self, passenger, flight):
        if flight.reserve_seat():
            booking = Booking(passenger, flight)
            self.bookings.append(booking)
            print(f"Booking confirmed for {passenger.name} on flight {flight.flight_number}.")
            return booking
        else:
            print("Booking failed. No available seats.")
            return None

    def display_flights(self):
        if not self.flights:
            print("No flights available.")
        for flight in self.flights:
            print(flight)

    def display_bookings(self):
        if not self.bookings:
            print("No bookings found.")
        for booking in self.bookings:
            print(booking)
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.add_flight(Flight("AA123", "Hyderabad", 5, 300))
    system.add_flight(Flight("AA124", "America", 0, 500))
    system.add_flight(Flight("AA125", "London", 3, 350))
    while True:
        print("\n---- Welcome To High-Fly Flight Booking System ----")
        print("1. Search Flights")
        print("2. Book a Flight")
        print("3. Display All Flights")
        print("4. Display All Bookings")
        print("5. Cancel a Booking")
        print("6. Reschedule a Booking")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            destination = input("Enter destination: ")
            available_flights = system.search_flights(destination)
            if available_flights:
                print(f"\nAvailable flights to {destination}:")
                for flight in available_flights:
                    print(flight)
            else:
                print(f"No available flights to {destination}.")

        elif choice == '2':
            name = input("Enter passenger name: ")
            passport_number = input("Enter passport number: ")
            passenger = Passenger(name, passport_number)
            
            destination = input("Enter destination for booking: ")
            available_flights = system.search_flights(destination)
            if available_flights:
                print(f"\nAvailable flights to {destination}:")
                for i, flight in enumerate(available_flights, 1):
                    print(f"{i}. {flight}")
                
                flight_choice = int(input("Choose a flight by number: ")) - 1
                chosen_flight = available_flights[flight_choice]
                system.make_booking(passenger, chosen_flight)
            else:
                print(f"No available flights to {destination}.")

        elif choice == '3':
            system.display_flights()

        elif choice == '4':
            system.display_bookings()

        elif choice == '5':
            if system.bookings:
                print("\nExisting bookings:")
                for i, booking in enumerate(system.bookings, 1):
                    print(f"{i}. {booking}")
                
                booking_choice = int(input("Choose a booking to cancel by number: ")) - 1
                chosen_booking = system.bookings[booking_choice]
                chosen_booking.cancel()
            else:
                print("No bookings to cancel.")

        elif choice == '6':
            if system.bookings:
                print("\nExisting bookings:")
                for i, booking in enumerate(system.bookings, 1):
                    print(f"{i}. {booking}")
                
                booking_choice = int(input("Choose a booking to reschedule by number: ")) - 1
                chosen_booking = system.bookings[booking_choice]
                
                new_destination = input("Enter the new destination for rescheduling: ")
                available_flights = system.search_flights(new_destination)
                if available_flights:
                    print(f"\nAvailable flights to {new_destination}:")
                    for i, flight in enumerate(available_flights, 1):
                        print(f"{i}. {flight}")
                    
                    flight_choice = int(input("Choose a new flight by number: ")) - 1
                    new_flight = available_flights[flight_choice]
                    chosen_booking.reschedule(new_flight)
                else:
                    print(f"No available flights to {new_destination}.")
            else:
                print("No bookings to reschedule.")

        elif choice == '7':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
