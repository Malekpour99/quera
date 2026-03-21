# https://quera.org/problemset/6375
# ---------------------------------

containers = list(map(int, input().strip().split()))

split_count = 0
avg_water = sum(containers) / len(containers)

for container in containers:
    if container != avg_water:
        split_count += 1

print(max(0, split_count - 1))
