# https://quera.org/problemset/2705
# ---------------------------------

p, d = map(int, input().strip().split())

while d % p > p // 2:
    d += d

print(d)
