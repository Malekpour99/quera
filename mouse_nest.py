# https://quera.org/problemset/91712
# ----------------------------------

from typing import Final

MOVE_LEFT: Final = "L"
MOVE_RIGHT: Final = "R"
HAPPY_NEW_YEAR: Final = "Saal Noo Mobarak!"

mouse_loc, nest_loc = map(int, input().strip().split())

if mouse_loc < nest_loc:
    print(f"{MOVE_RIGHT * abs(nest_loc - mouse_loc)}")
elif mouse_loc > nest_loc:
    print(f"{MOVE_LEFT * abs(nest_loc - mouse_loc)}")
else:
    print(HAPPY_NEW_YEAR)
