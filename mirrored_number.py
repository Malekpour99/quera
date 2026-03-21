# https://quera.org/problemset/617
# --------------------------------

num = input().strip()

# you can loop over number and compare corresponding index from end to solve this in log(n)!
if num == num[::-1]:
    print("YES")
else:
    print("NO")
