# https://quera.org/problemset/187845
# -----------------------------------

pigeons, nests = map(int, input().strip().split())

if pigeons > nests:
    print("Yes")
else:
    print("No")
