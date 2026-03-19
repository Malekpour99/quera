from collections import defaultdict, deque

n, m = map(int, input().strip().split())

required = set()
for _ in range(m):
    a, b = map(int, input().strip().split())
    required.add((a, b))

nodes_in_requirements = set()
for a, b in required:
    nodes_in_requirements.add(a)
    nodes_in_requirements.add(b)

graph = defaultdict(set)
for a, b in required:
    graph[a].add(b)


index_counter = [0]
stack = []
low_links = {}
index = {}
on_stack = {}
sccs = []  # Strongly Connected Components (SCCs)


def strong_connect(v):
    index[v] = index_counter[0]
    low_links[v] = index_counter[0]
    index_counter[0] += 1
    stack.append(v)
    on_stack[v] = True

    for w in graph[v]:
        if w not in index:
            strong_connect(w)
            low_links[v] = min(low_links[v], low_links[w])
        elif on_stack.get(w, False):
            low_links[v] = min(low_links[v], index[w])

    if low_links[v] == index[v]:
        scc = []
        while True:
            w = stack.pop()
            on_stack[w] = False
            scc.append(w)
            if w == v:
                break
        sccs.append(scc)


for v in nodes_in_requirements:
    if v not in index:
        strong_connect(v)

# Map each node to its SCC id
node_to_scc = {}
for scc_id, scc in enumerate(sccs):
    for node in scc:
        node_to_scc[node] = scc_id

# Count edges needed:
# 1. Within each SCC of size k, we need k edges (to make it strongly connected in a cycle)
# 2. Between SCCs, we need to preserve reachability in the DAG

edges_count = 0

# Edges within SCCs
for scc in sccs:
    if len(scc) > 1:
        edges_count += len(scc)
    elif len(scc) == 1:
        pass

# Build condensation graph (DAG between SCCs)
scc_graph = defaultdict(set)
for a, b in required:
    scc_a = node_to_scc[a]
    scc_b = node_to_scc[b]
    if scc_a != scc_b:
        scc_graph[scc_a].add(scc_b)


num_sccs = len(sccs)

in_degree = [0] * num_sccs
for u in scc_graph:
    for v in scc_graph[u]:
        in_degree[v] += 1

# Topological sort
queue = deque()
for i in range(num_sccs):
    if in_degree[i] == 0:
        queue.append(i)

topo_order = []
while queue:
    u = queue.popleft()
    topo_order.append(u)
    for v in scc_graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

# Build reachability for each node in topological order
reachable: list[set] = [set() for _ in range(num_sccs)]

for u in reversed(topo_order):
    for v in scc_graph[u]:
        reachable[u].add(v)
        reachable[u].update(reachable[v])

# Count necessary edges in condensation graph
for u in range(num_sccs):
    for v in scc_graph[u]:
        necessary = True
        for w in scc_graph[u]:
            if w != v and v in reachable[w]:
                necessary = False
                break
        if necessary:
            edges_count += 1

print(edges_count)
