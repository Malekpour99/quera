# https://quera.org/problemset/102252
# -----------------------------------

class Train:

    def __init__(self, last_visited_city, weight_capacity, is_on_trip):
        self.last_visited_city = last_visited_city
        self.weight_capacity = weight_capacity
        self.is_on_trip = is_on_trip


class Trip:

    all_cities = (
        "Arak",
        "Ardabil",
        "Urmia",
        "Isfahan",
        "Ahvaz",
        "Ilam",
        "Bojnord",
        "Bandar Abbas",
        "Bushehr",
        "Birjand",
        "Tabriz",
        "Tehran",
        "Khorramabad",
        "Rasht",
        "Zahedan",
        "Zanjan",
        "Sari",
        "Semnan",
        "Sanandaj",
        "Shahr-e Kord",
        "Shiraz",
        "Qazvin",
        "Qom",
        "Karaj",
        "Kermanshah",
        "Gorgan",
        "Mashhad",
        "Hamadan",
        "Yasuj",
        "Yazd",
    )

    def __init__(self, origin_city: str, destination_city: str, train: Train):
        self.train: Train = self.train_validation(train)
        self.destination_city = destination_city
        self.origin_city = self.origin_city_validation(origin_city)
        self.passengers: list[Passenger] = []

    def origin_city_validation(self, origin_city: str) -> str:
        if origin_city not in self.all_cities:
            raise Exception("This input is not a verified city!")

        if origin_city == self.destination_city:
            raise Exception("Origin and destination cities can't be the same!")

        if origin_city != self.train.last_visited_city:
            raise Exception(
                "The train of the trip is not available in the origin city!"
            )

        return origin_city

    def train_validation(self, train: Train) -> Train:
        if not isinstance(train, Train):
            raise Exception("This input is not a train!")

        if train.is_on_trip:
            raise Exception("This train is not available!")

        return train

    def __call__(self, *args, **kwds) -> float:
        return self.train.weight_capacity - sum(
            passenger.load_weight for passenger in self.passengers
        )


class Passenger:

    def __init__(self, fullname: str, load_weight: float):
        self.fullname = fullname
        self.load_weight = load_weight

    def attend_trip(self, trip: Trip):
        if trip() < self.load_weight:
            raise Exception("Heavy load!")

        trip.passengers.append(self)

    def cancel_trip(self, trip: Trip):
        if self not in trip.passengers:
            raise Exception("This passenger is not attended to this trip!")

        trip.passengers.remove(self)

    def __str__(self):
        return self.fullname
