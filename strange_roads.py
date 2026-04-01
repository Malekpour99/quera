# https://quera.org/problemset/34084
# ----------------------------------

import heapq

Road = tuple[int, int]  # (destination_city, weight)

cities, roads = map(int, input().strip().split())
reduction_ability_cost = list(map(int, input().strip().split()))

reduction_ability_limit: int = 0
adjacent_cities: list[list[Road]] = [
    [] for _ in range(cities)
]  # index: city, value: Roads

for road in range(roads):
    start, destination_city, road_weight = map(int, input().strip().split())
    start, destination_city = start - 1, destination_city - 1  # converting to 0 indexed
    adjacent_cities[start].append((destination_city, road_weight))
    adjacent_cities[destination_city].append(
        (start, road_weight)
    )  # since roads are 2-way

    if road_weight > reduction_ability_limit:
        reduction_ability_limit = (
            road_weight + 1
        )  # add one to include the last reduction where road is removed

# Distance table: stores the minimum time to reach a city with exactly 'k' total reductions performed.
# dist[city][reductions] = min_time (Initialize with infinity)
inf = float("inf")
dist = [[inf] * reduction_ability_limit for _ in range(cities)]

# Priority Queue: (elapsed_duration, current_city, reductions_count)
pq = [(0, 0, 0)]
dist[0][0] = 0

while pq:
    elapsed_duration, current_city, reductions_count = heapq.heappop(pq)

    # If we found a shorter path to this state already, skip
    if elapsed_duration > dist[current_city][reductions_count]:
        continue

    # If we reached the destination city (n-1), this is the minimum time
    # because Dijkstra guarantees we pop states in increasing order of cost.
    if current_city == cities - 1:
        print(elapsed_duration)
        exit()

    # Transition 1: Use the ability at current city
    if reductions_count + 1 < reduction_ability_limit:
        new_cost = elapsed_duration + reduction_ability_cost[current_city]
        if new_cost < dist[current_city][reductions_count + 1]:
            dist[current_city][reductions_count + 1] = new_cost
            heapq.heappush(pq, (new_cost, current_city, reductions_count + 1))

    # Transition 2: Travel to adjacent cities
    # Edge weight becomes (weight - reductions_count). Valid only if weight > reductions_count.
    for destination_city, road_weight in adjacent_cities[current_city]:
        if road_weight > reductions_count:
            travel_time = road_weight - reductions_count
            new_cost = elapsed_duration + travel_time
            if new_cost < dist[destination_city][reductions_count]:
                dist[destination_city][reductions_count] = new_cost
                heapq.heappush(pq, (new_cost, destination_city, reductions_count))

# If queue is empty, destination can not be reached
print("-1")
