# https://quera.org/problemset/4065
# ---------------------------------

wait_duration_1, wait_duration_2, total_count = map(int, input().strip().split())

elapsed_duration: int = 0

for i in range(total_count):
    if i % 2 == 0:
        elapsed_duration += wait_duration_1
    else:
        elapsed_duration += wait_duration_2

print(elapsed_duration)
