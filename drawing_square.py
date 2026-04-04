# https://quera.org/problemset/591
# --------------------------------

n = int(input().strip())

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
