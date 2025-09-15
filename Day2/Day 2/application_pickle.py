
import pickle
import os

class Flight:
    def __init__(self, id, number, airline_name, seats, price, source, destination):
        self.id = id
        self.number = number
        self.airline_name = airline_name
        self.seats = seats
        self.price = price
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"<Flight {self.number} {self.source}->{self.destination}>"

class BinaryFlightDB:
    def __init__(self, filename="flights.dat"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "wb") as f:
                pickle.dump([], f)

    def add_flight(self, flight):
        flights = self.get_all_flights()
        flights.append(flight)
        with open(self.filename, "wb") as f:
            pickle.dump(flights, f)

    def get_all_flights(self):
        with open(self.filename, "rb") as f:
            return pickle.load(f)

# Example Usage
if __name__ == "__main__":
    db = BinaryFlightDB()
    f2 = Flight(2, "6E202", "IndiGo", 220, 5500, "Chennai", "Bangalore")
    db.add_flight(f2)
    print(db.get_all_flights())