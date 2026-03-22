# https://quera.org/problemset/10232
# ----------------------------------

traffic_lights_count, total_distance = map(int, input().strip().split())

traffic_lights: dict[int, tuple[int, int]] = (
    {}
)  # Hint: distance: (red_light_duration, green_light_duration)

for _ in range(traffic_lights_count):
    tl_distance, red_duration, green_duration = map(int, input().strip().split())
    traffic_lights[tl_distance] = (red_duration, green_duration)

traveled_distance: int = 0  # Km
elapsed_time: int = 0  # minute

for distance, durations in traffic_lights.items():
    passed_distance = distance - traveled_distance
    traveled_distance += passed_distance
    elapsed_time += passed_distance  # each Km = 1 Minute

    light_current_time = elapsed_time % sum(durations)
    if light_current_time < durations[0]:  # durations[0] is red-light duration
        elapsed_time += durations[0] - light_current_time

if traveled_distance < total_distance:
    remaining_distance = total_distance - traveled_distance
    elapsed_time += remaining_distance

print(elapsed_time)
