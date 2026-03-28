# https://quera.org/problemset/6192
# ---------------------------------

from typing import Final

DEATH_MESSAGE: Final = "dari mimiri"
SURVIVE_MESSAGE: Final = "zende mimuni"

a, b, c, d, e, f = map(int, input().strip().split())

box_width = min(a, b)
box_length = max(a, b)

ice_cube_dimensions: list[int] = sorted([d, e, f])
ice_cube_width = ice_cube_dimensions[0]
ice_cube_length = ice_cube_dimensions[1]

can_survive: bool = True

if ice_cube_width > box_width or ice_cube_length > box_length:
    can_survive = False

if can_survive:
    print(SURVIVE_MESSAGE)
else:
    print(DEATH_MESSAGE)
