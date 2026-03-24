# https://quera.org/problemset/589
# --------------------------------

n = int(input().strip())

result = 1

for i in range(2, n + 1):
    result *= i

print(result)
