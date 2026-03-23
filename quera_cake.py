# https://quera.org/problemset/144082
# -----------------------------------

n = int(input().strip())

# Since every piece distributed is a multiple of 1/4, the total amount received by any person (3/n)
# must also be representable as a sum of these pieces. Therefore, 3/n must be a multiple of 1/4.
# so 3/n = k/4 => n = 12 / k so in order for everyone to get equal share, n must be dividable by 12.

if 12 % n == 0:
    print("YES")
else:
    print("NO")
