# https://quera.org/problemset/255960
# -----------------------------------

from typing import Final

CLOSED_PATH_SIGN: Final = "X"

n = int(input().strip())
first_row = input().strip()
second_row = input().strip()

can_win: bool = True

for i in range(n - 1):
    if (
        first_row[i + 1] == CLOSED_PATH_SIGN
        and (second_row[i] == CLOSED_PATH_SIGN or second_row[i + 1] == CLOSED_PATH_SIGN)
        or second_row[i + 1] == CLOSED_PATH_SIGN
        and (first_row[i] == CLOSED_PATH_SIGN or first_row[i + 1] == CLOSED_PATH_SIGN)
    ):
        can_win = False
        break

if can_win:
    print("Hooraaay!:))")
else:
    print("Awww:((")
