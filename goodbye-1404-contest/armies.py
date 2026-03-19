n, q = map(int, input().strip().split())

# DSU for main connectivity (Handles Types 1 and 2 unions)
# 1-based indexing, so size is n + 1
parent_main = list(range(n + 1))

# DSU for skipping processed ranges in Type 2 operations
# parent_next[i] helps find the next index that needs processing after i
# Size n + 2 to handle boundary conditions safely
parent_next = list(range(n + 2))


# Iterative find for main DSU with path compression
def find_main(i):
    root = i
    while root != parent_main[root]:
        root = parent_main[root]

    curr = i
    while curr != root:
        nxt = parent_main[curr]
        parent_main[curr] = root
        curr = nxt
    return root


# Iterative find for next DSU with path compression
def find_next(i):
    root = i
    while root != parent_next[root]:
        root = parent_next[root]

    curr = i
    while curr != root:
        nxt = parent_next[curr]
        parent_next[curr] = root
        curr = nxt
    return root


# Union for main DSU
def union_main(i, j):
    root_i = find_main(i)
    root_j = find_main(j)
    if root_i != root_j:
        parent_main[root_i] = root_j


# Union for next DSU
# Specifically links i to the representative of j to allow skipping
def union_next(i, j):
    root_i = find_next(i)
    root_j = find_next(j)
    if root_i != root_j:
        parent_next[root_i] = root_j


for _ in range(q):
    type_op, x, y = map(int, input().strip().split())

    if type_op == 1:
        union_main(x, y)
    elif type_op == 2:
        if x > y:
            x, y = y, x

        curr = find_next(x)

        while curr < y:
            union_main(curr, curr + 1)
            union_next(curr, curr + 1)
            curr = find_next(curr)
    elif type_op == 3:
        if find_main(x) == find_main(y):
            print("YES")
        else:
            print("NO")
