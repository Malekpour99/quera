# https://quera.org/problemset/170059
# -----------------------------------

from dataclasses import dataclass


@dataclass
class Coordinate:
    row: int
    column: int

    def find_distance(self, target: "Coordinate") -> int:
        return abs(self.row - target.row) + abs(self.column - target.column)


# considering top-left as center 0-0
coordinates: dict[int, Coordinate] = {
    1: Coordinate(row=0, column=0),
    2: Coordinate(row=0, column=1),
    3: Coordinate(row=1, column=0),
    4: Coordinate(row=1, column=1),
}

current_place = int(input().strip())
target_place = int(input().strip())

current_coordinate = coordinates[current_place]
target_coordinate = coordinates[target_place]

print(current_coordinate.find_distance(target_coordinate))
