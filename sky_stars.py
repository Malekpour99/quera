# https://quera.org/problemset/6082
# ---------------------------------

from typing import Final

STAR_SIGN: Final = "*"

rows, columns = map(int, input().strip().split())

stars_count: int = 0

for _ in range(rows):
    sky_row = input().strip()
    for sign in sky_row:
        if sign == STAR_SIGN:
            stars_count += 1

print(stars_count)
