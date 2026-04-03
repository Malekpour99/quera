# https://quera.org/problemset/10230
# ----------------------------------

from typing import Final

NOT_POSSIBLE_MESSAGE: Final = "No"
POSSIBLE_MESSAGE: Final = "Yes"

angle_1, angle_2, angle_3 = map(int, input().strip().split())

if angle_1 + angle_2 + angle_3 != 180:
    print(NOT_POSSIBLE_MESSAGE)
elif angle_1 == 0 or angle_2 == 0 or angle_3 == 0:
    print(NOT_POSSIBLE_MESSAGE)
else:
    print(POSSIBLE_MESSAGE)
