# https://quera.org/problemset/188852
# -----------------------------------

from typing import Annotated, Final, Literal

# Actions
BUY_GIFT: Final = "buy_one"
DOUBLE_GIFT: Final = "copy_paste"

Action = Annotated[str, Literal[BUY_GIFT, DOUBLE_GIFT]]

trips = int(input().strip())

for _ in range(trips):
    trip_gifts: int = 0
    options_count = int(input().strip())
    for _ in range(options_count):
        available_actions: set[Action] = set(input().strip().split())
        if DOUBLE_GIFT not in available_actions:
            trip_gifts += 1
        else:
            if trip_gifts == 0 and BUY_GIFT in available_actions:
                trip_gifts += 1
            else:
                trip_gifts *= 2

    print(trip_gifts)
