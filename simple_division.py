# https://quera.org/problemset/31025
# ----------------------------------

n, k = map(int, input().strip().split())

for _ in range(k):
    n = n // 2

print(n)
