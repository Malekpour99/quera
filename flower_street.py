# https://quera.org/problemset/275495
# -----------------------------------

cars, street_length = map(int, input().strip().split())

# (car index, duration to reach square)
first_arriving_car: tuple[int, float] = (0, float("inf"))

for i in range(1, cars + 1):  # 1-indexed
    location_from_start, speed = map(int, input().strip().split())
    remaining_duration = (street_length - location_from_start) / speed
    if remaining_duration < first_arriving_car[1]:
        first_arriving_car = (i, remaining_duration)

print(first_arriving_car[0])
