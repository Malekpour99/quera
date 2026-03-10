# https://quera.org/problemset/3412
# ---------------------------------

from typing import Final, Optional

TAXI_CAPACITY: Final = 4
TAXI_MIDDLE_SEAT_INDEX: Final = 1

TAXI_FRONT_DOOR: Final = "U"
TAXI_BACK_LEFT_DOOR: Final = "L"
TAXI_BACK_RIGHT_DOOR: Final = "R"

front_seat_passenger: Optional[str] = None
back_seat_passengers: list[str] = []

for _ in range(TAXI_CAPACITY):
    passenger, taxi_door = input().strip().split()
    if taxi_door == TAXI_FRONT_DOOR:
        front_seat_passenger = passenger
    elif taxi_door == TAXI_BACK_LEFT_DOOR:
        back_seat_passengers.insert(0, passenger)
    else:
        back_seat_passengers.append(passenger)

print(back_seat_passengers[TAXI_MIDDLE_SEAT_INDEX])
