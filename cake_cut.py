# https://quera.org/problemset/2757
# ---------------------------------

k = int(input().strip())

# We need to find the product of distinct prime factors of k.
# This is the smallest d such that k divides d^m for some m.

ans = 1
i = 2
temp = k

# Iterate from 2 up to sqrt(temp)
while i * i <= temp:
    if temp % i == 0:
        # i is a prime factor
        ans *= i
        # Remove all occurrences of this prime factor from temp
        while temp % i == 0:
            temp //= i
    i += 1

# If temp > 1, then the remaining temp is a prime factor
if temp > 1:
    ans *= temp

print(ans)
