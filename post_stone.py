# https://quera.org/problemset/3109
# ---------------------------------

power = int(input().strip())

while power % 2 == 0:
    power = power // 2

if power == 1:
    print("Yes")
else:
    print("No")
