# https://quera.org/problemset/3538
# ---------------------------------

from typing import Annotated, Literal

WeekDaysCount = Annotated[int, range(0, 8)]
WeekDay = Annotated[
    str,
    Literal["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"],
]

available_days_count: WeekDaysCount = 7
occupied_days: set[WeekDay] = set()

for _ in range(3):
    day_count = int(input().strip())
    days = list(input().strip().split())

    for day in days:
        if day not in occupied_days:
            occupied_days.add(day)
            available_days_count -= 1

print(available_days_count)
