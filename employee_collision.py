# https://quera.org/problemset/10636
# ----------------------------------

from collections import defaultdict

employees = int(input().strip())

employee_count: dict[str, int] = defaultdict(int)

for _ in range(employees):
    name, __ = input().strip().split()
    employee_count[name] += 1

print(max(employee_count.values()))
