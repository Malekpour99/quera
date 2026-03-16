# https://quera.org/problemset/61038
# ----------------------------------

from math import lcm

n = int(input().strip())

periods: list[int] = []
for _ in range(n):
    periods.append(int(input().strip()))

collision_day = lcm(*periods) % 30 + 1

print(collision_day)
