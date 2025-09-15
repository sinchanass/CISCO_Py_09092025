import json
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

    def to_dict(self):
        return self.__dict__

class JSONFlightDB:
    def __init__(self, filename="flights.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def add_flight(self, flight):
        flights = self.get_all_flights()
        flights.append(flight.to_dict())
        with open(self.filename, "w") as f:
            json.dump(flights, f, indent=4)

    def get_all_flights(self):
        with open(self.filename, "r") as f:
            return json.load(f)


if __name__ == "__main__":
    db = JSONFlightDB()
    f1 = Flight(1, "AI101", "Air India", 180, 6500, "Delhi", "Mumbai")
    db.add_flight(f1)
    print(db.get_all_flights())
