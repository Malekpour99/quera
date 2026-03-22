# https://quera.org/problemset/282
# --------------------------------

n = int(input().strip())

aggregate = 1
for i in range(2, n // 2 + 1):
    if n % i == 0:
        aggregate += i

if aggregate == n:
    print("YES")
else:
    print("NO")
