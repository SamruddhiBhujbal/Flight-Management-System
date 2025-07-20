class Flight:
    def __init__(self, flight_number, destination, time):
        self.flight_number = flight_number
        self.destination = destination
        self.time = time

class FlightManagementSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def display_flights(self):
        for flight in self.flights:
            print(f"Flight {flight.flight_number} to {flight.destination} at {flight.time}")

def main():
    fms = FlightManagementSystem()

    fms.add_flight(Flight("AI101", "Mumbai", "08:00"))
    fms.add_flight(Flight("SJ202", "Delhi", "10:30"))

    fms.display_flights()

if __name__ == "__main__":
    main()