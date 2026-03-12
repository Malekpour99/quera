# https://quera.org/problemset/616
# --------------------------------

num = int(input().strip())

i = 0
ans = 2**i
while ans <= num:
    i += 1
    ans = 2**i

print(ans)
