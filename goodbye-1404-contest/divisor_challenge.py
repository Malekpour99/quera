a, b = map(int, input().strip().split())

MOD = 10**9 + 7
limit = b

# Smallest Prime Factor (SPF) for every number up to b
# spf[i] will store a prime factor of i
spf = list(range(limit + 1))

for i in range(2, int(limit**0.5) + 1):
    if spf[i] == i:
        start = i * i
        if start <= limit:
            count = (limit - start) // i + 1
            spf[start : limit + 1 : i] = [i] * count

prime_counts = [0] * (limit + 1)

for num in range(a + 1, b + 1):
    while num > 1:
        p = spf[num]
        prime_counts[p] += 1
        num //= p

ans = 1
for count in prime_counts:
    if count > 0:
        ans = (ans * (count + 1)) % MOD

print(ans)
