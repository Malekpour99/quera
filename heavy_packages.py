# https://quera.org/problemset/3558
# ---------------------------------

# representing month days (0 indexed)
month_days: list[int] = [0 for _ in range(30)]

worker_one_ranges, worker_two_ranges = map(int, input().strip().split())

heavy_package_days_count: int = 0

for _ in range(worker_one_ranges):
    start, end = map(int, input().strip().split())
    for i in range(start - 1, end):
        month_days[i] = 1

for _ in range(worker_two_ranges):
    start, end = map(int, input().strip().split())
    heavy_package_days_count += sum(month_days[start - 1 : end])

print(heavy_package_days_count)
