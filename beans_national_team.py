# https://quera.org/problemset/10163
# ----------------------------------

(
    one_customer_cost,
    two_customer_cost,
    three_customer_cost,
) = map(int, input().strip().split())

time_intervals: list[tuple[int, int]] = []

for _ in range(3):
    enter_time, exit_time = map(int, input().strip().split())
    time_intervals.append((enter_time, exit_time))

total_cost = 0

# each minute from 1 to 100 (based on constraints)
for t in range(1, 101):
    count = 0
    for start, end in time_intervals:
        if start <= t < end:
            count += 1

    if count == 1:
        total_cost += 1 * one_customer_cost
    elif count == 2:
        total_cost += 2 * two_customer_cost
    elif count == 3:
        total_cost += 3 * three_customer_cost

print(total_cost)
