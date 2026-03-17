# https://quera.org/problemset/170171
# -----------------------------------

plans = int(input().strip())
votes = list(map(int, input().strip().split()))

min_agents = 0
max_agents = 100
max_citizens = 0

for vote in votes:
    max_agents = vote if vote < max_agents else max_agents
    # to maximize citizens, we are considering them as disjoint as possible (each person votes "NO" only once!)
    max_citizens += 100 - vote

min_agents = max(min_agents, 100 - max_citizens)

print(f"{min_agents} {max_agents}")
