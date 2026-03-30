# https://quera.org/problemset/72882
# ----------------------------------

from collections import OrderedDict
from typing import Final

MEAT_SIGN: Final = "*"
FIRST_PLATE: Final = "first_plate"
SECOND_PLATE: Final = "second_plate"

meat_count: dict[str, int] = OrderedDict(
    {
        FIRST_PLATE: 0,
        SECOND_PLATE: 0,
    }
)

plate_row_count, contents_count = map(int, input().strip().split())

for plate in meat_count:
    for _ in range(plate_row_count):
        plate_contents = input().strip()
        for content in plate_contents:
            if content == MEAT_SIGN:
                meat_count[plate] += 1

print(f"{meat_count[FIRST_PLATE]} {meat_count[SECOND_PLATE]}")
