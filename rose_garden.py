# https://quera.org/problemset/66867
# ----------------------------------

from typing import Final

WHITE_FLOWER: Final = "W"
BLACK_FLOWER: Final = "B"

BAD_STATUS: Final = "B"
GOOD_STATUS: Final = "F"

flowers, months = map(int, input().strip().split())

flower_blossom_count: list[int] = [0] * flowers

for _ in range(months):
    flowers_status = input().strip()

    for i, status in enumerate(flowers_status):
        if status == WHITE_FLOWER:
            flower_blossom_count[i] += 1

final_flower_status: str = ""

for blossom_count in flower_blossom_count:
    if blossom_count % 2 == 0:
        final_flower_status += BAD_STATUS
    else:
        final_flower_status += GOOD_STATUS

print(final_flower_status)
