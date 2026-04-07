# https://quera.org/problemset/104589
# -----------------------------------

from math import sqrt

cakes_count = int(input().strip())

profit: int = 1

for i in range(2, int(sqrt(cakes_count)) + 1):
    # first divisible number of cakes which can be sold results in the highest profit
    if cakes_count % i == 0 and cakes_count // i > profit:
        profit = cakes_count // i
        break

print(profit)
