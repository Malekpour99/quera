# https://quera.org/problemset/275483
# -----------------------------------

from typing import Final

WHITE_STATUS: Final = "White"
YELLOW_STATUS: Final = "Yellow"
RED_STATUS: Final = "Red"

new_cases_per_day = int(input().strip())
hospitalizations_per_day = int(input().strip())

if new_cases_per_day <= 50 and hospitalizations_per_day <= 10:
    print(WHITE_STATUS)
elif hospitalizations_per_day > 30:
    print(RED_STATUS)
else:
    print(YELLOW_STATUS)
