# https://quera.org/problemset/132247
# -----------------------------------

from collections import defaultdict

n = int(input().strip())

names_count: dict[str, int] = defaultdict(int)

for _ in range(n + n - 1):
    name = input().strip()
    names_count[name] += 1

for name, count_ in names_count.items():
    if count_ % 2 != 0:
        print(name)
        break
