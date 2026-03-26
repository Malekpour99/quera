# https://quera.org/problemset/2887
# ---------------------------------

from math import gcd

n = int(input().strip())
counted_objects = list(map(int, input().strip().split()))

count_gcd = gcd(*counted_objects)

objects: int = 0
for count_ in counted_objects:
    objects += count_ // count_gcd

print(objects)
