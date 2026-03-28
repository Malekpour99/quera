# https://quera.org/problemset/147191
# -----------------------------------

import math

a = int(input().strip())

# Area = a² × (1 + π/3 - √3)
area = (a**2) * (1 + math.pi / 3 - math.sqrt(3))

print(area)
