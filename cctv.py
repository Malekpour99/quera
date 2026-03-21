# https://quera.org/problemset/2794
# ---------------------------------

from collections import defaultdict

x_count: dict[int, int] = defaultdict(int)
y_count: dict[int, int] = defaultdict(int)

for _ in range(3):
    x, y = map(int, input().strip().split())
    x_count[x] += 1
    y_count[y] += 1

missing_x = None
missing_y = None

for x, c in x_count.items():
    if c == 1:
        missing_x = x
        break

for y, c in y_count.items():
    if c == 1:
        missing_y = y
        break

print(f"{x} {y}")
