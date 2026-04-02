# https://quera.org/problemset/6581
# ---------------------------------

total_travel_distance, jumps = map(int, input().strip().split())

initial_travel_distance = (total_travel_distance * 2 ** (jumps - 1)) / (2**jumps - 1)

print(f"{initial_travel_distance:.4f}")
