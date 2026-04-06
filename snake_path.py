# https://quera.org/problemset/226378
# -----------------------------------

from dataclasses import dataclass
from typing import Annotated, Literal, Final

Movement = Annotated[str, Literal["L", "R", "F"]]

INITIAL_ROW: Final = 1
INITIAL_COLUMN: Final = 0


@dataclass
class Snake:
    row: int = INITIAL_ROW
    column: int = INITIAL_COLUMN

    def move(self, movement: Movement):
        if movement == "L":
            self._move_left()
        elif movement == "R":
            self._move_right()
        elif movement == "F":
            self._move_forward()
        else:
            raise Exception(f"invalid movement: {movement}")

    def _move_forward(self):
        self.column += 1

    def _move_left(self):
        self.row -= 1
        self.column += 1

    def _move_right(self):
        self.row += 1
        self.column += 1

    def is_dead(self) -> bool:
        if self.row > 1 or self.row < 0:
            return True

        return False


path: tuple[list[str], list[str]] = (
    ["0"] * 8,
    ["0"] * 8,
)
snake = Snake()
path[snake.row][snake.column] = "1"

movements: Movement = input().strip()

for movement in movements:

    snake.move(movement=movement)

    if snake.is_dead():
        print("DEATH")
        exit()
    else:
        path[snake.row][snake.column] = "1"

for row in path:
    print("".join(row))
