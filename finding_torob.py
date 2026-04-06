# https://quera.org/problemset/62451
# ----------------------------------

from dataclasses import dataclass
from typing import Annotated, Literal, Final

LEFT_DIRECTION: Final = "left"
RIGHT_DIRECTION: Final = "right"
FIXED_POSITION: Final = "fixed"

Direction = Annotated[
    str,
    Literal[
        LEFT_DIRECTION,
        RIGHT_DIRECTION,
        FIXED_POSITION,
    ],
]

FIXED_DISTANCE: Final = "WAIT WAIT"
DECREASING_DISTANCE: Final = "SEE YOU"
INCREASING_DISTANCE: Final = "BORO BORO"

ReachStatus = Annotated[
    str,
    Literal[
        FIXED_DISTANCE,
        DECREASING_DISTANCE,
        INCREASING_DISTANCE,
    ],
]


@dataclass
class Mover:
    position: int
    velocity: int

    @property
    def move_direction(self) -> Direction:
        if self.velocity > 0:
            return RIGHT_DIRECTION
        elif self.velocity < 0:
            return LEFT_DIRECTION
        else:
            return FIXED_POSITION


def check_target_reach_possibility(*, person: Mover, target: Mover) -> ReachStatus:
    person_direction = person.move_direction
    target_direction = target.move_direction

    if person_direction != target_direction:
        if (
            person.position <= target.position and person_direction == RIGHT_DIRECTION
        ) or (
            target.position <= person.position and target_direction == RIGHT_DIRECTION
        ):
            return DECREASING_DISTANCE
        elif person.velocity != 0 or target.velocity != 0:
            return INCREASING_DISTANCE

    # person_direction == target_direction
    else:
        if person.position <= target.position:
            if person.velocity > target.velocity:
                return DECREASING_DISTANCE
            elif person.velocity < target.velocity:
                return INCREASING_DISTANCE
        else:
            if target.velocity > person.velocity:
                return DECREASING_DISTANCE
            elif target.velocity < person.velocity:
                return INCREASING_DISTANCE

    return FIXED_DISTANCE


ali_x = int(input().strip())
ali_v = int(input().strip())

ali = Mover(
    position=ali_x,
    velocity=ali_v,
)

torob_x = int(input().strip())
torob_v = int(input().strip())

torob = Mover(
    position=torob_x,
    velocity=torob_v,
)

possibility = check_target_reach_possibility(person=ali, target=torob)

print(possibility)
