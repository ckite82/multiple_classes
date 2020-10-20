class Bus: 
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger_1):
        self.passengers.append(passenger_1)

    def drop_off(self, passenger_2):
        self.passengers.remove(passenger_2)

    def empty(self):
        for person in self.passengers:
            self.passengers.remove(person)

    def pick_up_from_stop(self, bus_stop):
        for person in bus_stop.queue:
            self.passengers.append(person)
        # self.pick_up(bus_stop.queue)
        bus_stop.clear()

        # passengers with diff destinations going on to different bus
