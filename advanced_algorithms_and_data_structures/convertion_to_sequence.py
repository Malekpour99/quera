n, k = map(int, input().split())
seq = list(map(int, input().split()))

ans = float("inf")
base_line = (n - 1) * k
for num in range(min(seq) - base_line, max(seq) + 1):
    cost = 0
    for i in range(n):
        cost += abs(num + i * k - seq[i])

    if cost < ans:
        ans = cost

print(ans)
