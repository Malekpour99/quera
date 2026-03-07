# https://quera.org/problemset/275459
# -----------------------------------

CAN_WIN = "Yes"
CAN_NOT_WIN = "No"
number_of_coins = int(input().strip())

if number_of_coins % (1 + 4) in {0, 2}:
    win = True
else:
    win = False

if win:
    print(CAN_WIN)
else:
    print(CAN_NOT_WIN)
